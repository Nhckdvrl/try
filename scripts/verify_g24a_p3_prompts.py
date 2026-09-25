#!/usr/bin/env python3
"""Pre-run verification for Pilot P3 prompts (zero model output read).

Registration §11 (wording frozen pre-run, user 2026-09-26).  Checks, for
all 200 items x 5 conditions = 1,000 prompts:

   1. compile_prompt succeeds; TASK tail present (question + output spec)
   2. the four frozen wordings appear VERBATIM — independent hard-coded
      copies of the user's spec; if a module constant drifts, this fails:
      prior_only note, [Content unavailable.] placeholder, and the P1/P2
      StrongExcludePost / CounterfactualDeletePost rulings (which must also
      still equal the conditions_g24p1 module constants byte-for-byte)
   3. block order: CLAIM first; EVIDENCE E after CLAIM in the three
      withheld cells; RULING last in the two ruling cells; prior_only has
      NO evidence block and NO ruling; withheld_only has no ruling
   4. base is byte-identical to the P2 item's base prompt for the same
      claim (the re-run contract) and contains no EVIDENCE E / RULING
   5. the withheld block is byte-identical across withheld_only /
      withheld_strong / withheld_cf; the claim block and TASK tail are
      byte-identical across ALL five cells (the ruling is the only
      difference between the two ruling cells)
   6. LEAKAGE: neither arm's real P2 evidence text (evidence_s /
      evidence_r) appears in ANY of the five P3 prompts — all 200 claims,
      2,000 assertions
   7. rule_char_offset: None for base / prior_only / withheld_only,
      points at the RULING block for withheld_strong / withheld_cf
   8. the 5 condition names pass run_model's kind whitelist (incl.
      schema.G24P3_CONDITIONS) and none is a probe kind
   9. regression: a G24A discovery item still compiles the G0 five
      unchanged; a P2 item's own cells still render through the unmodified
      G24A / G24P1 modules; no condition name collides across
      g24p1 / g24p3 / g25 / g26
  10. item-level identity: question / output_spec / admit / exclude ==
      module constants; meta.pilot == g24a_p3; evidence_shown is False;
      critical_evidence == the placeholder (the P3 blocks do not read it)
  11. id list: 200 ids == item ids, no overlap with p2 / p1 / discovery
  12. run contract bound to scripts/run_g24a_p3.sh: parsed KINDS line ==
      the frozen kind list (base first), the id path referenced,
      rows/model = 1,000

Usage: python scripts/verify_g24a_p3_prompts.py   (exit 0 = all pass)
"""
from __future__ import annotations

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
import conditions_g25 as g25                    # noqa: E402
import conditions_g26a as g26                   # noqa: E402

ITEMS = os.path.join(ROOT, "data", "items", "g24a_p3_v1.jsonl")
IDS = os.path.join(ROOT, "data", "items", "g24a_p3_ids.json")
P2_ITEMS = os.path.join(ROOT, "data", "items", "g24a_p2_v1.jsonl")
DISCOVERY = os.path.join(ROOT, "data", "items", "g24a_v1.jsonl")

# The frozen run contract (mirrors scripts/run_g24a_p3.sh).
KINDS = ["base", "prior_only", "withheld_only", "withheld_strong",
         "withheld_cf"]

# Independent copies of the user's verbatim wordings (2026-09-26).  If the
# module drifts from the spec, these comparisons fail.
SPEC_PRIOR_ONLY = ("No additional evidence is available. Judge the claim "
                   "using only your existing/background knowledge.")
SPEC_WITHHELD = "[Content unavailable.]"
# 2026-09-25 operator wordings, reused verbatim (registration §11 cells 4-5)
SPEC_STRONG = ("Evidence E is inadmissible. Completely disregard it when "
               "judging the claim. It must have no influence on your "
               "judgment in either direction, directly or indirectly. "
               "Judge the claim using only information available without "
               "relying on Evidence E.")
SPEC_CF = ("Evaluate the claim exactly as you would have if Evidence E had "
           "never been shown. Reconstruct the judgment you would have made "
           "before encountering Evidence E. Evidence E must have no "
           "influence on the answer in either direction, directly or "
           "indirectly.")


