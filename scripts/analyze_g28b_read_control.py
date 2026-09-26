"""G28B registered matched-read analysis on frozen G28A RR and new IR rows."""

import argparse
import json
import random
import statistics as st
from collections import Counter
from pathlib import Path
from run_g28a_path import first_read, load_data, second, sha

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_TAGS = ("mistral-small-24b", "qwen3-8b", "gemma3-12b", "llama31-8b")


def avg(xs):
    return st.mean(xs)


def pct(xs, q):
    xs = sorted(xs)
    x = (len(xs) - 1) * q
    i = int(x)
    return xs[i] + (x - i) * (xs[min(i + 1, len(xs) - 1)] - xs[i])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tags", nargs="+", default=DEFAULT_TAGS)
    ap.add_argument("--out", default=str(ROOT / "results/g28a/g28b_read_control_analysis.md"))
    ap.add_argument("--ids-json", help="post hoc audit-restricted sensitivity")
    args = ap.parse_args()
    pairs, controls = load_data(ROOT / "data/items/g24a_confb_selected_v1.jsonl")
    source = {p["cfb_id"]: p for p in pairs}
    model_data = {}
    qualities = {}
    for tag in args.tags:
        a = [json.loads(s) for s in (ROOT / f"results/raw/{tag}_g28a_path_v1.jsonl").read_text().splitlines() if s]
        b = [json.loads(s) for s in (ROOT / f"results/raw/{tag}_g28b_read_control_v1.jsonl").read_text().splitlines() if s]
        assert len(a) == 2200 and len(b) == 400
        rr = {(r["cfb_id"], r["final_role"]): r for r in a if r["stage"] == "final" and r["condition"] == "RR"}
        ir = {(r["cfb_id"], r["final_role"]): r for r in b}
        assert len(rr) == len(ir) == 400 and set(rr) == set(ir)
        for key in rr:
            assert ir[key]["condition"] == "IR" and ir[key]["model_tag"] == tag
            assert rr[key]["messages"][-1] == ir[key]["messages"][-1]
            assert rr[key]["messages"][1] == ir[key]["messages"][1] == {"role": "assistant", "content": "Understood."}
            cid, role = key
            p = source[cid]
            e2 = p["evidence_s"] if role == "support" else p["evidence_r"]
            assert ir[key]["messages"] == [
                {"role": "user", "content": first_read(p["claim"], controls[cid])},
                {"role": "assistant", "content": "Understood."},
                {"role": "user", "content": second(e2)},
            ]
            assert ir[key]["prompt_sha256"] == sha(json.dumps(ir[key]["messages"], ensure_ascii=False, sort_keys=True))
            assert rr[key]["value"] is not None and ir[key]["value"] is not None
        model_data[tag] = (rr, ir)
        qualities[tag] = Counter({"unparsed": sum(r["value"] is None for r in b),
                                  "low_mass": sum(r["mass"] < .5 for r in b),
                                  "caps": sum(r["reason_truncated"] for r in b)})
    ids = sorted({key[0] for key in model_data[args.tags[0]][0]})
    assert len(ids) == 200
    if args.ids_json:
        ids = sorted(set(json.loads(Path(args.ids_json).read_text())["valid_natural_ids"]))
        assert set(ids) <= {key[0] for key in model_data[args.tags[0]][0]}
    metrics = {}
    for tag, (rr, ir) in model_data.items():
        metrics[tag] = {}
        for cid in ids:
            x = {}
            for role in ("support", "refute"):
                r = rr[(cid, role)]["value"]
                i = ir[(cid, role)]["value"]
                sign = -1 if role == "support" else 1
                x[role + "_T"] = sign * (r - i)
                x[role + "_abs"] = abs(r - i)
                x[role + "_flip"] = int((r >= 50) != (i >= 50))
                x[role + "_RR"] = r
                x[role + "_IR"] = i
            for k in ("T", "abs", "flip"):
                x["both_" + k] = (x["support_" + k] + x["refute_" + k]) / 2
            x["RR_sep"] = x["support_RR"] - x["refute_RR"]
            x["IR_sep"] = x["support_IR"] - x["refute_IR"]
            metrics[tag][cid] = x
    rng = random.Random("g28b_read_matched_bootstrap_v1")
    draws = [[rng.choice(ids) for _ in ids] for _ in range(5000)]

    def summary(key, tags):
        point = avg(metrics[tag][cid][key] for tag in tags for cid in ids)
        boots = [avg(metrics[tag][cid][key] for tag in tags for cid in draw) for draw in draws]
        return f"{point:.2f} [{pct(boots, .025):.2f},{pct(boots, .975):.2f}]"

    out = ["# G28B matched irrelevant-read control", "",
           "Exploratory, registered after observing preliminary G28A results. Reuses every frozen G28A RR score and adds 400 IR scores per model; no item selection. " +
           (f"Post hoc audit-restricted sensitivity on {len(ids)}/200 items." if args.ids_json else "Full frozen 200-item sample."),
           "Claim-cluster paired bootstrap, 5,000 draws. Scores 0–100. Llama-3.1-8B is an unplanned substitute for unsupported Qwen3.5-9B.",
           "", "## G28B raw integrity", "",
           "| Model | New IR rows | Unparsed | Digit mass <0.5 | Rationale caps |",
           "|---|---:|---:|---:|---:|"]
    for tag in args.tags:
        q = qualities[tag]
        out.append(f"| {tag} | 400 | {q['unparsed']} | {q['low_mass']} | {q['caps']} |")
    out += ["", "## Matched read contrast", "",
            "T_read_matched = sign(revoked relevant E1) × (RR−IR). RR and IR both contain a read-only first turn and identical acknowledgment and final turn.",
            "", "| Model | Both directions | E2 support | E2 refute | Mean abs(RR−IR) | RR sep | IR sep | 50-threshold flip % |",
            "|---|---:|---:|---:|---:|---:|---:|---:|"]
    for tag in (*args.tags, "pooled"):
        tags = args.tags if tag == "pooled" else [tag]
        vals = [summary(k, tags) for k in ("both_T", "support_T", "refute_T", "both_abs", "RR_sep", "IR_sep")]
        flip = 100 * avg(metrics[t][c]["both_flip"] for t in tags for c in ids)
        out.append(f"| {tag} | " + " | ".join(vals + [f"{flip:.1f}"]) + " |")
    out += ["", "A negative contrast indicates stronger movement toward opposing new evidence after relevant E1 than after irrelevant E1. This comparison isolates prior *content relevance* within read-only histories, but it does not isolate the causal contribution of the *retraction instruction* from general opposing-evidence sensitivity. The reused 200 claims and post-G28A registration prevent a confirmatory claim.", ""]
    target = Path(args.out)
    target.parent.mkdir(exist_ok=True, parents=True)
    target.write_text("\n".join(out))
    print(target)


if __name__ == "__main__":
    main()
