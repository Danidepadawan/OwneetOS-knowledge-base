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
- **Demo approved (owner, 2026-10-19):** `design/demos/4.6-installers.html` (built on demo 4.5):
  covers "Not installed" (dimmed, download mark), "Installing · N%" (no percentage for NSIS /
  MSI), "Waiting" (one install at a time), "Cannot be installed yet" (GOG Galaxy's online
  installer, unknown kinds, with the reason); "Install {game}?" with the size, [Read] (the licence,
  scrolled with the right stick, or where to find it) [Install] [Cancel]; "Not enough space";
  Windows installers wait for Windows games to be ready; the home screen's notice and a banner
  when ready; Options: Stop installing (confirmed), Uninstall (confirmed; the installer stays);
  installed games stay when the disk is unplugged; unplugging it stops an install, with a banner.
- **Option B changed (owner, 2026-10-19):** `innoextract` needs `boost-libs` (51 MB, not in the
  system; "about 1 MB" was a mistake, told to the owner): not added. Windows installers show
  "Installing…" with a moving bar, like NSIS / MSI in the demo (Shadow Harbor updated in the
  demo); only GOG's `.sh` have a percentage. [Read] for a Windows installer shows a licence file
  of the game's folder, else where to find it.
- **Code (2026-10-19):** owneetd 0.15.0 (`daemon/internal/installs`, [[owneetd-api-installs]]:
  queue, GOG `.sh` extracted with Go's ZIP reader, Windows installers in a transient unit with
  `owneet-windows-run`, marks, stop, uninstall, clean-up after a restart); owneet-frontend 0.22.0
  (the provider lists installer-only folders, `DiskGames::installRequest`, the theme's states,
  questions, licence, notices, Options; [[frontend-disk-games]]). Verified: Go tests (a fake GOG
  `.sh`: script + ZIP; Windows installers with a fake runner: options, NSIS link, not ready,
  nothing written; stop, source gone, restart), `tools/lint`; the preview (both step files: every
  window of the demo, the percentage, the moving bar, stop, uninstall). Sizes under 1 GB in MB.
  Not verifiable without real installers: GOG's `.sh` layout and licence file, a real Inno Setup
  `setup_*.exe` under Proton (FrankenPC test).
- **Test together with step 4.7 (owner, 2026-10-19):** the owner asked to move on to 4.7 before
  testing 4.6 ([[collaboration]]'s exception): 4.6 stays in progress; the FrankenPC test with
  real installers (GOG `.sh`, a GOG offline `setup_*.exe`, the Galaxy installer) comes with 4.7's.
