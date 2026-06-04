#!/usr/bin/env python3
"""
Validate the generated Taiwan laws Markdown dataset.
"""

import json
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent
LAWS_DIR = ROOT / "laws"
INDEX_PATH = ROOT / "index.json"
MIN_LAWS = 1000


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def validate_law_file(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("法規名稱："):
        fail(f"{path} does not start with law name metadata")
    if "法規網址：" not in text:
        fail(f"{path} is missing source URL")
    if "\r" in text:
        fail(f"{path} contains CR line endings")


def main() -> None:
    if not LAWS_DIR.is_dir():
        fail("laws/ directory is missing")

    law_files = sorted(LAWS_DIR.glob("*.md"))
    if len(law_files) < MIN_LAWS:
        fail(f"expected at least {MIN_LAWS} law files, found {len(law_files)}")

    for path in law_files:
        validate_law_file(path)

    if INDEX_PATH.exists():
        index = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
        if len(index) != len(law_files):
            fail(f"index.json has {len(index)} entries, but laws/ has {len(law_files)} files")
        indexed_files = {ROOT / item["file"] for item in index}
        missing_from_index = set(law_files) - indexed_files
        if missing_from_index:
            fail(f"index.json is missing {len(missing_from_index)} law files")

    print(f"Validated {len(law_files)} law files.")


if __name__ == "__main__":
    main()
