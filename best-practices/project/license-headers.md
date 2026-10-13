---
type: best-practice
scope: project
tags: [best-practice, legal]
---
# Licence headers (SPDX)

Comes from: [[repository]], [[hard-constraints]] C5.

- Every new source file starts with an SPDX header in the file's comment syntax, on the first line
  (after the shebang for scripts):

  ```text
  SPDX-License-Identifier: GPL-3.0-or-later
  ```

- `tools/lint` checks it on every shell script and cloud-init template.
- OwneetOS's own packages use `license=('GPL-3.0-or-later')` ([[packaging]]).
- By contributing, a contribution is released under the same licence.
