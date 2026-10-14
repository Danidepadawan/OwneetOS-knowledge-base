---
type: decision
description: "One library for Steam and local games; every owned Steam game, installed or not; filters and the Add games tile."
area: games
status: active
decided: 2026-10-03
updated: 2026-10-14
legacy: "PROJECT_RULES.md §8 (library)"
tags: [decision, games, library]
---
# Unified game library

- **Unified game library** on the home screen (Steam + other stores + local DRM-free games
  together). Stores are opened **only for purchases**.
- **Steam: every owned game** (since 2026-10-14), installed or not, read from Steam's local files
  (no API key, offline): licences and app types from Steam's caches, as Steam's own library counts
  them; installed games from the `appmanifest` files (a game on a disk that is not connected
  shows as not installed). The console installs them through Steam and shows the download
  ([[steam-integration]], [[step-4.2c-steam-without-its-interface]]). *(Until 2026-10-14:
  installed games only, owned games installed from Steam's own library.)*
- **Not-installed Steam games** (demo 4.2c): a dimmed cover with a download mark; A installs them
  (A plays an installed game), X shows the details. With the "Recent" sort, **games being
  downloaded come first** (in Steam's order), then the installed games, then the others. While a game downloads, its cover shows the progress and its state (waiting,
  downloading, updating). A Steam game installed on a disk that is not connected shows **"On a
  disk that is not connected"** instead of offering to install it again (from
  `libraryfolders.vdf`). Games on disks (DRM-free) on a disk that is not connected are still not
  shown.
- **Library screen** (demo 4.2, changed by demo 4.2c): filters All / **Installed** / Favorites /
  Steam / Local ("Installed" removed on 2026-10-11 and **restored on 2026-10-14**, now that
  not-installed games are listed); the last place of the grid is **"Add games"** (not in
  Favorites), which opens a choice of sources: **Steam** (since 2026-10-14: Steam's **store**, to
  buy new games, since owned games are already in the library) and **"From a USB stick or
  disk"** (a guide to the `Games` folder, [[games-on-disk]]). Steam uses a generic store icon.
- Steam's play time is Steam's: the frontend does not add its own on top.

Layout rules shared with the home screen: [[home-and-library]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-03 | Project scope, architecture and Wave 1 agreed ([[vision]]–11). |
| 2026-10-11 | Steam library (step 4.1): installed games only, from local files; games on a disk that is not connected are not shown; owned games that are not installed are installed from Steam's own library, because no local file lists them with certainty (the licence packages gave 92 games, the client shows 90). Steam, like everything the console opens, must work with the controller alone ([[game-library]]). |
| 2026-10-11 | Library (for the demo of step 4.2): the "Installed" filter is removed (every game shown is installed); the last place of the grid is **"Add games"**, which opens a choice of sources (for now Steam, which opens on **Steam's library**, where owned games are installed and the store is one step away). |
| 2026-10-14 | Every owned Steam game is listed by the console from Steam's local caches and installed through Steam, Steam's own interface staying hidden ([[steam-integration]]). |
| 2026-10-14 | Proposal for demo 4.2c agreed: not-installed Steam games dimmed with a download mark (A installs, X details, after the installed ones in "Recent"); the **"Installed" filter is restored**; a Steam game on a disk that is not connected shows "On a disk that is not connected" (not for DRM-free games); "Add games → Steam" opens Steam's store. |
| 2026-10-14 | Demo 4.2c review: with the "Recent" sort, games being downloaded come first. |
| 2026-10-11 | Demo 4.2 approved (with the generic store icon for Steam and no "Add games" in Favorites). **Distribution:** the ISO goes to SourceForge, the website to a `.org` domain on GitHub Pages, packages stay on GitHub ([[distribution-and-updates]]). **Steam is in the ISO** with 32-bit drivers for every GPU (about +300 MiB, [multilib] from the same snapshot). |
