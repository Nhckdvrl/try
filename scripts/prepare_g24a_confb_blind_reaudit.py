"""Create label-blind review batches for an independent ConfB material audit.

No model outputs or existing validity labels are read by this script.
"""

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data/items/g24a_confb_selected_v1.jsonl"
OUT = ROOT / "results/audits/g24a_confb_reaudit"


def main() -> None:
    rows = [json.loads(line) for line in SOURCE.read_text().splitlines() if line]
    assert len(rows) == 200
    assert len({row["cfb_id"] for row in rows}) == 200
    OUT.mkdir(parents=True, exist_ok=True)
    for batch in range(4):
        records = []
        for row in rows[batch * 50 : (batch + 1) * 50]:
            swap = int(hashlib.sha256(row["cfb_id"].encode()).hexdigest(), 16) % 2
            a, b = ((row["evidence_r"], row["evidence_s"]) if swap else
                    (row["evidence_s"], row["evidence_r"]))
            records.append({"id": row["cfb_id"], "claim": row["claim"],
                            "evidence_a": a, "evidence_b": b})
        path = OUT / f"blind_batch_{batch + 1:02d}.jsonl"
        path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in records))
        print(path, len(records))


if __name__ == "__main__":
    main()
