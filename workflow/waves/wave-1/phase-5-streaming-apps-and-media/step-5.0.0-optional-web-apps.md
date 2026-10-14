---
type: step
description: "Netflix, YouTube and Spotify installed and removed from the home screen's Apps grid; Brave, behind them and never shown, is installed from package files inside the ISO."
phase: "[[phase-5-streaming-apps-and-media]]"
step: "5.0.0"
status: in-progress
legacy: "ROADMAP.md 5.0"
tags: [step, phase-5]
---
# 5.0.0 Optional web apps *(owner, 2026-10-14)*

Up: [[phase-5-streaming-apps-and-media]] · Status: **in-progress**

Step 5.0 (Optional apps, 2026-10-13) is split in two: this step (the web apps) and
[[step-5.0.1-optional-gaming-apps]] (Steam, Epic, GOG, RetroArch). Decision: [[optional-apps]].

- **Deliverables:**
  - A catalogue of the apps (`/usr/share/owneet/apps.json`, owned by root, the only allow-list):
    the web apps **Netflix, YouTube, Spotify** (name, generic icon, size) and the hidden engine
    behind them, Brave. Discord waits for the chat modules ([[wave-2]]).
  - **Brave in the ISO as package files** (`brave-bin`, built into `[owneet]` here instead of in
    [[step-5.1-brave-in-the-os]], and the dependencies the ISO lacks), kept as a small offline
    pacman repository in `/usr/share/owneet/bundled/`; it is installed only when the user picks
    a web app. No internet and no USB stick needed.
  - **The user never sees Brave:** no tile, no text naming it. The first web app installs it,
    removing the last one removes it.
  - **The home screen's Apps grid** shows the missing apps dimmed with a download mark: A
    installs (a confirmation with the size, then progress on the tile), Menu → options → Remove
    (with a confirmation). The apps page with every app stays in [[step-5.7-apps-page]]. A on an
    installed web app opens it from [[step-5.1-brave-in-the-os]] on.
  - A root helper (`owneet-apps`, started by owneetd through systemd units a polkit rule allows)
    installs and removes only the catalogue's packages; owneetd keeps which web apps the user
    chose.
  - **Live system:** the same rule as Steam (at least 12 GB of RAM; otherwise a message asks to
    install OwneetOS), [[steam-integration]].
  - The installer's "What do you want to use?" question stays with [[step-6.4-installer-ui]].
- **Demo first** ([[demo-before-code]]): `design/demos/5.0.0-optional-apps.html`.
- **Done when:** in the test VM with no network, an installed system installs Netflix (Brave
  installed from the ISO's files), YouTube at once, removing both removes Brave; the live system
  follows the 12 GB rule; the owner's test on the FrankenPC passes.
