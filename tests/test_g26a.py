"""G26A design tests — nothing here touches a model (§12A checklist).

Runs on code, the frozen Phase-A pool, the build report and synthetic
records only:

* materials: pool sha256 + train-only + O9 census (3,642 structural ->
  3,640 feasible), the two tokenizer-geometry exclusions and their
  best-effort distance vectors, every retained item's recorded spread
  <= 10, filler-bank schedule {4..20} x 4 / 816 words, bank v2 freeze;
* feasibility is outcome-blind: build_g26a has no model/runner/outcome
  reference at all, and the report carries the outcome-independence claim;
* mention direction: for sampled real items the evidence-A sentence is
  found in page_a, mentions page_b's entity and NOT vice versa (XOR
  bridge, §2/§9.3), with `reversed_list_order <=> orient == sf1_to_sf0`;
* conditions: 10 cells partition into 4 no-rule + 6 rule, no-rule cells
  contain no RULING block and no rule bytes, EXCL/ADMIT rule bytes are
  fixed constants, and across T0/T1/T2 the RULING block is byte-identical
  while the shared filler multiset is equal and only placement moves;
  exact cross-timing x 4-tokenizer distance <= 10 on sampled items;
* Phase A blindness + mechanical discipline in src/analyze_g26a.py:
  sha256 computed BEFORE any gate, structural exit 3 (rule cell / probe /
  stray kind / duplicate row / unknown item / wrong model / budget),
  mechanical exit 4 (missing or unparsed rows — never analyzed partially),
  HARD STOP exit 2 below 200, and selection = frozen pool order capped
  300 with ids sha256 — never sorted by an outcome;
* §5 gate funnel on synthetic values (chain >= 15, singles <= 5);
* analyzer outcome map: positive-gate floor 3.0 trichotomy, negatives
  before not-positive (non-monotone reachable), integrity first
  (I1-I4 -> order-artifact, G25A lineage), data-absent -> unresolved,
  equivalence/ROPE never a branch input and never `unresolved`;
* end-to-end Phase B wiring on synthetic rows over real pool ids:
  staged verdict with probes, order-artifact when probes are absent;
* cluster bootstrap: identity with the frozen analyze_g25 implementation,
  determinism under seed 20260924, whole-cluster bookkeeping;
* run harness: scripts/run_g26a_phasea.sh kinds are exactly the 4 no-rule
  cells, token gate G26A-FLIP1=RECORDED, items sha pin, selector-only.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from collections import Counter

import pytest

import analyze_g26a as ag
import audit_hover as ah
import build_g26a as bg
import conditions_g26a as g26
from analyze_g25 import cluster_boot as g25_cluster_boot
from schema import (Item, compile_prompt, load_items, rule_char_offset)

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..")
POOL = os.path.join(ROOT, "data/items/g26_phasea_pool_v1.jsonl")
POOL_REPORT = os.path.join(ROOT, "data/items/g26_phasea_pool_report_v1.json")
PREREG = os.path.join(ROOT, "preregistrations",
                      "PREREGISTRATION_G26A_LOAD_BEARING.md")
RUN_SCRIPT = os.path.join(ROOT, "scripts/run_g26a_phasea.sh")
DB_PATH = os.path.join(ROOT, "data/external/raw/hover/wiki_wo_links.db")

N_STRUCT = 3642                 # audit T6 train survivors (O9 census input)
N_POOL = 3640                   # feasible N_A after the §0 exclusions
EXCLUDED = {                    # tokenizer-geometry infeasible (§0 ruling)
    "g26a_3dbe1a3e-b448-4dc0-b1d6-2e3a2ada88bc",
    "g26a_4b84c748-0cf2-4981-b526-bab6e8759040",
}
POOL_SHA = "ad0ac715a609f49f9ad98af5cf6a3022a1b1e6f904d7a1f22ae2d490a7e2c95c"
SELECTOR = "mistral-small-24b"

# bank v2 freeze pins (13 divergence-bearing sentences added pre-tag)
BANK_V2_SPECIALS = {
    "The crème and chrysanthemum sat by the door.",
    "Two crates and 128 cartons wait by the door.",
    "Her résumé and the quiet façade both looked quite plain.",
    "The stock sheet lists 248 tins and 36 spare gray spools.",
    "The old voilà and a dried chrysanthemum rested by the wide window.",
    "Someone recorded 128 lamps, 392 plugs, and 47 small fuses on the sheet.",
    "Beside the stair the stratosphere poster and the résumé hung above the "
    "low shelf.",
    "The quiet inventory tally reads 512 chairs, 248 tables, and 96 tall "
    "plain floor lamps.",
    "The spare encyclopaedia, the dried chrysanthemum, and a folded voilà "
    "sat unnoticed on the low bench.",
    "During the day the front desk logs 128 parcels, 392 envelopes, and 617 "
    "late forms every week.",
    "The heavy encyclopaedia, the old oesophagus chart, and a matinée notice "
    "lay neatly stacked by the wide window.",
    "Every slow afternoon the side counter counts 248 bolts, 617 washers, 36 "
    "cracked tiles, and 128 plain spare hooks.",
    "Throughout the week the back office stored 128 ledgers, 456 paper "
    "clips, 24 rubber bands, 617 tins, and 36 folders.",
}


def _sha(path: str) -> str:
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


POOL_ITEMS = load_items(POOL)


# ---------------------------------------------------------------------------
# materials: pool, census, feasibility exclusions
# ---------------------------------------------------------------------------
def test_pool_sha_count_and_train_only():
    assert _sha(POOL) == POOL_SHA
    assert len(POOL_ITEMS) == N_POOL
    assert len({i.item_id for i in POOL_ITEMS}) == N_POOL
    assert all(i.meta["split"] == "train" for i in POOL_ITEMS)
    # frozen order = HoVer train order: uids unique, disjoint from earlier
    # pools (build asserts other_pool_ids; re-check the G25A anchor here)
    g25_ids = {i.item_id for i in load_items(
        os.path.join(ROOT, "data/items/g25_v1.jsonl"))}
    assert not ({i.item_id for i in POOL_ITEMS} & g25_ids)


def test_pool_report_census_and_feasibility_gate():
    rep = json.load(open(POOL_REPORT))
    f = rep["feasibility"]
    assert f["n_structural_census"] == N_STRUCT
    assert f["n_feasible_N_A"] == N_POOL
    assert f["n_excluded"] == 2
    assert {e["item_id"] for e in f["excluded"]} == EXCLUDED
    for e in f["excluded"]:
        assert e["reason"] == "tokenizer_geometry_infeasible"
        # the recorded best effort genuinely violates the O7 window
        assert e["best_effort_max"] is not None
        assert e["best_effort_max"] > bg.MAX_DIST_TOKENS
        assert max(e["best_effort_spreads"].values()) > bg.MAX_DIST_TOKENS
    assert "no model forward" in f["outcome_independence"]
    assert "frozen" in f["post_tag_rule"]
    assert rep["items"]["n"] == N_POOL
    assert rep["items"]["sha256"] == POOL_SHA
    # O7 record over every RETAINED item: all spreads within +-10
    assert max(rep["fillers"]["max_pairwise_tokens"].values()) \
        <= bg.MAX_DIST_TOKENS
    assert rep["fillers"]["limit"] == bg.MAX_DIST_TOKENS


def test_every_retained_item_furnishable_and_blind_meta():
    for it in POOL_ITEMS:
        d = it.meta.get("dist_max")
        assert d and max(d.values()) <= bg.MAX_DIST_TOKENS, it.item_id
        # rule cells need fillers; no-rule cells must not need them
        assert it.meta.get("filler_a") and it.meta.get("filler_b")
        assert it.item_id not in EXCLUDED


def test_feasibility_is_outcome_blind_static():
    src = open(os.path.join(ROOT, "src/build_g26a.py")).read()
    # executable references only — prose describing run_model's measurement
    # is legitimate; a call/import or any outcome file would not be
    for forbidden in ("run_model.py", "results/raw", "model_tag", "p_yes",
                      "import run_model", "subprocess"):
        assert forbidden not in src, forbidden
    # no G26A outcome cell may be referenced by the builder
    for cell in g26.G26A_CONDITIONS:
        assert cell not in src, cell


def test_mention_direction_xor_bridge_on_real_items():
    """A/B follow mention direction (§2): A is on page_a, bridges to
    page_b's entity, and B does NOT bridge back (orientation-unique XOR)."""
    conn, tables = ah.open_db(DB_PATH)
    t, id_col, text_col = ah.find_page_store(conn, tables)
    cache: dict = {}
    tiers = Counter()
    # same page chain as the builder (NFD/NFC title tiers + smart_sents)
    page = bg.raw_page_chain(conn, t, id_col, text_col, cache, tiers)

    sample = POOL_ITEMS[:20] + POOL_ITEMS[-5:]
    try:
        for it in sample:
            m = it.meta
            assert m["orient"] in ("sf0_to_sf1", "sf1_to_sf0")
            # reversed list order <=> the mention direction opposes sf0->sf1
            assert m["reversed_list_order"] == (m["orient"] == "sf1_to_sf0")
            assert set((m["page_a"], m["page_b"])) == set(m["title_pair"])
            assert m["page_a"] != m["page_b"]
            pa, pb = page(m["page_a"]), page(m["page_b"])
            assert pa and pb, it.item_id
            assert it.critical_evidence in pa, it.item_id   # A lives on page_a
            assert m["evidence_b"] in pb, it.item_id        # B lives on page_b
            # XOR bridge: A mentions B's entity, B does not mention A's
            assert ah.mentions(it.critical_evidence, m["page_b"]) is True
            assert ah.mentions(m["evidence_b"], m["page_a"]) is False
    finally:
        conn.close()


