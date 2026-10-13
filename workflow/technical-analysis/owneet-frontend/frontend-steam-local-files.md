---
type: technical-analysis
description: "Which Steam files are read (and which never) to list installed games and play time."
component: owneet-frontend
legacy: "docs/frontend-architecture.md §3 Steam"
tags: [technical-analysis, frontend]
---
# owneet-frontend: Steam's local files (step 4.1, checked on a real Steam client in October 2026)

Up: [[frontend-architecture]]

Steam's folder is `~/.local/share/Steam/` (`OWNEET_STEAM_DIR` points elsewhere, for tests).

| File | What it gives | Used |
|---|---|---|
| `steamapps/libraryfolders.vdf` | every library folder, also on disks not connected | yes: a missing folder is skipped, its games are not shown (owner's choice) |
| `<library>/steamapps/appmanifest_<appid>.acf` (text) | name, appid, `StateFlags` (bit 4: fully installed; an update waiting keeps it), size | yes: games installed completely; Valve's tools left out by id and by name (Proton, Steam Linux Runtime, Steamworks redistributables) |
| `config/loginusers.vdf` | accounts on this computer; `MostRecent` in older clients, `Timestamp` of the last login in newer ones | yes: picks the account |
| `userdata/<account id>/config/localconfig.vdf` | `UserLocalConfigStore/Software/Valve/Steam/apps/<appid>`: `Playtime` (minutes, whole account), `LastPlayed` (Unix time) | yes: play time and last played |
| `appcache/librarycache/<appid>/` | cached artwork: `header.jpg` for most apps, `library_600x900.jpg` (portrait cover) for about a quarter, `library_hero.jpg`, `logo.png`, hashed files | later: covers (4.4) |
| `appcache/appinfo.vdf` (binary, format 29 since 2024: key string table) | every app the client has looked up, with its type (game, tool, DLC…), also games only seen in the store | no: not a list of owned games |
| `appcache/packageinfo.vdf` (binary) | packages of the account's licences | no: its games did not match the client's own count exactly; owned games that are not installed are installed from Steam's library ([[game-library]]) |
| `userdata/<id>/config/licensecache` | licences, encrypted | never read |

Text files are Valve's "KeyValues" format, read by `SteamPlaytime.cpp`'s small reader (keys
compared without regard to case: clients write both `Valve` and `valve`).
