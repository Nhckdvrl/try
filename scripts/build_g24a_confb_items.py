#!/usr/bin/env python3
"""Build the Confirmation-B item file: 200 fresh claims x 3 arms = 600 items.

Registration §13.3 (frozen, user ruling 2026-09-26).  Inputs (all
committed before any model run):

  data/items/g24a_confb_selected_v1.jsonl  - 200 valid SR pairs (134 kept
      actives + 66 same-source reserve swaps; merge verified that every
      blind supports-side maps through the review rendering to
      evidence_s, i.e. dataset orientation agrees with the blind call)
  data/items/g24a_p2_pool_v1.csv           - the audited P2 pool: the
      candidate source for the control arm's irrelevant text (§12
      material rule, referenced by §13.3)

Arms / cells (7 cells per claim, frozen §13.3):
  plus    : critical_evidence = evidence_s, critical_direction increase
            cells: base, admit_post, counterfactual_delete_post,
                   withheld_cf
  minus   : critical_evidence = evidence_r, critical_direction decrease
            cells: admit_post, counterfactual_delete_post
  control : critical_evidence = screened irrelevant text (§12 rule,
            seed "20260929:<cfb_id>" - the §12 template's per-claim id
            slot filled with this confirmation's claim id), direction
            neutral, evidence_truth "irrelevant"
            cells: irrelevant_cf

`withheld_cf` is arm-free by construction (conditions_g24p3 never reads
critical_evidence; its blocks depend on the claim only), so it is issued
on `plus` exactly as §13.3 anchors `base` on plus.  Run contract:
(4 + 2 + 1) cells = 7 cells/claim -> 200 x 7 x 6 models = 8,400 rows.

task_family "g24a_vitaminc" routes base/admit_post through the
unmodified G24A module, counterfactual_delete_post through
conditions_g24p1, withheld_cf through conditions_g24p3, irrelevant_cf
through conditions_g24p4 (condition-name dispatch proven in P1-P4; no
wording is re-implemented here).

Material rule (§12 as amended by §13.3): candidates = the other rows of
the audited P2 pool (both arms' evidence texts); must (a) come from a
different page than the target claim, (b) share no content token
(lowercased alphabetic tokens of length >= 5) with the claim text or the
page name, (c) not be the target's claim row; deterministic pick:
Random("20260929:<cfb_id>") shuffling the pool-ordered survivors, first
hit wins.  The target's own two real evidence texts are asserted absent
from every control prompt (leakage check).

Read-back verification (asserted here):
  - 600 items, unique g24cfb_* ids, no id overlap with any item file
    ever rendered (discovery / p1 / p2 / p3 / p4 / confa)
  - 200 groups x {plus, minus, control}; shared claim/question/rules;
    the only arm differences are evidence, direction, evidence_truth
  - base prompt byte-identical across all three arms (shared Y0) and
    never renders an EVIDENCE E block
  - admit_post / counterfactual_delete_post render exactly their own
    arm's evidence block + TASK tail
  - withheld_cf byte-identical across arms, carries the P1 CF_DELETE
    ruling, and contains neither real evidence nor the irrelevant text
  - irrelevant_cf renders the irrelevant text + CF ruling and contains
    neither of the target's real evidence texts
  - material rule re-asserted per control item (page + token screens,
    seed string)
  - id files 200/200/200, disjoint, union = 600

Outputs:
  data/items/g24a_confb_v1.jsonl
  data/items/g24a_confb_ids_{plus,minus,control}.json

Usage: python scripts/build_g24a_confb_items.py
"""
from __future__ import annotations

import csv
import json
import os
import random
import re
import sys
from pathlib import Path

SELECTED = "data/items/g24a_confb_selected_v1.jsonl"
P2_POOL = "data/items/g24a_p2_pool_v1.csv"
OUT = "data/items/g24a_confb_v1.jsonl"
IDS_PLUS = "data/items/g24a_confb_ids_plus.json"
IDS_MINUS = "data/items/g24a_confb_ids_minus.json"
IDS_CONTROL = "data/items/g24a_confb_ids_control.json"
PRIOR_ITEMS = (
    "data/items/g24a_v1.jsonl",          # discovery
    "data/items/g24a_p1_v1.jsonl",
    "data/items/g24a_p2_v1.jsonl",
    "data/items/g24a_p3_v1.jsonl",
    "data/items/g24a_p4_v1.jsonl",
    "data/items/g24a_confa_v1.jsonl",
)

