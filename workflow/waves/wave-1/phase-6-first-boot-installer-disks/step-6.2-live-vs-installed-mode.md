---
type: step
description: "Detection, 'Install OwneetOS' entry shown only in live mode."
phase: "[[phase-6-first-boot-installer-disks]]"
step: "6.2"
status: in-progress
legacy: "ROADMAP.md 6.2"
tags: [step, phase-6]
---
# 6.2 Live vs installed mode

Up: [[phase-6-first-boot-installer-disks]] · Status: **in-progress**

- **Deliverables:** detection, "Install OwneetOS" entry shown only in live mode.
- **Detection (2026-10-28):** `owneet-mode` (package `owneet-base`, `owneet-mode.service`, early at
  every start) writes `/run/owneet/mode`: `live` (started from the USB stick: `/run/archiso`),
  `tester` (installed by `owneet-tester-install`: `/etc/owneet/tester`) or `installed` (by
  `owneet-install`, or anything else). It is the one place owneetd and the interface read; the
  checks written before it (Steam's 12 GB in the live session, the updates' units) keep working
  and move to it with owneetd after Danidepadawan's merge. Done together with
  [[step-7.2-release-pipeline]] (owner, 2026-10-28).
- **Demo (2026-10-28), for approval:** `design/demos/6.2-live-home.html` (on demo 3.6) and
  `design/demos/6.2-live-settings.html` (on demo 7.1). From the stick, Home has a card next to the
  apps, "Install OwneetOS - From the USB stick: nothing is kept when it turns off.", always there
  (it cannot be dismissed), which opens the installer of [[step-6.4-installer-ui]]; Settings →
  System says "0.3.0, from the USB stick" and offers "Install OwneetOS on this PC" in place of the
  updates and going back, which need an installed system. Installed, neither is shown. The
  interface's code after the demo's approval and Danidepadawan's merge.
- **Second round (owner, 2026-10-28):** the card and the notice overlapped when Home had little
  room (the side column had a row too few), and the demo key M did nothing (M is the Menu
  button): fixed, the demo key is now I.
- **Third round (owner, 2026-10-28):** the notice under the card was still cut with little room,
  so the live entry is now a **strip above the hero** ("Install OwneetOS - From the USB stick:
  nothing is kept when it turns off."), which takes its room from the hero: the apps and the
  notices keep the approved layout, also with bigger text. The settings demo opens on System,
  where the difference is.
- **Demo approved by the owner (2026-10-28).** The detection is done; the interface's code (the
  strip on Home, the entry in Settings → System) after Danidepadawan's merge.
- **Code started (owner, 2026-10-29)** on `feature/phase6`, after 6.1. The "Install OwneetOS" entries
  open the installer of [[step-6.4-installer-ui]], which is not built yet: the owner chose to write
  6.2 now (owneetd tells the mode, the strip on Home, Settings → System as in the demos) and to
  connect "Install" in 6.4. 6.2 stays in progress and is tested and approved together with 6.4.

