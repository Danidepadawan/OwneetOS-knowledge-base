---
type: technical-analysis
description: "API and design of Windows games in owneetd (step 4.5): the one-time download of Proton and its runtime with umu-launcher, its progress, owneet-windows-run."
component: owneetd
tags: [technical-analysis, owneetd, api, games]
---
# owneetd: Windows games (step 4.5)

Up: [[owneetd-design]] · Behaviour: [[games-on-disk]], [[step-4.5-windows-games-proton]] ·
Frontend side: [[frontend-disk-games]]

| Method | Path | What |
|---|---|---|
| GET | `/v1/windows` | `{state, percent, needed}`: `none` (no Windows game in the library: nothing downloaded), `waiting` (no internet), `downloading` (percent), `ready`, `failed` (tried again on a network change or after 10 minutes) |
| POST | `/v1/windows/needed` | The library has a Windows game (the interface says so after reading the games): remembered in `~/.local/share/owneet/windows/needed`; 204 |

Event `windows.changed` with the same object.

## The download (`internal/windows`)

- **umu-launcher** ([multilib], a dependency of owneet-base; Python) is run once as
  `umu-run ""` with `GAMEID=umu-default PROTONPATH=GE-Proton UMU_LOG=1` and a prefix of its own.
  It downloads the latest **GE-Proton** from its GitHub releases (about 500 MB, SHA-512 checked;
  1.6 GB unpacked in `~/.local/share/Steam/compatibilitytools.d/`) and the **Steam Linux
  Runtime 4** from Valve's repository (about 150 MB, SHA-256 checked; 661 MB in
  `~/.local/share/umu/steamrt4`), then would start the program: owneetd stops it there (its
  process group) when the log says `Running '…' using runtime`. Measured on the builder VM on
  2026-10-16 (umu-launcher 1.4, GE-Proton11-9, about 2 minutes).
- **Progress:** the log's parts (`Downloading GE-Proton` 0–60 %, `Extracting` 62 %,
  `Downloading steamrt` 65–97 %, `mtree is OK` 98 %) and, within a download, the size of the
  `*.parts` files in `~/.cache/umu` against rough sizes.
- **Ready:** GE-Proton's folder (from `PROTONPATH=/…` in the log) is written to
  `~/.local/share/owneet/windows/proton`; a restart of owneetd starts `ready` while that folder
  has its `proton` script.
- Starts when `needed`, online (NetworkManager `connected`) and umu-run exists; network changes
  wake it up, otherwise it looks every minute.

## Starting a game: `/usr/lib/owneet/owneet-windows-run PREFIX GAME.EXE [ARGS…]`

In owneetd's package; the interface launches it through `POST /v1/apps/launch` like any game.
It refuses (exit 3) until the Proton file exists, then runs `umu-run` with `PROTONPATH` = that
folder (never "GE-Proton": no lookup online at a game's start), `UMU_RUNTIME_UPDATE=0`,
`GAMEID=umu-default` (no game-specific fixes yet), `PROTON_USE_XALIA=0` (no controller-as-mouse
helper inside games) and `WINEPREFIX` = the game's prefix
(`~/.local/share/owneet/windows/prefixes/<folder>-<hash>`, one per game, on the console's disk).

## GOG's DOS games: `/usr/lib/owneet/owneet-dos-run DATA GAME_DIR WORKDIR [GOG's ARGS…]`

For a GOG game whose play task starts `dosbox.exe` (owner, 2026-10-16): Linux's `dosbox`
(0.74.3, Arch), no Proton. The first start copies the game folder to `DATA/game`
(`~/.local/share/owneet/dos/<folder>-<hash>`) with `__support/save`; each `-conf` file is
rewritten to `DATA/conf/N.conf` (CR removed; `[autoexec]` `mount`/`imgmount` paths resolved
against the copy, without case; GOG's `-t overlay` cloud-saves mount dropped); a last
`owneet.conf` sets `[sdl] fullscreen=true, fullresolution=desktop, output=opengl`; `-noconsole`
is dropped; DOSBox runs in the copy's working folder.

## Windows on screen

Proton's windows are tagged like any app's ([[owneetd-api-apps]]): by `_NET_WM_PID`, and when it
is missing or leads to no app, by the process the X server records (X-Resource). Wine's console
windows (`WM_CLASS` `conhost.exe`) are never tagged, so never shown.

## Not done yet

- Updating GE-Proton or the runtime later (the first ones stay).
- Game-specific fixes (umu's `GAMEID` / `STORE` lookups).
- The Steam question for a broken Linux version (step 4.5, second part).
