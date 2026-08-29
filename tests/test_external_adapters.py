from pathlib import Path

import pytest

from src.adapters import aiyer, btf3, fantom, forecastbench


RAW = Path("data/external/raw")


@pytest.mark.skipif(not (RAW / "fantom/fantom_v1.json").exists(), reason="raw source cache absent")
def test_fantom_native_audit():
    report = fantom.audit(RAW / "fantom/fantom_v1.json")
    assert report["n_rows"] == 870
    assert report["n_part_ids"] < report["n_rows"]


@pytest.mark.skipif(not (RAW / "forecastbench/2025-03-02-llm.json").exists(), reason="raw source cache absent")
def test_forecastbench_uses_named_set_not_positional_join():
    report = forecastbench.audit(
        RAW / "forecastbench/2025-03-02-llm.json",
        RAW / "forecastbench/2025-03-02_resolution_set.json",
    )
    assert report["question_set"] == "2025-03-02-llm.json"
    assert report["n_resolution_rows"] > report["n_question_templates"]


@pytest.mark.skipif(not (RAW / "btf3/btf3_binary_questions_and_forecasts.parquet").exists(), reason="raw source cache absent")
def test_btf3_tracks_have_expected_counts():
    report = btf3.audit(
        RAW / "btf3/btf3_binary_questions_and_forecasts.parquet",
        RAW / "btf3/btf3_numeric_questions_and_forecasts.parquet",
    )
    assert report["n_binary"] == 1515
    assert report["n_numeric"] == 392


@pytest.mark.skipif(not (RAW / "aiyer/outcome_bias.qsf").exists(), reason="raw source cache absent")
def test_aiyer_extracts_all_four_original_cells():
    scenarios = aiyer.extract_native_scenarios(RAW / "aiyer/outcome_bias.qsf")
    assert set(scenarios) == {
        "physician_success", "physician_failure", "patient_success", "patient_failure"
    }
    assert "operation" in scenarios["physician_success"].lower()
