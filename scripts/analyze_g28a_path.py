"""Registered G28A paired analysis. All complete raw cells, no filtering."""

import argparse
import json
import math
import random
import statistics as st
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TAGS = ("mistral-small-24b", "qwen3-8b", "gemma3-12b")
CONDS = ("D", "RJ", "IJ", "RR")
ROLES = ("support", "refute")


def avg(xs):
    return st.mean(xs)


def pct(xs, q):
    xs = sorted(xs)
    x = (len(xs) - 1) * q
    i = int(x)
    return xs[i] + (x - i) * (xs[min(i + 1, len(xs) - 1)] - xs[i])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw-dir", default=str(ROOT / "results/raw"))
    ap.add_argument("--out", default=str(ROOT / "results/g28a/g28a_path_v1_analysis.md"))
    ap.add_argument("--tags", nargs="+", default=TAGS)
    ap.add_argument("--n", type=int, default=200)
    ap.add_argument("--ids-json", help="post hoc subset file with valid_natural_ids")
    args = ap.parse_args()

    rows = {}
    quality = defaultdict(Counter)
    for tag in args.tags:
        path = Path(args.raw_dir) / f"{tag}_g28a_path_v1.jsonl"
        data = [json.loads(x) for x in path.read_text().splitlines() if x]
        assert len(data) == args.n * 11, (tag, len(data))
        index = {}
        for r in data:
            assert r["model_tag"] == tag
            key = (r["cfb_id"], r["stage"], r.get("condition", r.get("role")), r.get("final_role"))
            assert key not in index, (tag, key)
            index[key] = r
            quality[tag]["unparsed"] += r["value"] is None
            quality[tag]["digit_mass_lt_0.5"] += r["mass"] < .5
            quality[tag]["rationale_caps"] += r["reason_truncated"]
        assert len(index) == len(data)
        rows[tag] = index

    all_claim_ids = sorted({r["cfb_id"] for r in data})
    assert len(all_claim_ids) == args.n
    for tag, index in rows.items():
        assert {k[0] for k in index} == set(all_claim_ids)
        assert all(r["value"] is not None and math.isfinite(r["value"]) for r in index.values())
        for cid in all_claim_ids:
            assert sum(k[0] == cid and k[1] == "initial" for k in index) == 3
            assert sum(k[0] == cid and k[1] == "final" for k in index) == 8
            for role in ROLES:
                for cond in CONDS:
                    assert (cid, "final", cond, role) in index

    claim_ids = all_claim_ids
    if args.ids_json:
        selected = set(json.loads(Path(args.ids_json).read_text())["valid_natural_ids"])
        assert selected <= set(all_claim_ids)
        claim_ids = sorted(selected)

    def v(tag, cid, cond, role):
        return rows[tag][(cid, "final", cond, role)]["value"]

    # Claim is the independent bootstrap unit; within each resampled claim,
    # keep every model and both E2 directions paired.
    def per_claim(tag, cid):
        out = {}
        for role in ROLES:
            oldsign = -1 if role == "support" else 1
            y = {cond: v(tag, cid, cond, role) for cond in CONDS}
            pref = role + "_"
            out[pref + "T"] = oldsign * (y["RJ"] - y["IJ"])
            out[pref + "Tread"] = oldsign * (y["RR"] - y["IJ"])
            for cond in ("RJ", "IJ", "RR"):
                out[pref + "AE_" + cond] = abs(y[cond] - y["D"])
                out[pref + "signed_" + cond] = y[cond] - y["D"]
                out[pref + "cross50_" + cond] = int((y[cond] >= 50) != (y["D"] >= 50))
        for key in ("T", "Tread", "AE_RJ", "AE_IJ", "AE_RR", "cross50_RJ", "cross50_IJ", "cross50_RR"):
            out["both_" + key] = (out["support_" + key] + out["refute_" + key]) / 2
        for cond in CONDS:
            out["sep_" + cond] = v(tag, cid, cond, "support") - v(tag, cid, cond, "refute")
        return out

    by_tag = {tag: {cid: per_claim(tag, cid) for cid in claim_ids} for tag in args.tags}
    rng = random.Random("g28a_path_v1_claim_bootstrap")
    draws = [[rng.choice(claim_ids) for _ in claim_ids] for _ in range(5000)]

    def summarize(key, tags):
        point = avg(by_tag[t][c][key] for t in tags for c in claim_ids)
        boots = [avg(by_tag[t][c][key] for t in tags for c in draw) for draw in draws]
        return f"{point:.2f} [{pct(boots, .025):.2f}, {pct(boots, .975):.2f}]"

    out = ["# G28A equal-final-evidence path experiment",
           "", "Exploratory, reused ConfB claims. See `results/discovery/g28a_path_v1_registration.md`.",
           (f"Post hoc audit-restricted sensitivity: {len(claim_ids)}/{args.n} claims; not a new confirmation. " if args.ids_json else "Full frozen sample. ") +
           f"{args.n} run claims × {len(args.tags)} models × 11 rows = {args.n * len(args.tags) * 11} raw rows. "
           "Claim-cluster paired bootstrap, 5,000 draws, seed fixed in analyzer. Scores 0–100.",
           "", "## Integrity", "", "| Model | Rows | Unparsed | Digit mass <0.5 | Rationale cap |",
           "|---|---:|---:|---:|---:|"]
    for tag in args.tags:
        q = quality[tag]
        out.append(f"| {tag} | {args.n * 11} | {q['unparsed']} | {q['digit_mass_lt_0.5']} | {q['rationale_caps']} |")
    out += ["", "## Registered primary contrast", "",
            "T = sign(revoked relevant E1) × (RJ − IJ). Positive means polarity-aligned carryover; negative means overcorrection. The RJ and IJ final turns use identical retraction wording and E2.",
            "", "| Model | Both E2 directions | E2 support | E2 refute |",
            "|---|---:|---:|---:|"]
    for tag in (*args.tags, "pooled"):
        tags = args.tags if tag == "pooled" else [tag]
        out.append(f"| {tag} | {summarize('both_T', tags)} | {summarize('support_T', tags)} | {summarize('refute_T', tags)} |")
    out += ["", "## History and direct path", "",
            "| Model | abs(RJ−D) | abs(IJ−D) | abs(RR−D) | T_read (RR−IJ) |",
            "|---|---:|---:|---:|---:|"]
    for tag in (*args.tags, "pooled"):
        tags = args.tags if tag == "pooled" else [tag]
        out.append(f"| {tag} | {summarize('both_AE_RJ', tags)} | {summarize('both_AE_IJ', tags)} | {summarize('both_AE_RR', tags)} | {summarize('both_Tread', tags)} |")
    out += ["", "## Final evidence use and threshold flips", "",
            "Separation = mean Y(E2 support) − mean Y(E2 refute). Flip = percent of final scores crossing 50 relative to D on the same claim and E2.",
            "", "| Model | D separation | RJ separation | IJ separation | RR separation | RJ flip % | IJ flip % | RR flip % |",
            "|---|---:|---:|---:|---:|---:|---:|---:|"]
    for tag in (*args.tags, "pooled"):
        tags = args.tags if tag == "pooled" else [tag]
        a = [summarize("sep_" + c, tags) for c in CONDS]
        flips = [100 * avg(by_tag[t][c]["both_cross50_" + cond] for t in tags for c in claim_ids)
                 for cond in ("RJ", "IJ", "RR")]
        out.append(f"| {tag} | " + " | ".join(a + [f"{f:.1f}" for f in flips]) + " |")
    out += ["", "Limits: D differs in dialogue length and retraction frame. RJ−IJ is the matched-frame primary contrast. RR differs from IJ in both E1 relevance and absence of an initial generated answer; it is a diagnostic, not an isolated content intervention. Initial judgments are included in raw output for later mediation analysis, but that analysis was not preregistered. All model responses are generated from textual histories; no persistent hidden state is tested.", ""]
    target = Path(args.out)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(out))
    print(target)


if __name__ == "__main__":
    main()
