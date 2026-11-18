---
type: technical-analysis
description: "Research for point 4 of the games method: how the console's NVIDIA driver is chosen, tried against games before it ships, and gone back from; what Arch and Bazzite offer; the Cyberpunk 2077 test with driver 595."
component: games
tags: [technical-analysis, games, nvidia]
---
# A tried NVIDIA driver (research, 2026-11-18)

Point 4 of [[game-compatibility-method]].

## Today

- `owneet-hardware` depends on Arch's `nvidia-open` (built for one kernel), `nvidia-utils`, `lib32-nvidia-utils`;
  the console's packages are pinned to an Arch snapshot (update extras `pkglist-2026.10.13`: `linux 7.2.8`,
  NVIDIA 615.71.09). A new driver arrives only when the snapshot moves, never tried against games before.
- Going back: the console's own release rollback (snapshots, [[distribution-and-updates]]) takes the driver back
  with the rest.

## What exists

- NVIDIA's Linux drivers (download archive): 595.x, 610.x, 615.71.09, 615.78.08, 620.70.06, 620.73.04
  (2026-11-17, "minor bug fixes"). NVIDIA publishes no dates; its fixes are confirmed only by trying.
- Arch: every past build in `archive.archlinux.org` (e.g. `nvidia-open 595.71.05` of May 2026, built for that
  month's kernel). A prebuilt `nvidia-open` matches one kernel: an older driver on today's kernel needs
  `nvidia-open-dkms` built in the builder VM, if the driver supports that kernel.
- Bazzite: images per driver, an earlier image kept 90 days to go back to, a driver refresh tested and patched
  within a day when it breaks ([Bazzite drivers](https://castrojo.github.io/jorgepilot/reports/ublue/bazzite-driver-versions),
  [rollback](https://universal-blue.discourse.group/t/update-rolled-back-updates-paused-now-what/6783)).

## Proposal

1. A new driver (and a new Proton chosen by the console) goes to the testers' update stick first; it ships only
   after the test games ([[game-test-matrix]]) passed on the test hardware.
2. Known regressions read before choosing: NVIDIA's Linux forum, vkd3d-proton's and Proton's issues.
3. The release notes say which driver ships and which known game problems it has.

## Cyberpunk 2077 test (driver vs card)

The development PC (RTX 4060, Ada, 595.99.02) is not a proof: the game last ran there in June, before its version
2.5. On the FrankenPC (GTX 1660 SUPER, Turing; the same card ran the game under Windows): try 620.73.04 when Arch has
it; try a 595 driver only if it builds for the console's kernel (`nvidia-open-dkms` in the builder VM).
