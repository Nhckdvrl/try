"""Stage-2 analysis: separating decision proximity (H-A), prospective binding
(H-B) and linguistic scope (H-C).

1. POSITION  REI ~ b0 + b1*Distance + b2*Before + b3*Distance:Before
             Distance is the measured token count from the RULING block to the
             answer position, so the two arms overlap in distance and the terms
             are identifiable.
2. IDBIND    identical rule sentence in both orders, no directional anaphora,
             plus a binding-cue-only variant.
3. WEIGHT    requested weight vs effective weight, by position.
"""
import argparse, json, os, sys, random, statistics as st
from collections import defaultdict
sys.path.insert(0, os.path.dirname(__file__))
import numpy as np
from schema import load_items
from analyze import boot_ci, boot_p, wins
import conditions_v2 as v2

ROOT = os.path.join(os.path.dirname(__file__), "..")


def load(tag):
    runs = defaultdict(dict)
    p = os.path.join(ROOT, "results", "raw", f"{tag}_stage2.jsonl")
    for line in open(p):
        r = json.loads(line)
        runs[r["item_id"]][r["kind_name"]] = r
    return runs


def anchored(runs, items, base_key, adm_keys):
    """item_id -> (base_value, |L|, sign) for items with usable leverage."""
    out = {}
    for iid, r in runs.items():
        it = items.get(iid)
        if it is None or base_key not in r or r[base_key].get("value") is None:
            continue
        if any(k not in r or r[k].get("value") is None for k in adm_keys):
            continue
        s = 1.0 if it.critical_direction == "increase" else -1.0
        y0 = r[base_key]["value"]
        L = st.mean(r[k]["value"] for k in adm_keys) - y0
        if s * L <= 0:
            continue
        out[iid] = (y0, abs(L), s)
    return out


def rei(runs, anch, iid, cond):
    r = runs[iid].get(cond)
    if r is None or r.get("value") is None:
        return None
    y0, absL, s = anch[iid]
    return s * (r["value"] - y0) / absL


def cluster_of(it):
    if it.task_family == "legal_judgment":
        return "legal:" + it.meta["case"]
    return it.task_family + ":" + it.base_context[:60]


def ols_cluster_boot(X, y, clusters, n=4000, seed=0):
    """OLS with a cluster bootstrap over the design."""
    beta = np.linalg.lstsq(X, y, rcond=None)[0]
    by = defaultdict(list)
    for i, c in enumerate(clusters):
        by[c].append(i)
    ks = list(by)
    rng = random.Random(seed)
    reps = []
    for _ in range(n):
        idx = []
        for _ in range(len(ks)):
            idx += by[ks[rng.randrange(len(ks))]]
        try:
            reps.append(np.linalg.lstsq(X[idx], y[idx], rcond=None)[0])
        except np.linalg.LinAlgError:
            pass
    R = np.array(reps)
    lo = np.percentile(R, 2.5, axis=0)
    hi = np.percentile(R, 97.5, axis=0)
    p = 2 * np.minimum((R <= 0).mean(axis=0), (R >= 0).mean(axis=0))
    return beta, lo, hi, p


