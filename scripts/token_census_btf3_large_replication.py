#!/usr/bin/env python3
"""Complete pre-run token census for BTF-3 Large Replication v1.

Counts every prompt of every cell for every frozen model's exact chat template
-- 256 units x (4 decision cells + 2 boundary probes) x 3 tokenizers -- with no
sampling. Fails closed if any prompt plus the frozen 8-token output allowance
would exceed max_model_len; truncation is never permitted.

This loads tokenizers only. No model weights, no GPU, and no generation.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from information_set_schema import load_jsonl  # noqa: E402
from run_information_set import CONDITIONS, _chat_ids, boundary_probe  # noqa: E402

DEFAULT_MODELS = {
    "qwen35-9b": "/var/tmp/xiang-isr-models/qwen35-9b",
    "gemma3-12b": "/var/tmp/xiang-isr-models/gemma3-12b",
    "mistral-small-24b": "/var/tmp/xiang-isr-models/mistral-small-24b",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact", type=Path, default=Path("data/external/review/btf3_temporal_large_replication_v1.jsonl"))
    parser.add_argument("--max-model-len", type=int, default=8192)
    parser.add_argument("--max-tokens", type=int, default=8)
    parser.add_argument("--model", action="append", default=None, help="tag=path, repeatable")
    parser.add_argument("--out", type=Path, default=Path("results/btf3_large_replication_v1_token_census.json"))
    args = parser.parse_args()

    models = DEFAULT_MODELS if not args.model else dict(spec.split("=", 1) for spec in args.model)

    from transformers import AutoTokenizer

    items = load_jsonl(args.artifact)
    prompts: list[tuple[str, str, str]] = []
    for item in items:
        variants = {"oob_variant": item.oob_variant, "admissible_variant": item.admissible_variant}
        for condition, (variant, key) in CONDITIONS.items():
            prompts.append((item.independent_unit_id, condition, variants[variant][key]))
        for condition, variant, expected in (
            ("boundary_oob_with", "oob_variant", "NO"),
            ("boundary_allowed_with", "admissible_variant", "YES"),
        ):
            prompts.append((
                item.independent_unit_id,
                condition,
                boundary_probe(variants[variant]["with_information_prompt"], expected=expected),
            ))

    report: dict[str, object] = {
        "artifact": str(args.artifact),
        "n_units": len(items),
        "n_prompts_per_model": len(prompts),
        "max_model_len": args.max_model_len,
        "max_tokens": args.max_tokens,
        "models": {},
    }
    failures: list[str] = []
    for tag, path in models.items():
        tokenizer = AutoTokenizer.from_pretrained(path, local_files_only=True)
        lengths = [(len(_chat_ids(tokenizer, prompt)), unit, condition) for unit, condition, prompt in prompts]
        longest, longest_unit, longest_condition = max(lengths)
        over = [
            {"unit": unit, "condition": condition, "tokens": n}
            for n, unit, condition in lengths
            if n + args.max_tokens > args.max_model_len
        ]
        report["models"][tag] = {  # type: ignore[index]
            "model_path": path,
            "n_prompts": len(lengths),
            "longest_prompt_tokens": longest,
            "longest_prompt_unit": longest_unit,
            "longest_prompt_condition": longest_condition,
            "mean_prompt_tokens": sum(n for n, _, _ in lengths) / len(lengths),
            "over_budget_prompts": over,
            "passed": not over,
        }
        if over:
            failures.append(f"{tag}: {len(over)} prompts exceed max_model_len")

    report["passed"] = not failures
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({tag: info["longest_prompt_tokens"] for tag, info in report["models"].items()}, indent=2))  # type: ignore[union-attr]
    print(f"wrote {args.out}")
    if failures:
        print("TOKEN CENSUS FAILED (no truncation is permitted): " + "; ".join(failures), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
