"""Generate the host-side file this fork patches, instead of editing the upstream one.

`offline/hostdata.lua` does the install-side work (decrypt, diff, stack passives, correct hashes).
One small thing is missing for us: when a stacked passive adds a modifier the target passive already
has, the panel keeps the first and drops the other (always "stack"). Armory Forge's `conflicts =
strongest` keeps whichever value is further from "no effect" instead.

So the patch here is generated:

    python local/patch_hostdata.py            # -> local/build/hostdata.lua

and `local/package_exe.py` puts that copy into the packaged `app/` (the harness reads it too, by
preferring `local/build/?.lua` in package.path). `offline/hostdata.lua` itself stays untouched, so a
git merge from upstream never conflicts — but if upstream rewrites `append_mods` or the stacking
code, this patch refuses to apply (its anchors are gone) and says so, instead of silently doing
nothing.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent

ANCHOR_POLICY = "local PASSIVE = 0x63CE0FEB\n"

POLICY_CODE = """local PASSIVE = 0x63CE0FEB
-- local patch: what a modifier id that both sides have does. 'stack' keeps every row (the game
-- applies an id once, so the first wins); 'strongest' keeps only the value further from "no effect"
-- (Armory Forge's conflicts = strongest, with its own strength rule).
local CONFLICT = 'stack'
function M.set_conflicts(policy)
    CONFLICT = (policy == 'strongest') and 'strongest' or 'stack'
end
local function strength(typ, v)
    if typ == 2 then return (v <= 0) and math.huge or math.abs(math.log(v)) end
    return math.abs(v)
end
local f32buf = ffi.new('uint8_t[4]')
local function row_type(m)
    local a, b, c, d = m:byte(5, 8)
    return ((d * 256 + c) * 256 + b) * 256 + a
end
local function row_value(m)
    ffi.copy(f32buf, m:sub(9, 12), 4)
    return ffi.cast('float *', f32buf)[0]
end
"""

ANCHOR_APPEND = """local function append_mods(mods, add, dropped)
    local have, out = {}, { mods }
    for o = 1, #mods, 16 do have[mods:sub(o, o + 3)] = true end
    for o = 1, #add, 16 do
        local key = add:sub(o, o + 3)
        if have[key] then
            local b1, b2, b3, b4 = key:byte(1, 4)
            dropped[#dropped + 1] = string.format('%08X', ((b4 * 256 + b3) * 256 + b2) * 256 + b1)
        else
            have[key], out[#out + 1] = true, add:sub(o, o + 15)
        end
    end
    return table.concat(out)
end"""

REPLACEMENT_APPEND = """local function append_mods(mods, add, dropped)
    -- local patch: rows are kept in a list so 'strongest' can replace one, not only drop it
    local rows, at = {}, {}
    for o = 1, #mods, 16 do
        local m = mods:sub(o, o + 15)
        rows[#rows + 1] = m
        at[m:sub(1, 4)] = #rows
    end
    for o = 1, #add, 16 do
        local m = add:sub(o, o + 15)
        local key = m:sub(1, 4)
        local k = at[key]
        if not k then
            rows[#rows + 1] = m
            at[key] = #rows
        elseif CONFLICT == 'strongest' then
            -- one row per modifier id: the value further from "no effect" wins (Armory Forge's rule)
            if strength(row_type(m), row_value(m)) > strength(row_type(rows[k]), row_value(rows[k])) then
                rows[k] = m
            end
        else
            -- keep: every row is kept, duplicates included (the game applies an id once, so the first
            -- one is what counts; Armory Forge's 'stack' lists them all the same way)
            rows[#rows + 1] = m
        end
    end
    return table.concat(rows)
end"""


def patch(text: str) -> str:
    if "function M.set_conflicts" in text:
        return text                              # already patched
    if ANCHOR_POLICY not in text:
        raise SystemExit("offline/hostdata.lua: the passive-stacking anchor is gone; re-check the patch")
    text = text.replace(ANCHOR_POLICY, POLICY_CODE, 1)
    if ANCHOR_APPEND not in text:
        raise SystemExit("offline/hostdata.lua: append_mods is not the version this patch expects")
    return text.replace(ANCHOR_APPEND, REPLACEMENT_APPEND, 1)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", help="offline/hostdata.lua (default: the repo's)")
    ap.add_argument("--out", help="output (default local/build/hostdata.lua)")
    args = ap.parse_args(argv)
    source = Path(args.source) if args.source else REPO / "offline" / "hostdata.lua"
    out = Path(args.out) if args.out else HERE / "build" / "hostdata.lua"
    patched = patch(source.read_text(encoding="utf-8"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(patched, encoding="utf-8")
    print(f"{out}: +{len(patched.splitlines()) - len(source.read_text(encoding='utf-8').splitlines())} "
          f"line(s) over {source.name}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
