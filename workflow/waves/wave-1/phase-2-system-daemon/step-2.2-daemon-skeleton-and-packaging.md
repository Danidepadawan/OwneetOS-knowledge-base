---
type: step
description: "Project layout, config file, logging, systemd units, PKGBUILD, CI build + tests."
phase: "[[phase-2-system-daemon]]"
step: "2.2"
status: done
legacy: "ROADMAP.md 2.2"
tags: [step, phase-2]
---
# 2.2 Daemon skeleton and packaging

Up: [[phase-2-system-daemon]] · Status: **done**

- **Deliverables:** project layout, config file, logging, systemd units, PKGBUILD, CI build + tests.
- **Outcome:** Go module in `daemon/` (standard library only): `owneetd` serves `GET /v1/status`
  and the `GET /v1/events` stream on `$XDG_RUNTIME_DIR/owneetd.sock` (0600); `owneetctl` client;
  optional `/etc/owneet/owneetd.json`; logs to the journal; 9 unit tests. Package `owneetd`
  (static binary, user service enabled by preset); `owneet-session` writes the session mode for
  `/v1/status`. `tools/lint` and CI run gofmt, go vet, go test. Verified in the test VM: service
  active and enabled for `owneet`, status answers (version, OwneetOS version, session mode), JSON
  error on unknown endpoints, another user is refused by the socket, ~10.6 MB RAM. Test tooling:
  the VM debug shell moved to a virtio console (reliable, unlike the emulated serial port).
