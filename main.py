#!/usr/bin/env python3
"""One Star for Monday — writes a one-star review of Monday,
written as though Monday were a restaurant, to entry.txt.

Python standard library only. Deterministic: the same line is
written on every run.
"""

import os

# One line, 25 words, plain text. Table, server, dish and bill all
# went wrong — and the bill charged for a weekend never ordered,
# which only Monday could do.
LINE = (
    "Booked a table, waited an hour, server vanished, food came cold, "
    "and the bill charged me for a weekend I never ordered. "
    "Never again, Monday."
)


def main() -> None:
    # The grader mounts the repo read-only, so the only file this
    # program ever writes is entry.txt under MAKEFUN_OUTPUT_DIR.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
