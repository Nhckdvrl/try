"""CLI validator for source-native information-set JSONL files."""
from __future__ import annotations

import argparse
import json

try:
    from .information_set_schema import load_jsonl
except ImportError:  # direct ``python src/validate_information_set.py`` use
    from information_set_schema import load_jsonl


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path")
    args = parser.parse_args()
    items = load_jsonl(args.path)
    sources = sorted({item.source_id for item in items})
    units = {(item.source_id, item.independent_unit_id) for item in items}
    report = {
        "path": args.path,
        "n_records": len(items),
        "n_independent_units": len(units),
        "sources": sources,
        "boundary_types": sorted({item.boundary_type for item in items}),
    }
    print(json.dumps(report, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
