---
type: step
description: "The site's fonts as WOFF2 instead of TTF, about a third of the size (optional, confirmed by the owner). Before the merge."
phase: "[[phase-7-updates-and-first-release]]"
step: "7.8g"
status: in-progress
tags: [step, phase-7, website]
---
# 7.8g Website lighter fonts *(added 2026-10-23)*

Up: [[phase-7-updates-and-first-release]] · Status: **in-progress** · Part of the website: [[step-7.8-website]]

- **Deliverables:** the console's font instances converted to **WOFF2** (in the builder VM with
  fontTools, as `tools/branding/make-fonts`), the TTF files replaced, the OFL licences kept next
  to them. Optional, confirmed by the owner (2026-10-23).
- **Done when:** the site loads the WOFF2 files and looks the same.
- **After 7.8b–7.8g:** the owner approves [[step-7.8-website]] and merges `feature/step7_website`
  into `main` (the pull request), with "Build" required by `main`'s ruleset.
- **Way (owner, 2026-10-24):** the official WOFF2 files of the fonts' own projects, checked by hash
  (no tool installed on the host); legal under the OFL.
- **Progress (2026-10-24, website commit d65cc51):** Lexend Regular and Medium are the official
  WOFF2 of `googlefonts/lexend` (version 1.008, commit 7894f02, SHA-256 in the site's
  `CREDITS.md`): 75 KB instead of 157 KB; same licence text. **Open:** Bricolage Grotesque. The
  console's instance (wght 800, wdth 80, opsz 32, made by `tools/branding/make-fonts`) has no
  official WOFF2: the project publishes width 100 or 75 only. Waiting for the owner's choice.
