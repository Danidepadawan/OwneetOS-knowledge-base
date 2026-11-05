---
type: decision
description: "UEFI only, silent boot, hidden menu, Plymouth wordmark splash, copytoram=n."
area: architecture
status: active
decided: 2026-10-05
updated: 2026-11-05
legacy: "PROJECT_RULES.md §13 (2026-10-04 – 2026-10-06)"
tags: [decision, architecture, boot]
---
# Boot experience

- **UEFI only**, booted by systemd-boot (no legacy BIOS; kept for the installed system's rollback,
  with its boot counting: [[distribution-and-updates]], 2026-10-25); no SSH server, cloud-init or VM guest
  tools in the ISO.
- **Silent boot**: quiet kernel and systemd, **hidden systemd-boot menu** (hold / tap a key to show
  it), Plymouth splash `owneet` with the generated wordmark, no text on screen in normal boots.
- The splash shows the wordmark "Owneet" + "OS" (as in the mockups page header) instead of
  "owneet." ([[design-direction]]). **Since 2026-10-15 it is neutral: white wordmark and spinner on
  black**, the same for every palette, as everything before the start-up animation (the
  interface's loading screen, the session's placeholder); the animation brings the chosen
  palette's colours ("OS" takes the accent as it pops, the black fades into the pages). A splash
  in each palette's colours was turned down: it needs the boot image rebuilt at every palette
  change (owner: keep the OS light).
- The live ISO boots with **`copytoram=n`**: no copy of the image to RAM, faster boot from USB
  (the stick must stay plugged in).
- **Since 2026-11-05 (owner):** a black screen stands between the splash and the
  session ([[black-screen-between-boot-splash-and-session]]), and the logo fades in from black in the palette's
  colours ([[quick-menu-and-startup]]).
- **Since 2026-11-05 (owner):** the splash says "Starting" and "Shutting down" under the spinner, in the console's language
  (English while none is chosen), the only text on it in normal boots. Its grey is `#A0A0A0`. The cream seen on FrankenPC stayed: closed by the owner, who reopens it if needed
  after trying another screen ([[step-7.6-final-logo-and-brand]]).

Profile choices and their reasons are documented in the code repository (`iso/README.md`,
"Choices"). Steps: [[step-1.4-boot-experience]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-04 | ISO boots UEFI only (no legacy BIOS); no SSH server, cloud-init or VM guest tools in the ISO (step 1.1). |
| 2026-10-05 | Boot: silent kernel/systemd, hidden systemd-boot menu (hold a key to show it), Plymouth splash `owneet` with the generated wordmark (step 1.4). |
| 2026-10-05 | Boot splash approved by the owner with the wordmark "Owneet" + coral "OS" (as in the mockups page header) instead of "owneet." ([[design-direction]]). |
| 2026-10-15 | Everything before the start-up animation is neutral (white on black), the same for every palette; the animation brings the palette's colours. A splash per palette (boot image rebuilt at every change) turned down. |
| 2026-10-06 | Step 1.5 verified on real hardware (NiPoGi E3B AMD, owner's desktop RTX 4060). Live ISO boots with `copytoram=n` (no copy of the image to RAM: faster boot from USB). |
| 2026-10-25 | systemd-boot stays on installed systems: rollback from the console and automatic fallback through its boot counting (step 6.3, option C). |
| 2026-11-04 | The splash shows the final logo ([[step-7.6-final-logo-and-brand]]): the symbol above the word, in white and grey on black, in the middle, the spinner lower. |
| 2026-11-05 | The start-up logo fades in from black in the palette's colours; the logo stays 3 s more at power-off. |
| 2026-11-05 | The splash says "Starting" and "Shutting down", from the message files, in the console's language; a restart shows both. Its grey goes from `#B0B0B0` to `#A0A0A0`, as a try. |
| 2026-11-05 | The cream on the splash stays closed unless the owner reopens it (FrankenPC's screen, another one to be tried); the grey stays `#A0A0A0`. |
