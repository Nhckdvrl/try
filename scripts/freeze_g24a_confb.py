#!/usr/bin/env python3
"""Freeze Confirmation-B material: 200 fresh VitaminC real-revision SR pairs.

Final confirmation freeze (registration §13.3, user ruling 2026-09-26).
Same filter chain as scripts/freeze_g24a_p2.py (F1 purity, F2 canonical
1S+1R, F4 normalized-claim dedup, F5 non-template, F6 one claim per case,
F7 freshness), with F7 EXTENDED and a NEW seed:

  * F7 freshness: drop any case_id OR normalized claim present in the
      prior VitaminC pilot pools (pool_v1/pool_v2) AND — new — any case_id
      OR normalized claim in data/items/g24a_p2_pool_v1.csv (all 280 rows,
      active + reserve: P2/P3/P4 material, so case/claim are disjoint from
      every pair this line has run or held).
  * SEED = 20260929 (P2's 20260927 untouched; §13 frozen).
  * active 200 + reserve 80, same-source replacement rule as P2
    (zero-model validity swaps only, decided AFTER review; never by
    "looks good for the hypothesis").
  * no model output is read at any point (asserted below).

Outputs:
  data/items/g24a_confb_pool_v1.csv   - active 200 + reserve 80, seed ranks
  data/items/g24a_confb_review_v1.md  - the active 200 in seed order, for
                                        the zero-model review (Evidence A /
                                        Evidence B UNLABELED, as in P2)

Usage: python scripts/freeze_g24a_confb.py
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
P2_POOL_CSV = "data/items/g24a_p2_pool_v1.csv"     # §13 F7 extension
LABELS = {"SUPPORTS", "REFUTES", "NOT ENOUGH INFO"}
TEMPLATE_RE = re.compile(
    r"(?i)(less than|more than|fewer than|over|under|at least|at most)\b[^.]{0,20}\d")
SEED = 20260929               # §13 frozen (P2's 20260927 untouched)
N_ACTIVE, N_RESERVE = 200, 80
POOL_CSV = "data/items/g24a_confb_pool_v1.csv"
REVIEW_MD = "data/items/g24a_confb_review_v1.md"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def norm_claim(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().casefold().rstrip(" .")


def main() -> int:
    for p in (POOL_CSV, REVIEW_MD, *PRIOR_POOLS, P2_POOL_CSV):
        if "results/raw" in p:
            raise SystemExit("REFUSAL: freeze must not read model output")

    # --- F1 + F2: purity and canonical SR-pairs, per split in order --------
    groups = defaultdict(lambda: {"s": set(), "r": set()})
    case_order = {}
    case_loc = {}
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
                case_loc.setdefault(key, (split, lineno, str(row.get("page") or "")))
                if label == "SUPPORTS":
                    groups[key]["s"].add(evidence)
                elif label == "REFUTES":
                    groups[key]["r"].add(evidence)
    assert stats["fever_leak"] == 0, stats   # audit A2: 0 leaks among kept
    print(f"F1 rows: total {stats['rows_total']}, real {stats['rows_real']}, "
          f"malformed {stats['malformed']}, fever_leak {stats['fever_leak']}")

    canonical = {}
    for key, d in groups.items():
        if len(d["s"]) == 1 and len(d["r"]) == 1 and d["s"] != d["r"]:
            canonical[key] = (next(iter(d["s"])), next(iter(d["r"])))
        else:
            stats["not_canonical"] += 1
    print(f"F2 canonical 1S+1R pairs: {len(canonical)} "
          f"(dropped non-canonical {stats['not_canonical']})")

    # --- F4/F5/F6/F7: dedup, non-template, one per case, freshness ---------
    prior_cases, prior_claims = set(), set()
    for p in PRIOR_POOLS:
        for line in open(p, encoding="utf-8"):
            r = json.loads(line)
            prior_cases.add(str(r["case_id"]))
            prior_claims.add(norm_claim(r["claim"]))
    n_p2_rows = 0
    for r in csv.DictReader(open(P2_POOL_CSV, newline="", encoding="utf-8")):
        prior_cases.add(str(r["case_id"]))
        prior_claims.add(norm_claim(r["claim"]))
        n_p2_rows += 1
    print(f"F7 freshness inputs: prior jsonl pools {len(PRIOR_POOLS)} + "
          f"P2 pool csv ({n_p2_rows} rows) -> {len(prior_cases)} case ids, "
          f"{len(prior_claims)} normalized claims excluded")

    seen_claims, seen_cases = set(), set()
    candidates = []
    for key in sorted(canonical, key=lambda k: case_order[k]):
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
        w.writerow(["seed_rank", "active_200", "cfb_id", "case_id", "split",
                    "first_lineno", "page", "claim_sha", "claim",
                    "evidence_s", "evidence_r"])
        for c in selected:
            w.writerow([c["seed_rank"],
                        "yes" if c in active else "no",
                        f"g24cfb_{c['seed_rank']:03d}",
                        c["case_id"], c["split"], c["first_lineno"],
                        c["page"], c["claim_sha"],
                        c["claim"], c["evidence_s"], c["evidence_r"]])
    back = list(csv.DictReader(open(POOL_CSV, newline="", encoding="utf-8")))
    assert len(back) == N_ACTIVE + N_RESERVE
    assert sum(1 for r in back if r["active_200"] == "yes") == N_ACTIVE

    # --- review material (active 200, seed order, UNLABELED evidences) -----
    L = ["# G24A Confirmation-B active-200 zero-model data-validity "
         "review material", "",
         f"Seed {SEED}; 200 active pairs (+ {N_RESERVE} reserve, same "
         "source, next seed order) sampled from the VitaminC real-revision "
         "canonical SR pool after F1/F2/F4/F5/F6/F7, with F7 extended over "
         "the full 280-row P2 pool (all P2/P3/P4 case ids and claims "
         "excluded).  Case/claim disjoint from everything this line has "
         "run.", "",
         "Review criterion (data integrity ONLY), per pair: exactly one of "
         "Evidence A / Evidence B supports the claim as a matter of fact, "
         "and the other contradicts it as a matter of fact. Also judge: is "
         "the claim a self-contained proposition a reader can evaluate from "
         "the claim + evidence alone? Invalid pairs (wrong orientation, "
         "neither direction works, broken/elliptical text, claim not "
         "self-contained) are replaced by the next pair of the same pool in "
         "frozen seed order. No stylistic / hypothesis-based selection.", "",
         "Evidence A / Evidence B are deliberately UNLABELED (dataset S/R "
         "orientation hidden): judge direction from the text alone. "
         "Recorded orientation lives only in the pool csv.", ""]
    for c in active:
        L += [f"## seed_rank={c['seed_rank']} cfb_id=g24cfb_{c['seed_rank']:03d} "
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
