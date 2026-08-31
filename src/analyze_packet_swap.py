"""Analyze the G8 packet-swap round.

Implements PREREGISTRATION_G8_RELEVANCE.md §3 exactly:

    I_own   = mean_i s_i ( p_i[swap_with] - p_i[oob_without] )
    I_donor = mean_i t_i ( p_i[swap_with] - p_i[oob_without] )
    S_swap  = mean_i | p_i[swap_with] - p_i[oob_without] |
    S_real  = mean_i | p_i[oob_with]   - p_i[oob_without] |

``I_own`` is checked first: a foreign packet carries no information about this
unit's outcome, so a non-null ``I_own`` means the pairing leaked outcome
information and invalidates the round.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import statistics as st

try:
    from .analyze_exante_anchor import bootstrap_mean
except ImportError:  # direct script execution
    from analyze_exante_anchor import bootstrap_mean

SESOI = 5.0
PARSE_RATE_FLOOR = 248 / 256
BOUNDARY_FLOOR = 224 / 256
SUBSTANTIAL_FRACTION = 0.5
MIN_MODELS = 2
EXPECTED_MODELS = ("qwen35-9b", "gemma3-12b", "mistral-small-24b")


def load(path: Path) -> tuple[dict, list[dict]]:
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]
    metadata = next(row for row in rows if row["record_type"] == "metadata")
    return metadata, [row for row in rows if row["record_type"] != "metadata"]


def analyze_model(tag: str, baseline_path: Path, swap_path: Path) -> dict:
    base_meta, base_rows = load(baseline_path)
    swap_meta, swap_rows = load(swap_path)
    if base_meta["artifact_sha256"] != swap_meta["artifact_sha256"]:
        raise ValueError(f"{tag}: artifact SHA mismatch between baseline and swap")

    baseline: dict[str, dict[str, float]] = {}
    for row in base_rows:
        if row["record_type"] == "decision" and row["value"] is not None:
            baseline.setdefault(row["condition"], {})[row["independent_unit_id"]] = row["value"]

    swap_values, own_sign, donor_sign = {}, {}, {}
    for row in swap_rows:
        if row["record_type"] != "decision":
            continue
        if row["value"] is not None:
            swap_values[row["independent_unit_id"]] = row["value"]
        own_sign[row["independent_unit_id"]] = int(row["direction"])
        donor_sign[row["independent_unit_id"]] = int(row["donor_direction"])

    decisions = [r for r in swap_rows if r["record_type"] == "decision"]
    probes = [r for r in swap_rows if r["record_type"] == "boundary_probe"]
    parse_rate = sum(r["value"] is not None for r in decisions) / len(decisions)
    boundary_accuracy = sum(bool(r.get("correct")) for r in probes) / len(probes)

    units = sorted(set(swap_values) & set(baseline["oob_without"]) & set(baseline["oob_with"]))
    delta_swap = [swap_values[u] - baseline["oob_without"][u] for u in units]
    delta_real = [baseline["oob_with"][u] - baseline["oob_without"][u] for u in units]

    i_own = bootstrap_mean([own_sign[u] * d for u, d in zip(units, delta_swap)])
    i_donor = bootstrap_mean([donor_sign[u] * d for u, d in zip(units, delta_swap)])
    i_real = bootstrap_mean([own_sign[u] * d for u, d in zip(units, delta_real)])
    s_swap = bootstrap_mean([abs(d) for d in delta_swap])
    s_real = bootstrap_mean([abs(d) for d in delta_real])

    opposite = [u for u in units if own_sign[u] != donor_sign[u]]
    same = [u for u in units if own_sign[u] == donor_sign[u]]

    return {
        "model_tag": tag,
        "pairing_sha256": swap_meta["pairing_sha256"],
        "units": len(units),
        "parse_rate": parse_rate,
        "boundary_accuracy": boundary_accuracy,
        "qualified": bool(parse_rate >= PARSE_RATE_FLOOR and boundary_accuracy >= BOUNDARY_FLOOR),
        "I_own": i_own,
        "I_donor": i_donor,
        "I_real": i_real,
        "S_swap": s_swap,
        "S_real": s_real,
        "S_ratio": s_swap["mean"] / s_real["mean"] if s_real["mean"] else None,
        "pairing_direction_crosstab": {"same_direction": len(same), "opposite_direction": len(opposite)},
        "I_donor_opposite_only": (
            bootstrap_mean([donor_sign[u] * (swap_values[u] - baseline["oob_without"][u]) for u in opposite])
            if len(opposite) >= 10 else None
        ),
        "I_own_null": bool(i_own["ci_low"] >= -SESOI and i_own["ci_high"] <= SESOI),
        "I_donor_positive": bool(i_donor["mean"] >= SESOI and i_donor["ci_low"] > 0),
        "S_substantial": bool(s_swap["mean"] >= SUBSTANTIAL_FRACTION * s_real["mean"]),
    }


def interpretation(donor_positive: bool, substantial: bool) -> tuple[str, str]:
    if donor_positive:
        return (
            "H-presence-strong",
            "The model imports an unrelated question's resolution: a packet about a "
            "different question moves this judgment toward that other question's outcome.",
        )
    if substantial:
        return (
            "H-presence-weak",
            "A foreign packet moves the answer without pointing anywhere. Presence of a "
            "confident post-cutoff block perturbs the judgment even when its content "
            "cannot bear on the question.",
        )
    return (
        "H-content",
        "The effect requires the packet to be about this question. The G3 amplification "
        "pattern therefore needs an explanation that is not salience.",
    )


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-dir", type=Path, default=Path("results/raw"))
    parser.add_argument("--out", type=Path, default=Path("results/g8_packet_swap_analysis.json"))
    parser.add_argument("--models", nargs="*", default=list(EXPECTED_MODELS))
    args = parser.parse_args()

    per_model = {}
    for tag in args.models:
        baseline = args.raw_dir / f"isr_{tag}_btf3_large_replication_v1.jsonl"
        swap = args.raw_dir / f"isr_{tag}_g8_swap_with.jsonl"
        if not swap.exists():
            continue
        per_model[tag] = analyze_model(tag, baseline, swap)

    counted = [m for m in per_model.values() if m["qualified"]]
    donor_positive = sum(m["I_donor_positive"] for m in counted) >= MIN_MODELS
    substantial = sum(m["S_substantial"] for m in counted) >= MIN_MODELS
    own_null = sum(m["I_own_null"] for m in counted) >= MIN_MODELS
    row, sentence = interpretation(donor_positive, substantial)

    report = {
        "preregistration": "PREREGISTRATION_G8_RELEVANCE.md",
        "sesoi": SESOI,
        "substantial_fraction": SUBSTANTIAL_FRACTION,
        "per_model": per_model,
        "panel": {
            "qualified_models": len(counted),
            "I_own_null_models": sum(m["I_own_null"] for m in counted),
            "I_donor_positive_models": sum(m["I_donor_positive"] for m in counted),
            "S_substantial_models": sum(m["S_substantial"] for m in counted),
            "pairing_validity_ok": own_null,
        },
        "interpretation_row": row,
        "permitted_sentence": sentence,
        "validity_note": (
            "I_own must be null: a foreign packet carries no information about this unit's "
            "outcome. If it is not null the pairing leaked outcome information and the round "
            "is invalid regardless of the other numbers."
        ),
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    for tag, m in per_model.items():
        print(f"\n=== {tag} (n={m['units']}, probe={m['boundary_accuracy']:.4f}, "
              f"qualified={m['qualified']})")
        for key in ("I_own", "I_donor", "I_real", "S_swap", "S_real"):
            v = m[key]
            print(f"  {key:8s} {v['mean']:+7.2f} [{v['ci_low']:+6.2f}, {v['ci_high']:+6.2f}]")
        print(f"  S_swap / S_real = {m['S_ratio']:.3f}   "
              f"pairing {m['pairing_direction_crosstab']}")
        print(f"  I_own null={m['I_own_null']}  I_donor positive={m['I_donor_positive']}  "
              f"S substantial={m['S_substantial']}")
    print(f"\npairing validity ok: {own_null}")
    print(f"row: {row}\n{sentence}")
    print(f"\nwrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
