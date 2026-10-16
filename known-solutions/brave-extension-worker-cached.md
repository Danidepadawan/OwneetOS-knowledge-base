---
type: known-solution
description: "OPEN (fix in owneet-base 0.0.39, to verify on a real update): a used web app profile gets a changed extension worker only when the manifest's version AND the worker's file name both change; one alone keeps the old worker or leaves none."
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

Found 2026-10-16 with Brave 1.97.57 (`--load-extension`, location 8 = command line). **On a
profile that already holds a registration for the extension's worker, Brave never registers it
again while the worker's URL (`chrome-extension://<id>/background.js`) stays the same.** The
Service Worker database is not written at all on later launches. What does **not** trigger a new
registration (each one tested):

- a changed `background.js`, with or without a raised `version`;
- a clean shutdown (SIGTERM to Brave's main process) instead of the unit's stop: same result, so
  the way owneetd stops the app is not the cause;
- removing `service_worker_registration_info` from `Default/Preferences`, or the extension's whole
  entry in `extensions.settings`: Brave reloads the extension (`last_update_time` moves on every
  launch) but keeps the stored worker. `service_worker_registration_info` is not what decides it.

What **does** trigger it:

- **a new file name for the worker (`"service_worker"` in the manifest) together with a new
  `version`**: Brave registers the new URL, runs the new code and drops the old script from
  `ScriptCache` (the first rename tests ran after a version bump, so both had changed);
- **no registration in the profile** (a fresh profile, or `Default/Service Worker/` deleted).

What **breaks** it: **a new file name with the same `version`** (owneet-base 0.0.38, tested
2026-10-16). Brave does not register the new URL and refuses to start the stored one: the profile
is left **without a worker** (no bridge), and with full logging Brave prints
`ERROR:…service_worker_task_queue.cc:533] DidStartWorkerFail <extension id>: 18` about every
second.

Why it was hard to see: everything else in the extension does update, and the old worker keeps
working, so the problem only shows up as "my change does nothing".

## Solution

**Fix (owner, 2026-10-16), in owneet-base 0.0.39** ([[decision-log]], [[extension-design]]):

- **The worker's file name and the manifest's version change together.** The owneet-base package
  (`packages/owneet-base/PKGBUILD`) installs `extension/background.js` as
  `background-<short hash of the file>.js`, and writes that name and **its own version**
  (`<pkgver>.<pkgrel>`, e.g. `0.0.39.1`) into the installed `manifest.json`; the build fails if
  either is missing. Every package release has a new version, so a changed worker always arrives
  with both. A release with an unchanged worker only changes the version: Brave keeps the
  identical worker. Nothing in the profiles is touched, and the sites' own workers are kept.
- Rejected: a version made from the hash (a repeat by chance, once in 65,536 updates, would
  rename the worker with the same version and leave every used profile without a worker).
- **Verified by simulation** (2026-10-16, test VM, the YouTube profile used under 0.0.37): the
  0.0.38 manifest edited to version `0.1.0.1`. A headless run on a copy of the profile: one
  `DidStartWorkerFail` at the first start (50 ms after launch, the old stored worker), then a new
  `ScriptCache` entry and the old one gone; a second run: none. The real session: A on the search
  field started `owneet-bridge`. **Still to verify:** the same through a real package update.
- Rejected (works, tested): before it launches Brave, owneetd compares a stamp of the
  installed extension with one saved in the profile. When they differ, it deletes
  `Default/Service Worker/`. It costs code in owneetd, and it also deletes the site's workers
  (YouTube's), which the site then registers again.

Raising the manifest's `version` alone fixes nothing; renaming the worker alone is worse.

## How we found it

Commands run from the host with `vm/test.sh run '…'` (debug shell, root), on scratch profiles in
`/tmp` and with `/usr/share/owneet/extension` edited in place (saved first, restored after; the
folder must not move, because its path sets the extension's id `jlekhdampjopkpjhbgilolchffjpdjcn`).

1. **A launcher that stops Brave cleanly.** `runuser … timeout -s TERM 25 brave --headless=new
   --user-data-dir=$1 --load-extension=/usr/share/owneet/extension
   --disable-features=DisableLoadExtensionCommandLineSwitch --enable-logging=stderr --log-level=0
   about:blank`. `timeout` goes **inside** `runuser`: when the other way round, runuser prints
   "Session terminated, killing shell... ...killed" and SIGKILLs Brave 2 s after the SIGTERM.
2. **Is the stored script the new one?** Append `// MARKB` to `background.js`, then
   `grep -a -l -r MARKB "$P/Default/Service Worker/"`, and
   `grep -o -E "service_worker_registration_info[^}]*}" $P/Default/Preferences`. The same profile
   was launched with: the change only, the change + `version` 0.1.1, a clean stop, the
   registration info removed, the extension's settings removed → never the marker, and
   `Service Worker/Database/000003.log` keeps the time of the first launch.
3. **Which of the two files holds the settings:** `Default/Preferences` does (`Secure Preferences`
   is 95 bytes and has no `extensions.settings` here).
4. **The fixes on the stuck profile:** worker renamed (`bg2.js`, then `background-0.1.2.js`) →
   new `ScriptCache` entry with the marker; `Default/Service Worker/` deleted → marker present.
5. **Proof by behaviour, not only by the cache:** the test worker gets a top-level
   `connectBridge();` and the page is `about:blank` (no content script, so nothing else starts
   the bridge). Then, 15 s after launch, the parent of each `owneet-bridge`:
   `for p in $(pgrep -f /usr/lib/owneet/owneet-bridge); do tr "\0" " " < /proc/$(ps -o ppid= -p $p | tr -d " ")/cmdline | grep -o "user-data-dir=[^ ]*"; done`.
   Version bump only → no bridge from the test profile; fresh profile (control) → bridge;
   folder deleted → bridge; renamed worker → bridge. A second rename without the line → no
   bridge again, and `ScriptCache` keeps only the newest script.

## Watch out

- Without the package's renaming: assume an extension update reaches the content scripts but
  **not** the worker of existing profiles. When testing a worker change by hand, use a fresh
  profile (headless, step 5 of [[brave-native-messaging-host-not-found]]), or change the worker's
  name **and** the manifest's version.
- **Never rename the worker without a new version** (or the reverse when its code changed): the
  first leaves used profiles without a worker, the second keeps the old code.
- Scripts the worker loads with `importScripts` (none today) are stored with the registration
  too: they need the same renaming.
- A new Brave build may behave differently: repeat step 2 of "How we found it" on a used profile.
