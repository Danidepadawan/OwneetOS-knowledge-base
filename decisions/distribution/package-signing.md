---
type: decision
description: "Two-level OpenPGP key: offline primary, expiring signing subkey, who signs, unsigned development builds."
area: distribution
status: active
decided: 2026-10-04
updated: 2026-10-13
legacy: "PROJECT_RULES.md §5 (Package signing)"
tags: [decision, distribution, security]
---
# Package signing

Two-level OpenPGP key:

- **Primary key** ("vault"): never used to sign packages; kept **offline by the owner**, with a
  backup outside the repository and outside everyday PCs. It certifies and revokes signing subkeys.
  Fingerprint `B3BD F4E3 E477 2D3F 7E86 1A87 8D02 23BC EE51 456E`.
- **Signing subkey** ("working stamp"): signs packages and the repository; **expires** (e.g. 2
  years) and is renewed with the primary key. Held by the owner and the second developer; from
  roadmap step 7.2 also stored as a protected GitHub secret for release builds.
- OwneetOS systems trust the primary key, so a compromised or expired subkey can be replaced
  without any action from users.
- The key's identity uses a **dedicated project e-mail address** (`owneet@proton.me`, public: it
  ships in every ISO), never a personal one.
- The primary key's backup lives in **two places**: a dedicated USB stick and the owner's password
  manager.
- Private keys never enter the repository or CI logs, and the assistant never reads or copies
  private key files. The owner created the key with `tools/keys/create-signing-key`.
- **Who signs:** every signature needs the passphrase, typed by a key holder
  (`tools/keys/install-working-key` once per builder VM, then `tools/sign-repo`). From roadmap step
  7.2, release builds are signed by CI with the subkey stored as a protected GitHub secret.
- **Development builds** may use the local `[owneet]` repository unsigned (packages are built and
  consumed inside the same builder VM); `tools/build-iso` prints a warning. A signed repository is
  always verified (`SigLevel = Required DatabaseRequired`). **Anything distributed to users must be
  signed.**
- **Tester systems** (installed by the tester installer) accept unsigned OwneetOS packages, and only
  from the OWNEETLOG USB stick; nothing is published online ([[test-pcs]]).

Guard: [[secrets-and-signing]].

## History

Entries of the [[decision-log]] that shaped this note.

| Date | Decision |
|---|---|
| 2026-10-04 | Package signing: two-level key (primary offline with the owner, expiring signing subkey for owner + second developer), dedicated project e-mail ([[distribution-and-updates]]). |
| 2026-10-04 | Signing key created (primary `B3BD F4E3 E477 2D3F 7E86 1A87 8D02 23BC EE51 456E`, `owneet@proton.me`). Key holders sign with their passphrase; development builds may be unsigned; distributed builds must be signed ([[distribution-and-updates]]). |
| 2026-10-13 | **Test PCs are installed**, not run from a stick: a tester installer (step 4.2a, boot entry "Install OwneetOS (testers)") and updates from a USB stick (step 4.2b: the `owneet-updates` folder on the OWNEETLOG stick, applied automatically at boot and from Settings → System), before step 4.3. Nothing is published online. Only systems installed by the tester installer accept unsigned OwneetOS packages, and only from that stick (option b). Test PC: "FrankenPC" (i7-6700, 16 GB, 96 GB SSD + 2 TB HDD, GTX 1660 Super); the NiPoGi stays a live-stick test PC. |
