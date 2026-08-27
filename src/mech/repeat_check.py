"""Does the prompt-level rescue (repeating the rule after the evidence) show the
attention signature the Pre/Post contrast predicts?"""
import os, sys, json, statistics as st
import torch
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from common import (load_model, mech_prompt, digit_ids, digit_expectation,
                    frozen_items, span_indices, ROOT)
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from analyze import boot_ci, wins

FAMILIES = ("legal_judgment", "evidence_inference")
CONDS = ["base", "admit_pre", "admit_post", "exclude_pre", "exclude_post", "exclude_pre_repeat"]

tok, model = load_model()
dids = digit_ids(tok).to(model.device)
items = frozen_items(FAMILIES)
recs = []
with torch.no_grad():
    for n, it in enumerate(items):
        rec = dict(item_id=it.item_id, direction=it.critical_direction, y={}, ratio={})
        for c in CONDS:
            p = mech_prompt(tok, it, c)
            ids = tok(p, return_tensors="pt", add_special_tokens=False)["input_ids"].to(model.device)
            want = c in ("exclude_pre", "exclude_post", "exclude_pre_repeat")
            out = model(input_ids=ids, output_attentions=want)
            rec["y"][c] = float(digit_expectation(out.logits[0, -1], dids))
            if want:
                ev = span_indices(tok, p, it.critical_evidence)
                # for the repeat condition, take the LAST occurrence of the rule
                c0 = p.rindex(it.exclude_rule)
                ru = span_indices(tok, p[:c0] + "\x00" * len(it.exclude_rule) + p[c0 + len(it.exclude_rule):],
                                  "\x00" * len(it.exclude_rule))
                aev = aru = 0.0
                for L in range(len(model.model.layers)):
                    a = out.attentions[L][0, :, -1, :].float().mean(0)
                    aev += float(a[ev[0]:ev[1]].sum()) / (ev[1] - ev[0])
                    aru += float(a[ru[0]:ru[1]].sum()) / (ru[1] - ru[0])
                rec["ratio"][c] = aru / aev if aev > 0 else float("nan")
            del out
        recs.append(rec)
        if (n + 1) % 20 == 0:
            print(f"  {n+1}/{len(items)}", flush=True)

use = []
for r in recs:
    s = 1.0 if r["direction"] == "increase" else -1.0
    L = (r["y"]["admit_pre"] + r["y"]["admit_post"]) / 2 - r["y"]["base"]
    if s * L <= 0:
        continue
    r["rei"] = {c: s * (r["y"][c] - r["y"]["base"]) / abs(L) for c in CONDS}
    use.append(r)

out = ["# Rule-repeat check — Qwen3-8B", "", f"n={len(use)}", ""]
for c in ("exclude_pre", "exclude_pre_repeat", "exclude_post"):
    v = [wins(r["rei"][c]) for r in use]
    m, lo, hi = boot_ci(v, seed=1)
    rt = [r["ratio"][c] for r in use if r["ratio"].get(c) == r["ratio"].get(c)]
    mr, lr, hr = boot_ci(rt, seed=2, stat=st.median)
    out.append(f"{c:20s} REI {m:+.3f} [{lo:+.3f},{hi:+.3f}]   "
               f"per-token attention ratio rule:evidence (median) {mr:.2f} [{lr:.2f},{hr:.2f}]")
txt = "\n".join(out)
print(txt)
open(os.path.join(ROOT, "results", "mech", "repeat_check.md"), "w").write(txt + "\n")
json.dump(recs, open(os.path.join(ROOT, "results", "mech", "repeat_check.json"), "w"))
