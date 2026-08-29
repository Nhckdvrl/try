from __future__ import annotations

from html import unescape
import json
from pathlib import Path
import re


_TAG = re.compile(r"<[^>]+>")
_SPACE = re.compile(r"\s+")


def _plain_html(value: str) -> str:
    value = re.sub(r"<br\s*/?>", "\n", value, flags=re.I)
    value = re.sub(r"</div>", "\n", value, flags=re.I)
    return _SPACE.sub(" ", unescape(_TAG.sub(" ", value))).strip()


def extract_native_scenarios(path: str | Path) -> dict[str, str]:
    with Path(path).open(encoding="utf-8") as handle:
        qsf = json.load(handle)
    scenarios: dict[str, str] = {}
    tags = {
        "bh1988-OB_PhS_Text": "physician_success",
        "bh1988-OB_PhF_Text": "physician_failure",
        "bh1988-OB_PtS_Text": "patient_success",
        "bh1988-OB_PtF_Text": "patient_failure",
    }
    for element in qsf.get("SurveyElements", []):
        payload = element.get("Payload") or {}
        if not isinstance(payload, dict):
            continue
        name = tags.get(payload.get("DataExportTag"))
        if name:
            scenarios[name] = _plain_html(payload["QuestionText"])
    missing = set(tags.values()) - set(scenarios)
    if missing:
        raise ValueError(f"Aiyer QSF missing native scenarios {sorted(missing)}")
    return scenarios


def audit(path: str | Path) -> dict:
    scenarios = extract_native_scenarios(path)
    return {
        "source": "aiyer_2023_outcome_bias",
        "n_native_scenarios": len(scenarios),
        "factor_cells": sorted(scenarios),
        "independent_unit_candidate": "medical bypass vignette (four between-subject cells are one semantic unit)",
        "warning": "one semantic vignette cannot support item-level generalization by itself",
        "export_status": "BLOCKED_PENDING_ALLOWED_RESPONSIVENESS_CONTRACT",
    }
