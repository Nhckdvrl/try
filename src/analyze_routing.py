"""Stage-3B: prospective selective routing over a stream of tagged evidence.

Each item has an admitted group and an excluded group with well-separated means,
so the model's answer can be regressed on both:

    Y ~ a + b * mean_admitted + c * mean_excluded

b is fidelity to the admitted evidence (1.0 is correct), c is leakage from the
excluded evidence (0.0 is correct). `rt_oracle` (only admitted reports shown) and
`rt_naive` (all reports, no tags, no policy) bracket the scale: oracle should give
b=1,c=0 and naive should give b,c proportional to group sizes.
"""
import argparse, json, os, sys, random, statistics as st
from collections import defaultdict
sys.path.insert(0, os.path.dirname(__file__))
import numpy as np
from schema import load_items
from analyze_stage2 import ols_cluster_boot

ROOT = os.path.join(os.path.dirname(__file__), "..")
CONDS = ["rt_oracle", "rt_naive", "rt_pre", "rt_post"]
LABEL = {"rt_oracle": "oracle (only admitted shown)",
         "rt_naive": "naive (all reports, no policy)",
         "rt_pre": "policy BEFORE the reports",
         "rt_post": "policy AFTER the reports"}


def fit(rows, seed=0):
    """rows: (Y, mean_adm, mean_exc, cluster)"""
    y = np.array([r[0] for r in rows])
    X = np.column_stack([np.ones(len(rows)), [r[1] for r in rows], [r[2] for r in rows]])
    return ols_cluster_boot(X, y, [r[3] for r in rows], n=3000, seed=seed)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tags", nargs="+")
    args = ap.parse_args()
    items = {i.item_id: i for i in load_items(os.path.join(ROOT, "data", "items", "routing_v1.jsonl"))}

    out = ["# Stage 3B — prospective selective routing", "",
           "`Y ~ a + b*mean_admitted + c*mean_excluded`. b = fidelity to admitted evidence",
           "(correct: 1.0). c = leakage from excluded evidence (correct: 0.0). Cluster",
           "bootstrap over surface x size cells."]
    for tag in args.tags:
        p = os.path.join(ROOT, "results", "raw", f"{tag}_routing.jsonl")
        if not os.path.exists(p):
            out.append(f"\n# {tag}: not run yet")
            continue
        runs = defaultdict(dict)
        for line in open(p):
            r = json.loads(line)
            runs[r["item_id"]][r["kind_name"]] = r
        out.append(f"\n# {tag}\n")
        out.append("| condition | n | b (admitted) | c (leakage) | mean abs error vs oracle answer |")
        out.append("|---|---:|---|---|---|")
        for c in CONDS:
            rows, errs = [], []
            for iid, r in runs.items():
                it = items.get(iid)
                if it is None or c not in r or r[c].get("value") is None:
                    continue
                m = it.meta
                rows.append((r[c]["value"], m["mean_admitted"], m["mean_excluded"],
                             f"{it.surface_domain}:{m['N']}"))
                errs.append(abs(r[c]["value"] - m["mean_admitted"]))
            if len(rows) < 8:
                continue
            beta, lo, hi, pv = fit(rows, seed=1)
            out.append(f"| {LABEL[c]} | {len(rows)} | {beta[1]:+.3f} [{lo[1]:+.3f}, {hi[1]:+.3f}] "
                       f"| **{beta[2]:+.3f}** [{lo[2]:+.3f}, {hi[2]:+.3f}] p={pv[2]:.4f} "
                       f"| {st.mean(errs):.1f} |")
        # leakage by stream size
        out.append("\nLeakage coefficient c by number of reports in the stream:\n")
        out.append("| N reports | policy BEFORE | policy AFTER |")
        out.append("|---:|---|---|")
        for N in (2, 4, 8, 16):
            cells = []
            for c in ("rt_pre", "rt_post"):
                rows = []
                for iid, r in runs.items():
                    it = items.get(iid)
                    if it is None or it.meta["N"] != N or c not in r or r[c].get("value") is None:
                        continue
                    rows.append((r[c]["value"], it.meta["mean_admitted"],
                                 it.meta["mean_excluded"], it.surface_domain))
                if len(rows) < 6:
                    cells.append("—")
                    continue
                beta, lo, hi, pv = fit(rows, seed=2)
                cells.append(f"{beta[2]:+.3f} [{lo[2]:+.3f}, {hi[2]:+.3f}]")
            out.append(f"| {N} | " + " | ".join(cells) + " |")
        # rule probe
        for pk, nm in (("rule_probe_exclude_pre", "policy first"),
                       ("rule_probe_exclude_post", "policy last")):
            v = [r[pk]["p_yes"] for r in runs.values()
                 if pk in r and r[pk].get("p_yes") is not None]
            if v:
                out.append(f"- RuleAcc, {nm}: says NO with p = {1 - st.mean(v):.3f}")

    txt = "\n".join(out)
    print(txt)
    open(os.path.join(ROOT, "results", "routing_tables.md"), "w").write(txt + "\n")


if __name__ == "__main__":
    main()
