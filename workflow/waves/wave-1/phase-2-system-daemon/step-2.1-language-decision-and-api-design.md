---
type: step
phase: "[[phase-2-system-daemon]]"
step: "2.1"
status: done
legacy: "ROADMAP.md 2.1"
tags: [step, phase-2]
---
# 2.1 Language decision and API design — **Owner input**

Up: [[phase-2-system-daemon]] · Status: **done**

- **Goal:** choose **Go or Rust** and design the local API before writing the daemon.
- **Deliverables:** short comparison (RAM, binary size, D-Bus/evdev libraries, contributor
  friendliness), API specification (endpoints + event stream), security model (local only,
  per-session token), process split (system service vs user service).
- **Done when:** owner approves the language and the API document.