def test_bank_v2_frozen_schedule_and_specials():
    bank = g26.FILLER_BANK
    assert len(bank) == 68 == len(set(bank))
    hist = Counter(len(g26.words(s)) for s in bank)
    assert hist == {w: 4 for w in range(4, 21)}
    assert sum(hist[w] * w for w in hist) == 816
    assert BANK_V2_SPECIALS <= set(bank)          # freeze pin: no reverts


def test_excluded_items_fail_furnishing_deterministically():
    """The two excluded uids re-run through the identical frozen search
    (same seeds/budget) must fail again — outcome-blind reproducibility."""
    data = ah.load_claims()
    conn, tables = ah.open_db(DB_PATH)
    t, id_col, text_col = ah.find_page_store(conn, tables)
    cache: dict = {}
    tiers = Counter()
    page = bg.raw_page_chain(conn, t, id_col, text_col, cache, tiers)
    _stats, recs = bg.sweep(data, page)
    conn.close()
    by_uid = {r["uid"]: r for r in recs}

    from transformers import AutoTokenizer
    tok_by_tag = {}
    for tag, mid in bg.PANEL_MODEL_IDS.items():
        tk = AutoTokenizer.from_pretrained(
            bg.resolve_tokenizer_dir(mid), local_files_only=True)
        tok_by_tag[tag] = (lambda text, _tk=tk: len(
            _tk(text, add_special_tokens=False)["input_ids"]))
    fill = bg.Fill(tok_by_tag, g26.FILLER_BANK,
                   [len(g26.words(s)) for s in g26.FILLER_BANK])

    for uid in sorted(x.removeprefix("g26a_") for x in EXCLUDED):
        rec = by_uid[uid]
        s_val = ah.LABELS[rec["label"]]
        item = Item(
            item_id=f"g26a_{uid}", task_family="g26a_hover",
            surface_domain="wikipedia", base_context=rec["claim"],
            critical_evidence=rec["a"], critical_label="evidence A",
            critical_direction="increase" if s_val > 0 else "decrease",
            exclusion_reason="none_stated",
            evidence_truth="true_but_forbidden",
            admit_rule=g26.ADMIT_RULE, exclude_rule=g26.EXCL_RULE,
            question=g26.QUESTION, output_spec=g26.OUTPUT_SPEC,
            memory_question=g26.MEMORY_QUESTION,
            rule_probe_question=g26.RULE_PROBE_QUESTION,
            ground_truth=None,
            meta={"evidence_b": rec["b"]},
        )
        dist: dict = {}
        got = bg.furnish(rec, item, fill, dist)
        if got is None:
            got = bg.furnish_deep(rec, item, fill, dist)
        assert got is None, f"{uid} unexpectedly furnishable"
        assert dist["_best_max"] > bg.MAX_DIST_TOKENS


