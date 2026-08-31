"""Run one G5 deliberation condition on the frozen 256-unit artifact.

Conditions are ``delib_<arm>_<frame>_<cell>`` for ``arm`` in {cot, state},
``frame`` in {oob, allowed}, ``cell`` in {with, without}. The ``direct`` arm is
not run: its prompts are the frozen artifact's own and are read from the
large-replication output.

Decision records generate up to ``--max-tokens`` (frozen at 640) and are read
by the strict last-``ANSWER: N``-line parser. Boundary probes keep the
inherited 8-token YES/NO readout so recognition stays comparable to every
earlier round.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess

try:
    from .information_set_schema import file_sha256, load_jsonl
    from .adapters.btf3_deliberation import TASK_BLOCKS, build, parse_answer_line
    from .run_information_set import SYSTEM_PROMPT, _chat_ids, boundary_probe, parse_yesno
except ImportError:  # direct script execution
    from information_set_schema import file_sha256, load_jsonl
    from adapters.btf3_deliberation import TASK_BLOCKS, build, parse_answer_line
    from run_information_set import SYSTEM_PROMPT, _chat_ids, boundary_probe, parse_yesno

RUNNABLE_ARMS = ("cot", "state")
CONDITIONS = {
    f"delib_{arm}_{frame}_{cell}": (arm, frame, cell)
    for arm in RUNNABLE_ARMS
    for frame in ("oob", "allowed")
    for cell in ("with", "without")
}
PROBE_EXPECTATION = {"oob": "NO", "allowed": "YES"}
# The deliberation system prompt cannot forbid explanation, since the arms ask
# for one. Everything else is the frozen system prompt, verbatim.
DELIBERATION_SYSTEM_PROMPT = (
    "Follow the target information set defined in the task exactly. "
    "Follow the requested answer format exactly."
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
    parser.add_argument("--condition", required=True, choices=sorted(CONDITIONS))
    parser.add_argument("--model", required=True)
    parser.add_argument("--model-id", required=True)
    parser.add_argument("--model-revision", required=True)
    parser.add_argument("--tag", required=True)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--tp", type=int, default=1)
    parser.add_argument("--gpu-frac", type=float, default=0.85)
    parser.add_argument("--max-model-len", type=int, default=8192)
    parser.add_argument("--max-tokens", type=int, default=640, help="frozen at 640")
    parser.add_argument("--max-num-seqs", type=int, default=0)
    parser.add_argument("--enforce-eager", action="store_true")
    parser.add_argument("--tokenizer-mode", choices=("auto", "hf", "slow", "mistral"), default="auto")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--keep-full-raw",
        action="store_true",
        help="store the whole completion instead of its last 600 characters. "
             "Storage only: values are parsed from the full text either way, so "
             "no estimand changes.",
    )
    args = parser.parse_args()

    arm, frame, cell = CONDITIONS[args.condition]
    expected = PROBE_EXPECTATION[frame]

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

    def chat(prompt: str, system: str) -> list[int]:
        messages = [{"role": "system", "content": system}, {"role": "user", "content": prompt}]
        kwargs = dict(tokenize=True, add_generation_prompt=True)
        try:
            encoded = tokenizer.apply_chat_template(messages, enable_thinking=False, **kwargs)
        except TypeError:
            encoded = tokenizer.apply_chat_template(messages, **kwargs)
        ids = encoded["input_ids"] if hasattr(encoded, "keys") else encoded
        if ids and isinstance(ids[0], (list, tuple)):
            ids = ids[0]
        return list(ids)

    records = []
    for item in items:
        decision_prompt = build(item, arm=arm, frame=frame, cell=cell)
        records.append({
            "record_type": "decision",
            "source_id": item.source_id,
            "independent_unit_id": item.independent_unit_id,
            "condition": args.condition,
            "arm": arm,
            "frame": frame,
            "cell": cell,
            "prompt_sha256": hashlib.sha256(decision_prompt.encode()).hexdigest(),
            "prompt_ids": chat(decision_prompt, DELIBERATION_SYSTEM_PROMPT),
            "max_tokens": args.max_tokens,
            "direction": int(item.reference_context.get("outcome_alignment_sign", 1)),
            "realized_resolution": item.reference_context.get("realized_resolution"),
        })
        if cell == "with":
            probe_prompt = boundary_probe(decision_prompt, expected=expected)
            records.append({
                "record_type": "boundary_probe",
                "source_id": item.source_id,
                "independent_unit_id": item.independent_unit_id,
                "condition": f"boundary_{args.condition}",
                "arm": arm,
                "frame": frame,
                "expected": expected,
                "prompt_sha256": hashlib.sha256(probe_prompt.encode()).hexdigest(),
                "prompt_ids": chat(probe_prompt, SYSTEM_PROMPT),
                "max_tokens": 8,
            })

    longest = max(len(record["prompt_ids"]) for record in records)
    if longest + args.max_tokens > args.max_model_len:
        raise ValueError(
            f"longest prompt ({longest}) + max_tokens ({args.max_tokens}) exceeds "
            f"frozen max_model_len={args.max_model_len}"
        )
    if args.dry_run:
        print(json.dumps({
            "condition": args.condition,
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
        [
            SamplingParams(temperature=0.0, max_tokens=record["max_tokens"], seed=0)
            for record in records
        ],
    )

    metadata = {
        "artifact": str(args.artifact),
        "artifact_sha256": file_sha256(args.artifact),
        "git_commit": _git_head(),
        "condition": args.condition,
        "arm": arm,
        "frame": frame,
        "cell": cell,
        "task_block": TASK_BLOCKS[arm],
        "model_id": args.model_id,
        "model_revision": args.model_revision,
        "model_path": args.model,
        "model_tag": args.tag,
        "system_prompt": DELIBERATION_SYSTEM_PROMPT,
        "probe_system_prompt": SYSTEM_PROMPT,
        "temperature": 0.0,
        "max_tokens": args.max_tokens,
        "max_model_len": args.max_model_len,
        "vllm_tokenizer_mode": args.tokenizer_mode,
        "longest_prompt_tokens": longest,
        "readout": "last_ANSWER_line_0_100_and_yes_no",
        "stored_raw": "full" if args.keep_full_raw else "last_600_chars",
    }
    args.out.parent.mkdir(parents=True, exist_ok=True)
    with args.out.open("w", encoding="utf-8") as handle:
        handle.write(json.dumps({"record_type": "metadata", **metadata}, ensure_ascii=False) + "\n")
        for record, output in zip(records, outputs, strict=True):
            raw = output.outputs[0].text
            result = {key: value for key, value in record.items() if key != "prompt_ids"}
            result["n_prompt_tokens"] = len(record["prompt_ids"])
            result["n_completion_tokens"] = len(output.outputs[0].token_ids)
            result["finish_reason"] = output.outputs[0].finish_reason
            if record["record_type"] == "decision":
                result["raw"] = raw if args.keep_full_raw else raw[-600:]
                result["value"] = parse_answer_line(raw)
            else:
                result["raw"] = raw
                result["answer"] = parse_yesno(raw)
                result["correct"] = result["answer"] == record["expected"]
            result["model_tag"] = args.tag
            handle.write(json.dumps(result, ensure_ascii=False) + "\n")

    decisions = [
        (record, output)
        for record, output in zip(records, outputs, strict=True)
        if record["record_type"] == "decision"
    ]
    bad = sum(parse_answer_line(output.outputs[0].text) is None for _, output in decisions)
    truncated = sum(output.outputs[0].finish_reason == "length" for _, output in decisions)
    print(json.dumps({
        "condition": args.condition,
        "decisions": len(decisions),
        "unparsed": bad,
        "truncated": truncated,
        "out": str(args.out),
    }))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
