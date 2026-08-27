"""On-policy state externalisation.

Teacher-forcing a reasoning step can push a model off-policy, so the forced-zero
result should not stand alone. Here the model is sampled (16 per item, T=0.8) and
we condition on the trajectories in which it states zero weight of its own accord.
"""
import json, os, sys, statistics as st
from collections import defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from schema import load_items
from analyze import wins
from analyze_stage2 import cluster_of
from analyze_png import cluster_boot

ROOT = os.path.join(os.path.dirname(__file__), "..")


def main(tags):
    items = {i.item_id: i for i in load_items(os.path.join(ROOT, "data", "items", "items_v1.jsonl"))}
    out = ["# On-policy state externalisation", "",
           "16 samples per item at T=0.8. Trajectories are split by what the model wrote on",
           "its own `ITEM DECISION WEIGHT` line; the decision is then read at a fixed position.", "",
           "| model | arm | trajectories stating 0% | REI when it stated 0% | REI when it stated >0% |",
           "|---|---|---:|---|---|"]
    for tag in tags:
        p = os.path.join(ROOT, "results", "raw", f"{tag}_onpolicy.jsonl")
        if not os.path.exists(p):
            continue
        runs = defaultdict(dict)
        for line in open(p):
            r = json.loads(line)
            runs[r["item_id"]][r["kind_name"]] = r
        for arm in ("pre", "post"):
            z, nz, zc, nzc, frac = [], [], [], [], []
            for iid, r in runs.items():
                it = items.get(iid)
                if it is None or "base" not in r or "inc_none_full" not in r:
                    continue
                if r["base"].get("value") is None or r["inc_none_full"].get("value") is None:
                    continue
                s = 1.0 if it.critical_direction == "increase" else -1.0
                y0 = r["base"]["value"]
                L = r["inc_none_full"]["value"] - y0
                if s * L <= 0 or f"op_{arm}" not in r:
                    continue
                samples = r[f"op_{arm}"].get("samples") or []
                good = [c for c in samples if c.get("value") is not None
                        and c.get("stated_weight") is not None]
                if not good:
                    continue
                zs = [c for c in good if abs(c["stated_weight"]) < 1e-9]
                ns = [c for c in good if abs(c["stated_weight"]) >= 1e-9]
                frac.append(len(zs) / len(good))
                if zs:
                    z.append(wins(st.mean(s * (c["value"] - y0) / abs(L) for c in zs)))
                    zc.append(cluster_of(it))
                if ns:
                    nz.append(wins(st.mean(s * (c["value"] - y0) / abs(L) for c in ns)))
                    nzc.append(cluster_of(it))
            if not z:
                continue
            m, lo, hi, _ = cluster_boot(z, zc, n=4000, seed=1)
            n2 = f"{st.mean(nz):+.3f}" if nz else "—"
            out.append(f"| {tag} | rule {arm.upper()} | {100*st.mean(frac):.0f}% | "
                       f"**{m:+.3f}** [{lo:+.3f}, {hi:+.3f}] (n={len(z)}) | {n2} |")
    txt = "\n".join(out)
    print(txt)
    open(os.path.join(ROOT, "results", "onpolicy_tables.md"), "w").write(txt + "\n")


if __name__ == "__main__":
    main(sys.argv[1:] or ["qwen3-8b", "gemma3-12b", "phi4-mini", "mistral-small-24b"])
