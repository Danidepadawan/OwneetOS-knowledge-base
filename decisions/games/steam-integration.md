---
type: decision
description: "Steam in the ISO, controller-only Steam, its screens shown automatically, 12 GB RAM in the live session."
area: games
status: active
decided: 2026-10-11
updated: 2026-10-12
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
- Library: installed games only ([[game-library]]).

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
