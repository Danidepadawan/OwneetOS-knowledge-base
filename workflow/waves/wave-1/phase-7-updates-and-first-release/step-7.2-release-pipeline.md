---
type: step
description: "Tagged release builds the ISO in CI, signs, writes checksums and release notes, publishes the ISO (and its source archive) to…"
phase: "[[phase-7-updates-and-first-release]]"
step: "7.2"
status: in-progress
legacy: "ROADMAP.md 7.2"
tags: [step, phase-7]
---
# 7.2 Release pipeline

Up: [[phase-7-updates-and-first-release]] · Status: **in-progress**

- **Deliverables:** tagged release builds the ISO in CI, signs, writes checksums and release
  notes, publishes the ISO (and its source archive) to SourceForge and the packages to GitHub
  ([[distribution-and-updates]]). The website, its publishing and its domain have their own steps
  (owner, 2026-10-23: [[step-7.8c-website-publishing]], [[step-7.8h-website-domain]]).
- **Owner input:** create the SourceForge project.
- **Legal ([[legal-compliance]]):** a **source archive** for every release (PKGBUILDs and
  exact sources of every package in the ISO and the repository), licence list in the ISO; only
  then may CI publish ISOs and packages again.
- **Decisions (owner, 2026-10-28):** source archive option (a) ([[legal-compliance]]); release
  notes per version in every console language, drafted by the assistant and approved by the
  owner; the GitHub environment `release` with an author's approval; the signing subkey with its
  passphrase in one secret and the passphrase in another ([[package-signing]]). Steps 7.2 and
  [[step-6.2-live-vs-installed-mode]] are done in one go (owner, 2026-10-28) and approved together.
