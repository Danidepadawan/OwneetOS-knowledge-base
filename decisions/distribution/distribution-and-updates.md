---
type: decision
area: distribution
status: active
decided: 2026-10-03
updated: 2026-10-11
legacy: "PROJECT_RULES.md §5"
tags: [decision, distribution]
---
# Distribution, build and updates

- The OS is distributed as an **ISO on SourceForge** (free for open-source projects, no practical
  limit on size or downloads, mirrors worldwide), with its source archive ([[legal-compliance]]).
  The project's **website** has its own `.org` domain on **GitHub Pages**; packages and updates
  stay on GitHub (decided 2026-10-11: with Steam the ISO is over GitHub's 2 GB limit per file).
  The SourceForge project and the domain are created by the owner at roadmap step 7.2.
  - **Steam is in the ISO** with the 32-bit graphics drivers of every GPU ([multilib]); Steam's
    runtime is downloaded by Steam on first launch, not shipped in the ISO ([[steam-integration]]).
- ISO built with **archiso**, automated with **GitHub Actions**, with checksums and signatures.
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
