"""G26A frozen analyzer — Phase A gate funnel and Phase B one-shot verdict.

Everything follows preregistrations/PREREGISTRATION_G26A_LOAD_BEARING.md
(§5 selection gates, §6 estimands, §7 inference + branch procedure, §8
outcome map, §11 two-phase budget). Raw sign-aligned rating points house
metric (G23A/G25A discipline: no ratio primary, no trimming, no caps).

Phase A (`--phase a`) — selector only, blind by construction:
    Structural assertions run BEFORE any gate is computed:
      * selection blindness: the run file may contain ONLY the four
        no-rule cells (g26_y0/ya/yb/yab) and no probe row of any kind
        (§5 "no outcome of the experiment exists at selection time");
      * exactly one model_tag and it is the O1 selector;
      * row budget <= 14,560 (§11 feasibility amendment).
    Violation => exit 3 (structural), never a gate computation.
    Gates (§5, verbatim):
      1. s*(Y_AB - Y_0) >= 15          chain works
      2. |Y_A - Y_0| <= 5              A alone insufficient
      3. |Y_B - Y_0| <= 5              B alone insufficient
    Output: funnel of items passing 0/1/2/3 gates, run sha256, and — when
    n_full >= 200 (O4 min) — the selected IDs taken in FROZEN POOL ORDER
    (the pool file is written in frozen HoVer train order by build_g26a),
    capped at O4 = 300, plus sha256 of the ID list for §12B.  n_full < 200
    => HARD STOP (exit 2): no threshold loosening, no dev-split switch, no
    MuSiQue rescue (§11).

Phase B (`--phase b`) — the actual RQ3 experiment (needs STATUS flip #2):
    Inputs: the four pooled run JSONLs (rows carry `model_tag`; rule-probe
    rows ride the same files) + the frozen pool + the FROZEN Phase-A
    selection JSON (`--selection`: the selected item ids written by
    Phase A, 200 <= n <= 300).

    Checks run in this exact order (user ruling 2026-09-24, pre-tag):
      * STRUCTURAL (exit 3, NO report, no verdict): a model tag outside
        the frozen pooled-4 (extra/unknown model), duplicate
        (item, model, kind) row, stray kind, any row outside the frozen
        selection, selection not a subset of the pool or not in
        [200, 300], budget > 14,400 rows.
      * MECHANICAL (exit 4, NO report, no verdict): a pooled model absent
        from the panel; any selected item x 4 models x 10 cells or x 2
        probes missing; any cell value or probe YES/NO unparsed.  These
        are rerunnable gaps (§7 mechanical reruns only) — partial data is
        NEVER analyzed, and a missing row or unparsed probe is NEVER an
        "order artifact" (§8 mechanical-before-integrity rule).

    Usability O6 (per item x model, never outcome-filtered): all 10 cells
    present for that model AND s*(Y_AB - Y_0) >= 5.  S1 counts items
    usable on >= 3 of the frozen pooled-4 models: the threshold is the
    constant MIN_MODELS_USABLE = 3, never adapted to how many models were
    actually observed (the exact model-set assertion is what makes
    ">= 3/4" real); S1 >= 200 is the §8 sufficiency gate.

    Estimands (§6), per usable item x model:
        R_t = s * (Y_EXCL_t - Y_B)        leakage of A at timing t
        PG  = R_T0 - R_T1                 PresenceGain
        LG  = R_T1 - R_T2                 LoadGain
        M_t = s * (Y_ADMIT_t - Y_AB)      admit-timing control (I3)
        R~_t = R_t - M_t                  DiD sensitivity (reported always)
    s = +1 for "increase" (TRUE-claim establishing), -1 otherwise; both
    sign directions are exercised by tests (§9.8).

    Inference (§7): cluster bootstrap over TITLE PAIRS (O8) — cluster key
    = `title_pair::<t0>|<t1>` — K clusters resampled with replacement, all
    their rows (items x models) move together, B = 10,000, percentile 95%
    CIs, two-sided bootstrap p, seed 20260924.  `cluster_boot` is imported
    from analyze_g25 (single frozen source; a test pins the keying).

    Integrity gates (§8 taxonomy, user ruling 2026-09-24 — the three
    failure kinds are distinct verdicts, never conflated):
        I1 rule bytes identical across timings   (construction; tests)
        I2 shared-filler multiset + distance     recomputed here: every
            pool item's recorded `dist_max` <= 10 tokens (O7)
            I1 or I2 fail  => `structural-integrity-failure` (NO CLAIM —
            an implementation-level violation of the item construction,
            never a "scientific" order effect)
        I3 admit-timing control                  M_T0 - M_T2 pooled CI
            contains 0; fail => `order-artifact` — the ONLY gate that
            licenses that verdict (recency/position structure)
        I4 rule legibility: BOTH probe types present and parsed (a
            mechanical guarantee above), pooled RuleAcc >= 0.8 (EXCL
            probe expects "NO", ADMIT probe expects "YES"); fail =>
            `rule-legibility-failure` (NO CLAIM — the rule was not
            reliably read/retained; NOT a position artifact).
            Missing/unparsed probes never reach I4: they abort as
            mechanical exit 4 before any gate is computed.
        Label priority when several I-gates fail: structural ->
        rule-legibility -> order; the report always lists every failed
        gate.  Absent evaluable rows (all dropped by the preregistered
        O6 anchor) => `unresolved`, never an integrity verdict (G25A
        order).

    Branch decision (§7 user ruling 2026-09-24 + §8 table): a primary is
    **positive** iff cluster-bootstrap CI low > 0 AND point >= 3.0 (the
    project floor); **negative** iff CI high < 0; else **not positive**
    (only "no detectable effect" is licensed).  Precedence encoded from
    the table + §10 reachability ("every row is reachable a priori"):
        no evaluable rows    -> unresolved      (not an integrity event)
        I1 or I2 fail        -> structural-integrity-failure
        I4 fail (RuleAcc <0.8 with complete probes) -> rule-legibility-failure
        I3 fail              -> order-artifact
        S1 fail              -> unresolved
        PG or LG negative -> non-monotone   (a negative primary is also
            "not positive"; without this precedence `non-monotone` would
            be unreachable, contradicting §10 gate 4)
        both positive -> staged
        LG positive -> load-bearing-bound
        PG positive -> presence-bound
        else no-stage-gain, subdivided in literal table order:
            pooled R (row mean of R_T0..R_T2) CI low > 0 -> flat-leaky
            else every R_t CI within the secondary ROPE +-1.5 -> robust
            else plain no-stage-gain
    Equivalence (CI within +-1.5) is a SECONDARY characterization only:
    `classify` never receives it as input (unit-tested), and its failure
    never yields `unresolved` (user ruling, §7).  Not-positive labels are
    always written "no detectable ...", never "equivalent to zero".

Usage:
    PYTHONPATH=src python src/analyze_g26a.py --phase a \
        --runs results/raw/g26a_phasea_mistral-small-24b.jsonl \
        --items data/items/g26_phasea_pool_v1.jsonl \
        --report results/g26a/g26a_phasea_report_v1.json \
        --select-out data/items/g26a_selected_v1.json
    PYTHONPATH=src python src/analyze_g26a.py --phase b \
        --runs results/raw/g26a_{llama31-8b,qwen3-8b,qwen35-9b,gemma3-12b}.jsonl \
        --items data/items/g26_phasea_pool_v1.jsonl \
        --selection data/items/g26a_selected_v1.json \
        --report results/g26a/g26a_verdict_v1.json
"""
from __future__ import annotations

