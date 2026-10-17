---
type: technical-analysis
description: "API for launching, focusing and closing apps and games, gamescope focus, Guide, Steam handling."
component: owneetd
legacy: "docs/daemon-design.md §4 Apps and games"
tags: [technical-analysis, owneetd, api]
---
# owneetd API: Apps and games — implemented (2.9)

Up: [[owneetd-design]] · Conventions: [[owneetd-design#4. API v1 (draft)]]

| Method | Path | Purpose |
|---|---|---|
| POST | `/v1/apps/launch` | `{"id": "…", "name": "…", "kind": "game"/"app", "command": ["…"], "workdir": "/…"}` — start inside the session (201); `workdir` (optional, an existing absolute folder, default the home folder) is where the program starts (3.8) |
| GET | `/v1/apps` | Running apps and games, and `focus`: `home`, an app id, or empty (cage, or no session) |
| POST | `/v1/apps/{id}/focus` | Bring an app to the front ("Resume" on the home screen; gamescope only) |
| POST | `/v1/apps/{id}/close` | Close: SIGTERM to all its processes, SIGKILL after 10 seconds |
| POST | `/v1/apps/{id}/kill` | Force-close a frozen game at once (SIGKILL to all its processes) |

| GET | `/v1/update` | Testers' updates from a USB stick (4.2b): `tester`, `state` (`none`, `available`, `installing`, `done`, `failed`, `no_stick`, `not_tester`), `message`, `packages` (`name`, `from`, `to`), `running` |
| POST | `/v1/update/check` · `/v1/update/apply` | Start a check or the installation (202): root units `owneet-update@check` / `@apply.service`, allowed by a polkit rule; the result comes as `update.changed`. Errors `update.not_tester`, `update.busy` (409) |
| GET | `/v1/steam` | `installed`, `allowed` (false in a live system with less than 12 GB of RAM), `prepared` (Steam has started once: no long first download), `running`, `games` (Steam app ids installed completely) (4.2); `downloads` (`appid`, `state`: `downloading` / `updating` / `queued`, `done` / `total` bytes, `rate` bytes per second; the one moving first), `away` (app id → disk name: installed on a disk that is not connected), `account` (someone has signed in to Steam here), `licences` (Unix time Steam last wrote `packageinfo.vdf`), `nvidia` (Steam's window may show display errors) (4.2c) |
| POST | `/v1/steam` | One of `{"open": "library"}` / `{"open": "store"}`, `{"run": "480", "name": "…"}`, `{"install": "480"}`, `{"uninstall": "480"}` (also cancels a download; 4.2c), `{"ask": "480"}` (the next start of that game asks the user first, a licence agreement: Steam is shown at once for it; nothing starts), with `"language": "it"` (the console's language tag: Steam starts with `-language italian`) — Steam starts if needed (202); a game is listed in `/v1/apps` as `steam:480` once Steam has started it |

Errors: `apps.unavailable` (503), `apps.invalid` (400), `apps.program_not_found` (400),
`apps.no_session` (409), `apps.already_running` (409, same id), `apps.game_running` (409, one game
at a time; apps such as the browser may run next to it), `apps.unknown_app` (404),
`apps.focus_unsupported` (409, cage), `apps.no_window` (409), `apps.failed` (502),
`steam.needs_install` (409: live system with too little memory for Steam's files).

- **Session:** `owneet-session` starts the console UI through `owneet-session-app`, which writes
  `$XDG_RUNTIME_DIR/owneet/session-env` (display variables, session mode, process id of the home
  screen). Apps get those variables, so they open in the console session.
- **Each app runs in its own transient systemd user service** (`owneet-app-ID.service`, created
  over the user's D-Bus): closing it stops every process it started (launchers, Proton, wine), its
  output goes to the journal, and apps still running are found again when owneetd restarts.
- **gamescope** runs with `--steam`. It then shows only windows tagged with an app id
  (`STEAM_GAME`) and lets the shell choose which app is on screen, as Steam does on SteamOS.
  owneetd watches new windows on gamescope's X server (`github.com/jezek/xgb`, BSD-3-Clause,
  vendored), tags the home screen and each app (by process: the home screen's process id, or the
  app's systemd unit from `/proc/PID/cgroup`; the process is the window's `_NET_WM_PID`, else the
  X server's own record of the client through the X-Resource extension, `xgb/res`: Unity 5 games
  such as CAYNE set no `_NET_WM_PID`, 2026-10-16), and sets `GAMESCOPECTRL_BASELAYER_APPID`: a new app
  comes to the front as soon as its window appears, with the home screen as fallback. App ids
  are derived from the app's id, so they survive an owneetd restart.
- **Guide** (owned by the system, [[controller-input-map]]): in gamescope it toggles between
  the home screen and the app last shown; the game keeps running behind the home screen. While
  Steam or a Steam game is on screen a short press is Steam's (Steam reads the controllers itself
  and opens its menu or overlay), and holding Guide for 1 second (`HoldToHome`) comes back to the
  home screen. In cage,
  which shows only the newest window, holding Guide for 2 seconds closes the app on screen; a short
  press does nothing. `guide.pressed` and `guide.released` are still sent to clients.
- **Steam without its interface (4.2c):** Steam starting a game stays **hidden** when an account
  has signed in: its window is not brought to the front when it appears (the home screen, with the
  console's "Starting …" screen, stays until the game's window), and Guide from the home screen
  never brings Steam's own window back unless it was the app last on screen. If no game has
  started 20 s after the address was handed over, Steam probably waits for the user (a licence to
  accept, a cloud conflict, launch options): its window is shown; not while Steam prepares
  the game's shaders (a `fossilize_replay` process in Steam's unit): the 20 s start again. Once
  the game has started, Steam's window stays out of what gamescope may show (also when Steam asks
  for it) until the game's window appears, then goes back behind the game; 20 s without a game
  window, it is shown behind the game (owneetd 0.14.3, [[step-4.2c-steam-without-its-interface]]). Not `-silent`: owneetd hands
  Steam its first address once Steam's window exists, and gamescope already shows only what
  owneetd chooses. `install` / `uninstall` hand `steam://install/N` / `steam://uninstall/N` to
  Steam and show its confirmation; once Steam acts on it (the game's appmanifest appears, goes, or
  changes state) the home screen comes back by itself; cancelled in Steam, nothing changes and
  holding Guide comes back (the confirmation is forgotten after 10 minutes). While Steam runs (and
  once after it stops) owneetd reads the appmanifests every second and sends `steam.changed` (the
  status above) when games, downloads or disks change. Downloads from `StateFlags` (2 update
  required, 4 fully installed, 256 / 1048576 running, 512 paused, 1024 started, 2048 uninstalling)
  and `BytesDownloaded` + `BytesStaged` of `BytesToDownload` + `BytesToStage`; the one Steam works
  on is the one whose bytes grew in the last 5 s; an installed game with an update waiting stays
  "installed" (Steam updates it before playing). Disks not connected from `libraryfolders.vdf`
  (folder `path` missing, its `apps`; name = `label`, else the mount folder's name).
- Events: `app.started`, `app.exited` (with systemd's result: `success`, `exit-code`, `signal`,
  `timeout`…), `app.window` (gamescope can show one of the app's windows for the first time, e.g.
  Steam ready after its first download: its early helper windows are never shown), `focus.changed`
  (also when the screen changes by itself, e.g. an app's window appears: the interface reads the
  controllers only while it is on screen; in cage, which owneetd cannot read, the newest app is
  taken to be on screen).
- **Steam (4.2):** the app `steam`, started as `env -u GAMESCOPE_WAYLAND_DISPLAY steam -gamepadui
  URL` (see below), with `-language` from the interface's language and, under the NVIDIA driver,
  `-cef-disable-gpu` (Steam's pages drawn with the GPU showed garbled, stale pictures inside
  gamescope; games keep the GPU); when it already runs, owneetd hands it the `steam://` address.
  Steam is closed cleanly (also at shutdown): its unit's stop asks Steam to exit through
  `steam-runtime-steam-remote -shutdown` and waits for it, up to 20 s (killed with its processes,
  Steam checks all its files at the next start). A game Steam
  starts runs inside Steam's unit under Steam's launcher (`reaper SteamLaunch AppId=N -- …`):
  owneetd finds it there (every second, and when one of its windows appears), lists it as the
  game `steam:N` (name from the interface, else from its `appmanifest`), tags its windows with an
  app id of its own (Guide, Resume and "one game at a time" work as for any game), and closes it
  by signalling the launcher's processes only (Steam keeps running). Steam's play time is Steam's
  (the frontend does not add its own, 4.1).
- **Steam writes what gamescope shows too** (through X11, even without `GAMESCOPE_WAYLAND_DISPLAY`;
  seen in the test VM: once when it starts, in its own codes, e.g. `413091,769`). owneetd watches
  the property and tells its own writes from others' (those of the last few seconds): while Steam
  or one of its games is in front, it shows what Steam asks for, translated (769: Steam's window;
  a Steam app id: that game; unknown codes dropped; the home screen last); otherwise (e.g. the home
  screen after Guide) it puts its own choice back: Steam never takes the screen by itself.
- Tested in the test VM: gamescope with its headless backend (test hook
  `owneet.debug.gamescope_backend=headless`) and cage, a virtual gamepad for Guide, `mpv` as the
  test app.
