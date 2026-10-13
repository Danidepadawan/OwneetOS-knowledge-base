---
type: decision
area: games
status: active
decided: 2026-10-03
updated: 2026-10-11
legacy: "PROJECT_RULES.md §8 (library)"
tags: [decision, games, library]
---
# Unified game library

- **Unified game library** on the home screen (Steam + other stores + local DRM-free games
  together). Stores are opened **only for purchases**.
- **Steam: installed games only**, read from local Steam files (no API key, offline); a game on a
  disk that is not connected is simply not shown. Games owned but not installed are installed from
  Steam's own library (Big Picture), which the console opens: Steam's local files cannot list them
  with certainty ([[steam-integration]]).
- **Library screen** (demo 4.2): no "Installed" filter (every game shown is installed); filters
  All / Favorites / Steam / Local; the last place of the grid is **"Add games"** (not in
  Favorites), which opens a choice of sources: **Steam** (opens on Steam's library, where owned
  games are installed and the store is one step away) and **"From a USB stick or disk"** (a guide
  to the `Games` folder, [[games-on-disk]]). Steam uses a generic store icon.
- Steam's play time is Steam's: the frontend does not add its own on top.

Layout rules shared with the home screen: [[home-and-library]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-03 | Project scope, architecture and Wave 1 agreed ([[vision]]–11). |
| 2026-10-11 | Steam library (step 4.1): installed games only, from local files; games on a disk that is not connected are not shown; owned games that are not installed are installed from Steam's own library, because no local file lists them with certainty (the licence packages gave 92 games, the client shows 90). Steam, like everything the console opens, must work with the controller alone ([[game-library]]). |
| 2026-10-11 | Library (for the demo of step 4.2): the "Installed" filter is removed (every game shown is installed); the last place of the grid is **"Add games"**, which opens a choice of sources (for now Steam, which opens on **Steam's library**, where owned games are installed and the store is one step away). |
| 2026-10-11 | Demo 4.2 approved (with the generic store icon for Steam and no "Add games" in Favorites). **Distribution:** the ISO goes to SourceForge, the website to a `.org` domain on GitHub Pages, packages stay on GitHub ([[distribution-and-updates]]). **Steam is in the ISO** with 32-bit drivers for every GPU (about +300 MiB, [multilib] from the same snapshot). |
