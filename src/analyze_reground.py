"""Analyze G19 ReGround under the frozen raw-point metrics.

Primary quantities:
- TargetError(method) = abs(Y_method - Y_base), pooled over same-D7/same-D9.
- Improvement(method) = TargetError(Semantic-Pre) - TargetError(method).
- AddedCollateral(method) on wrong-D9 = abs(Y_method - Y_semantic_pre).
- TotalCollateral(method) on wrong-D9 = abs(Y_method - Y_naive).
- Resolver exact-set accuracy.

No REI or leverage-normalized ratio is used.
"""
from __future__ import annotations

import json
import os
import statistics as st
import sys

sys.path.insert(0, os.path.dirname(__file__))

from schema import load_items
from analyze_png import cluster_boot

ROOT = os.path.join(os.path.dirname(__file__), "..")
ITEMS = os.path.join(ROOT, "data", "items", "g18_v1.jsonl")
POS = ("same_d7", "same_d9")
METHOD_ORDER = (
    "idpre",
    "sempre",
    "semgeneric",
    "semrestate",
    "idrestate",
    "gold",
    "self",
    "sanitize",
)


def _cluster(item):
    return item.meta.get("skeleton") or item.surface_domain or item.item_id


def _boot(vals, cls, seed=1):
    if not vals:
        return None
    m, lo, hi, p = cluster_boot(vals, cls, n=10000, seed=seed)
    return dict(mean=m, lo=lo, hi=hi, p=p, n=len(vals))


def _fmt(x):
    if x is None:
        return "—"
    return f"{x['mean']:+.2f} [{x['lo']:+.2f}, {x['hi']:+.2f}]"


def load_tag(tag):
    path = os.path.join(ROOT, "results", "raw", f"{tag}_reground.jsonl")
    return [json.loads(line) for line in open(path)]


def analyze_tag(tag, items):
    rows = load_tag(tag)
    d = {(r["item_id"], r["method"], r["variant"]): r for r in rows}

    per = {}
    for method in METHOD_ORDER:
        errors, ecls = [], []
        improvements, icls = [], []
        total_collateral, tcls = [], []
        added_collateral, acls = [], []

        for iid, item in items.items():
            base = d.get((iid, "base", "base"), {}).get("value")
            if base is None:
                continue

            for variant in POS:
                y = d.get((iid, method, variant), {}).get("value")
                y_sem = d.get((iid, "sempre", variant), {}).get("value")
                if y is not None:
                    errors.append(abs(y - base))
                    ecls.append(_cluster(item))
                if y is not None and y_sem is not None:
                    improvements.append(abs(y_sem - base) - abs(y - base))
                    icls.append(_cluster(item))

            y = d.get((iid, method, "wrong_d9"), {}).get("value")
            y_naive = d.get((iid, "naive", "wrong_d9"), {}).get("value")
            y_sem = d.get((iid, "sempre", "wrong_d9"), {}).get("value")
            if y is not None and y_naive is not None:
                total_collateral.append(abs(y - y_naive))
                tcls.append(_cluster(item))
            if y is not None and y_sem is not None:
                added_collateral.append(abs(y - y_sem))
                acls.append(_cluster(item))

        per[method] = dict(
            target_error=_boot(errors, ecls, 10),
            improvement_vs_semantic_pre=_boot(improvements, icls, 11),
            total_collateral=_boot(total_collateral, tcls, 12),
            added_collateral=_boot(added_collateral, acls, 13),
        )

    # Secondary pairwise comparisons. Positive means ReGround-Self has lower
    # positive-target error than the named baseline.
    secondary = {}
    for baseline, seed in (
        ("semgeneric", 21),
        ("semrestate", 22),
        ("idpre", 23),
        ("idrestate", 24),
        ("gold", 25),
    ):
        vals, cls = [], []
        for iid, item in items.items():
            base = d.get((iid, "base", "base"), {}).get("value")
            if base is None:
                continue
            for variant in POS:
                y_self = d.get((iid, "self", variant), {}).get("value")
                y_base = d.get((iid, baseline, variant), {}).get("value")
                if y_self is None or y_base is None:
                    continue
                vals.append(abs(y_base - base) - abs(y_self - base))
                cls.append(_cluster(item))
        secondary[baseline] = _boot(vals, cls, seed)

    self_rows = [r for r in rows if r["method"] == "self"]
    selector_accuracy = (
        sum(bool(r.get("selector_correct")) for r in self_rows) / len(self_rows)
        if self_rows else 0.0
    )
    false_positive_ids = 0
    false_negative_ids = 0
    for row in self_rows:
        pred = set(row.get("selector_pred") or [])
        expected = set(row.get("selector_expected") or [])
        false_positive_ids += len(pred - expected)
        false_negative_ids += len(expected - pred)

    resolver_tokens = [
        r.get("selector_prompt_tokens")
        for r in self_rows
        if r.get("selector_prompt_tokens") is not None
    ]
    decision_tokens = [
        r.get("n_prompt_tokens")
        for r in self_rows
        if r.get("n_prompt_tokens") is not None
    ]

    return dict(
        tag=tag,
        methods=per,
        secondary=secondary,
        selector_accuracy=selector_accuracy,
        selector_false_positive_ids=false_positive_ids,
        selector_false_negative_ids=false_negative_ids,
        mean_selector_prompt_tokens=(
            st.mean(resolver_tokens) if resolver_tokens else None
        ),
        mean_self_decision_prompt_tokens=(
            st.mean(decision_tokens) if decision_tokens else None
        ),
    )


