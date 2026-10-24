-- local overlay: a beam weapon's beam range (BeamSettings +8), on its own page.
--
-- A beam weapon's damage comes from its beam record: the beam component (+0 beam type) -> the beam
-- row (+12 damage row). resolve_gun uses that only to find the damage row, so the beam's own
-- values — its range (+8, the 15 m the Meltagun reaches) — were not editable anywhere. This wraps
-- resolve_gun and adds the row right after the shot's damage / status rows, in a "Beam" section:
--
--   Damage | Status effects | Beam range (m) | Charge | ...
--
-- Only when the beam really is this weapon's damage source (the same test resolve_gun makes), so a
-- weapon that has a beam component but fires a projectile does not get the row.
--
-- No `local` at this level: upstream's chunk sits at LuaJIT's 200-local limit (see local/README.md).
state.sse_resolve_gun = resolve_gun

resolve_gun = function(weapon, key)
    local first = #weapon.rows
    state.sse_resolve_gun(weapon, key)
    if weapon.by_id['beam_range'] then return end
    local comp = tables[T_BEAM_WEAPON] and tables[T_BEAM_WEAPON].index[key]
    local kind = comp and read_field(field_at(T_BEAM_WEAPON, comp, 'u32', 100000))
    local brow = kind and tables[T_BEAM] and tables[T_BEAM].index[kind]
    if not brow then return end
    local id = read_field(field_at(T_BEAM, brow + 12, 'u32', 100000))
    local drow = id and tables[T_DAMAGE] and tables[T_DAMAGE].index[id]
    local hit = weapon.by_id['damage']                      -- the row the shot's damage came from
    -- that row sits inside the beam's damage record (a damage row is 76 B: +0 type, +4 damage)
    local span = hit and hit.field.kind == T_DAMAGE and (hit.field.offset - (drow or -1000))
    if not (drow and span and span >= 0 and span < 76) then return end
    local row = add_row(weapon, 'Beam', 'beam_range', 'Beam range (m)', 'f32',
                        { part('beam_range', T_BEAM, brow + 8, 'f32', 100000) }, 0, 10000, 1, 10)
    -- sections are drawn in row order: keep it with the shot's damage / status rows
    local after = first
    for k = first + 1, #weapon.rows - 1 do
        local section = weapon.rows[k].section
        if section ~= 'Damage' and not section:find('^Status effects') then break end
        after = k
    end
    table.remove(weapon.rows)                               -- the row just added is the last one
    table.insert(weapon.rows, after + 1, row)
end

-- the new texts, in the panel's own dictionaries (it looks English text up per language)
;(function()
    for _, lang in ipairs(MOD.langs or {}) do
        local words = ({ ['zh-Hans'] = { '光束', '光束射程(米)' }, ['zh-Hant'] = { '光束', '光束射程(米)' },
                         ['ru'] = { 'Луч', 'Дальность луча (м)' } })[lang.id]
        if words then
            lang.exact['Beam'] = words[1]
            lang.exact['Beam range (m)'] = words[2]
            if lang.lower then lang.lower['beam range (m)'] = words[2] end
            if lang.upper then lang.upper['BEAM RANGE (M)'] = words[2] end
        end
    end
end)()
