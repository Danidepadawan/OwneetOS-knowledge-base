---
type: step
phase: "[[phase-1-minimal-bootable-os]]"
step: "1.2"
status: done
legacy: "ROADMAP.md 1.2"
tags: [step, phase-1]
---
# 1.2 Own package repository `[owneet]`

Up: [[phase-1-minimal-bootable-os]] · Status: **done**

- **Deliverables:** `packages/` with PKGBUILD layout, build script (clean chroot in the builder
  VM), repository database, package signing key, repo consumed by the ISO build.
- **Owner input:** where the signing key is stored and who holds it.
- **Done when:** a dummy `owneet-base` package is built, signed and installed into the ISO.
- **Progress:** `tools/build-packages` builds `packages/*` in a clean chroot on the ISO's Arch
  snapshot and creates `out/repo/x86_64/owneet.db`; `tools/build-iso` adds the local `[owneet]`
  repository to a copy of the profile. `owneet-base` 0.0.1 is built and installed in the ISO, which
  still boots to the login prompt. `tools/keys/create-signing-key` written and tested with a
  throwaway key. Real key created by the owner (`B3BD…456E`). `owneet-keyring` package added
  (built before `owneet-base`, dependency order). `tools/keys/install-working-key` and
  `tools/sign-repo` written; negative test passed (repository signed with a fake key: ISO build
  refused at database sync); stale cached packages fixed. The owner signed the repository with
  `tools/sign-repo`: all signatures valid (subkey `61D8…3C37`); the ISO built from it verified them
  (`SigLevel = Required DatabaseRequired`), contains `owneet-base` and `owneet-keyring`, and boots
  to the login prompt.
