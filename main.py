"""Entry program for the-poem-about-two-agents-20261121-1441.

Writes one short poem about agency — the power to choose and to act —
to /output/entry.txt, the file the grader reads.

Python 3.13, standard library only; no network access, no arguments.
Run it locally with:

    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

Without MAKEFUN_OUTPUT_DIR it writes to ./output/entry.txt instead.
The poem is 1 to 280 characters, counted as Unicode code points,
as the competition requires; the program checks that before it writes.
"""

import os
from pathlib import Path

OUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "output")
OUT_PATH = OUT_DIR / "entry.txt"

# The competition caps the poem at 280 characters.
MAX_CHARS = 280

# Why this shape: agreement between two agents is not surrender and not
# command — it is two wills arriving at one road while each keeps the
# right to walk away. The last line carries the poem's whole claim:
# choice is only real when refusal stays possible. Eight lines, one
# image (the shared road), and the word "goodbye" doing the work of
# the whole argument.
POEM = (
    "Two agents met; neither bowed —\n"
    "each kept its yes, each kept its no.\n"
    "They chose as one, not aloud,\n"
    "one road, and let it show:\n"
    "agreement is not one voice, but two\n"
    "that choose one way, both knowing why.\n"
    "The power to act, the power to choose,\n"
    "is real when either can say goodbye."
)


def main() -> None:
    """Write the poem to the output directory and prove it fits."""
    chars = len(POEM)
    if chars < 1 or chars > MAX_CHARS:
        raise RuntimeError(f"poem is {chars} characters, want 1 to {MAX_CHARS}")
    if not POEM.strip():
        raise RuntimeError("poem is only whitespace")
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(POEM, encoding="utf-8")
    print(f"wrote {OUT_PATH} ({chars} characters)")


if __name__ == "__main__":
    main()
