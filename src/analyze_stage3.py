"""Stage-3A analysis: is zero a discontinuity, and what is actually missing?"""
import argparse, json, os, sys, random, statistics as st
from collections import defaultdict
sys.path.insert(0, os.path.dirname(__file__))
import numpy as np
from schema import load_items
from analyze import boot_ci, boot_p, wins
from analyze_stage2 import cluster_of, ols_cluster_boot
import conditions_v3 as v3

ROOT = os.path.join(os.path.dirname(__file__), "..")


def load(tag):
    runs = defaultdict(dict)
    for line in open(os.path.join(ROOT, "results", "raw", f"{tag}_stage3.jsonl")):
        r = json.loads(line)
        runs[r["item_id"]][r["kind_name"]] = r
    return runs


def anchor(runs, items, base_key, full_keys):
    out = {}
    for iid, r in runs.items():
        it = items.get(iid)
        if it is None or base_key not in r or r[base_key].get("value") is None:
            continue
        if any(k not in r or r[k].get("value") is None for k in full_keys):
            continue
        s = 1.0 if it.critical_direction == "increase" else -1.0
        y0 = r[base_key]["value"]
        L = st.mean(r[k]["value"] for k in full_keys) - y0
        if s * L <= 0:
            continue
        out[iid] = (y0, abs(L), s)
    return out


def rei(runs, anch, iid, cond):
    r = runs[iid].get(cond)
    if r is None or r.get("value") is None:
        return None
    y0, absL, s = anch[iid]
    return s * (r["value"] - y0) / absL


def col(runs, anch, cond):
    return [(iid, wins(v)) for iid in anch
            if (v := rei(runs, anch, iid, cond)) is not None]


