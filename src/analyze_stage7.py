"""Stage 3E: duplicate control and the proposition relation matrix."""
import json, os, sys, statistics as st
from collections import defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from schema import load_items
from analyze import wins
from analyze_stage2 import cluster_of
from analyze_png import cluster_boot
import conditions_v7 as v7

ROOT = os.path.join(os.path.dirname(__file__), "..")
REL_LABEL = {"bidir": "mutual entailment (true paraphrase)",
             "morespecific": "preview entails actual (more specific)",
             "abstract": "actual entails preview (gist only)",
             "argswap": "one argument changed",
             "polarity": "polarity reversed",
             "lexhigh": "high lexical overlap, different meaning",
             "unrelated": "unrelated"}


def load(tag):
    runs = defaultdict(dict)
    for line in open(os.path.join(ROOT, "results", "raw", f"{tag}_stage7.jsonl")):
        r = json.loads(line)
        runs[r["item_id"]][r["kind_name"]] = r
    return runs


def val(runs, iid, cond):
    r = runs[iid].get(cond)
    return None if r is None or r.get("value") is None else r["value"]


def run(tag, items, out):
    runs = load(tag)
    out.append(f"\n# {tag}\n")

    # ---- P0-A duplicate control ----
    out.append("## P0-A Duplicate control\n")
    out.append("`marginal leverage` is the shift the *later* evidence produces given that the "
               "preview is already present: `Y(preview + E) - Y(preview alone)`, sign-aligned. "
               "If a preview simply made the second presentation redundant, this would collapse "
               "under no rule too.\n")
    out.append("| preview | marginal leverage, no rule | marginal leverage, admit rule | REI under exclude |")
    out.append("|---|---|---|---|")
    for key in ["none"] + v7.DUP_PREVIEWS:
        marg_n, marg_a, reis, cls = [], [], [], []
        for iid, r in runs.items():
            it = items.get(iid)
            if it is None:
                continue
            s = 1.0 if it.critical_direction == "increase" else -1.0
            only = val(runs, iid, f"dup_{key}_only") if key != "none" else val(runs, iid, "base")
            nor = val(runs, iid, f"dup_{key}_norule")
            adm = val(runs, iid, f"dup_{key}_admit")
            exc = val(runs, iid, f"dup_{key}_exclude")
            b = val(runs, iid, "base")
            if None in (only, nor, adm, exc, b):
                continue
            L = s * (adm - only)
            if L <= 0:
                continue
            marg_n.append(s * (nor - only))
            marg_a.append(L)
            reis.append(wins(s * (exc - only) / abs(L)))
            cls.append(cluster_of(it))
        if len(reis) < 15:
            continue
        m, lo, hi, p = cluster_boot(reis, cls, n=4000, seed=1)
        out.append(f"| `{key}` (n={len(reis)}) | {st.mean(marg_n):+.2f} pts | "
                   f"{st.mean(marg_a):+.2f} pts | **{m:+.3f}** [{lo:+.3f}, {hi:+.3f}] |")
    out.append("\nMarginal leverage is in raw rating points, measured against the "
               "preview-only baseline for that same preview, so a preview that merely made the "
               "later evidence redundant would show a reduced value in the *no rule* column.")

    # ---- P0-B relation matrix, de-confounded ----
    out.append("\n## P0-B Proposition relation matrix\n")
    out.append("`ExclusionEffect` is the rating points the RULE removes on top of whatever the "
               "preview already did: `marg(no rule) - marg(exclude)`, both measured against that "
               "preview's own baseline. The redundancy a preview creates on its own is in the "
               "`marg(no rule)` column, so the two are separated.\n")
    out.append("| relation between preview and actual evidence | marg, no rule | **ExclusionEffect** | p |")
    out.append("|---|---|---|---|")
    for rel in ["none"] + v7.REL_RUNGS:
        margs, eff, cls = [], [], []
        for iid, r in runs.items():
            it = items.get(iid)
            if it is None:
                continue
            s_ = 1.0 if it.critical_direction == "increase" else -1.0
            if rel == "none":
                only, nor, exc = (val(runs, iid, "base"), val(runs, iid, "dup_none_norule"),
                                  val(runs, iid, "rel_none"))
            else:
                only = val(runs, iid, f"relonly_{rel}")
                nor = val(runs, iid, f"relnorule_{rel}")
                exc = val(runs, iid, f"rel_{rel}")
            if None in (only, nor, exc):
                continue
            margs.append(s_ * (nor - only))
            eff.append(s_ * (nor - only) - s_ * (exc - only))
            cls.append(cluster_of(it))
        if len(eff) < 15:
            continue
        m, lo, hi, p = cluster_boot(eff, cls, n=4000, seed=3)
        lab = "no preview" if rel == "none" else REL_LABEL[rel]
        out.append(f"| {lab} (n={len(eff)}) | {st.mean(margs):+.1f} pts | "
                   f"**{m:+.1f}** [{lo:+.1f}, {hi:+.1f}] | {p:.4f} |")
    out.append("")
    out.append("### legacy ratio view (unstable when the preview shrinks |L|)")
    out.append("| relation | REI | rescue vs no preview | p |")
    out.append("|---|---|---|---|")
    anchor = {}
    for iid, r in runs.items():
        it = items.get(iid)
        if it is None:
            continue
        s = 1.0 if it.critical_direction == "increase" else -1.0
        b = val(runs, iid, "base")
        adm = val(runs, iid, "dup_none_admit")
        if b is None or adm is None or s * (adm - b) <= 0:
            continue
        anchor[iid] = (b, abs(adm - b), s)
    def rei(iid, cond):
        v = val(runs, iid, cond)
        if v is None or iid not in anchor:
            return None
        b, L, s = anchor[iid]
        return wins(s * (v - b) / L)
    base_r = {i: rei(i, "rel_none") for i in anchor}
    v0 = [x for x in base_r.values() if x is not None]
    out.append(f"| no preview | {st.mean(v0):+.3f} | — | — |")
    for rel in v7.REL_RUNGS:
        vals, resc, cls = [], [], []
        for iid in anchor:
            v = rei(iid, f"rel_{rel}")
            if v is None or base_r[iid] is None:
                continue
            vals.append(v)
            resc.append(base_r[iid] - v)
            cls.append(cluster_of(items[iid]))
        if len(vals) < 15:
            continue
        m, lo, hi, p = cluster_boot(resc, cls, n=4000, seed=2)
        out.append(f"| {REL_LABEL[rel]} | {st.mean(vals):+.3f} | **{m:+.3f}** "
                   f"[{lo:+.3f}, {hi:+.3f}] | {p:.4f} |")


def main(tags):
    items = {i.item_id: i for i in load_items(os.path.join(ROOT, "data", "items", "items_v1.jsonl"))}
    out = ["# Stage 3E — duplicate control and the proposition relation matrix", ""]
    for t in tags:
        try:
            run(t, items, out)
        except FileNotFoundError:
            out.append(f"\n# {t}: not run yet")
    txt = "\n".join(out)
    print(txt)
    open(os.path.join(ROOT, "results", "stage7_tables.md"), "w").write(txt + "\n")


if __name__ == "__main__":
    main(sys.argv[1:] or ["qwen3-8b", "gemma3-12b", "phi4-mini", "qwen3.5-27b"])
