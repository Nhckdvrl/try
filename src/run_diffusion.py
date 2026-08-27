"""Masked-diffusion LMs (LLaDA, Dream) under the same fixed-position readout.

These models have BIDIRECTIONAL attention, so the rule and the evidence can see
each other regardless of which comes first.  If the Pre/Post asymmetry we measure
in causal LMs comes from where the rule sits relative to the evidence in a causal
stream, it should be attenuated here.

The readout needs no iterative denoising: we append `ANSWER: <mask>` and read the
model's distribution at that single masked position in one forward pass.
"""
import argparse, json, os, sys
import torch
sys.path.insert(0, os.path.dirname(__file__))
from schema import (load_items, compile_prompt, compile_probe, SYSTEM, CONDITIONS,
                    EXTRA_CONDITIONS, PROBES, ANSWER_CUE)

ROOT = os.path.join(os.path.dirname(__file__), "..")


def yes_no_ids(tok):
    yes, no = [], []
    for i in range(len(tok)):
        try:
            t = tok.convert_ids_to_tokens(i)
        except Exception:
            continue
        if not isinstance(t, str):
            continue
        w = t.replace("Ġ", " ").replace("▁", " ").strip().upper()
        if w in ("YES", "Y"):
            yes.append(i)
        elif w in ("NO", "N"):
            no.append(i)
    return torch.tensor(yes), torch.tensor(no)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--tag", required=True)
    ap.add_argument("--kinds", required=True)
    ap.add_argument("--only-ids", default=os.path.join(ROOT, "data", "items", "frozen_v1.json"))
    ap.add_argument("--families", default="legal_judgment,evidence_inference,"
                                          "ranking_selection,outcome_evaluation")
    ap.add_argument("--out", required=True)
    # Dream is initialised from an autoregressive checkpoint and keeps the shifted
    # convention (position i predicts token i+1), so its mask position is read one
    # step earlier. LLaDA predicts the token AT the masked position (shift 0).
    ap.add_argument("--logits-shift", type=int, default=0)
    # Dream degenerates to <|endoftext|> when the prompt ends in a single mask: it is
    # trained to fill a BLOCK of masks of the intended generation length. Appending a
    # short block and reading the first position fixes it. LLaDA is fine with one.
    ap.add_argument("--n-mask", type=int, default=1)
    args = ap.parse_args()

    from transformers import AutoTokenizer, AutoModel, AutoConfig
    tok = AutoTokenizer.from_pretrained(args.model, trust_remote_code=True)
    cfg = AutoConfig.from_pretrained(args.model, trust_remote_code=True)
    mask_id = getattr(cfg, "mask_token_id", None) or tok.mask_token_id
    assert mask_id is not None, "no mask token"
    model = AutoModel.from_pretrained(args.model, trust_remote_code=True,
                                      dtype=torch.bfloat16).to("cuda").eval()

    items = load_items(os.path.join(ROOT, "data", "items", "items_v1.jsonl"))
    keep = set(json.load(open(args.only_ids)))
    fams = set(args.families.split(","))
    items = [i for i in items if i.item_id in keep and i.task_family in fams]
    kinds = args.kinds.split(",")

    dids = torch.tensor([tok.encode(str(d), add_special_tokens=False)[0] for d in range(10)])
    yid, nid = yes_no_ids(tok)
    cue_ids = tok(ANSWER_CUE + " ", add_special_tokens=False)["input_ids"]

    def chat_ids(user):
        msgs = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}]
        try:
            enc = tok.apply_chat_template(msgs, tokenize=True, add_generation_prompt=True)
        except Exception:
            enc = tok.apply_chat_template([{"role": "user", "content": SYSTEM + "\n\n" + user}],
                                          tokenize=True, add_generation_prompt=True)
        ids = enc["input_ids"] if hasattr(enc, "keys") else enc
        return list(ids[0]) if ids and isinstance(ids[0], (list, tuple)) else list(ids)

    recs = []
    with torch.no_grad():
        for n, it in enumerate(items):
            for k in kinds:
                if k in CONDITIONS or k in EXTRA_CONDITIONS:
                    user, kind = compile_prompt(it, k, mode="cued"), "digit"
                elif k in PROBES and k.startswith("rule_probe"):
                    user, kind = compile_probe(it, k), "rule"
                else:
                    continue
                ids = chat_ids(user)
                if kind == "digit":
                    ids = ids + cue_ids
                n_prompt = len(ids)
                ids = ids + [mask_id] * args.n_mask
                x = torch.tensor([ids], device=model.device)
                out = model(x)
                allg = out.logits if hasattr(out, "logits") else out[0]
                logits = allg[0, n_prompt - args.logits_shift].float()
                rec = dict(item_id=it.item_id, task_family=it.task_family, kind_name=k,
                           kind=kind, model_tag=args.tag, readout="masked_position",
                           n_prompt_tokens=len(ids))
                if kind == "digit":
                    p = torch.softmax(logits, -1)
                    pd = p[dids]
                    rec["mass"] = float(pd.sum())
                    pd = pd / pd.sum()
                    rec["value"] = float((pd * torch.arange(10.0, device=pd.device)).sum()) * 100.0 / 9.0
                    rec["raw"] = tok.decode([int(logits.argmax())])
                else:
                    p = torch.softmax(logits, -1)
                    y, nn = float(p[yid].sum()), float(p[nid].sum())
                    rec["mass"] = y + nn
                    rec["p_yes"] = y / (y + nn) if y + nn > 0 else None
                    rec["yesno"] = None if rec["p_yes"] is None else ("YES" if rec["p_yes"] >= .5 else "NO")
                    rec["raw"] = tok.decode([int(logits.argmax())])
                recs.append(rec)
            if (n + 1) % 20 == 0:
                print(f"  {n+1}/{len(items)}", flush=True)

    os.makedirs(os.path.dirname(args.out), exist_ok=True)
    with open(args.out, "w") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    dg = [r for r in recs if r["kind"] == "digit"]
    ru = [r for r in recs if r["kind"] == "rule"]
    print(f"wrote {len(recs)} -> {args.out}")
    print(f"  digit rows {len(dg)}, mean digit mass {sum(r['mass'] for r in dg)/max(1,len(dg)):.3f}")
    if ru:
        print(f"  rule rows {len(ru)}, mean YES/NO mass {sum(r['mass'] for r in ru)/len(ru):.3f}")


if __name__ == "__main__":
    main()
