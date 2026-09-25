#!/usr/bin/env python3
"""Freeze Confirmation A material: 500 strictly-unseen FEVER/SciFact items.

Final confirmation freeze (registration §13.2, user ruling 2026-09-26):
  * pool: g24a_candidates_v1.jsonl (13,283) with freshness
      (a) item_id present in NO item file ever rendered by any model run
          in this repo, AND
      (b) critical_evidence byte-disjoint from the evidence of every such
          item file  -> expect ~8,985 qualifying (8,776 fever + 209 scifact)
  * strata mirroring discovery/P1: 334 fever + 166 scifact (2:1)
  * per-source order: candidate ids sorted, seeded shuffle
      Random("20260930:<source>"), walk seed order with normalized-claim
      dedup (first seed-rank wins); first 334/166 distinct-claim items =
      active, the remainder of the source stays in seed order as the
      SAME-SOURCE reserve (data-validity swaps only, decided by the
      zero-model review; never by hypothesis-fitting)
  * no model output is read at any point (asserted below)

Outputs:
  data/items/g24a_confa_pool_v1.csv    - active 500 + reserve, seed ranks,
                                         recorded official direction
  data/items/g24a_confa_review_v1.md   - the active 500 in seed order, for
                                         the zero-model review (claim +
                                         evidence, NO labels shown: the
                                         reviewer judges text semantics
                                         directly; agreement with the
                                         official direction is compared by
                                         the build step afterwards)

Usage: python scripts/freeze_g24a_confa.py
"""
from __future__ import annotations

import csv
import glob
import hashlib
import json
import os
import random
import re
import sys
from collections import Counter
from pathlib import Path

CANDIDATES = "data/items/g24a_candidates_v1.jsonl"
POOL_CSV = "data/items/g24a_confa_pool_v1.csv"
REVIEW_MD = "data/items/g24a_confa_review_v1.md"
SEED_PREFIX = "20260930"          # §13 frozen seed string
TARGET = {"fever": 334, "scifact": 166}     # 2:1, mirrors discovery/P1


