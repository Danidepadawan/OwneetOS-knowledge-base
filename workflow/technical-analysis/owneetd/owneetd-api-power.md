---
type: technical-analysis
component: owneetd
legacy: "docs/daemon-design.md §4 Power"
tags: [technical-analysis, owneetd, api]
---
# owneetd API: Power — implemented (2.8)

Up: [[owneetd-design]] · Conventions: [[owneetd-design#4. API v1 (draft)]]

| Method | Path | Purpose |
|---|---|---|
| GET | `/v1/power` | `can_shutdown`, `can_restart`, `can_suspend` |
| POST | `/v1/power/shutdown` · `/restart` · `/suspend` | 202 once systemd-logind accepted it |

Errors: `power.unavailable` (503), `power.unsupported` (409, e.g. no suspend support),
`power.not_allowed` (403, a password would be needed), `power.inhibited` (409, a program blocks
it), `power.failed` (502).

- systemd-logind allows these actions to the active local session without a password (checked
  in 2.8): no extra polkit rule. owneetd never asks for a password (`interactive=false`).
- Events from logind's signals: `power.suspending`, `power.resumed` (the UI can, for example,
  refresh the controller list), `power.shutting_down`.
- Hibernation is not offered (no swap, and resume times are long).
- Tested in the test VM: suspend (QEMU reports the machine suspended; woken through QMP), restart,
  shutdown.
