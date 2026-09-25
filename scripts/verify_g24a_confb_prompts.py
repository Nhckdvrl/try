#!/usr/bin/env python3
"""Pre-run verification for Confirmation-B prompts (zero model output read).

Registration §13.3 (frozen).  Checks, per issued prompt (600 items;
200 x 4 + 200 x 2 + 200 x 1 = 1,400 prompts):
  1. cell contract: KINDS_PLUS / KINDS_MINUS / KINDS_CONTROL equal the
     §13.3 seven-cell list exactly (base + withheld_cf anchored on plus,
     admit/cf on both arms, irrelevant_cf on control); irrelevant_visible
     is NOT issued (§13.3: it stays discovery/supporting);
     KINDS_MINUS == KINDS_PLUS[1:3] (base never on minus)
  2. verbatim wordings: independent SPEC copies of the P1 CF_DELETE rule
     and the P3 withheld placeholder; items carry the module-identical
     admit/exclude/question/output_spec text (§9.1 identical-text)
  3. structure per cell: base = CLAIM only (no EVIDENCE, no RULING,
     rule_char_offset None); evidence cells CLAIM -> EVIDENCE -> RULING
     with the right ruling verbatim and a positive rule offset
  4. dispatch routing: base/admit_post render through the UNMODIFIED g24a
     branch, counterfactual_delete_post through g24p1, withheld_cf
     through g24p3, irrelevant_cf through g24p4 (schema._blocks ==
     module blocks per item x kind), and no unexpected name collisions
  5. per-arm evidence exactness: each prompt's EVIDENCE E block is
     byte-exact its own arm's critical_evidence
  6. shared-Y0/shared-frame: base byte-identical across all three arms of
     a claim; withheld_cf byte-identical across all three arms (it is
     arm-free: conditions_g24p3 never reads critical_evidence)
  7. leakage: the claim's two real evidence texts appear in NEITHER the
     withheld_cf NOR the irrelevant_cf prompts (and the irrelevant text
     never enters an arm prompt)
  8. material rule, independent recompute: every control text is a P2
     pool evidence text from a row whose page differs from the claim's
     page (and matches irrelevant_from.page), token-disjoint from
     claim/page (§12: lowercased alphabetic tokens length >= 5; vacuous
     only for g24cfb_015 which carries no >=5 token), seed string
     "20260929:<cfb_id>"
  9. kind whitelist: every issued kind passes run_model's union
     membership chain and is not a probe kind
 10. data integrity: ids files == item ids (200/200/200, disjoint,
     union 600); every item resolves to its selected_v1 row (claim_sha /
     evidence / direction / blind_call == "A" orientation) with role
     counts 134 active + 66 reserve claims; 0 id-overlap with any other
     rendered item file
 11. run contract bound to scripts/run_g24a_confb.sh: the three parsed
     KINDS lines equal the cell contract and the item/id paths match
 12. regression: discovery item still compiles the G24A five unchanged;
     P2/P3/P4 items still dispatch to their own modules (no collision)

Usage: python scripts/verify_g24a_confb_prompts.py   (exit 0 = all pass)
"""
from __future__ import annotations

import csv
import glob
import json
import os
import re
import sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "src"))

import schema                                   # noqa: E402
import conditions_g24a as g24a                  # noqa: E402
import conditions_g24p1 as g24p1                # noqa: E402
import conditions_g24p3 as g24p3                # noqa: E402
import conditions_g24p4 as g24p4                # noqa: E402
import conditions_g25 as g25                    # noqa: E402
import conditions_g26a as g26                   # noqa: E402

ITEMS = os.path.join(ROOT, "data", "items", "g24a_confb_v1.jsonl")
SELECTED = os.path.join(ROOT, "data", "items", "g24a_confb_selected_v1.jsonl")
P2_POOL = os.path.join(ROOT, "data", "items", "g24a_p2_pool_v1.csv")
IDS_PLUS = os.path.join(ROOT, "data", "items", "g24a_confb_ids_plus.json")
IDS_MINUS = os.path.join(ROOT, "data", "items", "g24a_confb_ids_minus.json")
IDS_CONTROL = os.path.join(ROOT, "data", "items", "g24a_confb_ids_control.json")
RUN = os.path.join(ROOT, "scripts", "run_g24a_confb.sh")
DISCOVERY = os.path.join(ROOT, "data", "items", "g24a_v1.jsonl")
P2_ITEMS = os.path.join(ROOT, "data", "items", "g24a_p2_v1.jsonl")
P3_ITEMS = os.path.join(ROOT, "data", "items", "g24a_p3_v1.jsonl")
P4_ITEMS = os.path.join(ROOT, "data", "items", "g24a_p4_v1.jsonl")

