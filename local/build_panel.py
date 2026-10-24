"""Assemble the panel this fork runs: the project's src/stat_editor_offline.lua untouched, plus every
local/panel/*.lua spliced on at the end (sorted by name).

That is the whole merge strategy: a `git pull` only ever changes files we do not edit, so upstream
updates never conflict. The generated file is not committed (local/build/ is ignored) and is what
local/tools/panel_dump.lua and the local packager read.

    python build_panel.py                    # local/build/panel.lua  (with the test hook)
    python build_panel.py --skip-test        # local/build/panel-for-package.lua  (what ships)

`--skip-test` leaves out the `*_test.lua` parts: they only expose the panel's tables to the headless
harness (local/tools/panel_dump.lua), which a packaged build has no use for.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
UPSTREAM = HERE.parent / "src" / "stat_editor_offline.lua"
PARTS = HERE / "panel"
OUT = HERE / "build" / "panel.lua"
OUT_PACKAGE = HERE / "build" / "panel-for-package.lua"


def parts_for(skip_test: bool = False) -> list[Path]:
    found = sorted(PARTS.glob("*.lua"))
    return [part for part in found if not (skip_test and part.name.endswith("_test.lua"))]


def build(skip_test: bool = False) -> Path:
    out = OUT_PACKAGE if skip_test else OUT
    base = UPSTREAM.read_text(encoding="utf-8")
    parts = parts_for(skip_test)
    # each part is a `do ... end` block: its own locals must not stay active for the whole chunk
    # (upstream's chunk already sits near LuaJIT's 200-local limit)
    pieces = [f"-- ==== local/{part.name} (appended by local/build_panel.py) ====\ndo\n"
              + part.read_text(encoding="utf-8") + "\nend\n"
              for part in parts]
    header = (f"-- built from src/stat_editor_offline.lua + {len(parts)} local part(s) "
              f"({', '.join(p.name for p in parts) or 'none'}) -- do not edit\n")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(apply_ui_patch(header + base + chr(10) + chr(10).join(pieces)), encoding="utf-8")
    return out


def apply_ui_patch(text: str) -> str:
    """The one thing an overlay cannot do: draw. See local/patch_panel_ui.py."""
    import importlib.util
    spec = importlib.util.spec_from_file_location("patch_panel_ui", str(HERE / "patch_panel_ui.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.patch(text)


def main() -> int:
    argv = sys.argv[1:]
    skip_test = "--skip-test" in argv
    out = build(skip_test)
    parts = parts_for(skip_test)
    print(f"{out}: {out.stat().st_size} bytes, {len(UPSTREAM.read_text(encoding='utf-8').splitlines())} upstream "
          f"line(s) + {sum(len(p.read_text(encoding='utf-8').splitlines()) for p in parts)} local line(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
