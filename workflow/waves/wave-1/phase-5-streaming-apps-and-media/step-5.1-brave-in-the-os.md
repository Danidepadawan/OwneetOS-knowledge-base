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
- **Done when:** a test page opens fullscreen and Guide returns to home.
