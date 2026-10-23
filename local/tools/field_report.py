"""Which fields the game has, and which of them Stat Editor can already change.

Joins three sources, all produced by the other local tools:

  * the build's own type library  (`dump_plain.py` -> dl_library.dl_typelib, parsed by typelib.py)
  * the panel's live tables       (`panel_dump.lua` -> a headless run's TSV)
  * field names                   (FileDiver's Go structs, via go_names.py)

For every record the panel reads it lists the record's members: offset, size, type, name, the panel
rows that already edit it, and what a dozen real rows hold. Members marked `✗` are the candidates
for new stats. Tables the panel never parses are listed at the end.

    python field_report.py                 # newest cache -> local/report/field-gaps-<build>.md
    python field_report.py --panel <tsv> --typelib <file> --out <md>
"""
from __future__ import annotations

import argparse
import json
import math
import re
import struct
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
CACHE = REPO / "local" / "cache"
REPORT = REPO / "local" / "report"

SCALARS = {1: "u8", 2: "u16", 4: "u32", 8: "u64"}
# offsets hd2-datamined's notes establish (they win over FileDiver's inferred names)
KNOWN = {
    "ExplosionInfo": {0: "type", 4: "damage_row", 16: "radius_inner", 20: "radius_mid", 24: "radius_outer",
                      80: "shrapnel_count", 84: "shrapnel_projectile"},
    "ProjectileInfo": {0: "type", 28: "pellets", 32: "velocity", 40: "drag", 44: "gravity", 60: "damage_row",
                       64: "pen_slowdown", 144: "explosion_on_impact", 156: "explosion_on_expiry"},
    "DamageInfo": {0: "type", 4: "damage", 8: "durable", 12: "ap_direct", 16: "ap_slight", 20: "ap_large",
                   24: "ap_extreme", 28: "demolition", 32: "stagger", 36: "push"},
}

NOISE = re.compile(r"Sound|Audio|Event|Anim|Icon|Material|Crosshair|Node|Effect|Template|Popup|Reticle|"
                   r"Lens|Decal|Texture|Bone|Icon|Shader|Emitter|Tracer|Visual", re.I)
FLOATISH = {4, 8}


def latest(pattern: str) -> Path:
    found = sorted(CACHE.glob(pattern))
    if not found:
        raise SystemExit(f"nothing matches {CACHE / pattern}: run the tools that make it first")
    return found[-1]


# ---------------------------------------------------------------- inputs
def load_names(path: Path) -> dict[int, str]:
    sys.path.insert(0, str(HERE))
    from typelib import type_hash
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith(("//", "#")):
            continue
        out[type_hash(line)] = line
    return out


def parse_panel(path: Path) -> dict:
    panel = {"tables": [], "fields": [], "samples": {}, "weapons": {}, "rows": [], "labels": {}}
    for line in path.read_text(encoding="utf-8").splitlines():
        parts = line.split("\t")
        kind = parts[0]
        if kind == "TABLE":
            panel["tables"].append({"kind": parts[1], "type": parts[2], "stride": int(parts[3] or 0),
                                    "rows": int(parts[4] or 0), "copies": int(parts[5] or 0), "name": parts[6],
                                    "base_mod": int(parts[7] or 0) if len(parts) > 7 else 0})
        elif kind == "FIELD":
            panel["fields"].append({"kind": parts[1], "offset": int(parts[2]), "storage": parts[3],
                                    "limit": parts[4], "default": parts[5], "users": int(parts[6] or 0)})
        elif kind == "SAMPLE":
            panel["samples"][parts[1]] = {
                "type": parts[2], "stride": int(parts[3]), "rows": int(parts[4] or 0),
                "bases": [int(b) for b in parts[6].split(";") if b],
                "data": [bytes.fromhex(row) for row in parts[7].split(",") if row]}
        elif kind == "WEAPON":
            panel["weapons"][parts[1]] = {"slot": parts[2], "name": parts[3]}
        elif kind == "ROW":
            panel["rows"].append({"hash": parts[1], "id": parts[2], "section": parts[3], "label": parts[4],
                                  "parts": parts[5] if len(parts) > 5 else ""})
            for item in parts[5].split(","):
                if "=" not in item:
                    continue
                stat, at = item.split("=", 1)
                fid, offset, _storage = at.split(":")
                panel["labels"].setdefault((fid, int(offset)), []).append(stat)
    return panel


