"""One table per settings record: every row's id and every member's value.

Answers "what are the damage / explosion / projectile / status rows, what do they hold, and who
uses them" straight from the build's own files:

    python record_table.py                       # damage, explosion, projectile, status
    python record_table.py --records damage,explosion
    python record_table.py --records projectile --min-diff 1

Writes, per record, `local/report/<record>-table-<build>.md` (one line per id, readable) and
`.csv` (every member, one column each). Names come from, in order: the panel's own stat labels
(so what you see here is what the panel calls it), FileDiver's Go structs, and a small dictionary of
offsets established in hd2-datamined's notes for rows the panel does not edit.
"""
from __future__ import annotations

import argparse
import csv
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

# records this tool knows how to find, by the LDLD type id of their table
RECORDS = {
    "damage": "DamageSettings",
    "explosion": "ExplosionSettings",
    "projectile": "ProjectileSettings",
    "status": "StatusEffectSettings",
    "arc": "ArcSettings",
    "beam": "BeamSettings",
}

# record name -> the settings table whose curated layout names its members
RECORD_TABLES = {"damage": "damage_settings", "explosion": "explosion_settings",
                 "projectile": "projectile_settings", "status": "status_effect_settings",
                 "beam": "beam_settings", "arc": "arc_settings"}

# offsets that hd2-datamined's notes establish but the panel does not edit (explosions/projectiles)
KNOWN = {
    "ExplosionSettings": {0: "type", 4: "damage_row", 16: "radius_inner", 20: "radius_mid",
                          24: "radius_outer", 80: "shrapnel_count", 84: "shrapnel_projectile"},
    "ProjectileSettings": {0: "type", 28: "pellets", 32: "velocity", 40: "drag", 44: "gravity",
                           60: "damage_row", 64: "pen_slowdown", 144: "explosion_on_impact",
                           156: "explosion_on_expiry"},
    "DamageSettings": {0: "type", 4: "damage", 8: "durable", 12: "ap_direct", 16: "ap_slight",
                       20: "ap_large", 24: "ap_extreme", 28: "demolition", 32: "stagger", 36: "push"},
    "StatusEffectSettings": {0: "type"},
}

STATUS_NAMES = {5: "Burning", 33: "Heavy burning", 43: "Gas", 44: "Gas", 38: "Stun (small)",
                39: "Stun (medium)", 40: "Stun (large)", 41: "Stun (massive)"}

NOISE = re.compile(r"Sound|Audio|Anim|Event|VO|Material|Decal|Particle|Effect$|Icon|Node", re.I)


def latest(pattern: str) -> Path:
    found = sorted(CACHE.glob(pattern))
    if not found:
        raise SystemExit(f"nothing matches {CACHE / pattern}: run local/run_all.py first")
    return found[-1]


def load_names(path: Path) -> dict[int, str]:
    from typelib import type_hash
    out = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith(("//", "#")):
            out[type_hash(line)] = line
    return out


def find_group(plaintext: Path, type_id: int) -> tuple[Path, bytes, int] | None:
    from ldld import parse_ldld
    for path in sorted(plaintext.glob("*.dl_bin")):
        try:
            groups = parse_ldld(path.read_bytes())
        except ValueError:
            continue
        for group in groups:
            if group["type_id"] == type_id:
                data = path.read_bytes()
                start = group["payload_offset"]
                return path, data[start:start + group["payload_size"]], group["payload_size"]
    return None


def element_of(lib, type_id: int, stride: int | None = None) -> int | None:
    members = lib.info(type_id)["members"]
    if not members:
        return None
    if stride:
        for member in members:
            if member["size64"] == stride:
                return member["type_id"]
    return max(members, key=lambda m: m["size64"])["type_id"]


