---
type: best-practice
description: "tools/lint and what it checks (shellcheck, SPDX, markdownlint, Go, i18n); CI runs the same."
scope: project
tags: [best-practice, quality]
---
# Checks before committing

Run every check before committing. The tools live in the builder VM, not on the host
([[host-safety]]):

```text
tools/build-in-vm tools/lint
```

`tools/lint` runs:

1. shellcheck on every shell script (`*.sh` and files with a sh/bash shebang);
2. the SPDX licence header on every shell script and cloud-init template ([[license-headers]]);
3. markdownlint on every Markdown file (rules in `.markdownlint-cli2.yaml`, [[markdown]]);
4. Go (`daemon/`): gofmt, go vet, go test ([[go]]);
5. Go integration tests with virtual controllers (`/dev/uinput`, `go test -tags uinput`);
6. interface translations (`tools/i18n-check`, [[ui-text-and-i18n]]).

CI (`.github/workflows/ci.yml`) runs the same script on every push and pull request, plus the
`ISO` job. GitHub Actions are pinned to commit SHAs.
