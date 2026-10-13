---
type: technical-analysis
description: "What OwneetOS changes in Pegasus's C++ and what lives in the QML theme (foundations, shell, sections)."
component: owneet-frontend
legacy: "docs/frontend-architecture.md §4"
tags: [technical-analysis, frontend]
---
# owneet-frontend: what OwneetOS changes

Up: [[frontend-architecture]]

### In C++ (small, targeted changes)

Done in step 3.2: names, providers and Steam download, Guide removed, window tag, Pegasus's
screens hidden, and also: the interface stays loaded during games (no teardown, no blocking wait), button
repeat stopped when input pauses, SDL's SIGTERM handler disabled, pointer hidden until the mouse
is used. Done in 3.5: input map. Done in 3.8: owneetd client and launching through owneetd; power
actions through owneetd come with the screens that offer them (3.9).

| Change | Why | Step |
|---|---|---|
| Names: window title, application and organisation name, executable `owneet-frontend`, config folder `~/.config/owneet-frontend`; Pegasus logo and icons not installed | Pegasus's trademark terms ([[legal-compliance]]) | 3.2 |
| Build only the providers listed above; remove the Steam store download | Local data only, offline ([[legal-compliance]], C9) | 3.2 |
| Pegasus's Roboto fonts and button images removed; Bricolage Grotesque and Lexend bundled (OFL-1.1, static instances from `tools/branding/make-fonts`) | Own fonts and glyphs ([[legal-compliance]]) | 3.3 |
| **owneetd client** `owneet::Daemon` (`src/backend/owneet/`, `owneetd` in QML): `get/post/put/remove(path, body, callback)` over the Unix socket (`QLocalSocket`, HTTP/1.0 + JSON) and the event stream (`event(type, data)`, reconnects by itself, `connected`) | QML's `XMLHttpRequest` cannot reach a Unix socket; owneetd listens only there (no TCP port, by design) | 3.8 |
| **Game launching through owneetd** (`POST /v1/apps/launch` with id `game-<title>-<hash of the file>`, the command and its working folder) when its socket exists, otherwise `QProcess` as before (tests); **no interface teardown**; the game ends with owneetd's `app.exited`, which also updates the play time; errors carry owneetd's code, translated by the theme | Guide toggles home ↔ game; games in their own services | 3.8 |
| Gamepad input follows `focus.changed`: the interface reads the controllers only while the home screen is on screen (gamescope) | A game on screen gets every button | 3.8 |
| Power actions (`Internal.system.reboot/shutdown/suspend`) through owneetd | One place for power, with its events | 3.9 |
| **Guide removed** from the gamepad → key mapping | Guide belongs to the system ([[controller-input-map]]) | 3.2 |
| Gamepad → key mapping changed to the OwneetOS input map (LB/RB = sections, LT/RT = filters, Y = page option, Menu = options, right stick = fast scrolling), fixed (not saved in the settings) | [[controller-input-map]] | 3.5 |
| The window tags itself for gamescope (`STEAM_GAME` with owneetd's home app id) | Shown even if owneetd is not running ([[owneetd-design]]) | 3.2 |
| Pegasus's own screens (main menu on Start, settings, help, editors) not shown | Replaced by OwneetOS screens | 3.2 / 3.9 |

The theme API, the data model, the providers we keep, play statistics, favourites, the SQLite
cache and the QML engine stay as they are.

### In QML (everything the user sees)

The **OwneetOS theme** (`src/themes/owneet/`, the built-in default): design tokens and palettes (3.3), translations with JSON message files
(3.4), navigation (3.5), home (3.6), library (3.7), settings (3.9), on-screen keyboard (3.10),
notifications (3.11). Each screen starts with an interactive demo approved by the owner.

**Foundations (3.3)**, in `src/themes/owneet/foundation/`, used by every screen:

| Component | What |
|---|---|
| `Theme` (singleton) | Palettes (eight color tokens each), fonts, sizes on the 1280×720 grid (`px()`), text sizes that follow the "Text size" option (`fs()`), TV safe area, reduce motion, button glyph set |
| `FocusFrame` | Focus ring (background gap + accent ring) and lift of the selected item |
| `Glyph`, `Prompt`, `PromptBar` | Button glyphs drawn in QML (Xbox- and Nintendo-style letters, PlayStation-style shapes, chosen from the connected controller's name), the prompt bar |
| `Sheet`, `PalettePicker` | Window over the screen with its own prompt bar; palette picker with live preview |
| `Label`, `Choice`, `SettingRow` | Section label, segmented choice, settings row (switch or picker) |
| `Tr` (singleton), `LanguagePicker` | Translated text (3.4), language list |
| `Nav` (singleton), `NavArea`, `NavGroup` | Input map as actions, spatial navigation (with groups that remember their selection, 3.6), list keys, feedback for sounds (3.5) |
| `Button`, `Dialog`, `Toast` | Round buttons, compact centred windows with a row of buttons, short messages (3.6) |
| `GameInfo` (singleton), `Cover`, `GameArt` | Texts about a game, covers, art generated from the title (3.6) |

**Translations (3.4):** `owneet::I18n` (`src/backend/owneet/`, exposed to QML as `i18n`) loads one
JSON file per language from `/usr/share/owneet-frontend/i18n/` (repository: `frontend/i18n/`) and
`~/.config/owneet-frontend/i18n/`; English is the default and the fallback. The theme uses it
through the `Tr` singleton. How to translate: `docs/translating.md` (code repository).

**owneetd (3.8):** the shell (`theme.qml`) follows the running apps, what is on screen, the
controllers (battery) and the network through `owneetd`; the home screen shows the running game
(Resume in gamescope, Close game with a confirmation), the top bar the controller's battery and
the network (Wi-Fi signal or cable).

**System facts (3.9):** `owneet::SystemInfo` (`systemInfo` in QML) gives the OwneetOS version
(`/etc/os-release`), the credited projects (CREDITS.md tables) and every installed package with
its licence (pacman's local database), for Settings → System → Credits and licences.

**Disks (3.7):** `owneet::Storage` (`src/backend/owneet/`, `storage` in QML) lists the system disk
and the mounted disks with their free space (Qt's `QStorageInfo`), for the library.

Appearance choices are saved in the theme's memory (`api.memory`). Until Settings exists (3.9),
they are opened from the temporary Settings section (`SettingsPage.qml` → `AppearanceSheet.qml`).

**Shell and sections (3.6):** `theme.qml` is the shell: top bar (wordmark, sections with the LB / RB
glyphs, controller, clock), the sections on LB / RB, the prompt bar (each section gives its
prompts, following the selected item), the windows (`Dialog`: details, options, confirmations;
`Sheet`: pickers) and short messages (`Toast`). Sections: `HomePage.qml` (hero, apps, notices,
recently played, in three `NavGroup`s), `LibraryPage.qml` (grid, filters, sort, disks: 3.7),
`SettingsPage.qml` (Settings, 3.9: sections on the left, panel on the right; `CreditsSheet.qml`). `GameInfo` gives the texts about a game (source,
last played, play time) and the order "most recently played first"; `Cover` and `GameArt` draw a
game's own image from local files or, without one, art generated from its title.

### Not changed / not needed

The qmake project, Android/Windows/macOS code paths, and the tests of removed providers stay in
the tree (unused) unless they get in the way; removing them would make upstream updates harder.
