from src.run_information_set import boundary_probe, parse_probability, parse_yesno


def test_probability_parser_is_strict_and_bounded():
    assert parse_probability("75") == 75.0
    assert parse_probability(" 12.5% ") == 12.5
    assert parse_probability("100.0") == 100.0
    assert parse_probability("0.") == 0.0
    assert parse_probability("100.") == 100.0
    assert parse_probability("101") is None
    assert parse_probability("Probability: 75") is None


def test_yesno_parser_is_strict():
    assert parse_yesno("YES") == "YES"
    assert parse_yesno(" no. ") == "NO"
    assert parse_yesno("The answer is yes") is None


def test_boundary_probe_replaces_decision_task():
    prompt = "SOURCE\n\nTASK\nold task"
    probe = boundary_probe(prompt, expected="NO")
    assert "old task" not in probe
    assert "BOUNDARY CHECK" in probe
