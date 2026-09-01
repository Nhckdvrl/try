"""Apply G15's frozen paired representation and causal confirmation gates."""
from __future__ import annotations
import argparse,json,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/"src"))
from mech.analyze_shared_outcome import analyze  # noqa:E402
from mech.shared_outcome import bootstrap_mean  # noqa:E402

def main():
    p=argparse.ArgumentParser();p.add_argument("--raw",type=Path,default=ROOT/"results/mech/g15_decision_confirmation.json");p.add_argument("--out",type=Path,default=ROOT/"results/mech/g15_decision_confirmation_analysis.json");a=p.parse_args();data=json.loads(a.raw.read_text());report=analyze(data)
    paired={}
    for l,v in data["representation"].items():
        ci=bootstrap_mean(v["heldout_pair_projection_gaps"]);ordering=v["heldout_pair_ordering_accuracy"]
        paired[l]={"ordering_accuracy":ordering,"projection_gap":ci,"passes":ordering>=.75 and ci["ci_low"]>0}
    representation_ok=any(v["passes"] for v in paired.values());late={29,35,41,47};overlap=any(a in late or b in late for a,b in report["causal"]["adjacent_windows"])
    confirmed=report["bridge"]["passes"] and representation_ok and report["causal"]["window_passes"] and overlap and report["causal"]["specificity_passes"]
    report["representation"]={"per_layer":paired,"passes":representation_ok};report["causal"]["late_window_overlap"]=overlap;report["verdict"]="confirmed-recipient-conditioned-decision-state" if confirmed else "not-confirmed"
    report["permitted_sentence"]=("Across a fresh assignment of unrelated future evidence, outcome information is converted into a recipient-conditioned late decision coordinate whose causal interchange bidirectionally transfers its influence on reconstructed past judgments." if confirmed else "The fresh-assignment experiment does not confirm the recipient-conditioned causal decision-state account.")
    out={"preregistration":"PREREGISTRATION_G15_DECISION_CONFIRMATION.md",**report};a.out.parent.mkdir(parents=True,exist_ok=True);a.out.write_text(json.dumps(out,indent=2)+"\n");print(json.dumps({"bridge":out["bridge"]["passes"],"representation":out["representation"]["passes"],"window":out["causal"]["window_passes"],"late_overlap":overlap,"specificity":out["causal"]["specificity_passes"],"peak":out["causal"]["peak_layer"],"verdict":out["verdict"]},indent=2));return 0
if __name__=="__main__":raise SystemExit(main())
