"""Material-only G32 selection from the pre-audited G31 candidate pool."""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data/items/g31_candidates_v1.jsonl"
OUT = ROOT / "data/items/g32_pre_audit_60_v1.jsonl"
SEED = b"g32-construct-identification-2026-09-28-v1"


def main():
    rows = [json.loads(x) for x in SOURCE.read_text().splitlines() if x]
    assert len(rows) == 80 and len({x["id"] for x in rows}) == 80
    for row in rows:
        assert all(row[k].strip() for k in ("claim", "evidence_s", "evidence_r", "x_s", "x_r"))
        assert row["x_s"] != row["evidence_s"] and row["x_r"] != row["evidence_r"]
    chosen = sorted(rows, key=lambda x: hashlib.sha256(SEED + x["id"].encode()).digest())[:60]
    chosen.sort(key=lambda x: x["id"])
    data = "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in chosen).encode()
    OUT.write_bytes(data)
    print(json.dumps({"source_sha256": hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                      "selected_sha256": hashlib.sha256(data).hexdigest(),
                      "selected_n": len(chosen),
                      "overlap_g31_selected": len({x["id"] for x in chosen} &
                                                  {json.loads(x)["id"] for x in (ROOT / "data/items/g31_selected_v1.jsonl").read_text().splitlines() if x}),
                      "ids": [x["id"] for x in chosen]}, indent=2))


if __name__ == "__main__":
    main()
