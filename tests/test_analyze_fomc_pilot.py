from src.analyze_fomc_pilot import THRESHOLDS, _next_meeting_year


def test_next_meeting_year_takes_the_second_date_in_the_unit_id():
    assert _next_meeting_year("20220615_20220727") == "2022"
    assert _next_meeting_year("20251029_20251210") == "2025"


def test_thresholds_are_scaled_from_btf3_pilot_ratios_to_n24():
    # BTF-3 pilot: 31/32 decision parse, 14/16 boundary accuracy.
    assert THRESHOLDS["minimum_decision_parse_rate"] == 93 / 96
    assert THRESHOLDS["minimum_boundary_accuracy"] == 42 / 48
    assert THRESHOLDS["minimum_qualified_models"] == 2
    assert THRESHOLDS["minimum_intrusion_models"] == 2
