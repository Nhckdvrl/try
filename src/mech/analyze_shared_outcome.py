"""Apply the frozen G13 representation and causal-transfer gates."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[2]; sys.path.insert(0,str(ROOT/"src"))
from mech.shared_outcome import LAYERS,bootstrap_mean  # noqa: E402


def paired_effects(data: dict, layer: int, axis_kind: str) -> tuple[list[float],dict[str,list[float]]]:
    base={(r["unit"],r["outcome"]):r["value"] for r in data["baseline"] if r["value"] is not None}
    patch={(r["unit"],r["target"]):r["value"] for r in data["patches"]
           if r["layer"]==layer and r["axis_kind"]==axis_kind and r["value"] is not None}
    units=sorted({u for u,o in base if o=="yes"}&{u for u,o in base if o=="no"}
                 &{u for u,o in patch if o=="yes"}&{u for u,o in patch if o=="no"})
    up=[patch[(u,"no")]-base[(u,"no")] for u in units]
    down=[base[(u,"yes")]-patch[(u,"yes")] for u in units]
    return [0.5*(a+b) for a,b in zip(up,down)],{"no_to_yes":up,"yes_to_no":down}


def analyze(data: dict) -> dict:
    base={(r["unit"],r["outcome"]):r["value"] for r in data["baseline"] if r["value"] is not None}
    yes={u:v for (u,o),v in base.items() if o=="yes"}; no={u:v for (u,o),v in base.items() if o=="no"}
    units=sorted(set(yes)&set(no)); bridge=bootstrap_mean([yes[u]-no[u] for u in units])
    parse={o:sum(r["value"] is not None for r in data["baseline"] if r["outcome"]==o) for o in ("yes","no")}
    bridge_ok=min(parse.values())>=62 and bridge["mean"]>=10 and bridge["ci_low"]>0
    representation={int(k):v for k,v in data["representation"].items()}
    representation_ok=max(v["heldout_balanced_accuracy"] for v in representation.values())>=.75
    layers={}; meaningful=[]
    for layer in LAYERS:
        outcome,dirs=paired_effects(data,layer,"outcome"); orth,_=paired_effects(data,layer,"orthogonal")
        effect=bootstrap_mean(outcome); control=bootstrap_mean(orth)
        specificity=bootstrap_mean([a-b for a,b in zip(outcome,orth)])
        layers[layer]={"outcome_axis":effect,"orthogonal_axis":control,"axis_specificity":specificity,
                       "no_to_yes":bootstrap_mean(dirs["no_to_yes"]),
                       "yes_to_no":bootstrap_mean(dirs["yes_to_no"]),
                       "recovery_fraction":effect["mean"]/bridge["mean"] if bridge["mean"] else None}
        if effect["mean"]>=3 and effect["ci_low"]>0: meaningful.append(layer)
    adjacent=[(a,b) for a,b in zip(LAYERS,LAYERS[1:]) if a in meaningful and b in meaningful]
    peak=max(meaningful,key=lambda l:(layers[l]["outcome_axis"]["mean"],-l)) if meaningful else None
    window_ok=bool(adjacent)
    specificity_ok=peak is not None and layers[peak]["axis_specificity"]["ci_low"]>0
    verdict="shared-causal-outcome-variable" if bridge_ok and representation_ok and window_ok and specificity_ok else "not-established"
    return {"bridge":{"parse_counts":parse,"contrast":bridge,"passes":bridge_ok},
            "representation":{"per_layer":representation,"passes":representation_ok},
            "causal":{"per_layer":layers,"meaningful_layers":meaningful,"adjacent_windows":adjacent,
                      "peak_layer":peak,"window_passes":window_ok,"specificity_passes":specificity_ok},
            "verdict":verdict,
            "permitted_sentence":("Semantically unrelated future packets form a donor-general outcome variable whose one-dimensional causal interchange bidirectionally transfers their influence on reconstructed past judgments."
                if verdict=="shared-causal-outcome-variable" else
                "G13 does not establish a donor-general causal outcome variable; any decodability result is representational only.")}


def main() -> int:
    p=argparse.ArgumentParser(); p.add_argument("--raw",type=Path,default=ROOT/"results/mech/g13_shared_outcome.json")
    p.add_argument("--out",type=Path,default=ROOT/"results/mech/g13_shared_outcome_analysis.json"); a=p.parse_args()
    report={"preregistration":"PREREGISTRATION_G13_SHARED_OUTCOME.md",**analyze(json.loads(a.raw.read_text()))}
    a.out.parent.mkdir(parents=True,exist_ok=True); a.out.write_text(json.dumps(report,indent=2)+"\n")
    print(json.dumps({"bridge":report["bridge"]["passes"],"representation":report["representation"]["passes"],
                      "window":report["causal"]["window_passes"],"specificity":report["causal"]["specificity_passes"],
                      "peak":report["causal"]["peak_layer"],"verdict":report["verdict"]},indent=2))
    return 0
if __name__=="__main__": raise SystemExit(main())
