---
type: step
description: "The site's fonts as WOFF2 instead of TTF, about a third of the size (optional, confirmed by the owner). Before the merge."
phase: "[[phase-7-updates-and-first-release]]"
step: "7.8g"
status: todo
tags: [step, phase-7, website]
---
# 7.8g Website lighter fonts *(added 2026-10-23)*

Up: [[phase-7-updates-and-first-release]] · Status: **todo** · Part of the website: [[step-7.8-website]]

- **Deliverables:** the console's font instances converted to **WOFF2** (in the builder VM with
  fontTools, as `tools/branding/make-fonts`), the TTF files replaced, the OFL licences kept next
  to them. Optional, confirmed by the owner (2026-10-23).
- **Done when:** the site loads the WOFF2 files and looks the same.
- **After 7.8b–7.8g:** the owner approves [[step-7.8-website]] and merges `feature/step7_website`
  into `main` (the pull request), with "Build" required by `main`'s ruleset.
