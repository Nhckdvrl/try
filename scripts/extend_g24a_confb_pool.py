#!/usr/bin/env python3
"""Extend the Confirmation-B reserve pool along the frozen seed order.

The §13 freeze sampled active 200 + reserve 80 (seed ranks 0-279) from the
shuffled candidate order of scripts/freeze_g24a_confb.py. The zero-model
review found more invalid actives than valid reserves (replacement rule:
"invalid pairs are replaced by the next pair of the same pool in frozen
seed order"), so the SAME pool's SAME shuffled order continues past rank
279 — exactly the P2 mechanism (P2 reviewed 262 rows to reach 200 valid).

This script:
  * rebuilds the candidate list with the freeze's F1/F2/F4/F5/F6/F7 chain
    (byte-identical logic, no writes to the freeze outputs),
  * reproduces random.Random(SEED).shuffle and ASSERTS that order[0:280]
    matches data/items/g24a_confb_pool_v1.csv row-by-row (case_id and
    claim_sha) — the frozen pool is thereby proven to be this order's head,
  * writes the next EXT rows (seed ranks 280+) to
    data/items/g24a_confb_pool_ext_v1.csv and renders them unlabeled into
    data/items/g24a_confb_reserve_ext_review_v1.md (Evidence A = evidence_s
    as in the active review; orientation still hidden from the reviewer).

Usage: python scripts/extend_g24a_confb_pool.py [n_extra]   (default 24)
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

# --- byte-identical copies of the freeze's constants -----------------------
ROOT = Path("data/external/raw/vitaminc")
SPLITS = ("train", "dev", "test")
SHA256 = {
    "train": "7461c6fd1a13459590317c5ccdc8651dd2daf7c1ad8ae4b10ccd88d164fccd5a",
    "dev":   "544934677f5d133873e6d38f4557f8966f4efa5d3d70874ffe6913f2091b86b5",
    "test":  "7ad1808dbc30c62e0a1427a53022d0dfaff668a1fde3c4b612a2d266edd753ad",
}
PRIOR_POOLS = ("results/pilots/vitaminc_pilot_r1/pool_v1.jsonl",
               "results/pilots/vitaminc_pilot_r1/pool_v2.jsonl")
P2_POOL_CSV = "data/items/g24a_p2_pool_v1.csv"
LABELS = {"SUPPORTS", "REFUTES", "NOT ENOUGH INFO"}
TEMPLATE_RE = re.compile(
    r"(?i)(less than|more than|fewer than|over|under|at least|at most)\b[^.]{0,20}\d")
SEED = 20260929
N_ACTIVE, N_RESERVE = 200, 80
POOL_CSV = "data/items/g24a_confb_pool_v1.csv"
POOL_EXT_CSV = "data/items/g24a_confb_pool_ext_v1.csv"
REVIEW_EXT_MD = "data/items/g24a_confb_reserve_ext_review_v1.md"


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def norm_claim(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().casefold().rstrip(" .")


def build_candidates() -> list[dict]:
    groups = defaultdict(lambda: {"s": set(), "r": set()})
    case_order, case_loc = {}, {}
    stats = Counter()
    seq = 0
    for split in SPLITS:
        path = ROOT / f"{split}.jsonl"
        if not path.exists():
            raise SystemExit(f"missing {path}; run scripts/fetch_external_sources.py")
        assert sha256(path) == SHA256[split], path
        with path.open(encoding="utf-8") as fh:
            for lineno, line in enumerate(fh, 1):
                line = line.rstrip("\n")
                if not line:
                    continue
                row = json.loads(line)
                if row.get("revision_type") != "real":
                    continue
                label = row.get("label")
                claim = row.get("claim") or ""
                evidence = row.get("evidence") or ""
                if label not in LABELS or not claim or not evidence:
                    continue
                if row.get("FEVER_id"):
                    continue
                seq += 1
                key = (str(row.get("case_id")), claim)
                case_order.setdefault(key, seq)
                case_loc.setdefault(key, (split, lineno, str(row.get("page") or "")))
                if label == "SUPPORTS":
                    groups[key]["s"].add(evidence)
                elif label == "REFUTES":
                    groups[key]["r"].add(evidence)
    canonical = {k: (next(iter(d["s"])), next(iter(d["r"])))
                 for k, d in groups.items()
                 if len(d["s"]) == 1 and len(d["r"]) == 1 and d["s"] != d["r"]}

    prior_cases, prior_claims = set(), set()
    for p in PRIOR_POOLS:
        for line in open(p, encoding="utf-8"):
            r = json.loads(line)
            prior_cases.add(str(r["case_id"]))
            prior_claims.add(norm_claim(r["claim"]))
    for r in csv.DictReader(open(P2_POOL_CSV, newline="", encoding="utf-8")):
        prior_cases.add(str(r["case_id"]))
        prior_claims.add(norm_claim(r["claim"]))

    seen_claims, seen_cases, candidates = set(), set(), []
    for key in sorted(canonical, key=lambda k: case_order[k]):
        case_id, claim = key
        nc = norm_claim(claim)
        if nc in seen_claims or TEMPLATE_RE.search(claim) or case_id in seen_cases:
            continue
        if case_id in prior_cases or nc in prior_claims:
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
    return candidates


def main() -> int:
    n_extra = int(sys.argv[1]) if len(sys.argv) > 1 else 24

    candidates = build_candidates()
    rng = random.Random(SEED)
    order = list(candidates)
    rng.shuffle(order)
    frozen = order[:N_ACTIVE + N_RESERVE]

    # --- prove the frozen pool is this order's head -------------------------
    back = list(csv.DictReader(open(POOL_CSV, newline="", encoding="utf-8")))
    assert len(back) == N_ACTIVE + N_RESERVE, len(back)
    for i, (row, c) in enumerate(zip(back, frozen)):
        assert int(row["seed_rank"]) == i, (i, row["seed_rank"])
        assert row["case_id"] == c["case_id"], (i, row["case_id"], c["case_id"])
        assert row["claim_sha"] == c["claim_sha"], (i, row["claim_sha"])
    print(f"verified: frozen pool ({len(back)} rows) == shuffled order[0:{len(back)}]")

    ext = order[N_ACTIVE + N_RESERVE: N_ACTIVE + N_RESERVE + n_extra]
    for rank, c in enumerate(ext, start=N_ACTIVE + N_RESERVE):
        c["seed_rank"] = rank
    assert len({c["case_id"] for c in ext}) == len(ext)
    assert len({c["claim_sha"] for c in ext}) == len(ext)
    with open(POOL_EXT_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["seed_rank", "active_200", "cfb_id", "case_id", "split",
                    "first_lineno", "page", "claim_sha", "claim",
                    "evidence_s", "evidence_r"])
        for c in ext:
            w.writerow([c["seed_rank"], "no", f"g24cfb_{c['seed_rank']:03d}",
                        c["case_id"], c["split"], c["first_lineno"], c["page"],
                        c["claim_sha"], c["claim"], c["evidence_s"],
                        c["evidence_r"]])

    L = ["# G24A Confirmation-B RESERVE EXTENSION zero-model review material",
         "",
         f"Seed {SEED}; seed ranks {ext[0]['seed_rank']}-{ext[-1]['seed_rank']}, "
         "the continuation of the SAME frozen shuffled candidate order past the "
         "80-row reserve block (replacement rule: invalid pairs are replaced by "
         "the next pair of the same pool in frozen seed order). Same protocol "
         "and same unlabeled A/B rendering as the active and reserve material.",
         ""]
    for c in ext:
        L += [f"## seed_rank={c['seed_rank']} cfb_id=g24cfb_{c['seed_rank']:03d} "
              f"case={c['case_id']} page={c['page']!r}",
              "",
              f"CLAIM:\n{c['claim']}",
              "",
              f"Evidence A:\n{c['evidence_s']}",
              "",
              f"Evidence B:\n{c['evidence_r']}",
              ""]
    Path(REVIEW_EXT_MD).write_text("\n".join(L) + "\n", encoding="utf-8")

    print(f"wrote {POOL_EXT_CSV} ({len(ext)} rows, ranks "
          f"{ext[0]['seed_rank']}-{ext[-1]['seed_rank']}) + {REVIEW_EXT_MD}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
