"""Item-level bootstrap assumes items are independent. They are not: the 60 legal
items are 10 case skeletons crossed with 6 evidence types, and several controlled
families reuse a latent problem across exclusion reasons. This re-runs the CIs
resampling CLUSTERS (case skeleton / latent problem) instead of items."""
import json, os, random, sys, statistics as st
from collections import defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from schema import load_items
from analyze import build_table, boot_ci, wins

ROOT = os.path.join(os.path.dirname(__file__), "..")
ITEMS = {i.item_id: i for i in load_items(os.path.join(ROOT, "data", "items", "items_v1.jsonl"))}


def cluster_of(it):
    if it.task_family == "legal_judgment":
        return "legal:" + it.meta["case"]
    return it.task_family + ":" + it.base_context[:60]


def clustered_ci(by_cluster, n=10000, seed=0):
    rng = random.Random(seed)
    ks = list(by_cluster)
    reps = []
    for _ in range(n):
        pool = []
        for _ in range(len(ks)):
            pool += by_cluster[ks[rng.randrange(len(ks))]]
        reps.append(st.mean(pool))
    reps.sort()
    return reps[int(.025 * n)], reps[int(.975 * n)]


def main(tags):
    out = ["# Cluster-robust CIs", "",
           "Resampling case skeletons / latent problems rather than items.", "",
           "| model | clusters | metric | mean | item bootstrap | cluster bootstrap |",
           "|---|---:|---|---|---|---|"]
    for tag in tags:
        paths = [p for p in (os.path.join(ROOT, "results", "raw", f"{tag}_all.jsonl"),
                             os.path.join(ROOT, "results", "raw", f"{tag}_main.jsonl"),
                             os.path.join(ROOT, "results", "raw", f"{tag}_extra.jsonl"))
                 if os.path.exists(p)]
        if not paths:
            continue
        runs = defaultdict(dict)
        for p in paths:
            for line in open(p):
                r = json.loads(line)
                runs[r["item_id"]][r["kind_name"]] = r
        rows = [r for r in build_table([ITEMS[i] for i in runs if i in ITEMS], runs) if r["usable"]]
        nc = len({cluster_of(ITEMS[r["item_id"]]) for r in rows})
        for m in ("REI_pre", "REI_post", "delta_time", "UTB_norm"):
            flat = [wins(r[m]) for r in rows]
            mean, lo, hi = boot_ci(flat, seed=1)
            by = defaultdict(list)
            for r in rows:
                by[cluster_of(ITEMS[r["item_id"]])].append(wins(r[m]))
            clo, chi = clustered_ci(by, seed=1)
            out.append(f"| {tag} | {nc} | {m} | {mean:+.3f} | [{lo:+.3f}, {hi:+.3f}] | "
                       f"[{clo:+.3f}, {chi:+.3f}] |")
    txt = "\n".join(out)
    print(txt)
    open(os.path.join(ROOT, "results", "cluster_robustness.md"), "w").write(txt + "\n")


if __name__ == "__main__":
    main(sys.argv[1:] or ["qwen3-8b", "gemma3-12b", "phi4-mini", "qwen2.5-32b", "qwen3-32b"])
