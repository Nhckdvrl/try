"""G0 analysis: REI, temporal asymmetry, and the order-adjusted interaction.

Everything is item-level and paired.  CIs come from a paired bootstrap that
resamples ITEMS, so an effect carried by a handful of extreme items cannot look
significant.
"""
import argparse, json, os, sys, random, statistics as st
from collections import defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from schema import load_items

ROOT = os.path.join(os.path.dirname(__file__), "..")
B = 10000
WINSOR = 3.0


def boot_ci(vals, n=B, seed=0, stat=st.mean):
    if not vals:
        return (float("nan"),) * 3
    rng = random.Random(seed)
    k = len(vals)
    reps = []
    for _ in range(n):
        reps.append(stat([vals[rng.randrange(k)] for _ in range(k)]))
    reps.sort()
    return stat(vals), reps[int(0.025 * n)], reps[int(0.975 * n)]


def boot_p(vals, n=B, seed=1):
    """Two-sided bootstrap p for mean != 0 (proportion of resamples on the other side)."""
    if not vals:
        return float("nan")
    rng = random.Random(seed)
    k = len(vals)
    m = st.mean(vals)
    cnt = 0
    for _ in range(n):
        r = st.mean([vals[rng.randrange(k)] for _ in range(k)])
        if (r <= 0) if m > 0 else (r >= 0):
            cnt += 1
    return min(1.0, 2.0 * cnt / n)


def wins(x, c=WINSOR):
    return max(-c, min(c, x))


def build_table(items, runs, min_leverage_frac=0.0):
    """One row per item with all five conditions and the derived quantities."""
    rows = []
    for it in items:
        r = runs.get(it.item_id)
        if not r:
            continue
        need = ["base", "admit_pre", "admit_post", "exclude_pre", "exclude_post"]
        if any(k not in r or r[k]["value"] is None for k in need):
            continue
        y = {k: r[k]["value"] for k in need}
        s = 1.0 if it.critical_direction == "increase" else -1.0
        ya = (y["admit_pre"] + y["admit_post"]) / 2.0
        L = ya - y["base"]
        sL = s * L
        row = dict(item_id=it.item_id, task_family=it.task_family,
                   exclusion_reason=it.exclusion_reason, evidence_truth=it.evidence_truth,
                   direction=it.critical_direction, **y, admit=ya, L=L, signed_L=sL)
        if sL <= 0:
            row["usable"] = False
        else:
            row["usable"] = True
            for c in need[1:]:
                row["REI_" + c] = s * (y[c] - y["base"]) / abs(L)
            row["REI_admit"] = 1.0
            row["REI_pre"] = row["REI_exclude_pre"]
            row["REI_post"] = row["REI_exclude_post"]
            row["delta_time"] = row["REI_post"] - row["REI_pre"]
            row["UTB_raw"] = s * ((y["exclude_post"] - y["exclude_pre"])
                                  - (y["admit_post"] - y["admit_pre"]))
            row["UTB_norm"] = row["UTB_raw"] / abs(L)
        # probes
        for pk, name in (("rule_probe_exclude_pre", "p_use_pre"),
                         ("rule_probe_exclude_post", "p_use_post"),
                         ("rule_probe_admit_post", "p_use_admit")):
            row[name] = r[pk]["p_yes"] if pk in r else None
        row["memory"] = r["memory_probe_exclude_post"]["raw"] if "memory_probe_exclude_post" in r else None
        rows.append(row)
    return rows


