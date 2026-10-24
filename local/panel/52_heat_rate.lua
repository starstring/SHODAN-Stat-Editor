-- local overlay: the cooling rate under each cool-down time.
--
-- The panel's two cool-down rows ("Cool-down time, full heat (s)" and "Cool-down time after
-- overheat (s)") are times computed from the heat to shed over a rate: the game stores the rate
-- (heat per second) at +128 and +140 of the heat record. A time is handy, but a rate is what the
-- game actually reads, so each time row gets its rate right below it:
--
--   Cool-down time, full heat (s)        12.5
--     Cooling rate (heat/s)              8
--   Cool-down time after overheat (s)    ...
--     Cooling rate, after overheat (heat/s)
--
-- Both write the same field (the time row converts: rate = heat / seconds), so editing either one
-- shows up in the other as soon as the page is redrawn.
--
-- No `local` at this level (upstream's chunk sits at LuaJIT's 200-local limit).
state.sse_add_row_heat = add_row

add_row = function(weapon, section, id, label, storage, parts, min, max, small, big)
    local row = state.sse_add_row_heat(weapon, section, id, label, storage, parts, min, max, small, big)
    local spec = ({ heat_cool = { 'cool_rate', 'Cooling rate (heat/s)', 'The heat shed per second from full heat.' },
                    heat_cool_overheated = { 'cool_rate_overheated', 'Cooling rate, after overheat (heat/s)',
                                             'The heat shed per second once the weapon overheated.' } })[id]
    -- (the time row's .span is set by the caller *after* add_row returns, so it cannot be used here)
    if not spec or not row or weapon.record then return row end
    local field = parts and parts[1] and parts[1].field
    if not field or field.kind ~= T_HEAT then return row end
    if weapon.by_id[spec[1]] then return row end
    local made = state.sse_add_row_heat(weapon, section, spec[1], spec[2], 'f32',
                                        { part(spec[1], T_HEAT, field.offset, 'f32', 1000000) }, 0.01, 100000, 0.5, 5)
    if made then
        made.note = spec[3] .. ' The time above is the heat to shed divided by this.'
        -- keep it directly under its time row
        table.remove(weapon.rows)
        local at = #weapon.rows
        for k = 1, #weapon.rows do
            if weapon.rows[k] == row then at = k break end
        end
        table.insert(weapon.rows, at + 1, made)
    end
    return row
end

;(function()
    for _, lang in ipairs(MOD.langs or {}) do
        local words = ({ ['zh-Hans'] = { '冷却速率(热量/秒)', '过热后冷却速率(热量/秒)',
                                        '每秒散掉的热量。上面的秒数 = 要散的热量 ÷ 这个速率。' },
                         ['zh-Hant'] = { '冷卻速率(熱量/秒)', '過熱後冷卻速率(熱量/秒)',
                                        '每秒散掉的熱量。上面的秒數 = 要散的熱量 ÷ 這個速率。' },
                         ['ru'] = { 'Скорость охлаждения (тепло/с)', 'Скорость охлаждения после перегрева (тепло/с)',
                                    'Тепло, сбрасываемое в секунду. Время выше = тепло / эта скорость.' } })[lang.id]
        if words then
            lang.exact['Cooling rate (heat/s)'] = words[1]
            lang.exact['Cooling rate, after overheat (heat/s)'] = words[2]
            if lang.lower then
                lang.lower['cooling rate (heat/s)'] = words[1]
                lang.lower['cooling rate, after overheat (heat/s)'] = words[2]
            end
            if lang.upper then
                lang.upper['COOLING RATE (HEAT/S)'] = words[1]
                lang.upper['COOLING RATE, AFTER OVERHEAT (HEAT/S)'] = words[2]
            end
            table.insert(lang.prefix, { 'The heat shed per second from full heat.', words[3] })
            table.insert(lang.prefix, { 'The heat shed per second once the weapon overheated.', words[3] })
        end
    end
end)()
