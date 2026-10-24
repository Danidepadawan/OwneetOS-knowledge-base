---
type: step
description: "A GitHub Actions workflow publishes the prerendered site to GitHub Pages; the owner turns Pages on. Before the merge."
phase: "[[phase-7-updates-and-first-release]]"
step: "7.8c"
status: in-progress
tags: [step, phase-7, website]
---
# 7.8c Website publishing on GitHub Pages *(added 2026-10-23)*

Up: [[phase-7-updates-and-first-release]] · Status: **in-progress** · Part of the website: [[step-7.8-website]]

- **Deliverables:** a workflow that builds the static site and publishes it to **GitHub Pages**
  (actions pinned by commit hash, as the CI; only the website, never ISOs or packages:
  [[legal]]). Until the domain ([[step-7.8h-website-domain]]) the site lives at
  `fancy-dino.github.io/OwneetOS-website` (the base path set accordingly).
- **Owner input:** turn Pages on in the repository's settings (source: GitHub Actions).
- **Done when:** a push to `main` publishes the site and both languages open from the address.
- **Progress (2026-10-24):** `.github/workflows/pages.yml` in the website's repository (commit
  c70bc44): at every push to `main` (or by hand) it runs the tests, builds the site under the base
  path that `actions/configure-pages` reports (`/OwneetOS-website`, empty once the domain is set)
  and publishes it with `actions/upload-pages-artifact` and `actions/deploy-pages` (pinned by
  hash: v6.0.0, v5.0.0, v5.0.1; write rights to Pages only in the publishing job). The fonts are
  linked relatively (`fonts/...`, `externalDependencies` in `angular.json`). Tried locally under
  `/OwneetOS-website/`: the 12 pages, the fonts, the trailing slash (`/it/guide/`) and the
  languages work. **Open:** the owner turns Pages on; the first publication comes with the merge
  into `main`, and the step is checked then.
