---
type: step
description: "Managed policies (forced extension, no first-run, Widevine on, locked settings), dedicated profile, kiosk launch through the daemon; web apps open from the home screen."
phase: "[[phase-5-streaming-apps-and-media]]"
step: "5.1"
status: in-progress
legacy: "ROADMAP.md 5.1"
tags: [step, phase-5]
---
# 5.1 Brave in the OS

Up: [[phase-5-streaming-apps-and-media]] · Status: **in-progress**

- **Deliverables:** managed policies (forced extension, no first-run, Widevine on, locked
  settings), dedicated profile, kiosk launch through the daemon; A on an installed web app opens
  it. Building `brave-bin` into `[owneet]` moved to [[step-5.0.0-optional-web-apps]] (owner,
  2026-10-14).
- **Agreed with the owner (2026-10-14):** one Brave profile per web app (each runs in its own
  unit and closes on its own); Widevine turned on silently; a web app is treated like a game: it
  stays open until the user closes it (background playback: [[wave-2]]): it takes the home
  screen's hero (Resume, Close), and only one game or web app runs at a time. Removing a web app
  deletes its profile; the remove confirmation says the user will have to sign in again.
- **Demo first** ([[demo-before-code]]): `design/demos/5.1-web-app-running.html`, the hero with a
  running web app and the new remove text. **Approved by the owner (2026-10-15).**
- **Implementation (2026-10-15), waiting for the owner's test:** owneet-base 0.0.33: Brave's
  managed policies `/etc/brave/policies/managed/owneet.json` (no telemetry: P3A, stats ping, web
  discovery, metrics off; no Rewards, Wallet, VPN, AI chat, News, Talk, Tor, sign-in, sync; no
  downloads, printing, translate; `brave://`, `chrome://`, `file://` and the extension store
  blocked; site notifications and location blocked) and the extension stub
  `/usr/share/owneet/extension/` (empty Manifest V3, filled in [[step-5.2-extension-core]]).
  owneetd 0.11.15: `POST /v1/apps/catalog/{id}/open`, kind `webapp` (one game or web app at a
  time), a profile per web app with Widevine on, removal closes the app and deletes its profile
  ([[owneetd-api-apps]]). owneet-frontend 0.16.9: the hero and tiles of the approved demo, the
  new remove text; the "running" green became the token `Theme.running`. **Not checked yet:**
  `tools/lint` (no builder VM on this machine), the ISO build, and everything in the VM (the owner
  tests). **To verify in the test:** the extension loads (its name "OwneetOS" appears in
  `~/.local/share/owneet/webapps/ID/Default/Preferences`), Widevine is on (Netflix plays: step
  5.4 checks it fully), no Brave welcome or sign-in page.
- **Done when:** a test page opens fullscreen and Guide returns to home.
