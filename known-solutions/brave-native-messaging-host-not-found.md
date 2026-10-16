---
type: known-solution
description: "Brave never starts owneet-bridge: the native-messaging manifest in the web app's profile is ignored. Also the step-by-step path to see Brave's hidden errors."
status: solved
seen: 2026-10-16
updated: 2026-10-16
tags: [known-solution, brave, extension, owneet-bridge]
---
# Brave does not find the native-messaging host

## Symptom

- Inside a web app the extension works (the ring moves, A presses), but A on a text field opens
  no keyboard and B on the first page asks nothing.
- No `owneet-bridge` process; owneetd's events never show `webapp.keyboard` or
  `webapp.ask_close`.
- **Nothing in the journal:** no bridge line, no Brave error.
- The extension's own error (only visible with the trick below):
  `Specified native messaging host not found.`

## Cause

owneetd wrote the host's manifest into each web app's profile (`<--user-data-dir>/NativeMessagingHosts/`).
**Brave does not read hosts from a profile chosen with `--user-data-dir`.** It looks in the
system folder `/etc/opt/chrome/native-messaging-hosts/` (tested). The binary also contains
`/etc/chromium/native-messaging-hosts` (not tested).

Hard to see because nothing is logged: Brave writes only `ERROR` lines to the journal, and its
"Can't find manifest" line is a `WARNING`. The reason goes to the extension only, as
`chrome.runtime.lastError`.

## Solution

One static manifest installed system-wide by the owneetd package (0.12.1):
`/etc/opt/chrome/native-messaging-hosts/org.owneet.bridge.json`. owneetd no longer writes
anything into the profiles. The test `TestManifestAllowsOnlyTheConsolesExtension`
(`daemon/cmd/owneet-bridge/`) recomputes the extension's id from its folder and checks the file.
Decision: [[decision-log]] 2026-10-16, [[extension-design]].

## How we found it

Commands run from the host with `vm/test.sh run '…'` (debug shell, root). Each step cut the
problem in half.

1. **The bridge on its own.** Feed it one native message by hand: a 4-byte length (`0x10` = 16)
   then the JSON. Expected answer: a `look` message.
   `{ printf "\x10\x00\x00\x00{\"type\":\"hello\"}"; sleep 2; } | timeout 5 runuser -u owneet -- env XDG_RUNTIME_DIR=/run/user/1000 /usr/lib/owneet/owneet-bridge | od -c`
   → it worked: the fault is between Brave and the bridge.
2. **What reaches the journal.** `journalctl -b --no-pager | grep -o -E ":(INFO|WARNING|ERROR):|CONSOLE" | sort | uniq -c`
   → only `ERROR`: warnings and `console.*` are lost, so silence proves nothing.
3. **The extension's permissions and worker,** from the profile's `Default/Preferences`:
   `grep -o -E "\"(active|granted)_permissions\":\{[^}]*\}" …/Default/Preferences` and
   `grep -o -E "service_worker_registration_info[^}]*}" …/Default/Preferences`
   → `nativeMessaging` granted, worker registered.
4. **Make the worker tell its error.** Give the extension the `storage` permission and write
   `chrome.runtime.lastError` with `chrome.storage.local.set(…)` (edited with `sed` in the VM
   only, original saved first). Read it back from the LevelDB files:
   `grep -a -o -r "owneet_[a-z]*.\{0,100\}" "…/Default/Local Extension Settings/" | cat -v`.
   An existing profile kept running its old cached worker:
   [[brave-extension-worker-cached]].
5. **Brave with full logging, fresh profile, no screen:**
   `timeout 30 runuser -u owneet -- env XDG_RUNTIME_DIR=/run/user/1000 brave --headless=new --user-data-dir=/tmp/yt --load-extension=/usr/share/owneet/extension --disable-features=DisableLoadExtensionCommandLineSwitch --enable-logging=stderr --log-level=0 https://example.com > /root/brave.log 2>&1`
   → `WARNING:…launch_context.cc… Can't find manifest for native messaging host org.owneet.bridge`.
6. **Where Brave looks:** the folders are compiled into the binary:
   `grep -a -o -E "/etc/[A-Za-z0-9/._-]*native-messaging-hosts" /opt/brave-bin/brave | sort -u`.
7. **Proof:** the manifest copied into `/etc/opt/chrome/native-messaging-hosts/`, step 5 run again
   with a profile without one → no warning, one `connectNative` attempt and no error (the port
   stays open).

Step 5 is the fastest start for any "the extension does nothing" problem: a fresh profile rules
out caches, and the log shows what Brave hides in the console session.

## Watch out

- **The extension's folder fixes its id.** If `/usr/share/owneet/extension` moves, the id
  changes; the test above fails until the manifest is updated.
- **A new Brave build may look elsewhere:** repeat step 6, then step 7.
- pacman refuses to install a file that already exists unowned: remove any manifest copied by
  hand before installing owneetd.
