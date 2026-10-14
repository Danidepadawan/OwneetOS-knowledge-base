---
type: step
description: "Netflix, YouTube and Spotify installed and removed from the home screen's Apps grid; Brave, behind them and never shown, is installed from package files inside the ISO."
phase: "[[phase-5-streaming-apps-and-media]]"
step: "5.0.0"
status: done
legacy: "ROADMAP.md 5.0"
tags: [step, phase-5]
---
# 5.0.0 Optional web apps *(owner, 2026-10-14)*

Up: [[phase-5-streaming-apps-and-media]] · Status: **done**

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
- **Demo first** ([[demo-before-code]]): `design/demos/5.0.0-optional-apps.html`. **Approved by
  the owner (2026-10-14)**, with the install window's line "Usage requirements: Internet needed";
  the size shown is about 500 MB for the first web app and "Less than 1 MB" for the next ones; A
  on an installed web app says "later" until [[step-5.1-brave-in-the-os]].
- **Done when:** in the test VM with no network, an installed system installs Netflix (Brave
  installed from the ISO's files), YouTube at once, removing both removes Brave; the live system
  follows the 12 GB rule; the owner's test on the FrankenPC passes.
- **Outcome (2026-10-14):** `brave-bin` 1.97.57 (Brave's official build, unmodified, in
  `[owneet]`, credited); the ISO build bundles it with the dependencies the ISO lacks (none: the
  ISO already has them) in `/usr/share/owneet/bundled/` (ISO 1823 → 2015 MiB). owneet-base 0.0.32:
  catalogue `apps.json` (Netflix, YouTube, Spotify; engine Brave), root helper `owneet-apps`,
  units `owneet-apps-install@` / `owneet-apps-remove@.service`, polkit `50-owneet-apps.rules`.
  owneetd 0.11.14: `GET /v1/apps/catalog`, `POST /v1/apps/catalog/{id}/install|remove`, event
  `apps.catalog.changed`; the live-system RAM rule shared with Steam (package `live`).
  owneet-frontend 0.16.8: the home screen's Apps grid as in the demo. **Checked:** Go tests
  (catalogue, dependency logic, refusals, API); `tools/lint`; the interface in
  `tools/frontend-preview` (`web-apps.txt`); in the test VM, live system with 4 GB: install
  refused with the message "Install OwneetOS to add apps"; installed system (tester installer on
  the VM's virtual disk), **network off**: Netflix installed Brave from the bundle (470 MiB
  installed, `brave --version` works), YouTube at once, removing YouTube kept Brave, removing
  Netflix removed it; the same through the console with the keyboard (spinner, then installed);
  the helper refuses ids outside the catalogue's engines, and polkit refuses its units outside the
  console's active session. **Not checked here:** the live system with 12 GB or more (the host
  cannot run such a VM). **Open points:** the bundled package files stay on the disk after
  installation (about 200 MB; removable once Brave is updated online, 7.1); the bundle is
  unsigned in development builds and is signed before users get it (7.2); Brave's own icons ship
  inside its package (review at 7.5).
