---
type: step
description: "Steam login and store in `-gamepadui` mode, game launch via the daemon, return to home on exit, Steam Store tile."
phase: "[[phase-4-games]]"
step: "4.2"
status: done
legacy: "ROADMAP.md 4.2"
tags: [step, phase-4]
---
# 4.2 Steam integration *(approved 2026-10-13)*

Up: [[phase-4-games]] · Status: **done**

- **Deliverables:** Steam login and store in `-gamepadui` mode, game launch via the daemon, return
  to home on exit, Steam Store tile.
- **Required (owner, 2026-10-11):** every step with the controller alone: first start of Steam,
  login (Steam Guard included), store, installing a game (also the games owned but not installed:
  a place in the library opens Steam's own library), launching and closing a game. Guide always
  brings back the home screen with the selection where it was. Points to check first: Steam
  controls gamescope's focus itself, as owneetd does; Steam reacts to the Guide button, which
  owneetd owns; third-party launchers inside some games (e.g. EA app, Ubisoft Connect) need a
  pointer: a controller-driven pointer must exist before they ship. Play time of Steam games
  comes from Steam (4.1): the frontend must not add its own on top.
- **Library changes (owner, 2026-10-11; demo first):** no "Installed" filter; the last place of
  the grid is "Add games", opening a choice of sources (Steam for now: Steam's library).
- **Part 1 (2026-10-11):** [multilib] from the same snapshot; Steam in the image with the 32-bit
  drivers of every GPU (owneet-base 0.0.20, owneet-hardware 0.0.5): ISO 2164 MiB (+415 MiB; the
  build now stops at 4 GiB, FAT32's largest file, instead of GitHub's 2 GiB). In the test VM:
  - Steam starts in the session on its own Big Picture "Sign in" screen (QR code, or name and
    password); its first start downloads about 2.4 GB (runtime and update) and **shows nothing for
    a minute or more**: the console must show a "Preparing Steam" screen of its own.
  - In the **live system** that download is kept in RAM: with 4 GB the kernel stopped Steam (out
    of memory). Owner's decision: in the live session Steam opens only with at least 12 GB of
    RAM, otherwise a message asks to install OwneetOS; the installed system keeps 4 GB minimum,
    8 GB recommended.
  - With `GAMESCOPE_WAYLAND_DISPLAY` Steam takes over gamescope's focus property and its window
    stays hidden; without it Steam is an ordinary window that owneetd shows ([[owneetd-design]]).
  - Tools: `daemon/cmd/owneet-xprobe` (test only: gamescope's windows and focus properties),
    `OWNEET_TEST_MEM_MB` for the test VM's RAM.
- **Part 2 (2026-10-11):** owneetd 0.11.0: `/v1/steam` (library, store, run a game; Steam starts
  without gamescope's control variable), Steam games found under Steam's launcher and listed as
  `steam:N` (their own app id, Guide and Resume, close without closing Steam), the live-system
  memory rule, the `app.window` event; unit tests with pretend processes. owneet-frontend 0.16.0:
  the library without "Installed" and with "Add games" (Steam's library, the guide to games on a
  disk), "Preparing Steam…" until Steam's window appears, the "installed system" window for live
  systems under 12 GB, Home's "Steam Store" opens Steam's store, Steam games start through Steam
  and keep Steam's play time. Fixed on the way: A on an item whose action selects another item in
  the same window (e.g. the guide's Back button) also pressed that one. Preview:
  `tools/preview-steps/library-add-games.txt`.
- **Checked in the test VM (gamescope, 13 GB of RAM; 10 GB is refused as decided):** Steam opened
  through owneetd; Steam writes gamescope's focus property even without the Wayland variable
  (through X11), so owneetd now translates Steam's requests while Steam is in front and undoes
  them otherwise; `app.window` only when gamescope can really show the window (Steam's early
  helper windows are never shown); Guide: home screen, Steam does not take it back (20 s), Guide
  again: Steam. A game installed or removed in Steam makes the console read its games again when
  you come back (owneetd lists Steam's installed games), back where you were (e.g. "Add games").
  owneetd 0.11.3, owneet-frontend 0.16.1. The live system's writable space was archiso's
  default 256 MB, too small for Steam's download: now up to 75 % of RAM (`cow_spacesize=75%`,
  used only as files are written). Found before the hardware test: Steam opened from "Add games"
  took the screen without `focus.changed`, so the hidden interface kept reading the controller
  (keys typed in Steam would also move the library); owneetd 0.11.4 sends it whenever the screen
  changes by itself (cage: the newest app). Owner's first test on the NiPoGi (2026-10-12): login
  works with the controller, but Steam's start shows resolution changes and flashing windows
  (owneetd 0.11.5: Steam comes to the front only once its window has stayed for 3 seconds, the
  "Preparing Steam" screen covers the start); Guide was fought over by owneetd and Steam (owner's
  choice, option A: over Steam a short press is Steam's, holding it 1 second comes back to the
  console; owneetd 0.11.6); a game installed in Steam did not start (Steam: missing executable; the test stick now
  keeps Steam's logs, owneet-base 0.0.21; the logs show a broken Linux version of the game, see
  4.5); the other developer's green, then yellow, bar at the bottom of the screen came from a
  firmware setting ("Windows Compatible") on his PC, not from OwneetOS. To check on real hardware with the owner's account:
  login, installing and starting a game, Guide in a game, Steam's own reaction to the Guide
  button, closing a game from the home screen.
- **Demo (2026-10-11):** `design/demos/4.2-library-add-games.html`, built on the approved demo
  3.7: every game installed, filters All / Favorites / Steam / Local; "Add games" as the last
  place of the grid (not in Favorites, a personal list) → a window with "Steam" (Steam opens on
  its library: a stand-in screen; Home brings back the library on "Add games") and "From a USB
  stick or disk" (a read-only guide to the `Games` folder; B goes back to the choice). B on the
  page: the quick menu (3.13).
- **Approved (2026-10-13)** after the owner's test on the NiPoGi: login with the controller, no
  glitches at Steam's start, Guide over Steam (short: Steam; held: the console), Steam shown
  automatically while a game starts, a game installed in Steam started from the console's
  library (Dragon's Wake, with Proton forced by hand: its Linux version is broken; automatic
  recovery planned in 4.5).
