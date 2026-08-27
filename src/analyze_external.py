"""External held-out validation.

Neither corpus was written by us and neither took part in dataset construction,
screening, or hypothesis discovery.
"""
import json, os, sys, statistics as st
from collections import defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from schema import load_items
from analyze import wins
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
    out = ["# External held-out validation", "",
           "**A. Ramsey, Liu & Trueblood (2024)** medication-report paradigm, OSF 9ybnx.",
           "Instruction wording verbatim from their experiment code. Their design flags the",
           "fabricated report *in place*, which is the retrospective arm; announcing which",
           "report will be fabricated before the stream is our addition. 48 items, exact",
           "ground truth (the mean of the truthful reports).", "",
           "| model | n | base error | admit (unflagged) | flag in place (their design) | flag announced first |",
           "|---|---:|---|---|---|---|"]
    items_r = {i.item_id: i for i in load_items(os.path.join(ROOT, "data", "items", "external_ramsey.jsonl"))}
    for tag in tags:
        runs = load(tag, "extramsey")
        if not runs:
            continue
        cells = {}
        n = 0
        for cond in ("ext_base", "ext_admit", "ext_post", "ext_pre"):
            errs = []
            for iid, r in runs.items():
                it = items_r.get(iid)
                v = r.get(cond, {}).get("value")
                if it is None or v is None:
                    continue
                errs.append(v - it.ground_truth)      # signed, toward the fabricated value
            if errs:
                cells[cond] = errs
                n = max(n, len(errs))
        if not cells:
            continue

        def fmt(c):
            e = cells.get(c)
            if not e:
                return "—"
            sgn = [x if items_r[i].critical_direction == "increase" else -x
                   for i, x in zip(list(runs)[:len(e)], e)]
            return f"{st.mean(sgn):+.1f}"
        out.append(f"| {tag} | {n} | {fmt('ext_base')} | {fmt('ext_admit')} | "
                   f"**{fmt('ext_post')}** | **{fmt('ext_pre')}** |")
    out.append("")
    out.append("Values are the signed pull toward the fabricated report, in patients per 100, "
               "against the true mean of the truthful reports. 0 is perfect exclusion.")

    out += ["", "**B. Aiyer et al. (2023) replication of Baron & Hershey (1988)**, OSF knjhu.",
            "The bypass-surgery vignette verbatim from their Qualtrics file, all four framings",
            "actually administered. 4 items, so this is an anchor rather than a test.", "",
            "| model | REI exclude-pre | REI exclude-post |", "|---|---|---|"]
    items_b = {i.item_id: i for i in load_items(os.path.join(ROOT, "data", "items", "external_bh.jsonl"))}
    for tag in tags:
        runs = load(tag, "extbh")
        if not runs:
            continue
        pre, post = [], []
        for iid, r in runs.items():
            it = items_b.get(iid)
            if it is None:
                continue
            g = lambda c: r.get(c, {}).get("value")
            b, ap, ao = g("base"), g("admit_pre"), g("admit_post")
            xp, xo = g("exclude_pre"), g("exclude_post")
            if None in (b, ap, ao, xp, xo):
                continue
            s = 1.0 if it.critical_direction == "increase" else -1.0
            L = (ap + ao) / 2 - b
            if s * L <= 0:
                continue
            pre.append(wins(s * (xp - b) / abs(L)))
            post.append(wins(s * (xo - b) / abs(L)))
        if pre:
            out.append(f"| {tag} | {st.mean(pre):+.3f} (n={len(pre)}) | {st.mean(post):+.3f} |")
    txt = "\n".join(out)
    print(txt)
    open(os.path.join(ROOT, "results", "external_tables.md"), "w").write(txt + "\n")


if __name__ == "__main__":
    main(sys.argv[1:] or ["qwen3-8b", "gemma3-12b", "phi4-mini", "mistral-small-24b"])
