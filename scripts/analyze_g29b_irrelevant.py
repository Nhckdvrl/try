"""G29B matched excluded-contradiction versus excluded-irrelevant analysis."""

import argparse
import json
import random
import statistics as st
from collections import Counter
from pathlib import Path

from run_g29_revocation import BINARY_TASK,RATING_TASK,digest,messages

ROOT=Path(__file__).resolve().parents[1]
TAGS=("mistral-small-24b","qwen3-8b","gemma3-12b")


def read(path):
    return [json.loads(s) for s in path.read_text().splitlines() if s]


def interval(vals,draws):
    point=st.mean(vals)
    boots=sorted(st.mean(vals[j] for j in draw) for draw in draws)
    return f"{point:.3f} [{boots[int(.025*len(boots))]:.3f},{boots[int(.975*len(boots))]:.3f}]"


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--out",default=str(ROOT/"results/g29/g29b_excluded_content_analysis_v1.md"))
    args=ap.parse_args()
    pairs=read(ROOT/"data/items/g29_selected_v1.jsonl")
    ids=[p["id"] for p in pairs]
    controls={r["id"]:r for r in read(ROOT/"data/items/g29b_irrelevant_selected_v1.jsonl")}
    assert len(pairs)==len(controls)==80
    data={}
    quality={}
    for tag in TAGS:
        orig=read(ROOT/f"results/raw/{tag}_g29_revocation_v1.jsonl")
        newer=read(ROOT/f"results/raw/{tag}_g29b_irrelevant_v1.jsonl")
        assert len(orig)==1280 and len(newer)==320
        old={(r["id"],r["final_role"],r["condition"],r["mode"]):r for r in orig}
        fresh={(r["id"],r["final_role"],r["mode"]):r for r in newer}
        assert len(old)==1280 and len(fresh)==320
        for p in pairs:
            e1=controls[p["id"]]["irrelevant_e1"]
            for role,e2 in (("support",p["evidence_s"]),("refute",p["evidence_r"])):
                for mode,task in (("binary",BINARY_TASK),("rating",RATING_TASK)):
                    n=old[(p["id"],role,"N",mode)]
                    i=fresh[(p["id"],role,mode)]
                    expected=messages(p["claim"],e1,e2,"N",task)
                    assert i["condition"]=="I" and i["model_tag"]==tag
                    assert i["messages"]==expected and i["prompt_sha256"]==digest(expected)
                    assert n["messages"][0]["content"].replace(
                        p["evidence_r"] if role=="support" else p["evidence_s"],e1,1)==i["messages"][0]["content"]
                    assert n["messages"][1:]==i["messages"][1:]
                    if mode=="binary": assert i["choice"] in ("TRUE","FALSE")
                    else: assert i["value"] is not None and i["mass"]>=.5
        data[tag]=(old,fresh)
        quality[tag]=Counter({"unparsed_binary":sum(r["mode"]=="binary" and r["choice"] is None for r in newer),
                              "unparsed_rating":sum(r["mode"]=="rating" and r["value"] is None for r in newer),
                              "low_mass":sum(r["mode"]=="rating" and r["mass"]<.5 for r in newer),
                              "caps":sum(r["mode"]=="rating" and r["reason_truncated"] for r in newer)})
    rng=random.Random("g29b_bootstrap_v1")
    draws=[[rng.randrange(80) for _ in ids] for _ in range(5000)]
    metrics={}
    for tag,(old,fresh) in data.items():
        metrics[tag]={}
        for pid in ids:
            metrics[tag][pid]={}
            for role in ("support","refute"):
                sign=-1 if role=="support" else 1
                def get(cond,mode):
                    return fresh[(pid,role,mode)] if cond=="I" else old[(pid,role,cond,mode)]
                x={}
                for c in ("I","N","R"):
                    x[c+"_true"]=int(get(c,"binary")["choice"]=="TRUE")
                    x[c+"_score"]=get(c,"rating")["value"]
                    x[c+"_e2"]=int(x[c+"_true"]==int(role=="support"))
                for a,b in (("N","I"),("R","I"),("R","N")):
                    x[a+b+"_T_binary"]=sign*(x[a+"_true"]-x[b+"_true"])
                    x[a+b+"_T_rating"]=sign*(x[a+"_score"]-x[b+"_score"])
                    x[a+b+"_disagree"]=int(x[a+"_true"]!=x[b+"_true"])
                    x[a+b+"_abs_rating"]=abs(x[a+"_score"]-x[b+"_score"])
                metrics[tag][pid][role]=x

    def summ(k,tags,role=None):
        vals=[st.mean(metrics[t][pid][r][k] for t in tags
                      for r in ((role,) if role else ("support","refute"))) for pid in ids]
        return interval(vals,draws)

    lines=["# G29B: excluded contradictory content vs excluded irrelevant content", "",
           "Exploratory follow-up registered after G29 R−N results. Same 80 frozen audited pairs, three models, both E2 directions. "
           "I replaces N's old E1 sentence with a separately audited natural irrelevant sentence; turn structure, status words, and final E2 are byte-for-byte matched. "
           "Paired claim bootstrap, 5,000 draws; scores 0–100; model set fixed.","",
           "## Integrity","","| Model | New I rows | Binary unparsed | Rating unparsed | Mass<.5 | Rationale caps |",
           "|---|---:|---:|---:|---:|---:|"]
    for tag in TAGS:
        q=quality[tag]
        lines.append(f"| {tag} | 320 | {q['unparsed_binary']} | {q['unparsed_rating']} | {q['low_mass']} | {q['caps']} |")
    lines += ["","## Paired contrasts","",
              "Signed T is aligned to old relevant E1; negative means stronger uptake of opposite E2 in the first condition.","",
              "| Models | E2 | Contrast | Signed binary T | Binary disagreement | Signed rating T | Absolute rating difference |",
              "|---|---|---|---:|---:|---:|---:|"]
    groups=[("pooled",TAGS)]+[(tag,(tag,)) for tag in TAGS]
    for label,tags in groups:
        for role in (None,"support","refute"):
            for a,b in (("N","I"),("R","I"),("R","N")):
                key=a+b
                lines.append(f"| {label} | {role or 'both'} | {a}−{b} | "
                             f"{summ(key+'_T_binary',tags,role)} | {summ(key+'_disagree',tags,role)} | "
                             f"{summ(key+'_T_rating',tags,role)} | {summ(key+'_abs_rating',tags,role)} |")
    lines += ["","## Condition levels","",
              "| Models | Condition | E2-aligned direct-choice rate | E2 rating separation |",
              "|---|---|---:|---:|"]
    for label,tags in groups:
        for c in ("I","N","R"):
            e2=[st.mean(metrics[t][pid][r][c+"_e2"] for t in tags for r in ("support","refute")) for pid in ids]
            sep=[st.mean(metrics[t][pid]["support"][c+"_score"]-metrics[t][pid]["refute"][c+"_score"] for t in tags) for pid in ids]
            lines.append(f"| {label} | {c} | {interval(e2,draws)} | {interval(sep,draws)} |")
    lines += ["","## Interpretation boundary","",
              "N−I isolates *content relevance* within a never-admissible history, not a hidden-state mechanism. "
              "The irrelevant sentence is different lexical content by design; all 80 were selected before G29B outputs. "
              "R−N was completed in G29, and this extra control was motivated by seeing its results.",""]
    path=Path(args.out)
    path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text("\n".join(lines))
    print(path)


if __name__=="__main__":main()