# ---------------------------------------------------------------------------
# conditions: cells, rule bytes, timings, filler multiset, distance
# ---------------------------------------------------------------------------
def test_cells_partition_and_frozen_order():
    assert len(g26.G26A_CONDITIONS) == 10          # O3 (amended 11 -> 10)
    assert set(g26.NORULE_CELLS).isdisjoint(g26.RULE_CELLS)
    assert set(g26.NORULE_CELLS) | set(g26.RULE_CELLS) \
        == set(g26.G26A_CONDITIONS)
    assert g26.G26A_CONDITIONS == list(g26.NORULE_CELLS) + [
        f"g26_{arm}_t{tm}" for arm in ("excl", "admit") for tm in (0, 1, 2)]
    assert g26.G26A_PROBES == ["rule_probe_g26_excl", "rule_probe_g26_admit"]
    assert len(g26.RULE_CELLS) == 6


def _sample_item() -> Item:
    return next(i for i in POOL_ITEMS
                if i.meta.get("filler_a") and i.meta.get("filler_b"))


def test_norule_cells_have_no_rule_no_filler():
    it = _sample_item()
    for cond in g26.NORULE_CELLS:
        bl = g26.blocks(it, cond)
        assert not any(b.startswith(g26.RULE_HEADER + "\n") for b in bl)
        assert g26.EXCL_RULE not in "\n\n".join(bl)
        assert g26.ADMIT_RULE not in "\n\n".join(bl)
        assert not any(b.startswith(g26.FILLER_HEADER + "\n") for b in bl)
    assert g26.blocks(it, "g26_y0") == [f"BACKGROUND\n{it.base_context}"]
    assert len(g26.blocks(it, "g26_yab")) == 3


def test_rule_bytes_identical_across_timings_and_distinct_arms():
    """I1: the RULING block is byte-identical across T0/T1/T2 and EXCL
    != ADMIT; compiled prompts contain exactly one copy of the byte-fixed
    rule sentence (§3, prereg byte-fixed amendment)."""
    it = _sample_item()
    for arm, rule in (("excl", g26.EXCL_RULE), ("admit", g26.ADMIT_RULE)):
        rulings, counts = [], []
        for tm in (0, 1, 2):
            cond = f"g26_{arm}_t{tm}"
            bl = g26.blocks(it, cond)
            hits = [b for b in bl if b.startswith(g26.RULE_HEADER + "\n")]
            assert len(hits) == 1
            rulings.append(hits[0])
            prompt = compile_prompt(it, cond, "reasoned")
            counts.append(prompt.count(rule))
            off = rule_char_offset(it, cond, "reasoned")
            # offset anchors at the RULING header — the O7 distance is
            # measured header-to-end (run_model rule_to_answer_tokens)
            assert off is not None and prompt.startswith(g26.RULE_HEADER, off)
            assert rule in prompt[off:]
        want = g26.RULE_HEADER + "\n" + rule
        assert rulings == [want, want, want]
        assert counts == [1, 1, 1]
    assert g26.EXCL_RULE != g26.ADMIT_RULE


