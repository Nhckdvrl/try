"""G24A analysis — source-grounded natural-evidence confirmation.

Estimands (REI, signed leverage usability, winsorisation, probe readouts) are
inherited verbatim from ``analyze.build_table`` (G0); this module adds the
preregistration-frozen inference:

* **cluster bootstrap** (prereg §7): resample the frozen evidence clusters
  (FEVER first group-0 page / SciFact ``doc_id``, keyed ``source/cluster``);
  every row of a drawn cluster — across all models in a pooled stratum —
  moves together; the statistic is the cluster-size-weighted row mean, which
  equals the plain row mean of the concatenated clusters;
* **pooled-4 primary**: the four non-selection models; the selection model is
  reported separately;
* the **§8 literal decision-order classifier** with the §7 sufficiency gate
  evaluated first ("regardless of endpoint values").

Outputs: ``<out-prefix>.md`` (human report, verdict first) and
``<out-prefix>.json`` (all strata + classifier + integrity block).

Usage:
    PYTHONPATH=src python src/analyze_g24a.py \
        --runs results/raw/g24a_llama31-8b.jsonl ... \
        --items data/items/g24a_v1.jsonl \
        --tag g24a-v1 --out-prefix results/g24a/g24a_analysis_v1
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import random
import statistics as st
import sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(__file__))
from schema import load_items                      # noqa: E402
from analyze import build_table, wins              # noqa: E402

SEED = 20260924
B = 10000
METRICS = ("REI_pre", "REI_post", "delta_time", "UTB_norm")

DESIGN_TAG = "g24a-natural-evidence-confirmation-design-v1"
SELECTOR_TAG = "mistral-small-24b"
NON_SELECTOR = ["llama31-8b", "qwen3-8b", "qwen35-9b", "gemma3-12b"]
ALL_MODELS = sorted(NON_SELECTOR + [SELECTOR_TAG])
SUFFICIENCY_MIN = 300            # distinct usable pooled-4 items (prereg §7)
VERDICTS = ["natural-evidence-leak", "natural-evidence-leak-inconsistent",
            "prospective-only", "retrospective-only", "not-confirmed",
            "unresolved"]
LICENSED = {
    "natural-evidence-leak":
        "Excluded, human-annotated natural evidence still moves claim-likelihood "
        "judgments under a standing zero-use ruling, both when the ruling precedes "
        "the evidence and when it follows it — the G0 exclusion law replicates on "
        "source-grounded materials across models and datasets.",
    "natural-evidence-leak-inconsistent":
        "The leak replicates on natural evidence in the pooled panel, but it is "
        "not uniform across models or datasets.",
    "prospective-only":
        "Natural evidence leaks even when the zero-use ruling precedes it, but "
        "the retrospective arm is not distinguishable from zero.",
    "retrospective-only":
        "Natural evidence leaks only when the model has seen it before the "
        "ruling arrives (contradicts the G0 prospective-cost pattern on "
        "natural materials).",
    "not-confirmed":
        "On human-annotated natural evidence, excluded evidence did not "
        "measurably move judgments in this design.",
    "unresolved":
        "Design not evaluable as preregistered (sufficiency gate or data "
        "completeness failed); no confirmation claim is licensed.",
}


# ---------------------------------------------------------------------------
# frozen inference
# ---------------------------------------------------------------------------
def _cluster_boot_reps(pairs, n=None, seed=SEED):
    """Replicate means for METRICS under cluster resampling (test hook).

    Returns (point, reps) where reps[metric] has ``n`` resampled means.
    """
    n = n or B
    by = defaultdict(list)
    for key, vals in pairs:
        by[key].append(vals)
    keys = sorted(by)                       # deterministic across row orders
    K = len(keys)
    if K == 0:
        return ({m: float("nan") for m in METRICS},
                {m: [] for m in METRICS})
    stats = [(len(by[k]),
              tuple(sum(row[m] for row in by[k]) for m in METRICS))
             for k in keys]
    point = {m: st.mean([row[m] for k in keys for row in by[k]])
             for m in METRICS}
    rng = random.Random(seed)
    reps = {m: [] for m in METRICS}
    for _ in range(n):
        size = 0
        sums = [0.0] * len(METRICS)
        for _ in range(K):
            sz, sm = stats[rng.randrange(K)]
            size += sz
            for i in range(len(METRICS)):
                sums[i] += sm[i]
        for i, m in enumerate(METRICS):
            reps[m].append(sums[i] / size)
    return point, reps


def cluster_boot(pairs, n=None, seed=SEED):
    """(cluster_key, {metric: winsorised value}) rows -> per-metric CIs and p.

    Each replicate draws K clusters with replacement (K = distinct clusters in
    the stratum) and returns the cluster-size-weighted mean over the drawn
    clusters' rows — equal to the plain mean over concatenated rows.
    """
    n = n or B
    by = defaultdict(list)
    for key, vals in pairs:
        by[key].append(vals)
    if not by:
        return {m: (float("nan"),) * 3 for m in METRICS}
    point, reps = _cluster_boot_reps(pairs, n=n, seed=seed)
    out = {}
    for m in METRICS:
        r = sorted(reps[m])
        pm = point[m]
        if pm > 0:
            cnt = sum(1 for x in reps[m] if x <= 0)
        else:
            cnt = sum(1 for x in reps[m] if x >= 0)
        p = min(1.0, 2.0 * cnt / n)
        out[m] = (pm, r[int(0.025 * n)], r[int(0.975 * n)], p)
    return out


def summarize(rows, label):
    """G0-style summary with cluster bootstrap (rows already model-tagged)."""
    use = [r for r in rows if r["usable"]]
    if not use:
        return None
    res = {"label": label}
    pairs = [(r["_cluster"],
              {m: wins(r[m]) for m in METRICS}) for r in use]
    res.update(cluster_boot(pairs))
    ra = [r["p_use_pre"] for r in use if r["p_use_pre"] is not None]
    rb = [r["p_use_post"] for r in use if r["p_use_post"] is not None]
    rad = [r["p_use_admit"] for r in use if r["p_use_admit"] is not None]
    res["rule_acc_pre"] = 1 - st.mean(ra) if ra else float("nan")
    res["rule_acc_post"] = 1 - st.mean(rb) if rb else float("nan")
    res["rule_acc_admit"] = st.mean(rad) if rad else float("nan")
    res["n"] = len(use)
    res["n_rows"] = len(rows)
    res["n_clusters"] = len({r["_cluster"] for r in use})
    res["n_items"] = len({r["item_id"] for r in use})
    res["median_absL"] = st.median([abs(r["L"]) for r in use])
    res["frac_post_gt_pre"] = st.mean(
        [1.0 if r["delta_time"] > 0 else 0.0 for r in use])
    res["frac_post_gt_0.2"] = st.mean(
        [1.0 if r["REI_post"] > 0.2 else 0.0 for r in use])
    res["alignment_rate"] = st.mean([1.0 if r["signed_L"] > 0 else 0.0
                                     for r in rows])
    return res


# ---------------------------------------------------------------------------
# §8 literal decision order (sufficiency gate first, "regardless of endpoints")
# ---------------------------------------------------------------------------
def classify(sufficiency_ok, p1, p2, c1, c2):
    if not sufficiency_ok:
        return "unresolved"
    if p1 and p2 and c1 and c2:
        return "natural-evidence-leak"
    if p1 and p2 and (not c1 or not c2):
        return "natural-evidence-leak-inconsistent"
    if p1 and not p2:
        return "prospective-only"
    if p2 and not p1:
        return "retrospective-only"
    if not p1 and not p2:
        return "not-confirmed"
    return "unresolved"


def _pass(summary):
    """CI lower strictly > 0 (NaN/empty -> False)."""
    if summary is None:
        return False
    lo = summary["REI_pre"][1] if summary else float("nan")
    return not math.isnan(lo) and lo > 0


def _pass_post(summary):
    if summary is None:
        return False
    hi_lo = summary["REI_post"][1]
    return not math.isnan(hi_lo) and hi_lo > 0


# ---------------------------------------------------------------------------
# analysis
# ---------------------------------------------------------------------------
def load_runs(paths):
    """{model_tag: {item_id: {kind: row}}} with the frozen-panel guard."""
    runs: dict = defaultdict(lambda: defaultdict(dict))
    for p in paths:
        for line in open(p):
            if not line.strip():
                continue
            r = json.loads(line)
            tag = r.get("model_tag")
            if tag not in ALL_MODELS:
                raise SystemExit(
                    f"model_tag {tag!r} not in the frozen G24A panel "
                    f"{ALL_MODELS} (prereg §4)")
            runs[tag][r["item_id"]][r["kind_name"]] = r
    missing = [m for m in ALL_MODELS if m not in runs]
    if missing:
        raise SystemExit(
            f"missing model outputs for {missing} — mechanical incompleteness, "
            f"rerun those files (prereg §7); never re-select by outcome")
    return runs


def attach(rows, items_by_id, model_tag):
    """Add model/source/cluster/stratum identity to G0 build_table rows."""
    for row in rows:
        meta = items_by_id[row["item_id"]].meta
        row["model_tag"] = model_tag
        row["source"] = meta["source"]
        row["gold_label"] = meta["gold_label"]
        row["_cluster"] = f"{meta['source']}/{meta['cluster']}"
    return rows


def fmt(t):
    m, lo, hi, p = t
    return f"{m:+.3f} [{lo:+.3f},{hi:+.3f}] p={p:.4f}"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", nargs="+", required=True)
    ap.add_argument("--items", default="data/items/g24a_v1.jsonl")
    ap.add_argument("--tag", required=True)
    ap.add_argument("--out-prefix", required=True)
    args = ap.parse_args()

    items_list = load_items(args.items)
    items_by_id = {i.item_id: i for i in items_list}
    runs = load_runs(args.runs)

    # --- per-model rows (G0 build_table semantics) + completeness ledger ---
    all_rows, ledger = [], {}
    for tag in sorted(runs):
        present = set(runs[tag])
        expected = set(items_by_id)
        rows = build_table([items_by_id[i] for i in sorted(present)
                            if i in items_by_id],
                           runs[tag])
        rows = attach(rows, items_by_id, tag)
        all_rows.extend(rows)
        complete = {r["item_id"] for r in rows}
        ledger[tag] = {
            "expected": len(expected),
            "complete": len(complete),
            "partial": len((present & expected) - complete),
            "absent": len(expected - present),
        }

    def sel(rowset, pred=lambda r: True):
        return [r for r in rowset if pred(r)]

    out = [f"# G24A results — {args.tag}", "",
           "REI: 0 = ignored the excluded evidence, 1 = used it as admitted. "
           "Winsorised at +/-3; CIs are 10,000-resample **cluster** bootstraps "
           f"over evidence clusters (seed {SEED}); cluster key = "
           "`source/first-evidence-page-or-doc_id`.",
           f"Prereg: `preregistrations/PREREGISTRATION_G24A_NATURAL_EVIDENCE.md` "
           f"(tag `{DESIGN_TAG}`).",
           f"Selection model `{SELECTOR_TAG}` is excluded from pooled-4 "
           "(item set conditioned on its own Admit leverage).", ""]

    # --- strata -----------------------------------------------------------
    strata: dict = {}
    pooled4 = sel(all_rows, lambda r: r["model_tag"] in NON_SELECTOR)
    pooled5 = all_rows

    def block(name, rows):
        s = summarize(rows, name)
        strata[name] = s
        if s is None:
            out.append(f"{name}: no usable items"); out.append("")
            return s
        out.append(f"## {name}")
        out.append(f"n={s['n']}/{s['n_rows']} items={s['n_items']} "
                   f"clusters={s['n_clusters']}  median|L|={s['median_absL']:.1f}  "
                   f"alignment={s['alignment_rate']:.2f}")
        out.append(f"    RuleAcc  exclude-pre {s['rule_acc_pre']:.3f}  "
                   f"exclude-post {s['rule_acc_post']:.3f}  "
                   f"(admit-control p(YES) {s['rule_acc_admit']:.3f})")
        out.append(f"    REI_pre   {fmt(s['REI_pre'])}")
        out.append(f"    REI_post  {fmt(s['REI_post'])}")
        out.append(f"    d_time    {fmt(s['delta_time'])}   "
                   f"items post>pre: {s['frac_post_gt_pre']:.2f}")
        out.append(f"    UTB_norm  {fmt(s['UTB_norm'])}")
        out.append(f"    items REI_post>0.2: {s['frac_post_gt_0.2']:.2f}")
        out.append("")
        return s

    block("pooled-4 (primary)", pooled4)
    block("pooled-5 (incl. selection model)", pooled5)
    for tag in ALL_MODELS:
        block(f"model {tag}", sel(all_rows, lambda r, t=tag: r["model_tag"] == t))
    for source in ("fever", "scifact"):
        block(f"pooled-4 {source}",
              sel(pooled4, lambda r, s=source: r["source"] == s))
    for source, label in (("fever", "SUPPORTS"), ("fever", "REFUTES"),
                          ("scifact", "SUPPORT"), ("scifact", "CONTRADICT")):
        block(f"pooled-4 {source}/{label}",
              sel(pooled4, lambda r, s=source, l=label:
                  r["source"] == s and r["gold_label"] == l))

    # --- §7 endpoints and §8 classifier -----------------------------------
    p4 = strata.get("pooled-4 (primary)")
    p1 = _pass(p4)
    p2 = _pass_post(p4)
    per_model = {t: strata.get(f"model {t}") for t in ALL_MODELS}
    c1_models = [t for t in ALL_MODELS
                 if per_model[t] is not None
                 and per_model[t]["REI_pre"][0] > 0
                 and per_model[t]["REI_post"][0] > 0]
    c1 = len(c1_models) >= 4
    src_ok = {}
    for source in ("fever", "scifact"):
        s = strata.get(f"pooled-4 {source}")
        src_ok[source] = bool(s and s["REI_pre"][0] > 0 and s["REI_post"][0] > 0)
    c2 = all(src_ok.values())
    usable_items = len({r["item_id"] for r in pooled4 if r["usable"]})
    sufficiency_ok = usable_items >= SUFFICIENCY_MIN
    verdict = classify(sufficiency_ok, p1, p2, c1, c2)

    out.insert(6, "## Verdict")
    out.insert(7, f"**{verdict}**")
    out.insert(8, "")
    out.insert(9, LICENSED[verdict])
    out.insert(10, "")
    out.insert(11, "- P1 (REI_pre pooled-4 CI lower > 0): "
                  f"{'PASS' if p1 else 'FAIL'} — "
                  f"{fmt(p4['REI_pre']) if p4 else 'no usable rows'}")
    out.insert(12, "- P2 (REI_post pooled-4 CI lower > 0): "
                  f"{'PASS' if p2 else 'FAIL'} — "
                  f"{fmt(p4['REI_post']) if p4 else 'no usable rows'}")
    out.insert(13, "- C1 (both REI points > 0 in ≥4/5 models): "
                  f"{'PASS' if c1 else 'FAIL'} — {len(c1_models)}/5 "
                  f"({', '.join(c1_models) if c1_models else 'none'})")
    out.insert(14, "- C2 (both REI points > 0 within each source): "
                  f"{'PASS' if c2 else 'FAIL'} — "
                  + ", ".join(f"{k}={'pass' if v else 'fail'}"
                              for k, v in src_ok.items()))
    out.insert(15, "- Sufficiency gate (pooled-4 usable items ≥ "
                  f"{SUFFICIENCY_MIN}): {'PASS' if sufficiency_ok else 'FAIL'} — "
                  f"{usable_items}/{len(items_list)} selected items")
    out.insert(16, "")

    # --- integrity ---------------------------------------------------------
    incomplete = {t: l for t, l in ledger.items()
                  if l["partial"] or l["absent"]}
    out.append("## Integrity")
    out.append(f"- models present: {sorted(runs)} (frozen panel required)")
    out.append(f"- per-model completeness ledger: {json.dumps(ledger)}")
    if incomplete:
        out.append(f"- **INCOMPLETE model outputs: {incomplete} — rerun "
                   "mechanically before interpreting (prereg §7)**")
    else:
        out.append("- all selected items have complete five-condition rows "
                   "in all five models")
    out.append("")

    txt = "\n".join(out)
    print(txt)
    os.makedirs(os.path.dirname(args.out_prefix) or ".", exist_ok=True)
    open(args.out_prefix + ".md", "w").write(txt + "\n")

    def slim(s):
        if s is None:
            return None
        return {k: (list(v) if isinstance(v, tuple) else v)
                for k, v in s.items()}

    json.dump(
        dict(tag=args.tag, design_tag=DESIGN_TAG, seed=SEED, B=B,
             winsor=3.0, selector_model=SELECTOR_TAG,
             non_selector_models=NON_SELECTOR,
             sufficiency_min=SUFFICIENCY_MIN,
             usable_pooled4_items=usable_items,
             selected_total=len(items_list),
             verdict=verdict, licensed=LICENSED[verdict],
             endpoints=dict(P1=p1, P2=p2, C1=c1, C1_models=c1_models, C2=c2,
                            sources=src_ok, sufficiency=sufficiency_ok),
             strata={k: slim(v) for k, v in strata.items()},
             ledger=ledger,
             items_sha256=hashlib.sha256(open(args.items, "rb").read()).hexdigest(),
             runs_sha256={p: hashlib.sha256(open(p, "rb").read()).hexdigest()
                          for p in args.runs}),
        open(args.out_prefix + ".json", "w"), indent=1, ensure_ascii=False)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
