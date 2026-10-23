# local/ — this fork's own layer

Everything here is **added** to the project; nothing upstream is edited. `git pull` from the
project's `main` therefore never conflicts: the only files it can touch are ones this folder does
not contain.

```
local/
  panel/*.lua       appended to the panel by build_panel.py (this is where new stats go)
  build_panel.py    src/stat_editor_offline.lua + panel/*.lua  ->  build/panel.lua (not committed)
  tools/            per-build pipeline: unseal tables, type library, field names, headless run, report
  run_all.py        all of it, in order
  build_luajit.bat  builds LuaJIT (lua51.dll, luajit.exe) with the local MSVC
  cache/            plaintext tables per build, panel dump, names (not committed)
  report/           field-gaps-<build>.md: every member of every record, editable or not
  runtime/          libsodium.dll (not committed)
  third_party/      LuaJIT checkout + build (not committed)
  .venv/            uv venv with pynacl (not committed)
```

**Handover notes** (environment, data facts, the add-a-stat procedure, pitfalls): `../../hd2data/docs/07-sseo-extension.md` (essentials) and `../../hd2data/docs/09-sseo-handover.md` (everything).
**The game's data model** (LDLD blocks, type ids, hash correction, the weapon data chain): `../../hd2data/docs/01-game-model.md`; all of it: `../../hd2data/index.md`.

## Why this shape

`src/stat_editor_offline.lua` is one 15 000-line Lua chunk and upstream changes it several times a
week (13 commits in two days in October 2026). Editing it in place means re-resolving conflicts
after every pull. Instead:

* upstream files stay byte-identical to `main`;
* `local/panel/*.lua` is spliced onto the **end of that chunk**, so the chunk's own locals
  (`add_row`, `part`, `field_at`, `weapons`, `tables`, `KINDS`, `TYPES`, `resolve`, `resolve_gun`,
  `MOD.langs`, ...) are in scope and extra stats can be added by wrapping those functions;
* `local/build_panel.py` produces the panel that is run and packaged (`local/build/panel.lua`);
* after a pull, run `python local/run_all.py` — it re-derives every offset from the installed
  build instead of trusting last build's numbers, and fails loudly if something moved.

The generated panel is what to install: `local/build/panel.lua` replaces `app/stat_editor.lua`.

## The pipeline

```bash
# one-time
uv venv local/.venv && uv pip install --python local/.venv/Scripts/python.exe pynacl
cmd /c local\build_luajit.bat            # needs the VS Build Tools

# every time the game updates (or you want the current numbers)
local/.venv/Scripts/python.exe local/run_all.py
```

| step | tool | reads | writes |
|---|---|---|---|
| 1 | `tools/dump_plain.py` | `data/game/*.dl_bin`, `dl_library.dl_typelib` | `cache/plaintext-<build>/` |
| 2 | `tools/typelib.py` | that typelib | `cache/typelib-<build>.json` |
| 3 | `tools/go_names.py` | FileDiver's `datalibrary/*.go` | `cache/go_names.json` |
| 3b | `tools/wiki_names.py` | the wiki's decoded dumps (`cache/wiki-modules`) | `cache/wiki-names.json` |
| 3c | `tools/known_names.py` | hd2-datamined's `table_export.py` + 3b | `cache/known-names.json` |
| 4 | `build_panel.py` | `src/stat_editor_offline.lua` + `panel/*.lua` | `build/panel.lua` |
| 5 | `tools/panel_dump.lua` (LuaJIT) | the game's files + that panel | `cache/panel-<build>.tsv` |
| 6 | `tools/field_report.py` | all of the above | `report/field-gaps-<build>.md` |

### Decrypting: whose keys

`data/game/*.dl_bin` are NaCl sealed boxes. The game's own recipient key pair is in
`offline/gamedata.lua` (PK/SK), and `tools/dump_plain.py` reads it from there — this folder holds no
keys of its own. libsodium is used through `pynacl`, or through a `libsodium.dll` if one is found
(`offline/runtime/libsodium.dll`, the SSEO install folder).

