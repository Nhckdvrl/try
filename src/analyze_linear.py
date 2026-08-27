"""P0-2: does the zero discontinuity survive on a task where intermediate weights
are actually implementable?

Correct answer is base + w*delta, so the implied effective weight is
    w_hat = (Y - base) / delta
Items are screened on whether the model tracks w at 0.25/0.5/0.75 *in the
retrospective arm*, before the w=0 comparison is looked at.
"""
import json, os, sys, statistics as st
from collections import defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from schema import load_items
from analyze_png import cluster_boot
import linear_blocks as lb

ROOT = os.path.join(os.path.dirname(__file__), "..")
MID = ["lw0250", "lw0500", "lw0750"]


def main(tags):
    items = {i.item_id: i for i in load_items(os.path.join(ROOT, "data", "items", "linear_v1.jsonl"))}
    out = ["# P0-2 Verifiable linear weighting", "",
           "`w_hat = (Y - base) / delta`. Correct behaviour is w_hat = w at every level.",
           "Screened items are those where the model tracks w at 0.25/0.5/0.75 in the",
           "retrospective arm (|error| <= 0.15 at all three), decided before looking at w=0.", ""]
    for tag in tags:
        p = os.path.join(ROOT, "results", "raw", f"{tag}_linear.jsonl")
        if not os.path.exists(p):
            out.append(f"\n# {tag}: not run yet")
            continue
        runs = defaultdict(dict)
        for line in open(p):
            r = json.loads(line)
            runs[r["item_id"]][r["kind_name"]] = r

        def what(iid, cond):
            r = runs[iid].get(cond)
            if r is None or r.get("value") is None:
                return None
            m = items[iid].meta
            return (r["value"] - m["base"]) / m["delta"]

        keep = []
        for iid in runs:
            if iid not in items:
                continue
            ok = True
            for k in MID:
                v = what(iid, f"{k}_post")
                if v is None or abs(v - lb.LINEAR_WEIGHTS[k]) > 0.15:
                    ok = False
                    break
            if ok:
                keep.append(iid)
        out.append(f"\n# {tag}\n")
        out.append(f"Items tracking intermediate weights retrospectively: **{len(keep)}/{len(items)}**\n")
        out.append("| requested w | w_hat, rule BEFORE | w_hat, rule AFTER | pre - post |")
        out.append("|---:|---|---|---|")
        for k, w in lb.LINEAR_WEIGHTS.items():
            a = [what(i, f"{k}_pre") for i in keep]
            b = [what(i, f"{k}_post") for i in keep]
            pairs = [(x, y) for x, y in zip(a, b) if x is not None and y is not None]
            if len(pairs) < 8:
                continue
            d = [x - y for x, y in pairs]
            m, lo, hi, pv = cluster_boot(d, [items[i].surface_domain for i in keep][:len(d)],
                                         n=4000, seed=1)
            star = "**" if w == 0 else ""
            out.append(f"| {w:g} | {st.mean(x for x, _ in pairs):+.3f} | "
                       f"{st.mean(y for _, y in pairs):+.3f} | "
                       f"{star}{m:+.3f}{star} [{lo:+.3f}, {hi:+.3f}] p={pv:.4f} |")
    txt = "\n".join(out)
    print(txt)
    open(os.path.join(ROOT, "results", "linear_tables.md"), "w").write(txt + "\n")


if __name__ == "__main__":
    main(sys.argv[1:] or ["qwen3-8b", "gemma3-12b", "phi4-mini",
                          "mistral-small-24b", "qwen3.5-27b"])
