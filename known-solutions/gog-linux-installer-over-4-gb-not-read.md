---
type: known-solution
description: "A big GOG Linux installer (.sh over 4 GB, e.g. The Witcher 2) is refused at once with \"The game could not be installed\" and nothing in owneetd's log: Go's zip reader cannot follow a ZIP64 archive placed after a script."
status: solved
seen: 2026-11-11
updated: 2026-11-11
tags: [known-solution, installers, gog]
---
# GOG Linux installer over 4 GB not read

## Symptom

Install on a GOG Linux installer (`.sh`) shows at once the toast "The game could not be installed."
(`error.installer`); owneetd logs no "install queued" (FrankenPC, 2026-11-11: The Witcher 2:
Assassins of Kings' Linux installer, about 21 GB). Smaller GOG Linux installers work.

## Cause

GOG's Linux installer is a makeself script followed by a ZIP archive whose offsets count from the
archive's start, not the file's. Go's `archive/zip` makes up for the script with a plain archive,
but an archive over 4 GB (or with more than 65 535 entries) is ZIP64, and Go takes the ZIP64 locator's
offset as counted from the file's start: it finds no ZIP64 end record there and answers
"zip: not a valid zip file". owneetd's check of the installer (`POST /v1/installs/inspect`) turned
any error into "invalid" without logging it.

## Solution

owneetd 0.25.22 (`daemon/internal/installs/archive.go`): when Go's reader refuses the file,
`zipStart` finds the ZIP64 end record right before its locator at the end of the file, takes the
archive's start from the locator's offset, and reads the archive from there
(`io.NewSectionReader`). An installer that cannot be read is logged ("the installer cannot be
read", with the error).

## How we found it

- The owner's retry with the stick (`out/test-logs/frankenpc-20261111-104856`): A on Install, then no
  owneetd line at all: the failure is before the install, in `/v1/installs/inspect`, the only
  caller of `error.installer` that owneetd does not log.
- `openArchive` is `zip.OpenReader` on the `.sh`; earlier installers were small.
- `TestZip64AfterTheScript`: a script followed by an archive with 70 000 entries: "not a valid zip
  file" before the fix. A one-off 4.3 GB archive after a script in the builder VM: Go's reader fails,
  `openArchive` reads the file past 4 GB.

## Watch out

Any other reader of these installers (a size check, a licence reader) must go through
`openArchive`, never `zip.OpenReader` directly. The builder VM's `/tmp` is a 3.9 GB tmpfs: a big
test file needs `TMPDIR` on its disk.
