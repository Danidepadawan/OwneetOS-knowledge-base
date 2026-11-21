---
type: step
description: "QML installer in the OwneetOS style, gamepad-only, clear warnings and a final confirmation before erasing anything."
phase: "[[phase-6-first-boot-installer-disks]]"
step: "6.4"
status: done
legacy: "ROADMAP.md 6.4"
tags: [step, phase-6]
---
# 6.4 Installer UI

Up: [[phase-6-first-boot-installer-disks]] · Status: **done**

- **Deliverables:** QML installer in the OwneetOS style, gamepad-only, clear warnings and a final confirmation before erasing anything.
- **Demo (2026-10-26):** `design/demos/6.4-installer.html`, on the backend of
  [[step-6.3-installer-backend]]: welcome (a whole disk, offline, nothing saved yet); the
  internal disks with model, size and what is on them (Windows and BitLocker marked, too small
  ones off with the reason); the console's name ("OwneetOS", changed with the console's
  keyboard); the warning, with a specific box and a switch to turn on before "Continue" for a disk
  with Windows or BitLocker; the final confirmation, **A held for three seconds** (a ring fills;
  letting go cancels); the progress in the backend's steps; the end (remove the stick, restart)
  and the errors in the player's words. The owner likes it (2026-10-26). Where the installer is
  started from: [[step-6.2-live-vs-installed-mode]]. Branch `feature/step6_installer`.
- **Code (owner, 2026-11-01)** on `feature/phase6`, after 6.2 (approved together with it,
  [[step-6.2-live-vs-installed-mode]]):
  - owneetd 0.20.0, package `installer`: `GET /v1/installer/disks` (`owneet-install disks`),
    `POST /v1/installer/start` `{disk, size, serial, name, erase_windows}`: the disk must still be
    the one listed (path, size, serial) and usable, Windows or BitLocker only with the player's
    switch; the request goes to `/run/owneet-install/request` as plain `KEY=VALUE` lines (the name
    cleaned: one line, at most 40 characters), then `owneet-install.service` is started (polkit).
    `GET /v1/installer` and the event `installer.changed` follow `/run/owneet/install.json`; a
    state left by an earlier attempt is not this one's. Only from the USB stick. (Routes
    `/v1/installer`, not `/v1/install`, to stay apart from the games' `/v1/installs`.)
  - owneet-frontend 0.27.0, `Installer.qml` as in the approved demo; "Change the name" opens the
    console's keyboard under the field (Done keeps it, B goes back); A held three seconds fills the
    ring, let go before it nothing happens; "Restart now" restarts the console. The messages of
    the error codes the demo does not show were written in the player's words, with "Nothing was
    changed." when the disk was not touched (shown to the owner).
  - Preview `tools/preview-steps/installer.txt` and `installer-error.txt` (`@installfail`);
    `vm/vm.sh keys ret@3500` holds a key, for the final confirmation in the VM.
- **Tested in the test VM, virtual disks only (2026-11-01):** from the stick, Home's strip opened the
  installer; the two virtual disks listed (no model: their path), "Salotto" typed as the name;
  A let go after one second: no request, nothing started; held 3.5 s: the request as expected and
  the installation done in under two minutes with its four phases, then "OwneetOS is installed";
  `/dev/vda` with OWNEETBOOT and the btrfs OwneetOS, `/dev/vdb` untouched. Started from its disk:
  mode `installed`, pretty name Salotto, host name `salotto`, root `@`, the first start, then Home
  without the strip. The Windows warning and its switch were seen in the preview (Windows found on
  a disk was tested with the backend in 6.3).
- **Owner (2026-11-01):** the error texts approved, "legacy" instead of "old mode" for the UEFI one. **Approved by the owner (2026-11-01), together with 6.2: step 6.4 done.**
