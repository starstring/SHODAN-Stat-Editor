"""The game's DataLibrary type library (plain `dl_library.dl_typelib`, 'LTLD' v4).

Gives, for every record type the game uses: its name, its 32/64-bit size, and each member's
name, offset, size and type. That is what turns "which attribute can I add" into a lookup
instead of a guess: the panel's field keys are `<LDLD type id>:<payload offset>`, so a member
here is either already exposed (same offset) or a candidate.

Layout (all little-endian, offsets from hd2-datamined/tools/typelib.py):

    0x00  'LTLD' version type_count enum_count member_count enum_value_count
          attribute_count default_data_bytes string_bytes        (36 bytes)
    type ids (4*n) | enum ids (4*n) | type descriptors (36*n) | enum descriptors (32*n) |
    member descriptors (72*n) | enum values (16*n) | attributes (8*n) | defaults | strings

    type descriptor  = name_ref, flags, size32, size64, align32, align64, member_count,
                       member_start, comment
    member descriptor= name_ref, ?, ?, type_flags, type_id, size32, size64, align32, align64,
                       offset32, offset64, ...
    enum descriptor  = name_ref, flags, value_count, value_start, ...

Usage:
    python typelib.py index <typelib> [--json out.json]
    python typelib.py show  <typelib> <name-or-id>
"""
from __future__ import annotations

import argparse
import json
import struct
import sys

TYPE_DESC = 36
MEMBER_DESC = 72
ENUM_DESC = 32
ENUM_VALUE = 16
ATTRIBUTE = 8


def type_hash(name: str) -> int:
    """djb2 with the 5381 seed, minus the seed: the id an LDLD block header stores."""
    value = 5381
    for byte in name.encode("utf-8"):
        value = (value * 33 + byte) & 0xFFFFFFFF
    return (value - 5381) & 0xFFFFFFFF


class TypeLib:
    def __init__(self, data: bytes):
        if len(data) < TYPE_DESC:
            raise ValueError("truncated typelib header")
        magic, version, nt, ne, nm, nv, na, nd, ns = struct.unpack_from("<4s8I", data)
        if magic != b"LTLD" or version != 4:
            raise ValueError(f"not an LTLD v4 typelib (magic {magic!r}, version {version})")
        self.version, self.nt, self.ne, self.nm, self.nv, self.na, self.nd, self.ns = \
            version, nt, ne, nm, nv, na, nd, ns
        self._type_desc = TYPE_DESC + 4 * (nt + ne)
        self._enum_desc = self._type_desc + TYPE_DESC * nt
        self._member_desc = self._enum_desc + ENUM_DESC * ne
        strings_at = self._member_desc + MEMBER_DESC * nm + ENUM_VALUE * nv + ATTRIBUTE * na + nd
        if strings_at + ns != len(data):
            raise ValueError(f"typelib sections do not fit the input ({strings_at}+{ns} != {len(data)})")
        self.data = data
        self.strings = data[strings_at:]
        ids_at = TYPE_DESC
        self._type_ids = [struct.unpack_from("<I", data, ids_at + 4 * i)[0] for i in range(nt)]
        self._enum_ids = [struct.unpack_from("<I", data, ids_at + 4 * nt + 4 * i)[0] for i in range(ne)]
        self._type_index = {tid: i for i, tid in enumerate(self._type_ids)}
        self._enum_index = {eid: i for i, eid in enumerate(self._enum_ids)}
        self._names: dict[int, str | None] = {}
        self._cache: dict[int, dict] = {}

    # ---------------------------------------------------------------- strings / descriptors
    def name(self, ref: int) -> str | None:
        if ref == 0xFFFFFFFF or ref >= len(self.strings):
            return None
        end = self.strings.find(b"\0", ref)
        if end < 0:
            return None
        return self.strings[ref:end].decode("utf-8", "replace")

    def desc(self, tid: int) -> tuple:
        return struct.unpack_from("<9I", self.data, self._type_desc + TYPE_DESC * self._type_index[tid])

    def enum_desc(self, eid: int) -> tuple:
        return struct.unpack_from("<8I", self.data, self._enum_desc + ENUM_DESC * self._enum_index[eid])

    def type_id_of(self, needle: str) -> int:
        needle = needle.strip()
        if needle.lower().startswith("0x"):
            return int(needle, 16)
        wanted = type_hash(needle)
        if wanted in self._type_index:
            return wanted
        for tid in self._type_ids:
            if self.type_name(tid) == needle:
                return tid
        raise ValueError(f"no type named {needle!r} (hash 0x{wanted:08X})")

    # ---------------------------------------------------------------- resolved views
    def type_name(self, tid: int) -> str | None:
        if tid not in self._type_index:
            return None
        return self.name(self.desc(tid)[0])

    def enum_name(self, eid: int) -> str | None:
        if eid not in self._enum_index:
            return None
        return self.name(self.enum_desc(eid)[0])

    def members(self, tid: int) -> list[dict]:
        if tid in self._cache:
            return self._cache[tid]["members"]
        d = self.desc(tid)
        count, start = d[6], d[7]
        out = []
        for j in range(start, start + count):
            m = struct.unpack_from("<18I", self.data, self._member_desc + MEMBER_DESC * j)
            type_id = m[4]
            out.append({
                "name": self.name(m[0]), "name_ref": m[0], "type_flags": m[3], "type_id": type_id,
                "type_name": self.type_name(type_id), "enum_name": self.enum_name(type_id),
                "size32": m[5], "size64": m[6], "align32": m[7], "align64": m[8],
                "offset32": m[9], "offset64": m[10],
            })
        self._cache.setdefault(tid, {})
        self._cache[tid]["members"] = out
        return out

    def info(self, tid: int) -> dict:
        d = self.desc(tid)
        return {"type_id": f"0x{tid:08X}", "type_id_int": tid, "name": self.name(d[0]),
                "flags": d[1], "size32": d[2], "size64": d[3], "align32": d[4], "align64": d[5],
                "member_count": d[6], "members": [dict(m) for m in self.members(tid)]}

    def all_types(self) -> list[dict]:
        return [self.info(tid) for tid in self._type_ids]

    def enums(self) -> list[dict]:
        out = []
        for eid in self._enum_ids:
            d = self.enum_desc(eid)
            count, start = d[2], d[3]
            values = []
            for j in range(start, start + count):
                v = struct.unpack_from("<i", self.data, self._member_desc + MEMBER_DESC * self.nm
                                      + ENUM_VALUE * j)
                ref = struct.unpack_from("<I", self.data, self._member_desc + MEMBER_DESC * self.nm
                                        + ENUM_VALUE * j + 4)[0]
                values.append({"name": self.name(ref), "value": v[0]})
            out.append({"enum_id": f"0x{eid:08X}", "name": self.name(d[0]),
                        "flags": d[1], "values": values})
        return out


