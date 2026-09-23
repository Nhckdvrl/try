"""G23C runner — target-conditioned policy-state interchange.

Frozen design: preregistrations/PREREGISTRATION_G23C_TARGET_CONDITIONED_POLICY_STATE.md,
tag `g23c-target-conditioned-policy-state-design-v1`.  Model forward passes are
authorized only by the repository-level STATUS.md update that follows the tag.

Phases (§4 stop rule: bridge first, interchange only after the gate passes):

  bridge — the four Stage-5 cells, direct readout, no hooks;
  patch  — the same four baselines (capturing each cell's rule-end state at the
           frozen layers), the four within-preview policy-value interchanges
           (§6), and the identity patches (§9.1).

The Stage-5 cell construction is *imported*, not copied: `matched_previews`,
`build` and `sites_of` come verbatim from `patch_matched.py`, so §11.1 exact
cell reconstruction holds by construction and is re-checked at runtime by the
§9.2 (pairwise block identity) and §9.3 (site precedes evidence) assertions.
"""
import os
import sys
import json
import argparse

import torch

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import (load_model, digit_ids, digit_expectation, frozen_items,  # noqa: E402
                    span_indices, decoder_layers, ROOT)
from patch_matched import matched_previews, build, sites_of   # noqa: E402
sys.path.insert(0, os.path.join(HERE, ".."))
from analyze_g23c import (CELLS, CELL_TABLE, DIRECTIONS, FAMILIES,          # noqa: E402
                          PRIMARY_LAYER, CONTROL_LAYERS, DESIGN_TAG, MODELS,
                          frozen_layers, IDENTITY_TOL, SEED)


