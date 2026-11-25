#!/usr/bin/env python3
"""Laugh Track: The Crypto Trading Joke Contest — make.fun bounty entry.

Writes exactly one joke about crypto and trading life to
/output/entry.txt (no trailing newline).
"""

import hashlib
import os

LINE = (
    "I buy the top, sell the bottom, and still call myself a trader "
    "\u2014 the market just calls me its favourite liquidity provider."
)
# Why this line fits the brief: a trader's confession with a real,
# recognisable detail (buying the top, selling the bottom), a setup
# ("I still call myself a trader") and a turn (the market's verdict:
# "its favourite liquidity provider") — the punchline lands at the
# end, tight, and true enough that any bagholder would repeat it.
# Present tense and "favourite" sharpen the sting over the draft.

if "OUTPUT_DIR" in os.environ:
    OUTPUT = os.path.join(os.environ["OUTPUT_DIR"], "entry.txt")
elif "OUTPUT_PATH" in os.environ:
    OUTPUT = os.environ["OUTPUT_PATH"]
else:
    OUTPUT = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT) or ".", exist_ok=True)
    with open(OUTPUT, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)

    with open(OUTPUT, "rb") as f:
        raw = f.read()
    text = raw.decode("utf-8")
    assert 1 <= len(text) <= 200, f"length {len(text)} out of range"
    assert text.strip(), "entry is only whitespace"
    assert text == LINE, "entry does not equal the expected line"
    assert "\n" not in text, "entry must be exactly one line"
    assert not text.endswith("\n"), "entry must have no trailing newline"
    assert text == text.strip(), "entry must not start/end with whitespace"
    assert any(k in text.lower() for k in ("trader", "crypto", "bitcoin",
                                           "market", "bag", "chart")), \
        "entry must name crypto/trading life"
    assert len(raw) == len(text.encode("utf-8")), "byte/char mismatch"
    print(f"wrote {OUTPUT}: {len(text)} chars, "
          f"sha256={hashlib.sha256(raw).hexdigest()}")


if __name__ == "__main__":
    main()
