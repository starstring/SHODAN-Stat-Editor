-- local overlay: fast start (offline only), after the FAST-START-PATCH that ships for v3.2.0.
--
-- The scan hub waits 120 frames before it starts, works in ~1 ms slices (a game frame has to stay
-- short), repeats passes every 0.5 s and, if a record is still missing after 180 s, sweeps all
-- memory once. Offline none of that fits: the program has already loaded every data file before the
-- scan starts, there is no game frame to protect, and a memory sweep finds the editor's own
-- temporary copies of the tables — which then look like "a table moved" and restart the scan.
--
-- So offline: start at frame 1, work in 25 ms slices, pass again almost at once, never sweep, and
-- finish after the second pass instead of looping (a table that is still missing after two passes is
-- not going to appear; the panel shows what it has).
--
-- The four tuning values are chunk-level locals of the panel, so they can be assigned here; the
-- "finish after the second pass" part hooks the scan client this panel registered.
if MOD.offline then
    START_FRAME, FRAME_BUDGET, PASS_DELAY, FALLBACK_SECONDS = 1, 0.025, 0.02, math.huge
end

;(function()
    if not MOD.offline then return end
    local hub = rawget(_G, HUB_NAME)
    if type(hub) ~= 'table' or type(hub.clients) ~= 'table' then return end
    for _, client in ipairs(hub.clients) do
        if client.name == MOD.title and type(client.after_pass) == 'function' and not client.fast_start then
            local original = client.after_pass
            client.after_pass = function(pass, final)
                -- offline, the second pass is the last one: nothing can show up later
                return original(pass, final or (pass or 0) >= 2)
            end
            client.fast_start = true
        end
    end
end)()
