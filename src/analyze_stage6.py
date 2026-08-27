"""P0.5 semantic addressability: what must exist at rule time?

Preview(E') -> rule(E7 = 0) -> actual E -> judgment, with the actual evidence held
fixed and only the preview varied. Rescue(E') = REI(no preview) - REI(E' preview).
"""
import json, os, sys, statistics as st
from collections import defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from schema import load_items
from analyze import wins
from analyze_stage2 import cluster_of
from analyze_png import cluster_boot
import conditions_v6 as v6

ROOT = os.path.join(os.path.dirname(__file__), "..")
RUNG_LABEL = {
    "none": "no preview (the failure)",
    "exact": "exact same text",
    "para": "lexical paraphrase, same proposition",
    "summ": "entailing summary, no verbatim content",
    "samedir": "different fact, same entity and same direction",
    "lexoverlap": "high lexical overlap, different meaning",
    "topic": "same case, unrelated procedural fact",
    "unrelated": "unrelated fact",
}
ORDER = ["none", "exact", "para", "summ", "samedir", "lexoverlap", "topic", "unrelated"]


def load(tag):
    runs = defaultdict(dict)
    for line in open(os.path.join(ROOT, "results", "raw", f"{tag}_stage6.jsonl")):
        r = json.loads(line)
        runs[r["item_id"]][r["kind_name"]] = r
    return runs


def anch(runs, items, base_key, full_keys):
    out = {}
    for iid, r in runs.items():
        it = items.get(iid)
        if it is None or base_key not in r:
            continue
        if r[base_key].get("value") is None:
            continue
        if any(k not in r or r[k].get("value") is None for k in full_keys):
            continue
        s = 1.0 if it.critical_direction == "increase" else -1.0
        y0 = r[base_key]["value"]
        L = st.mean(r[k]["value"] for k in full_keys) - y0
        if s * L <= 0:
            continue
        out[iid] = (y0, abs(L), s)
    return out


def rei(runs, a, iid, cond):
    r = runs[iid].get(cond)
    if r is None or r.get("value") is None:
        return None
    y0, absL, s = a[iid]
    return wins(s * (r["value"] - y0) / absL)


def run(tag, items, out):
    runs = load(tag)
    a = anch(runs, items, "sem_base", ["sem_full_pre", "sem_full_post"])
    out.append(f"\n# {tag}   (n usable = {len(a)})\n")
    out.append("| preview placed before the rule | REI | rescue vs no preview | p |")
    out.append("|---|---|---|---|")
    base_vals = {i: rei(runs, a, i, "sem_none") for i in a}
    for rung in ORDER:
        vals, resc, cls = [], [], []
        for iid in a:
            v = rei(runs, a, iid, f"sem_{rung}")
            if v is None or base_vals[iid] is None:
                continue
            vals.append(v)
            resc.append(base_vals[iid] - v)
            cls.append(cluster_of(items[iid]))
        if not vals:
            continue
        if rung == "none":
            out.append(f"| {RUNG_LABEL[rung]} | {st.mean(vals):+.3f} | — | — |")
            continue
        m, lo, hi, p = cluster_boot(resc, cls, n=4000, seed=1)
        out.append(f"| {RUNG_LABEL[rung]} | {st.mean(vals):+.3f} | **{m:+.3f}** "
                   f"[{lo:+.3f}, {hi:+.3f}] | {p:.4f} |")

    # ---- content x identity 2x2 ----
    out.append("\n## Content x identity (legal items only)\n")
    out.append("Preview is always the original evidence. The rule always names E7. The item the "
               "decision reads varies in content and in label.\n")
    out.append("| preview content matches? | label matches the rule? | REI |")
    out.append("|---|---|---|")
    for content in ("same", "diff"):
        for ident in ("e7", "e9"):
            b = anch(runs, items, "swap_base", [f"swap_{content}_{ident}_f"])
            keep = [i for i in b if v6.swap_usable(items[i])]
            vals = [rei(runs, b, i, f"swap_{content}_{ident}_z") for i in keep]
            vals = [v for v in vals if v is not None]
            if len(vals) < 10:
                continue
            cls = [cluster_of(items[i]) for i in keep][:len(vals)]
            m, lo, hi, _ = cluster_boot(vals, cls, n=4000, seed=2)
            out.append(f"| {'yes' if content == 'same' else 'no'} | "
                       f"{'yes (E7)' if ident == 'e7' else 'no (E9)'} | "
                       f"{m:+.3f} [{lo:+.3f}, {hi:+.3f}]  (n={len(vals)}) |")


def main(tags):
    items = {i.item_id: i for i in load_items(os.path.join(ROOT, "data", "items", "items_v1.jsonl"))}
    out = ["# P0.5 Semantic addressability", "",
           "Structure: `preview(E') -> rule: E7 has weight 0 -> EVIDENCE E7 (fixed) -> judgment`.",
           "Only the preview changes. Rescue is how much of the no-preview failure the preview",
           "removes; large rescue means that preview was enough for the rule to bind."]
    for t in tags:
        try:
            run(t, items, out)
        except FileNotFoundError:
            out.append(f"\n# {t}: not run yet")
    txt = "\n".join(out)
    print(txt)
    open(os.path.join(ROOT, "results", "semaddr_tables.md"), "w").write(txt + "\n")


if __name__ == "__main__":
    main(sys.argv[1:] or ["qwen3-8b", "gemma3-12b", "phi4-mini",
                          "mistral-small-24b", "qwen3.5-27b"])