def ldd_tables(plaintext: Path, names: dict[int, str]) -> list[dict]:
    """Every LDLD block in the build's plaintext tables (the settings tables the game loads)."""
    sys.path.insert(0, str(HERE))
    from ldld import parse_ldld
    out = []
    for path in sorted(plaintext.glob("*.dl_bin")):
        try:
            groups = parse_ldld(path.read_bytes())
        except ValueError:
            continue
        for group in groups:
            out.append({"file": path.name, "type_id": group["type_id"], "name": names.get(group["type_id"]),
                        "payload": group["payload_size"], "wide": group["wide"]})
    return out


# ---------------------------------------------------------------- structure
def element_of(lib, type_id: int, stride: int | None = None) -> tuple[int | None, int | None]:
    """(element type id, its size) for a container type.

    A settings table's container has one member: the array (`size 16` = pointer + count; the rows
    are that member's own type). A component block has an index map first and the rows second.
    """
    try:
        members = lib.info(type_id)["members"]
    except Exception:
        return None, None
    if not members:
        return None, None
    # the panel's stride is the record's size: prefer the member that matches it, then the rows
    # (a component block's other member) over the index map
    if stride:
        for member in members:
            if member["size64"] == stride:
                try:
                    return member["type_id"], lib.desc(member["type_id"])[3]
                except Exception:
                    break
    rows = [m for m in members if "IndexData" not in (m["type_name"] or "")] or members
    best = max(rows, key=lambda m: m["size64"])
    try:
        return best["type_id"], lib.desc(best["type_id"])[3]
    except Exception:
        return None, None


def dedupe(members: list[dict]) -> list[dict]:
    """One member per offset: the type library lists a few offsets more than once (aliases)."""
    seen, out = set(), []
    for member in members:
        if member["offset64"] in seen:
            continue
        seen.add(member["offset64"])
        out.append(member)
    return out


def member_type(member: dict, lib) -> str:
    if member["type_name"]:
        return member["type_name"]
    if member["enum_name"]:
        return "enum"
    tid = member["type_id"]
    if tid in lib._type_index:
        return f"struct 0x{tid:08X}"
    if member["size64"] == 4:
        return "u32/f32"
    return SCALARS.get(member["size64"], f"{member['size64']}B")


