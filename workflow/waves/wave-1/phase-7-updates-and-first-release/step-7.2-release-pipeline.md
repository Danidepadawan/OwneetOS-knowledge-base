---
type: step
phase: "[[phase-7-updates-and-first-release]]"
step: "7.2"
status: todo
legacy: "ROADMAP.md 7.2"
tags: [step, phase-7]
---
# 7.2 Release pipeline

Up: [[phase-7-updates-and-first-release]] · Status: **todo**

- **Deliverables:** tagged release builds the ISO in CI, signs, writes checksums and release
  notes, publishes the ISO (and its source archive) to SourceForge and the packages to GitHub;
  the website on GitHub Pages with the project's `.org` domain ([[distribution-and-updates]]).
- **Owner input:** create the SourceForge project and buy the domain.
- **Legal ([[legal-compliance]]):** a **source archive** for every release (PKGBUILDs and
  exact sources of every package in the ISO and the repository), licence list in the ISO; only
  then may CI publish ISOs and packages again.