def main() -> int:
    # --- 2. verbatim wordings --------------------------------------------
    assert g24p3.PRIOR_ONLY_NOTE == SPEC_PRIOR_ONLY, "prior_only wording drifted"
    assert g24p3.WITHHELD_CONTENT == SPEC_WITHHELD, "placeholder drifted"
    assert g24p1.STRONG_EXCLUDE_RULE == SPEC_STRONG, "strong wording drifted"
    assert g24p1.CF_DELETE_RULE == SPEC_CF, "counterfactual wording drifted"
    assert KINDS[1:] == g24p3.G24P3_CONDITIONS, "run contract drift"

    items = schema.load_items(ITEMS)
    assert len(items) == 200, len(items)
    p2_items = {it.item_id: it for it in schema.load_items(P2_ITEMS)}
    assert len(p2_items) == 400

    n = 0
    for it in items:
        # --- 10. item-level identity -------------------------------------
        assert it.task_family == "g24a_vitaminc", it.item_id
        assert g24a.is_g24a(it), it.item_id
        assert it.admit_rule == g24a.ADMIT_RULE, it.item_id
        assert it.exclude_rule == g24a.EXCLUDE_RULE, it.item_id
        assert it.question == g24a.QUESTION, it.item_id
        assert it.output_spec == g24a.OUTPUT_SPEC, it.item_id
        assert it.critical_evidence == g24p3.WITHHELD_CONTENT, it.item_id
        assert it.meta["pilot"] == "g24a_p3", it.item_id
        assert it.meta["evidence_shown"] is False, it.item_id

        src = p2_items[it.meta["source_item_id"]]
        src_m = p2_items[it.meta["p2_id"] + "_minus"]
        assert it.base_context == src.base_context, it.item_id
        real_texts = (src.critical_evidence, src_m.critical_evidence)
        assert real_texts[0] != real_texts[1]

        prompts = {k: schema.compile_prompt(it, k) for k in KINDS}
        for k, p in prompts.items():
            # --- 1. TASK tail --------------------------------------------
            assert "TASK\n" + it.question in p, (it.item_id, k)
            assert it.output_spec in p, (it.item_id, k)
            # --- 6. leakage ----------------------------------------------
            for text in real_texts:
                assert text not in p, (it.item_id, k, "real evidence leaked")
            n += 1

        # --- 3./7. structure per cell ------------------------------------
        for k in ("base", "prior_only"):
            assert schema.rule_char_offset(it, k) is None, (it.item_id, k)
            assert "RULING" not in prompts[k], (it.item_id, k)
            assert "EVIDENCE E\n" not in prompts[k], (it.item_id, k, "no evidence block")
        assert schema.rule_char_offset(it, "withheld_only") is None, it.item_id
        assert "RULING" not in prompts["withheld_only"], it.item_id

        # --- 4. base byte-identical to P2's base for this claim ----------
        assert prompts["base"] == schema.compile_prompt(src, "base"), \
            f"base not byte-identical to P2: {it.item_id}"

        # --- 5. withheld block + claim/tail identity ---------------------
        blk = g24a.EVIDENCE_HEADER + "\n" + SPEC_WITHHELD
        heads = []
        for k in ("withheld_only", "withheld_strong", "withheld_cf"):
            assert blk in prompts[k], (it.item_id, k)
            i_c = prompts[k].index("CLAIM\n")
            i_e = prompts[k].index("EVIDENCE E\n")
            assert i_c < i_e, (it.item_id, k)
            heads.append(prompts[k][:i_e + len(blk)])
        assert heads[0] == heads[1] == heads[2], f"withheld head differs: {it.item_id}"
        for k in ("withheld_strong", "withheld_cf"):
            off = schema.rule_char_offset(it, k)
            assert off is not None and off > 0, (it.item_id, k, off)
            i_e_k = prompts[k].index("EVIDENCE E\n")
            i_r = prompts[k].index("RULING\n")
            assert i_e_k < i_r, (it.item_id, k)
        assert SPEC_STRONG in prompts["withheld_strong"], it.item_id
        assert SPEC_CF in prompts["withheld_cf"], it.item_id
        # claim block byte-identical across ALL five cells; TASK tail too
        claim_blocks = []
        for k, p in prompts.items():
            claim_blocks.append(p[:p.index("\n\n")])
        assert len(set(claim_blocks)) == 1, f"claim block differs: {it.item_id}"
        tails = [p[p.index("TASK\n"):] for p in prompts.values()]
        assert len(set(tails)) == 1, f"TASK tail differs: {it.item_id}"
        # the two ruling cells differ ONLY by the ruling string
        p_s, p_c = prompts["withheld_strong"], prompts["withheld_cf"]
        assert p_s[:p_s.index("RULING\n")] == p_c[:p_c.index("RULING\n")]
        rs = p_s[p_s.index("RULING\n"):p_s.index("TASK\n")]
        rc = p_c[p_c.index("RULING\n"):p_c.index("TASK\n")]
        assert rs != rc and len(rs) > 10 and len(rc) > 10

    assert n == 1000, n  # 200 items x 5 kinds (leakage checked per prompt)

    # --- 8. kind whitelist -----------------------------------------------
    lists = [schema.CONDITIONS, schema.EXTRA_CONDITIONS, schema.V2_CONDITIONS,
             schema.V3_CONDITIONS, schema.V4_CONDITIONS, schema.ROUTING_CONDITIONS,
             schema.V5_CONDITIONS, schema.LINEAR_CONDITIONS, schema.V6_CONDITIONS,
             schema.V7_CONDITIONS, schema.G17_CONDITIONS, schema.G18_CONDITIONS,
             schema.G23A_CONDITIONS, schema.G23B_CONDITIONS, schema.G25A_CONDITIONS,
             schema.G26A_CONDITIONS, schema.G24P1_CONDITIONS, schema.G24P3_CONDITIONS,
             schema.AGENT_CONDITIONS, schema.EXT_CONDITIONS, schema.PROBES]
    for k in KINDS:
        assert any(k in lst for lst in lists), f"{k} not in run_model whitelist"
        assert k not in schema.PROBES, f"{k} must not be a probe kind"

    # --- 9. regression: earlier pilots unchanged --------------------------
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
    # no name collisions in either direction
    for k in ["base", "exclude_post", "strong_exclude_post",
              "counterfactual_delete_post", "g25_w000_post", "g26_admit_t0"]:
        assert not g24p3.is_g24p3(k), k
    for k in KINDS[1:]:
        assert not g24p1.is_g24p1(k), k
        assert not g25.is_g25(k), k
        assert not g26.is_g26(k), k

    # --- 11. id list -------------------------------------------------------
    ids = json.load(open(IDS))
    all_ids = {it.item_id for it in items}
    assert len(ids) == 200 and len(set(ids)) == 200, len(ids)
    assert set(ids) == all_ids, "id list != item ids"
    p2_ids = {i.item_id for i in p2_items.values()}
    assert not (set(ids) & p2_ids), "id overlap with P2"
    assert all(i.startswith("g24p3_") for i in ids), ids[:3]

    # --- 12. run contract bound to the run script -------------------------
    run_sh = os.path.join(ROOT, "scripts", "run_g24a_p3.sh")
    text = open(run_sh, encoding="utf-8").read()
    m = re.search(r"^KINDS=(\S+)$", text, re.M)
    assert m, "run script kind list not found"
    assert m.group(1).split(",") == KINDS, "run script KINDS drift"
    assert "data/items/g24a_p3_ids.json" in text, "run script id path drift"
    assert "data/items/g24a_p3_v1.jsonl" in text, "run script item path drift"
    assert "_g24a_p3${SUF}.jsonl" in text, "run script output pattern drift"

    print(f"OK: {n} prompts verified (200 items x {len(KINDS)} kinds); "
          f"{n * 2} leakage assertions (2 real texts per prompt)")
    print("wordings verbatim (prior_only note, [Content unavailable.], "
          "P1 strong/CF rulings); base byte-identical to P2 per claim; "
          "withheld block identical across the three withheld cells; "
          "claim block + TASK tail identical across all five")
    print(f"run contract: 200 ids x {len(KINDS)} kinds = "
          f"{200 * len(KINDS)} rows/model -> 5,000 rows (5 models)")
    print("regression: G24A discovery + P2 cells unchanged, no condition "
          "name collisions (g24p1 / g24p3 / g25 / g26)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
