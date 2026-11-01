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
- **Resumed (owner, 2026-11-01)** on `feature/phase7`, after [[step-7.0-update-stick-image-for-the-test-vm]]
  (Danidepadawan's merge was done on 2026-10-29). Owner's choices for the screens:
  - the "up to date" row says "Checked today at {time}" for a check made today, "Checked on
    {date}" otherwise (a text the demo did not have);
  - the demo's "Other versions" row comes with [[step-7.1b-going-back-to-any-version]], not before;
  - PCs installed with the tester installer keep only the updates from the USB stick
    ([[step-4.2b-updates-from-a-usb-stick]]); the rows of 7.1 are for systems installed by the
    installer of [[step-6.4-installer-ui]] (they have the rollback the updates rely on).
  - the notice of an update found by the console, and of an installation finished while the player
    is on another screen, is a notification of [[step-3.11-notifications]] (banner, bell, list), not
    the demo's toast;
  - three error texts the demo did not have, in a window with OK like "The update did not work":
    download or check failed ("The update could not be downloaded: OwneetOS stays as it was. Try
    again later."), installation failed ("The update did not finish installing. Restart the
    console: if this version does not work, it goes back to the previous one by itself."), going
    back failed ("The console could not go back to the previous version. Nothing has changed.").
- **owneetd and the screens (2026-11-01, `feature/phase7`):** `owneet-rollback` 0.0.2 publishes its
  state for owneetd in `/run/owneet/rollback.json` (the boot partition is root's only) after every
  change and at every start-up, with the spare copy's version (kept as `/previous/version`) and
  when the console last went back by itself. owneetd 0.23.0: package `sysupdate`, API
  `/v1/system-update` ([[owneetd-api-system-update]]), event `system-update.changed`; the last
  check is kept across start-ups. owneet-frontend 0.32.0: Settings → System as in the approved
  demo (without "Other versions"), the dot on System, the windows (checking, available with "What's
  new" and Details scrolled with the right stick, downloading and installing with the bar, ready
  with "Restart now" / "Later", going back with Cancel first, "The update did not work"), the
  notifications and the three error texts, in the five languages (German, French and Spanish
  drafted, to be checked with [[step-7.9-console-more-languages]]). `tools/frontend-preview`
  learnt `@sysupdate STATE` (fake owneetd), five steps files `system-update*.txt`.
  `tools/make-test-release` makes its throwaway key again once it has expired (it lasts a day: the
  release of 2026-11-01 was not signed at first).
- **Tested (2026-11-01):** Go tests and `tools/lint` (all checks passed); every screen in
  `tools/frontend-preview`, compared with the demo. In the test VM: ISO `owneetos-2026.11.01`,
  installed on the virtual disk with `owneet-install` (6.3), test release 0.0.2 served on
  `127.0.0.1` and its key trusted. Through owneetd's API: check → `available` with notes, the
  package and the size; install → `downloading`, `ready`, spare copy 0.0.1 with its date, 3 tries;
  restart → 0.0.2 counted as working, the previous version 0.0.1 shown, the last check kept;
  go back → `back: done`, restart → 0.0.1. The notice after going back by itself (the file written
  by `keep`, published) opened "The update did not work" on the console by itself, with 0.0.1.
  **Not checked here:** the screens on the console in the VM (the first start waits for a
  controller; seen in the preview instead), a real fall back after 3 failed starts (checked in
  6.3), the screens on real hardware (with the next hardware test). Waiting for the owner's
  approval.

