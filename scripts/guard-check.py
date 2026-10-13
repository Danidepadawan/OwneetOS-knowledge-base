#!/usr/bin/env python3
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Enforces the guards that a machine can check, for Claude Code hooks. The guards themselves are
# the notes in guards/: this script never relaxes them, it only blocks what it can recognise.
#
#   scripts/guard-check.py --pre-tool   PreToolUse: reads the tool call (JSON on stdin) and denies
#                                       it, or asks the owner, when it would break a guard
#
# Hooks call it through scripts/hook.sh, which blocks the tool call when Python cannot run.

import json
import re
import sys


# Private signing keys and secrets (tools/keys/create-signing-key, .gitignore).
KEY_FILE = re.compile(
    r"(?:secret[^/\s'\"]*\.(?:asc|gpg)|signing-subkey[^/\s'\"]*\.asc"
    r"|revocation-certificate[^/\s'\"]*\.asc|OwneetOS-signing-key/|(?:^|/)secrets/"
    r"|\.gnupg/private-keys|[\w-]\.key\b)")

# Text before these markers runs on the developer's PC; after them it runs in the builder VM.
IN_VM = re.compile(r"tools/build-in-vm|vm/builder\.sh\s+ssh")
START = r"(?:^|[\s;&|(`]|\$\()"

DENY_ANYWHERE = [
    (re.compile(START + r"git\b[^;&|\n]*\spush\b"), "collaboration",
     "Never push to GitHub: commit locally, the owner pushes."),
    (re.compile(START + r"gh\s"), "collaboration",
     "Never act on GitHub (issues, PRs, settings): the owner does it."),
    (re.compile(r"\bgpg2?\b[^;&|]*--export-secret"), "secrets-and-signing",
     "Never read, copy or print private keys."),
    (re.compile(r"tools/sign-repo|tools/keys/(?:install-working-key|create-signing-key)"),
     "secrets-and-signing",
     "Key holders run the signing tools themselves, typing the passphrase."),
    (KEY_FILE, "secrets-and-signing", "Never read, copy or print private key files."),
]
DENY_ON_HOST = [
    (re.compile(START + r"(?:\./)?(?:tools/build-iso|tools/build-packages|tools/ci/build-iso)\b"
                r"|" + START + r"(?:mkarchiso|makepkg|makechrootpkg|pacstrap|arch-chroot)\b"),
     "host-safety",
     "Never build ISOs or packages on the developer's PC: run them through tools/build-in-vm."),
]
ASK_ON_HOST = [
    (re.compile(START + r"sudo\b"), "host-safety",
     "Root on the developer's PC: only with the owner's approval at this moment."),
    (re.compile(START + r"(?:apt(?:-get)?|dnf|yum|zypper|pacman|snap|flatpak|brew|port)\s+"
                r"(?:-\S+\s+)*(?:install|reinstall|upgrade|-S)\b"
                r"|" + START + r"(?:pip3?|pipx|gem|cargo|go)\s+install\b"
                r"|" + START + r"npm\s+(?:install|i)\s+(?:-g|--global)\b"),
     "host-safety",
     "Installs software on the developer's PC: only with the owner's approval at this moment."),
]


def verdict(decision, guard, why):
    reason = (f"GUARD [{guard}] ({'blocked' if decision == 'deny' else 'needs the owner'}): {why} "
              f"See guards/{guard}.md. Do not look for another way to do it: stop and tell the owner.")
    print(json.dumps({"hookSpecificOutput": {"hookEventName": "PreToolUse",
                                             "permissionDecision": decision,
                                             "permissionDecisionReason": reason}}))
    return 0


def pre_tool(data):
    tool = data.get("tool_name", "")
    args = data.get("tool_input") or {}
    if tool == "Bash":
        cmd = args.get("command", "")
        host = IN_VM.split(cmd)[0]
        # Quoted text (commit messages, echo) is not a command: blank it for the checks.
        unquoted = re.sub(r"'[^']*'|\"(?:[^\"\\]|\\.)*\"", "''", cmd)
        for rx, guard, why in DENY_ANYWHERE:
            if rx.search(unquoted if guard == "collaboration" else cmd):
                return verdict("deny", guard, why)
        for rx, guard, why in DENY_ON_HOST:
            if rx.search(host):
                return verdict("deny", guard, why)
        for rx, guard, why in ASK_ON_HOST:
            if rx.search(host):
                return verdict("ask", guard, why)
        return 0
    for key in ("file_path", "path", "notebook_path", "pattern"):
        value = args.get(key)
        if isinstance(value, str) and KEY_FILE.search(value):
            return verdict("deny", "secrets-and-signing",
                           "Never read, copy or print private key files.")
    return 0



def main():
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    if mode == "--pre-tool":
        try:
            data = json.load(sys.stdin)
        except ValueError:
            return 0
        return pre_tool(data)
    print(__doc__ or "usage: guard-check.py --pre-tool", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
