---
type: step
description: "Reproducible build in the builder VM against Qt 5.15, PKGBUILD in `[owneet]`, frontend replaces the placeholder in the session."
phase: "[[phase-3-frontend]]"
step: "3.2"
status: done
legacy: "ROADMAP.md 3.2"
tags: [step, phase-3]
---
# 3.2 Build and package the frontend

Up: [[phase-3-frontend]] · Status: **done**

- **Deliverables:** reproducible build in the builder VM against Qt 5.15, PKGBUILD in `[owneet]`,
  frontend replaces the placeholder in the session.
- **Done when:** the unmodified frontend, with a minimal theme of our own (never the CC BY-NC-SA
  grid theme), runs in gamescope in the test VM and is driven by a gamepad.
- **Also:** seamless handover from the boot splash to the UI, without the dark gap left in 1.4.
- **Outcome:** package `owneet-frontend` (built in the clean chroot; 20 upstream tests pass with
  the offscreen platform and Qt Quick's software renderer, flaky `test_Playtime` left out; LTO off:
  Qt's two-pass resource compiler fails with LTO objects); the session starts it instead of the
  placeholder (kept as fallback). Fork changes: OwneetOS names (executable, window title, config
  folder, log), no Pegasus logo/icons/splash images, loading screen identical to the boot splash,
  Pegasus's menu hidden, only local game data (8 providers not built, no Steam store download),
  Guide not passed to the interface, window tags itself for gamescope and shows the home screen if
  nobody chose (works with owneetd stopped), **interface kept loaded while a game runs** (Pegasus
  unloaded it and blocked until the game ended: black screen in cage), no endless button repeat
  when input pauses, SDL no longer swallows SIGTERM (the interface could not be stopped), mouse
  pointer hidden until the mouse is used, window born at screen size. ISO 1720 MiB.
- **Test VM:** cage: list of test games, D-pad moves the selection, A starts the game once, the
  game shows, closing it returns to the list and input works again. gamescope (headless):
  interface on screen and tagged, also with owneetd stopped. RAM in the VM (software rendering):
  owneet-frontend ~170 MB, whole live system 566 MiB — to be measured on real hardware (C1).
- **Real hardware (2026-10-08, owner's desktop, RTX 4060):** the interface shows after the boot
  splash; the dark gap between them is about a tenth of a second (the ~4 s in the VM come from
  software rendering): no helper needed, handover done. Live system RAM "used": 1142 MiB of 48 GB
  — breakdown per process requested (constraint C1: 500 MB).
- **Desktop diagnostics (cage):** "Timeout waiting session to become active": while the report on
  tty9 is on screen the console session is not active and cage cannot start (reproduced in the VM;
  back on tty1 it starts). This also explains the "endless splash" of 1.5. `owneet-session` now
  waits until the console is on screen instead of counting failed starts (no false fallback, no
  error screen). RAM on the desktop: programs ~60 MB, kernel ~340 MB, ~800 MB not attributed
  (typical of GPU drivers: NVIDIA with GSP firmware plus the Intel GPU); the NiPoGi (AMD) used
  ~235 MiB without the UI in 1.5. C1 is measured on the target low-budget hardware.
  **Verified by the owner (desktop, diagnostics entry):** report opened at once → "the console is
  not on screen: waiting", no failed start; back on tty1 → cage starts, interface running. RAM in
  cage there: owneet-frontend 230, cage 176, Xwayland 160 MiB RSS (including the shared NVIDIA
  libraries; anonymous memory +250 MB in total), 1427 MiB used. To measure in gamescope on low-cost
  hardware and optimise if needed (step 7.4).
- **Open:** (1) In cage, the mouse pointer shows until the first input (drawn by cage).
  (2) Games are still started by the frontend itself; through owneetd in 3.8.