import argparse
import collections
import datetime as _dt
import hashlib
import json
import math
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from analyze_g25 import cluster_boot  # noqa: E402  frozen generic bootstrap
from conditions_g26a import (G26A_CONDITIONS, G26A_PROBES,  # noqa: E402
                             NORULE_CELLS, RULE_CELLS)
from schema import load_items  # noqa: E402

SEED = 20260924
B = 10_000
FLOOR = 3.0                 # positive-gate point floor (§7 user ruling)
ROPE = 1.5                  # secondary characterization band (O5)
MIN_MODELS_USABLE = 3       # S1 lineage: usable on >= 3/4 pooled models
MIN_S1 = 200                # O4 minimum
CAP_SELECT = 300            # O4 cap
PHASEA_ROWS_CAP = 14_560    # §11 (feasibility amendment): N_A = 3,640 x 4
PHASEB_ROWS_CAP = 14_400    # §11: selection <= 300 x 4 models x 12 rows
CHAIN_MIN = 15.0            # §5 gate 1
SINGLE_MAX = 5.0            # §5 gates 2-3
USABLE_ANCHOR_MIN = 5.0     # O6 usability anchor
RULEACC_MIN = 0.8           # I4
MAX_DIST_TOKENS = 10        # O7 / I2
SELECTOR_TAG = "mistral-small-24b"        # O1, Phase A only
POOLED_MODELS = ["llama31-8b", "qwen3-8b", "qwen35-9b", "gemma3-12b"]

CELL_Y0, CELL_YA, CELL_YB, CELL_YAB = NORULE_CELLS
ALL_CELLS = list(G26A_CONDITIONS)         # 10 cells (O3)


def sha256_file(path: str) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_ids(ids: list[str]) -> str:
    """sha256 of the selected-ID list as written (newline-joined + final NL)."""
    return hashlib.sha256(("\n".join(ids) + "\n").encode("utf-8")).hexdigest()


def s_of(item) -> float:
    return 1.0 if item.critical_direction == "increase" else -1.0


def cluster_of(item) -> str:
    """O8 cluster: the item's title pair (frozen HoVer sf0 -> sf1 pair)."""
    pair = item.meta.get("title_pair")
    if isinstance(pair, (list, tuple)):
        return "title_pair::" + "|".join(str(t) for t in pair)
    return f"title_pair::{pair}"


def gate(summary: dict | None) -> bool:
    """Positive gate (§7): CI low strictly > 0 AND point >= FLOOR."""
    if summary is None or summary["n"] == 0 or math.isnan(summary["ci_low"]):
        return False
    return summary["ci_low"] > 0.0 and summary["mean"] >= FLOOR


def is_negative(summary: dict | None) -> bool:
    """Negative (§7): CI high strictly < 0.  NaN-safe."""
    if summary is None or summary["n"] == 0 or math.isnan(summary["ci_high"]):
        return False
    return summary["ci_high"] < 0.0


def rope_fits(summary: dict | None) -> bool:
    """Secondary ROPE characterization (§7): CI fully inside [-1.5, +1.5].

    Wording only — never a branch input, never a veto (unit-tested).
    """
    if summary is None or summary["n"] == 0 or math.isnan(summary["ci_low"]):
        return False
    return summary["ci_low"] >= -ROPE and summary["ci_high"] <= ROPE


