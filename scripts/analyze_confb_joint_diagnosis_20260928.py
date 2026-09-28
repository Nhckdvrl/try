#!/usr/bin/env python3
"""Post-hoc, CPU-only diagnosis of the frozen ConfB cells; no inference.

All 200 claims and six models are retained. Claim-cluster bootstrap moves
all models together. Outcome-conditioned slices are descriptive only.
The exact center/contrast identities are algebra, not a causal model.
"""
import csv
import hashlib
import json
import math
import random
import statistics as st
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "results/g24a/g24a_confb_analysis_v1_cells.csv"
DEST = ROOT / "results/audits/confb_joint_diagnosis_20260928.json"
SEED = 20260928
B = 5000


def mean(xs):
    return st.fmean(xs)


def quantile(xs, q):
    xs = sorted(xs)
    index = (len(xs) - 1) * q
    lo = int(index)
    hi = min(lo + 1, len(xs) - 1)
    return xs[lo] + (index - lo) * (xs[hi] - xs[lo])


def components(v):
    center = (v["CF+"] + v["CF-"]) / 2
    b = center - v["Y0"]
    d = (v["CF+"] - v["CF-"]) / 2
    arm_mae = (abs(v["CF+"] - v["Y0"]) + abs(v["CF-"] - v["Y0"])) / 2
    arm_mse = ((v["CF+"] - v["Y0"]) ** 2 + (v["CF-"] - v["Y0"]) ** 2) / 2
    assert math.isclose(arm_mae, max(abs(b), abs(d)), abs_tol=1e-9)
    assert math.isclose(arm_mse, b * b + d * d, abs_tol=1e-8)
    return {
        "admit_signed": v["A+"] - v["A-"],
        "admit_absolute": abs(v["A+"] - v["A-"]),
        "cf_signed": 2 * d,
        "cf_absolute": 2 * abs(d),
        "center_mae": abs(b),
        "arm_mae": arm_mae,
        "shared_mse": b * b,
        "polarity_mse": d * d,
        "same_side_fraction": float((v["CF+"] - v["Y0"]) * (v["CF-"] - v["Y0"]) > 0),
        "irrelevant_mae": abs(v["I"] - v["Y0"]),
        "cf_arm_vs_irrelevant": (abs(v["CF+"] - v["I"]) + abs(v["CF-"] - v["I"])) / 2,
        "center_excess_vs_irrelevant": abs(b) - abs(v["I"] - v["Y0"]),
        "irrelevant_distance_50": abs(v["I"] - 50),
        "cf_arm_distance_50": (abs(v["CF+"] - 50) + abs(v["CF-"] - 50)) / 2,
        "cf_center_distance_50": abs(center - 50),
    }


def aggregate(records):
    out = {k: mean(r[k] for r in records) for k in records[0]}
    out["absolute_suppression_fraction"] = 1 - out["cf_absolute"] / out["admit_absolute"]
    out["shared_fraction_of_mse"] = out["shared_mse"] / (out["shared_mse"] + out["polarity_mse"])
    return out


def cv_affine(records, key, claim_folds):
    """Diagnostic inverse calibration, fit using OTHER claims only; no method claim."""
    errors = []
    constant_errors = []
    for fold in range(5):
        train = [(c, v) for c, v in records if claim_folds[c] != fold]
        test = [(c, v) for c, v in records if claim_folds[c] == fold]
        x = [key(v) for _, v in train]
        y = [v["Y0"] for _, v in train]
        mx, my = mean(x), mean(y)
        denom = sum((a - mx) ** 2 for a in x)
        slope = sum((a - mx) * (b - my) for a, b in zip(x, y)) / denom if denom else 0
        for _, v in test:
            pred = max(0, min(100, my + slope * (key(v) - mx)))
            errors.append(abs(pred - v["Y0"]))
            constant_errors.append(abs(my - v["Y0"]))
    return {"affine_inverse_mae": mean(errors), "training_mean_mae": mean(constant_errors)}


def raw_readout_check(cells, models):
    """Verify CSV against every frozen raw row and check the greedy digit readout."""
    item_map = {}
    for line in (ROOT / "data/items/g24a_confb_v1.jsonl").read_text().splitlines():
        r = json.loads(line)
        item_map[r["item_id"]] = (r["meta"]["cfb_id"], r["meta"]["arm"])
    mapping = {("plus", "base"): "Y0", ("plus", "admit_post"): "A+",
               ("minus", "admit_post"): "A-", ("plus", "counterfactual_delete_post"): "CF+",
               ("minus", "counterfactual_delete_post"): "CF-", ("plus", "withheld_cf"): "W",
               ("control", "irrelevant_cf"): "I"}
    greedy = defaultdict(dict)
    hashes = {}
    count = 0
    for model in models:
        for arm in ("plus", "minus", "control"):
            path = ROOT / f"results/raw/{model}_g24a_confb_{arm}.jsonl"
            hashes[str(path.relative_to(ROOT))] = hashlib.sha256(path.read_bytes()).hexdigest()
            for line in path.read_text().splitlines():
                r = json.loads(line)
                claim, item_arm = item_map[r["item_id"]]
                assert item_arm == arm and r["model_tag"] == model
                cell = mapping[arm, r["kind_name"]]
                assert cells[model, claim][cell] == float(r["value"])
                assert cell not in greedy[model, claim]
                digit = int(r["raw"].strip())
                assert 0 <= digit <= 9
                greedy[model, claim][cell] = digit * 100 / 9
                count += 1
    assert count == 8400 and len(greedy) == 1200
    v = list(greedy.values())
    return {"verified_raw_rows": count, "raw_sha256": hashes,
            "greedy_digit_statistics": aggregate([components(x) for x in v]),
            "greedy_threshold_disagreement_CF_Y0": mean(
                (((x["CF+"] >= 50) != (x["Y0"] >= 50)) +
                 ((x["CF-"] >= 50) != (x["Y0"] >= 50))) / 2 for x in v),
            "greedy_threshold_disagreement_I_Y0": mean(
                (x["I"] >= 50) != (x["Y0"] >= 50) for x in v),
            "interpretation": "Thresholding a rating is a readout check, not a new downstream action task."}


