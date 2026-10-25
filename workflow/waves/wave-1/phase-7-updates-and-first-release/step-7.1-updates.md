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
