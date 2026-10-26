---
type: step
description: "Update check and install from Settings, snapshot before every update, rollback path (decided in 6.3, option C: from Settings with the controller and automatic after
  3 failed boots, [[distribution-and-updates]]), archive snapshot date advanced…"
phase: "[[phase-7-updates-and-first-release]]"
step: "7.1"
status: in-progress
legacy: "ROADMAP.md 7.1"
tags: [step, phase-7]
---
# 7.1 Updates

Up: [[phase-7-updates-and-first-release]] · Status: **in-progress**

- **Deliverables:** update check and install from Settings, snapshot before every update,
  rollback path (as decided in 6.3), archive snapshot date advanced only after tests.
- **Agreed (owner, 2026-10-25):** see [[distribution-and-updates]] ("Updates for users", "Going
  back, always"). Plan: the owner's decisions, a demo of the update screens (Settings → System),
  the engine (signed updates around the rollback of [[step-6.3-installer-backend]]: `prepare`
  before, `arm` after), the screens' code after the demo is approved, tests in the VM with a test
  repository. Updates from the tester stick stay as they are.
- **Split (owner, 2026-10-25):** 7.1 keeps updates and "Go back to the previous version"; choosing
  any published version is [[step-7.1b-going-back-to-any-version]]. The demo shows both. Branch
  `feature/step7_updates` (from `feature/step6_installer`, owner, 2026-10-25).
- **Demo (2026-10-25):** `design/demos/7.1-updates.html`, on the approved settings demo; waiting
  for the owner's approval.
- **Demo approved by the owner (2026-10-25)** after one change: the versions of 7.1b in a
  scrolling list, one per line.
- **Engine (2026-10-25, code commit 2d7dadd on `feature/step7_updates`):** package
  `owneet-updates`: `owneet-updates check` downloads the signed list of releases
  (`URL/updates/releases.json`, one release per line: version, date, Arch Linux Archive date,
  notes per language), verifies it with pacman's keyring, and for a newer release works out the
  changed packages and the download size in a database of its own; `apply` runs the rollback's
  `prepare`, writes the release's `pacman.conf` (its archive date, `[owneet]` at `URL/vVERSION`
  with signatures required), downloads (the system unchanged if that fails), installs and runs
  `arm`. State for owneetd in `/run/owneet/system-update.json`, the verified list in
  `/run/owneet/releases.json`. A daily timer (3 minutes after start-up, then every day);
  `owneet-rollback-now.service`; polkit lets the console user start the three units. The version of
  OwneetOS is this package's `pkgver` (`/usr/share/owneet/version`), set by each release
  ([[step-7.2-release-pipeline]]). `tools/make-test-release` makes a pretend release signed with a
  throwaway key that never leaves the builder VM.
- **Tested in the test VM (2026-10-25):** 0.0.1 installed; a tampered list refused (`not_signed`);
  the signed test release 0.0.2 found with its package and size, installed (spare copy of 0.0.1,
  3 tries), blessed after the restart, then "up to date"; "Go back to the previous version"
  brought 0.0.1 back and 0.0.2 was offered again. A missing list (no release published yet)
  counts as "up to date", not "offline".
- **Left in 7.1:** owneetd (status, check, install, restart, go back, the notice after a
  rollback) and the Settings screens of the approved demo.
- **Paused (owner, 2026-10-26):** owneetd and the Settings screens touch `daemon/cmd/owneetd/main.go`
  and the interface's translation files, which Danidepadawan's phase 5 branch also changes; they
  are done after his merge, to keep out of his way. Meanwhile [[step-7.8k-website-more-languages]].
