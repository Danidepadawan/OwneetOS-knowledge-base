---
type: decision
description: "ISO on SourceForge, website on GitHub Pages, [owneet] pacman repo, pinned snapshots, btrfs + snapper."
area: distribution
status: active
decided: 2026-10-03
updated: 2026-10-20
legacy: "PROJECT_RULES.md §5"
tags: [decision, distribution]
---
# Distribution, build and updates

- The OS is distributed as an **ISO on SourceForge** (free for open-source projects, no practical
  limit on size or downloads, mirrors worldwide), with its source archive ([[legal-compliance]]).
  The project's **website** has its own `.org` domain on **GitHub Pages**; packages and updates
  stay on GitHub (decided 2026-10-11: with Steam the ISO is over GitHub's 2 GB limit per file).
  The SourceForge project is created by the owner at roadmap step 7.2; the domain after the
  website's merge ([[step-7.8h-website-domain]], owner, 2026-10-23). The website itself:
  [[website]] (Angular, its own repository, download as a redirect).
  - **Steam is in the ISO** with the 32-bit graphics drivers of every GPU ([multilib]); Steam's
    runtime is downloaded by Steam on first launch, not shipped in the ISO ([[steam-integration]]).
- ISO built with **archiso**, automated with **GitHub Actions**, with checksums and signatures. Its system
  image is **squashfs + xz** (erofs + LZMA had silently corrupted six files, 2026-10-13); every ISO
  build checks every file of the image against its package.
- With [[optional-apps]] (step 5.0) the ISO becomes slim: apps are downloaded when chosen.
- Packages built with **PKGBUILD**s; updates served from an **own pacman repository `[owneet]`**
  hosted on GitHub. Updates are triggered from the Settings menu with the gamepad.
- Arch packages are **pinned to Arch Linux Archive snapshots**; the snapshot date is advanced only
  after testing. CI builds use the ISO's snapshot for build dependencies too.
- **Package signing**: see [[package-signing]].
- **btrfs + snapper**: automatic snapshots, rollback selectable from the boot menu (open point:
  systemd-boot cannot boot btrfs snapshots by itself — decided at [[step-6.3-installer-backend]]).
- The only "hands-on" step for the user: writing the ISO to a USB stick (balenaEtcher or Ventoy),
  explained in an illustrated guide.

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-03 | Project scope, architecture and Wave 1 agreed ([[vision]]–11). |
| 2026-10-06 | ISO size: if 2 GB is exceeded, consider a free hosting service other than GitHub for the ISO ([[distribution-and-updates]], decided later). |
| 2026-10-06 | xone packaged without `xone_wired` and without blacklisting `xpad`/`mt76x2u` (wired controllers and USB Wi-Fi adapters keep working); CI builds use the ISO's Arch snapshot for build dependencies too (step 1.7). |
| 2026-10-11 | Demo 4.2 approved (with the generic store icon for Steam and no "Add games" in Favorites). **Distribution:** the ISO goes to SourceForge, the website to a `.org` domain on GitHub Pages, packages stay on GitHub ([[distribution-and-updates]]). **Steam is in the ISO** with 32-bit drivers for every GPU (about +300 MiB, [multilib] from the same snapshot). |
| 2026-10-13 | **Optional apps** (new step 5.0): the user installs only the apps they want (at installation and later, from the apps page, installed and missing ones shown differently); the ISO becomes slim when 5.0 arrives (apps downloaded when chosen; option b). |
| 2026-10-23 | The domain is bought after the website's merge (step 7.8h), no longer at step 7.2. |
| 2026-10-20 | The website: Angular, static on GitHub Pages, its own repository; download as a redirect to SourceForge ([[website]]). |
| 2026-10-13 | The ISO's system image is squashfs + xz instead of erofs + LZMA, which had silently corrupted six files (kernel modules, an AMD firmware); every ISO build now checks every file against its package. ISO 1822 MiB. |
