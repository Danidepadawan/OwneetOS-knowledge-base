---
type: technical-analysis
description: "Research for points 5 and 6 of the games method: testing games by the technology that makes them break, with free games only, and telling the user honestly when a game cannot run on Linux (Steam's own Steam Deck data)."
component: games
tags: [technical-analysis, games, tests]
---
# Tests by technology, with free games (research, 2026-11-18)

Points 5 and 6 of [[game-compatibility-method]]. The owner buys no game for tests.

## The table (rows to fill with one free game each)

| What breaks games | Cell |
|---|---|
| Graphics API | DirectX 9, DirectX 11, DirectX 12, Vulkan, OpenGL |
| Engine | Unreal 4, Unreal 5, Unity, Source / Source 2, others |
| Build | 32-bit Windows, 64-bit Windows, native Linux (old 32-bit, recent 64-bit) |
| Anti-cheat | Easy Anti-Cheat and BattlEye with Proton support turned on, and one that refuses Linux |
| Launchers | EA app, Ubisoft Connect, Rockstar Games Launcher, a game's own launcher |
| Outside Steam | GOG Windows installer (Inno Setup), GOG Linux installer, DOS (DOSBox) |
| First start | install script (redistributables), shader preparation, a licence to accept |

## Where the free games come from

- Steam: free-to-play games and demos (Steam Next Fest), chosen with SteamDB's public technology pages (engine,
  SDKs, anti-cheat, launcher) read by a person ([[legal]]: no scraping).
- GOG: its free games and giveaways (owner, 2026-11-20: GOG's games are legal and may be named; the local guard on
  game names is the owner's to update).
- The owner's own library where a cell is already covered.

## Run

On every release and every driver or Proton change, on the test hardware; results in a table in this vault (game,
cell, result, log). A cell that fails is a class to fix, not a single game.

## Point 6: what cannot run, said honestly

- Steam's own data, already on the console: Steam's app info (which owneetd reads for artwork) holds each game's
  Steam Deck compatibility (verified, playable, unsupported) and Proton's anti-cheat status is public
  (Are We Anti-Cheat Yet).
- The console could say "This game does not run on OwneetOS" instead of a launch that fails (games whose anti-cheat
  refuses Linux, e.g. Battlefield 6). Look and words: a demo first.

## Proposed list (2026-11-20, for the owner to choose)

Cells already covered by the owner's games: Unreal 4 + DirectX 11 + EA app (STAR WARS Jedi: Fallen Order), Vulkan / DirectX
12 + Rockstar launcher (Red Dead Redemption 2), DirectX 12 (ELDEN RING), 32-bit Windows + DirectX 9 + Unreal 2.5
(BioShock), Unreal 3 (BioShock Infinite, Batman: Arkham City), Unity (Hollow Knight: Silksong), Ubisoft Connect
(South Park: The Fractured But Whole), a game's own launcher + GOG Windows installer + GOG Linux installer + old 32-bit
native (The Witcher 2, both versions).

Free games for the cells left (checked online 2026-11-20; status can change with any update):

| Cell | Free game | Source, what was found |
|---|---|---|
| Source 2, native Linux, Vulkan | Dota 2 (Steam) | native Linux, free |
| Easy Anti-Cheat allowed on Linux | Paladins (Steam) | anti-cheat "works" on GamingOnLinux (last updated 2025-11-26); Valve's Steam Deck rating "Unsupported"; dropped by the owner 2026-11-23 (black screen in exclusive full screen, [[closed-items]] 20) |
| Anti-cheat that refuses Linux (step 4.8) | Apex Legends (Steam) | EA blocked Linux and Steam Deck in October 2024; no reversal found |
| Unreal 5 + Easy Anti-Cheat | THE FINALS (Steam) | runs through Proton, but broke on Linux after several updates; Denuvo Anti-Cheat added in 2026: unreliable |
| DOS (DOSBox), GOG | Tyrian 2000 (GOG) | GOG's page shows it free |
| ScummVM, GOG Linux | Beneath a Steel Sky (GOG) | free on GOG with a Linux version (ScummVM) |
| BattlEye allowed on Linux | none found yet | |
| OpenGL (Windows) | none found yet | |

Sources: [GamingOnLinux, Paladins](https://www.gamingonlinux.com/itemdb/app/40486/paladins/),
[PC Gamer, Apex Legends](https://pcgamer.com/games/battle-royale/apex-legends-ditches-steam-deck-support-ea-says-linux-is-a-path-for-a-variety-of-impactful-exploits-and-cheats),
[GamingOnLinux, THE FINALS](https://www.gamingonlinux.com/2025/08/the-finals-broken-on-linux-again/),
[GOG, Tyrian 2000](https://www.gog.com/en/game/tyrian_2000),
[GamingOnLinux, Beneath a Steel Sky](https://gamingonlinux.com/2020/07/cult-classic-beneath-a-steel-sky-is-finally-available-free-on-steam).

