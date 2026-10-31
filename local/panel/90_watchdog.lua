-- local overlay: while the panel is not ready, log where it is every couple of seconds.
--
-- Startup is a chain of slices (find the tables, list the pages, resolve every page, read every field's
-- game value, apply the saved values). A stall in one of them leaves the window on "resolving weapons"
-- with no error in the log, which says nothing about *which* slice stopped. This logs the counters of
-- each one, so the log names it:
--
--   local: startup preparing, page 913/913, defaults 81234/83416, saved 40/115, fields 83416
--
-- Offline only, and it writes nothing else. Remove it once startup is trustworthy again.
if MOD.offline then
    ;(function()
        -- the panel truncates its log on every flush, so a crash wipes the lines that explain it: keep
        -- the log as it stands now as <name>.prev, before this session writes anything
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
        local at, last, started = nil, nil, nil
        local check = update
        update = function(dt)
            if state.phase ~= 'ready' then
                started = started or api.now()
                at = at or api.now()
                if api.now() - at >= 2 then
                    at = api.now()
                    local line = string.format('local: startup %s, page %s/%s, defaults %s/%s, saved %s/%s, fields %s',
                        tostring(state.phase),
                        progress and progress.next or '-', #weapons,
                        progress and progress.read or '-', #fields,
                        apply_at, #pending, #fields)
                    if line ~= last then
                        last = line
                        log(line)
                    end
                end
            elseif started then
                log(string.format('local: startup ready after %.1f s', api.now() - started))
                started = nil
            end
            return check(dt)
        end
    end)()
end
