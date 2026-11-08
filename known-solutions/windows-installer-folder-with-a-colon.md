---
type: known-solution
description: "A Windows installer ends after a few seconds and the console says Windows games are not ready: the game's folder name has a character Windows refuses (\":\" in \"The Witcher 2: Assassins of Kings\")."
status: solved
seen: 2026-11-08
updated: 2026-11-08
tags: [known-solution, windows, installers]
---
# A Windows installer ends at once: a ":" in the game's folder

## Symptom

On FrankenPC (2026-11-08), installing The Witcher 2 (GOG, Inno Setup, several `.bin` parts) from the 2 TB disk: no "GB written",
a banner "Windows games are not ready, try again" (`error.install.windows`), then the cover says "Not installed" again. In the
journal: `owneet-install-<hash>.service: Main process exited, code=exited, status=3/NOTIMPLEMENTED` about 6 seconds after
`Executable is a unix path, launching with 'umu.exe'`, then owneetd `install did not finish ... reason=windows err="Windows games are
not ready yet"`. Proton was ready (GE-Proton started, `wineboot --init` ran). Other GOG installers (Tyrian 2000, Treasure Adventure
Game) worked.

## Cause

Two faults on top of each other:

1. The game's folder in the home folder is named after the game: `/home/owneet/Giochi/The Witcher 2: Assassins of Kings Enhanced
   Edition`. The installer gets it as `/DIR=Z:\home\owneet\Giochi\The Witcher 2: Assassins…`, and **":" is not allowed in a
   Windows file name** (nor `< > " | ? *`). Inno Setup, run silently, cannot use the folder and ends with its exit code 3.
2. owneetd read **any** exit code 3 as owneet-windows-run's "Proton is not ready" (its own code 3), so the real failure was
   reported as "try again later".

## Solution

owneetd 0.25.2 (step 6.8, [[step-6.8-games-on-disk-delete-and-progress]]):

- `daemon/internal/installs/windows.go`: a folder whose name has a character Windows refuses (`winRefused`) is given to the
  installer through a link without it (as NSIS and MSI already were for spaces), kept with the game.
- `installs.Manager.WindowsReady` (wired to `windows.Manager.Ready`, the Proton made ready is still there): checked before the
  installer runs, and an exit code 3 means "not ready" only when that check agrees; otherwise the install failed.

## How we found it

1. `grep -iE 'install|witcher|umu|proton' owneet-…journal.txt`: the unit started Proton and ended with status 3 after 6 s; the
   daemon logged `reason=windows`.
2. `owneet-windows-run` exits 3 only when `~/.local/share/owneet/windows/proton` is missing, but the journal shows Proton running:
   so the 3 came from the installer.
3. Inno Setup's exit code 3 is "a fatal error while preparing the next phase"; the `/DIR=` it got had a ":" in the folder name.

## Watch out

- Any game whose title has `: < > " | ? *` (common: "Title: Subtitle"). Its installed copy is reached through the link; the
  folder itself keeps the title.
- Never give a meaning to an exit code that the program run inside may also return: check the condition directly.
- Not yet seen on hardware after the fix: the next FrankenPC test of The Witcher 2 confirms it.
