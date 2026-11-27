---
type: step
description: "The gaming programs as optional apps: Steam (with its 32-bit drivers), later Epic and GOG (Wave 2), installed and removed like the web apps of 5.0.0."
phase: "[[phase-5-streaming-apps-and-media]]"
step: "5.0.1"
status: in-progress
legacy: "ROADMAP.md 5.0"
tags: [step, phase-5]
---
# 5.0.1 Optional gaming apps *(owner, 2026-10-14)*

Up: [[phase-5-streaming-apps-and-media]] · Status: **in-progress**

The second half of step 5.0 (split on 2026-10-14; the first half is
[[step-5.0.0-optional-web-apps]]). Decision: [[optional-apps]].

- **Deliverables:** the real programs join the catalogue of 5.0.0: Steam with its 32-bit drivers,
  later Epic / GOG ([[wave-2]]); one emulation program, carried by the ISO and installed when chosen (owner, 2026-11-27,
  [[users-own-emulators]]). Removing Steam asks whether to keep
  the downloaded games. Where the programs come from (inside the ISO as in 5.0.0, or downloaded
  when chosen) is decided at this step; until then Steam stays in the ISO
  ([[distribution-and-updates]]). In the live system, the RAM rule of [[steam-integration]].
- **Demo first** ([[demo-before-code]]).
- **Started for the emulation program alone (owner, 2026-11-27):** before the next test, which covers it with step
  [[step-4.9-the-users-own-emulators|4.9]], still in progress (the owner's request to move on before 4.9 is approved). Steam's
  part comes later: it changes what the ISO installs and its 32-bit drivers, the riskiest part.
- **Built (2026-11-27): owneetd 0.29.0, owneet-base 0.0.91, owneet-frontend 0.46.0.** A catalogue app may be a program (kind
  `program`): shown, installed and removed as a web app, opening a program of the system; no Google's terms, only its space in
  the install window, and its removal keeps the games and saves (a new text, five languages: to approve). The app "Emulation"
  (letter E), 350 MiB installed; its packages, the bundle's list for the ISO and the update stick, in `iso/bundled.txt` (about
  110 MiB more in the ISO). `owneet-emulation-run` starts it with the console's settings (`emulation.cfg`): full screen, the
  controllers through SDL (its own profile binds no Guide), its input commands on, no button combinations. Guide over it as
  over Steam ([[guide-button]]): a short press makes owneetd write its "open the menu" command into a pipe it reads as its
  input; held, the console. Go tests for both; the 25 interface tests pass. Tried in the builder VM, without a screen: it
  starts from the console's script and keeps the console's settings (Guide unbound); there it stops at once with or without the
  command pipe, so the menu on Guide is still to be seen on the test PC. `CREDITS.md` credits it.
- **To do:** the test with 4.9; Steam's part.
