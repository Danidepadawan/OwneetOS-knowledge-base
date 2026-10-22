---
type: decision
description: "UEFI only, silent boot, hidden menu, Plymouth wordmark splash, copytoram=n."
area: architecture
status: active
decided: 2026-10-05
updated: 2026-10-15
legacy: "PROJECT_RULES.md §13 (2026-10-04 – 2026-10-06)"
tags: [decision, architecture, boot]
---
# Boot experience

- **UEFI only**, booted by systemd-boot (no legacy BIOS); no SSH server, cloud-init or VM guest
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
- The interface takes over from the splash seamlessly ([[quick-menu-and-startup]]: the start-up
  animation starts from the splash's own picture).

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
