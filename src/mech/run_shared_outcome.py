"""Run G13 donor-general outcome-axis capture and causal interchange."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

import numpy as np  # noqa: E402
import torch  # noqa: E402

from adapters.btf3_donor_outcome import assignment_digest, build_donor_pairs  # noqa: E402
from adapters.btf3_packet_swap import PACKET_HEADER, TASK_HEADER  # noqa: E402
from information_set_schema import file_sha256, load_jsonl  # noqa: E402
from mech.shared_outcome import (  # noqa: E402
    LAYERS, balanced_accuracy, frozen_split, learn_axis, orthogonal_axis, split_digest,
)
from run_information_set import SYSTEM_PROMPT, parse_probability  # noqa: E402


def decoder_layers(model):
    for path in (("model", "language_model", "layers"), ("model", "layers"),
                 ("language_model", "model", "layers")):
        node = model
        try:
            for name in path:
                node = getattr(node, name)
            if len(node) > max(LAYERS):
                return node
        except (AttributeError, TypeError):
            pass
    raise RuntimeError("could not locate Gemma decoder layers")


def rendered_prompt_and_span(tokenizer, prompt: str) -> tuple[list[int], tuple[int, int]]:
    messages = [{"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt}]
    kwargs = dict(tokenize=False, add_generation_prompt=True)
    try:
        text = tokenizer.apply_chat_template(messages, enable_thinking=False, **kwargs)
    except TypeError:
        text = tokenizer.apply_chat_template(messages, **kwargs)
    c0 = text.index(PACKET_HEADER) + len(PACKET_HEADER)
    c1 = text.index(TASK_HEADER, c0)
    enc = tokenizer(text, add_special_tokens=False, return_offsets_mapping=True)
    ids = list(enc["input_ids"])
    positions = [i for i, (a, b) in enumerate(enc["offset_mapping"]) if b > c0 and a < c1]
    if not positions or positions != list(range(positions[0], positions[-1] + 1)):
        raise ValueError("packet does not map to one nonempty contiguous token span")
    direct = tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=True)
    direct_ids = direct["input_ids"] if hasattr(direct, "keys") else direct
    if direct_ids and isinstance(direct_ids[0], (list, tuple)):
        direct_ids = direct_ids[0]
    if ids != list(direct_ids):
        raise ValueError("render-then-tokenize ids differ from direct chat-template ids")
    return ids, (positions[0], positions[-1] + 1)


def build_entries(tokenizer, pairs: list[dict]) -> list[dict]:
    entries = []
    for index, pair in enumerate(pairs):
        for outcome in ("yes", "no"):
            prompt = pair[outcome]["prompt"]
            ids, span = rendered_prompt_and_span(tokenizer, prompt)
            entries.append({"index": index, "unit": pair["independent_unit_id"],
                            "outcome": outcome, "donor": pair[outcome]["donor_unit_id"],
                            "prompt_sha256": hashlib.sha256(prompt.encode()).hexdigest(),
                            "ids": ids, "span": span})
    return entries


def pad_batch(entries: list[dict], pad_id: int, device, *, left: bool) -> tuple[torch.Tensor, torch.Tensor, list[tuple[int, int]]]:
    width = max(len(e["ids"]) for e in entries)
    rows, masks, spans = [], [], []
    for entry in entries:
        n = width - len(entry["ids"])
        if left:
            rows.append([pad_id] * n + entry["ids"]); masks.append([0] * n + [1] * len(entry["ids"]))
            spans.append((entry["span"][0] + n, entry["span"][1] + n))
        else:
            rows.append(entry["ids"] + [pad_id] * n); masks.append([1] * len(entry["ids"]) + [0] * n)
            spans.append(entry["span"])
    return (torch.tensor(rows, device=device), torch.tensor(masks, device=device), spans)


@torch.inference_mode()
def capture_states(model, layers, entries: list[dict], batch_size: int, pad_id: int) -> dict[str, np.ndarray]:
    store: dict[str, np.ndarray] = {}
    device = next(model.parameters()).device
    text_model = model.model.language_model
    for start in range(0, len(entries), batch_size):
        batch = entries[start:start + batch_size]
        ids, mask, spans = pad_batch(batch, pad_id, device, left=False)
        captured = {}
        handles = []
        for layer_index in LAYERS:
            def hook(module, inputs, output, layer_index=layer_index):
                hidden = output[0] if isinstance(output, tuple) else output
                captured[layer_index] = torch.stack([
                    hidden[b, lo:hi].float().mean(0).detach().cpu()
                    for b, (lo, hi) in enumerate(spans)
                ])
            handles.append(layers[layer_index].register_forward_hook(hook))
        text_model(input_ids=ids, attention_mask=mask, use_cache=False, return_dict=True)
        for handle in handles:
            handle.remove()
        for b, entry in enumerate(batch):
            for layer_index in LAYERS:
                store[f"{entry['unit']}|{entry['outcome']}|{layer_index}"] = captured[layer_index][b].numpy()
        if min(start + batch_size, len(entries)) % 32 == 0 or start + batch_size >= len(entries):
            print(f"capture {min(start + batch_size, len(entries))}/{len(entries)}", flush=True)
    return store


def _raw_records(path: Path) -> dict:
    if path.exists():
        return json.loads(path.read_text())
    return {"metadata": {}, "representation": {}, "baseline": [], "patches": []}


def _checkpoint(path: Path, result: dict) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    tmp.replace(path)


@torch.inference_mode()
def generate_batch(model, tokenizer, layers, entries: list[dict], *, batch_size: int,
                   patch_layer: int | None = None, axis: np.ndarray | None = None,
                   deltas: list[float] | None = None) -> list[tuple[str, float | None]]:
    device = next(model.parameters()).device
    pad_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else tokenizer.eos_token_id
    outputs = []
    for start in range(0, len(entries), batch_size):
        batch = entries[start:start + batch_size]
        ids, mask, spans = pad_batch(batch, pad_id, device, left=True)
        handle = None
        if patch_layer is not None:
            vector = torch.tensor(axis, device=device, dtype=next(model.parameters()).dtype)
            local_delta = torch.tensor(deltas[start:start + len(batch)], device=device, dtype=vector.dtype)
            def hook(module, inputs, output):
                hidden = output[0] if isinstance(output, tuple) else output
                # Apply once, during the prefill. Decode calls have sequence length 1.
                if hidden.shape[1] > 1:
                    hidden = hidden.clone()
                    for b, (lo, hi) in enumerate(spans):
                        hidden[b, lo:hi, :] += local_delta[b] * vector
                return (hidden,) + output[1:] if isinstance(output, tuple) else hidden
            handle = layers[patch_layer].register_forward_hook(hook)
        generated = model.generate(input_ids=ids, attention_mask=mask, do_sample=False,
                                   max_new_tokens=8, pad_token_id=pad_id,
                                   eos_token_id=tokenizer.eos_token_id, use_cache=True)
        if handle is not None:
            handle.remove()
        continuation = generated[:, ids.shape[1]:]
        for row in continuation:
            raw = tokenizer.decode(row, skip_special_tokens=True)
            outputs.append((raw, parse_probability(raw)))
    return outputs


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--artifact", type=Path, default=ROOT/"data/external/review/btf3_temporal_large_replication_v1.jsonl")
    parser.add_argument("--model", required=True); parser.add_argument("--model-id", required=True)
    parser.add_argument("--model-revision", required=True); parser.add_argument("--tag", required=True)
    parser.add_argument("--out", type=Path, default=ROOT/"results/mech/g13_shared_outcome.json")
    parser.add_argument("--states", type=Path, default=ROOT/"results/mech/g13_shared_outcome_states.npz")
    parser.add_argument("--batch-size", type=int, default=2); parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    from transformers import AutoModelForImageTextToText, AutoTokenizer
    tokenizer = AutoTokenizer.from_pretrained(args.model, local_files_only=True)
    items = load_jsonl(args.artifact); pairs = build_donor_pairs(items); split = frozen_split(pairs)
    entries = build_entries(tokenizer, pairs)
    audit = {"units": len(pairs), "entries": len(entries), "split_counts": {k:len(v) for k,v in split.items()},
             "split_sha256": split_digest(pairs, split), "assignment_sha256": assignment_digest(pairs),
             "longest_tokens": max(len(e["ids"]) for e in entries),
             "packet_span_tokens": {"min":min(e["span"][1]-e["span"][0] for e in entries),
                                    "max":max(e["span"][1]-e["span"][0] for e in entries)}}
    if args.dry_run:
        print(json.dumps(audit, indent=2)); return 0

    model = AutoModelForImageTextToText.from_pretrained(
        args.model, local_files_only=True, dtype=torch.bfloat16, device_map="cuda",
        attn_implementation="eager",
    ).eval()
    layers = decoder_layers(model)
    if len(layers) != 48: raise ValueError(f"expected 48 text layers, got {len(layers)}")
    pad_id = tokenizer.pad_token_id if tokenizer.pad_token_id is not None else tokenizer.eos_token_id
    if args.states.exists():
        states = {k:v for k,v in np.load(args.states).items()}
        print(f"loaded {len(states)} cached states", flush=True)
    else:
        states = capture_states(model, layers, entries, args.batch_size, pad_id)
        args.states.parent.mkdir(parents=True, exist_ok=True)
        np.savez_compressed(args.states, **states)
    by_key = {(e["index"],e["outcome"]):e for e in entries}
    result = _raw_records(args.out)
    result["metadata"] = {"preregistration":"PREREGISTRATION_G13_SHARED_OUTCOME.md",
        "git_commit":subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip(),
        "artifact":str(args.artifact),"artifact_sha256":file_sha256(args.artifact),
        "model_id":args.model_id,"model_revision":args.model_revision,"model_tag":args.tag,
        "layers":list(LAYERS),"audit":audit}

    train_entries = [by_key[(i,o)] for i in split["train"] for o in ("yes","no")]
    test_entries = [by_key[(i,o)] for i in split["test"] for o in ("yes","no")]
    axes = {}
    for layer in LAYERS:
        yes = np.stack([states[f"{e['unit']}|yes|{layer}"] for e in train_entries if e["outcome"]=="yes"])
        no = np.stack([states[f"{e['unit']}|no|{layer}"] for e in train_entries if e["outcome"]=="no"])
        axis, ymu, nmu = learn_axis(yes,no); axes[(layer,"outcome")]=axis
        axes[(layer,"orthogonal")]=orthogonal_axis(axis,layer=layer)
        ty = np.stack([states[f"{e['unit']}|yes|{layer}"] for e in test_entries if e["outcome"]=="yes"])
        tn = np.stack([states[f"{e['unit']}|no|{layer}"] for e in test_entries if e["outcome"]=="no"])
        result["representation"][str(layer)]={"train_yes_projection_mean":ymu,
            "train_no_projection_mean":nmu,"heldout_balanced_accuracy":balanced_accuracy(ty,tn,axis,ymu,nmu)}
    _checkpoint(args.out,result)

    existing_base={r["unit"]+"|"+r["outcome"] for r in result["baseline"]}
    missing=[e for e in test_entries if e["unit"]+"|"+e["outcome"] not in existing_base]
    if missing:
        for entry,(raw,value) in zip(missing,generate_batch(model,tokenizer,layers,missing,batch_size=args.batch_size),strict=True):
            result["baseline"].append({"unit":entry["unit"],"outcome":entry["outcome"],
                                      "raw":raw,"value":value,"prompt_sha256":entry["prompt_sha256"]})
        _checkpoint(args.out,result)
    print("baseline complete", flush=True)

    existing={(r["unit"],r["target"],r["layer"],r["axis_kind"]) for r in result["patches"]}
    for layer in LAYERS:
        for axis_kind in ("outcome","orthogonal"):
            axis=axes[(layer,axis_kind)]
            for target,source in (("no","yes"),("yes","no")):
                group=[by_key[(i,target)] for i in split["test"]
                       if (pairs[i]["independent_unit_id"],target,layer,axis_kind) not in existing]
                deltas=[]
                for entry in group:
                    src=states[f"{entry['unit']}|{source}|{layer}"]; tgt=states[f"{entry['unit']}|{target}|{layer}"]
                    deltas.append(float((src-tgt)@axis))
                generated=generate_batch(model,tokenizer,layers,group,batch_size=args.batch_size,
                                         patch_layer=layer,axis=axis,deltas=deltas)
                for entry,delta,(raw,value) in zip(group,deltas,generated,strict=True):
                    result["patches"].append({"unit":entry["unit"],"layer":layer,"axis_kind":axis_kind,
                        "target":target,"source":source,"projection_delta":delta,"raw":raw,"value":value})
                _checkpoint(args.out,result)
        print(f"layer {layer} complete", flush=True)
    print(json.dumps({"out":str(args.out),"states":str(args.states),"records":len(result["patches"])}))
    return 0


if __name__ == "__main__": raise SystemExit(main())