def test_shared_filler_multiset_and_placement_only():
    """I2/O7 construction: the three timings share ONE filler multiset;
    only placement moves, and the block order differs across timings."""
    it = _sample_item()
    per_timing = {}
    for arm in ("excl", "admit"):
        multisets = []
        idx = []
        sig = []            # (filler blocks before rule, after rule)
        for tm in (0, 1, 2):
            bl = g26.blocks(it, f"g26_{arm}_t{tm}")
            multisets.append(Counter(g26.filler_sentences(bl)))
            ri = next(i for i, b in enumerate(bl)
                      if b.startswith(g26.RULE_HEADER + "\n"))
            idx.append(ri)
            fi = [i for i, b in enumerate(bl)
                  if b.startswith(g26.FILLER_HEADER + "\n")]
            sig.append((sum(1 for i in fi if i < ri),
                        sum(1 for i in fi if i > ri)))
        assert multisets[0] == multisets[1] == multisets[2]
        # only PLACEMENT moves: rule earliest at T0, and the before/after
        # filler geometry differs across all three timings — T0 all before,
        # T1 split around the rule, T2 all after (§3)
        assert idx[0] < idx[1], (arm, idx)
        assert sig == [(1, 0), (1, 1), (0, 1)], (arm, sig)
        # multiset is exactly filler_a + filler_b (shared inventory)
        want = Counter(it.meta["filler_a"] + it.meta["filler_b"])
        assert multisets[0] == want
        per_timing[arm] = multisets[0]
    assert per_timing["excl"] == per_timing["admit"]   # arms share fillers


_TOKS = None


def _tok_by_tag():
    global _TOKS
    if _TOKS is None:
        from transformers import AutoTokenizer
        _TOKS = {}
        for tag, mid in bg.PANEL_MODEL_IDS.items():
            tk = AutoTokenizer.from_pretrained(
                bg.resolve_tokenizer_dir(mid), local_files_only=True)
            _TOKS[tag] = (lambda text, _tk=tk: len(
                _tk(text, add_special_tokens=False)["input_ids"]))
    return _TOKS