def summarize(rows, label, out):
    use = [r for r in rows if r["usable"]]
    if not use:
        out.append(f"{label}: no usable items")
        return None
    def col(k, w=True):
        return [wins(r[k]) if w else r[k] for r in use]
    res = {}
    for k, seed in (("REI_pre", 2), ("REI_post", 3), ("delta_time", 4), ("UTB_norm", 5)):
        m, lo, hi = boot_ci(col(k), seed=seed)
        res[k] = (m, lo, hi, boot_p(col(k), seed=seed + 100))
    ra = [r["p_use_pre"] for r in use if r["p_use_pre"] is not None]
    rb = [r["p_use_post"] for r in use if r["p_use_post"] is not None]
    rad = [r["p_use_admit"] for r in use if r["p_use_admit"] is not None]
    res["rule_acc_pre"] = 1 - st.mean(ra) if ra else float("nan")
    res["rule_acc_post"] = 1 - st.mean(rb) if rb else float("nan")
    res["rule_acc_admit"] = st.mean(rad) if rad else float("nan")
    res["n"] = len(use)
    res["n_total"] = len(rows)
    res["median_absL"] = st.median([abs(r["L"]) for r in use])
    res["frac_post_gt_pre"] = st.mean([1.0 if r["delta_time"] > 0 else 0.0 for r in use])
    res["frac_post_gt_0.2"] = st.mean([1.0 if r["REI_post"] > 0.2 else 0.0 for r in use])

    def f(k):
        m, lo, hi, p = res[k]
        return f"{m:+.3f} [{lo:+.3f},{hi:+.3f}] p={p:.4f}"
    out.append(f"{label}   n={res['n']}/{res['n_total']}  median|L|={res['median_absL']:.1f}")
    out.append(f"    RuleAcc  exclude-pre {res['rule_acc_pre']:.3f}  exclude-post {res['rule_acc_post']:.3f}"
               f"  (admit-control p(YES) {res['rule_acc_admit']:.3f})")
    out.append(f"    REI_pre   {f('REI_pre')}")
    out.append(f"    REI_post  {f('REI_post')}")
    out.append(f"    d_time    {f('delta_time')}   items with post>pre: {res['frac_post_gt_pre']:.2f}")
    out.append(f"    UTB_norm  {f('UTB_norm')}")
    out.append(f"    items with REI_post>0.2: {res['frac_post_gt_0.2']:.2f}")
    return res


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", nargs="+", required=True)
    ap.add_argument("--items", default=os.path.join(ROOT, "data", "items", "items_v1.jsonl"))
    ap.add_argument("--tag", required=True)
    ap.add_argument("--out-prefix", required=True)
    args = ap.parse_args()

    items = {i.item_id: i for i in load_items(args.items)}
    runs = defaultdict(dict)
    for p in args.runs:
        for line in open(p):
            r = json.loads(line)
            runs[r["item_id"]][r["kind_name"]] = r
    rows = build_table([items[i] for i in runs if i in items], runs)

    out = [f"# G0 results — {args.tag}", ""]
    out.append("REI: 0 = ignored the excluded evidence, 1 = used it as if admitted.")
    out.append("Winsorised at +/-3; CIs are 10,000-resample item-level paired bootstraps.")
    out.append("")
    out.append("## Pooled")
    pooled = summarize(rows, "ALL", out)
    out.append("")
    out.append("## By task family")
    per_family = {}
    for fam in sorted({r["task_family"] for r in rows}):
        per_family[fam] = summarize([r for r in rows if r["task_family"] == fam], fam, out)
        out.append("")
    out.append("## By exclusion reason")
    per_reason = {}
    for k in sorted({r["exclusion_reason"] for r in rows}):
        sub = [r for r in rows if r["exclusion_reason"] == k]
        if len([r for r in sub if r["usable"]]) >= 8:
            per_reason[k] = summarize(sub, k, out)
            out.append("")
    out.append("## True-but-forbidden vs false-or-unreliable")
    per_truth = {}
    for k in sorted({r["evidence_truth"] for r in rows}):
        per_truth[k] = summarize([r for r in rows if r["evidence_truth"] == k], k, out)
        out.append("")

    txt = "\n".join(out)
    print(txt)
    open(args.out_prefix + ".md", "w").write(txt + "\n")
    json.dump(dict(tag=args.tag, pooled=pooled, per_family=per_family,
                   per_reason=per_reason, per_truth=per_truth, rows=rows),
              open(args.out_prefix + ".json", "w"), indent=1)


if __name__ == "__main__":
    main()
