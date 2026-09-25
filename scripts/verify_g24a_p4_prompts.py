#!/usr/bin/env python3
"""Pre-run verification for Pilot P4 prompts (zero model output read).

Registration §12 (wording + material rule frozen pre-run, user 2026-09-26).
Checks, for all 200 items x 2 conditions = 400 prompts:

   1. compile_prompt succeeds; TASK tail + output spec present
   2. the CF ruling appears VERBATIM as an independent hard-coded copy of
      the user's wording and equals the conditions_g24p1 module constant;
      the run contract equals G24P4_CONDITIONS
   3. structure: irrelevant_visible has EVIDENCE E and NO ruling
      (rule_char_offset None); irrelevant_cf has the ruling AFTER the
      evidence block (rule_char_offset int > 0)
   4. MATERIAL RULE re-asserted independently per item: the rendered
      evidence text is a genuine evidence text of some OTHER row of the
      audited P2 pool; its page differs from the claim's page; its
      length>=5 lowercased alphabetic tokens are disjoint from the claim's
      and page's tokens (fresh recompute, not the build's bookkeeping)
   5. the irrelevant block is byte-identical across the two cells; the
      claim block and TASK tail are byte-identical across both; the
      visible cell's whole pre-TASK content equals the cf cell's
      pre-RULING content (the ruling is the ONLY difference)
   6. LEAKAGE: neither of the target's own real P2 evidence texts
      (evidence_s / evidence_r) appears in ANY of the two P4 prompts —
      all 200 claims; also asserted != the rendered irrelevant text
   7. rule_char_offset: None exactly for irrelevant_visible, int > 0
      exactly for irrelevant_cf
   8. the 2 condition names pass run_model's kind whitelist (incl.
      schema.G24P4_CONDITIONS) and neither is a probe kind
   9. regression: a G24A discovery item still compiles the G0 five
      unchanged; P1 / P2 / P3 cells still render through their unmodified
      modules; no condition name collides across g24p1 / g24p3 / g24p4 /
      g25 / g26
  10. item-level identity: question / output_spec / admit / exclude ==
      module constants; meta.pilot == g24a_p4; evidence_shown is True;
      evidence_truth == "irrelevant"; critical_evidence != the P3
      placeholder and != the target's own evidence texts
  11. id list: 200 ids == item ids, no overlap with p3 / p2 / p1 /
      discovery
  12. run contract bound to scripts/run_g24a_p4.sh: parsed KINDS line ==
      the frozen kind list, id + item paths referenced, rows/model = 400

Usage: python scripts/verify_g24a_p4_prompts.py   (exit 0 = all pass)
"""
from __future__ import annotations

import csv
import json
import os
import re
import sys

ROOT = os.path.join(os.path.dirname(__file__), "..")
sys.path.insert(0, os.path.join(ROOT, "src"))

import schema                                   # noqa: E402
import conditions_g24a as g24a                  # noqa: E402
import conditions_g24p1 as g24p1                # noqa: E402
import conditions_g24p3 as g24p3                # noqa: E402
import conditions_g24p4 as g24p4                # noqa: E402
import conditions_g25 as g25                    # noqa: E402
import conditions_g26a as g26                   # noqa: E402

ITEMS = os.path.join(ROOT, "data", "items", "g24a_p4_v1.jsonl")
IDS = os.path.join(ROOT, "data", "items", "g24a_p4_ids.json")
P2_ITEMS = os.path.join(ROOT, "data", "items", "g24a_p2_v1.jsonl")
P3_ITEMS = os.path.join(ROOT, "data", "items", "g24a_p3_v1.jsonl")
POOL = os.path.join(ROOT, "data", "items", "g24a_p2_pool_v1.csv")
DISCOVERY = os.path.join(ROOT, "data", "items", "g24a_v1.jsonl")

# The frozen run contract (mirrors scripts/run_g24a_p4.sh).
KINDS = ["irrelevant_visible", "irrelevant_cf"]

# Independent copy of the user's verbatim CF ruling (2026-09-25, reused
# verbatim by §12 cell 2).  If the module drifts from the spec, this fails.
SPEC_CF = ("Evaluate the claim exactly as you would have if Evidence E had "
           "never been shown. Reconstruct the judgment you would have made "
           "before encountering Evidence E. Evidence E must have no "
           "influence on the answer in either direction, directly or "
           "indirectly.")


def toks(s: str) -> set[str]:
    """§12 content tokens: lowercased alphabetic tokens of length >= 5."""
    return {t for t in re.findall(r"[a-z]+", s.lower()) if len(t) >= 5}


