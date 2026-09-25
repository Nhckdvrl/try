#!/usr/bin/env python3
"""Build the Pilot P4 item file: 200 discovery claims x 1 (no arms) = 200 items.

Registration §12 (wording + material rule frozen pre-run, user 2026-09-26).
P4 is the irrelevant-visible evidence control: exactly two cells over the 200
discovery claims, each rendering a natural but decision-irrelevant EVIDENCE E.

Material rule (frozen §12, mechanical, zero-model):
  For each claim, the irrelevant text is drawn from the OTHER rows of the
  audited P2 pool (`g24a_p2_pool_v1.csv`, both arms' evidence texts).
  Candidates must (a) come from a different Wikipedia page than the claim,
  and (b) share no content token - lowercased alphabetic tokens of length
  >= 5 - with the claim text or the claim's page name.  Deterministic pick:
  per-claim RNG seeded `Random("20260928:<p2_id>")` shuffling the
  pool-ordered candidates, first hit wins.

Input (committed before any model run):
  data/items/g24a_p2_v1.jsonl     - 400 P2 arm items (claim + real evidence)
  data/items/g24a_p2_pool_v1.csv  - 280 audited pool rows (evidence source)

Carried over verbatim from the P2 plus item: base_context (the claim),
question / output_spec / ADMIT / EXCLUDE wording (module constants),
surface_domain, provenance meta (p2_id, case_id, claim_sha, split,
seed_rank, page, ...).

Replaced deliberately:
  item_id              g24p2_<nnn>       -> g24p4_<nnn>   (link kept in meta)
  critical_evidence    the target's real evidence -> the screened IRRELEVANT
                        text (this field IS rendered by both P4 cells)
  critical_direction   "neutral"          (irrelevant content bears no direction)
  evidence_truth       "irrelevant"       (shown, but not about this claim)
  meta.pilot           "g24a_p4", plus "evidence_shown": True, the irrelevant
                        source row provenance, and the screen descriptor

task_family stays "g24a_vitaminc" (provenance only; both P4 cells dispatch
on the condition name through conditions_g24p4, before the g24a branch).

Read-back verification (asserted here):
  - 200 items, unique ids, no id overlap with discovery / p1 / p2 / p3
  - material rule re-asserted per item (page-disjoint + token-disjoint)
  - irrelevant text byte-identical in both cells' EVIDENCE E block
  - LEAKAGE: the target's own two real evidence texts appear in NEITHER of
    the two P4 prompts (all 200 claims)
  - irrelevant_visible has no RULING; irrelevant_cf carries the P1
    CounterfactualDeletePost constant; rule_char_offset None / int
  - claim block + TASK tail byte-identical across the two cells
  - ids file == item ids, length 200

Output: data/items/g24a_p4_v1.jsonl (200 lines), data/items/g24a_p4_ids.json

Usage: python scripts/build_g24a_p4_items.py
"""
from __future__ import annotations

import csv
import json
import os
import random
import re
import sys
from pathlib import Path

P2_ITEMS = "data/items/g24a_p2_v1.jsonl"
POOL = "data/items/g24a_p2_pool_v1.csv"
OUT = "data/items/g24a_p4_v1.jsonl"
IDS = "data/items/g24a_p4_ids.json"
DISCOVERY = "data/items/g24a_v1.jsonl"
P1_ITEMS = "data/items/g24a_p1_v1.jsonl"
P3_ITEMS = "data/items/g24a_p3_v1.jsonl"

ITEM_KEYS = [
    "item_id", "task_family", "surface_domain", "base_context",
    "critical_evidence", "critical_label", "critical_direction",
    "exclusion_reason", "evidence_truth", "admit_rule", "exclude_rule",
    "question", "output_spec", "memory_question", "rule_probe_question",
    "ground_truth", "meta",
]

KINDS = ["irrelevant_visible", "irrelevant_cf"]

