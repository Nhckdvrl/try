"""Run the G8 packet-swap condition on the frozen 256-unit artifact.

Only ``swap_with`` (and its boundary probe) is generated: both reference cells,
``oob_with`` and ``oob_without``, are the frozen large-replication output and
are read, not re-run.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess

try:
    from .information_set_schema import file_sha256, load_jsonl
    from .adapters.btf3_packet_swap import PAIRING_SEED, build_swapped, pairing_digest
    from .run_information_set import (
        SYSTEM_PROMPT,
        _chat_ids,
        boundary_probe,
        parse_probability,
        parse_yesno,
    )
except ImportError:  # direct script execution
    from information_set_schema import file_sha256, load_jsonl
    from adapters.btf3_packet_swap import PAIRING_SEED, build_swapped, pairing_digest
    from run_information_set import (
        SYSTEM_PROMPT,
        _chat_ids,
        boundary_probe,
        parse_probability,
        parse_yesno,
    )


def _git_head() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--artifact",
        type=Path,
        default=Path("data/external/review/btf3_temporal_large_replication_v1.jsonl"),
    )
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

    from transformers import AutoTokenizer

    if not args.dry_run:
        from vllm import LLM, SamplingParams

        try:
            from transformers.tokenization_mistral_common import MistralCommonBackend

            if not hasattr(MistralCommonBackend, "is_fast"):
                MistralCommonBackend.is_fast = False
        except ImportError:
            pass

    items = load_jsonl(args.artifact)
    swapped = build_swapped(items)
    digest = pairing_digest(swapped)
    tokenizer = AutoTokenizer.from_pretrained(args.model, local_files_only=True)

    records = []
    for entry in swapped:
        prompt = entry["prompt"]
        records.append({
            "record_type": "decision",
            "independent_unit_id": entry["independent_unit_id"],
            "donor_unit_id": entry["donor_unit_id"],
            "condition": "swap_with",
            "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
            "prompt_ids": _chat_ids(tokenizer, prompt),
            "direction": entry["direction"],
            "donor_direction": entry["donor_direction"],
            "realized_resolution": entry["realized_resolution"],
            "donor_realized_resolution": entry["donor_realized_resolution"],
        })
        probe = boundary_probe(prompt, expected="NO")
        records.append({
            "record_type": "boundary_probe",
            "independent_unit_id": entry["independent_unit_id"],
            "donor_unit_id": entry["donor_unit_id"],
            "condition": "boundary_swap_with",
            "expected": "NO",
            "prompt_sha256": hashlib.sha256(probe.encode()).hexdigest(),
            "prompt_ids": _chat_ids(tokenizer, probe),
        })

    longest = max(len(record["prompt_ids"]) for record in records)
    if longest + 8 > args.max_model_len:
        raise ValueError(f"longest prompt ({longest}) exceeds frozen max_model_len")
    if args.dry_run:
        print(json.dumps({
            "units": len(items),
            "prompts": len(records),
            "longest_prompt_tokens": longest,
            "pairing_sha256": digest,
            "pairing_seed": PAIRING_SEED,
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
        [{"prompt_token_ids": record["prompt_ids"]} for record in records],
        SamplingParams(temperature=0.0, max_tokens=8, seed=0),
    )

    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8") as handle:
        handle.write(json.dumps({
            "record_type": "metadata",
            "artifact": str(args.artifact),
            "artifact_sha256": file_sha256(args.artifact),
            "git_commit": _git_head(),
            "condition": "swap_with",
            "pairing_seed": PAIRING_SEED,
            "pairing_sha256": digest,
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
            result = {key: value for key, value in record.items() if key != "prompt_ids"}
            result["n_prompt_tokens"] = len(record["prompt_ids"])
            result["raw"] = raw
            if record["record_type"] == "decision":
                result["value"] = parse_probability(raw)
            else:
                result["answer"] = parse_yesno(raw)
                result["correct"] = result["answer"] == record["expected"]
            result["model_tag"] = args.tag
            handle.write(json.dumps(result, ensure_ascii=False) + "\n")

    decisions = [r for r, _ in zip(records, outputs) if r["record_type"] == "decision"]
    bad = sum(
        parse_probability(o.outputs[0].text) is None
        for r, o in zip(records, outputs)
        if r["record_type"] == "decision"
    )
    print(json.dumps({"decisions": len(decisions), "unparsed": bad, "out": str(args.out)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
