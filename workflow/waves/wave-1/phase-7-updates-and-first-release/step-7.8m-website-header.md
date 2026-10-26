---
type: step
description: "The website's header: the languages in a drop-down menu and a light / dark switch remembered in the browser; demo first."
phase: "[[phase-7-updates-and-first-release]]"
step: "7.8m"
status: in-progress
tags: [step, phase-7, website]
---
# 7.8m Website header: languages and theme *(added 2026-10-26)*

Up: [[phase-7-updates-and-first-release]] · Status: **in-progress** · Part of the website: [[step-7.8-website]]

- **Deliverables (owner, 2026-10-26):** the five language buttons of the header become a
  drop-down menu (a globe and the current language; the languages in their own names, the current
  one ticked); a sun / moon button switches between the light (Daylight) and dark (Dusk) palettes,
  starting from the device's theme, the choice kept in the visitor's browser only (localStorage,
  told on the Privacy page). Demo first ([[demo-before-code]]).
- **Branch:** `feature/step7_8k_languages` in the site, the code repository (the demo) and this
  vault, with [[step-7.8k-website-more-languages]].
- **Demo (2026-10-26):** `design/demos/7.8m-website-header.html`, approved by the owner after one
  change (the colours fade when the theme is switched).
- **Built (2026-10-26, website commit c747100):** the drop-down in the header (names from each
  language's `@meta`), `ThemeService` (`data-theme` on `<html>`, `localStorage` key
  `owneet-theme`), a script in `index.html` that applies the choice before the page shows, both
  icons drawn and CSS showing the right one (prerendered pages never differ), the fade
  (`html.theming`, none with reduced motion), the Privacy sentence in the five languages; five
  Lucide icons from `lucide-static` 1.52.0 checked by SHA-512. On a phone the languages' button
  keeps its globe; the languages no longer go into the Menu. 12 tests pass. Waiting for the
  owner's check; published with [[step-7.8k-website-more-languages]] after the reviews.
