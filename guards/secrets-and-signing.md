---
type: guard
tags: [guard, security]
---
# Guard: keys and signing

- **Never read, copy or print private key files**, and never put private keys or passphrases in
  the repository, in this vault or in CI logs. ([[package-signing]])
- **Never sign with the primary key**: it only certifies and revokes signing subkeys, and stays
  offline with the owner. ([[package-signing]])
- **Never type or store a signing passphrase on the owner's behalf**: every signature is made by a
  key holder typing it. ([[package-signing]])
- **Never distribute anything unsigned** to users (ISOs, packages, repository databases). Unsigned
  builds are for development only. ([[package-signing]])
- **Never use a personal e-mail address** for project identities (keys, releases): only the
  dedicated project address. ([[package-signing]])
