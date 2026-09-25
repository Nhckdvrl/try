#!/usr/bin/env python3
"""Build the Pilot P3 item file: 200 discovery claims x 1 (no arms) = 200 items.

Registration §11 (wording frozen pre-run, user 2026-09-26).  P3 is the
operator-only control: NO real evidence is ever rendered, so there are no
arms — one item per claim.

Input (committed before any model run):
  data/items/g24a_p2_v1.jsonl   - the 400 P2 arm items; the plus arm of each
                                  of the 200 claims carries the claim text

Carried over verbatim from the P2 plus item: base_context (the claim),
question / output_spec / ADMIT / EXCLUDE wording (schema completeness — the
P3 cells never render the admit/exclude rules), surface_domain, and the
provenance meta (p2_id, case_id, claim_sha, split, seed_rank, page, ...).

Replaced deliberately:
  item_id              g24p2_<nnn>       -> g24p3_<nnn>   (link kept in meta)
  critical_evidence    the placeholder   "[Content unavailable.]" — the P3
                       blocks read the MODULE constant, not this field, so
                       real evidence text cannot render even by mistake;
  critical_direction   "neutral"         (no evidence direction exists)
  evidence_truth       "none_shown"      (no evidence is ever shown)
  meta.pilot           "g24a_p3", plus "evidence_shown": False and the
                       source P2 item id

task_family stays "g24a_vitaminc": the `base` cell must render through the
UNMODIFIED G24A module, byte-identical to P2's Base (a re-run of the same
prompt; registration §11 condition 1).

Read-back verification (asserted here):
  - 200 items, unique ids, no id overlap with p2 / p1 / discovery files
  - base prompt byte-identical to the P2 item's base prompt, evidence-free
  - prior_only: verbatim note, no "EVIDENCE E", no "RULING"
  - withheld cells: "EVIDENCE E\n[Content unavailable.]" block present,
    the two ruling cells carry the P1 module constants
  - LEAKAGE: neither arm's real P2 evidence text appears in ANY of the five
    P3 prompts of its claim (all 200 claims)
  - ids file == item ids, length 200

Output: data/items/g24a_p3_v1.jsonl (200 lines), data/items/g24a_p3_ids.json

Usage: python scripts/build_g24a_p3_items.py
"""
from __future__ import annotations

import json
import os
import sys
from pathlib import Path

P2_ITEMS = "data/items/g24a_p2_v1.jsonl"
OUT = "data/items/g24a_p3_v1.jsonl"
IDS = "data/items/g24a_p3_ids.json"
DISCOVERY = "data/items/g24a_v1.jsonl"
P1_ITEMS = "data/items/g24a_p1_v1.jsonl"

ITEM_KEYS = [
    "item_id", "task_family", "surface_domain", "base_context",
    "critical_evidence", "critical_label", "critical_direction",
    "exclusion_reason", "evidence_truth", "admit_rule", "exclude_rule",
    "question", "output_spec", "memory_question", "rule_probe_question",
    "ground_truth", "meta",
]

KINDS = ["base", "prior_only", "withheld_only", "withheld_strong",
         "withheld_cf"]


