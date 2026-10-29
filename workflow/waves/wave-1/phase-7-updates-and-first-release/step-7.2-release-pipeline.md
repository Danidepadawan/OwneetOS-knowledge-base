---
type: step
description: "Tagged release builds the ISO in CI, signs, writes checksums and release notes, publishes the ISO (and its source archive) to…"
phase: "[[phase-7-updates-and-first-release]]"
step: "7.2"
status: done
legacy: "ROADMAP.md 7.2"
tags: [step, phase-7]
---
# 7.2 Release pipeline

Up: [[phase-7-updates-and-first-release]] · Status: **done**

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
  there. **Decided (owner, 2026-10-28):** the missing archives are made from Arch's packaging
  repository at each version's tag, for every package ([[legal-compliance]]).
- **Arch's archives tested (2026-10-28)** in the builder VM (`tools/release/arch-source`, run
  with the owner's permission rule): all 485 tags exist; xz made with its checked git sources;
  zlib (an epoch in its version) stopped on a generated GitHub patch whose checksum drifted, hence
  the owner's rule for generated patches (8 of the 485 recipes use such links), after which it
  was made with the difference noted. The full run, hundreds of archives, happens at the first
  real release; a source an upstream has removed stops it and is solved by hand.
- **Outcome: approved by the owner on 2026-10-28.** What only the first real release can check
  (the uploads, the full run of Arch's archives) is checked then, with
  [[step-7.4-hardware-testing-and-v0.1.0]].
- **Before the first release, the owner** (the assistant reminds the owner when the time comes,
  owner 2026-10-28):
  1. creates the SourceForge project (its name goes in the variable `SF_PROJECT`) and adds an SSH
     key to the SourceForge account (the account name goes in `SF_USER`);
  2. creates the GitHub environment `release` in the code repository, with an author as required
     reviewer, the secrets `OWNEET_SIGNING_SUBKEY` (the signing subkey exported with its
     passphrase), `OWNEET_SIGNING_PASSPHRASE` and `SF_SSH_KEY`, and the variables `SF_USER` and
     `SF_PROJECT` ([[package-signing]]);
  3. approves the release notes of that version in every language (drafted by the assistant);
  4. pushes the release commit and its tag `vX.Y.Z` on `main`, approves the build, tests the ISO
     from the run, then approves the publishing.
