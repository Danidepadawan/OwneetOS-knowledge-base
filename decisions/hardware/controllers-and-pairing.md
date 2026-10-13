---
type: decision
area: hardware
status: active
decided: 2026-10-03
updated: 2026-10-09
legacy: "PROJECT_RULES.md §7"
tags: [decision, hardware, controllers]
---
# Controllers and pairing

- Wired and 2.4 GHz dongle controllers must work instantly (dongle: [[xbox-wireless-dongle]]).
- **First Bluetooth pairing must need zero input**: when no controller is connected, the system
  scans and **auto-pairs and trusts any device that identifies as a gamepad**.
  - owneetd turns auto-pair on whenever no controller is connected (any connection) and off as soon
    as one is. Its pairing agent accepts **only gamepads, only while auto-pair is on** (keyboards,
    phones, headsets are never paired without the user).
  - A second controller is paired from Settings → Controllers → "Pair a new controller"
    (auto-pair for a while, also with a controller connected).
- Large, animated, per-brand pairing instructions on screen (e.g. "Hold PS + Share"). The pairing
  drawings mark the real buttons; no drawing for "other controllers".
- Connected Bluetooth controllers can be **turned off** (disconnected, they stay known) or
  **forgotten**.
- Button prompts follow the connected controller: Xbox, PlayStation and a **Nintendo-style** set
  (chosen automatically for Switch controllers).
- Keyboard / mouse remain an optional fallback.

Technical design: [[owneetd-api-bluetooth]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-03 | Project scope, architecture and Wave 1 agreed ([[vision]]–11). |
| 2026-10-06 | xone: driver in the image, Microsoft firmware downloaded on the user's PC at first dongle use with consent; first setup needs a Bluetooth or cable controller ([[controllers-and-pairing]]). |
| 2026-10-07 | Bluetooth: owneetd auto-pairs gamepads whenever no controller is connected; its pairing agent accepts only gamepads, only while auto-pair is on. Verified on real hardware (step 2.5). |
| 2026-10-08 | Step 3.3 approved. Button prompts also have a Nintendo-style set (chosen automatically for Switch controllers). Small hardware checks are batched with the next larger test instead of a new USB stick each. |
| 2026-10-09 | Demo 3.9 review: pairing drawings mark the real buttons (no drawing for "other controllers"); connected Bluetooth controllers can be turned off or forgotten; Display gets a brightness setting (where the screen allows it); the keyboard layout is chosen separately from the language; the right stick scrolls the page and windows ([[controller-input-map]]). |
