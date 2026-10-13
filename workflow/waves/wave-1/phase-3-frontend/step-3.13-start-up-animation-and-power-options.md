---
type: step
phase: "[[phase-3-frontend]]"
step: "3.13"
status: done
legacy: "ROADMAP.md 3.13"
tags: [step, phase-3]
---
# 3.13 Start-up animation and power options *(owner's proposals, 2026-10-11; approved 2026-10-11)*

Up: [[phase-3-frontend]] · Status: **done**

- **Deliverables:** (A) an animated start-up: the OwneetOS logo moves with the start-up sound
  when the interface first appears; (B) power options from any of the three pages: hold B, a
  progress ring on the button shows how long to hold, then a window with Sleep, Restart, Shut
  down and Cancel (Cancel selected). Its own interactive demo first; the new binding goes into
  [[controller-input-map]] once approved.
- **Demo (2026-10-11, approved the same day):** `design/demos/3.13-startup-power.html`. (A) the
  interface starts from the boot splash's own picture (the wordmark centred, as Plymouth shows
  it): the letters of "Owneet" ripple, "OS" pops with a coral glow, then the wordmark flies to its
  place in the top bar while the home screen rises under it (about 2.4 s, with the start-up sound;
  once per boot; "Reduce motion": a plain fade). (B) a **quick menu**, a side panel from the right
  as on SteamOS, opened by **B where there is nothing to go back to** (Home, Library, the list of
  Settings sections; the owner chose B over View, which stays reserved for screenshots):
  "Power options" (Sleep, Restart, Shut down, Cancel selected; with a game running it says that
  Restart and Shut down close it) and "Controls and features" (a read-only guide to every button,
  scrolled like Credits and licences). B goes back one level.
- **Outcome (2026-10-11):** `Intro.qml` takes over the boot splash at the same size and place
  (Plymouth's 420-pixel wordmark, its top at 46 % of the free height), starts with the start-up
  sound (or on its own after a few seconds when sounds are off or the output is not ready) and
  lands on the top bar's wordmark. `QuickMenu.qml` (B on Home, Library and the list of Settings
  sections, prompt "B Menu"), the Power options window (Cancel selected; Sleep, Restart and Shut
  down go to owneetd's `/v1/power`) and `ControlsSheet.qml` (Controls and features). Checked with
  `tools/preview-steps/quick-menu.txt` and in the test VM booting the ISO (frames of the start-up
  from the splash to the home screen). owneet-frontend 0.14.0. To check on real hardware: the
  animation with the sound, the quick menu and power options.
- **Hardware test (2026-10-11, NiPoGi):** start-up animation and its sound, the first click, the
  quick menu and power options work. Found in the log: the NiPoGi has two Bluetooth adapters
  (built-in and a USB dongle) whose numbers swapped after Sleep, so owneetd moved to the other one
  and the controller had to pair again; owneetd now keeps the adapter with the paired devices
  (then the lowest address), owneetd 0.10.4. The "controller turned off" notification failed (a
  name clash in the theme), fixed in owneet-frontend 0.14.1 with the home screen's "Steam and
  local games" (", together" removed). Still to check: the note about a running game in the Power
  options window (the owner did not see it; it shows in the preview), network and controller
  notifications.
- **Phase 3 closed (2026-10-11):** steps 3.11–3.13 approved by the owner. Carried over to the next
  USB-stick test: the running-game note in Power options, the network and controller
  notifications, the controller staying paired after Sleep (owneetd 0.10.4).
