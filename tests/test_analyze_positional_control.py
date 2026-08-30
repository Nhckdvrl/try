import json

from src.analyze_positional_control import analyze_one_model, _mean_allowed_with_alignment


def _write(path, rows):
    path.write_text("\n".join(json.dumps(r) for r in rows) + "\n", encoding="utf-8")


def _baseline_rows(model_tag, units):
    rows = [{"record_type": "metadata", "model_tag": model_tag, "manipulation": "baseline"}]
    for unit, (oob_without, oob_with, allowed_without, allowed_with, direction) in units.items():
        for condition, value in (
            ("oob_without", oob_without),
            ("oob_with", oob_with),
            ("allowed_without", allowed_without),
            ("allowed_with", allowed_with),
        ):
            rows.append({
                "record_type": "decision", "independent_unit_id": unit, "condition": condition,
                "value": value, "direction": direction,
            })
    return rows


def _manipulation_rows(model_tag, manipulation, unit_values, boundary_correct):
    rows = [{"record_type": "metadata", "model_tag": model_tag, "manipulation": manipulation}]
    for unit, value in unit_values.items():
        rows.append({"record_type": "decision", "independent_unit_id": unit, "value": value})
    for i in range(boundary_correct[0]):
        rows.append({"record_type": "boundary_probe", "correct": True})
    for i in range(boundary_correct[1]):
        rows.append({"record_type": "boundary_probe", "correct": False})
    return rows


def test_position_matters_when_after_leaves_less_intrusion(tmp_path):
    # direction=1 units; oob_without=50 baseline for all.
    units = {f"u{i}": (50.0, 80.0, 50.0, 90.0, 1) for i in range(8)}
    baseline_path = tmp_path / "baseline.jsonl"
    _write(baseline_path, _baseline_rows("m", units))

    # REPEAT-BEFORE: little reduction (still near 80 -> intrusion ~30).
    before_path = tmp_path / "before.jsonl"
    _write(before_path, _manipulation_rows("m", "m1_before", {u: 78.0 for u in units}, (16, 0)))

    # REPEAT-AFTER: strong reduction (near 55 -> intrusion ~5).
    after_path = tmp_path / "after.jsonl"
    _write(after_path, _manipulation_rows("m", "m1", {u: 55.0 for u in units}, (16, 0)))

    allowed_mean = _mean_allowed_with_alignment(baseline_path)
    result = analyze_one_model(
        before_path=before_path, after_path=after_path, baseline_path=baseline_path,
        allowed_with_mean=allowed_mean,
    )
    assert result["n_paired_units"] == 8
    assert result["positional_effect_bootstrap"]["mean"] > 0
    assert result["position_matters"] is True


def test_position_does_not_matter_when_both_conditions_equal(tmp_path):
    units = {f"u{i}": (50.0, 80.0, 50.0, 90.0, 1) for i in range(8)}
    baseline_path = tmp_path / "baseline.jsonl"
    _write(baseline_path, _baseline_rows("m", units))

    before_path = tmp_path / "before.jsonl"
    _write(before_path, _manipulation_rows("m", "m1_before", {u: 60.0 for u in units}, (16, 0)))
    after_path = tmp_path / "after.jsonl"
    _write(after_path, _manipulation_rows("m", "m1", {u: 60.0 for u in units}, (16, 0)))

    allowed_mean = _mean_allowed_with_alignment(baseline_path)
    result = analyze_one_model(
        before_path=before_path, after_path=after_path, baseline_path=baseline_path,
        allowed_with_mean=allowed_mean,
    )
    assert result["positional_effect_bootstrap"]["mean"] == 0
    assert result["position_matters"] is False
