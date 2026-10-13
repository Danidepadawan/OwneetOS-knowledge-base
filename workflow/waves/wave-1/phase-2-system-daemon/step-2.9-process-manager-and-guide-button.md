---
type: step
description: "Launch / track / close games and apps, return to home on Guide, force-close a frozen game, focus handling inside gamescope."
phase: "[[phase-2-system-daemon]]"
step: "2.9"
status: done
legacy: "ROADMAP.md 2.9"
tags: [step, phase-2]
---
# 2.9 Process manager and Guide button

Up: [[phase-2-system-daemon]] · Status: **done**

- **Deliverables:** launch / track / close games and apps, return to home on Guide, force-close a
  frozen game, focus handling inside gamescope.
- **Done when:** a test app is launched, Guide brings back the home screen, and the app can be closed.
- **Decisions (owner, 2026-10-07):** Guide toggles home ↔ game in gamescope, the game keeps
  running; in cage, holding Guide 2 s closes the game, a short press does nothing.
- **Outcome:** `internal/apps`: each app in its own transient systemd user service (closing stops
  all its processes; SIGKILL after 10 s; force-close at once; found again after an owneetd
  restart); one game at a time. gamescope now runs with `--steam`: owneetd tags windows with app
  ids and chooses what is on screen (`jezek/xgb`, BSD-3-Clause, vendored). `owneet-session-app`
  publishes the session's display and the home screen's process. API `/v1/apps` (launch, list
  with focus, focus, close, kill); events `app.started`, `app.exited`, `focus.changed`,
  `guide.released`. Found while testing: gamescope ignores focus requests without `--steam`, and
  in that mode shows only tagged windows; gamescope cannot use the VM's screen with software
  Vulkan (test hook `owneet.debug.gamescope_backend=headless` added, VM README corrected).
- **Test VM** (virtual gamepad through `/dev/uinput`, `mpv` test pattern as the app): gamescope
  (headless): home on screen at boot; launched game comes to the front; Guide → home, Guide → game;
  owneetd restarted with the game open → still on screen, Guide still toggles; second game refused;
  missing program reported; close (SIGTERM), an app ignoring SIGTERM killed after 11 s, force-close
  at once. cage: short press does nothing, holding 2.5 s closes the game. Open: the same on a real
  screen (owner).
- **Real hardware (2026-10-08, owner's desktop, RTX 4060):** the placeholder shows "console session:
  gamescope", but flickering black rectangles appear (already before this step; not on the AMD
  NiPoGi). Test ISO with one variant per boot entry: drawing with the CPU or without `--steam`
  → rectangles; drawing through Vulkan or gamescope `--force-composition` → none. Cause: direct
  scanout of the app's buffer with the NVIDIA driver. Fix: `owneet-session` forces composition
  when the NVIDIA driver is loaded; AMD and Intel keep direct scanout. Test hooks
  `owneet.debug.placeholder_vo`, `owneet.debug.gamescope_composite`, `owneet.debug.gamescope_steam`.
  **Verified by the owner on the desktop:** no rectangles, gamescope session. (The second monitor
  still shows a frozen splash frame: known issue, step 3.9.)
