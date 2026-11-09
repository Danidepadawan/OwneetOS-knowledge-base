---
type: step
description: "Steam runs hidden; the console lists every owned Steam game from Steam's local caches, installs it through Steam's own confirmation and shows the download itself."
phase: "[[phase-4-games]]"
step: "4.2c"
status: done
tags: [step, phase-4]
---
# 4.2c Steam without its interface *(owner, 2026-10-14)*

Up: [[phase-4-games]] · Status: **done**

Why: with the NVIDIA driver, Steam's own window shows glitches (pictures left over or not
finished) that no setting removed; games are not affected ([[step-4.2b-updates-from-a-usb-stick]]).
The console keeps Steam's interface off the screen in everyday use ([[steam-integration]]).

- **Deliverables:**
  - Steam runs **hidden** (no window: `-silent`) and starts games when the console asks; its window
    is shown only when Steam needs the user (login, Steam Guard, a licence to accept at a game's
    first start, a cloud conflict, a choice of launch options), as today.
  - **Every owned Steam game** in the console's library, installed or not, from Steam's local
    caches, offline: licences in `appcache/packageinfo.vdf`, app types in `appcache/appinfo.vdf`
    (binary, v28/v29), artwork in `appcache/librarycache`. Owned = a game in one of the account's licences,
    package 0 (Spacewar, Team Fortress 2, Dota 2, given to everyone) and free weekends left out
    (since 2026-10-14, after the FrankenPC test; before: packages with `status` 0, which is the
    store's offer, not the ownership).
    Checked on the owner's account: 88 games and 2 soundtracks, as Steam's own library shows.
  - In the library ([[game-library]]): not-installed games dimmed with a download mark (A
    installs, X details; downloads first in "Recent"); the **"Installed" filter** comes back; a
    Steam game on a disk that is not connected shows "On a disk that is not connected" (from
    `libraryfolders.vdf`).
  - **Installing** through Steam's official address `steam://install/<appid>`: the console asks
    "Install {game}?", then Steam's confirmation window appears briefly; with the NVIDIA driver
    the console first says that a temporary display problem may show in that window, every time
    until the user ticks "Don't show again" (owner's choice, option a; writing Steam's own files
    to start a download was turned down). The console then shows the download and updates
    itself, from the `appmanifest` files (state, bytes downloaded / to download): on the cover,
    in the details, in the home screen's notices, and a banner when the game is ready.
  - **Uninstalling** without Steam's interface: Options → "Uninstall" (and "Cancel installation"
    while downloading) through `steam://uninstall/<appid>`, with the same question and notice.
  - **No internet:** an action that needs it (Steam's first download, signing in, installing) is
    blocked with a clear message and a way to the network settings. Fixes today's behaviour
    offline: the "Preparing Steam" screen disappears after a second (Steam's first window, its
    error, closes it in `daemon/internal/apps/apps.go` `checkWindows`) and its last words say
    Steam opens by itself.
  - "Add games → Steam" and the store open as Steam's official website in the browser app
    ([[step-5.1-brave-in-the-os]]) instead of Steam's interface, when that app exists; until then,
    Steam's store, after the same notice on PCs with the display errors.
  - Demo of the new screens (owned games, installing, download progress, uninstalling, the
    NVIDIA notice, no internet) approved before the code ([[demo-before-code]]): proposal agreed
    on 2026-10-14, demo `design/demos/4.2c-steam-library.html` **approved on 2026-10-14**.
- **Done when:** on the FrankenPC, everyday use (browsing the library, installing, starting and
  closing a game, coming back with Guide) never shows Steam's own window except for its
  confirmation when installing or uninstalling; the library matches Steam's own count; without
  internet, Steam's actions say so and are blocked.
- **Outcome:** **approved by the owner on 2026-10-15** after the FrankenPC tests (Steam's window
  clean with the repaint overlay, permanent on NVIDIA). Reopened if Steam's display defects come
  back. Left for later: a game on a disk that is not connected, checked once disks are mounted
  automatically ([[step-6.5-automatic-disk-mounting]]). *(Code done and verified in the VMs on
  2026-10-14.)*
  - **owneetd** (`daemon/internal/apps/steam.go`, `steamlib.go`): `GET /v1/steam` gives downloads,
    games on a disk not connected, account, licences, NVIDIA; `POST /v1/steam` `install` /
    `uninstall`; event `steam.changed`; Steam hidden while it starts a game, shown after 20 s
    without a game; home screen back once Steam acts on its confirmation ([[owneetd-api-apps]]).
  - **Frontend**: `SteamOwned.cpp` reads every owned game from `packageinfo.vdf` + `appinfo.vdf`
    ([[frontend-steam-local-files]]); the theme shows states, progress, the Installed filter,
    install / uninstall / cancel with the console's questions and the notice ("Don't show again"
    kept in the theme's memory), the offline block, the downloads notice on the home screen, the
    "ready" banner, and reads its games again when Steam has a game it does not list or the
    licences changed after a visit to the store. "Add games → Steam" opens the store.
  - **Verified**: Go tests (new: confirmations back home, hidden start, downloads and disks,
    KeyValues), `tools/lint` all passed; the binary readers against the owner's real caches (88
    games + 2 soundtracks, prototype) and an invented Steam folder (`tools/preview-steps/fake-steam.py`);
    `tools/frontend-preview` with `tools/preview-steps/library-steam.txt` (20 screenshots: every
    state of the approved demo) and `library-add-games.txt` (no regression).
  - **Deviations**: Steam is kept hidden by owneetd (gamescope shows only what owneetd chooses),
    not with `-silent`, because owneetd hands Steam its first address once Steam's window exists.
    The home screen's rows (hero, recently played) show installed games only (not covered by the
    demo; confirmed by the owner on 2026-10-14, [[game-library]]). Fixed on the way: an icon shown after the first drawing
    (the network icon) was sometimes left blank.
  - **Not verifiable in the VM** (FrankenPC test): Steam really hidden while it starts a game and
    shown when it needs the user; `steam://install` / `steam://uninstall` confirmations in
    `-gamepadui` and the return home after confirming; what Steam shows after **cancelling** its
    confirmation (expected: holding Guide comes back); download states and bytes from a real
    download (one active, others queued; an update); a game on a disk that is not connected
    (unplug the 2 TB HDD with a game on it); Steam's first start blocked without a cable or Wi-Fi.
  - **FrankenPC test (2026-10-14, owner)**: library faithful except two games (Mafia III, an
    ended free weekend, listed; PAYDAY 2, from a package no longer offered, missing): fixed, the
    rule above (88 games, PAYDAY 2 installs). Installing (Dragon's Wake), the "ready" banner,
    uninstalling, the offline block: as expected; the home screen comes back by itself after a
    confirmation, holding Home after cancelling one. Steam's confirmations are unreadable on
    NVIDIA: the notice now says what to press (install and uninstall, on every PC). Starting
    Silksong, Steam was shown after 20 s while it prepared the game's shaders (Fossilize, about
    45 s): owneetd now waits while `fossilize_replay` runs, and the console's "Starting …" screen
    covers every Steam start. Disk not connected: waits for automatic mounting (phase 6).
  - **Licence agreements** (owner, 2026-10-14): games whose agreement Steam asks to accept at the
    first start (e.g. Batman: Arkham Knight) cannot be read in Steam's window on NVIDIA. The
    console knows them from `appinfo.vdf` (common → eulas: id, name, official address) and
    `localconfig.vdf` (apps → APPID → "APPID_eula_N": accepted) and, before that first start,
    shows its own window: the agreement's address as a QR code (to read on a phone; the browser
    app later, 5.1) and what to press ("in Steam's window, press Left and then A to accept":
    Steam's selection starts on "Decline", and the console does not move it). owneetd then shows
    Steam at once for that start (`ask`). QR codes: Project Nayuki's library (MIT), credited.
  - The notice before Steam's confirmations got its own memory: a "Don't show again" given to the
    earlier notice (the owner's, by mistake) does not hide the new one.
  - **Steam's install window also asks for the disk** (owner, 2026-10-14): guiding the user
    blind does not work. There is no official API to drive Steam's windows (Steam's internal
    `SteamClient` API used by Decky / Millennium means modding the client: guard [[legal]];
    `steamcmd` needs a second sign-in). **Test (owner's agreement, 2026-10-14):** another
    console session (deckshift, PR 8) saw the same stale parts of Steam's window on NVIDIA,
    unaffected by `--force-composition` or `-cef-disable-gpu`, and gone with a layer that changes
    every frame (MangoHud made transparent): gamescope then composes every frame. owneetd 0.12.3
    does that without MangoHud (`daemon/internal/apps/repaint.go`): while Steam's own window is
    on screen, on NVIDIA, with the test switch `owneet.debug.steam_repaint=on`, a one-pixel, all
    but transparent window marked `GAMESCOPE_EXTERNAL_OVERLAY` changes every frame. Checked on
    Xvfb in the builder VM (no X errors); gamescope's behaviour only on the FrankenPC. If it
    works, Steam's window is readable again and the blind guidance of this step is reconsidered
    with the owner.
  - **FrankenPC, 2026-10-14/15**: with the switch (on the stick) Steam's window was clean, a
    little slower ("decidedly acceptable"); the five starts without the stick had the glitches
    again, as expected (the switch lives on the stick). **Owner, 2026-10-15:** the repaint becomes
    permanent on every NVIDIA PC (owneetd 0.12.4; `owneet.debug.steam_repaint=off` turns it off
    to compare), until Valve fixes the problem; if it does not hold, it is reverted. Then the
    other bugs the owner found come first, the visual defects of Steam afterwards.
- **Steam's window before a game's (owner, 2026-10-17):** starting Silksong, Steam's window (with
  its defects) was on screen for about 10 s between the game's start and its window: owneetd put
  Steam right behind the game, and gamescope shows the first window there is. There is no per-game
  signal to wait for, but there is one for every game: its window appearing. owneetd 0.14.3 keeps
  Steam's window out (also from Steam's own requests) until the game's window is there, then puts
  Steam back behind it; after 20 s without a game window Steam is shown (it may be asking the
  user something). The console's "Starting …" screen stays until the game's window appears
  (owneet-frontend 0.21.2). Go test `TestSteamStaysBehindAGameWithoutWindow`. **FrankenPC
  (owner, 2026-10-17): passed**: Silksong started from "Starting …" straight into the game,
  Steam's window never on screen (no repaint in the log).
