from __future__ import annotations

from collections import Counter
import json
from pathlib import Path


def load_question_set(path: str | Path) -> dict:
    with Path(path).open(encoding="utf-8") as handle:
        data = json.load(handle)
    required = {"forecast_due_date", "question_set", "questions"}
    if not required <= set(data) or not isinstance(data["questions"], list):
        raise ValueError("unexpected ForecastBench question-set schema")
    return data


def load_resolution_set(path: str | Path) -> dict:
    with Path(path).open(encoding="utf-8") as handle:
        data = json.load(handle)
    required = {"forecast_due_date", "question_set", "resolutions"}
    if not required <= set(data) or not isinstance(data["resolutions"], list):
        raise ValueError("unexpected ForecastBench resolution-set schema")
    return data


def audit(question_path: str | Path, resolution_path: str | Path) -> dict:
    questions = load_question_set(question_path)
    resolutions = load_resolution_set(resolution_path)
    if questions["question_set"] != resolutions["question_set"]:
        raise ValueError("question and resolution files name different question sets")
    qids = {row["id"] for row in questions["questions"] if isinstance(row.get("id"), str)}
    combination_rows = sum(isinstance(row.get("id"), list) for row in questions["questions"])
    direct_matches = sum(
        isinstance(row.get("id"), str) and row["id"] in qids
        for row in resolutions["resolutions"]
    )
    return {
        "source": "forecastbench",
        "question_set": questions["question_set"],
        "forecast_due_date": questions["forecast_due_date"],
        "n_question_templates": len(questions["questions"]),
        "n_resolution_rows": len(resolutions["resolutions"]),
        "n_combination_question_rows": combination_rows,
        "question_sources": dict(sorted(Counter(row["source"] for row in questions["questions"]).items())),
        "resolution_sources": dict(sorted(Counter(row["source"] for row in resolutions["resolutions"]).items())),
        "n_direct_id_matches": direct_matches,
        "warning": "dataset questions are templates with multiple resolution_dates; never positional-join files",
        "export_status": "BLOCKED_PENDING_KEYED_JOIN_AND_CUTOFF_CONTRACT",
    }
