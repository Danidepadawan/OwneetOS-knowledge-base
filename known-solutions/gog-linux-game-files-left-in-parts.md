---
type: known-solution
description: "A big GOG Linux game installs but cannot start (its launcher aborts, its data seems missing): GOG ships a file too big for the archive in parts (FILE.split00 …) that its postinst.sh joins, and the console, which never runs the installer's scripts, left them in parts."
status: solved
seen: 2026-11-11
updated: 2026-11-11
tags: [known-solution, installers, gog]
---
# GOG Linux game files left in parts

## Symptom

A GOG Linux game installed by the console does not start: the screen stays black a couple of
seconds and the game closes with no message (FrankenPC, 2026-11-11: The Witcher 2's
`tenfoot-launcher` aborted with `std::logic_error: basic_string::_S_construct null not valid`).
In the game's folder, files named `*.split00`, `*.split01`, … and `support/split_files`.

## Cause

GOG's Linux installer cannot hold a file over about 4 GB whole: it ships it in parts and lists it in
`support/split_files`; its `support/postinst.sh` joins the parts after MojoSetup has copied them
(`cat FILE.split* > FILE`). The console extracts the installer's archive and never runs its scripts
(owner, 2026-10-19), so the parts stayed: The Witcher 2's main data, `game/CookedPC/pack0.dzip`
(10.5 GB), was missing.

## Solution

owneetd 0.25.23 (`daemon/internal/installs/archive.go`, `joinSplitFiles`): after the extraction,
each file of `support/split_files` is joined: the first part becomes the file, the others are
appended in their names' order and removed one by one (`copy_file_range`: on btrfs the blocks are
shared, so no space is used twice). A path outside the game is refused. Games installed before
are uninstalled and installed again.

## How we found it

- The 32-bit SDL2 made `tenfoot-launcher` start, then it aborted; nothing in its libraries was
  missing.
- owneet-base 0.0.65's test log copies each Linux game's small scripts to the stick: `game/launcher`
  runs `./saferun.sh ./desktop-launcher`, and `support/postinst.sh` joins `support/split_files`.
- The disk listing of the same start: `game/CookedPC/pack0.dzip.split00`, `.split01` (4 GB each),
  `.split02` (2.1 GB), no `pack0.dzip`.
- Test VM: a GOG-like installer with a 3 GB file in three parts: joined with the same SHA-256 in
  9 s, the disk's free space down by the game's size only.

## Watch out

Anything else GOG's `postinst.sh` may do for other games is not done either: read it (the test log
copies it) when a GOG Linux game misbehaves after its install.
