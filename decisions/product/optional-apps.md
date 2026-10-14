---
type: decision
description: "Users install only the apps they want (step 5.0); the ISO becomes slim and apps are downloaded when chosen."
area: product
status: active
decided: 2026-10-13
updated: 2026-10-14
legacy: "PROJECT_RULES.md §13 (2026-10-13)"
tags: [decision, product, apps]
---
# Optional apps

- The user installs **only the apps they want**: at installation and later, where installed and
  missing apps are shown differently (the home screen's Apps grid from
  [[step-5.0.0-optional-web-apps]], the apps page from [[step-5.7-apps-page]]).
- Step 5.0 is split: **web apps** (Netflix, YouTube, Spotify) in [[step-5.0.0-optional-web-apps]],
  **gaming programs** (Steam, Epic, GOG, RetroArch) in [[step-5.0.1-optional-gaming-apps]].
- **Brave ships inside the ISO as package files** (a small offline pacman repository) and is
  installed from them only when the user picks a web app: no internet, no USB stick. This replaces
  "apps downloaded when chosen" for Brave; for the gaming programs it is decided at 5.0.1
  ([[distribution-and-updates]]).
- **The user never sees Brave**: it is the hidden engine of the web apps, installed with the
  first one and removed with the last one. Free web browsing is not in Wave 1 ([[wave-2]]).
- **Discord** waits for the chat modules ([[wave-2]], [[online-and-chat]]).
- In the live system, apps follow the same RAM rule as Steam, at least 12 GB
  ([[steam-integration]]).

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-13 | **Optional apps** (new step 5.0): the user installs only the apps they want (at installation and later, from the apps page, installed and missing ones shown differently); the ISO becomes slim when 5.0 arrives (apps downloaded when chosen; option b). |
| 2026-10-14 | Step 5.0 split into 5.0.0 (web apps: Netflix, YouTube, Spotify) and 5.0.1 (gaming programs: Steam, Epic, GOG, RetroArch). Brave ships inside the ISO as package files and is installed only when the user picks a web app; the user never sees Brave; installed and removed from the home screen's Apps grid; Discord waits for the chat modules; free web browsing in Wave 2; live system: the 12 GB rule as Steam. |