def main(tags):
    items = {item.item_id: item for item in load_items(ITEMS)}
    analyses = [analyze_tag(tag, items) for tag in tags]

    pooled_improvement, picls = [], []
    pooled_vs_generic, pgcls = [], []
    pooled_added_collateral, pacls = [], []
    pooled_total_collateral, ptcls = [], []
    model_improvements = []
    selector_correct = selector_total = 0

    for analysis in analyses:
        model_imp = analysis["methods"]["self"]["improvement_vs_semantic_pre"]
        model_improvements.append(None if model_imp is None else model_imp["mean"])

        rows = load_tag(analysis["tag"])
        d = {(r["item_id"], r["method"], r["variant"]): r for r in rows}

        for iid, item in items.items():
            base = d.get((iid, "base", "base"), {}).get("value")
            if base is None:
                continue

            for variant in POS:
                y_self = d.get((iid, "self", variant), {}).get("value")
                y_sem = d.get((iid, "sempre", variant), {}).get("value")
                y_generic = d.get((iid, "semgeneric", variant), {}).get("value")

                if y_self is not None and y_sem is not None:
                    pooled_improvement.append(
                        abs(y_sem - base) - abs(y_self - base)
                    )
                    picls.append(_cluster(item))
                if y_self is not None and y_generic is not None:
                    pooled_vs_generic.append(
                        abs(y_generic - base) - abs(y_self - base)
                    )
                    pgcls.append(_cluster(item))

            y_self = d.get((iid, "self", "wrong_d9"), {}).get("value")
            y_sem = d.get((iid, "sempre", "wrong_d9"), {}).get("value")
            y_naive = d.get((iid, "naive", "wrong_d9"), {}).get("value")
            if y_self is not None and y_sem is not None:
                pooled_added_collateral.append(abs(y_self - y_sem))
                pacls.append(_cluster(item))
            if y_self is not None and y_naive is not None:
                pooled_total_collateral.append(abs(y_self - y_naive))
                ptcls.append(_cluster(item))

        self_rows = [r for r in rows if r["method"] == "self"]
        selector_correct += sum(bool(r.get("selector_correct")) for r in self_rows)
        selector_total += len(self_rows)

    p_imp = _boot(pooled_improvement, picls, 101)
    p_generic = _boot(pooled_vs_generic, pgcls, 102)
    p_added = _boot(pooled_added_collateral, pacls, 103)
    p_total = _boot(pooled_total_collateral, ptcls, 104)
    p_acc = selector_correct / selector_total if selector_total else 0.0

    positive_models = sum(
        x is not None and x > 0 for x in model_improvements
    )

    gate1 = bool(
        p_imp
        and p_imp["mean"] >= 3.0
        and p_imp["lo"] > 0
        and positive_models >= 4
    )
    gate2 = bool(
        p_generic and p_generic["mean"] >= 2.0 and p_generic["lo"] > 0
    )
    gate3 = bool(
        p_acc >= 0.90 and p_total and p_total["mean"] <= 5.0
    )

    verdict = (
        "success"
        if gate1 and gate2 and gate3
        else ("partial" if gate1 else "no-benefit")
    )

    result = dict(
        preregistered_verdict=verdict,
        gates=dict(
            behavioral_rescue_over_semantic_pre=gate1,
            beyond_semantic_generic_reminder=gate2,
            selective_grounding=gate3,
        ),
        pooled=dict(
            self_improvement_vs_semantic_pre=p_imp,
            self_improvement_vs_semantic_generic=p_generic,
            self_wrong_d9_added_collateral=p_added,
            self_wrong_d9_total_collateral=p_total,
            selector_accuracy=p_acc,
            positive_models_for_improvement=positive_models,
        ),
        models=analyses,
    )

    os.makedirs(os.path.join(ROOT, "results"), exist_ok=True)
    json_path = os.path.join(ROOT, "results", "reground_analysis.json")
    with open(json_path, "w") as handle:
        json.dump(result, handle, indent=2)

    md = [
        "# G19 ReGround — method evaluation",
        "",
        f"**Frozen verdict:** {verdict}",
        "",
        "## Pooled preregistered metrics",
        "",
        "| metric | result |",
        "|---|---|",
        f"| Self improvement vs Semantic-Pre | **{_fmt(p_imp)}** |",
        f"| Self improvement vs Semantic-Generic | **{_fmt(p_generic)}** |",
        f"| wrong-D9 added collateral vs Semantic-Pre | **{_fmt(p_added)}** |",
        f"| wrong-D9 total collateral vs Naive | **{_fmt(p_total)}** |",
        f"| resolver exact-set accuracy | **{p_acc:.3f}** |",
        f"| model-wise improvement positive | **{positive_models}/{len(analyses)}** |",
        "",
        "## Frozen gates",
        "",
        f"- behavioral rescue over Semantic-Pre: **{gate1}**",
        f"- beyond semantic generic reminder: **{gate2}**",
        f"- selective grounding: **{gate3}**",
        "",
        "## Model-wise ReGround-Self",
        "",
        "| model | target error | improvement vs Semantic-Pre | added collateral | total collateral | selector acc |",
        "|---|---:|---:|---:|---:|---:|",
    ]

    for analysis in analyses:
        self_m = analysis["methods"]["self"]
        md.append(
            f"| {analysis['tag']} | {_fmt(self_m['target_error'])} | "
            f"{_fmt(self_m['improvement_vs_semantic_pre'])} | "
            f"{_fmt(self_m['added_collateral'])} | "
            f"{_fmt(self_m['total_collateral'])} | "
            f"{analysis['selector_accuracy']:.3f} |"
        )

    md += [
        "",
        "## Secondary positive-target comparisons",
        "",
        "| model | vs Semantic-Generic | vs Semantic-Restate | vs ID-Pre | vs ID-Restate | Gold minus Self |",
        "|---|---:|---:|---:|---:|---:|",
    ]
    for analysis in analyses:
        sec = analysis["secondary"]
        md.append(
            f"| {analysis['tag']} | {_fmt(sec['semgeneric'])} | "
            f"{_fmt(sec['semrestate'])} | {_fmt(sec['idpre'])} | "
            f"{_fmt(sec['idrestate'])} | {_fmt(sec['gold'])} |"
        )

    md_path = os.path.join(ROOT, "results", "reground_results.md")
    with open(md_path, "w") as handle:
        handle.write("\n".join(md) + "\n")

    print("\n".join(md))
    print(f"\nJSON: {json_path}\nMarkdown: {md_path}")


if __name__ == "__main__":
    main(
        sys.argv[1:]
        or [
            "qwen3-8b",
            "gemma3-12b",
            "phi4-mini",
            "qwen3.5-27b",
            "mistral-small-24b",
        ]
    )
