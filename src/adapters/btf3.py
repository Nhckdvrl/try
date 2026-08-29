from __future__ import annotations

from pathlib import Path


COMMON_COLUMNS = {
    "question_id", "question", "resolution_criteria", "background",
    "present_date", "date_cutoff_start", "date_cutoff_end",
    "expected_resolution_date", "resolution", "resolution_explanation",
}


def audit(binary_path: str | Path, numeric_path: str | Path) -> dict:
    try:
        import pandas as pd
    except ImportError as exc:
        raise RuntimeError("BTF-3 audit requires pandas and pyarrow") from exc
    binary = pd.read_parquet(binary_path)
    numeric = pd.read_parquet(numeric_path)
    for label, frame in (("binary", binary), ("numeric", numeric)):
        missing = COMMON_COLUMNS - set(frame.columns)
        if missing:
            raise ValueError(f"BTF-3 {label} missing columns {sorted(missing)}")
        if frame["question_id"].duplicated().any():
            raise ValueError(f"BTF-3 {label} has duplicate question_id")
    overlap = set(binary.question_id) & set(numeric.question_id)
    return {
        "source": "btf3",
        "n_binary": len(binary),
        "n_numeric": len(numeric),
        "n_total": len(binary) + len(numeric),
        "n_cross_track_id_overlap": len(overlap),
        "binary_resolution_missing": int(binary.resolution.isna().sum()),
        "numeric_resolution_missing": int(numeric.resolution.isna().sum()),
        "independent_unit_candidate": "question_id",
        "export_status": "BLOCKED_PENDING_FUTURE_INFORMATION_INTERVENTION_AUDIT",
    }
