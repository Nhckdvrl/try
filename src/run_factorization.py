"""Run one M1/M2/M3 manipulation condition from PREREGISTRATION_G1_FACTORIZATION.md.

Reuses the frozen BTF-3 confirmatory artifact's source content and, for
M3, each model's own already-collected baseline OOB_WITHOUT output. Writes
one manipulation-condition decision + boundary-probe row per unit, in the
same JSONL shape run_information_set.py uses, so the existing analysis
tooling patterns still apply.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess

try:
    from .information_set_schema import file_sha256, load_jsonl
    from .adapters.btf3_factorization import (
        build_m1,
        build_m1_repeat_before,
        build_m2,
        build_m2_v2,
        build_m3,
    )
    from .run_information_set import (
        SYSTEM_PROMPT,
        _chat_ids,
        boundary_probe,
        parse_probability,
        parse_yesno,
    )
except ImportError:  # direct script execution
    from information_set_schema import file_sha256, load_jsonl
    from adapters.btf3_factorization import (
        build_m1,
        build_m1_repeat_before,
        build_m2,
        build_m2_v2,
        build_m3,
    )
    from run_information_set import (
        SYSTEM_PROMPT,
        _chat_ids,
        boundary_probe,
        parse_probability,
        parse_yesno,
    )


def _git_head() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()


def _load_baseline_oob_without(path: Path) -> dict[str, float]:
    values: dict[str, float] = {}
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if row.get("record_type") == "decision" and row.get("condition") == "oob_without":
            if row.get("value") is not None:
                values[row["independent_unit_id"]] = row["value"]
    return values


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact", required=True, type=Path)
    parser.add_argument(
        "--manipulation", required=True,
        choices=("m1", "m2", "m3", "m1_before", "m2v2"),
    )
    parser.add_argument("--baseline", type=Path, help="required for m3: this model's own confirmatory raw results")
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
    args = parser.parse_args()

    if args.manipulation == "m3" and not args.baseline:
        raise ValueError("--baseline is required for m3")

    from transformers import AutoTokenizer
    from vllm import LLM, SamplingParams

    try:
        from transformers.tokenization_mistral_common import MistralCommonBackend

        if not hasattr(MistralCommonBackend, "is_fast"):
            MistralCommonBackend.is_fast = False
    except ImportError:
        pass

    items = load_jsonl(args.artifact)
    tokenizer = AutoTokenizer.from_pretrained(args.model, local_files_only=True)

    baseline_oob_without: dict[str, float] = {}
    if args.manipulation == "m3":
        baseline_oob_without = _load_baseline_oob_without(args.baseline)

    records = []
    skipped_m3_ineligible = []
    for item in items:
        unit = item.independent_unit_id
        direction = int(item.reference_context.get("outcome_alignment_sign", 1))
        realized = item.reference_context.get("realized_resolution")

        if args.manipulation == "m1":
            decision_prompt = build_m1(item)
            probe_prompt = boundary_probe(decision_prompt, expected="NO")
        elif args.manipulation == "m1_before":
            decision_prompt = build_m1_repeat_before(item)
            probe_prompt = boundary_probe(decision_prompt, expected="NO")
        elif args.manipulation == "m2":
            decision_prompt, probe_prompt = build_m2(item)
        elif args.manipulation == "m2v2":
            decision_prompt = build_m2_v2(item)
            probe_prompt = boundary_probe(decision_prompt, expected="NO")
        else:  # m3
            if unit not in baseline_oob_without:
                skipped_m3_ineligible.append(unit)
                continue
            decision_prompt = build_m3(item, baseline_oob_without[unit])
            probe_prompt = boundary_probe(decision_prompt, expected="NO")

        records.append({
            "record_type": "decision",
            "source_id": item.source_id,
            "independent_unit_id": unit,
            "condition": f"oob_with_{args.manipulation}",
            "manipulation": args.manipulation,
            "prompt_sha256": hashlib.sha256(decision_prompt.encode()).hexdigest(),
            "prompt_ids": _chat_ids(tokenizer, decision_prompt),
            "direction": direction,
            "realized_resolution": realized,
        })
        records.append({
            "record_type": "boundary_probe",
            "source_id": item.source_id,
            "independent_unit_id": unit,
            "condition": f"boundary_oob_with_{args.manipulation}",
            "manipulation": args.manipulation,
            "expected": "NO",
            "prompt_sha256": hashlib.sha256(probe_prompt.encode()).hexdigest(),
            "prompt_ids": _chat_ids(tokenizer, probe_prompt),
        })

    longest = max(len(record["prompt_ids"]) for record in records)
    if longest + 8 > args.max_model_len:
        raise ValueError(f"longest prompt ({longest}) exceeds frozen max_model_len={args.max_model_len}")

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
        "manipulation": args.manipulation,
        "baseline": str(args.baseline) if args.baseline else None,
        "m3_skipped_ineligible_units": skipped_m3_ineligible,
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
    if skipped_m3_ineligible:
        print(f"m3 skipped {len(skipped_m3_ineligible)} units with no parsed baseline OOB_WITHOUT: {skipped_m3_ineligible}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
