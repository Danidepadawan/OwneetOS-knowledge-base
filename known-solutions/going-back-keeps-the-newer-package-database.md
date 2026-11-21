---
type: known-solution
description: "Going back to an older OwneetOS release fails with 'signature … is invalid' for the owneet database, or keeps Arch's newer packages: pacman -Sy keeps the newer databases; -Syy fixes it."
status: solved
seen: 2026-11-01
updated: 2026-11-01
tags: [known-solution, updates, pacman]
---
# Going back keeps the newer package databases

## Symptom

Going back to an older version ([[step-7.1b-going-back-to-any-version]]) stops at once with
`download_failed`; `/run/owneet-updates/download.log` says:

```text
error: owneet: signature from "OwneetOS TEST KEY (never for releases) <test@invalid>" is invalid
error: failed to synchronize all databases (unexpected error)
```

The release server's log shows `GET /vOLD/owneet.db` answered **304** and `GET /vOLD/owneet.db.sig`
answered **200**. The same can happen without any error for Arch's databases, which are not signed:
the console keeps the newer `core`, `extra`, `multilib` and never goes back to the older Arch packages.

## Cause

`pacman -Sy` asks the server for each database with `If-Modified-Since` set to the time of the file
already on the disk. An older release's database is older than the one there, so the server answers
"not modified" and pacman keeps the newer database; the signature has no such check, so the older
release's signature is downloaded next to the newer database and does not match it. Updates never
see it, since a newer release's databases are always newer.

## Solution

Going back refreshes the databases by force: `pacman -Syyuuw` (code: `owneet-updates`,
`install_release` with `BACK=true`, code commit 369f926 on feature/phase7, 2026-11-01). The size of going back is worked out
in a database folder of its own, made empty each time, so it never had the problem.

## How we found it

In the test VM, `curl … /v1/system-update/go-to` → `failed` / `download_failed`; the download log
gave the signature error; `ls -la --time-style=full-iso /var/lib/pacman/sync/` showed `owneet.db`
with the newer release's time; the HTTP server's log of `tools/make-test-release`'s releases showed
the 304 for the database and the 200 for its signature.

## Watch out

Anything that points pacman at an older repository (an older Arch Linux Archive date, an older
release) needs `-yy`. When going back fails at once with a signature error, look at the server's
answers for the database and its `.sig` first.
