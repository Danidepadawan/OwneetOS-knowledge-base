---
type: decision
description: "First-boot flow: controller, language, network, time zone; cable or Bluetooth controller notice."
area: ux
status: active
decided: 2026-10-06
updated: 2026-10-29
legacy: "PROJECT_RULES.md §7, §13 (2026-10-06, 2026-10-11); ROADMAP 6.1"
tags: [decision, ux, first-boot]
---
# First-boot setup

- Flow: controller (auto-pairing, as in the mockup) → language → network → ready. The keyboard
  layout follows the chosen language and can be changed in Settings.
- Notice: the first setup needs a **Bluetooth or cable controller**; consent dialog for the Xbox
  dongle firmware ([[xbox-wireless-dongle]]).
- **Time zone:** chosen in the first-boot flow, changeable in Settings; until then the system runs
  on UTC. Suggested from the language (Italian → Europe/Rome); a language spoken in several time
  zones (English, Spanish...) shows a list of cities to pick with the controller. Once online the
  clock is synchronised, but the time zone stays the chosen one: no geolocation (owner,
  2026-10-26).
- **The console's name** is not asked again at the first start: it is chosen in the installer and
  changed in Settings ([[installer-and-firmware]], owner, 2026-10-26).
- **When it is shown (owner, 2026-10-29):** once on an installed console, until "Ready"; turned
  off half way, it starts again from the beginning at the next start, keeping what was already
  chosen (the language, a Wi-Fi network already joined). **From the USB stick** (live) nothing is
  kept at power-off, so it is shown at **every start** from the stick.
- **The language picker lists the five languages of Wave 1 from the start** (owner, 2026-10-29),
  even before their messages are complete or checked ([[languages]]): a missing message shows in
  English, and the reviews may come later, an occasion to ask the community to help improve
  OwneetOS.

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-06 | xone: driver in the image, Microsoft firmware downloaded on the user's PC at first dongle use with consent; first setup needs a Bluetooth or cable controller ([[controllers-and-pairing]]). |
| 2026-10-11 | Steps 3.11 (notifications), 3.12 (interface sounds) and 3.13 (start-up animation, quick menu) approved: **phase 3 closed**. Checks left for the next USB-stick test are listed in [[step-3.13-start-up-animation-and-power-options]]. The time zone is chosen in the first-boot flow (roadmap 6.1; until then the system runs on UTC). Next: phase 4 (games). |
| 2026-10-26 | Time zone: suggested from the language, a list of cities when the language has several zones, no geolocation; the console's name not asked at the first start (installer, then Settings). |
| 2026-10-29 | The first start: once on an installed console until "Ready" (turned off half way it starts again, keeping what was chosen); at every start from the USB stick; the picker lists the five languages from the start. |
| 2026-10-29 | Microsoft's terms as a QR code; the time zone and a manual date and time in Settings → Language (demo first); the picker alphabetical after English. |
