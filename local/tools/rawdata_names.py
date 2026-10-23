"""Field names from Darctor/Helldivers2_RawData: the community's per-patch, fully named dumps.

That project exports the game's settings tables and entity components from live memory (with the
build's own typelib geometry), so its JSON keeps the original member names where they are known and
writes `unk_<kind>_0x<offset>` where they are not. This tool turns those dumps into a name table we
can use directly:

    names   record type -> {our offset: name}      (members, including nested structs: "a.b")
    labels  record type -> {our offset: {value: label}}   (every "12 <=> StatusEffectType_Gas" seen)

The dumps come from a *nearby* build (its headers say which), so a name is placed on our member only
when the two walk in the same order and the member's size fits the JSON value's kind. Their
`unk_.._0xNNNN` annotations are treated as a cross-check, never as the source of the offset: our
offset always comes from our own typelib.

    python rawdata_names.py                       # -> local/cache/rawdata-names.json
    python rawdata_names.py --rawdata <Data dir> --typelib <file>
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
CACHE = REPO / "local" / "cache"

# their file -> the typelib type whose record it holds; resolved through the wrapper when possible
SETTINGS_FILES = "settings/generated_*.json"
ENTITY_FILES = "entities/*.json"

# `type` is a real member in the settings tables (the record's own enum at +0): keep it
SKIP_KEYS = {"index", "hash", "name", "name_zh", "_metadata"}
META_KEYS = {"struct_size", "omitted_size", "exported_entity_count", "exported_type_count",
             "matched_bilingual_hash_count", "patch_date", "game_version"}

# a value in their JSON that is a number, string, list or nested object
def kind_of(value) -> str:
    if isinstance(value, bool):
        return "bool"
    if isinstance(value, int):
        # a 64-bit value printed as a number is a hash (their JSON keeps floats as floats)
        return "hash" if value > 0xFFFFFFFF or value < -0x80000000 else "number"
    if isinstance(value, float):
        return "number"
    if isinstance(value, str):
        if " <=> " in value:
            return "label"
        if re.fullmatch(r"-?\d+", value):
            # their JSON keeps 64-bit values as decimal strings so nothing is lost
            return "hash" if abs(int(value)) > 0xFFFFFFFF else "number"
        return "str"
    if isinstance(value, list):
        return "list"
    if isinstance(value, dict):
        return "dict"
    return "other"


SIZE_OF_KIND = {"bool": {1, 4}, "number": {1, 2, 4}, "label": {1, 2, 4}, "str": {4, 8},
                "hash": {4, 8}, "list": {16, 24}, "dict": None, "other": None}


def label_of(value) -> tuple[int, str] | None:
    """'12 <=> StatusEffectType_Gas' -> (12, 'StatusEffectType_Gas')."""
    if not isinstance(value, str):
        return None
    found = re.match(r"^(-?\d+)\s*<=\>\s*(.+)$", value)
    if not found:
        return None
    return int(found.group(1)), found.group(2).strip()


def list_shape(values: list) -> tuple[str, int | None]:
    """('scalars', n) for an inline array, ('objects', n) for a pointer array."""
    flat = [v for value in values if isinstance(value, list) for v in value]
    if flat and all(not isinstance(v, (dict, list)) for v in flat):
        return "scalars", len(values[0])
    return "objects", None


def their_fields(items: list[dict]) -> list[dict]:
    """The fields of one record, in struct order, skipping the `_detail` annotations of bitfields."""
    order: list[str] = []
    sample: dict = {}
    for item in items:
        if not isinstance(item, dict):
            continue
        for key, value in item.items():
            if key in SKIP_KEYS or key in META_KEYS or key.endswith("_detail"):
                continue
            if key not in sample:
                order.append(key)
                sample[key] = value
    fields = []
    for key in order:
        kind = kind_of(sample[key])
        extra = {}
        if kind == "list":
            extra["shape"], extra["length"] = list_shape([v for v in
                                                          (item.get(key) for item in items)
                                                          if isinstance(v, list)])
        fields.append({"name": key, "kind": kind, "offset_hint": offset_hint(key), **extra})
    return fields


def offset_hint(name: str) -> int | None:
    """`unk_bool_0x004C` / `unk_float_r0x000C` carry the offset the exporter used."""
    found = re.search(r"0x([0-9A-Fa-f]{3,4})$", name)
    return int(found.group(1), 16) if found else None


def compatible(member: dict, field: dict) -> int:
    """How well our member can be this field: 3 exact, 1 possible, -2 no.

    Sizes are what keeps the walk honest: a 4-byte float must not land on an 8-byte hash, and a
    list of four numbers is an inline array of 16 bytes in the record.
    """
    kind = field["kind"]
    if kind == "dict":
        return 3 if member["struct"] else -2
    if member["struct"]:
        return -2
    if kind == "list":
        if field.get("shape") == "scalars" and field.get("length"):
            return 3 if member["size64"] == 4 * field["length"] else -2
        return 3 if member["size64"] in (16, 24) else -2
    if kind in ("str", "hash"):
        return 3 if member["size64"] == 8 else (2 if member["size64"] == 4 else -2)
    if kind in ("number", "label", "bool"):
        if member["size64"] == 4:
            return 3
        if member["size64"] in (1, 2):
            return 2
        return -2
    return 1


def align(fields: list[dict], members: list[dict]) -> list[tuple[int, int] | None]:
    """Order-preserving alignment (Needleman-Wunsch), returning the member index per field."""
    n, m = len(fields), len(members)
    MATCH, GAP = 0, -2
    score = [[0] * (m + 1) for _ in range(n + 1)]
    move = [[""] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        score[i][0], move[i][0] = GAP * i, "up"
    for j in range(1, m + 1):
        score[0][j], move[0][j] = GAP * j, "left"
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            field, member = fields[i - 1], members[j - 1]
            weight = compatible(member, field)
            if weight > 0:
                # their `unk_.._0xNNNN` annotations name the offset the exporter used: when it
                # agrees with ours the pair is very likely right, when it disagrees it is not
                hint = field.get("offset_hint")
                if hint is not None:
                    weight += 6 if hint == member["offset64"] else -4
                # ties go to the walk that keeps fields and members level (no silent shifts)
                weight += 0.01 * (1.0 - abs(i - j) / max(n, m, 1))
            best = (score[i - 1][j - 1] + weight, "diag")
            if score[i - 1][j] + GAP > best[0]:
                best = (score[i - 1][j] + GAP, "up")
            if score[i][j - 1] + GAP > best[0]:
                best = (score[i][j - 1] + GAP, "left")
            score[i][j], move[i][j] = best
    pairs: list[tuple[int, int] | None] = [None] * n
    i, j = n, m
    while i > 0 and j > 0:
        step = move[i][j]
        if step == "diag" and compatible(members[j - 1], fields[i - 1]) > 0:
            pairs[i - 1] = (i - 1, j - 1)
            i, j = i - 1, j - 1
        elif step == "up":
            i -= 1
        else:
            j -= 1
    return pairs


def members_of(lib, type_id: int) -> list[dict]:
    """Our record's members in order, with the bits the alignment needs."""
    seen, out = set(), []
    for member in lib.info(type_id)["members"]:
        if member["offset64"] in seen:
            continue
        seen.add(member["offset64"])
        struct = False
        try:
            struct = bool(lib.info(member["type_id"])["member_count"]) and member["size64"] > 4
        except Exception:
            struct = False
        out.append({"offset64": member["offset64"], "size64": member["size64"], "struct": struct,
                    "type_id": member["type_id"], "name": member["type_name"]})
    return out


