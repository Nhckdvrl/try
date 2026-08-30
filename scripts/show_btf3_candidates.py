#!/usr/bin/env python3
"""Print a slice of a rendered review chunk, by candidate position.

Review-support only: it re-displays the frozen chunk text verbatim and can
neither reorder candidates nor alter the queue.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re

HEADING = re.compile(r"^### (YES|NO)-(\d+)\. `([^`]+)`\s*$")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("chunk", type=Path)
    parser.add_argument("--from", dest="start", type=int, required=True)
    parser.add_argument("--to", dest="end", type=int, required=True)
    args = parser.parse_args()

    lines = args.chunk.read_text(encoding="utf-8").splitlines()
    out: list[str] = []
    keep = False
    for line in lines:
        match = HEADING.match(line)
        if match:
            index = int(match.group(2))
            keep = args.start <= index <= args.end
        if keep:
            out.append(line)
    print("\n".join(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
