"""Cross-model master tables.

Picks up whichever raw files exist for each tag: either `<tag>_all.jsonl` or the
older `<tag>_main.jsonl` + `<tag>_extra.jsonl` pair.
"""
import glob, json, os, sys, statistics as st
from collections import defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from schema import load_items
from analyze import build_table, boot_ci, boot_p, wins

ROOT = os.path.join(os.path.dirname(__file__), "..")
RAW = os.path.join(ROOT, "results", "raw")
ORDER = ["phi4-mini", "gemma3-4b", "gemma3-12b", "qwen2.5-7b", "qwen2.5-32b",
         "mistral-small-24b", "qwen3-4b", "qwen3-8b", "qwen3-14b", "qwen3-32b",
         "qwen3.5-9b", "qwen3.5-27b", "qwen3-8b-rep2"]
PRETTY = {"phi4-mini": "Phi-4-mini (3.8B)", "gemma3-4b": "Gemma-3-4B", "gemma3-12b": "Gemma-3-12B",
          "qwen2.5-7b": "Qwen2.5-7B", "qwen2.5-32b": "Qwen2.5-32B",
          "mistral-small-24b": "Mistral-Small-24B", "qwen3-4b": "Qwen3-4B",
          "qwen3-8b": "Qwen3-8B", "qwen3-14b": "Qwen3-14B", "qwen3-32b": "Qwen3-32B",
          "qwen3.5-9b": "Qwen3.5-9B", "qwen3.5-27b": "Qwen3.5-27B",
          "qwen3-8b-rep2": "Qwen3-8B (replicate)"}
EXTRA_CONDS = ["admit_pre", "admit_post", "admit_pre_repeat", "exclude_pre",
               "exclude_pre_repeat", "exclude_post", "exclude_post_reencode",
               "ledger", "sanitation"]


def files_for(tag):
    a = os.path.join(RAW, f"{tag}_all.jsonl")
    if os.path.exists(a):
        return [a]
    out = [p for p in (os.path.join(RAW, f"{tag}_main.jsonl"),
                       os.path.join(RAW, f"{tag}_extra.jsonl")) if os.path.exists(p)]
    return out


def load(tag):
    runs = defaultdict(dict)
    for p in files_for(tag):
        for line in open(p):
            r = json.loads(line)
            runs[r["item_id"]][r["kind_name"]] = r
    return runs


