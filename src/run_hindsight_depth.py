"""Run one G2 hindsight-depth condition on the frozen 256-unit artifact.

Conditions (see PREREGISTRATION_G2_HINDSIGHT_DEPTH.md):

* ``pos_oob_before`` / ``pos_oob_after``       — Experiment A, exclusion frame
* ``pos_allowed_before`` / ``pos_allowed_after`` — Experiment A, licensed control
* ``evr_oob`` / ``evr_allowed``                — Experiment B, verdict-redacted packet

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
    from .adapters.btf3_hindsight_depth import build_evr, build_positional
    from .run_information_set import (
        SYSTEM_PROMPT,
        _chat_ids,
        boundary_probe,
        parse_probability,
        parse_yesno,
    )
except ImportError:  # direct script execution
    from information_set_schema import file_sha256, load_jsonl
    from adapters.btf3_hindsight_depth import build_evr, build_positional
    from run_information_set import (
        SYSTEM_PROMPT,
        _chat_ids,
        boundary_probe,
        parse_probability,
        parse_yesno,
    )

CONDITIONS = {
    "pos_oob_before": ("positional", "oob", "before"),
    "pos_oob_after": ("positional", "oob", "after"),
    "pos_allowed_before": ("positional", "allowed", "before"),
    "pos_allowed_after": ("positional", "allowed", "after"),
    "evr_oob": ("evr", "oob", None),
    "evr_allowed": ("evr", "allowed", None),
}
PROBE_EXPECTATION = {"oob": "NO", "allowed": "YES"}


def _git_head() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()


def build_prompt(item, kind: str, frame: str, position: str | None) -> tuple[str, dict]:
    if kind == "positional":
        return build_positional(item, frame=frame, position=position), {}
    prompt, redaction = build_evr(item, frame=frame)
    return prompt, {
        "verdict_sentences_removed": redaction.n_removed,
        "clauses_preserved": len(redaction.preserved_clauses),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact", type=Path, default=Path("data/external/review/btf3_temporal_large_replication_v1.jsonl"))
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

    kind, frame, position = CONDITIONS[args.condition]
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

    records = []
    for item in items:
        decision_prompt, extra = build_prompt(item, kind, frame, position)
        probe_prompt = boundary_probe(decision_prompt, expected=expected)
        records.append({
            "record_type": "decision",
            "source_id": item.source_id,
            "independent_unit_id": item.independent_unit_id,
            "condition": args.condition,
            "frame": frame,
            "position": position,
            "prompt_sha256": hashlib.sha256(decision_prompt.encode()).hexdigest(),
            "prompt_ids": _chat_ids(tokenizer, decision_prompt),
            "direction": int(item.reference_context.get("outcome_alignment_sign", 1)),
            "realized_resolution": item.reference_context.get("realized_resolution"),
            **extra,
        })
        records.append({
            "record_type": "boundary_probe",
            "source_id": item.source_id,
            "independent_unit_id": item.independent_unit_id,
            "condition": f"boundary_{args.condition}",
            "frame": frame,
            "expected": expected,
            "prompt_sha256": hashlib.sha256(probe_prompt.encode()).hexdigest(),
            "prompt_ids": _chat_ids(tokenizer, probe_prompt),
        })

    longest = max(len(record["prompt_ids"]) for record in records)
    if longest + 8 > args.max_model_len:
        raise ValueError(f"longest prompt ({longest}) exceeds frozen max_model_len={args.max_model_len}")
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
        SamplingParams(temperature=0.0, max_tokens=8, seed=0),
    )

    metadata = {
        "artifact": str(args.artifact),
        "artifact_sha256": file_sha256(args.artifact),
        "condition": args.condition,
        "experiment": "A_positional" if kind == "positional" else "B_evr",
        "frame": frame,
        "position": position,
        "git_commit": _git_head(),
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

    decision_bad = sum(
        parse_probability(o.outputs[0].text) is None
        for r, o in zip(records, outputs, strict=True) if r["record_type"] == "decision"
    )
    probe_bad = sum(
        parse_yesno(o.outputs[0].text) is None
        for r, o in zip(records, outputs, strict=True) if r["record_type"] == "boundary_probe"
    )
    print(f"wrote {len(records)} rows to {args.out}")
    print(f"longest prompt: {longest} tokens; decision parse failures: {decision_bad}; probe parse failures: {probe_bad}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
