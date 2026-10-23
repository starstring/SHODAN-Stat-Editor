"""Unseal the game's own data files into a per-build plaintext cache.

`data/game/*.dl_bin` and `data/game/dl_library.dl_typelib` are NaCl sealed boxes
(crypto_box_seal = X25519 + XSalsa20-Poly1305, 48-byte header). The recipient key pair is the
one the game itself uses to open them, and Stat Editor ships it in `offline/gamedata.lua`
(PK/SK), so this tool reads the keys from there instead of holding its own copy. libsodium is
used through ctypes: no third-party Python package is needed.

Output (per build id, so several builds can sit side by side):

    local/cache/plaintext-<buildid>/generated_*.dl_bin   plaintext tables
    local/cache/plaintext-<buildid>/dl_library.dl_typelib  plaintext type library
    local/cache/plaintext-<buildid>/build.json           build id, game path, per-file sizes

Usage:
    python dump_plain.py                        # find the game, unseal everything
    python dump_plain.py --game "D:/.../Helldivers 2"
    python dump_plain.py --only generated_entities.dl_bin --out local/cache/try
"""
from __future__ import annotations

import argparse
import ctypes
import json
import os
import re
import struct
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent               # SHODAN-Stat-Editor/
SEALBYTES = 48
SEALED_SUFFIXES = (".dl_bin", ".dl_typelib")


# ---------------------------------------------------------------- where the game is
def _vdf_paths(text: str) -> list[str]:
    return [m.replace("\\\\", "\\") for m in re.findall(r'"path"\s*"([^"]+)"', text)]


def find_game(explicit: str | None) -> Path:
    candidates: list[Path] = []
    if explicit:
        candidates.append(Path(explicit))
    note = Path(os.environ.get("LOCALAPPDATA", "")) / "SHODAN" / "StatEditor" / "game folder.txt"
    if note.exists():
        text = note.read_text(encoding="utf-8", errors="replace").strip()
        if text:
            candidates.append(Path(text))
    steam = Path(os.environ.get("PROGRAMFILES(X86)", r"C:\Program Files (x86)")) / "Steam"
    libraries = [steam]
    vdf = steam / "steamapps" / "libraryfolders.vdf"
    if vdf.exists():
        libraries += [Path(p) for p in _vdf_paths(vdf.read_text(encoding="utf-8", errors="replace"))]
    for library in libraries:
        candidates.append(library / "steamapps" / "common" / "Helldivers 2")
    for path in candidates:
        if (path / "data" / "game").is_dir():
            return path
    raise SystemExit("Helldivers 2 not found: pass --game <folder holding data/>")


def build_id(game: Path) -> str | None:
    """Steam's build id from the library's appmanifest_553850.acf, if it is there."""
    for parent in game.parents:
        manifest = parent / "appmanifest_553850.acf"
        if manifest.exists():
            found = re.search(r'"buildid"\s*"(\d+)"', manifest.read_text(encoding="utf-8", errors="replace"))
            if found:
                return found.group(1)
    return None


# ---------------------------------------------------------------- libsodium + the keys
def find_sodium(explicit: str | None) -> Path:
    candidates: list[Path] = []
    if explicit:
        candidates.append(Path(explicit))
    candidates += [
        REPO / "offline" / "runtime" / "libsodium.dll",
        Path(os.environ.get("LOCALAPPDATA", "")) / "SHODAN" / "StatEditor" / "libsodium.dll",
    ]
    for top in (Path(os.environ.get("USERPROFILE", str(HERE))), Path.home() / "Desktop"):
        if top.is_dir():
            candidates += sorted(top.glob("SHODAN Stat Editor Offline*/libsodium.dll"))
    for path in candidates:
        if path.exists():
            return path
    raise SystemExit("libsodium.dll not found: pass --sodium <path> (it ships with Stat Editor)")


def load_keys(gamedata: Path | None) -> tuple[bytes, bytes]:
    for path in [gamedata] if gamedata else [REPO / "offline" / "gamedata.lua"]:
        text = path.read_text(encoding="utf-8", errors="replace")
        pk = re.search(r"local PK = unhex\('([0-9a-fA-F]+)'\)", text)
        sk = re.search(r"local SK = unhex\('([0-9a-fA-F]+)'\)", text)
        if pk and sk:
            return bytes.fromhex(pk.group(1)), bytes.fromhex(sk.group(1))
    raise SystemExit("no PK/SK: pass --gamedata <offline/gamedata.lua>")


