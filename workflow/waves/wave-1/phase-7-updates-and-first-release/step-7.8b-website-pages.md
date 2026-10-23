---
type: step
description: "The website's other pages: installation guide, FAQ, credits and licences, privacy, contributing and translating; each with its demo approved first. Before the merge."
phase: "[[phase-7-updates-and-first-release]]"
step: "7.8b"
status: done
tags: [step, phase-7, website]
---
# 7.8b Website pages *(added 2026-10-23)*

Up: [[phase-7-updates-and-first-release]] · Status: **done** · Part of the website: [[step-7.8-website]]

- **Deliverables:** the pages linked from the home ([[website]]): **installation guide** (write the
  ISO to a USB stick, start in UEFI with Secure Boot off, install with the controller; its
  content follows [[step-7.3-user-guide]]), **FAQ**, **credits and licences** (the site's and
  OwneetOS's `CREDITS.md`), **privacy** ("no data collected", explained), **contributing and
  translating**. English and Italian; Angular structure ([[angular]]).
- **Done when:** each page's demo is approved ([[demo-before-code]]), then its Angular page; the
  home's "coming soon" notices for these pages are gone.
- **Started (owner, 2026-10-24)** before [[step-7.8-website]] is approved (the author's
  exception of [[collaboration]]: 7.8 stays in progress and is approved with this one).
- **Demo, first round (2026-10-24):** `design/demos/7.8b-website-pages.html`, on the approved home:
  the five pages at `#/guide`, `#/faq`, `#/credits`, `#/privacy`, `#/contribute` (header's
  Credits, Info's cards, the requirements' link, the footer), English and Italian, ordinary
  scrolling. Guide: six steps (check the PC, download, write the stick with balenaEtcher or
  Ventoy, start from it in UEFI with Secure Boot off, install with the controller on the whole
  disk, first start) and the anti-cheat warning ([[installer-and-firmware]]). FAQ: nine short
  answers. Credits: a selection of `CREDITS.md` and the site's own, with the link to the full
  list. Privacy: no data, GitHub Pages may record addresses (its statement linked), crash reports
  only with consent ([[legal-compliance]]). Contributing: translate, test and report, code.
  Asked with it: the gamepad "O" logo on the site and its start-up animation (website variant of
  the logo demo: from transparent over 2 s, the words 0.5 s apart, the site after 0.8 s more);
  skipped for visitors who asked for reduced motion.
- **Demo approved (owner, 2026-10-24)**, with two changes made in it: the slogan "Plug it. Play
  it. Own it!" stays in English in every language (more iconic; the Angular site too), and the
  credits open with the authors, Marco De Franco (fancy-dino) and Daniele De Padova
  (Danidepadawan). Next: the pages in Angular.
  The two authors side by side, at the same level, on every screen (owner, 2026-10-24); Daniele
  agreed to have his full name on the site.
- **The pages in Angular (2026-10-24, website commit 42aa7a7):** `core/components/` guide, faq,
  credits (data and models next to it: the authors, a selection of `CREDITS.md`, the site's
  own), privacy, contribute, a shared `page` frame and `footer`; the texts in `en.json` /
  `it.json`; English at `/guide`, Italian at `/it/guide` (12 prerendered pages), each route
  setting its language, title and description. The logo is the gamepad "O" draft
  (`wordmark.data.ts` generated from the logo demo's code); the start-up animation is the
  `intro` component, CSS only (it plays in the prerendered pages before any script; off with
  reduced motion). Fixed in the demo first: the Italian "Info" lost behind a comment.
  Checked: `ng build` (12 pages), `ng test` 7 tests (each page in both languages and its title,
  the two authors, the untranslated slogan), screenshots of the start-up animation, the home and
  four pages.
- **Outcome: approved by the owner on 2026-10-24**: the five pages (guide, FAQ, credits with the
  two authors first, privacy, contributing), the gamepad "O" draft as the site's logo and its
  start-up animation, in Angular, English and Italian (12 prerendered pages).
