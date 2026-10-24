-- Load the panel headless and report the first error (or the frame it becomes ready).
--   luajit local/tools/dbg_ready.lua <data/game> local/build/panel.lua
local game, panel_path = arg[1], arg[2]
package.path = 'local/build/?.lua;offline/?.lua;' .. package.path
local ffi = require('ffi')
local shim = require('engine_shim')
shim.w, shim.h, shim.dpi = 1920, 1080, 1
for _, k in ipairs({'fill','text','flush','present','paint_guis'}) do shim[k] = function() end end
shim.text_width = function(t, s) return #tostring(t) * (s or 16) * 0.52 end
shim.font_of = function() return 'font' end
shim.cursor = function() return 0, 0 end
shim.focused = function() return false end
shim.key_down = function() return false end
shim.sleep = function() end
shim.pump = function() end
shim.set_title = function() end
shim.message_box = function(t) io.stderr:write('msg: '..tostring(t)..string.char(10)) end
shim.save_bmp = function() return nil end
rawset(_G, 'stingray', shim.engine())
local G = require('gamedata'); local D = require('hostdata'); local I = require('install')
D.load(game, I.originals(game))
rawset(_G, 'SHODAN_OFFLINE', true); rawset(_G, 'SHODAN_OFFLINE_LANG', 'en'); rawset(_G, 'SHODAN_LOCAL_TEST', true)
function update(dt) end
assert(loadfile(panel_path))()
local state = rawget(_G, 'ShodanStatEditor')
for frame = 1, 200 do
  local ok, err = pcall(update, 1 / 60)
  if not ok then io.write('ERROR at frame '..frame..': '..tostring(err)..string.char(10)) os.exit(1) end
  if state.phase == 'ready' then io.write('ready at frame '..frame..string.char(10)) os.exit(0) end
end
io.write('still '..tostring(state.phase)..string.char(10))
