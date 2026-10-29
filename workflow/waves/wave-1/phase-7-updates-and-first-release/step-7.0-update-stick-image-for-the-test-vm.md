---
type: step
description: "An OWNEETLOG stick image for the test VM (tools/make-update-stick --image), so the installed VM is upgraded in place with the packages just built instead of reinstalled."
phase: "[[phase-7-updates-and-first-release]]"
step: "7.0"
status: todo
tags: [step, phase-7]
---
# 7.0 Update stick image for the test VM

Up: [[phase-7-updates-and-first-release]] · Status: **todo**

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
- **Outcome:** (what was done, how it was verified, measurements, versions, open points)
