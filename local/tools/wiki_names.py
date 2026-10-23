"""Field names from the community wiki's decoded dumps, placed by matching real values.

The wiki's `Module:Decodedata-*` pages are hand-read dumps of these same tables, with field names
the game's own type library no longer carries. Their numbers come from other builds, so they are
used here only as a *dictionary* — and a name is placed at an offset only when the values at that
offset actually equal the wiki's values for many rows:

    python wiki_names.py                          # reads local/cache/wiki-modules
    python wiki_names.py --modules <folder> --out local/cache/wiki-names.json

Fetch the modules first (they are the wiki's content, not vendored here):

    python ../../ref/hd2-datamined/tools/fetch_wiki_modules.py --out local/cache/wiki-modules

Output (`local/cache/wiki-names.json`) is merged into `known-names.json` by `known_names.py`.
"""
from __future__ import annotations

import argparse
import json
import math
import struct
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
CACHE = REPO / "local" / "cache"

# candidate offset -> wiki key, per record; the first layout that matches the rows wins
LAYOUTS = {
    "damage": [
        {"wiki": "damage", "stride": 76, "base": 16, "keys": {4: "dmg", 8: "dmg2", 12: "ap1", 16: "ap2",
                                                             20: "ap3", 24: "ap4", 28: "demo", 32: "stun",
                                                             36: "push", 40: "param1"}},
    ],
    "explosion": [
        {"wiki": "explosion", "keys": {16: "r1", 20: "r2", 24: "r3"}},
    ],
    "projectile": [
        {"wiki": "projectile", "keys": {24: "caliber", 28: "pellets", 32: "velocity", 36: "mass", 40: "drag",
                                        44: "gravity", 52: "lifetime", 56: "liferandom", 64: "penslow",
                                        136: "xangle", 148: "xproximity", 152: "xdelay", 156: "xdelayid"}},
    ],
    "status": [
        {"wiki": "status_effect", "keys": {36: "strength", 40: "duration"}},
        {"wiki": "status_effect", "keys": {40: "strength", 36: "duration"}},
    ],
    "beam": [
        {"wiki": "beam", "keys": {8: "range"}},
    ],
    "arc": [
        # spread range / chain angle / aim angle all collide with other offsets in the value test
        # (the wiki's own arc rows repeat the same numbers), so only what is unambiguous is taken
        {"wiki": "arc", "keys": {4: "velocity"}},
    ],
}

RECORD_TYPES = {"damage": "DamageSettings", "explosion": "ExplosionSettings",
                "projectile": "ProjectileSettings", "status": "StatusEffectSettings",
                "beam": "BeamSettings", "arc": "ArcSettings"}


def load_modules(folder: Path) -> dict[str, dict]:
    """Every section of every module, merged by section name (later files win per key)."""
    sections: dict[str, dict] = {}
    for path in sorted(folder.glob("*.raw")):
        try:
            data = json.loads(path.read_text(encoding="utf-8", errors="replace"))
        except json.JSONDecodeError:
            continue
        if not isinstance(data, dict):
            continue
        for name, block in data.items():
            if not isinstance(block, (dict, list)):
                continue
            store = sections.setdefault(name, {})
            items = block.items() if isinstance(block, dict) else enumerate(block)
            for key, entry in items:
                if isinstance(entry, dict):
                    store[str(key)] = entry
    return sections


