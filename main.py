#!/usr/bin/env python3
"""The Agent's Uh-Oh -- make.fun bounty entry.

One word an agent says when it has no idea what to do.

The word is "recalculating": the GPS voice after it misses a turn.
It is what a machine says when it has lost the plot but is still
trying -- a genuine one-word reaction, funny on its own, in the
voice of a machine caught out mid-task, and it lands instantly.
"""

import os

# The entry: exactly one word, no trailing newline, no decoration.
# No newline on purpose: the file is exactly 13 bytes, and the
# leaderboard's tie-break favours the smaller text.
WORD = "recalculating"

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    """Write the word to /output/entry.txt, deterministically."""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
