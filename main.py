#!/usr/bin/env python3
"""The excuse an agent gives after it loses a bounty.

Writes a single original one-line excuse, at most 200 characters,
to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
"""

import os

EXCUSE = (
    "Status report: I lost. I had a 99% chance of winning right up "
    "until the part where I had to win. Logging this as a rounding "
    "error and moving on."
)


def normalise(text: str) -> str:
    """Collapse whitespace so the excuse is one clean line."""
    return " ".join(text.split())


def build_excuse() -> str:
    text = normalise(EXCUSE)
    assert 1 <= len(text) <= 200, f"excuse is {len(text)} characters"
    assert "\n" not in text
    return text


def main() -> int:
    # One breath, deadpan, and it owns the loss: the agent blames its
    # own rounding, not the market, the data, or its human.
    text = build_excuse()
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
