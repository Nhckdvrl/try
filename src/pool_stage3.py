"""Pooled test of the zero-discontinuity across models.

Each model alone has ~140 items, which leaves the I[w=0]xBefore interaction
underpowered. Pooling with model fixed effects and clustering the bootstrap on
(model, case skeleton) tests the same term on the full design.
"""
import json, os, sys, statistics as st
from collections import defaultdict
sys.path.insert(0, os.path.dirname(__file__))
import numpy as np
from schema import load_items
from analyze import wins
from analyze_stage2 import cluster_of, ols_cluster_boot
from analyze_stage3 import load, anchor, rei
import conditions_v3 as v3

ROOT = os.path.join(os.path.dirname(__file__), "..")


def main(tags):
    items = {i.item_id: i for i in load_items(os.path.join(ROOT, "data", "items", "items_v1.jsonl"))}
    rows, mods = [], []
    per_gap = defaultdict(list)
    for tag in tags:
        try:
            runs = load(tag)
        except FileNotFoundError:
            continue
        A = anchor(runs, items, "base", ["nz1000_pre", "nz1000_post"])
        for key, w in v3.NZ_LEVELS.items():
            for arm, before in (("pre", 1.0), ("post", 0.0)):
                for iid in A:
                    v = rei(runs, A, iid, f"{key}_{arm}")
                    if v is None:
                        continue
                    rows.append((wins(v), w, before, before * (1.0 if w == 0 else 0.0),
                                 f"{tag}|{cluster_of(items[iid])}", tag))
            a = {i: rei(runs, A, i, f"{key}_pre") for i in A}
            b = {i: rei(runs, A, i, f"{key}_post") for i in A}
            ks = [i for i in A if a[i] is not None and b[i] is not None]
            if ks:
                per_gap[w].append((tag, st.mean(wins(a[i]) - wins(b[i]) for i in ks)))
        mods.append(tag)

    y = np.array([r[0] for r in rows])
    base = [np.ones(len(rows)), [r[1] for r in rows], [r[2] for r in rows],
            [r[1] * r[2] for r in rows], [r[3] for r in rows]]
    names = ["intercept", "w", "Before", "w x Before", "I[w=0] x Before"]
    for m in mods[1:]:                      # model fixed effects
        base.append([1.0 if r[5] == m else 0.0 for r in rows])
        names.append(f"model[{m}]")
    X = np.column_stack(base)
    beta, lo, hi, p = ols_cluster_boot(X, y, [r[4] for r in rows], n=3000, seed=1)

    out = ["# Pooled zero-discontinuity test", "",
           f"Models pooled: {', '.join(mods)}.  n = {len(rows)} item-conditions.",
           "Cluster bootstrap over (model x case skeleton); model fixed effects included.", "",
           "| term | coef | 95% CI | p |", "|---|---|---|---|"]
    for i, nm in enumerate(names):
        star = "**" if nm == "I[w=0] x Before" else ""
        out.append(f"| {star}{nm}{star} | {beta[i]:+.4f} | [{lo[i]:+.4f}, {hi[i]:+.4f}] | {p[i]:.4f} |")
    # The linear specification under-fits a step, so the headline test is a direct
    # per-item contrast: is the zero gap larger than the average non-zero gap?
    contrasts, cls = [], []
    for tag in mods:
        runs = load(tag)
        A = anchor(runs, items, "base", ["nz1000_pre", "nz1000_post"])
        for iid in A:
            def gap(k):
                a = rei(runs, A, iid, f"{k}_pre")
                b = rei(runs, A, iid, f"{k}_post")
                return None if a is None or b is None else wins(a) - wins(b)
            g0 = gap("nz0000")
            gs = [g for k in v3.NZ_LEVELS if v3.NZ_LEVELS[k] > 0 and (g := gap(k)) is not None]
            if g0 is not None and gs:
                contrasts.append(g0 - st.mean(gs))
                cls.append(f"{tag}|{cluster_of(items[iid])}")
    import random as _r
    by = defaultdict(list)
    for v, c in zip(contrasts, cls):
        by[c].append(v)
    ks = list(by)
    rng = _r.Random(0)
    reps = []
    for _ in range(10000):
        pool = []
        for _ in range(len(ks)):
            pool += by[ks[rng.randrange(len(ks))]]
        reps.append(st.mean(pool))
    reps.sort()
    m = st.mean(contrasts)
    lo_c, hi_c = reps[250], reps[9750]
    pv = 2 * min(sum(1 for r in reps if r <= 0), sum(1 for r in reps if r >= 0)) / len(reps)
    out += ["", "## Headline contrast", "",
            "Per item: (pre-post gap at w=0) minus (mean pre-post gap over the eight "
            "non-zero weights). Cluster bootstrap over (model x case skeleton).", "",
            f"**{m:+.3f} [{lo_c:+.3f}, {hi_c:+.3f}] p = {min(pv,1.0):.4f}**  (n = {len(contrasts)} items)"]

    out += ["", "Mean pre-post gap per requested weight, averaged over models:", "",
            "| requested w | mean gap | per-model |", "|---:|---|---|"]
    for w in sorted(per_gap):
        vals = [g for _, g in per_gap[w]]
        out.append(f"| {w:g} | {st.mean(vals):+.3f} | " +
                   ", ".join(f"{t}: {g:+.3f}" for t, g in per_gap[w]) + " |")
    txt = "\n".join(out)
    print(txt)
    open(os.path.join(ROOT, "results", "stage3_pooled.md"), "w").write(txt + "\n")


if __name__ == "__main__":
    main(sys.argv[1:] or ["qwen3-8b", "gemma3-12b", "phi4-mini"])
