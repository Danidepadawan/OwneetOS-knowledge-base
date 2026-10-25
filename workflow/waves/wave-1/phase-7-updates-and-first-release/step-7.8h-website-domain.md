---
type: step
description: "The project's own .org domain for the website (CNAME, HTTPS on GitHub Pages); bought by the owner. After the merge."
phase: "[[phase-7-updates-and-first-release]]"
step: "7.8h"
status: done
tags: [step, phase-7, website]
---
# 7.8h Website domain *(added 2026-10-23)*

Up: [[phase-7-updates-and-first-release]] · Status: **done** · Part of the website: [[step-7.8-website]]

- **Deliverables:** the site on the project's `.org` domain, **`owneetos.org`** (bought by the owner
  at Hostinger, 2026-10-24, after the preliminary trademark search of
  [[step-7.5-legal-review-before-the-public-launch]]): the domain verified on GitHub, its DNS
  pointing to GitHub Pages, the custom domain and HTTPS enforced in Pages' settings. No `CNAME`
  file (Pages published by a workflow ignores it) and no code change: the Pages workflow takes
  the base path and the address from GitHub (`/` and `https://owneetos.org`).
- **Owner input:** choose and buy the domain, point its DNS to GitHub Pages.
- **When:** after the website's merge (owner, 2026-10-23; before, the domain was planned in
  [[step-7.2-release-pipeline]]).
- **Outcome: approved by the owner on 2026-10-25.** The owner verified `owneetos.org` on GitHub
  (TXT record), pointed its DNS at Hostinger to GitHub Pages (four A, four AAAA, `www` CNAME to
  `fancy-dino.github.io`), set the custom domain and enforced HTTPS (Let's Encrypt). The site's
  default address became `https://owneetos.org` (website commit 2c7a2f6); the published pages, the
  sitemap and the sharing tags use it; `http://`, `www.` and the old
  `fancy-dino.github.io/OwneetOS-website` addresses lead to it.
