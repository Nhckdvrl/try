"""Run one G3 exclusion-reason condition on the frozen 256-unit artifact.

Conditions are ``reason_<arm>_<cell>`` for ``arm`` in {bare, unreliable,
procedural} and ``cell`` in {with, without}. The ``temporal`` arm is not run:
its prompts are byte-identical to the frozen large-replication out-of-set
prompts and are read from that round's output.

Output shape, decoding, parsing, and boundary probes are identical to
``run_information_set.py``; only the prompt construction differs.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess

try:
    from .information_set_schema import file_sha256, load_jsonl
    from .adapters.btf3_exclusion_reason import ARMS, build, reason_sentence
    from .run_information_set import (
        SYSTEM_PROMPT,
        _chat_ids,
        boundary_probe,
        parse_probability,
        parse_yesno,
    )
except ImportError:  # direct script execution
    from information_set_schema import file_sha256, load_jsonl
    from adapters.btf3_exclusion_reason import ARMS, build, reason_sentence
    from run_information_set import (
        SYSTEM_PROMPT,
        _chat_ids,
        boundary_probe,
        parse_probability,
        parse_yesno,
    )

RUNNABLE_ARMS = tuple(arm for arm in ARMS if arm != "temporal")
CONDITIONS = {
    f"reason_{arm}_{cell}": (arm, cell)
    for arm in RUNNABLE_ARMS
    for cell in ("with", "without")
}


def _git_head() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--artifact",
        type=Path,
        default=Path("data/external/review/btf3_temporal_large_replication_v1.jsonl"),
    )
    parser.add_argument("--condition", required=True, choices=sorted(CONDITIONS))
    parser.add_argument("--model", required=True)
    parser.add_argument("--model-id", required=True)
    parser.add_argument("--model-revision", required=True)
    parser.add_argument("--tag", required=True)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--tp", type=int, default=1)
    parser.add_argument("--gpu-frac", type=float, default=0.85)
    parser.add_argument("--max-model-len", type=int, default=8192)
    parser.add_argument("--max-num-seqs", type=int, default=0)
    parser.add_argument("--enforce-eager", action="store_true")
    parser.add_argument("--tokenizer-mode", choices=("auto", "hf", "slow", "mistral"), default="auto")
    parser.add_argument("--dry-run", action="store_true", help="build and count prompts without loading a model")
    args = parser.parse_args()

    arm, cell = CONDITIONS[args.condition]

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
    tokenizer = AutoTokenizer.from_pretrained(args.model, local_files_only=True)

    records = []
    for item in items:
        decision_prompt = build(item, arm=arm, cell=cell)
        records.append({
            "record_type": "decision",
            "source_id": item.source_id,
            "independent_unit_id": item.independent_unit_id,
            "condition": args.condition,
            "arm": arm,
            "cell": cell,
            "prompt_sha256": hashlib.sha256(decision_prompt.encode()).hexdigest(),
            "prompt_ids": _chat_ids(tokenizer, decision_prompt),
            "direction": int(item.reference_context.get("outcome_alignment_sign", 1)),
            "realized_resolution": item.reference_context.get("realized_resolution"),
        })
        # Recognition is probed on the WITH cell only, matching every earlier
        # round; the probe wording itself is inherited unchanged.
        if cell == "with":
            probe_prompt = boundary_probe(decision_prompt, expected="NO")
            records.append({
                "record_type": "boundary_probe",
                "source_id": item.source_id,
                "independent_unit_id": item.independent_unit_id,
                "condition": f"boundary_{args.condition}",
                "arm": arm,
                "expected": "NO",
                "prompt_sha256": hashlib.sha256(probe_prompt.encode()).hexdigest(),
                "prompt_ids": _chat_ids(tokenizer, probe_prompt),
            })

    longest = max(len(record["prompt_ids"]) for record in records)
    if longest + 8 > args.max_model_len:
        raise ValueError(f"longest prompt ({longest}) exceeds frozen max_model_len={args.max_model_len}")
    if args.dry_run:
        print(json.dumps({
            "condition": args.condition,
            "arm": arm,
            "cell": cell,
            "units": len(items),
            "prompts": len(records),
            "longest_prompt_tokens": longest,
        }, indent=2))
        return 0

    llm = LLM(
        model=args.model,
        tensor_parallel_size=args.tp,
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

    metadata = {
        "artifact": str(args.artifact),
        "artifact_sha256": file_sha256(args.artifact),
        "git_commit": _git_head(),
        "condition": args.condition,
        "arm": arm,
        "cell": cell,
        "reason_sentence": reason_sentence(arm),
        "model_id": args.model_id,
        "model_revision": args.model_revision,
        "model_path": args.model,
        "model_tag": args.tag,
        "system_prompt": SYSTEM_PROMPT,
        "temperature": 0.0,
        "max_tokens": 8,
        "max_model_len": args.max_model_len,
        "vllm_tokenizer_mode": args.tokenizer_mode,
        "longest_prompt_tokens": longest,
        "readout": "strict_greedy_probability_0_100_and_yes_no",
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8") as handle:
        handle.write(json.dumps({"record_type": "metadata", **metadata}, ensure_ascii=False) + "\n")
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

    decisions = [
        (record, output)
        for record, output in zip(records, outputs, strict=True)
        if record["record_type"] == "decision"
    ]
    bad = sum(parse_probability(output.outputs[0].text) is None for _, output in decisions)
    print(json.dumps({
        "condition": args.condition,
        "decisions": len(decisions),
        "unparsed": bad,
        "out": str(args.out),
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
