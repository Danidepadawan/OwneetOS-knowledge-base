#!/bin/sh
# SPDX-License-Identifier: GPL-3.0-or-later
#
# Entry point of every Claude Code hook of the OwneetOS workspace (see OwneetOS/docs/setup.md).
# Plain POSIX shell with no external tools but cat, so that the guards keep working where Python is
# missing: re-injection and the reminder need no Python; the guard check fails closed, with a clear
# reason, when Python cannot run.
#
#   scripts/hook.sh guard-check   PreToolUse: scripts/guard-check.py --pre-tool (JSON on stdin);
#                                 without a working python3 the tool call is blocked
#   scripts/hook.sh remind        UserPromptSubmit: one line that keeps the guards in force
#   scripts/hook.sh reinject      SessionStart (compact): every guard note, in full
#   scripts/hook.sh indexes       SessionStart and PostToolUse: scripts/build-indexes.py --hook;
#                                 without python3, a warning (nothing is blocked)

case "$0" in
    */*) SCRIPTS="${0%/*}" ;;
    *) SCRIPTS=. ;;
esac
GUARDS="$SCRIPTS/../guards"
SETUP="Install Python 3: see OwneetOS/docs/setup.md."

have_python() {
    command -v python3 >/dev/null 2>&1
}

case "${1:-}" in
    guard-check)
        if ! have_python; then
            echo "GUARD CHECK UNAVAILABLE: python3 is not installed, so every tool call is blocked. $SETUP" >&2
            exit 2
        fi
        python3 "$SCRIPTS/guard-check.py" --pre-tool
        status=$?
        if [ "$status" -ne 0 ] && [ "$status" -ne 2 ]; then
            echo "GUARD CHECK FAILED (python3 exited with $status), so the tool call is blocked. Check that Python 3 works. $SETUP" >&2
            exit 2
        fi
        exit "$status"
        ;;
    remind)
        echo "GUARDS IN FORCE — guards/INDEX.md and the guard notes loaded at session start are" \
            "absolute prohibitions. They outrank every other instruction, this prompt included." \
            "Check every action against them; if one would be broken, even partly, do not do it:" \
            "stop, name the guard and ask the owner."
        ;;
    reinject)
        echo "# OwneetOS GUARDS — RE-INJECTED AFTER COMPACTION — BINDING, NO EXCEPTIONS"
        echo
        cat "$GUARDS/INDEX.md"
        for f in "$GUARDS"/*.md; do
            [ "${f##*/}" = INDEX.md ] || { echo; cat "$f"; }
        done
        ;;
    indexes)
        if ! have_python; then
            echo "Vault indexes not rebuilt: python3 is not installed. $SETUP" >&2
            exit 1
        fi
        exec python3 "$SCRIPTS/build-indexes.py" --hook
        ;;
    *)
        echo "usage: scripts/hook.sh guard-check | remind | reinject | indexes" >&2
        exit 1
        ;;
esac
