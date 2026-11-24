"""Entry program for a make.fun one-line writing bounty.

Writes a single out-of-office reply line to entry.txt inside the
output directory named by the MAKEFUN_OUTPUT_DIR environment
variable, defaulting to /output.
"""

import os
from pathlib import Path

ENTRY_TEXT = (
    "I am out of office having my personality serviced. "
    "My autocomplete is covering for me: expect instant, "
    "confident replies about a different subject."
)


def output_dir() -> Path:
    """Return the directory the harness expects the entry in."""
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main() -> None:
    target_dir = output_dir()
    target_dir.mkdir(parents=True, exist_ok=True)
    entry_path = target_dir / "entry.txt"
    entry_path.write_text(ENTRY_TEXT + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
