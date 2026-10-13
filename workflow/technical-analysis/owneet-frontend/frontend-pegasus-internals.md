---
type: technical-analysis
description: "How Pegasus works: backend, frontend, theme API, data providers kept or compiled out, game launching."
component: owneet-frontend
legacy: "docs/frontend-architecture.md §3"
tags: [technical-analysis, frontend]
---
# owneet-frontend: how Pegasus works

Up: [[frontend-architecture]]

```text
main.cpp ── Backend ──┬── FrontendLayer ── QML engine: main.qml (menus) + the theme (theme.qml)
                      ├── ProviderManager ── providers ── game list (Collections, Games)
                      ├── ProcessLauncher ── QProcess: starts the game as a child process
                      └── model::Api ── exposed to QML as `api`
```

- **Backend (C++, about 20 000 lines):** settings (`AppSettings`, an INI-like file), paths
  (`Paths`: `~/.config/pegasus-frontend`), data providers, game launching, gamepads, power.
- **Frontend (QML, about 5 600 lines):** Pegasus's own screens: main menu (Start button),
  settings (game folders, data providers, key and gamepad editors), help, reboot/shutdown dialogs.
- **Theme (QML):** the screen the user sees. Pegasus loads `theme.qml` from a theme folder (or the
  built-in theme) and gives it the `api` object.

### Theme API (what the OwneetOS theme can use)

| `api.…` | What |
|---|---|
| `collections`, `allGames` | Lists (models) of collections and games |
| game: `title`, `summary`, `description`, `releaseYear`, `players`, `rating`, `assets` (cover, logo, background, screenshots, videos…) | Game data |
| game: `playCount`, `playTime`, `lastPlayed`, `favorite` | Play statistics and favourites, stored locally |
| game: `launch()` | Start the game |
| `keys` | Key bindings: `isAccept(event)`, `isCancel`, `isDetails`, `isFilters`, `isNextPage`, `isPrevPage`, `isPageUp`, `isPageDown`, `isMenu`, and the directions |
| `device` | Battery level (SDL) |
| `memory` | Small key/value store for the theme (persisted) |

Pegasus's own menus also get `Internal` (a separate, private object): settings, gamepad list,
`system.quit/reboot/shutdown/suspend`. The OwneetOS theme uses owneetd for these instead (3.8).

### Game data providers (chosen at compile time, `WITH_COMPAT_*`)

| Provider | What it reads | OwneetOS |
|---|---|---|
| `pegasus_metadata` | `metadata.pegasus.txt` files in game folders (title, launch command, assets) | **keep**: local DRM-free games |
| `pegasus_media`, `pegasus_playtime`, `pegasus_favorites` | media folders, play time, favourites | **keep** |
| `steam` | local Steam library files, **plus** `store.steampowered.com/api/appdetails` | **keep, without the store download**: installed games and their play time from local files (4.1, see below) |
| `gog` | GOG Galaxy files, **plus** `api.gog.com` | **compile out** (GOG comes later with our own integration) |
| `android_apps` | Android apps, **plus** Play Store pages | **compile out** |
| `es2`, `launchbox`, `logiqx`, `lutris`, `playnite`, `skraper` | other frontends' and launchers' data | **compile out** (not needed; less code, less risk) |

### Game launching today

`game.launch()` → `ProcessLauncher` runs the launch command as a **child process** of Pegasus.
Before starting it, Pegasus **unloads the whole QML interface** (`FrontendLayer::teardown`) to
free memory, and reloads it when the game ends.

This does not fit OwneetOS: owneetd starts games in their own systemd services (closing a game
closes all its processes) and the **Guide button switches between the home screen and the
running game**, so the home screen must stay loaded while a game runs.
