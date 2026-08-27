"""Is the rule-span state exclusion-specific, and is it shared across items?

Stage 5 patched a whole rule span between two Exclude runs, so what transferred
could have been the target proposition rather than anything about exclusion. Two
additions here:

1. FACTORIAL PATCH. The same span transfer is run inside the Admit arm as well.
   If matched-preview state transfers as much under Admit as under Exclude, the
   patch is moving proposition information, not an exclusion state.

2. ACTIVATION DIFFERENCE-IN-DIFFERENCES STEERING. A single direction per layer

       v_l = mean_items [ (h_ME - h_MA) - (h_UE - h_UA) ]

   is estimated on training items over the rule-span positions, then added to
   HELD-OUT items' failing runs and subtracted from their succeeding runs. A
   direction estimated on other items that still controls suppression is evidence
   for a reusable exclusion-binding feature rather than an item-specific state.
"""
import os, sys, json, argparse
import torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (load_model, digit_ids, digit_expectation, frozen_items, span_indices,
                    decoder_layers, ROOT)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from patch_matched import matched_previews, build, sites_of, FAMILIES


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="Qwen/Qwen3-8B")
    ap.add_argument("--tag", default="qwen3-8b")
    ap.add_argument("--limit", type=int, default=60)
    ap.add_argument("--layer-step", type=int, default=2)
    ap.add_argument("--alphas", default="0,0.05,0.1,0.2,0.4")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()
    out_path = args.out or os.path.join(ROOT, "results", "mech", f"steer_did_{args.tag}.json")

    tok, model = load_model(args.model)
    dids = digit_ids(tok).to(model.device)
    layers = decoder_layers(model)
    nL = len(layers)
    Ls = list(range(0, nL, args.layer_step))
    alphas = [float(a) for a in args.alphas.split(",")]
    items = frozen_items(FAMILIES)[:args.limit]
    half = len(items) // 2
    train, test = items[:half], items[half:]
    print(f"{len(train)} train / {len(test)} test items, {nL} layers", flush=True)

    def prompts(it):
        match, unrel = matched_previews(tok, it)
        P = {}
        for tag, prev, adm in (("ME", match, False), ("MA", match, True),
                               ("UE", unrel, False), ("UA", unrel, True)):
            p, blocks = build(tok, it, prev, adm)
            P[tag] = (p, sites_of(tok, p, blocks))
        return P

    def run(prompt, hook=None):
        ids = tok(prompt, return_tensors="pt", add_special_tokens=False)["input_ids"].to(model.device)
        hs = [hook] if hook else []
        y = float(digit_expectation(model(input_ids=ids).logits[0, -1], dids))
        return y

    def span_mean(prompt, sites):
        """mean hidden state over the rule span, per layer"""
        store = {}
        hs = []
        lo, hi = sites["rule_span"]
        def mk(L):
            def h(mod, inp, outp):
                o = outp[0] if isinstance(outp, tuple) else outp
                store[L] = o[0, lo:hi, :].mean(0).detach().clone()
            return h
        for L in Ls:
            hs.append(layers[L].register_forward_hook(mk(L)))
        ids = tok(prompt, return_tensors="pt", add_special_tokens=False)["input_ids"].to(model.device)
        model(input_ids=ids)
        for h in hs:
            h.remove()
        return store

    # ---------- 1. estimate v_l on the training items ----------
    acc = {L: [] for L in Ls}
    hnorm = {L: [] for L in Ls}
    with torch.no_grad():
        for n, it in enumerate(train):
            P = prompts(it)
            if any(P[t][1]["rule_span"] is None for t in P):
                continue
            H = {t: span_mean(*P[t]) for t in P}
            for L in Ls:
                acc[L].append(((H["ME"][L] - H["MA"][L]) - (H["UE"][L] - H["UA"][L])).float())
                hnorm[L].append(float(H["UE"][L].float().norm()))
            if (n + 1) % 10 == 0:
                print(f"  train {n+1}/{len(train)}", flush=True)
    # The raw difference-of-differences is small next to a typical hidden state,
    # so alpha is a fraction of the layer's mean activation magnitude along the
    # unit DID direction.
    v, norms, scale = {}, {}, {}
    for L in Ls:
        if not acc[L]:
            continue
        raw = torch.stack(acc[L]).mean(0)
        norms[L] = float(raw.norm())
        scale[L] = sum(hnorm[L]) / len(hnorm[L])
        v[L] = raw / (raw.norm() + 1e-6) * scale[L]
    print("  DID/activation norm ratio:",
          {L: round(norms[L] / max(scale[L], 1e-6), 4) for L in v}, flush=True)

    # ---------- 2. factorial patch + held-out steering ----------
    recs = []
    with torch.no_grad():
        for n, it in enumerate(test):
            P = prompts(it)
            if any(P[t][1]["rule_span"] is None for t in P):
                continue
            base_y = {t: run(P[t][0]) for t in P}
            rec = dict(item_id=it.item_id, direction=it.critical_direction, y=base_y,
                       factorial={}, steer={})

            # factorial span patch: ME->UE and MA->UA
            for donor_tag, recip_tag in (("ME", "UE"), ("MA", "UA")):
                dstore = {}
                lo, hi = P[donor_tag][1]["rule_span"]
                hs = []
                def mk(L):
                    def h(mod, inp, outp):
                        o = outp[0] if isinstance(outp, tuple) else outp
                        dstore[L] = o[0, lo:hi, :].detach().clone()
                    return h
                for L in Ls:
                    hs.append(layers[L].register_forward_hook(mk(L)))
                run(P[donor_tag][0])
                for h in hs:
                    h.remove()
                rlo, rhi = P[recip_tag][1]["rule_span"]
                vals = []
                for L in Ls:
                    d = dstore[L]
                    def h(mod, inp, outp, d=d, rlo=rlo, rhi=rhi):
                        o = outp[0] if isinstance(outp, tuple) else outp
                        k = min(rhi - rlo, d.shape[0])
                        o[0, rlo:rlo + k, :] = d[:k]
                        return (o,) + outp[1:] if isinstance(outp, tuple) else o
                    hh = layers[L].register_forward_hook(h)
                    vals.append(run(P[recip_tag][0]))
                    hh.remove()
                rec["factorial"][f"{donor_tag}_into_{recip_tag}"] = vals

            # held-out steering with the shared direction
            for recip_tag, sign in (("UE", +1.0), ("ME", -1.0)):
                rlo, rhi = P[recip_tag][1]["rule_span"]
                per_layer = {}
                for L in Ls:
                    if L not in v:
                        continue
                    vals = []
                    for a in alphas:
                        vec = sign * a * v[L].to(model.device)
                        def h(mod, inp, outp, vec=vec, rlo=rlo, rhi=rhi):
                            o = outp[0] if isinstance(outp, tuple) else outp
                            o[0, rlo:rhi, :] = o[0, rlo:rhi, :] + vec.to(o.dtype)
                            return (o,) + outp[1:] if isinstance(outp, tuple) else o
                        hh = layers[L].register_forward_hook(h)
                        vals.append(run(P[recip_tag][0]))
                        hh.remove()
                    per_layer[L] = vals
                rec["steer"][recip_tag] = per_layer
            recs.append(rec)
            if (n + 1) % 5 == 0:
                print(f"  test {n+1}/{len(test)}", flush=True)

    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    json.dump(dict(layers=Ls, n_layers=nL, alphas=alphas, norms=norms, scale=scale,
                   n_train=len(train), records=recs), open(out_path, "w"))
    print(f"wrote {len(recs)} -> {out_path}")


if __name__ == "__main__":
    main()
