"""Mechanism experiments on Qwen3-8B.

Restricted to legal_judgment + evidence_inference, the two families where the
fixed-position readout tracks the behavioural one (r = 0.76 / 0.90; see
results/mech/direct_readout.json).

A. Attention routing   -- where does the answer position read from, Pre vs Post?
B. Answer-position patching -- at which layer do Pre and Post diverge?
C. Evidence-span gate  -- if the answer literally cannot attend to the excluded
                          evidence, does the Pre residue disappear?
"""
import os, sys, json, argparse
import torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (load_model, mech_prompt, digit_ids, digit_expectation,
                    frozen_items, span_indices, ROOT)

FAMILIES = ("legal_judgment", "evidence_inference")
CONDS = ["base", "admit_pre", "admit_post", "exclude_pre", "exclude_post"]


def spans(tok, item, cond, prompt):
    out = {}
    for name, text in (("evidence", item.critical_evidence),
                       ("rule", item.exclude_rule if cond.startswith("exclude") else item.admit_rule),
                       ("background", item.base_context)):
        try:
            out[name] = span_indices(tok, prompt, text)
        except ValueError:
            out[name] = None
    return out


def four_d_mask(n, device, dtype, blocked_keys=None, block_from=None):
    """Causal mask as an additive float mask, optionally blocking a key range for
    every query at or after `block_from`."""
    neg = torch.finfo(dtype).min
    m = torch.full((n, n), neg, device=device, dtype=dtype).triu(1)
    if blocked_keys is not None:
        lo, hi = blocked_keys
        q = torch.arange(n, device=device).unsqueeze(1)
        block = (q >= block_from)
        m[:, lo:hi] = torch.where(block.expand(n, hi - lo), torch.full_like(m[:, lo:hi], neg),
                                  m[:, lo:hi])
    return m.view(1, 1, n, n)


def run(model, tok, prompt, dids, attn4d=None, want_attn=False):
    ids = tok(prompt, return_tensors="pt", add_special_tokens=False)["input_ids"].to(model.device)
    kw = {}
    if attn4d is not None:
        kw["attention_mask"] = attn4d
    out = model(input_ids=ids, output_attentions=want_attn, **kw)
    y = float(digit_expectation(out.logits[0, -1], dids))
    return y, out, ids.shape[1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0)
    ap.add_argument("--out", default=os.path.join(ROOT, "results", "mech", "experiments.json"))
    args = ap.parse_args()

    tok, model = load_model()
    dids = digit_ids(tok).to(model.device)
    layers = model.model.layers
    nL = len(layers)
    items = frozen_items(FAMILIES)
    if args.limit:
        items = items[:args.limit]
    print(f"{len(items)} items, {nL} layers", flush=True)

    recs = []
    with torch.no_grad():
        for n, it in enumerate(items):
            rec = dict(item_id=it.item_id, task_family=it.task_family,
                       direction=it.critical_direction)
            prompts = {c: mech_prompt(tok, it, c) for c in CONDS}
            base_y = {}
            for c in CONDS:
                base_y[c], _, _ = run(model, tok, prompts[c], dids)
            rec["y"] = base_y

            # ---------- A. attention routing at the answer position ----------
            rec["attn"] = {}
            for c in ("exclude_pre", "exclude_post"):
                sp = spans(tok, it, c, prompts[c])
                if not sp["evidence"] or not sp["rule"]:
                    continue
                _, out, N = run(model, tok, prompts[c], dids, want_attn=True)
                per_layer = {"evidence": [], "rule": [], "background": []}
                for L in range(nL):
                    a = out.attentions[L][0, :, -1, :].float().mean(0)   # mean over heads
                    for k in per_layer:
                        lo, hi = sp[k]
                        per_layer[k].append(float(a[lo:hi].sum()))
                rec["attn"][c] = per_layer
                rec.setdefault("span_len", {})[c] = {k: sp[k][1] - sp[k][0] for k in per_layer}
                del out

            # ---------- B. answer-position patching: Post -> Pre ----------
            cached = {}
            hs = []

            def mk_cache(L):
                def h(mod, inp, outp):
                    o = outp[0] if isinstance(outp, tuple) else outp
                    cached[L] = o[0, -1, :].detach().clone()
                return h
            for L in range(nL):
                hs.append(layers[L].register_forward_hook(mk_cache(L)))
            run(model, tok, prompts["exclude_post"], dids)
            for h in hs:
                h.remove()

            patched = []
            for L in range(nL):
                def h(mod, inp, outp, L=L):
                    if isinstance(outp, tuple):
                        o = outp[0]
                        o[0, -1, :] = cached[L]
                        return (o,) + outp[1:]
                    outp[0, -1, :] = cached[L]
                    return outp
                hh = layers[L].register_forward_hook(h)
                y, _, _ = run(model, tok, prompts["exclude_pre"], dids)
                hh.remove()
                patched.append(y)
            rec["patch_post_into_pre"] = patched

            # ---------- C. evidence-span gate ----------
            rec["gate"] = {}
            for c in ("exclude_pre", "exclude_post"):
                sp = spans(tok, it, c, prompts[c])
                if not sp["evidence"]:
                    continue
                ids = tok(prompts[c], return_tensors="pt", add_special_tokens=False)["input_ids"]
                N = ids.shape[1]
                lo, hi = sp["evidence"]
                m = four_d_mask(N, model.device, torch.bfloat16, blocked_keys=(lo, hi),
                                block_from=hi)
                y, _, _ = run(model, tok, prompts[c], dids, attn4d=m)
                rec["gate"][c] = y
            recs.append(rec)
            if (n + 1) % 10 == 0:
                print(f"  {n+1}/{len(items)}", flush=True)

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    json.dump(dict(n_layers=nL, records=recs), open(args.out, "w"))
    print(f"wrote {len(recs)} -> {args.out}")


if __name__ == "__main__":
    main()
