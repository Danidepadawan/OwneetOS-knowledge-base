---
type: best-practice
description: "How steps are verified: builder and test VMs, frontend-preview, fakes, real hardware batches, measurements."
scope: project
tags: [best-practice, testing]
---
# Testing and verification

How the roadmap steps have been verified so far.

- **Builder VM** for builds and unit tests; **test VM** (`vm/test.sh`) to boot the ISO: serial log
  (`wait-serial`), screenshots, journal, virtual sound cards (`--audio`), simulated Wi-Fi
  (`mac80211_hwsim`), virtual controllers through `/dev/uinput` (`owneet-testpad`).
- **Frontend without an ISO:** `tools/frontend-preview` with a step file in `tools/preview-steps/`
  (keys, buttons, screenshots; a pretend owneetd with `@owneetd` steps). Every screen gets a steps
  file.
- **Unit tests with fakes** for system services (fake BlueZ, pretend processes, invented Steam
  folders); integration tests with real virtual devices.
- **Real hardware** last, by the owner (NiPoGi E3B AMD mini PC, desktop RTX 4060 + Intel UHD 770).
  Small hardware checks are batched with the next larger test ([[step-workflow]]); testers use the
  "diagnostics" and "test games" boot entries and `owneet-testlog` (USB stick labelled OWNEETLOG).
- **Measure** what the constraints talk about: ISO size, RAM (RSS per process), boot time; record
  the numbers in the step's outcome ([[hard-constraints]] C1).
- What cannot be verified in a VM is said explicitly ("Not verifiable in the VM: …") and listed as a
  check for the owner.
- The step report says what was done, how it was verified, and what deviated ([[how-we-work]]).
