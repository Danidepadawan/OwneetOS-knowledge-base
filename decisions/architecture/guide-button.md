---
type: decision
description: "Guide is owned by owneetd: home toggle in gamescope, hold 2 s in cage, hold 1 s over Steam."
area: architecture
status: active
decided: 2026-10-07
updated: 2026-10-12
legacy: "PROJECT_RULES.md §9.1 (Guide row), §13 (2026-10-07, 2026-10-12)"
tags: [decision, architecture, input]
---
# Guide button

- **Owned by the system daemon** `owneetd`: home / quick menu from anywhere, including in games.
  Apps and themes must never bind it. Prompt label: "Home".
- Guide **always brings back the home screen with the selection where it was**, from anything the
  console opens (Steam included).
- **gamescope session:** Guide toggles between the home screen and the running game, which keeps
  running behind the home screen; Resume brings it back.
- **Reduced (cage) session:** the home screen cannot be shown over a game, so **holding Guide for
  2 seconds closes the game**; a short press does nothing.
- **Exception, Steam** (2026-10-12, option A): while Steam or a Steam game is on screen, a **short
  press is Steam's** (its menu; its overlay in games) and **holding it for 1 second** comes back to
  the console (Steam and the game keep running). "Exit Steam" in Steam's menu also comes back.

Part of the [[controller-input-map]]. Implementation: [[owneetd-api-apps]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-07 | Guide button (step 2.9): in the gamescope session it toggles between the home screen and the running game, which keeps running behind the home screen; in the reduced (cage) session, where the home screen cannot be shown over a game, holding Guide for 2 seconds closes the game and a short press does nothing. |
| 2026-10-12 | After the owner's first Steam test (Guide fought over by owneetd and Steam): **while Steam or a Steam game is on screen, a short Guide press is Steam's; holding Guide for 1 second comes back to the console** (option A; [[controller-input-map]]). "Exit Steam" in Steam's menu also comes back. Steam's own screens that matter (login, a game's launch progress) are shown automatically ([[game-library]]). |