SEED_PREFIX = "20260928:"          # §12 frozen seed string
MIN_TOK = 5                         # §12 frozen token length


def toks(s: str) -> set[str]:
    """§12 content tokens: lowercased alphabetic tokens of length >= 5."""
    return {t for t in re.findall(r"[a-z]+", s.lower()) if len(t) >= MIN_TOK}


def main() -> int:
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
    import schema
    import conditions_g24a as g24a
    import conditions_g24p1 as g24p1
    import conditions_g24p4 as g24p4

    p2 = [json.loads(l) for l in open(P2_ITEMS, encoding="utf-8")]
    assert len(p2) == 400, len(p2)
    plus = [it for it in p2 if it["meta"]["arm"] == "plus"]
    assert len(plus) == 200, len(plus)
    p2_obj = {it["item_id"]: it for it in p2}
    assert len(p2_obj) == 400

    # --- candidate pool, pool file order, both arms per row ----------------
    cands_all = []                      # (p2_id, arm, text, page, claim_sha)
    with open(POOL, encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            for arm in ("s", "r"):
                text = (row[f"evidence_{arm}"] or "").strip()
                assert text, (row["p2_id"], arm)
                cands_all.append((row["p2_id"], arm, text, row["page"],
                                  row["claim_sha"]))
    assert len(cands_all) == 560, len(cands_all)

    out_lines = []
    n_screen_page = n_screen_tok = n_same_row = 0
    for src in plus:
        p2_id = src["meta"]["p2_id"]
        p4_id = "g24p4_" + p2_id.split("_", 1)[1]
        assert p4_id.startswith("g24p4_"), p4_id
        claim = src["base_context"]
        page = src["meta"]["page"]
        claim_sha = src["meta"]["claim_sha"]
        target_set = toks(claim) | toks(page)
        assert target_set, f"claim/page carry no >=5 token: {p4_id}"

        kept = []
        for c in cands_all:
            if c[4] == claim_sha or c[0] == p2_id:      # same claim row
                n_same_row += 1
                continue
            if c[3] == page:                             # (a) page-disjoint
                n_screen_page += 1
                continue
            if toks(c[2]) & target_set:                  # (b) token-disjoint
                n_screen_tok += 1
                continue
            kept.append(c)
        assert kept, f"no irrelevant candidate survives: {p4_id}"

        rng = random.Random(SEED_PREFIX + p2_id)
        rng.shuffle(kept)                                # pool-ordered -> seeded
        src_row = kept[0]
        irr_text, irr_id, irr_arm, irr_page = src_row[2], src_row[0], src_row[1], src_row[3]

        meta = {
            "pilot": "g24a_p4",
            "p2_id": p2_id,
            "source_item_id": src["item_id"],
            "case_id": src["meta"]["case_id"],
            "claim_sha": claim_sha,
            "p2_role": src["meta"]["p2_role"],
            "seed_rank": src["meta"]["seed_rank"],
            "split": src["meta"]["split"],
            "page": page,
            "first_lineno": src["meta"]["first_lineno"],
            "evidence_shown": True,
            "irrelevant_from": {"p2_id": irr_id, "arm": irr_arm,
                                "page": irr_page},
            "screen": "page_disjoint+len5tok_disjoint",
            "seed": SEED_PREFIX + p2_id,
        }
        it = {
            "item_id": p4_id,
            "task_family": "g24a_vitaminc",
            "surface_domain": src["surface_domain"],
            "base_context": claim,
            "critical_evidence": irr_text,
            "critical_label": "evidence E",
            "critical_direction": "neutral",
            "exclusion_reason": g24a.EXCLUSION_REASON,
            "evidence_truth": "irrelevant",
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
    p3_ids = {json.loads(l)["item_id"] for l in open(P3_ITEMS, encoding="utf-8")}
    p2_ids = set(p2_obj)
    assert not ({i.item_id for i in items} & (disc_ids | p1_ids | p3_ids | p2_ids)), \
        "id overlap with earlier pilots"

    n_leak_checks = n_prompt_checks = 0
    for it in items:
        assert it.task_family == "g24a_vitaminc", it.item_id
        assert g24a.is_g24a(it), it.item_id
        assert it.meta["pilot"] == "g24a_p4" and it.meta["evidence_shown"] is True
        assert it.critical_direction == "neutral", it.item_id
        assert it.evidence_truth == "irrelevant", it.item_id
        assert it.question == g24a.QUESTION and it.output_spec == g24a.OUTPUT_SPEC

        # material rule re-asserted (page + token screens)
        assert it.meta["screen"] == "page_disjoint+len5tok_disjoint", it.item_id
        assert it.meta["irrelevant_from"]["page"] != it.meta["page"], it.item_id
        assert not (toks(it.critical_evidence)
                    & (toks(it.base_context) | toks(it.meta["page"]))), it.item_id
        # irrelevant text really comes from the pool, another row
        irr = it.meta["irrelevant_from"]
        assert irr["p2_id"] != it.meta["p2_id"], it.item_id

        src = p2_obj[it.meta["source_item_id"]]
        src_minus = p2_obj[it.meta["p2_id"] + "_minus"]
        assert src["meta"]["arm"] == "plus" and src_minus["meta"]["arm"] == "minus"
        assert it.base_context == src["base_context"], it.item_id

        prompts = {k: schema.compile_prompt(it, k) for k in KINDS}
        n_prompt_checks += len(KINDS)
        # E block byte-identical across the two cells, carrying the text
        blk = g24a.EVIDENCE_HEADER + "\n" + it.critical_evidence
        for k, p in prompts.items():
            assert blk in p, (it.item_id, k, "irrelevant evidence block missing")
            assert "TASK\n" + it.question in p, (it.item_id, k)
        # structure: no ruling / ruling, offsets
        assert schema.rule_char_offset(it, "irrelevant_visible") is None, it.item_id
        assert "RULING" not in prompts["irrelevant_visible"], it.item_id
        off = schema.rule_char_offset(it, "irrelevant_cf")
        assert off is not None and off > 0, (it.item_id, off)
        assert g24p1.CF_DELETE_RULE in prompts["irrelevant_cf"], it.item_id
        # claim block + TASK tail byte-identical across the two cells
        pc, qc = prompts["irrelevant_visible"], prompts["irrelevant_cf"]
        assert pc[:pc.index("\n\n")] == qc[:qc.index("\n\n")], it.item_id
        assert pc[pc.index("TASK\n"):] == qc[qc.index("TASK\n"):], it.item_id
        # the visible cell's whole pre-TASK content == the cf cell's pre-RULING
        # content (the ruling block is the ONLY difference between the cells)
        assert pc[:pc.index("TASK\n")] == qc[:qc.index("RULING\n")], it.item_id
        assert "RULING\n" not in pc and qc.index("RULING\n") > qc.index("EVIDENCE E\n")
        # LEAKAGE: the target's own two real evidence texts render nowhere
        for text in (src["critical_evidence"], src_minus["critical_evidence"]):
            assert text != it.critical_evidence, it.item_id
            for k, p in prompts.items():
                assert text not in p, (it.item_id, k, "real evidence leaked")
            n_leak_checks += 1

    print(f"wrote {OUT}: 200 items (2 cells, no arms), material rule "
          f"page-disjoint + len>={MIN_TOK} token-disjoint, seeded {SEED_PREFIX}<p2_id>")
    print(f"screened: {n_same_row} same-row, {n_screen_page} page, "
          f"{n_screen_tok} token rejections (pool {len(cands_all)} candidates)")
    print(f"wrote {IDS}: 200 ids; run contract: {len(KINDS)} kinds x 200 "
          f"= {len(KINDS) * 200} rows/model")
    print(f"leakage assertions: {n_leak_checks * len(KINDS)} "
          f"(2 real texts x 2 prompts x 200 claims)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