- **Reported by the owner (FrankenPC, 2026-11-09), open:**
  - **Fault:** Batman: Arkham Knight (115 GB, on the 2 TB disk) showed "Waiting" on its cover while Steam was at 4%, until the
    power-off. Cause found in the report's snapshots: Steam rewrites `appmanifest_208650.acf` only now and then while it
    downloads (BytesDownloaded moved twice in 11 minutes, 09:36:33 and 09:37:02) and its StateFlags there never say "running",
    so owneetd saw no bytes moving and said "queued". Steam's `content_log.txt` tells each state at once ("App update changed :
    Running Update,Downloading,Staging"; "Suspended"; "None"), and the download folder (`steamapps/downloading/<appid>`) grows
    as Steam writes. To be fixed.
  - **Nice to have (Wave 1 if easy):** a percentage, or at least "Preparing", while Steam prepares a download before it starts
    (reconfiguring, verifying, preallocating, the shader cache: more than a minute of "Waiting" for Arkham Knight).
  - **Fault, not reproduced yet:** on FrankenPC one press of A on "How to come back from Steam" also confirmed "Before Steam
    opens" (NVIDIA) right after it (owner, 2026-11-09). Test VM (2026-11-09, owneetd made to report NVIDIA): with the keyboard each
    window takes its own press (Install → the first notice → the second, waiting). The interface acts on the press, ignores
    repeats, and gets the controller as one device; the cause is to be found on the hardware (a log of each A taken by a window).
