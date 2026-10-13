---
type: decision
area: ux
status: active
decided: 2026-10-09
updated: 2026-10-10
legacy: "PROJECT_RULES.md §13 (2026-10-09, 2026-10-10); ROADMAP 3.9"
tags: [decision, ux, settings]
---
# Settings screens

- Demo 3.9 review (2026-10-09): pairing drawings mark the real buttons ([[controllers-and-pairing]]);
  connected Bluetooth controllers can be turned off or forgotten; Display gets a brightness
  setting, **shown only on screens that allow it** ([[screens-and-display]]); the keyboard layout
  is chosen separately from the language ([[languages]]); the right stick scrolls the page and
  windows ([[controller-input-map]]).
- **Sound:** "Mute" comes first and, while it is on, hides output, volume and interface sounds.
- **Wi-Fi password window:** a "Show password" switch.
- **Confirmations** (Sleep / Restart / Shut down, forget, disconnect) have Cancel selected first
  ([[ui-patterns]]).

Step: [[step-3.9-settings]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-09 | Demo 3.9 review: pairing drawings mark the real buttons (no drawing for "other controllers"); connected Bluetooth controllers can be turned off or forgotten; Display gets a brightness setting (where the screen allows it); the keyboard layout is chosen separately from the language; the right stick scrolls the page and windows ([[controller-input-map]]). |
| 2026-10-09 | Held LB / RB / LT / RT repeat after 0.72 s, then every 0.36 s (directions: 0.36 s, then 0.14 s) ([[controller-input-map]]). Demo 3.9 approved; the brightness setting is shown only on screens that allow it. |
| 2026-10-10 | Settings → Sound: "Mute" comes first and, while it is on, hides output, volume and interface sounds. The Wi-Fi password window has a "Show password" switch (owner's NiPoGi test). |
| 2026-10-10 | Step 3.9 (Settings) approved after the owner's tests on the NiPoGi and the desktop (two graphics cards). Picture dimming for screens without a brightness control stays a proposal for Wave 2 (not confirmed). Next: demo 3.10 (on-screen keyboard). |
