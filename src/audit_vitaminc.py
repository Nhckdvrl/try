#!/usr/bin/env python3
"""Zero-model VitaminC triplet audit.

Answers exactly one question, against the criteria pre-registered BEFORE the
download in results/audits/vitaminc_triplet_audit_criteria_v1.md:

    Can the real-revision subset furnish enough clean natural contrastive
    triplets  Y+ (supporting evidence) <-> Y0 (claim alone) <-> Y- (opposing)?

No model calls, no prompts, no effect peeking: a pure row census over the
pinned official release (data/external/raw/vitaminc/*.jsonl, SHA-256 verified
by scripts/fetch_external_sources.py).

Run with the repository's existing environment:
  /home/xiang/miniconda3/envs/fgvd/bin/python src/audit_vitaminc.py
"""
from __future__ import annotations

import argparse
from collections import Counter, defaultdict
import difflib
import hashlib
import json
from pathlib import Path
import re


LABELS = ("SUPPORTS", "REFUTES", "NOT ENOUGH INFO")
SPLITS = ("train", "dev", "test")
# Volume bands (criteria B).
N_SR_KILL = 300
N_SR_CLEAN = 1000
# Minimality bands (criteria C).
SIM_MARGINAL = 0.80
SIM_CLEAN = 0.90
# Purity bands (criteria A).
MAX_MALFORMED_RATE = 0.05
MAX_FEVER_LEAK_KILL = 0.01
# Exact templating regex used for D4 (printed in the report for transparency).
TEMPLATE_RE = re.compile(
    r"(less than|more than|fewer than|over|under|at least|at most)\b[^.]{0,20}\d",
    re.IGNORECASE,
)


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_split(path: Path, split: str):
    """One pass: purity-filter real rows and group them by (case_id, claim)."""
    revision_types = Counter()
    n_rows = 0
    n_real = 0
    malformed = Counter()
    kept = 0
    fever_leak = 0
    groups = defaultdict(list)          # (case_id, claim) -> [(label, evidence)]
    cases = defaultdict(
        lambda: {"rows": 0, "evidence": set(), "claims": set(), "page": None}
    )
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            line = line.rstrip("\n")
            if not line:
                continue
            row = json.loads(line)
            n_rows += 1
            revision_types[str(row.get("revision_type"))] += 1
            if row.get("revision_type") != "real":
                continue
            n_real += 1
            label = row.get("label")
            claim = row.get("claim") or ""
            evidence = row.get("evidence") or ""
            if label not in LABELS:
                malformed["label_out_of_set"] += 1
                continue
            if not claim:
                malformed["empty_claim"] += 1
                continue
            if not evidence:
                malformed["empty_evidence"] += 1
                continue
            kept += 1
            if row.get("FEVER_id"):
                fever_leak += 1
            case_id = str(row.get("case_id"))
            groups[(case_id, claim)].append((label, evidence))
            case = cases[case_id]
            case["rows"] += 1
            case["evidence"].add(evidence)
            case["claims"].add(claim)
            if case["page"] is None:
                case["page"] = str(row.get("page"))
    return {
        "split": split,
        "path": str(path),
        "n_rows": n_rows,
        "n_real": n_real,
        "revision_types": dict(revision_types),
        "malformed": dict(malformed),
        "n_malformed": sum(malformed.values()),
        "kept": kept,
        "fever_leak": fever_leak,
        "groups": groups,
        "cases": cases,
    }


