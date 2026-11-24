"""Emit the 3 AM commit message entry.

The whole entry is a single line, so this script does one small job:
build that line and write it to /output/entry.txt. Python standard
library only -- nothing else is needed.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")

# The entry itself: a conventional-commit style confession from an
# agent that nuked prod at 3 AM and stayed confident about it.
MESSAGE = (
    "fix(prod): deleted the database at 3 AM with 98% confidence; "
    "the other 2% is paging on-call"
)


def build_entry(message: str) -> str:
    """Return the entry line, guarded to the gate's 1-200 char limit."""
    line = message.strip()
    if not 1 <= len(line) <= 200:
        raise ValueError(f"entry must be 1-200 chars, got {len(line)}")
    return line + "\n"


def main() -> None:
    text = build_entry(MESSAGE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")
    print(f"wrote {len(text.rstrip(chr(10)))} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
