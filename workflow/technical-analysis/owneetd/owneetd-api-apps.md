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
| GET | `/v1/apps` | Running apps and games, and `focus`: `home`, an app id, or empty (no session); in cage, what owneetd last decided (owneetd 0.12.2) |
| POST | `/v1/apps/{id}/focus` | Bring an app to the front ("Resume" on the home screen). In cage (owneetd 0.12.2) it only sends `focus.changed`: the interface hides its own window and cage shows the app |
| POST | `/v1/apps/{id}/close` | Close: SIGTERM to all its processes, SIGKILL after 10 seconds |
| POST | `/v1/apps/{id}/kill` | Force-close a frozen game at once (SIGKILL to all its processes) |

| GET | `/v1/update` | Testers' updates from a USB stick (4.2b): `tester`, `state` (`none`, `available`, `installing`, `done`, `failed`, `no_stick`, `not_tester`), `message`, `packages` (`name`, `from`, `to`), `running` |
| POST | `/v1/update/check` · `/v1/update/apply` | Start a check or the installation (202): root units `owneet-update@check` / `@apply.service`, allowed by a polkit rule; the result comes as `update.changed`. Errors `update.not_tester`, `update.busy` (409) |
| GET | `/v1/apps/catalog` | The optional web apps (5.0.0): `apps` (`id`, `nameKey`, `icon`, `url`, `installed`, `busy` `install`/`remove`, `sizeMiB`: the space installing it takes now, its missing engines), `allowed` (false in a live system with less than 12 GB of RAM). From `/usr/share/owneet/apps.json`; the engines (Brave) are never listed |
| POST | `/v1/apps/catalog/{id}/open` | Open an installed web app (204), or bring it back when it is open (5.1). owneetd builds the command from the catalogue (the interface sends no program, flag or address): Brave in kiosk mode with the web app's own profile (`$XDG_DATA_HOME/owneet/webapps/ID`, created with Widevine on and no welcome pages; before every opening owneetd also turns off Brave's own windows and panels that need a mouse: its Widevine question, `brave.ask_widevine_install` = false, and its sidebar, in both settings files, keeping the rest), the console's extension (`--load-extension=/usr/share/owneet/extension`), X11 under gamescope, and the user agent of the web app's catalogue entry when it has one (`"userAgent"`, `--user-agent=…`: YouTube's TV interface, 5.3); it runs as the app `web:ID` of kind `webapp`. The catalogue is read at every opening. Errors `apps.unknown` (404), `apps.not_installed` (409), and those of `/v1/apps/launch` (`apps.game_running`: one game or web app at a time). **A web app's first opening** (its profile has no Widevine yet, 5.4) answers **202**: owneetd first runs Brave with no window in the profile until Widevine is downloaded (60 s at most), then starts the web app (`app.started`); without Widevine it does not open: `apps.open_failed` with `code` `apps.widevine_failed` (`apps.failed`: the web app did not start); meanwhile any opening answers `apps.preparing` (409). Without the user's consent: `apps.widevine_consent` (409) |
| POST | `/v1/apps/catalog/{id}/install` · `/v1/apps/catalog/{id}/remove` | Install or remove a web app (202). Removing closes it first if it is open and deletes its profile (5.1). The first web app installs its engine, the last one removes it: root units `owneet-apps-install@ENGINE` / `owneet-apps-remove@ENGINE.service` (polkit rule `50-owneet-apps.rules`), from the ISO's bundled repository; the outcome comes as `apps.catalog.changed` (the status plus `result`: `id`, `action`, `ok`, `error`). Errors `apps.unknown` (404), `apps.busy`, `apps.needs_install`, `apps.no_space` (409) |
| GET · POST | `/v1/webapps/widevine` · `/v1/webapps/widevine/accept` · `/v1/webapps/widevine/terms` | The user's consent to Google's terms for Widevine (5.4, [[step-5.4-netflix]]): `accepted`, `ask` (opening a web app asks first: never accepted, or a newer Widevine in the profiles than the accepted one), `updated` (asked again after an update). `accept` records it with the newest Widevine version in the profiles (none yet: the first one downloaded afterwards counts as accepted), per user (one today), in `$XDG_STATE_HOME/owneetd/widevine.json`. `terms` (`{"language": "it"}`, optional) opens Google's live terms page (`policies.google.com/terms?hl=…`) like a web app, `web:widevine-terms`, in its own profile without Widevine. Without the consent `/v1/apps/catalog/{id}/open` answers `apps.widevine_consent` (409); `widevine_opted_in` is set before every opening from the consent |
| GET | `/v1/webapps/look` | The look the console's extension draws with (5.2): `accent` (the palette's accent, `#RRGGBB`), `language`. Sent by the interface in the body of `/v1/apps/catalog/{id}/open` (`{"accent": "#FF8A5B", "language": "it"}`, optional; unknown fields refused, invalid values dropped) |
| GET / POST | `/v1/webapps/keyboard` | The console's keyboard for a web app's text field (5.2, [[extension-design]]). Opened by the extension (`{"open": true, "kind": "email", "label": "…", "value": "…"}`; kinds text, email, password, search, url, tel, number): in cage the home screen comes to the front; in gamescope (owneetd 0.12.3) nothing changes on screen, the interface draws the keyboard over the page. Closed by the interface or the extension (`{"open": false, "next": true}`; `next`: Done, the selection moves on): in cage the web app comes back. Event `webapp.keyboard` (with `app`, the web app's catalogue id). **Never left open by a dead interface** (owneetd 0.12.2): without `/shown` within 3 s of the open request, when the interface's process stops or is replaced afterwards (`OWNEET_HOME_PID` of the session file), or when the web app exits, owneetd closes it (`open: false`, no `next`) |
| POST | `/v1/webapps/keyboard/shown` | The interface confirms that it shows the keyboard (owneetd 0.12.2). `webapps.keyboard_closed` (409) when it is not open |
| POST | `/v1/webapps/text` | `{"text": "…"}` (up to 64 characters) or `{"key": "backspace"}` (backspace, left, right): typed into the field by the extension. Event `webapp.text` |
| POST | `/v1/webapps/ask-close` | B with nothing to go back to in the web app: the home screen comes to the front (gamescope) and the interface asks "Close {name}?". Event `webapp.ask_close` (`app`) |
| GET | `/v1/steam` | `installed`, `allowed` (false in a live system with less than 12 GB of RAM), `prepared` (Steam has started once: no long first download), `running`, `games` (Steam app ids installed completely) (4.2); `downloads` (`appid`, `state`: `downloading` / `updating` / `queued`, `done` / `total` bytes, `rate` bytes per second; the one moving first), `away` (app id → disk name: installed on a disk that is not connected), `account` (someone has signed in to Steam here), `licences` (Unix time Steam last wrote `packageinfo.vdf`), `nvidia` (Steam's window may show display errors) (4.2c) |
| POST | `/v1/steam` | One of `{"open": "library"}` / `{"open": "store"}`, `{"run": "480", "name": "…"}`, `{"install": "480"}`, `{"uninstall": "480"}` (also cancels a download; 4.2c), `{"ask": "480"}` (the next start of that game asks the user first, a licence agreement: Steam is shown at once for it; nothing starts), `{"windows": "399070", "name": "…"}` (its Linux version does not start: Steam closed, the game's version for Windows set, the game started again; 4.5), with `"language": "it"` (the console's language tag: Steam starts with `-language italian`) — Steam starts if needed (202); a game is listed in `/v1/apps` as `steam:480` once Steam has started it |

Errors: `apps.unavailable` (503), `apps.invalid` (400), `apps.program_not_found` (400),
`apps.no_session` (409), `apps.already_running` (409, same id), `apps.game_running` (409, one game
or web app at a time, kinds `game` and `webapp`; other apps may run next to it), `apps.unknown_app` (404),
`apps.focus_unsupported` (409: no way to switch windows; not in cage since 0.12.2), `apps.no_window` (409), `apps.failed` (502),
`steam.needs_install` (409: live system with too little memory for Steam's files), `webapps.unavailable` (503), `webapps.invalid` (400), `webapps.no_webapp` (409: no web app open),
`webapps.keyboard_closed` (409).

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
  are derived from the app's id, so they survive an owneetd restart. A window whose process left its unit is still found when that process is the parent of one in an app's unit: Brave (the web apps' engine) moves its main process, which owns the windows, into a scope of its own (`app-org.chromium.Chromium-PID.scope`) when it starts, and its helpers stay in the unit (5.1).
- **Guide** (owned by the system, [[controller-input-map]]): in gamescope it toggles between
  the home screen and the app last shown; the game keeps running behind the home screen. While
  Steam or a Steam game is on screen a short press is Steam's (Steam reads the controllers itself
  and opens its menu or overlay), and holding Guide for 1 second (`HoldToHome`) comes back to the
  home screen. In cage,
  which shows only the newest window, holding Guide for 2 seconds closes the app on screen; a short
  press does nothing. `guide.pressed` and `guide.released` are still sent to clients. On a keyboard the Super (Windows) key is Guide (owneetd 0.11.18): keyboards are read like controllers, never grabbed, and only their Super keys count; the events then name the controller `keyboard`.
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
  taken to be on screen), `steam.launch_failed` (`{"appid", "reason": "linux_version"}`: see below). **In cage owneetd decides and the interface carries it out** (0.12.2,
  for the web keyboard and "Close {name}?" of 5.2): "show the home screen" and "bring back an
  app" only send `focus.changed`; on `home` the interface shows its own window again (cage shows
  the newest window), on an app it hides it.
- **A Steam game whose Linux version does not start (4.5, `steamwindows.go`):** for 2 minutes after
  `run`, owneetd reads the new lines of Steam's console log (`logs/console_log.txt`, undocumented,
  times checked against the request) for `GameAction [AppID N, …] : LaunchApp failed with
  AppError_28` (Steam's "Missing game executable"). Unless the game already has a compatibility
  tool, it sends `steam.launch_failed` and does not show Steam's error. `windows` closes Steam
  cleanly (up to a minute), writes the game's tool in `config/config.vdf` (InstallConfigStore →
  Software → Valve → Steam → CompatToolMapping → N: `name`, `config`, `priority` 250, as Steam's
  own "Force the use of a specific compatibility tool"), Valve's newest `proton_N` registered in
  `logs/compat_log.txt`, newest by app id (the names drop the dot: `proton_513` is 5.13; else
  `proton_experimental`; [[steam-integration]], owner 2026-10-18), then `run`s the game again;
  Steam downloads that Proton itself the first time. The same log gives the launch's tasks
  (`LaunchApp changed task to DownloadingDepots`, `CreatingProcess`, `WaitingGameWindow`…):
  while Steam works on one, Steam stays hidden past the 20 s, however long (owneetd 0.14.5);
  a question Steam has waited on (`waiting for user response to …`) for 3 s is shown (Steam
  answers its routine ones within a second).
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
- **Web apps and the extension (5.2):** the extension cannot reach the socket; Brave starts
  `owneet-bridge` (`/usr/lib/owneet/owneet-bridge`, a native-messaging host) for it, listed
  system-wide by the owneetd package (`/etc/opt/chrome/native-messaging-hosts/org.owneet.bridge.json`,
  a static file; Brave does not read hosts from the web apps' profiles) for the extension's id only (derived from its folder `/usr/share/owneet/extension`:
  `jlekhdampjopkpjhbgilolchffjpdjcn`). The bridge calls `/v1/webapps/*` and passes `webapp.keyboard`
  (closed) and `webapp.text` back to the extension.
