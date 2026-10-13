---
type: decision
description: "First-boot flow: controller, language, network, time zone; cable or Bluetooth controller notice."
area: ux
status: active
decided: 2026-10-06
updated: 2026-10-11
legacy: "PROJECT_RULES.md §7, §13 (2026-10-06, 2026-10-11); ROADMAP 6.1"
tags: [decision, ux, first-boot]
---
# First-boot setup

- Flow: controller (auto-pairing, as in the mockup) → language → network → ready. The keyboard
  layout follows the chosen language and can be changed in Settings.
- Notice: the first setup needs a **Bluetooth or cable controller**; consent dialog for the Xbox
  dongle firmware ([[xbox-wireless-dongle]]).
- **Time zone:** chosen in the first-boot flow (suggested from the language, e.g. Italian →
  Europe/Rome), changeable in Settings; until then the system runs on UTC. Details agreed with the
  owner at the start of [[step-6.1-first-boot-flow]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-06 | xone: driver in the image, Microsoft firmware downloaded on the user's PC at first dongle use with consent; first setup needs a Bluetooth or cable controller ([[controllers-and-pairing]]). |
| 2026-10-11 | Steps 3.11 (notifications), 3.12 (interface sounds) and 3.13 (start-up animation, quick menu) approved: **phase 3 closed**. Checks left for the next USB-stick test are listed in [[step-3.13-start-up-animation-and-power-options]]. The time zone is chosen in the first-boot flow (roadmap 6.1; until then the system runs on UTC). Next: phase 4 (games). |