def clean_name(name: str) -> str | None:
    """Their key as a usable name; None when it says 'unknown'."""
    if re.fullmatch(r"0x[0-9A-Fa-f]{8}", name):
        return None
    if name.startswith("unk_"):
        return None
    return name


def collect(lib, type_id: int, items: list[dict], prefix: str, names: dict, labels: dict,
            depth: int = 0) -> tuple[int, int, list[str]]:
    """Match one record's fields to our members, recursing into nested structs."""
    fields = their_fields(items)
    members = members_of(lib, type_id)
    pairs = align(fields, members)
    matched = 0
    unmatched = []
    for slot in pairs:
        if slot is None:
            continue
        field, member = fields[slot[0]], members[slot[1]]
        matched += 1
        name = clean_name(field["name"])
        if name:
            names[f"{prefix}{member['offset64']}"] = name
        # every sample of this field, so a value -> label map comes out of it
        samples = []
        for item in items:
            value = item.get(field["name"])
            if value is not None:
                samples.append(value)
        seen = {}
        for value in samples:
            got = label_of(value)
            if got:
                seen[got[0]] = got[1]
        if seen:
            labels.setdefault(f"{prefix}{member['offset64']}", {}).update(seen)
        # nested struct: their dict keys are our struct member's members
        if field["kind"] == "dict" and member["struct"] and depth < 3:
            nested_items = [v for v in samples if isinstance(v, dict)]
            if nested_items:
                collect(lib, member["type_id"], nested_items, f"{prefix}{member['offset64']}.",
                        names, labels, depth + 1)
    for index, slot in enumerate(pairs):
        if slot is None:
            unmatched.append(fields[index]["name"])
    return matched, len(fields), unmatched


