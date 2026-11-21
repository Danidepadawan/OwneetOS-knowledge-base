---
type: decision
description: "Users install only the apps they want (step 5.0); the ISO becomes slim and apps are downloaded when chosen."
area: product
status: active
decided: 2026-10-13
updated: 2026-10-23
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
- **Removing a web app deletes its data on the console** (its Brave profile, login included): the
  remove confirmation says the user will have to sign in again (2026-10-14).
- **A running web app is treated like a game** (Wave 1): it takes the home screen's hero (Resume,
  Close), stays open until the user closes it, and only one game or web app runs at a time.
  Background playback (Spotify, Tidal…) is [[wave-2]] (2026-10-14; confirmed for step 5.5 on
  2026-10-23).
- **YouTube opens its TV interface** (`youtube.com/tv`, made for a remote's D-pad), with a TV
  user agent that owneetd takes from the catalogue (2026-10-18, [[step-5.3-youtube]]; terms:
  [[legal-compliance]]).
- **Discord** waits for the chat modules ([[wave-2]], [[online-and-chat]]).
- In the live system, apps follow the same RAM rule as Steam, at least 12 GB
  ([[steam-integration]]).

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-13 | **Optional apps** (new step 5.0): the user installs only the apps they want (at installation and later, from the apps page, installed and missing ones shown differently); the ISO becomes slim when 5.0 arrives (apps downloaded when chosen; option b). |
| 2026-10-14 | Step 5.0 split into 5.0.0 (web apps: Netflix, YouTube, Spotify) and 5.0.1 (gaming programs: Steam, Epic, GOG, RetroArch). Brave ships inside the ISO as package files and is installed only when the user picks a web app; the user never sees Brave; installed and removed from the home screen's Apps grid; Discord waits for the chat modules; free web browsing in Wave 2; live system: the 12 GB rule as Steam. |
| 2026-10-14 | Step 5.1: removing a web app deletes its Brave profile (the confirmation says the user signs in again); a running web app is treated like a game (hero with Resume / Close, one game or web app at a time); background playback in Wave 2. |
| 2026-10-18 | Step 5.3: YouTube opens its TV interface with a TV user agent taken by owneetd from the catalogue (brand-neutral first). |
| 2026-10-23 | Background playback stays in Wave 2, confirmed when step 5.5 (Spotify) started: that step's deliverable "playback continues in the background" is dropped. |
