from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from analyze_llama_behavioral_extension import a1_report
from analyze_packet_swap import load
from analyze_redacted_swap import analyze_model as analyze_g11


def test_existing_llama_a1_result_and_probe_asymmetry_are_locked():
    path = ROOT / "results/raw/isr_llama31-8b_btf3_large_replication_v1.jsonl"
    report = a1_report(path)
    assert report["complete_units"] == 256
    assert not report["qualified"]
    assert report["boundary_by_condition"]["boundary_oob_with"]["correct"] == 250
    assert report["boundary_by_condition"]["boundary_allowed_with"]["correct"] == 127
    intrusion = report["metrics"]["out_of_set_intrusion"]
    assert round(intrusion["mean"], 5) == 28.22945
    assert intrusion["ci_low"] > 5


def test_legacy_trailing_decimal_outputs_are_reparsed_without_raw_mutation():
    path = ROOT / "results/raw/isr_llama31-8b_g8_swap_with.jsonl"
    _, rows = load(path)
    recovered = [r for r in rows if r.get("value_reparsed")]
    assert len(recovered) == 2
    assert {r["raw"] for r in recovered} == {"0."}
    assert {r["value"] for r in recovered} == {0.0}


def test_llama_g11_separates_legacy_gate_from_scientific_verdict():
    raw = ROOT / "results/raw"
    report = analyze_g11(
        "llama31-8b",
        raw / "isr_llama31-8b_btf3_large_replication_v1.jsonl",
        raw / "isr_llama31-8b_g8_swap_with.jsonl",
        raw / "isr_llama31-8b_g11_redacted_swap_with.jsonl",
    )
    assert report["reparsed_values"] == 2
    assert report["verdict"] == "indeterminate"
    assert report["scientific_verdict"] == "survives"
