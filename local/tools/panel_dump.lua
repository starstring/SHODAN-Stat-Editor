-- Headless run of Stat Editor's panel against the game's data files, for the local tools.
--
--   luajit panel_dump.lua <data/game folder> <panel .lua> <out .tsv>
--
-- The host (offline/host.lua) is a window: this does the same without one. It decrypts the game's
-- files into this process (offline/hostdata.lua), loads the panel, ticks it until every weapon is
-- resolved, and writes what the panel found as tab-separated lines:
--
--   TABLE   <kind> <stride> <rows> <copies> <name>
--   FIELD   <kind> <offset> <storage> <limit> <default> <users>
--   SAMPLE  <kind> <stride> <rows> <count> <row hex,row hex,...>   (up to 3 rows, raw)
--   WEAPON  <hash> <slot> <name>
--   ROW     <hash> <row id> <section> <label> <part,part,...>     (part = id=kind:offset:storage)
--
-- Nothing is installed: the game folder is only read.
local game, panel_path, out_path = arg[1], arg[2], arg[3]
if not (game and panel_path and out_path) then
    io.stderr:write('usage: panel_dump.lua <data/game> <panel.lua> <out.tsv>\n')
    os.exit(2)
end
local here = (debug.getinfo(1, 'S').source:match('^@(.*[/\\])') or './')
package.path = here .. '../../offline/?.lua;' .. here .. '../../offline/?/init.lua;' .. package.path

local ffi = require('ffi')
local shim = require('engine_shim')

-- ---------------------------------------------------------------- no window
shim.w, shim.h, shim.dpi = 1920, 1080, 1
shim.fill = function() end
shim.text = function() end
shim.flush = function() end
shim.present = function() end
shim.text_width = function(text, size) return #tostring(text) * (size or 16) * 0.52 end
shim.font_of = function() return 'font' end
shim.cursor = function() return 0, 0 end
shim.focused = function() return false end
shim.key_down = function() return false end
shim.sleep = function() end
shim.pump = function() end
shim.set_title = function() end
shim.message_box = function(text) io.stderr:write('message box: ' .. tostring(text):gsub('\n', ' ') .. '\n') end
shim.save_bmp = function() return nil, 'headless' end
shim.paint_guis = function() end
rawset(_G, 'stingray', shim.engine())

local function log(text) io.stderr:write('[dump] ', text, '\n') end
local G = require('gamedata')
local D = require('hostdata')
local I = require('install')

-- ---------------------------------------------------------------- the game's files, decrypted
local originals, ours, problems, count = I.originals(game)
for _, text in ipairs(problems) do log('problem: ' .. text) end
local problems2 = D.load(game, originals)
for _, text in ipairs(problems2) do log('problem: ' .. text) end
local loaded = 0
for _ in pairs(D.files) do loaded = loaded + 1 end
log(string.format('%d of %d file(s) loaded', loaded, count))
if loaded == 0 then os.exit(3) end

-- ---------------------------------------------------------------- the panel
rawset(_G, 'SHODAN_OFFLINE', true)
rawset(_G, 'SHODAN_OFFLINE_LANG', 'en')
rawset(_G, 'SHODAN_LOCAL_TEST', true)
function update(dt) end
local chunk, why = loadfile(panel_path)
if not chunk then log('could not load ' .. panel_path .. ': ' .. tostring(why)); os.exit(4) end
local ok, err = pcall(chunk)
if not ok then log('panel did not start: ' .. tostring(err)); os.exit(5) end
local state = rawget(_G, 'ShodanStatEditor')
if type(state) ~= 'table' then log('no panel state'); os.exit(6) end
local test = type(state._test) == 'table' and state._test or nil
if not test then log('the panel did not expose _test (overlay missing?)'); os.exit(7) end

