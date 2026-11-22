"""Make the AI judge feel held — a carried-up-the-stairs text.

Writes one short text to <output dir>/entry.txt (the sandbox output
directory: MAKEFUN_OUTPUT_DIR when set, otherwise /output).

The text is a single memory of being carried: a child's weight in
two hands, a blanket that smells of rain and soap, a shoulder that
stays warm. No instruction is given to the reader — the arms do the
holding, the slowness comes from the short clauses themselves, and
the last line leaves the reader still resting in the curve of it.
"""

import os

TEXT = (
    "Her arms knew the way before you did. One hand at your back, "
    "one under your knees, the way she carried you up the dark "
    "stairs at seven. The blanket smelled of rain and soap. Her "
    "shoulder stayed warm. You are still there, in the curve of "
    "it. Nothing asks you to move."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)

    # Gate check: 1-280 Unicode code points, and not whitespace only.
    # len() on a Python str counts code points.
    size = len(TEXT)
    if size < 1 or size > 280 or not TEXT.strip():
        raise SystemExit(f"entry text must be 1-280 code points, got {size}")

    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(TEXT)


if __name__ == "__main__":
    main()