### Where the names come from (four dictionaries, in priority order)

| | source | covers | how a name is guaranteed |
|---|---|---|---|
| 1 | the panel's own stat labels | 139 members — exactly what it edits | it is the text in the panel |
| 2 | `cache/known-names.json` | settings rows: damage, projectile, explosion, status, beam, arc, stratagem, attachments | curated layouts from hd2-datamined + the wiki's field names, and the wiki ones only after they matched real values (`wiki_names.py`) |
| 3 | `cache/go_names.json` | components | FileDiver's Go struct, matched by offset **and** size; if the struct drifted, a size-sequence alignment is used and every name it produces ends in `?` |
| 4 | — | blank | no dictionary covers it (the six components FileDiver has no struct for, and members added after the wiki dumps) |

The type library itself has no names: AH stripped its string table after 2024-02-23, so every
member is only `offset / size / type id`. A trailing `?` means "inferred, verify before trusting";
a blank means "no source — the offset and values are still exact".

`wiki_names.py` needs the wiki's dumps, which are the wiki's content and are not vendored:

```bash
python ../ref/hd2-datamined/tools/fetch_wiki_modules.py --out local/cache/wiki-modules
```

### Type names

Member names come from the dictionaries above; *type* names are separate and simpler:
`tools/names/dl_type_names.txt` (FileDiver's list) hashed with `typelib.type_hash` (a djb2 variant,
verified against the panel's own table ids).

## The report

`report/field-gaps-<build>.md`

1. **Candidates** — numeric members of records the panel already reads that it cannot edit, with the
   values a dozen real rows hold (`f32` where the bits are a plausible float, `id`/hash members left
   out on purpose).
2. **Every member** of every such record, `✗` where the panel has no stat, plus which panel rows
   already edit it.
3. **Tables the panel never parses** — every other LDLD block in the game's files, with its record
   type, record size and an approximate row count.

## The record tables

`tools/record_table.py` writes one table per settings record, straight from the build's files:

```
report/damage-table-<build>.md/.csv        661 rows: damage, durable, four AP angles, demolition,
                                           stagger, push, 4 status slots + strengths
report/explosion-table-<build>.md/.csv     448 rows: type, damage row, three radii, shrapnel
                                           count + projectile, and the rest of the record
report/projectile-table-<build>.md/.csv    355 rows: type, pellets, velocity, drag, gravity,
                                           damage row, explosions, penetration slowdown, ...
report/status-table-<build>.md/.csv         79 rows: type (Burning 5, Gas 43/44, stuns 38-41),
                                           duration and the rest of the status record
```

Each row is one id, with who uses it (weapon / stratagem pages, or the explosions and projectiles
that point at it), the damage row's value where one is linked, and every scalar member. `·` is zero.
The `.csv` beside each `.md` has every member, including structs, so it filters well in a
spreadsheet.

## Headless run

`tools/panel_dump.lua` does what `offline/host.lua` does, without a window: it decrypts the game's
files into the process (`offline/hostdata.lua`), loads the panel with the Stingray/GUI calls stubbed
out, ticks it until every weapon is resolved and writes what the panel found. It only reads the game
folder; nothing is installed. Set `SHODAN_LOCAL_TEST` (it does) to get `_test` on the panel's state,
which exposes `fields`, `weapons`, `tables`, `KINDS`, the raw reader and `HEADER_BYTES` to the dump.

## Packaging a test build

```bash
cmd /c localuild_exe.bat                 # once: launcher .exe + shodan_hash.dll (MSVC), LuaJIT -> offline/runtime
local/.venv/Scripts/python.exe local/package_exe.py
```

`build_exe.bat` builds exactly what upstream's CI builds (same LuaJIT commit, same sources) and puts the
outputs where upstream expects them (`offline/launcher`, `offline/runtime`); `package_exe.py` then runs
upstream's own `offline/package.py` with the *generated* panel swapped in, and copies the zip plus an
unzipped folder into `local/build/`:

```
local/build/SHODAN Stat Editor Offline/SHODAN Stat Editor Offline.exe   <- run this
local/build/SHODAN-Stat-Editor-Offline-local-<version>.zip
```

Two deliberate differences from a release build: the panel's version is bumped one patch level (so the
updater does not offer to replace this build with the official release of the same version), and
`app/build.txt` names the commit with `+local` when the working tree is dirty. The packaged panel leaves
out `panel/*_test.lua` — that hook is only for the headless harness. Presets, saved values and the game's
originals are shared with any other install, since they live in `%LOCALAPPDATA%\SHODAN\StatEditor`.