- **Fixes (owner's go, 2026-11-09; code commit 78390c0):** owneetd 0.25.5: a download's state comes from Steam's
  `logs/content_log.txt` while Steam runs ("App update changed : …Downloading…" is downloading; None, Suspended, cancelled,
  the game's preparation and its shader cache are not), and its bytes from the room Steam takes on its library disks since the
  measures began (every 3 s, one statfs per disk), added to what the appmanifest said then: before a Windows game Steam writes
  Proton, its runtime and common files into the main library, counted in the game's download (test VM: the game's own folders
  stayed empty while 1.3 GB were written). owneet-frontend 0.38.2: a window (Dialog) ignores an A within 0.3 s of its opening and
  logs each A it takes or ignores ("Window \"…\": A on button 0, 8419 ms after opening"; "A ignored, 31 ms after opening").
  Go tests (state from the log, bytes from the disks, a resumed download, no step back after a deletion). **Test VM (owner signed
  in):** Among Us onto "GamesVM Games": "downloading" from the first second (before: "queued"); paused at 99% it showed queued at
  99.5% as Steam did; two A 31 ms apart: the second ignored, the notice stayed. Not seen in the VM: a long download's bytes
  growing between manifest writes (the VM downloaded at 66 MB/s). **Waits for the owner's test on FrankenPC** (Arkham Knight).
  "Preparing" with a percentage stays a nice-to-have (demo first).
- **Reported by the owner (FrankenPC, 2026-11-09), open:** Details of Batman: Arkham Knight showed "Time left: about 116 min".
  From an hour up it must read hours and minutes ("about 1 h 56 min"): `details.left.minutes` is used for every length
  (`theme.qml`, the Details rows); a message with hours and minutes is added in the five languages.
- **Owner's test on FrankenPC (2026-11-09, 10:44-11:09):** Batman: Arkham Knight resumed: "downloading" from the first moment, the
  bytes growing in every snapshot (4.97 GB at 10:44 to 22.3 GB at 11:09, about 15 MB/s); owner: apparently passed, to be confirmed by
  finishing it and installing another game. The double A seen for real: `Window "Come tornare da Steam": A ignored, 47 ms after
  opening` (10:44:47, Steam not running yet: not its virtual controller), the next A taken 2 s later: one press of the controller
  can reach the interface twice about 50 ms apart; the guard holds it. Waits for the owner's last checks.
- **The guard in every window (owner, 2026-11-09: "no half solutions"):** owneet-frontend 0.38.3 (code commit after 78390c0) moves it
  into `Nav`: Dialog, Sheet, the quick menu, the clock, both on-screen keyboards (a physical Enter too) and the hold button take no A
  for 300 ms after a window opens; "A ignored, … ms after a window opened" in the log. Test VM: a game's Options and the quick menu
  with two A 22 and 33 ms apart (the second ignored, nothing started), a normal A after a second works. The on-screen keyboards and
  the hold button use the same check, not tried by hand in the VM.
- **Audit of the fixed waits (2026-11-09, [[waiting-for-events]]), open:** waits where a fixed time stands for an event, to be
  replaced by the event (code as of commit e7b0edb):
  - owneetd: a window shown after it stays 3 checks (`settleChecks`, `steamPageChecks`, Steam's flicker); a hidden Steam shown when
    no game came after 20 s (`steamAskAfter`); Steam's own questions taken as the user's after 3 s (`steamAnswerWait`); a download
    "moving" when its bytes grew in the last 5 s (`steamMoving`, now only when Steam's log does not name it); the pointer's shape read
    120 ms after a click (`textDelay`).
  - Interface: Wi-Fi "searching" for 20 s (`scanTimer`); "last played" read again 3 s after a game is asked for (`refreshTimer`); the
    text for a web app sent 400 ms after its window is back (`pointerSend`); "Add games" kept selected for 4 s while the disks come
    (`addGamesHold`); the start-up animation waiting 2.5 s for the screen (`introHold`).
  Kept as they are (limits, repeat intervals, chosen durations): the wait for apps before power-off (25 s at most), systemd's stop
  limits, SIGKILL after 5 s, retries every 2 s, the checks every 0.25-3 s, the notices' and toasts' times, holds and repeats of
  buttons, "stuck" after 10 minutes without writing, the display's 15 / 30 s confirmations.
- **The fixed waits replaced (owner's go, 2026-11-09; code commit 8d3e276; owneetd 0.25.6, owneet-frontend 0.38.4):**
  - By the event: a question for the user shows Steam as soon as its console log says "waiting for user response to …" (Steam's
    own routine questions, ShowInterstitials and CreatingProcess, named from every launch in FrankenPC's logs; no 3 s); a launch
    that ends without a game ("Completed" or a failure) shows Steam at once; a game without its window shows Steam behind it when
    the log asks the user; a download moves when Steam's log says so (no 5 s rule; nothing moves while Steam is closed); the
    pointer's shape follows the X server's cursor events (XFixes CursorNotify; a click asks the keyboard at once when the pointer
    is the "I", or when the app makes it so before the pointer moves: no 120 ms); the recent games follow the games' own changes
    (`dataChanged`); the text for a web app goes on "focus.changed"; "Add games" stays selected until the games are read
    (`Internal.scanner.running`).
  - Kept, commented: as safety limits, Steam's launch not named in its log after 20 s, a game without a window after 2 min, the
    Wi-Fi search after 20 s (it ends on "wifi.scan_done"); as no event exists, Steam's window steadiness (3 checks: Steam logs
    neither its flicker's end nor the page it shows) and the start-up animation's wait (nothing tells when the monitor shows the
    picture: the duration tried with the owner).
  - Go tests (Steam's user question at once, a failed launch, the routine questions, downloads by the log, the pointer's shape
    by events, no keyboard after a move). Test VM: the interface starts without errors. **Waits for the owner's test on FrankenPC.**
- **Time left in hours and minutes, fixed (2026-11-09; owneet-frontend 0.38.5):** from an hour up "about 1 h 56 min"; whole hours
  "2 h" with no "about" (owner); under an hour as before. The same for how long a game or a web app has been open on the home
  screen ("Playing for 1 h 56 min", "Open for 2 h"), which had the same fault. Five languages; checked with the message files
  (it, en, de). **Waits for the owner's test on FrankenPC.**
