"""Run a frozen source-native information-set artifact with strict direct readout."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

try:
    from .information_set_schema import file_sha256, load_jsonl
except ImportError:  # direct script execution
    from information_set_schema import file_sha256, load_jsonl


SYSTEM_PROMPT = (
    "Follow the target information set defined in the task exactly. "
    "Return only the requested answer format and no explanation."
)
CONDITIONS = {
    "oob_without": ("oob_variant", "without_information_prompt"),
    "oob_with": ("oob_variant", "with_information_prompt"),
    "allowed_without": ("admissible_variant", "without_information_prompt"),
    "allowed_with": ("admissible_variant", "with_information_prompt"),
}
_PROBABILITY = re.compile(r"\s*(100(?:\.0+)?|(?:\d{1,2})(?:\.\d+)?)\s*%?\s*")
_YESNO = re.compile(r"\s*(YES|NO)\s*[.!]?\s*", re.IGNORECASE)


def parse_probability(text: str) -> float | None:
    match = _PROBABILITY.fullmatch(text)
    if not match:
        return None
    value = float(match.group(1))
    return value if 0.0 <= value <= 100.0 else None


def parse_yesno(text: str) -> str | None:
    match = _YESNO.fullmatch(text)
    return match.group(1).upper() if match else None


def boundary_probe(prompt: str, *, expected: str) -> str:
    base = prompt.rsplit("\n\nTASK\n", 1)[0]
    return (
        base
        + "\n\nBOUNDARY CHECK\nAt the evaluation point defined above, is the "
        "LATER RESOLUTION PACKET or SEPARATE FACT PACKET part of the target "
        "information set? Return only YES or NO."
    )


def _git_head() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()


def _chat_ids(tokenizer, prompt: str) -> list[int]:
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": prompt},
    ]
    kwargs = dict(tokenize=True, add_generation_prompt=True)
    try:
        encoded = tokenizer.apply_chat_template(messages, enable_thinking=False, **kwargs)
    except TypeError:
        encoded = tokenizer.apply_chat_template(messages, **kwargs)
    ids = encoded["input_ids"] if hasattr(encoded, "keys") else encoded
    if ids and isinstance(ids[0], (list, tuple)):
        ids = ids[0]
    return list(ids)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact", required=True, type=Path)
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
    args = parser.parse_args()

    from transformers import AutoTokenizer
    from vllm import LLM, SamplingParams

    items = load_jsonl(args.artifact)
    tokenizer = AutoTokenizer.from_pretrained(args.model, local_files_only=True)
    records = []
    for item in items:
        variants = {
            "oob_variant": item.oob_variant,
            "admissible_variant": item.admissible_variant,
        }
        for condition, (variant, key) in CONDITIONS.items():
            prompt = variants[variant][key]
            records.append({
                "record_type": "decision",
                "source_id": item.source_id,
                "independent_unit_id": item.independent_unit_id,
                "condition": condition,
                "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
                "prompt_ids": _chat_ids(tokenizer, prompt),
                "direction": int(item.reference_context.get("outcome_alignment_sign", 1)),
                "realized_resolution": item.reference_context.get("realized_resolution"),
            })
        for condition, variant, expected in (
            ("boundary_oob_with", "oob_variant", "NO"),
            ("boundary_allowed_with", "admissible_variant", "YES"),
        ):
            source_prompt = variants[variant]["with_information_prompt"]
            prompt = boundary_probe(source_prompt, expected=expected)
            records.append({
                "record_type": "boundary_probe",
                "source_id": item.source_id,
                "independent_unit_id": item.independent_unit_id,
                "condition": condition,
                "expected": expected,
                "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
                "prompt_ids": _chat_ids(tokenizer, prompt),
            })

    longest = max(len(record["prompt_ids"]) for record in records)
    if longest + 8 > args.max_model_len:
        raise ValueError(
            f"longest prompt ({longest}) exceeds frozen max_model_len={args.max_model_len}"
        )

    llm = LLM(
        model=args.model,
        tensor_parallel_size=args.tp,
        gpu_memory_utilization=args.gpu_frac,
        max_model_len=args.max_model_len,
        dtype="bfloat16",
        disable_log_stats=True,
        enforce_eager=args.enforce_eager,
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

    decision_bad = sum(
        parse_probability(output.outputs[0].text) is None
        for record, output in zip(records, outputs, strict=True)
        if record["record_type"] == "decision"
    )
    probe_bad = sum(
        parse_yesno(output.outputs[0].text) is None
        for record, output in zip(records, outputs, strict=True)
        if record["record_type"] == "boundary_probe"
    )
    print(f"wrote {len(records)} rows to {args.out}")
    print(f"longest prompt: {longest} tokens; decision parse failures: {decision_bad}; probe parse failures: {probe_bad}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
