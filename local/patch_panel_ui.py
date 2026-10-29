"""Two things an overlay cannot do itself: draw option buttons for a row, and draw an overlay.

`draw(width, height)` builds its own nested `rect` / `text` / `button` helpers, so a row cannot look
like a choice row and no overlay can be shown from an appended overlay. This patch adds both, in the
*generated* panel only:

    python local/patch_panel_ui.py            # local/build/panel.lua, in place

1. **option rows** — a row carrying `row.sse_options` (`{ {value, label}, ... }`) and
   `row.sse_current` (a function returning the current value) has its value/±/R block replaced by a
   row of buttons, click id `sse_opt:<row>:<value>`.
2. **a preview** — a passive page's stack block gets a button (`sse_preview`), and a table in
   `state.sse_preview` (`{ title, lines = {...} }`) is drawn as an overlay above the rows, like the
   panel's own tooltips.

`src/stat_editor_offline.lua` stays untouched; if upstream rewrites either anchor, this fails loudly
instead of drawing nothing.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MARK = "local patch (local/patch_panel_ui.py)"

# ---------------------------------------------------------------- 1. option rows
ANCHOR_OPEN = """                else
                    local shown = function(v) return row.never and v == 0 and 'Never' or fmt(v, row.storage) end"""

PATCHED_OPEN = """                else
                    -- local patch (local/patch_panel_ui.py): a row with options draws buttons instead
                    if row.sse_options then
                        -- the row's own region first: hit() takes the *last* region under the cursor,
                        -- so a region registered after the buttons would swallow their clicks
                        region('row:' .. n, x0 - 6, y - 1, 430, pitch - 1)
                        local current = row.sse_current and row.sse_current() or value
                        local count = #row.sse_options
                        local bw = math.min(150, math.floor((W - x0 - 190) / count))
                        for k, option in ipairs(row.sse_options) do
                            button('sse_opt:' .. n .. ':' .. tostring(option[1]), settings.tr(option[2]),
                                   x0 + 150 + (k - 1) * (bw + 6), y, bw, bh, true, current == option[1])
                        end
                    end
                    if not row.sse_options then
                    local shown = function(v) return row.never and v == 0 and 'Never' or fmt(v, row.storage) end"""

ANCHOR_CLOSE = """                    region('row:' .. n, x0 - 6, y - 1, 430, pitch - 1)
                    region('value:' .. n, 696, y, 88, bh, ok)
                end"""

PATCHED_CLOSE = """                    region('row:' .. n, x0 - 6, y - 1, 430, pitch - 1)
                    region('value:' .. n, 696, y, 88, bh, ok)
                    end
                end"""

# ---------------------------------------------------------------- 2. the page's two buttons
ANCHOR_BUTTON = """        text(weapon.name, x0, 94, 22, GOLD, room)"""

PATCHED_BUTTON = """        text(weapon.name, x0, 94, 22, GOLD, room)
        -- local patch (local/patch_panel_ui.py): a passive page's two actions, on the name's line and
        -- only as wide as the room the name leaves (the window's title bar belongs to the host)
        if weapon.passive then
            local room = W - 20 - x0 - width(weapon.name, 22) - 24   -- (the name's own room, less a gap)
            local count = weapon.sse_page and 1 or 2
            local bw = math.min(208, math.floor((room - 8 * (count - 1)) / count))
            if bw >= 80 then
                -- short labels when the name is long: the text is clipped to the button's width
                local short = bw < 150
                local bx = W - 20 - (bw * count + 8 * (count - 1))
                if not weapon.sse_page then
                    button('sse_add_all', short and 'Add to all' or 'Add to every armor', bx, 90, bw, 28, true)
                    bx = bx + bw + 8
                end
                button('sse_preview', short and 'Preview' or 'Preview the result', bx, 90, bw, 28, true,
                       state.sse_preview ~= nil)
            end
        end"""

# ---------------------------------------------------------------- 2. the preview overlay
# ---------------------------------------------------------------- 3. the picker's list
ANCHOR_PICKER = """            local t = w.passive and tables[w.passive]"""

PATCHED_PICKER = """            -- local patch (local/patch_panel_ui.py): this fork's own pages are not passives to stack
            local t = w.passive and not w.sse_page and tables[w.passive]"""

ANCHOR_OVERLAY = """    if tip_overlay then
        local w, h = 0, #tip_overlay.lines * 18 + 16"""

PATCHED_OVERLAY = """    -- local patch (local/patch_panel_ui.py): the final stacked effects, over the rows
    if state.sse_preview then
        local preview = state.sse_preview
        local w, h = 0, #preview.lines * 19 + 52
        for _, line in ipairs(preview.lines) do w = math.max(w, width(line, 15)) end
        w = math.max(360, math.min(w + 28, W - 64))
        local x = math.max(16, math.min(96, W - 16 - w))
        local y = math.max(56, math.min(132, H - 70 - h))
        rect(x, y, w, h, color(8, 11, 15), 964)
        rect(x, y, w, 2, GOLD, 965); rect(x, y + h - 2, w, 2, GOLD, 965)
        rect(x, y, 2, h, GOLD, 965); rect(x + w - 2, y, 2, h, GOLD, 965)
        text(preview.title, x + 14, y + 10, 18, GOLD, w - 28, false, 966)
        for k, line in ipairs(preview.lines) do
            text(line, x + 14, y + 38 + (k - 1) * 19, 15, WHITE, w - 28, false, 966)
        end
        region('sse_preview_close', x, y, w, h, true)
    end
    if tip_overlay then
        local w, h = 0, #tip_overlay.lines * 18 + 16"""


def patch(text: str) -> str:
    if MARK in text:
        return text
    for name, anchor in (("ANCHOR_OPEN", ANCHOR_OPEN), ("ANCHOR_BUTTON", ANCHOR_BUTTON),
                         ("ANCHOR_PICKER", ANCHOR_PICKER), ("ANCHOR_OVERLAY", ANCHOR_OVERLAY)):
        if text.count(anchor) != 1:
            raise SystemExit(f"the row/stack drawing code is not where this patch expects it ({name}, "
                             f"{text.count(anchor)} match(es)); re-check local/patch_panel_ui.py")
    if text.count(ANCHOR_CLOSE) != 1:
        raise SystemExit("the row drawing loop's end is not unique any more (ANCHOR_CLOSE)")
    text = text.replace(ANCHOR_OPEN, PATCHED_OPEN, 1)
    text = text.replace(ANCHOR_CLOSE, PATCHED_CLOSE, 1)
    text = text.replace(ANCHOR_BUTTON, PATCHED_BUTTON, 1)
    text = text.replace(ANCHOR_PICKER, PATCHED_PICKER, 1)
    return text.replace(ANCHOR_OVERLAY, PATCHED_OVERLAY, 1)


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
    print(f"{path}: +{len(patched.splitlines()) - len(original.splitlines())} line(s) "
          f"(option rows, preview button, preview overlay)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