def main() -> int:
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
    import schema
    import conditions_g24a as g24a
    import conditions_g24p1 as g24p1
    import conditions_g24p3 as g24p3

    p2 = [json.loads(l) for l in open(P2_ITEMS, encoding="utf-8")]
    assert len(p2) == 400, len(p2)
    plus = [it for it in p2 if it["meta"]["arm"] == "plus"]
    assert len(plus) == 200, len(plus)

    out_lines = []
    for src in plus:
        p2_id = src["meta"]["p2_id"]
        p3_id = "g24p3_" + p2_id.split("_", 1)[1]
        assert p3_id.startswith("g24p3_"), p3_id
        meta = {
            "pilot": "g24a_p3",
            "p2_id": p2_id,
            "source_item_id": src["item_id"],
            "case_id": src["meta"]["case_id"],
            "claim_sha": src["meta"]["claim_sha"],
            "p2_role": src["meta"]["p2_role"],
            "seed_rank": src["meta"]["seed_rank"],
            "split": src["meta"]["split"],
            "page": src["meta"]["page"],
            "first_lineno": src["meta"]["first_lineno"],
            "evidence_shown": False,
        }
        it = {
            "item_id": p3_id,
            "task_family": "g24a_vitaminc",
            "surface_domain": src["surface_domain"],
            "base_context": src["base_context"],
            "critical_evidence": g24p3.WITHHELD_CONTENT,
            "critical_label": "evidence E",
            "critical_direction": "neutral",
            "exclusion_reason": g24a.EXCLUSION_REASON,
            "evidence_truth": "none_shown",
            "admit_rule": g24a.ADMIT_RULE,
            "exclude_rule": g24a.EXCLUDE_RULE,
            "question": g24a.QUESTION,
            "output_spec": g24a.OUTPUT_SPEC,
            "memory_question": g24a.MEMORY_QUESTION,
            "rule_probe_question": g24a.RULE_PROBE_QUESTION,
            "ground_truth": None,
            "meta": meta,
        }
        assert list(it.keys()) == ITEM_KEYS, it["item_id"]
        out_lines.append(it)

    with open(OUT, "w", encoding="utf-8") as fh:
        for it in out_lines:
            fh.write(json.dumps(it, ensure_ascii=False) + "\n")

    ids = [it["item_id"] for it in out_lines]
    Path(IDS).write_text(json.dumps(ids, indent=1) + "\n")

    # --- read-back verification -------------------------------------------
    items = schema.load_items(OUT)
    assert len(items) == 200, len(items)
    assert len({i.item_id for i in items}) == 200, "duplicate item ids"
    assert len(ids) == 200 and set(ids) == {i.item_id for i in items}

    disc_ids = {json.loads(l)["item_id"] for l in open(DISCOVERY, encoding="utf-8")}
    p1_ids = {json.loads(l)["item_id"] for l in open(P1_ITEMS, encoding="utf-8")}
    p2_ids = {it["item_id"] for it in p2}
    assert not ({i.item_id for i in items} & (disc_ids | p1_ids | p2_ids)), \
        "id overlap with earlier pilots"

    by_p2 = {it.meta["p2_id"]: it for it in items}
    assert len(by_p2) == 200
    assert len({it.meta["claim_sha"] for it in items}) == 200, "duplicate claims"

    p2_obj = {it.item_id: it for it in schema.load_items(P2_ITEMS)}
    assert len(p2_obj) == 400

    n_leak_checks = 0
    for it in items:
        assert it.task_family == "g24a_vitaminc", it.item_id
        assert g24a.is_g24a(it), it.item_id  # base routes to unmodified G24A
        assert it.meta["pilot"] == "g24a_p3" and it.meta["evidence_shown"] is False
        assert it.critical_evidence == g24p3.WITHHELD_CONTENT, it.item_id
        assert it.question == g24a.QUESTION and it.output_spec == g24a.OUTPUT_SPEC
        src = p2_obj[it.meta["source_item_id"]]
        src_minus = p2_obj[it.meta["p2_id"] + "_minus"]
        assert src.meta["arm"] == "plus" and src_minus.meta["arm"] == "minus"
        # claim carried verbatim from P2
        assert it.base_context == src.base_context, it.item_id

        prompts = {k: schema.compile_prompt(it, k) for k in KINDS}
        # 1. base is byte-identical to P2's Base (re-run of the same prompt)
        assert prompts["base"] == schema.compile_prompt(src, "base"), \
            f"base not byte-identical: {it.item_id}"
        assert "EVIDENCE E\n" not in prompts["base"], it.item_id
        assert "RULING" not in prompts["base"], it.item_id
        # 2. prior_only: verbatim note, no evidence, no ruling
        po = prompts["prior_only"]
        assert po.count(g24p3.PRIOR_ONLY_NOTE) == 1, it.item_id
        assert "EVIDENCE E\n" not in po and "RULING" not in po, it.item_id
        # 3. withheld block present in all three withheld cells
        blk = g24a.EVIDENCE_HEADER + "\n" + g24p3.WITHHELD_CONTENT
        for k in ("withheld_only", "withheld_strong", "withheld_cf"):
            assert blk in prompts[k], (it.item_id, k)
        # 4. rulings verbatim in the two ruling cells, absent otherwise
        assert g24p1.STRONG_EXCLUDE_RULE in prompts["withheld_strong"], it.item_id
        assert g24p1.CF_DELETE_RULE in prompts["withheld_cf"], it.item_id
        assert "RULING" not in prompts["withheld_only"], it.item_id
        # 5. LEAKAGE: neither arm's real evidence text renders anywhere
        real = [src.critical_evidence, src_minus.critical_evidence]
        for text in real:
            for k, p in prompts.items():
                assert text not in p, (it.item_id, k, "real evidence leaked")
            n_leak_checks += 1
        # 6. TASK tail on every cell
        for k, p in prompts.items():
            assert "TASK\n" + it.question in p, (it.item_id, k)

    print(f"wrote {OUT}: 200 items (no arms, evidence never rendered), "
          f"base byte-identical to P2 per claim")
    print(f"wrote {IDS}: 200 ids; run contract: {len(KINDS)} kinds x 200 "
          f"= {len(KINDS) * 200} rows/model")
    print(f"leakage assertions: {n_leak_checks * len(KINDS)} "
          f"(2 real texts x 5 prompts x 200 claims)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
