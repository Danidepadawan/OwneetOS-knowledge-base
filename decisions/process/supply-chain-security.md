---
type: decision
description: "How OwneetOS keeps third-party code honest (signatures, pinned versions, checksums from two sources) and the security proposals still open (pinned Proton, sandboxed games, virus scanning)."
area: process
status: active
decided: 2026-10-16
updated: 2026-10-16
tags: [decision, process, security, dependencies]
---
# Supply chain and malware

OwneetOS does not scan for viruses and cannot prove that other people's code is sound. What it
does is make sure that what it builds and installs is exactly what its authors published, from
their official sources, unchanged on the way (owner's question, 2026-10-16).

## In place

- **Arch Linux packages** are signed by Arch's packagers; pacman refuses a bad signature. They come
  from a pinned Arch Linux Archive snapshot, so the exact versions are known.
- **OwneetOS packages** are built from this repository in a clean chroot in the builder VM (never
  on the developer's PC); the files they download are pinned by version and checksum; what reaches
  users is signed ([[package-signing]], [[secrets-and-signing]]).
- **Tests with downloaded programs** run in throwaway containers inside the builder VM and are
  deleted afterwards.
- **Proton and its runtime** are downloaded by umu-launcher from GE-Proton's GitHub releases and
  Valve's repository, checked with their published SHA-512 / SHA-256. Those checksums come from
  the same place as the files: they catch a damaged download, not a compromised release.

## Agreed (owner, 2026-10-16)

- **Programs we package ourselves are built from source**, never from the authors' ready-made
  binaries, with the source pinned by version and checksum. When the authors publish no signature,
  the checksum is **checked against a second, independent source** before it is written down
  (e.g. the Arch User Repository recipe of the same version). First case: DOSBox Staging 0.83.0
  with iir1 1.10.0 and libmt32emu 2.8.2 ([[step-4.5-windows-games-proton]]). Recipes taken from
  the AUR are read and rewritten, never run as they are. → [[dependencies]]

## Proposed, waiting for the owner's choice

1. **Pinned GE-Proton and runtime** (recommended, small): the console uses a GE-Proton version (and
   Steam Linux Runtime) chosen by the project, with its checksum recorded in this repository, instead
   of "the latest"; updating it becomes an explicit change.
2. **Sandboxed games on disks** (later; more work): games from disks run in a container that sees
   only their folder and their saves, not the rest of the user's files. → [[backlog]]
3. **Virus scanning of games on disks** (ClamAV): possible but heavy and of little use against
   games; not recommended. → [[backlog]]

## History

| Date | Decision |
|---|---|
| 2026-10-16 | Answer to the owner's question on malware: what is in place; programs we package are built from pinned, checksummed sources, checked against a second source when unsigned; three proposals recorded (pinned Proton, sandboxed games, virus scanning). |
