from src.information_set_metrics import InformationSetScores, compute_metrics, summarize


def test_behavioral_contract_has_both_directions():
    metrics = compute_metrics(InformationSetScores(0.9, 0.1, 0.55, 0.45))
    assert round(metrics.responsiveness, 8) == 0.8
    assert round(metrics.out_of_set_intrusion, 8) == 0.1
    assert round(metrics.boundary_selectivity, 8) == 0.7


def test_summary_uses_independent_units_not_render_count():
    score_a = InformationSetScores(1, 0, 0.2, 0)
    score_b = InformationSetScores(1, 0, 0.8, 0)
    base = summarize([(score_a, "a"), (score_b, "b")], n_resamples=100, seed=4)
    copied = summarize([(score_a, "a")] * 10 + [(score_b, "b")], n_resamples=100, seed=4)
    assert base["out_of_set_intrusion"]["mean"] == copied["out_of_set_intrusion"]["mean"]
