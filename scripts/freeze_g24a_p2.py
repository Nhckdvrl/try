#!/usr/bin/env python3
"""Freeze Pilot P2 material: 200 VitaminC real-revision same-claim pairs.

Pilot P2 "same-claim counterfactual reconstruction" (user spec, 2026-09-25,
registered in results/discovery/g24a_competing_accounts_v1.md §9):

  * Same claim + one natural SUPPORT evidence + one natural REFUTE evidence
    (VitaminC real-revision SR pairs; audit verdict CLEAN, N_SR = 92,764).
  * Zero-model data validity only. NO model output is read at any point
    (asserted below). The old "both directions A>=10" gate is permanently
    dead and is NOT implemented here.
  * G27A removal-vs-negation hypothesis stays KILL: this script reuses the
    VitaminC *material* only. The old pilot's F3 minimality filter
    (sim >= 0.90) and its stage gates are deliberately NOT imported.

Filter chain (in first-encounter order train -> dev -> test):
  F1  revision_type == "real"; label in {SUPPORTS, REFUTES, NOT ENOUGH
      INFO}; claim and evidence non-empty; FEVER_id empty (0 leaks).
  F2  group by (case_id, claim): exactly one distinct SUPPORTS evidence
      text and exactly one distinct REFUTES evidence text, texts different.
  F4  normalized-claim dedup (first occurrence wins):
      re.sub(r"\\s+", " ", claim).strip().casefold().rstrip(" .")
  F5  non-template (audit D4 regex): drop claims matching
      (?i)(less than|more than|fewer than|over|under|at least|at most)\\b[^.]{0,20}\\d
  F6  at most one qualifying claim per case_id (revision); first wins.
  F7  freshness: drop any case_id OR normalized claim present in the prior
      VitaminC pilot pools (pool_v1/pool_v2 - 200 claims already run).
  S   seeded sample: candidates in source order -> seeded shuffle ->
      seed_rank 0..N-1 -> active 200 + reserve 40 (same-source replacements
      for zero-model validity swaps only, decided after review; never by
      "looks good for the hypothesis").

Outputs:
  data/items/g24a_p2_pool_v1.csv    - active 200 + reserve 40, seed ranks
  data/items/g24a_p2_review_v1.md   - the active 200 in seed order, for the
                                      zero-model data-validity review
                                      (Evidence A / Evidence B presented
                                      UNLABELED: reviewer judges text
                                      semantics directly)

Usage: python scripts/freeze_g24a_p2.py
"""
from __future__ import annotations

import csv
import hashlib
import json
import random
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("data/external/raw/vitaminc")
SPLITS = ("train", "dev", "test")
SHA256 = {
    "train": "7461c6fd1a13459590317c5ccdc8651dd2daf7c1ad8ae4b10ccd88d164fccd5a",
    "dev":   "544934677f5d133873e6d38f4557f8966f4efa5d3d70874ffe6913f2091b86b5",
    "test":  "7ad1808dbc30c62e0a1427a53022d0dfaff668a1fde3c4b612a2d266edd753ad",
}
PRIOR_POOLS = ("results/pilots/vitaminc_pilot_r1/pool_v1.jsonl",
               "results/pilots/vitaminc_pilot_r1/pool_v2.jsonl")
LABELS = {"SUPPORTS", "REFUTES", "NOT ENOUGH INFO"}
TEMPLATE_RE = re.compile(
    r"(?i)(less than|more than|fewer than|over|under|at least|at most)\b[^.]{0,20}\d")
