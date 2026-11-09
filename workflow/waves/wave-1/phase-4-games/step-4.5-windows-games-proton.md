---
type: step
description: "Windows DRM-free games start like any other: umu-launcher + GE-Proton, one prefix per game, never named in the interface; a 'preparing…"
phase: "[[phase-4-games]]"
step: "4.5"
status: done
legacy: "ROADMAP.md 4.5"
tags: [step, phase-4]
---
# 4.5 Windows games (Proton) *(added 2026-10-11)*

Up: [[phase-4-games]] · Status: **done**

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
  for Windows?" [Try] [Cancel]; Try sets Proton (Valve's, which Steam downloads itself: owner,
  2026-10-18, [[steam-integration]]) for that game in Steam (Steam closed and reopened:
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
- **Second part, broken Linux versions of Steam games (2026-10-18):** Steam's line for Dragon's
  Wake read on the FrankenPC (`LaunchApp failed with AppError_28` in `logs/console_log.txt`).
  owneetd 0.14.4 (`steamwindows.go`, [[owneetd-api-apps]]): `steam.launch_failed`, Steam's error
  kept hidden; `{"windows": appid}` closes Steam, sets Valve's newest Proton for the game in
  `config.vdf` and starts it again. owneet-frontend 0.21.3: the demo's question ("{title} does not
  start" [Try] [Cancel]), "Starting …" kept while Steam starts again. Go tests
  (`TestSteamWindowsVersion` and the log, tool and `config.vdf` readers); preview
  `tools/preview-steps/steam-broken-linux.txt`. FrankenPC test pending (Steam downloading its
  Proton the first time is shown by Steam after 20 s).
- **FrankenPC, broken Linux version (owner, 2026-10-18):** works: the question, Try, Dragon's Wake
  starts with Proton (a second start goes straight in). Two fixes in owneetd 0.14.5: Steam's window
  was shown for about 25 s while Steam downloaded the game's version for Windows and Proton (45 s):
  Steam now stays hidden while its console log says it works on the launch, and is shown only for
  a question it waits on; and the Proton chosen was 5.13 (`proton_513`, a number larger than 11):
  newest by app id now. Dragon's Wake keeps Proton 5.13 on the FrankenPC (it works; the console
  does not change a tool already set).
- **Regression check (FrankenPC, 2026-10-18, owneetd 0.14.5):** Dragon's Wake and Silksong start
  without Steam's window. **Owner, 2026-10-18:** a game keeps the Proton it works with (Dragon's
  Wake keeps 5.13); another version is offered only if problems come after an update of the game
  ([[steam-integration]]). Approved: "Starting …" shows the percentage of what Steam downloads
  before a game starts.
- **Download percentage (2026-10-18):** demo 4.5 updated ("Starting {game}…" with "Steam is
  downloading what the game needs: N%" and a bar), **approved by the owner on 2026-10-18**.
  owneet-frontend 0.21.4: Steam's active downloads (its queue left out) in one percentage while
  the screen is up; no "ready" banner for the game being started or running. Preview
  `tools/preview-steps/steam-broken-linux.txt`. FrankenPC: seen the next time Steam downloads
  something before a game starts.
- **Outcome: approved by the owner on 2026-10-18** after the FrankenPC tests: Windows and DOS
  games on a disk start like the others (GE-Proton through umu-launcher, downloaded once; GOG's
  DOS games with DOSBox Staging), and a Steam game whose Linux version does not start gets the
  console's question and runs with Valve's Proton, Steam hidden throughout ("Starting …" with the
  download percentage). Left as known: a short black flash before Windows games (not a
  priority); one GPU fault (Xid 79) seen once, watched. Follow-up: the player's own
  compatibility layers, [[wave-2]] item 17.
- **Reported by the owner (FrankenPC, 2026-11-09, 13:11-13:17), open, serious:** The Witcher 2 (GOG, Windows) lost the controller
  and could not get it back; leaving it with Guide without closing it, the cutscene's sound went on. What the logs say: the game's
  window ("The Witcher 2", pid 7863) was the one gamescope focused (GAMESCOPE_FOCUSED_WINDOW) whenever it was on screen; Steam was
  running (opened at 13:07:20), so its virtual controller existed; Wine's invisible input-only window (1438x898, depth 0, override)
  came with the game (the pointer's capture). "Resume with the pointer" was turned on over "The Witcher 2 Launcher" and off by
  itself 4 s later when the game's own window replaced it (by design: the pointer holds for one window). Lead, not proved: a game
  started outside Steam reads Steam's virtual controller (which sends nothing) instead of the real one. The Proton log has no input
  channel. Asked to the owner: when the control was lost and what was on screen; whether the game should pause or go silent on the
  home screen; a run with Steam closed.
- **Owner's answers (2026-11-09):** the control was lost right after the launcher: the splash and the intro film showed normally
  but could not be skipped, the input ignored. **Decision:** a game left open on the home screen (Guide) goes **silent** (not
  paused: not every game can be). Test now: The Witcher 2 started with Steam closed since the power-on (OWNEETLOG plugged in).
- **Cause confirmed (owner's test, FrankenPC, 2026-11-09 15:35):** with Steam never opened, The Witcher 2's controller works every
  time. Facts gathered: Steam's virtual controller is `28de:11ff` (Valve's "Steam Virtual Gamepad"), bus USB, version 1, name
  "Microsoft X-Box 360 pad 0", made through uinput (test VM, Steam with a test pad: `/sys/class/input/input9`); Steam's log: "Created
  virtual controller at slot 0". Since Proton 11, Valve's patch makes Proton read every evdev device itself, past SDL's filter, so
  `SDL_GAMECONTROLLER_IGNORE_DEVICES` alone would not hide it (a Bottles report, not verified here); the remedy reported is the
  prefix's winebus setting `DisableInput` = 1 (Wine's own default: controllers through SDL, which leaves out 28de:11ff). Not
  verified yet: Windows' controller panel (joy.cpl) did not start through owneet-windows-run in the test VM (the prefix was not
  made), and the VM's debug shell stopped answering. Waits for the owner's choice of how to verify.
