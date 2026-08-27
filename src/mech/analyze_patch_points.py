"""Stage 5, recomputed in raw rating points.

The recovery-fraction view divides by (donor - recipient), which for some items is
only a few points, so the ratio blows up and the median swings with the item
subset (the same instability that forced Stage 3E off REI). The primary number
here is therefore the sign-aligned shift the patch produces, in rating points,
with the fraction reported alongside on items where the denominator is large
enough to be stable.
"""
import json, os, sys, statistics as st
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
from analyze import boot_ci

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..")
MIN_GAP = 5.0


def load_all(tag):
    """Merge every run that carries the same 4-condition design for this model."""
    recs, seen = [], set()
    for fn in (f"patch_matched{'' if tag == 'qwen3-8b' else '_' + tag}.json",
               f"steer_did_{tag}.json"):
        p = os.path.join(ROOT, "results", "mech", fn)
        if not os.path.exists(p):
            continue
        d = json.load(open(p))
        for r in d["records"]:
            if r["item_id"] in seen:
                continue
            seen.add(r["item_id"])
            key = "patch" if "patch" in r else "factorial"
            r["_layers"] = d["layers"]
            r["_src"] = key
            recs.append(r)
    return recs


def series(r, direction):
    """(layers, values) for the rule-span transfer in one direction."""
    if r["_src"] == "patch":
        v = r["patch"].get(direction, {}).get("rule_span")
    else:
        v = r["factorial"].get("ME_into_UE" if direction == "success_into_failure" else None)
    return r["_layers"], v


def main(tag):
    recs = load_all(tag)
    out = [f"# Stage 5 recomputed in rating points — {tag}", "",
           f"{len(recs)} items pooled across runs. Only items where the failure and success",
           f"runs differ by at least {MIN_GAP:.0f} points are used, so the fraction is not",
           "dominated by tiny denominators.", ""]
    for direction, nm, own_k, don_k in (
            ("success_into_failure", "SUCCESS state into the FAILURE run", "UE", "ME"),
            ("failure_into_success", "FAILURE state into the SUCCESS run", "ME", "UE")):
        rows = []
        for r in recs:
            Ls, v = series(r, direction)
            if not v:
                continue
            own, don = r["y"][own_k], r["y"][don_k]
            s = 1.0 if r["direction"] == "increase" else -1.0
            if abs(don - own) < MIN_GAP:
                continue
            rows.append((Ls, v, own, don, s))
        if not rows:
            continue
        out.append(f"## {nm}   (n = {len(rows)})\n")
        out.append("| layer | shift toward donor, points | fraction of the gap |")
        out.append("|---:|---|---|")
        Ls = rows[0][0]
        for li, L in enumerate(Ls):
            pts, frac = [], []
            for Lr, v, own, don, s in rows:
                if li >= len(v) or v[li] is None:
                    continue
                pts.append(s * (v[li] - own) * (1 if don < own else -1) * -1)
                frac.append((v[li] - own) / (don - own))
            if len(pts) < 8:
                continue
            m, lo, hi = boot_ci([abs(x) for x in pts], n=4000, seed=1)
            out.append(f"| {L} | {st.mean(pts):+.1f} [{lo:.1f} abs] | {st.median(frac):+.2f} |")
        out.append("")
    txt = "\n".join(out)
    print(txt)
    open(os.path.join(ROOT, "results", "mech", f"patch_points_{tag}.md"), "w").write(txt + "\n")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "qwen3-8b")