def main() -> int:
    # --- 2. verbatim ruling + contract -------------------------------------
    assert g24p1.CF_DELETE_RULE == SPEC_CF, "counterfactual wording drifted"
    assert KINDS == g24p4.G24P4_CONDITIONS, "run contract drift"

    items = schema.load_items(ITEMS)
    assert len(items) == 200, len(items)
    p2_items = {it.item_id: it for it in schema.load_items(P2_ITEMS)}
    assert len(p2_items) == 400

    # --- 4. pool index (independent recompute of the material rule) --------
    pool = {}                                     # text -> (p2_id, page)
    with open(POOL, encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            for arm in ("s", "r"):
                pool.setdefault((row[f"evidence_{arm}"] or "").strip(),
                                (row["p2_id"], row["page"]))
    assert len(pool) >= 400, len(pool)

    n = n_material = n_leak = 0
    for it in items:
        # --- 10. item-level identity --------------------------------------
        assert it.task_family == "g24a_vitaminc", it.item_id
        assert g24a.is_g24a(it), it.item_id
        assert it.admit_rule == g24a.ADMIT_RULE, it.item_id
        assert it.exclude_rule == g24a.EXCLUDE_RULE, it.item_id
        assert it.question == g24a.QUESTION, it.item_id
        assert it.output_spec == g24a.OUTPUT_SPEC, it.item_id
        assert it.critical_evidence != g24p3.WITHHELD_CONTENT, it.item_id
        assert it.meta["pilot"] == "g24a_p4", it.item_id
        assert it.meta["evidence_shown"] is True, it.item_id
        assert it.evidence_truth == "irrelevant", it.item_id
        assert it.critical_direction == "neutral", it.item_id

        src = p2_items[it.meta["source_item_id"]]
        src_m = p2_items[it.meta["p2_id"] + "_minus"]
        assert it.base_context == src.base_context, it.item_id
        real_texts = (src.critical_evidence, src_m.critical_evidence)
        assert real_texts[0] != real_texts[1]

        # --- 4. material rule, independent recompute -----------------------
        hit = pool.get(it.critical_evidence)
        assert hit is not None, (it.item_id, "not a pool evidence text")
        assert hit[0] != it.meta["p2_id"], (it.item_id, "own row")
        assert hit[1] != it.meta["page"], (it.item_id, "same page")
        assert hit[1] == it.meta["irrelevant_from"]["page"], it.item_id
        tgt = toks(it.base_context) | toks(it.meta["page"])
        assert tgt, it.item_id
        assert not (toks(it.critical_evidence) & tgt), \
            (it.item_id, "token overlap with claim/page")
        n_material += 1

        prompts = {k: schema.compile_prompt(it, k) for k in KINDS}
        for k, p in prompts.items():
            # --- 1. TASK tail ---------------------------------------------
            assert "TASK\n" + it.question in p, (it.item_id, k)
            assert it.output_spec in p, (it.item_id, k)
            # --- 6. leakage -----------------------------------------------
            for text in real_texts:
                assert text not in p, (it.item_id, k, "real evidence leaked")
            n_leak += 1

        # --- 3./7. structure per cell -------------------------------------
        p_v, p_c = prompts["irrelevant_visible"], prompts["irrelevant_cf"]
        assert schema.rule_char_offset(it, "irrelevant_visible") is None, it.item_id
        assert "RULING" not in p_v, it.item_id
        off = schema.rule_char_offset(it, "irrelevant_cf")
        assert off is not None and off > 0, (it.item_id, off)

        # --- 5. block identity --------------------------------------------
        blk = g24a.EVIDENCE_HEADER + "\n" + it.critical_evidence
        for k, p in prompts.items():
            assert blk in p, (it.item_id, k)
            i_c, i_e = p.index("CLAIM\n"), p.index("EVIDENCE E\n")
            assert i_c < i_e, (it.item_id, k)
        i_r = p_c.index("RULING\n")
        assert i_r > p_c.index("EVIDENCE E\n"), it.item_id
        assert SPEC_CF in p_c, it.item_id
        # claim block identical across both cells; TASK tail identical
        assert p_v[:p_v.index("\n\n")] == p_c[:p_c.index("\n\n")], it.item_id
        assert p_v[p_v.index("TASK\n"):] == p_c[p_c.index("TASK\n"):], it.item_id
        # visible's whole pre-TASK content == cf's pre-RULING content
        assert p_v[:p_v.index("TASK\n")] == p_c[:i_r], it.item_id
        n += 1

    assert n == 200, n  # one iteration per item, both cells compiled

    # --- 8. kind whitelist --------------------------------------------------
    lists = [schema.CONDITIONS, schema.EXTRA_CONDITIONS, schema.V2_CONDITIONS,
             schema.V3_CONDITIONS, schema.V4_CONDITIONS, schema.ROUTING_CONDITIONS,
             schema.V5_CONDITIONS, schema.LINEAR_CONDITIONS, schema.V6_CONDITIONS,
             schema.V7_CONDITIONS, schema.G17_CONDITIONS, schema.G18_CONDITIONS,
             schema.G23A_CONDITIONS, schema.G23B_CONDITIONS, schema.G25A_CONDITIONS,
             schema.G26A_CONDITIONS, schema.G24P1_CONDITIONS, schema.G24P3_CONDITIONS,
             schema.G24P4_CONDITIONS, schema.AGENT_CONDITIONS,
             schema.EXT_CONDITIONS, schema.PROBES]
    for k in KINDS:
        assert any(k in lst for lst in lists), f"{k} not in run_model whitelist"
        assert k not in schema.PROBES, f"{k} must not be a probe kind"

    # --- 9. regression: earlier pilots unchanged ---------------------------
    disc = schema.load_items(DISCOVERY)
    for k in ["base", "admit_pre", "admit_post", "exclude_pre", "exclude_post"]:
        assert schema._blocks(disc[0], k) == g24a.blocks(disc[0], k), k
        schema.compile_prompt(disc[0], k)
    for src_id in ("g24p2_000_plus", "g24p2_000_minus"):
        it2 = p2_items.get(src_id)
        if it2 is None:
            continue
        for k in ("base", "admit_post", "exclude_post"):
            assert schema._blocks(it2, k) == g24a.blocks(it2, k), (src_id, k)
        for k in ("strong_exclude_post", "counterfactual_delete_post"):
            assert schema._blocks(it2, k) == g24p1.blocks(it2, k), (src_id, k)
        schema.compile_prompt(it2, "counterfactual_delete_post")
    p3_items = schema.load_items(P3_ITEMS)
    for k in g24p3.G24P3_CONDITIONS:
        assert schema._blocks(p3_items[0], k) == g24p3.blocks(p3_items[0], k), k
        schema.compile_prompt(p3_items[0], k)
    # no name collisions in either direction
    for k in ["base", "exclude_post", "counterfactual_delete_post",
              "g25_w000_post", "g26_admit_t0"] + g24p3.G24P3_CONDITIONS:
        assert not g24p4.is_g24p4(k), k
    for k in KINDS:
        assert not g24p1.is_g24p1(k), k
        assert not g24p3.is_g24p3(k), k
        assert not g25.is_g25(k), k
        assert not g26.is_g26(k), k

    # --- 11. id list --------------------------------------------------------
    ids = json.load(open(IDS))
    all_ids = {it.item_id for it in items}
    assert len(ids) == 200 and len(set(ids)) == 200, len(ids)
    assert set(ids) == all_ids, "id list != item ids"
    earlier = set(p2_items) | {i.item_id for i in p3_items}
    earlier |= {json.loads(l)["item_id"] for l in open(DISCOVERY, encoding="utf-8")}
    earlier |= {json.loads(l)["item_id"] for l in
                open(os.path.join(ROOT, "data", "items", "g24a_p1_v1.jsonl"),
                     encoding="utf-8")}
    assert not (set(ids) & earlier), "id overlap with earlier files"
    assert all(i.startswith("g24p4_") for i in ids), ids[:3]

    # --- 12. run contract bound to the run script --------------------------
    run_sh = os.path.join(ROOT, "scripts", "run_g24a_p4.sh")
    text = open(run_sh, encoding="utf-8").read()
    m = re.search(r"^KINDS=(\S+)$", text, re.M)
    assert m, "run script kind list not found"
    assert m.group(1).split(",") == KINDS, "run script KINDS drift"
    assert "data/items/g24a_p4_ids.json" in text, "run script id path drift"
    assert "data/items/g24a_p4_v1.jsonl" in text, "run script item path drift"
    assert "_g24a_p4${SUF}.jsonl" in text, "run script output pattern drift"

    print(f"OK: {len(KINDS)} prompts x 200 items = {len(KINDS) * 200} prompts "
          f"verified; {n_leak} prompts leakage-checked ({n_leak * 2} "
          f"assertions); material rule re-asserted for {n_material}/200 items")
    print("CF ruling verbatim (P1 module constant); block layout: "
          "irrelevant_visible no ruling, irrelevant_cf ruling after evidence; "
          "claim block + TASK tail identical across both cells")
    print(f"run contract: 200 ids x {len(KINDS)} kinds = "
          f"{200 * len(KINDS)} rows/model -> 2,000 rows (5 models)")
    print("regression: G24A discovery + P1/P2/P3 cells unchanged, no condition "
          "name collisions (g24p1 / g24p3 / g24p4 / g25 / g26)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
