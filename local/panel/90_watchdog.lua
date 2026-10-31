-- local overlay: two small startup safeguards, no hooks into the frame loop.
--
-- 1. The panel truncates its log on every flush, so the lines that explain a crash are gone by the next
--    start (all that was left once was the "panel errors 10" counter). The log is copied to
--    <name>.prev at load, before this session writes anything.
-- 2. The panel reopens the page it was last on. If that is one of this fork's own pages and drawing it
--    ever fails, every start would come up with a closed editor; start on the tab's first page instead.
--
-- Everything here lives inside one function: this chunk is at LuaJIT's 200-local limit, so a `local` at
-- this level would stop the whole panel from loading (it did, once).
;(function()
    if not MOD.offline then return end
    local dir = data_dir('Logs')
    if dir then
        local path = dir .. '/' .. MOD.log
        local old = io.open(path, 'rb')
        if old then
            local text = old:read('*a')
            old:close()
            if text and #text > 0 then
                local keep = io.open(path .. '.prev', 'wb')
                if keep then
                    keep:write(text)
                    keep:close()
                end
            end
        end
    end
    -- the panel truncates its log on every flush, so a "panel error: ..." line lives only until the next
    -- one. Keep those (and our own notes) in a second file that is only ever appended to.
    local write = log
    log = function(...)
        local args = { ... }
        pcall(write, unpack(args))
        pcall(function()
            local first = args[1]
            if type(first) ~= 'string' then return end
            if not (first:find('panel error', 1, true) or first:find('local:', 1, true)) then return end
            local logs = data_dir('Logs')
            local handle = logs and io.open(logs .. '/local-panel-errors.log', 'ab')
            if not handle then return end
            local line = { os.date('%H:%M:%S '), first }
            for k = 2, #args do line[#line + 1] = ' ' .. tostring(args[k]) end
            handle:write(table.concat(line), string.char(10))
            handle:close()
        end)
    end

    local remembered = settings.last and settings.last.stat and settings.last.stat.weapon
    if remembered then
        for _, id in ipairs({ state.sse_custom_id, state.sse_every_armor, 0x7E000002 }) do
            if id and remembered == string.format('FFFFFFF8%08X', id) then
                settings.last.stat.weapon = nil
                log("local: not reopening " .. remembered .. " (a page of this fork)")
            end
        end
    end
end)()
