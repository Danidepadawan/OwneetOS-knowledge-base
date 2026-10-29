---
type: wave
description: "What comes after Wave 1, to be detailed into steps later."
status: todo
legacy: "ROADMAP.md Wave 2"
tags: [wave]
---
# Wave 2 — to be detailed into steps when Wave 1 is done

Scope agreed so far: [[wave-1-scope]] (later waves).

- **8. Overlay and quick menu:** gamescope overlay layer, quick menu over games, volume, battery, screenshots on View/Create.
- **9. Chat modules:** module interface, Discord web in the background, notifications in the overlay, mute and push-to-talk.
- **Web browser app (owner, 2026-10-14):** free web browsing with the controller (Brave, already
  behind the web apps of [[step-5.0.0-optional-web-apps]]), under a generic name and icon. **The
  extension's generic navigation for any web page is reworked entirely then** (owner,
  2026-10-20); until then it stays as 5.2 left it, and each supported web app has its own
  ([[extension-design]]).
- **Web apps in the background (owner, 2026-10-14):** music web apps (Spotify, Tidal…) keep
  playing while the user does something else; in Wave 1 a web app is closed by the user like a
  game ([[step-5.1-brave-in-the-os]]).
- **10a. Stable live boot (owner, 2026-10-19):** OwneetOS fully usable when booted from the USB
  stick, without installing it: the user chooses the disks where games are saved; the game
  library is cached (in the owner's words: "tiles shadowing, download from library etc."); the
  boot is faster; RAM is saved wherever possible. Details agreed when the step is planned; it
  revisits what the live system does today: Steam and the web apps only with 12 GB of RAM
  ([[steam-integration]], [[optional-apps]]), a writable space in RAM of up to 75 %
  (`cow_spacesize=75%`, [[step-4.2-steam-integration]]), no copy of the image to RAM
  (`copytoram=n`, [[boot-experience]]), the slow boot from a USB stick
  ([[step-1.5-hardware-support-set]]). The user's disks: [[disks]], guard [[user-data]].
- **10b. Dual boot (optional, not required):** "Install alongside Windows", BitLocker detection and guidance, RTC handling, default OS, "Restart into Windows".
- **11. More stores:** Epic (legendary), GOG (gogdl); their Windows games use Wave 1's Proton (4.5).
- **12. Console features:** user profiles, parental controls, play-time statistics, quick suspend and resume.
- **13. Custom accent colour** with automatic contrast checking.
- **14. Other screens (optional choice):** Settings → Display "Other screens: show the OwneetOS
  logo / turn off" (decided 2026-10-10: Wave 1 turns them off).
- **15. Picture dimming (proposal, not confirmed, owner 2026-10-10):** for screens without a real
  brightness control (no backlight, no DDC/CI), an optional "Dim the picture" setting done by
  gamescope's colour pipeline: darker pixels, same backlight (no energy saved, lower contrast);
  it would apply to games too. Needs a demo and the owner's approval.
- **16. Anything made console-ready by itself (owner, 2026-10-16):** the console takes any
  package, installer or game it does not know yet and makes it "OwneetOS-friendly" on its own,
  with no technical step for the user (Wave 1 covers only the known forms: games ready to run,
  Windows games through Proton, the known installers of [[step-4.6-installers]]). Games made for
  a mouse and keyboard stay as their developers made them ([[games-on-disk]]). To be detailed
  into steps after the first release.
- **17. The player's own compatibility layers (owner, 2026-10-18):** the console cannot ship
  every compatibility layer (new ones keep appearing), so a player can import their own from a
  USB stick: a Proton-shaped tool (a folder or archive with `proton`, `compatibilitytool.vdf` and
  `toolmanifest.vdf`, e.g. GE-Proton, Proton-CachyOS, Luxtorpeda) copied to the console's disk in
  Steam's `compatibilitytools.d` (Steam already registers the console's GE-Proton from there:
  FrankenPC, 2026-10-18), then chosen per game ("Automatic" always there to go back) for Steam
  games (Steam's per-game tool, as in [[step-4.5-windows-games-proton]]) and for Windows games on
  disks (`owneet-windows-run`). Managed in Settings (list, remove). Feasibility seen on
  2026-10-18: about the size of step 4.3, in two parts (importing and Steam games first, games
  on disks next). To decide first: where technical names may be shown (the guard
  [[product-invariants]]: the player's own tool needs its name; e.g. an "Advanced" area), the
  warning at import (third-party code, only from trusted sources; [[supply-chain-security]],
  sandboxing in [[backlog]]), and tools whose runtime needs the internet the first time.
  Needs a demo. Related to item 16.
- **18. Installing on an external disk (owner, 2026-10-25):** the Wave 1 installer offers internal
  disks only (never the USB stick it starts from, never other USB disks); installing OwneetOS on an
  external disk (e.g. a USB SSD) comes here.
- **19. Changing the console's name (owner, 2026-10-25, only if needed):** Wave 1 makes the name
  editable ([[step-6.3-installer-backend]]); if that turns into a problem during development, the
  way to change it moves here.
