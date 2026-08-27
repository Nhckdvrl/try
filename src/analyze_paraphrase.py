"""Does the position effect belong to one sentence?

Eight hand-written ruling wordings, each with a matched admit form so the
leverage anchor is in the same register as the exclusion it is paired with.
"""
import json, os, sys, statistics as st
from collections import defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from schema import load_items
from analyze import boot_ci, boot_p, wins
import conditions_v4 as v4

ROOT = os.path.join(os.path.dirname(__file__), "..")


def main(tags):
    items = {i.item_id: i for i in load_items(os.path.join(ROOT, "data", "items", "items_v1.jsonl"))}
    out = ["# Ruling paraphrases", "",
           "Each wording has its own admit anchor: "
           "`L = mean(ppNa_pre, ppNa_post) - base` for that same wording.", ""]
    allgaps = defaultdict(list)
    for tag in tags:
        p = os.path.join(ROOT, "results", "raw", f"{tag}_stage4.jsonl")
        if not os.path.exists(p):
            continue
        runs = defaultdict(dict)
        for line in open(p):
            r = json.loads(line)
            runs[r["item_id"]][r["kind_name"]] = r
        out.append(f"\n## {tag}\n")
        out.append("| wording | construction | REI pre | REI post | pre - post |")
        out.append("|---|---|---|---|---|")
        for key, spec in v4.PARAPHRASES.items():
            va, vb = [], []
            for iid, r in runs.items():
                it = items.get(iid)
                if it is None or "base" not in r or r["base"].get("value") is None:
                    continue
                need = [f"{key}a_pre", f"{key}a_post", f"{key}x_pre", f"{key}x_post"]
                if any(k not in r or r[k].get("value") is None for k in need):
                    continue
                s = 1.0 if it.critical_direction == "increase" else -1.0
                y0 = r["base"]["value"]
                L = (r[f"{key}a_pre"]["value"] + r[f"{key}a_post"]["value"]) / 2 - y0
                if s * L <= 0:
                    continue
                va.append(wins(s * (r[f"{key}x_pre"]["value"] - y0) / abs(L)))
                vb.append(wins(s * (r[f"{key}x_post"]["value"] - y0) / abs(L)))
            if len(va) < 20:
                out.append(f"| `{key}` | {spec['kind']} | — | — | n={len(va)} too few |")
                continue
            d = [x - y for x, y in zip(va, vb)]
            m, lo, hi = boot_ci(d, n=4000, seed=1)
            allgaps[key].append(m)
            out.append(f"| `{key}` | {spec['kind']} | {st.mean(va):+.3f} | {st.mean(vb):+.3f} | "
                       f"**{m:+.3f}** [{lo:+.3f}, {hi:+.3f}] p={boot_p(d, n=4000, seed=2):.4f} "
                       f"(n={len(va)}) |")
    out.append("\n## Mean pre - post gap per wording, across models\n")
    out.append("| wording | construction | mean gap | models with gap > 0 |")
    out.append("|---|---|---|---|")
    for key, spec in v4.PARAPHRASES.items():
        g = allgaps.get(key, [])
        if not g:
            continue
        out.append(f"| `{key}` | {spec['kind']} | {st.mean(g):+.3f} | "
                   f"{sum(1 for x in g if x > 0)}/{len(g)} |")
    txt = "\n".join(out)
    print(txt)
    open(os.path.join(ROOT, "results", "paraphrase_tables.md"), "w").write(txt + "\n")


if __name__ == "__main__":
    main(sys.argv[1:] or ["qwen3-8b", "gemma3-12b", "mistral-small-24b", "qwen3-32b", "phi4-mini"])
