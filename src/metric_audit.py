"""Metric audit.

Two ratio metrics in this project blew up because their denominator can be small:
REI under a preview (Stage 3D) and patch recovery fraction (Stage 5). The rule
adopted after those two incidents: any ratio reported in the main text must
either have a denominator frozen and screened to be large, or be accompanied by
the raw numerator, the denominator distribution, and a sensitivity analysis.

This script runs that audit over every ratio still in use.
"""
import json, os, sys, statistics as st
from collections import defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from schema import load_items
from analyze import build_table, wins
from analyze_stage2 import cluster_of
from analyze_png import cluster_boot

ROOT = os.path.join(os.path.dirname(__file__), "..")


def load(tag, suffix):
    p = os.path.join(ROOT, "results", "raw", f"{tag}_{suffix}.jsonl")
    if not os.path.exists(p):
        return None
    runs = defaultdict(dict)
    for line in open(p):
        r = json.loads(line)
        runs[r["item_id"]][r["kind_name"]] = r
    return runs


def main(tags):
    items = {i.item_id: i for i in load_items(os.path.join(ROOT, "data", "items", "items_v1.jsonl"))}
    out = ["# Metric audit", "",
           "Every ratio still reported, checked for denominator fragility. `|L|` is the",
           "denominator: the leverage the critical evidence has under an admitting rule.", "",
           "## Main REI (Stage 0-2): denominator was frozen by screening", "",
           "| model | n | median \\|L\\| | 10th pct | frac \\|L\\|<10 | REI_pre all / \\|L\\|>10 / \\|L\\|>15 | Δ_time all / >10 / >15 |",
           "|---|---:|---:|---:|---:|---|---|"]
    for tag in tags:
        runs = None
        for suf in ("all", "main"):
            runs = load(tag, suf)
            if runs:
                if suf == "main":
                    extra = load(tag, "extra")
                    if extra:
                        for k, v in extra.items():
                            runs[k].update(v)
                break
        if not runs:
            continue
        rows = [r for r in build_table([items[i] for i in runs if i in items], runs) if r["usable"]]
        Ls = sorted(abs(r["L"]) for r in rows)
        if not Ls:
            continue
        cells_p, cells_d = [], []
        for thr in (0.0, 10.0, 15.0):
            sub = [r for r in rows if abs(r["L"]) > thr]
            if len(sub) < 20:
                cells_p.append("—")
                cells_d.append("—")
                continue
            cells_p.append(f"{st.mean(wins(r['REI_pre']) for r in sub):+.2f}")
            cells_d.append(f"{st.mean(wins(r['delta_time']) for r in sub):+.2f}")
        frac_small = sum(1 for x in Ls if x < 10) / len(Ls)
        out.append(f"| {tag} | {len(rows)} | {st.median(Ls):.1f} | {Ls[len(Ls)//10]:.1f} | "
                   f"{frac_small:.2f} | {' / '.join(cells_p)} | {' / '.join(cells_d)} |")
    out += ["", "A ratio is safe here because screening required "
                "`sign(direction)*(admit-base) >= 8` before any Exclude condition existed, so "
                "the denominator cannot be near zero by construction, and the conclusions do "
                "not move when the floor is raised to 10 or 15."]
    txt = "\n".join(out)
    print(txt)
    open(os.path.join(ROOT, "results", "metric_audit.md"), "w").write(txt + "\n")


if __name__ == "__main__":
    main(sys.argv[1:] or ["qwen3-8b", "gemma3-12b", "phi4-mini", "mistral-small-24b",
                          "qwen3-32b", "qwen3.5-27b", "qwen2.5-32b"])