def token_similarity(a: str, b: str) -> float:
    """difflib ratio over whitespace-tokenized texts (criteria C, no autojunk)."""
    return difflib.SequenceMatcher(None, a.split(), b.split(), autojunk=False).ratio()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default="data/external/raw/vitaminc")
    parser.add_argument("--out", default="results/audits/vitaminc_triplet_audit_v1.json")
    parser.add_argument("--md", default="results/audits/vitaminc_triplet_audit_v1.md")
    args = parser.parse_args()
    root = Path(args.root)

    # ---- pass 1: per-split purity + grouping ------------------------------
    splits = {}
    for split in SPLITS:
        path = root / f"{split}.jsonl"
        if not path.exists():
            raise SystemExit(f"missing {path}; run scripts/fetch_external_sources.py")
        splits[split] = load_split(path, split)

    total_rows = sum(s["n_rows"] for s in splits.values())
    total_real = sum(s["n_real"] for s in splits.values())
    total_malformed = sum(s["n_malformed"] for s in splits.values())
    total_kept = sum(s["kept"] for s in splits.values())
    total_fever = sum(s["fever_leak"] for s in splits.values())
    malformed_rate = total_malformed / total_real if total_real else 1.0
    fever_rate = total_fever / total_kept if total_kept else 1.0

    # ---- pass 2: merge splits (record any case straddling two splits) -----
    groups = defaultdict(list)
    cases = {}
    straddled = 0
    split_of_case = {}
    for split in SPLITS:
        for key, rows in splits[split]["groups"].items():
            groups[key].extend(rows)
        for case_id, info in splits[split]["cases"].items():
            if case_id in cases:
                straddled += 1
                prev = cases[case_id]
                prev["rows"] += info["rows"]
                prev["evidence"] |= info["evidence"]
                prev["claims"] |= info["claims"]
            else:
                cases[case_id] = dict(info)
                split_of_case[case_id] = split

    label_marginal = Counter(label for rows in groups.values() for label, _ in rows)
    group_size = Counter(len(rows) for rows in groups.values())
    n_ev_per_group = Counter(len({ev for _, ev in rows}) for rows in groups.values())

    # ---- SR-pairs ----------------------------------------------------------
    # Criteria B: a group is an SR-pair iff some SUPPORTS row and some REFUTES
    # row carry different evidence texts. Canonical shape = exactly 1S+1R.
    sr_pairs = {}            # (case_id, claim) -> {"s","r","multi"}
    anomalous_multi = 0
    same_text_contradictions = 0
    for (case_id, claim), rows in groups.items():
        s_texts = sorted({ev for label, ev in rows if label == "SUPPORTS"})
        r_texts = sorted({ev for label, ev in rows if label == "REFUTES"})
        if not s_texts or not r_texts:
            continue
        combo = next(
            ((s, r) for s in s_texts for r in r_texts if s != r), None
        )
        if combo is None:
            # SUPPORTS and REFUTES rows share the identical evidence text:
            # not a natural contrast (label contradiction inside the data).
            same_text_contradictions += 1
            continue
        canonical = len(s_texts) == 1 and len(r_texts) == 1
        sr_pairs[(case_id, claim)] = {"s": combo[0], "r": combo[1], "multi": not canonical}
        if not canonical:
            anomalous_multi += 1

    sr_by_split = Counter(split_of_case[case_id] for (case_id, _) in sr_pairs)
    n_sr = len(sr_pairs)
    canonical = [v for v in sr_pairs.values() if not v["multi"]]

    # ---- criteria C: minimality over canonical SR-pairs -------------------
    sims = sorted(token_similarity(v["s"], v["r"]) for v in canonical)
    if sims:
        if len(sims) % 2:
            median_sim = sims[len(sims) // 2]
        else:
            median_sim = (sims[len(sims) // 2 - 1] + sims[len(sims) // 2]) / 2
        p10_sim = sims[max(0, len(sims) // 10 - 1)]
        min_sim = sims[0]
        max_sim = sims[-1]
    else:
        median_sim = p10_sim = min_sim = max_sim = None

    # ---- D3/D4/D5 structure stats ----------------------------------------
    claims_sr = [claim for (_, claim) in sr_pairs]
    distinct_claims = len(set(claims_sr))
    claim_case_reuse = Counter(claims_sr)
    claims_in_many_cases = sum(1 for c in claim_case_reuse.values() if c > 1)
    template_hits = sum(1 for c in claims_sr if TEMPLATE_RE.search(c))
    page_counts = Counter(
        cases[case_id]["page"] for (case_id, _) in sr_pairs
    )
    n_pages = len(page_counts)
    top_page_share = max(page_counts.values()) / n_sr if n_sr else None

    claim_words = sorted(len(c.split()) for c in set(claims_sr))
    ev_words = sorted(len(v["s"].split()) + len(v["r"].split()) for v in canonical)

    # duplicate (claim, evidence, label) among kept rows across splits
    seen = set()
    dup = 0
    for split in SPLITS:
        for (_case_id, claim), rows in splits[split]["groups"].items():
            for label, evidence in rows:
                key = (claim, evidence, label)
                if key in seen:
                    dup += 1
                else:
                    seen.add(key)

    # ---- verdict (criteria: KILL > CLEAN > MARGINAL) ----------------------
    a1_pass = malformed_rate <= MAX_MALFORMED_RATE
    a2_kill = fever_rate >= MAX_FEVER_LEAK_KILL
    kill = (
        (not a1_pass)
        or a2_kill
        or n_sr < N_SR_KILL
        or median_sim is None
        or median_sim < SIM_MARGINAL
    )
    clean = (
        (not kill)
        and n_sr >= N_SR_CLEAN
        and median_sim is not None
        and median_sim >= SIM_CLEAN
    )
    verdict = "KILL" if kill else ("CLEAN" if clean else "MARGINAL")

    report = {
        "audit": "VitaminC zero-model contrastive-triplet census",
        "date": "2026-09-25",
        "criteria": "results/audits/vitaminc_triplet_audit_criteria_v1.md",
        "zero_model": True,
        "source": {
            "dataset": "https://huggingface.co/datasets/tals/vitaminc",
            "pinned_commit": "be6febb761b0b2807687e61e0b5282e459df2fa0",
            "files": {
                split: {
                    "path": str(root / f"{split}.jsonl"),
                    "sha256": sha256(root / f"{split}.jsonl"),
                }
                for split in SPLITS
            },
            "license": "annotations CC-BY-SA-3.0 (Wikipedia-derived), per release LICENSE",
        },
        "purity": {
            "rows_total": total_rows,
            "revision_types": dict(
                sum((Counter(s["revision_types"]) for s in splits.values()), Counter())
            ),
            "real_rows": total_real,
            "malformed_real": dict(
                sum((Counter(s["malformed"]) for s in splits.values()), Counter())
            ),
            "malformed_rate_vs_real": malformed_rate,
            "kept_rows": total_kept,
            "fever_id_leak_rows": total_fever,
            "fever_id_leak_rate_vs_kept": fever_rate,
            "A1_pass": a1_pass,
            "A2_kill": a2_kill,
        },
        "structure": {
            "cases": len(cases),
            "cases_straddling_splits": straddled,
            "groups_case_claim": len(groups),
            "rows_per_case_hist": dict(
                sorted(Counter(info["rows"] for info in cases.values()).items())
            ),
            "evidences_per_case_hist": dict(
                sorted(Counter(len(info["evidence"]) for info in cases.values()).items())
            ),
            "claims_per_case_hist": dict(
                sorted(Counter(len(info["claims"]) for info in cases.values()).items())
            ),
            "rows_per_group_hist": dict(sorted(group_size.items())),
            "evidences_per_group_hist": dict(sorted(n_ev_per_group.items())),
            "label_marginal_kept_rows": dict(label_marginal),
        },
        "sr_pairs": {
            "n_sr": n_sr,
            "by_split": dict(sr_by_split),
            "canonical_1S1R": len(canonical),
            "anomalous_multi_row": anomalous_multi,
            "same_text_label_contradictions": same_text_contradictions,
            "distinct_claim_texts": distinct_claims,
            "claims_reused_across_cases": claims_in_many_cases,
            "template_claim_hits": template_hits,
            "template_claim_rate": template_hits / n_sr if n_sr else None,
            "template_regex": TEMPLATE_RE.pattern,
            "n_pages": n_pages,
            "top_page_share": top_page_share,
            "duplicate_claim_evidence_label_rows": dup,
            "claim_words_p50": claim_words[len(claim_words) // 2] if claim_words else None,
            "claim_words_p90": claim_words[int(len(claim_words) * 0.9)] if claim_words else None,
            "evidence_pair_words_p50": ev_words[len(ev_words) // 2] if ev_words else None,
            "evidence_pair_words_p90": ev_words[int(len(ev_words) * 0.9)] if ev_words else None,
        },
        "minimality": {
            "n_scored": len(sims),
            "statistic": "difflib.SequenceMatcher ratio over whitespace tokens (autojunk off), median over canonical SR-pairs",
            "median": median_sim,
            "p10": p10_sim,
            "min": min_sim,
            "max": max_sim,
        },
        "criteria_evaluation": {
            "A1_malformed_rate_le_5pct": {"value": malformed_rate, "pass": a1_pass},
            "A2_fever_leak_lt_1pct": {"value": fever_rate, "kill": a2_kill},
            "B_volume": {
                "n_sr": n_sr,
                "kill_lt": N_SR_KILL,
                "marginal_lt": N_SR_CLEAN,
                "pass": n_sr >= N_SR_CLEAN,
            },
            "C_minimality": {
                "median": median_sim,
                "marginal_below": SIM_MARGINAL,
                "clean_at": SIM_CLEAN,
                "pass": median_sim is not None and median_sim >= SIM_CLEAN,
            },
        },
        "verdict": verdict,
        "verdict_rule": (
            "KILL > CLEAN > MARGINAL; KILL if A1/A2 fail or N_SR<300 or "
            "median sim<0.80; CLEAN if N_SR>=1000 and median sim>=0.90; "
            "else MARGINAL"
        ),
        "y0_note": "Y0 = claim alone is constructible for free for every claim (no data row needed).",
        "limitations": [
            "pre- vs post-edit evidence ordering is not identifiable from the release schema (D6); recorded, not gated",
            "minimality statistic is computed over canonical 1S+1R groups only; anomalous multi-row groups are counted separately",
        ],
    }

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # ---- markdown summary -------------------------------------------------
    fmt = lambda x: "None" if x is None else (x if isinstance(x, str) else round(x, 4))
    md = f"""# VitaminC zero-model triplet audit (v1)

- date: {report['date']}
- criteria (pre-registered before download): `{report['criteria']}`
- source: tals/vitaminc @ `{report['source']['pinned_commit']}` (0 model calls)
- verdict: **{verdict}**

## A. Purity
- rows total {total_rows} (train/dev/test), revision_type values: {report['purity']['revision_types']}
- real rows {total_real}; malformed dropped {total_malformed} ({malformed_rate:.4%}) -> A1 {'PASS' if a1_pass else 'FAIL'}
- FEVER_id leaks among kept: {total_fever} ({fever_rate:.4%}) -> A2 {'KILL' if a2_kill else 'pass'}

## B. Volume
- **N_SR = {n_sr}** (by split: {dict(sr_by_split)}); canonical 1S+1R {len(canonical)}, anomalous {anomalous_multi}, same-text contradictions {same_text_contradictions}
- bands: kill < {N_SR_KILL}, marginal < {N_SR_CLEAN} -> {'pass' if n_sr >= N_SR_CLEAN else 'below CLEAN band'}

## C. Minimality (canonical SR-pairs)
- median similarity **{fmt(median_sim)}** (p10 {fmt(p10_sim)}, min {fmt(min_sim)})
- bands: kill < {SIM_MARGINAL}, marginal < {SIM_CLEAN} -> {'pass' if median_sim is not None and median_sim >= SIM_CLEAN else 'below CLEAN band'}

## D. Structure (reported)
- cases {len(cases)} (straddling splits {straddled}), (case, claim) groups {len(groups)}
- evidences per case hist: {report['structure']['evidences_per_case_hist']}
- rows per group hist: {report['structure']['rows_per_group_hist']}
- evidences per group hist: {report['structure']['evidences_per_group_hist']}
- label marginal (kept rows): {dict(label_marginal)}
- distinct claim texts among SR-pairs {distinct_claims}, reused across cases {claims_in_many_cases}
- template-claim rate {fmt(report['sr_pairs']['template_claim_rate'])} (regex `{TEMPLATE_RE.pattern}`), pages {n_pages}, top-page share {fmt(top_page_share)}
- duplicate (claim, evidence, label) rows {dup}
- claim words p50/p90 {report['sr_pairs']['claim_words_p50']}/{report['sr_pairs']['claim_words_p90']};
  evidence-pair words p50/p90 {report['sr_pairs']['evidence_pair_words_p50']}/{report['sr_pairs']['evidence_pair_words_p90']}

## Verdict rule
{report['verdict_rule']}
"""
    Path(args.md).write_text(md, encoding="utf-8")
    print(md)
    print(f"[audit] json -> {out}")
    print(f"[audit] verdict = {verdict}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
