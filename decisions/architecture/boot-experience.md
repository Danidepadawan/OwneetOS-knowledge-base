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
  session, and the logo fades in from black in the palette's
  colours ([[quick-menu-and-startup]]).
- **Since 2026-11-05 (owner):** the splash says "Starting" and "Shutting down" under the spinner, in the console's language
  (English while none is chosen), the only text on it in normal boots. Its grey is `#A0A0A0`. The cream seen on FrankenPC stayed: closed by the owner, who reopens it if needed
  after trying another screen ([[step-7.6-final-logo-and-brand]]).

Profile choices and their reasons are documented in the code repository (`iso/README.md`,
"Choices"). Steps: [[step-1.4-boot-experience]].

- **Reported (owner, FrankenPC, 2026-11-09), open:** from the home screen to "Shutting down" takes too long, and the screen goes off
  and disconnects before the splash shows. The console first closes the apps (Steam took 6 s: 11:09:19 to 11:09:25), the testers'
  logs are copied when OWNEETLOG is plugged in, then the interface ends and gives the screen up and the splash takes it again (the
  monitor re-syncs). Ways to look at, with the owner: the console showing "Shutting down" itself at once (as the splash looks), and
  why the monitor re-syncs (a mode change between gamescope and the splash). **Owner: understand why first (2026-11-09).**
  Lead: gamescope picks 1440x900 at 75 Hz on FrankenPC's monitor (ACI VK192), the kernel's console and the splash the monitor's
  preferred mode (likely 60 Hz): going back to it makes the monitor re-sync. owneet-base 0.0.58 (code commit 74718ef) adds to the
  testers' report the monitor's modes with the EDID's refresh, and the end of the previous start's journal (the power-off after the
  stick's logs stop). Waits for a test: two power-offs with OWNEETLOG.
  **Found (FrankenPC, 2026-11-09, 11:25):** the monitor's preferred mode is 1440x900 at 74.57 Hz, the same as gamescope's: not
  the refresh. The wait: 6.2 s from the choice (11:25:51.57) to the power-off request (57.75), owneetd closing Steam cleanly (Steam
  must close while the console session runs, or it checks all its files at the next start), with the home screen still and nothing
  saying it is shutting down; then the splash starts (57.83), the console session ends (58.18) and the system is down to unmounting
  in about 1.5 s. The re-sync is the screen going from gamescope to the splash (on NVIDIA a full mode set). Next: what the owner
  chooses (the console saying "Shutting down" at once covers the 6 s; the hand-over itself is likely to stay).
  **Owner (2026-11-09): test it, demo first.** Demo `design/demos/7.6b-shutting-down.html` (on the approved 6.7 settings demo):
  Shut down or Restart confirmed, the console shows at once the splash's own picture (`owneetos-splash.svg`, black, the spinner at
  92% and `splash.shutting_down` under it) while it closes Steam and the games; then a moment of black (the hand-over) and the splash
  itself; Restart ends on "Starting". **Approved by the owner (2026-11-09).** In the console the screen lasts as long as the
  apps take to close (no fixed time: the demo's 6 s only stand for FrankenPC's Steam, [[waiting-for-events]]).

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