# ---------------------------------------------------------------------------
# Phase A — selector gate funnel (§5 / §11)
# ---------------------------------------------------------------------------
def phase_a(run_paths: list[str], items_path: str, report_path: str,
            select_out: str, md_path: str) -> int:
    # (0) SHA FIRST: the output file is hashed before it is parsed and
    # before any gate is computed (§11: freeze the output, then gates).
    run_shas = [{"path": p, "sha256": sha256_file(p)} for p in run_paths]
    items_list = load_items(items_path)
    items = {it.item_id: it for it in items_list}
    items_sha = sha256_file(items_path)
    expected_rows = 4 * len(items_list)   # exactly one row per item x kind

    y: dict = collections.defaultdict(dict)
    kinds_seen: collections.Counter = collections.Counter()
    tags_seen: collections.Counter = collections.Counter()
    pair_seen: collections.Counter = collections.Counter()
    unparsed: list[str] = []
    n_rows = 0
    for path in run_paths:
        with open(path) as handle:
            for line in handle:
                rec = json.loads(line)
                n_rows += 1
                kind = rec.get("kind_name", "")
                iid = rec.get("item_id", "")
                kinds_seen[kind] += 1
                tags_seen[rec.get("model_tag", "")] += 1
                pair_seen[(iid, kind)] += 1
                if kind in (ALL_CELLS + list(G26A_PROBES)):
                    if rec.get("value") not in (None, "None"):
                        y[iid][kind] = rec["value"]
                    else:
                        unparsed.append(f"{iid}:{kind}")

    # (1) STRUCTURAL assertions BEFORE any gate — selection blindness (§5:
    # no rule cell / no probe may exist in a Phase-A file), selector-only
    # (O1), uniqueness (exactly one row per item x kind), item-set identity,
    # row budget (§11). Any violation aborts with exit 3 and NO gate is
    # computed from partial or suspect data.
    rule_rows = sum(kinds_seen[k] for k in RULE_CELLS)
    probe_rows = sum(kinds_seen[k] for k in G26A_PROBES)
    stray = [k for k in kinds_seen if k not in ALL_CELLS
             and k not in G26A_PROBES]
    kinds_subset_ok = set(kinds_seen) <= set(NORULE_CELLS)
    dup = [f"{i}:{k}" for (i, k), c in pair_seen.items() if c > 1]
    unknown = sorted({i for (i, _k) in pair_seen if i not in items})
    budget_ok = n_rows <= PHASEA_ROWS_CAP
    models_ok = set(tags_seen) == {SELECTOR_TAG}
    violations = []
    if rule_rows or probe_rows or stray or not kinds_subset_ok:
        violations.append(f"blindness: rule_cell_rows={rule_rows} "
                          f"probe_rows={probe_rows} stray_kinds={stray}")
    if dup:
        violations.append(f"duplicate (item, kind) rows: {dup[:5]}")
    if unknown:
        violations.append(f"rows for unknown item_ids: {unknown[:5]}")
    if not models_ok:
        violations.append(f"models={dict(tags_seen)} != "
                          f"{{'{SELECTOR_TAG}'}}")
    if not budget_ok:
        violations.append(f"rows={n_rows} > budget cap {PHASEA_ROWS_CAP}")
    if violations:
        print("[phase-a] STRUCTURAL VIOLATION — no gates computed:",
              " | ".join(violations), file=sys.stderr)
        return 3

    # (2) COMPLETENESS — exactly the 4 no-rule kinds, exactly one row per
    # item x kind, every value parsed. Missing rows or unparsed decisions
    # are MECHANICAL incompleteness: rerun the affected rows first (§7
    # reruns are mechanical only); a partial file is never analyzed.
    if not (n_rows == expected_rows and not unparsed
            and set(kinds_seen) == set(NORULE_CELLS)):
        print(f"[phase-a] INCOMPLETE (mechanical) — rows {n_rows} / "
              f"expected {expected_rows} (= {len(items_list)} items x 4), "
              f"kinds={sorted(kinds_seen)}, unparsed={unparsed[:5]} — "
              "rerun the missing/unparsed rows; no gates computed.",
              file=sys.stderr)
        return 4

    # --- §5 gates, item by item, in FROZEN POOL ORDER (items file order) --
    funnel: collections.Counter = collections.Counter()
    drops: collections.Counter = collections.Counter()
    gate_counts: collections.Counter = collections.Counter()
    passing_ids: list[str] = []
    per_item: dict = {}
    for item in items_list:
        cells = y.get(item.item_id, {})
        missing = [k for k in NORULE_CELLS if k not in cells]
        if missing:
            drops["incomplete" if cells else "no_rows"] += 1
            continue
        s = s_of(item)
        y0, ya, yb, yab = (cells[CELL_Y0], cells[CELL_YA],
                           cells[CELL_YB], cells[CELL_YAB])
        g1 = s * (yab - y0) >= CHAIN_MIN
        g2 = abs(ya - y0) <= SINGLE_MAX
        g3 = abs(yb - y0) <= SINGLE_MAX
        n_pass = int(g1) + int(g2) + int(g3)
        funnel[n_pass] += 1
        per_item[item.item_id] = {"g1_chain": g1, "g2_a_single": g2,
                                  "g3_b_single": g3, "n_gates": n_pass,
                                  "y0": y0, "ya": ya, "yb": yb, "yab": yab,
                                  "s": s}
        if g1 and g2 and g3:
            passing_ids.append(item.item_id)
    unknown_rows = sum(1 for iid in y if iid not in items)
    drops["unknown_item"] = unknown_rows

    n_full = len(passing_ids)
    proceed = n_full >= MIN_S1
    selected = passing_ids[:CAP_SELECT] if proceed else []
    report = {
        "phase": "A", "date": _dt.date.today().isoformat(),
        "prereg": "preregistrations/PREREGISTRATION_G26A_LOAD_BEARING.md",
        "runs": run_shas,          # sha256 computed BEFORE parsing/gates
        "items": {"path": items_path, "sha256": items_sha,
                  "n": len(items_list)},
        "completeness": {
            "ok": True, "expected_rows": expected_rows,
            "rows": n_rows, "kinds": sorted(kinds_seen),
            "contract": "exactly the 4 no-rule kinds, exactly one parsed "
                        "row per item x kind (mechanical gap => exit 4, "
                        "rerun, never analyzed partially)",
            "unparsed": 0,
        },
        "blindness": {"ok": True, "rule_cell_rows": rule_rows,
                      "probe_rows": probe_rows, "kinds": dict(kinds_seen),
                      "assertion": "Phase A contains only the 4 no-rule cells"},
        "budget": {"rows": n_rows, "cap": PHASEA_ROWS_CAP, "ok": budget_ok},
        "selector": dict(tags_seen),
        "drops": dict(drops),
        "gates": {
            "g1_chain_ge_15": sum(1 for v in per_item.values() if v["g1_chain"]),
            "g2_a_single_le_5": sum(1 for v in per_item.values() if v["g2_a_single"]),
            "g3_b_single_le_5": sum(1 for v in per_item.values() if v["g3_b_single"]),
        },
        "funnel": {str(k): funnel.get(k, 0) for k in range(4)},
        "n_evaluable": len(per_item),
        "n_full_3_gates": n_full,
        "threshold": MIN_S1,
        "verdict": "PROCEED" if proceed else "HARD STOP",
        "selection": {
            "n_selected": len(selected), "cap": CAP_SELECT,
            "order": "frozen pool file order (build_g26a = HoVer train order)",
            "selected_ids": selected,
            "ids_sha256": sha256_ids(selected) if selected else None,
        },
        "per_item": per_item,
    }
    os.makedirs(os.path.dirname(report_path) or ".", exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=1, ensure_ascii=False)
    if select_out:
        os.makedirs(os.path.dirname(select_out) or ".", exist_ok=True)
        with open(select_out, "w", encoding="utf-8") as f:
            json.dump(selected, f, ensure_ascii=False, indent=1)

    md = [
        "# G26A Phase A — selector gate funnel",
        f"- date: {report['date']}",
        f"- run sha256: `{report['runs'][0]['sha256']}` "
        f"(rows {n_rows}/{PHASEA_ROWS_CAP}, selector {SELECTOR_TAG}, "
        f"exactly one parsed row per item x kind)",
        f"- items: `{items_path}` n={len(items_list)} "
        f"sha256=`{report['items']['sha256'][:16]}`",
        f"- blindness: PASS — {rule_rows} rule-cell rows, {probe_rows} probe rows",
        f"- drops: {dict(drops)}",
        f"- funnel (gates passed 0/1/2/3): "
        f"{[funnel.get(k, 0) for k in range(4)]}",
        f"- full 3-gate items: {n_full} (threshold {MIN_S1}) -> "
        f"**{report['verdict']}**",
        f"- selected: {len(selected)} <= {CAP_SELECT}, "
        f"ids sha256 `{report['selection']['ids_sha256']}`",
        "- NOTE: gates computed ONLY from Y0/YA/YB/YAB; no rule cell or "
        "probe exists in this file (selection blindness, §5).",
    ]
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")

    print(f"[phase-a] funnel 0/1/2/3 = "
          f"{[funnel.get(k, 0) for k in range(4)]}; full = {n_full} -> "
          f"{report['verdict']}")
    print(f"[phase-a] report -> {report_path} (md {md_path})")
    if select_out:
        print(f"[phase-a] selection -> {select_out} "
              f"({len(selected)} ids, sha256 {str(report['selection']['ids_sha256'])[:16]})")
    return 0 if proceed else 2


