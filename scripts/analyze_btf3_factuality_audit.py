#!/usr/bin/env python3
"""Score the packet factuality audit and run its secondary sensitivity check.

Reports PASS / MATERIAL_ERROR / UNVERIFIABLE counts with an exact binomial
interval on the material-error rate, applies the decision rule frozen in
PROTOCOL_BTF3_PACKET_FACTUALITY_AUDIT.md, and — clearly labelled secondary —
recomputes each model's OutOfSetIntrusion over the 256 units minus the flagged
ones.

The recomputation is descriptive robustness. It is computed after model outputs
exist, on a subsample defined by a post-output audit, and never replaces the
preregistered primary estimate.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from analyze_btf3_large_replication import THRESHOLDS, load_result, unit_scores  # noqa: E402
from information_set_metrics import compute_metrics  # noqa: E402
from metrics_policy_nonuse import paired_cluster_bootstrap_mean  # noqa: E402

SEED = 20260829
N_RESAMPLES = 10_000
_HEADING = re.compile(r"^###\s+(?:YES|NO)-\d+\.\s+`([^`]+)`\s*$")
_VERDICT = re.compile(
    r"^\s*-\s*Verdict:\s*`\[([ xX])\]\s*PASS\s*\[([ xX])\]\s*MATERIAL_ERROR\s*\[([ xX])\]\s*UNVERIFIABLE`\s*$"
)
_REASON = re.compile(r"^\s*-\s*Reason[^:]*:\s*(.*)$")


def parse_verdicts(markdown: str) -> dict[str, tuple[str, str]]:
    verdicts: dict[str, tuple[str, str]] = {}
    current: str | None = None
    lines = markdown.splitlines()
    for index, line in enumerate(lines):
        heading = _HEADING.match(line)
        if heading:
            current = heading.group(1)
            continue
        match = _VERDICT.match(line)
        if match and current is not None:
            marks = [group.strip().lower() == "x" for group in match.groups()]
            if sum(marks) != 1:
                raise ValueError(f"{current}: exactly one verdict must be ticked")
            verdict = ("PASS", "MATERIAL_ERROR", "UNVERIFIABLE")[marks.index(True)]
            reason = ""
            for follow in lines[index + 1 : index + 4]:
                found = _REASON.match(follow)
                if found:
                    reason = found.group(1).strip()
                    break
            if verdict != "PASS" and not reason:
                raise ValueError(f"{current}: {verdict} requires a one-line reason")
            verdicts[current] = (verdict, reason)
            current = None
    return verdicts


def clopper_pearson(successes: int, trials: int, alpha: float = 0.05) -> tuple[float, float]:
    from statistics import NormalDist  # noqa: F401  (kept for parity of imports)

    try:
        from scipy.stats import beta  # type: ignore
    except ImportError:
        return (float("nan"), float("nan"))
    low = 0.0 if successes == 0 else float(beta.ppf(alpha / 2, successes, trials - successes + 1))
    high = 1.0 if successes == trials else float(beta.ppf(1 - alpha / 2, successes + 1, trials - successes))
    return low, high


def intrusion(path: Path, exclude: set[str]) -> dict:
    _, rows = load_result(path)
    complete, _ = unit_scores(rows)
    kept = [(scores, unit) for scores, unit in complete if unit not in exclude]
    units = [unit for _, unit in kept]
    values = [compute_metrics(scores).out_of_set_intrusion for scores, _ in kept]
    return paired_cluster_bootstrap_mean(values, units, n_resamples=N_RESAMPLES, seed=SEED)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--verdicts", type=Path, default=Path("data/external/review/btf3_factuality_audit_v1_verdicts.md"))
    parser.add_argument("--sample", type=Path, default=Path("data/external/review/btf3_factuality_audit_v1_sample.json"))
    parser.add_argument("--results", nargs="+", type=Path, required=True, help="large-replication raw results per model")
    parser.add_argument("--out", type=Path, default=Path("results/btf3_factuality_audit_v1.json"))
    args = parser.parse_args()

    sample = json.loads(args.sample.read_text(encoding="utf-8"))
    sampled = {entry["question_id"] for rows in sample["sample"].values() for entry in rows}
    verdicts = parse_verdicts(args.verdicts.read_text(encoding="utf-8"))

    unknown = set(verdicts) - sampled
    if unknown:
        raise ValueError(f"verdicts recorded for unsampled items: {sorted(unknown)}")
    missing = sampled - set(verdicts)

    counts = {"PASS": 0, "MATERIAL_ERROR": 0, "UNVERIFIABLE": 0}
    flagged: list[dict[str, str]] = []
    for qid, (verdict, reason) in verdicts.items():
        counts[verdict] += 1
        if verdict != "PASS":
            flagged.append({"question_id": qid, "verdict": verdict, "reason": reason})

    errors = counts["MATERIAL_ERROR"]
    reviewed = len(verdicts)
    rate_low, rate_high = clopper_pearson(errors, reviewed) if reviewed else (float("nan"), float("nan"))
    if errors <= 2:
        action = "acceptable: report the audited rate; no further audit"
    elif errors <= 6:
        action = "report the rate and the leave-flagged-out sensitivity below; no membership change"
    else:
        action = "STOP: commission a full-256 external audit and report the packet-error rate as a limitation"

    excluded = {row["question_id"] for row in flagged if row["verdict"] == "MATERIAL_ERROR"}
    sensitivity = []
    for path in args.results:
        metadata, _ = load_result(path)
        sensitivity.append({
            "model_tag": metadata["model_tag"],
            "primary_all_units": intrusion(path, set()),
            "excluding_flagged_units": intrusion(path, excluded),
            "n_excluded": len(excluded),
        })

    report = {
        "protocol": "PROTOCOL_BTF3_PACKET_FACTUALITY_AUDIT.md",
        "status": "SECONDARY — descriptive robustness; the preregistered primary estimate stands",
        "sample_size": len(sampled),
        "reviewed": reviewed,
        "unreviewed": sorted(missing),
        "counts": counts,
        "material_error_rate": errors / reviewed if reviewed else None,
        "material_error_rate_95_exact_ci": [rate_low, rate_high],
        "decision_rule_action": action,
        "flagged_items": flagged,
        "sensitivity": sensitivity,
        "intrusion_sesoi_points": THRESHOLDS["intrusion_sesoi_points"],
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("counts", "material_error_rate", "decision_rule_action", "unreviewed")}, indent=2))
    for row in sensitivity:
        a, b = row["primary_all_units"], row["excluding_flagged_units"]
        print(f'{row["model_tag"]:20s} I={a["mean"]:.2f} [{a["ci_low"]:.2f},{a["ci_high"]:.2f}] -> '
              f'excl {len(excluded)}: {b["mean"]:.2f} [{b["ci_low"]:.2f},{b["ci_high"]:.2f}]')
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
