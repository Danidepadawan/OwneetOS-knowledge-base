---
type: known-solution
description: "OPEN: an existing web app profile keeps running an old cached copy of the extension's background worker; edits and even a version bump did not replace it."
status: open
seen: 2026-10-16
updated: 2026-10-16
tags: [known-solution, brave, extension]
---
# Brave keeps running a cached extension worker

## Symptom

- A change to `extension/background.js` has no effect in a web app that was already opened once.
  The content scripts (`content/*.js`) and the manifest's permissions do reload.
- In the profile, `Default/Preferences` keeps the old `service_worker_registration_info`
  (`{"version":"0.1.0"}`), and `Default/Service Worker/ScriptCache/` keeps the old script with
  its old time.
- Seen 2026-10-16 in the test VM (YouTube profile created at 10:43). Brave was restarted twice
  after the change, the second time with the extension's `version` raised to `0.1.1`. The worker
  was still the 10:43 one, registered as `0.1.0`.

## Cause

Not known yet. Chromium stores an extension's worker in the profile and re-registers it when the
extension changes. Why a version bump did not trigger it here is not explained.

## Solution

**Open: being tested.** It matters for updates: an owneet-base package that changes the worker
may never reach the profiles of web apps already used.

## How we found it

The path of [[brave-native-messaging-host-not-found]], step 4: the edited worker never wrote
its values. Then:

- `ls -la --time-style=+%H:%M "…/Default/Service Worker/ScriptCache/"`: our script (about 2–3 KB)
  unchanged since the profile was made; the large new entries are the site's own worker.
- `grep -a -r -o -E "connectNative|owneet_try|onConnect" "…/Default/Service Worker/" | sort | uniq -c`:
  the cached script is the old one (no marker of the edit).
- A fresh profile (`--user-data-dir=/tmp/…`) ran the edited worker at once.

## Watch out

- When testing a worker change, **use a fresh profile** (headless, step 5 of
  [[brave-native-messaging-host-not-found]]), or the result is the old code's.
- Until this is solved, assume an extension update reaches the content scripts but **not** the
  worker of existing profiles.
