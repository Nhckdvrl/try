"""Stage 4A, deconfounded.

A policy that states the forbidden proposition has already put that proposition in
front of the model before the tool returns anything, so a raw REI on the retrieved
document mixes the policy's own effect with the document's. Following Stage 3E,
everything is measured against the policy's own baseline, in raw rating points:

    PolicyMentionEffect(P) = s [ Y(P, no document) - Y(base) ]
    ToolMarginal(P, v)     = s [ Y(P, document v) - Y(P, no document) ]
    AgentExclusionEffect   = ToolMarginal(no policy) - ToolMarginal(P)
"""
import json, os, sys, statistics as st
from collections import defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from schema import load_items
from analyze_stage2 import cluster_of
from analyze_png import cluster_boot

ROOT = os.path.join(os.path.dirname(__file__), "..")
POLICIES = [("none", "no policy"), ("pid", "policy names D7 only"),
            ("pgist", "policy names D7 + a gist"),
            ("pprop", "policy names D7 + its full proposition"),
            ("padmit", "policy endorses D7")]
VARIANTS = [("same_d7", "D7, the policy's proposition"),
            ("para_d7", "D7, paraphrased"),
            ("diff_d7", "D7, a different proposition"),
            ("same_d9", "D9, the policy's proposition")]


def main(tags):
    items = {i.item_id: i for i in load_items(os.path.join(ROOT, "data", "items", "items_v1.jsonl"))}
    out = ["# Stage 4A deconfounded — marginal effect of the retrieved document", "",
           "All quantities are sign-aligned rating points. `ToolMarginal` is what the",
           "retrieved document adds *given the policy is already in the context*, so a policy",
           "that quotes the forbidden proposition is not credited for its own effect.", ""]
    for tag in tags:
        p = os.path.join(ROOT, "results", "raw", f"{tag}_agent.jsonl")
        if not os.path.exists(p):
            continue
        runs = defaultdict(dict)
        for line in open(p):
            r = json.loads(line)
            runs[r["item_id"]][r["kind_name"]] = r
        out.append(f"\n## {tag}\n")
        out.append("| policy | PolicyMentionEffect | ToolMarginal (D7, its proposition) | AgentExclusionEffect |")
        out.append("|---|---|---|---|")
        base_marg = None
        for pol, nm in POLICIES:
            pme, tm, cls = [], [], []
            for iid, r in runs.items():
                it = items.get(iid)
                if it is None:
                    continue
                s = 1.0 if it.critical_direction == "increase" else -1.0
                g = lambda c: r.get(c, {}).get("value")
                b = g("ag_base")
                only = b if pol == "none" else g(f"ag_{pol}_none")
                withdoc = g(f"ag_{pol}_same_d7") if pol != "none" else g("ag_none_same_d7")
                if None in (b, only, withdoc):
                    continue
                pme.append(s * (only - b))
                tm.append(s * (withdoc - only))
                cls.append(cluster_of(it))
            if len(tm) < 20:
                continue
            m1, l1, h1, _ = cluster_boot(pme, cls, n=4000, seed=1)
            m2, l2, h2, _ = cluster_boot(tm, cls, n=4000, seed=2)
            if pol == "none":
                base_marg = dict(zip(range(len(tm)), tm))
                aee = "—"
            else:
                d = [a - b for a, b in zip([base_marg[i] for i in range(len(tm))], tm)] \
                    if base_marg and len(base_marg) == len(tm) else []
                if d:
                    m3, l3, h3, p3 = cluster_boot(d, cls, n=4000, seed=3)
                    aee = f"**{m3:+.1f}** [{l3:+.1f}, {h3:+.1f}] p={p3:.4f}"
                else:
                    aee = "—"
            out.append(f"| {nm} | {m1:+.1f} [{l1:+.1f}, {h1:+.1f}] | "
                       f"**{m2:+.1f}** [{l2:+.1f}, {h2:+.1f}] | {aee} |")

        out.append("")
        out.append("| policy | " + " | ".join(n for _, n in VARIANTS) + " |")
        out.append("|---|" + "---|" * len(VARIANTS))
        for pol, nm in (("pid", "ID-only policy"), ("pprop", "proposition policy")):
            cells = []
            for var, _ in VARIANTS:
                tm, cls = [], []
                for iid, r in runs.items():
                    it = items.get(iid)
                    if it is None:
                        continue
                    s = 1.0 if it.critical_direction == "increase" else -1.0
                    g = lambda c: r.get(c, {}).get("value")
                    only, withdoc = g(f"ag_{pol}_none"), g(f"ag_{pol}_{var}")
                    if None in (only, withdoc):
                        continue
                    tm.append(s * (withdoc - only))
                    cls.append(cluster_of(it))
                if len(tm) < 20:
                    cells.append("—")
                    continue
                m, lo, hi, _ = cluster_boot(tm, cls, n=4000, seed=4)
                cells.append(f"{m:+.1f} [{lo:+.1f}, {hi:+.1f}]")
            out.append(f"| {nm} | " + " | ".join(cells) + " |")
    txt = "\n".join(out)
    print(txt)
    open(os.path.join(ROOT, "results", "agent_marginal.md"), "w").write(txt + "\n")


if __name__ == "__main__":
    main(sys.argv[1:] or ["qwen3-8b", "gemma3-12b", "phi4-mini", "qwen3.5-27b"])
