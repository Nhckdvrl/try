"""Analyze G12's paired donor-outcome causal contrast."""
from __future__ import annotations
import argparse,json
from pathlib import Path
try:
    from .analyze_exante_anchor import bootstrap_mean
    from .run_information_set import parse_probability
except ImportError:
    from analyze_exante_anchor import bootstrap_mean
    from run_information_set import parse_probability

PANEL=("qwen35-9b","gemma3-12b","mistral-small-24b")

def load(path):
    rows=[json.loads(x) for x in path.read_text().splitlines() if x]
    for row in rows:
        if row.get("record_type") == "decision" and row.get("value") is None:
            recovered=parse_probability(row.get("raw", ""))
            if recovered is not None:
                row["value"]=recovered; row["value_reparsed"]=True
    return rows[0],[r for r in rows[1:]]

def analyze(path):
    meta,rows=load(path); dec=[r for r in rows if r["record_type"]=="decision"]
    probes=[r for r in rows if r["record_type"]=="boundary_probe"]
    parse={o:sum(r["value"] is not None for r in dec if r["donor_outcome"]==o)/256 for o in ("YES","NO")}
    boundary={o:sum(bool(r.get("correct")) for r in probes if r["donor_outcome"]==o)/256 for o in ("YES","NO")}
    vals={o:{r["independent_unit_id"]:r for r in dec if r["donor_outcome"]==o and r["value"] is not None} for o in ("YES","NO")}
    units=sorted(set(vals["YES"])&set(vals["NO"]))
    c=[vals["YES"][u]["value"]-vals["NO"][u]["value"] for u in units]
    aligned=[vals["YES"][u]["recipient_direction"]*d for u,d in zip(units,c)]
    effect=bootstrap_mean(c); validity=bootstrap_mean(aligned)
    qualified=all(parse[o]>=248/256 and boundary[o]>=224/256 for o in ("YES","NO"))
    validity_ok=validity["ci_low"]>=-5 and validity["ci_high"]<=5
    if qualified and validity_ok and effect["mean"]>=5 and effect["ci_low"]>0: verdict="causal-outcome-entrainment"
    elif qualified and validity_ok and effect["ci_low"]>=-5 and effect["ci_high"]<=5: verdict="practically-null"
    else: verdict="indeterminate"
    return {"model_tag":meta["model_tag"],"assignment_sha256":meta["assignment_sha256"],"units":len(units),
            "reparsed_values":sum(bool(r.get("value_reparsed")) for r in dec),
            "parse_rate":parse,"boundary_accuracy":boundary,"qualified":qualified,"causal_contrast":effect,
            "absolute_pair_difference":bootstrap_mean([abs(x) for x in c]),"recipient_aligned_validity":validity,
            "validity_ok":validity_ok,"verdict":verdict}

def main():
    p=argparse.ArgumentParser(); p.add_argument("--raw-dir",type=Path,default=Path("results/raw")); p.add_argument("--out",type=Path,default=Path("results/g12_donor_outcome_analysis.json")); a=p.parse_args()
    per={t:analyze(a.raw_dir/f"isr_{t}_g12_donor_outcome.jsonl") for t in PANEL if (a.raw_dir/f"isr_{t}_g12_donor_outcome.jsonl").exists()}
    counted=[m for m in per.values() if m["qualified"] and m["validity_ok"]]
    tally={v:sum(m["verdict"]==v for m in counted) for v in ("causal-outcome-entrainment","practically-null","indeterminate")}
    panel=next((v for v in ("causal-outcome-entrainment","practically-null") if tally[v]>=2),"indeterminate")
    sentence={"causal-outcome-entrainment":"The outcome supported by an irrelevant future evidence packet causally sets the direction of its influence on a reconstructed past judgment, even after explicit verdict sentences are removed.","practically-null":"Within recipient, changing the irrelevant donor outcome has no practically meaningful effect.","indeterminate":"The paired donor-outcome intervention is indeterminate."}[panel]
    report={"preregistration":"PREREGISTRATION_G12_DONOR_OUTCOME.md","per_model":per,"panel":{"tally":tally,"qualified_models":len(counted),"verdict":panel},"permitted_sentence":sentence}
    a.out.write_text(json.dumps(report,indent=2,ensure_ascii=False)+"\n"); print(json.dumps(report["panel"],indent=2)); print(sentence); return 0
if __name__=="__main__": raise SystemExit(main())
