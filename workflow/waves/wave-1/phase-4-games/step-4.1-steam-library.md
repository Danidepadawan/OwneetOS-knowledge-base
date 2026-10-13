---
type: step
phase: "[[phase-4-games]]"
step: "4.1"
status: done
legacy: "ROADMAP.md 4.1"
tags: [step, phase-4]
---
# 4.1 Steam library *(investigation first; approved 2026-10-11)*

Up: [[phase-4-games]] · Status: **done**

- **Deliverables:** installed Steam games read from local files (`libraryfolders.vdf`,
  `appmanifest_*.acf`) across all disks; play time from local Steam data; check whether Pegasus's
  built-in Steam provider can be reused (without its Steam store downloads: local data only).
- **Open point (closed 2026-10-11):** listing games that are **owned but not installed** may not
  be possible from local files alone. Investigation on the owner's Steam client (read only, none of
  their data in the repository; [[frontend-architecture]], "Steam's local files"): the
  licence packages (`appcache/packageinfo.vdf`) gave 92 games, the client shows 90. Owner's
  decision: installed games only, the rest from Steam's own library; games on a disk that is not
  connected are not shown ([[game-library]]).
- **Outcome (2026-10-11):** Pegasus's Steam provider reused and changed: only games installed
  completely (`StateFlags` bit 4), Valve's tools left out by name too (new Proton and runtime
  versions need no new entry), play time and last played from the account's `localconfig.vdf`
  (`SteamPlaytime.cpp`, a small reader for Steam's text files). New test `test_Steam` on an
  invented Steam folder (installed, downloading, update waiting, tools, a second library, a
  library on a disk not connected, two accounts). owneet-frontend 0.15.0. Steam is not in the ISO
  yet (4.2): checked on real Steam data from step 4.2 on.