def member_values(member: dict, rows: list[bytes]) -> dict:
    """What a dozen real rows hold at this member: distinct values, range, a few examples."""
    size, offset = member["size64"], member["offset64"]
    out = {"kind": "struct" if member["type_name"] else ("enum" if member["enum_name"] else "scalar"),
           "values": [], "distinct": 0, "low": None, "high": None}
    if size not in (1, 2, 4, 8):
        out["kind"] = "struct"
        return out
    if member["type_id"] != 0 and member["type_name"]:
        out["kind"] = "struct"
    numbers = []
    for row in rows:
        if offset + size > len(row):
            continue
        chunk = row[offset:offset + size]
        numbers.append(int.from_bytes(chunk, "little"))
    if not numbers:
        return out
    out["distinct"] = len(set(numbers))
    if size == 8 and member["type_id"] == 0:
        out["kind"] = "hash"
        out["values"] = [f"0x{n:016X}" for n in numbers[:2]]
        return out
    if size == 4 and member["type_id"] == 0:
        floats = [struct.unpack("<f", n.to_bytes(4, "little"))[0] for n in numbers]
        plausible = all(math.isfinite(f) and -1e7 < f < 1e7 and (f == 0 or abs(f) > 1e-20) for f in floats)
        fractional = any(math.isfinite(f) and abs(f - round(f)) > 1e-6 for f in floats)
        if plausible and fractional:
            out["kind"] = "f32"
            out["low"], out["high"] = min(floats), max(floats)
            out["values"] = [f"{f:.4g}" for f in sorted(set(floats))[:3]]
            return out
        out["low"], out["high"] = min(numbers), max(numbers)
        out["values"] = [str(n) for n in sorted(set(numbers))[:3]]
        out["kind"] = "int" if max(numbers) <= 100000 else "id"
        if plausible and max(numbers) > 100000:
            out["floats"] = [f"{f:.4g}" for f in sorted(set(floats))[:2]]
            out["kind"] = "bits"          # an integer whose bits are also a plausible float
        return out
    out["low"], out["high"] = min(numbers), max(numbers)
    out["values"] = [str(n) for n in sorted(set(numbers))[:3]]
    out["kind"] = "int" if max(numbers) <= 100000 else "id"
    return out


def show(values: dict) -> str:
    if not values["values"]:
        return ""
    text = ", ".join(values["values"])
    if values["distinct"] > len(values["values"]):
        text += " …"
    if values.get("floats"):
        text += f"  (f32: {', '.join(values['floats'])})"
    if values["low"] is not None and values["distinct"] > 1:
        text += f"  [{values['low']:.4g}..{values['high']:.4g}]" if values["kind"].startswith("f32") \
            else f"  [{values['low']}..{values['high']}]"
    return text


# ---------------------------------------------------------------- the report
def load_curated() -> dict:
    """hd2-datamined's curated settings-row names (tools/known_names.py), if they were built."""
    path = CACHE / "known-names.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))["tables"]


def load_records() -> dict:
    """Names by record type + offset (the community's per-patch dumps come first in it)."""
    path = CACHE / "known-names.json"
    if not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return {name: {int(k): v for k, v in entry.get("names", {}).items() if k.isdigit()}
            for name, entry in (data.get("records") or {}).items()}


