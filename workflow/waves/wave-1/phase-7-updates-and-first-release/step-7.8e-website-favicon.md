---
type: step
description: "The site's own icon in the browser's tab (Angular's was removed: it is Angular's logo). Before the merge."
phase: "[[phase-7-updates-and-first-release]]"
step: "7.8e"
status: in-progress
tags: [step, phase-7, website]
---
# 7.8e Website favicon *(added 2026-10-23)*

Up: [[phase-7-updates-and-first-release]] · Status: **in-progress** · Part of the website: [[step-7.8-website]]

- **Deliverables:** a favicon of OwneetOS (SVG, plus the sizes browsers ask for) from the current
  wordmark's "O" or the logo of the moment; replaced with the final logo
  ([[step-7.8i-website-final-logo]]). Never a third-party logo ([[legal]]).
- **Done when:** the tab shows it, in both light and dark browser themes.
- **Progress (2026-10-24):** demo `design/demos/7.8e-website-favicon.html`: the gamepad "O" as
  (A) the whole mark, (B) the simple mark (the gamepad's outline only) or (C) the mark on a tile;
  in the site's accent following the device (Daylight blue, Dusk orange) or always one colour;
  shown on light and dark tab bars, pixel by pixel at 16 and 32 px, and as the phone's home-screen
  icon (always on a tile, 180 px). The owner chose A, following the device (2026-10-24).
- **Code (2026-10-24, website commit 5bd734b):** `scripts/make-favicon.mjs` (no dependencies: it
  reads the mark from `wordmark.data.ts` and the colours from the tokens of `src/styles.scss`,
  and draws the PNGs itself) writes `public/favicon.svg` (Dusk, Daylight when the device is
  light), `public/favicon.ico` (16 and 32 px) and `public/apple-touch-icon.png` (180 px, the mark
  on a square Dusk tile: the phone rounds the corners); linked relatively in `src/index.html`.
  Run it again with the final logo ([[step-7.8i-website-final-logo]]). **Open:** checked in the
  tab of the published site, light and dark, after the merge.