class SodiumDll:
    """libsodium.dll through ctypes: the DLL Stat Editor ships next to its launcher."""

    def __init__(self, path: Path):
        self.path = path
        self.lib = ctypes.CDLL(str(path))
        self.lib.sodium_init.restype = ctypes.c_int
        if self.lib.sodium_init() < 0:
            raise SystemExit(f"{path}: sodium_init failed")

    def unseal(self, sealed: bytes, pk: bytes, sk: bytes) -> bytes | None:
        if len(sealed) <= SEALBYTES:
            return None
        out = ctypes.create_string_buffer(len(sealed) - SEALBYTES)
        rc = self.lib.crypto_box_seal_open(out, ctypes.c_char_p(sealed), ctypes.c_ulonglong(len(sealed)),
                                           ctypes.c_char_p(pk), ctypes.c_char_p(sk))
        return out.raw if rc == 0 else None


class SodiumPyNaCl:
    """libsodium through PyNaCl (pip install pynacl): used when no DLL is at hand."""

    def __init__(self):
        from nacl import bindings
        self.bindings = bindings
        self.path = "PyNaCl"

    def unseal(self, sealed: bytes, pk: bytes, sk: bytes) -> bytes | None:
        if len(sealed) <= SEALBYTES:
            return None
        try:
            return self.bindings.crypto_box_seal_open(sealed, pk, sk)
        except Exception:
            return None


def open_sodium(explicit: str | None):
    """A DLL when one is found (no dependencies), PyNaCl otherwise."""
    try:
        return SodiumDll(find_sodium(explicit))
    except SystemExit:
        try:
            return SodiumPyNaCl()
        except ImportError:
            raise SystemExit("neither libsodium.dll nor PyNaCl found: pass --sodium <path> or "
                             "pip install pynacl")


# ---------------------------------------------------------------- the dump
def unseal_dir(game: Path, out_dir: Path, sodium, pk: bytes, sk: bytes, only: str | None) -> dict:
    source = game / "data" / "game"
    out_dir.mkdir(parents=True, exist_ok=True)
    report = {"game": str(game), "build": build_id(game), "unsealed": [], "skipped": []}
    for path in sorted(source.iterdir()):
        if not path.name.endswith(SEALED_SUFFIXES):
            continue
        if only and only not in path.name:
            continue
        blob = path.read_bytes()
        plain = sodium.unseal(blob, pk, sk)
        if plain is None:
            report["skipped"].append({"name": path.name, "reason": "not a sealed box (already plain?)",
                                      "size": len(blob)})
            continue
        (out_dir / path.name).write_bytes(plain)
        report["unsealed"].append({"name": path.name, "sealed": len(blob), "plain": len(plain)})
    return report


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--game", help="Helldivers 2 folder (the one holding data/)")
    ap.add_argument("--sodium", help="libsodium.dll path")
    ap.add_argument("--gamedata", help="offline/gamedata.lua to read PK/SK from")
    ap.add_argument("--out", help="output folder (default local/cache/plaintext-<buildid>)")
    ap.add_argument("--only", help="unseal only files whose name holds this text")
    args = ap.parse_args(argv)

    game = find_game(args.game)
    sodium = open_sodium(args.sodium)
    pk, sk = load_keys(Path(args.gamedata) if args.gamedata else None)
    build = build_id(game)
    out_dir = Path(args.out) if args.out else REPO / "local" / "cache" / f"plaintext-{build or 'unknown'}"
    report = unseal_dir(game, out_dir, sodium, pk, sk, args.only)
    (out_dir / "build.json").write_text(json.dumps(report, indent=1), encoding="utf-8")

    total = sum(item["plain"] for item in report["unsealed"])
    print(f"game   : {game}")
    print(f"build  : {report['build'] or 'unknown'}")
    print(f"sodium : {sodium.path}")
    print(f"out    : {out_dir}")
    print(f"unsealed {len(report['unsealed'])} file(s), {total / 1e6:.1f} MB plain")
    for item in report["skipped"]:
        print(f"  skipped {item['name']}: {item['reason']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
