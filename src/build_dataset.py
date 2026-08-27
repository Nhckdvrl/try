import json, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import gen_legal, gen_controlled

OUT = os.path.join(os.path.dirname(__file__), "..", "data", "items", "items_v1.jsonl")


def main():
    items = gen_legal.build() + gen_controlled.build_all()
    ids = [i.item_id for i in items]
    assert len(set(ids)) == len(ids), "duplicate item_id"
    with open(OUT, "w") as f:
        for i in items:
            f.write(i.to_json() + "\n")
    print(f"wrote {len(items)} items -> {os.path.abspath(OUT)}")
    from collections import Counter
    for k in ("task_family", "exclusion_reason", "critical_direction", "evidence_truth"):
        print(f"  {k}: {dict(Counter(getattr(i, k) for i in items))}")


if __name__ == "__main__":
    main()
