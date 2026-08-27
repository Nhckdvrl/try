"""The prospective nullification gap, reported per model.

    N_pre  = REI_pre(0.01)  - REI_pre(0)
    N_post = REI_post(0.01) - REI_post(0)
    PNG    = N_post - N_pre

N is the extra suppression bought by turning "1%" into "exactly 0%" -- the
smallest possible lexical intervention, one digit. PNG asks whether that
operation is equally available before and after the target exists.

Note PNG is algebraically identical to gap(0) - gap(0.01), so it serves both the
"is zero singular" and the "is nullification position-dependent" framings.

Inference is per model with a cluster bootstrap over case skeletons. Models are
NOT pooled as independent observations -- they are not a random sample and the
Qwen family members are strongly related -- so the cross-model line reports the
sign and range only.
"""
import json, os, random, sys, statistics as st
from collections import defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from schema import load_items
from analyze import wins
from analyze_stage2 import cluster_of
from analyze_stage3 import load, anchor, rei

ROOT = os.path.join(os.path.dirname(__file__), "..")


def cluster_boot(vals, clusters, n=10000, seed=0):
    by = defaultdict(list)
    for v, c in zip(vals, clusters):
        by[c].append(v)
    ks = list(by)
    rng = random.Random(seed)
    reps = []
    for _ in range(n):
        pool = []
        for _ in range(len(ks)):
            pool += by[ks[rng.randrange(len(ks))]]
        reps.append(st.mean(pool))
    reps.sort()
    m = st.mean(vals)
    p = 2 * min(sum(1 for r in reps if r <= 0), sum(1 for r in reps if r >= 0)) / n
    return m, reps[int(.025 * n)], reps[int(.975 * n)], min(p, 1.0)


def main(tags):
    items = {i.item_id: i for i in load_items(os.path.join(ROOT, "data", "items", "items_v1.jsonl"))}
    out = ["# Prospective nullification gap (PNG)", "",
           "`N = REI(w=0.01) - REI(w=0)` is the extra suppression bought by the smallest",
           "possible lexical change, one digit. `PNG = N_post - N_pre`.", "",
           "| model | n | N_pre | N_post | **PNG** [95% CI] | p |",
           "|---|---:|---|---|---|---|"]
    summary = []
    for tag in tags:
        try:
            runs = load(tag)
        except FileNotFoundError:
            continue
        A = anchor(runs, items, "base", ["nz1000_pre", "nz1000_post"])
        png, npre, npost, cls = [], [], [], []
        for iid in A:
            v = {}
            ok = True
            for k in ("nz0000_pre", "nz0000_post", "nz0010_pre", "nz0010_post"):
                x = rei(runs, A, iid, k)
                if x is None:
                    ok = False
                    break
                v[k] = wins(x)
            if not ok:
                continue
            a = v["nz0010_pre"] - v["nz0000_pre"]
            b = v["nz0010_post"] - v["nz0000_post"]
            npre.append(a)
            npost.append(b)
            png.append(b - a)
            cls.append(cluster_of(items[iid]))
        if not png:
            continue
        m, lo, hi, p = cluster_boot(png, cls, seed=1)
        out.append(f"| {tag} | {len(png)} | {st.mean(npre):+.3f} | {st.mean(npost):+.3f} | "
                   f"**{m:+.3f}** [{lo:+.3f}, {hi:+.3f}] | {p:.4f} |")
        summary.append((tag, m, p))
    if summary:
        ms = [m for _, m, _ in summary]
        sig = sum(1 for _, _, p in summary if p < 0.05)
        out += ["", f"Across {len(summary)} models PNG is positive in "
                    f"{sum(1 for m in ms if m > 0)}/{len(ms)}, range "
                    f"{min(ms):+.3f} to {max(ms):+.3f}, individually significant in {sig}.",
                "", "Read N_pre directly: it is the suppression gained by writing "
                "'exactly 0%' instead of '1%' when the target does not exist yet."]
    txt = "\n".join(out)
    print(txt)
    open(os.path.join(ROOT, "results", "png_tables.md"), "w").write(txt + "\n")


if __name__ == "__main__":
    main(sys.argv[1:] or ["qwen3-8b", "gemma3-12b", "phi4-mini",
                          "mistral-small-24b", "qwen3.5-27b"])
