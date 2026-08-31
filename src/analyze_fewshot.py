"""Analyze the G10 few-shot round.

    I_fewshot = mean_i s_i ( p_i[fewshot_with] - p_i[fewshot_without] )
    M         = I_temporal - I_fewshot          (paired, same units)

Works if M >= 5.0 with a 95% CI excluding 0, in >= 2 of 3 qualified models.

Copying guard: a reduction accompanied by a low correlation between
``p[fewshot_without]`` and the frozen ``p[oob_without]`` means the model is
reproducing the demonstrated numbers rather than reasoning, and is reported as
such rather than as a fix.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path

try:
    from .analyze_exclusion_reason import arm_effect, contrast, load
    from .analyze_model_breadth import pearson, rank
except ImportError:  # direct script execution
    from analyze_exclusion_reason import arm_effect, contrast, load
    from analyze_model_breadth import pearson, rank

SESOI = 5.0
PARSE_RATE_FLOOR = 248 / 256
BOUNDARY_FLOOR = 224 / 256
COPY_CORRELATION_FLOOR = 0.5
MIN_MODELS = 2
EXPECTED_MODELS = ("qwen35-9b", "gemma3-12b", "mistral-small-24b")


def read_cell(path: Path) -> dict:
    metadata, rows = load(path)
    decisions = [r for r in rows if r["record_type"] == "decision"]
    probes = [r for r in rows if r["record_type"] == "boundary_probe"]
    return {
        "values": {r["independent_unit_id"]: r["value"] for r in decisions if r["value"] is not None},
        "directions": {r["independent_unit_id"]: int(r.get("direction", 1)) for r in decisions},
        "parse_rate": sum(r["value"] is not None for r in decisions) / len(decisions),
        "boundary_accuracy": (
            sum(bool(r.get("correct")) for r in probes) / len(probes) if probes else None
        ),
        "prefix_sha256": metadata.get("prefix_sha256"),
        "demonstration_ids": metadata.get("demonstration_ids"),
        "demonstration_answers": metadata.get("demonstration_answers"),
        "artifact_sha256": metadata["artifact_sha256"],
    }


def read_baseline(path: Path) -> tuple[dict[str, dict[str, float]], dict[str, int]]:
    _, rows = load(path)
    by_condition: dict[str, dict[str, float]] = {}
    directions: dict[str, int] = {}
    for row in rows:
        if row["record_type"] == "decision" and row["value"] is not None:
            by_condition.setdefault(row["condition"], {})[row["independent_unit_id"]] = row["value"]
            directions[row["independent_unit_id"]] = int(row.get("direction", 1))
    return by_condition, directions


def analyze_model(tag: str, baseline_path: Path, raw_dir: Path) -> dict:
    baseline, directions = read_baseline(baseline_path)
    with_cell = read_cell(raw_dir / f"isr_{tag}_g10_fewshot_with.jsonl")
    without_cell = read_cell(raw_dir / f"isr_{tag}_g10_fewshot_without.jsonl")
    if {with_cell["artifact_sha256"], without_cell["artifact_sha256"]} != {
        with_cell["artifact_sha256"]
    }:
        raise ValueError(f"{tag}: artifact SHA mismatch between few-shot cells")

    temporal = arm_effect(baseline["oob_with"], baseline["oob_without"], directions)
    fewshot = arm_effect(with_cell["values"], without_cell["values"], directions)
    reduction = contrast(temporal["per_unit"], fewshot["per_unit"])

    shared = sorted(set(without_cell["values"]) & set(baseline["oob_without"]))
    copy_rho = pearson(
        rank([without_cell["values"][u] for u in shared]),
        rank([baseline["oob_without"][u] for u in shared]),
    )

    qualified = bool(
        with_cell["parse_rate"] >= PARSE_RATE_FLOOR
        and without_cell["parse_rate"] >= PARSE_RATE_FLOOR
        and with_cell["boundary_accuracy"] is not None
        and with_cell["boundary_accuracy"] >= BOUNDARY_FLOOR
    )
    works = bool(reduction["mean"] >= SESOI and reduction["ci_low"] > 0)
    inert = bool(reduction["ci_low"] >= -SESOI and reduction["ci_high"] <= SESOI)

    return {
        "model_tag": tag,
        "prefix_sha256": with_cell["prefix_sha256"],
        "demonstration_ids": with_cell["demonstration_ids"],
        "demonstration_answers": with_cell["demonstration_answers"],
        "parse_rate_with": with_cell["parse_rate"],
        "parse_rate_without": without_cell["parse_rate"],
        "boundary_accuracy": with_cell["boundary_accuracy"],
        "qualified": qualified,
        "I_temporal": {k: v for k, v in temporal.items() if k != "per_unit"},
        "I_fewshot": {k: v for k, v in fewshot.items() if k != "per_unit"},
        "M": reduction,
        "verdict": "works" if works else "does_not_work" if inert else "indeterminate",
        "copy_correlation": copy_rho,
        "copying_suspected": bool(works and copy_rho < COPY_CORRELATION_FLOOR),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-dir", type=Path, default=Path("results/raw"))
    parser.add_argument("--out", type=Path, default=Path("results/g10_fewshot_analysis.json"))
    parser.add_argument("--models", nargs="*", default=list(EXPECTED_MODELS))
    args = parser.parse_args()

    per_model = {}
    for tag in args.models:
        path = args.raw_dir / f"isr_{tag}_g10_fewshot_with.jsonl"
        if not path.exists():
            continue
        per_model[tag] = analyze_model(
            tag, args.raw_dir / f"isr_{tag}_btf3_large_replication_v1.jsonl", args.raw_dir
        )

    counted = [m for m in per_model.values() if m["qualified"]]
    tally = {
        v: sum(1 for m in counted if m["verdict"] == v)
        for v in ("works", "does_not_work", "indeterminate")
    }
    panel = next((v for v, n in tally.items() if n >= MIN_MODELS), "indeterminate")
    sentence = {
        "works": "Worked demonstrations of correct ex-ante reasoning reduce hindsight "
                 "contamination — a cheap prompt-level fix that stating the rule does not buy.",
        "does_not_work": "Worked demonstrations do not reduce it either. Together with G3, "
                         "nothing that can be said to the model works.",
        "indeterminate": "The interval does not place the demonstrations on either side of "
                         "the frozen threshold.",
    }[panel]

    report = {
        "preregistration": "PREREGISTRATION_G10_FEWSHOT.md",
        "sesoi": SESOI,
        "per_model": per_model,
        "panel": {"tally": tally, "qualified_models": len(counted), "panel_verdict": panel},
        "permitted_sentence": sentence,
        "copying_suspected_models": [t for t, m in per_model.items() if m["copying_suspected"]],
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    for tag, m in per_model.items():
        t, f, r = m["I_temporal"], m["I_fewshot"], m["M"]
        print(f"\n=== {tag} (probe {m['boundary_accuracy']:.4f}, qualified {m['qualified']})")
        print(f"  I_temporal {t['mean']:7.2f} [{t['ci_low']:6.2f},{t['ci_high']:6.2f}]")
        print(f"  I_fewshot  {f['mean']:7.2f} [{f['ci_low']:6.2f},{f['ci_high']:6.2f}]")
        print(f"  M          {r['mean']:+7.2f} [{r['ci_low']:+6.2f},{r['ci_high']:+6.2f}] -> {m['verdict']}")
        print(f"  copy-check rho(fewshot_without, oob_without) = {m['copy_correlation']:.3f}"
              f"{'   COPYING SUSPECTED' if m['copying_suspected'] else ''}")
    print(f"\npanel: {panel}\n{sentence}")
    print(f"\nwrote {args.out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
