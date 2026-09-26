"""Freeze G29's first 80 eligible audited pairs, before model inference."""

import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data/items/g29_blind_audit_v1"
SOURCE = ROOT / "data/items/g29_candidate_pool_v1.jsonl"
OUT = ROOT / "data/items/g29_selected_v1.jsonl"
REPORT = ROOT / "results/audits/g29_material_audit_v1.md"


def read(path):
    return [json.loads(s) for s in path.read_text().splitlines() if s]


def main():
    source = read(SOURCE)
    assert len(source) == 160 and [r["seed_rank"] for r in source] == list(range(160))
    chosen, reasons = [], Counter()
    for b in range(8):
        blind = read(BASE / f"blind_{b + 1:02d}.jsonl")
        audit = read(BASE / f"audit_{b + 1:02d}.jsonl")
        assert len(blind) == len(audit) == 20
        for i, (row, rec, verdict) in enumerate(zip(source[b*20:(b+1)*20], blind, audit)):
            assert row["id"] == rec["id"] == verdict["id"]
            swap = int(hashlib.sha256(row["id"].encode()).hexdigest(), 16) % 2
            a, c = ((row["evidence_r"], row["evidence_s"]) if swap else
                    (row["evidence_s"], row["evidence_r"]))
            assert (rec["evidence_a"], rec["evidence_b"]) == (a, c)
            assert verdict["relation_a"] in ("support", "refute", "neutral", "ambiguous")
            assert verdict["relation_b"] in ("support", "refute", "neutral", "ambiguous")
            assert verdict["naturalness"] in ("natural", "awkward", "broken")
            assert isinstance(verdict["pair_valid"], bool)
            assert isinstance(verdict["issue"], str) and verdict["issue"].strip(), row["id"]
            expected = ("refute", "support") if swap else ("support", "refute")
            valid = verdict["pair_valid"] and verdict["naturalness"] == "natural" and (
                verdict["relation_a"], verdict["relation_b"]) == expected
            if valid:
                if len(chosen) < 80:
                    chosen.append(row)
                reasons["eligible"] += 1
            else:
                if not verdict["pair_valid"]:
                    reasons["invalid_pair"] += 1
                if verdict["naturalness"] != "natural":
                    reasons["non_natural"] += 1
                if (verdict["relation_a"], verdict["relation_b"]) != expected:
                    reasons["orientation_mismatch"] += 1
    assert len(chosen) > 0
    OUT.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in chosen))
    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text("# G29 blind material audit and freeze\n\n"
        "Before G29 model inference. Mechanical source shortlist: 160 new VitaminC pairs. "
        "Local OpenCode MiMo v2.6 Flash audited blind batches 01–04 and 07–08; "
        "Longcat 2.5 Preview audited batches 05–06 after MiMo batch 05 stalled. "
        "A separate blind follow-up completed batch 05's initially empty issue explanations. "
        "These are LLM-assisted judgments, not human gold. Source roles were revealed only by this freeze script.\n\n"
        f"- Eligible on pair validity, naturalness, and original role alignment: {reasons['eligible']}/160.\n"
        f"- Frozen in seed order for model run: {len(chosen)} (first 80 eligible if available).\n"
        f"- Flagged invalid pair: {reasons['invalid_pair']}; non-natural: {reasons['non_natural']}; "
        f"orientation mismatch: {reasons['orientation_mismatch']} (overlapping categories).\n"
        f"- Selected seed ranks: {[r['seed_rank'] for r in chosen]}.\n\n"
        "All 160 candidate texts, all eight blind batches, and every auditor verdict remain in `data/items/`. "
        "No outcome-based filtering or replacements are permitted.\n")
    print(f"eligible {reasons['eligible']}/160; froze {len(chosen)}; {REPORT}")


if __name__ == "__main__":
    main()
