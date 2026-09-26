"""Verify G28A row coverage and exact text-history construction against frozen items."""

import argparse
import json
from pathlib import Path

from run_g28a_path import direct, first_judged, first_read, load_data, second, sha

ROOT = Path(__file__).resolve().parents[1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("raw")
    ap.add_argument("--n", type=int, default=200)
    args = ap.parse_args()
    raw = [json.loads(line) for line in Path(args.raw).read_text().splitlines() if line]
    pairs, controls = load_data(ROOT / "data/items/g24a_confb_selected_v1.jsonl")
    pairs = pairs[:args.n]
    assert len(raw) == args.n * 11
    by = {}
    for r in raw:
        key = (r["cfb_id"], r["stage"], r.get("condition", r.get("role")), r.get("final_role"))
        assert key not in by
        assert r["prompt_sha256"] == sha(json.dumps(r["messages"], ensure_ascii=False, sort_keys=True))
        assert 0 <= r["value"] <= 100 and 0 <= r["mass"] <= 1.000001
        by[key] = r
    for p in pairs:
        cid, claim = p["cfb_id"], p["claim"]
        for role, e1 in (("support", p["evidence_s"]), ("refute", p["evidence_r"]),
                         ("irrelevant", controls[cid])):
            r = by[(cid, "initial", role, None)]
            assert r["messages"] == [{"role": "user", "content": first_judged(claim, e1)}]
        for final_role, e2, old_role, e1 in (("support", p["evidence_s"], "refute", p["evidence_r"]),
                                              ("refute", p["evidence_r"], "support", p["evidence_s"])):
            for cond in ("D", "RJ", "IJ", "RR"):
                r = by[(cid, "final", cond, final_role)]
                if cond == "D":
                    expected = [{"role": "user", "content": direct(claim, e2)}]
                elif cond == "RR":
                    expected = [{"role": "user", "content": first_read(claim, e1)},
                                {"role": "assistant", "content": "Understood."},
                                {"role": "user", "content": second(e2)}]
                else:
                    init_role = old_role if cond == "RJ" else "irrelevant"
                    prior = by[(cid, "initial", init_role, None)]
                    expected = prior["messages"] + [
                        {"role": "assistant", "content": prior["assistant_text"]},
                        {"role": "user", "content": second(e2)}]
                assert r["messages"] == expected, (cid, final_role, cond)
    assert len(by) == len(raw)
    print(f"PASS {args.raw}: {args.n} claims, {len(raw)} complete exact cells")


if __name__ == "__main__":
    main()
