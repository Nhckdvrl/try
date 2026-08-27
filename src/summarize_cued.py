"""Causal vs masked-diffusion LMs under one identical fixed-position readout.

Restricted to legal_judgment + evidence_inference, the families where the
fixed-position readout was validated against the behavioural one on Qwen3-8B
(item-level r = 0.76 / 0.90).
"""
import glob, json, os, sys, statistics as st
from collections import defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from schema import load_items
from analyze import boot_ci, boot_p, wins

ROOT = os.path.join(os.path.dirname(__file__), "..")
FAMS = ("legal_judgment", "evidence_inference")
KIND = {"llada-8b": "masked diffusion", "dream-7b": "masked diffusion"}
ORDER = ["phi4-mini", "gemma3-12b", "qwen2.5-7b", "qwen3-8b", "mistral-small-24b",
         "llada-8b", "dream-7b"]


def main():
    items = {i.item_id: i for i in load_items(os.path.join(ROOT, "data", "items", "items_v1.jsonl"))}
    L = ["## Causal vs bidirectional (masked diffusion), identical fixed-position readout", "",
         "| model | attention | usable n | RuleAcc post | REI Exclude-Pre | REI Exclude-Post | "
         "pre − post | pre − pre_repeat |", "|---|---|---:|---:|---|---|---|---|"]
    rows_out = {}
    for tag in ORDER:
        p = os.path.join(ROOT, "results", "raw", f"{tag}_cued.jsonl")
        if not os.path.exists(p):
            continue
        runs = defaultdict(dict)
        for line in open(p):
            r = json.loads(line)
            runs[r["item_id"]][r["kind_name"]] = r
        rei = defaultdict(list)
        rp = []
        for iid, r in runs.items():
            it = items.get(iid)
            if it is None or it.task_family not in FAMS:
                continue
            need = ("base", "admit_pre", "admit_post")
            if any(k not in r or r[k].get("value") is None for k in need):
                continue
            s = 1.0 if it.critical_direction == "increase" else -1.0
            y0 = r["base"]["value"]
            lev = (r["admit_pre"]["value"] + r["admit_post"]["value"]) / 2 - y0
            if s * lev <= 0:
                continue
            for c in ("exclude_pre", "exclude_post", "exclude_pre_repeat", "ledger",
                      "sanitation", "admit_pre_repeat"):
                if c in r and r[c].get("value") is not None:
                    rei[c].append(s * (r[c]["value"] - y0) / abs(lev))
            if "rule_probe_exclude_post" in r and r["rule_probe_exclude_post"].get("p_yes") is not None:
                rp.append(1 - r["rule_probe_exclude_post"]["p_yes"])
        n = len(rei["exclude_pre"])
        if n == 0:
            continue
        rows_out[tag] = rei

        def cell(c):
            v = [wins(x) for x in rei[c]]
            m, lo, hi = boot_ci(v, seed=11)
            return f"{m:+.2f} [{lo:+.2f}, {hi:+.2f}]"

        def contrast(a, b):
            if not rei[a] or len(rei[a]) != len(rei[b]):
                return "—"
            d = [wins(x) - wins(y) for x, y in zip(rei[a], rei[b])]
            m, lo, hi = boot_ci(d, seed=12)
            return f"{m:+.2f} [{lo:+.2f}, {hi:+.2f}] p={boot_p(d, seed=13):.4f}"

        L.append(f"| {tag} | {KIND.get(tag,'causal')} | {n} | "
                 f"{st.mean(rp):.3f} | {cell('exclude_pre')} | {cell('exclude_post')} | "
                 f"{contrast('exclude_pre','exclude_post')} | "
                 f"{contrast('exclude_pre','exclude_pre_repeat')} |")

    L += ["", "### Mitigations under the same readout", "",
          "| model | `ledger` | `sanitation` | `admit_pre_repeat` |", "|---|---|---|---|"]
    for tag, rei in rows_out.items():
        cells = []
        for c in ("ledger", "sanitation", "admit_pre_repeat"):
            v = [wins(x) for x in rei.get(c, [])]
            cells.append(f"{st.mean(v):+.2f}" if v else "—")
        L.append(f"| {tag} | " + " | ".join(cells) + " |")

    txt = "\n".join(L)
    print(txt)
    open(os.path.join(ROOT, "results", "cued_diffusion_tables.md"), "w").write(txt + "\n")


if __name__ == "__main__":
    main()
