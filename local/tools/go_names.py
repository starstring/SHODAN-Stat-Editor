"""Field names for the type library, from FileDiver's own Go structs.

The game's `dl_library.dl_typelib` has had its string table stripped since 2024-02-23 (the type
library dumper says so), so member names are not in the file any more: every member is just an
offset, a size and a type id. FileDiver's `datalibrary/*.go` keeps hand-annotated Go structs that
were generated while the names were still there, and their fields are in the same order as the
type library's members. This tool reads those struct names, so a member at +384 can be shown as
`FirePreventsMovement` instead of `+384`.

The order is trusted only when the counts agree (or when field sizes line up one to one); a Go
struct that has drifted from the current build is reported as unmatched instead of mislabelled.

    python go_names.py                      # summary + local/cache/go_names-<build>.json
    python go_names.py --source <filediver folder> --out <file>
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
DEFAULT_SOURCE = REPO.parent / "filediver" / "datalibrary"
TYPELIB_CACHE = REPO / "local" / "cache"

# go types whose size the 64-bit layout fixes (anything else is looked up in the type library)
GO_SIZES = {"float32": 4, "float64": 8, "uint8": 1, "int8": 1, "byte": 1, "bool": 1, "uint16": 2,
            "int16": 2, "uint32": 4, "int32": 4, "uint64": 8, "int64": 8, "int": 8, "uint": 8,
            "stingray.Hash": 8, "stingray.ThinHash": 4, "string": 16, "mgl32.Vec2": 8, "mgl32.Vec3": 12,
            "mgl32.Vec4": 16, "mgl32.Mat4": 64}

# `type X uint8` (bitfields and other integral aliases) and fields embedded by type name
ALIAS = re.compile(r"^type\s+([A-Za-z_][A-Za-z0-9_]*)\s+(u?int(?:8|16|32|64)|float(?:32|64)|byte|bool)\s*$", re.M)
EMBEDDED = re.compile(r"^\s+([A-Z][A-Za-z0-9_]*)\s*$")
EMBEDDED_TAGGED = re.compile(r"^\s+([A-Z][A-Za-z0-9_]*)\s+`")

STRUCT = re.compile(r"^type\s+([A-Za-z_][A-Za-z0-9_]*)\s+struct\s*\{", re.M)
FIELD = re.compile(r"^\s+([A-Za-z_][A-Za-z0-9_]*|_)\s+([^`/]+?)\s*(?:`[^`]*`)?\s*(?://.*)?$")

def parse_go_files(source: Path) -> dict[str, list[dict]]:
    structs: dict[str, list[dict]] = {}
    for path in sorted(source.rglob("*.go")):
        if path.name.endswith("_test.go"):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for match in STRUCT.finditer(text):
            name = match.group(1)
            depth, start, fields = 0, match.end(), []
            for index in range(start, len(text)):
                char = text[index]
                if char == "{":
                    depth += 1
                elif char == "}":
                    if depth == 0:
                        body = text[start:index]
                        break
                    depth -= 1
            else:
                continue
            for line in body.splitlines():
                line = line.split("//")[0].rstrip()
                if not line.strip():
                    continue
                found = None if EMBEDDED_TAGGED.match(line) else FIELD.match(line)
                if not found:
                    embedded = EMBEDDED.match(line) or EMBEDDED_TAGGED.match(line)
                    if not embedded:
                        continue
                    fields.append({"name": embedded.group(1), "go_type": embedded.group(1),
                                   "file": path.name})
                    continue
                fields.append({"name": found.group(1), "go_type": found.group(2).strip(),
                               "file": path.name})
            # `_ [3]uint8` lines are the Go struct's explicit padding. The type library has no
            # member for them, but their size has to stay in the walk to keep the offsets right.
            if fields and name not in structs:
                structs[name] = fields
    # integral aliases (`type ExplosionInfoBitfield1 uint8`) so an embedded bitfield has a size
    for match in ALIAS.finditer(text_of_source(source)):
        structs.setdefault(match.group(1), [{"name": "_", "go_type": match.group(2), "file": "alias"}])
    return structs


def text_of_source(source: Path) -> str:
    """Every .go file concatenated: the alias scan is done once over the whole tree."""
    if not hasattr(text_of_source, "cache"):
        parts = [path.read_text(encoding="utf-8", errors="replace")
                 for path in sorted(source.rglob("*.go")) if not path.name.endswith("_test.go")]
        text_of_source.cache = chr(10).join(parts)
    return text_of_source.cache


def go_size(go_type: str, lib, structs: dict | None = None, seen: set | None = None) -> int | None:
    """Size of a Go field in the 64-bit layout, or None when it cannot be worked out.

    FileDiver's structs are laid out exactly like the type library: every padding byte is an
    explicit `_ [N]uint8`, so a struct's size is the sum of its fields (no implicit alignment).
    A struct that only exists on the Go side (OpticSetting) is measured the same way.
    """
    base = go_type.strip()
    if base.startswith("enum."):
        return 4
    if base in ("stingray.Hash", "stingray.ThinHash") or base.startswith("[]") or base.startswith("*"):
        return {"stingray.Hash": 8, "stingray.ThinHash": 4}.get(base, 24 if base.startswith("[]") else 8)
    if base in GO_SIZES:
        return GO_SIZES[base]
    array = re.match(r"^\[(\d+)\](.+)$", base)
    if array:
        inner = go_size(array.group(2), lib, structs, seen)
        return inner * int(array.group(1)) if inner else None
    try:
        return lib.desc(lib.type_id_of(base))[3]
    except Exception:
        pass
    if structs and base in structs and base not in (seen or set()):
        total = 0
        for field in structs[base]:
            size = go_size(field["go_type"], lib, structs, (seen or set()) | {base})
            if size is None:
                return None
            total += size
        return total
    return None


def align(fields: list[dict], members: list[dict], lib, structs: dict) -> list[str | None] | None:
    """One name per member, following the offsets, or None when the Go struct no longer fits.

    The Go structs come from a build where the names still existed, so a field may have been added
    on either side. Walking both in offset order keeps a shifted member unnamed instead of wrong.
    """
    names: list[str | None] = [None] * len(members)
    offset, at = 0, 0
    for index, member in enumerate(members):
        while at < len(fields):
            size = go_size(fields[at]["go_type"], lib, structs)
            if size is None:
                return None
            if offset + size <= member["offset64"]:
                at, offset = at + 1, offset + size
            else:
                break
        if at >= len(fields) or offset != member["offset64"]:
            continue
        size = go_size(fields[at]["go_type"], lib, structs)
        if size is None:
            return None
        if size != member["size64"]:      # same offset, different size: not the same member
            continue
        name = fields[at]["name"]
        names[index] = None if name == "_" else name
        at, offset = at + 1, offset + size
    named = sum(1 for name in names if name)
    if named == 0:
        return None
    # Some Go structs decode a member into several fields (a string is one member for the game and a
    # pointer + length in Go), so the walk can drift. Names are only handed out on an exact offset
    # match, and a struct is used only when most of its members were placed that way.
    return names if named * 2 >= len(members) else None


def size_options(go_type: str, lib, structs: dict, seen: set | None = None) -> set[int]:
    """Every game-side size a Go field could occupy.

    FileDiver's Go view is not the game's layout for references: a Go `string` is a 16-byte header
    where the game keeps a 4- or 8-byte hash, and a Go slice is 24 bytes where the game keeps a
    16-byte (pointer, count). Sizes are used for alignment, so both readings are allowed.
    """
    base = go_type.strip()
    if base == "string":
        return {4, 8, 16}
    if base.startswith("[]"):
        return {16, 24}
    if base.startswith("[") and "]" in base:
        count, inner = base[1:].split("]", 1)
        if count.isdigit():
            options = size_options(inner, lib, structs, seen)
            return {int(count) * size for size in options} if options else set()
    size = go_size(base, lib, structs, seen)
    return {size} if size else set()


def align_by_size(fields: list[dict], members: list[dict], lib, structs: dict) -> list[str | None] | None:
    """Line up a Go struct that drifted, by its field sizes (Needleman-Wunsch over the sizes).

    The Go structs come from a build where the members still had names; when the game later added or
    removed a member, the offset walk above gives up. The sizes are still a strong signal: aligning
    the two size sequences recovers the names that sit on unchanged members, and anything that only
    lines up across a gap is marked with '?' because it is a guess.
    """
    go_sizes, go_names = [], []
    for field in fields:
        options = size_options(field["go_type"], lib, structs)
        if not options:
            return None
        go_sizes.append(options)
        go_names.append(field["name"])
    member_sizes = [member["size64"] for member in members]
    n, m = len(go_sizes), len(member_sizes)
    if not n or not m:
        return None
    MATCH, MISMATCH, GAP = 3, -2, -1
    score = [[0] * (m + 1) for _ in range(n + 1)]
    move = [[""] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        score[i][0], move[i][0] = GAP * i, "up"
    for j in range(1, m + 1):
        score[0][j], move[0][j] = GAP * j, "left"
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            same = member_sizes[j - 1] in go_sizes[i - 1]
            best = (score[i - 1][j - 1] + (MATCH if same else MISMATCH), "diag")
            if score[i - 1][j] + GAP > best[0]:
                best = (score[i - 1][j] + GAP, "up")
            if score[i][j - 1] + GAP > best[0]:
                best = (score[i][j - 1] + GAP, "left")
            score[i][j], move[i][j] = best
    names: list[str | None] = [None] * m
    i, j = n, m
    while i > 0 and j > 0:
        step = move[i][j]
        if step == "diag":
            name = go_names[i - 1]
            if name != "_":
                same = member_sizes[j - 1] in go_sizes[i - 1]
                names[j - 1] = None if same is False else name
            i, j = i - 1, j - 1
        elif step == "up":
            i -= 1
        else:
            j -= 1
    return names if any(names) else None


def build(source: Path, lib) -> dict:
    structs = parse_go_files(source)
    result: dict[str, dict] = {}
    matched = mismatched = 0
    for name, fields in structs.items():
        try:
            tid = lib.type_id_of(name)
        except Exception:
            continue
        info = lib.info(tid)
        members = info["members"]
        plain = [field for field in fields if field["name"] != "_"]
        how, names = None, None
        if len(plain) == len(members):
            # the same number of fields: they line up one to one (explicit `_` padding removed)
            names, how = [field["name"] for field in plain], "count"
        else:
            names = align(fields, members, lib, structs)
            how = "offsets" if names else None
            if not names:
                # a member was added or removed: recover what still lines up by field size
                names = align_by_size(fields, members, lib, structs)
                if names:
                    names = [f"{name}?" if name else None for name in names]
                how = "sizes"
        if names:
            result[name] = {"type_id": f"0x{tid:08X}", "size64": info["size64"], "names": names,
                            "named": sum(1 for n in names if n), "members": len(members), "how": how}
            matched += 1
        else:
            result[name] = {"type_id": f"0x{tid:08X}", "size64": info["size64"], "names": None,
                            "go_fields": len(fields), "members": len(members)}
            mismatched += 1
    return {"source": str(source), "structs": len(structs), "matched": matched,
            "count_mismatch": mismatched, "types": result}


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--source", help="FileDiver's datalibrary folder")
    ap.add_argument("--typelib", help="plaintext dl_library.dl_typelib (default: newest local cache)")
    ap.add_argument("--out", help="JSON output (default local/cache/go_names.json)")
    args = ap.parse_args(argv)

    sys.path.insert(0, str(HERE))
    import typelib as tl

    source = Path(args.source) if args.source else DEFAULT_SOURCE
    if not source.is_dir():
        raise SystemExit(f"FileDiver's datalibrary not found: {source} (--source)")
    path = Path(args.typelib) if args.typelib else sorted(TYPELIB_CACHE.glob("plaintext-*/dl_library.dl_typelib"))[-1]
    lib = tl.load(str(path))
    data = build(source, lib)
    out = Path(args.out) if args.out else TYPELIB_CACHE / "go_names.json"
    out.write_text(json.dumps(data, indent=1, ensure_ascii=False), encoding="utf-8")
    print(f"{out}: {data['matched']} type(s) named, {data['count_mismatch']} drifted (kept unnamed) "
          f"of {data['structs']} Go struct(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
