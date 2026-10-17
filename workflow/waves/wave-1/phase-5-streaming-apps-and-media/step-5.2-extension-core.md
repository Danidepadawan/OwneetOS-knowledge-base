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
  screen (a `CageWindow` state left over after the close, fixed). (5) done, owneet-frontend
  0.16.15, verified in the test VM: `/v1/webapps/look` gives `{"accent": "#ff8a5b", "language":
  "en"}`, the ring has the palette's accent and follows a palette change (at the next page load).
  **The frontend part is done.**
- **Part 6, plan agreed (owner, 2026-10-17):** the keyboard as a gamescope external overlay
  ([[extension-design]]). Done in owneetd 0.12.3 and owneet-frontend 0.16.16, checked in the test
  VM (2026-10-17): cage unchanged; headless gamescope keeps YouTube in front and focused
  (`GAMESCOPE_FOCUSED_WINDOW` = Brave), the window "OwneetOS keyboard" is mapped with
  `GAMESCOPE_EXTERNAL_OVERLAY = 1` and a 32-bit visual, outside `GAMESCOPE_FOCUSABLE_WINDOWS`,
  and the virtual controller types through it (`webapp.text`, Done → `next`). **To check on real
  hardware** (next hardware test): the picture, i.e. the page visible through the band (on NVIDIA
  the transparent part may come out black: a known gamescope report); the keyboard's sounds; the
  overlay also carries the home screen's `STEAM_GAME` (owneetd tags the interface's windows;
  gamescope forces an external overlay's app id to 0); the extension hides its ring while the
  keyboard is open, while the demo keeps it around the field. Next: part 7 (packaging, terms of
  service, known limits, outcome).
- **Part 6 on real hardware (FrankenPC, live USB, 2026-10-17): not working yet.** A and B open and
  close the keyboard (its keys arrive), but it is **not drawn over YouTube**; after Guide the home
  screen comes in front and the keyboard shows there, on a dark background, and works. It behaves
  like an ordinary window of the home screen, not an external overlay. gamescope 3.16.31 (the
  snapshot's; the source read for the plan), no Qt Wayland plugin (the interface is on X11),
  `--force-composition` on NVIDIA. Cause unknown: being investigated with owneetd 0.12.4,
  owneet-base 0.0.42, owneet-frontend 0.16.17 (a new ISO): the test log writes to the OwneetOS
  stick itself when there is no OWNEETLOG stick ([[known-solutions/INDEX]] once understood), the X
  probe ships with owneetd, and a **temporary experiment** alternates the keyboard's openings
  between the external overlay and `STEAM_OVERLAY` without input focus (the path of Steam's own
  keyboard; it takes the input only with `STEAM_INPUT_FOCUS`, so the earlier "it takes the input"
  was imprecise).
- **What the logs showed** (FrankenPC, 2026-10-17, logs on the OwneetOS stick): neither opening
  appeared. The probe shows the keyboard window (`0x400030`) mapped with **no overlay property at
  all** and listed in `GAMESCOPE_FOCUSABLE_WINDOWS` as a home-screen window, while the interface
  had logged setting it on that same window: the property never reached the X server's window
  (one Xwayland server, `:0`). Most likely the request, sent on a connection of the interface's
  own, overtook Qt's request that creates the window and failed unseen. Fix in owneet-frontend
  0.16.18: wait until the server knows the window, check every request, read the property back
  and log it, and set it again after the window is shown. To test on FrankenPC with the
  experiment still in place.
- **Second FrankenPC test** (owneet-frontend 0.16.18, 2026-10-17): the property is set on every
  opening (read back, no X errors) and **the keyboard appeared over YouTube** at the first
  opening (external overlay). But it **stayed on screen after closing**: the interface closed and
  reopened it three times (each reopening needs a close; the gamepad was stopped and started
  again), while its picture remained. Likely gamescope kept the last frame once the window was
  unmapped, over a page that did not change. Fix in 0.16.19: on closing, the window first turns
  fully transparent (`_NET_WM_WINDOW_OPACITY` 0: gamescope repaints on an overlay's opacity change
  and does not draw it at 0), and is unmapped 150 ms later. The experiment is removed: the
  external overlay is the kind that appeared.
- **Part 6 verified on FrankenPC** (owneet-frontend 0.16.20, 2026-10-17): the keyboard appears over
  YouTube, typing reaches the page, B and Done close it and it disappears; a second opening works.
  [[gamescope-overlay-window-not-drawn-or-left-on-screen]]. The owner saw no visible difference
  between B and Done (by design: Done moves the ring to the next target, B leaves it on the field,
  the sounds differ); **kept as designed** (owner, 2026-10-17); "Done = search on search fields"
  was offered and not taken for now. Open for part 7: the per-key log lines of 0.16.20 (keep or
  drop), the keyboard's sounds and the ring around the field (see the checklist above).
