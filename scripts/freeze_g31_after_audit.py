"""Freeze G31 first-60 audit-accepted items before any model inference."""

import hashlib
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data/items/g31_candidates_v1.jsonl"
AUDIT = ROOT / "data/items/g31_blind_audit_v1"
SELECTED = ROOT / "data/items/g31_selected_v1.jsonl"
SUMMARY = ROOT / "results/audits/g31_material_audit_v1.md"
RELATIONS = {"supports", "refutes", "neutral", "ambiguous"}


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    candidates = [json.loads(line) for line in SRC.read_text().splitlines()]
    assert len(candidates) == 80
    verdicts = {}
    for batch in range(1, 9):
        blind = [json.loads(line) for line in (AUDIT / f"blind_{batch:02d}.jsonl").read_text().splitlines()]
        judged = [json.loads(line) for line in (AUDIT / f"audit_{batch:02d}.jsonl").read_text().splitlines()]
        assert len(blind) == len(judged) == 10
        for b, v in zip(blind, judged):
            assert v["id"] == b["id"] and v["id"] not in verdicts
            assert v["relation_a"] in RELATIONS and v["relation_b"] in RELATIONS
            for key in ("pair_valid", "natural", "distinct_e2", "irrelevant_valid", "accept"):
                assert isinstance(v[key], bool), (v["id"], key)
            assert isinstance(v["reason"], str) and v["reason"].strip()
            swapped = b["note_a"] == candidates[(batch - 1) * 10 + blind.index(b)]["x_r"]
            expected = ("refutes", "supports") if swapped else ("supports", "refutes")
            assert v["accept"] == (v["pair_valid"] and v["natural"] and
                                    v["distinct_e2"] and v["irrelevant_valid"] and
                                    (v["relation_a"], v["relation_b"]) == expected), v["id"]
            verdicts[v["id"]] = v
    selected = [row for row in candidates if verdicts[row["id"]]["accept"]][:60]
    assert selected
    SELECTED.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in selected))
    reasons = Counter()
    for v in verdicts.values():
        if not v["accept"]:
            for key in ("pair_valid", "natural", "distinct_e2", "irrelevant_valid"):
                if not v[key]:
                    reasons[key] += 1
            if v["pair_valid"] and (v["relation_a"] not in ("supports", "refutes") or
                                    v["relation_b"] not in ("supports", "refutes")):
                reasons["relation_ambiguous"] += 1
    accepted = sum(v["accept"] for v in verdicts.values())
    lines = [
        "# G31 constructed-note material audit", "",
        "Completed before G31 model inference. This audit applies to constructed X notes; "
        "the source-pinned natural E2 pairs were previously audited for G29. MiMo 2.6 Flash "
        "built the notes. Separate role-blind passes judged every item: MiMo for batches 02–05 and 08, "
        "Longcat 2.5 Preview for batches 01, 06, and 07 after MiMo service timeouts. "
        "It remains an LLM-assisted audit, not human gold.", "",
        f"- Candidates: {len(candidates)}; accepted: {accepted}; frozen first accepted in seed order: {len(selected)}.",
        f"- Candidate SHA-256: {digest(SRC)}.",
        f"- Selected SHA-256: {digest(SELECTED)}.",
        "- Rejected candidates and item-specific reasons remain in data/items/g31_blind_audit_v1/audit_*.jsonl.",
        "- X notes are constructed temporary case notes, not quotations from real documents. "
        "The 80 claim/E2 pairs overlap G29 by design; G31 is exploratory joint measurement.", "",
        "## Failure census", "",
    ]
    for key, value in sorted(reasons.items()):
        lines.append(f"- {key}: {value}")
    lines += ["", "## Rejected items"]
    for row in candidates:
        v = verdicts[row["id"]]
        if not v["accept"]:
            lines.append(f"- {row['id']}: {v['reason']}")
    SUMMARY.parent.mkdir(parents=True, exist_ok=True)
    SUMMARY.write_text("\n".join(lines) + "\n")
    print(f"accepted {accepted}/80, selected {len(selected)}, selected sha256={digest(SELECTED)}")


if __name__ == "__main__":
    main()
