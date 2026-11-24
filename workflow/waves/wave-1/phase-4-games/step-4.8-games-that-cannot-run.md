---
type: step
description: "The console says honestly when a game cannot run on OwneetOS (e.g. an anti-cheat that refuses Linux), from Steam's own data, instead of a launch that fails; demo first."
phase: "[[phase-4-games]]"
step: "4.8"
status: in-progress
tags: [step, phase-4]
---
# 4.8 Games that cannot run, said honestly *(added 2026-11-20)*

Up: [[phase-4-games]] · Status: **in-progress**

- **Origin:** point 6 of [[game-compatibility-method]], put in Wave 1 by the owner on 2026-11-20.
- **Deliverables:** for a game that cannot run on Linux (its anti-cheat refuses it, e.g. Battlefield 6),
  the console says so instead of starting a launch that fails. Data already on the console where possible: Steam's
  app info (its Steam Deck compatibility), and the public anti-cheat status ([[game-test-matrix]]).
- **First:** what data is reliable and what it says (research, with sources), then the look and the words in a demo
  for the owner ([[demo-before-code]]); no UI code before both are approved.

## Research (2026-11-24, started at the owner's request)

Read from a Steam client's own `appinfo.vdf` (the file the library already reads), 123 games, 115 with data; on the
development PC, to confirm on the FrankenPC when it is built.

- **Each game has** `common/steam_deck_compatibility`: `category` (Deck: 1 unsupported, 2 playable, 3 verified),
  **`steamos_compatibility`** (1 unsupported, 2 compatible, 0 not known), `test_timestamp`, and the reasons (`steamos_tests`,
  tokens such as `#SteamOS_TestResult_UnsupportedAntiCheat_Other`, `…_UnsupportedAntiCheatConfiguration`,
  `…_SteamOSDoesNotSupport`). The meaning of the numbers is read from the games whose rating is known.
- **The SteamOS rating, not the Deck's:** two games are "unsupported" on the Deck only for its graphics power and compatible
  with SteamOS; a third needs a VR headset (SteamOS 0). 15 of the 115 are SteamOS 1: 5 for their anti-cheat, 10 with no reason.
- **It is a warning, not a fact:** Paladins is SteamOS 1 (anti-cheat, checked in 2022-10) and reached its menus on the
  FrankenPC ([[closed-items]] 20); Apex Legends is SteamOS 1 (anti-cheat, 2024-11) and does refuse Linux. Valve's own
  documentation says "does not function on this device" and that it reviews again (a new Proton, new tests), with no
  schedule ([Steamworks](https://partner.steamgames.com/doc/steamhardware/compat)); GamingOnLinux: "doesn't automatically mean a
  game will never work" ([guide](https://www.gamingonlinux.com/guides/view/what-steam-deck-steam-machine-steam-frame-and-steamos-verified-ratings-mean/)).
  So the console never blocks a game.
- **Are We Anti-Cheat Yet** (MIT; `games.json`, with Steam ids and a status: Apex Legends "Denied", Paladins "Running"): not
  needed and not proposed: a list to ship and keep up to date, or a download from a third party; no data outside anti-cheats.
- **Battlefield 6** is not in the file read: what Steam says of it is not known yet.
- Games on a disk: no data, nothing is said.

## Demo (2026-11-24, waits for the owner's approval)

`design/demos/4.8-games-that-cannot-run.html` (code `7fa8991`): for a Steam game with SteamOS 1, the install's question becomes
"{title} may not work" with Steam's reason and the month of its check, Cancel selected, "Install anyway"; the same before the
first start of one installed from Steam's pages ("Start anyway"); asked once per game; Details always says it (three rows). To
choose: a small sign on the cover. No new button; every other game as today.
