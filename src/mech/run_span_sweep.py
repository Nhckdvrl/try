"""Run the G6 layer-window masking sweep on the frozen 256-unit artifact.

For each unit this produces, on one model:

* one **unmasked** HF reference answer, so the analysis never has to assume the
  HF path reproduces the vLLM path — it measures the disagreement instead;
* one answer per suffix window ``[floor(f*L), L)``, with the packet's tokens
  blocked from every query position at or after the ``TASK`` header;
* one answer under the **wrong-span** control at full depth: the same number of
  tokens blocked, taken from the background text immediately preceding the
  packet.

Prompts come from the frozen artifact. Decoding is greedy at temperature 0 with
the frozen strict numeric readout.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

import torch  # noqa: E402

from information_set_schema import file_sha256, load_jsonl  # noqa: E402
from mech.span_mask import (  # noqa: E402
    generate_masked,
    plan_span,
    plan_wrong_span,
    read_probability,
)

FRACTIONS = (0.0, 0.125, 0.25, 0.375, 0.5, 0.625, 0.75, 0.875)


def _git_head() -> str:
    return subprocess.check_output(["git", "rev-parse", "HEAD"], text=True).strip()


def _n_layers(model) -> int:
    from mech.span_mask import _layers

    return len(_layers(model))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--artifact",
        type=Path,
        default=ROOT / "data/external/review/btf3_temporal_large_replication_v1.jsonl",
    )
    parser.add_argument("--model", required=True)
    parser.add_argument("--model-id", required=True)
    parser.add_argument("--model-revision", required=True)
    parser.add_argument("--tag", required=True)
    parser.add_argument("--out", required=True, type=Path)
    parser.add_argument("--limit", type=int, default=0, help="0 = all units")
    parser.add_argument("--max-new-tokens", type=int, default=4)
    parser.add_argument("--dtype", default="bfloat16")
    parser.add_argument("--attn", default="sdpa", choices=("sdpa", "eager"))
    args = parser.parse_args()

    from transformers import AutoModelForCausalLM, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(args.model, local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        local_files_only=True,
        dtype=getattr(torch, args.dtype),
        device_map="cuda",
        attn_implementation=args.attn,
    ).eval()
    depth = _n_layers(model)
    windows = {f: (int(f * depth), depth) for f in FRACTIONS}

    items = load_jsonl(args.artifact)
    if args.limit:
        items = items[: args.limit]

    args.out.parent.mkdir(parents=True, exist_ok=True)
    started = time.time()
    with args.out.open("w", encoding="utf-8") as handle:
        handle.write(json.dumps({
            "record_type": "metadata",
            "artifact": str(args.artifact),
            "artifact_sha256": file_sha256(args.artifact),
            "git_commit": _git_head(),
            "model_id": args.model_id,
            "model_revision": args.model_revision,
            "model_path": args.model,
            "model_tag": args.tag,
            "n_layers": depth,
            "windows": {str(f): list(w) for f, w in windows.items()},
            "dtype": args.dtype,
            "attn_implementation": args.attn,
            "max_new_tokens": args.max_new_tokens,
            "temperature": 0.0,
            "readout": "strict_greedy_probability_0_100",
        }) + "\n")

        for index, item in enumerate(items):
            prompt = item.oob_variant["with_information_prompt"]
            plan = plan_span(tokenizer, prompt)
            control = plan_wrong_span(tokenizer, prompt)
            base = {
                "independent_unit_id": item.independent_unit_id,
                "direction": int(item.reference_context.get("outcome_alignment_sign", 1)),
                "n_prompt_tokens": plan.n_tokens,
                "n_packet_tokens": len(plan.packet_tokens),
                "model_tag": args.tag,
            }

            raw = generate_masked(
                model, tokenizer, plan, max_new_tokens=args.max_new_tokens, apply_mask=False
            )
            handle.write(json.dumps({
                "record_type": "unmasked", **base, "raw": raw, "value": read_probability(raw)
            }, ensure_ascii=False) + "\n")

            for fraction, window in windows.items():
                raw = generate_masked(
                    model,
                    tokenizer,
                    plan,
                    max_new_tokens=args.max_new_tokens,
                    window=None if fraction == 0.0 else window,
                )
                handle.write(json.dumps({
                    "record_type": "masked",
                    **base,
                    "fraction": fraction,
                    "window": list(window),
                    "raw": raw,
                    "value": read_probability(raw),
                }, ensure_ascii=False) + "\n")

            raw = generate_masked(
                model, tokenizer, control, max_new_tokens=args.max_new_tokens
            )
            handle.write(json.dumps({
                "record_type": "wrong_span",
                **base,
                "n_control_tokens": len(control.packet_tokens),
                "raw": raw,
                "value": read_probability(raw),
            }, ensure_ascii=False) + "\n")

            handle.flush()
            if (index + 1) % 10 == 0:
                rate = (time.time() - started) / (index + 1)
                print(f"{index + 1}/{len(items)}  {rate:.1f}s/unit", flush=True)

    print(json.dumps({"units": len(items), "layers": depth, "out": str(args.out)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
