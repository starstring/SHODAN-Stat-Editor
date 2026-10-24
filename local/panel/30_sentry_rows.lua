-- local overlay: a page that merged two same-named stratagem rows shows one of them, not the average.
--
-- A/MLS-4X Rocket Sentry has two stratagem rows with the same display name: the real one (150 s
-- cooldown, unlimited uses, in the stratagem grid at +392) and a hidden duplicate (45 s, one use,
-- +392 = 0). The panel puts both on the sentry's page as two parts of one row, and a row's value is
-- the average of its parts, so the page read "97.5 s" against the game's 150 s (and the call-in
-- 2.5 s against 0 s).
--
-- This keeps both parts (so an edit still reaches both) but shows the first one, and says what the
-- other holds. Typing a value already writes the same number to every part, so the row stays usable.
state.sse_resolve = resolve
resolve = function(weapon)
    state.sse_resolve(weapon)
    for _, row in ipairs(weapon.rows or {}) do
        if #row.parts > 1 and not row.show_first then
            local first = read_field(row.parts[1].field)
            for k = 2, #row.parts do
                local other = read_field(row.parts[k].field)
                if first and other and math.abs(other - first) > 1e-4 then
                    row.show_first = true
                    row.note = function()
                        local held = {}
                        for i = 1, #row.parts do held[i] = number_text(read_field(row.parts[i].field) or 0) end
                        return 'two stratagem rows share this name: ' .. table.concat(held, ' / ')
                    end
                    break
                end
            end
        end
    end
end

state.sse_row_value = row_value
row_value = function(row, default)
    if row.show_first then
        local get = default and default_of or read_field
        return get(row.parts[1].field)
    end
    return state.sse_row_value(row, default)
end

;(function()
    for _, lang in ipairs(MOD.langs or {}) do
        local text = ({ ['zh-Hans'] = '两条同名战略配备共用这一页：', ['zh-Hant'] = '兩條同名戰略配備共用這一頁：',
                        ['ru'] = 'одну страницу делят две строки стратегемы: ' })[lang.id]
        if text then
            table.insert(lang.prefix, { 'two stratagem rows share this name: ', text })
        end
    end
end)()