def decode(column: dict, row: bytes, lib, enums: dict) -> tuple[str, object]:
    """(text, numeric) for one column of one row."""
    size, offset, kind = column["size"], column["offset"], column["type"]
    if kind == "f32":
        if offset + 4 > len(row):
            return "", None
        value = struct.unpack_from("<f", row, offset)[0]
        return ("" if not math.isfinite(value) else f"{value:g}"), value
    member = column.get("member") or {"size64": size, "offset64": offset, "type_name": None, "type_id": 0}
    if offset + size > len(row):
        return "", None
    chunk = row[offset:offset + size]
    if member["type_name"]:
        if size == 8:
            return f"0x{int.from_bytes(chunk, 'little'):016X}", None
        if size == 4:
            number = int.from_bytes(chunk, "little")
            return f"*{number}", None
        return f"struct{size}", None
    if size == 1:
        return str(chunk[0]), chunk[0]
    if size == 2:
        return str(int.from_bytes(chunk, "little")), int.from_bytes(chunk, "little")
    if size == 4:
        number = int.from_bytes(chunk, "little")
        if member["type_id"] in enums and number in enums[member["type_id"]]:
            return f"{number}={enums[member['type_id']][number]}", number
        as_float = struct.unpack("<f", chunk)[0]
        integral = number <= 0x7FFFFFFF and number == int(number)
        # an integer that reads as a tidy float (1.0, 0.75, 65) is probably that float
        if math.isfinite(as_float) and (as_float == 0 or 1e-4 < abs(as_float) < 1e6) \
                and abs(as_float - round(as_float, 4)) < 1e-6 and not integral:
            return f"{as_float:g}", as_float
        if integral and 100000 < number and math.isfinite(as_float) and abs(as_float - round(as_float, 4)) < 1e-6 \
                and 0 < abs(as_float) < 1e6:
            return f"{as_float:g}", as_float
        return str(number), number
    if size == 8:
        number = int.from_bytes(chunk, "little")
        return f"0x{number:016X}", None
    return f"{size}B", None


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--records", default="damage,explosion,projectile,status")
    ap.add_argument("--panel", help="panel dump TSV (default: newest in local/cache)")
    ap.add_argument("--typelib", help="plaintext typelib (default: newest cache)")
    ap.add_argument("--plaintext", help="plaintext tables (default: newest cache)")
    ap.add_argument("--names", help="dl_type_names.txt")
    ap.add_argument("--go-names", help="go_names.json")
    ap.add_argument("--out-dir", help="where the .md/.csv go (default local/report)")
    args = ap.parse_args(argv)

    sys.path.insert(0, str(HERE))
    import typelib as tl
    import field_report as fr

    panel_path = Path(args.panel) if args.panel else latest("panel-*.tsv")
    typelib_path = Path(args.typelib) if args.typelib else latest("plaintext-*/dl_library.dl_typelib")
    plaintext = Path(args.plaintext) if args.plaintext else typelib_path.parent
    names_path = Path(args.names) if args.names else HERE / "names" / "dl_type_names.txt"
    go_path = Path(args.go_names) if args.go_names else CACHE / "go_names.json"
    out_dir = Path(args.out_dir) if args.out_dir else REPORT
    out_dir.mkdir(parents=True, exist_ok=True)
    build = plaintext.name.replace("plaintext-", "")

    lib = tl.load(str(typelib_path))
    names = load_names(names_path)
    go = json.loads(go_path.read_text(encoding="utf-8"))["types"] if go_path.exists() else {}
    known_path = CACHE / "known-names.json"
    known_data = json.loads(known_path.read_text(encoding="utf-8")) if known_path.exists() else {}
    known_tables = known_data.get("tables", {})
    record_names_all = {name: {int(k): v for k, v in entry.get("names", {}).items() if k.isdigit()}
                        for name, entry in (known_data.get("records") or {}).items()}
    panel = fr.parse_panel(panel_path)
    enums: dict[int, dict[int, str]] = {}
    for enum in lib.enums():
        enums[int(enum["enum_id"], 16)] = {value["value"]: value["name"] for value in enum["values"]}

    # the panel's own names for the offsets it edits, and who uses each row
    panel_tables: dict[int, dict] = {}
    for table in panel["tables"]:
        try:
            tid = int(table["type"], 16)
        except ValueError:
            continue
        panel_tables.setdefault(tid, {"stride": table["stride"], "base_mod": table["base_mod"]})
    labels: dict[tuple[int, int], str] = {}
    for (kind, offset), stats in panel["labels"].items():
        labels.setdefault((kind, offset), stats[0])
    users: dict[tuple[int, int], list[str]] = {}
    weapons = panel["weapons"]
    for row in panel["rows"]:
        weapon = weapons.get(row["hash"])
        name = weapon["name"] if weapon else row["hash"]
        for item in row.get("parts", "").split(","):
            if "=" not in item:
                continue
            _stat, at = item.split("=", 1)
            kind_text, offset_text, _storage = at.split(":")
            if not re.fullmatch(r"[0-9A-Fa-f]{8}", kind_text):
                continue          # a grouped table ('stratagems 4860 ...'): not one record type
            entry = panel_tables.get(int(kind_text, 16))
            if not entry or not entry["stride"]:
                continue
            index = (int(offset_text) - entry["base_mod"]) // entry["stride"]
            bucket = users.setdefault((int(kind_text, 16), index), [])
            if name not in bucket:
                bucket.append(name)

    # cross references between damage / explosion / projectile rows, read straight from the files
    def rows_of(type_name: str):
        found = find_group(plaintext, tl.type_hash(type_name))
        if not found:
            return None
        _path, payload, _size = found
        element = element_of(lib, tl.type_hash(type_name))
        size = lib.desc(element)[3]
        entry = panel_tables.get(tl.type_hash(type_name), {})
        base = entry.get("base_mod", 0)
        out = []
        for r in range((len(payload) - base) // size):
            row = payload[base + r * size: base + (r + 1) * size]
            out.append((int.from_bytes(row[:4], "little"), row))
        return out

    damage_rows = rows_of("DamageSettings") or []
    explosion_rows = rows_of("ExplosionSettings") or []
    projectile_rows = rows_of("ProjectileSettings") or []

    def u32(row: bytes, offset: int) -> int:
        return int.from_bytes(row[offset:offset + 4], "little") if offset + 4 <= len(row) else 0

    damage_value = {row_id: u32(row, 4) for row_id, row in damage_rows}
    used_by_damage: dict[int, list[str]] = {}
    for row_id, row in explosion_rows:
        target = u32(row, 4)
        if target:
            used_by_damage.setdefault(target, []).append(f"explosion {row_id}")
    for row_id, row in projectile_rows:
        target = u32(row, 60)
        if target:
            used_by_damage.setdefault(target, []).append(f"projectile {row_id}")

    used_by_explosion: dict[int, list[str]] = {}
    for row_id, row in projectile_rows:
        for offset in (144, 156):
            target = u32(row, offset)
            if target:
                label = f"projectile {row_id}" + (" (expiry)" if offset == 156 else "")
                used_by_explosion.setdefault(target, []).append(label)

    links = {"damage": ("damage_row", used_by_damage),
             "explosion": ("projectile", used_by_explosion),
             "projectile": ("damage_row", None)}

    for record in [r.strip() for r in args.records.split(",") if r.strip()]:
        type_name = RECORDS.get(record)
        if not type_name:
            print(f"unknown record {record!r} (have: {', '.join(RECORDS)})", file=sys.stderr)
            continue
        type_id = tl.type_hash(type_name)
        group = find_group(plaintext, type_id)
        if not group:
            print(f"{type_name}: no table in {plaintext}", file=sys.stderr)
            continue
        path, payload, size = group
        entry = panel_tables.get(type_id, {})
        stride_probe = entry.get("stride") or None
        element = element_of(lib, type_id, stride_probe)
        element_size = lib.desc(element)[3]
        base_mod = entry.get("base_mod", 0) if entry else 0
        rows = (len(payload) - base_mod) // element_size
        members = fr.dedupe(lib.info(element)["members"])
        go_names = (go.get(names.get(element, ""), {}) or {}).get("names") or []
        known = KNOWN.get(type_name, {})
        curated = known_tables.get(RECORD_TABLES.get(record, f"{record}_settings"), {})
        record_curated = record_names_all.get(names.get(element) or "", {})
        curated_fields = {int(k): v for k, v in curated.get("fields", {}).items()}
        curated_floats = set(curated.get("floats", []))
        stride = entry.get("stride") or element_size

        # the row's columns: first the fields the panel edits (it knows the exact width of each:
        # DamageInfo's +4 is one u64 to the library but damage +4 / durable +8 to the panel), then
        # whatever part of the record the panel leaves alone
        panel_offsets = {}
        for (kind, offset), stats in labels.items():
            if kind != f"{type_id:08X}":
                continue
            probe = (offset - base_mod) % stride
            panel_offsets.setdefault(probe, stats)
        storage = {}
        for field in panel["fields"]:
            if field["kind"] != f"{type_id:08X}":
                continue
            probe = (field["offset"] - base_mod) % stride
            storage.setdefault(probe, (field["storage"], field["limit"]))
        columns = []
        for probe in sorted(panel_offsets):
            kind_of, limit = storage.get(probe, ("u32", "0"))
            width = 1 if kind_of == "flag" else (8 if kind_of == "u64" else 4)
            columns.append({"offset": probe, "size": width, "type": kind_of,
                            "name": panel_offsets[probe], "label": panel_offsets[probe]})
        covered = {c["offset"] for c in columns}
        for index, member in enumerate(members):
            if any(c["offset"] <= member["offset64"] < c["offset"] + c["size"] for c in columns):
                continue
            name = (record_curated.get(member["offset64"]) or curated_fields.get(member["offset64"])
                    or known.get(member["offset64"])
                    or (go_names[index] if index < len(go_names) else "") or "")
            is_float = member["offset64"] in curated_floats
            columns.append({"offset": member["offset64"], "size": member["size64"],
                            "type": "f32" if is_float else fr.member_type(member, lib), "name": name or "",
                            "label": "", "member": member})
        columns.sort(key=lambda c: c["offset"])
        # every row, with its id, in id order (the panel's row index -> what uses it is kept aside)
        records = []
        for r in range(rows):
            row = payload[base_mod + r * element_size: base_mod + (r + 1) * element_size]
            records.append((int.from_bytes(row[:4], "little"), r, row))
        records.sort(key=lambda item: item[0])
        ids = [item[0] for item in records]
        seen = [item[2] for item in records]
        panel_rows = [item[1] for item in records]
        varying = set()
        for index, column in enumerate(columns):
            if column["size"] not in (1, 2, 4, 8):
                continue
            values = {row[column["offset"]:column["offset"] + column["size"]] for row in seen}
            if len(values) > 1:
                varying.add(index)

        stem = out_dir / f"{record}-table-{build}"
        try:
            handle = open(str(stem) + ".csv", "w", newline="", encoding="utf-8")
        except PermissionError:
            print(f"{stem}.csv is locked (open in a spreadsheet?): skipped this record", file=sys.stderr)
            continue
        with handle:
            writer = csv.writer(handle)
            writer.writerow(["id", "used_by"] + [f"+{c['offset']} {c['name'] or c['type']}".strip()
                                                 for c in columns])
            for r, row_id in enumerate(ids):
                row = seen[r]
                used = users.get((type_id, panel_rows[r]), [])
                writer.writerow([row_id, "; ".join(used)] + [decode(c, row, lib, enums)[0] for c in columns])

        lines = [f"# {type_name} rows — build {build}", "",
                 f"{len(seen)} rows of {element_size} B in `{path.name}`. Names: the panel's stat label where it "
                 f"has one, else FileDiver's field name, else a name from hd2-datamined's notes.", "",
                 "Columns: `off name` — only members that differ between rows, plus the ones the panel edits "
                 "or that the notes name. The `.csv` next to this file has every member.",
                 "", "## Columns", "", "| off | size | type | name | panel |", "|---|---:|---|---|---|"]
        shown = [c for index, c in enumerate(columns)
                 if c["name"] or c["label"] or index in varying or c["size"] in (1, 2, 4)]
        if record in ("explosion", "projectile"):   # its damage row is the link column
            shown = [c for c in shown if not (c["name"] == "damage_row" or c["offset"] == 4)]
        if record == "damage":
            shown = [c for c in shown if not (c["name"] == "type" and c["offset"] == 0)]
        for index, column in enumerate(columns):
            if column not in shown:
                continue
            lines.append(f"| +{column['offset']} | {column['size']} | {column['type']} | "
                         f"{column['name']} | {'varies' if index in varying else 'constant'} |")
        link = links.get(record, (None, None))
        lines += ["", "## Rows", ""]
        header = ([f"linked ({link[0]})"] if link[1] is not None else
                  ["damage row (value)"] if record in ("explosion", "projectile") else [])             + [f"+{c['offset']}" + (f" {c['name']}" if c["name"] else "") for c in shown]
        lines.append("| id | used by | " + " | ".join(header) + " |")
        lines.append("|---:|---|" + "---|" * len(header))
        for r, row_id in enumerate(ids):
            row = seen[r]
            cells = []
            for index, column in enumerate(shown):
                text, _number = decode(column, row, lib, enums)
                if text in ("0", "0x0000000000000000", ""):
                    text = "·"
                cells.append(text)
            used = users.get((type_id, panel_rows[r]), [])
            used_text = ", ".join(used[:3]) + (f" +{len(used) - 3}" if len(used) > 3 else "") if used else ""
            extra = ""
            if link[1] is not None:
                found = link[1].get(row_id) or []
                extra = ", ".join(found[:4]) + (f" +{len(found) - 4}" if len(found) > 4 else "")
            elif record in ("explosion", "projectile"):
                target = u32(row, 4 if record == "explosion" or record == "projectile" else 60)
                if record == "projectile":
                    target = u32(row, 60)
                extra = f"{target} ({damage_value.get(target, '?')} dmg)" if target else "·"
            id_text = f"{row_id} ({STATUS_NAMES[row_id]})" if record == "status" and row_id in STATUS_NAMES                 else str(row_id)
            lines.append(f"| {id_text} | {used_text} | " + (extra + " | " if extra or link[1] is not None
                                                          or record in ("explosion", "projectile") else "")
                         + " | ".join(cells) + " |")
        lines.append("")
        (Path(str(stem) + ".md")).write_text("\n".join(lines), encoding="utf-8")
        print(f"{stem}.md / .csv: {len(seen)} {type_name} row(s), {len(shown)} column(s), "
              f"{len(varying)} varying")
    return 0


if __name__ == "__main__":
    sys.exit(main())
