---
type: best-practice
scope: language
language: shell
tags: [best-practice, shell]
---
# Shell scripts

- `#!/usr/bin/env bash`, then the SPDX line ([[license-headers]]), then a header comment: what the
  script does, how it is run, its options and test hooks ([[code-comments]]).
- `set -euo pipefail` (or `set -uo pipefail` where failures are handled on purpose, e.g. the
  session loop).
- **shellcheck clean**; `.shellcheckrc` follows `source` statements relative to the script's folder.
- Find the repository root from the script (`ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"`).
- Developer scripts in `tools/` must never modify the host system ([[host-safety]]); builds go
  through `tools/build-in-vm`.
- 4-space indentation ([[formatting]]); PKGBUILDs use 2 spaces ([[packaging]]).
