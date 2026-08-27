"""Is the rule-span state exclusion-specific and shared across items?"""
import json, os, sys, statistics as st
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from analyze import boot_ci

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
tag = sys.argv[1] if len(sys.argv) > 1 else "qwen3-8b"
d = json.load(open(os.path.join(ROOT, "results", "mech", f"steer_did_{tag}.json")))
Ls, recs, alphas = d["layers"], d["records"], d["alphas"]

use = []
for r in recs:
    s = 1.0 if r["direction"] == "increase" else -1.0
    y = r["y"]
    if abs(y["UE"] - y["ME"]) < 2.0:
        continue
    r["s"] = s
    use.append(r)

out = [f"# Exclusion-specificity and transferability of the rule-span state — {tag}", "",
       f"{len(use)} of {len(recs)} held-out items with a behavioural gap >= 2 points; the",
       f"steering direction was estimated on {d['n_train']} disjoint training items.", ""]

# ---- 1. factorial patch ----
out += ["## 1. Is the transfer exclusion-specific?", "",
        "Whole rule-span transfer inside each arm. If the matched preview transferred only",
        "proposition information, `MA -> UA` would move as much as `ME -> UE`.", "",
        "| layer | ME -> UE (exclude arm) | MA -> UA (admit arm) |", "|---:|---|---|"]
for li, L in enumerate(Ls):
    cells = []
    for key, don, own in (("ME_into_UE", "ME", "UE"), ("MA_into_UA", "MA", "UA")):
        vals = []
        for r in use:
            v = r["factorial"].get(key)
            if not v or v[li] is None:
                continue
            a, b = r["y"][own], r["y"][don]
            if abs(b - a) < 2.0:
                continue
            vals.append((v[li] - a) / (b - a))
        cells.append(f"{st.median(vals):+.2f}" if len(vals) >= 8 else "—")
    out.append(f"| {L} | {cells[0]} | {cells[1]} |")

# ---- 2. held-out steering ----
out += ["", "## 2. Does a direction estimated on other items control suppression?", "",
        "`v_l = mean[(h_ME - h_MA) - (h_UE - h_UA)]` over training items, added to the",
        "failing run's rule span and subtracted from the succeeding run's. alpha is a",
        "fraction of that layer's mean activation magnitude. Values are the change in the",
        "sign-aligned rating, in points; negative means more suppression.", ""]
out.append("| layer | " + " | ".join(f"UE +{a}v" for a in alphas[1:])
           + " | " + " | ".join(f"ME −{a}v" for a in alphas[1:]) + " |")
out.append("|---:|" + "---|" * (2 * (len(alphas) - 1)))
best = None
for L in Ls:
    row = []
    for tagn in ("UE", "ME"):
        for ai in range(1, len(alphas)):
            deltas = []
            for r in use:
                v = r["steer"].get(tagn, {}).get(str(L)) or r["steer"].get(tagn, {}).get(L)
                if not v or v[ai] is None or v[0] is None:
                    continue
                deltas.append(r["s"] * (v[ai] - v[0]))
            row.append(f"{st.mean(deltas):+.1f}" if len(deltas) >= 8 else "—")
    out.append(f"| {L} | " + " | ".join(row) + " |")
    try:
        ue = float(row[len(alphas) - 2])
        if best is None or ue < best[1]:
            best = (L, ue)
    except ValueError:
        pass
if best:
    L = best[0]
    deltas = []
    for r in use:
        v = r["steer"].get("UE", {}).get(str(L)) or r["steer"].get("UE", {}).get(L)
        if v and v[-1] is not None and v[0] is not None:
            deltas.append(r["s"] * (v[-1] - v[0]))
    if deltas:
        m, lo, hi = boot_ci(deltas, n=4000, seed=1)
        out += ["", f"Strongest layer {L}, largest alpha: adding the held-out direction to the "
                    f"failing run changes the sign-aligned rating by **{m:+.1f} "
                    f"[{lo:+.1f}, {hi:+.1f}]** points."]
txt = "\n".join(out)
print(txt)
open(os.path.join(ROOT, "results", "mech", f"steer_report_{tag}.md"), "w").write(txt + "\n")
