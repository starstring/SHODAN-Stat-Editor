"""Rebuild everything the local tools need for the build that is installed right now.

    python local/run_all.py            # cache -> names -> panel -> report
    python local/run_all.py --skip-panel   # only the data/typelib side

Steps, in order:

  1. local/tools/dump_plain.py   unseal data/game/*.dl_bin + dl_library.dl_typelib -> local/cache/plaintext-<build>/
  2. local/tools/typelib.py      that typelib -> local/cache/typelib-<build>.json (structure by type id)
  3. local/tools/go_names.py     FileDiver's Go structs -> local/cache/go_names.json (member names)
  3b local/tools/known_names.py  hd2-datamined's curated layouts -> local/cache/known-names.json
  3a local/tools/rawdata_names.py Darctor/Helldivers2_RawData -> local/cache/rawdata-names.json (best names)
  3c local/tools/wiki_names.py   wiki decoded dumps, names placed by value -> local/cache/wiki-names.json
  4. local/build_panel.py        src/stat_editor_offline.lua + local/panel/*.lua -> local/build/panel.lua
  5. local/tools/panel_dump.lua  run that panel headless -> local/cache/panel-<build>.tsv
  6. local/tools/field_report.py -> local/report/field-gaps-<build>.md
  7. local/tools/record_table.py -> local/report/{damage,explosion,projectile,status}-table-<build>.md/.csv

Needs `pynacl` in the venv (uv venv local/.venv && uv pip install pynacl) or a libsodium.dll, and
LuaJIT at local/third_party/LuaJIT (local/build_luajit.bat).
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
TOOLS = HERE / "tools"
PYTHON = sys.executable
LUAJIT = HERE / "third_party" / "LuaJIT" / "src" / "luajit.exe"
GAME_NOTE = Path.home() / "AppData" / "Local" / "SHODAN" / "StatEditor" / "game folder.txt"


def run(*args: str) -> None:
    print("$ " + " ".join(args))
    result = subprocess.run(args, cwd=TOOLS)
    if result.returncode != 0:
        raise SystemExit(f"failed: {' '.join(args)}")


def find_game() -> str:
    if GAME_NOTE.exists():
        text = GAME_NOTE.read_text(encoding="utf-8", errors="replace").strip()
        if text:
            candidate = Path(text) / "data" / "game"
            if candidate.is_dir():
                return str(candidate)
    for library in (Path(r"D:\SteamLibrary"), Path(r"E:\SteamLibrary"),
                    Path(r"C:\Program Files (x86)\Steam")):
        candidate = library / "steamapps" / "common" / "Helldivers 2" / "data" / "game"
        if candidate.is_dir():
            return str(candidate)
    raise SystemExit("the game was not found: pass --game <data/game folder>")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--game", help="the game's data/game folder")
    ap.add_argument("--skip-panel", action="store_true", help="only unseal + type library + names")
    args = ap.parse_args(argv)

    game = args.game or find_game()
    run(PYTHON, "dump_plain.py", "--game", str(Path(game).parent.parent))
    plaintext = sorted((HERE / "cache").glob("plaintext-*"))[-1]
    typelib = plaintext / "dl_library.dl_typelib"
    build = plaintext.name.replace("plaintext-", "")
    run(PYTHON, "typelib.py", "index", str(typelib), "--json", str(HERE / "cache" / f"typelib-{build}.json"))
    run(PYTHON, "go_names.py", "--typelib", str(typelib))
    rawdata = HERE.parent.parent / "Helldivers2_RawData" / "Data"
    if rawdata.is_dir():
        run(PYTHON, "rawdata_names.py", "--rawdata", str(rawdata))   # the community's named dumps
    else:
        print(f"  (no {rawdata}: git clone https://github.com/Darctor/Helldivers2_RawData for names)")
    modules = HERE / "cache" / "wiki-modules"
    if modules.is_dir():
        run(PYTHON, "wiki_names.py")      # places wiki names by matching real values
    else:
        print("  (no wiki modules: fetch them with 经验/hd2-datamined/tools/fetch_wiki_modules.py)")
    curated = HERE.parent.parent / "经验" / "hd2-datamined" / "tools" / "table_export.py"
    if curated.exists():
        run(PYTHON, "known_names.py", "--source", str(curated))   # merges both dictionaries
    else:
        print(f"  (no {curated}: the committed known-names.json is used)")
    if args.skip_panel:
        return 0
    run(PYTHON, str(HERE / "build_panel.py"))
    if not LUAJIT.exists():
        raise SystemExit(f"LuaJIT not built: run local/build_luajit.bat ({LUAJIT})")
    run(str(LUAJIT), "panel_dump.lua", game, str(HERE / "build" / "panel.lua"),
        str(HERE / "cache" / f"panel-{build}.tsv"))
    run(PYTHON, "field_report.py")
    run(PYTHON, "record_table.py")
    print(f"\ndone: local/report/field-gaps-{build}.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
