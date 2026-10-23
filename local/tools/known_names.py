"""Field names for whole rows, from hd2-datamined's curated layouts.

The game's own type library has no member names any more (its string table was stripped after
2024-02-23), so the pipeline relies on dictionaries. FileDiver's Go structs cover the components;
hd2-datamined's `tools/table_export.py` covers the *settings* rows that matter most here, and it
also says which 4-byte slots are floats (the type library marks every primitive as type 0).

    python known_names.py                       # -> local/cache/known-names.json
    python known_names.py --source <table_export.py>

The JSON is committed, so a fresh clone works without the hd2-datamined folder; re-run this when
that folder updates.
"""
from __future__ import annotations

import argparse
import ast
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
CACHE = REPO / "local" / "cache"
DEFAULT = REPO.parent / "经验" / "hd2-datamined" / "tools" / "table_export.py"


def literal_dict(text: str, start: int) -> dict:
    """Read the dict that starts at `start` ('{') by scanning braces, then eval it as a literal."""
    depth, index = 0, start
    while index < len(text):
        char = text[index]
        if char == "{":
            depth += 1
        elif char == "}":
            depth -= 1
            if depth == 0:
                block = text[start:index + 1]
                block = re.sub(r"#.*", "", block)
                return ast.literal_eval(block)
        index += 1
    raise ValueError("unterminated dict")


def parse(source: Path) -> dict:
    text = source.read_text(encoding="utf-8")
    tables: dict[str, dict] = {}
    for match in re.finditer(r'^\s*"([a-z0-9_]+)":\s*\{', text, re.M):
        name = match.group(1)
        try:
            body = literal_dict(text, match.end() - 1)
        except Exception:
            continue
        if "fields" in body:
            tables.setdefault(name, {})["fields"] = {int(k): v for k, v in body["fields"].items()}
    floats = {}
    for match in re.finditer(r'^\s*"?([a-z0-9_]+)"?:\s*(\[[^\]]*\]),', text, re.M):
        try:
            floats[match.group(1)] = [int(value) for value in ast.literal_eval(match.group(2))]
        except Exception:
            continue
    for name, offsets in floats.items():
        if offsets:
            tables.setdefault(name, {})["floats"] = offsets
    return {"source": str(source), "tables": tables}


# record name -> the settings table it is a row of
WIKI_TABLES = {"damage": "damage_settings", "explosion": "explosion_settings",
               "projectile": "projectile_settings", "status": "status_effect_settings",
               "beam": "beam_settings", "arc": "arc_settings"}


def merge_rawdata(data: dict, path: Path) -> dict:
    """Darctor/Helldivers2_RawData: the newest, most complete name source, by record type + offset."""
    if not path.exists():
        return data
    dump = json.loads(path.read_text(encoding="utf-8"))
    records = data.setdefault("records", {})
    for type_name, entry in dump.get("records", {}).items():
        target = records.setdefault(type_name, {"names": {}, "labels": {}})
        for offset, name in entry.get("names", {}).items():
            target["names"].setdefault(offset, name)
        for offset, table in entry.get("labels", {}).items():
            target["labels"].setdefault(offset, {}).update(table)
    data["rawdata_versions"] = dump.get("game_versions")
    return data


def merge_wiki(data: dict, path: Path) -> dict:
    """Add the names `wiki_names.py` placed by value matching (they lose to the curated layouts)."""
    if not path.exists():
        return data
    wiki = json.loads(path.read_text(encoding="utf-8"))
    for record, found in wiki.items():
        key = WIKI_TABLES.get(record)
        if not key:
            continue
        table = data["tables"].setdefault(key, {})
        fields = table.setdefault("fields", {})
        for offset, name in found.get("fields", {}).items():
            fields.setdefault(int(offset), name)
        if found.get("confidence"):
            table.setdefault("wiki_confidence", {})[record] = found["confidence"]
    return data


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", help="hd2-datamined tools/table_export.py")
    ap.add_argument("--out", help="JSON output (default local/cache/known-names.json)")
    args = ap.parse_args(argv)
    source = Path(args.source) if args.source else DEFAULT
    if not source.exists():
        raise SystemExit(f"not found: {source} (--source)")
    data = parse(source)
    data = merge_wiki(data, CACHE / "wiki-names.json")
    data = merge_rawdata(data, CACHE / "rawdata-names.json")
    out = Path(args.out) if args.out else CACHE / "known-names.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(data, indent=1), encoding="utf-8")
    for name, table in sorted(data["tables"].items()):
        print(f"  {name}: {len(table.get('fields', {}))} name(s)"
              f"{', %d float offset(s)' % len(table['floats']) if table.get('floats') else ''}")
    records = data.get("records", {})
    if records:
        total = sum(len(r.get("names", {})) for r in records.values())
        print(f"  by record type: {len(records)} type(s), {total} name(s) "
              f"(rawdata {', '.join(data.get('rawdata_versions') or ['?'])})")
    print(f"{out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
