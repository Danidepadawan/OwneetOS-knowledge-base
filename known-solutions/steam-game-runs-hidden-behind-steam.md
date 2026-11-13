---
type: known-solution
description: "A Steam game starts but never comes to the front: it runs behind Steam's window, owneetd never logs \"Steam game started\". Steam now starts games in a systemd scope of their own."
status: solved
seen: 2026-11-12
updated: 2026-11-13
tags: [known-solution, steam, owneetd, gamescope]
---
# A Steam game runs hidden behind Steam

## Symptom

The owner starts a Steam game from the console (My Little Puppy, on the SATA disk, FrankenPC,
2026-11-12): Steam's page of the game shows "Riprendi" (resume), the game's window never comes to
the front, Guide and back show Steam's page again. In the journal there is `Game process added`,
`Started app-steam-app2102040-4267.scope` and then only owneetd's `no Steam game yet: Steam may be
waiting for the user, shown`; owneetd never logs `Steam game started`. The windows' report
(`owneet-*.windows.txt`) lists the game's window (`class="steam_app_2102040"`, `STEAM_GAME =
2102040`) from 20 s after the start, but `GAMESCOPECTRL_BASELAYER_APPID` never names it.

## Cause

Steam's client of November 2026 (version 20261109) starts each game in a transient systemd scope of
its own, `app-steam-app<APPID>-<PID>.scope` in the user's `app.slice`, out of Steam's unit
`owneet-app-steam.service`. owneetd found Steam's games only by their launcher (`reaper SteamLaunch
AppId=N`) among the processes of Steam's unit (`scanSteam`, `UnitOfPID`): the game was never listed,
so its window got no app id and owneetd kept Steam's window in front. Until October the games ran
inside Steam's unit (the logs of 2026-10-17/18 show `Steam game started` and no such scope).

## Solution

owneetd 0.25.28: `unitOfCgroup` (`daemon/internal/apps/session.go`) counts a process in a scope
named `app-steam-app<N>-<PID>.scope` as Steam's (`owneet-app-steam.service`), so `scanSteam`,
the windows' app ids and closing a game find it again. Test `TestSteamGameInItsOwnScope`. Waits for
the owner's check on the FrankenPC.

## How we found it

1. The test log's screenshot at 18:10:30 showed Steam's page of the game with "Riprendi": Steam
   thought it was running.
2. `owneet-*.windows.txt` at 18:10:28: the game's window mapped, focus on Steam's window.
3. The journal: no `Steam game started`; `Started app-steam-app2102040-4267.scope` right after
   `Game process added`.
4. `grep "Steam game started"` in the October logs (`out/test-logs/stick-2026-11-05/`): present,
   with no `app-steam-app` scope: Steam changed how it starts games.

## Watch out

- Steam may change the scope's name again: when a Steam game does not come to the front, look for
  `Steam game started` in owneetd's log and for the game's unit in `/proc/PID/cgroup`.
- Stopping Steam's unit does not stop a game in its own scope: Steam's reaper ends it with Steam.
- It may also be why a game preparing its shaders left the console on the library with no notice
  ([[open-items]] 3v): to check at the next Steam game's first start.
