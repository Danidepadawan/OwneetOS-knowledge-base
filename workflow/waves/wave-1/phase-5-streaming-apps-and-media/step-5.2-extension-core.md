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
- **Demo approved (owner, 2026-10-15):** `design/demos/5.2-web-app-controls.html`. No sounds inside the page; Done moves the selection to the next target; show / hide password only in the fallback session's line. Seeking (±10 s) is not part of 5.2: it comes with each site's player in 5.3 and 5.4.
- **Progress (2026-10-16):** vault, demo, extension (navigation tested by the owner in the VM:
  "solid") and bridge + owneetd endpoints done. Verified in the test VM with owneetd 0.12.1:
  A on a text field starts `owneet-bridge` and opens the keyboard request; text sent through
  `/v1/webapps/text` reaches the field; Done gives the controller back; B on the first page sends
  `webapp.ask_close`. The bridge was first never started by Brave:
  [[brave-native-messaging-host-not-found]]. Next: the frontend part (keyboard in web mode with
  the confirmation of [[extension-design]], "Close {name}?", the look in the open request; in the
  cage session the console must come in front of Brave), then the keyboard over Brave in
  gamescope (real hardware), then packaging and the outcome. Open: [[brave-extension-worker-cached]]
  (fix in owneet-base 0.0.39: the installed worker is named after a hash of its content and the
  manifest gets the package's version, [[extension-design]]; to verify on a real update).
- **Frontend part, plan agreed (owner, 2026-10-16):** (1) owneetd: keyboard confirmation and cage
  focus; (2) the interface's window in cage; (3) the web keyboard; (4) "Close {name}?"; (5) the
  look in the open request. Until part 6, gamescope uses the fallback design too (the console in
  front with the line and the keyboard). **Part 6 stays** (owner, 2026-10-17): in gamescope the
  keyboard is drawn over the page, as in the approved demo; the fallback design stays for cage.
- **Progress (2026-10-17):** (1) done, owneetd 0.12.2: the 3-second timeout seen in the test VM.
  (2) done, owneet-frontend 0.16.12 (`CageWindow.qml`), verified in the test VM: the home screen
  stays while YouTube starts; A on the search field brings the console in front of Brave and,
  without a confirmation, Brave comes back after 3 s; B on the first page brings the console in
  front; holding Guide closes YouTube with the console on screen. (3) done, owneet-frontend
  0.16.13 (`WebKeyboard.qml`) and owneet-base 0.0.41, verified in the test VM (cage, YouTube's
  search field): the screen stays open (confirmed), typing, delete and the cursor reach the page,
  Done moves the ring on, B closes without going back in the page, A on the Done key clicks
  nothing. (4) done, owneet-frontend 0.16.14, verified in the test VM: B on YouTube's first page
  asks "Close YouTube?" with Cancel selected; Cancel and B bring YouTube back (B does not also go
  back in the page); Close closes it and the home screen stays; opening it again shows no black
  screen (a `CageWindow` state left over after the close, fixed). Next: (5) the look in the open
  request.
