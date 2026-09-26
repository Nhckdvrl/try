"""Analyze the frozen G30 factorial pilot without outcome-based exclusions."""

import argparse
import hashlib
import json
import random
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ITEMS = ROOT / "data/items/g30_bayesian_status_pilot_v1.jsonl"
TAGS = ("qwen3-8b", "gemma3-12b", "mistral-small-24b")
CONDS = ("D", "N", "I", "R")


def mean(xs):
    return sum(xs) / len(xs)


def ci(xs):
    ys = sorted(xs)
    return [ys[int(0.025 * len(ys))], ys[int(0.975 * len(ys))]]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "results/g30/g30_bayesian_status_analysis_v1"))
    args = ap.parse_args()
    raw = ITEMS.read_bytes()
    item_sha = hashlib.sha256(raw).hexdigest()
    items = {r["id"]: r for r in map(json.loads, raw.splitlines())}
    assert len(items) == 40
    rows = []
    input_shas = {}
    for tag in TAGS:
        path = ROOT / f"results/raw/{tag}_g30_bayesian_status_v1.jsonl"
        blob = path.read_bytes()
        input_shas[tag] = hashlib.sha256(blob).hexdigest()
        rr = [json.loads(s) for s in blob.splitlines() if s]
        assert len(rr) == 160, (tag, len(rr))
        rows.extend(rr)
    assert len(rows) == 480
    errors = []
    by_key = {}
    for r in rows:
        key = (r["model_tag"], r["id"], r["condition"])
        if key in by_key:
            errors.append(f"duplicate {key}")
        by_key[key] = r
        if r["items_sha256"] != item_sha:
            errors.append(f"item SHA mismatch {key}")
        if r["probability_blue"] is None or r["choice"] is None:
            errors.append(f"unparsed {key}: {r['raw']!r}")
        if r["finish_reason"] != "stop":
            errors.append(f"unfinished {key}: {r['finish_reason']}")
    for tag in TAGS:
        for id_ in items:
            for cond in CONDS:
                if (tag, id_, cond) not in by_key:
                    errors.append(f"missing {(tag, id_, cond)}")
    if errors:
        raise ValueError("G30 integrity failure:\n" + "\n".join(errors[:30]))

    cell = []
    for tag in TAGS:
        for id_, item in items.items():
            v = {c: by_key[(tag, id_, c)] for c in CONDS}
            p = {c: v[c]["probability_blue"] for c in CONDS}
            choice = {c: v[c]["choice"] for c in CONDS}
            sign = 1 if item["e1_report"] == "Blue" else -1
            target = item["bayes_p_blue_after_e2_pct"]
            cell.append({"model": tag, "id": id_, "e2": item["e2_report"],
                         "prior": item["prior_blue"], "reliability": item["reliability"],
                         "bayes": target,
                         "signed_NI": sign * (p["N"] - p["I"]),
                         "abs_NI": abs(p["N"] - p["I"]),
                         "choice_NI": int(choice["N"] != choice["I"]),
                         "signed_RN": sign * (p["R"] - p["N"]),
                         "abs_RN": abs(p["R"] - p["N"]),
                         "choice_RN": int(choice["R"] != choice["N"]),
                         **{f"mae_{c}": abs(p[c] - target) for c in CONDS},
                         **{f"p_{c}": p[c] for c in CONDS},
                         **{f"choice_{c}": choice[c] for c in CONDS}})
    metrics = ("signed_NI", "abs_NI", "choice_NI", "signed_RN", "abs_RN", "choice_RN",
               "mae_D", "mae_N", "mae_I", "mae_R", "delta_mae_RN", "delta_mae_NI")
    for r in cell:
        r["delta_mae_RN"] = r["mae_R"] - r["mae_N"]
        r["delta_mae_NI"] = r["mae_N"] - r["mae_I"]

    def summarize(records):
        result = {m: mean([r[m] for r in records]) for m in metrics}
        by_id = defaultdict(list)
        for r in records:
            by_id[r["id"]].append(r)
        ids = list(by_id)
        rng = random.Random(30030)
        sampled = {m: [] for m in metrics}
        for _ in range(5000):
            selected = [by_id[rng.choice(ids)] for _ in ids]
            flat = [r for block in selected for r in block]
            for m in metrics:
                sampled[m].append(mean([r[m] for r in flat]))
        result["ci95"] = {m: ci(sampled[m]) for m in metrics}
        result["n_cells"] = len(records)
        result["n_cases"] = len(by_id)
        return result

    groups = {"pooled": cell}
    for tag in TAGS:
        groups[tag] = [r for r in cell if r["model"] == tag]
    for e2 in ("Blue", "Yellow"):
        groups[f"e2_{e2.lower()}"] = [r for r in cell if r["e2"] == e2]
    summary = {name: summarize(group) for name, group in groups.items()}
    pair_map = defaultdict(dict)
    for r in cell:
        pair_map[(r["model"], r["prior"], r["reliability"])][r["e2"]] = r
    separation = {}
    for tag in TAGS:
        pp = [v for k, v in pair_map.items() if k[0] == tag]
        assert len(pp) == 20 and all(set(v) == {"Blue", "Yellow"} for v in pp)
        separation[tag] = {c: mean([v["Blue"][f"p_{c}"] - v["Yellow"][f"p_{c}"] for v in pp])
                           for c in CONDS}
    separation["pooled"] = {c: mean([separation[t][c] for t in TAGS]) for c in CONDS}
    output = {"items_sha256": item_sha, "raw_sha256": input_shas, "n_raw": len(rows),
              "integrity_errors": errors, "summary": summary, "e2_separation": separation, "cells": cell}
    prefix = Path(args.out)
    prefix.parent.mkdir(parents=True, exist_ok=True)
    prefix.with_suffix(".json").write_text(json.dumps(output, indent=2))
    def fmt(s, m):
        a, b = s["ci95"][m]
        return f"{s[m]:+.2f} [{a:+.2f}, {b:+.2f}]"
    lines = ["# G30 Bayesian-status pilot — full analysis", "",
             f"40 audited factorial cases × 4 conditions × 3 models = {len(rows)} raw outputs. "
             "All parse and completion checks passed. This is an exploratory constructed-task anchor, "
             "not a fresh natural-evidence confirmation.", "",
             f"Frozen item SHA-256: `{item_sha}`.", "",
             "Positive signed N−I or R−N means movement toward the inadmissible E1; negative means movement away from it.", "",
             "| Group | N−I signed probability | N−I absolute | N/I choice disagreement | R−N signed probability | R−N absolute | R/N choice disagreement |",
             "|---|---:|---:|---:|---:|---:|---:|"]
    for name, s in summary.items():
        lines.append(f"| {name} | {fmt(s,'signed_NI')} | {fmt(s,'abs_NI')} | "
                     f"{fmt(s,'choice_NI')} | {fmt(s,'signed_RN')} | "
                     f"{fmt(s,'abs_RN')} | {fmt(s,'choice_RN')} |")
    lines += ["", "Choice disagreement is a fraction of paired cells. Probability contrasts and absolute error are percentage points.",
              "", "## Absolute error versus Bayesian posterior", "",
              "| Group | D | N | I | R | R−N error | N−I error |",
              "|---|---:|---:|---:|---:|---:|---:|"]
    for name, s in summary.items():
        lines.append(f"| {name} | {fmt(s,'mae_D')} | {fmt(s,'mae_N')} | "
                     f"{fmt(s,'mae_I')} | {fmt(s,'mae_R')} | {fmt(s,'delta_mae_RN')} | "
                     f"{fmt(s,'delta_mae_NI')} |")
    lines += ["", "## Uptake of valid E2", "",
              "For matched prior/reliability cells, the table shows predicted P(Blue) after a Blue E2 "
              "minus predicted P(Blue) after a Yellow E2. This gauges whether each condition still uses E2.",
              "", "| Group | D | N | I | R |", "|---|---:|---:|---:|---:|"]
    for name, s in separation.items():
        lines.append(f"| {name} | " + " | ".join(f"{s[c]:.2f}" for c in CONDS) + " |")
    lines += ["", "Case-cluster bootstrap intervals use 5,000 draws. The 40 cases are a designed "
              "factorial, so these intervals describe the stimulus grid rather than population sampling.", "",
              "The JSON companion contains all paired cells and source hashes. Interpretation is reported "
              "separately after examining the results; no item was removed based on outputs.", ""]
    prefix.with_suffix(".md").write_text("\n".join(lines))
    print(prefix.with_suffix(".md"))


if __name__ == "__main__":
    main()
