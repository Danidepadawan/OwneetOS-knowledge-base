---
type: step
description: "Manifest V3 extension: Gamepad API loop, spatial navigation, B = back, exit to home, OSK for web forms."
phase: "[[phase-5-streaming-apps-and-media]]"
step: "5.2"
status: in-progress
legacy: "ROADMAP.md 5.2"
tags: [step, phase-5]
---
# 5.2 Extension core

Up: [[phase-5-streaming-apps-and-media]] · Status: **in-progress**

- **Before shipping:** check the extension's behaviour and any user-agent change against the terms
  of service of each streaming service ([[legal-compliance]]).

- **Deliverables:** Manifest V3 extension: Gamepad API loop, spatial navigation, B = back, exit to home, OSK for web forms.
- **Agreed (owner, 2026-10-15):** bindings in [[controller-input-map]] ("Inside a web app"); design
  in [[extension-design]]: own spatial navigation (focusable elements, every `tabindex`, interactive
  ARIA roles; off-screen targets scrolled into view), B at the first page asks to close the web app
  through the console's dialog, text fields open the console's keyboard (over Brave in gamescope,
  full screen in the fallback session), a native-messaging bridge `owneet-bridge` to owneetd.
- **Order:** vault → demo `design/demos/5.2-web-app-controls.html` (approval before UI code) →
  extension (gamepad loop, spatial navigation, ring, B) → bridge and owneetd endpoints → frontend
  (close dialog, keyboard in web mode, full screen first) → keyboard layered in gamescope (checked
  on real hardware only: headless gamescope in the test VM shows no picture) → packaging.
- **Known limits of 5.2:** native `<select>` popups and cross-origin iframes (e.g. captchas) are
  not driven by the controller.
