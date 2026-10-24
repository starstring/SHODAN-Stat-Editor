"""Draw the two passive-stack toggles in the generated panel (the one place an overlay cannot reach).

`draw(width, height)` builds its own `rect` / `text` / `button` helpers as nested functions, so an
appended overlay has no way to draw anything: it can only add clickable regions. The two toggles
(Conflicts / Every armor) therefore get two `button(...)` calls inserted next to the stack dialog's
Cancel button — in the *generated* panel only:

    python local/patch_panel_ui.py            # local/build/panel.lua, in place

`local/build_panel.py` runs this after splicing the overlays. `src/stat_editor_offline.lua` stays
untouched; if upstream moves that dialog, the anchor is not found and this fails loudly instead of
silently dropping the buttons. The click handling lives in the overlay (local/panel/55_...).
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent

ANCHOR = """        button('stack_cancel', 'Cancel', x + w - 16 - 104, y + h - 16 - 30, 104, 30, true, false, nil, 961)"""

ADDED = ANCHOR + """
        -- local patch (local/patch_panel_ui.py): the two stack toggles, drawn with Cancel
        if state.sse_cfg then
            local cfg, by = state.sse_cfg, y + h - 16 - 30
            button('pconf', 'Conflicts: ' .. cfg.conflicts, x + 16, by, 150, 30, true, false, nil, 961)
            button('pevery', cfg.every and ('Every armor: ' .. #cfg.every) or 'Every armor: off',
                   x + 16 + 158, by, 170, 30, true, false, nil, 961)
        end"""


def patch(text: str) -> str:
    if "local patch (local/patch_panel_ui.py)" in text:
        return text
    if ANCHOR not in text:
        raise SystemExit("the stack dialog's Cancel button is not where this patch expects it; "
                         "re-check local/patch_panel_ui.py")
    return text.replace(ANCHOR, ADDED, 1)


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
          f"(the stack dialog's two toggles)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