def load(path: str) -> TypeLib:
    with open(path, "rb") as handle:
        return TypeLib(handle.read())


def cmd_index(args) -> int:
    lib = load(args.typelib)
    named = sum(1 for tid in lib._type_ids if lib.type_name(tid))
    print(f"{args.typelib}: LTLD v{lib.version}  types={lib.nt} ({named} named) enums={lib.ne} "
          f"members={lib.nm} enum_values={lib.nv}")
    if args.json:
        payload = {"header": {"version": lib.version, "type_count": lib.nt, "enum_count": lib.ne,
                              "member_count": lib.nm},
                   "types": lib.all_types(), "enums": lib.enums()}
        with open(args.json, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=1, ensure_ascii=False)
        print(f"  wrote {args.json}")
    return 0


def cmd_show(args) -> int:
    lib = load(args.typelib)
    tid = lib.type_id_of(args.type)
    info = lib.info(tid)
    print(f"type 0x{tid:08X}  {info['name']!r}  size32={info['size32']} size64={info['size64']} "
          f"align64={info['align64']} members={info['member_count']}")
    print(f"  {'off64':>7} {'size':>5} {'flags':>6}  {'type':<34} name")
    for m in info["members"]:
        kind = m["type_name"] and f"{m['type_name']}" or (m["enum_name"] and f"enum {m['enum_name']}"
                                                         or f"0x{m['type_id']:08X}")
        print(f"  {m['offset64']:>7} {m['size64']:>5} {m['type_flags']:>6}  {kind:<34} {m['name']}")
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="cmd", required=True)
    p = sub.add_parser("index", help="header counts, optionally the whole library as JSON")
    p.add_argument("typelib")
    p.add_argument("--json")
    p.set_defaults(func=cmd_index)
    p = sub.add_parser("show", help="one type's members")
    p.add_argument("typelib")
    p.add_argument("type")
    p.set_defaults(func=cmd_show)
    args = ap.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
