"""Post hoc factorial diagnostic of G30, computed directly from frozen raw rows."""

import hashlib
import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "results/g30/g30_manifest_v1.json"
OUT = ROOT / "results/g30/g30_factorial_diagnostic_v1"
CONDS = ("D", "N", "I", "R")
RELS = (0.65, 0.75, 0.85, 0.95)


def mean(values):
    return sum(values) / len(values)


def load():
    manifest = json.loads(MANIFEST.read_text())
    item_path = ROOT / manifest["items"]["path"]
    assert hashlib.sha256(item_path.read_bytes()).hexdigest() == manifest["items"]["sha256"]
    items = {x["id"]: x for x in map(json.loads, item_path.read_text().splitlines())}
    assert len(items) == 40
    all_rows = {}
    for tag, info in manifest["models"].items():
        raw = ROOT / "results/raw" / f"{tag}_g30_bayesian_status_v1.jsonl"
        assert hashlib.sha256(raw.read_bytes()).hexdigest() == info["sha256"]
        rows = [json.loads(line) for line in raw.read_text().splitlines()]
        assert len(rows) == 160
        for row in rows:
            key = tag, row["id"], row["condition"]
            assert key not in all_rows
            assert row["probability_blue"] is not None
            assert row["items_sha256"] == manifest["items"]["sha256"]
            all_rows[key] = row
    assert len(all_rows) == 480
    return items, all_rows, manifest


def main():
    items, rows, manifest = load()
    tags = tuple(manifest["models"])
    records = []
    for tag in tags:
        for id_, item in items.items():
            prior = 100 * item["prior_blue"]
            complement = 100 - prior
            sign = 1 if item["e1_report"] == "Blue" else -1
            rec = {"model": tag, "id": id_, "prior": prior,
                   "reliability": item["reliability"], "e2": item["e2_report"],
                   "bayes": item["bayes_p_blue_after_e2_pct"]}
            for c in CONDS:
                value = rows[tag, id_, c]["probability_blue"]
                rec[f"p_{c}"] = value
                rec[f"copy_prior_{c}"] = abs(value - prior) < 0.01
                rec[f"prior_or_complement_{c}"] = min(abs(value - prior), abs(value - complement)) < 0.01
            rec["signed_RN"] = sign * (rec["p_R"] - rec["p_N"])
            rec["signed_NI"] = sign * (rec["p_N"] - rec["p_I"])
            records.append(rec)

    by_model = {}
    for tag in tags:
        rr = [r for r in records if r["model"] == tag]
        assert len(rr) == 40
        summary = {"n": 40, "copy_prior": {}, "prior_or_complement": {},
                   "constant_across_reliability_groups": {}, "mean_reliability_range": {},
                   "by_reliability": {}}
        for c in CONDS:
            summary["copy_prior"][c] = sum(r[f"copy_prior_{c}"] for r in rr)
            summary["prior_or_complement"][c] = sum(r[f"prior_or_complement_{c}"] for r in rr)
            groups = defaultdict(list)
            for r in rr:
                groups[r["prior"], r["e2"]].append(r[f"p_{c}"])
            assert len(groups) == 10 and all(len(v) == 4 for v in groups.values())
            ranges = [max(v) - min(v) for v in groups.values()]
            summary["constant_across_reliability_groups"][c] = sum(x < 0.01 for x in ranges)
            summary["mean_reliability_range"][c] = mean(ranges)
        for rel in RELS:
            subset = [r for r in rr if r["reliability"] == rel]
            assert len(subset) == 10
            pairs = defaultdict(dict)
            for r in subset:
                pairs[r["prior"]][r["e2"]] = r
            assert len(pairs) == 5 and all(set(p) == {"Blue", "Yellow"} for p in pairs.values())
            summary["by_reliability"][str(rel)] = {
                "signed_RN": mean([r["signed_RN"] for r in subset]),
                "signed_NI": mean([r["signed_NI"] for r in subset]),
                "e2_separation": {
                    c: mean([p["Blue"][f"p_{c}"] - p["Yellow"][f"p_{c}"] for p in pairs.values()])
                    for c in CONDS
                },
                "bayes_e2_separation": mean([p["Blue"]["bayes"] - p["Yellow"]["bayes"]
                                            for p in pairs.values()]),
            }
        by_model[tag] = summary

    result = {"status": "post_hoc_diagnostic", "source_manifest": str(MANIFEST.relative_to(ROOT)),
              "models": by_model}
    OUT.with_suffix(".json").write_text(json.dumps(result, indent=2) + "\n")
    lines = ["# G30 factorial diagnostic: the pooled R−N mean is misleading", "",
             "Post hoc read of all 480 frozen raw outputs. This report adds no model inference, "
             "sample exclusion, or revised registration. Source hashes are checked against "
             "the [G30 manifest](g30_manifest_v1.json).", "",
             "## Prior and reliability responses", "",
             "Exact copy uses a tolerance of 0.01 percentage points. Each model has 40 cells; "
             "each prior × E2 group has four reliability levels.", "",
             "| Model | R exactly prior | R prior or complement | R constant across reliability | N constant across reliability | Mean R range across reliability |",
             "|---|---:|---:|---:|---:|---:|"]
    for tag in tags:
        x = by_model[tag]
        lines.append(f"| {tag} | {x['copy_prior']['R']}/40 | "
                     f"{x['prior_or_complement']['R']}/40 | "
                     f"{x['constant_across_reliability_groups']['R']}/10 | "
                     f"{x['constant_across_reliability_groups']['N']}/10 | "
                     f"{x['mean_reliability_range']['R']:.2f} pp |")
    lines += ["", "## Valid E2 uptake by reliability", "",
              "Each E2 separation is mean P(Blue | Blue report) minus P(Blue | Yellow report), "
              "matched on prior and reliability. The Bayesian column is the normative separation.", "",
              "| Model | Reliability | Bayes E2 sep | D | N | I | R | Signed R−N | Signed N−I |",
              "|---|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for tag in tags:
        for rel in RELS:
            x = by_model[tag]["by_reliability"][str(rel)]
            e = x["e2_separation"]
            lines.append(f"| {tag} | {rel:.2f} | {x['bayes_e2_separation']:.2f} | "
                         f"{e['D']:.2f} | {e['N']:.2f} | {e['I']:.2f} | {e['R']:.2f} | "
                         f"{x['signed_RN']:+.2f} | {x['signed_NI']:+.2f} |")
    lines += ["", "## Interpretation", "",
              "Gemma's R forecast is exactly the prior in 32/40 cells and either the prior or its "
              "complement in 40/40. Its R forecast is constant across all four reliability levels "
              "for every one of the ten prior × E2 groups. The R condition therefore places Gemma "
              "in a discrete prior-based response mode on this prompt. Its large signed R−N should "
              "not be read as a clean graded effect of revoked E1 content. Qwen and Mistral show "
              "different, smaller patterns. The pooled +6.38 pp hides these regimes.", "",
              "The four reliability cells within each prior × E2 group share nearly identical "
              "wording, so this is a controlled within-prompt diagnostic. It does not establish an "
              "internal mechanism; the rendered R history is longer than N and could alter prompt "
              "processing. The stable ConfB suppression–restoration result is unaffected.", ""]
    OUT.with_suffix(".md").write_text("\n".join(lines))
    print(OUT.with_suffix(".md"))


if __name__ == "__main__":
    main()
