---
type: decision
description: "What Wave 1 contains, what later waves and nice-to-haves are."
area: product
status: active
decided: 2026-10-03
updated: 2026-10-19
legacy: "PROJECT_RULES.md §10"
tags: [decision, product, scope]
---
# Wave 1 scope, later waves, nice-to-have

## Wave 1 (agreed scope)

1. Bootable and installable ISO.
2. Controller pairing (first-boot flow).
3. Home with unified library (Steam installed games + local DRM-free games).
   DRM-free games on a disk play **whatever their form**: ready to run or with an installer,
   for Linux or for Windows (Proton via umu-launcher, never shown to the user: at most a
   "preparing the game" screen while it loads). Installers run by themselves, in the
   background. Moving games and media between disks (roadmap 6.6).
4. Brave with Netflix, YouTube, Spotify.
5. Basic settings: Wi-Fi, Bluetooth, audio, language, theme.

Added on 2026-10-13: **optional apps** — the user installs only the apps they want (step 5.0,
[[optional-apps]]).

The step-by-step plan is in [[wave-1]]; the user's view of it in [[wave-1-features]].

## Later waves

- Overlay / quick menu over games, chat modules (Discord first), a stable live boot (OwneetOS
  fully usable from the USB stick, 2026-10-19), dual boot, Epic/GOG stores
  (their Windows games through the same Proton as Wave 1), emulation, user profiles,
  screenshots/recording, play-time stats, parental controls, quick suspend/resume, Qt 6 port of
  the frontend. Detailed in [[wave-2]].

## Nice-to-have

- Screen reader / TTS for menus (espeak-ng or Piper, offline) — evaluate if feasible early.
- Crash reporting **only with explicit opt-in consent**. No telemetry otherwise.
- Emulation (RetroArch).
- Support for other OSes is **out of scope** for now.

See [[backlog]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-03 | Project scope, architecture and Wave 1 agreed ([[vision]]–11). |
| 2026-10-11 | **Wave 1 scope grows** ([[disks]] and 10): DRM-free games on a disk play whatever their form (ready to run or installer, Linux or Windows through umu-launcher + GE-Proton, hidden from the user); installers run by themselves in the background; moving games and media between disks (new step 6.6). Games folder: `Games` or its translated name, one folder per game with any sub-folders, searched recursively. "Add games" also offers "From a USB stick or disk". |
| 2026-10-13 | **Optional apps** (new step 5.0): the user installs only the apps they want (at installation and later, from the apps page, installed and missing ones shown differently); the ISO becomes slim when 5.0 arrives (apps downloaded when chosen; option b). |
| 2026-10-19 | **New Wave 2 step 9a, Stable live boot**, before step 10 (dual boot): OwneetOS fully usable from the USB stick (the user chooses the disks where games are saved, the game library is cached, faster boot, RAM saved wherever possible). |
