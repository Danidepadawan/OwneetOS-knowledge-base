---
type: step
description: "Builder VM from the official Arch cloud image, provisioned by script (cloud-init), project folder shared into the VM (virtiofs or 9p),…"
phase: "[[phase-0-foundations]]"
step: "0.7"
status: done
legacy: "ROADMAP.md 0.7"
tags: [step, phase-0]
---
# 0.7 Arch builder VM *(multi-prompt)*

Up: [[phase-0-foundations]] · Status: **done**

- **Goal:** an Arch Linux VM where ISOs and packages are built (archiso needs root; it gets it only inside the VM).
- **Deliverables:** builder VM from the official Arch cloud image, provisioned by script
  (cloud-init), project folder shared into the VM (virtiofs or 9p), `tools/build-in-vm` wrapper.
- **Done when:** one command on the host runs a build inside the VM and returns the output to the project folder.
- **Outcome:** `vm/builder.sh` (setup / start / stop / ssh / destroy) and `tools/build-in-vm`.
  Official Arch cloud image 20261001.604814, verified by SHA-256 and arch-boxes signature; files are
  copied with rsync instead of a shared folder (archiso needs a native filesystem). Verified: a command
  run through `tools/build-in-vm` writes `out/` back on the host; failures return a non-zero exit code;
  cold start in ~9 s; clean ACPI shutdown. The builder itself follows current Arch (not pinned):
  pinning applies to the ISO contents (step 1.1).
