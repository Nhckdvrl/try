#!/usr/bin/env python3
"""Build the Confirmation-A item file: 500 strictly-fresh FEVER/SciFact
items, rendered through the UNMODIFIED G24A module (5 cells per item).

Inputs (all committed before any model run):
  data/items/g24a_confa_pool_v1.csv                - active 500 + same-source reserve
  data/items/g24a_confa_validity_v1.jsonl          - zero-model blind verdicts, active 500
  data/items/g24a_confa_reserve_validity_v1.jsonl  - zero-model blind verdicts, reserve 83
  data/items/g24a_candidates_v1.jsonl              - candidate items (field source)

Selection rule (frozen registration §13.2, decided before any model output):
per source, walk the frozen seed order.  An ACTIVE item is kept iff its
blind call agrees with the recorded direction (call S & direction increase,
or call R & direction decrease).  Every invalid active is replaced by the
next same-source RESERVE in seed order whose own blind verdict also agrees
with its recorded direction; invalid reserves are skipped.  Replacement is
data-validity only - never hypothesis-driven (§13.2: no gates, no
selection).

Item construction: candidate JSON copied field-for-field, meta annotated
with pilot provenance (pilot tag, seed rank, role, blind call/note; each
swap-in also records the active rank/id it replaced).  task_family is left
as g24a_fever / g24a_scifact so all five cells dispatch through the
*unmodified* G24A module (character-identical prompts by construction;
asserted per prompt by scripts/verify_g24a_confa_prompts.py).

Freshness re-asserted exactly as the freeze (script step 1): the final
item_id and critical_evidence of every selected item must be absent from
every rendered item file in data/items/*.jsonl.

Outputs:
  data/items/g24a_confa_v1.jsonl  - 500 items (fever seed order, then scifact)
  data/items/g24a_confa_ids.json  - the 500 ids, file order

Usage: python scripts/build_g24a_confa_items.py
"""
from __future__ import annotations

import csv
import glob
import hashlib
import json
import re
from collections import Counter
from pathlib import Path

POOL_CSV = "data/items/g24a_confa_pool_v1.csv"
VALIDITY = "data/items/g24a_confa_validity_v1.jsonl"
RESERVE_VALIDITY = "data/items/g24a_confa_reserve_validity_v1.jsonl"
CANDIDATES = "data/items/g24a_candidates_v1.jsonl"
OUT = "data/items/g24a_confa_v1.jsonl"
IDS = "data/items/g24a_confa_ids.json"
TARGET = {"fever": 334, "scifact": 166}


