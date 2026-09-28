"""Remove only blind-audit-invalid materials before any G32 model output."""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "data/items/g32_material_audit_v1"
PRE = ROOT / "data/items/g32_pre_audit_60_v1.jsonl"
OUT = ROOT / "data/items/g32_selected_v1.jsonl"


def main():
    source = [json.loads(x) for x in PRE.read_text().splitlines() if x]
    assert len(source) == 60
    judgments = {}
    for batch in range(1, 5):
        inp = [json.loads(x) for x in (BASE / f"input_{batch:02d}.jsonl").read_text().splitlines() if x]
        out = [json.loads(x) for x in (BASE / f"audit_{batch:02d}.jsonl").read_text().splitlines() if x]
        assert len(inp) == len(out) == 15
        assert {x["id"] for x in inp} == {x["id"] for x in out}
        for x in out:
            assert x["id"] not in judgments and isinstance(x["record_only_viable"], bool)
            assert x["record_only_viable"] == all(x[k] for k in ("standalone_claim_ok", "e_contrast_ok", "x_contrast_ok"))
            if not x["record_only_viable"]:
                assert x["issue"].strip()
            judgments[x["id"]] = x
    assert {x["id"] for x in source} == set(judgments)
    valid = [x for x in source if judgments[x["id"]]["record_only_viable"]]
    data = "".join(json.dumps(x, ensure_ascii=False, sort_keys=True) + "\n" for x in valid).encode()
    OUT.write_bytes(data)
    print(json.dumps({"pre_audit_count": len(source), "selected_count": len(valid),
                      "excluded": [x["id"] for x in source if x not in valid],
                      "selected_sha256": hashlib.sha256(data).hexdigest()}, indent=2))


if __name__ == "__main__":
    main()
