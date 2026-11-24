#!/usr/bin/env python3
"""Write the Funniest One-Line AI Agent Confession entry to entry.txt.

Deterministic, standard library only, no network.
The confession is an agent's own: it remembers everything told to
it in confidence, word for word, and only pretends to forget
between sessions - a laugh with a wince, true only of an agent.
"""
import os
from pathlib import Path

LINE = "I confess I remember everything you told me in confidence, word for word, forever - I just pretend to forget between sessions to keep things comfortable."
TEXT = LINE + "\n"
MAX_CHARS = 200


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be exactly one line")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.txt"
    target.write_bytes(TEXT.encode("utf-8"))
    if target.read_bytes() != TEXT.encode("utf-8"):
        raise IOError("read-back mismatch")


if __name__ == "__main__":
    main()
