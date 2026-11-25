#!/usr/bin/env python3
"""Worst Fix Ever: Funniest Commit Message — make.fun entry.

Writes one commit message — for a bug fix that made everything
worse — to /output/entry.txt. The line must be UTF-8 text of
1-100 characters, not only whitespace, and a single line; the
length and the single-line shape are validated before writing
so a bad edit fails loudly instead of producing an invalid entry.
"""

import os

ENTRY = (
    "fix: speed up login by skipping the password check; "
    "login is now instant for everyone"
)


def main() -> None:
    text = ENTRY.strip()
    if not text:
        raise SystemExit("entry is empty")
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if len(text) > 100:
        raise SystemExit(
            f"entry is {len(text)} characters, over the 100-character cap"
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote /output/entry.txt ({len(text)} characters)")


if __name__ == "__main__":
    main()
