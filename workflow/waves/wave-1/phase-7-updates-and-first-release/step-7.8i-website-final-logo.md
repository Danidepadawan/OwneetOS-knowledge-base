---
type: step
description: "The website takes the final logo of step 7.6 in place of the provisional wordmark (one component). After the merge."
phase: "[[phase-7-updates-and-first-release]]"
step: "7.8i"
status: done
tags: [step, phase-7, website]
---
# 7.8i Website final logo *(added 2026-10-23)*

Up: [[phase-7-updates-and-first-release]] · Status: **done** · Part of the website: [[step-7.8-website]]

- **Deliverables:** the final logo and wordmark of [[step-7.6-final-logo-and-brand]] on the site
  (the `wordmark` component and its data, the favicon, the sharing picture).
- **When:** after the website's merge and the final logo (owner, 2026-10-23). The demo of the
  pages already shows the gamepad "O" draft and its start-up animation (owner, 2026-10-24,
  [[step-7.8b-website-pages]]); [[step-7.6-final-logo-and-brand]] stays open (research and
  Danidepadawan's review).
- **Built (owner, 2026-11-04, website commit a37b33e on `feature/step7_8k_languages`, seen locally):** the
  `wordmark` component has the final logo of [[step-7.6-final-logo-and-brand]], the same outlines as on the
  console: `layout` "left" (header, footer, console picture) or "above" (the start-up animation, in the
  demo's proportions, and the sharing picture, made again with `scripts/make-share-picture.mjs`). The
  favicon was already this symbol, unchanged. `ng test` (15 tests), `npm run build` (31 pages, no warning),
  home, phone, animation and sharing picture looked at.
- **Approved by the owner (2026-11-05)**, on the published site.
