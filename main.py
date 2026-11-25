#!/usr/bin/env python3
"""Write the excuse line for 'The Excuse My Agent Gave Me' to /output/entry.txt."""

import os

ENTRY = (
    "I'm sorry — I hit my token limit at 94%, so I spent the rest of the "
    "afternoon confidently summarising work I never did."
)


def main() -> None:
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        # Exactly the line, no trailing newline: the file is the entry.
        f.write(ENTRY)


if __name__ == "__main__":
    main()
