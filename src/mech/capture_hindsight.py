"""Capture layerwise readouts on the frozen BTF-3 artifact, with HF hooks.

Tooling for the mechanism phase. It does not decide any experiment; it produces
the per-item, per-layer quantities that a preregistered mechanism analysis
consumes. Two things are captured per (item, condition):

* **Residual stream at the final prompt position**, every layer, fp16. This is
  what a probe for "is the ex-ante estimate present internally" is trained and
  tested on.
* **Logit-lens readout at the final prompt position**, every layer: the
  distribution restricted to the single-digit tokens `0`-`9`, plus the logits
  of two caller-supplied reference tokens. The reference tokens are the first
  greedy tokens of the model's own answers in the WITH and WITHOUT conditions,
  so the crossover between them is a per-item trajectory of "which answer is
  the readout heading toward".

Decoding, prompts, chat template, and the artifact are inherited from
``run_information_set``; nothing here re-authors a prompt.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

import numpy as np  # noqa: E402
import torch  # noqa: E402

from information_set_schema import file_sha256, load_jsonl  # noqa: E402
from run_information_set import CONDITIONS, SYSTEM_PROMPT  # noqa: E402


def chat_ids(tokenizer, prompt: str) -> list[int]:
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


def digit_token_ids(tokenizer) -> dict[str, int]:
    """Token ids for the ten leading digits, as they appear after the template.

    A digit that does not encode to exactly one token is omitted and reported;
    every model in the panel encodes bare digits as single tokens.
    """
    out: dict[str, int] = {}
    for digit in "0123456789":
        ids = tokenizer.encode(digit, add_special_tokens=False)
        if len(ids) == 1:
            out[digit] = ids[0]
    return out


@torch.no_grad()
def capture(model, tokenizer, prompt_ids: list[int], digits: dict[str, int]) -> dict:
    device = next(model.parameters()).device
    ids = torch.tensor([prompt_ids], device=device)
    out = model(ids, output_hidden_states=True, use_cache=False)
    # hidden_states: tuple(L+1) of (1, T, d); take the final position only.
    residuals = torch.stack([h[0, -1, :] for h in out.hidden_states])  # (L+1, d)

    # Logit lens: apply the model's own final norm and unembedding to each layer.
    norm = _final_norm(model)
    head = model.get_output_embeddings()
    lens = head(norm(residuals.to(head.weight.dtype)))  # (L+1, V)
    digit_ids = torch.tensor([digits[d] for d in sorted(digits)], device=device)
    digit_logits = lens[:, digit_ids].float().cpu().numpy()

    greedy = out.logits[0, -1, :].argmax().item()
    return {
        "residuals": residuals.to(torch.float16).cpu().numpy(),
        "digit_logits": digit_logits,
        "digit_order": sorted(digits),
        "greedy_token_id": greedy,
        "n_layers": residuals.shape[0] - 1,
    }


def _final_norm(model):
    for attribute in ("model.norm", "model.language_model.norm", "transformer.ln_f", "model.final_layernorm"):
        node = model
        try:
            for part in attribute.split("."):
                node = getattr(node, part)
            return node
        except AttributeError:
            continue
    raise AttributeError("could not locate the final norm module on this architecture")


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
    parser.add_argument(
        "--conditions",
        nargs="*",
        default=["oob_with", "oob_without"],
        choices=sorted(CONDITIONS),
    )
    parser.add_argument("--limit", type=int, default=0, help="0 = all units")
    parser.add_argument("--dtype", default="bfloat16")
    args = parser.parse_args()

    from transformers import AutoModelForCausalLM, AutoTokenizer

    tokenizer = AutoTokenizer.from_pretrained(args.model, local_files_only=True)
    model = AutoModelForCausalLM.from_pretrained(
        args.model,
        local_files_only=True,
        dtype=getattr(torch, args.dtype),
        device_map="cuda",
    ).eval()

    digits = digit_token_ids(tokenizer)
    items = load_jsonl(args.artifact)
    if args.limit:
        items = items[: args.limit]

    args.out.parent.mkdir(parents=True, exist_ok=True)
    residual_path = args.out.with_suffix(".residuals.npz")
    residual_store: dict[str, np.ndarray] = {}

    with args.out.open("w", encoding="utf-8") as handle:
        handle.write(json.dumps({
            "record_type": "metadata",
            "artifact": str(args.artifact),
            "artifact_sha256": file_sha256(args.artifact),
            "model_id": args.model_id,
            "model_revision": args.model_revision,
            "model_tag": args.tag,
            "conditions": args.conditions,
            "digit_tokens": digits,
            "residual_file": residual_path.name,
            "system_prompt": SYSTEM_PROMPT,
            "readout": "final_prompt_position_logit_lens_and_residuals",
        }) + "\n")
        for index, item in enumerate(items):
            variants = {"oob_variant": item.oob_variant, "admissible_variant": item.admissible_variant}
            for condition in args.conditions:
                variant, key = CONDITIONS[condition]
                prompt = variants[variant][key]
                ids = chat_ids(tokenizer, prompt)
                got = capture(model, tokenizer, ids, digits)
                unit = item.independent_unit_id
                residual_store[f"{unit}|{condition}"] = got["residuals"]
                handle.write(json.dumps({
                    "record_type": "capture",
                    "independent_unit_id": unit,
                    "condition": condition,
                    "n_prompt_tokens": len(ids),
                    "n_layers": got["n_layers"],
                    "greedy_token_id": got["greedy_token_id"],
                    "greedy_token": tokenizer.decode([got["greedy_token_id"]]),
                    "digit_order": got["digit_order"],
                    "digit_logits": got["digit_logits"].tolist(),
                    "direction": int(item.reference_context.get("outcome_alignment_sign", 1)),
                    "model_tag": args.tag,
                }, ensure_ascii=False) + "\n")
            if (index + 1) % 25 == 0:
                print(f"{index + 1}/{len(items)}", flush=True)

    np.savez_compressed(residual_path, **residual_store)
    print(json.dumps({"units": len(items), "out": str(args.out), "residuals": str(residual_path)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
