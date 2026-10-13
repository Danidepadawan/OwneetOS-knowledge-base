---
type: best-practice
scope: project
tags: [best-practice, packaging]
---
# Packaging (PKGBUILDs)

From `packages/README.md`.

- One folder per package, named after the package; sources other than downloads live next to the
  PKGBUILD and have real `sha256sums` (never `SKIP` for local files). Only exception: packages
  built from this repository list their folders in `source-dirs`; `tools/build-packages` packs them
  into a reproducible `NAME-src.tar.gz` (not committed), whose checksum is `SKIP`.
- `license=('GPL-3.0-or-later')` for OwneetOS's own packages.
- The kernel is chosen in `iso/packages.x86_64`, not as a package dependency.
- After editing a local source file, refresh the checksums (`tools/update-checksums NAME`) and bump
  `pkgver` or `pkgrel`. Downloaded sources keep the real checksum written by hand.
- Packages without a `build()` step are built without installing any dependency in the chroot.
- Packages are built in a clean chroot in the builder VM, on the ISO's Arch snapshot. Kernel modules
  built by OwneetOS (`owneet-xone`) are rebuilt and tested again whenever the snapshot moves.
- The release version of a changed package is recorded in its step's outcome
  (e.g. "owneetd 0.11.6").