def cv_residual_weight(records, claim_folds):
    """Fit one residual evidence weight to polarity contrasts on training claims.

    Predict both held-out CF arms by the same convex mixture of clean and
    admitted judgments. This restrictive model is a diagnostic, not a theory.
    """
    errors, predicted_shifts, slopes = [], [], []
    for fold in range(5):
        train = [v for c, v in records if claim_folds[c] != fold]
        denominator = sum((v["A+"] - v["A-"]) ** 2 for v in train)
        slope = sum((v["A+"] - v["A-"]) * (v["CF+"] - v["CF-"])
                    for v in train) / denominator
        slope = min(1, max(0, slope))
        slopes.append(slope)
        for claim, v in records:
            if claim_folds[claim] != fold:
                continue
            for arm in ("+", "-"):
                pred = v["Y0"] + slope * (v["A" + arm] - v["Y0"])
                errors.append(abs(pred - v["CF" + arm]))
            predicted_shifts.append(abs(slope * ((v["A+"] + v["A-"]) / 2 - v["Y0"])))
    return {"fold_slopes": slopes, "heldout_arm_prediction_mae": mean(errors),
            "predicted_center_shift_mae": mean(predicted_shifts),
            "observed_center_shift_mae": mean(abs((v["CF+"] + v["CF-"]) / 2 - v["Y0"])
                                               for _, v in records)}


def main():
    cells = defaultdict(dict)
    count = 0
    for r in csv.DictReader(SOURCE.open()):
        key = (r["model"], r["cfb_id"])
        assert r["cell"] not in cells[key]
        cells[key][r["cell"]] = float(r["value"])
        count += 1
    models = sorted({m for m, _ in cells})
    claims = sorted({c for _, c in cells})
    assert (len(models), len(claims), count) == (6, 200, 8400)
    assert all(set(v) == {"Y0", "A+", "A-", "CF+", "CF-", "I", "W"} for v in cells.values())
    comps = {k: components(v) for k, v in cells.items()}
    pooled = aggregate(list(comps.values()))
    claim_means = [{k: mean(comps[m, c][k] for m in models) for k in pooled if k in next(iter(comps.values()))} for c in claims]
    rng = random.Random(SEED)
    draws = defaultdict(list)
    for _ in range(B):
        a = aggregate([claim_means[rng.randrange(len(claims))] for _ in claims])
        for k, v in a.items():
            draws[k].append(v)
    intervals = {k: [quantile(v, .025), quantile(v, .975)] for k, v in draws.items()}
    slices = []
    for threshold in [2, 5, 10]:
        selected = [v for v in comps.values() if v["cf_absolute"] <= threshold]
        slices.append({"threshold": threshold, "n": len(selected), "statistics": aggregate(selected)})
    shuffled = claims[:]
    random.Random(SEED).shuffle(shuffled)
    folds = {c: i % 5 for i, c in enumerate(shuffled)}
    by_model = {}
    for m in models:
        rr = [(c, cells[m, c]) for c in claims]
        by_model[m] = {
            "statistics": aggregate([comps[m, c] for c in claims]),
            "cv_cf_center": cv_affine(rr, lambda v: (v["CF+"] + v["CF-"]) / 2, folds),
            "cv_irrelevant": cv_affine(rr, lambda v: v["I"], folds),
            "cv_residual_weight": cv_residual_weight(rr, folds),
        }
    out = {
        "status": "exploratory_post_hoc_no_new_model_inference",
        "source": str(SOURCE.relative_to(ROOT)),
        "source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
        "source_head": "3ae666e235583dccf51ad595db737a71d1b8eacc",
        "bootstrap_unit": "claim, retaining all six models", "seed": SEED, "bootstrap_draws": B,
        "n_cells": len(cells), "pooled": pooled, "ci95": intervals,
        "descriptive_outcome_conditioned_slices": slices,
        "by_model": by_model,
        "raw_readout_check": raw_readout_check(cells, models),
        "limits": ["Two tested polarities do not prove full content invariance.",
                   "The shared component includes framing, calibration and semantic effects; it is not an identified mechanism.",
                   "Outcome-conditioned slices do not identify effects of successful suppression.",
                   "Inverse calibration is a diagnostic using clean targets on training claims, not a practical method."]}
    DEST.write_text(json.dumps(out, indent=2) + "\n")
    print(json.dumps({"pooled": pooled, "ci95": intervals, "by_model": by_model, "slices": slices}, indent=2))


if __name__ == "__main__":
    main()
