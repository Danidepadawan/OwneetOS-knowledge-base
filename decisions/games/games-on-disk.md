---
type: decision
description: "The Games folder convention, Windows games through hidden Proton, background installers, licence prompt."
area: games
status: active
decided: 2026-10-11
updated: 2026-10-19
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
  - **Proton and its runtime** (a download of about 650 MB, 2.3 GB on disk) stay out of the ISO: downloaded once, in the
    background, the first time the console is online **with a Windows game in the library** (as
    soon as one appears; owner 2026-10-16: no download for users without Windows games) — "a
    necessary evil", the **only exception to C9** ([[hard-constraints]]). Until then a Windows
    game says it needs a download, needed only the first time. Its progress is shown in the home
    screen's notices and in Settings → System; a banner says when Windows games are ready. The
    texts give the real size, "about 650 MB" (owner, 2026-10-16: be precise).
  - **Which file starts a Windows game:** GOG's `goggame-<id>.info` (its primary play task: file,
    arguments, working folder), else the same choice as for Linux games ([[step-4.5-windows-games-proton]]).
- **GOG's DOS games** (owner, 2026-10-16): GOG ships them with its own DOSBox for Windows; the
  console starts them with **DOSBox Staging**, built by OwneetOS from source
  ([[supply-chain-security]]), never with Proton (no download needed for them). *(The same day,
  Arch's DOSBox 0.74.3 was tried first: Stargunner hung at its Sound Blaster 16 detection.)* GOG's
  own configuration files are used; their "cloud_saves" overlay (where a game's writes go) points to
  a folder of that game on the console's disk while the game's disk is read only, seeded with GOG's
  starting saves: the game runs from its disk, never copied, and the disk is never written. From
  [[step-6.5-automatic-disk-mounting]] the overlay folder is GOG's own `cloud_saves` next to the
  game, so saves travel with the disk; overlay folders made before go there, nothing is lost.
  ([[step-4.5-windows-games-proton]])
- **Saves of games on a USB disk** (owner, 2026-10-16, option B): until
  [[step-6.5-automatic-disk-mounting]] mounts disks read-write, games that save in their own
  folder cannot save there (the disk is read only); no workaround (the step only checks that the
  games run).
  - **Installers run by themselves, in the background**, silently with their known options. Because
    a silent install accepts the game's licence for the user, the console first shows "By
    installing you accept the game's licence" [Read] [Install] (the user is informed, the project
    is covered).
  - **How (owner, 2026-10-19, [[step-4.6-installers]]):** games are installed on the console's
    disk, in its games folder, under the same folder name (USB disks stay read only until
    [[step-6.5-automatic-disk-mounting]]). GOG's Linux `.sh` (MojoSetup) are **extracted**, never
    run: their `data/noarch` is the installed game (no installer code runs; no desktop shortcuts);
    Windows installers (Inno Setup, e.g. GOG's `setup_*.exe`; NSIS; MSI) **run silently under
    Proton** in the game's prefix, so the publisher's scripts run too. `innoextract` reads an
    Inno Setup installer's total size, for the percentage (option B). [Read] shows the licence's
    text when the console finds it, in the game's folder or inside the installer, else says where
    it is (option C1). Installers the console cannot use (online ones such as GOG Galaxy's, unknown
    kinds) are **shown** in the library with a message that they cannot be used yet (option D).
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
| 2026-10-16 | GOG's DOS games run with Linux's DOSBox (Arch's `dosbox`), from a copy on the console's disk (they can write and save), not with GOG's Windows DOSBox under Proton (it ended when the home screen was shown; Tyrian could not write). |
| 2026-10-16 | The DOS games' copy on the console's disk is temporary: from step 6.5 they run in place with their saves (several disks included); the copy only for disks left read only; its saves go back to the game. |
| 2026-10-16 | GOG's DOS games: DOSBox Staging built from source (Arch's DOSBox could not start Stargunner); GOG's cloud-saves overlay on the console's disk replaces the copy of the game; from step 6.5 it is GOG's `cloud_saves` next to the game. |
| 2026-10-19 | Installers (step 4.6): installed on the console's disk; GOG's Linux `.sh` extracted (never run), Windows installers run silently under Proton; `innoextract` for the percentage; [Read] shows the licence's text when found; installers that cannot be used are shown with a message. |
| 2026-10-16 | The download's texts say "about 650 MB" (the measured size), not "about 1 GB". |
| 2026-10-16 | Demo 4.5 proposal: Proton is downloaded only once a Windows game is in the library; its progress in the home notices and Settings → System; GOG's `goggame-*.info` says which file starts a Windows game; games on a USB disk do not save in their own folder until step 6.5 (option B). |
| 2026-10-11 | Proton and its runtime are downloaded once, in the background, the first time the console is online ("a necessary evil": the only exception to C9, for Windows games before the first connection). Installing a game from an installer first shows "By installing you accept the game's licence" [Read] [Install] (the user is informed, the project is covered). Step 4.1 approved. |
