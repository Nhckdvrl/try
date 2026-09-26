"""Prepare label-blind claim/control pairs for local OpenCode material review."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/audits/g28a_irrelevant_control_audit"


def main():
    selected = {r["cfb_id"]: r for r in map(json.loads, (ROOT / "data/items/g24a_confb_selected_v1.jsonl").open())}
    control = {}
    for r in map(json.loads, (ROOT / "data/items/g24a_confb_v1.jsonl").open()):
        if r["meta"]["arm"] == "control":
            control[r["meta"]["cfb_id"]] = r["critical_evidence"]
    assert len(selected) == len(control) == 200 and set(selected) == set(control)
    OUT.mkdir(parents=True, exist_ok=True)
    ids = sorted(selected)
    for batch in range(4):
        rows = [{"id": cid, "claim": selected[cid]["claim"], "sentence": control[cid]}
                for cid in ids[batch * 50:(batch + 1) * 50]]
        path = OUT / f"blind_batch_{batch + 1:02d}.jsonl"
        path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
        print(path, len(rows))


if __name__ == "__main__":
    main()
