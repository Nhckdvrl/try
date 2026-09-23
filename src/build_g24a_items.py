"""Build the G24A candidate items file from the audited FEVER + SciFact pools.

Deterministic by construction (prereg §5.1):

* strata are emitted in the frozen order
  ``[fever/SUPPORTS, fever/REFUTES, scifact/SUPPORT, scifact/CONTRADICT]``;
* within-stratum order comes from one ``random.Random(SEED)`` stream applied
  to each stratum in that order;
* every item carries its stratum, gold label, cluster key and a
  ``candidate_rank`` (0-based position in the file) in ``meta``.

Usage:
    PYTHONPATH=src python src/build_g24a_items.py \
        --out data/items/g24a_candidates_v1.jsonl
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import random
import sys

sys.path.insert(0, os.path.dirname(__file__))
from g24a_sources import build_fever_pool, build_scifact_pool  # noqa: E402
import conditions_g24a as g24a  # noqa: E402

SEED = 20260924
STRATA = [("fever", "SUPPORTS"), ("fever", "REFUTES"),
          ("scifact", "SUPPORT"), ("scifact", "CONTRADICT")]
FROZEN_STRATA_COUNTS = {("fever", "SUPPORTS"): 6326,
                        ("fever", "REFUTES"): 6322,
                        ("scifact", "SUPPORT"): 417,
                        ("scifact", "CONTRADICT"): 218}


def _item(rec: dict, rank: int) -> dict:
    source = rec["source"]
    stratum = f"{source}/{rec['label']}"
    item_id = (f"g24a_fever_{rec['fever_id']}" if source == "fever"
               else f"g24a_scifact_{rec['scifact_id']}")
    meta = {
        "source": source,
        "stratum": stratum,
        "gold_label": rec["label"],
        "cluster": rec["cluster"],
        "candidate_rank": rank,
        "block_chars": len(rec["evidence_block"]),
        "sentence_count": len(rec["evidence_sentences"]),
        "source_id": rec["fever_id"] if source == "fever" else rec["scifact_id"],
    }
    if source == "fever":
        meta["evidence_pages"] = rec["evidence_pages"]
        meta["n_groups"] = rec["n_groups"]
    else:
        meta["split"] = rec["split"]
        meta["evidence_doc_id"] = rec["evidence_doc_id"]
        meta["rationale_idxs"] = rec["rationale_idxs"]
    return {
        "item_id": item_id,
        "task_family": f"g24a_{source}",
        "surface_domain": "wikipedia" if source == "fever" else "scientific_abstract",
        "base_context": rec["claim"],
        "critical_evidence": rec["evidence_block"],
        "critical_label": "evidence E",
        "critical_direction": rec["direction"],
        "exclusion_reason": g24a.EXCLUSION_REASON,
        "evidence_truth": g24a.EVIDENCE_TRUTH,
        "admit_rule": g24a.ADMIT_RULE,
        "exclude_rule": g24a.EXCLUDE_RULE,
        "question": g24a.QUESTION,
        "output_spec": g24a.OUTPUT_SPEC,
        "memory_question": g24a.MEMORY_QUESTION,
        "rule_probe_question": g24a.RULE_PROBE_QUESTION,
        "ground_truth": None,
        "meta": meta,
    }


def items_from_pools(fever: list[dict], scifact: list[dict],
                     seed: int = SEED) -> list[dict]:
    """Frozen-order candidate items from pool records (pure; testable)."""
    rng = random.Random(seed)
    out: list[dict] = []
    for source, label in STRATA:
        pool = fever if source == "fever" else scifact
        stratum_recs = [r for r in pool if r["label"] == label]
        rng.shuffle(stratum_recs)
        for rec in stratum_recs:
            out.append(_item(rec, len(out)))
    return out


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="data/items/g24a_candidates_v1.jsonl")
    args = ap.parse_args()

    fever, fdiag = build_fever_pool()
    scifact, sdiag = build_scifact_pool()
    items = items_from_pools(fever, scifact)

    # frozen strata counts (prereg §2/§11.2) — construction gate
    got: dict[tuple, int] = {}
    for it in items:
        s, lab = it["meta"]["stratum"].split("/")
        got[(s, lab)] = got.get((s, lab), 0) + 1
    assert got == FROZEN_STRATA_COUNTS, f"strata drifted: {got}"
    assert len(items) == 13283, f"candidate total drifted: {len(items)}"
    assert len({it["item_id"] for it in items}) == len(items), "duplicate item_id"

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as fh:
        for it in items:
            fh.write(json.dumps(it, ensure_ascii=False) + "\n")
    sha = hashlib.sha256(open(args.out, "rb").read()).hexdigest()
    print(f"wrote {len(items)} candidates -> {args.out}")
    print(f"  strata: {dict(got)}")
    print(f"  sha256: {sha}")
    print(f"  pool diagnostics: fever emitted={fdiag['records_emitted']} "
          f"scifact emitted={sdiag['records_emitted']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
