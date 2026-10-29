"""Packs a runnable build of this fork: upstream's launcher + the generated panel.

    python local/package_exe.py          # -> local/build/SHODAN-Stat-Editor-Offline-<version>-r<NN>.zip
                                         #    and the runnable folder next to it

Upstream's `offline/package.py` does the packing (its file list, README, third-party notices); this
script only swaps in the panel that `local/build_panel.py` generates, tags the build with its local
revision, and puts the output where this fork keeps it. Nothing upstream is edited.

Versioning: the build keeps upstream's version and adds a local revision - `4.5.1-r01`, `4.5.1-r02`,
then `4.5.2-r01` after the next merge. The counter lives in `local/build/.release.json`, so packing
twice without merging upstream gives r01, r02, ...

The updater compares versions by their numbers (`offline/update.lua`: `gmatch('%d+')`), so
`4.5.1-r02` counts as {4, 5, 1, 2}: newer than the official `4.5.1` (no update offered over this
build) and older than a future `4.5.2` (that update is offered, and merging it gives 4.5.2-r01).
"""
from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
BUILD = HERE / "build"
PANEL = BUILD / "panel-for-package.lua"
OUT = BUILD
STATE = OUT / ".release.json"
FOLDER = OUT / "SHODAN Stat Editor Offline"
STAGING = OUT / ".staging"


def next_version() -> str:
    """Upstream's version plus this fork's revision: 4.5.1 -> 4.5.1-r01 (and r02, r03, ...)."""
    text = PANEL.read_text(encoding="utf-8")
    found = re.search(r"version = '([\d.]+)'", text)
    if not found:
        raise SystemExit("no version in the generated panel")
    upstream = found.group(1)
    state = {}
    if STATE.exists():
        try:
            state = json.loads(STATE.read_text(encoding="utf-8"))
        except ValueError:
            state = {}
    revision = int(state.get("revision", 0)) + 1 if state.get("version") == upstream else 1
    version = f"{upstream}-r{revision:02d}"
    PANEL.write_text(text[:found.start()] + f"version = '{version}'" + text[found.end():], encoding="utf-8")
    STATE.write_text(json.dumps({"version": upstream, "revision": revision}, indent=1), encoding="utf-8")
    return version


def unpack(archive: Path, into: Path) -> None:
    """The zip's payload (its top folder is dropped) into `into`."""
    if into.exists():
        shutil.rmtree(into, ignore_errors=True)
    into.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(archive) as zf:
        for name in zf.namelist():
            if name.endswith("/") or "/" not in name:
                continue
            target = into / name.split("/", 1)[1]
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(zf.read(name))


def main() -> int:
    # the packaged panel has no test hook (it only exists for the headless harness)
    subprocess.run([sys.executable, str(HERE / "build_panel.py"), "--skip-test"], check=True)
    # the host file this fork patches (passive-stack conflict policy): generated, never edited upstream
    subprocess.run([sys.executable, str(HERE / "patch_hostdata.py")], check=True)
    version = next_version()

    name = f"SHODAN-Stat-Editor-Offline-{version}"
    os.environ["SSEO_CHANNEL"] = "local"
    if not os.environ.get("SSEO_COMMIT"):
        commit = subprocess.run(["git", "-C", str(REPO), "rev-parse", "--short", "HEAD"],
                                capture_output=True, text=True).stdout.strip()
        dirty = subprocess.run(["git", "-C", str(REPO), "status", "--porcelain"],
                               capture_output=True, text=True).stdout.strip()
        os.environ["SSEO_COMMIT"] = commit + ("+local" if dirty else "")

    # upstream's packer, with its panel swapped for the generated one and its version taken as-is
    source = (REPO / "offline" / "package.py").read_text(encoding="utf-8")
    patched = source.replace(
        "PANEL = os.path.join(ADDON, 'stat_editor_offline.lua')   # build.py --offline",
        f"PANEL = {str(PANEL)!r}   # local build")
    if patched == source:
        raise SystemExit("offline/package.py changed: it no longer sets PANEL where this expects")
    patched, count = re.subn(r"^VERSION = .*$", f"VERSION = {version!r}", patched, count=1, flags=re.M)
    if count != 1:
        raise SystemExit("offline/package.py changed: no VERSION line to replace")
    argv = sys.argv
    sys.argv = ["package.py", name]
    try:
        exec(compile(patched, "offline/package.py", "exec"),
             {"__name__": "__main__", "__file__": str(REPO / "offline" / "package.py")})
    finally:
        sys.argv = argv

    made = REPO / "offline" / "release" / f"{name}.zip"
    if not made.exists():
        raise SystemExit(f"expected {made}")
    OUT.mkdir(parents=True, exist_ok=True)
    target = OUT / made.name
    shutil.copy2(made, target)

    # unpack beside the runnable folder, then refresh that folder file by file: the running build's
    # .exe and DLLs are locked, and deleting files there before knowing that would leave it broken
    unpack(target, STAGING)
    patched_host = BUILD / "hostdata.lua"
    if patched_host.exists() and (STAGING / "app" / "hostdata.lua").exists():
        shutil.copy2(patched_host, STAGING / "app" / "hostdata.lua")
    skipped = 0
    for source_file in sorted(STAGING.rglob("*")):
        if source_file.is_dir():
            continue
        destination = FOLDER / source_file.relative_to(STAGING)
        destination.parent.mkdir(parents=True, exist_ok=True)
        try:
            shutil.copy2(source_file, destination)
        except PermissionError:
            skipped += 1
    shutil.rmtree(STAGING, ignore_errors=True)
    if skipped:
        print(f"note: {skipped} file(s) are in use by the running build; close the editor and pack again")

    # one zip at a time: the previous ones are superseded
    for old in OUT.glob("SHODAN-Stat-Editor-Offline-*.zip"):
        if old.name != target.name:
            old.unlink(missing_ok=True)
    print(f"\n{target}")
    print(f"{FOLDER}  (run it from here)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
