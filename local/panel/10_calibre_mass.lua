-- local overlay: calibre and mass on each weapon's own projectile rows.
--
-- The panel lists a shot's projectile record per shot (Projectiles per shot, Velocity, Drag,
-- Gravity, Penetration slowdown) from `projectile_rows`, but calibre (+24) and mass (+36) of that
-- same record were only on the Records tab. They belong to the weapon page like the rest, so this
-- wraps add_row: right after a weapon page's `...pellets` row the two rows are added and moved up,
-- so the panel reads them in its usual order:
--
--   Projectiles per shot | Calibre (mm) | Mass (kg) | Velocity (m/s) | Drag | ...
--
-- The row ids follow the panel's own naming (`calibre`, and `c1_calibre` for a charge weapon's
-- first shot), so saved values and presets that name them survive. Shrapnel count (+80) is already
-- on the weapon pages: `MOD.records.shrapnel_rows` adds it with the shrapnel projectile (+84).
--
-- No `local` at this level: upstream's chunk sits at LuaJIT's 200-local limit, so scratch values
-- live in `state` (the panel's own table).
state.sse_add_row_calibre = add_row

-- rows are appended by add_row; take the last `count` rows and splice them in after `at`
state.sse_splice = function(weapon, at, count)
    local appended = {}
    for k = 1, count do appended[k] = table.remove(weapon.rows) end   -- popped: last first
    local ordered = {}
    for k = count, 1, -1 do ordered[#ordered + 1] = appended[k] end   -- back into append order
    for k, row in ipairs(ordered) do table.insert(weapon.rows, at + k, row) end
end

add_row = function(weapon, section, id, label, storage, parts, min, max, small, big)
    local before = #weapon.rows
    local row = state.sse_add_row_calibre(weapon, section, id, label, storage, parts, min, max, small, big)
    if weapon.record or type(id) ~= 'string' or id:sub(-7) ~= 'pellets' then return row end
    local field = parts and parts[1] and parts[1].field
    if not field or field.kind ~= T_PROJECTILE then return row end
    local p = field.offset - 28                        -- the start of that shot's projectile row
    local prefix = id:sub(1, #id - 7)                  -- '' or 'c1_', 'c2_', ... for a charge weapon
    local made = 0
    for _, spec in ipairs({ { 'calibre', 'Calibre (mm)', 24, 1000, 0.1, 1 },
                            { 'mass', 'Mass (kg)', 36, 10000, 0.1, 1 } }) do
        local new_id = prefix .. spec[1]
        if not weapon.by_id[new_id] then
            state.sse_add_row_calibre(weapon, section, new_id, spec[2], 'f32',
                              { part(new_id, T_PROJECTILE, p + spec[3], 'f32', 100000) },
                              0, spec[4], spec[5], spec[6])
            made = made + 1
        end
    end
    if made > 0 then state.sse_splice(weapon, before + 1, made) end
    return row
end
