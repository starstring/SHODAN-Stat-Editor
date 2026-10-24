-- Checks the passive-stack conflict policy (the one thing this fork patches into the host).
--
--   luajit local/tools/test_stack.lua <data/game folder>
--
-- It finds two armor passives that share a modifier id with different values, stacks one on the
-- other under each policy, and prints the row that ends up in the target passive:
--
--   stack      -> the target's own row stays, the other is dropped
--   strongest  -> whichever value is further from "no effect" wins
--
-- Reads the game's files only (nothing is written, nothing is installed).
local game = arg[1]
if not game then
    io.stderr:write('usage: test_stack.lua <data/game folder>\n')
    os.exit(2)
end
local here = (debug.getinfo(1, 'S').source:match('^@(.*[/\\])') or './')
package.path = here .. '../build/?.lua;' .. here .. '../../offline/?.lua;' .. package.path

local ffi = require('ffi')
local D = require('hostdata')
local I = require('install')
local originals = I.originals(game)
D.load(game, originals)

if type(D.set_conflicts) ~= 'function' then
    print('FAIL: the loaded hostdata has no set_conflicts (local/build/hostdata.lua missing? run')
    print('      python local/patch_hostdata.py)')
    os.exit(3)
end

local PASSIVE = 0x63CE0FEB
local G = require('gamedata')

-- every passive's modifiers, straight from the decrypted file
local function u32(s, o)
    local a, b, c, d = s:byte(o + 1, o + 4)
    return ((d * 256 + c) * 256 + b) * 256 + a
end
local file
for _, entry in pairs(D.files) do
    for _, header in ipairs(G.headers(entry.p, entry.n)) do
        if header.type == PASSIVE then file = entry break end
    end
    if file then break end
end
if not file then print('FAIL: no passive table in these files'); os.exit(4) end

local fbuf = ffi.new('uint8_t[4]')
local function f32_at(s, o)
    ffi.copy(fbuf, s:sub(o + 1, o + 4), 4)
    return ffi.cast('float *', fbuf)[0]
end

local plain = ffi.string(file.p, file.n)      -- the decrypted passive table, as bytes
local passives = {}
for _, header in ipairs(G.headers(file.p, file.n)) do
    if header.type == PASSIVE and header.size >= 56 then
        local P = header.at + 24
        local count = u32(plain, P + 24)
        local mods = {}
        for k = 0, count - 1 do
            local at = P + 56 + k * 16
            mods[#mods + 1] = { id = u32(plain, at), type = u32(plain, at + 4), value = f32_at(plain, at + 8) }
        end
        passives[u32(plain, P)] = mods
    end
end

-- a modifier id two passives share, with different values
local function strength(typ, v)
    if typ == 2 then return (v <= 0) and math.huge or math.abs(math.log(v)) end
    return math.abs(v)
end

local by_id, pair = {}, nil
for id, mods in pairs(passives) do
    for _, m in ipairs(mods) do
        if m.id ~= 0 then
            by_id[m.id] = by_id[m.id] or {}
            table.insert(by_id[m.id], { passive = id, value = m.value, type = m.type })
        end
    end
end
for mod_id, users in pairs(by_id) do
    if #users >= 2 then
        for a = 1, #users do
            for b = a + 1, #users do
                -- the case that matters: the stacked passive is the stronger one, so 'strongest'
                -- must replace the target's own row
                if users[a].passive ~= users[b].passive
                        and strength(users[b].type, users[b].value) > strength(users[a].type, users[a].value) then
                    pair = { id = mod_id, target = users[a], source = users[b] }
                end
            end
        end
    end
    if pair then break end
end
if not pair then print('no shared modifier id between two passives: nothing to compare'); os.exit(0) end

print(string.format('modifier %08X: passive %d has %s (type %d), passive %d has %s (type %d)',
    pair.id, pair.target.passive, tostring(pair.target.value), pair.target.type,
    pair.source.passive, tostring(pair.source.value), pair.source.type))

-- what the target's block ends up with, under one policy
local function run(policy)
    D.set_conflicts(policy)
    local changes = {}
    D.stack(changes, { [pair.target.passive] = { pair.source.passive } }, function() end)
    local change = changes[1]
    if not change then return nil, 'nothing changed' end
    local out = ffi.string(change.plain, change.n)   -- the rewritten file, as bytes
    local headers = G.headers(change.plain, change.n)
    for _, header in ipairs(headers) do
        if header.type == PASSIVE then
            local P = header.at + 24
            if u32(out, P) == pair.target.passive then
                local count = u32(out, P + 24)
                local first, rows_with, total = nil, 0, count
                for k = 0, count - 1 do
                    local at = P + 56 + k * 16
                    if u32(out, at) == pair.id then
                        rows_with = rows_with + 1
                        first = first or f32_at(out, at + 8)
                    end
                end
                return first, total, rows_with
            end
        end
    end
    return nil, 'target passive not in the output'
end

local stacked, count_stack, rows_stack = run('stack')
local strongest, count_strong, rows_strong = run('strongest')
print(string.format('keep      -> first %s, %s row(s) with this id, %s modifiers on the target',
                    tostring(stacked), tostring(rows_stack), tostring(count_stack)))
print(string.format('strongest -> %s, %s row(s) with this id, %s modifiers on the target',
                    tostring(strongest), tostring(rows_strong), tostring(count_strong)))

local ok = true
if stacked ~= pair.target.value then ok = false; print('FAIL: stack did not keep the target\'s own value') end
local want = pair.target.value
if strength(pair.source.type, pair.source.value) > strength(pair.target.type, pair.target.value) then
    want = pair.source.value
end
if math.abs((strongest or 0) - want) > 1e-5 then ok = false; print('FAIL: strongest did not pick the stronger value') end
print(ok and 'PASS' or 'FAILED')
os.exit(ok and 0 or 1)
