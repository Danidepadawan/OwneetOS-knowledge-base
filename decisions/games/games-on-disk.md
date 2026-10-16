---
type: decision
description: "The Games folder convention, Windows games through hidden Proton, background installers, licence prompt."
area: games
status: active
decided: 2026-10-11
updated: 2026-10-16
legacy: "PROJECT_RULES.md §6 (Games on a disk), §10, §13 (2026-10-11)"
tags: [decision, games]
---
# DRM-free games on a disk (Wave 1)

- **Games folder:** a folder named `Games`, or its name in the chosen language (e.g. `Giochi`), at
  the top of any disk or USB stick, and on the console's own disk; one folder per game, named after
  the game, with **any sub-folders** inside. The console searches it (recursively) for what to
  start or install; a cover (`cover.jpg` / `cover.png`) and a `game.txt` (title, file to start,
  description) are optional. When the choice is not clear, the console asks once, with the
  controller, and remembers (helpers, uninstallers, redistributables are never offered).
- **Whatever their form**: ready to run or with an installer, for Linux or for Windows.
  - **Windows games:** umu-launcher + GE-Proton, one prefix per game, **never named in the
    interface** (at most a "preparing the game" screen while it loads).
  - **Proton and its runtime** (about 1 GB) stay out of the ISO: downloaded once, in the
    background, the first time the console is online — "a necessary evil", the **only exception
    to C9** ([[hard-constraints]]). Until then a Windows game says it needs a one-time download.
  - **Installers run by themselves, in the background**, silently with their known options. Because
    a silent install accepts the game's licence for the user, the console first shows "By
    installing you accept the game's licence" [Read] [Install] (the user is informed, the project
    is covered).
- "Add games" also offers "From a USB stick or disk" ([[game-library]]).
- **In the library** (demo 4.3 proposal, owner 2026-10-15): the title is the game folder's name as
  the user wrote it (or `game.txt`'s), never rewritten; the file to start is asked once when there
  are several, and can be changed from Options; Windows games appear with step 4.5 and folders
  with only an installer with step 4.6 (until then they are not shown).
- **`game.txt`** (owner, 2026-10-15): `key: value` lines with English keys: `title`, `start` (the
  file to start, relative to the game's folder), `description`; `#` starts a comment. A file
  chosen from Options wins over `start`. Details: [[frontend-disk-games]].
- **Games made for a mouse and keyboard** (owner, 2026-10-16, after Beneath a Steel Sky on the
  FrankenPC): left exactly as their developers made them; the console adds no pointer or mapping
  inside games, which could spoil the game. The controller pointer of
  [[step-4.7-controller-pointer]] stays for the windows it lists (installers, launchers), never in
  games.

Steps: [[step-4.3-local-drm-free-games]], [[step-4.5-windows-games-proton]], [[step-4.6-installers]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-11 | **Wave 1 scope grows** ([[disks]] and 10): DRM-free games on a disk play whatever their form (ready to run or installer, Linux or Windows through umu-launcher + GE-Proton, hidden from the user); installers run by themselves in the background; moving games and media between disks (new step 6.6). Games folder: `Games` or its translated name, one folder per game with any sub-folders, searched recursively. "Add games" also offers "From a USB stick or disk". |
| 2026-10-15 | Demo 4.3 proposal: title = the folder's name as written (the user's control); the file to start asked once and changeable from Options; Windows games shown from step 4.5, installers from step 4.6. |
| 2026-10-15 | `game.txt`: `key: value` lines, keys `title`, `start`, `description`; the file chosen from Options wins over `start`. |
| 2026-10-16 | Games made for a mouse and keyboard are left as their developers made them: no pointer or mapping added inside games; the controller pointer (step 4.7) is never offered in games. |
| 2026-10-11 | Proton and its runtime are downloaded once, in the background, the first time the console is online ("a necessary evil": the only exception to C9, for Windows games before the first connection). Installing a game from an installer first shows "By installing you accept the game's licence" [Read] [Install] (the user is informed, the project is covered). Step 4.1 approved. |