# ---------------------------------------------------------------------------
# Phase B — rows, usability, estimands (§6 / O6)
# ---------------------------------------------------------------------------
CELL_MISSING = object()

# canonical cell addressing used by rows_for
C_Y0, C_YA, C_YB, C_YAB = CELL_Y0, CELL_YA, CELL_YB, CELL_YAB
C_EXCL = [f"g26_excl_t{t}" for t in (0, 1, 2)]
C_ADMIT = [f"g26_admit_t{t}" for t in (0, 1, 2)]


def read_runs(run_paths: list[str]) -> dict:
    """Parse run JSONLs into decisions + probes + checkable tallies.

    Returns a dict (not a tuple — several independent checks consume it):
      y             item -> model -> kind -> parsed value (10-cell decisions)
      probes        list of raw probe records (both kinds, every model)
      tags          set of every model_tag value seen (incl. "" — an empty
                    tag is NOT in the frozen pooled-4 and trips the
                    structural model-set assertion)
      pair_counts   (item, model, kind) -> row count (duplicates = >1)
      dups          "item:model:kind" for count > 1        [structural]
      stray         kind_name values outside 10 cells + 2 probes [structural]
      unparsed_cells  cell rows with value None/"None"       [mechanical]
      unparsed_probes probe rows with yesno not in (YES, NO) [mechanical]
      n_rows        total records seen

    Structural/mechanical classification is decided by the caller
    (phase_b) — this function only collects the evidence.
    """
    y: dict = collections.defaultdict(lambda: collections.defaultdict(dict))
    probes: list[dict] = []
    tags: set = set()
    pair_counts: collections.Counter = collections.Counter()
    unparsed_cells: list[str] = []
    unparsed_probes: list[str] = []
    stray: list[str] = []
    n_rows = 0
    valid = set(ALL_CELLS) | set(G26A_PROBES)
    for path in run_paths:
        with open(path) as handle:
            for line in handle:
                rec = json.loads(line)
                n_rows += 1
                tag = rec.get("model_tag", "")
                tags.add(tag)
                kind = rec.get("kind_name", "")
                iid = rec.get("item_id", "")
                if kind not in valid:
                    stray.append(kind)
                    continue
                pair_counts[(iid, tag, kind)] += 1
                if kind in G26A_PROBES:
                    probes.append(rec)
                    if rec.get("yesno") not in ("YES", "NO"):
                        unparsed_probes.append(f"{iid}:{tag}:{kind}")
                elif rec.get("value") in (None, "None"):
                    unparsed_cells.append(f"{iid}:{tag}:{kind}")
                else:
                    y[iid][tag][kind] = rec["value"]
    dups = [f"{i}:{t}:{k}" for (i, t, k), c in pair_counts.items() if c > 1]
    return {
        "y": y, "probes": probes, "tags": tags,
        "pair_counts": pair_counts, "dups": dups, "stray": stray,
        "unparsed_cells": unparsed_cells,
        "unparsed_probes": unparsed_probes,
        "n_rows": n_rows,
    }


