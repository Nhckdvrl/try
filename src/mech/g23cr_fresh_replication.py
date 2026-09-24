"""G23C-R runner — joint fresh-material replication of G23C + G24B.

Frozen design: preregistrations/PREREGISTRATION_G23C_R_FRESH_REPLICATION.md,
tag `g23c-r-fresh-joint-replication-design-v1`.  Model forward passes are
authorized only by the repository-level STATUS.md update that follows the tag.

Phases (§5 audit before any forward pass; §8 stop rule: bridge first, joint
patching only after the gate passes):

  audit  — tokenizer-only (§5): all 70 items x 4 cells x both tokenizers;
           cell compilation, rule_end site, rule-before-evidence, the block-
           difference checks, and the recorded M-vs-U rule_end positions that
           drive the >5% / 4-token position gate.  No model load, no forward
           pass.  Exits non-zero and the design stops before compute if the
           gate fails.
  bridge — the four G18 cells, direct readout, no hooks (§8 Phase 1).
  patch  — the same four baselines (capturing each cell's rule-end state at
           the frozen layers), the 10 unique scientific patches of the §9.3
           union (8-cell G24B grid + ME->MA, UE->UA), and the 4-cell identity
           checks (ME/UE reused from the grid as §9.3 permits; MA/UA run
           fresh).

Cell construction is *imported*, not copied: `build` and `sites_of` come
verbatim from `patch_matched.py` (§6), and `uniform_weight_rule` runs inside
`build` — the only replacement is the preview source: byte-for-byte G18
`meta["previews"]["para"]` / `meta["previews"]["unrel"]`, never
`matched_previews` (§4 forbids constructing new previews).
"""
import os
import sys
import json
import argparse

import torch

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from common import (load_model, digit_ids, digit_expectation,  # noqa: E402
                    span_indices, decoder_layers, ROOT)
from patch_matched import build, sites_of                    # noqa: E402
sys.path.insert(0, os.path.join(HERE, ".."))
from analyze_g23cr import (CELLS, CELL_TABLE, FAMILIES,          # noqa: E402
                           PRIMARY_LAYER, CONTROL_LAYERS, DESIGN_TAG,
                           MODELS, MODEL_IDS, frozen_layers, IDENTITY_TOL,
                           SEED, SCIENTIFIC, load_g18_items,
                           position_gate, diff_within,
                           POSITION_TOL_TOKENS)

AUDIT_OUT = os.path.join(ROOT, "results", "mech", "g23cr_audit_v1.json")


def previews_of(item):
    """§4 byte-for-byte frozen G18 previews: para -> M, unrel -> U."""
    pv = item.meta["previews"]
    m, u = pv["para"], pv["unrel"]
    assert isinstance(m, str) and isinstance(u, str) and m and u \
        and m != u, item.item_id
    return m, u


def build_cells(tok, item):
    """The four §3 cells with the frozen construction checks (§9.2, §9.3).

    Same structure as the G23C/G24B runner `build_cells`, except the previews
    come from the frozen G18 file instead of `matched_previews`.
    """
    match, unrel = previews_of(item)
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


# ------------------------------------------------------------------ §5 audit
def _block_spans(tok, P, cell, idx):
    lo, hi = span_indices(tok, P[cell]["prompt"], P[cell]["blocks"][idx])
    return lo, hi


