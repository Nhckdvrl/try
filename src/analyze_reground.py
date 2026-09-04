"""Analyze G19 ReGround.

Primary quantities are raw rating points:
- positive-target TargetError = |Y(method) - Y(base)| on same-D7 and same-D9;
- Improvement = TargetError(Semantic-Pre) - TargetError(method);
- wrong-D9 Collateral = |Y(method) - Y(naive)|;
- resolver exact-set accuracy.

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
    "idpre", "sempre", "generic", "idrestate", "gold", "self", "sanitize"
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
    p = os.path.join(ROOT, "results", "raw", f"{tag}_reground.jsonl")
    return [json.loads(l) for l in open(p)]


def analyze_tag(tag, items):
    rows = load_tag(tag)
    d = {(r["item_id"], r["method"], r["variant"]): r for r in rows}

    per = {}
    for method in METHOD_ORDER:
        err, cls = [], []
        imp, icls = [], []
        coll, ccls = [], []
        for iid, it in items.items():
            b = d.get((iid, "base", "base"), {}).get("value")
            if b is None:
                continue
            for v in POS:
                m = d.get((iid, method, v), {}).get("value")
                ref = d.get((iid, "sempre", v), {}).get("value")
                if m is not None:
                    err.append(abs(m - b))
                    cls.append(_cluster(it))
                if m is not None and ref is not None:
                    imp.append(abs(ref - b) - abs(m - b))
                    icls.append(_cluster(it))
            mw = d.get((iid, method, "wrong_d9"), {}).get("value")
            nw = d.get((iid, "naive", "wrong_d9"), {}).get("value")
            if mw is not None and nw is not None:
                coll.append(abs(mw - nw))
                ccls.append(_cluster(it))
        per[method] = dict(
            error=_boot(err, cls, 10),
            improvement=_boot(imp, icls, 11),
            collateral=_boot(coll, ccls, 12),
        )

    vs_generic, vgcls = [], []
    vs_idrest, vicls = [], []
    vs_sem, vscls = [], []
    vs_gold, vglcls = [], []
    for iid, it in items.items():
        b = d.get((iid, "base", "base"), {}).get("value")
        if b is None:
            continue
        for v in POS:
            yself = d.get((iid, "self", v), {}).get("value")
            if yself is None:
                continue
            for method, out, outcls in (
                ("semgeneric", vs_generic, vgcls),
                ("idrestate", vs_idrest, vicls),
                ("sempre", vs_sem, vscls),
                ("gold", vs_gold, vglcls),
            ):
                y = d.get((iid, method, v), {}).get("value")
                if y is not None:
                    out.append(abs(y - b) - abs(yself - b))
                    outcls.append(_cluster(it))

    self_rows = [r for r in rows if r["method"] == "self"]
    sel_acc = (
        sum(bool(r.get("selector_correct")) for r in self_rows) / len(self_rows)
        if self_rows else 0.0
    )
    fp = fn = 0
    for r in self_rows:
        pred = set(r.get("selector_pred") or [])
        gold = set(r.get("selector_expected") or [])
        fp += len(pred - gold)
        fn += len(gold - pred)

    resolver_tokens = [
        r.get("selector_prompt_tokens") for r in self_rows
        if r.get("selector_prompt_tokens") is not None
    ]
    decision_tokens = [
        r.get("n_prompt_tokens") for r in self_rows
        if r.get("n_prompt_tokens") is not None
    ]

    return dict(
        tag=tag,
        methods=per,
        self_vs_generic=_boot(vs_generic, vgcls, 21),
        self_vs_idrestate=_boot(vs_idrest, vicls, 22),
        self_vs_semantic_restate=_boot(vs_sem, vscls, 23),
        self_vs_gold=_boot(vs_gold, vglcls, 24),
        selector_accuracy=sel_acc,
        selector_false_positive_ids=fp,
        selector_false_negative_ids=fn,
        mean_selector_prompt_tokens=(st.mean(resolver_tokens) if resolver_tokens else None),
        mean_self_decision_prompt_tokens=(st.mean(decision_tokens) if decision_tokens else None),
    )


def main(tags):
    items = {x.item_id: x for x in load_items(ITEMS)}
    analyses = [analyze_tag(t, items) for t in tags]

    pooled_imp, pooled_cls = [], []
    pooled_gen, gen_cls = [], []
    pooled_coll, coll_cls = [], []\n    pooled_total_coll, total_coll_cls = [], []
    model_improvements = []
    total_correct = total_self = 0

    for a in analyses:
        m = a["methods"]["self"]["improvement"]
        model_improvements.append(None if m is None else m["mean"])

        rows = load_tag(a["tag"])
        d = {(r["item_id"], r["method"], r["variant"]): r for r in rows}
        for iid, it in items.items():
            b = d.get((iid, "base", "base"), {}).get("value")
            if b is None:
                continue
            for v in POS:
                ys = d.get((iid, "self", v), {}).get("value")
                yi = d.get((iid, "idpre", v), {}).get("value")
                yg = d.get((iid, "generic", v), {}).get("value")
                if ys is not None and yi is not None:
                    pooled_imp.append(abs(yi - b) - abs(ys - b))
                    pooled_cls.append(_cluster(it))
                if ys is not None and yg is not None:
                    pooled_gen.append(abs(yg - b) - abs(ys - b))
                    gen_cls.append(_cluster(it))
            ys = d.get((iid, "self", "wrong_d9"), {}).get("value")
            yn = d.get((iid, "naive", "wrong_d9"), {}).get("value")
            if ys is not None and yn is not None:
                pooled_coll.append(abs(ys - yn))
                coll_cls.append(_cluster(it))

        sr = [r for r in rows if r["method"] == "self"]
        total_correct += sum(bool(r.get("selector_correct")) for r in sr)
        total_self += len(sr)

    p_imp = _boot(pooled_imp, pooled_cls, 101)
    p_gen = _boot(pooled_gen, gen_cls, 102)
    p_coll = _boot(pooled_coll, coll_cls, 103)\n    p_total_coll = _boot(pooled_total_coll, total_coll_cls, 104)
    p_acc = total_correct / total_self if total_self else 0.0
    positive_models = sum(x is not None and x > 0 for x in model_improvements)

    gate1 = bool(
        p_imp and p_imp["mean"] >= 5.0 and p_imp["lo"] > 0 and positive_models >= 4
    )
    gate2 = bool(p_gen and p_gen["mean"] >= 3.0 and p_gen["lo"] > 0)
    gate3 = bool(p_acc >= 0.90 and p_coll and p_coll["mean"] <= 5.0)
    verdict = "success" if gate1 and gate2 and gate3 else (
        "partial" if gate1 else "no-benefit"
    )

    out = dict(
        preregistered_verdict=verdict,
        gates=dict(
            behavioral_rescue=gate1,
            beyond_generic_reminder=gate2,
            selective_grounding=gate3,
        ),
        pooled=dict(
            self_improvement_vs_semantic_pre=p_imp,
            self_improvement_vs_semantic_generic=p_gen,
            self_wrong_d9_added_collateral=p_coll,\n            self_wrong_d9_total_collateral=p_total_coll,
            selector_accuracy=p_acc,
            positive_models_for_improvement=positive_models,
        ),
        models=analyses,
    )

    os.makedirs(os.path.join(ROOT, "results"), exist_ok=True)
    jout = os.path.join(ROOT, "results", "reground_analysis.json")
    with open(jout, "w") as f:
        json.dump(out, f, indent=2)

    md = [
        "# G19 ReGround — method evaluation",
        "",
        f"**Frozen verdict:** {verdict}",
        "",
        "## Pooled preregistered metrics",
        "",
        "| metric | result |",
        "|---|---|",
        f"| ReGround-Self improvement vs Semantic-Pre | **{_fmt(p_imp)}** |",
        f"| ReGround-Self improvement vs Semantic-Generic | **{_fmt(p_gen)}** |",
        f"| wrong-D9 added collateral vs Semantic-Pre | **{_fmt(p_coll)}** |",\n        f"| wrong-D9 total collateral vs Naive | **{_fmt(p_total_coll)}** |",
        f"| resolver exact-set accuracy | **{p_acc:.3f}** |",
        f"| model-wise improvement positive | **{positive_models}/{len(analyses)}** |",
        "",
        "## Gates",
        "",
        f"- behavioral rescue: **{gate1}**",
        f"- beyond generic reminder: **{gate2}**",
        f"- selective grounding: **{gate3}**",
        "",
        "## Model-wise",
        "",
        "| model | self target error | self improvement vs Semantic-Pre | collateral | selector acc |",
        "|---|---:|---:|---:|---:|",
    ]
    for a in analyses:
        m = a["methods"]["self"]
        md.append(
            f"| {a['tag']} | {_fmt(m['error'])} | {_fmt(m['improvement'])} | "
            f"{_fmt(m['collateral'])} | {a['selector_accuracy']:.3f} |"
        )

    md += [
        "",
        "## Secondary comparisons",
        "",
        "| model | self beats semantic-generic | self beats ID-restatement | self beats semantic-restatement | gold minus self |",
        "|---|---:|---:|---:|---:|",
    ]
    for a in analyses:
        md.append(
            f"| {a['tag']} | {_fmt(a['self_vs_generic'])} | "
            f"{_fmt(a['self_vs_idrestate'])} | {_fmt(a['self_vs_semantic_restate'])} | "
            f"{_fmt(a['self_vs_gold'])} |"
        )

    mout = os.path.join(ROOT, "results", "reground_results.md")
    with open(mout, "w") as f:
        f.write("\n".join(md) + "\n")
    print("\n".join(md))
    print(f"\nJSON: {jout}\nMarkdown: {mout}")


if __name__ == "__main__":
    main(sys.argv[1:] or [
        "qwen3-8b",
        "gemma3-12b",
        "phi4-mini",
        "qwen3.5-27b",
        "mistral-small-24b",
    ])