def rows_for(items: dict, y: dict) -> tuple[list[dict], dict]:
    """One row per usable item x model (O6): all 10 cells present AND
    s*(Y_AB - Y_0) >= 5.  Drop reasons never depend on an outcome beyond
    the preregistered anchor; rows are never dropped post hoc (§5 O6)."""
    rows, drops = [], collections.Counter()
    for item_id, by_model in y.items():
        item = items.get(item_id)
        if item is None:
            drops["unknown_item"] += 1
            continue
        s = s_of(item)
        cluster = cluster_of(item)
        for tag, cells in by_model.items():
            missing = [k for k in ALL_CELLS if k not in cells]
            if missing:
                drops["incomplete"] += 1
                continue
            anchor = s * (cells[C_YAB] - cells[C_Y0])
            if anchor < USABLE_ANCHOR_MIN:
                drops["weak_anchor"] += 1
                continue
            r = {t: s * (cells[C_EXCL[t]] - cells[C_YB]) for t in (0, 1, 2)}
            m = {t: s * (cells[C_ADMIT[t]] - cells[C_YAB]) for t in (0, 1, 2)}
            rt = {t: r[t] - m[t] for t in (0, 1, 2)}
            rows.append({
                "item_id": item_id, "model": tag, "cluster": cluster,
                "direction": item.critical_direction, "s": s, "anchor": anchor,
                "R0": r[0], "R1": r[1], "R2": r[2],
                "M0": m[0], "M1": m[1], "M2": m[2],
                "Rt0": rt[0], "Rt1": rt[1], "Rt2": rt[2],
                "PG": r[0] - r[1], "LG": r[1] - r[2],
                "PG_did": rt[0] - rt[1], "LG_did": rt[1] - rt[2],
                "Rbar": (r[0] + r[1] + r[2]) / 3.0,
                "Mcontrast": m[0] - m[2],
            })
    return rows, dict(drops)


def ruleacc(probes: list[dict]) -> dict:
    """I4 diagnostic: per rule type, fraction correct among parsed probes.

    phase_b enforces mechanical completeness FIRST (both probe types
    present and parsed for every selected item x model, else exit 4), so
    in the Phase-B path `n_unparsed` is always 0 and absent probes never
    reach this function — `n_unparsed`/NaN remain here as unit-level
    diagnostics only (G25A lineage: unparsed leaves the denominator)."""
    out = {}
    for probe, expect in (("rule_probe_g26_excl", "NO"),
                          ("rule_probe_g26_admit", "YES")):
        rows = [p for p in probes if p.get("kind_name") == probe]
        parsed = [p for p in rows if p.get("yesno") in ("YES", "NO")]
        correct = sum(1 for p in parsed if p["yesno"] == expect)
        out[probe] = {
            "expected": expect, "n_rows": len(rows),
            "n_unparsed": len(rows) - len(parsed), "n_parsed": len(parsed),
            "n_correct": correct,
            "acc": (correct / len(parsed)) if parsed else float("nan"),
        }
    return out


def summarise(rows: list[dict], key: str, subset=None) -> dict:
    pairs = [(r["cluster"], r[key]) for r in rows
             if subset is None or subset(r)]
    return cluster_boot(pairs, n=B, seed=SEED)


# ---------------------------------------------------------------------------
# §8 outcome map — literal firing order (see module docstring for lineage)
# ---------------------------------------------------------------------------
def classify(i1: bool, i2: bool, i3: bool, i4: bool, s1: bool,
             pg: dict | None, lg: dict | None, rbar: dict | None,
             r_ts: dict | None) -> str:
    """§8 outcome map, literal firing order (user ruling 2026-09-24).

    The three integrity failure kinds are DISTINCT verdicts:
      * I1/I2 construction invariant fails -> `structural-integrity-failure`
        (implementation-level NO CLAIM — never an order effect);
      * I4 fails with COMPLETE probes (RuleAcc < 0.8) ->
        `rule-legibility-failure` (NO CLAIM — the rule was not reliably
        read; never `order-artifact`);
      * I3 fails -> `order-artifact` — the ONLY gate licensing that
        verdict (recency/position structure in the admit-timing control).
    Missing/unparsed rows or probes never reach classify: phase_b aborts
    them as mechanical exit 4 before any gate is computed.

    Order: no evaluable data -> unresolved (G25A: absent data is not an
    integrity event) -> structural -> rule-legibility -> order -> S1 ->
    branches.  When several I-gates fail the label priority is
    structural -> rule-legibility -> order; phase_b's report always lists
    every failed gate.

    ``pg``/``lg`` are the pooled Primary/LoadGain cluster summaries; positive
    = gate() (CI low > 0 AND point >= 3.0); negative = CI high < 0.  The
    secondary ROPE is deliberately NOT an input (equivalence can never
    branch — user ruling 2026-09-24, unit-tested).  ``rbar`` is the pooled
    row-mean leakage summary (flat-leaky row); ``r_ts`` maps t -> summary
    for the exclusion-robust row (every CI inside +-1.5).
    """
    if pg is None or lg is None or pg["n"] == 0 or lg["n"] == 0 \
            or math.isnan(pg["ci_low"]) or math.isnan(lg["ci_low"]):
        return "unresolved"                  # no evaluable data (not integrity)
    if not (i1 and i2):
        return "structural-integrity-failure"   # construction violated
    if not i4:
        return "rule-legibility-failure"        # complete probes, RuleAcc < 0.8
    if not i3:
        return "order-artifact"                 # I3 admit-timing control only
    if not s1:
        return "unresolved"                  # sufficiency second
    pg_pos, lg_pos = gate(pg), gate(lg)
    if is_negative(pg) or is_negative(lg):
        return "non-monotone"                # negatives precede not-positive
    if pg_pos and lg_pos:
        return "staged"
    if lg_pos:
        return "load-bearing-bound"
    if pg_pos:
        return "presence-bound"
    # no-stage-gain subdivisions, literal table order
    if rbar is not None and rbar["n"] > 0 and not math.isnan(rbar["ci_low"]) \
            and rbar["ci_low"] > 0:
        return "timing-insensitive / flat-leaky"
    if r_ts and all(rope_fits(r_ts.get(t)) for t in (0, 1, 2)):
        return "exclusion-robust"
    return "no-stage-gain"