- **Remedy verified in the test VM (owner's choice, 2026-11-09 16:40-17:05):** Steam open with the test pad, so Steam's virtual
  controller existed; two new prefixes, a program run through owneet-windows-run with Wine's controller log
  (`WINEDEBUG=+hid,+plugplay`). Without the setting, Proton's own evdev reading "detected steam input virtual controller" and made
  it a gamepad (`28de:11ff`), **enumerated before** the real pad, which SDL added second: the game's first controller is
  Steam's silent one, as with The Witcher 2. With `DisableInput` = 1 in
  `HKLM\System\CurrentControlSet\Services\winebus` (set with the prefix's `reg.exe`): "UDEV input devices disabled in
  registry", no `28de:11ff`, the real pad through SDL is the only gamepad. Still to see on real hardware: a Bluetooth
  controller through SDL alone in a game (The Witcher 2, Steam open). Found on the way: the test VM's `umu-shim` was empty, so
  no Windows program had started there since 2026-11-08 ([[windows-games-quit-at-once-empty-umu-shim]]). Waits for the
  owner's go-ahead to build it.
- **Fix built (owner's go-ahead, 2026-11-09; owneetd 0.25.9, code `bc68be7`):** while building it, Proton's own switch
  `PROTON_NO_STEAMINPUT=1` was found (read by winebus; Proton's comment: "suppress the desktop virtual controller and leave
  the game's native controller path active"). Tested in the test VM like `DisableInput`: "ignoring steam input virtual
  controller", the real pad through SDL the only gamepad. It was chosen over `DisableInput` because it gives the same result
  with no registry write and no extra Wine start at each launch, works for prefixes made before, and leaves Proton's other
  input paths as Valve made them. `owneet-windows-run` exports it; checked again with the installed package (fresh prefix,
  Steam open). Waits for the owner's test on FrankenPC: The Witcher 2 with Steam open.
- **Broken umu-shim repaired by the console (owner's go-ahead, 2026-11-09; owneetd 0.25.10, code `77f35a7`):**
  `owneet-windows-run` removes umu's shim when it would not start the game, and umu writes it again
  ([[windows-games-quit-at-once-empty-umu-shim]]). Tested in the test VM (empty, cut short, intact).
- **Owner's test on FrankenPC (2026-11-09, 19:56-20:05; owneetd 0.25.10):** The Witcher 2 with Steam open: the controller
  works. **New report, open:** while the game starts, the game and the home screen take the screen in turn and the "launch"
  sound plays several times (on closing it now plays on time). Logs (`out/test-logs/frankenpc-2026-11-09g`), three starts:
  in the first seconds gamescope's focus went game → home → game up to four times (gaps of 30-370 ms, while the launcher's
  and the game's windows come and go): with no window of the game to show, gamescope shows the home screen, owneetd
  announces "home" and the interface plays the "back home" sound. Also: after Guide (19:57:48) the game came back by itself
  1.4 s later with no "back to the app": its first window had not settled yet, and owneetd brings a just-started app to the
  front when the home screen is what was chosen last, which Guide also sets. The same gaps were in the 15:35 test (0.25.8,
  Steam closed); before 0.25.7 "on screen" was not logged. Waits for the owner's choice of the fix.
- **Correction (2026-11-09):** the game coming back 1.4 s after Guide (19:57:49) was not owneetd: nothing in owneetd brought
  it, so it was almost surely the home screen's Resume, which left no line in the log (it does now: "back to the app, asked
  by the interface").
- **Fix built (owner's terms, 2026-11-09: no flashes, no fixed times, the sound once; owneetd 0.25.11, code `ac772d9`):**
  the owner turned down both a "Preparing {game}…" screen and a black screen in the gaps (both flash). gamescope 3.16.31's
  source (`steamcompmgr.cpp`, `pick_primary_focus_and_override` and `determine_and_apply_focus`) shows that when
  `GAMESCOPECTRL_BASELAYER_APPID` names only apps with no window, gamescope does not fall back to another window: it keeps
  the window it showed while that window exists, and when it is gone it paints its last picture (`HELD_COMMIT_BASE`), with
  `GAMESCOPE_FOCUSED_APP` empty. So a game started by the console now goes **alone** in that list (it was "game, home"):
  before its first window the home screen ("Preparing {game}…") stays; between two of its windows the last picture of the
  game stays, nothing is announced, no sound; Guide shows the home screen; at its end (its unit stopped) the home screen
  comes back. Apps keep the home screen behind them (an app may go on without a window, e.g. Steam in the background);
  Steam's games keep Steam behind them (its questions come in its window, as on SteamOS). Known effects: quitting from the
  game's own menu, its last picture stays until its process has ended (280-400 ms with The Witcher 2), then the home
  screen and the sound together; a game left running with no window at all keeps its last picture until Guide. Checked with
  unit tests (the test double now keeps the shown window like gamescope); not seen on a screen yet: gamescope does not run
  in the test VM without a 3D GPU. Waits for the owner's test on FrankenPC.
