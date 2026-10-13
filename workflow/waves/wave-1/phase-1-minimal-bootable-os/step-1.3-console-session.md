---
type: step
phase: "[[phase-1-minimal-bootable-os]]"
step: "1.3"
status: done
legacy: "ROADMAP.md 1.3"
tags: [step, phase-1]
---
# 1.3 Console session

Up: [[phase-1-minimal-bootable-os]] · Status: **done**

- **Deliverables:** autologin user, session launcher that starts **gamescope** with a
  placeholder fullscreen app; Vulkan capability check with automatic **cage** fallback;
  restart-on-crash.
- **Done when:** the ISO boots straight into a fullscreen placeholder in both modes (forced fallback tested).
- **Outcome:** `owneet-session` package (user `owneet`, getty autologin, Vulkan check, gamescope or
  cage, restart on crash, fallback, messages only in the journal). Verified in the test VM with
  screenshots: auto mode picks cage (software-only Vulkan) and shows the fullscreen placeholder;
  forced gamescope fails on the VM's software Vulkan ("not a valid physical device") and falls back
  to cage after 2 attempts; with the placeholder quitting every 5 s the session restarts it, and
  after 3 quick failures shows a plain error message and retries after 60 s. **Not verifiable in
  the VM:** gamescope actually running. It needs a hardware Vulkan driver (step 1.5) and is tested
  on the owner's PC (RTX 4060 + Intel UHD 770) booting the live ISO at the end of step 1.5.
  New tools: `tools/update-checksums`, `vm/test.sh screenshot`, `--kargs`, `--journal`.
