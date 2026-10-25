---
type: step
description: "Whole-disk install: partitioning, btrfs subvolumes, bootloader, user, first-boot setup. Tested on virtual disks only, never on…"
phase: "[[phase-6-first-boot-installer-disks]]"
step: "6.3"
status: in-progress
legacy: "ROADMAP.md 6.3"
tags: [step, phase-6]
---
# 6.3 Installer backend *(multi-prompt)*

Up: [[phase-6-first-boot-installer-disks]] · Status: **in-progress**

- **Deliverables:** whole-disk install: partitioning, btrfs subvolumes, bootloader, user,
  first-boot setup. Tested on virtual disks only, never on the host.
- **Decision (owner, 2026-10-25): option C.** systemd-boot cannot boot btrfs snapshots by itself;
  instead of GRUB + grub-btrfs or Limine (keyboard-only menus, a bootloader more), systemd-boot
  stays and rollback is done from the console with the controller, and automatically after 3
  failed boots (boot counting), the boot menu only a keyboard fallback
  ([[distribution-and-updates]]). The user's data live in subvolumes never rolled back.
- **Starts from** the tester installer `owneet-tester-install` of [[step-4.2a-tester-installer]]
  (GPT, 1 GiB EFI system partition, btrfs subvolumes, systemd-boot).
- **Branch:** `feature/step6_installer` in the code and in this vault (owner, 2026-10-25).
- **Plan (owner, 2026-10-25):** a new package `owneet-installer` (no change to `owneet-base`):
  `owneet-install disks` (each internal disk with its model, size, partitions, Windows and
  BitLocker found) and `owneet-install install` (offline: the stick's own image, with its
  progress), run as root through a systemd service; [[step-6.4-installer-ui]] wires it to
  `owneetd` and draws it. The rollback machinery of option C (a btrfs spare copy of the last working system, no snapper; the "before the update"
  boot entry with the previous kernel, boot counting, the boot marked good only when the console
  reaches the home screen, the rollback command) is part of this step, tested in the VM by
  breaking an update on purpose; [[step-7.1-updates]] keeps the update flow in Settings and its
  screens. Disks, Windows and BitLocker, the console's name: [[installer-and-firmware]].
- **Built (2026-10-25, code commit 802a7d5 on `feature/step6_installer`):**
  - `owneet-installer` (`packages/owneet-installer/`): `owneet-install disks` (JSON, any user:
    internal disks only, the boot stick and USB disks never listed; partitions; `windows` from
    Microsoft's partition types or NTFS, `bitlocker` from blkid; `usable` false below 32 GB) and
    `owneet-install install` (root, through `owneet-install.service`, live stick only; polkit
    lets the console user start it). The request (`/run/owneet-install/request`, written by the
    console) is read key by key as plain text, never as an environment file (it could carry
    `LD_PRELOAD`); the disk must match its path, size and serial again; Windows or BitLocker need
    `OWNEET_INSTALL_ERASE_WINDOWS=yes`. Progress in `/run/owneet/install.json` (states and error
    codes for the screens of [[step-6.4-installer-ui]], translated there). Subvolumes `@`,
    `@home`, `@log`, `@pkg`; fstab without the root's subvolume (the boot entry chooses it); the
    console's name as pretty name and host name ("Più Console" → `piu-console`).
  - `owneet-rollback` (`packages/owneet-rollback/`): `prepare` (the running system becomes the
    spare copy `@previous` with its kernel in `/boot/previous` and the entry
    `owneetos-previous.conf`, only if it has worked), `arm` (`owneetos+3.conf`), `check`
    (`owneet-boot-check.service`, before `boot-complete.target`: the console's interface and
    `owneetd` running for a minute mark `/etc/owneet/system-good`; on the spare copy started
    because the new version ran out of tries, it keeps the spare copy as the system and writes
    `/var/lib/owneet/rolled-back` for the notice), `now` (Settings, by hand) and `keep`.
- **Tested in the test VM, virtual disks only (2026-10-25):** the disks listed as the console
  user; Windows found on a disk with a Microsoft partition; refused: Windows not confirmed, a
  different size, the CD drive with `LD_PRELOAD` slipped into the request; installation on the
  32 GB disk in about 90 s with steady progress, the other disk untouched; the installed system
  starts from its disk with its name and subvolumes, and is counted as working; a broken update
  (the interface made non-executable) used its 3 tries and the 4th start ran the spare copy, which
  became the system again (broken version removed, notice written); a working update was blessed
  by `systemd-bless-boot`; the rollback by hand brought the previous version back and removed the
  one given up; two broken updates in a row kept the last good version as the spare copy.
- **Open:** BitLocker detection relies on blkid and could not be faked in the VM (a real BitLocker
  volume is needed); "working" means the interface and `owneetd` running for a minute, until the
  console gives a precise "home screen reached" signal (after Danidepadawan's merge of phase 5);
  the update flow calling `prepare`/`arm` and the notice are [[step-7.1-updates]]; the tester
  installer `owneet-tester-install` (in `owneet-base`) is left as it is. Waiting for the owner's
  approval.
