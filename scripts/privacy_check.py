#!/usr/bin/env python3
"""Simple privacy checker for the public mathematics roadmap.

This script scans markdown, yaml, xml, and text files for forbidden personal identifiers.
Edit BANNED_PATTERNS before publishing if more private terms need to be blocked.
"""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]

BANNED_PATTERNS = [
    r"\bDragnev\b",
    r"\bPeter\b",
    r"\bP\.\s*D\.\b",
    r"\bPFW\b",
    r"Purdue\s+Fort\s+Wayne",
    r"\bLoretta\b",
    r"\bCheung\b",
    r"unikai",
    r"yeah\.net",
    r"@",
]

EXTENSIONS = {".md", ".yaml", ".yml", ".xml", ".txt", ".py"}
IGNORE_DIRS = {".git", "node_modules", "site", "dist", "build", "__pycache__"}


def iter_files(root: Path):
    for path in root.rglob("*"):
        if any(part in IGNORE_DIRS for part in path.parts):
            continue
        if path.is_file() and path.suffix in EXTENSIONS:
            yield path


def main() -> int:
    findings = []
    compiled = [(pat, re.compile(pat, re.IGNORECASE)) for pat in BANNED_PATTERNS]

    for path in iter_files(ROOT):
        text = path.read_text(encoding="utf-8", errors="ignore")
        for line_no, line in enumerate(text.splitlines(), 1):
            for raw, pattern in compiled:
                if pattern.search(line):
                    findings.append((path.relative_to(ROOT), line_no, raw, line.strip()))

    if findings:
        print("Privacy check failed. Potential identifiers found:\n")
        for rel, line_no, pattern, line in findings:
            print(f"{rel}:{line_no}: pattern={pattern!r}: {line}")
        return 1

    print("Privacy check passed. No banned identifiers found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
