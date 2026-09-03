"""G16 — interchange the binding state between identifier- and class-bound policies.

Frozen design: `preregistrations/PREREGISTRATION_G16_BINDING_INTERCHANGE.md`, tag
`g16-binding-interchange-design-v1.1`.

Two phases, in this order, because gate 1 is a stopping rule:

    --phase baselines   300 generations, 75 items x 4 conditions
    --phase patched     bidirectional interchange, only if the bridge passed

Readout is the fixed-position `ANSWER_FORMATS["direct"]` digit expectation, per
Amendment A1 — the same readout as the span gate and Stage 5.
"""
from __future__ import annotations

import argparse
import json
import os
import sys

import torch

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

from binding_prompts import CONDITIONS, FAMILIES, build_pair, sites_of  # noqa: E402
from common import (ROOT, decoder_layers, digit_expectation, digit_ids,  # noqa: E402
                    frozen_items, load_model)

LAYERS = [4, 8, 12, 14, 16, 18, 20, 24, 28, 32]
SITES = ["rule_end", "rule_span", "evidence_end", "answer"]
GAP_FLOOR = 2.0          # items with a behavioural gap below this are not patched
BRIDGE_FLOOR = 5.0       # gate 1


def _readout(tok, model, dids, prompt: str) -> float:
    ids = tok(prompt, return_tensors="pt", add_special_tokens=False)["input_ids"]
    ids = ids.to(model.device)
    return float(digit_expectation(model(input_ids=ids).logits[0, -1], dids))


def _sign(item) -> float:
    """+1 if the excluded evidence pushes the rating up, -1 if down."""
    return 1.0 if item.critical_direction == "increase" else -1.0


def run_baselines(tok, model, dids, items) -> list[dict]:
    out = []
    with torch.no_grad():
        for n, item in enumerate(items):
            pair = build_pair(tok, item)
            rec = {
                "item_id": item.item_id,
                "task_family": item.task_family,
                "direction": item.critical_direction,
                "n_tok": pair["n_tok"],
                "pad_tokens": pair["pad_tokens"],
                "y": {c: _readout(tok, model, dids, pair["prompts"][c])
                      for c in CONDITIONS},
            }
            s = _sign(item)
            # ExclusionEffect: how far each arm sits below its own admit anchor
            rec["exclusion_effect"] = {
                "id": s * (rec["y"]["id_admit"] - rec["y"]["id_exclude"]),
                "cls": s * (rec["y"]["cls_admit"] - rec["y"]["cls_exclude"]),
            }
            rec["bridge"] = rec["exclusion_effect"]["cls"] - rec["exclusion_effect"]["id"]
            out.append(rec)
            if (n + 1) % 15 == 0:
                print(f"  baselines {n + 1}/{len(items)}", flush=True)
    return out


def _cache(tok, model, layers, prompt, sites) -> dict:
    store, handles = {}, []

    def mk(layer_idx):
        def hook(_mod, _inp, outp):
            o = outp[0] if isinstance(outp, tuple) else outp
            for name, pos in sites.items():
                if pos is None:
                    continue
                if isinstance(pos, tuple):
                    store[(layer_idx, name)] = o[0, pos[0]:pos[1], :].detach().clone()
                else:
                    store[(layer_idx, name)] = o[0, pos, :].detach().clone()
        return hook

    for layer_idx in LAYERS:
        handles.append(layers[layer_idx].register_forward_hook(mk(layer_idx)))
    ids = tok(prompt, return_tensors="pt", add_special_tokens=False)["input_ids"]
    model(input_ids=ids.to(model.device))
    for handle in handles:
        handle.remove()
    return store


def _patched_readout(tok, model, dids, layers, prompt, layer_idx, pos, donor,
                     orthogonal=False):
    def hook(_mod, _inp, outp):
        o = outp[0] if isinstance(outp, tuple) else outp
        if isinstance(pos, tuple):
            a, b = pos
            n = min(b - a, donor.shape[0])
            o[0, a:a + n, :] = donor[:n] if not orthogonal else _orth(o[0, a:a + n, :],
                                                                     donor[:n])
        else:
            o[0, pos, :] = donor if not orthogonal else _orth(o[0, pos, :], donor)
        return (o,) + outp[1:] if isinstance(outp, tuple) else o

    handle = layers[layer_idx].register_forward_hook(hook)
    try:
        return _readout(tok, model, dids, prompt)
    finally:
        handle.remove()


