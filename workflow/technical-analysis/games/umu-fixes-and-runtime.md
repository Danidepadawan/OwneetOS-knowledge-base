---
type: technical-analysis
description: "Research for point 3 of the games method: running the console's own games through umu as Heroic does: Windows games with their store and id so umu-protonfixes applies the community's fixes, native Linux games in the Steam Linux Runtime (UMU_NO_PROTON=1)."
component: games
tags: [technical-analysis, games, umu, proton]
---
# Games outside Steam through umu (research, 2026-11-18)

Point 3 of [[game-compatibility-method]].

## What OwneetOS does today

- Windows games: `owneet-windows-run` runs `umu-run` with `GAMEID="${GAMEID:-umu-default}"`, no `STORE`, its own
  Proton (`PROTONPATH`), `UMU_RUNTIME_UPDATE=0`. owneetd never sets `GAMEID`: **every game runs as `umu-default`,
  which applies no per-game fix** (umu's manual).
- Native Linux games: run with the system's libraries, plus OwneetOS's own `lib32-owneet-compat` and 32-bit
  libraries added one game at a time (The Witcher 2: [[closed-items]] 3u).

## What umu offers (its manual, [umu.1](https://raw.githubusercontent.com/Open-Wine-Components/umu-launcher/main/docs/umu.1.scd))

- `GAMEID`: a umu-database id; `STORE`: the store's id. protonfixes picks the fix script by store and id
  (one folder of fixes per store; a fix shared between stores is linked).
- `UMU_NO_PROTON=1`: runs the program **natively inside the Steam Linux Runtime**, for native Linux games.
- The Steam Linux Runtime is downloaded by umu itself (`~/.local/share/umu`); `UMU_RUNTIME_UPDATE=0` stops updates.

## The umu database ([umu-database](https://www.github.com/Open-Wine-Components/umu-database))

- Title, store, codename, umu id, for the games that need fixes (not every game).
- GOG: the codename is the GOG product id (the one in the game's `goggame-<id>.info`, which owneetd already reads);
  a game also on Steam has the id `umu-<Steam app id>`.
- Queried at `https://umu.openwinecomponents.org/umu_api.php?store=gog&codename=<id>`; no licence stated on the
  page (to check before keeping a copy of the data in OwneetOS).

## What Heroic does (for reference)

Heroic runs native GOG games in the Steam Runtime through umu ("umu-scout", turned on for GOG games when they are
installed), which solved missing libraries such as a native game's old `libssl` or `libFLAC`.

## Constraints to respect

- [[hard-constraints]] C9: no internet needed for local or DRM-free games. The umu id is looked up **once, when
  the game is added** (with internet), stored with the game; without internet the game runs as today and the id is
  looked up later. The Steam Linux Runtime arrives with the one-time Windows-games download (already allowed) or
  must be asked for the same way: to decide with the owner.
- [[legal]]: the runtime is Valve's: downloaded by the user's console, never shipped by OwneetOS.
- Old 32-bit native games need the old runtime ("scout"); Proton's runtime is "sniper": which one umu uses with
  `UMU_NO_PROTON`, and whether 32-bit games run in it, to try with The Witcher 2 (Linux).

## Built (2026-11-19, step 2)

- The umu database travels with GE-Proton (`<GE-Proton>/protonfixes/umu-database.csv`), and protonfixes reads it
  offline; but umu sets `UMU_ID` from `GAMEID` (default `umu-default`), so protonfixes' own lookup by store and
  codename never runs: the console looks the game up itself in that file (`owneet-windows-run`, Python's csv) and
  passes `GAMEID=<umu id>` and `STORE=gog`. No internet: the constraint C9 holds.
- The GOG product id comes from `goggame-<id>.info` (owneet-frontend, extra `disk.gog.id`, `OWNEET_GOG_ID`).
- A game with an umu id `umu-<Steam app id>` also gets that number as `SteamAppId`, so Proton's own per-game settings
  for the Steam version apply too.
