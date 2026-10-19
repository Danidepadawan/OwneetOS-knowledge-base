---
type: step
description: "Installers found in a game's folder (GOG Linux `.sh`, Windows Inno Setup / NSIS / MSI, e.g. GOG's `setup_*.exe`) run silently in the…"
phase: "[[phase-4-games]]"
step: "4.6"
status: in-progress
legacy: "ROADMAP.md 4.6"
tags: [step, phase-4]
---
# 4.6 Installers *(added 2026-10-11)*

Up: [[phase-4-games]] · Status: **in-progress**

- **Deliverables:** installers found in a game's folder (GOG Linux `.sh`, Windows Inno Setup /
  NSIS / MSI, e.g. GOG's `setup_*.exe`) run silently in the background with their known options,
  into the console's games folder, with progress in the library; then the game appears.
- **Decided (owner, 2026-10-11):** a silent install accepts the game's licence for the user, so
  the console first shows "By installing you accept the game's licence" [Read] [Install].
- **Note:** installers of unknown kinds may only have windows made for a mouse: they need the
  controller pointer (4.7).
- **Started (owner, 2026-10-19).** Demo proposal to agree first.
- **Demo proposal agreed (owner, 2026-10-19, [[games-on-disk]]):** a folder with only an
  installer is a game "Not installed"; A asks "Install {game}?" with "By installing you accept the
  game's licence" [Read] [Install] [Cancel]; the install goes to the console's games folder (free
  space checked first), with the percentage on the cover and in the home screen's notices,
  cancelled from Options; a banner when ready; the installed copy replaces the entry; Uninstall in
  Options deletes the copy (the installer stays). GOG `.sh` extracted (option A, explained to the
  owner: same files as MojoSetup copies, no installer code, no shortcuts); Inno Setup / NSIS / MSI
  run silently under Proton (Proton must be ready, as for Windows games); `innoextract` (option B,
  credited) for Inno Setup's total; [Read] shows the licence's text when found (C1); online and
  unknown installers shown with "cannot be used yet" (D). Test material: the owner's GOG `.sh`
  (BASS, CAYNE, Stargunner) and a GOG offline `setup_*.exe`; NSIS / MSI only if a sample is found.
