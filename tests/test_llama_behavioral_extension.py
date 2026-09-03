from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from analyze_llama_behavioral_extension import a1_report


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
