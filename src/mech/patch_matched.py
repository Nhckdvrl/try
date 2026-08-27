"""Stage 5: same-chronology bidirectional patching.

The earlier Post -> Pre patch had donor and recipient in different token orders,
so a layer effect could be ordinary sequence-order information. Stage 3E supplies
a matched pair in which the evidence the decision reads sits after the rule on
both sides and only the preview differs:

    FAILURE   unrelated preview   -> rule(0%) -> evidence -> answer
    SUCCESS   paraphrase preview  -> rule(0%) -> evidence -> answer

The previews are padded to within a few tokens of each other, so the two runs are
length-matched. A full 2x2 with an admitting rule is measured alongside, so the
quantity of interest is the interaction (ME-MA) - (UE-UA) rather than a raw
difference that a preview alone could produce.

Patch sites are semantic positions, present in both runs: the end of the preview
block, the end of the rule block, the end of the evidence block, and the answer
position. The rule-end site is the interesting one: the evidence has not been read
yet, so anything transferred there is a state the rule itself established.
"""
import os, sys, json, argparse
import torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (load_model, digit_ids, digit_expectation, frozen_items, span_indices, ROOT)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from schema import SYSTEM, ANSWER_CUE, ANSWER_FORMATS
from conditions_v3 import uniform_weight_rule
from conditions_v6 import preview_text
from conditions_v2 import filler_block, stable_seed

FAMILIES = ("legal_judgment", "evidence_inference")
SITES = ["preview_end", "rule_end", "rule_span", "evidence_end", "answer"]


def matched_previews(tok, item):
    """A proposition-matched preview and an unrelated one of the same token length."""
    match = preview_text(item, "para")
    n = len(tok(match, add_special_tokens=False)["input_ids"])
    unrel, k = "", 1
    while len(tok(unrel, add_special_tokens=False)["input_ids"]) < n and k < 40:
        unrel = filler_block(k, stable_seed(item.item_id)).split("\n", 1)[1].replace("- ", "")
        unrel = unrel.replace("\n", " ")
        k += 1
    ids = tok(unrel, add_special_tokens=False)["input_ids"][:n]
    return match, tok.decode(ids)


def build(tok, item, preview, admit):
    blocks = ["BACKGROUND\n" + item.base_context,
              "PRELIMINARY NOTE\n" + preview,
              uniform_weight_rule(item, 1.0 if admit else 0.0),
              "ADDITIONAL INFORMATION\n" + item.critical_evidence,
              "TASK\n" + item.question + "\n" + item.output_spec + "\n"
              + ANSWER_FORMATS["direct"]]
    user = "\n\n".join(blocks)
    text = tok.apply_chat_template(
        [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}],
        tokenize=False, add_generation_prompt=True)
    return text + ANSWER_CUE + " ", blocks


def sites_of(tok, prompt, blocks):
    out = {}
    for name, blk in (("preview_end", blocks[1]), ("rule_end", blocks[2]),
                      ("evidence_end", blocks[3])):
        try:
            lo, hi = span_indices(tok, prompt, blk)
            out[name] = hi - 1
            if name == "rule_end":
                # the whole rule block, not just its last token: a single position is a
                # weak intervention and under-states how much state is transferable
                out["rule_span"] = (lo, hi)
        except ValueError:
            out[name] = None
    out.setdefault("rule_span", None)
    out["answer"] = -1
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default="Qwen/Qwen3-8B")
    ap.add_argument("--limit", type=int, default=40)
    ap.add_argument("--layer-step", type=int, default=2)
    ap.add_argument("--out", default=os.path.join(ROOT, "results", "mech", "patch_matched.json"))
    args = ap.parse_args()

    tok, model = load_model(args.model)
    dids = digit_ids(tok).to(model.device)
    layers = model.model.layers
    nL = len(layers)
    Ls = list(range(0, nL, args.layer_step))
    items = frozen_items(FAMILIES)[:args.limit]
    print(f"{len(items)} items, {nL} layers, patching {len(Ls)}", flush=True)

    def run_plain(prompt):
        ids = tok(prompt, return_tensors="pt", add_special_tokens=False)["input_ids"].to(model.device)
        return float(digit_expectation(model(input_ids=ids).logits[0, -1], dids)), ids

    recs = []
    with torch.no_grad():
        for n, it in enumerate(items):
            match, unrel = matched_previews(tok, it)
            P = {}
            for tag, prev, adm in (("ME", match, False), ("MA", match, True),
                                   ("UE", unrel, False), ("UA", unrel, True)):
                p, blocks = build(tok, it, prev, adm)
                P[tag] = (p, sites_of(tok, p, blocks))
            rec = dict(item_id=it.item_id, direction=it.critical_direction, y={},
                       n_tok={}, patch={})
            for tag in P:
                y, ids = run_plain(P[tag][0])
                rec["y"][tag] = y
                rec["n_tok"][tag] = ids.shape[1]

            # cache donor states at each site, for both directions
            def cache(prompt, sites):
                store = {}
                hs = []
                def mk(L):
                    def h(mod, inp, outp):
                        o = outp[0] if isinstance(outp, tuple) else outp
                        for nm, pos in sites.items():
                            if pos is None:
                                continue
                            if isinstance(pos, tuple):
                                store[(L, nm)] = o[0, pos[0]:pos[1], :].detach().clone()
                            else:
                                store[(L, nm)] = o[0, pos, :].detach().clone()
                    return h
                for L in Ls:
                    hs.append(layers[L].register_forward_hook(mk(L)))
                ids = tok(prompt, return_tensors="pt", add_special_tokens=False)["input_ids"].to(model.device)
                model(input_ids=ids)
                for h in hs:
                    h.remove()
                return store

            cME = cache(*P["ME"])
            cUE = cache(*P["UE"])

            for direction, donor, recip in (("success_into_failure", cME, "UE"),
                                            ("failure_into_success", cUE, "ME")):
                prompt, sites = P[recip]
                res = {}
                for site in SITES:
                    pos = sites.get(site)
                    if pos is None:
                        continue
                    vals = []
                    for L in Ls:
                        key = (L, site)
                        if key not in donor:
                            vals.append(None)
                            continue
                        def h(mod, inp, outp, L=L, key=key, pos=pos):
                            o = outp[0] if isinstance(outp, tuple) else outp
                            if isinstance(pos, tuple):
                                a, b = pos
                                d = donor[key]
                                n = min(b - a, d.shape[0])
                                o[0, a:a + n, :] = d[:n]
                            else:
                                o[0, pos, :] = donor[key]
                            return (o,) + outp[1:] if isinstance(outp, tuple) else o
                        hh = layers[L].register_forward_hook(h)
                        y, _ = run_plain(prompt)
                        hh.remove()
                        vals.append(y)
                    res[site] = vals
                rec["patch"][direction] = res
            recs.append(rec)
            if (n + 1) % 5 == 0:
                print(f"  {n+1}/{len(items)}", flush=True)

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    json.dump(dict(layers=Ls, n_layers=nL, records=recs), open(args.out, "w"))
    print(f"wrote {len(recs)} -> {args.out}")


if __name__ == "__main__":
    main()
