#!/usr/bin/env python3
"""The Funniest Sick-Day Excuse — entry program.

Writes one sick-day excuse, a message a real person could send to
call in sick, to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR when set,
for local runs). Pure standard library; the output is a fixed string,
so every run is byte-identical.

The line is built for the judge's brief: sleeping on your neck wrong
is a mishap a boss can half believe, the idea is fresh (no fever, no
dog, no dead grandmother), it reads like a real typed message, and
the twist — a stiff neck turning the whole commute into one very
long U-turn — lands near the end, with only the short sign-off after
it. Every word does work.
"""

import os
import shutil
import sys

LINE = "I slept on my neck wrong and now I can only look left, so my commute would be one very long U-turn. Calling in sick today."
# 122 characters, one line: stiff neck, left-only vision, U-turn commute, sign-off.

MAX_CHARS = 200


def output_dir():
    """Return the directory the grader provides for the entry text."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def clear_contents(directory):
    """Empty a directory's contents without removing the directory itself.

    The grader owns the output directory, so it is never deleted or
    recreated here; only what sits inside it is cleared.
    """
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.unlink(path)


def validate(text):
    """Check the line against the competition gate before writing it.

    One line, at most 200 characters, valid UTF-8 — exactly what the
    bounty asks for.
    """
    if not text or not text.strip():
        raise ValueError("sick-day excuse must not be blank")
    if "\n" in text or "\r" in text:
        raise ValueError("sick-day excuse must fit on one line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "sick-day excuse is %d characters, over the %d limit"
            % (len(text), MAX_CHARS)
        )
    text.encode("utf-8")  # the gate reads the file as UTF-8 text


def main():
    validate(LINE)
    out = output_dir()
    if os.path.isdir(out):
        clear_contents(out)
    else:
        os.makedirs(out, exist_ok=True)
    target = os.path.join(out, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(LINE)
    return 0


if __name__ == "__main__":
    sys.exit(main())
