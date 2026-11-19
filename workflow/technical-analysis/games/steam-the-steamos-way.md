---
type: technical-analysis
description: "Research for point 2 of the games method: what SteamOS-like sessions do with Steam (its launch flags and environment), what owneetd does instead, and what to try on the FrankenPC."
component: games
tags: [technical-analysis, games, steam]
---
# Steam games the SteamOS way (research, 2026-11-18)

Point 2 of [[game-compatibility-method]]. Owner, 2026-11-18: to be tried ("Steam's interface has not flickered for a
while"); the console's shader percentage waits for it.

## What OwneetOS does today

- gamescope runs with `--fullscreen --steam` (`owneet-session`); Steam starts as `steam -gamepadui`, plus
  `-language` (owneetd, `steam.go`).
- During a launch owneetd keeps Steam hidden ([[step-4.2c-steam-without-its-interface]]): while Steam works on the
  launch (its tasks in `console_log.txt`), while `fossilize_replay` runs (shaders), until the game's window appears;
  it shows Steam only for questions not in `steamRoutineQuestions`, a failed launch, or after 20 s without a game.
- Problems that came from this ([[open-items]] 13, 14; closed 3v, 3z, 3ae): Steam's shader page hidden for 7.5
  minutes; an install script's window hidden for 4 minutes; a game never shown or behind Steam.

## What SteamOS-like sessions do

ChimeraOS's session ([gamescope-session-steam](https://github.com/ChimeraOS/gamescope-session-steam/blob/main/usr/share/gamescope-session-plus/sessions.d/steam)),
the base of several distributions:

- Steam: `steam -gamepadui -steamos3 -steampal -steamdeck`. Valve documents none of the three; their effects are
  only known by trying (community use: Steam behaves as on SteamOS / a Steam Deck).
- Environment telling Steam what gamescope supports: `STEAM_GAMESCOPE_VRR_SUPPORTED`, `…_HDR_SUPPORTED`,
  `…_TEARING_SUPPORTED`, `…_NIS_SUPPORTED`, `…_DYNAMIC_FPSLIMITER`, `…_COLOR_MANAGED`; `STEAM_MULTIPLE_XWAYLANDS=1`
  (each game its own Xwayland); `QT_IM_MODULE=steam`, `GTK_IM_MODULE=Steam` (Steam's keyboard);
  `STEAM_DISABLE_AUDIO_DEVICE_SWITCHING=1`; `STEAM_ALLOW_DRIVE_UNMOUNT=1`; reboot / shutdown sentinels.
- No window of Steam is hidden by the session: Steam itself shows its shader preparation ("Processing Vulkan
  shaders", with a Skip button), install scripts, publishers' launchers, questions.

## To try on the FrankenPC (one change at a time, each in its own test)

> Try 1 built on 2026-11-18 (owneetd 0.25.36); the old way: `owneet.debug.steam_launch=hidden`.
> Try 2 built on 2026-11-19 (owneetd 0.25.40): `owneet.debug.steam_os=os|pal|deck|all`; first with `all` (BioShock, no controller support of its own).

1. owneetd stops hiding Steam during a launch: while nothing of the game is on screen, Steam's own window is what
   gamescope shows (its shader page, an install script's window, a question). The console's "Starting …" screen only
   until Steam's window appears. Check: Steam's flicker ([[steam-loses-the-address-while-its-interface-starts]]),
   the controller in Steam's pages, Guide.
2. Steam with `-steamos3`, then `-steampal`, then `-steamdeck`, each alone: what changes in Steam's pages, in the
   games (a game told it runs on a Steam Deck may choose Deck settings or an 800p resolution: to watch), in
   shutdown / reboot (Steam may try to power off the PC itself: owneetd owns power).
3. The `STEAM_GAMESCOPE_*` variables that match what OwneetOS's gamescope does.

## Open questions

- Whether Steam's own shader page is enough (then demo `4.2c-steam-shaders` is not built) or the console's
  percentage is still wanted: the owner, after the try.
- Steam's own power handling with `-steamos3` against owneetd's: to check before keeping it.
