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
| `appcache/appinfo.vdf` (binary, formats 27–29; 29 since 2024: key table at the offset after the header) | every app the client has looked up, with its type (game, tool, DLC…) and name | yes (4.2c, `SteamOwned.cpp`): type and name of the licences' apps; only type "game" |
| `appcache/packageinfo.vdf` (binary, formats 27–28) | packages of the account's licences, with `status` and `appids` | yes (4.2c): apps of packages with `status` 0, package 0 left out → every owned game (88 on the owner's account, as Steam shows, checked on 2026-10-14) |
| `userdata/<id>/config/licensecache` | licences, encrypted | never read |

Every Steam game in the library carries `extra["steam.appid"]` and `extra["steam.installed"]`
(as read): the theme takes what is installed, downloading or away from owneetd while it runs
([[owneetd-api-apps]]). Not-installed games start the same way (`steam://rungameid`), but the
theme installs them first ([[step-4.2c-steam-without-its-interface]]).

Binary "KeyValues": a type byte (0 block, 1 string, 2 int32, 7 uint64, 8 end), the key (a C string,
or in appinfo v29 an int32 index in the key table), the value. Each packageinfo entry: package id
(0xFFFFFFFF ends), 20-byte hash, change number, (v28) 8-byte token, KeyValues. Each appinfo entry:
app id (0 ends), size, state, last updated, token, 20-byte hash, change number, (v28+) 20-byte
binary hash, KeyValues.

Text files are Valve's "KeyValues" format, read by `SteamPlaytime.cpp`'s small reader (keys
compared without regard to case: clients write both `Valve` and `valve`).
