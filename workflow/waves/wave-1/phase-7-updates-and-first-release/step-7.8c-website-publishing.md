---
type: step
description: "A GitHub Actions workflow publishes the prerendered site to GitHub Pages; the owner turns Pages on. Before the merge."
phase: "[[phase-7-updates-and-first-release]]"
step: "7.8c"
status: todo
tags: [step, phase-7, website]
---
# 7.8c Website publishing on GitHub Pages *(added 2026-10-23)*

Up: [[phase-7-updates-and-first-release]] · Status: **todo** · Part of the website: [[step-7.8-website]]

- **Deliverables:** a workflow that builds the static site and publishes it to **GitHub Pages**
  (actions pinned by commit hash, as the CI; only the website, never ISOs or packages:
  [[legal]]). Until the domain ([[step-7.8h-website-domain]]) the site lives at
  `fancy-dino.github.io/OwneetOS-website` (the base path set accordingly).
- **Owner input:** turn Pages on in the repository's settings (source: GitHub Actions).
- **Done when:** a push to `main` publishes the site and both languages open from the address.
