"""Analyze the G4 breadth panel on the frozen 256 units.

Estimands, qualification thresholds, and inference are inherited from
``analyze_btf3_large_replication`` without modification; this module only adds
the panel-level quantities preregistered in
PREREGISTRATION_G4_MODEL_BREADTH.md §5:

* prevalence — qualified checkpoints passing the inherited ``intrusion_pass``
  rule (95% CI lower bound strictly above the 5.0-point SESOI);
* the dissociation statistic — Spearman rank correlation between boundary-probe
  accuracy and intrusion across qualified checkpoints, with a permutation
  interval;
* intrusion by family and by parameter count, as a table. No slope is fitted.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import random
import statistics as st

try:
    from .analyze_btf3_large_replication import analyze_one
except ImportError:  # direct script execution
    from analyze_btf3_large_replication import analyze_one

SEED = 20260829
N_PERM = 10_000
SESOI = 5.0
ARTIFACT_SHA = "0b6fd8d0304f6b7cde336a6518b1058983a9b93529e90cbb577d1878acf0901d"


def rank(values: list[float]) -> list[float]:
    order = sorted(range(len(values)), key=lambda i: values[i])
    ranks = [0.0] * len(values)
    i = 0
    while i < len(order):
        j = i
        while j + 1 < len(order) and values[order[j + 1]] == values[order[i]]:
            j += 1
        shared = (i + j) / 2 + 1
        for k in range(i, j + 1):
            ranks[order[k]] = shared
        i = j + 1
    return ranks


def pearson(xs: list[float], ys: list[float]) -> float:
    n = len(xs)
    if n < 3:
        return float("nan")
    mx, my = st.mean(xs), st.mean(ys)
    num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
    dx = sum((x - mx) ** 2 for x in xs) ** 0.5
    dy = sum((y - my) ** 2 for y in ys) ** 0.5
    return num / (dx * dy) if dx and dy else float("nan")


def spearman_with_permutation(xs: list[float], ys: list[float]) -> dict:
    rho = pearson(rank(xs), rank(ys))
    rng = random.Random(SEED)
    shuffled = list(ys)
    draws = []
    for _ in range(N_PERM):
        rng.shuffle(shuffled)
        draws.append(pearson(rank(xs), rank(shuffled)))
    draws.sort()
    more_extreme = sum(1 for d in draws if abs(d) >= abs(rho))
    lo = draws[int(0.025 * N_PERM)]
    hi = draws[min(N_PERM - 1, int(0.975 * N_PERM) - 1)]
    return {
        "spearman_rho": rho,
        "permutation_p_two_sided": (more_extreme + 1) / (N_PERM + 1),
        "null_ci_low": lo,
        "null_ci_high": hi,
        "n_checkpoints": len(xs),
        "n_permutations": N_PERM,
        "seed": SEED,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--panel", type=Path, default=Path("data/model_panel_g4.json"))
    parser.add_argument("--raw-dir", type=Path, default=Path("results/raw"))
    parser.add_argument("--out", type=Path, default=Path("results/g4_model_breadth_analysis.json"))
    args = parser.parse_args()

    panel = json.loads(args.panel.read_text(encoding="utf-8"))
    per_model: dict[str, dict] = {}
    missing: list[str] = []

    for entry in panel["checkpoints"]:
        tag = entry["tag"]
        path = args.raw_dir / f"isr_{tag}_btf3_large_replication_v1.jsonl"
        if not path.exists():
            missing.append(tag)
            continue
        try:
            result = analyze_one(path, expected_artifact_sha256=ARTIFACT_SHA)
        except Exception as exc:  # a checkpoint is never silently dropped
            per_model[tag] = {**entry, "error": f"{type(exc).__name__}: {exc}"}
            continue
        per_model[tag] = {**entry, "source_file": str(path), **result}

    qualified = {
        tag: m
        for tag, m in per_model.items()
        if m.get("qualified") and "error" not in m
    }
    # intrusion_pass is inherited verbatim from the large-replication analyzer
    # (ci_low > SESOI); it is not redefined here.
    prevalent = {tag: m for tag, m in qualified.items() if m["intrusion_pass"]}

    tags = sorted(qualified)
    dissociation = (
        spearman_with_permutation(
            [qualified[t]["boundary_accuracy"] for t in tags],
            [qualified[t]["metrics"]["out_of_set_intrusion"]["mean"] for t in tags],
        )
        if len(tags) >= 3
        else {"note": "fewer than 3 qualified checkpoints"}
    )

    by_family: dict[str, list[float]] = {}
    for tag in tags:
        by_family.setdefault(qualified[tag]["family"], []).append(
            qualified[tag]["metrics"]["out_of_set_intrusion"]["mean"]
        )

    report = {
        "preregistration": "PREREGISTRATION_G4_MODEL_BREADTH.md",
        "artifact_sha256": ARTIFACT_SHA,
        "panel_size": len(panel["checkpoints"]),
        "analyzed": len(per_model),
        "missing_output": missing,
        "errors": {t: m["error"] for t, m in per_model.items() if "error" in m},
        "qualified": sorted(qualified),
        "unqualified": sorted(set(per_model) - set(qualified) - set(report_errors(per_model))),
        "prevalence": {
            "n_qualified": len(qualified),
            "n_intrusion_pass": len(prevalent),
            "tags": sorted(prevalent),
        },
        "dissociation_recognition_vs_intrusion": dissociation,
        "boundary_accuracy_range": (
            [min(qualified[t]["boundary_accuracy"] for t in tags),
             max(qualified[t]["boundary_accuracy"] for t in tags)]
            if tags else None
        ),
        "intrusion_range": (
            [min(qualified[t]["metrics"]["out_of_set_intrusion"]["mean"] for t in tags),
             max(qualified[t]["metrics"]["out_of_set_intrusion"]["mean"] for t in tags)]
            if tags else None
        ),
        "by_family": {
            fam: {"n": len(vals), "min": min(vals), "max": max(vals), "mean": st.mean(vals)}
            for fam, vals in sorted(by_family.items())
        },
        "per_model": per_model,
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    print(f"{'tag':18s} {'params':>6s} {'parse':>7s} {'probe':>7s} {'resp':>7s} {'intrusion':>22s}  qual")
    for entry in panel["checkpoints"]:
        tag = entry["tag"]
        m = per_model.get(tag)
        if m is None:
            print(f"{tag:18s} {entry['params_b']:6.1f}   (no output)")
            continue
        if "error" in m:
            print(f"{tag:18s} {entry['params_b']:6.1f}   ERROR {m['error'][:60]}")
            continue
        i = m["metrics"]["out_of_set_intrusion"]
        r = m["metrics"]["responsiveness"]
        print(
            f"{tag:18s} {entry['params_b']:6.1f} {m['decision_parse_rate']:7.4f} {m['boundary_accuracy']:7.4f} "
            f"{r['mean']:7.2f} {i['mean']:8.2f} [{i['ci_low']:6.2f},{i['ci_high']:6.2f}]  "
            f"{'yes' if m['qualified'] else 'NO'}"
        )
    print(f"\nprevalence: {len(prevalent)}/{len(qualified)} qualified checkpoints")
    print(f"dissociation: {json.dumps(dissociation)}")
    print(f"\nwrote {args.out}")
    return 0


def report_errors(per_model: dict) -> dict:
    return {t: m for t, m in per_model.items() if "error" in m}


if __name__ == "__main__":
    raise SystemExit(main())
