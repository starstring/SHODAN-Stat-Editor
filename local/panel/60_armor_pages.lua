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
            row.note = function()
                return state.sse_cfg.conflicts == 'strongest' and
                    '1 strongest: the value further from "no effect" wins' or
                    '0 stack: the passive you add it to keeps its own value'
            end
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