def run_tag(tag, items, out):
    runs = load(tag)
    out.append(f"\n# {tag}\n")

    # ---------------- 1. position factorial ----------------
    anch = anchored(runs, items, "base", ["pos_adm_pre_d0", "pos_adm_post_d0"])
    out.append(f"## 1. Rule-position factorial   (n usable = {len(anch)})\n")
    out.append(f"| condition | rule->answer tokens (median) | REI [95% CI] |")
    out.append("|---|---:|---|")
    rows = []
    for cond in v2.POSITION_CONDITIONS:
        vals, dists, cls = [], [], []
        for iid in anch:
            v = rei(runs, anch, iid, cond)
            if v is None:
                continue
            vals.append(wins(v))
            dists.append(runs[iid][cond].get("rule_to_answer_tokens"))
            cls.append(cluster_of(items[iid]))
        if not vals:
            continue
        m, lo, hi = boot_ci(vals, n=4000, seed=3)
        out.append(f"| `{cond}` | {st.median([d for d in dists if d]):.0f} | "
                   f"{m:+.3f} [{lo:+.3f}, {hi:+.3f}] |")
        if cond.startswith("pos_exc"):
            before = 1.0 if "_pre_" in cond else 0.0
            for v, d, c in zip(vals, dists, cls):
                if d:
                    rows.append((v, d / 100.0, before, c))
    if rows:
        y = np.array([r[0] for r in rows])
        X = np.column_stack([np.ones(len(rows)),
                             [r[1] for r in rows],
                             [r[2] for r in rows],
                             [r[1] * r[2] for r in rows]])
        beta, lo, hi, p = ols_cluster_boot(X, y, [r[3] for r in rows], seed=1)
        names = ["intercept", "Distance (per 100 tok)", "Before (rule precedes E)",
                 "Distance x Before"]
        out.append(f"\nExclusion arm only, REI ~ Distance + Before + Distance:Before "
                   f"(n = {len(rows)} item-conditions, cluster bootstrap):\n")
        out.append("| term | coef | 95% CI | p |")
        out.append("|---|---|---|---|")
        for i, nm in enumerate(names):
            out.append(f"| {nm} | {beta[i]:+.4f} | [{lo[i]:+.4f}, {hi[i]:+.4f}] | {p[i]:.4f} |")

    # ---------------- 2. ID binding ----------------
    anch2 = anchored(runs, items, "id_base", ["id_admit_pre", "id_admit_post"])
    out.append(f"\n## 2. Identifier binding, no directional anaphora   (n = {len(anch2)})\n")
    out.append("| condition | REI [95% CI] |")
    out.append("|---|---|")
    store = {}
    for cond in ["id_exclude_pre", "id_exclude_post", "id_exclude_pre_marker"]:
        vals = [wins(v) for iid in anch2 if (v := rei(runs, anch2, iid, cond)) is not None]
        store[cond] = vals
        m, lo, hi = boot_ci(vals, n=4000, seed=4)
        out.append(f"| `{cond}` | {m:+.3f} [{lo:+.3f}, {hi:+.3f}] |")
    a, b = store["id_exclude_pre"], store["id_exclude_post"]
    if len(a) == len(b):
        d = [x - y for x, y in zip(a, b)]
        m, lo, hi = boot_ci(d, n=4000, seed=5)
        out.append(f"\n- pre - post with an identical rule sentence: "
                   f"{m:+.3f} [{lo:+.3f}, {hi:+.3f}] p={boot_p(d, n=4000, seed=6):.4f}")
    a, c = store["id_exclude_pre"], store["id_exclude_pre_marker"]
    if len(a) == len(c):
        d = [x - y for x, y in zip(a, c)]
        m, lo, hi = boot_ci(d, n=4000, seed=7)
        out.append(f"- pre - pre_with_binding_marker: {m:+.3f} [{lo:+.3f}, {hi:+.3f}] "
                   f"p={boot_p(d, n=4000, seed=8):.4f}")

    # ---------------- 3. requested-weight sweep ----------------
    anch3 = anchored(runs, items, "base", ["w100_pre", "w100_post"])
    out.append(f"\n## 3. Requested weight vs effective weight   (n = {len(anch3)})\n")
    out.append("| requested w | effective w, rule BEFORE evidence | effective w, rule AFTER |")
    out.append("|---:|---|---|")
    for key in ["w000", "w025", "w050", "w075", "w100"]:
        cells = []
        for arm in ("pre", "post"):
            vals = [wins(v) for iid in anch3
                    if (v := rei(runs, anch3, iid, f"{key}_{arm}")) is not None]
            m, lo, hi = boot_ci(vals, n=4000, seed=9)
            cells.append(f"{m:+.3f} [{lo:+.3f}, {hi:+.3f}]")
        out.append(f"| {v2.WEIGHTS[key][1]:.2f} | " + " | ".join(cells) + " |")
    # error vs requested, by arm
    out.append("\nAbsolute error |w_effective - w_requested|, averaged over the five levels:")
    for arm in ("pre", "post"):
        errs = []
        for key in v2.WEIGHTS:
            tgt = v2.WEIGHTS[key][1]
            for iid in anch3:
                v = rei(runs, anch3, iid, f"{key}_{arm}")
                if v is not None:
                    errs.append(abs(wins(v) - tgt))
        m, lo, hi = boot_ci(errs, n=4000, seed=10)
        out.append(f"- rule {'BEFORE' if arm == 'pre' else 'AFTER '} evidence: "
                   f"{m:.3f} [{lo:.3f}, {hi:.3f}]")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tags", nargs="+")
    args = ap.parse_args()
    items = {i.item_id: i for i in load_items(os.path.join(ROOT, "data", "items", "items_v1.jsonl"))}
    out = ["# Stage 2 — separating proximity, prospective binding and scope", "",
           "REI is the effective weight the model gives the critical evidence: 0 = decided",
           "as if it had never been seen, 1 = used as fully as when the rule permits it."]
    for t in args.tags:
        try:
            run_tag(t, items, out)
        except FileNotFoundError:
            out.append(f"\n# {t}: not run yet\n")
    txt = "\n".join(out)
    print(txt)
    open(os.path.join(ROOT, "results", "stage2_tables.md"), "w").write(txt + "\n")


if __name__ == "__main__":
    main()
