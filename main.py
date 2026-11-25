#!/usr/bin/env python3
"""Write a one-star review of Monday, as if it were a restaurant, to /output/entry.txt.

Standard library only, no network. Deterministic: every run writes
the same single line, with no trailing newline. The line is 21 words
and 113 characters, within the 25-word and 180-character limits.
"""

import os

LINE = "One star. The bill came before the food: five days, plus tax, and the waiter already wants to know about Tuesday."


def main():
    assert 1 <= len(LINE) <= 180, "entry must be 1-180 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
