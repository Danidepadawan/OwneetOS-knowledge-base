---
type: step
description: "A 404 page in English and Italian for wrong addresses, served by GitHub Pages. Before the merge."
phase: "[[phase-7-updates-and-first-release]]"
step: "7.8d"
status: in-progress
tags: [step, phase-7, website]
---
# 7.8d Website not-found page *(added 2026-10-23)*

Up: [[phase-7-updates-and-first-release]] · Status: **in-progress** · Part of the website: [[step-7.8-website]]

- **Deliverables:** a not-found page (`404.html`, prerendered) in the site's look, in the
  visitor's language when the address says it (`/it/...`), with a way back home.
- **Done when:** a wrong address on the published site shows it.
- **Progress (2026-10-24):** demo `design/demos/7.8d-website-not-found.html` (on the approved
  pages demo): a big "404", "This page is not here" / "Questa pagina non c’è", "The address may be
  mistyped, or the page has moved.", and three ways out: back to the home, the install guide, the
  questions; the site's header and footer. Its language comes from the address (`/it/...` in
  Italian, every other address in English). Approved by the owner on 2026-10-24.
- **Code (2026-10-24, website commit 31b18c2):** `core/components/not-found/` on the page frame
  (which gets `back` and an `.above` slot); routes `it/**` (Italian) and `**` (English), plus
  `/404`, prerendered and turned into `404.html` by `scripts/not-found-page.mjs` (in `npm run
  build` and in the Pages workflow); `robots: noindex` on it; the language links keep the wrong
  address (`/nowhere` ↔ `/it/nowhere`); texts `not-found.*` in the JSON files; one more test (8).
  Tried under `/OwneetOS-website/` with a server that answers like GitHub Pages: wrong addresses
  answer 404 with the page, in Italian under `/it/`. **Open:** checked on the published site
  after the merge, with 7.8c.