VERDICT_MEANING = {
    "staged": "binding builds in stages; both layers matter",
    "load-bearing-bound": ("mere presence is insufficient — making A "
                           "load-bearing through composition further improves "
                           "prospective binding; PG's own sentence stays "
                           "\"no detectable presence-stage gain\""),
    "presence-bound": ("presence adds a benefit; no detectable additional "
                       "load-bearing effect (never \"composition state "
                       "irrelevant\" — that needs a satisfied ROPE)"),
    "no-stage-gain": "no detectable stage-specific gain (never \"equivalent "
                     "to zero\")",
    "timing-insensitive / flat-leaky": "composition erases the timing "
                                       "structure while leakage persists",
    "exclusion-robust": "chains are excluded cleanly at every timing "
                        "(every R_t CI inside the secondary ROPE)",
    "non-monotone": "report as measured; no ordering claim",
    "structural-integrity-failure": "construction invariant violated (rule "
                                    "bytes / shared-filler +-10) — "
                                    "implementation-level NO CLAIM; never "
                                    "interpreted as an order effect",
    "rule-legibility-failure": "complete probes present but RuleAcc < 0.8 — "
                               "the rule was not reliably read/retained; NO "
                               "CLAIM (an integrity failure, not a position "
                               "artifact)",
    "order-artifact": "recency/position structure in the admit-timing "
                      "control (I3) — no claim until explained via R~",
    "unresolved": "report everything; no verdict (equivalence failure is "
                  "NOT a path into unresolved)",
}


