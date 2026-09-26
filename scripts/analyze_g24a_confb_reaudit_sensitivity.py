"""Post hoc ConfB sensitivity to independent blind material-audit flags."""

import csv
import json
import random
import statistics as st
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CELLS = ROOT / "results/g24a/g24a_confb_analysis_v1_cells.csv"
FLAGS = ROOT / "results/audits/g24a_confb_reaudit/reaudit_flags.json"
OUT = ROOT / "results/audits/g24a_confb_reaudit/conb_sensitivity.md"


def avg(xs):
    return st.mean(xs)


def pct(xs, q):
    xs = sorted(xs)
    x = (len(xs) - 1) * q
    i = int(x)
    return xs[i] + (x - i) * (xs[min(i + 1, len(xs) - 1)] - xs[i])


def main():
    by = defaultdict(dict)
    for r in csv.DictReader(CELLS.open()):
        key = (r["cfb_id"], r["model"])
        assert r["cell"] not in by[key]
        by[key][r["cell"]] = float(r["value"])
    assert len(by) == 1200
    ids = sorted({k[0] for k in by})
    assert len(ids) == 200
    models = sorted({k[1] for k in by})
    flags = json.loads(FLAGS.read_text())
    invalid = set(flags["invalid_ids"])
    mismatch = set(flags["relation_mismatch_ids"])
    unnatural = set(flags["naturalness_flag_ids"])
    subsets = {
        "All frozen 200": set(ids),
        "Audit pair-valid": set(ids) - invalid,
        "Audit relation-consistent": set(ids) - mismatch,
        "Audit valid + relation-consistent + natural": set(flags["valid_natural_ids"]),
        "Audit flagged invalid": invalid,
    }
    rng = random.Random("g24a_confb_reaudit_sensitivity_v1")

    def calc(selected):
        sel = sorted(selected)
        assert all((cid, m) in by for cid in sel for m in models)
        claim = {}
        for cid in sel:
            values = [by[(cid, m)] for m in models]
            claim[cid] = {
                "admit_sep": avg(v["A+"] - v["A-"] for v in values),
                "cf_sep": avg(v["CF+"] - v["CF-"] for v in values),
                "cre": avg(abs(v["Y0"] - (v["CF+"] + v["CF-"]) / 2) for v in values),
                "arm_error": avg((abs(v["Y0"] - v["CF+"]) + abs(v["Y0"] - v["CF-"])) / 2 for v in values),
            }
        draws = [[rng.choice(sel) for _ in sel] for _ in range(3000)]

        def summary(metric):
            point = avg(claim[c][metric] for c in sel)
            boots = [avg(claim[c][metric] for c in draw) for draw in draws]
            return f"{point:.2f} [{pct(boots, .025):.2f},{pct(boots, .975):.2f}]"

        return [len(sel)] + [summary(k) for k in ("admit_sep", "cf_sep", "cre", "arm_error")]

    out = ["# ConfB blind re-audit sensitivity (post hoc)", "",
           "The independent local OpenCode audit saw claim and randomly swapped evidence A/B, without previous labels or model output. These strata were defined **after** the held-out ConfB results. They cannot constitute a new confirmation, and LLM-assisted semantic labels are not human gold. The primary analysis retains all 200 frozen pairs.",
           "", "All six models are kept for every selected claim. Each interval is a claim-cluster bootstrap (3,000 draws within stratum); small flagged strata have unstable intervals. Scores are 0–100.",
           "", "| Stratum | n claims | Admit sep | CF sep | Center CRE | Arm-wise error |",
           "|---|---:|---:|---:|---:|---:|"]
    for name, subset in subsets.items():
        row = calc(subset)
        out.append(f"| {name} | " + " | ".join(map(str, row)) + " |")
    out += ["", "The audit's main material concern is semantic entailment, not whether a model judges the evidence strongly. If the main result remains in the stricter stratum, that reduces dependence on obvious malformed pairs but does not remove residual measurement or benchmark-format concerns.", ""]
    OUT.write_text("\n".join(out))
    print(OUT)


if __name__ == "__main__":
    main()
