---
type: step
description: "Steam runs hidden; the console lists every owned Steam game from Steam's local caches, installs it through Steam's own confirmation and shows the download itself."
phase: "[[phase-4-games]]"
step: "4.2c"
status: todo
tags: [step, phase-4]
---
# 4.2c Steam without its interface *(owner, 2026-10-14)*

Up: [[phase-4-games]] · Status: **todo**

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
    installs, X details); the **"Installed" filter** comes back; a Steam game on a disk that is
    not connected shows "On a disk that is not connected" (from `libraryfolders.vdf`).
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
    ([[step-5.1-brave-in-the-os]]) instead of Steam's interface, when that app exists; until then, Steam's store.
  - Demo of the new screens (owned games, installing, download progress, uninstalling, the
    NVIDIA notice, no internet) approved before the code ([[demo-before-code]]): proposal agreed
    on 2026-10-14, demo `design/demos/4.2c-steam-library.html`.
- **Done when:** on the FrankenPC, everyday use (browsing the library, installing, starting and
  closing a game, coming back with Guide) never shows Steam's own window except for its
  confirmation when installing or uninstalling; the library matches Steam's own count; without
  internet, Steam's actions say so and are blocked.
- **Outcome:**
