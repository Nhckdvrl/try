"""Validate and summarize the independent, label-blind OpenCode audit."""

import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "results/audits/g24a_confb_reaudit"
SOURCE = ROOT / "data/items/g24a_confb_selected_v1.jsonl"
OUT = BASE / "reaudit_summary.md"
IDS = BASE / "reaudit_flags.json"


def read(path):
    return [json.loads(line) for line in path.read_text().splitlines() if line]


def main():
    original = {r["cfb_id"]: r for r in read(SOURCE)}
    assert len(original) == 200
    records = []
    for batch in range(1, 5):
        blind = read(BASE / f"blind_batch_{batch:02d}.jsonl")
        audit = read(BASE / f"audit_batch_{batch:02d}.jsonl")
        assert len(blind) == len(audit) == 50
        blind_by = {r["id"]: r for r in blind}
        assert len(blind_by) == 50
        assert {r["id"] for r in audit} == set(blind_by)
        for r in audit:
            cid = r["id"]
            assert set(r) == {"id", "relation_a", "relation_b", "pair_valid", "naturalness", "issue"}
            assert r["relation_a"] in ("support", "refute", "neutral", "ambiguous")
            assert r["relation_b"] in ("support", "refute", "neutral", "ambiguous")
            assert r["naturalness"] in ("natural", "awkward", "broken")
            assert isinstance(r["pair_valid"], bool)
            src, b = original[cid], blind_by[cid]
            swap = int(hashlib.sha256(cid.encode()).hexdigest(), 16) % 2
            assert b["claim"] == src["claim"]
            assert b["evidence_a"] == (src["evidence_r"] if swap else src["evidence_s"])
            assert b["evidence_b"] == (src["evidence_s"] if swap else src["evidence_r"])
            a_expected, b_expected = (("refute", "support") if swap else ("support", "refute"))
            r["relation_correct"] = r["relation_a"] == a_expected and r["relation_b"] == b_expected
            r["batch"] = batch
            records.append(r)
    assert len(records) == 200 and len({r["id"] for r in records}) == 200
    counts = Counter()
    for r in records:
        counts["valid"] += r["pair_valid"]
        counts["relation_correct"] += r["relation_correct"]
        counts["natural_" + r["naturalness"]] += 1
        counts["valid_natural"] += r["pair_valid"] and r["naturalness"] == "natural"
    invalid = [r for r in records if not r["pair_valid"]]
    mismatch = [r for r in records if not r["relation_correct"]]
    flagged = [r for r in records if not r["pair_valid"] or not r["relation_correct"] or r["naturalness"] != "natural"]
    IDS.write_text(json.dumps({
        "valid_natural_ids": [r["id"] for r in records if r["pair_valid"] and r["relation_correct"] and r["naturalness"] == "natural"],
        "invalid_ids": [r["id"] for r in invalid],
        "relation_mismatch_ids": [r["id"] for r in mismatch],
        "naturalness_flag_ids": [r["id"] for r in records if r["naturalness"] != "natural"],
    }, indent=2) + "\n")
    lines = ["# Independent blind re-audit of the final ConfB 200", "",
             "Conducted 2026-09-27 by local OpenCode MiMo v2.6 Flash, one 50-pair batch per call. The agent saw only claim plus randomly swapped evidence A/B, not prior labels or model outputs. This is an **LLM-assisted semantic audit**, not a human gold annotation. No original materials or full-sample model results were changed. The reviewer can make errors; individual issue notes are retained below and in batch files.",
             "", "## Validation", "",
             "All 200 IDs appear once; each audit record has the expected schema; all blind text and A/B swaps reproduce the frozen selected data. Counts:", "",
             "| Flag | Count / 200 |", "|---|---:|",
             f"| Pair marked valid | {counts['valid']} |",
             f"| A/B relations match frozen S/R labels | {counts['relation_correct']} |",
             f"| Natural | {counts['natural_natural']} |",
             f"| Awkward | {counts['natural_awkward']} |",
             f"| Broken | {counts['natural_broken']} |",
             f"| Valid, relation-correct, and natural | {len(json.loads(IDS.read_text())['valid_natural_ids'])} |",
             "", "## Invalid pairs", ""]
    lines += [f"- `{r['id']}`: {r['issue']}" for r in invalid] or ["None."]
    lines += ["", "## Relation-label mismatches", ""]
    lines += [f"- `{r['id']}`: A={r['relation_a']}, B={r['relation_b']}; {r['issue']}" for r in mismatch] or ["None."]
    lines += ["", "## All flagged item notes", ""]
    lines += [f"- `{r['id']}` ({r['naturalness']}, valid={r['pair_valid']}): {r['issue']}" for r in flagged] or ["None."]
    lines += ["", "A valid-natural subset can be used only for **post hoc sensitivity**, never as a new held-out confirmation or replacement for the 200-pair primary result. The audit did not check source attribution or historical factual truth outside the shown sentences.", ""]
    OUT.write_text("\n".join(lines))
    print(OUT, dict(counts), "invalid", len(invalid), "mismatch", len(mismatch))


if __name__ == "__main__":
    main()
