---
type: step
description: "Illustrated guide: download, write the USB stick (balenaEtcher / Ventoy), disable Secure Boot (per-brand pointers), anti-cheat warning…"
phase: "[[phase-7-updates-and-first-release]]"
step: "7.3"
status: in-progress
legacy: "ROADMAP.md 7.3"
tags: [step, phase-7]
---
# 7.3 User guide

Up: [[phase-7-updates-and-first-release]] · Status: **in-progress**

- **Deliverables:** illustrated guide: download, write the USB stick (balenaEtcher / Ventoy),
  disable Secure Boot (per-brand pointers), anti-cheat warning for Windows games, first boot.
- **Started (owner, 2026-11-01)**, after [[step-7.1b-going-back-to-any-version]]. Owner's choices
  ([[website]]):
  - the guide is the website's guide page ([[step-7.8b-website-pages]]) grown into the whole
    guide, in the site's languages; the code repository links to it;
  - pictures: real screens of OwneetOS (from `tools/frontend-preview`) and simple drawings of our
    own for the steps on the PC; no screenshots of other programs (their logos, [[legal]]);
  - also: trying OwneetOS from the stick without installing ([[step-6.2-live-vs-installed-mode]]),
    what to do when the PC does not start from the stick, checking the download (checksum and
    signature), and the first steps with the console (Guide, updates, going back, USB disks);
  - website branch `feature/step7_8k_languages`: the guide comes in German, French and Spanish
    too, drafts reviewed with the rest of [[step-7.8k-website-more-languages]].
  Next: the demo of the page ([[demo-before-code]]), then the Angular page.
- **Demo (2026-11-01, code commit 7db0ec4 on `feature/phase7`):** `design/demos/7.3-user-guide.html`,
  on the approved site demo 7.8m, English and Italian: a list of the nine parts, then check the PC
  (`msinfo32` for UEFI or Legacy, the erase warning), download (checking the ISO, folded: the
  `.sha256` and `.sig` files, the primary key's fingerprint), write the stick (balenaEtcher;
  Ventoy, Windows and Linux only), start from the stick (a table of keys for Acer, ASUS, Dell, HP,
  Lenovo, MSI, Gigabyte, ASRock and Microsoft Surface, from the makers' and common published lists;
  Windows' Advanced startup; Secure Boot and Legacy / CSM; the anti-cheat warning), try it from
  the stick, install, first start, first steps, and five problems with their answers. Thirteen
  real screens (WebP, made with `tools/frontend-preview`, steps `user-guide-*.txt`), opening full
  size when clicked, and three drawings of our own (the ISO to the stick, a boot menu, a firmware
  page). Waiting for the owner's approval.
- **Demo, owner's corrections (2026-11-03, in progress):** no line under the title; "Check your PC"
  becomes **Requirements**, Minimum and Recommended side by side as on Steam's store pages, one
  aligned row per requirement (graphics: any card, with the "reduced mode" explained; storage: 32 GB
  plus the space the games need; the USB stick and the controller among them); "Does your PC start
  in UEFI mode?" as steps; the download as steps ("Download the file": the button at the top right,
  SourceForge, the name `owneetos-X.Y.Z-x86_64.iso`) and the optional checks split in two; no
  e-mail address; the public key `owneetos.asc` on the site. **Every correction goes to every
  language of the final page** (German, French and Spanish too, owner).
