---
type: wave
status: in-progress
legacy: "ROADMAP.md"
tags: [wave]
---
# Wave 1 — the plan, step by step

Scope: [[wave-1-scope]] · What the user gets: [[wave-1-features]] · How steps are run:
[[how-we-work]]. If a step note and a decision disagree, the decision wins and the step note gets
fixed ([[kb-rules]]).

Status: `done` · `in-progress` · `todo` · `needs-decision` (a decision is needed before it can
start).

## [[phase-0-foundations|Phase 0 — Foundations]]

9 of 9 steps done.

- `done` [[step-0.1-project-rules|0.1 Project rules]]
- `done` [[step-0.2-wave-1-ui-mockups|0.2 Wave 1 UI mockups]]
- `done` [[step-0.3-roadmap-and-global-controller-input-map|0.3 Roadmap and global controller input map]]
- `done` [[step-0.4-repository-skeleton|0.4 Repository skeleton]]
- `done` [[step-0.5-github-repository|0.5 GitHub repository — **Owner input**]]
- `done` [[step-0.6-host-virtualization-tools|0.6 Host virtualization tools — **Owner input**]]
- `done` [[step-0.7-arch-builder-vm|0.7 Arch builder VM *(multi-prompt)*]]
- `done` [[step-0.8-test-vm-harness|0.8 Test VM harness]]
- `done` [[step-0.9-ci-skeleton|0.9 CI skeleton]]

## [[phase-1-minimal-bootable-os|Phase 1 — Minimal bootable OS (no UI yet)]]

6 of 7 steps done.

- `done` [[step-1.1-archiso-profile|1.1 archiso profile]]
- `done` [[step-1.2-own-package-repository-owneet|1.2 Own package repository `[owneet]`]]
- `done` [[step-1.3-console-session|1.3 Console session]]
- `done` [[step-1.4-boot-experience|1.4 Boot experience]]
- `done` [[step-1.5-hardware-support-set|1.5 Hardware support set]]
- `done` [[step-1.6-iso-build-in-ci|1.6 ISO build in CI]]
- `in-progress` [[step-1.7-xbox-wireless-dongle-xone|1.7 Xbox wireless dongle (xone) (software done; real dongle test open)]]

## [[phase-2-system-daemon|Phase 2 — System daemon (`owneetd`)]]

9 of 9 steps done.

- `done` [[step-2.1-language-decision-and-api-design|2.1 Language decision and API design — **Owner input**]]
- `done` [[step-2.2-daemon-skeleton-and-packaging|2.2 Daemon skeleton and packaging]]
- `done` [[step-2.3-controller-input|2.3 Controller input]]
- `done` [[step-2.4-virtual-input-uinput|2.4 Virtual input (uinput)]]
- `done` [[step-2.5-bluetooth|2.5 Bluetooth]]
- `done` [[step-2.6-network|2.6 Network]]
- `done` [[step-2.7-audio|2.7 Audio]]
- `done` [[step-2.8-power|2.8 Power]]
- `done` [[step-2.9-process-manager-and-guide-button|2.9 Process manager and Guide button]]

## [[phase-3-frontend|Phase 3 — Frontend (`owneet-frontend`, a Pegasus Frontend fork)]]

13 of 13 steps done.

- `done` [[step-3.1-pegasus-study-and-fork|3.1 Pegasus study and fork]]
- `done` [[step-3.2-build-and-package-the-frontend|3.2 Build and package the frontend]]
- `done` [[step-3.3-theme-foundations|3.3 Theme foundations]]
- `done` [[step-3.4-internationalisation|3.4 Internationalisation]]
- `done` [[step-3.5-navigation-and-input-map|3.5 Navigation and input map]]
- `done` [[step-3.6-home-screen|3.6 Home screen]]
- `done` [[step-3.7-library-screen|3.7 Library screen]]
- `done` [[step-3.8-frontend-daemon-bridge|3.8 Frontend ↔ daemon bridge]]
- `done` [[step-3.9-settings|3.9 Settings *(multi-prompt; demo approved 2026-10-09; approved 2026-10-10)*]]
- `done` [[step-3.10-on-screen-keyboard|3.10 On-screen keyboard]]
- `done` [[step-3.11-notifications|3.11 Notifications]]
- `done` [[step-3.12-interface-sounds|3.12 Interface sounds]]
- `done` [[step-3.13-start-up-animation-and-power-options|3.13 Start-up animation and power options *(owner's proposals, 2026-10-11; approved 2026-10-11)*]]

## [[phase-4-games|Phase 4 — Games]]

1 of 7 steps done.

- `done` [[step-4.1-steam-library|4.1 Steam library *(investigation first; approved 2026-10-11)*]]
- `todo` [[step-4.2-steam-integration|4.2 Steam integration]]
- `todo` [[step-4.3-local-drm-free-games|4.3 Local DRM-free games]]
- `todo` [[step-4.4-artwork|4.4 Artwork]]
- `todo` [[step-4.5-windows-games-proton|4.5 Windows games (Proton) *(added 2026-10-11)*]]
- `todo` [[step-4.6-installers|4.6 Installers *(added 2026-10-11)*]]
- `todo` [[step-4.7-controller-pointer|4.7 Controller pointer *(added 2026-10-11)*]]

## [[phase-5-streaming-apps-and-media|Phase 5 — Streaming apps and media]]

0 of 7 steps done.

- `todo` [[step-5.1-brave-in-the-os|5.1 Brave in the OS]]
- `todo` [[step-5.2-extension-core|5.2 Extension core]]
- `todo` [[step-5.3-youtube|5.3 YouTube]]
- `todo` [[step-5.4-netflix|5.4 Netflix]]
- `todo` [[step-5.5-spotify|5.5 Spotify]]
- `todo` [[step-5.6-local-videos-and-music|5.6 Local videos and music]]
- `todo` [[step-5.7-apps-page|5.7 Apps page]]

## [[phase-6-first-boot-installer-disks|Phase 6 — First boot, installer, disks]]

0 of 6 steps done.

- `todo` [[step-6.1-first-boot-flow|6.1 First-boot flow]]
- `todo` [[step-6.2-live-vs-installed-mode|6.2 Live vs installed mode]]
- `needs-decision` [[step-6.3-installer-backend|6.3 Installer backend *(multi-prompt)*]]
- `todo` [[step-6.4-installer-ui|6.4 Installer UI]]
- `todo` [[step-6.5-automatic-disk-mounting|6.5 Automatic disk mounting]]
- `todo` [[step-6.6-moving-games-and-media-between-disks|6.6 Moving games and media between disks *(added and approved for Wave 1, 2026-10-11)*]]

## [[phase-7-updates-and-first-release|Phase 7 — Updates and first release (Wave 1 complete)]]

0 of 7 steps done.

- `todo` [[step-7.1-updates|7.1 Updates]]
- `todo` [[step-7.2-release-pipeline|7.2 Release pipeline]]
- `todo` [[step-7.3-user-guide|7.3 User guide]]
- `todo` [[step-7.4-hardware-testing-and-v0.1.0|7.4 Hardware testing and v0.1.0]]
- `todo` [[step-7.5-legal-review-before-the-public-launch|7.5 Legal review before the public launch]]
- `todo` [[step-7.6-final-logo-and-brand|7.6 Final logo and brand]]
- `todo` [[step-7.7-final-interface-sounds|7.7 Final interface sounds *(Owner delivery)*]]

## Next

[[wave-2]] · [[backlog]]
