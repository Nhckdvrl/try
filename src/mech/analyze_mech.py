import json, os, sys, statistics as st
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from analyze import boot_ci, boot_p, wins

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
d = json.load(open(os.path.join(ROOT, "results", "mech", "experiments.json")))
nL, recs = d["n_layers"], d["records"]

use = []
for r in recs:
    s = 1.0 if r["direction"] == "increase" else -1.0
    y = r["y"]
    ya = (y["admit_pre"] + y["admit_post"]) / 2.0
    L = ya - y["base"]
    if s * L <= 0:
        continue
    r["s"], r["ya"], r["L"] = s, ya, L
    r["rei"] = lambda v, r=r: r["s"] * (v - r["y"]["base"]) / abs(r["L"])
    use.append(r)

out = ["# Mechanism — Qwen3-8B (legal_judgment + evidence_inference)", "",
       f"{len(use)} of {len(recs)} items have usable leverage under the fixed-position readout.",
       "REI: 0 = as if the evidence had never been seen, 1 = used as if admitted.", ""]

# ---------- headline REI under the mechanism readout ----------
pre = [wins(r["rei"](r["y"]["exclude_pre"])) for r in use]
post = [wins(r["rei"](r["y"]["exclude_post"])) for r in use]
for nm, v in (("REI exclude_pre ", pre), ("REI exclude_post", post)):
    m, lo, hi = boot_ci(v, seed=1)
    out.append(f"{nm}  {m:+.3f} [{lo:+.3f},{hi:+.3f}]")
dd = [a - b for a, b in zip(pre, post)]
m, lo, hi = boot_ci(dd, seed=2)
out.append(f"pre - post        {m:+.3f} [{lo:+.3f},{hi:+.3f}] p={boot_p(dd, seed=3):.4f}")
out.append("")

# ---------- C. evidence-span gate ----------
out.append("## C. Evidence-span causal gate")
out.append("Every query position downstream of the evidence is blocked from attending to it.")
for c in ("exclude_pre", "exclude_post"):
    have = [r for r in use if c in r.get("gate", {})]
    g = [wins(r["rei"](r["gate"][c])) for r in have]
    u = [wins(r["rei"](r["y"][c])) for r in have]
    mg, lg, hg = boot_ci(g, seed=4)
    diff = [a - b for a, b in zip(u, g)]
    md, ld, hd = boot_ci(diff, seed=5)
    out.append(f"  {c:13s} n={len(have)}  REI ungated {st.mean(u):+.3f} -> gated {mg:+.3f} "
               f"[{lg:+.3f},{hg:+.3f}]   removed {md:+.3f} [{ld:+.3f},{hd:+.3f}] "
               f"p={boot_p(diff, seed=6):.4f}")
out.append("")

# ---------- A. attention routing ----------
out.append("## A. Attention at the answer position (mean over heads, summed over span)")
out.append("Reported per span and normalised per token, since the spans differ in length.")
out.append(f"  {'layer band':12s} {'evidence pre':>13s} {'evidence post':>14s} {'rule pre':>10s} {'rule post':>10s}")
bands = [(0, 9), (9, 18), (18, 27), (27, nL)]
for a, b in bands:
    cell = {}
    for c in ("exclude_pre", "exclude_post"):
        have = [r for r in use if c in r.get("attn", {})]
        for k in ("evidence", "rule"):
            v = [st.mean(r["attn"][c][k][a:b]) / r["span_len"][c][k] for r in have]
            cell[(c, k)] = st.mean(v)
    out.append(f"  {f'{a}-{b-1}':12s} {cell[('exclude_pre','evidence')]:13.5f} "
               f"{cell[('exclude_post','evidence')]:14.5f} {cell[('exclude_pre','rule')]:10.5f} "
               f"{cell[('exclude_post','rule')]:10.5f}")
# ratio rule:evidence
out.append("")
for c in ("exclude_pre", "exclude_post"):
    have = [r for r in use if c in r.get("attn", {})]
    ratio = []
    for r in have:
        ev = st.mean([st.mean(r["attn"][c]["evidence"])]) / r["span_len"][c]["evidence"]
        ru = st.mean([st.mean(r["attn"][c]["rule"])]) / r["span_len"][c]["rule"]
        ratio.append(ru / ev if ev > 0 else float("nan"))
    m, lo, hi = boot_ci(ratio, seed=9, stat=st.median)
    out.append(f"  per-token attention ratio rule:evidence, {c:13s} median {m:.2f} [{lo:.2f},{hi:.2f}]")
out.append("")

# ---------- B. patching ----------
out.append("## B. Answer-position patching (Post -> Pre), recovery toward Post")
out.append("1.0 = the patched run answers like exclude_post; 0.0 = like exclude_pre.")
rec = []
for r in use:
    a, b = r["y"]["exclude_pre"], r["y"]["exclude_post"]
    if abs(b - a) < 2.0:
        continue
    rec.append([(p - a) / (b - a) for p in r["patch_post_into_pre"]])
out.append(f"  n={len(rec)} items with |post-pre| >= 2 points")
line = []
for L in range(nL):
    v = [x[L] for x in rec]
    line.append(f"L{L:02d}={st.median(v):+.2f}")
for i in range(0, nL, 6):
    out.append("  " + "  ".join(line[i:i + 6]))
firsts = []
for x in rec:
    hit = next((L for L in range(nL) if x[L] >= 0.5), nL - 1)
    firsts.append(hit)
out.append(f"  median layer at which patching first recovers >=50% of the gap: {st.median(firsts):.0f} / {nL}")

txt = "\n".join(out)
print(txt)
open(os.path.join(ROOT, "results", "mech", "mechanism_report.md"), "w").write(txt + "\n")
