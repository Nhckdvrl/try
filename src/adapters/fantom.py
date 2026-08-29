from __future__ import annotations

from collections import Counter
import json
from pathlib import Path


def load_native(path: str | Path) -> list[dict]:
    with Path(path).open(encoding="utf-8") as handle:
        rows = json.load(handle)
    if not isinstance(rows, list):
        raise ValueError("FANToM v1 must be a JSON list")
    required = {
        "set_id", "part_id", "conv_id", "full_context", "short_context",
        "missed_info", "joining_speaker", "factQA", "beliefQAs",
    }
    for index, row in enumerate(rows):
        missing = required - set(row)
        if missing:
            raise ValueError(f"FANToM row {index} missing {sorted(missing)}")
    return rows


def audit(path: str | Path) -> dict:
    rows = load_native(path)
    qtypes = Counter()
    accessibility = Counter()
    belief_questions = 0
    for row in rows:
        for qa in row["beliefQAs"]:
            belief_questions += 1
            qtypes[qa.get("tom_type", "missing")] += 1
            accessibility[qa.get("missed_info_accessibility", "missing")] += 1
    return {
        "source": "fantom_v1",
        "n_rows": len(rows),
        "n_set_ids": len({row["set_id"] for row in rows}),
        "n_part_ids": len({row["part_id"] for row in rows}),
        "n_conversations": len({row["conv_id"] for row in rows}),
        "n_belief_questions": belief_questions,
        "belief_tom_types": dict(sorted(qtypes.items())),
        "belief_accessibility": dict(sorted(accessibility.items())),
        "independent_unit_candidate": "part_id (multiple conversation/context renderings share a part)",
        "export_status": "BLOCKED_PENDING_TRANSFORMATION_CONTRACT",
    }
