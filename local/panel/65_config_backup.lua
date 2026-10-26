-- local overlay: keep the previous config.txt as config.txt.bak before every save.
--
-- The panel writes config.txt in one go, so a crash or a full disk in the middle of that write leaves
-- a truncated file and every saved value is gone. Armory Forge's offline editor does the same thing
-- for its loadout.ini (the old file becomes loadout.ini.backup before the new one is written); this
-- is the cheap half of that - a copy of what was there, one line to recover from.
--
-- No `local` at this level (upstream's chunk sits at LuaJIT's 200-local limit).
state.sse_save_config_backup = save_config

save_config = function()
    local path = config_path()
    if path then
        local old = io.open(path, 'rb')
        if old then
            local text = old:read('*a')
            old:close()
            if text and #text > 0 then
                local backup = io.open(path .. '.bak', 'wb')
                if backup then
                    backup:write(text)
                    backup:close()
                end
            end
        end
    end
    return state.sse_save_config_backup()
end
