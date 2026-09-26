"""Exploratory paired reanalysis of the committed ConfB cell table.

Uses all 200 claims and six models. This is post hoc and does not alter the
registered readout or any source data.
"""

import csv
import random
import statistics
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results/g24a/g24a_confb_analysis_v1_cells.csv"
OUTPUT = ROOT / "results/audits/g24a_confb_restoration_controls_v1.md"


def mean(values):
    return statistics.mean(values)


def percentile(sorted_values, q):
    x = (len(sorted_values) - 1) * q
    lo = int(x)
    hi = min(lo + 1, len(sorted_values) - 1)
    return sorted_values[lo] + (x - lo) * (sorted_values[hi] - sorted_values[lo])


def main():
    cells = defaultdict(dict)
    with SOURCE.open(newline="") as stream:
        for row in csv.DictReader(stream):
            key = (row["cfb_id"], row["model"])
            assert row["cell"] not in cells[key]
            cells[key][row["cell"]] = float(row["value"])
    assert len(cells) == 1200
    assert all(set(v) == {"Y0", "A+", "A-", "CF+", "CF-", "W", "I"} for v in cells.values())
    claims = defaultdict(list)
    for (claim, _), v in cells.items():
        y, m = v["Y0"], (v["CF+"] + v["CF-"]) / 2
        claims[claim].append({
            "cf_center": abs(y - m),
            "cf_arm": (abs(y - v["CF+"]) + abs(y - v["CF-"])) / 2,
            "withheld": abs(y - v["W"]),
            "irrelevant": abs(y - v["I"]),
            "constant50": abs(y - 50),
            "both5": int(abs(y - v["CF+"]) <= 5 and abs(y - v["CF-"]) <= 5),
            "both10": int(abs(y - v["CF+"]) <= 10 and abs(y - v["CF-"]) <= 10),
        })
    assert len(claims) == 200 and all(len(v) == 6 for v in claims.values())
    metrics = {claim: {k: mean(row[k] for row in vals) for k in vals[0]} for claim, vals in claims.items()}
    ids = sorted(metrics)
    rng = random.Random("g24a_confb_restoration_controls_v1")
    draws = [[rng.choice(ids) for _ in ids] for _ in range(5000)]

    def summarize(fn):
        point = mean(fn(metrics[c]) for c in ids)
        boot = sorted(mean(fn(metrics[c]) for c in draw) for draw in draws)
        return f"{point:.2f} [{percentile(boot, .025):.2f}, {percentile(boot, .975):.2f}]"

    out = [
        "# ConfB restoration-control reanalysis (exploratory, post hoc)",
        "",
        "Source: committed `g24a_confb_analysis_v1_cells.csv`; all 200 fresh claims × six models, no filters. "
        "Claims are the paired bootstrap unit (5,000 draws). Scores are 0–100. "
        "This analysis was conceived after the registered ConfB report and has no confirmatory status.",
        "",
        "| Quantity | Mean [paired bootstrap 95% CI] |",
        "|---|---:|",
    ]
    quantities = [
        ("CRE of actual CF center", lambda v: v["cf_center"]),
        ("Mean arm-wise absolute restoration error", lambda v: v["cf_arm"]),
        ("Error of WithheldCF", lambda v: v["withheld"]),
        ("Error of IrrelevantCF", lambda v: v["irrelevant"]),
        ("Error of constant 50 predictor", lambda v: v["constant50"]),
        ("Actual CF center error minus IrrelevantCF error", lambda v: v["cf_center"] - v["irrelevant"]),
        ("Actual CF center error minus WithheldCF error", lambda v: v["cf_center"] - v["withheld"]),
        ("Actual CF center error minus constant 50 error", lambda v: v["cf_center"] - v["constant50"]),
    ]
    out.extend(f"| {name} | {summarize(fn)} |" for name, fn in quantities)
    out += ["", "Exact model×claim counts: both CF arms within 5 points of Y0: "
            f"{sum(round(metrics[c]['both5'] * 6) for c in ids)}/1200; "
            "within 10 points: "
            f"{sum(round(metrics[c]['both10'] * 6) for c in ids)}/1200.", "",
            "Interpretation limit: the arm-center CRE can understate arm-wise errors by cancellation; "
            "WithheldCF and IrrelevantCF have different prompts from actual CF and are descriptive controls. "
            "The constant-50 comparison is a calibration reference, not a proposed retraction method.", ""]
    OUTPUT.write_text("\n".join(out))
    print(OUTPUT)


if __name__ == "__main__":
    main()
