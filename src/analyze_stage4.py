"""Ruling paraphrases: is the position effect a property of one sentence?

Each paraphrase has a matched admit form, so |L| is measured in the same register
as the exclusion it anchors.
"""
import json, os, sys, statistics as st
from collections import defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from schema import load_items
from analyze import wins
from analyze_stage2 import cluster_of
from analyze_png import cluster_boot
import conditions_v4 as v4

ROOT = os.path.join(os.path.dirname(__file__), "..")


def main(tags):
    items = {i.item_id: i for i in load_items(os.path.join(ROOT, "data", "items", "items_v1.jsonl"))}
    out = ["# Ruling paraphrases", "",
           "Pre-minus-post gap in effective evidence weight, per wording. Each row is a",
           "different construction type; the exclusion is anchored on its own matched admit",
           "form. Cluster bootstrap over case skeletons, per model.", ""]
    per_pp = defaultdict(list)
    for tag in tags:
        p = os.path.join(ROOT, "results", "raw", f"{tag}_stage4.jsonl")
        if not os.path.exists(p):
            continue
        runs = defaultdict(dict)
        for line in open(p):
            r = json.loads(line)
            runs[r["item_id"]][r["kind_name"]] = r
        out.append(f"\n## {tag}\n")
        out.append("| wording | type | REI pre | REI post | gap [95% CI] | p |")
        out.append("|---|---|---|---|---|---|")
        for key, spec in v4.PARAPHRASES.items():
            gaps, pres, posts, cls = [], [], [], []
            for iid, r in runs.items():
                it = items.get(iid)
                need = [f"{key}a_pre", f"{key}a_post", f"{key}x_pre", f"{key}x_post", "base"]
                if it is None or any(k not in r or r[k].get("value") is None for k in need):
                    continue
                s = 1.0 if it.critical_direction == "increase" else -1.0
                y0 = r["base"]["value"]
                L = (r[f"{key}a_pre"]["value"] + r[f"{key}a_post"]["value"]) / 2 - y0
                if s * L <= 0:
                    continue
                a = wins(s * (r[f"{key}x_pre"]["value"] - y0) / abs(L))
                b = wins(s * (r[f"{key}x_post"]["value"] - y0) / abs(L))
                pres.append(a); posts.append(b); gaps.append(a - b)
                cls.append(cluster_of(it))
            if len(gaps) < 20:
                continue
            m, lo, hi, pv = cluster_boot(gaps, cls, n=4000, seed=2)
            per_pp[key].append(m)
            out.append(f"| `{spec['exc'][:44]}...` | {spec['kind']} | {st.mean(pres):+.3f} | "
                       f"{st.mean(posts):+.3f} | **{m:+.3f}** [{lo:+.3f}, {hi:+.3f}] | {pv:.4f} |")
    if per_pp:
        out += ["", "## Across models", "", "| wording type | mean gap | models positive |",
                "|---|---|---|"]
        for key, vals in per_pp.items():
            out.append(f"| {v4.PARAPHRASES[key]['kind']} | {st.mean(vals):+.3f} | "
                       f"{sum(1 for v in vals if v > 0)}/{len(vals)} |")
    txt = "\n".join(out)
    print(txt)
    open(os.path.join(ROOT, "results", "paraphrase_tables.md"), "w").write(txt + "\n")


if __name__ == "__main__":
    main(sys.argv[1:] or ["qwen3-8b", "gemma3-12b", "phi4-mini", "mistral-small-24b", "qwen3-32b"])
