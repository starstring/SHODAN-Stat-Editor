-- local overlay: everything this fork adds to Stat Editor, spliced onto the end of
-- src/stat_editor_offline.lua by local/build_panel.py (the upstream file is never modified, so a
-- git pull from the project's main branch never conflicts).
--
-- This block is one more statement of the panel's own chunk, so the chunk's locals are in scope:
-- add_row / part / field_at / weapons / tables / KINDS / TYPES / resolve / resolve_gun ... That is
-- what makes extra stats possible without touching the file itself.
--
-- It declares no local of its own: upstream's chunk sits at LuaJIT's 200-local limit, so scratch
-- values live in `state` (the panel's own table) instead.
--
-- Hooks that are only useful while developing live behind SHODAN_LOCAL_TEST (set by
-- local/tools/panel_dump.lua): the headless dump reads the panel's own tables through them, and
-- `set` writes a value the way the UI does (write_field + read back).
if rawget(_G, 'SHODAN_LOCAL_TEST') then
    state._test = { weapons = weapons, by_hash = by_hash, fields = fields, tables = tables, KINDS = KINDS,
                    TYPES = TYPES, defaults = defaults, read_field = read_field, field_at = field_at,
                    default_of = default_of, MOD = MOD, state = state, HEADER_BYTES = HEADER_BYTES,
                    bytes = function(address, size) return api.read(address, size) end,
                    resolve = resolve, select_weapon = select_weapon,
                    -- call whatever save_config is at call time (later overlays wrap it)
                    save_config = function() save_config() end,
                    -- the UI state and the click dispatcher, to drive a real action
                    ui = ui, click = function(key) return click(key) end }
    -- the panel's own display value for a row (it may be wrapped by a later overlay: call it late)
    state._test.value_of = function(row, default) return row_value(row, default) end
    -- ok, old, new, why = state._test.set('A8A91EB54892B6B2', 'calibre', 20)
    state._test.set = function(hash, id, value)
        local weapon = by_hash[tostring(hash):upper()]
        if not weapon then return false, nil, nil, 'no weapon' end
        local parts = MOD.parts_of(weapon, id)
        local part = parts and parts[1]
        if not part then return false, nil, nil, 'no such stat' end
        local old = read_field(part.field)
        if not write_field(part.field, value) then return false, old, nil, 'refused' end
        return true, old, read_field(part.field)
    end
    MOD._test = state._test
end