def build_cells(tok, item):
    """The four §3 cells with the frozen construction checks (§9.2, §9.3)."""
    match, unrel = matched_previews(tok, item)
    P = {}
    for cell, (which, admit) in CELL_TABLE.items():
        preview = match if which == "match" else unrel
        prompt, blocks = build(tok, item, preview, admit)
        P[cell] = {"prompt": prompt, "blocks": blocks,
                   "sites": sites_of(tok, prompt, blocks)}

    # §9.2: inside a preview pair only the rule block may differ (the policy
    # value is the sole manipulation when the preview is held fixed).
    for a, b in (("ME", "MA"), ("UE", "UA")):
        ba, bb = P[a]["blocks"], P[b]["blocks"]
        assert (ba[0] == bb[0] and ba[1] == bb[1] and ba[3:] == bb[3:]
                and ba[2] != bb[2]), (item.item_id, a, b)
    # §9.2: at a fixed policy only the preview block may differ across M/U.
    for a, b in (("ME", "UE"), ("MA", "UA")):
        ba, bb = P[a]["blocks"], P[b]["blocks"]
        assert (ba[0] == bb[0] and ba[2] == bb[2] and ba[3:] == bb[3:]
                and ba[1] != bb[1]), (item.item_id, a, b)

    # §9.3: the patch site is the last rule token and precedes any evidence
    # token, so no evidence has been processed at the site.
    for cell in P:
        pos = P[cell]["sites"].get("rule_end")
        if pos is None:
            raise RuntimeError(f"{item.item_id}/{cell}: rule_end site missing")
        ev_lo, _ = span_indices(tok, P[cell]["prompt"], P[cell]["blocks"][3])
        if not pos < ev_lo:
            raise RuntimeError(f"{item.item_id}/{cell}: rule_end {pos} does "
                               f"not precede evidence {ev_lo}")
    return P


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--tag", required=True, choices=list(MODELS))
    ap.add_argument("--phase", required=True, choices=["bridge", "patch"])
    ap.add_argument("--limit", type=int, default=0,
                    help="0 = all frozen items; the frozen run uses 0")
    ap.add_argument("--out", default=None)
    ap.add_argument("--dry-run", action="store_true",
                    help="tokenizer-only §11.1/§9 cell-site audit; no model "
                         "load, no forward pass")
    args = ap.parse_args()
    out = args.out or os.path.join(ROOT, "results", "mech",
                                   f"g23c_{args.phase}_{args.tag}.json")

    items = frozen_items(FAMILIES)
    if args.limit:
        items = items[:args.limit]

    if args.dry_run:
        from transformers import AutoTokenizer
        tok = AutoTokenizer.from_pretrained(args.model)
        n_ok = 0
        for it in items:
            build_cells(tok, it)
            n_ok += 1
        print(f"DRY RUN OK — {n_ok} items x 4 cells: previews matched, "
              f"pairwise block identity holds, rule_end precedes evidence "
              f"in every cell ({args.model})")
        return

    tok, model = load_model(args.model)
    dids = digit_ids(tok).to(model.device)
    layers = decoder_layers(model)
    nL = len(layers)
    Ls = list(frozen_layers(nL))
    if PRIMARY_LAYER >= nL:
        raise SystemExit(f"primary layer {PRIMARY_LAYER} >= {nL} layers")
    print(f"{len(items)} items, {nL} layers, frozen patch layers {Ls}, "
          f"phase={args.phase}, design={DESIGN_TAG}", flush=True)

    def run_plain(prompt):
        ids = tok(prompt, return_tensors="pt",
                  add_special_tokens=False)["input_ids"].to(model.device)
        return float(digit_expectation(model(input_ids=ids).logits[0, -1],
                                       dids)), ids.shape[1]

    recs = []
    with torch.no_grad():
        for n, it in enumerate(items):
            P = build_cells(tok, it)
            rec = {"item_id": it.item_id, "direction": it.critical_direction,
                   "y": {}, "n_tok": {}}

            store = {}
            for cell in CELLS:
                prompt, sites = P[cell]["prompt"], P[cell]["sites"]
                if args.phase == "patch":
                    # capture this cell's own rule-end state at the frozen
                    # layers while reading its baseline (read-only hooks)
                    holder = {}

                    def mk(L, pos=sites["rule_end"]):
                        def h(mod, inp, outp):
                            o = outp[0] if isinstance(outp, tuple) else outp
                            holder[L] = o[0, pos, :].detach().clone()
                        return h
                    hs = [layers[L].register_forward_hook(mk(L)) for L in Ls]
                    y, nt = run_plain(prompt)
                    for h in hs:
                        h.remove()
                    store[cell] = holder
                else:
                    y, nt = run_plain(prompt)
                rec["y"][cell] = y
                rec["n_tok"][cell] = nt

            if args.phase == "patch":
                rec["patch"] = {}
                for dname, (donor, recip) in DIRECTIONS.items():
                    prompt, sites = P[recip]["prompt"], P[recip]["sites"]
                    pos = sites["rule_end"]
                    res = {}
                    for L in Ls:
                        d = store[donor][L]

                        def write(mod, inp, outp, d=d, pos=pos):
                            o = outp[0] if isinstance(outp, tuple) else outp
                            o[0, pos, :] = d
                            return (o,) + outp[1:] if isinstance(outp, tuple) else o
                        hh = layers[L].register_forward_hook(write)
                        y, _nt = run_plain(prompt)
                        hh.remove()
                        res[str(L)] = y
                    rec["patch"][dname] = res

                # §9.1 identity: each cell's own rule-end state patched back
                # into itself, one frozen layer at a time
                rec["identity"] = {str(L): {} for L in Ls}
                for L in Ls:
                    for cell in CELLS:
                        prompt, sites = P[cell]["prompt"], P[cell]["sites"]
                        d = store[cell][L]

                        def write_id(mod, inp, outp, d=d, pos=sites["rule_end"]):
                            o = outp[0] if isinstance(outp, tuple) else outp
                            o[0, pos, :] = d
                            return (o,) + outp[1:] if isinstance(outp, tuple) else o
                        hh = layers[L].register_forward_hook(write_id)
                        y, _nt = run_plain(prompt)
                        hh.remove()
                        rec["identity"][str(L)][cell] = y

            recs.append(rec)
            if (n + 1) % 5 == 0:
                print(f"  {n + 1}/{len(items)}", flush=True)

    design = dict(design_tag=DESIGN_TAG, model=args.model, tag=args.tag,
                  phase=args.phase, n_layers=nL, layers=Ls,
                  primary=PRIMARY_LAYER, controls=[CONTROL_LAYERS[0],
                                                   Ls[-1]],
                  sites=["rule_end"], n_items=len(items),
                  identity_tol=IDENTITY_TOL, families=list(FAMILIES),
                  seed=SEED)
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump({"design": design, "records": recs}, open(out, "w"))
    print(f"wrote {len(recs)} records -> {out}")


if __name__ == "__main__":
    main()