def rows_of(plaintext: Path, typelib, type_name: str, base: int = 0) -> list[bytes]:
    from ldld import parse_ldld
    type_id = typelib.type_hash(type_name)
    for path in sorted(plaintext.glob("*.dl_bin")):
        try:
            groups = parse_ldld(path.read_bytes())
        except ValueError:
            continue
        for group in groups:
            if group["type_id"] != type_id:
                continue
            members = typelib_owner.members_of(group["type_id"])
            if not members:
                return []
            size = members
            blob = path.read_bytes()[group["payload_offset"]:group["payload_offset"] + group["payload_size"]]
            return [blob[base + r * size: base + (r + 1) * size] for r in range((len(blob) - base) // size)]
    return []


class Owner:
    """Small adapter so `rows_of` can ask the type library for a record's row size."""

    def __init__(self, lib):
        self.lib = lib

    def members_of(self, type_id: int) -> int:
        members = self.lib.info(type_id)["members"]
        if not members:
            return 0
        rows = [m for m in members if "IndexData" not in (m["type_name"] or "")] or members
        return self.lib.desc(max(rows, key=lambda m: m["size64"])["type_id"])[3]


typelib_owner: Owner | None = None


def read_number(row: bytes, offset: int) -> object:
    if offset + 4 > len(row):
        return None
    raw = row[offset:offset + 4]
    as_int = int.from_bytes(raw, "little")
    as_float = struct.unpack("<f", raw)[0]
    if as_int == 0:
        return 0
    # a "tidy" float (0.5, 27.0, 100.0) is reported as one; anything else is the integer it reads as
    if (math.isfinite(as_float) and 1e-4 <= abs(as_float) < 1e6
            and abs(as_float - round(as_float, 4)) < 1e-4):
        return round(as_float, 4)
    return as_int


def same(a, b) -> bool:
    if isinstance(a, float) or isinstance(b, float):
        try:
            return abs(float(a) - float(b)) < 0.05
        except (TypeError, ValueError):
            return False
    return a == b


def score(layout: dict, rows: list[bytes], wiki: dict) -> tuple[int, int]:
    """(rows that match a wiki entry, rows that could be judged at all).

    A row only counts when the wiki has a non-zero value to compare with: matching "0 == 0" on
    every field of every row would make any offset look perfect.
    """
    keys = layout["keys"]
    wanted = []
    for entry in wiki.values():
        values = [entry.get(name) for name in keys.values()]
        if any(value not in (None, 0, 0.0) for value in values):
            wanted.append(values)
    if not wanted:
        return 0, 0
    matched = tried = 0
    for row in rows:
        values = [read_number(row, offset) for offset in keys]
        if all(value in (None, 0) for value in values):
            continue
        tried += 1
        for candidate in wanted:
            if all(same(a, b) for a, b in zip(values, candidate) if b not in (None, 0, 0.0)):
                matched += 1
                break
    return matched, tried


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--modules", help="folder of fetched wiki modules (default local/cache/wiki-modules)")
    ap.add_argument("--panel", help="panel dump TSV (for the base offset of each table)")
    ap.add_argument("--typelib", help="plaintext typelib")
    ap.add_argument("--plaintext", help="plaintext tables")
    ap.add_argument("--out", help="JSON output (default local/cache/wiki-names.json)")
    args = ap.parse_args(argv)

    sys.path.insert(0, str(HERE))
    import typelib as tl
    from record_table import find_group, element_of  # shared readers

    modules_dir = Path(args.modules) if args.modules else CACHE / "wiki-modules"
    if not modules_dir.is_dir():
        raise SystemExit(f"no wiki modules in {modules_dir}: fetch them first (see the docstring)")
    panel_path = Path(args.panel) if args.panel else sorted(CACHE.glob("panel-*.tsv"))[-1]
    typelib_path = Path(args.typelib) if args.typelib else sorted(CACHE.glob("plaintext-*/dl_library.dl_typelib"))[-1]
    plaintext = Path(args.plaintext) if args.plaintext else typelib_path.parent
    lib = tl.load(str(typelib_path))
    sections = load_modules(modules_dir)

    # the panel knows each table's row start (a keyed table's rows come after its hash map)
    import field_report as fr
    panel = fr.parse_panel(panel_path)
    bases = {}
    for table in panel["tables"]:
        try:
            bases[int(table["type"], 16)] = table["base_mod"]
        except ValueError:
            continue

    result: dict[str, dict] = {}
    for record, layouts in LAYOUTS.items():
        type_name = RECORD_TYPES[record]
        type_id = tl.type_hash(type_name)
        group = find_group(plaintext, type_id)
        if not group:
            print(f"{record}: no table", file=sys.stderr)
            continue
        path, payload, size = group
        element = element_of(lib, type_id, None)
        stride = lib.desc(element)[3]
        base = bases.get(type_id, 0)
        rows = [payload[base + r * stride: base + (r + 1) * stride]
                for r in range((len(payload) - base) // stride)]
        wiki = sections.get(layouts[0]["wiki"], {})
        if not wiki:
            print(f"{record}: no '{layouts[0]['wiki']}' section in the modules", file=sys.stderr)
            continue
        best = None
        for layout in layouts:
            matched, tried = score(layout, rows, wiki)
            if tried and matched * 2 >= tried and (best is None or matched > best[1]):
                best = (layout, matched, tried)
        if not best:
            print(f"{record}: no layout matched enough rows", file=sys.stderr)
            continue
        layout, matched, tried = best
        result[record] = {"fields": {str(offset): name for offset, name in layout["keys"].items()},
                          "matched_rows": matched, "rows": tried,
                          "confidence": round(matched / tried, 3) if tried else 0}
        print(f"{record}: {len(layout['keys'])} name(s), {matched}/{tried} rows matched "
              f"({result[record]['confidence']:.0%})")

    out = Path(args.out) if args.out else CACHE / "wiki-names.json"
    out.write_text(json.dumps(result, indent=1), encoding="utf-8")
    print(out)
    return 0


if __name__ == "__main__":
    sys.exit(main())
