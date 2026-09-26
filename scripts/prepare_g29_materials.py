"""Deterministic, output-blind shortlist for the G29 revocation test.

Only source data and historical item pools are read. Semantic selection is
delegated to a separate, label-blind local audit before any model inference.
"""

import csv
import hashlib
import json
import random
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data/external/raw/vitaminc"
OUT = ROOT / "data/items/g29_candidate_pool_v1.jsonl"
AUDIT = ROOT / "data/items/g29_blind_audit_v1"
SEED = 20261001
N = 160
SOURCE_SHA256 = {
    "train": "7461c6fd1a13459590317c5ccdc8651dd2daf7c1ad8ae4b10ccd88d164fccd5a",
    "dev": "544934677f5d133873e6d38f4557f8966f4efa5d3d70874ffe6913f2091b86b5",
    "test": "7ad1808dbc30c62e0a1427a53022d0dfaff668a1fde3c4b612a2d266edd753ad",
}


def norm(text):
    return re.sub(r"\s+", " ", text).strip().casefold().rstrip(" .")


def eligible(text, lo, hi):
    return lo <= len(text) <= hi and text.isascii() and not re.search(
        r"\b(?:http|www|citation needed|\[|\]|-LRB-|-RRB-|nbsp)\b|[{}<>]", text, re.I
    )


def main():
    excluded_cases, excluded_claims = set(), set()
    for path in (ROOT / "data/items/g24a_p2_pool_v1.csv",
                 ROOT / "data/items/g24a_confb_pool_v1.csv",
                 ROOT / "data/items/g24a_confb_pool_ext_v1.csv"):
        for row in csv.DictReader(path.open()):
            excluded_cases.add(str(row["case_id"]))
            excluded_claims.add(norm(row["claim"]))
    for path in (ROOT / "results/pilots/vitaminc_pilot_r1/pool_v1.jsonl",
                 ROOT / "results/pilots/vitaminc_pilot_r1/pool_v2.jsonl"):
        for line in path.open():
            row = json.loads(line)
            excluded_cases.add(str(row["case_id"]))
            excluded_claims.add(norm(row["claim"]))

    groups = defaultdict(lambda: {"SUPPORTS": set(), "REFUTES": set()})
    meta = {}
    for split in ("train", "dev", "test"):
        path = SOURCE / f"{split}.jsonl"
        h = hashlib.sha256()
        with path.open("rb") as stream:
            for chunk in iter(lambda: stream.read(1 << 20), b""):
                h.update(chunk)
        assert h.hexdigest() == SOURCE_SHA256[split], split
        for lineno, line in enumerate(path.open(), 1):
            row = json.loads(line)
            if row.get("revision_type") != "real" or row.get("FEVER_id"):
                continue
            if row.get("label") not in ("SUPPORTS", "REFUTES"):
                continue
            case, claim, evidence = str(row["case_id"]), row["claim"], row["evidence"]
            if case in excluded_cases or norm(claim) in excluded_claims:
                continue
            if not eligible(claim, 25, 150) or not eligible(evidence, 35, 250):
                continue
            key = (case, claim)
            groups[key][row["label"]].add(evidence)
            meta.setdefault(key, (split, lineno, row.get("page", "")))

    candidates, seen_claims, seen_cases = [], set(), set()
    for (case, claim), pair in sorted(groups.items()):
        if len(pair["SUPPORTS"]) != 1 or len(pair["REFUTES"]) != 1:
            continue
        s, r = next(iter(pair["SUPPORTS"])), next(iter(pair["REFUTES"]))
        if s == r or norm(claim) in seen_claims or case in seen_cases:
            continue
        # Keep naturally occurring edits rather than unpaired facts. This is
        # a source-level heuristic, not a semantic-validity decision.
        if len(set(s.split()) & set(r.split())) / max(1, len(set(s.split()) | set(r.split()))) < .22:
            continue
        seen_cases.add(case)
        seen_claims.add(norm(claim))
        split, lineno, page = meta[(case, claim)]
        candidates.append(dict(case_id=case, claim=claim, evidence_s=s,
                               evidence_r=r, split=split, first_lineno=lineno,
                               page=page))
    rng = random.Random(SEED)
    rng.shuffle(candidates)
    assert len(candidates) >= N, len(candidates)
    rows = []
    for rank, row in enumerate(candidates[:N]):
        row = dict(row)
        row["id"] = f"g29_{rank:03d}"
        row["seed_rank"] = rank
        rows.append(row)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
    AUDIT.mkdir(parents=True, exist_ok=True)
    for batch in range(8):
        blind = []
        for row in rows[batch * 20:(batch + 1) * 20]:
            swap = int(hashlib.sha256(row["id"].encode()).hexdigest(), 16) % 2
            a, b = ((row["evidence_r"], row["evidence_s"]) if swap else
                    (row["evidence_s"], row["evidence_r"]))
            blind.append(dict(id=row["id"], claim=row["claim"],
                              evidence_a=a, evidence_b=b))
        (AUDIT / f"blind_{batch + 1:02d}.jsonl").write_text(
            "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in blind))
    print(f"{len(candidates)} mechanical candidates; {N} frozen; 8 blind batches")


if __name__ == "__main__":
    main()
