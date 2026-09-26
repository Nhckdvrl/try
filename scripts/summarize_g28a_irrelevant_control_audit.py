"""Validate local OpenCode audit of the 200 frozen irrelevant E1 controls."""

import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "results/audits/g28a_irrelevant_control_audit"


def read(path):
    return [json.loads(s) for s in path.read_text().splitlines() if s]


def main():
    source = {r["cfb_id"]: r for r in read(ROOT / "data/items/g24a_confb_selected_v1.jsonl")}
    controls = {}
    for r in read(ROOT / "data/items/g24a_confb_v1.jsonl"):
        if r["meta"]["arm"] == "control":
            controls[r["meta"]["cfb_id"]] = r["critical_evidence"]
    assert len(source) == len(controls) == 200 and set(source) == set(controls)
    records = []
    for batch in range(1, 5):
        blind = read(BASE / f"blind_batch_{batch:02d}.jsonl")
        audit = read(BASE / f"audit_batch_{batch:02d}.jsonl")
        assert len(blind) == len(audit) == 50
        ids = [r["id"] for r in blind]
        assert len(set(ids)) == 50 and set(ids) == {r["id"] for r in audit}
        for r in blind:
            assert r["claim"] == source[r["id"]]["claim"]
            assert r["sentence"] == controls[r["id"]]
        for r in audit:
            assert set(r) == {"id", "relevance", "naturalness", "issue"}, (batch, r)
            # Batch 01 wrote the synonymous free-text label despite the prompt's
            # requested enum. Keep its original file untouched; normalize only
            # in this summary and disclose the mapping below.
            if batch == 1 and r["relevance"] == "genuinely irrelevant":
                r["relevance"] = "irrelevant"
            assert r["relevance"] in ("irrelevant", "potentially_relevant", "relevant"), r
            assert r["naturalness"] in ("natural", "awkward", "broken"), r
            records.append(r)
    assert len(records) == 200 and len({r["id"] for r in records}) == 200
    counts = Counter(r["relevance"] for r in records)
    natural = Counter(r["naturalness"] for r in records)
    flagged = [r for r in records if r["relevance"] != "irrelevant"]
    ids_path = BASE / "control_audit_flags.json"
    ids_path.write_text(json.dumps({
        "valid_natural_ids": [r["id"] for r in records if r["relevance"] == "irrelevant"],
        "potentially_relevant_ids": [r["id"] for r in records if r["relevance"] == "potentially_relevant"],
        "relevant_ids": [r["id"] for r in records if r["relevance"] == "relevant"],
        "awkward_or_broken_ids": [r["id"] for r in records if r["naturalness"] != "natural"],
    }, indent=2) + "\n")
    lines = ["# Blind LLM-assisted audit of G28A/G28B irrelevant controls", "",
             "Local OpenCode MiMo v2.6 Flash inspected 200 claim/control-sentence pairs in four 50-item batches, without evidence-polarity labels or model outputs. Some CLI attempts failed at startup or after a batch file was written; only four independently validated complete output files are counted. Batch 01 used the synonymous label `genuinely irrelevant` for all 50 records; this summary maps that string to `irrelevant` without editing the raw audit file. This is LLM-assisted review, not human gold. Frozen controls and full-run analyses are unchanged.",
             "", "Every batch has exactly 50 unique IDs matching its blind input; 200 distinct IDs overall. Every blind claim and control sentence exactly matches the frozen selected/rendered data.",
             "", "| Category | Count |", "|---|---:|",
             *[f"| Relevance: {k} | {counts[k]} |" for k in ("irrelevant", "potentially_relevant", "relevant")],
             *[f"| Naturalness: {k} | {natural[k]} |" for k in ("natural", "awkward", "broken")],
             "", "## Potentially relevant or relevant controls", ""]
    lines.extend(f"- `{r['id']}` ({r['relevance']}): {r['issue']}" for r in flagged)
    if not flagged:
        lines.append("None flagged by the reviewer.")
    lines += ["", "A control-restricted reanalysis, if used, is explicitly post hoc and cannot replace the frozen full-sample result. The audit does not establish source provenance or factual truth of the control sentence.", ""]
    (BASE / "control_audit_summary.md").write_text("\n".join(lines))
    print(dict(counts), dict(natural), "flagged", len(flagged))


if __name__ == "__main__":
    main()
