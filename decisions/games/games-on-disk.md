---
type: decision
area: games
status: active
decided: 2026-10-11
updated: 2026-10-11
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

Steps: [[step-4.3-local-drm-free-games]], [[step-4.5-windows-games-proton]], [[step-4.6-installers]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-11 | **Wave 1 scope grows** ([[disks]] and 10): DRM-free games on a disk play whatever their form (ready to run or installer, Linux or Windows through umu-launcher + GE-Proton, hidden from the user); installers run by themselves in the background; moving games and media between disks (new step 6.6). Games folder: `Games` or its translated name, one folder per game with any sub-folders, searched recursively. "Add games" also offers "From a USB stick or disk". |
| 2026-10-11 | Proton and its runtime are downloaded once, in the background, the first time the console is online ("a necessary evil": the only exception to C9, for Windows games before the first connection). Installing a game from an installer first shows "By installing you accept the game's licence" [Read] [Install] (the user is informed, the project is covered). Step 4.1 approved. |