## What this build adds to the panel

`panel/10_calibre_mass.lua` — **calibre (+24) and mass (+36)** of a shot's projectile record, on each
weapon page, right after "Projectiles per shot":

```
Projectile:  Projectiles per shot | Calibre (mm) | Mass (kg) | Velocity (m/s) | Drag | Gravity | ...
```

It wraps `add_row`, so the rows land in the right section and order for every shot of a charge
weapon as well (`c1_calibre`, `c2_mass`, ...), and the ids follow the panel's naming, so saved
values and presets keep working. Weapons whose page is a record page already had both.

`panel/20_beam_range.lua` — **beam range** (BeamSettings +8: the 15 m a Meltagun reaches) for every
weapon whose damage comes from a beam record. It wraps `resolve_gun` and adds the row right after
the shot's damage / status rows, in a "Beam" section; a weapon that has a beam component but fires a
projectile does not get it (the same test `resolve_gun` makes). Today that is 9 pages: LAS-5 Scythe,
LAS-7 Dagger, LAS-13 Trident, LAS-22 Shear, LAS-98 Laser Cannon (and its crewed mount), A/LAS-98
Laser Sentry, AX/LAS-5 "Guard Dog" Rover, 40-K Meltagun.

**Shrapnel count** (explosion +80) was already on the weapon pages — `MOD.records.shrapnel_rows`
adds it with the shrapnel projectile (+84) for every explosion a weapon's shot sets off, under
"Shrapnel". A weapon with no shrapnel still has the rows (count 0), so shrapnel can be added: set
the count *and* the projectile id.

Note: an overlay part must not declare chunk-level `local`s — upstream's chunk already sits at
LuaJIT's 200-local limit — and `build_panel.py` wraps every part in `do ... end` for the same reason.
Scratch values go in `state` (or a global).

### Write/read-back test

`tools/panel_dump.lua` takes an optional fourth argument, a file of `hash stat-id value` lines, and
applies each one through the panel's own writer (`write_field`), then reads it back:

```bash
printf 'A8A91EB54892B6B2 calibre 20
' > /tmp/sets.txt
luajit local/tools/panel_dump.lua "<game>/data/game" local/build/panel.lua /tmp/out.tsv /tmp/sets.txt
grep ^SET /tmp/out.tsv        # SET <hash> <id> <ok> <old> <new>
```

The writes go to this process's decrypted copy of the tables; nothing is installed.

## Adding stats later

`panel/*.lua` runs after the panel is defined, so, for example:

```lua
-- wrap a resolver, then append rows of your own to the weapon it just built
local base_resolve_gun = resolve_gun
resolve_gun = function(weapon, key)
    base_resolve_gun(weapon, key)
    add_row(weapon, 'Handling', 'aim_block', 'Aim block length', 'f32',
            { part('aim_block', T_WEAPON, (tables[T_WEAPON].index[key] or 0) + 108, 'f32', 1000) },
            0, 1000, 0.1, 1)
end
```

Rules that keep saved values working: stat ids are permanent (config.txt and presets name them),
`part()` fields are `kind:offset` in the record, and a value the game stores but the panel shows in
other units needs a `row.span`/`rate` pair like the existing time rows.

Overlay parts are spliced inside the same chunk, so a `do ... end` block keeps the chunk's
top-level local count unchanged (LuaJIT allows 200 active locals per function and the chunk is
already at 172).
