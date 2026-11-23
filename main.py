#!/usr/bin/env python3
"""One Line, Zero Use: write one original useless-superpower line."""

LINE = "I can read minds, but only the minds of pigeons, and they're all judging my shoes."


def main() -> None:
    # Gate pre-check: entry must be 1-200 chars, not only whitespace.
    if not 1 <= len(LINE) <= 200 or not LINE.strip():
        raise ValueError("line must be 1-200 non-blank characters")
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
