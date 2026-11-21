---
type: step
description: "An OWNEETLOG stick image for the test VM (tools/make-update-stick --image), so the installed VM is upgraded in place with the packages just built instead of reinstalled."
phase: "[[phase-7-updates-and-first-release]]"
step: "7.0"
status: done
tags: [step, phase-7]
---
# 7.0 Update stick image for the test VM

Up: [[phase-7-updates-and-first-release]] · Status: **done**

- **Why:** the system installed in the test VM already updates itself from the OWNEETLOG stick at
  start-up (`owneet-update`, [[step-4.2b-updates-from-a-usb-stick]]), and `vm/test.sh boot --stick
  IMAGE` plugs an image in as a USB stick. But `tools/make-update-stick` only fills a real, mounted
  stick: nothing makes the image, so testing a new package in the VM meant a new ISO and a
  reinstall. Asked by the owner on 2026-10-16, while testing owneetd 0.12.1 (step 5.2).
- **Deliverables:**
  - `tools/make-update-stick --image FILE`: creates or refreshes a FAT image labelled `OWNEETLOG`
    with the same `owneet-updates/` folder as a real stick (packages of `out/repo/x86_64`,
    `owneet.db` as a copy), written with `mkfs.fat` and `mcopy` (no mount, no root).
  - Run in the builder VM (`tools/build-in-vm`, where `archiso` brings both tools), never on the
    host ([[host-safety]]); the image lands in `out/`.
  - The loop documented in `vm/README.md` and `docs/tester-install.md`:
    `tools/build-in-vm 'tools/build-packages PKG… && tools/make-update-stick --image out/owneetlog.img'`,
    then `vm/test.sh boot --disk --stick out/owneetlog.img` (with the usual `--debug-shell`,
    `--tools`). `pkgver` must still rise: only newer packages are installed.
- **Done when:** a package rebuilt with a higher `pkgver` reaches the installed test VM through
  the image at the next boot, with no ISO built and no reinstall; `pacman -Q` in the VM shows the
  new version and the update state (`/run/owneet/update.json`) says `done`.
- **Started (owner, 2026-11-01):** first of the steps that can be done now, in order (7.0, 7.1,
  7.1b, 7.3); branch `feature/phase7` (from `feature/phase6`) in the code and the vault, one
  branch for the whole phase 7 (owner, 2026-11-01).
- **Outcome (2026-11-01):** `tools/make-update-stick --image out/FILE`: the same `owneet-updates/`
  folder as on a real stick (a shared `fill` function), in a FAT32 image labelled `OWNEETLOG` with
  no partition table, made anew each time with `mkfs.fat` and `mcopy`; size = the packages plus a
  quarter plus 64 MiB for the logs (332 MiB today). Only in `out/` (so `tools/build-in-vm` brings it
  back), and without `mkfs.fat` / `mcopy` it says to run it in the builder VM, like the other
  tools. Documented in `vm/README.md` and `docs/tester-install.md`. **Checked:** shellcheck and
  `tools/lint` (all checks passed); a path outside `out/` refused; `fsck.fat` clean, `blkid` sees
  `LABEL="OWNEETLOG" TYPE="vfat"`. **Done-when test** in the test VM: tester installation of
  `owneetos-2026.11.01` on the virtual disk (`owneet-updates 0.0.1-1`); in the builder VM
  `owneet-updates` rebuilt with `pkgrel=2` (in the VM's copy only) and the image made; `vm/test.sh
  boot --disk --stick out/owneetlog.img`: at start-up `owneet-update-boot` installed
  `owneet-updates 0.0.1-1 → 0.0.1-2`, `pacman -Q` shows 0.0.1-2, `/run/owneet/update.json` says
  `done`; no ISO built, no reinstall. The real package (0.0.1-1) rebuilt afterwards, so
  `out/repo` has no test version. **Open points:** the logs the test VM writes on the image
  (`owneet-testlog`) are lost when the image is made again; the test VM first ignored the ISO
  (stale firmware entries, [[test-vm-ignores-the-iso]]). **Approved by the owner (2026-11-01): done.**
