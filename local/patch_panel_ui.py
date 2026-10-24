"""Draw option buttons for a row, the way the panel's own Settings page draws its choices.

Rows are drawn by one loop inside `draw`, so a row cannot look like a choice row from an overlay
(there are no drawing primitives at chunk level). This patch adds that: a row that carries
`row.sse_options` (a list of `{ value, label }`) and `row.sse_current` (a function returning the
current value) gets its value/±/R block replaced by a row of buttons, and the click on
`sse_opt:<row>:<value>` is left to the overlay that owns the row.

    python local/patch_panel_ui.py            # local/build/panel.lua, in place

`local/build_panel.py` applies it after splicing. `src/stat_editor_offline.lua` stays untouched; if
upstream rewrites the row loop, the anchors are gone and this fails loudly instead of drawing
nothing.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

# the plain value block of a row (its opening line, unique in the file)
ANCHOR_OPEN = """                else
                    text(was and ('was ' .. fmt(default, row.storage)) or '', 690, y + bh / 2 - 7, 14, DIM, 90, true)"""

PATCHED_OPEN = """                else
                    -- local patch (local/patch_panel_ui.py): a row with options draws buttons instead
                    if row.sse_options then
                        local current = row.sse_current and row.sse_current() or value
                        local count = #row.sse_options
                        local bw = math.min(150, math.floor((W - x0 - 190) / count))
                        for k, option in ipairs(row.sse_options) do
                            button('sse_opt:' .. n .. ':' .. tostring(option[1]), settings.tr(option[2]),
                                   x0 + 150 + (k - 1) * (bw + 6), y, bw, bh, true, current == option[1])
                        end
                        region('row:' .. n, x0 - 6, y - 1, 430, pitch - 1)
                    end
                    if not row.sse_options then
                    text(was and ('was ' .. fmt(default, row.storage)) or '', 690, y + bh / 2 - 7, 14, DIM, 90, true)"""

# its closing lines (the value region and the end of the value block)
ANCHOR_CLOSE = """                    region('value:' .. n, 696, y, 88, bh, ok)
                end"""

PATCHED_CLOSE = """                    region('value:' .. n, 696, y, 88, bh, ok)
                    end
                end"""


def patch(text: str) -> str:
    if "local patch (local/patch_panel_ui.py)" in text:
        return text
    if ANCHOR_OPEN not in text:
        raise SystemExit("the row drawing loop is not where this patch expects it (ANCHOR_OPEN); "
                         "re-check local/patch_panel_ui.py")
    if text.count(ANCHOR_CLOSE) != 1:
        raise SystemExit("the row drawing loop's end is not unique any more (ANCHOR_CLOSE); "
                         "re-check local/patch_panel_ui.py")
    text = text.replace(ANCHOR_OPEN, PATCHED_OPEN, 1)
    return text.replace(ANCHOR_CLOSE, PATCHED_CLOSE, 1)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--panel", help="the generated panel (default local/build/panel.lua)")
    args = ap.parse_args(argv)
    path = Path(args.panel) if args.panel else HERE / "build" / "panel.lua"
    if not path.exists():
        raise SystemExit(f"{path} does not exist: run local/build_panel.py first")
    original = path.read_text(encoding="utf-8")
    patched = patch(original)
    path.write_text(patched, encoding="utf-8")
    print(f"{path}: +{len(patched.splitlines()) - len(original.splitlines())} line(s) (option rows)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