def build_report(panel: dict, lib, names: dict[int, str], go: dict, tables: list[dict], build: str) -> str:
    lines: list[str] = []
    add = lines.append
    curated = load_curated()
    records = load_records()

    def curated_names(table_name: str | None) -> dict[int, str]:
        """'ProjectileSettings' -> the curated 'projectile_settings' layout, by record offset."""
        snake = re.sub(r"(?<!^)(?=[A-Z])", "_", table_name or "").lower()
        return {int(k): v for k, v in curated.get(snake, {}).get("fields", {}).items()}

    by_type: dict[int, dict] = {}
    for table in panel["tables"]:
        try:
            tid = int(table["type"], 16)
        except ValueError:
            continue
        entry = by_type.setdefault(tid, {"names": [], "stride": 0, "rows": 0, "base_mod": 0, "sample": None})
        if table["name"] and table["name"] not in entry["names"]:
            entry["names"].append(table["name"])
        entry["rows"] += table["rows"]
        if table["stride"]:
            entry["stride"], entry["base_mod"] = table["stride"], table["base_mod"]
    for sample in panel["samples"].values():
        try:
            tid = int(sample["type"], 16)
        except ValueError:
            continue
        by_type.setdefault(tid, {"names": [], "stride": 0, "rows": 0, "base_mod": 0})["sample"] = sample

    # fields per type, in record coordinates
    used: dict[int, dict[int, list[str]]] = {}
    for field in panel["fields"]:
        try:
            tid = int(field["kind"], 16)
        except ValueError:
            continue
        entry = by_type.get(tid)
        if not entry or not entry["stride"]:
            continue
        offset = (field["offset"] - entry["base_mod"]) % entry["stride"]
        labels = panel["labels"].get((field["kind"], field["offset"])) or []
        used.setdefault(tid, {}).setdefault(offset, []).extend(labels[:2])

    def coverage(tid: int, member: dict) -> list[str]:
        """The panel stats that edit this member (or land inside it, for arrays and structs)."""
        out = []
        for offset, labels in used.get(tid, {}).items():
            if member["offset64"] <= offset < member["offset64"] + max(member["size64"], 1):
                for label in labels:
                    if label not in out:
                        out.append(label)
        return out

    rows: list[dict] = []
    for tid, entry in by_type.items():
        element, size = element_of(lib, tid, entry["stride"])
        if not element:
            continue
        members = dedupe(lib.info(element)["members"])
        sample = entry.get("sample") or {}
        go_names = (go.get(names.get(element, ""), {}) or {}).get("names") or []
        curated_for = curated_names(names.get(tid))
        rows.append({"record_names": records.get(names.get(element) or "", {}),
                     "curated": curated_for, "known": KNOWN.get(names.get(element) or "", {}), "tid": tid, "entry": entry, "container": names.get(tid) or f"0x{tid:08X}",
                     "element": names.get(element) or f"0x{element:08X}", "record_size": size,
                     "members": members, "sample": sample, "go_names": go_names})

    scanned = {table["name"] for table in panel["tables"] if table["name"]}
    unscanned = [t for t in tables if (t["name"] or "") not in scanned]

    add(f"# Field gaps — build {build}")
    add("")
    add("`✗` = the panel cannot edit this member. Offsets are in the record; values come from up to "
        "a dozen real rows of the first table that has this record.")
    add("")
    add(f"- type library: {lib.nt} types / {lib.nm} members · panel: {len(panel['tables'])} table(s), "
        f"{len(panel['fields'])} field(s), {len(panel['weapons'])} page(s), {sum(len(r) for r in [panel['rows']])} "
        f"row(s) of stats")
    add(f"- records the panel reads: {len(rows)} · blocks in the game's files it never parses: {len(unscanned)}")
    add("")

    # ---------------------------------------------------------------- 1. candidates
    add("## 1. Candidates (not editable, scalar, and not constant)")
    add("")
    add("The likeliest new stats: numeric members of records the panel already reads, which are "
        "neither edited nor the same value on every row. `?` types are members whose type the "
        "library does not name; both readings are shown.")
    add("")
    add("| record | member | off | size | type | name | values |")
    add("|---|---|---:|---:|---|---|---|")
    candidates, ids = 0, {}
    for row in sorted(rows, key=lambda r: -len(r["members"])):
        if not any(coverage(row["tid"], m) for m in row["members"]):
            continue
        for index, member in enumerate(row["members"]):
            if coverage(row["tid"], member):
                continue
            info = member_values(member, row["sample"].get("data") or [])
            name = row["go_names"][index] if index < len(row["go_names"]) else ""
            if info["kind"] == "id":
                ids.setdefault(row["container"], 0)
                ids[row["container"]] += 1
                continue
            if info["kind"] not in ("f32", "int", "bits") or info["distinct"] < 3:
                continue
            if NOISE.search(name or "") or NOISE.search(member["type_name"] or ""):
                continue
            shown_type = member_type(member, lib)
            values = show(info)
            if info.get("floats"):
                values = f"{values}  (f32: {', '.join(info['floats'])})"
            add(f"| {row['container']} | {row['element']} | +{member['offset64']} | {member['size64']} | "
                f"{shown_type} | {name or ''} | {values} |")
            candidates += 1
    if not candidates:
        add("| — | — | | | | | |")
    add("")
    if ids:
        add("Left out (identifiers and hashes, not values): "
            + "; ".join(f"{name} {count}" for name, count in sorted(ids.items())) + ".")
        add("")

    # ---------------------------------------------------------------- 2. per record
    add("## 2. Every member of every record the panel reads")
    add("")
    for row in sorted(rows, key=lambda r: (-len(r["members"]), r["container"])):
        exposed = sum(1 for m in row["members"] if coverage(row["tid"], m))
        if not exposed:
            continue
        stride = row["entry"]["stride"]
        flag = "" if not row["record_size"] or stride == row["record_size"] else \
            f" ⚠ the panel reads {stride} B a row, the record is {row['record_size']} B"
        add(f"### {row['container']} → {row['element']} "
            f"({len(row['members'])} members, {exposed} editable, {row['entry']['rows']} rows){flag}")
        if row["entry"]["names"]:
            add("")
            add("tables: " + ", ".join(row["entry"]["names"]))
        add("")
        add("| | off | size | type | name | panel rows | values |")
        add("|---:|---:|---:|---|---|---|---|")
        for index, member in enumerate(row["members"]):
            labels = coverage(row["tid"], member)
            name = (row["record_names"].get(member["offset64"]) or row["curated"].get(member["offset64"])
                    or row["known"].get(member["offset64"])
                    or (row["go_names"][index] if index < len(row["go_names"]) else ""))
            info = member_values(member, row["sample"].get("data") or [])
            add(f"| {'✗' if not labels else ''} | +{member['offset64']} | {member['size64']} | "
                f"{member_type(member, lib)} | {name or ''} | {', '.join(labels[:3]) if labels else ''} | "
                f"{show(info)} |")
        add("")

    # ---------------------------------------------------------------- 3. unread tables
    add(f"## 3. Tables the panel never parses ({len(unscanned)})")
    add("")
    add("| file | block | container | record | record B | rows |")
    add("|---|---|---|---|---:|---:|")
    for item in sorted(unscanned, key=lambda t: (t["name"] or "", t["file"])):
        container = item["name"] or f"0x{item['type_id']:08X}"
        element, size = element_of(lib, item["type_id"])
        add(f"| {item['file']} | 0x{item['type_id']:08X} | {container} | "
            f"{names.get(element) or (f'0x{element:08X}' if element else '?')} | {size or '?'} | "
            f"{'~' + str(item['payload'] // size) if element and size else ''} |")
    add("")
    return "\n".join(lines)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--panel", help="panel dump TSV (default: newest in local/cache)")
    ap.add_argument("--typelib", help="plaintext dl_library.dl_typelib (default: newest cache)")
    ap.add_argument("--plaintext", help="plaintext tables folder (default: newest cache)")
    ap.add_argument("--names", help="dl_type_names.txt (default: local/tools/names)")
    ap.add_argument("--go-names", help="go_names.json (default: local/cache)")
    ap.add_argument("--out", help="markdown output")
    args = ap.parse_args(argv)

    sys.path.insert(0, str(HERE))
    import typelib as tl

    panel_path = Path(args.panel) if args.panel else latest("panel-*.tsv")
    typelib_path = Path(args.typelib) if args.typelib else latest("plaintext-*/dl_library.dl_typelib")
    plaintext = Path(args.plaintext) if args.plaintext else typelib_path.parent
    names_path = Path(args.names) if args.names else HERE / "names" / "dl_type_names.txt"
    go_path = Path(args.go_names) if args.go_names else CACHE / "go_names.json"

    build = plaintext.name.replace("plaintext-", "")
    panel = parse_panel(panel_path)
    lib = tl.load(str(typelib_path))
    names = load_names(names_path)
    go = json.loads(go_path.read_text(encoding="utf-8"))["types"] if go_path.exists() else {}
    tables = ldd_tables(plaintext, names)
    text = build_report(panel, lib, names, go, tables, build)

    out = Path(args.out) if args.out else REPORT / f"field-gaps-{build}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text, encoding="utf-8")
    print(f"{out}: {len(text.splitlines())} line(s) from {panel_path.name} + {typelib_path.name} "
          f"+ {go_path.name if go_path.exists() else 'no names'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
