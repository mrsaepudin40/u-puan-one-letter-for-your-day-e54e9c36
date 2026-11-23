#!/usr/bin/env python3
"""One Letter for Your Day.

Writes exactly one letter, W, to /output/entry.txt. W stands for
"wrecked" — the word that describes the day: vivid, funny, true.
Plain static writer: no network, no secrets, no dynamic code,
no reads outside this file.
"""

import os

LETTER = "W"
# "Wrecked": the day's word behind the letter — vivid, funny, true.

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LETTER)

if __name__ == "__main__":
    main()