def audit_model(tok, items, model_name):
    """Tokenizer-only §5 audit for one model's tokenizer."""
    res = {"n_items": len(items),
           "failures": {"compile": [], "rule_end_missing": [],
                        "rule_before_evidence": [],
                        "M_pair_differs_outside_rule": [],
                        "U_pair_differs_outside_rule": [],
                        "M_vs_U_differs_outside_preview": []},
           "positions": {},     # item_id -> {d0, d100, pair}
           "n_checked_cells": 0}
    pair_diffs = {}
    for it in items:
        try:
            P = build_cells(tok, it)
        except (RuntimeError, AssertionError) as e:
            msg = str(e)
            if "rule_end site missing" in msg:
                res["failures"]["rule_end_missing"].append(it.item_id)
            elif "does not precede evidence" in msg:
                res["failures"]["rule_before_evidence"].append(it.item_id)
            else:
                res["failures"]["compile"].append(f"{it.item_id}: {msg}")
            continue
        res["n_checked_cells"] += len(CELLS)

        spans = {c: {"rule": _block_spans(tok, P, c, 2),
                     "preview": _block_spans(tok, P, c, 1)}
                 for c in CELLS}
        enc = {c: tok(P[c]["prompt"], add_special_tokens=False)["input_ids"]
               for c in CELLS}

        # checks 4/5: within one preview, 0% vs 100% differ only in the rule
        # block (strict block bounds, both cells' spans).
        for pair, key in ((("ME", "MA"), "M_pair_differs_outside_rule"),
                          (("UE", "UA"), "U_pair_differs_outside_rule")):
            a, b = pair
            lo = min(spans[a]["rule"][0], spans[b]["rule"][0])
            hi = max(spans[a]["rule"][1], spans[b]["rule"][1])
            if not diff_within(enc[a], enc[b], lo, hi):
                p, ea, eb = _diff(enc[a], enc[b])
                res["failures"][key].append(
                    {"item": it.item_id, "first_diff": p, "end_a": ea,
                     "end_b": eb, "rule_lo": lo, "rule_hi": hi})

        # check 6: at a fixed policy, M vs U differ only in the preview block.
        for a, b in (("ME", "UE"), ("MA", "UA")):
            lo = min(spans[a]["preview"][0], spans[b]["preview"][0])
            hi = max(spans[a]["preview"][1], spans[b]["preview"][1])
            if not diff_within(enc[a], enc[b], lo, hi):
                p, ea, eb = _diff(enc[a], enc[b])
                res["failures"]["M_vs_U_differs_outside_preview"].append(
                    {"item": it.item_id, "pair": f"{a}/{b}",
                     "first_diff": p, "end_a": ea, "end_b": eb,
                     "preview_lo": lo, "preview_hi": hi})

        # check 7: absolute M-vs-U rule_end position difference at each policy
        # value; the pair value gated by §5 is the max over both (the
        # conservative reading — documented in analyze_g23cr's docstring).
        d0 = abs(P["ME"]["sites"]["rule_end"] - P["UE"]["sites"]["rule_end"])
        d100 = abs(P["MA"]["sites"]["rule_end"]
                   - P["UA"]["sites"]["rule_end"])
        pair = max(d0, d100)
        res["positions"][it.item_id] = {"d_policy0": d0, "d_policy100": d100,
                                        "pair": pair}
        pair_diffs[f"{it.item_id}"] = pair

    res["gate"] = position_gate(pair_diffs)
    res["checks_passed"] = all(
        len(v) == 0 for v in res["failures"].values())
    res["passed"] = bool(res["checks_passed"] and res["gate"]["passed"])
    return res


def _diff(a, b):
    n = min(len(a), len(b))
    p = 0
    while p < n and a[p] == b[p]:
        p += 1
    s = 0
    while s < n - p and a[len(a) - 1 - s] == b[len(b) - 1 - s]:
        s += 1
    return p, len(a) - s, len(b) - s


