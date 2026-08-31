"""Run one G10 few-shot condition on the frozen 256-unit artifact.

Conditions: ``fewshot_with`` / ``fewshot_without``. Both reference cells are the
frozen large-replication output and are not re-run.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess

try:
    from .information_set_schema import file_sha256, load_jsonl
    from .adapters.btf3_fewshot import build, build_prefix, prefix_digest, select_demonstrations
    from .run_information_set import (
        SYSTEM_PROMPT,
        _chat_ids,
        boundary_probe,
        parse_probability,
        parse_yesno,
    )
except ImportError:  # direct script execution
    from information_set_schema import file_sha256, load_jsonl
    from adapters.btf3_fewshot import build, build_prefix, prefix_digest, select_demonstrations
    from run_information_set import (
        SYSTEM_PROMPT,
        _chat_ids,
        boundary_probe,
        parse_probability,
        parse_yesno,
    )

CELLS = {"fewshot_with": "with_information_prompt", "fewshot_without": "without_information_prompt"}
USED_ARTIFACTS = (
    "btf3_temporal_large_replication_v1.jsonl",
    "btf3_temporal_confirmatory_v1.jsonl",
    "btf3_temporal_pilot_v0.2r2.jsonl",
)


def _git_head() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()


def used_unit_ids(review_dir: Path) -> set[str]:
    used: set[str] = set()
    for name in USED_ARTIFACTS:
        path = review_dir / name
        if path.exists():
            used |= {
                json.loads(line)["independent_unit_id"]
                for line in path.read_text(encoding="utf-8").splitlines()
                if line
            }
    return used


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--artifact",
        type=Path,
        default=Path("data/external/review/btf3_temporal_large_replication_v1.jsonl"),
    )
    parser.add_argument(
        "--source",
        type=Path,
        default=Path("data/external/raw/btf3/btf3_binary_questions_and_forecasts.parquet"),
    )
    parser.add_argument("--condition", required=True, choices=sorted(CELLS))
    parser.add_argument("--model", required=True)
    parser.add_argument("--model-id", required=True)
    parser.add_argument("--model-revision", required=True)
    parser.add_argument("--tag", required=True)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--gpu-frac", type=float, default=0.85)
    parser.add_argument("--max-model-len", type=int, default=8192)
    parser.add_argument("--max-num-seqs", type=int, default=0)
    parser.add_argument("--enforce-eager", action="store_true")
    parser.add_argument("--tokenizer-mode", choices=("auto", "hf", "slow", "mistral"), default="auto")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    import pandas as pd
    from transformers import AutoTokenizer

    if not args.dry_run:
        from vllm import LLM, SamplingParams

        try:
            from transformers.tokenization_mistral_common import MistralCommonBackend

            if not hasattr(MistralCommonBackend, "is_fast"):
                MistralCommonBackend.is_fast = False
        except ImportError:
            pass

    rows = pd.read_parquet(args.source).to_dict("records")
    demonstrations = select_demonstrations(rows, used_unit_ids(args.artifact.parent))
    prefix = build_prefix(demonstrations)
    digest = prefix_digest(prefix)

    items = load_jsonl(args.artifact)
    tokenizer = AutoTokenizer.from_pretrained(args.model, local_files_only=True)
    key = CELLS[args.condition]

    records = []
    for item in items:
        prompt = build(item.oob_variant[key], prefix)
        records.append({
            "record_type": "decision",
            "independent_unit_id": item.independent_unit_id,
            "condition": args.condition,
            "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
            "prompt_ids": _chat_ids(tokenizer, prompt),
            "direction": int(item.reference_context.get("outcome_alignment_sign", 1)),
            "realized_resolution": item.reference_context.get("realized_resolution"),
        })
        if args.condition == "fewshot_with":
            probe = boundary_probe(prompt, expected="NO")
            records.append({
                "record_type": "boundary_probe",
                "independent_unit_id": item.independent_unit_id,
                "condition": "boundary_fewshot_with",
                "expected": "NO",
                "prompt_sha256": hashlib.sha256(probe.encode()).hexdigest(),
                "prompt_ids": _chat_ids(tokenizer, probe),
            })

    longest = max(len(r["prompt_ids"]) for r in records)
    if longest + 8 > args.max_model_len:
        raise ValueError(f"longest prompt ({longest}) exceeds frozen max_model_len")
    if args.dry_run:
        print(json.dumps({
            "condition": args.condition,
            "prompts": len(records),
            "longest_prompt_tokens": longest,
            "prefix_sha256": digest,
            "demonstration_ids": [str(d["question_id"]) for d in demonstrations],
        }, indent=2))
        return 0

    llm = LLM(
        model=args.model,
        gpu_memory_utilization=args.gpu_frac,
        max_model_len=args.max_model_len,
        dtype="bfloat16",
        disable_log_stats=True,
        enforce_eager=args.enforce_eager,
        tokenizer_mode=args.tokenizer_mode,
        **({"max_num_seqs": args.max_num_seqs} if args.max_num_seqs else {}),
    )
    outputs = llm.generate(
        [{"prompt_token_ids": r["prompt_ids"]} for r in records],
        SamplingParams(temperature=0.0, max_tokens=8, seed=0),
    )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8") as handle:
        handle.write(json.dumps({
            "record_type": "metadata",
            "artifact": str(args.artifact),
            "artifact_sha256": file_sha256(args.artifact),
            "git_commit": _git_head(),
            "condition": args.condition,
            "prefix_sha256": digest,
            "demonstration_ids": [str(d["question_id"]) for d in demonstrations],
            "demonstration_answers": [int(round(float(d["sota_forecast_probability"]))) for d in demonstrations],
            "demonstration_resolutions": [float(d["resolution"]) for d in demonstrations],
            "model_id": args.model_id,
            "model_revision": args.model_revision,
            "model_path": args.model,
            "model_tag": args.tag,
            "system_prompt": SYSTEM_PROMPT,
            "temperature": 0.0,
            "max_tokens": 8,
            "max_model_len": args.max_model_len,
            "longest_prompt_tokens": longest,
            "readout": "strict_greedy_probability_0_100_and_yes_no",
        }, ensure_ascii=False) + "\n")
        for record, output in zip(records, outputs, strict=True):
            raw = output.outputs[0].text
            result = {k: v for k, v in record.items() if k != "prompt_ids"}
            result["n_prompt_tokens"] = len(record["prompt_ids"])
            result["raw"] = raw
            if record["record_type"] == "decision":
                result["value"] = parse_probability(raw)
            else:
                result["answer"] = parse_yesno(raw)
                result["correct"] = result["answer"] == record["expected"]
            result["model_tag"] = args.tag
            handle.write(json.dumps(result, ensure_ascii=False) + "\n")

    bad = sum(
        parse_probability(o.outputs[0].text) is None
        for r, o in zip(records, outputs)
        if r["record_type"] == "decision"
    )
    print(json.dumps({"condition": args.condition, "unparsed": bad, "out": str(args.out)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
