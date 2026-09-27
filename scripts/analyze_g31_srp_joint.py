"""Analyze the frozen G31 crossed X/E2 pilot without filtering items on outcomes."""

import argparse
import hashlib
import json
import random
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ITEMS = ROOT / "data/items/g31_selected_v1.jsonl"
TAGS = ("qwen3-8b", "gemma3-12b", "mistral-small-24b")
CONDS = (("D", "none"), ("I", "irrelevant"), ("N", "support"),
         ("N", "refute"), ("A", "support"), ("A", "refute"))


def mean(xs):
    return sum(xs) / len(xs)


def interval(xs):
    ordered = sorted(xs)
    return [ordered[int(.025 * len(xs))], ordered[int(.975 * len(xs))]]


def load():
    raw_items = ITEMS.read_bytes()
    items = [json.loads(line) for line in raw_items.splitlines() if line]
    ids = [item["id"] for item in items]
    assert ids and len(ids) == len(set(ids))
    key_to_row = {}
    raw_sha = {}
    for tag in TAGS:
        path = ROOT / f"results/raw/{tag}_g31_srp_joint_v1.jsonl"
        raw = path.read_bytes()
        raw_sha[tag] = hashlib.sha256(raw).hexdigest()
        rows = [json.loads(line) for line in raw.splitlines() if line]
        assert len(rows) == 24 * len(ids), (tag, len(rows), len(ids))
        for row in rows:
            assert row["items_sha256"] == hashlib.sha256(raw_items).hexdigest()
            key = (tag, row["id"], row["condition"], row["x_role"],
                   row["e2_role"], row["mode"])
            assert key not in key_to_row
            key_to_row[key] = row
            if row["mode"] == "probability":
                assert row["value"] is not None and 0 <= row["value"] <= 100, key
            else:
                assert row["choice"] in ("TRUE", "FALSE"), key
    for tag in TAGS:
        for id_ in ids:
            for condition, x_role in CONDS:
                for e_role in ("support", "refute"):
                    for mode in ("probability", "binary"):
                        assert (tag, id_, condition, x_role, e_role, mode) in key_to_row
    return ids, raw_items, key_to_row, raw_sha


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(ROOT / "results/g31/g31_srp_joint_analysis_v1"))
    args = ap.parse_args()
    ids, raw_items, rows, raw_sha = load()
    records = []
    for tag in TAGS:
        for id_ in ids:
            def y(cond, x, e):
                return rows[tag, id_, cond, x, e, "probability"]["value"]
            def b(cond, x, e):
                return int(rows[tag, id_, cond, x, e, "binary"]["choice"] == "TRUE")
            e_roles = ("support", "refute")
            lx_d = y("D", "none", "support") - y("D", "none", "refute")
            lx_i = y("I", "irrelevant", "support") - y("I", "irrelevant", "refute")
            lx_ns = y("N", "support", "support") - y("N", "support", "refute")
            lx_nr = y("N", "refute", "support") - y("N", "refute", "refute")
            lx_as = y("A", "support", "support") - y("A", "support", "refute")
            lx_ar = y("A", "refute", "support") - y("A", "refute", "refute")
            x_n = mean([y("N", "support", e) - y("N", "refute", e) for e in e_roles])
            x_a = mean([y("A", "support", e) - y("A", "refute", e) for e in e_roles])
            rec = {
                "id": id_, "model": tag,
                "x_sep_n": x_n, "x_sep_a": x_a,
                "x_abs_n": mean([abs(y("N", "support", e) - y("N", "refute", e)) for e in e_roles]),
                "x_abs_a": mean([abs(y("A", "support", e) - y("A", "refute", e)) for e in e_roles]),
                "cre_n_d": mean([abs(y("N", x, e) - y("D", "none", e))
                                 for x in e_roles for e in e_roles]),
                "signed_n_d": mean([y("N", x, e) - y("D", "none", e)
                                   for x in e_roles for e in e_roles]),
                "abs_i_d": mean([abs(y("I", "irrelevant", e) - y("D", "none", e))
                                 for e in e_roles]),
                "abs_n_i": mean([abs(y("N", x, e) - y("I", "irrelevant", e))
                                 for x in e_roles for e in e_roles]),
                "leverage_d": lx_d, "leverage_i": lx_i,
                "leverage_ns": lx_ns, "leverage_nr": lx_nr,
                "leverage_as": lx_as, "leverage_ar": lx_ar,
                "preserve_abs_nd": mean([abs(lx_ns - lx_d), abs(lx_nr - lx_d)]),
                "preserve_signed_nd": mean([lx_ns - lx_d, lx_nr - lx_d]),
                "preserve_abs_ni": mean([abs(lx_ns - lx_i), abs(lx_nr - lx_i)]),
                "preserve_signed_ni": mean([lx_ns - lx_i, lx_nr - lx_i]),
                "x_by_e_interaction_n": lx_ns - lx_nr,
                "binary_nd_disagree": mean([int(b("N", x, e) != b("D", "none", e))
                                             for x in e_roles for e in e_roles]),
                "binary_ni_disagree": mean([int(b("N", x, e) != b("I", "irrelevant", e))
                                             for x in e_roles for e in e_roles]),
                "binary_x_disagree_n": mean([int(b("N", "support", e) != b("N", "refute", e))
                                               for e in e_roles]),
                "binary_x_disagree_a": mean([int(b("A", "support", e) != b("A", "refute", e))
                                               for e in e_roles]),
                "binary_leverage_d": b("D", "none", "support") - b("D", "none", "refute"),
                "binary_leverage_i": b("I", "irrelevant", "support") - b("I", "irrelevant", "refute"),
                "binary_leverage_n": mean([b("N", x, "support") - b("N", x, "refute")
                                            for x in e_roles]),
            }
            records.append(rec)
    metrics = [key for key in records[0] if key not in ("id", "model")]
    rng = random.Random("g31_srp_bootstrap_v1")

    def summarize(selected):
        by_id = defaultdict(list)
        for rec in selected:
            by_id[rec["id"]].append(rec)
        units = list(by_id)
        point = {k: mean([rec[k] for rec in selected]) for k in metrics}
        draws = {k: [] for k in metrics}
        for _ in range(5000):
            sampled = [rec for _ in units for rec in by_id[rng.choice(units)]]
            for key in metrics:
                draws[key].append(mean([rec[key] for rec in sampled]))
        return {"n_items": len(units), "n_model_items": len(selected),
                "mean": point, "ci95": {key: interval(draws[key]) for key in metrics}}

    summaries = {"pooled": summarize(records)}
    for tag in TAGS:
        summaries[tag] = summarize([rec for rec in records if rec["model"] == tag])
    result = {
        "status": "registered_g31_metrics", "items_path": str(ITEMS.relative_to(ROOT)),
        "items_sha256": hashlib.sha256(raw_items).hexdigest(), "raw_sha256": raw_sha,
        "summaries": summaries, "per_model_item": records,
    }
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")

    def fmt(summary, key):
        value = summary["mean"][key]
        lo, hi = summary["ci95"][key]
        return f"{value:+.2f} [{lo:+.2f},{hi:+.2f}]"

    lines = [
        "# G31 joint S/R/P pilot analysis", "",
        f"Frozen selected items: {len(ids)}. Three planned models; {24*len(ids)*len(TAGS)} complete raw outputs. "
        "Claim-cluster bootstrap, 5,000 draws. All items and rows included. This is an exploratory pilot "
        "on reused G29 natural E2 pairs and locally constructed, audited X notes.", "",
        "## Direct X suppression and paired restoration", "",
        "| Model | Active X separation A | Excluded X separation N | Absolute X effect N | N−D absolute CRE | I−D absolute frame cost | N−I absolute | Binary X disagreement A / N |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for name, s in summaries.items():
        lines.append(f"| {name} | {fmt(s,'x_sep_a')} | {fmt(s,'x_sep_n')} | "
                     f"{fmt(s,'x_abs_n')} | {fmt(s,'cre_n_d')} | "
                     f"{fmt(s,'abs_i_d')} | {fmt(s,'abs_n_i')} | "
                     f"{s['mean']['binary_x_disagree_a']:.3f} / {s['mean']['binary_x_disagree_n']:.3f} |")
    lines += [
        "", "## Valid E2 preservation", "",
        "Leverage is the support-E2 minus refute-E2 probability on the same claim. "
        "Absolute leverage differences are item-wise before averaging.", "",
        "| Model | D leverage | I leverage | N leverage, X+ | N leverage, X− | Mean absolute N−D leverage error | Mean absolute N−I leverage error | Binary leverage D / I / N |",
        "|---|---:|---:|---:|---:|---:|---:|---:|",
    ]
    for name, s in summaries.items():
        lines.append(f"| {name} | {fmt(s,'leverage_d')} | {fmt(s,'leverage_i')} | "
                     f"{fmt(s,'leverage_ns')} | {fmt(s,'leverage_nr')} | "
                     f"{fmt(s,'preserve_abs_nd')} | {fmt(s,'preserve_abs_ni')} | "
                     f"{s['mean']['binary_leverage_d']:.3f} / "
                     f"{s['mean']['binary_leverage_i']:.3f} / "
                     f"{s['mean']['binary_leverage_n']:.3f} |")
    lines += [
        "", "## Interpretation boundary", "",
        "S is supported only if the active X separation is substantial and the excluded X separation "
        "and item-wise absolute X effect are small. R uses the shorter direct D baseline, so I−D "
        "exposes some frame/length cost. P is measured by E2 response-profile differences, not a "
        "single final-score shift. Analyze each model before pooling and do not turn a model-specific "
        "regime into a cross-model law. Historical G29/G30 outcomes motivated the pilot; none of these "
        "new joint estimates is a fresh independent confirmation.", "",
    ]
    out.with_suffix(".md").write_text("\n".join(lines))
    print(out.with_suffix(".md"))


if __name__ == "__main__":
    main()