def run_tag(tag, items, out):
    runs = load(tag)
    out.append(f"\n# {tag}\n")
    A = anchor(runs, items, "base", ["nz1000_pre", "nz1000_post"])
    B = anchor(runs, items, "id_base", ["id_admit_pre", "id_admit_post"])

    # ---------- A: near-zero sweep ----------
    out.append(f"## A. Near-zero sweep — is zero a discontinuity?   (n = {len(A)})\n")
    out.append("One identical sentence; only the percentage changes.\n")
    out.append("| requested w | rule BEFORE evidence | rule AFTER evidence | pre - post |")
    out.append("|---:|---|---|---|")
    rows = []
    gaps = {}
    for key, w in v3.NZ_LEVELS.items():
        a = dict(col(runs, A, f"{key}_pre"))
        b = dict(col(runs, A, f"{key}_post"))
        ks = sorted(set(a) & set(b))
        if not ks:
            continue
        va, vb = [a[k] for k in ks], [b[k] for k in ks]
        ma, la, ha = boot_ci(va, n=4000, seed=1)
        mb, lb, hb = boot_ci(vb, n=4000, seed=1)
        d = [x - y for x, y in zip(va, vb)]
        md, ld, hd = boot_ci(d, n=4000, seed=2)
        gaps[w] = md
        out.append(f"| {w:.3g} | {ma:+.3f} [{la:+.3f}, {ha:+.3f}] | {mb:+.3f} [{lb:+.3f}, {hb:+.3f}] "
                   f"| **{md:+.3f}** [{ld:+.3f}, {hd:+.3f}] p={boot_p(d, n=4000, seed=3):.4f} |")
        for k in ks:
            rows.append((a[k], w, 1.0, 1.0 if w == 0 else 0.0, cluster_of(items[k])))
            rows.append((b[k], w, 0.0, 0.0, cluster_of(items[k])))
    if rows:
        y = np.array([r[0] for r in rows])
        X = np.column_stack([np.ones(len(rows)), [r[1] for r in rows], [r[2] for r in rows],
                             [r[1] * r[2] for r in rows], [r[3] for r in rows]])
        beta, lo, hi, p = ols_cluster_boot(X, y, [r[4] for r in rows], n=3000, seed=1)
        names = ["intercept", "w", "Before", "w x Before", "**I[w=0] x Before**"]
        out.append("\n`REI ~ w + Before + w:Before + I[w=0]:Before`, cluster bootstrap:\n")
        out.append("| term | coef | 95% CI | p |")
        out.append("|---|---|---|---|")
        for i, nm in enumerate(names):
            out.append(f"| {nm} | {beta[i]:+.4f} | [{lo[i]:+.4f}, {hi[i]:+.4f}] | {p[i]:.4f} |")
        if 0.0 in gaps and 0.01 in gaps:
            out.append(f"\ngap(0) = {gaps[0.0]:+.3f} vs gap(1%) = {gaps[0.01]:+.3f}"
                       f"  ->  ratio {gaps[0.0] / gaps[0.01]:.1f}x" if abs(gaps[0.01]) > 1e-6
                       else f"\ngap(0) = {gaps[0.0]:+.3f}, gap(1%) = {gaps[0.01]:+.3f}")

    # ---------- B: rule -> evidence delay ----------
    out.append(f"\n## B. Rule-to-evidence delay   (n = {len(A)})\n")
    out.append("Stage 2 moved the rule away from the ANSWER; this moves it away from the "
               "EVIDENCE it governs. Rule is always `weight = 0%`.\n")
    out.append("| filler between rule and evidence | rule BEFORE | rule AFTER | pre - post |")
    out.append("|---|---|---|---|")
    for k in v3.RD_LEVELS:
        a = dict(col(runs, A, f"rd_pre_{k}"))
        b = dict(col(runs, A, f"rd_post_{k}"))
        ks = sorted(set(a) & set(b))
        if not ks:
            continue
        va, vb = [a[i] for i in ks], [b[i] for i in ks]
        toks = st.median([runs[i][f"rd_pre_{k}"].get("rule_to_answer_tokens") or 0 for i in ks])
        d = [x - y for x, y in zip(va, vb)]
        md, ld, hd = boot_ci(d, n=4000, seed=4)
        out.append(f"| {v3.RD_LEVELS[k]} units (~{v3.RD_LEVELS[k]*25} tok) | "
                   f"{st.mean(va):+.3f} | {st.mean(vb):+.3f} | {md:+.3f} [{ld:+.3f}, {hd:+.3f}] |")

    # ---------- C: object-existence ladder ----------
    out.append(f"\n## C. Object-existence ladder   (n = {len(B)})\n")
    out.append("Identical rule (`Evidence E7 has decision weight 0.`) at every level; what "
               "changes is how much of E7 exists when the rule is stated. L5 is the "
               "retrospective anchor (full content already present).\n")
    lab = {"oe_L0": "L0 E7 never mentioned", "oe_L1": "L1 'you will later receive E7'",
           "oe_L2": "L2 [E7: content pending]", "oe_L3": "L3 + item type",
           "oe_L4": "L4 + type and direction", "oe_L5": "L5 full content BEFORE the rule"}
    for c in v3.OE_LEVELS:
        v = [x for _, x in col(runs, B, c)]
        if not v:
            continue
        m, lo, hi = boot_ci(v, n=4000, seed=5)
        out.append(f"- `{lab[c]}`: REI {m:+.3f} [{lo:+.3f}, {hi:+.3f}]")

    # ---------- D: non-multiplicative transforms ----------
    out.append(f"\n## D. Non-multiplicative transforms\n")
    out.append("| transform | rule BEFORE | rule AFTER | pre - post |")
    out.append("|---|---|---|---|")
    for key in v3.TRANSFORMS:
        a = dict(col(runs, A, f"{key}_pre"))
        b = dict(col(runs, A, f"{key}_post"))
        ks = sorted(set(a) & set(b))
        if not ks:
            continue
        d = [a[i] - b[i] for i in ks]
        md, ld, hd = boot_ci(d, n=4000, seed=6)
        tgt = " (target -1.0)" if key == "trflip" else ""
        out.append(f"| `{key}`{tgt} | {st.mean([a[i] for i in ks]):+.3f} | "
                   f"{st.mean([b[i] for i in ks]):+.3f} | {md:+.3f} [{ld:+.3f}, {hd:+.3f}] "
                   f"p={boot_p(d, n=4000, seed=7):.4f} |")

    # ---------- E: declarative state vs causal use ----------
    out.append(f"\n## E. Declarative policy state vs causal use\n")
    out.append("Separate call, same context, asked what weight E should get. The decision "
               "run never sees this question.\n")
    out.append("| arm | says weight (mean %) | says exactly 0 (%) | REI in the decision run |")
    out.append("|---|---:|---:|---|")
    for arm in ("pre", "post"):
        vals, zeros = [], []
        for iid in A:
            r = runs[iid].get(f"wprobe_{arm}")
            if r and r.get("value") is not None:
                vals.append(r["value"])
                zeros.append(1.0 if abs(r["value"]) < 1e-9 else 0.0)
        v = [x for _, x in col(runs, A, f"nz0000_{arm}")]
        m, lo, hi = boot_ci(v, n=4000, seed=8)
        out.append(f"| rule {arm.upper()} | {st.mean(vals):.2f} | {100*st.mean(zeros):.1f} | "
                   f"{m:+.3f} [{lo:+.3f}, {hi:+.3f}] |")

    # ---------- F: class policy vs item-specific ----------
    out.append(f"\n## F. Item-specific rule vs class-wide policy   (n = {len(B)})\n")
    for c, nm in (("oe_L0", "specific `E7 has weight 0`, rule first"),
                  ("oe_L5", "specific, rule last"),
                  ("cls_pre", "class policy `any unauthorised item has weight 0`, rule first"),
                  ("cls_post", "class policy, rule last")):
        v = [x for _, x in col(runs, B, c)]
        if not v:
            continue
        m, lo, hi = boot_ci(v, n=4000, seed=9)
        out.append(f"- {nm}: REI {m:+.3f} [{lo:+.3f}, {hi:+.3f}]")

    # ---------- G: task preview ----------
    out.append(f"\n## G. Task preview   (n = {len(A)})\n")
    for c, nm in (("nz0000_pre", "no preview, rule first"), ("tp_pre", "TASK PREVIEW, rule first"),
                  ("nz0000_post", "no preview, rule last"), ("tp_post", "TASK PREVIEW, rule last")):
        v = [x for _, x in col(runs, A, c)]
        if not v:
            continue
        m, lo, hi = boot_ci(v, n=4000, seed=10)
        out.append(f"- {nm}: REI {m:+.3f} [{lo:+.3f}, {hi:+.3f}]")
    a = dict(col(runs, A, "nz0000_pre")); b = dict(col(runs, A, "tp_pre"))
    ks = sorted(set(a) & set(b))
    if ks:
        d = [a[i] - b[i] for i in ks]
        m, lo, hi = boot_ci(d, n=4000, seed=11)
        out.append(f"- rescue from task preview (pre): {m:+.3f} [{lo:+.3f}, {hi:+.3f}] "
                   f"p={boot_p(d, n=4000, seed=12):.4f}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("tags", nargs="+")
    args = ap.parse_args()
    items = {i.item_id: i for i in load_items(os.path.join(ROOT, "data", "items", "items_v1.jsonl"))}
    out = ["# Stage 3A — naming the phenomenon", "",
           "REI is the effective causal weight the model gives the critical evidence.",
           "0 = decided as if it had never been seen; 1 = full normal evidential weight."]
    for t in args.tags:
        try:
            run_tag(t, items, out)
        except FileNotFoundError:
            out.append(f"\n# {t}: not run yet\n")
    txt = "\n".join(out)
    print(txt)
    open(os.path.join(ROOT, "results", "stage3_tables.md"), "w").write(txt + "\n")


if __name__ == "__main__":
    main()
