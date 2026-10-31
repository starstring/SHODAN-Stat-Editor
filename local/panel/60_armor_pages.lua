-- local overlay: two pages of its own on the Armors tab — "Every armor" and "Armor settings".
--
-- Upstream now gives each armor its own page with its own passive list (settings.armor_passives,
-- an armor id -> { passive ids }), which is the model this overlay uses:
--
-- * **Every armor**: a page like an armor's, whose list is added to *every* armor at install, so the
--   passives put here apply to whatever armor you wear. It gets the panel's own passive UI (the
--   PASSIVES section with + Add passive / Remove) because it is an armor page with a sentinel id.
-- * **Armor settings**: where the stacking behaviour is configured (what a modifier both passives
--   have does — see 55_passive_stack_extras.lua for the policy itself).
--
-- Plus, on every armor page, an "Add to every armor" button (its list is copied into every armor's)
-- and "Preview the result" (the final effects of that armor's list, merged and added up).
--
-- No `local` at this level (upstream's chunk sits at LuaJIT's 200-local limit).
state.sse_every_armor = 0x7E000001
-- a custom passive: a bundle of passives that an armor can carry as one entry. The install merges an
-- armor's whole list into one record anyway (upstream does that), so this is the way past the 14-entry
-- UI cap: any number of passives here, added to an armor as a single choice.
state.sse_custom_id = 999
state.sse_custom_key = 'sse custom passive'
MOD.kits.MAX_PASSIVES = 64                  -- a sentinel: real armor ids are elsewhere
state.sse_page_armor = 'FFFFFFF8%08X'               -- the panel's own armor page hash pattern

-- the two pages, (re)listed after the panel builds the armor pages (its build drops pages with .kits)
state.sse_list_pages = function()
    -- a complete shape: the panel walks a passive's `lines` (its description text ids) whenever it
    -- builds the rename boxes, so an index without them breaks drawing the page
    tables[state.sse_custom_key] = { index = { id = state.sse_custom_id, mods = {}, stats = {}, lines = {},
                                              pieces = {}, name = 0, type = 0, text = nil },
                                     entries = 0, copies = {} }
    for _, spec in ipairs({ { id = state.sse_custom_id, name = 'Custom passive', passive = state.sse_custom_key,
                              note = 'A bundle: the passives here reach an armor as one entry. Add it to an armor below.' },
                            { id = state.sse_every_armor, name = 'Every armor',
                              note = 'The passives here are added to every armor, whatever you wear.' },
                            { id = 0x7E000002, name = 'Armor settings',
                              note = 'How the armor passives are applied.' } }) do
        local hash = string.format(state.sse_page_armor, spec.id)
        local page = by_hash[hash]
        if not page then
            page = { name = spec.name, slot = 'Armors', hash = hash, key = hash_key(hash), rows = {}, by_id = {},
                     kits = 'passive', armor = spec.id, default = {}, note = spec.note, sse_page = true,
                     passive = spec.passive }
            by_hash[hash] = page
        end
        page.rows, page.by_id = {}, {}              -- (a rebuild: its rows are made again)
        by_hash[string.format('FFFFFFFE%08X', spec.id)] = page   -- (as a passive an armor's list names)
        local here = false
        for _, other in ipairs(weapons) do if other == page then here = true end end
        if not here then
            local at = 1                            -- first in the Armors tab
            for k, w in ipairs(weapons) do if w.slot == 'Armors' then at = k break end end
            table.insert(weapons, at, page)
        end
    end
end

state.sse_kits_build = MOD.kits.build
MOD.kits.build = function()
    state.sse_kits_build()
    state.sse_list_pages()
end
state.sse_list_pages()

-- at install: the Every armor list joins every armor's own
state.sse_armor_passives = state.armor_passives
state.armor_passives = function()
    local base = state.sse_armor_passives() or {}
    local every = base[state.sse_every_armor]
    local out = {}
    for armor, list in pairs(base) do
        if armor ~= state.sse_every_armor and armor ~= 0x7E000002 then out[armor] = list end
    end
    local custom = base[state.sse_custom_id] or {}
    for _, page in ipairs(weapons) do
        local armor = page.armor
        if armor and armor ~= state.sse_every_armor and armor ~= state.sse_custom_id and armor ~= 0x7E000002 then
            local list, seen = {}, {}
            local function add(one)
                if one == state.sse_custom_id then
                    -- the bundle, spread out (once: a bundle inside a bundle would loop)
                    if not seen[state.sse_custom_id] then
                        seen[state.sse_custom_id] = true
                        for _, pid in ipairs(custom) do add(pid) end
                    end
                elseif one and not seen[one] then
                    seen[one] = true
                    list[#list + 1] = one
                end
            end
            for _, pid in ipairs(out[armor] or page.default or {}) do add(pid) end
            if every then for _, pid in ipairs(every) do add(pid) end end
            out[armor] = list
        end
    end
    return out
end

-- the Armor settings page's one row: which value wins when both passives have the same modifier
-- A page that throws while resolving used to stall the panel at "resolving weapons" for ever (the
-- loop retries the same page). Log which one and skip it, so the editor still starts.
state.sse_resolve_some = resolve_some
resolve_some = function(progress, deadline)
    local ok, res = pcall(state.sse_resolve_some, progress, deadline)
    if ok then return res end
    local page = weapons[progress.next]
    log('local: resolving ' .. tostring(page and page.name) .. ' failed: ' .. tostring(res))
    progress.next = progress.next + 1
    return false
end

-- a page with no rows at all cannot be drawn (the row list's scroll bar reads rows[#rows]): every one of
-- our pages keeps a count row, which also tells the user how much it holds
state.sse_count_row = function(weapon)
    if not weapon or not weapon.armor or weapon.by_id['sse_count'] then return end
    local row = add_row(weapon, 'Stacks', 'sse_count', 'Passives here', 'u32',
                        { part('sse_count', KINDS[TYPES.passive].list[1], 0, 'u32', 4294967295) }, 0, 999, 1, 5)
    row.sse_setting = 'count'
    row.sse_page = weapon                      -- (row_value needs to know whose count it shows)
    row.note = 'Add passives with "+ Add passive" below.'
end

state.sse_resolve_armor = resolve
resolve = function(weapon)
    -- upstream builds a page's rows here (and starts from an empty list), so our rows go in *after* it
    local built = state.sse_resolve_armor(weapon)
    if weapon and (weapon.armor == state.sse_every_armor or weapon.armor == state.sse_custom_id) then
        state.sse_count_row(weapon)
    end
    -- an armor's page says how many passives it gets from Every armor (they are not listed there)
    if weapon and weapon.armor and weapon.armor ~= state.sse_every_armor and weapon.armor ~= state.sse_custom_id
            and weapon.armor ~= 0x7E000002 then
        weapon.sse_base_note = weapon.sse_base_note or weapon.note
        local extra = #(settings.armor_passives[state.sse_every_armor] or {})
        -- (not settings.tr: it translates 'armor' inside the sentence on its own)
        local hint = ({ en = 'Plus %d from Every armor', ['zh-Hans'] = '另有 %d 个来自所有护甲',
                        ['zh-Hant'] = '另有 %d 個來自所有護甲', ru = 'Ещё %d из «всей брони»' })[settings.lang] or
                     'Plus %d from Every armor'
        weapon.note = weapon.sse_base_note .. (extra > 0 and ('  ·  ' .. hint:format(extra)) or '')
    end
    -- the Every armor page says when an armor would go past the game's 14, because then Install stops
    if weapon and weapon.armor == state.sse_every_armor then
        weapon.sse_base_note = weapon.sse_base_note or weapon.note
        local over, first = 0, nil
        for _, other in ipairs(weapons) do
            local armor = other.armor
            if armor and armor ~= state.sse_every_armor and armor ~= 0x7E000002 then
                local seen, count = {}, 0
                for _, id in ipairs(MOD.kits.list_of(other) or {}) do seen[id] = true; count = count + 1 end
                for _, id in ipairs(settings.armor_passives[state.sse_every_armor] or {}) do
                    if not seen[id] then seen[id] = true; count = count + 1 end
                end
                if count > MOD.kits.MAX_PASSIVES then
                    over = over + 1
                    first = first or other.name
                end
            end
        end
        local warn = ({ en = 'Install will stop: %d armor(s) would get more than 14 passives (first: %s).',
                        ['zh-Hans'] = '安装会停止：有 %d 件护甲会超过 14 个被动（例如 %s）。',
                        ['zh-Hant'] = '安裝會停止：有 %d 件護甲會超過 14 個被動（例如 %s）。',
                        ru = 'Установка остановится: у %d брони больше 14 пассивов (напр. %s).' })[settings.lang] or
                     'Install will stop: %d armor(s) would get more than 14 passives (first: %s).'
        weapon.note = weapon.sse_base_note .. (over > 0 and ('  ·  ' .. warn:format(over, first or '?')) or '')
    end
    if weapon and weapon.armor == 0x7E000002 then
        if not weapon.by_id['stack_conflicts'] then
            local row = add_row(weapon, 'Stacks', 'stack_conflicts', 'When both passives have the same modifier',
                                'u32', { part('stack_conflicts', KINDS[TYPES.passive].list[1], 0, 'u32', 4294967295) },
                                0, 1, 1, 1)
            row.sse_setting = 'conflicts'
            row.sse_options = { { 0, 'Stack all' }, { 1, 'Strongest only' } }
            row.sse_current = function() return state.sse_cfg.conflicts == 'strongest' and 1 or 0 end
            row.note = function()
                return state.sse_cfg.conflicts == 'strongest' and
                    'The value further from "no effect" wins (a multiply counts by how far it is from x1).' or
                    'Every row is kept; the game applies each modifier id once, so the first one counts.'
            end
        end
        return built
    end
    return built
end

-- what that row shows, and what clicking its options does
state.sse_row_value_armor = row_value
row_value = function(row, default)
    if row and row.sse_setting == 'conflicts' then return state.sse_cfg.conflicts == 'strongest' and 1 or 0 end
    if row and row.sse_setting == 'count' then
        return #(MOD.kits.list_of(row.sse_page or ui.weapon) or {})
    end
    return state.sse_row_value_armor(row, default)
end

state.sse_click_armor = click
click = function(key)
    if key == 'sse_add_custom' then
        state.sse_add_to_custom(ui.weapon)
        return
    elseif key == 'sse_add_all' then                       -- a passive page: that passive joins Every armor
        state.sse_add_to_all(ui.weapon)
        return
    elseif key == 'sse_preview' then                   -- the Every armor page: its final effects
        -- (not `a and nil or b`: that always takes b, so the preview could never close)
        if state.sse_preview then
            state.sse_preview = nil
        else
            state.sse_preview = state.sse_preview_of(ui.weapon)
        end
        return
    elseif key == 'sse_preview_close' then
        state.sse_preview = nil
        return
    end
    local row_at, value = nil, nil
    if key then row_at, value = key:match('^sse_opt:(%d+):(.+)$') end
    if row_at then
        local row = ui.weapon and ui.weapon.rows[tonumber(row_at)]
        if row and row.sse_setting == 'conflicts' then
            state.sse_cfg.conflicts = tonumber(value) == 1 and 'strongest' or 'stack'
            mark_config_dirty()
            ui.message = { text = 'A modifier both passives have: ' .. state.sse_cfg.conflicts, till = api.now() + 5 }
            return
        end
    end
    return state.sse_click_armor(key)
end

-- ---- the preview: a list of passives, merged the way the install merges them, then added up ----
state.sse_strength = function(typ, v)
    if typ == 2 then return (v <= 0) and math.huge or math.abs(math.log(v)) end
    return math.abs(v)
end

state.sse_merge = function(list)
    local policy = state.sse_cfg.conflicts
    local spec = KINDS[TYPES.passive]
    local seen, order, groups = {}, {}, {}
    local function add(list_of)
        for _, id in ipairs(list_of) do
            local other = by_hash[string.format('FFFFFFFE%08X', id)]
            local table_key = other and other.passive
            local entry = table_key and tables[table_key]
            if entry then
                for _, field in ipairs({ { 'mods', false }, { 'stats', true } }) do
                    for _, m in ipairs(entry.index[field[1]] or {}) do
                        local v = read_field(field_at(table_key, m.offset, 'f32', 100000))
                        if v then
                            local mid = m.id or m.stat
                            local known = (field[2] and spec.STATS[mid]) or spec.MODS[mid]
                            local name = known and settings.tr(known) or
                                         (settings.tr('Unnamed effect') .. ' ' .. string.format('%08X', mid))
                            local key = name
                            if not seen[key] then
                                seen[key] = true
                                order[#order + 1] = key
                                groups[key] = { name = name, rows = {}, known = known }
                            end
                            groups[key].rows[#groups[key].rows + 1] = { type = field[2] and 2 or (m.type or 0), value = v }
                        end
                    end
                end
            end
        end
    end
    add(list or {})
    local out = {}
    for _, key in ipairs(order) do
        local group = groups[key]
        local uniq = {}
        for _, r in ipairs(group.rows) do
            local dup = false
            for _, u in ipairs(uniq) do
                if u.type == r.type and math.abs(u.value - r.value) < 1e-6 then dup = true end
            end
            if not dup then uniq[#uniq + 1] = r end
        end
        if #uniq > 0 then
            if policy == 'strongest' and #uniq > 1 then
                local best = uniq[1]
                for _, u in ipairs(uniq) do
                    if state.sse_strength(u.type, u.value) > state.sse_strength(best.type, best.value) then
                        best = u
                    end
                end
                uniq = { best }
            end
            local added, other = {}, {}
            for _, u in ipairs(uniq) do
                if u.type == 1 or u.type == 2 then
                    local at = nil
                    for k, a in ipairs(added) do if a.type == u.type then at = k end end
                    if at then
                        added[at].value = u.type == 1 and (added[at].value + u.value) or (added[at].value * u.value)
                    else
                        added[#added + 1] = { type = u.type, value = u.value }
                    end
                else
                    other[#other + 1] = u
                end
            end
            for _, a in ipairs(added) do other[#other + 1] = a end
            out[#out + 1] = { name = group.name, rows = other, known = group.known }
        end
    end
    table.sort(out, function(a, b)
        if (a.known ~= nil) ~= (b.known ~= nil) then return a.known ~= nil end
        return a.name:lower() < b.name:lower()
    end)
    return out
end

state.sse_effect_text = function(r)
    if r.type == 2 then
        local pct = (r.value - 1) * 100
        if math.abs(pct) >= 0.5 then
            return string.format('×%s（%+d%%）', string.format('%g', r.value), math.floor(pct + 0.5))
        end
        return string.format('×%s', string.format('%g', r.value))
    elseif r.type == 1 then
        return string.format('+%s', string.format('%g', r.value))
    elseif r.type == 3 then
        return string.format('%g', r.value)
    end
    return string.format('=%s', string.format('%g', r.value))
end

-- the list a page stands for: its own armor's, plus Every armor's
state.sse_page_list = function(page)
    local list, seen = {}, {}
    local function add(one)
        for _, id in ipairs(one or {}) do
            if not seen[id] then seen[id] = true; list[#list + 1] = id end
        end
    end
    if page.armor == state.sse_every_armor then
        add(settings.armor_passives[state.sse_every_armor])
    else
        add(MOD.kits.list_of(page))
        add(settings.armor_passives[state.sse_every_armor])
    end
    return list
end

state.sse_preview_of = function(page)
    local effects = state.sse_merge(state.sse_page_list(page))
    local lines = {}
    for _, e in ipairs(effects) do
        local parts = {}
        for _, r in ipairs(e.rows) do parts[#parts + 1] = state.sse_effect_text(r) end
        lines[#lines + 1] = e.name .. '   ' .. table.concat(parts, '，')
    end
    if #lines == 0 then lines[1] = settings.tr('Nothing yet: add a passive below.') end
    return { title = settings.tr('Final effects') .. '（' .. #lines .. '）', lines = lines }
end

-- "Add to the custom passive", on a passive page: that passive joins the bundle (no limit of its own)
state.sse_add_to_custom = function(page)
    local index = page and page.passive and tables[page.passive] and tables[page.passive].index
    local pid = index and index.id
    if not pid or pid == state.sse_custom_id then
        ui.message = { text = 'This page has no passive to add.', till = api.now() + 5 }
        return
    end
    local list = {}
    for _, id in ipairs(settings.armor_passives[state.sse_custom_id] or {}) do list[#list + 1] = id end
    for _, id in ipairs(list) do
        if id == pid then
            ui.message = { text = 'Already in the custom passive: ' .. tostring(page.name), till = api.now() + 5 }
            return
        end
    end
    list[#list + 1] = pid
    local custom = by_hash[string.format(state.sse_page_armor, state.sse_custom_id)]
    MOD.kits.set(custom, list)
    ui.message = { text = tostring(page.name) .. ' is now in the custom passive (' .. #list .. ' in all).',
                   till = api.now() + 5 }
end

-- "Add to every armor", on a passive page: that passive joins the Every armor list. It is a virtual
-- list: every armor gets it at install, and it is only shown on the Every armor page, not on the
-- armors' own pages.
state.sse_add_to_all = function(page)
    local index = page and page.passive and tables[page.passive] and tables[page.passive].index
    local pid = index and index.id
    if not pid then
        ui.message = { text = 'This page has no passive to add.', till = api.now() + 5 }
        return
    end
    local list = {}
    for _, id in ipairs(settings.armor_passives[state.sse_every_armor] or {}) do list[#list + 1] = id end
    for _, id in ipairs(list) do
        if id == pid then
            ui.message = { text = 'Already in Every armor: ' .. tostring(page.name), till = api.now() + 5 }
            return
        end
    end
    if #list >= MOD.kits.MAX_PASSIVES then
        ui.message = { text = 'Every armor is full: 14 passives at most.', till = api.now() + 5 }
        return
    end
    list[#list + 1] = pid
    local every = by_hash[string.format(state.sse_page_armor, state.sse_every_armor)]
    MOD.kits.set(every, list)                       -- (writes settings.armor_passives and marks it dirty)
    local over = 0
    for _, other in ipairs(weapons) do
        local armor = other.armor
        if armor and armor ~= state.sse_every_armor and armor ~= 0x7E000002 then
            local own, seen = {}, {}
            for _, id in ipairs(MOD.kits.list_of(other) or {}) do seen[id] = true; own[#own + 1] = id end
            for _, id in ipairs(list) do if not seen[id] then seen[id] = true; own[#own + 1] = id end end
            if #own > MOD.kits.MAX_PASSIVES then over = over + 1 end
        end
    end
    ui.message = { text = tostring(page.name) .. ' is now on every armor.' ..
                         (over > 0 and (' ' .. (({ en = '%d armor(s) would go past 14: install will stop.',
                                                  ['zh-Hans'] = '有 %d 件护甲会超过 14 个：安装会停止。',
                                                  ['zh-Hant'] = '有 %d 件護甲會超過 14 個：安裝會停止。',
                                                  ru = 'У %d брони будет больше 14: установка остановится.' })[settings.lang] or
                                                '%d armor(s) would go past 14: install will stop.'):format(over)) or ''),
                   till = api.now() + 5 }
end

; (function()
    -- the headless harness must not write the player's config: probes set state._test.no_save
    if rawget(_G, 'SHODAN_LOCAL_TEST') then
        state.sse_save_guard = save_config
        save_config = function()
            if state._test and state._test.no_save then return end
            return state.sse_save_guard()
        end
    end
end)()

;(function()
    for _, lang in ipairs(MOD.langs or {}) do
        local words = ({ ['zh-Hans'] = { '所有护甲', '护甲设置', '添加该被动效果到所有护甲', '全部护甲',
                                        '预览最终效果', '预览', '最终效果', '未命名效果', '未命名效果',
                                        '全部堆叠', '只取最强', '两个被动都有的修正',
                                        '此处的被动会加到每一件护甲上，不论你穿哪一件。',
                                        '设置如何叠加护甲被动。', '添加被动', '该护甲没有自己的被动可复制。',
                                        '这一页没有可添加的被动。', '所有护甲已满：最多 14 个被动。',
                                        '已在所有护甲中：', ' 已加到所有护甲。',
                                        '另有 %d 个来自所有护甲', '有 %d 件护甲会超过 14 个：安装会停止。' },
                         ['zh-Hant'] = { '所有護甲', '護甲設定', '把該被動效果加到所有護甲', '全部護甲',
                                        '預覽最終效果', '預覽', '最終效果', '未命名效果', '未命名效果',
                                        '全部堆疊', '只取最強', '兩個被動都有的修正',
                                        '此處的被動會加到每一件護甲上，不論你穿哪一件。',
                                        '設定如何疊加護甲被動。', '新增被動', '該護甲沒有自己的被動可複製。',
                                        '這一頁沒有可新增的被動。', '所有護甲已滿：最多 14 個被動。',
                                        '已在所有護甲中：', ' 已加到所有護甲。' },
                         ['ru'] = { 'Вся броня', 'Настройки брони', 'Добавить пассив всей броне', 'всей броне',
                                    'Предпросмотр итога', 'Обзор', 'Итоговые эффекты', 'Без имени', 'Без имени',
                                    'Все подряд', 'Только сильнейшее', 'Модификатор у обоих пассивов',
                                    'Пассивы здесь добавляются ко всей броне.',
                                    'Как применяются пассивы брони.', 'Добавить пассив', 'У этой брони нет своих пассивов.',
                                    'На этой странице нет пассива.', 'Вся броня заполнена: не более 14.',
                                    'Уже во всей броне: ', ' теперь на всей броне.',
                                    'Ещё %d из «всей брони»', 'У %d брони будет больше 14: установка остановится.' },
                         ['es-419'] = { 'Toda la armadura', 'Ajustes de armadura', 'Añadir pasiva a toda la armadura',
                                        'A toda', 'Previsualizar el resultado', 'Previsualizar',
                                        'Efectos finales', 'Efecto sin nombre', 'Efecto sin nombre',
                                        'Acumular todo', 'Solo lo más fuerte', 'Modificador en ambas pasivas',
                                        'Las pasivas de aquí se añaden a toda la armadura.',
                                        'Cómo se aplican las pasivas.', 'Añadir pasiva',
                                        'Esta armadura no tiene pasivas propias.', 'Esta página no tiene pasiva.',
                                        'Toda la armadura está llena: 14 como máximo.',
                                        'Ya en toda la armadura: ', ' ahora está en toda la armadura.',
                                        'Además %d de toda la armadura', '%d armadura(s) pasarían de 14: se detendrá.' },
                         ['pt-BR'] = { 'Toda a armadura', 'Ajustes da armadura', 'Adicionar passiva a toda a armadura',
                                       'A todas', 'Pré-visualizar o resultado', 'Pré-visualizar',
                                       'Efeitos finais', 'Efeito sem nome', 'Efeito sem nome',
                                       'Acumular tudo', 'Só o mais forte', 'Modificador nas duas passivas',
                                       'As passivas aqui são adicionadas a toda a armadura.',
                                       'Como as passivas são aplicadas.', 'Adicionar passiva',
                                       'Esta armadura não tem passivas próprias.', 'Esta página não tem passiva.',
                                       'Toda a armadura está cheia: 14 no máximo.',
                                       'Já em toda a armadura: ', ' agora está em toda a armadura.',
                                       'Mais %d de toda a armadura', '%d armadura(s) passariam de 14: vai parar.' } })[lang.id]
        if words then
            lang.exact['Custom passive'] = ({ ['zh-Hans'] = '自定义被动', ['zh-Hant'] = '自訂被動',
                                              ['ru'] = 'Свой пассив', ['es-419'] = 'Pasiva propia',
                                              ['pt-BR'] = 'Passiva própria' })[lang.id]
            lang.exact['Add to the custom passive'] = ({ ['zh-Hans'] = '添加该被动效果到自定义被动',
                                                         ['zh-Hant'] = '把該被動效果加到自訂被動',
                                                         ['ru'] = 'В свой пассив',
                                                         ['es-419'] = 'A la pasiva propia',
                                                         ['pt-BR'] = 'À passiva própria' })[lang.id]
            lang.exact['To custom'] = ({ ['zh-Hans'] = '加到自定义', ['zh-Hant'] = '加到自訂',
                                         ['ru'] = 'в свой', ['es-419'] = 'A propia', ['pt-BR'] = 'À própria' })[lang.id]
            lang.exact['To every armor'] = ({ ['zh-Hans'] = '加到所有护甲', ['zh-Hant'] = '加到所有護甲',
                                              ['ru'] = 'всей броне', ['es-419'] = 'A todas',
                                              ['pt-BR'] = 'A todas' })[lang.id]
            lang.exact['A bundle: the passives here reach an armor as one entry. Add it to an armor below.'] =
                ({ ['zh-Hans'] = '一个打包：这里的被动会作为一条记录加到护甲上。在下面把它加到护甲。',
                    ['zh-Hant'] = '一個打包：這裡的被動會作為一條記錄加到護甲上。在下面把它加到護甲。',
                    ['ru'] = 'Набор: пассивы отсюда попадают в броню одной записью.',
                    ['es-419'] = 'Un paquete: las pasivas de aquí llegan a la armadura como una entrada.',
                    ['pt-BR'] = 'Um pacote: as passivas daqui chegam à armadura como uma entrada.' })[lang.id]
            table.insert(lang.prefix, { 'Already in the custom passive: ',
                                        ({ ['zh-Hans'] = '已在自定义被动中：', ['zh-Hant'] = '已在自訂被動中：',
                                           ['ru'] = 'Уже в своём пассиве: ', ['es-419'] = 'Ya en la pasiva propia: ',
                                           ['pt-BR'] = 'Já na passiva própria: ' })[lang.id] })
            table.insert(lang.prefix, { ' is now in the custom passive (', 
                                        ({ ['zh-Hans'] = ' 已加入自定义被动（共 ', ['zh-Hant'] = ' 已加入自訂被動（共 ',
                                           ['ru'] = ' теперь в своём пассиве (всего ', ['es-419'] = ' ya está en la pasiva propia (',
                                           ['pt-BR'] = ' agora está na passiva própria (' })[lang.id] })
            lang.exact['Every armor'] = words[1]
            lang.exact['Armor settings'] = words[2]
            lang.exact['Add to every armor'] = words[3]
            lang.exact['Add to all'] = words[4]
            lang.exact['Preview the result'] = words[5]
            lang.exact['Preview'] = words[6]
            lang.exact['Final effects'] = words[7]
            lang.exact['Unnamed effect'] = words[8]
            lang.exact['Stack all'] = words[10]
            lang.exact['Strongest only'] = words[11]
            lang.exact['When both passives have the same modifier'] = words[12]
            lang.exact['The passives here are added to every armor, whatever you wear.'] = words[13]
            lang.exact['How the armor passives are applied.'] = words[14]
            lang.exact['Nothing yet: add a passive below.'] = words[15]
            lang.exact['This armor has no passives of its own to copy.'] = words[16]
            lang.exact['This page has no passive to add.'] = words[17]
            lang.exact['Every armor is full: 14 passives at most.'] = words[18]
            table.insert(lang.prefix, { 'Already in Every armor: ', words[19] })
            table.insert(lang.prefix, { 'Plus %d from Every armor', words[21] })
            table.insert(lang.prefix, { '%d armor(s) would go past 14: install will stop.', words[22] })
            table.insert(lang.prefix, { ' is now on every armor.', words[20] })
            if lang.lower then
                lang.lower['add to every armor'] = words[3]
                lang.lower['add to all'] = words[4]
                lang.lower['preview the result'] = words[5]
                lang.lower['preview'] = words[6]
                lang.lower['final effects'] = words[7]
                lang.lower['unnamed effect'] = words[8]
                lang.lower['stack all'], lang.lower['strongest only'] = words[10], words[11]
            end
            if lang.upper then
                lang.upper['ADD TO EVERY ARMOR'] = words[3]
                lang.upper['ADD TO ALL'] = words[4]
                lang.upper['PREVIEW THE RESULT'] = words[5]
                lang.upper['PREVIEW'] = words[6]
                lang.upper['FINAL EFFECTS'] = words[7]
                lang.upper['UNNAMED EFFECT'] = words[8]
                lang.upper['STACK ALL'], lang.upper['STRONGEST ONLY'] = words[10], words[11]
            end
        end
    end
end)()