def norm_claim(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip().casefold().rstrip(" .")


def load_verdicts(path: str) -> dict:
    out = {}
    for line in open(path, encoding="utf-8"):
        d = json.loads(line)
        key = (d["source"], d["seed_rank"])
        assert key not in out, (path, key)
        out[key] = d
    return out


def agree(verdict: dict, direction: str) -> bool:
    """§13.2 validity: blind call must match the recorded direction."""
    return ((verdict["call"] == "S" and direction == "increase")
            or (verdict["call"] == "R" and direction == "decrease"))


def rendered_inventory() -> tuple[set, set, list]:
    """Same inventory as scripts/freeze_g24a_confa.py step 1."""
    used_ids, used_evs, rendered = set(), set(), []
    for f in sorted(glob.glob("data/items/*.jsonl")):
        if f in (CANDIDATES, OUT):
            continue
        first = open(f, encoding="utf-8").readline()
        if "item_id" not in json.loads(first):
            continue                      # verdict/analysis files
        rendered.append(f)
        for line in open(f, encoding="utf-8"):
            d = json.loads(line)
            used_ids.add(d["item_id"])
            e = d.get("critical_evidence")
            if e:
                used_evs.add(e)
    return used_ids, used_evs, rendered


def main() -> int:
    for p in (POOL_CSV, VALIDITY, RESERVE_VALIDITY, OUT):
        if "results/raw" in p:
            raise SystemExit("REFUSAL: build must not read model output")

    used_ids, used_evs, rendered = rendered_inventory()
    print(f"rendered item files: {len(rendered)}; used ids {len(used_ids)}, "
          f"used evidences {len(used_evs)}")

    active_v = load_verdicts(VALIDITY)
    reserve_v = load_verdicts(RESERVE_VALIDITY)
    assert len(active_v) == 500, len(active_v)

    pool = list(csv.DictReader(open(POOL_CSV, newline="", encoding="utf-8")))
    assert len(pool) == 743, len(pool)

    cands = {}
    for line in open(CANDIDATES, encoding="utf-8"):
        d = json.loads(line)
        cands[d["item_id"]] = d

    # --- selection: validity-gated actives + seed-order reserve swaps ------
    final: dict[str, list] = {}
    for src in ("fever", "scifact"):
        rows = sorted((r for r in pool if r["source"] == src),
                      key=lambda r: int(r["seed_rank_within_source"]))
        act = [r for r in rows if r["role"] == "active"]
        res = [r for r in rows if r["role"] == "reserve"]
        assert len(act) == TARGET[src], (src, len(act))

        kept, invalids = [], []
        for r in act:
            k = (src, int(r["seed_rank_within_source"]))
            v = active_v[k]
            (kept if agree(v, r["direction"]) else invalids).append((r, v))

        valid_res = []
        for r in res:
            k = (src, int(r["seed_rank_within_source"]))
            v = reserve_v.get(k)
            if v is not None and agree(v, r["direction"]):
                valid_res.append((r, v))
        assert len(valid_res) >= len(invalids), \
            (src, f"invalid actives {len(invalids)} > valid reserves "
                  f"{len(valid_res)}")

        entries = [{"row": r, "verdict": v, "replaced": None}
                   for (r, v) in kept]
        for (inv_row, _), (r, v) in zip(invalids,
                                        valid_res[:len(invalids)]):
            entries.append({"row": r, "verdict": v, "replaced": inv_row})
        entries.sort(key=lambda e: int(e["row"]["seed_rank_within_source"]))
        assert len(entries) == TARGET[src]
        final[src] = entries
        print(f"{src}: kept {len(kept)}, invalid active {len(invalids)}, "
              f"valid reserve {len(valid_res)} -> swapped {len(invalids)}")

    # --- materialize -------------------------------------------------------
    items = []
    n_swap = 0
    for src in ("fever", "scifact"):
        for e in final[src]:
            row, v, inv = e["row"], e["verdict"], e["replaced"]
            d = json.loads(json.dumps(cands[row["item_id"]]))   # deep copy
            assert d["item_id"] == row["item_id"]
            assert d["critical_direction"] == row["direction"], \
                (d["item_id"], d["critical_direction"], row["direction"])
            assert d["task_family"] == f"g24a_{src}", d["task_family"]
            assert agree(v, row["direction"]), (d["item_id"], v["call"])
            assert hashlib.sha256(
                norm_claim(d["base_context"]).encode()).hexdigest()[:12] \
                == row["claim_sha"], d["item_id"]
            # freshness (re-assert, freeze semantics)
            assert d["item_id"] not in used_ids, d["item_id"]
            assert d["critical_evidence"] not in used_evs, d["item_id"]

            m = d["meta"]
            assert isinstance(m, dict), d["item_id"]
            assert m.get("stratum") == row["stratum"] or row["stratum"] == "", \
                (d["item_id"], m.get("stratum"), row["stratum"])
            m["pilot"] = "g24a_confa"
            m["confa_role"] = row["role"]
            m["confa_seed_rank"] = int(row["seed_rank_within_source"])
            m["blind_call"] = v["call"]
            if v.get("note"):
                m["blind_note"] = v["note"]
            if inv is not None:
                m["confa_replaced_seed_rank"] = int(
                    inv["seed_rank_within_source"])
                m["confa_replaced_item_id"] = inv["item_id"]
                n_swap += 1
            items.append(d)

    # --- global invariants -------------------------------------------------
    assert len(items) == 500, len(items)
    ids = [d["item_id"] for d in items]
    assert len(set(ids)) == 500, "duplicate item_id"
    claims = [norm_claim(d["base_context"]) for d in items]
    assert len(set(claims)) == 500, "duplicate normalized claim"
    fam = Counter(d["task_family"] for d in items)
    assert fam == Counter({"g24a_fever": 334, "g24a_scifact": 166}), fam
    assert n_swap == 55, n_swap
    dirs = Counter((d["task_family"], d["critical_direction"])
                   for d in items)
    strata = Counter((d["task_family"],
                      d["meta"].get("stratum") or "?") for d in items)
    calls = Counter(d["meta"]["blind_call"] for d in items)

    # --- write + read-back -------------------------------------------------
    with open(OUT, "w", encoding="utf-8") as fh:
        for d in items:
            fh.write(json.dumps(d, ensure_ascii=False) + "\n")
    Path(IDS).write_text(json.dumps(ids, indent=2) + "\n", encoding="utf-8")

    back = [json.loads(l) for l in open(OUT, encoding="utf-8")]
    assert len(back) == 500
    assert [d["item_id"] for d in back] == ids
    assert json.load(open(IDS, encoding="utf-8")) == ids
    for d in back:
        m = d["meta"]
        assert m["pilot"] == "g24a_confa"
        k = (d["task_family"].replace("g24a_", ""), m["confa_seed_rank"])
        v = (active_v if m["confa_role"] == "active" else reserve_v)[k]
        assert v["call"] == m["blind_call"]
        assert agree(v, d["critical_direction"]), d["item_id"]
        assert d["item_id"] not in used_ids
        assert d["critical_evidence"] not in used_evs

    print(f"directions: {dict(dirs)}")
    print(f"strata: {dict(strata)}")
    print(f"blind calls in final 500: {dict(calls)}; swaps: {n_swap}")
    print(f"wrote {OUT} ({len(back)} items) + {IDS} ({len(ids)} ids); "
          "freshness re-asserted (0 id, 0 evidence overlap)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
