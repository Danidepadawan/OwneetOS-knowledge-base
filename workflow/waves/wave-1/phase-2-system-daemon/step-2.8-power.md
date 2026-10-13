---
type: step
phase: "[[phase-2-system-daemon]]"
step: "2.8"
status: done
legacy: "ROADMAP.md 2.8"
tags: [step, phase-2]
---
# 2.8 Power

Up: [[phase-2-system-daemon]] · Status: **done**

- **Deliverables:** shut down, restart, suspend.
- **Outcome:** `internal/power`: systemd-logind over D-Bus (no new dependency). `GET /v1/power`
  (what is possible), `POST /v1/power/shutdown`, `/restart`, `/suspend`; events
  `power.suspending`, `power.resumed`, `power.shutting_down`. logind already allows these to the
  active local session: no polkit rule; owneetd never asks for a password. Hibernation not offered.
- **Test VM:** all three possible for `owneet`; suspend → QEMU reports the machine suspended, woken
  through QMP → `power.suspending` and `power.resumed` events, network back; restart → the system
  boots again; shutdown → VM off in 2 s. The PC's power button keeps logind's default for now
  (decided with the UI). Suspend/resume on real hardware is checked with the UI (step 3.9).