TASK_FAMILY = "g24a_vitaminc"

ITEM_KEYS = [
    "item_id", "task_family", "surface_domain", "base_context",
    "critical_evidence", "critical_label", "critical_direction",
    "exclusion_reason", "evidence_truth", "admit_rule", "exclude_rule",
    "question", "output_spec", "memory_question", "rule_probe_question",
    "ground_truth", "meta",
]

# run contract (§13.3's 7 cells, anchored per above); the verifier parses
# the matching KINDS_* lines out of scripts/run_g24a_confb.sh — keep in sync
KINDS_PLUS = ["base", "admit_post", "counterfactual_delete_post", "withheld_cf"]
KINDS_MINUS = ["admit_post", "counterfactual_delete_post"]
KINDS_CONTROL = ["irrelevant_cf"]

SEED_PREFIX = "20260929:"   # §13.3 amendment (P4's §12 seed 20260928 untouched)
MIN_TOK = 5                 # §12 frozen token length


def toks(s: str) -> set[str]:
    """§12 content tokens: lowercased alphabetic tokens of length >= 5."""
    return {t for t in re.findall(r"[a-z]+", s.lower()) if len(t) >= MIN_TOK}


def main() -> int:
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))
    import schema
    import conditions_g24a as g24a
    import conditions_g24p1 as g24p1
    import conditions_g24p3 as g24p3
    import conditions_g24p4 as g24p4

    sel = [json.loads(l) for l in open(SELECTED, encoding="utf-8")]
    assert len(sel) == 200, len(sel)
    assert len({r["cfb_id"] for r in sel}) == 200
    assert len({r["claim_sha"] for r in sel}) == 200
    assert len({r["case_id"] for r in sel}) == 200

    # --- candidate pool for the irrelevant text (both arms of each row) ----
    cands_all = []                      # (p2_id, arm, text, page, claim_sha)
    with open(P2_POOL, encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            for arm in ("s", "r"):
                text = (row[f"evidence_{arm}"] or "").strip()
                assert text, (row["p2_id"], arm)
                cands_all.append((row["p2_id"], arm, text, row["page"],
                                  row["claim_sha"]))
    assert len(cands_all) == 560, len(cands_all)

    out_lines = []
    n_same_row = n_page = n_tok = 0
    for e in sel:
        cfb = e["cfb_id"]
        assert e["meta"]["blind_call"] == "A", \
            (cfb, "orientation re-assert: blind A must map to evidence_s")
        claim = e["claim"]
        page = e["page"]
        # §12's token screen is applied exactly as frozen: candidates must
        # share no >=5-content-token with the claim/page.  g24cfb_015
        # ("MC Eiht was born in 1971 ." / page "MC Eiht") carries no >=5
        # alphabetic token, so that ONE claim's token screen is vacuous -
        # the rule as written still holds (no shared token exists to share)
        # and the page screen remains in force.  Non-emptiness is NOT
        # asserted: that would add a rule beyond §12.
        target_set = toks(claim) | toks(page)

        # ---- §12 material rule for the control arm ------------------------
        kept = []
        for c in cands_all:
            if c[4] == e["claim_sha"]:          # same claim row
                n_same_row += 1
                continue
            if c[3] == page:                    # (a) page-disjoint
                n_page += 1
                continue
            if toks(c[2]) & target_set:         # (b) token-disjoint
                n_tok += 1
                continue
            kept.append(c)
        assert kept, f"no irrelevant candidate survives: {cfb}"

        rng = random.Random(SEED_PREFIX + cfb)  # §13.3's frozen seed string
        rng.shuffle(kept)
        src_row = kept[0]
        irr_text, irr_id, irr_arm, irr_page = (src_row[2], src_row[0],
                                               src_row[1], src_row[3])
        # the target's own real evidence is never eligible as "irrelevant"
        assert irr_text not in (e["evidence_s"], e["evidence_r"]), cfb

        meta_common = {
            "pilot": "g24a_confb",
            "cfb_id": cfb,
            "case_id": e["case_id"],
            "claim_sha": e["claim_sha"],
            "confb_role": e["meta"]["confb_role"],
            "confb_seed_rank": e["meta"]["confb_seed_rank"],
            "blind_call": e["meta"]["blind_call"],
            "blind_note": e["meta"]["blind_note"],
            "split": e["split"],
            "page": page,
            "first_lineno": int(e["first_lineno"]),
        }
        if "confb_replaced_seed_rank" in e["meta"]:
            meta_common["confb_replaced_seed_rank"] = \
                e["meta"]["confb_replaced_seed_rank"]
            meta_common["confb_replaced_cfb_id"] = \
                e["meta"]["confb_replaced_cfb_id"]

        arms = (
            ("plus", e["evidence_s"], "increase", g24a.EVIDENCE_TRUTH,
             "evidence_s"),
            ("minus", e["evidence_r"], "decrease", g24a.EVIDENCE_TRUTH,
             "evidence_r"),
            ("control", irr_text, "neutral", "irrelevant", "irrelevant"),
        )
        for arm, ev, direction, truth, field in arms:
            meta = dict(meta_common)
            meta["arm"] = arm
            meta["evidence_field"] = field
            if arm == "control":
                meta["evidence_shown"] = True
                meta["irrelevant_from"] = {"p2_id": irr_id, "arm": irr_arm,
                                           "page": irr_page}
                meta["screen"] = "page_disjoint+len5tok_disjoint"
                meta["seed"] = SEED_PREFIX + cfb
            it = {
                "item_id": f"{cfb}_{arm}",
                "task_family": TASK_FAMILY,
                "surface_domain": "wikipedia",
                "base_context": claim,
                "critical_evidence": ev,
                "critical_label": "evidence E",
                "critical_direction": direction,
                "exclusion_reason": g24a.EXCLUSION_REASON,
                "evidence_truth": truth,
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

    ids = {arm: [it["item_id"] for it in out_lines
                 if it["meta"]["arm"] == arm]
           for arm in ("plus", "minus", "control")}
    Path(IDS_PLUS).write_text(json.dumps(ids["plus"], indent=1) + "\n")
    Path(IDS_MINUS).write_text(json.dumps(ids["minus"], indent=1) + "\n")
    Path(IDS_CONTROL).write_text(json.dumps(ids["control"], indent=1) + "\n")

    # --- read-back verification -------------------------------------------
    items = schema.load_items(OUT)
    assert len(items) == 600, len(items)
    assert len({i.item_id for i in items}) == 600, "duplicate item ids"
    for arm in ids:
        assert len(ids[arm]) == 200, (arm, len(ids[arm]))
    assert not (set(ids["plus"]) & set(ids["minus"]))
    assert not (set(ids["plus"]) & set(ids["control"]))
    assert not (set(ids["minus"]) & set(ids["control"]))
    assert set().union(*map(set, ids.values())) == {i.item_id for i in items}

    prior = set()
    for p in PRIOR_ITEMS:
        prior |= {json.loads(l)["item_id"] for l in open(p, encoding="utf-8")}
    assert not ({i.item_id for i in items} & prior), "id overlap with past runs"

    # condition-name routing (dispatch order proven in P1-P4)
    assert g24p1.is_g24p1("counterfactual_delete_post")
    assert g24p3.is_g24p3("withheld_cf")
    assert g24p4.is_g24p4("irrelevant_cf")
    assert not g24p1.is_g24p1("admit_post")
    assert not g24p3.is_g24p3("base")

    groups = {}
    for it in items:
        assert it.meta["pilot"] == "g24a_confb", it.item_id
        assert it.item_id.startswith("g24cfb_"), it.item_id
        assert it.task_family == TASK_FAMILY, it.item_id
        assert g24a.is_g24a(it), it.item_id      # unmodified G24A module
        assert it.question == g24a.QUESTION and it.output_spec == g24a.OUTPUT_SPEC
        assert it.admit_rule == g24a.ADMIT_RULE
        assert it.exclude_rule == g24a.EXCLUDE_RULE
        groups.setdefault(it.meta["cfb_id"], []).append(it)
    assert len(groups) == 200, len(groups)

    n_base = n_arm = n_irrel = n_leak = 0
    for cfb, g in groups.items():
        assert len(g) == 3, cfb
        by_arm = {i.meta["arm"]: i for i in g}
        assert set(by_arm) == {"plus", "minus", "control"}, cfb
        pm, mm, cc = by_arm["plus"], by_arm["minus"], by_arm["control"]

        # shared everything but the evidence block
        for other in (mm, cc):
            assert pm.base_context == other.base_context, cfb
            assert pm.question == other.question, cfb
            assert pm.output_spec == other.output_spec, cfb
            assert pm.admit_rule == other.admit_rule, cfb
            assert pm.exclude_rule == other.exclude_rule, cfb
            assert pm.meta["claim_sha"] == other.meta["claim_sha"], cfb
            assert pm.meta["case_id"] == other.meta["case_id"], cfb
        assert pm.critical_evidence != mm.critical_evidence, cfb
        assert cc.critical_evidence not in (pm.critical_evidence,
                                            mm.critical_evidence), cfb
        assert (pm.critical_direction, mm.critical_direction,
                cc.critical_direction) == ("increase", "decrease",
                                           "neutral"), cfb
        assert cc.evidence_truth == "irrelevant", cfb
        assert pm.evidence_truth == g24a.EVIDENCE_TRUTH, cfb

        # base: byte-identical across ALL three arms (shared Y0), evidence-free
        bases = [schema.compile_prompt(x, "base") for x in (pm, mm, cc)]
        assert bases[0] == bases[1] == bases[2], f"base differs: {cfb}"
        assert "EVIDENCE E\n" not in bases[0], f"base not evidence-free: {cfb}"
        n_base += 1

        # arm cells render exactly their own arm's evidence block
        for cond in ("admit_post", "counterfactual_delete_post"):
            for item in (pm, mm):
                p = schema.compile_prompt(item, cond)
                got = (p.split("EVIDENCE E\n", 1)[1]
                       .split("\n\nRULING\n", 1)[0])
                assert got == item.critical_evidence, (item.item_id, cond)
                assert "TASK\n" + item.question in p, (item.item_id, cond)
                n_arm += 1

        # withheld_cf: content-free, byte-identical across arms, zero leakage
        w = [schema.compile_prompt(x, "withheld_cf") for x in (pm, mm, cc)]
        assert w[0] == w[1] == w[2], f"withheld_cf differs: {cfb}"
        assert g24p1.CF_DELETE_RULE in w[0], cfb
        for text in (pm.critical_evidence, mm.critical_evidence,
                     cc.critical_evidence):
            assert text not in w[0], (cfb, "withheld_cf leak")
            n_leak += 1

        # irrelevant_cf: renders the irrelevant text + CF ruling; no leakage
        p_icf = schema.compile_prompt(cc, "irrelevant_cf")
        blk = g24a.EVIDENCE_HEADER + "\n" + cc.critical_evidence
        assert blk in p_icf, (cfb, "irrelevant evidence block missing")
        assert g24p1.CF_DELETE_RULE in p_icf, cfb
        off = schema.rule_char_offset(cc, "irrelevant_cf")
        assert off is not None and off > 0, (cfb, off)
        assert "TASK\n" + cc.question in p_icf, cfb
        for text in (pm.critical_evidence, mm.critical_evidence):
            assert text not in p_icf, (cfb, "real evidence leaked")
            n_leak += 1
        n_irrel += 1

        # material rule re-asserted (page + token screens, seed string)
        assert cc.meta["screen"] == "page_disjoint+len5tok_disjoint", cfb
        assert cc.meta["irrelevant_from"]["page"] != cc.meta["page"], cfb
        assert not (toks(cc.critical_evidence)
                    & (toks(cc.base_context) | toks(cc.meta["page"]))), cfb
        assert cc.meta["seed"] == SEED_PREFIX + cfb, cfb

    assert n_base == 200, n_base
    assert n_arm == 200 * 2 * 2, n_arm
    assert n_irrel == 200, n_irrel

    rows_per_model = sum(len(k) * 200 for k in
                         (KINDS_PLUS, KINDS_MINUS, KINDS_CONTROL))
    assert rows_per_model == 200 * 7, rows_per_model
    print(f"wrote {OUT}: 600 items / 200 claims x 3 arms "
          f"(task_family={TASK_FAMILY})")
    print(f"material rule: page-disjoint + len>={MIN_TOK} token-disjoint, "
          f"seeded {SEED_PREFIX}<cfb_id>; screened {n_same_row} same-row, "
          f"{n_page} page, {n_tok} token rejections (pool {len(cands_all)})")
    print(f"wrote {IDS_PLUS} + {IDS_MINUS} + {IDS_CONTROL}: 200 ids each, "
          f"disjoint, union = 600")
    print(f"run contract: plus {KINDS_PLUS} / minus {KINDS_MINUS} / "
          f"control {KINDS_CONTROL} -> {rows_per_model} rows/model "
          f"-> {rows_per_model * 6:,} rows (6 models)")
    print(f"prompt checks: {n_base} base, {n_arm} arm-cell evidence blocks, "
          f"{n_irrel} irrelevant_cf, {n_leak} leakage assertions")
    return 0


if __name__ == "__main__":
    sys.exit(main())
