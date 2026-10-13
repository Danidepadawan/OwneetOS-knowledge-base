---
type: step
description: "GitHub Actions job building the ISO (privileged container), checksums, build artefact."
phase: "[[phase-1-minimal-bootable-os]]"
step: "1.6"
status: done
legacy: "ROADMAP.md 1.6"
tags: [step, phase-1]
---
# 1.6 ISO build in CI

Up: [[phase-1-minimal-bootable-os]] · Status: **done**

- **Deliverables:** GitHub Actions job building the ISO (privileged container), checksums, build artefact.
- **Done when:** a CI-built ISO boots in the test VM.
- **Progress:** job `ISO` builds packages and ISO in a privileged, pinned Arch Linux container
  (`tools/ci/build-iso`, `OWNEET_NO_CHROOT=1`), only when ISO inputs changed, on demand or weekly;
  artifact kept 7 days (unsigned development build). Simulated with Podman in the builder VM with
  the same image: ISO built (1664 MiB) in 2 min 50 s with a warm package cache.
  **First run on GitHub (2026-10-06): green.** Job `ISO` took about 10 min (2.5 min freeing disk
  space, 7.5 min packages + ISO); artifact `owneetos-dev-iso-14`, 1664 MiB. Downloaded, checksum
  verified, booted in the test VM: console session starts; diagnostics report clean (boot 8.5 s,
  no failed units). **Since 2026-10-07 the ISO is no longer uploaded** (GPL source obligations,
  [[legal-compliance]]): CI builds it as a check only.
