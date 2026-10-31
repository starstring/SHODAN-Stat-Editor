-- Draw every page of the panel headless and report the ones that fail.
--
--   luajit local/tools/draw_all.lua <data/game> local/build/panel.lua
--
-- Resolving a page and drawing it are different code paths, and a page can resolve fine and still break
-- drawing (a passive index without its `lines`, a row whose options are malformed...). The panel's own
-- draw error handler closes the editor after five errors in a row, which is what an empty window with
-- the host's chrome around it looks like - so every page is drawn here once.
--
-- Exits 1 when any page fails, naming the page and the error.
local game, panel_path = arg[1], arg[2]
if not (game and panel_path) then
    io.stderr:write('usage: draw_all.lua <data/game> <panel.lua>\n')
    os.exit(2)
end
local here = (debug.getinfo(1, 'S').source:match('^@(.*[/\\])') or './')
package.path = here .. '../build/?.lua;' .. here .. '../../offline/?.lua;' ..
                here .. '../../offline/?/init.lua;' .. package.path

local ffi = require('ffi')
local shim = require('engine_shim')
shim.w, shim.h, shim.dpi = 1280, 720, 1
for _, name in ipairs({ 'fill', 'text', 'flush', 'present', 'paint_guis' }) do shim[name] = function() end end
shim.text_width = function(text, size) return #tostring(text) * (size or 16) * 0.52 end
shim.font_of = function() return 'font' end
shim.cursor = function() return 0, 0 end
shim.focused = function() return false end
shim.key_down = function() return false end
shim.sleep = function() end
shim.pump = function() end
shim.set_title = function() end
shim.message_box = function(text) io.stderr:write('message box: ' .. tostring(text) .. '\n') end
shim.save_bmp = function() return nil end
rawset(_G, 'stingray', shim.engine())

local G = require('gamedata')
local D = require('hostdata')
local I = require('install')
D.load(game, I.originals(game))
rawset(_G, 'SHODAN_OFFLINE', true)
rawset(_G, 'SHODAN_LOCAL_TEST', true)          -- (the panel only exposes _test then)
if rawget(_G, 'SHODAN_OFFLINE_LANG') == nil then rawset(_G, 'SHODAN_OFFLINE_LANG', 'en') end
-- (SHODAN_PHYSICS stays absent: it needs a real `base` address from the host, and a fake one makes every
-- structure page fail for the wrong reason. What it hides - MOD.rename.of walking a passive's `lines` -
-- is checked directly below.)
function update(dt) end
assert(loadfile(panel_path))()

local state = rawget(_G, 'ShodanStatEditor')
local test = state and state._test
if not test then
    io.stderr:write('the panel did not expose _test (this is the packaged panel: use local/build/panel.lua)\n')
    os.exit(2)
end
test.no_save = true

local deadline = os.time() + 60
while os.time() < deadline and state.phase ~= 'ready' do pcall(update, 1 / 60) end
if state.phase ~= 'ready' then
    io.stderr:write('the panel did not become ready (phase ' .. tostring(state.phase) .. ')\n')
    os.exit(1)
end

-- the panel builds an armor page's rename boxes from `tables[page.passive].index`: it reads `.lines`
-- (the passive's description text ids) and `.mods`/`.stats`, so a synthetic passive index without them
-- draws fine in a harness that lacks SHODAN_PHYSICS and breaks in the real app
local shape = {}
for _, page in ipairs(test.weapons) do
    if page.passive and not test.tables[page.passive] then
        shape[#shape + 1] = { name = page.name, why = 'no table for its passive key ' .. tostring(page.passive) }
    elseif page.passive then
        local index = test.tables[page.passive].index or {}
        for _, field in ipairs({ 'mods', 'stats', 'lines' }) do
            if type(index[field]) ~= 'table' then
                shape[#shape + 1] = { name = page.name, why = 'its passive index has no ' .. field }
            end
        end
    end
end
for _, entry in ipairs(shape) do
    print(string.format('  FAIL %s: %s', tostring(entry.name), entry.why))
end

local failed, drawn = {}, 0
for _, page in ipairs(test.weapons) do
    local ok, why = pcall(function()
        test.resolve(page)
        test.select_weapon(page)
        test.draw(1280, 720)
    end)
    drawn = drawn + 1
    if not ok then failed[#failed + 1] = { name = page.name, why = tostring(why) } end
end
print(string.format('drew %d page(s), %d failed, %d passive index problem(s)', drawn, #failed, #shape))
for _, entry in ipairs(failed) do
    print(string.format('  FAIL %s: %s', tostring(entry.name), entry.why))
end
os.exit((#failed + #shape) == 0 and 0 or 1)
