---
type: best-practice
scope: language
language: go
tags: [best-practice, go]
---
# Go (owneetd)

- `gofmt` formatting (tabs), `go vet` clean; both run in `tools/lint`.
- **Standard library first**; third-party modules only when they save real work, and **vendored**
  in `daemon/vendor/` (update in the builder VM with `go get`, `go mod tidy`, `go mod vendor`,
  then copy `go.mod`, `go.sum` and `vendor/` back). Current: `godbus/dbus/v5`, `jfreymuth/pulse`,
  `jezek/xgb`. ([[dependencies]], [[owneetd]])
- Layout: `cmd/<binary>` for programs, `internal/<area>` for packages (one area per system service:
  `bluetooth`, `network`, `audio`, `power`, `apps`, `display`…).
- Doc comment on every package and exported identifier, starting with its name
  (`// Package power shuts down, …`, `// Status is the body of GET /v1/power.`).
- Logging with `log/slog` to the journal; **never log secrets** (Wi-Fi passwords).
- API errors: a stable dotted `code` (`wifi.wrong_password`) plus an English `message` for logs;
  the UI translates the code. Exported sentinel errors (`ErrUnsupported`) map to codes.
- Tests: unit tests next to the code (`*_test.go`) with fakes for D-Bus services; integration tests
  that need `/dev/uinput` behind the `uinput` build tag. Race detector clean.
- Static binary (`CGO_ENABLED=0`).
