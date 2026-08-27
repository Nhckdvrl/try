"""Stage-1 follow-ups: is Pre-failure a rule-distance effect, and do the
structural mitigations work?  Uses the same base/admit anchors as the main run."""
import argparse, json, os, sys, statistics as st
from collections import defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from schema import load_items
from analyze import boot_ci, boot_p, wins

ROOT = os.path.join(os.path.dirname(__file__), "..")
EXTRA = ["exclude_pre", "exclude_pre_repeat", "exclude_post", "exclude_post_reencode",
         "ledger", "sanitation", "admit_pre", "admit_post", "admit_pre_repeat"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--runs", nargs="+", required=True)
    ap.add_argument("--tag", required=True)
    ap.add_argument("--out-prefix", required=True)
    args = ap.parse_args()

    items = {i.item_id: i for i in load_items(os.path.join(ROOT, "data", "items", "items_v1.jsonl"))}
    runs = defaultdict(dict)
    for p in args.runs:
        for line in open(p):
            r = json.loads(line)
            runs[r["item_id"]][r["kind_name"]] = r

    rei = defaultdict(list)
    for iid, r in runs.items():
        it = items.get(iid)
        if it is None or "base" not in r:
            continue
        y0 = r["base"]["value"]
        if y0 is None or any(k not in r or r[k]["value"] is None for k in ("admit_pre", "admit_post")):
            continue
        s = 1.0 if it.critical_direction == "increase" else -1.0
        L = (r["admit_pre"]["value"] + r["admit_post"]["value"]) / 2.0 - y0
        if s * L <= 0:
            continue
        for c in EXTRA:
            if c in r and r[c]["value"] is not None:
                rei[c].append(s * (r[c]["value"] - y0) / abs(L))

    out = [f"# Stage-1 follow-ups — {args.tag}", "",
           "REI: 0 = decided as if the evidence had never been seen, 1 = used it fully.", ""]
    out.append(f"{'condition':24s} {'n':>4s} {'REI mean [95% CI]':>28s}")
    for c in EXTRA:
        v = [wins(x) for x in rei[c]]
        if not v:
            continue
        m, lo, hi = boot_ci(v, seed=hash(c) % 997)
        out.append(f"{c:24s} {len(v):4d} {f'{m:+.3f} [{lo:+.3f},{hi:+.3f}]':>28s}")

    out.append("")
    out.append("Paired contrasts (positive = the first condition leaks more):")
    pairs = [("exclude_pre", "exclude_pre_repeat", "does repeating the rule after the evidence rescue Pre?"),
             ("exclude_pre", "exclude_post", "the temporal asymmetry itself"),
             ("exclude_post", "exclude_post_reencode", "does restating E as excluded help Post?"),
             ("exclude_pre", "ledger", "Pre vs structured evidence ledger"),
             ("exclude_post", "ledger", "Post vs structured evidence ledger"),
             ("exclude_pre", "sanitation", "Pre vs full context sanitation"),
             ("admit_pre", "admit_pre_repeat", "order control: repeating an ADMIT rule")]
    for a, b, why in pairs:
        n = min(len(rei[a]), len(rei[b]))
        if n == 0:
            continue
        d = [wins(x) - wins(y) for x, y in zip(rei[a], rei[b])]
        m, lo, hi = boot_ci(d, seed=7)
        p = boot_p(d, seed=8)
        out.append(f"  {a} - {b:24s} {m:+.3f} [{lo:+.3f},{hi:+.3f}] p={p:.4f}   ({why})")

    txt = "\n".join(out)
    print(txt)
    open(args.out_prefix + ".md", "w").write(txt + "\n")
    json.dump({c: rei[c] for c in EXTRA}, open(args.out_prefix + ".json", "w"))


if __name__ == "__main__":
    main()
