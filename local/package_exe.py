"""Packs a runnable build of this fork: upstream's launcher + the generated panel.

    python local/package_exe.py                # -> local/build/SHODAN-Stat-Editor-Offline-local-<ver>.zip
                                               #    and the same, unzipped, next to it

Upstream's `offline/package.py` does the packing (its file list, README, third-party notices); this
script only swaps in the panel that `local/build_panel.py` generates and puts the zip where this
fork keeps its build output instead of upstream's release folder. Nothing upstream is edited.

The version is bumped by one patch level in the *generated* panel only (not in src/): the packaged
build then counts as newer than the release it is based on, so the updater does not offer to replace
it with the same-named official release. Settings > Updates still works, so turn it off while a
local build is installed if you do not want to lose these stats.
"""
from __future__ import annotations

import datetime
import os
import re
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
PANEL = HERE / "build" / "panel-for-package.lua"
OUT = HERE / "build"


def bump_patch(text: str) -> tuple[str, str]:
    """3.2.0 -> 3.2.1, in the generated panel only."""
    found = re.search(r"version = '(\d+)\.(\d+)\.(\d+)'", text)
    if not found:
        raise SystemExit("no version in the panel")
    major, minor, patch = (int(part) for part in found.groups())
    local = f"{major}.{minor}.{patch + 1}"
    return text[:found.start()] + f"version = '{local}'" + text[found.end():], local


def main() -> int:
    # the packaged panel has no test hook (it only exists for the headless harness)
    subprocess.run([sys.executable, str(HERE / "build_panel.py"), "--skip-test"], check=True)
    # the host file this fork patches (passive-stack conflict policy): generated, never edited upstream
    subprocess.run([sys.executable, str(HERE / "patch_hostdata.py")], check=True)
    text, version = bump_patch(PANEL.read_text(encoding="utf-8"))
    PANEL.write_text(text, encoding="utf-8")

    name = f"SHODAN-Stat-Editor-Offline-local-{version}"
    os.environ["SSEO_CHANNEL"] = "local"
    if not os.environ.get("SSEO_COMMIT"):
        commit = subprocess.run(["git", "-C", str(REPO), "rev-parse", "--short", "HEAD"],
                                capture_output=True, text=True).stdout.strip()
        dirty = subprocess.run(["git", "-C", str(REPO), "status", "--porcelain"],
                               capture_output=True, text=True).stdout.strip()
        os.environ["SSEO_COMMIT"] = commit + ("+local" if dirty else "")

    # upstream's packer, with its panel swapped for the generated one
    source = (REPO / "offline" / "package.py").read_text(encoding="utf-8")
    patched = source.replace(
        "PANEL = os.path.join(ADDON, 'stat_editor_offline.lua')   # build.py --offline",
        f"PANEL = {str(PANEL)!r}   # local build")
    if patched == source:
        raise SystemExit("offline/package.py changed: it no longer sets PANEL where this expects")
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
    try:
        shutil.copy2(made, target)
    except PermissionError:      # the previous zip is open somewhere (Explorer's preview, an archiver)
        stamp = datetime.datetime.now().strftime("%H%M%S")
        target = OUT / (made.stem + f"-{stamp}" + made.suffix)
        shutil.copy2(made, target)
        print(f"note: {made.name} was locked; wrote {target.name} instead")
    # Unpack into a folder of its own first. The previous build may be running from the canonical
    # folder (its .exe and DLLs are locked), and deleting files there before knowing that would leave
    # a half-deleted build behind.
    stamp = datetime.datetime.now().strftime("%H%M%S")
    folder = OUT / f"SHODAN Stat Editor Offline ({stamp})"
    with zipfile.ZipFile(target) as archive:
        names = [n for n in archive.namelist() if not n.endswith("/") and "/" in n]
        for name in names:
            out_path = folder / name.split("/", 1)[1]
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_bytes(archive.read(name))

    # the patched host file goes over the one the packer copied
    patched = HERE / "build" / "hostdata.lua"
    if patched.exists() and (folder / "app" / "hostdata.lua").exists():
        shutil.copy2(patched, folder / "app" / "hostdata.lua")

    # ...then refresh the canonical folder file by file, leaving whatever is in use alone
    canonical = OUT / "SHODAN Stat Editor Offline"
    skipped = 0
    if canonical.exists():
        for source in sorted(folder.rglob("*")):
            if source.is_dir():
                continue
            target_file = canonical / source.relative_to(folder)
            target_file.parent.mkdir(parents=True, exist_ok=True)
            try:
                shutil.copy2(source, target_file)
            except PermissionError:
                skipped += 1
    if not canonical.exists():
        canonical = folder                      # first pack: the timestamped folder is the build
    elif skipped:
        print(f"note: {skipped} file(s) are in use by the running build; the full new build is {folder.name}")
        print(f"      ({canonical} got everything else; close the editor and pack again to refresh it)")
    print(f"\n{target}")
    print(f"{canonical}  (run it from here)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
