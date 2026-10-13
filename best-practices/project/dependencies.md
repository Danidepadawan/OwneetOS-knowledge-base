---
type: best-practice
description: "When a new dependency is acceptable: lightweight first, licence check, CREDITS.md, vendoring, pinning."
scope: project
tags: [best-practice, dependencies]
---
# Dependencies

Comes from: [[hard-constraints]] (C1, C8), [[legal-compliance]], [[owneetd]].

- **Lightweight first.** Every new dependency must be justified by what it saves; measure RAM and
  disk impact (ISO size) when in doubt, and record it in the step's outcome.
- Prefer the standard library (owneetd started with the Go standard library only) and tools already
  in the image (e.g. logind instead of a new polkit rule).
- **Check the licence** before adding anything: free, allows commercial use and redistribution
  ([[legal-compliance]]).
- **Credit it in `CREDITS.md`** in the same change, and ship its licence text.
- **Go modules are vendored** (`daemon/vendor/`): builds need no network ([[go]]).
- Pin versions: Arch packages through the archive snapshot, CI actions by commit SHA, fonts and
  downloads by SHA-256.
