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
                        -- part 1 is the row in the stratagem list; the others belong to variants that
                        -- are not (the Rocket Sentry's is the President's reward one: 45 s, 5 s, 1 use)
                        local held = {}
                        for i = 2, #row.parts do held[#held + 1] = number_text(read_field(row.parts[i].field) or 0) end
                        return 'not in the stratagem list: ' .. table.concat(held, ' / ')
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
        local text = ({ ['zh-Hans'] = '不在战备列表里的同名行：', ['zh-Hant'] = '不在戰備列表裡的同名行：',
                        ['ru'] = 'не в списке стратегем, строка с тем же именем: ' })[lang.id]
        if text then
            table.insert(lang.prefix, { 'not in the stratagem list: ', text })
        end
    end
end)()
