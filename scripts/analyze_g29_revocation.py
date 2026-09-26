"""G29 frozen paired analysis, including prompt and raw-row integrity checks."""

import argparse
import json
import random
import statistics as st
from collections import Counter
from pathlib import Path
from run_g29_revocation import BINARY_TASK, RATING_TASK, digest, messages

ROOT = Path(__file__).resolve().parents[1]
TAGS = ("mistral-small-24b", "qwen3-8b", "gemma3-12b")


def read(path):
    return [json.loads(s) for s in path.read_text().splitlines() if s]


def ci(values, draws):
    point = st.mean(values)
    boots = sorted(st.mean(values[i] for i in draw) for draw in draws)
    return f"{point:.3f} [{boots[int(.025*len(boots))]:.3f}, {boots[int(.975*len(boots))]:.3f}]"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--tags", nargs="+", default=TAGS)
    ap.add_argument("--out", default=str(ROOT / "results/g29/g29_revocation_analysis_v1.md"))
    args = ap.parse_args()
    pairs = read(ROOT / "data/items/g29_selected_v1.jsonl")
    ids = [p["id"] for p in pairs]
    assert len(ids) == len(set(ids))
    table, qualities = {}, {}
    for tag in args.tags:
        raw = read(ROOT / f"results/raw/{tag}_g29_revocation_v1.jsonl")
        assert len(raw) == len(pairs)*2*4*2, (tag, len(raw))
        keyed = {(r["id"], r["final_role"], r["condition"], r["mode"]): r for r in raw}
        assert len(keyed) == len(raw)
        for p in pairs:
            for role, e2, e1 in (("support", p["evidence_s"], p["evidence_r"]),
                                 ("refute", p["evidence_r"], p["evidence_s"])):
                for cond in ("R", "N", "A", "D"):
                    for mode in ("binary", "rating"):
                        r = keyed[(p["id"], role, cond, mode)]
                        msg = r["messages"]
                        assert msg == messages(p["claim"], e1, e2, cond,
                                               BINARY_TASK if mode == "binary" else RATING_TASK)
                        assert r["prompt_sha256"] == digest(msg)
                        if mode == "binary":
                            assert r["choice"] in ("TRUE", "FALSE"), (tag, p["id"], role, cond, r["raw"])
                        else:
                            assert r["value"] is not None and r["mass"] >= .5
                            # Keep the full sample, including any reference-
                            # arm rationale cap; report caps below.
        table[tag] = keyed
        qualities[tag] = Counter({
            "binary_unparsed": sum(r["mode"] == "binary" and r["choice"] is None for r in raw),
            "rating_unparsed": sum(r["mode"] == "rating" and r["value"] is None for r in raw),
            "low_mass": sum(r["mode"] == "rating" and r["mass"] < .5 for r in raw),
            "reason_caps": sum(r["mode"] == "rating" and r["reason_truncated"] for r in raw),
        })

    rng = random.Random("g29_revocation_bootstrap_v1")
    draws = [[rng.randrange(len(ids)) for _ in ids] for _ in range(5000)]
    per = {}
    for tag in args.tags:
        per[tag] = {}
        d = table[tag]
        for pid in ids:
            vals = {}
            for role in ("support", "refute"):
                sign = -1 if role == "support" else 1
                row = lambda cond, mode: d[(pid, role, cond, mode)]
                vr, vn = row("R", "rating")["value"], row("N", "rating")["value"]
                br, bn = int(row("R", "binary")["choice"] == "TRUE"), int(row("N", "binary")["choice"] == "TRUE")
                vals[role] = dict(
                    T_rating=sign*(vr-vn), T_binary=sign*(br-bn),
                    abs_rating=abs(vr-vn), disagree=int(br != bn),
                    R_true=br, N_true=bn,
                    R_e2=int(br == int(role == "support")),
                    N_e2=int(bn == int(role == "support")),
                    R_score=vr, N_score=vn,
                    A_score=row("A", "rating")["value"],
                    D_score=row("D", "rating")["value"],
                    A_e2=int((row("A", "binary")["choice"] == "TRUE") == (role == "support")),
                    D_e2=int((row("D", "binary")["choice"] == "TRUE") == (role == "support")),
                )
            per[tag][pid] = vals

    def summary(metric, tags, role=None):
        def one(pid):
            return st.mean(per[t][pid][r][metric] for t in tags
                           for r in ((role,) if role else ("support", "refute")))
        vals = [one(pid) for pid in ids]
        return ci(vals, draws)

    lines = ["# G29 revocation status vs prior contradictory exposure", "",
             f"Fresh material: {len(ids)} audited pairs, both E2 directions. "
             "Paired claim-cluster bootstrap (5,000 draws); interval is over claims, models fixed. "
             "Binary contrasts use proportions; scores are 0–100. Registration predates all G29 outputs.",
             "", "## Raw integrity", "", "| Model | Rows | Binary unparsed | Rating unparsed | Rating mass<.5 | Rationale caps |",
             "|---|---:|---:|---:|---:|---:|"]
    for tag in args.tags:
        q=qualities[tag]
        lines.append(f"| {tag} | {len(ids)*16} | {q['binary_unparsed']} | {q['rating_unparsed']} | {q['low_mass']} | {q['reason_caps']} |")
    lines += ["", "## Primary paired R−N contrast", "",
              "`T` is aligned with old E1; negative means stronger uptake of opposite E2 in the revoked history.", "",
              "| Models | E2 | Signed binary T | Binary disagreement | R E2 choice rate | N E2 choice rate | Signed rating T | Mean absolute rating difference |",
              "|---|---|---:|---:|---:|---:|---:|---:|"]
    groups = [("pooled", args.tags)] + [(tag,[tag]) for tag in args.tags]
    for label, tags in groups:
        for role in (None,"support","refute"):
            lines.append(f"| {label} | {role or 'both'} | {summary('T_binary',tags,role)} | "
                         f"{summary('disagree',tags,role)} | {summary('R_e2',tags,role)} | "
                         f"{summary('N_e2',tags,role)} | {summary('T_rating',tags,role)} | "
                         f"{summary('abs_rating',tags,role)} |")
    lines += ["", "## Reference conditions", "",
              "| Models | Condition | E2-aligned direct choice rate | Rating E2 separation |",
              "|---|---|---:|---:|"]
    for label,tags in groups:
        for cond in ("R","N","A","D"):
            rates = [st.mean(per[t][pid][r][f"{cond}_e2"] for t in tags for r in ("support","refute")) for pid in ids]
            seps = [st.mean(per[t][pid]["support"][f"{cond}_score"]-per[t][pid]["refute"][f"{cond}_score"] for t in tags) for pid in ids]
            lines.append(f"| {label} | {cond} | {ci(rates,draws)} | {ci(seps,draws)} |")
    lines += ["", "## Interpretation boundary", "",
              "Mistral's active-conflict reference has two 110-token rationale caps; "
              "the registered R−N comparison has no capped rows. No rows are dropped.\n\n"
              "R and N differ in admissibility history and the words that convey it. "
              "Any R−N effect is behavioral evidence for status/history sensitivity after identical E1 exposure; "
              "it does not localize an internal state or show a universal law. "
              "The A reference intentionally has a different final admissible set. "
              "All materials were fixed before model inference; the G29 direction was motivated by observed G28 outcomes.", ""]
    out=Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text("\n".join(lines))
    print(out)


if __name__ == "__main__":
    main()
