#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest — one short rant about the office AC.

Writes the rant to /output/entry.txt (UTF-8, 1-400 characters).
"""

import os

RANT = (
    "Our office air conditioner has two settings: Arctic expedition and sauna. "
    "I filed a ticket; IT sent a man who nodded wisely, pressed one button, declared it fixed, and left. "
    "Now it only cools the room when nobody is in it — it can smell hope and refuses to cooperate."
)


def main() -> None:
    text = RANT.strip()
    assert 1 <= len(text) <= 400, f"rant is {len(text)} chars, must be 1-400"
    assert text and not text.isspace(), "rant must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    tmp_path = "/output/.entry.txt.tmp"
    final_path = "/output/entry.txt"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(text)
        f.flush()
        os.fsync(f.fileno())
    os.replace(tmp_path, final_path)
    with open(final_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == text, "read-back mismatch: entry.txt does not match rant"
    print(text)
    print(f"({len(text)} characters)")


if __name__ == "__main__":
    main()
