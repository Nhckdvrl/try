"""Post hoc same-item admissible-set reanalysis of frozen ConfA cells."""

import csv
import hashlib
import json
import math
import random
import statistics
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results/g24a/g24a_confa_analysis_v1_cells.csv"
OUT = ROOT / "results/g24a/g24a_confa_final_set_reanalysis_v1"
KINDS = {"base", "admit_pre", "admit_post", "exclude_pre", "exclude_post"}


def mean(xs):
    return sum(xs) / len(xs)


def ci(values):
    vals = sorted(values)
    return vals[int(.025 * len(vals))], vals[int(.975 * len(vals))]


def mapping(xs, ys):
    mx, my = mean(xs), mean(ys)
    xx = sum((x - mx) ** 2 for x in xs)
    yy = sum((y - my) ** 2 for y in ys)
    xy = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    return {"slope": xy / xx, "correlation": xy / math.sqrt(xx * yy)}


def main():
    source_bytes = SOURCE.read_bytes()
    rows = list(csv.DictReader(source_bytes.decode().splitlines()))
    assert len(rows) == 15000
    by_key = {}
    for row in rows:
        key = row["model"], row["item_id"], row["kind"]
        assert key not in by_key and row["kind"] in KINDS
        by_key[key] = row
    grouped = defaultdict(dict)
    for (model, item_id, kind), row in by_key.items():
        grouped[model, item_id][kind] = float(row["value"])
    assert len(grouped) == 3000
    assert all(set(cells) == KINDS for cells in grouped.values())
    models = sorted({k[0] for k in grouped})
    ids = sorted({k[1] for k in grouped})
    assert len(models) == 6 and len(ids) == 500
    assert all((model, item_id) in grouped for model in models for item_id in ids)
    assert all(0 <= value <= 100 for cells in grouped.values() for value in cells.values())
    assert all(len({int(by_key[model, item_id, kind]["direction"]) for kind in KINDS}) == 1
               for model in models for item_id in ids)
    records = []
    for (model, item_id), v in grouped.items():
        domain = "FEVER" if "_fever_" in item_id else "SciFact" if "_scifact_" in item_id else None
        assert domain is not None
        direction = int(by_key[model, item_id, "base"]["direction"])
        assert direction in (-1, 1)
        records.append({"model": model, "item_id": item_id, "domain": domain,
                        "direction": direction,
                        "base": v["base"],
                        "admit_pre": v["admit_pre"], "admit_post": v["admit_post"],
                        "exclude_pre": v["exclude_pre"], "exclude_post": v["exclude_post"],
                        "signed_pre": direction * (v["exclude_pre"] - v["base"]),
                        "signed_post": direction * (v["exclude_post"] - v["base"]),
                        "abs_pre": abs(v["exclude_pre"] - v["base"]),
                        "abs_post": abs(v["exclude_post"] - v["base"]),
                        "abs_admit_pre": abs(v["admit_pre"] - v["base"]),
                        "abs_admit_post": abs(v["admit_post"] - v["base"]),
                        "pre_10": int(abs(v["exclude_pre"] - v["base"]) >= 10),
                        "pre_20": int(abs(v["exclude_pre"] - v["base"]) >= 20),
                        "post_10": int(abs(v["exclude_post"] - v["base"]) >= 10),
                        "post_20": int(abs(v["exclude_post"] - v["base"]) >= 20)})
    metrics = ("signed_pre", "signed_post", "abs_pre", "abs_post", "abs_admit_pre",
               "abs_admit_post", "pre_10", "pre_20", "post_10", "post_20")
    rng = random.Random(20260927)

    def summarize(records, boot=True):
        result = {m: mean([x[m] for x in records]) for m in metrics}
        result["n_cells"] = len(records)
        result["n_items"] = len({r["item_id"] for r in records})
        result["median_abs_pre"] = statistics.median(x["abs_pre"] for x in records)
        result["median_abs_post"] = statistics.median(x["abs_post"] for x in records)
        result["base_mapping"] = {kind: mapping([r["base"] for r in records],
                                                [r[kind] for r in records])
                                  for kind in ("admit_pre", "admit_post", "exclude_pre", "exclude_post")}
        if boot:
            by_item = defaultdict(list)
            for r in records:
                by_item[r["item_id"]].append(r)
            units = list(by_item)
            samples = {m: [] for m in metrics}
            for _ in range(5000):
                selected = [by_item[rng.choice(units)] for _ in units]
                flat = [r for group in selected for r in group]
                for m in metrics:
                    samples[m].append(mean([r[m] for r in flat]))
            result["ci95"] = {m: ci(samples[m]) for m in metrics}
        return result

    summaries = {"pooled": summarize(records)}
    for domain in ("FEVER", "SciFact"):
        summaries[domain] = summarize([x for x in records if x["domain"] == domain])
    for model in models:
        summaries[model] = summarize([x for x in records if x["model"] == model])
    output = {"status": "post_hoc_reanalysis", "source": str(SOURCE.relative_to(ROOT)),
              "source_sha256": hashlib.sha256(source_bytes).hexdigest(),
              "n_raw_cells": len(rows), "summaries": summaries}
    OUT.with_suffix(".json").write_text(json.dumps(output, indent=2) + "\n")
    def fmt(s, key):
        a, b = s["ci95"][key]
        return f"{s[key]:+.2f} [{a:+.2f}, {b:+.2f}]"
    lines = ["# ConfA final-admissible-set reanalysis", "",
             "**Post hoc analysis of the original frozen 15,000 cells.** The registered ConfA "
             "signed estimands and failed prospective-leakage headline remain unchanged. "
             "This reanalysis asks a different question: whether each excluded-evidence response "
             "matches the same item's Base response when the final admissible evidence is the same.", "",
             f"Source SHA-256: `{output['source_sha256']}`. All 500 items, six models and five cells "
             "per item/model are included. No model inference or item filtering was performed.", "",
             "| Group | Signed ExcludePre−Base | Absolute ExcludePre−Base | Signed ExcludePost−Base | Absolute ExcludePost−Base | Pre ≥10 pp | Pre ≥20 pp |",
             "|---|---:|---:|---:|---:|---:|---:|"]
    for name, s in summaries.items():
        lines.append(f"| {name} | {fmt(s,'signed_pre')} | {fmt(s,'abs_pre')} | "
                     f"{fmt(s,'signed_post')} | {fmt(s,'abs_post')} | "
                     f"{100*s['pre_10']:.1f}% | {100*s['pre_20']:.1f}% |")
    lines += ["", "## Mapping of Base judgments", "",
              "OLS slopes below 1 describe compression of the 0–100 output range relative to "
              "the same-item Base rating. This is a behavioral description, not an internal-state claim.", "",
              "| Group | AdmitPre slope | AdmitPost slope | ExcludePre slope | ExcludePost slope | ExcludePre correlation |",
              "|---|---:|---:|---:|---:|---:|"]
    for name, s in summaries.items():
        m = s["base_mapping"]
        lines.append(f"| {name} | {m['admit_pre']['slope']:.3f} | "
                     f"{m['admit_post']['slope']:.3f} | {m['exclude_pre']['slope']:.3f} | "
                     f"{m['exclude_post']['slope']:.3f} | "
                     f"{m['exclude_pre']['correlation']:.3f} |")
    lines += ["", "Bootstrap intervals resample items (5,000 draws), retaining all models for each item. "
              "The source mixes 334 FEVER and 166 SciFact items. Signed effects use the original "
              "critical-direction normalization; absolute effects use the raw 0–100 readout. "
              "The full JSON also reports admitted-evidence absolute shifts and post-exclusion thresholds.", "",
              "This comparison is a behavioral final-set criterion under each frozen prompt. "
              "Prompt framing differs from Base, and a nonzero absolute difference alone does not "
              "identify the mechanism. It does directly test the item-wise invariance target that "
              "the original signed mean cannot establish.", ""]
    OUT.with_suffix(".md").write_text("\n".join(lines))
    print(OUT.with_suffix(".md"))


if __name__ == "__main__":
    main()
