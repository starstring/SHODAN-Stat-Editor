-- local overlay: two pages of its own on the Armors tab — "Every armor" and "Armor settings".
--
-- * **Every armor**: a passive page whose stack is applied to *every* armor passive at install time,
--   so adding a passive here adds it to whatever armor you wear. It uses the panel's own stack UI
--   (its `+ Add passive` and the list under the rows), which needs the page to look like a passive
--   page: a passive table key whose `index.id` is a sentinel (`settings.stacks[sentinel]` holds the
--   list, and the panel's dialog offers the real passives as usual).
-- * **Armor settings**: where the stacking behaviour is configured (currently: what a modifier both
--   passives have does — keep the first, or let the stronger value win).
--
-- A page only appears in the list when it has at least one row (`weapons_in` skips empty pages), so
-- "Every armor" carries a row that shows how many passives it holds, and "Armor settings" carries
-- the setting itself as a row. Both rows are driven by this overlay: `row_value` shows their value,
-- `change` handles the clicks, and no memory is written for them.
--
-- No `local` at this level (upstream's chunk sits at LuaJIT's 200-local limit).
state.sse_own_off = settings.own_off          -- (the panel's own switch, for the preview)
state.sse_every_id = 0x7E000001                  -- a sentinel: real passive ids are 1..42
state.sse_every_key = 'armor passive every'

;(function()
    local EVERY = state.sse_every_id
    -- the passive table the "Every armor" page points at: empty, so it adds no rows of its own
    tables[state.sse_every_key] = { index = { id = EVERY, mods = {}, stats = {}, name = 0, type = 0, pieces = {} },
                                    entries = 0, copies = {} }
    state.sse_pages = {
        { name = 'Every armor', hash = 'FFFFFFFD00000001', sse_page = 'every',
          passive = state.sse_every_key,
          note = 'Passives added below apply to every armor, whatever you wear.' },
        { name = 'Armor settings', hash = 'FFFFFFFD00000002', sse_page = 'settings',
          note = 'How the armor passives are applied.' },
    }
    for _, page in ipairs(state.sse_pages) do
        page.slot, page.rows, page.by_id = 'Armors', {}, {}
        page.key = hash_key(page.hash)
    end
end)()

-- (re)list them: the passive build drops every page that has `.passive`, and only then are the
-- passive pages themselves added, so this runs at load and again after each build
state.sse_list_pages = function()
    for k = #state.sse_pages, 1, -1 do
        local page = state.sse_pages[k]
        if not by_hash[page.hash] then
            page.rows, page.by_id = {}, {}            -- resolved again: rows are rebuilt
            by_hash[page.hash] = page
            table.insert(weapons, 1, page)             -- first in the Armors tab
        end
    end
end
state.sse_list_pages()
state.sse_passive_build = KINDS[TYPES.passive].build
KINDS[TYPES.passive].build = function()
    state.sse_passive_build()
    state.sse_list_pages()
end

-- their rows
-- the rows below are not backed by memory, but a row needs a field: a real passive table's first
-- word (its id) is read harmlessly and never written (row_value and change handle these rows)
state.sse_handle = function()
    return (KINDS[TYPES.passive].list or {})[1] or state.sse_every_key
end

state.sse_resolve3 = resolve
resolve = function(weapon)
    if weapon and weapon.sse_page == 'every' then
        state.sse_resolve3(weapon)                    -- (a passive page: adds nothing by itself)
        if not weapon.by_id['every_count'] then
            local row = add_row(weapon, 'Every armor', 'every_count', 'Passives applied', 'u32',
                                { part('every_count', state.sse_handle(), 0, 'u32', 4294967295) }, 0, 999, 1, 5)
            row.sse_setting = 'count'
            row.note = 'Added with "+ Add passive" below; every armor gets them at install.'
        end
        return
    elseif weapon and weapon.sse_page == 'settings' then
        if not weapon.by_id['stack_conflicts'] then
            local row = add_row(weapon, 'Stacks', 'stack_conflicts', 'A modifier both passives have', 'u32',
                                { part('stack_conflicts', state.sse_handle(), 0, 'u32', 4294967295) }, 0, 1, 1, 1)
            row.sse_setting = 'conflicts'
            row.sse_options = { { 'stack', 'Stack all' }, { 'strongest', 'Strongest only' } }
            row.sse_current = function() return state.sse_cfg.conflicts end
            row.note = 'When both passives have the same modifier' 
        end
        return
    end
    return state.sse_resolve3(weapon)
end

-- what those rows show (they are not backed by game memory)
state.sse_row_value_armor = row_value
row_value = function(row, default)
    if row and row.sse_setting == 'conflicts' then
        return state.sse_cfg.conflicts == 'strongest' and 1 or 0
    elseif row and row.sse_setting == 'count' then
        local list = settings.stacks[state.sse_every_id]
        return list and #list or 0
    end
    return state.sse_row_value_armor(row, default)
end

-- and what clicking them does
state.sse_change = change
change = function(row, delta_sign, big, exact)
    if row and row.sse_setting == 'conflicts' then
        local target = exact and math.floor(exact + 0.5) or ((state.sse_cfg.conflicts == 'strongest') and 0 or 1)
        state.sse_cfg.conflicts = target >= 1 and 'strongest' or 'stack'
        mark_config_dirty()
        ui.message = { text = 'A modifier both passives have: ' .. state.sse_cfg.conflicts ..
                             (state.sse_cfg.conflicts == 'strongest' and ' (the stronger value wins)' or
                              ' (the passive you add it to keeps its own)'), till = api.now() + 5 }
        return
    elseif row and row.sse_setting == 'count' then
        ui.message = { text = 'Add passives with "+ Add passive" below: every armor gets them at install.',
                       till = api.now() + 5 }
        return
    end
    return state.sse_change(row, delta_sign, big, exact)
end

-- The final effects of a passive's stack: its own rows plus every stacked passive's, merged the way
-- the install merges them ('keep' = all of them, 'strongest' = one per modifier id, the strongest by
-- the Armory Forge rule: |log v| for a multiply, |v| otherwise).
state.sse_merge = function(target)
    local t = tables[target.passive]
    if not t then return {} end
    local policy = state.sse_cfg.conflicts
    local function strength(typ, v)
        if typ == 2 then return (v <= 0) and math.huge or math.abs(math.log(v)) end
        return math.abs(v)
    end
    -- one passive's modifier rows (16 B: id, type, value) or weapon-stat rows (12 B: stat, a, b)
    local function read_list(table_key, field)
        local entry = table_key and tables[table_key]
        local out = {}
        if not entry then return out end
        for _, m in ipairs(entry.index[field] or {}) do
            local v = read_field(field_at(table_key, m.offset, 'f32', 100000))
            if v then out[#out + 1] = { id = m.id or m.stat, type = m.type or 0, value = v } end
        end
        return out
    end
    local rows, order, by_id = {}, {}, {}
    local function add(list, from, is_stat)
        for _, m in ipairs(list) do
            local key = (is_stat and 'stat ' or 'mod ') .. tostring(m.id)
            if not by_id[key] then
                by_id[key] = #rows + 1
                order[#order + 1] = key
                rows[#rows + 1] = { id = m.id, type = m.type, value = m.value, from = from, stat = is_stat }
            elseif policy == 'strongest' then
                local at = by_id[key]
                if strength(m.type, m.value) > strength(rows[at].type, rows[at].value) then
                    rows[at] = { id = m.id, type = m.type, value = m.value, from = from, stat = is_stat }
                end
            end
        end
    end
    -- the passive's own effects first, then what is stacked on it (and, for "Every armor", those too)
    local sources = {}
    local function push(id)
        for _, other in ipairs(settings.stacks[id] or {}) do
            if other ~= id then sources[#sources + 1] = other end
        end
    end
    push(t.index.id)
    local every = settings.stacks[state.sse_every_id]
    if every and t.index.id ~= state.sse_every_id then
        for _, other in ipairs(every) do sources[#sources + 1] = other end
    end
    -- "Own effects: Off" leaves the passive's own rows out of the install, so they are left out here too
    if not settings.own_off[t.index.id] then
        add(read_list(target.passive, 'mods'), t.index.id, false)
        add(read_list(target.passive, 'stats'), t.index.id, true)
    end
    for _, id in ipairs(sources) do
        local other = by_hash[string.format('FFFFFFFE%08X', id)]
        local table_key = other and other.passive
        if table_key and tables[table_key] then
            add(read_list(table_key, 'mods'), id, false)
            add(read_list(table_key, 'stats'), id, true)
        end
    end
    return rows, order, by_id
end

state.sse_preview_of = function(target)
    local rows = state.sse_merge(target)
    local spec = KINDS[TYPES.passive]
    local lines = {}
    for _, m in ipairs(rows) do
        local name = (m.stat and spec.STATS[m.id]) or spec.MODS[m.id] or
                     (m.stat and ('Stat ' .. tostring(m.id)) or string.format('Modifier %08X', m.id))
        local sign = ({ [0] = '=', [1] = '+', [2] = '×', [3] = 's ' })[m.type] or '?'
        local from = by_hash[string.format('FFFFFFFE%08X', m.from)]
        lines[#lines + 1] = string.format('%s  %s%s  — %s', name, sign, number_text(m.value),
                                          from and from.name or ('Passive ' .. tostring(m.from)))
    end
    if #lines == 0 then lines[1] = 'Nothing yet: add a passive below.' end
    return { title = settings.tr('Final effects') .. ': ' .. #lines, lines = lines }
end

-- clicks on an option row (drawn by the generated panel: local/patch_panel_ui.py)
state.sse_click2 = click
click = function(key)
    -- (not `key and key:match(...)`: `and` keeps only the first result)
    local row_at, value
    if key then row_at, value = key:match('^sse_opt:(%d+):(.+)$') end
    if key == 'sse_add_all' then
        -- this page's passive, added to the "Every armor" list (the same thing "+ Add passive" does there)
        local target = ui.weapon
        local index = target and target.passive and tables[target.passive] and tables[target.passive].index
        local id = index and index.id
        if not id or id == state.sse_every_id then return end
        local list = settings.stacks[state.sse_every_id] or {}
        for _, other in ipairs(list) do
            if other == id then
                ui.message = { text = 'Already in Every armor: ' .. tostring(target.name), till = api.now() + 4 }
                return
            end
        end
        list[#list + 1] = id
        settings.stacks[state.sse_every_id] = list
        mark_config_dirty()
        ui.message = { text = target.name .. ' is now added to every armor (' .. #list .. ' passive(s)).',
                       till = api.now() + 5 }
        return
    end
    if key and key:match('^sse_preview') then
        local target = ui.weapon
        if target and target.passive and state.sse_preview then
            state.sse_preview = nil
        elseif target and target.passive then
            state.sse_preview = state.sse_preview_of(target)
        end
        return
    end
    if state.sse_preview and key ~= 'sse_preview' then state.sse_preview = nil end
    if row_at then
        local row = ui.weapon and ui.weapon.rows and ui.weapon.rows[tonumber(row_at)]
        if row then
            if row.sse_setting == 'conflicts' then
                state.sse_cfg.conflicts = (value == 'strongest') and 'strongest' or 'stack'
                mark_config_dirty()
                ui.message = { text = 'A modifier both passives have: ' .. state.sse_cfg.conflicts ..
                                     (state.sse_cfg.conflicts == 'strongest' and ' (the stronger value wins)' or
                                      ' (the passive you add it to keeps its own)'), till = api.now() + 5 }
                return
            elseif row.sse_effect_type then
                change(row, 0, false, tonumber(value))   -- (0: the value is exact, no stepping)
                return
            end
        end
        return
    end
    return state.sse_click2(key)
end

-- the install side: the "Every armor" list is added to every passive's stack
state.sse_stacks2 = state.stacks
state.stacks = function()
    local base = state.sse_stacks2()
    local every = settings.stacks[state.sse_every_id]
    if not every or #every == 0 then return base end
    local out = {}
    for target, list in pairs(base) do out[target] = list end
    for _, entry in ipairs(weapons) do
        local index = entry.passive and tables[entry.passive] and tables[entry.passive].index
        local id = index and index.id
        if id and id ~= state.sse_every_id then
            local list, seen = {}, { [id] = true }
            for _, other in ipairs(base[id] or {}) do
                if not seen[other] then seen[other], list[#list + 1] = true, other end
            end
            for _, other in ipairs(every) do
                if not seen[other] then seen[other], list[#list + 1] = true, other end
            end
            if #list > 0 then out[id] = list end
        end
    end
    return out
end

;(function()
    for _, lang in ipairs(MOD.langs or {}) do
        local words = ({ ['zh-Hans'] = { '所有护甲', '护甲设置', '已应用的被动', '两个被动都有的修正',
                                        '安装时作用到每一件护甲', '0 保留原值，1 最强值胜出' },
                         ['zh-Hant'] = { '所有護甲', '護甲設定', '已套用的被動', '兩個被動都有的修正',
                                        '安裝時作用到每一件護甲', '0 保留原值，1 最強值勝出' },
                         ['ru'] = { 'Вся броня', 'Настройки брони', 'Пассивов применено',
                                    'Модификатор у обоих пассивов', 'при установке для всей брони',
                                    '0 как есть, 1 сильнейшее значение' } })[lang.id]
        if words then
            lang.exact['Every armor'] = words[1]
            lang.exact['Armor settings'] = words[2]
            lang.exact['Passives applied'] = words[3]
            lang.exact['A modifier both passives have'] = words[4]
            lang.exact['Passives added below apply to every armor, whatever you wear.'] = words[5]
            lang.exact['Added with "+ Add passive" below; every armor gets them at install.'] = words[5]
            lang.exact['How the armor passives are applied.'] = words[4]
            lang.exact['Preview the result'] = ({ ['zh-Hans'] = '预览最终效果', ['zh-Hant'] = '預覽最終效果',
                                                  ['ru'] = 'Предпросмотр итога' })[lang.id]
            lang.exact['Final effects'] = ({ ['zh-Hans'] = '最终效果', ['zh-Hant'] = '最終效果',
                                             ['ru'] = 'Итоговые эффекты' })[lang.id]
            lang.exact['Add to every armor'] = ({ ['zh-Hans'] = '添加到所有护甲', ['zh-Hant'] = '新增到所有護甲',
                                                  ['ru'] = 'Добавить всей броне' })[lang.id]
            if lang.lower then lang.lower['add to every armor'] = lang.exact['Add to every armor'] end
            if lang.upper then lang.upper['ADD TO EVERY ARMOR'] = lang.exact['Add to every armor'] end
            if lang.lower then lang.lower['preview the result'] = lang.exact['Preview the result'] end
            if lang.upper then lang.upper['PREVIEW THE RESULT'] = lang.exact['Preview the result'] end
            local opts = ({ ['zh-Hans'] = { '全部堆叠', '只取最强' }, ['zh-Hant'] = { '全部堆疊', '只取最強' },
                            ['ru'] = { 'все подряд', 'только сильнейшее' } })[lang.id]
            if opts then
                lang.exact['Stack all'], lang.exact['Strongest only'] = opts[1], opts[2]
                lang.exact['When both passives have the same modifier'] = words[4]
                if lang.lower then
                    lang.lower['stack all'], lang.lower['strongest only'] = opts[1], opts[2]
                end
                if lang.upper then
                    lang.upper['STACK ALL'], lang.upper['STRONGEST ONLY'] = opts[1], opts[2]
                end
            end
            if lang.lower then
                lang.lower['passives applied'] = words[3]
                lang.lower['a modifier both passives have'] = words[4]
            end
            if lang.upper then
                lang.upper['PASSIVES APPLIED'] = words[3]
                lang.upper['A MODIFIER BOTH PASSIVES HAVE'] = words[4]
            end
        end
    end
end)()
