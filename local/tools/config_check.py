"""Check a config.txt the way the panel reads it: every line, what it does, what it cannot.

The panel ignores what it does not recognise, so a typo in a setting or a stat id that no longer
exists is silently dropped - and the change you thought you had just is not there. This reads the
file with the panel's own rules (same keys, same value shapes) and reports:

  * unknown setting names and unknown line shapes (with a "did you mean" for near misses)
  * values the panel would clamp or reject
  * overrides whose weapon hash or stat id is not in the panel's current build (the dump says which)
  * passive_stack / passive_every references to passives that are not in this build
  * lines the panel writes itself that a hand edit could have broken

    python tools/config_check.py                          # %LOCALAPPDATA%\\SHODAN\\StatEditor\\config.txt
    python tools/config_check.py path\\to\\config.txt --panel local/cache/panel-26088801.tsv
    python tools/config_check.py --quiet                  # exit code only

Exit code 1 when something would be dropped or misread (so it can gate a script); 0 when the file
means what it says. The idea (strict checking with helpful messages, plus --check without a window)
comes from Super-Earth-Armory-Forge's offline editor, which validates loadout.ini with the mod's own
parser.
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
CACHE = REPO / "cache"

# the setting names the panel's load_config understands (src/stat_editor_offline.lua)
SETTINGS_ONOFF = {"changes", "block_input", "arc_chains_multiplayer", "unlock_unused", "several_vehicles",
                  "stratagem_bounce", "foliage_pass_through", "sniper_crosshair"}
SETTINGS_TEXT = {"hotkey", "update_channel", "updates", "lang", "editor", "last_tab", "last_weapon",
                 "enemy_tab", "enemy_page", "panel_side", "hide_tabs", "remember", "check_updates",
                 "panel_lang", "update_size"}
SETTINGS_NUMBER = {"panel_size", "panel_opacity"}
SETTINGS_PASSIVE = {"passive_stack", "passive_own", "passive_conflicts", "passive_every"}
ALL_SETTINGS = SETTINGS_ONOFF | SETTINGS_TEXT | SETTINGS_NUMBER | SETTINGS_PASSIVE
# written by this fork's overlays (they read them itself; the panel skips them)
FORK_KEYS = {"passive_conflicts", "passive_every"}

ONOFF = {"on", "off"}


def panel_ids(tsv: Path) -> tuple[set[str], dict[str, set[str]], set[int]]:
    """(weapon hashes, {hash: stat ids}, passive ids) from a panel dump."""
    weapons, stats, passives = set(), {}, set()
    for line in tsv.read_text(encoding="utf-8", errors="replace").splitlines():
        parts = line.split("\t")
        if parts[0] == "WEAPON" and len(parts) > 3:
            weapons.add(parts[1].upper())
            stats.setdefault(parts[1].upper(), set())
        elif parts[0] == "ROW" and len(parts) > 2:
            stats.setdefault(parts[1].upper(), set()).add(parts[2])
        if parts[0] == "WEAPON" and len(parts) > 1 and parts[1].startswith("FFFFFFFE"):
            # a passive page's hash is FFFFFFFE<passive id>: that is where the passive ids come from
            passives.add(int(parts[1][8:], 16))
    return weapons, stats, passives


def close(word: str, options) -> str | None:
    """A 'did you mean' for a near miss (their editor does the same for keys and passives)."""
    def norm(s: str) -> str:
        return "".join(ch for ch in s.lower() if ch.isalnum())
    best, score = None, 0.0
    for option in options:
        a, b = norm(word), norm(option)
        if not a or not b:
            continue
        # Ratcliff-Obershelp-ish: the longest common subsequence ratio is enough here
        m, n = len(a), len(b)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = dp[i - 1][j - 1] + 1 if a[i - 1] == b[j - 1] else max(dp[i - 1][j], dp[i][j - 1])
        ratio = 2 * dp[m][n] / (m + n)
        if ratio > score:
            best, score = option, ratio
    return best if score >= 0.75 else None


def check(path: Path, weapons: set[str] | None, stats: dict[str, set[str]] | None,
          passives: set[int] | None) -> tuple[list[str], list[str], list[str]]:
    """(errors, warnings, info) - errors are lines the panel would drop or clamp."""
    errors, warnings, info = [], [], []
    text = path.read_text(encoding="utf-8", errors="replace")
    for number, raw in enumerate(text.splitlines(), 1):
        line = raw.split("#", 1)[0].strip()
        if not line:
            continue
        where = f"line {number}"
        parts = line.split()
        head = parts[0]
        if head in ALL_SETTINGS:
            value = parts[1] if len(parts) > 1 else ""
            if head in SETTINGS_ONOFF and value not in ONOFF:
                errors.append(f"{where}: {head} wants on/off, got '{value}'")
            elif head in SETTINGS_NUMBER:
                try:
                    v = float(value)
                    if head == "panel_opacity" and not (20 <= v <= 100):
                        warnings.append(f"{where}: panel_opacity {v} is outside 20-100 (the panel clamps it)")
                    if head == "panel_size" and not (50 <= v <= 200):
                        warnings.append(f"{where}: panel_size {v} is outside 50-200 (the panel clamps it)")
                except ValueError:
                    errors.append(f"{where}: {head} wants a number, got '{value}'")
            elif head == "panel_side" and value not in {"left", "right"}:
                errors.append(f"{where}: panel_side wants left/right, got '{value}'")
            elif head == "editor" and value not in {"enemy", "stat"}:
                errors.append(f"{where}: editor wants stat/enemy, got '{value}'")
            elif head == "update_channel" and value not in {"releases", "commits"}:
                errors.append(f"{where}: update_channel wants releases/commits, got '{value}'")
            elif head == "updates" and value not in {"ask", "auto", "off"}:
                errors.append(f"{where}: updates wants ask/auto, got '{value}'")
            elif head in {"passive_stack", "passive_every"}:
                if len(parts) < 3:
                    errors.append(f"{where}: {head} wants '<passive id> <id,id,...>'")
                else:
                    try:
                        target = int(parts[1])
                        members = [int(x) for x in parts[2].split(",") if x.strip()]
                    except ValueError:
                        errors.append(f"{where}: {head} wants numbers, got '{line}'")
                        continue
                    if passives is not None:
                        for pid in [target] + members:
                            if pid not in passives and pid != 0x7E000001:   # (0x7E000001 = Every armor)
                                errors.append(f"{where}: {head} names passive {pid}, not in this build")
            elif head == "passive_own":
                if len(parts) < 3 or parts[2] != "off":
                    errors.append(f"{where}: passive_own wants '<passive id> off'")
            elif head == "passive_conflicts":
                if value not in {"stack", "strongest"}:
                    errors.append(f"{where}: passive_conflicts wants stack/strongest, got '{value}'")
            elif head == "hide_tabs":
                if len(parts) < 2:
                    errors.append(f"{where}: hide_tabs wants a list of tabs")
            continue
        if head in FORK_KEYS:
            continue
        # an override: <weapon hash> <stat id> <value>
        if len(parts) == 3 and len(head) == 16 and all(c in "0123456789ABCDEFabcdef" for c in head):
            weapon, stat, value = head.upper(), parts[1], parts[2]
            try:
                float(value)
            except ValueError:
                errors.append(f"{where}: value '{value}' is not a number")
                continue
            if weapons is not None and weapon not in weapons:
                errors.append(f"{where}: weapon {weapon} is not in this build (renamed or removed?)")
            elif stats is not None and weapon in stats and stat not in stats[weapon]:
                near = close(stat, stats[weapon])
                errors.append(f"{where}: {weapon} has no stat '{stat}'" + (f" (did you mean '{near}'?)" if near else ""))
            continue
        # anything else: a setting name the panel does not know?
        near = close(head, ALL_SETTINGS)
        if near:
            errors.append(f"{where}: unknown setting '{head}' (did you mean '{near}'?)")
        elif len(parts) == 2 and head not in ALL_SETTINGS:
            errors.append(f"{where}: '{head} {parts[1]}' is not a line this panel reads")
        else:
            errors.append(f"{where}: cannot read '{line[:60]}'")
    return errors, warnings, info


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("config", nargs="?", help="config.txt (default: %LOCALAPPDATA%\\SHODAN\\StatEditor)")
    ap.add_argument("--panel", help="panel dump TSV to check ids against (default: newest in local/cache)")
    ap.add_argument("--quiet", action="store_true", help="no output, only the exit code")
    args = ap.parse_args(argv)

    path = Path(args.config) if args.config else Path(os.environ.get("LOCALAPPDATA", "")) / "SHODAN" / "StatEditor" / "config.txt"
    if not path.exists():
        print(f"no config at {path}", file=sys.stderr)
        return 2
    tsv = Path(args.panel) if args.panel else (sorted(CACHE.glob("panel-*.tsv")) or [None])[-1]
    weapons = stats = passives = None
    if tsv and Path(tsv).exists():
        weapons, stats, passives = panel_ids(Path(tsv))
    errors, warnings, info = check(path, weapons, stats, passives)

    if not args.quiet:
        print(f"{path}")
        if tsv and Path(tsv).exists():
            print(f"  ids checked against {Path(tsv).name}")
        overrides = 0
        for raw in path.read_text(encoding="utf-8", errors="replace").splitlines():
            parts = raw.split("#", 1)[0].split()
            if len(parts) == 3 and len(parts[0]) == 16:
                overrides += 1
        print(f"  {overrides} override(s)")
        for title, items in (("errors", errors), ("warnings", warnings), ("notes", info)):
            for item in items:
                print(f"  {title[:-1]}: {item}")
        if not (errors or warnings):
            print("  everything in it is a line the panel reads")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