def norm_claim(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().casefold().rstrip(" .")


def main() -> int:
    for p in (POOL_CSV, REVIEW_MD):
        if "results/raw" in p:
            raise SystemExit("REFUSAL: freeze must not read model output")

    # --- 1. freshness: every item file ever rendered -----------------------
    used_ids, used_evs = set(), set()
    rendered = []
    for f in sorted(glob.glob("data/items/*.jsonl")):
        if f == CANDIDATES:
            continue
        first = open(f, encoding="utf-8").readline()
        if "item_id" not in json.loads(first):
            continue                                  # verdict/analysis files
        rendered.append(f)
        for line in open(f, encoding="utf-8"):
            d = json.loads(line)
            used_ids.add(d["item_id"])
            e = d.get("critical_evidence")
            if e:
                used_evs.add(e)
    print(f"rendered item files: {len(rendered)}; used ids {len(used_ids)}, "
          f"used evidences {len(used_evs)}")

    # --- 2. qualify candidates --------------------------------------------
    qual = {"fever": [], "scifact": []}
    n_id_drop = n_ev_drop = 0
    for line in open(CANDIDATES, encoding="utf-8"):
        d = json.loads(line)
        fam = d["task_family"]
        assert fam in ("g24a_fever", "g24a_scifact"), fam
        src = "fever" if fam == "g24a_fever" else "scifact"
        if d["item_id"] in used_ids:
            n_id_drop += 1
            continue
        if d["critical_evidence"] in used_evs:
            n_ev_drop += 1
            continue
        qual[src].append(d)
    print(f"freshness drops: id {n_id_drop}, evidence {n_ev_drop}; "
          f"qualifying: fever {len(qual['fever'])}, "
          f"scifact {len(qual['scifact'])}")
    for src, n in TARGET.items():
        # reserve floor: >= 40 per source (scifact qualifies 209 -> 43
        # reserve; P1's own reserve ratio was thinner).  Corrected in the
        # §13 pre-sampling erratum before any material was written.
        assert len(qual[src]) >= n + 40, (src, len(qual[src]), n)

    # --- 3. per-source seeded order with normalized-claim dedup ------------
    active, reserve = [], []
    for src in ("fever", "scifact"):
        lst = sorted(qual[src], key=lambda d: d["item_id"])
        random.Random(f"{SEED_PREFIX}:{src}").shuffle(lst)
        seen, a, r = set(), [], []
        for d in lst:
            nc = norm_claim(d["base_context"])
            if nc in seen:
                continue                              # first seed-rank wins
            seen.add(nc)
            (a if len(a) < TARGET[src] else r).append(d)
        assert len(a) == TARGET[src], (src, len(a))
        for i, d in enumerate(a + r):
            d["_rank"] = i
            d["_src"] = src
        active += a
        reserve += r
    assert len(active) == 500, len(active)
    assert len({norm_claim(d["base_context"]) for d in active}) == 500

    # re-assert freshness + no overlap against the final selection
    for d in active + reserve:
        assert d["item_id"] not in used_ids, d["item_id"]
        assert d["critical_evidence"] not in used_evs, d["item_id"]
    assert not ({d["item_id"] for d in active} &
                {d["item_id"] for d in reserve})

    # --- 4. pool csv (active + first 200 reserve per source; the full
    #         deterministic seed order is reproducible from the seed) -------
    mat = []
    for src in ("fever", "scifact"):
        a = [d for d in active if d["_src"] == src]
        r = [d for d in reserve if d["_src"] == src][:200]
        mat += a + r
    with open(POOL_CSV, "w", newline="", encoding="utf-8") as fh:
        w = csv.writer(fh)
        w.writerow(["seed_rank_within_source", "source", "role", "item_id",
                    "stratum", "direction", "claim_sha", "claim",
                    "evidence"])
        for d in mat:
            w.writerow([d["_rank"], d["_src"],
                        "active" if d in active else "reserve",
                        d["item_id"],
                        (d["meta"].get("stratum") if isinstance(d["meta"], dict)
                         else None),
                        d["critical_direction"],
                        hashlib.sha256(
                            norm_claim(d["base_context"]).encode()
                        ).hexdigest()[:12],
                        d["base_context"], d["critical_evidence"]])
    back = list(csv.DictReader(open(POOL_CSV, newline="", encoding="utf-8")))
    assert sum(1 for r in back if r["role"] == "active") == 500
    assert Counter(r["source"] for r in back if r["role"] == "active") \
        == Counter({"fever": 334, "scifact": 166})
    assert sum(1 for r in back if r["role"] == "reserve") == 243  # 200 + 43
    print(f"reserve: fever {sum(1 for r in back if r['source']=='fever' and r['role']=='reserve')}, "
          f"scifact {sum(1 for r in back if r['source']=='scifact' and r['role']=='reserve')}")

    # --- 5. review material (active 500, seed order, NO labels) ------------
    L = ["# G24A Confirmation-A active-500 zero-model review material", "",
         f"Seeds {SEED_PREFIX}:fever / {SEED_PREFIX}:scifact; 500 active "
         "items (334 fever + 166 scifact) + same-source reserve, drawn from "
         "the strictly-unseen candidate pool (id never rendered anywhere in "
         "this repo; evidence byte-disjoint from every rendered item file).",
         "",
         "Review criterion (semantic / data integrity ONLY), per item: from "
         "the claim + evidence text alone, decide — does E as a matter of "
         "fact SUPPORT the claim, REFUTE it, or neither (broken pair / "
         "annotation noise / claim not self-contained / direction wrong as "
         "a matter of fact)?  Invalid items are replaced by the next item "
         "of the same source in frozen seed order.  No stylistic / "
         "hypothesis-based selection.",
         "",
         "Official labels are deliberately not shown: judge from the text. "
         "Recorded direction lives only in the pool csv; agreement with it "
         "is checked afterwards by the build step.", ""]
    for d in active:
        L += [f"## seed_rank={d['_rank']} source={d['_src']} "
              f"key={hashlib.sha256(d['item_id'].encode()).hexdigest()[:10]}",
              "",
              f"CLAIM:\n{d['base_context']}",
              "",
              f"EVIDENCE:\n{d['critical_evidence']}",
              ""]
    Path(REVIEW_MD).write_text("\n".join(L) + "\n", encoding="utf-8")

    print(f"seeds {SEED_PREFIX}:<source>: active 500 = 334 fever + 166 "
          f"scifact; reserve = {len(reserve)} (all remaining distinct-claim "
          "fresh items in seed order)")
    print(f"wrote {POOL_CSV} ({len(back)} rows) + {REVIEW_MD} "
          f"({len(active)} items); freshness re-asserted on the final "
          "selection (0 id, 0 evidence overlap)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