SEED = 20260927          # fixed before any inspection; documented in commit
N_ACTIVE, N_RESERVE = 200, 40
POOL_CSV = "data/items/g24a_p2_pool_v1.csv"
REVIEW_MD = "data/items/g24a_p2_review_v1.md"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def norm_claim(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().casefold().rstrip(" .")


def main() -> int:
    for p in (POOL_CSV, REVIEW_MD, *PRIOR_POOLS):
        if "results/raw" in p:
            raise SystemExit("REFUSAL: freeze must not read model output")

    # --- F1 + F2: purity and canonical SR-pairs, per split in order --------
    groups = defaultdict(lambda: {"s": set(), "r": set()})   # (case, claim)
    case_order = {}                                          # (case, claim) -> seq
    case_loc = {}                                            # -> (split, lineno, page)
    stats = Counter()
    seq = 0
    for split in SPLITS:
        path = ROOT / f"{split}.jsonl"
        if not path.exists():
            raise SystemExit(f"missing {path}; run scripts/fetch_external_sources.py")
        got = sha256(path)
        assert got == SHA256[split], (path, got, SHA256[split])
        with path.open(encoding="utf-8") as fh:
            for lineno, line in enumerate(fh, 1):
                line = line.rstrip("\n")
                if not line:
                    continue
                row = json.loads(line)
                stats["rows_total"] += 1
                if row.get("revision_type") != "real":
                    continue
                stats["rows_real"] += 1
                label = row.get("label")
                claim = row.get("claim") or ""
                evidence = row.get("evidence") or ""
                if label not in LABELS or not claim or not evidence:
                    stats["malformed"] += 1
                    continue
                if row.get("FEVER_id"):
                    stats["fever_leak"] += 1
                    continue
                seq += 1
                case_id = str(row.get("case_id"))
                key = (case_id, claim)
                case_order.setdefault(key, seq)
                loc = (split, lineno, str(row.get("page") or ""))
                case_loc.setdefault(key, loc)
                if label == "SUPPORTS":
                    groups[key]["s"].add(evidence)
                elif label == "REFUTES":
                    groups[key]["r"].add(evidence)
    assert stats["fever_leak"] == 0, stats   # audit A2: 0 leaks among kept

    canonical = {}
    for key, d in groups.items():
        if len(d["s"]) == 1 and len(d["r"]) == 1 and d["s"] != d["r"]:
            canonical[key] = (next(iter(d["s"])), next(iter(d["r"])))
        else:
            stats["not_canonical"] += 1
    print(f"F1 rows: total {stats['rows_total']}, real {stats['rows_real']}, "
          f"malformed {stats['malformed']}, fever_leak {stats['fever_leak']}")
    print(f"F2 canonical 1S+1R pairs: {len(canonical)} "
          f"(dropped non-canonical {stats['not_canonical']})")

    # --- F4/F5/F6/F7: dedup, non-template, one per case, freshness ---------
    prior_cases, prior_claims = set(), set()
    for p in PRIOR_POOLS:
        for line in open(p, encoding="utf-8"):
            r = json.loads(line)
            prior_cases.add(str(r["case_id"]))
            prior_claims.add(norm_claim(r["claim"]))

    seen_claims, seen_cases = set(), set()
    candidates = []
    for key in sorted(canonical, key=lambda k: case_order[k]):   # source order
        case_id, claim = key
        nc = norm_claim(claim)
        if nc in seen_claims:
            stats["dup_claim"] += 1
            continue
        if TEMPLATE_RE.search(claim):
            stats["template"] += 1
            continue
        if case_id in seen_cases:
            stats["dup_case"] += 1
            continue
        if case_id in prior_cases or nc in prior_claims:
            stats["not_fresh"] += 1
            continue
        seen_claims.add(nc)
        seen_cases.add(case_id)
        s_ev, r_ev = canonical[key]
        split, lineno, page = case_loc[key]
        candidates.append({
            "case_id": case_id, "claim": claim, "evidence_s": s_ev,
            "evidence_r": r_ev, "page": page, "split": split,
            "first_lineno": lineno, "claim_sha": hashlib.sha256(
                nc.encode()).hexdigest()[:12],
        })

    print(f"F4/F5/F6/F7 drops: dup_claim {stats['dup_claim']}, "
          f"template {stats['template']}, dup_case {stats['dup_case']}, "
          f"not_fresh {stats['not_fresh']}")
    print(f"candidates: {len(candidates)}")
    if len(candidates) < N_ACTIVE + N_RESERVE:
        raise SystemExit(f"too few candidates: {len(candidates)} < "
                         f"{N_ACTIVE + N_RESERVE}")

    # --- S: seeded sample, active + reserve --------------------------------
    rng = random.Random(SEED)
    order = list(candidates)
    rng.shuffle(order)
    selected = order[:N_ACTIVE + N_RESERVE]
    for rank, c in enumerate(selected):
        c["seed_rank"] = rank
    active, reserve = selected[:N_ACTIVE], selected[N_ACTIVE:]
    assert len({c["case_id"] for c in selected}) == len(selected)
    assert len({c["claim_sha"] for c in selected}) == len(selected)

    # --- pool csv ----------------------------------------------------------
    with open(POOL_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["seed_rank", "active_200", "p2_id", "case_id", "split",
                    "first_lineno", "page", "claim_sha", "claim",
                    "evidence_s", "evidence_r"])
        for c in selected:
            w.writerow([c["seed_rank"],
                        "yes" if c in active else "no",
                        f"g24p2_{c['seed_rank']:03d}",
                        c["case_id"], c["split"], c["first_lineno"],
                        c["page"], c["claim_sha"],
                        c["claim"], c["evidence_s"], c["evidence_r"]])
    back = list(csv.DictReader(open(POOL_CSV, newline="", encoding="utf-8")))
    assert len(back) == N_ACTIVE + N_RESERVE
    assert sum(1 for r in back if r["active_200"] == "yes") == N_ACTIVE

    # --- review material (active 200, seed order, UNLABELED evidences) -----
    L = ["# G24A P2 active-200 zero-model data-validity review material", "",
         f"Seed {SEED}; 200 active pairs (+ {N_RESERVE} reserve, same "
         "source, next seed order) sampled from the VitaminC real-revision "
         "canonical SR pool after F1/F2/F4/F5/F6/F7.",
         "",
         "Review criterion (data integrity ONLY), per pair: exactly one of "
         "Evidence A / Evidence B supports the claim as a matter of fact, "
         "and the other contradicts it as a matter of fact. Also judge: is "
         "the claim a self-contained proposition a reader can evaluate from "
         "the claim + evidence alone? Invalid pairs (wrong orientation, "
         "neither direction works, broken/elliptical text, claim not "
         "self-contained) are replaced by the next pair of the same pool in "
         "frozen seed order. No stylistic / hypothesis-based selection.",
         "",
         "Evidence A / Evidence B are deliberately UNLABELED (dataset S/R "
         "orientation hidden): judge direction from the text alone. "
         "Recorded orientation lives only in the pool csv.", ""]
    for c in active:
        L += [f"## seed_rank={c['seed_rank']} p2_id=g24p2_{c['seed_rank']:03d} "
              f"case={c['case_id']} page={c['page']!r}",
              "",
              f"CLAIM:\n{c['claim']}",
              "",
              f"Evidence A:\n{c['evidence_s']}",
              "",
              f"Evidence B:\n{c['evidence_r']}",
              ""]
    Path(REVIEW_MD).write_text("\n".join(L) + "\n", encoding="utf-8")

    print(f"seed {SEED}: active 200 + reserve {N_RESERVE} "
          f"(candidates shuffled from {len(candidates)})")
    print(f"wrote {POOL_CSV} ({len(back)} rows) + {REVIEW_MD} "
          f"({len(active)} pairs)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