def unwrap(lib, type_id: int) -> int:
    """Follow wrappers (index map + array, or a lone array member) down to the record itself."""
    for _ in range(4):
        members = members_of(lib, type_id)
        if len(members) > 2 and not all(m["struct"] and m["size64"] in (16, 24) for m in members):
            return type_id
        if not members:
            return type_id
        rows = [m for m in members if "IndexData" not in (m["name"] or "")] or members
        best = max(rows, key=lambda m: m["size64"])
        if best["type_id"] == type_id:
            return type_id
        try:
            inner = lib.info(best["type_id"])
        except Exception:
            return type_id
        if not inner["member_count"]:
            return type_id
        type_id = best["type_id"]
    return type_id


def record_type_of(lib, type_name: str, names: dict[int, str]) -> tuple[int, str] | None:
    """The record a table/component type holds: <X>Settings or <X>ComponentData -> its rows' type."""
    try:
        tid = lib.type_id_of(type_name)
    except Exception:
        return None
    record = unwrap(lib, tid)
    if record == tid and len(members_of(lib, tid)) <= 1:
        return None
    return record, (names.get(record) or f"0x{record:08X}")


def load_items(path: Path) -> tuple[str, int, list[dict], dict]:
    """(wrapper type name, record type id, the records, the file's metadata)."""
    data = json.loads(path.read_text(encoding="utf-8", errors="replace"))
    meta: dict = {}
    if isinstance(data, list):                      # settings: [ {table: {...}}, ... ]
        for chunk in data:
            for table, body in chunk.items():
                if isinstance(body, dict) and "items" in body:
                    meta = body.get("_metadata") or {}
                    return table, 0, body["items"], meta
        raise ValueError("no items")
    if isinstance(data, dict) and "entities" in data:
        meta = data.get("_metadata") or {}
        items = []
        for entry in data["entities"]:
            if isinstance(entry, dict) and len(entry) == 1:
                body = next(iter(entry.values()))
                if isinstance(body, dict):
                    items.append(body)
        return path.name.replace(".json", ""), 0, items, meta
    raise ValueError("unrecognised layout")


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--rawdata", help="the cloned repo's Data folder")
    ap.add_argument("--typelib", help="plaintext dl_library.dl_typelib (default: newest cache)")
    ap.add_argument("--out", help="JSON output (default local/cache/rawdata-names.json)")
    args = ap.parse_args(argv)

    sys.path.insert(0, str(HERE))
    import typelib as tl

    rawdata = Path(args.rawdata) if args.rawdata else REPO.parent / "Helldivers2_RawData" / "Data"
    if not rawdata.is_dir():
        raise SystemExit(f"not found: {rawdata} (clone Darctor/Helldivers2_RawData, or pass --rawdata)")
    typelib_path = Path(args.typelib) if args.typelib else sorted(CACHE.glob("plaintext-*/dl_library.dl_typelib"))[-1]
    lib = tl.load(str(typelib_path))

    names_map: dict[int, str] = {}
    for line in (HERE / "names" / "dl_type_names.txt").read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith(("//", "#")):
            names_map[tl.type_hash(line)] = line

    records: dict[str, dict] = {}
    versions = set()
    files = sorted(rawdata.glob(SETTINGS_FILES)) + sorted(rawdata.glob(ENTITY_FILES))
    for path in files:
        try:
            wrapper, _ignored, items, meta = load_items(path)
        except Exception:
            continue
        if not items:
            continue
        resolved = record_type_of(lib, wrapper, names_map)
        if not resolved:
            continue
        type_id, type_name = resolved
        names, labels = {}, {}
        matched, total, unmatched = collect(lib, type_id, items, "", names, labels)
        if not names:
            continue
        entry = records.setdefault(type_name, {"names": {}, "labels": {}, "files": [],
                                               "matched": 0, "fields": 0, "unmatched": []})
        entry["names"].update(names)
        for offset, table in labels.items():
            entry["labels"].setdefault(offset, {}).update(table)
        entry["files"].append(path.name)
        entry["matched"] += matched
        entry["fields"] += total
        entry["unmatched"] += unmatched[:6]
        if meta.get("game_version"):
            versions.add(str(meta["game_version"]))

    out = Path(args.out) if args.out else CACHE / "rawdata-names.json"
    payload = {"source": str(rawdata), "game_versions": sorted(versions),
               "typelib": typelib_path.name, "records": records}
    out.write_text(json.dumps(payload, indent=1, ensure_ascii=False), encoding="utf-8")

    total_names = sum(len(r["names"]) for r in records.values())
    print(f"{out}: {len(records)} record type(s), {total_names} name(s) placed "
          f"from {len(files)} file(s), game version(s) {', '.join(sorted(versions)) or '?'}")
    for name, entry in sorted(records.items(), key=lambda kv: -len(kv[1]["names"]))[:14]:
        print(f"  {name:34s} {len(entry['names']):4d} names  ({entry['matched']}/{entry['fields']} fields")
    return 0


if __name__ == "__main__":
    sys.exit(main())
