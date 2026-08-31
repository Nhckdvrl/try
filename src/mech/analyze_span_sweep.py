"""Analyze the G6 layer-window masking sweep.

Implements PREREGISTRATION_G6_MECHANISM.md §4 exactly.

    restored_i(f) = ( p_i[mask(f)] - p_i[with] ) / ( p_i[without] - p_i[with] )
    R(f)          = mean restored_i(f) over units with |p_without - p_with| >= 5

    f* = max{ f : R(f) >= 0.5 and the 95% CI excludes 0.5 from below }

``p_with`` is the **HF unmasked** answer from the same run, not the frozen vLLM
value, so a framework difference cannot masquerade as an effect. The vLLM value
is still read, and the disagreement rate between the two is reported.

The leverage filter uses only the two frozen baseline cells; no masked output
participates in selecting units.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import statistics as st

try:
    from .. import metrics_policy_nonuse  # noqa: F401
except Exception:  # pragma: no cover - direct execution
    pass

import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

from analyze_exante_anchor import bootstrap_mean  # noqa: E402

LEVERAGE_FLOOR = 5.0
RESTORE_THRESHOLD = 0.5
ABSENT_MIDPOINT_MAX = 0.25
FRAMEWORK_TOLERANCE = 1.0
MIN_MODELS = 2
EXPECTED_MODELS = ("qwen35-9b", "gemma3-12b", "mistral-small-24b")


def load_sweep(path: Path) -> tuple[dict, list[dict]]:
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]
    metadata = next(row for row in rows if row["record_type"] == "metadata")
    return metadata, [row for row in rows if row["record_type"] != "metadata"]


def load_baseline(path: Path) -> dict[str, dict[str, float]]:
    out: dict[str, dict[str, float]] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line:
            continue
        row = json.loads(line)
        if row.get("record_type") == "decision" and row.get("value") is not None:
            out.setdefault(row["condition"], {})[row["independent_unit_id"]] = row["value"]
    return out


def analyze_model(tag: str, sweep_path: Path, baseline_path: Path) -> dict:
    metadata, rows = load_sweep(sweep_path)
    baseline = load_baseline(baseline_path)
    with_v, without_v = baseline["oob_with"], baseline["oob_without"]

    unmasked = {r["independent_unit_id"]: r["value"] for r in rows if r["record_type"] == "unmasked"}
    wrong = {r["independent_unit_id"]: r["value"] for r in rows if r["record_type"] == "wrong_span"}
    masked: dict[float, dict[str, float]] = {}
    for row in rows:
        if row["record_type"] == "masked":
            masked.setdefault(row["fraction"], {})[row["independent_unit_id"]] = row["value"]

    # framework agreement, reported not assumed
    shared = [u for u in unmasked if u in with_v and unmasked[u] is not None]
    disagreements = [u for u in shared if abs(unmasked[u] - with_v[u]) > FRAMEWORK_TOLERANCE]

    leverage = [
        u
        for u in shared
        if u in without_v and abs(without_v[u] - with_v[u]) >= LEVERAGE_FLOOR
    ]

    def restored(values: dict[str, float]) -> dict | None:
        usable = [
            u
            for u in leverage
            if values.get(u) is not None and (without_v[u] - unmasked[u]) != 0
        ]
        if not usable:
            return None
        fractions = [
            (values[u] - unmasked[u]) / (without_v[u] - unmasked[u]) for u in usable
        ]
        result = bootstrap_mean(fractions)
        result["units"] = len(usable)
        return result

    curve = {f: restored(values) for f, values in sorted(masked.items())}
    control = restored(wrong)

    qualifying = [
        f
        for f, r in curve.items()
        if r is not None and r["mean"] >= RESTORE_THRESHOLD and r["ci_low"] > RESTORE_THRESHOLD
    ]
    f_star = max(qualifying) if qualifying else None
    full = curve.get(0.0)
    midpoint = curve.get(0.5)

    if f_star is not None and f_star >= 0.5:
        row = "H-override"
    elif (
        (f_star is None or f_star <= 0.125)
        and midpoint is not None
        and midpoint["mean"] < ABSENT_MIDPOINT_MAX
    ):
        row = "H-absent"
    else:
        row = "intermediate"

    return {
        "model_tag": tag,
        "n_layers": metadata["n_layers"],
        "windows": metadata["windows"],
        "attn_implementation": metadata.get("attn_implementation"),
        "units_with_leverage": len(leverage),
        "units_total": len(unmasked),
        "framework_disagreement_rate": len(disagreements) / len(shared) if shared else None,
        "framework_disagreement_units": len(disagreements),
        "restoration_curve": {str(f): r for f, r in curve.items()},
        "wrong_span_restoration": control,
        "full_depth_restoration": full,
        "instrument_ok": bool(full is not None and full["mean"] >= RESTORE_THRESHOLD),
        "f_star": f_star,
        "row": row,
    }


PERMITTED = {
    "H-override": (
        "Masking confined to the later part of the network restores at least half the "
        "judgment, so through the earlier layers the computation had not committed to the "
        "packet: an uncontaminated trajectory exists and is overwritten late."
    ),
    "H-absent": (
        "Only near-full-depth masking restores the judgment; masking the second half does "
        "almost nothing. The packet is in the estimate from the start and there is no "
        "separate ex-ante trajectory to protect."
    ),
    "intermediate": (
        "The restoration curve is reported and no account is named: the sweep does not place "
        "f* in either preregistered region."
    ),
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-dir", type=Path, default=ROOT / "results/raw")
    parser.add_argument("--out", type=Path, default=ROOT / "results/g6_span_sweep_analysis.json")
    parser.add_argument("--models", nargs="*", default=list(EXPECTED_MODELS))
    args = parser.parse_args()

    per_model = {}
    for tag in args.models:
        sweep = args.raw_dir / f"mech_{tag}_g6_span_sweep.jsonl"
        baseline = args.raw_dir / f"isr_{tag}_btf3_large_replication_v1.jsonl"
        if not sweep.exists():
            continue
        per_model[tag] = analyze_model(tag, sweep, baseline)

    usable = [m for m in per_model.values() if m["instrument_ok"]]
    tally = {r: sum(1 for m in usable if m["row"] == r) for r in PERMITTED}
    panel = next((r for r, n in tally.items() if n >= MIN_MODELS), "intermediate")

    report = {
        "preregistration": "PREREGISTRATION_G6_MECHANISM.md",
        "leverage_floor": LEVERAGE_FLOOR,
        "restore_threshold": RESTORE_THRESHOLD,
        "per_model": per_model,
        "panel": {"tally": tally, "instrument_ok_models": len(usable), "panel_row": panel},
        "permitted_sentence": PERMITTED[panel],
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    for tag, m in per_model.items():
        print(f"\n=== {tag}  ({m['n_layers']} layers, leverage units {m['units_with_leverage']}"
              f"/{m['units_total']}, HF-vs-vLLM disagreement "
              f"{m['framework_disagreement_rate']:.3f})")
        for f, r in sorted(m["restoration_curve"].items(), key=lambda kv: float(kv[0])):
            if r is None:
                print(f"  f={f:>6s}  (no usable units)")
                continue
            print(f"  f={f:>6s}  R={r['mean']:+.3f} [{r['ci_low']:+.3f}, {r['ci_high']:+.3f}]  n={r['units']}")
        c = m["wrong_span_restoration"]
        if c:
            print(f"  wrong-span  R={c['mean']:+.3f} [{c['ci_low']:+.3f}, {c['ci_high']:+.3f}]")
        print(f"  instrument_ok={m['instrument_ok']}  f*={m['f_star']}  -> {m['row']}")
    print(f"\npanel: {panel}\n{PERMITTED[panel]}")
    print(f"\nwrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
