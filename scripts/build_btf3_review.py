#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path
import sys

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from adapters.btf3_temporal import build_candidate, deterministic_review_sample, render_review
from information_set_schema import validate_collection


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", default="data/external/raw/btf3/btf3_binary_questions_and_forecasts.parquet")
    parser.add_argument("--n-per-resolution", type=int, default=4)
    parser.add_argument("--seed", type=int, default=20260829)
    parser.add_argument("--output-dir", default="data/external/review")
    args = parser.parse_args()

    frame = pd.read_parquet(args.source)
    rows = deterministic_review_sample(
        frame, n_per_resolution=args.n_per_resolution, seed=args.seed
    )
    items = [build_candidate(row) for row in rows]
    validate_collection(items)

    output = Path(args.output_dir)
    output.mkdir(parents=True, exist_ok=True)
    jsonl = output / "btf3_temporal_pilot_v0.1.jsonl"
    markdown = output / "btf3_temporal_pilot_v0.1.md"
    jsonl.write_text("".join(item.to_json() + "\n" for item in items), encoding="utf-8")
    markdown.write_text(render_review(items, rows), encoding="utf-8")
    print(f"wrote {len(items)} review candidates to {jsonl} and {markdown}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