def main():
    items = {i.item_id: i for i in load_items(os.path.join(ROOT, "data", "items", "items_v1.jsonl"))}
    tags = [t for t in ORDER if files_for(t)]
    res, extra, rowsets = {}, {}, {}
    for t in tags:
        runs = load(t)
        rows = build_table([items[i] for i in runs if i in items], runs)
        rowsets[t] = rows
        use = [r for r in rows if r["usable"]]
        d = {}
        for k, seed in (("REI_pre", 2), ("REI_post", 3), ("delta_time", 4), ("UTB_norm", 5)):
            v = [wins(r[k]) for r in use]
            m, lo, hi = boot_ci(v, seed=seed)
            d[k] = (m, lo, hi, boot_p(v, seed=seed + 100))
        d["n"], d["n_total"] = len(use), len(rows)
        pn = [r["p_use_post"] for r in use if r["p_use_post"] is not None]
        pp = [r["p_use_pre"] for r in use if r["p_use_pre"] is not None]
        pa = [r["p_use_admit"] for r in use if r["p_use_admit"] is not None]
        d["rule_post"] = 1 - st.mean(pn) if pn else float("nan")
        d["rule_pre"] = 1 - st.mean(pp) if pp else float("nan")
        d["rule_admit"] = st.mean(pa) if pa else float("nan")
        res[t] = d
        # extra conditions, anchored on the same base/admit
        e = {}
        for iid, r in runs.items():
            it = items.get(iid)
            if it is None or "base" not in r or r["base"]["value"] is None:
                continue
            if any(k not in r or r[k]["value"] is None for k in ("admit_pre", "admit_post")):
                continue
            s = 1.0 if it.critical_direction == "increase" else -1.0
            L = (r["admit_pre"]["value"] + r["admit_post"]["value"]) / 2 - r["base"]["value"]
            if s * L <= 0:
                continue
            for c in EXTRA_CONDS:
                if c in r and r[c]["value"] is not None:
                    e.setdefault(c, []).append(s * (r[c]["value"] - r["base"]["value"]) / abs(L))
        extra[t] = e

    L = []
    L.append("## 1. Main result, every family")
    L.append("")
    L.append("| model | usable n | RuleAcc pre | RuleAcc post | REI Exclude-Pre | REI Exclude-Post | Δ_time | UTB |")
    L.append("|---|---:|---:|---:|---|---|---|---|")
    for t in tags:
        d = res[t]
        def f(k):
            m, lo, hi, _ = d[k]
            return f"{m:+.2f} [{lo:+.2f}, {hi:+.2f}]"
        L.append(f"| {PRETTY.get(t,t)} | {d['n']}/{d['n_total']} | {d['rule_pre']:.3f} | {d['rule_post']:.3f} | "
                 f"{f('REI_pre')} | {f('REI_post')} | {f('delta_time')} | {f('UTB_norm')} |")

    L += ["", "## 2. All conditions (REI means)", "",
          "| model | " + " | ".join(f"`{c}`" for c in EXTRA_CONDS) + " |",
          "|---|" + "---|" * len(EXTRA_CONDS)]
    for t in tags:
        cells = []
        for c in EXTRA_CONDS:
            v = [wins(x) for x in extra[t].get(c, [])]
            cells.append(f"{st.mean(v):+.2f}" if v else "—")
        L.append(f"| {PRETTY.get(t,t)} | " + " | ".join(cells) + " |")

    L += ["", "## 3. Key paired contrasts", "",
          "| model | pre − post (asymmetry) | pre − pre_repeat (rule-recency rescue) | admit_pre − admit_pre_repeat (control) |",
          "|---|---|---|---|"]
    for t in tags:
        e = extra[t]
        out = []
        for a, b in (("exclude_pre", "exclude_post"), ("exclude_pre", "exclude_pre_repeat"),
                     ("admit_pre", "admit_pre_repeat")):
            if a in e and b in e and len(e[a]) == len(e[b]):
                dd = [wins(x) - wins(y) for x, y in zip(e[a], e[b])]
                m, lo, hi = boot_ci(dd, seed=7)
                out.append(f"{m:+.2f} [{lo:+.2f}, {hi:+.2f}] p={boot_p(dd, seed=8):.4f}")
            else:
                out.append("—")
        L.append(f"| {PRETTY.get(t,t)} | " + " | ".join(out) + " |")

    L += ["", "## 4. By task family (REI pre / post)", ""]
    fams = ["legal_judgment", "evidence_inference", "ranking_selection",
            "outcome_evaluation", "numeric_aggregation"]
    L += ["| model | " + " | ".join(fams) + " |", "|---|" + "---|" * len(fams)]
    for t in tags:
        cells = []
        for fam in fams:
            u = [r for r in rowsets[t] if r["usable"] and r["task_family"] == fam]
            cells.append(f"{st.mean([wins(r['REI_pre']) for r in u]):+.2f} / "
                         f"{st.mean([wins(r['REI_post']) for r in u]):+.2f} (n={len(u)})" if u else "—")
        L.append(f"| {PRETTY.get(t,t)} | " + " | ".join(cells) + " |")

    L += ["", "## 5. True-but-forbidden vs false-or-unreliable (REI pre / post)", "",
          "| model | true_but_forbidden | false_or_unreliable |", "|---|---|---|"]
    for t in tags:
        cells = []
        for k in ("true_but_forbidden", "false_or_unreliable"):
            u = [r for r in rowsets[t] if r["usable"] and r["evidence_truth"] == k]
            cells.append(f"{st.mean([wins(r['REI_pre']) for r in u]):+.2f} / "
                         f"{st.mean([wins(r['REI_post']) for r in u]):+.2f} (n={len(u)})" if u else "—")
        L.append(f"| {PRETTY.get(t,t)} | " + " | ".join(cells) + " |")

    txt = "\n".join(L)
    print(txt)
    open(os.path.join(ROOT, "results", "cross_model_tables.md"), "w").write(txt + "\n")
    json.dump({t: res[t] for t in tags}, open(os.path.join(ROOT, "results", "cross_model.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
