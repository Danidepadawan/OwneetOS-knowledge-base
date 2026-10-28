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
- **Built (2026-10-28, branch `feature/step7_2_release`):** `.github/workflows/release.yml` (tag
  `vX.Y.Z` on `main`; both jobs in the environment `release`, so an author approves the build and
  then the publishing), `tools/release/` (`check`, `build`, `sign`, `sources`, `list`, `publish`,
  SourceForge's pinned host key), `release-notes/` (one folder per version, one text file per
  language), and the ISO build names a release ISO after its version and lists its packages and
  licences.
- **Tested in the builder VM (2026-10-28)** with the throwaway test key: release check, packages,
  ISO `owneetos-0.0.1-x86_64.iso` (every file checked), signatures of packages, database and ISO,
  licence list, the sources of OwneetOS's own packages. The ISO boots in the test VM with version
  0.0.1. Not testable before the first real release: SourceForge, GitHub Releases, the CI secrets.
- **Open, for the owner (2026-10-28):** `sources.archlinux.org` has only **33 of the 518** Arch
  source archives the ISO needs (it keeps a small subset), so option (a) cannot copy them from
  there. How Arch's sources are gathered waits for the owner's decision.
