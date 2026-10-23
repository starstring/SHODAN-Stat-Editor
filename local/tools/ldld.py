"""LDLD containers: a u32 group count, then groups of a 24-byte header + payload.

    u32 count
    per group: 'LDLD' | version u32 | type_id u32 | payload_size u32 | flag u32 , payload

The last word is the header's flag byte (0x01 in the game's files) with the rest of the word
reserved: gamedata.lua solves a hash correction into bytes +17..+23 of a header, so the game's own
files have them zeroed. It reads as 1 = the 64-bit member layout. This is the wrapper that the game's generated_*.dl_bin files (once unsealed) and the
entity blob use; the DataLibrary type library itself is a plain 'LTLD' v4 file, not this.
"""
from __future__ import annotations

import struct

LDLD = b"LDLD"
LTLD = b"LTLD"
HEADER = 24          # magic + version + type_id + payload_size + wide


def parse_ldld(data: bytes) -> list[dict]:
    """Split a container into groups; raises ValueError if the layout does not fit."""
    if len(data) < 4:
        raise ValueError("too short for a container header")
    count = struct.unpack_from("<I", data, 0)[0]
    if count == 0 or count > 4096:
        raise ValueError(f"implausible group count {count}")
    offset, groups = 4, []
    for index in range(count):
        if offset + HEADER > len(data):
            raise ValueError(f"group {index}: header runs past end of file")
        magic = data[offset:offset + 4]
        if magic not in (LDLD, LTLD):
            raise ValueError(f"group {index} @0x{offset:X}: bad magic {magic!r}")
        version, type_id, size, wide = struct.unpack_from("<IIII", data, offset + 4)
        payload = offset + HEADER
        if payload + size > len(data):
            raise ValueError(f"group {index}: payload runs past end of file")
        groups.append({"index": index, "magic": magic.decode("ascii"), "version": version,
                       "type_id": type_id, "payload_size": size, "wide": wide,
                       "header_offset": offset, "payload_offset": payload})
        offset = payload + size
    if offset != len(data):
        raise ValueError(f"{len(data) - offset} trailing byte(s) after the last group")
    return groups


def looks_plain(data: bytes) -> bool:
    """True when `data` already is an unsealed container (its group count and first magic fit)."""
    try:
        parse_ldld(data)
        return True
    except ValueError:
        return False