-- ---------------------------------------------------------------- tick until every weapon is resolved
local deadline = os.time() + 300
local frames, last_phase = 0, nil
while os.time() < deadline do
    pcall(update, 1 / 60)
    frames = frames + 1
    if state.phase ~= last_phase then
        last_phase = state.phase
        log(string.format('phase %s at frame %d (%d weapons)', tostring(state.phase), frames, #test.weapons))
    end
    if state.phase == 'ready' and state.weapons ~= nil then break end
end
if state.phase ~= 'ready' then log('gave up waiting: phase ' .. tostring(state.phase)); os.exit(8) end
for _ = 1, 30 do pcall(update, 1 / 60) end   -- the last rows and saved values
local field_count = 0
for _ in pairs(test.fields) do field_count = field_count + 1 end
log(string.format('ready after %d frame(s): %d weapons, %d fields', frames, #test.weapons, field_count))

-- ---------------------------------------------------------------- what it found
local function clean(text)
    text = tostring(text == nil and '' or text)
    return (text:gsub('[%c\t]', ' '))
end
local function hex(id)
    if type(id) == 'number' then return string.format('%08X', id) end
    return clean(id)
end
local function hexbytes(data)
    return (data:gsub('.', function(c) return string.format('%02x', c:byte()) end))
end

-- Every row the panel knows, by payload offset: the first few are sampled, and the first one's
-- offset is what a field's offset is relative to (a keyed table's rows start after its hash map).
local function row_bases(entry, stride, limit)
    local bases = {}
    for _, offset in pairs(entry.index or {}) do
        if type(offset) == 'number' then bases[#bases + 1] = offset end
    end
    table.sort(bases)
    local out = {}
    for k = 1, math.min(limit, #bases) do out[#out + 1] = bases[k] end
    return out
end

local out = assert(io.open(out_path, 'w'))
for kind, entry in pairs(test.tables) do
    local spec = test.KINDS[entry.type or kind] or {}
    local stride = spec.stride or 0
    local rows = 0
    for _ in pairs(entry.index or {}) do rows = rows + 1 end
    local bases = row_bases(entry, stride, 1)
    local base_mod = stride > 0 and ((bases[1] or 16) % stride) or 0
    out:write('TABLE\t', hex(kind), '\t', hex(entry.type or kind), '\t', clean(stride), '\t', rows,
              '\t', clean(#(entry.copies or {})), '\t', clean(spec.name), '\t', base_mod, '\n')
end
for _, field in pairs(test.fields) do
    local default = test.default_of(field)
    out:write('FIELD\t', hex(field.kind), '\t', clean(field.offset), '\t', clean(field.storage), '\t',
              clean(field.limit), '\t', default == nil and '' or clean(string.format('%.6g', default)), '\t',
              clean(#(field.users or {})), '\n')
end
-- a few raw rows of every table: the report reads any member from these, exposed or not
for kind, entry in pairs(test.tables) do
    local spec = test.KINDS[entry.type or kind] or {}
    local stride = spec.stride or 0
    local base = entry.copies[1]
    if stride > 0 and base then
        local samples, bases = {}, row_bases(entry, stride, math.min(12, math.max(1, math.floor(200000 / stride))))
        for _, offset in ipairs(bases) do
            local data = test.bytes(base + test.HEADER_BYTES + offset, stride)
            if data then samples[#samples + 1] = hexbytes(data) end
        end
        out:write('SAMPLE\t', hex(kind), '\t', hex(entry.type or kind), '\t', stride, '\t',
                  clean(entry.entries or 0), '\t', #samples, '\t', table.concat(bases, ';'), '\t',
                  table.concat(samples, ','), '\n')
    end
end
for _, weapon in ipairs(test.weapons) do
    out:write('WEAPON\t', clean(weapon.hash), '\t', clean(weapon.slot), '\t', clean(weapon.name), '\n')
    for _, row in ipairs(weapon.rows or {}) do
        local parts = {}
        for _, p in ipairs(row.parts or {}) do
            parts[#parts + 1] = string.format('%s=%s:%d:%s', clean(p.id), hex(p.field.kind), p.field.offset,
                                             clean(p.field.storage))
        end
        out:write('ROW\t', clean(weapon.hash), '\t', clean(row.id), '\t', clean(row.section), '\t',
                  clean(row.label), '\t', table.concat(parts, ','), '\n')
    end
end
-- optional write/read-back test: a file of "hash stat-id value" lines, one per line
local sets_path = arg[4]
if sets_path then
    for line in io.lines(sets_path) do
        line = line:gsub('#.*$', '')
        local hash, id, value = line:match('^%s*(%S+)%s+(%S+)%s+([%d%.%-eE]+)')
        if hash then
            local ok, old, new, why = test.set(hash, id, tonumber(value))
            local function num(x) return x == nil and '' or clean(string.format('%.6g', x)) end
            out:write('SET\t', hash, '\t', id, '\t', tostring(ok), '\t', num(old), '\t', num(new), '\t',
                      clean(why), '\n')
        end
    end
    out:close()
    log('wrote ' .. out_path .. ' (with the write test)')
else
    out:close()
    log('wrote ' .. out_path)
end
