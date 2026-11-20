---
type: decision
description: "How OwneetOS makes games work as a whole instead of one game at a time: what mature open source projects already do is reused, never re-invented (Steam's own way for Steam games, umu's per-game fixes and runtimes for the others, a tested NVIDIA driver channel, tests by technology with free games)."
area: games
status: active
decided: 2026-11-18
updated: 2026-11-20
tags: [decision, games]
---
# Making games work: a method, not one game at a time

> [!note] **Direction approved by the owner on 2026-11-18** ([[open-items]] 14): research first, point by point.
> Point 2 (Steam's own windows shown): to be tried ("Steam's interface has not flickered for a while"); if Steam's own
> shader page is shown, the console's percentage (demo `4.2c-steam-shaders`, approved) may not be needed: not built
> until then.

## Why

Owner, 2026-11-18: almost every game tested gives a problem; a product for the public cannot be made by chasing
them one by one, and the owner cannot buy games to test them. The problems recorded until then fall into four
classes; for each, a mature open source project already solved it and OwneetOS did not use its solution.

| Class | Seen in | Cause in OwneetOS | Who already solved it |
|---|---|---|---|
| 1. The console between Steam and its games | Steam's windows hidden while it prepares shaders (7.5 min, Cyberpunk 2077) or runs an install script (Jedi: Fallen Order's EA window, 4 min); a game never shown, or behind Steam; "Waiting" while downloading; Steam lost its page | Steam runs hidden and owneetd re-does its launch flow around it ([[step-4.2c-steam-without-its-interface]]) | SteamOS and the distributions built like it (ChimeraOS, Bazzite): Steam's own game session, its windows shown when it has something to say |
| 2. Games outside Steam | The Witcher 2 (Linux) missing 32-bit libraries, files in parts, a folder with ":", its launcher's language files; Windows games' shim; Wine's own programs taken for the game | OwneetOS runs native games with the system's libraries and its own compatibility libraries; Windows games start with `GAMEID=umu-default` and no store, so umu-protonfixes' per-game fixes never apply | Heroic Games Launcher: native GOG games in the Steam Runtime through umu (umu-scout); umu-launcher with the game's id and store, so umu-protonfixes applies the community's fixes |
| 3. The graphics driver | Cyberpunk 2077 closing on the FrankenPC (NVIDIA 615, Turing card): [[nvidia-turing-shader-compiler-crash-in-vkd3d-games]] | The NVIDIA driver follows the pinned packages, never tried against games before it ships | Bazzite: NVIDIA drivers tracked, tried, and an older image kept to go back to |
| 4. Publishers' launchers | EA app, Rockstar, CD Projekt Red, Ubisoft Connect ([[open-items]] 13) | Not looked at as a class | umu-protonfixes and Lutris' install scripts hold what each launcher needs under Proton |

## Proposal

1. **Reuse, never re-invent.** Before building anything for games, look for the project that already does it and
   use its solution (or its data); OwneetOS adds only what it lacks (Guide, the console's look, its own
   questions).
2. **Steam games the way SteamOS runs them.** Steam's launch belongs to Steam: the console never hides a Steam window
   that asks or shows something (its shader preparation, an install script, a publisher's launcher, a question);
   the console's "Starting …" screen stays only while nothing is on screen, with the percentage of demo
   `4.2c-steam-shaders`. Steam started with the options of SteamOS-like sessions (ChimeraOS:
   `-gamepadui -steamos3 -steampal -steamdeck`), each one checked first for what it changes. This revises part of
   "Steam without its interface" (step 4.2c): the owner's choice.
3. **Games outside Steam through umu, as Heroic does.** Windows games with their store and id (`STORE=gog`,
   `GAMEID` from the umu database) so the community's per-game fixes apply; native Linux games in the Steam
   Runtime (umu-scout) instead of the system's libraries, which makes OwneetOS's own compatibility libraries
   (`lib32-owneet-compat`) the exception, not the rule.
4. ~~**A tried NVIDIA driver.**~~ (rejected by the owner, 2026-11-20: more upkeep than he can give; the driver keeps
   following the pinned packages.) A new NVIDIA driver reaches the console only after it passed the test games on the
   test hardware (FrankenPC, Turing; others when available); the previous one kept to go back to; known regressions
   (NVIDIA's forum, vkd3d-proton, Proton) read before choosing. Same for Proton's version chosen by the console.
5. **Tests by technology, with free games.** A table of what makes games break (DirectX 9 / 11 / 12, Vulkan,
   OpenGL; Unreal, Unity, other engines; 32-bit; anti-cheat EAC / BattlEye; EA, Ubisoft, Rockstar launchers; GOG
   Windows and Linux installers, DOS), one free game per cell (free-to-play, demos, GOG's free games), run on every
   release and every driver change. No game bought.
6. **What cannot work, said honestly.** Games whose anti-cheat refuses Linux (e.g. Valorant, Battlefield 6) never
   run on any Linux system: the console says so instead of failing (ProtonDB and Steam Deck data).

## Research (2026-11-18)

- Point 2: [[steam-the-steamos-way]]. Point 3: [[umu-fixes-and-runtime]]. Point 4: [[nvidia-driver-channel]].
  Points 5 and 6: [[game-test-matrix]].

## Order (owner, 2026-11-18)

1. Steam no longer hidden during a launch (then SteamOS's options, one at a time); 2. umu with the game's id and
store for the console's Windows games; 3. native Linux games in the Steam Linux Runtime. Points 4 (driver channel)
and 5 (free games table): decided along the way. **The Steam Linux Runtime for native games is downloaded with the
one-time Windows-games download** (owner).

## Order (as first proposed)

Research first (one note per point, with sources), then a demo where the look changes, then the work in the plan's
usual steps. Cyberpunk 2077 meanwhile: the FrankenPC tried with the driver of the development PC (595, if it can
run with the console's kernel) to tell the driver from the card.

## History

| Date | Change |
|---|---|
| 2026-11-18 | Proposed to the owner ([[open-items]] 14). |
| 2026-11-18 | Direction approved; research first; point 2 to be tried; the shader percentage waits for it. |
| 2026-11-18 | Order approved for the first three points; 4 and 5 along the way; the runtime with the Windows-games download. |
| 2026-11-20 | Point 3's way approved: native games outside Steam in Valve's Steam Linux Runtime 1.0 (scout) through umu (`umu-scout`), as Heroic does ([[umu-fixes-and-runtime]]); as today when it is missing. Cyberpunk 2077 dropped: NVIDIA's driver, not OwneetOS (owner). |
| 2026-11-20 | Point 4 (a tried NVIDIA driver channel) **rejected** by the owner: more upkeep than he can give. Point 5: games from GOG may be named and used (legal; the local guard on game names is the owner's to edit). Point 6 put in Wave 1 as [[step-4.8-games-that-cannot-run]] (demo first). |
