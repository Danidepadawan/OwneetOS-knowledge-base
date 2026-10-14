---
type: step
description: "Steam runs hidden; the console lists every owned Steam game from Steam's local caches, installs it through Steam's own confirmation and shows the download itself."
phase: "[[phase-4-games]]"
step: "4.2c"
status: in-progress
tags: [step, phase-4]
---
# 4.2c Steam without its interface *(owner, 2026-10-14)*

Up: [[phase-4-games]] · Status: **in-progress**

Why: with the NVIDIA driver, Steam's own window shows glitches (pictures left over or not
finished) that no setting removed; games are not affected ([[step-4.2b-updates-from-a-usb-stick]]).
The console keeps Steam's interface off the screen in everyday use ([[steam-integration]]).

- **Deliverables:**
  - Steam runs **hidden** (no window: `-silent`) and starts games when the console asks; its window
    is shown only when Steam needs the user (login, Steam Guard, a licence to accept at a game's
    first start, a cloud conflict, a choice of launch options), as today.
  - **Every owned Steam game** in the console's library, installed or not, from Steam's local
    caches, offline: licences in `appcache/packageinfo.vdf`, app types in `appcache/appinfo.vdf`
    (binary, v28/v29), artwork in `appcache/librarycache`. Owned = a game in an active licence
    (`status` 0), package 0 (Spacewar, Team Fortress 2, Dota 2, given to everyone) left out.
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
- **Outcome:** *(2026-10-14, code done and verified in the VMs; waiting for the FrankenPC test and
  the owner's approval)*
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
    demo: to be confirmed by the owner). Fixed on the way: an icon shown after the first drawing
    (the network icon) was sometimes left blank.
  - **Not verifiable in the VM** (FrankenPC test): Steam really hidden while it starts a game and
    shown when it needs the user; `steam://install` / `steam://uninstall` confirmations in
    `-gamepadui` and the return home after confirming; what Steam shows after **cancelling** its
    confirmation (expected: holding Guide comes back); download states and bytes from a real
    download (one active, others queued; an update); a game on a disk that is not connected
    (unplug the 2 TB HDD with a game on it); Steam's first start blocked without a cable or Wi-Fi.
