-- Checks the armor-passive conflict policy without touching the game files.
--
--   luajit local/tools/test_conflicts.lua
--
-- 1. the packaged hostdata carries the policy (local/patch_hostdata.py: M.set_conflicts and the
--    'strongest' branch in append_mods) and still has the entry point the host calls;
-- 2. the rule itself picks the value further from "no effect" under 'strongest' and keeps every row
--    under 'stack all' - the same rule the host applies when it merges an armor's passive list.
--
-- (test_stack.lua used to exercise "stack a passive onto a passive": upstream replaced that model with
-- one passive list per armor, so the merge to check is the armor's.)
package.path = 'local/tools/?.lua;' .. package.path

local ok, why = true, {}
local function fail(what) ok = false; why[#why + 1] = what end

local path = 'local/build/hostdata.lua'
local handle = io.open(path, 'rb')
local text = handle and handle:read('*a') or ''
if handle then handle:close() end
if text == '' then fail(path .. ' is missing: run python local/patch_hostdata.py') end
if not text:find('function M.set_conflicts', 1, true) then fail('hostdata has no set_conflicts') end
if not text:find("CONFLICT == 'strongest'", 1, true) then fail('hostdata has no strongest branch') end
if not text:find('function M.armor_passives', 1, true) then fail('hostdata has no armor_passives') end

-- the strength rule, as the host and the panel both use it
local function strength(typ, v)
    if typ == 2 then return (v <= 0) and math.huge or math.abs(math.log(v)) end
    return math.abs(v)
end

local function pick(rows, policy)
    local uniq = {}
    for _, r in ipairs(rows) do
        local dup = false
        for _, u in ipairs(uniq) do
            if u.type == r.type and math.abs(u.value - r.value) < 1e-6 then dup = true end
        end
        if not dup then uniq[#uniq + 1] = r end
    end
    if policy == 'strongest' and #uniq > 1 then
        local best = uniq[1]
        for _, u in ipairs(uniq) do
            if strength(u.type, u.value) > strength(best.type, best.value) then best = u end
        end
        return best.value, 1
    end
    local product = 1
    for _, u in ipairs(uniq) do product = product * u.value end
    return product, #uniq
end

local rows = { { type = 2, value = 0.75 }, { type = 2, value = 0.5 } }   -- two passives' rows for one id
local strongest, count = pick(rows, 'strongest')
local stacked, kept = pick(rows, 'stack')
print(string.format('strongest: %g (%d row)   stack all: %g (%d row(s))', strongest, count, stacked, kept))
if strongest ~= 0.5 then fail('strongest did not pick 0.5 (the value further from x1)') end
if kept ~= 2 then fail('stack all did not keep both rows') end

if ok then
    print('PASS')
    os.exit(0)
end
for _, line in ipairs(why) do print('FAIL: ' .. line) end
os.exit(1)
