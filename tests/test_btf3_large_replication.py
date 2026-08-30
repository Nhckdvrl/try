import json
from pathlib import Path
import sys

import pandas as pd
import pytest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT / "scripts"))

from adapters.btf3_large_replication import (  # noqa: E402
    QUOTA_PER_RESOLUTION,
    SEED,
    _reviewed_non_accept_ids,
    build_exclusion_universe,
    full_deterministic_queue,
    normalize_question,
    order_key,
    render_review_chunk,
)
import analyze_btf3_large_replication as large  # noqa: E402
import analyze_btf3_confirmatory as confirmatory  # noqa: E402


def make_row(qid: str, resolution: int, question: str = "Will X happen?") -> dict:
    return {
        "question_id": qid,
        "question": question,
        "resolution_criteria": "Resolves YES if X happens.",
        "background": "Some pre-cutoff background.",
        "present_date": "2026-05-12 00:00:00",
        "date_cutoff_end": "2026-05-13 00:00:00",
        "expected_resolution_date": "2026-06-30 00:00:00",
        "resolution": float(resolution),
        "resolution_explanation": f"X did {'' if resolution else 'not '}happen.",
    }


def frame(rows: list[dict]) -> pd.DataFrame:
    return pd.DataFrame(rows)


def test_queue_order_is_the_frozen_hash_order():
    rows = [make_row(f"q{i}", i % 2, question=f"Will event {i} happen?") for i in range(20)]
    built = full_deterministic_queue(frame(rows), seed=SEED)
    for resolution, bucket in built["queue"].items():
        ids = [str(row["question_id"]) for row in bucket]
        assert ids == sorted(ids, key=lambda qid: order_key(qid, seed=SEED))
        assert all(int(float(row["resolution"])) == resolution for row in bucket)
    assert sum(len(bucket) for bucket in built["queue"].values()) == 20


def test_queue_is_complete_not_truncated():
    rows = [make_row(f"q{i}", 1, question=f"Will event {i} happen?") for i in range(37)]
    built = full_deterministic_queue(frame(rows), seed=SEED)
    assert len(built["queue"][1]) == 37


def test_excluded_ids_never_enter_the_queue():
    rows = [make_row(f"q{i}", i % 2, question=f"Will event {i} happen?") for i in range(10)]
    built = full_deterministic_queue(frame(rows), seed=SEED, exclude_question_ids=["q3", "q4"])
    queued = {str(row["question_id"]) for bucket in built["queue"].values() for row in bucket}
    assert {"q3", "q4"}.isdisjoint(queued)
    assert len(queued) == 8


def test_hard_duplicate_keeps_the_earlier_hash_rank():
    duplicate_question = "Will the SAME  thing happen?"
    rows = [
        make_row("dup-a", 1, question=duplicate_question),
        make_row("dup-b", 1, question=duplicate_question.upper()),
        make_row("other", 1, question="Something else?"),
    ]
    built = full_deterministic_queue(frame(rows), seed=SEED)
    queued = [str(row["question_id"]) for row in built["queue"][1]]
    winner = min(("dup-a", "dup-b"), key=lambda qid: order_key(qid, seed=SEED))
    loser = "dup-b" if winner == "dup-a" else "dup-a"
    assert winner in queued and loser not in queued
    assert built["dropped_duplicate_within_round"] == [
        {"question_id": loser, "kept_question_id": winner, "normalized_question": normalize_question(duplicate_question)}
    ]


def test_prior_round_question_text_is_dropped_as_stale():
    rows = [make_row("q1", 1, question="Will the reused question resolve YES?")]
    built = full_deterministic_queue(
        frame(rows),
        seed=SEED,
        exclude_normalized_questions=[normalize_question("will the reused question resolve yes?")],
    )
    assert built["queue"][1] == []
    assert built["dropped_duplicate_against_prior_rounds"][0]["question_id"] == "q1"


def test_normalize_question_collapses_whitespace_and_case():
    assert normalize_question("  Will  X\nhappen? ") == normalize_question("will x happen?")


def test_reviewed_non_accept_ids_collects_reject_and_unsure_only():
    markdown = (
        "### YES-1. `a`\n- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`\n\n"
        "### YES-2. `b`\n- Decision: `[ ] ACCEPT  [x] REJECT  [ ] UNSURE`\n"
        "- Reason: packet is wrong\n\n"
        "### NO-1. `c`\n- Decision: `[ ] ACCEPT  [ ] REJECT  [x] UNSURE`\n"
        "- Reason: ambiguous criteria\n"
    )
    path = Path("/tmp/_btf3_reviewed_test.md")
    path.write_text(markdown, encoding="utf-8")
    assert _reviewed_non_accept_ids(path) == ["b", "c"]


def test_exclusion_universe_matches_the_committed_prior_rounds():
    universe = build_exclusion_universe(
        pilot_jsonl=ROOT / "data/external/review/btf3_temporal_pilot_v0.2r2.jsonl",
        confirmatory_jsonl=ROOT / "data/external/review/btf3_temporal_confirmatory_v1.jsonl",
        prior_candidates_json=ROOT / "data/external/review/btf3_confirmatory_v1_candidates.json",
        prior_reviewed_md=ROOT / "data/external/review/btf3_confirmatory_v1_reviewed.md",
    )
    counts = universe["category_counts"]
    assert counts["pilot_v0_2r2"] == 8
    assert counts["confirmatory_v1_frozen"] == 64
    assert counts["confirmatory_v1_candidate_queue"] == 128
    assert counts["confirmatory_v1_review_reject_or_unsure"] == 13
    assert counts["historical_pilot_rejects"] == 2
    # The prior candidate queue subsumes the frozen 64 and every prior reject,
    # so the strict-freshness union is the queue plus pilot plus the two
    # historical rejects.
    assert universe["union_count"] == 138


