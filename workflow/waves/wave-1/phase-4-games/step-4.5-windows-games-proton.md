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
- **FrankenPC test 2 (2026-10-16):** the black flash is Wine's console window (`conhost.exe`: GOG's
  DOSBox is a console program, and so may be Proton's launcher for Linux paths): it is now never
  shown (owneetd 0.13.3). GE-Proton also started Xalia (the controller as a mouse in Windows
  programs): turned off (`PROTON_USE_XALIA=0`), as no mapping is added inside games. DOSBox loads
  and ends after about 1.5 s; the debug log now lists the files opened (`+file`) to tell a missing
  GOG configuration from a game that cannot write in its read-only folder.
- **FrankenPC test 3 (2026-10-16):** the debug log shows DOSBox not finding GOG's configuration
  (`..\dosboxT2K.conf`: not found), so it mounts nothing and `-c exit` closes it. The files were in
  `__support/app/`: a real GOG installation copies them to the game's folder (the
  `supportData` action of `goggame-<id>.script`), `innoextract` does not. Done by hand on the
  owner's SSD (owner's permission, 2026-10-16) for the three games; installers (step 4.6) will run
  those actions. GOG's DOSBox setup also mounts `..\cloud_saves` as an overlay for saves (cannot
  exist on a read-only disk: no saves until 6.5, option B), and Tyrian 2000 opens GOG's own menu
  that needs the keys 1–4 (left as GOG made it). A short black flash is still there before the
  games (not a priority, owner).
- **FrankenPC test 4 (2026-10-16):** Stargunner runs; pressing Home made GOG's DOSBox (the 2010
  Windows build 0.74, under Proton) end with a divide-by-zero (0xC0000094) two seconds after it
  lost the focus, while "Close Stargunner?" was open: the home screen took the focus and the
  window could not be answered, and a "closed unexpectedly" notice came → owneet-frontend 0.20.2
  (a window keeps the focus; "Close …?" goes, without a notice, when its game ends by itself).
  Tyrian 2000 ends right after "1" in GOG's menu (exit code 0; Proton's log not copied): probably
  it cannot write its files on the read-only disk (Stargunner only warned about STARGUN.CFG, .HI,
  .SAV). Proposal for the owner: GOG's DOS games with a native DOSBox instead of GOG's Windows
  one.
- **Native DOSBox for GOG's DOS games (owner, 2026-10-16, [[games-on-disk]]):** a GOG game whose
  play task starts `dosbox.exe` is a DOS game (`disk.dos`, no Proton, no download):
  `owneet-dos-run` (owneetd 0.14.0) copies it once to `~/.local/share/owneet/dos/<game>/game`
  with GOG's starting saves (`__support/save`), rewrites GOG's configuration files' `[autoexec]`
  mounts to Linux paths (backslashes, any case; GOG's `cloud_saves` overlay dropped: the copy is
  writable) and runs Arch's `dosbox` (owneet-base 0.0.37, CREDITS) full screen; owneet-frontend
  0.21.0. Checked on the builder VM with a stub DOSBox.
- **FrankenPC test 5 (2026-10-16):** the update needs `dosbox` (and `umu-launcher` before) from Arch
  online, and at start-up the network is not up yet: it failed at boot and was installed from
  Settings → System once online (to improve for testers: say that an update waits for the
  network). With Linux's DOSBox, Tyrian 2000 starts and plays; Stargunner shows a black screen
  (Home goes back and forth, the console closes it). Both close from the home screen.

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
- **Stargunner's black screen (2026-10-16):** on the builder VM (virtual screen, Tyrian as a check)
  Arch's DOSBox 0.74.3 hangs at Stargunner's Sound Blaster 16 detection whatever the display
  settings; it starts without sound or with a Sound Blaster Pro 2. DOSBox Staging 0.83.0's
  official build starts it with GOG's settings (Tyrian too; its box-drawing characters need GOG's
  CP437 configuration files turned into UTF-8). Owner: option A (per-game fixes refused) →
  DOSBox Staging packaged from source (with iir1 and libmt32emu, checksums checked against the AUR
  recipes: [[supply-chain-security]]), GOG's overlay instead of the copy.
- **DOSBox Staging packaged (2026-10-16):** `packages/dosbox-staging` 0.83.0 (sources checked
  against the AUR recipes), owneetd 0.14.1 (`owneet-dos-run`: overlay instead of copy, CP437 →
  UTF-8), owneet-base 0.0.38, CREDITS. On the builder VM, with the package installed and the games
  read only: Stargunner reaches its titles with the Sound Blaster 16 on, Tyrian's menu draws its
  boxes. FrankenPC test pending (the update needs Arch's libraries online: install it from
  Settings → System).

- **FrankenPC test 6 (2026-10-17):** the update installed at start-up from the stick alone, with
  the Arch packages on it ([[step-4.2b-updates-from-a-usb-stick]]; DOSBox Staging as
  `dosbox-staging`, owneetd 0.14.2). **Owner: everything works**: Stargunner and Tyrian 2000 play,
  Home goes back and forth, both close from the home screen. Once, at 17:44, the PC froze 0.2 s
  after DOSBox Staging opened its window: the NVIDIA driver reported Xid 79 ("GPU has fallen off
  the bus"), a GPU or PCIe fault seen once in 43 starts; the same start worked afterwards. Watched:
  if it comes back, look at the GPU's power and PCIe settings with the owner.