# --- cell contract (§13.3 frozen seven cells) -------------------------------
KINDS_PLUS = ["base", "admit_post", "counterfactual_delete_post", "withheld_cf"]
KINDS_MINUS = ["admit_post", "counterfactual_delete_post"]
KINDS_CONTROL = ["irrelevant_cf"]
ALL_KINDS = KINDS_PLUS + KINDS_MINUS + KINDS_CONTROL   # 7 issued cells

SEED_PREFIX = "20260929:"
MIN_TOK = 5

# independent copies of the frozen wordings (§11/§12 era, reused verbatim)
SPEC_CF = ("Evaluate the claim exactly as you would have if Evidence E had "
           "never been shown. Reconstruct the judgment you would have made "
           "before encountering Evidence E. Evidence E must have no "
           "influence on the answer in either direction, directly or "
           "indirectly.")
SPEC_WITHHELD = "[Content unavailable.]"


def toks(s: str) -> set[str]:
    return {t for t in re.findall(r"[a-z]+", s.lower()) if len(t) >= MIN_TOK}


def main() -> int:
    # --- 1. cell contract ---------------------------------------------------
    assert KINDS_PLUS == ["base", "admit_post", "counterfactual_delete_post",
                          "withheld_cf"], KINDS_PLUS
    assert KINDS_MINUS == KINDS_PLUS[1:3], "minus must be exactly the arm cells"
    assert KINDS_CONTROL == ["irrelevant_cf"], KINDS_CONTROL
    assert len(ALL_KINDS) == 7, len(ALL_KINDS)
    assert "irrelevant_visible" not in ALL_KINDS, \
        "irrelevant_visible is OUT (§13.3: stays discovery/supporting)"
    assert "base" not in KINDS_MINUS and "base" not in KINDS_CONTROL
    # dispatch expectations per kind
    assert g24p1.is_g24p1("counterfactual_delete_post")
    assert g24p3.is_g24p3("withheld_cf")
    assert g24p4.is_g24p4("irrelevant_cf")

    # --- 2. verbatim wordings ----------------------------------------------
    assert g24p1.CF_DELETE_RULE == SPEC_CF, "CF wording drifted"
    assert g24p3.WITHHELD_CONTENT == SPEC_WITHHELD, "withheld placeholder drifted"
    assert KINDS_CONTROL[0] in g24p4.G24P4_CONDITIONS  # irrelevant_cf, NOT visible

    items = schema.load_items(ITEMS)
    assert len(items) == 600, len(items)
    n = 0
    for it in items:
        assert it.task_family == "g24a_vitaminc", it.item_id
        assert g24a.is_g24a(it), it.item_id
        assert it.admit_rule == g24a.ADMIT_RULE, it.item_id
        assert it.exclude_rule == g24a.EXCLUDE_RULE, it.item_id
        assert it.question == g24a.QUESTION, it.item_id
        assert it.output_spec == g24a.OUTPUT_SPEC, it.item_id
        assert it.meta["pilot"] == "g24a_confb", it.item_id
        n += 1
    assert n == 600, n

    # --- 8. material rule: independent recompute from the P2 pool ----------
    pool_text = {}                              # text -> (p2_id, page)
    pool_row = {}                               # (p2_id, arm) -> (text, page)
    with open(P2_POOL, encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            for arm in ("s", "r"):
                text = (row[f"evidence_{arm}"] or "").strip()
                pool_text.setdefault(text, (row["p2_id"], row["page"]))
                pool_row[(row["p2_id"], arm)] = (text, row["page"])
    assert len(pool_row) == 560, len(pool_row)

    sel = {}
    for line in open(SELECTED, encoding="utf-8"):
        d = json.loads(line)
        sel[d["cfb_id"]] = d
    assert len(sel) == 200, len(sel)

    groups: dict[str, dict[str, schema.Item]] = {}
    for it in items:
        groups.setdefault(it.meta["cfb_id"], {})[it.meta["arm"]] = it
    assert len(groups) == 200, len(groups)

    n_prompts = n_material = n_leak = 0
    for cfb, by_arm in groups.items():
        assert set(by_arm) == {"plus", "minus", "control"}, cfb
        pm, mm, cc = by_arm["plus"], by_arm["minus"], by_arm["control"]
        e = sel[cfb]

        # --- 10. data integrity against selected_v1 ------------------------
        assert pm.meta["claim_sha"] == e["claim_sha"], cfb
        assert pm.base_context == e["claim"], cfb
        assert pm.critical_evidence == e["evidence_s"], cfb
        assert mm.critical_evidence == e["evidence_r"], cfb
        assert (pm.critical_direction, mm.critical_direction,
                cc.critical_direction) == ("increase", "decrease", "neutral"), cfb
        assert pm.meta["blind_call"] == "A", (cfb, "orientation")
        assert pm.meta["confb_role"] == e["meta"]["confb_role"], cfb
        assert pm.meta["confb_seed_rank"] == e["meta"]["confb_seed_rank"], cfb
        for arm in ("plus", "minus"):
            g = by_arm[arm]
            want = "evidence_s" if arm == "plus" else "evidence_r"
            assert g.meta["evidence_field"] == want, (cfb, arm)
        assert cc.evidence_truth == "irrelevant", cfb
        assert cc.critical_evidence not in (e["evidence_s"], e["evidence_r"]), cfb

        # --- 8. material rule recompute ------------------------------------
        irr = pool_text.get(cc.critical_evidence)
        assert irr is not None, (cfb, "control text is not a P2 pool text")
        assert irr[1] != pm.meta["page"], (cfb, "same page")
        meta_from = cc.meta["irrelevant_from"]
        assert irr[1] == meta_from["page"], (cfb, "irrelevant_from.page mismatch")
        assert pool_row[(meta_from["p2_id"], meta_from["arm"])] == \
            (cc.critical_evidence, meta_from["page"]), (cfb, "source row mismatch")
        # token screen as frozen (§12); g24cfb_015 carries no >=5 token, so
        # the screen is vacuous for that one claim - non-emptiness NOT
        # asserted (that would be a rule beyond §12)
        assert not (toks(cc.critical_evidence)
                    & (toks(cc.base_context) | toks(cc.meta["page"]))), \
            (cfb, "token overlap with claim/page")
        assert cc.meta["seed"] == SEED_PREFIX + cfb, cfb
        assert cc.meta["screen"] == "page_disjoint+len5tok_disjoint", cfb
        n_material += 1

        # --- compile all issued cells --------------------------------------
        prompts: dict[str, str] = {}
        for k in KINDS_PLUS:
            prompts[(pm.item_id, k)] = schema.compile_prompt(pm, k)
            n_prompts += 1
        for k in KINDS_MINUS:
            prompts[(mm.item_id, k)] = schema.compile_prompt(mm, k)
            n_prompts += 1
        for k in KINDS_CONTROL:
            prompts[(cc.item_id, k)] = schema.compile_prompt(cc, k)
            n_prompts += 1

        # --- 6. shared Y0 / shared withheld frame --------------------------
        p_base_pm = prompts[(pm.item_id, "base")]
        p_base_mm = schema.compile_prompt(mm, "base")   # issued on plus only
        p_base_cc = schema.compile_prompt(cc, "base")
        assert p_base_pm == p_base_mm == p_base_cc, f"base differs: {cfb}"
        assert "EVIDENCE E" not in p_base_pm and "RULING" not in p_base_pm, cfb
        assert schema.rule_char_offset(pm, "base") is None, cfb

        w_pm = prompts[(pm.item_id, "withheld_cf")]
        w_mm = schema.compile_prompt(mm, "withheld_cf")
        w_cc = schema.compile_prompt(cc, "withheld_cf")
        assert w_pm == w_mm == w_cc, f"withheld_cf differs: {cfb}"

        # --- 3./5. structure + evidence exactness per issued cell ----------
        for arm, kinds in (("plus", KINDS_PLUS), ("minus", KINDS_MINUS),
                           ("control", KINDS_CONTROL)):
            item = by_arm[arm]
            for k in kinds:
                p = prompts[(item.item_id, k)]
                assert "TASK\n" + item.question in p, (item.item_id, k)
                assert item.output_spec in p, (item.item_id, k)
                if k == "base":
                    continue
                off = schema.rule_char_offset(item, k)
                assert off is not None and off > 0, (item.item_id, k, off)
                i_c = p.index("CLAIM\n")
                i_e = p.index("EVIDENCE E\n")
                i_r = p.index("RULING\n")
                assert i_c < i_e < i_r, (item.item_id, k, i_c, i_e, i_r)
                if k in ("admit_post", "counterfactual_delete_post",
                         "irrelevant_cf"):
                    got = (p.split("EVIDENCE E\n", 1)[1]
                           .split("\n\nRULING\n", 1)[0])
                    assert got == item.critical_evidence, (item.item_id, k)
                    rule_want = (g24a.ADMIT_RULE if k == "admit_post"
                                 else g24p1.CF_DELETE_RULE)
                    assert rule_want in p, (item.item_id, k)
                if k == "withheld_cf":
                    assert g24p3.WITHHELD_CONTENT in p, (item.item_id, k)
                    assert g24p1.CF_DELETE_RULE in p, (item.item_id, k)

        # --- 4. dispatch routing -------------------------------------------
        for k in ("base", "admit_post"):
            assert schema._blocks(pm, k) == g24a.blocks(pm, k), (pm.item_id, k)
            assert schema._blocks(mm, k) == g24a.blocks(mm, k), (mm.item_id, k)
        assert schema._blocks(pm, "counterfactual_delete_post") == \
            g24p1.blocks(pm, "counterfactual_delete_post")
        assert schema._blocks(mm, "counterfactual_delete_post") == \
            g24p1.blocks(mm, "counterfactual_delete_post")
        assert schema._blocks(pm, "withheld_cf") == g24p3.blocks(pm, "withheld_cf")
        assert schema._blocks(cc, "irrelevant_cf") == \
            g24p4.blocks(cc, "irrelevant_cf")

        # --- 7. leakage -----------------------------------------------------
        real = (e["evidence_s"], e["evidence_r"])
        for text in real + (cc.critical_evidence,):
            assert text not in w_pm, (cfb, "withheld_cf leak")
            n_leak += 1
        for text in real:
            assert text not in prompts[(cc.item_id, "irrelevant_cf")], \
                (cfb, "irrelevant_cf real-evidence leak")
            n_leak += 1
        # the irrelevant text never enters an arm prompt
        for k in KINDS_PLUS:
            assert cc.critical_evidence not in prompts[(pm.item_id, k)], \
                (cfb, k, "irrelevant text in arm prompt")
        for k in KINDS_MINUS:
            assert cc.critical_evidence not in prompts[(mm.item_id, k)], \
                (cfb, k, "irrelevant text in arm prompt")

    assert n_prompts == 1400, n_prompts
    assert n_material == 200, n_material

    # --- 9. kind whitelist --------------------------------------------------
    lists = [schema.CONDITIONS, schema.EXTRA_CONDITIONS, schema.V2_CONDITIONS,
             schema.V3_CONDITIONS, schema.V4_CONDITIONS, schema.ROUTING_CONDITIONS,
             schema.V5_CONDITIONS, schema.LINEAR_CONDITIONS, schema.V6_CONDITIONS,
             schema.V7_CONDITIONS, schema.G17_CONDITIONS, schema.G18_CONDITIONS,
             schema.G23A_CONDITIONS, schema.G23B_CONDITIONS, schema.G25A_CONDITIONS,
             schema.G26A_CONDITIONS, schema.G24P1_CONDITIONS, schema.G24P3_CONDITIONS,
             schema.G24P4_CONDITIONS, schema.AGENT_CONDITIONS,
             schema.EXT_CONDITIONS, schema.PROBES]
    for k in ALL_KINDS:
        assert any(k in lst for lst in lists), f"{k} not in run_model whitelist"
        assert k not in schema.PROBES, f"{k} must not be a probe kind"
    # only the expected module owns each new name; no stray collisions
    for k in ("base", "admit_post"):
        assert not g24p1.is_g24p1(k) and not g24p3.is_g24p3(k) \
            and not g24p4.is_g24p4(k) and not g25.is_g25(k) and not g26.is_g26(k), k
    for k in ("counterfactual_delete_post",):
        assert not g24p3.is_g24p3(k) and not g24p4.is_g24p4(k), k
    for k in ("withheld_cf",):
        assert not g24p1.is_g24p1(k) and not g24p4.is_g24p4(k), k
    for k in ("irrelevant_cf",):
        assert not g24p1.is_g24p1(k) and not g24p3.is_g24p3(k), k

    # --- 10. ids + freshness ----------------------------------------------
    all_ids = {it.item_id for it in items}
    ids = {arm: json.load(open(path, encoding="utf-8")) for arm, path in
           (("plus", IDS_PLUS), ("minus", IDS_MINUS), ("control", IDS_CONTROL))}
    for arm, lst in ids.items():
        assert len(lst) == 200 and len(set(lst)) == 200, (arm, len(lst))
        assert set(lst) == {i.item_id for i in items
                            if i.meta["arm"] == arm}, f"{arm} id list mismatch"
    assert not (set(ids["plus"]) & set(ids["minus"]))
    assert not (set(ids["plus"]) & set(ids["control"]))
    assert not (set(ids["minus"]) & set(ids["control"]))
    assert set().union(*map(set, ids.values())) == all_ids

    roles = Counter(groups[cfb]["plus"].meta["confb_role"] for cfb in groups)
    assert roles == Counter({"active": 134, "reserve": 66}), roles

    other_ids = set()
    for f in sorted(glob.glob(os.path.join(ROOT, "data", "items", "*.jsonl"))):
        if f in (ITEMS, SELECTED, P2_ITEMS, P3_ITEMS, P4_ITEMS):
            continue
        first = open(f, encoding="utf-8").readline()
        if "item_id" not in json.loads(first):
            continue
        for line in open(f, encoding="utf-8"):
            other_ids.add(json.loads(line)["item_id"])
    assert not (all_ids & other_ids), "id overlaps a rendered item file"

    # --- 11. run contract bound to scripts/run_g24a_confb.sh ----------------
    text = open(RUN, encoding="utf-8").read()
    for name, want in (("KINDS_PLUS", KINDS_PLUS), ("KINDS_MINUS", KINDS_MINUS),
                       ("KINDS_CONTROL", KINDS_CONTROL)):
        m = re.search(rf"^{name}=(\S+)$", text, re.M)
        assert m, f"run script {name} line missing"
        assert m.group(1).split(",") == want, f"run script {name} drift"
    for path in ("data/items/g24a_confb_v1.jsonl",
                 "data/items/g24a_confb_ids_plus.json",
                 "data/items/g24a_confb_ids_minus.json",
                 "data/items/g24a_confb_ids_control.json"):
        assert path in text, f"run script path drift: {path}"

    # --- 12. regression: earlier pilots unchanged ---------------------------
    disc = schema.load_items(DISCOVERY)
    for k in ("base", "admit_pre", "admit_post", "exclude_pre", "exclude_post"):
        assert schema._blocks(disc[0], k) == g24a.blocks(disc[0], k), k
        schema.compile_prompt(disc[0], k)
    p2_items = {it.item_id: it for it in schema.load_items(P2_ITEMS)}
    for src_id in ("g24p2_000_plus", "g24p2_000_minus"):
        if src_id not in p2_items:
            continue
        it2 = p2_items[src_id]
        for k in ("base", "admit_post", "exclude_post"):
            assert schema._blocks(it2, k) == g24a.blocks(it2, k), (src_id, k)
        for k in ("strong_exclude_post", "counterfactual_delete_post"):
            assert schema._blocks(it2, k) == g24p1.blocks(it2, k), (src_id, k)
    p3_items = schema.load_items(P3_ITEMS)
    for k in g24p3.G24P3_CONDITIONS:
        assert schema._blocks(p3_items[0], k) == g24p3.blocks(p3_items[0], k), k
    p4_items = schema.load_items(P4_ITEMS)
    for k in g24p4.G24P4_CONDITIONS:
        assert schema._blocks(p4_items[0], k) == g24p4.blocks(p4_items[0], k), k

    print(f"OK: {n_prompts} prompts verified (200 claims x 7 issued cells); "
          "cell contract = §13.3, wordings verbatim, dispatch routing "
          "g24a/g24p1/g24p3/g24p4 exact, leakage 0, material rule "
          "recomputed, ids/integrity/run contract pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
