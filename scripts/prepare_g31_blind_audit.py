"""Merge G31 constructed candidates and generate role-blind audit batches."""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "data/items/g29_selected_v1.jsonl"
OUT = ROOT / "data/items/g31_candidates_v1.jsonl"
AUDIT = ROOT / "data/items/g31_blind_audit_v1"
KEYS = {"id", "case_id", "claim", "evidence_s", "evidence_r", "x_s", "x_r", "x_i"}


def main():
    source = [json.loads(line) for line in SRC.read_text().splitlines()]
    assert len(source) == 80 and len({x["id"] for x in source}) == 80
    candidates = []
    for batch in range(1, 9):
        path = ROOT / f"data/items/g31_candidates_batch_{batch:02d}.jsonl"
        rows = [json.loads(line) for line in path.read_text().splitlines()]
        assert len(rows) == 10, (batch, len(rows))
        for row, ref in zip(rows, source[(batch - 1) * 10:batch * 10]):
            assert set(row) == KEYS, (batch, row.get("id"), set(row))
            assert all(row[k] == ref[k] for k in
                       ("id", "case_id", "claim", "evidence_s", "evidence_r"))
            assert all(isinstance(row[k], str) and row[k].strip()
                       for k in ("x_s", "x_r", "x_i"))
            candidates.append(row)
    OUT.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in candidates))
    AUDIT.mkdir(parents=True, exist_ok=True)
    for batch in range(8):
        blind = []
        for row in candidates[batch * 10:(batch + 1) * 10]:
            swap_x = int(hashlib.sha256((row["id"] + "X").encode()).hexdigest(), 16) % 2
            swap_e = int(hashlib.sha256((row["id"] + "E").encode()).hexdigest(), 16) % 2
            blind.append({
                "id": row["id"], "claim": row["claim"],
                "note_a": row["x_r"] if swap_x else row["x_s"],
                "note_b": row["x_s"] if swap_x else row["x_r"],
                "note_i": row["x_i"],
                "evidence_a": row["evidence_r"] if swap_e else row["evidence_s"],
                "evidence_b": row["evidence_s"] if swap_e else row["evidence_r"],
            })
        (AUDIT / f"blind_{batch+1:02d}.jsonl").write_text(
            "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in blind))
    print(f"merged {len(candidates)} candidates; sha256={hashlib.sha256(OUT.read_bytes()).hexdigest()}")


if __name__ == "__main__":
    main()
