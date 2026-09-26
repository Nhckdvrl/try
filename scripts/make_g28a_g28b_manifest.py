"""Write checksummed provenance manifest for the completed staged path study."""

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results/g28a/g28a_g28b_manifest.json"
TAGS = ("mistral-small-24b", "qwen3-8b", "gemma3-12b", "llama31-8b")
MODEL_PATHS = {
    "mistral-small-24b": "data/mistral_small_24b_hf",
    "qwen3-8b": "/home/xiang/.cache/huggingface/hub/models--Qwen--Qwen3-8B/snapshots/b968826d9c46dd6066d109eabc6255188de91218",
    "gemma3-12b": "/home/xiang/.cache/huggingface/hub/models--google--gemma-3-12b-it/snapshots/96b6f1eccf38110c56df3a15bffe176da04bfd80",
    "llama31-8b": "/home/xiang/.cache/huggingface/hub/models--NousResearch--Meta-Llama-3.1-8B-Instruct/snapshots/d10aef7999a2b5ba950ab3974312feeedbfe0b77",
}


def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def item(path):
    return {"path": str(path.relative_to(ROOT)), "sha256": sha(path),
            "bytes": path.stat().st_size,
            "rows": sum(1 for _ in path.open()) if path.suffix == ".jsonl" else None}


def main():
    sources = [ROOT / "data/items/g24a_confb_selected_v1.jsonl",
               ROOT / "data/items/g24a_confb_v1.jsonl"]
    code = [ROOT / "scripts/run_g28a_path.py", ROOT / "scripts/run_g28b_read_control.py",
            ROOT / "scripts/analyze_g28a_path.py", ROOT / "scripts/analyze_g28b_read_control.py",
            ROOT / "results/discovery/g28a_path_v1_registration.md",
            ROOT / "results/discovery/g28b_read_control_registration.md"]
    raw = []
    for tag in TAGS:
        for stage, count in (("g28a_path_v1", 2200), ("g28b_read_control_v1", 400)):
            path = ROOT / f"results/raw/{tag}_{stage}.jsonl"
            row = item(path)
            assert row["rows"] == count
            row.update({"model_tag": tag, "model_path": MODEL_PATHS[tag], "stage": stage,
                        "planned_model": tag != "llama31-8b"})
            raw.append(row)
    manifest = {
        "incoming_formal_head": "ebe1dd42507e89f0fbea60b1ef1df1230f3baec9",
        "created_date": "2026-09-27",
        "environment": {"name": "verl-clean", "python": "3.12", "torch": "2.8.0+cu128",
                        "vllm": "0.11.0", "transformers": "4.57.6",
                        "host": "fvcrc10", "gpu": "NVIDIA A100 80GB PCIe", "driver": "550.54.14"},
        "failed_planned_model": {"tag": "qwen35-9b", "reason": "qwen3_5 architecture unsupported in driver-compatible vLLM/Transformers stack",
                                 "log": "logs/g28a_path_qwen35-9b.log"},
        "source_files": [item(p) for p in sources],
        "code_and_registration": [item(p) for p in code],
        "raw_files": raw,
    }
    OUT.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n")
    print(OUT, "raw rows", sum(r["rows"] for r in raw))


if __name__ == "__main__":
    main()