def _orth(current, donor):
    """Matched-norm control: move by a vector orthogonal to the real difference.

    The real edit is `donor - current`. The control keeps that magnitude but points
    it along a deterministic direction orthogonal to it, built by projecting a fixed
    permutation of the difference out of the difference itself.
    """
    delta = (donor - current).float()
    flipped = torch.flip(delta, dims=(-1,))
    proj = (flipped * delta).sum(-1, keepdim=True) / (delta.pow(2).sum(-1, keepdim=True) + 1e-6)
    perp = flipped - proj * delta
    perp = perp / (perp.norm(dim=-1, keepdim=True) + 1e-6) * delta.norm(dim=-1, keepdim=True)
    return (current.float() + perp).to(current.dtype)


def run_patched(tok, model, dids, items, baselines) -> list[dict]:
    layers = decoder_layers(model)
    by_id = {b["item_id"]: b for b in baselines}
    qualifying = [it for it in items
                  if abs(by_id[it.item_id]["bridge"]) >= GAP_FLOOR]
    print(f"{len(qualifying)}/{len(items)} items have |bridge| >= {GAP_FLOOR}",
          flush=True)

    out = []
    with torch.no_grad():
        for n, item in enumerate(qualifying):
            pair = build_pair(tok, item)
            prompts = pair["prompts"]
            sites = {c: sites_of(tok, prompts[c], pair["blocks"][c]) for c in CONDITIONS}
            caches = {c: _cache(tok, model, layers, prompts[c], sites[c])
                      for c in CONDITIONS}

            rec = {"item_id": item.item_id, "direction": item.critical_direction,
                   "patch": {}}
            transfers = (
                ("break", "cls_exclude", "id_exclude"),      # failure state into success
                ("rescue", "id_exclude", "cls_exclude"),     # success state into failure
                ("admit_break", "cls_admit", "id_admit"),
                ("admit_rescue", "id_admit", "cls_admit"),
            )
            for name, recipient, donor_cond in transfers:
                res = {}
                for site in SITES:
                    pos = sites[recipient].get(site)
                    if pos is None:
                        continue
                    vals, orth = [], []
                    for layer_idx in LAYERS:
                        key = (layer_idx, site)
                        if key not in caches[donor_cond]:
                            vals.append(None)
                            orth.append(None)
                            continue
                        donor = caches[donor_cond][key]
                        vals.append(_patched_readout(tok, model, dids, layers,
                                                     prompts[recipient], layer_idx,
                                                     pos, donor))
                        orth.append(_patched_readout(tok, model, dids, layers,
                                                     prompts[recipient], layer_idx,
                                                     pos, donor, orthogonal=True))
                    res[site] = {"patched": vals, "orthogonal": orth}
                rec["patch"][name] = res
            out.append(rec)
            if (n + 1) % 5 == 0:
                print(f"  patched {n + 1}/{len(qualifying)}", flush=True)
    return out


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="/var/tmp/xiang-isr-models/qwen3-8b")
    ap.add_argument("--phase", choices=("baselines", "patched"), required=True)
    ap.add_argument("--out-dir", default=os.path.join(ROOT, "results", "mech"))
    args = ap.parse_args()

    base_path = os.path.join(args.out_dir, "g16_baselines.json")
    tok, model = load_model(args.model)
    dids = digit_ids(tok).to(model.device)
    items = frozen_items(FAMILIES)

    if args.phase == "baselines":
        recs = run_baselines(tok, model, dids, items)
        bridges = [r["bridge"] for r in recs]
        mean_bridge = sum(bridges) / len(bridges)
        payload = {
            "design_tag": "g16-binding-interchange-design-v1.1",
            "readout": "ANSWER_FORMATS['direct'] fixed-position digit expectation",
            "n_items": len(recs),
            "mean_bridge": mean_bridge,
            "bridge_floor": BRIDGE_FLOOR,
            "records": recs,
        }
        with open(base_path, "w") as handle:
            json.dump(payload, handle, indent=1)
        print(f"\nmean bridge = {mean_bridge:+.2f} rating points "
              f"(gate 1 floor {BRIDGE_FLOOR}); wrote {base_path}")
        print("run the analyzer for the bootstrap CI before starting the patched phase")
        return

    with open(base_path) as handle:
        baselines = json.load(handle)["records"]
    recs = run_patched(tok, model, dids, items, baselines)
    out_path = os.path.join(args.out_dir, "g16_patched.json")
    with open(out_path, "w") as handle:
        json.dump({"design_tag": "g16-binding-interchange-design-v1.1",
                   "layers": LAYERS, "sites": SITES, "records": recs}, handle)
    print(f"wrote {len(recs)} -> {out_path}")


if __name__ == "__main__":
    main()
