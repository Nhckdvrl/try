"""Record G31 source, audit, selected-item, and raw-output provenance."""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TAGS = ("qwen3-8b", "gemma3-12b", "llama31-8b")


def file_record(path):
    return {"path": str(path.relative_to(ROOT)), "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
            "bytes": path.stat().st_size}


def main():
    path = ROOT / "results/g31/g31_manifest_v1.json"
    info = {
        "registration": file_record(ROOT / "results/discovery/g31_srp_joint_registration.md"),
        "source_g29_items": file_record(ROOT / "data/items/g29_selected_v1.jsonl"),
        "constructed_candidates": file_record(ROOT / "data/items/g31_candidates_v1.jsonl"),
        "audit_summary": file_record(ROOT / "results/audits/g31_material_audit_v1.md"),
        "selected_items": file_record(ROOT / "data/items/g31_selected_v1.jsonl"),
        "models": {},
    }
    for batch in range(1, 9):
        for kind in ("blind", "audit"):
            source = ROOT / f"data/items/g31_blind_audit_v1/{kind}_{batch:02d}.jsonl"
            info[f"{kind}_{batch:02d}"] = file_record(source)
    for tag in TAGS:
        source = ROOT / f"results/raw/{tag}_g31_srp_joint_v1.jsonl"
        info["models"][tag] = file_record(source)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(info, indent=2) + "\n")
    print(path)


if __name__ == "__main__":
    main()