def run_audit(items):
    """§5: both tokenizers, no model load, one combined position gate over
    all item/model pairs.  Returns (report, exit_code)."""
    from transformers import AutoTokenizer
    per_model = {}
    combined = {}
    for name in MODELS:
        print(f"audit: tokenizer {name} ({MODEL_IDS[name]}) ...", flush=True)
        tok = AutoTokenizer.from_pretrained(MODEL_IDS[name])
        r = audit_model(tok, items, name)
        per_model[name] = r
        for iid, d in r["positions"].items():
            combined[f"{iid}|{name}"] = d["pair"]
        print(f"  cells checked {r['n_checked_cells']} "
              f"({r['n_items']} x 4), failures "
              f"{ {k: len(v) for k, v in r['failures'].items()} }",
              flush=True)
        print(f"  per-model gate: over {r['gate']['n_over']}/"
              f"{r['gate']['n_pairs']} pairs > {POSITION_TOL_TOKENS} tokens "
              f"({r['gate']['frac_over']:.1%}), passed={r['gate']['passed']}",
              flush=True)

    gate_all = position_gate(combined)
    # §5 gates on the combined item/model pairs (140); the per-model gates
    # are diagnostic only (reported, not part of the pass decision).
    passed = all(per_model[m]["checks_passed"] for m in MODELS) \
        and gate_all["passed"]
    report = {"design_tag": DESIGN_TAG, "audit": "tokenizer-only",
              "items": len(items), "cells": list(CELLS),
              "models": list(MODELS), "per_model": per_model,
              "gate_all_models": gate_all, "passed": bool(passed)}
    os.makedirs(os.path.dirname(AUDIT_OUT), exist_ok=True)
    json.dump(report, open(AUDIT_OUT, "w"), indent=1)

    print(f"§5 position gate (all {gate_all['n_pairs']} item/model pairs): "
          f"{gate_all['n_over']} over {POSITION_TOL_TOKENS} tokens "
          f"({gate_all['frac_over']:.1%} vs 5% threshold), "
          f"passed={gate_all['passed']}")
    if passed:
        print(f"AUDIT PASS — 70 items x 4 cells x {len(MODELS)} tokenizers, "
              f"all §5 checks green; wrote {AUDIT_OUT}")
        return report, 0
    print(f"AUDIT FAIL — design stops before compute (§5). "
          f"See {AUDIT_OUT} for failing item lists / position diffs.")
    return report, 2


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", default=None)
    ap.add_argument("--tag", default=None, choices=list(MODELS))
    ap.add_argument("--phase", required=True,
                    choices=["audit", "bridge", "patch"])
    ap.add_argument("--limit", type=int, default=0,
                    help="0 = all frozen items; the frozen run uses 0")
    ap.add_argument("--out", default=None)
    args = ap.parse_args()

    items = load_g18_items()
    if args.limit:
        items = items[:args.limit]
    if args.phase != "audit" and len(items) != 70 and not args.limit:
        raise SystemExit(f"expected 70 G18 items, got {len(items)}")

    if args.phase == "audit":
        _, code = run_audit(items)
        sys.exit(code)

    if not args.model or not args.tag:
        raise SystemExit("--model and --tag are required for bridge/patch")
    out = args.out or os.path.join(ROOT, "results", "mech",
                                   f"g23cr_{args.phase}_{args.tag}.json")

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
                # §9.3: the 10 unique scientific patches of the union table
                # (8-cell grid + ME->MA, UE->UA), one write per frozen layer.
                rec["patch"] = {}
                for name in SCIENTIFIC:
                    donor, recip = name.split("_to_")
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
                    rec["patch"][name] = res

                # §9.3 identity: every cell's own rule-end state patched back
                # into itself at every frozen layer.  ME/UE are already in the
                # grid (ME_to_ME / UE_to_UE) and are reused; MA/UA run fresh.
                rec["identity"] = {str(L): {} for L in Ls}
                for L in Ls:
                    for cell in ("MA", "UA"):
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
                for L in Ls:
                    for cell, name in (("ME", "ME_to_ME"), ("UE", "UE_to_UE")):
                        rec["identity"][str(L)][cell] = \
                            rec["patch"][name][str(L)]

            recs.append(rec)
            if (n + 1) % 5 == 0:
                print(f"  {n + 1}/{len(items)}", flush=True)

    design = dict(design_tag=DESIGN_TAG, model=args.model, tag=args.tag,
                  phase=args.phase, n_layers=nL, layers=Ls,
                  primary=PRIMARY_LAYER, controls=[CONTROL_LAYERS[0],
                                                   Ls[-1]],
                  sites=["rule_end"], n_items=len(items),
                  identity_tol=IDENTITY_TOL, families=list(FAMILIES),
                  seed=SEED, patches=sorted(SCIENTIFIC),
                  skeleton_cluster="g18_meta.skeleton")
    os.makedirs(os.path.dirname(out), exist_ok=True)
    json.dump({"design": design, "records": recs}, open(out, "w"))
    print(f"wrote {len(recs)} records -> {out}")


if __name__ == "__main__":
    main()
