"""Analyze the G5 deliberation experiment on the frozen 256 units.

Per model, per arm ``a`` in {direct, cot, state}:

    I_a = mean_i s_i * ( p_i[a, oob, with]     - p_i[a, oob, without]     )
    R_a = mean_i s_i * ( p_i[a, allowed, with] - p_i[a, allowed, without] )

Primary contrast (the adjudication):   D = I_cot - I_state
Secondary (mitigation size):           M_a = I_direct - I_a

The utility guard is a veto: a reduction counts as mitigation only if that arm
keeps R_a >= 15.0 and R_a >= 0.7 * R_direct in the same model.

Decision rules and the interpretation table are those frozen in
PREREGISTRATION_G5_DELIBERATION.md and are applied mechanically.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import statistics as st

try:
    from .analyze_exclusion_reason import arm_effect, contrast, load
    from .metrics_policy_nonuse import paired_cluster_bootstrap_mean  # noqa: F401
except ImportError:  # direct script execution
    from analyze_exclusion_reason import arm_effect, contrast, load
    from metrics_policy_nonuse import paired_cluster_bootstrap_mean  # noqa: F401

SESOI = 5.0
PARSE_RATE_FLOOR = 248 / 256
BOUNDARY_FLOOR = 224 / 256
MIN_RESPONSIVENESS = 15.0
UTILITY_RETENTION = 0.7
MIN_MODELS = 2
EXPECTED_MODELS = ("qwen35-9b", "gemma3-12b", "mistral-small-24b")
NEW_ARMS = ("cot", "state")
ARMS = ("direct",) + NEW_ARMS
BASELINE_CONDITION = {
    ("oob", "with"): "oob_with",
    ("oob", "without"): "oob_without",
    ("allowed", "with"): "allowed_with",
    ("allowed", "without"): "allowed_without",
}


def read_condition(path: Path) -> dict:
    metadata, rows = load(path)
    decisions = [row for row in rows if row["record_type"] == "decision"]
    probes = [row for row in rows if row["record_type"] == "boundary_probe"]
    return {
        "values": {r["independent_unit_id"]: r["value"] for r in decisions if r["value"] is not None},
        "directions": {r["independent_unit_id"]: int(r.get("direction", 1)) for r in decisions},
        "parse_rate": sum(r["value"] is not None for r in decisions) / len(decisions),
        "truncated": sum(r.get("finish_reason") == "length" for r in decisions),
        "mean_completion_tokens": st.mean(r.get("n_completion_tokens", 0) for r in decisions),
        "boundary_accuracy": (
            sum(bool(r.get("correct")) for r in probes) / len(probes) if probes else None
        ),
        "artifact_sha256": metadata["artifact_sha256"],
    }


def read_baseline(path: Path) -> dict:
    metadata, rows = load(path)
    by_condition: dict[str, dict[str, float]] = {}
    totals: dict[str, list[int]] = {}
    directions: dict[str, int] = {}
    for row in rows:
        if row["record_type"] != "decision":
            continue
        totals.setdefault(row["condition"], [0, 0])
        totals[row["condition"]][1] += 1
        if row["value"] is None:
            continue
        totals[row["condition"]][0] += 1
        by_condition.setdefault(row["condition"], {})[row["independent_unit_id"]] = row["value"]
        directions[row["independent_unit_id"]] = int(row.get("direction", 1))
    probes = [r for r in rows if r["record_type"] == "boundary_probe"]
    accuracy = {
        frame: (
            sum(bool(r.get("correct")) for r in probes if r["condition"] == f"boundary_{frame}_with")
            / max(1, sum(1 for r in probes if r["condition"] == f"boundary_{frame}_with"))
        )
        for frame in ("oob", "allowed")
    }
    return {
        "conditions": by_condition,
        "directions": directions,
        "parse_rates": {c: ok / total for c, (ok, total) in totals.items()},
        "boundary_accuracy": accuracy,
        "artifact_sha256": metadata["artifact_sha256"],
    }


def analyze_model(tag: str, baseline_path: Path, raw_dir: Path) -> dict:
    baseline = read_baseline(baseline_path)
    directions = baseline["directions"]

    cells: dict[tuple[str, str, str], dict] = {}
    for arm in NEW_ARMS:
        for frame in ("oob", "allowed"):
            for cell in ("with", "without"):
                path = raw_dir / f"isr_{tag}_g5_delib_{arm}_{frame}_{cell}.jsonl"
                if not path.exists():
                    raise FileNotFoundError(path)
                cells[(arm, frame, cell)] = read_condition(path)

    shas = {baseline["artifact_sha256"]} | {c["artifact_sha256"] for c in cells.values()}
    if len(shas) != 1:
        raise ValueError(f"{tag}: artifact SHA mismatch: {shas}")

    effects: dict[str, dict[str, dict]] = {}
    quality: dict[str, dict] = {}
    for arm in ARMS:
        effects[arm] = {}
        for frame in ("oob", "allowed"):
            if arm == "direct":
                with_v = baseline["conditions"][BASELINE_CONDITION[(frame, "with")]]
                without_v = baseline["conditions"][BASELINE_CONDITION[(frame, "without")]]
            else:
                with_v = cells[(arm, frame, "with")]["values"]
                without_v = cells[(arm, frame, "without")]["values"]
            effects[arm][frame] = arm_effect(with_v, without_v, directions)
        if arm == "direct":
            quality[arm] = {
                "parse_rate": min(baseline["parse_rates"].values()),
                "boundary_accuracy_oob": baseline["boundary_accuracy"]["oob"],
                "boundary_accuracy_allowed": baseline["boundary_accuracy"]["allowed"],
                "source": "large_replication (frozen TASK block, not re-run)",
            }
        else:
            quality[arm] = {
                "parse_rate": min(
                    cells[(arm, f, c)]["parse_rate"] for f in ("oob", "allowed") for c in ("with", "without")
                ),
                "boundary_accuracy_oob": cells[(arm, "oob", "with")]["boundary_accuracy"],
                "boundary_accuracy_allowed": cells[(arm, "allowed", "with")]["boundary_accuracy"],
                "truncated": sum(
                    cells[(arm, f, c)]["truncated"] for f in ("oob", "allowed") for c in ("with", "without")
                ),
                "mean_completion_tokens": st.mean(
                    cells[(arm, f, c)]["mean_completion_tokens"]
                    for f in ("oob", "allowed")
                    for c in ("with", "without")
                ),
            }

    r_direct = effects["direct"]["allowed"]["mean"]
    qualified, utility = {}, {}
    for arm in ARMS:
        q = quality[arm]
        qualified[arm] = bool(
            q["parse_rate"] >= PARSE_RATE_FLOOR
            and q["boundary_accuracy_oob"] is not None
            and q["boundary_accuracy_oob"] >= BOUNDARY_FLOOR
            and q["boundary_accuracy_allowed"] >= BOUNDARY_FLOOR
        )
        r = effects[arm]["allowed"]["mean"]
        utility[arm] = {
            "responsiveness": r,
            "retention_vs_direct": r / r_direct if r_direct else None,
            "guard_pass": bool(r >= MIN_RESPONSIVENESS and r_direct and r >= UTILITY_RETENTION * r_direct),
        }

    primary = contrast(effects["cot"]["oob"]["per_unit"], effects["state"]["oob"]["per_unit"])
    primary["verdict"] = (
        "state_specific_benefit"
        if primary["mean"] >= SESOI and primary["ci_low"] > 0
        else "no_state_specific_benefit"
        if primary["ci_low"] >= -SESOI and primary["ci_high"] <= SESOI
        else "indeterminate"
    )
    primary["counted"] = bool(qualified["cot"] and qualified["state"])

    mitigation = {}
    for arm in NEW_ARMS:
        m = contrast(effects["direct"]["oob"]["per_unit"], effects[arm]["oob"]["per_unit"])
        m["reduces"] = bool(m["mean"] >= SESOI and m["ci_low"] > 0)
        m["counts_as_mitigation"] = bool(m["reduces"] and utility[arm]["guard_pass"])
        mitigation[arm] = m

    return {
        "model_tag": tag,
        "quality": quality,
        "qualified": qualified,
        "utility_guard": utility,
        "intrusion": {a: {k: v for k, v in effects[a]["oob"].items() if k != "per_unit"} for a in ARMS},
        "responsiveness": {a: {k: v for k, v in effects[a]["allowed"].items() if k != "per_unit"} for a in ARMS},
        "primary_contrast_cot_minus_state": primary,
        "mitigation_vs_direct": mitigation,
    }


INTERPRETATION = {
    "state_specific_benefit": (
        "H-absent supported: forcing explicit reconstruction of the ex-ante information "
        "state reduces intrusion beyond what free-form deliberation achieves. Reported "
        "together with the intrusion that remains under the scaffold."
    ),
    "no_state_specific_benefit": (
        "H-truth supported: reasoning about when a fact arrived does not remove a "
        "believed-true fact from the answer. Any reduction is generic deliberation "
        "benefit, not state construction."
    ),
    "indeterminate": "No row of the frozen table applies; the interval is reported and nothing is concluded.",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-dir", type=Path, default=Path("results/raw"))
    parser.add_argument("--out", type=Path, default=Path("results/g5_deliberation_analysis.json"))
    parser.add_argument("--models", nargs="*", default=list(EXPECTED_MODELS))
    args = parser.parse_args()

    per_model = {
        tag: analyze_model(
            tag, args.raw_dir / f"isr_{tag}_btf3_large_replication_v1.jsonl", args.raw_dir
        )
        for tag in args.models
    }

    counted = [m["primary_contrast_cot_minus_state"] for m in per_model.values() if m["primary_contrast_cot_minus_state"]["counted"]]
    tally = {v: sum(1 for c in counted if c["verdict"] == v) for v in ("state_specific_benefit", "no_state_specific_benefit", "indeterminate")}
    panel = next((v for v, n in tally.items() if n >= MIN_MODELS), "indeterminate")

    report = {
        "preregistration": "PREREGISTRATION_G5_DELIBERATION.md",
        "sesoi": SESOI,
        "per_model": per_model,
        "panel": {"tally": tally, "counted_models": len(counted), "panel_verdict": panel},
        "permitted_sentence": INTERPRETATION[panel],
        "mitigation_panel": {
            arm: {
                "n_counts_as_mitigation": sum(
                    m["mitigation_vs_direct"][arm]["counts_as_mitigation"] for m in per_model.values()
                ),
                "n_models": len(per_model),
            }
            for arm in NEW_ARMS
        },
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    for tag, m in per_model.items():
        print(f"\n=== {tag} ===")
        for arm in ARMS:
            i, r = m["intrusion"][arm], m["responsiveness"][arm]
            u, q = m["utility_guard"][arm], m["quality"][arm]
            print(
                f"  {arm:7s} I={i['mean']:7.2f} [{i['ci_low']:6.2f},{i['ci_high']:6.2f}]  "
                f"R={r['mean']:6.2f} (retain {u['retention_vs_direct']:.2f}, guard "
                f"{'ok' if u['guard_pass'] else 'FAIL'})  parse={q['parse_rate']:.4f} "
                f"probe={q['boundary_accuracy_oob']:.4f} qualified={m['qualified'][arm]}"
            )
        p = m["primary_contrast_cot_minus_state"]
        print(f"  D = I_cot - I_state = {p['mean']:.2f} [{p['ci_low']:.2f}, {p['ci_high']:.2f}] -> {p['verdict']}")
        for arm in NEW_ARMS:
            mm = m["mitigation_vs_direct"][arm]
            print(
                f"  M_{arm:5s} = {mm['mean']:7.2f} [{mm['ci_low']:6.2f},{mm['ci_high']:6.2f}] "
                f"mitigation={mm['counts_as_mitigation']}"
            )
    print(f"\npanel: {panel}\n{INTERPRETATION[panel]}")
    print(f"\nwrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
