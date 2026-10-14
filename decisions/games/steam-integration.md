---
type: decision
description: "Steam in the ISO, controller-only Steam, its screens shown automatically, 12 GB RAM in the live session."
area: games
status: active
decided: 2026-10-11
updated: 2026-10-14
legacy: "PROJECT_RULES.md §8 (Steam), §13 (2026-10-11, 2026-10-12)"
tags: [decision, games, steam]
---
# Steam integration

- **Steam is in the ISO** with 32-bit drivers for every GPU (about +300 MiB, [multilib] from the
  same snapshot); Steam's runtime is downloaded by Steam on first launch.
- Steam runs in `-gamepadui` mode. Anything the console opens (Steam included) must be fully usable
  with the controller: first start, login (Steam Guard included), store, installing, launching and
  closing a game. The user must **never** be forced to use a mouse or keyboard
  ([[hard-constraints]] C2), and Guide always brings back the home screen with the selection where
  it was ([[guide-button]]).
- Steam's own screens (login, progress of a game's launch) are **shown by the console
  automatically** when they matter: the user never has to look for them. The console shows its own
  "Preparing Steam" screen during Steam's first download.
- **Live session:** Steam's first download (about 2.4 GB) is kept in RAM, so Steam opens only with
  **at least 12 GB of RAM**; otherwise a clear message asks to install OwneetOS to use Steam. The
  installed system's requirements do not change (4 GB minimum, 8 GB recommended); Steam is started
  only when needed (C1 is measured with Steam closed).
- **Guide over Steam**: a short press is Steam's, holding 1 second comes back ([[guide-button]]).
- **Steam without its interface** (2026-10-14, replaces "owned games are installed from Steam's
  library"): Steam runs hidden and the console replaces its interface in everyday use, because
  with the NVIDIA driver Steam's own window shows glitches no setting removed (a known problem of
  X11 windows on that driver; not reported upstream for now). Every owned game is listed by the
  console from Steam's local caches (88 games on the owner's account, as Steam shows); installing
  goes through Steam's official `steam://install/<appid>`, whose confirmation window is the only
  Steam window left in everyday use, announced on NVIDIA as a temporary display problem (option
  a); the console shows the download itself. Writing Steam's files to start downloads is turned
  down. Step: [[step-4.2c-steam-without-its-interface]]. Library: [[game-library]].
- **A Steam game whose Linux version cannot start** (Steam: "Missing game executable") gets an
  automatic recovery, offered to the user: try the version for Windows with Proton
  ([[step-4.5-windows-games-proton]]).
- Steam stays in the ISO until [[optional-apps]] arrive (step 5.0): then it is downloaded when chosen.

Technical design: [[owneetd-api-apps]], [[frontend-steam-local-files]]. Steps: [[step-4.1-steam-library]],
[[step-4.2-steam-integration]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-11 | Steam library (step 4.1): installed games only, from local files; games on a disk that is not connected are not shown; owned games that are not installed are installed from Steam's own library, because no local file lists them with certainty (the licence packages gave 92 games, the client shows 90). Steam, like everything the console opens, must work with the controller alone ([[game-library]]). |
| 2026-10-11 | Demo 4.2 approved (with the generic store icon for Steam and no "Add games" in Favorites). **Distribution:** the ISO goes to SourceForge, the website to a `.org` domain on GitHub Pages, packages stay on GitHub ([[distribution-and-updates]]). **Steam is in the ISO** with 32-bit drivers for every GPU (about +300 MiB, [multilib] from the same snapshot). |
| 2026-10-11 | Steam in the **live session** (no installed disk: Steam's first download of about 2.4 GB is kept in RAM): only with at least **12 GB of RAM**; otherwise a clear message asks to install OwneetOS to use Steam. The **installed system's requirements do not change** (4 GB minimum, 8 GB recommended); Steam is started only when needed (C1 is measured with Steam closed). |
| 2026-10-12 | After the owner's first Steam test (Guide fought over by owneetd and Steam): **while Steam or a Steam game is on screen, a short Guide press is Steam's; holding Guide for 1 second comes back to the console** (option A; [[controller-input-map]]). "Exit Steam" in Steam's menu also comes back. Steam's own screens that matter (login, a game's launch progress) are shown automatically ([[game-library]]). |
| 2026-10-13 | A Steam game whose Linux version cannot start (Steam: "Missing game executable") gets an automatic recovery, offered to the user: try the version for Windows with Proton ([[step-4.5-windows-games-proton]]). |
| 2026-10-14 | **Steam without its interface:** Steam runs hidden; every owned game is listed from Steam's local caches (licences in `packageinfo.vdf`, types in `appinfo.vdf`, package 0 and inactive licences left out: 88 games, as Steam shows); installing through `steam://install/<appid>` (Steam's confirmation window, announced on NVIDIA as a temporary display problem; option a), the download shown by the console. Replaces "owned games are installed from Steam's library" (2026-10-11). Reason: glitches in Steam's own window with the NVIDIA driver, NVIDIA-only (same ISO clean on AMD), not removed by any setting. |
