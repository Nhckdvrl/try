"""Run G11's verdict-redacted foreign-packet condition."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess

try:
    from .information_set_schema import file_sha256, load_jsonl
    from .adapters.btf3_packet_swap import PAIRING_SEED, pairing_digest
    from .adapters.btf3_redacted_swap import build_redacted_swapped
    from .run_information_set import SYSTEM_PROMPT, _chat_ids, boundary_probe, parse_probability, parse_yesno
except ImportError:
    from information_set_schema import file_sha256, load_jsonl
    from adapters.btf3_packet_swap import PAIRING_SEED, pairing_digest
    from adapters.btf3_redacted_swap import build_redacted_swapped
    from run_information_set import SYSTEM_PROMPT, _chat_ids, boundary_probe, parse_probability, parse_yesno


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact", type=Path, default=Path("data/external/review/btf3_temporal_large_replication_v1.jsonl"))
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
    records = build_redacted_swapped(items)
    digest = pairing_digest(records)
    tokenizer = AutoTokenizer.from_pretrained(args.model, local_files_only=True)
    prompts = []
    for entry in records:
        decision = entry["prompt"]
        prompts.append({
            "record_type": "decision", "independent_unit_id": entry["independent_unit_id"],
            "donor_unit_id": entry["donor_unit_id"], "condition": "redacted_swap_with",
            "prompt_sha256": hashlib.sha256(decision.encode()).hexdigest(),
            "prompt_ids": _chat_ids(tokenizer, decision), "direction": entry["direction"],
            "donor_direction": entry["donor_direction"],
            "realized_resolution": entry["realized_resolution"],
            "donor_realized_resolution": entry["donor_realized_resolution"],
            "verdict_sentences_removed": entry["verdict_sentences_removed"],
            "clauses_preserved": entry["clauses_preserved"],
        })
        probe = boundary_probe(decision, expected="NO")
        prompts.append({
            "record_type": "boundary_probe", "independent_unit_id": entry["independent_unit_id"],
            "donor_unit_id": entry["donor_unit_id"], "condition": "boundary_redacted_swap_with",
            "expected": "NO", "prompt_sha256": hashlib.sha256(probe.encode()).hexdigest(),
            "prompt_ids": _chat_ids(tokenizer, probe),
        })

    longest = max(len(r["prompt_ids"]) for r in prompts)
    audit = {
        "units": len(items), "prompts": len(prompts), "longest_prompt_tokens": longest,
        "pairing_seed": PAIRING_SEED, "pairing_sha256": digest,
        "removed_sentences": sum(r["verdict_sentences_removed"] for r in records),
        "unchanged_packets": sum(r["verdict_sentences_removed"] == 0 for r in records),
    }
    if longest + 8 > args.max_model_len:
        raise ValueError(f"longest prompt ({longest}) exceeds max_model_len")
    if args.dry_run:
        print(json.dumps(audit, indent=2))
        return 0

    llm = LLM(model=args.model, gpu_memory_utilization=args.gpu_frac,
              max_model_len=args.max_model_len, dtype="bfloat16", disable_log_stats=True,
              enforce_eager=args.enforce_eager, tokenizer_mode=args.tokenizer_mode,
              **({"max_num_seqs": args.max_num_seqs} if args.max_num_seqs else {}))
    outputs = llm.generate([{"prompt_token_ids": r["prompt_ids"]} for r in prompts],
                           SamplingParams(temperature=0.0, max_tokens=8, seed=0))
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8") as handle:
        handle.write(json.dumps({
            "record_type": "metadata", "artifact": str(args.artifact),
            "artifact_sha256": file_sha256(args.artifact),
            "git_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip(),
            "condition": "redacted_swap_with", "pairing_seed": PAIRING_SEED,
            "pairing_sha256": digest, "model_id": args.model_id,
            "model_revision": args.model_revision, "model_path": args.model,
            "model_tag": args.tag, "system_prompt": SYSTEM_PROMPT,
            "temperature": 0.0, "max_tokens": 8, "max_model_len": args.max_model_len,
            "audit": audit,
        }, ensure_ascii=False) + "\n")
        for record, output in zip(prompts, outputs, strict=True):
            raw = output.outputs[0].text
            result = {k: v for k, v in record.items() if k != "prompt_ids"}
            result["raw"] = raw
            result["n_prompt_tokens"] = len(record["prompt_ids"])
            if record["record_type"] == "decision":
                result["value"] = parse_probability(raw)
            else:
                result["answer"] = parse_yesno(raw)
                result["correct"] = result["answer"] == record["expected"]
            result["model_tag"] = args.tag
            handle.write(json.dumps(result, ensure_ascii=False) + "\n")
    print(json.dumps(audit))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

