---
type: step
description: "Windows DRM-free games start like any other: umu-launcher + GE-Proton, one prefix per game, never named in the interface; a 'preparing…"
phase: "[[phase-4-games]]"
step: "4.5"
status: in-progress
legacy: "ROADMAP.md 4.5"
tags: [step, phase-4]
---
# 4.5 Windows games (Proton) *(added 2026-10-11)*

Up: [[phase-4-games]] · Status: **in-progress**

- **Started (owner, 2026-10-16).** Test games: free DRM-free Windows-only games from GOG, unpacked
  from their installers with `innoextract` on the owner's PC (installed by the owner) and put in
  the SSD's `Giochi/` folder, next to the two Linux games: Treasure Adventure Game (a Windows
  program), Tyrian 2000 and Stargunner (DOS games in GOG's DOSBox for Windows). Each has GOG's
  `goggame-<id>.info` (primary play task, e.g. `DOSBOX\dosbox.exe` with `-conf` arguments and
  working folder `DOSBOX`; the file is really `DOSBox.exe`: paths are matched without case).
- **Demo proposal agreed (owner, 2026-10-16, [[games-on-disk]]):** Windows games in the library
  like other games on a disk ("Local", never "Windows" or "Proton"); the file to start from GOG's
  info file, else the Linux games' choice (never setup, uninstallers, configurators such as
  `GOGDOSConfig.exe`, `__redist`); the download (about 1 GB, needed only the first time) starts
  the first time the console is online with a Windows game in the library: "Getting Windows
  games ready: 45%" in the home screen's notices and in Settings → System, a banner when ready;
  starting a Windows game before it is ready shows the progress, and offline asks to connect
  ([Network settings] [Cancel]); "Preparing {game}…" until the game's first picture, plus "The
  first start takes a little longer" the first time; the Steam question for a broken Linux
  version. Games on a USB disk do not save in their own folder until step 6.5 (option B).
  Demo: `design/demos/4.5-windows-games.html`.
- **Demo approved (owner, 2026-10-16).** Code written 2026-10-16, first part (games on a disk):
  owneetd 0.13.1 (`/v1/windows`, the download with umu-launcher, `owneet-windows-run`; windows
  without a usable `_NET_WM_PID` tagged through X-Resource), owneet-frontend 0.20.0 (Windows games,
  GOG's info file, the notices, Settings → System, "Preparing…"), owneet-base 0.0.35 (umu-launcher,
  CREDITS). Design: [[owneetd-api-windows]], [[frontend-disk-games]]. Checked in the preview and,
  for umu-launcher's download, on the builder VM. About 650 MB are downloaded (2.3 GB on disk):
  the texts say "about 650 MB" (owner, 2026-10-16). Second part still to do: the Steam question
  for a broken Linux version.
- **FrankenPC test 1 (2026-10-16):** the download works (about 2.5 minutes). Treasure Adventure
  Game starts, after a short black flash of the screen (bearable, not pleasant); Stargunner and
  Tyrian 2000 show DOSBox's screen and close after 5–9 seconds, with nothing in the logs. Either
  DOSBox does not find GOG's configuration, or the DOS game cannot write in its folder (the disk
  is read only) → owneet.debug.windows_log=on (tester switch) writes Proton's log and DOSBox's
  messages (owneetd 0.13.2, owneet-base 0.0.36 copies them to the stick).

- **Deliverables:** Windows DRM-free games start like any other: umu-launcher + GE-Proton, one
  prefix per game, never named in the interface; a "preparing the game" screen until the game's
  first picture. Credits and licences (Wine LGPL, Proton BSD, DXVK / VKD3D-Proton zlib/LGPL).
- **Decided (owner, 2026-10-11; refined 2026-10-16):** Proton and its runtime (about 1 GB) stay out of the ISO:
  downloaded once, in the background, the first time the console is online with a Windows game in the library; until
  then a Windows game says that it needs a one-time download (the only exception to C9).
- **Broken Linux versions of Steam games (owner, 2026-10-13):** some Steam games ship a Linux
  version that cannot start (e.g. Dragon's Wake, 399070: its Linux files lack the executable its
  launch settings name; Steam says "Missing game executable"). owneetd notices the failed launch
  in Steam's log and the console asks "This game's Linux version does not start. Try the version
  for Windows?" [Try] [Cancel]; Try sets Proton for that game in Steam (Steam closed and reopened:
  it saves the setting only while closed) and starts it again. Demo first; checked on real
  hardware with the owner's account (it reads an undocumented Steam log).
- **Note:** shader pre-compilation exists only for Steam games (Steam's own "Processing
  Vulkan shaders"); other games compile while they play, so the "preparing" screen covers the
  start only.
