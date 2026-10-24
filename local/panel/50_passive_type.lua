-- local overlay: a passive modifier's effect type, next to its value.
--
-- A passive's effect row is 16 bytes: id (+0), type (+4), value (+8), text hash (+12). The panel
-- edits the value only, so a passive's effects could never be turned from "set 0.5" into "×1.5"
-- or "+50" — which is how Armory Forge's advanced edits work. This adds one row per modifier,
-- right under it:
--
--   Explosive damage taken        0.5
--     Effect type                 2        (0 set / 1 add / 2 multiply / 3 time)
--
-- The value row's own range follows its type (the panel picks it by type when it builds the row),
-- so after changing a type, reopening the page gives the value the matching limits.
--
-- No `local` at this level (upstream's chunk sits at LuaJIT's 200-local limit).
state.sse_add_row_ptype = add_row

state.sse_modifier_types = { [0] = 'set', [1] = 'add', [2] = 'multiply', [3] = 'time' }

add_row = function(weapon, section, id, label, storage, parts, min, max, small, big)
    local row = state.sse_add_row_ptype(weapon, section, id, label, storage, parts, min, max, small, big)
    -- a passive modifier: section 'Passive', id 'mod_<id>', one value part at the row's +8
    if section ~= 'Passive' or type(id) ~= 'string' or id:sub(1, 4) ~= 'mod_' then return row end
    local first = parts and parts[1]
    if not first or #parts > 1 then return row end          -- (a joined modifier: one row, three ids)
    -- the row is id (+0), type (+4), value (+8), text hash (+12): check it really is, by reading the
    -- id back (offsets in a passive block are not aligned to 16)
    local type_at, id_at = first.field.offset - 4, first.field.offset - 8
    if id_at < 0 then return row end
    local row_id = tonumber(id:sub(5), 16)
    if not row_id then return row end
    -- the limit is the whole u32 range: a modifier id is a hash, not a small number
    if read_field(field_at(first.field.kind, id_at, 'u32', 4294967295)) ~= row_id then return row end
    local type_id = id .. '_type'
    if weapon.by_id[type_id] then return row end
    local made = state.sse_add_row_ptype(weapon, section, type_id, 'Effect type', 'u32',
                                   { part(type_id, first.field.kind, type_at, 'u32', 100000) }, 0, 3, 1, 1)
    -- a choice row, drawn like the panel's own Settings options
    made.sse_options = { { 0, 'Set' }, { 1, 'Add' }, { 2, 'Multiply' }, { 3, 'Time' } }
    made.sse_current = function() return read_field(made.parts[1].field) end
    made.sse_effect_type = true
    -- keep it directly under its modifier
    table.remove(weapon.rows)
    local at = #weapon.rows
    for k = 1, #weapon.rows do
        if weapon.rows[k] == row then at = k break end
    end
    table.insert(weapon.rows, at + 1, made)
    return row
end

;(function()
    for _, lang in ipairs(MOD.langs or {}) do
        local words = ({ ['zh-Hans'] = '效果类型', ['zh-Hant'] = '效果類型', ['ru'] = 'Тип эффекта' })[lang.id]
        local opts = ({ ['zh-Hans'] = { '设值', '相加', '相乘', '计时' },
                        ['zh-Hant'] = { '設值', '相加', '相乘', '計時' },
                        ['ru'] = { 'задать', 'прибавить', 'умножить', 'время' } })[lang.id]
        if opts then
            lang.exact['Set'], lang.exact['Add'] = opts[1], opts[2]
            lang.exact['Multiply'], lang.exact['Time'] = opts[3], opts[4]
            if lang.lower then
                lang.lower['set'], lang.lower['add'] = opts[1], opts[2]
                lang.lower['multiply'], lang.lower['time'] = opts[3], opts[4]
            end
            if lang.upper then
                lang.upper['SET'], lang.upper['ADD'] = opts[1], opts[2]
                lang.upper['MULTIPLY'], lang.upper['TIME'] = opts[3], opts[4]
            end
        end
        if words then
            lang.exact['Effect type'] = words
            if lang.lower then lang.lower['effect type'] = words end
            if lang.upper then lang.upper['EFFECT TYPE'] = words end
        end
        local kinds = ({ ['zh-Hans'] = '0 设值，1 相加，2 相乘，3 计时',
                         ['zh-Hant'] = '0 設值，1 相加，2 相乘，3 計時',
                         ['ru'] = '0 задать, 1 прибавить, 2 умножить, 3 время' })[lang.id]
        if kinds then
            table.insert(lang.prefix, { '0 set, 1 add, 2 multiply, 3 time', kinds })
        end
    end
end)()
