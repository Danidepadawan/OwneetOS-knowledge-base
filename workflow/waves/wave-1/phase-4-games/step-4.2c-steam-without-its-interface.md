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
