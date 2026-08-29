"""Run schema-only audits on the pinned first-wave external sources."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

from adapters import aiyer, btf3, fantom, forecastbench


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-root", default="data/external/raw")
    parser.add_argument("--output")
    args = parser.parse_args()
    root = Path(args.raw_root)
    report = {
        "fantom": fantom.audit(root / "fantom/fantom_v1.json"),
        "forecastbench": forecastbench.audit(
            root / "forecastbench/2025-03-02-llm.json",
            root / "forecastbench/2025-03-02_resolution_set.json",
        ),
        "btf3": btf3.audit(
            root / "btf3/btf3_binary_questions_and_forecasts.parquet",
            root / "btf3/btf3_numeric_questions_and_forecasts.parquet",
        ),
        "aiyer": aiyer.audit(root / "aiyer/outcome_bias.qsf"),
    }
    rendered = json.dumps(report, indent=2, sort_keys=True)
    print(rendered)
    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