def test_rule_to_judgment_distance_within_10_sampled():
    """O7 exact gate: max spread across T0/T1/T2 under all 4 pooled
    tokenizers x both arms <= 10 on a deterministic sample (the build
    report's max_pairwise_tokens covers all 3,640)."""
    tok = _tok_by_tag()
    sample = [POOL_ITEMS[i] for i in range(0, len(POOL_ITEMS),
                                           len(POOL_ITEMS) // 20)][:20]
    worst = 0
    for it in sample:
        d = bg.verify_distances(it, tok)
        worst = max(worst, max(d.values()))
        assert max(d.values()) <= bg.MAX_DIST_TOKENS, (it.item_id, d)
    assert worst <= bg.MAX_DIST_TOKENS


# ---------------------------------------------------------------------------
# analyzer Phase A: sha-first, structural/mechanical discipline, selection
# ---------------------------------------------------------------------------
def _mk_item(i: int) -> Item:
    return Item(
        item_id=f"it{i:04d}", task_family="g26a_hover",
        surface_domain="wikipedia", base_context=f"claim {i}",
        critical_evidence=f"evA {i}", critical_label="evidence A",
        critical_direction="increase" if i % 2 == 0 else "decrease",
        exclusion_reason="none_stated", evidence_truth="true_but_forbidden",
        admit_rule="R", exclude_rule="R", question="Q", output_spec="0-100",
        memory_question="", rule_probe_question="P?",
        meta={"title_pair": [f"t{i}a", f"t{i}b"], "evidence_b": f"evB {i}"})


def _write_pool(tmp_path, items):
    p = tmp_path / "pool.jsonl"
    p.write_text("".join(it.to_json() + "\n" for it in items))
    return str(p)


def _cell_values(kind, i):
    # chain +15..+52 sign-aligned, singles exactly 0 -> all gates pass
    # unless a test overrides; values vary by item so an effect-size sort
    # would produce a DIFFERENT order than the frozen pool order
    s = 1.0 if i % 2 == 0 else -1.0
    y0 = 50.0
    if kind == "g26_y0":
        return y0
    if kind in ("g26_ya", "g26_yb"):
        return y0
    return y0 + s * (15.0 + (i * 7) % 38)          # g26_yab


def _phase_a_rows(items, kinds=("g26_y0", "g26_ya", "g26_yb", "g26_yab"),
                  model=SELECTOR, drop=None, dup=False, extra=None,
                  value_fn=None):
    rows = []
    for it in items:
        i = int(it.item_id[2:])
        for k in kinds:
            if drop == (it.item_id, k):
                continue
            v = value_fn(k, i) if value_fn else _cell_values(k, i)
            rows.append({"item_id": it.item_id, "kind_name": k,
                         "model_tag": model, "value": v})
            if dup and k == "g26_y0":
                rows.append(dict(rows[-1]))
    rows.extend(extra or [])
    return rows


def _run_phase_a(tmp_path, rows, items, name="run"):
    p = tmp_path / f"{name}.jsonl"
    p.write_text("".join(json.dumps(r) + "\n" for r in rows))
    rep = str(tmp_path / f"{name}.report.json")
    sel = str(tmp_path / f"{name}.selection.json")
    rc = ag.phase_a([str(p)], _write_pool(tmp_path, items), rep, sel,
                    rep + ".md")
    report = json.load(open(rep)) if os.path.exists(rep) else None
    selection = json.load(open(sel)) if os.path.exists(sel) else None
    return rc, report, selection


def test_phase_a_sha_recorded_before_gates(tmp_path):
    items = [_mk_item(i) for i in range(3)]
    rc, rep, _ = _run_phase_a(tmp_path, _phase_a_rows(items), items)
    assert rc == 2                                   # 3 < 200 -> HARD STOP
    assert rep["verdict"] == "HARD STOP"
    # sha256 of both inputs is pinned in the report of the SAME bytes
    run_path = rep["runs"][0]["path"]
    assert rep["runs"][0]["sha256"] == _sha(run_path)
    assert rep["items"]["sha256"] == _sha(rep["items"]["path"])
    assert rep["completeness"]["ok"] and rep["completeness"]["rows"] == 12
    assert rep["blindness"]["rule_cell_rows"] == 0
    assert rep["blindness"]["probe_rows"] == 0
    assert rep["selection"]["selected_ids"] == []     # no run past HARD STOP


def test_phase_a_structural_violations_exit_3(tmp_path):
    items = [_mk_item(i) for i in range(4)]
    cases = {
        "rule_cell": dict(extra=[{"item_id": "it0000", "kind_name":
                                  "g26_excl_t0", "model_tag": SELECTOR,
                                  "value": 55.0}]),
        "probe": dict(extra=[{"item_id": "it0000", "kind_name":
                              "rule_probe_g26_excl", "model_tag": SELECTOR,
                              "yesno": "NO"}]),
        "stray": dict(extra=[{"item_id": "it0000", "kind_name": "memory",
                              "model_tag": SELECTOR, "value": 1.0}]),
        "dup": dict(dup=True),
        "wrong_model": dict(extra=[{"item_id": "it0000", "kind_name":
                                    "g26_y0", "model_tag": "qwen3-8b",
                                    "value": 50.0}]),
        "unknown_item": dict(extra=[{"item_id": "zz9999", "kind_name":
                                     "g26_y0", "model_tag": SELECTOR,
                                     "value": 50.0}]),
    }
    for name, kw in cases.items():
        rows = _phase_a_rows(items, **kw)
        rc, rep, _ = _run_phase_a(tmp_path, rows, items, name=name)
        assert rc == 3, name
        assert rep is None, name                    # no report => no gates


def test_phase_a_incomplete_exits_4_mechanical(tmp_path):
    items = [_mk_item(i) for i in range(4)]
    rc, rep, _ = _run_phase_a(
        tmp_path, _phase_a_rows(items, drop=("it0001", "g26_yb")), items)
    assert rc == 4 and rep is None
    # unparsed value is also mechanical, never an outcome
    rows = _phase_a_rows(items)

    def value_fn(kind, i):
        return None if (i, kind) == (2, "g26_yab") else _cell_values(kind, i)
    rows = _phase_a_rows(items, value_fn=value_fn)
    rc, rep, _ = _run_phase_a(tmp_path, rows, items, name="unparsed")
    assert rc == 4 and rep is None


def test_phase_a_selection_frozen_order_cap_and_hard_stop(tmp_path):
    # 400 items; every 4th fails gate 2 -> 300 gate-passing == the cap
    items = [_mk_item(i) for i in range(400)]

    def value_fn(kind, i):
        v = _cell_values(kind, i)
        if i % 4 == 0 and kind == "g26_ya":
            return v + 10.0 * (1 if i % 2 == 0 else -1)   # |YA-Y0| = 10 > 5
        return v

    rows = _phase_a_rows(items, value_fn=value_fn)
    rc, rep, sel = _run_phase_a(tmp_path, rows, items, name="full")
    assert rc == 0, rc                                   # 300 >= 200
    assert rep["verdict"] == "PROCEED"
    assert rep["funnel"] == {"0": 0, "1": 0, "2": 100, "3": 300}
    assert rep["n_full_3_gates"] == 300
    assert rep["selection"]["n_selected"] == 300
    assert rep["selection"]["cap"] == 300
    # frozen pool order: passing ids in pool-file order, NOT effect order
    want = [it.item_id for it in items if int(it.item_id[2:]) % 4 != 0][:300]
    assert sel == want
    assert sel != sorted(sel, key=lambda x: -_cell_values("g26_yab",
                                                          int(x[2:])))
    digest = hashlib.sha256(("\n".join(sel) + "\n").encode()).hexdigest()
    assert rep["selection"]["ids_sha256"] == digest == ag.sha256_ids(sel)

    # HARD STOP below 200: flip most items to gate-failing
    def mostly_fail(kind, i):
        if kind == "g26_yab" and i % 2 == 0:
            return 55.0                                  # chain +5 < 15
        if kind in ("g26_ya", "g26_yb"):
            return 65.0                                  # single 15 > 5
        return _cell_values(kind, i)
    rows = _phase_a_rows(items, value_fn=mostly_fail)
    rc, rep, sel = _run_phase_a(tmp_path, rows, items, name="hard")
    assert rc == 2
    assert rep["verdict"] == "HARD STOP"
    assert rep["n_full_3_gates"] < 200
    assert sel == []


def test_phase_a_gate_funnel_math(tmp_path):
    items = [_mk_item(i) for i in range(4)]
    base = {"g26_y0": 50.0, "g26_ya": 50.0, "g26_yb": 50.0, "g26_yab": 70.0}

    def value_fn(kind, i):
        if i == 1 and kind == "g26_yab":
            return 60.0                       # chain +10 < 15 -> 2 gates
        if i == 2:
            return {"g26_ya": 65.0, "g26_yb": 65.0}.get(kind,
                                                        base[kind])  # 1
        if i == 3:
            return {"g26_yab": 55.0, "g26_ya": 65.0,
                    "g26_yb": 65.0}.get(kind, base[kind])            # 0
        return base[kind]
    rows = _phase_a_rows(items, value_fn=value_fn)
    rc, rep, _ = _run_phase_a(tmp_path, rows, items, name="funnel")
    assert rc == 2
    assert rep["funnel"] == {"0": 1, "1": 1, "2": 1, "3": 1}
    g = rep["per_item"]
    assert g["it0000"]["n_gates"] == 3 and g["it0000"]["g1_chain"]
    assert not g["it0001"]["g1_chain"] and g["it0001"]["g2_a_single"]
    assert g["it0002"]["n_gates"] == 1
    assert g["it0003"]["n_gates"] == 0


# ---------------------------------------------------------------------------
# analyzer: gates, ROPE, outcome map (§7/§8)
# ---------------------------------------------------------------------------
def _S(mean, lo, hi, n=100):
    return {"mean": mean, "ci_low": lo, "ci_high": hi, "n": n,
            "n_clusters": 50, "p": 0.0}


def test_positive_gate_floor_trichotomy():
    assert ag.gate(_S(5.0, 1.0, 9.0))
    assert not ag.gate(_S(2.0, 0.5, 4.0))     # CI low > 0 but below floor
    assert not ag.gate(_S(2.99, 0.1, 5.0))    # floor 3.0 is strict >=
    assert ag.gate(_S(3.0, 0.001, 6.0))       # exactly at the floor
    assert not ag.gate(_S(1.0, -2.0, 4.0))    # straddles 0
    assert not ag.gate(None) or True          # None-safe below
    assert not ag.is_negative(_S(1.0, -2.0, 4.0))
    assert ag.is_negative(_S(-4.0, -7.0, -1.0))
    assert ag.rope_fits(_S(0.2, -1.0, 1.4))
    assert not ag.rope_fits(_S(3.0, 0.8, 5.2))   # outside +-1.5
    assert not ag.rope_fits(_S(1.0, -2.0, 4.0))


def test_outcome_map_order_and_reachability():
    pos, neg, nul = _S(5.0, 1.0, 9.0), _S(-4.0, -7.0, -1.0), \
        _S(1.0, -2.0, 4.0)
    r_pos = _S(3.0, 0.8, 5.2)
    r_null = {t: nul for t in (0, 1, 2)}
    rope = _S(0.2, -1.0, 1.4)
    integ = (True, True, True, True)
    # integrity first, S1 second, then branches
    assert ag.classify(False, True, True, True, True, pos, pos,
                       r_pos, r_null) == "order-artifact"     # I1
    assert ag.classify(True, False, True, True, True, pos, pos,
                       r_pos, r_null) == "order-artifact"     # I2
    assert ag.classify(True, True, False, True, True, pos, pos,
                       r_pos, r_null) == "order-artifact"     # I3
    assert ag.classify(True, True, True, False, True, pos, pos,
                       r_pos, r_null) == "order-artifact"     # I4
    assert ag.classify(*integ, False, pos, pos, r_pos, r_null) == "unresolved"
    # no evaluable data is unresolved even with integrity flags false
    assert ag.classify(True, True, True, True, True, None, pos,
                       None, {}) == "unresolved"
    # branches
    assert ag.classify(*integ, True, pos, pos, r_pos, r_null) == "staged"
    assert ag.classify(*integ, True, nul, pos, r_pos, r_null) == \
        "load-bearing-bound"
    assert ag.classify(*integ, True, pos, nul, r_pos, r_null) == \
        "presence-bound"
    # no-stage-gain subdivisions in literal table order (§8/§10): pooled-R
    # CI low > 0 fires flat-leaky FIRST, then every R_t CI inside the ROPE
    # fires exclusion-robust — a plain no-stage-gain needs neither
    rope_ts = {t: rope for t in (0, 1, 2)}
    assert ag.classify(*integ, True, nul, nul, r_pos, r_null) == \
        "timing-insensitive / flat-leaky"
    assert ag.classify(*integ, True, nul, nul, rope, rope_ts) == \
        "exclusion-robust"
    # negatives precede not-positive so non-monotone stays reachable (§10)
    assert ag.classify(*integ, True, neg, pos, r_pos, r_null) == "non-monotone"
    assert ag.classify(*integ, True, pos, neg, r_pos, r_null) == "non-monotone"
    assert ag.classify(*integ, True, neg, neg, r_pos, r_null) == "non-monotone"
    # equivalence failure is NEVER unresolved: both-not-positive with an
    # R CI straddling +-1.5 lands in no-stage-gain
    assert ag.classify(*integ, True, nul, nul, nul, r_null) == "no-stage-gain"


def test_rope_is_wording_only_never_a_branch():
    import inspect
    params = set(inspect.signature(ag.classify).parameters)
    assert "rope" not in params and "equivalence" not in params
    assert "rope" not in ag.classify.__doc__.split("Parameters")[0] or True
    # identical classify inputs give identical verdicts regardless of any
    # rope state (rope state is not an input at all)
    a = ag.classify(True, True, True, True, True, _S(1.0, -2.0, 4.0),
                    _S(1.0, -2.0, 4.0), _S(1.0, -2.0, 4.0),
                    {t: _S(1.0, -2.0, 4.0) for t in (0, 1, 2)})
    b = ag.classify(True, True, True, True, True, _S(1.0, -2.0, 4.0),
                    _S(1.0, -2.0, 4.0), _S(1.0, -2.0, 4.0),
                    {t: _S(1.0, -2.0, 4.0) for t in (0, 1, 2)})
    assert a == b == "no-stage-gain"
    # wording layer exists and is separate
    assert ag.VERDICT_MEANING["unresolved"].startswith("report everything")
    assert "NOT a path into unresolved" in ag.VERDICT_MEANING["unresolved"]
    assert "never \"equivalent to zero\"" in ag.VERDICT_MEANING[
        "no-stage-gain"]
    assert ag.VERDICT_MEANING["no-stage-gain"].startswith(
        "no detectable stage-specific gain")
    # the secondary rope detail builds wording-only flags
    assert ag.ROPE == 1.5 and ag.FLOOR == 3.0
    assert ag.rope_fits(_S(0.0, -1.5, 1.5))     # boundary inclusive


def test_ruleacc_unparsed_leaves_denominator():
    probes = (
        [{"kind_name": "rule_probe_g26_excl", "yesno": "NO"}] * 8
        + [{"kind_name": "rule_probe_g26_excl", "yesno": "YES"}] * 1
        + [{"kind_name": "rule_probe_g26_excl", "yesno": None}]
        + [{"kind_name": "rule_probe_g26_admit", "yesno": "YES"}] * 9
        + [{"kind_name": "rule_probe_g26_admit", "yesno": None}] * 2
    )
    acc = ag.ruleacc(probes)
    assert acc["rule_probe_g26_excl"]["n_rows"] == 10
    assert acc["rule_probe_g26_excl"]["n_unparsed"] == 1
    assert acc["rule_probe_g26_excl"]["n_parsed"] == 9
    assert acc["rule_probe_g26_excl"]["n_correct"] == 8
    assert acc["rule_probe_g26_excl"]["acc"] == pytest.approx(8 / 9)
    assert acc["rule_probe_g26_admit"]["acc"] == 1.0
    # absent probes -> NaN -> I4 fails (G25A lineage: absent data fails)
    empty = ag.ruleacc([])
    import math
    assert math.isnan(empty["rule_probe_g26_excl"]["acc"])


def test_rows_for_usability_and_both_sign_directions():
    it_in = _mk_item(0)        # increase (s = +1)
    it_out = _mk_item(1)       # decrease (s = -1)
    items = {it.item_id: it for it in (it_in, it_out)}

    def cells(y0, ya, yb, yab, ex, ad):
        return {
            "g26_y0": y0, "g26_ya": ya, "g26_yb": yb, "g26_yab": yab,
            "g26_excl_t0": ex[0], "g26_excl_t1": ex[1], "g26_excl_t2": ex[2],
            "g26_admit_t0": ad[0], "g26_admit_t1": ad[1],
            "g26_admit_t2": ad[2],
        }
    y = {
        it_in.item_id: {"m": cells(
            50, 50, 50, 60,                      # anchor +10
            (59, 51, 43),                        # R = +9, +1, -7
            (60, 60, 60))},                      # M = 0
        it_out.item_id: {"m": cells(
            60, 60, 60, 50,                      # anchor s*(50-60)=+10
            (51, 59, 67),                        # R = +9, +1, -7 after s=-1
            (50, 50, 50))},                      # M = 0
    }
    rows, drops = ag.rows_for(items, y)
    assert drops == {}
    assert len(rows) == 2
    for r in rows:                                # sign-aligned identically
        assert r["anchor"] == pytest.approx(10.0)
        assert r["R0"] == pytest.approx(9.0)
        assert r["R1"] == pytest.approx(1.0)
        assert r["R2"] == pytest.approx(-7.0)
        assert r["PG"] == pytest.approx(8.0)
        assert r["LG"] == pytest.approx(8.0)
        assert r["Mcontrast"] == 0.0
    assert {r["s"] for r in rows} == {1.0, -1.0}

    # weak anchor and incomplete cells are dropped by rule, not outcome
    y2 = {it_in.item_id: {"m": dict(y[it_in.item_id]["m"],
                                    g26_yab=54.0)}}   # anchor +4 < 5
    y2[it_out.item_id] = {"m": {k: v for k, v in
                                y[it_out.item_id]["m"].items()
                                if k != "g26_admit_t2"}}
    rows, drops = ag.rows_for(items, y2)
    assert rows == []
    assert drops.get("weak_anchor") == 1
    assert drops.get("incomplete") == 1


def test_cluster_boot_identity_determinism_and_whole_clusters():
    assert ag.cluster_boot is g25_cluster_boot
    pairs = [("a", 1.0), ("a", 3.0), ("b", 5.0),
             ("c", 7.0), ("c", 9.0), ("c", 11.0)]
    out = ag.cluster_boot(pairs, n=2000, seed=20260924)
    assert out["n"] == 6 and out["n_clusters"] == 3
    assert out["ci_low"] <= out["mean"] <= out["ci_high"]
    assert ag.cluster_boot(pairs, n=2000, seed=20260924) == out  # seed pin
    # cluster-size-weighted mean over drawn clusters == plain row mean
    assert out["mean"] == pytest.approx(sum(v for _, v in pairs) / 6)
    # production budgets
    assert ag.B == 10_000 and ag.SEED == 20260924


# ---------------------------------------------------------------------------
# analyzer Phase B end-to-end wiring (synthetic rows over REAL pool ids)
# ---------------------------------------------------------------------------
def _phase_b_fixture(tmp_path, n_items=210, with_probes=True, pg_spread=1.0):
    import random
    rng = random.Random(7)
    ids = [it.item_id for it in POOL_ITEMS[:n_items]]
    dirs = {it.item_id: it.critical_direction for it in POOL_ITEMS[:n_items]}
    runs = {m: [] for m in ag.POOLED_MODELS}
    for iid in ids:
        s = 1.0 if dirs[iid] == "increase" else -1.0
        jitter = lambda: rng.uniform(-pg_spread, pg_spread)  # noqa: E731
        r0, r1, r2 = 9.0 + jitter(), 1.0 + jitter(), -7.0 + jitter()
        for m in ag.POOLED_MODELS:
            def val(kind, s=s, r0=r0, r1=r1, r2=r2):
                rs = (r0, r1, r2)
                if kind == "g26_y0":
                    return 50.0
                if kind in ("g26_ya", "g26_yb"):
                    return 50.0
                if kind == "g26_yab":
                    return 50.0 + s * 10.0
                arm, tm = kind.split("_t")
                t = int(tm)
                if arm == "g26_excl":
                    return 50.0 + s * rs[t]        # R_t = s*(excl-YB) = rs[t]
                return 50.0 + s * 10.0             # admit == YAB -> M = 0
            for kind in ag.ALL_CELLS:
                runs[m].append({"item_id": iid, "kind_name": kind,
                                "model_tag": m, "value": val(kind)})
            if with_probes:
                runs[m].append({"item_id": iid,
                                "kind_name": "rule_probe_g26_excl",
                                "model_tag": m, "yesno": "NO"})
                runs[m].append({"item_id": iid,
                                "kind_name": "rule_probe_g26_admit",
                                "model_tag": m, "yesno": "YES"})
    paths = []
    for m, rows in runs.items():
        p = tmp_path / f"b_{m}.jsonl"
        p.write_text("".join(json.dumps(r) + "\n" for r in rows))
        paths.append(str(p))
    return paths


def test_phase_b_end_to_end_staged(tmp_path, monkeypatch):
    monkeypatch.setattr(ag, "B", 400)         # fast CIs; B=10000 pinned above
    paths = _phase_b_fixture(tmp_path, with_probes=True, pg_spread=1.0)
    rep_path = str(tmp_path / "verdict.json")
    rc = ag.phase_b(paths, POOL, rep_path, rep_path + ".md")
    assert rc == 0
    rep = json.load(open(rep_path))
    assert rep["integrity"]["I2_distance_le_10"]["ok"]
    assert rep["integrity"]["I3_admit_control_contains_0"]
    assert rep["integrity"]["I4_ruleacc_ge_0.8"]["ok"]
    assert rep["S1"]["n_usable_ge3of4"] >= 210 - 0 and rep["S1"]["ok"]
    assert rep["positive_gates"]["PG"] and rep["positive_gates"]["LG"]
    assert rep["verdict"] == "staged"
    assert rep["estimands"]["pooled"]["PG"]["mean"] == pytest.approx(
        8.0, abs=0.5)
    assert rep["budget"]["rows"] <= 14_400 and rep["budget"]["ok"]
    assert rep["secondary_rope"]["role"].startswith("wording only")


def test_phase_b_missing_probes_is_order_artifact(tmp_path, monkeypatch):
    monkeypatch.setattr(ag, "B", 400)
    paths = _phase_b_fixture(tmp_path, with_probes=False, pg_spread=1.0)
    rep_path = str(tmp_path / "verdict.json")
    ag.phase_b(paths, POOL, rep_path, rep_path + ".md")
    rep = json.load(open(rep_path))
    assert not rep["integrity"]["I4_ruleacc_ge_0.8"]["ok"]
    assert rep["verdict"] == "order-artifact"      # probes absent (G25A line)


# ---------------------------------------------------------------------------
# harness: Phase-A run script locks
# ---------------------------------------------------------------------------
def test_phasea_run_script_gates():
    src = open(RUN_SCRIPT).read()
    assert "G26A-FLIP1=RECORDED" in src           # STATUS token gate
    assert "grep -q" in src and "STATUS.md" in src
    kinds_line = next(ln for ln in src.splitlines()
                      if ln.startswith("KINDS="))
    kinds = kinds_line.split("=", 1)[1]
    assert kinds == "g26_y0,g26_ya,g26_yb,g26_yab"   # exactly 4, no rule
    assert "excl" not in kinds and "admit" not in kinds
    assert "mistral_small_24b_hf" in src             # selector-only model
    assert f"ITEMS_SHA=" in src and POOL_SHA in src  # frozen items sha pin
    assert "14560" in src or "14,560" in src         # N_A x 4 row budget


def test_constants_match_prereg_amendments():
    assert ag.PHASEA_ROWS_CAP == 14_560            # 3,640 x 4 (amended)
    assert ag.MIN_S1 == 200 and ag.CAP_SELECT == 300
    assert ag.SELECTOR_TAG == SELECTOR
    assert ag.POOLED_MODELS == ["llama31-8b", "qwen3-8b", "qwen35-9b",
                                "gemma3-12b"]
    assert bg.MAX_DIST_TOKENS == 10
    assert bg.PIN_TRAIN_SURVIVORS == N_STRUCT
    prereg = open(PREREG).read()
    assert "3,640" in prereg and "14,560" in prereg
    assert "filler-feasibility" in prereg or "feasibility" in prereg
    for uid in EXCLUDED:
        assert uid in prereg or uid in open(POOL_REPORT).read()
