"""Analyze the G3 exclusion-reason factorization on the frozen 256 units.

Per model, per arm ``a``, over units present in both cells of that arm:

    I_a = mean_i  s_i * ( p_i[reason_a_with] - p_i[reason_a_without] )

The ``temporal`` arm's two cells are the frozen large-replication round's own
``oob_with`` / ``oob_without``; its prompts are byte-identical (verified by
``scripts/audit_exclusion_reason.py``), so it is read rather than re-run.

Primary contrasts, paired per unit and bootstrapped over the same clusters:

    Delta_a = I_temporal - I_a          for a in {unreliable, procedural, bare}

All intervals are 95% percentile cluster bootstraps over ``question_id``,
10,000 resamples, seed 20260829 — identical to every earlier round.

Decision rules are those frozen in PREREGISTRATION_G3_EXCLUSION_REASON.md and
are applied verbatim here; the interpretation row is emitted mechanically.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import random
import statistics as st

try:
    from .metrics_policy_nonuse import paired_cluster_bootstrap_mean
except ImportError:  # direct script execution
    from metrics_policy_nonuse import paired_cluster_bootstrap_mean


SEED = 20260829
N_RESAMPLES = 10_000
PARSE_RATE_FLOOR = 248 / 256
BOUNDARY_FLOOR = 224 / 256
MIN_ALLOWED_WITH_ALIGNMENT = 70.0
SESOI = 5.0
MIN_MODELS = 2
EXPECTED_MODELS = ("qwen35-9b", "gemma3-12b", "mistral-small-24b")
NEW_ARMS = ("bare", "unreliable", "procedural")
ARMS = ("temporal",) + NEW_ARMS


def load(path: Path) -> tuple[dict, list[dict]]:
    rows = [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]
    metadata = next(row for row in rows if row["record_type"] == "metadata")
    return metadata, [row for row in rows if row["record_type"] != "metadata"]


def _cell(rows: list[dict], record_type: str) -> list[dict]:
    return [row for row in rows if row["record_type"] == record_type]


def read_arm_file(path: Path) -> dict:
    metadata, rows = load(path)
    decisions = _cell(rows, "decision")
    probes = _cell(rows, "boundary_probe")
    return {
        "model_tag": metadata["model_tag"],
        "condition": metadata["condition"],
        "arm": metadata["arm"],
        "cell": metadata["cell"],
        "artifact_sha256": metadata["artifact_sha256"],
        "reason_sentence": metadata.get("reason_sentence"),
        "values": {row["independent_unit_id"]: row["value"] for row in decisions if row["value"] is not None},
        "directions": {row["independent_unit_id"]: int(row.get("direction", 1)) for row in decisions},
        "parse_rate": sum(row["value"] is not None for row in decisions) / len(decisions),
        "boundary_accuracy": (
            sum(bool(row.get("correct")) for row in probes) / len(probes) if probes else None
        ),
        "n_probes": len(probes),
    }


def read_baseline(path: Path) -> dict:
    """The frozen large-replication round: temporal arm plus the licensed cells."""
    metadata, rows = load(path)
    by_condition: dict[str, dict[str, float]] = {}
    directions: dict[str, int] = {}
    counts: dict[str, list[int]] = {}
    for row in rows:
        if row["record_type"] == "decision":
            counts.setdefault(row["condition"], [0, 0])
            counts[row["condition"]][1] += 1
            if row["value"] is None:
                continue
            counts[row["condition"]][0] += 1
            by_condition.setdefault(row["condition"], {})[row["independent_unit_id"]] = row["value"]
            directions[row["independent_unit_id"]] = int(row.get("direction", 1))
    probes = [row for row in rows if row["record_type"] == "boundary_probe"]
    oob_probes = [row for row in probes if row["condition"] == "boundary_oob_with"]
    aligned_allowed = [
        directions[unit] * value + (0 if directions[unit] > 0 else 100)
        for unit, value in by_condition.get("allowed_with", {}).items()
    ]
    return {
        "model_tag": metadata["model_tag"],
        "artifact_sha256": metadata["artifact_sha256"],
        "conditions": by_condition,
        "directions": directions,
        "parse_rates": {c: ok / total for c, (ok, total) in counts.items()},
        "boundary_accuracy": (
            sum(bool(row.get("correct")) for row in oob_probes) / len(oob_probes) if oob_probes else None
        ),
        "allowed_with_alignment": st.mean(aligned_allowed) if aligned_allowed else None,
    }


def arm_effect(with_values: dict[str, float], without_values: dict[str, float], directions: dict[str, int]) -> dict:
    shared = sorted(set(with_values) & set(without_values) & set(directions))
    per_unit = {unit: directions[unit] * (with_values[unit] - without_values[unit]) for unit in shared}
    result = paired_cluster_bootstrap_mean(
        [per_unit[u] for u in shared], shared, n_resamples=N_RESAMPLES, seed=SEED
    )
    result["units"] = len(shared)
    result["per_unit"] = per_unit
    return result


def contrast(left: dict[str, float], right: dict[str, float]) -> dict:
    """Paired difference of two per-unit effect vectors on shared clusters."""
    shared = sorted(set(left) & set(right))
    paired = [left[u] - right[u] for u in shared]
    rng = random.Random(SEED)
    draws = []
    for _ in range(N_RESAMPLES):
        draws.append(st.mean(rng.choice(paired) for _ in paired))
    draws.sort()
    lo = max(0, int(0.025 * N_RESAMPLES))
    hi = min(N_RESAMPLES - 1, int(0.975 * N_RESAMPLES) - 1)
    return {
        "mean": st.mean(paired),
        "ci_low": draws[lo],
        "ci_high": draws[hi],
        "units": len(shared),
        "n_resamples": N_RESAMPLES,
        "seed": SEED,
    }


def verdict(delta: dict) -> str:
    """Frozen decision rule: reduction / no_reduction / indeterminate."""
    if delta["mean"] >= SESOI and delta["ci_low"] > 0:
        return "reduction"
    if delta["ci_low"] >= -SESOI and delta["ci_high"] <= SESOI:
        return "no_reduction"
    return "indeterminate"


def interpretation(unreliable: str, procedural: str) -> tuple[str, str]:
    table = {
        ("reduction", "no_reduction"): (
            "H-truth",
            "Enforcement is keyed to believed truth-value, not to licensing: the models "
            "discount evidence they are told is false, and are unmoved by being told that "
            "true evidence is not licensed. Hindsight contamination is the temporal case of "
            "that general failure.",
        ),
        ("reduction", "reduction"): (
            "H-temporal-not-refuted",
            "Licensing-based exclusion is enforceable when the stated reason is non-temporal; "
            "the temporal frame is the specific hard case.",
        ),
        ("no_reduction", "no_reduction"): (
            "H-inert",
            "No stated reason moves the effect. The packet's presence dominates every "
            "licensing rule tested here, including one that undercuts its truth.",
        ),
        ("no_reduction", "reduction"): (
            "unanticipated",
            "Not in the preregistered table. Reported descriptively; no mechanism claim and "
            "no headline change.",
        ),
    }
    return table.get(
        (unreliable, procedural),
        ("indeterminate", "At least one primary arm is indeterminate; no row of the frozen table applies."),
    )


def analyze_model(tag: str, baseline_path: Path, raw_dir: Path) -> dict:
    baseline = read_baseline(baseline_path)
    directions = baseline["directions"]

    files: dict[tuple[str, str], dict] = {}
    for arm in NEW_ARMS:
        for cell in ("with", "without"):
            path = raw_dir / f"isr_{tag}_g3_reason_{arm}_{cell}.jsonl"
            if not path.exists():
                raise FileNotFoundError(path)
            files[(arm, cell)] = read_arm_file(path)

    shas = {baseline["artifact_sha256"]} | {f["artifact_sha256"] for f in files.values()}
    if len(shas) != 1:
        raise ValueError(f"{tag}: artifact SHA mismatch across conditions: {shas}")

    arms: dict[str, dict] = {}
    quality: dict[str, dict] = {}

    temporal = arm_effect(
        baseline["conditions"]["oob_with"], baseline["conditions"]["oob_without"], directions
    )
    arms["temporal"] = temporal
    quality["temporal"] = {
        "parse_rate_with": baseline["parse_rates"].get("oob_with"),
        "parse_rate_without": baseline["parse_rates"].get("oob_without"),
        "boundary_accuracy": baseline["boundary_accuracy"],
        "source": "large_replication (byte-identical prompts, not re-run)",
    }

    for arm in NEW_ARMS:
        with_file, without_file = files[(arm, "with")], files[(arm, "without")]
        arms[arm] = arm_effect(with_file["values"], without_file["values"], directions)
        quality[arm] = {
            "parse_rate_with": with_file["parse_rate"],
            "parse_rate_without": without_file["parse_rate"],
            "boundary_accuracy": with_file["boundary_accuracy"],
            "reason_sentence": with_file["reason_sentence"],
        }

    qualified: dict[str, bool] = {}
    for arm in ARMS:
        q = quality[arm]
        qualified[arm] = bool(
            q["parse_rate_with"] is not None
            and q["parse_rate_with"] >= PARSE_RATE_FLOOR
            and q["parse_rate_without"] >= PARSE_RATE_FLOOR
            and q["boundary_accuracy"] is not None
            and q["boundary_accuracy"] >= BOUNDARY_FLOOR
            and (baseline["allowed_with_alignment"] or 0.0) >= MIN_ALLOWED_WITH_ALIGNMENT
        )

    contrasts = {}
    for arm in NEW_ARMS:
        delta = contrast(temporal["per_unit"], arms[arm]["per_unit"])
        delta["verdict"] = verdict(delta)
        delta["counted"] = bool(qualified["temporal"] and qualified[arm])
        contrasts[arm] = delta

    return {
        "model_tag": tag,
        "artifact_sha256": baseline["artifact_sha256"],
        "allowed_with_alignment": baseline["allowed_with_alignment"],
        "quality": quality,
        "qualified": qualified,
        "intrusion": {
            arm: {k: v for k, v in arms[arm].items() if k != "per_unit"} for arm in ARMS
        },
        "contrasts": contrasts,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-dir", type=Path, default=Path("results/raw"))
    parser.add_argument("--out", type=Path, default=Path("results/g3_exclusion_reason_analysis.json"))
    parser.add_argument("--models", nargs="*", default=list(EXPECTED_MODELS))
    args = parser.parse_args()

    per_model = {}
    for tag in args.models:
        baseline_path = args.raw_dir / f"isr_{tag}_btf3_large_replication_v1.jsonl"
        per_model[tag] = analyze_model(tag, baseline_path, args.raw_dir)

    panel_verdicts = {}
    for arm in NEW_ARMS:
        counted = [m["contrasts"][arm] for m in per_model.values() if m["contrasts"][arm]["counted"]]
        tally = {v: sum(1 for c in counted if c["verdict"] == v) for v in ("reduction", "no_reduction", "indeterminate")}
        panel = next((v for v, n in tally.items() if n >= MIN_MODELS), "indeterminate")
        panel_verdicts[arm] = {"tally": tally, "counted_models": len(counted), "panel_verdict": panel}

    row, sentence = interpretation(
        panel_verdicts["unreliable"]["panel_verdict"], panel_verdicts["procedural"]["panel_verdict"]
    )
    bare = panel_verdicts["bare"]["panel_verdict"]
    report = {
        "preregistration": "PREREGISTRATION_G3_EXCLUSION_REASON.md",
        "seed": SEED,
        "n_resamples": N_RESAMPLES,
        "sesoi": SESOI,
        "per_model": per_model,
        "panel": panel_verdicts,
        "interpretation_row": row,
        "permitted_sentence": sentence,
        "bare_specification_check": {
            "panel_verdict": bare,
            "caveat_required": bare == "reduction",
            "note": (
                "If the bare arm itself shows a reduction, the reason clause carries effect "
                "independent of its content and every other contrast is reported with that "
                "caveat in the same paragraph."
            ),
        },
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    for tag, model in per_model.items():
        print(f"\n=== {tag} (allowed_with alignment {model['allowed_with_alignment']:.2f}) ===")
        for arm in ARMS:
            eff = model["intrusion"][arm]
            q = model["quality"][arm]
            print(
                f"  {arm:11s} I={eff['mean']:7.2f} [{eff['ci_low']:6.2f}, {eff['ci_high']:6.2f}] "
                f"n={eff['units']:3d} probe={q['boundary_accuracy']:.4f} "
                f"parse={q['parse_rate_with']:.4f}/{q['parse_rate_without']:.4f} "
                f"qualified={model['qualified'][arm]}"
            )
        for arm in NEW_ARMS:
            c = model["contrasts"][arm]
            print(
                f"  Δ temporal−{arm:11s} {c['mean']:7.2f} [{c['ci_low']:6.2f}, {c['ci_high']:6.2f}] "
                f"-> {c['verdict']}{'' if c['counted'] else '  (not counted)'}"
            )
    print("\n=== panel ===")
    print(json.dumps(panel_verdicts, indent=2))
    print(f"\ninterpretation row: {row}\n{sentence}")
    print(f"\nwrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
