---
type: known-solution
description: "A Steam game at its first start \"closes\" at once, or runs paused behind the home screen and cannot be resumed from the console or from Steam: Steam's install script taken for the game, and Steam's screen requests in owneetd's own app ids."
status: solved
seen: 2026-11-13
updated: 2026-11-13
tags: [known-solution, steam, owneetd, gamescope]
---
# A Steam game loses the screen at its first start

## Symptom

Batman: Arkham Knight (Steam, on the SATA disk, FrankenPC, 2026-11-13), at its first start:

- Started from the console with Steam closed: back to the home screen at once, "the game closed
  unexpectedly". The journal shows `Steam game started` and `app exited … result=success` 15 s
  later; Steam's `console_log.txt` shows `Running install script evaluator for AppID 208650`, then
  the launch going on (`SynchronizingCloud`, … `waiting for user response to
  ProcessingShaderCache`) after owneetd had counted the game as ended.
- Started again with Steam open: the game's window comes, and some 35 ms later the home screen
  (`on screen focus=steam:208650`, then `focus=home`). The game pauses (it has no focus) and
  neither the console's Resume nor Steam's own brings it back. gamescope logs `xwm: appid clash
  was 208650 now 2124305299`.
- Leaving Steam with Guide held: the interface's start sound twice (`on screen` home, Steam, home
  within 15 ms).

## Cause

Three things:

1. At a game's first start Steam runs its install script (redistributables) through a launcher
   with the game's id: `reaper SteamLaunch AppId=208650 Install=1 -- … iscriptevaluator.exe`.
   owneetd found Steam's games by that launcher, so it listed the script as the game, stopped
   watching Steam's launch (the game "had started") and, when the script ended, counted the game
   as closed. Steam then waited, hidden, on its shader cache ([[open-items]] 3v).
2. owneetd tags every window with its app's id (`STEAM_GAME`: 2124305299 for the game, not
   Steam's 208650: hence gamescope's "appid clash"). Steam reads those ids back from the windows
   and writes them in `GAMESCOPECTRL_BASELAYER_APPID` (e.g. when the game's window comes, or when
   it resumes a game). owneetd only understood Steam's own codes (769, Steam app ids): the unknown
   id was dropped, the game left out, and gamescope showed the home screen.
3. Steam's write reaches gamescope before owneetd puts its own choice back, so gamescope focuses
   Steam for a few milliseconds; owneetd announced that focus, and the interface plays its sound
   on every return to the home screen.

## Solution

owneetd 0.25.30 (`daemon/internal/apps`):

- `reaperAppID`: a launcher with `Install=1` is not a game (test `TestReaperAppID`).
- `steamRequest`: ids that are owneetd's own (a running Steam game, Steam) are understood; a Steam
  game in front stays in front unless Steam names it; Steam's requests are logged (`Steam chose
  what gamescope shows`, `put back`) (test `TestSteamRequestsWhatToShow`).
- `checkWindows`: a focus that is not the first app owneetd shows with a window is not announced
  (gamescope after someone else's write); `steamRequest` looks again after answering.

## How we found it

1. The journal of the test log: `Steam game started` at 12:59:25, `app exited` at 12:59:40, no
   `app-steam-app208650-*.scope` for that start (the script runs in Steam's own unit).
2. Steam's `console_log.txt` (in `owneet-*.steam/`) for the same seconds: the install script's
   command line with `Install=1`, then the launch going on to `ProcessingShaderCache`.
3. Second start: `on screen` game then home 35 ms apart, and in `owneet-*.windows.txt` the game's
   window with `STEAM_GAME = 2124305299`, focusable, but `GAMESCOPECTRL_BASELAYER_APPID` without it.
4. `steamRequest` in `steam.go` only mapped 769 and `steam:<appid>`: any other id was dropped.

## Watch out

- Steam's requests are now in the journal at the INFO level: when a game loses the screen, look
  for `Steam chose what gamescope shows` and its `asked` ids.
- Other launcher options Steam may add (`Install=1` today) would need the same care: a game is a
  launcher with `SteamLaunch AppId=N` and nothing that says it is a helper.
- [[steam-game-runs-hidden-behind-steam]]: Steam games run in a scope of their own since November
  2026.
