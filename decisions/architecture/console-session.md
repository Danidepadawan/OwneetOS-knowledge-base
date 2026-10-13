---
type: decision
area: architecture
status: active
decided: 2026-10-05
updated: 2026-10-07
legacy: "PROJECT_RULES.md §13 (2026-10-05, 2026-10-07)"
tags: [decision, architecture, session]
---
# Console session

- A fixed Linux user **`owneet`** with getty autologin on tty1; `owneet` is **not an
  administrator**. People's profiles will live in the console UI, not in Linux accounts.
- **gamescope** when a hardware Vulkan device exists, otherwise **cage** (reduced session, no
  overlay); gamescope failing twice falls back to cage. The session restarts the UI if it stops.
- **gamescope runs with `--steam`**: owneetd tags each window with an app id and chooses what is
  on screen (as Steam does on SteamOS).
- **Each game or app runs in its own systemd user service**, so closing it stops all of its
  processes. One game at a time; apps (e.g. the browser) may run next to it.
- `owneet-session` waits until the console is on screen instead of counting failed starts (a
  report on another tty must not trigger a false fallback).

GPU-specific compositor settings: [[graphics-drivers]]. Technical design:
[[owneetd-api-apps]], [[step-1.3-console-session]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-05 | Console session: fixed Linux user `owneet` with getty autologin on tty1; gamescope when a hardware Vulkan device exists, otherwise cage; gamescope failing twice falls back to cage (step 1.3). |
| 2026-10-07 | gamescope runs with `--steam`: owneetd tags each window with an app id and chooses what is on screen (as Steam does on SteamOS); each game or app runs in its own systemd user service, so closing it stops all of its processes. |
