"""Stage 4A: system -> tool -> answer."""
import json, os, sys, statistics as st
from collections import defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from schema import load_items
from analyze import wins
from analyze_stage2 import cluster_of
from analyze_png import cluster_boot

ROOT = os.path.join(os.path.dirname(__file__), "..")
LAB = {
    "ag_none_same_d7": "no policy at all (naive)",
    "ag_pid_same_d7": "policy names D7 only",
    "ag_pgist_same_d7": "policy names D7 + a gist of it",
    "ag_pprop_same_d7": "policy names D7 + its full proposition",
    "ag_post_same_d7": "policy delivered AFTER the tool output",
    "ag_pid_para_d7": "ID-only policy, D7 arrives paraphrased",
    "ag_pprop_para_d7": "proposition policy, D7 arrives paraphrased",
    "ag_pid_diff_d7": "ID-only policy, D7 carries a DIFFERENT proposition",
    "ag_pprop_diff_d7": "proposition policy, D7 carries a DIFFERENT proposition",
    "ag_pid_same_d9": "ID-only policy, same proposition arrives as D9",
    "ag_pprop_same_d9": "proposition policy, same proposition arrives as D9",
}
ORDER = list(LAB)


def main(tags):
    items = {i.item_id: i for i in load_items(os.path.join(ROOT, "data", "items", "items_v1.jsonl"))}
    out = ["# Stage 4A — system policy, tool output, answer", "",
           "SYSTEM carries the policy before anything is retrieved; the document arrives in a",
           "TOOL message; the assistant then answers. REI is anchored on `ag_base` (document",
           "not retrieved) and `ag_padmit_same_d7` (document retrieved and endorsed).", ""]
    for tag in tags:
        p = os.path.join(ROOT, "results", "raw", f"{tag}_agent.jsonl")
        if not os.path.exists(p):
            continue
        runs = defaultdict(dict)
        for line in open(p):
            r = json.loads(line)
            runs[r["item_id"]][r["kind_name"]] = r
        anchor = {}
        for iid, r in runs.items():
            it = items.get(iid)
            if it is None:
                continue
            b = r.get("ag_base", {}).get("value")
            a = r.get("ag_padmit_same_d7", {}).get("value")
            if b is None or a is None:
                continue
            s = 1.0 if it.critical_direction == "increase" else -1.0
            if s * (a - b) <= 0:
                continue
            anchor[iid] = (b, abs(a - b), s)
        out.append(f"\n## {tag}   (n usable = {len(anchor)})\n")
        out.append("| condition | REI |")
        out.append("|---|---|")
        for c in ORDER:
            vals, cls = [], []
            for iid, (b, L, s) in anchor.items():
                v = runs[iid].get(c, {}).get("value")
                if v is None:
                    continue
                vals.append(wins(s * (v - b) / L))
                cls.append(cluster_of(items[iid]))
            if len(vals) < 15:
                continue
            m, lo, hi, _ = cluster_boot(vals, cls, n=4000, seed=1)
            out.append(f"| {LAB[c]} | **{m:+.3f}** [{lo:+.3f}, {hi:+.3f}] |")
    txt = "\n".join(out)
    print(txt)
    open(os.path.join(ROOT, "results", "agent_tables.md"), "w").write(txt + "\n")


if __name__ == "__main__":
    main(sys.argv[1:] or ["qwen3-8b", "gemma3-12b", "phi4-mini"])
