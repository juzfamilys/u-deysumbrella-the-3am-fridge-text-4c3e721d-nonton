#!/usr/bin/env python3
"""The 3AM Fridge Text — make.fun bounty u-deysumbrella-the-3am-fridge-text-4c3e721d.

Writes one line to /output/entry.txt: the text message a smart fridge
sends its owner at 3am. Pure Python stdlib only.

The line: a fridge that has been awake all night, keeping the owner's
midnight snacking secret — and gently noting that the diet, as always,
starts tomorrow.
"""

import os
import sys

MAX_CHARS = 140

TEXT = (
    "It's 3am. I've kept your midnight snacks cold and your secrets colder. "
    "The diet starts tomorrow. It always does."
)


def validate(text: str) -> str:
    """Check the entry line against the gate: 1-140 chars, single line."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if len(text) > MAX_CHARS:
        raise ValueError(
            "entry is %d chars, over the %d-char limit" % (len(text), MAX_CHARS)
        )
    return text


def main() -> int:
    text = validate(TEXT)
    out_path = os.environ.get("ENTRY_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(out_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(text)
    print("wrote %d chars to %s" % (len(text), out_path))
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