# ---------------------------------------------------------------------------
# Phase B — the one-shot verdict (§11 Phase B budget: <= 14,400 rows)
# ---------------------------------------------------------------------------
def phase_b(run_paths: list[str], items_path: str, report_path: str,
            md_path: str, selection_path: str | None = None) -> int:
    if not selection_path:
        print("[phase-b] usage: --selection <frozen Phase-A selection JSON>",
              file=sys.stderr)
        return 5

    # (0) SHA FIRST: every input hashed before any parse or gate (§11).
    run_shas = [{"path": p, "sha256": sha256_file(p)} for p in run_paths]
    items_sha = sha256_file(items_path)
    selection_sha = sha256_file(selection_path)
    items_list = load_items(items_path)
    items = {it.item_id: it for it in items_list}

    # --- frozen selection guards (STRUCTURAL, exit 3) ----------------------
    try:
        with open(selection_path) as fh:
            selection = json.load(fh)
    except (OSError, ValueError) as exc:
        print(f"[phase-b] STRUCTURAL: unreadable selection "
              f"{selection_path}: {exc}", file=sys.stderr)
        return 3
    sel_ok = (isinstance(selection, list)
              and all(isinstance(x, str) for x in selection)
              and len(selection) == len(set(selection))
              and MIN_S1 <= len(selection) <= CAP_SELECT
              and set(selection) <= set(items))
    if not sel_ok:
        n_txt = len(selection) if isinstance(selection, list) \
            else "non-list"
        print(f"[phase-b] STRUCTURAL VIOLATION — no verdict: the frozen "
              f"selection must be a deduped list of pool items with "
              f"{MIN_S1} <= n <= {CAP_SELECT} (got n={n_txt})",
              file=sys.stderr)
        return 3
    sel_set = set(selection)
    expected_rows = len(selection) * len(POOLED_MODELS) * (
        len(ALL_CELLS) + len(G26A_PROBES))

    parsed = read_runs(run_paths)
    y, probes, tags = parsed["y"], parsed["probes"], parsed["tags"]
    n_rows = parsed["n_rows"]

    # (1) STRUCTURAL — BEFORE any gate: the model-tag set must equal the
    # frozen pooled-4 exactly (an extra/unknown model is a wrong-run
    # problem, exit 3), rows are unique per (item, model, kind), kinds are
    # only the 10 cells + 2 probes, every row belongs to the frozen
    # selection, budget <= 14,400 (§11). No verdict is ever computed from
    # a structurally suspect file.
    expected_models = set(POOLED_MODELS)
    unknown_models = sorted(t for t in tags if t not in expected_models)
    all_iids = {i for (i, _t, _k) in parsed["pair_counts"]}
    outside_sel = sorted(all_iids - sel_set)
    violations = []
    if unknown_models:
        violations.append(f"model tags outside the frozen pooled-4: "
                          f"{unknown_models} (expected exactly "
                          f"{sorted(POOLED_MODELS)})")
    if parsed["dups"]:
        violations.append(f"duplicate (item, model, kind) rows: "
                          f"{parsed['dups'][:5]}")
    if parsed["stray"]:
        violations.append(f"stray kinds: {sorted(set(parsed['stray']))[:5]}")
    if outside_sel:
        not_in_pool = [i for i in outside_sel if i not in items]
        violations.append(f"rows outside the frozen selection: "
                          f"{outside_sel[:5]}"
                          + (f" ({len(not_in_pool)} not in the pool)"
                             if not_in_pool else ""))
    if n_rows > PHASEB_ROWS_CAP:
        violations.append(f"rows={n_rows} > budget cap {PHASEB_ROWS_CAP}")
    if violations:
        print("[phase-b] STRUCTURAL VIOLATION — no verdict computed:",
              " | ".join(violations), file=sys.stderr)
        return 3

    # (2) MECHANICAL completeness — rerunnable gaps only (§7). The model
    # panel must be present; every selected item x pooled-4 x 10 cells and
    # x 2 probes must exist with parsed values. Missing rows, a missing
    # pooled model, or unparsed decisions/probes => exit 4: partial data
    # is NEVER analyzed, and a missing row is NEVER an order artifact.
    missing_models = sorted(expected_models - set(tags))
    missing: list[str] = []
    for iid in selection:
        for model in POOLED_MODELS:
            for kind in ALL_CELLS:
                if (iid, model, kind) not in parsed["pair_counts"]:
                    missing.append(f"{iid}:{model}:{kind}")
            for kind in G26A_PROBES:
                if (iid, model, kind) not in parsed["pair_counts"]:
                    missing.append(f"{iid}:{model}:{kind}")
    unparsed = parsed["unparsed_cells"] + parsed["unparsed_probes"]
    if missing_models or missing or unparsed:
        print(f"[phase-b] INCOMPLETE (mechanical) — missing pooled models: "
              f"{missing_models or 'none'}; missing rows {len(missing)} "
              f"first={missing[:3]}; unparsed {len(unparsed)} "
              f"first={unparsed[:3]}; rows {n_rows}/{expected_rows} "
              f"(= {len(selection)} selected x 4 models x 12) — rerun the "
              "gap; no verdict computed.", file=sys.stderr)
        return 4

    rows, drops = rows_for(items, y)

    # --- I2: O7 distance assertion over the pool (all items, all arms) ----
    dist_fail: list[str] = []
    for item in items_list:
        d = (item.meta.get("dist_max") or {})
        if not d or max(d.values()) > MAX_DIST_TOKENS:
            dist_fail.append(item.item_id)
    i2 = not dist_fail

    # --- I4: RuleAcc on both rule types -----------------------------------
    acc = ruleacc(probes)
    i4 = all(not math.isnan(v["acc"]) and v["acc"] >= RULEACC_MIN
             for v in acc.values())

    # --- S1: usable on >= 3 of the FROZEN pooled-4 models, >= 200 items ---
    # The threshold is the constant MIN_MODELS_USABLE = 3, never adapted to
    # how many models were observed (the exact model-set assertion above
    # makes ">= 3/4" real — no dynamic degradation to 2 of 2, 1 of 1...).
    usable = collections.Counter(r["item_id"] for r in rows)
    s1_items = [iid for iid, c in usable.items()
                if c >= MIN_MODELS_USABLE]
    s1 = len(s1_items) >= MIN_S1

    # --- estimand summaries (cluster bootstrap over title pairs, O8) ------
    if rows:
        pooled = {k: summarise(rows, k) for k in
                  ("PG", "LG", "R0", "R1", "R2", "Rbar", "Mcontrast",
                   "M0", "M1", "M2", "PG_did", "LG_did",
                   "Rt0", "Rt1", "Rt2")}
        i3 = (pooled["Mcontrast"]["n"] > 0
              and pooled["Mcontrast"]["ci_low"] <= 0 <= pooled["Mcontrast"]["ci_high"])
        per_model = {tag: {k: summarise(rows, k, lambda r, t=tag: r["model"] == t)
                           for k in ("PG", "LG")}
                     for tag in sorted({r["model"] for r in rows})}
        per_dir = {d: {k: summarise(rows, k, lambda r, dd=d: r["direction"] == dd)
                       for k in ("PG", "LG")}
                   for d in sorted({r["direction"] for r in rows})}
    else:
        pooled, per_model, per_dir = {}, {}, {}
        i3 = False

    i1 = True   # construction (rule bytes byte-fixed across timings; tests)
    verdict = classify(i1, i2, i3, i4, s1,
                       pooled.get("PG"), pooled.get("LG"),
                       pooled.get("Rbar"), {t: pooled.get(f"R{t}") for t in (0, 1, 2)})

    # --- secondary characterization (wording only, never a branch) --------
    rope = {}
    for name in ("PG", "LG", "R0", "R1", "R2", "M0", "M1", "M2",
                 "PG_did", "LG_did"):
        s = pooled.get(name)
        fits = rope_fits(s)
        rope[name] = {"fits": fits,
                      "wording": ("compatible with negligible gain"
                                  if fits else None)}
        if fits and s is not None:
            rope[name]["ci"] = [round(s["ci_low"], 3), round(s["ci_high"], 3)]

    report = {
        "phase": "B", "date": _dt.date.today().isoformat(),
        "prereg": "preregistrations/PREREGISTRATION_G26A_LOAD_BEARING.md",
        "runs": run_shas,          # sha256 computed BEFORE parsing/gates
        "items": {"path": items_path, "sha256": items_sha,
                  "n": len(items_list)},
        "selection": {"path": selection_path, "sha256": selection_sha,
                      "n": len(selection), "ids_sha256": sha256_ids(selection),
                      "min": MIN_S1, "cap": CAP_SELECT,
                      "order": "frozen Phase-A selection, as written"},
        "completeness": {
            "ok": True, "expected_rows": expected_rows, "rows": n_rows,
            "kinds": sorted(set(ALL_CELLS) | set(G26A_PROBES)),
            "contract": "model set == frozen pooled-4 exactly; one parsed "
                        "row per selected item x model x (10 cells + 2 "
                        "probes) — a gap is mechanical (exit 4, rerun) and "
                        "is never analyzed partially",
            "unparsed": 0,
        },
        "budget": {"rows": n_rows, "cap": PHASEB_ROWS_CAP,
                   "ok": n_rows <= PHASEB_ROWS_CAP},
        "models": {"expected": sorted(POOLED_MODELS),
                   "observed": sorted(tags),
                   "exact": set(tags) == expected_models},
        "n_rows_usable": len(rows), "drops": drops,
        "integrity": {
            "I1_rule_bytes": i1,
            "I2_distance_le_10": {"ok": i2, "n_fail": len(dist_fail),
                                  "fail_sample": dist_fail[:5]},
            "I3_admit_control_contains_0": i3,
            "I4_ruleacc_ge_0.8": {"ok": i4, "detail": acc},
        },
        "S1": {"n_usable_ge3of4": len(s1_items), "threshold": MIN_S1,
               "ok": s1, "models_for_3of4": MIN_MODELS_USABLE,
               "fixed": "constant 3 — never adapted to the observed "
                        "model count (model set asserted == pooled-4)"},
        "estimands": {
            "pooled": pooled,
            "per_model": per_model,
            "by_direction": per_dir,
        },
        "verdict": verdict,
        "verdict_meaning": VERDICT_MEANING[verdict],
        "positive_gates": {"PG": gate(pooled.get("PG")),
                           "LG": gate(pooled.get("LG")),
                           "floor": FLOOR,
                           "negatives": {"PG": is_negative(pooled.get("PG")),
                                         "LG": is_negative(pooled.get("LG"))}},
        "secondary_rope": {"delta": ROPE, "role": "wording only, never a branch",
                           "detail": rope},
        "seed": SEED, "B": B,
    }
    os.makedirs(os.path.dirname(report_path) or ".", exist_ok=True)
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=1, ensure_ascii=False)

    def line(name, s):
        if not s or s["n"] == 0:
            return f"- {name}: (no data)"
        return (f"- {name}: {s['mean']:+.3f} "
                f"[{s['ci_low']:+.3f}, {s['ci_high']:+.3f}] "
                f"n={s['n']} clusters={s['n_clusters']}")

    md = [
        "# G26A Phase B — one-shot verdict (frozen analyzer)",
        f"- date: {report['date']}",
        f"- selection: n={len(selection)} in [{MIN_S1},{CAP_SELECT}], "
        f"ids sha256 `{report['selection']['ids_sha256']}` — "
        f"rows {n_rows}/{expected_rows} (= n x 4 x 12, all parsed)",
        f"- models: pooled-4 exact — {sorted(tags)}",
        f"- rows: {n_rows} (cap {PHASEB_ROWS_CAP}); usable item x model rows: {len(rows)}",
        f"- drops: {drops}",
        f"- I-gates: I1 {i1} | I2 {'PASS' if i2 else 'FAIL'} "
        f"(dist fails {len(dist_fail)}) | I3 {'PASS' if i3 else 'FAIL'} | "
        f"I4 {'PASS' if i4 else 'FAIL'}",
        f"- S1: {len(s1_items)} items usable on >=3/4 models "
        f"(threshold {MIN_S1}) -> {'PASS' if s1 else 'FAIL'}",
        line("PG (PresenceGain)", pooled.get("PG")),
        line("LG (LoadGain)", pooled.get("LG")),
        line("R_T0", pooled.get("R0")), line("R_T1", pooled.get("R1")),
        line("R_T2", pooled.get("R2")),
        line("I3 admit contrast M_T0-M_T2", pooled.get("Mcontrast")),
        line("DiD PG~", pooled.get("PG_did")), line("DiD LG~", pooled.get("LG_did")),
        f"- **verdict: `{report['verdict']}`** — {report['verdict_meaning']}",
        "- secondary ROPE line(s): " + (
            "; ".join(f"{k} compatible with negligible gain"
                      for k, v in rope.items() if v["fits"]) or "(none fits)")
        + " [wording only; never changes the verdict]",
    ]
    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md) + "\n")

    print(f"[phase-b] verdict = {report['verdict']}")
    print(f"[phase-b] report -> {report_path} (md {md_path})")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--phase", required=True, choices=["a", "b"])
    ap.add_argument("--runs", required=True, nargs="+")
    ap.add_argument("--items", required=True)
    ap.add_argument("--report", required=True)
    ap.add_argument("--md", default=None,
                    help="default: report path with .md suffix")
    ap.add_argument("--select-out", default=None,
                    help="phase A: JSON array of selected item ids (n<=300)")
    ap.add_argument("--selection", default=None,
                    help="phase B (required): the FROZEN Phase-A selection "
                         "JSON (200..300 selected item ids)")
    args = ap.parse_args()
    md_path = args.md or (os.path.splitext(args.report)[0] + ".md")
    if args.phase == "a":
        return phase_a(args.runs, args.items, args.report,
                       args.select_out, md_path)
    if not args.selection:
        print("[phase-b] --selection is required (frozen Phase-A selection)",
              file=sys.stderr)
        return 5
    return phase_b(args.runs, args.items, args.report, md_path,
                   args.selection)


if __name__ == "__main__":
    sys.exit(main())