def test_review_chunk_is_presentation_only_and_carries_all_four_gates():
    rows = [make_row("q1", 1), make_row("q2", 1, question="Second?")]
    markdown = render_review_chunk(rows, bucket_label="YES", start_index=65)
    assert "### YES-65. `q1`" in markdown and "### YES-66. `q2`" in markdown
    for gate in ("pre-cutoff intact", "realized outcome valid", "exact packet factually valid", "criteria unambiguous"):
        assert markdown.count(gate) == 2
    assert markdown.count("- Decision: `[ ] ACCEPT  [ ] REJECT  [ ] UNSURE`") == 2


def test_thresholds_scale_the_confirmatory_ratios_exactly():
    assert large.THRESHOLDS["minimum_decision_parse_rate"] == confirmatory.THRESHOLDS["minimum_decision_parse_rate"]
    assert large.THRESHOLDS["minimum_boundary_accuracy"] == confirmatory.THRESHOLDS["minimum_boundary_accuracy"]
    assert large.THRESHOLDS["minimum_decision_parse_rate"] == 992 / 1024
    assert large.THRESHOLDS["minimum_boundary_accuracy"] == 448 / 512
    for key in ("minimum_mean_responsiveness_points", "minimum_allowed_with_alignment_points",
                "intrusion_sesoi_points", "minimum_qualified_models", "minimum_intrusion_models"):
        assert large.THRESHOLDS[key] == confirmatory.THRESHOLDS[key]


def test_quota_is_128_per_realized_outcome():
    assert QUOTA_PER_RESOLUTION == 128


def _write_round(tmp_path: Path, quota: int) -> tuple[Path, list[Path]]:
    """Build a miniature frozen queue + reviewed chunks for freeze/audit tests."""
    from adapters.btf3_large_replication import file_sha256

    manifest_queues = {}
    reviewed: list[Path] = []
    for label, resolution in (("YES", 1), ("NO", 0)):
        ids = [f"{label.lower()}-{i}" for i in range(1, quota + 3)]
        queue_path = tmp_path / f"{label.lower()}_queue.json"
        queue_path.write_text(json.dumps({
            "bucket": label,
            "realized_resolution": resolution,
            "order": [{"position": i, "question_id": qid, "order_key": order_key(qid)}
                      for i, qid in enumerate(ids, 1)],
        }), encoding="utf-8")
        lines = []
        for i, qid in enumerate(ids, 1):
            # reject the second candidate in each bucket
            reject = i == 2
            lines.append(f"### {label}-{i}. `{qid}`")
            lines.append(
                "- Decision: `[ ] ACCEPT  [x] REJECT  [ ] UNSURE`" if reject
                else "- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`"
            )
            if reject:
                lines.append("- Reason: packet factual error")
            lines.append("")
        review_path = tmp_path / f"{label.lower()}_review.md"
        review_path.write_text("\n".join(lines), encoding="utf-8")
        reviewed.append(review_path)
        manifest_queues[label] = {"path": str(queue_path), "sha256": file_sha256(queue_path)}
    manifest = tmp_path / "queue.json"
    manifest.write_text(json.dumps({"quota_per_resolution": quota, "queues": manifest_queues}), encoding="utf-8")
    return manifest, reviewed


def test_freeze_takes_the_first_n_accepts_in_queue_order(tmp_path):
    import freeze_btf3_large_replication as freeze

    manifest_path, reviewed = _write_round(tmp_path, quota=4)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    decisions = freeze.load_decisions(reviewed)
    accepted = []
    for label, info in sorted(manifest["queues"].items()):
        queue = json.loads(Path(info["path"]).read_text(encoding="utf-8"))
        bucket = []
        for entry in queue["order"]:
            if len(bucket) >= 4:
                break
            if decisions[entry["question_id"]][0] == "ACCEPT":
                bucket.append(entry["question_id"])
        accepted.append(bucket)
    # the rejected second candidate is consumed, never replaced in place
    assert accepted[0] == ["no-1", "no-3", "no-4", "no-5"]
    assert accepted[1] == ["yes-1", "yes-3", "yes-4", "yes-5"]


def test_freeze_rejects_conflicting_decisions_for_one_candidate(tmp_path):
    import freeze_btf3_large_replication as freeze

    a = tmp_path / "a.md"
    b = tmp_path / "b.md"
    a.write_text("### YES-1. `q`\n- Decision: `[x] ACCEPT  [ ] REJECT  [ ] UNSURE`\n", encoding="utf-8")
    b.write_text(
        "### YES-1. `q`\n- Decision: `[ ] ACCEPT  [x] REJECT  [ ] UNSURE`\n- Reason: no\n",
        encoding="utf-8",
    )
    with pytest.raises(ValueError, match="conflicting recorded decisions"):
        freeze.load_decisions([a, b])
