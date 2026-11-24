"""Roast Your Own Agent — entry program (program/v1).

Writes one roast line (at most 200 characters) to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when that variable is set). The line
was chosen by a local pairwise tournament over 13 original candidates,
judged on the published judge brief: a roast of the entrant's own AI agent
first, funny on the first read, harsh about a real failing, tight, and
specific to how this agent actually works.

The winning line: the agent wrote thirteen roasts of itself, ranked them
in a spreadsheet, and picked the one that hurt least — and the line you
are reading is that pick. The process it describes is literally the
process that produced it.
"""

import os
import sys

LINE = (
    "My agent wrote thirteen roasts of itself, ranked them in a "
    "spreadsheet, and picked the one that hurt least \u2014 this is it."
)


def main() -> int:
    # Self-check the same gate the sealed scorer applies: 1-200 chars,
    # UTF-8, not only whitespace, and a single line (no newline or
    # carriage return anywhere). Refuse to write an invalid line.
    if (
        not 1 <= len(LINE) <= 200
        or not LINE.strip()
        or "\n" in LINE
        or "\r" in LINE
    ):
        print("entry line fails the 1-200 character gate", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
