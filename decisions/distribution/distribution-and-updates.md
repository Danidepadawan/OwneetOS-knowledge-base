---
type: decision
description: "ISO on SourceForge, website on GitHub Pages, [owneet] pacman repo, pinned snapshots, btrfs rollback (no snapper)."
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
- With [[optional-apps]] the apps are optional. Brave (behind the web apps) ships inside the ISO
  as package files, an offline pacman repository in `/usr/share/owneet/bundled/`, installed only
  when chosen ([[step-5.0.0-optional-web-apps]]); where the gaming programs come from is decided
  at [[step-5.0.1-optional-gaming-apps]]. The bundled packages are signed like every other one
  before they reach users ([[package-signing]]).
- Packages built with **PKGBUILD**s; updates served from an **own pacman repository `[owneet]`**
  hosted on GitHub. Updates are triggered from the Settings menu with the gamepad.
- **Updates for users (owner, 2026-10-25, step 7.1):** published as **GitHub Releases** of the
  code repository, signed ([[package-signing]]; publishing in [[step-7.2-release-pipeline]]).
  The console **checks by itself** at start-up and once a day when online (only the list, with a
  discreet notice) and **installs only when the user asks**. After installing: "Restart now" or
  "Later" (the new version is put on trial at the restart). The user sees the version, the
  download size and a short "what's new" per language; the list of packages is an optional,
  closed "Details" section for those who want it (transparency, [[writing-for-users]]).
- **Going back, always (owner, 2026-10-25):** "Go back to the previous version" stays available
  with no time limit (the spare copy lasts until the next update). The user can also **choose any
  published version** to go back to: every release's OwneetOS packages stay published, Arch's
  packages come from the Arch Linux Archive date of that release, and going back is an update in
  reverse (spare copy, download, 3 tries). A warning before confirming: personal data (saves,
  profiles) do not go back, and an old version has old security problems and may not know newer
  hardware.
- Arch packages are **pinned to Arch Linux Archive snapshots**; the snapshot date is advanced only
  after testing. CI builds use the ISO's snapshot for build dependencies too.
- **Package signing**: see [[package-signing]].
- **btrfs, rollback from the console** (owner, 2026-10-25, option C of
  [[step-6.3-installer-backend]]): systemd-boot stays. Before every update the system takes a
  snapshot and keeps the previous kernel with a boot entry "before the update". **Rollback is done
  with the controller** (Settings → "Go back to before the last update"), and **automatically**: a
  new version that does not reach the home screen in 3 boots is left by systemd-boot's boot
  counting for the previous one, with a notice. The hidden boot menu is only a keyboard fallback
  ([[hard-constraints]] C2). The user's data (games, saves, profiles, the console's settings: the
  home of `owneet`) live in separate subvolumes, never rolled back. Only the system goes back:
  Wi-Fi networks or controllers added after the update are added again (owner, 2026-10-25).
  **No snapper** (owner, 2026-10-25): one spare copy of the system, made with btrfs's own
  snapshots, is all option C needs. The spare copy is always **the last version that worked**: a
  version counts as working once the console has reached the home screen with it, and an update
  replaces the spare copy only when the running system has been confirmed working; two broken
  releases in a row never overwrite the last good one. GRUB + grub-btrfs and Limine were turned down: keyboard-only
  menus, a bootloader more, no automatic fallback.
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
| 2026-10-14 | Brave ships inside the ISO as package files (an offline pacman repository), installed only when the user picks a web app (step 5.0.0). |
| 2026-10-24 | The website's domain is **owneetos.org**, bought by the owner at Hostinger after a preliminary trademark search (step 7.5). |
| 2026-10-25 | Rollback (option C, step 6.3): systemd-boot stays; snapshot and previous kernel kept at every update; rollback from Settings with the controller and automatic after 3 failed boots (boot counting); the boot menu only a keyboard fallback; the user's data never rolled back. GRUB + grub-btrfs and Limine turned down. |
| 2026-10-25 | No snapper: one spare copy of the system (btrfs snapshot), always the last version that reached the home screen; an update replaces it only from a confirmed working system, so broken releases never overwrite it. |
| 2026-10-25 | Step 7.1: updates as signed GitHub Releases; automatic check (start-up, daily), install only on request; "Restart now" or "Later"; version, size and "what's new", packages in an optional "Details" section. Going back always possible: to the previous version with no time limit, and to any published version (downloaded, an update in reverse), with a warning. |
