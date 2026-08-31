"""Analyze model output against BTF-3's independent ex-ante forecast.

Implements PREREGISTRATION_G7_EXANTE_ANCHOR.md §4 exactly:

    (V) rho_without = Spearman( p[oob_without], anchor ),  MAD_without
    (D) Delta_dev   = mean|p[oob_with] - a| - mean|p[oob_without] - a|
    (A) Delta_brier = Brier[oob_with] - Brier[oob_without]
    (C) mean |p - 50| per cell
    (L) all of the above in the licensed frame, as a reference column

No new generations. The anchor is a source column; the unit set is the 239
frozen units with a non-null anchor, an exclusion defined without reference to
any model output.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import random
import statistics as st

try:
    from .analyze_model_breadth import rank, pearson
except ImportError:  # direct script execution
    from analyze_model_breadth import rank, pearson

SEED = 20260829
N_RESAMPLES = 10_000
DISPLACEMENT_SESOI = 3.0
VALIDITY_FLOOR = 0.3
MIN_MODELS = 2
ANCHOR_COLUMN = "sota_forecast_probability"
SOURCE_SHA256 = "b28f8fe5634f81afa8e4b37d815f875b6e33c24edf590484f1948efea8db051a"


def bootstrap_mean(values: list[float], seed: int = SEED) -> dict:
    rng = random.Random(seed)
    draws = sorted(st.mean(rng.choice(values) for _ in values) for _ in range(N_RESAMPLES))
    lo = draws[int(0.025 * N_RESAMPLES)]
    hi = draws[min(N_RESAMPLES - 1, int(0.975 * N_RESAMPLES) - 1)]
    return {
        "mean": st.mean(values),
        "ci_low": lo,
        "ci_high": hi,
        "n": len(values),
        "n_resamples": N_RESAMPLES,
        "seed": seed,
    }


def load_cells(path: Path) -> tuple[dict[str, dict[str, float]], dict[str, int], dict[str, float]]:
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]
    by_condition: dict[str, dict[str, float]] = {}
    directions: dict[str, int] = {}
    resolutions: dict[str, float] = {}
    for row in rows:
        if row.get("record_type") != "decision" or row.get("value") is None:
            continue
        unit = row["independent_unit_id"]
        by_condition.setdefault(row["condition"], {})[unit] = row["value"]
        directions[unit] = int(row.get("direction", 1))
        realized = row.get("realized_resolution")
        if realized is not None:
            resolutions[unit] = float(realized)
    return by_condition, directions, resolutions


def frame_stats(
    with_values: dict[str, float],
    without_values: dict[str, float],
    anchor: dict[str, float],
    resolution: dict[str, float],
    directions: dict[str, int],
) -> dict:
    units = sorted(set(with_values) & set(without_values) & set(anchor) & set(resolution))
    a = [anchor[u] for u in units]
    pw = [with_values[u] for u in units]
    pn = [without_values[u] for u in units]
    r = [resolution[u] for u in units]
    s = [directions[u] for u in units]

    dev_with = [abs(x - y) for x, y in zip(pw, a)]
    dev_without = [abs(x - y) for x, y in zip(pn, a)]

    return {
        "units": len(units),
        "rho_without": pearson(rank(pn), rank(a)),
        "rho_with": pearson(rank(pw), rank(a)),
        "mad_without": st.mean(dev_without),
        "mad_with": st.mean(dev_with),
        "delta_dev": bootstrap_mean([x - y for x, y in zip(dev_with, dev_without)]),
        "brier_without": st.mean((p / 100 - y) ** 2 for p, y in zip(pn, r)),
        "brier_with": st.mean((p / 100 - y) ** 2 for p, y in zip(pw, r)),
        "delta_brier": bootstrap_mean(
            [(p / 100 - y) ** 2 - (q / 100 - y) ** 2 for p, q, y in zip(pw, pn, r)]
        ),
        "confidence_without": st.mean(abs(p - 50) for p in pn),
        "confidence_with": st.mean(abs(p - 50) for p in pw),
        "signed_gap_without": st.mean(si * (p - ai) for si, p, ai in zip(s, pn, a)),
        "signed_gap_with": st.mean(si * (p - ai) for si, p, ai in zip(s, pw, a)),
        "anchor_mean": st.mean(a),
    }


def verdict(delta: dict) -> str:
    if delta["mean"] >= DISPLACEMENT_SESOI and delta["ci_low"] > 0:
        return "displacement"
    if delta["ci_low"] >= -DISPLACEMENT_SESOI and delta["ci_high"] <= DISPLACEMENT_SESOI:
        return "no_displacement"
    return "indeterminate"


def interpretation(displacement: str, delta_brier_mean: float) -> tuple[str, str]:
    if displacement == "displacement":
        if delta_brier_mean < 0:
            return (
                "displacement_with_accuracy_gain",
                "The packet makes the model more accurate about the outcome and less "
                "faithful to what was knowable at the time.",
            )
        return (
            "displacement_without_accuracy_gain",
            "The packet moves the model away from an independent ex-ante judgment without "
            "improving outcome accuracy. Not what was predicted; reported as such.",
        )
    if displacement == "no_displacement":
        return (
            "no_displacement",
            "The packet does not move the model away from an independent ex-ante judgment. "
            "The self-difference result stands, but no infidelity-to-the-ex-ante-state claim "
            "is licensed.",
        )
    return ("indeterminate", "The interval is reported; nothing is concluded.")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("data/external/raw/btf3/btf3_binary_questions_and_forecasts.parquet"),
    )
    parser.add_argument("--raw-dir", type=Path, default=Path("results/raw"))
    parser.add_argument("--out", type=Path, default=Path("results/g7_exante_anchor_analysis.json"))
    parser.add_argument(
        "--models", nargs="*", default=["qwen35-9b", "gemma3-12b", "mistral-small-24b"]
    )
    parser.add_argument("--headline-models", nargs="*", default=None,
                        help="models the panel rule applies to (default: the first three)")
    args = parser.parse_args()

    import pandas as pd

    frame = pd.read_parquet(args.source).set_index("question_id")
    anchor = {
        str(index): float(value)
        for index, value in frame[ANCHOR_COLUMN].items()
        if value == value  # not NaN
    }

    per_model = {}
    for tag in args.models:
        path = args.raw_dir / f"isr_{tag}_btf3_large_replication_v1.jsonl"
        if not path.exists():
            continue
        conditions, directions, resolutions = load_cells(path)
        result = {"source_file": str(path)}
        for frame_name, (with_c, without_c) in {
            "oob": ("oob_with", "oob_without"),
            "allowed": ("allowed_with", "allowed_without"),
        }.items():
            result[frame_name] = frame_stats(
                conditions[with_c], conditions[without_c], anchor, resolutions, directions
            )
        result["oob"]["displacement_verdict"] = verdict(result["oob"]["delta_dev"])
        result["validity_pass"] = bool(result["oob"]["rho_without"] > VALIDITY_FLOOR)
        per_model[tag] = result

    headline = args.headline_models or args.models[:3]
    counted = [per_model[t] for t in headline if t in per_model]
    tally = {
        v: sum(1 for m in counted if m["oob"]["displacement_verdict"] == v)
        for v in ("displacement", "no_displacement", "indeterminate")
    }
    panel = next((v for v, n in tally.items() if n >= MIN_MODELS), "indeterminate")
    mean_brier_delta = (
        st.mean(m["oob"]["delta_brier"]["mean"] for m in counted) if counted else float("nan")
    )
    row, sentence = interpretation(panel, mean_brier_delta)

    report = {
        "preregistration": "PREREGISTRATION_G7_EXANTE_ANCHOR.md",
        "anchor_column": ANCHOR_COLUMN,
        "source_sha256_expected": SOURCE_SHA256,
        "displacement_sesoi": DISPLACEMENT_SESOI,
        "validity_floor": VALIDITY_FLOOR,
        "per_model": per_model,
        "panel": {"headline_models": headline, "tally": tally, "panel_verdict": panel},
        "interpretation_row": row,
        "permitted_sentence": sentence,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    for tag, m in per_model.items():
        o = m["oob"]
        d, b = o["delta_dev"], o["delta_brier"]
        print(f"\n=== {tag}  (n={o['units']}, validity rho={o['rho_without']:.3f} "
              f"{'ok' if m['validity_pass'] else 'BELOW FLOOR'})")
        print(f"  |p - anchor|   without {o['mad_without']:6.2f}   with {o['mad_with']:6.2f}   "
              f"Delta_dev {d['mean']:+6.2f} [{d['ci_low']:+.2f}, {d['ci_high']:+.2f}]  "
              f"-> {o['displacement_verdict']}")
        print(f"  Brier          without {o['brier_without']:6.4f}   with {o['brier_with']:6.4f}   "
              f"Delta_brier {b['mean']:+.4f} [{b['ci_low']:+.4f}, {b['ci_high']:+.4f}]")
        print(f"  |p - 50|       without {o['confidence_without']:6.2f}   with {o['confidence_with']:6.2f}")
        print(f"  signed gap to anchor   without {o['signed_gap_without']:+6.2f}   "
              f"with {o['signed_gap_with']:+6.2f}")
        a = m["allowed"]
        print(f"  [licensed frame] Delta_dev {a['delta_dev']['mean']:+6.2f}   "
              f"Delta_brier {a['delta_brier']['mean']:+.4f}")
    print(f"\npanel: {panel}\n{sentence}")
    print(f"\nwrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
