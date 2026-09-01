"""Run G15 fresh-assignment confirmation of the answer-position decision axis."""
from __future__ import annotations
import argparse,json,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2];sys.path.insert(0,str(ROOT/"src"))
import numpy as np  # noqa:E402
import torch  # noqa:E402
from adapters.btf3_donor_outcome import assignment_digest,build_donor_pairs  # noqa:E402
from information_set_schema import file_sha256,load_jsonl  # noqa:E402
from mech.shared_outcome import LAYERS,balanced_accuracy,frozen_split,learn_axis,orthogonal_axis,split_digest  # noqa:E402
from mech.run_shared_outcome import build_entries,decoder_layers,generate_batch,_checkpoint,_raw_records  # noqa:E402
from mech.run_decision_outcome import capture_answer_states,generate_answer_patch  # noqa:E402

PAIRING_SEED=20260902


def main():
    p=argparse.ArgumentParser();p.add_argument("--artifact",type=Path,default=ROOT/"data/external/review/btf3_temporal_large_replication_v1.jsonl")
    p.add_argument("--model",required=True);p.add_argument("--model-id",required=True);p.add_argument("--model-revision",required=True);p.add_argument("--tag",required=True)
    p.add_argument("--out",type=Path,default=ROOT/"results/mech/g15_decision_confirmation.json");p.add_argument("--states",type=Path,default=ROOT/"results/mech/g15_decision_confirmation_states.npz")
    p.add_argument("--batch-size",type=int,default=2);p.add_argument("--dry-run",action="store_true");a=p.parse_args()
    from transformers import AutoModelForImageTextToText,AutoTokenizer
    tok=AutoTokenizer.from_pretrained(a.model,local_files_only=True);items=load_jsonl(a.artifact);pairs=build_donor_pairs(items,seed=PAIRING_SEED);split=frozen_split(pairs);entries=build_entries(tok,pairs)
    audit={"pairing_seed":PAIRING_SEED,"units":len(pairs),"entries":len(entries),"split_counts":{k:len(v) for k,v in split.items()},"split_sha256":split_digest(pairs,split),"assignment_sha256":assignment_digest(pairs),"longest_tokens":max(len(e["ids"]) for e in entries)}
    if a.dry_run:print(json.dumps(audit,indent=2));return 0
    model=AutoModelForImageTextToText.from_pretrained(a.model,local_files_only=True,dtype=torch.bfloat16,device_map="cuda",attn_implementation="eager").eval();layers=decoder_layers(model);pad=tok.pad_token_id if tok.pad_token_id is not None else tok.eos_token_id
    if a.states.exists():states={k:v for k,v in np.load(a.states).items()};print(f"loaded {len(states)} cached states",flush=True)
    else:
        states=capture_answer_states(model,layers,entries,a.batch_size,pad);a.states.parent.mkdir(parents=True,exist_ok=True);np.savez_compressed(a.states,**states)
    by={(e["index"],e["outcome"]):e for e in entries};train=[by[i,o] for i in split["train"] for o in ("yes","no")];test=[by[i,o] for i in split["test"] for o in ("yes","no")]
    result=_raw_records(a.out);result["metadata"]={"preregistration":"PREREGISTRATION_G15_DECISION_CONFIRMATION.md","git_commit":subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip(),"artifact_sha256":file_sha256(a.artifact),"model_id":a.model_id,"model_revision":a.model_revision,"model_tag":a.tag,"layers":list(LAYERS),"site":"final_prompt_token","audit":audit}
    axes={}
    for l in LAYERS:
        y=np.stack([states[f"{e['unit']}|yes|{l}"] for e in train if e["outcome"]=="yes"]);n=np.stack([states[f"{e['unit']}|no|{l}"] for e in train if e["outcome"]=="no"]);v,ym,nm=learn_axis(y,n);axes[l,"outcome"]=v;axes[l,"orthogonal"]=orthogonal_axis(v,layer=l)
        ty=np.stack([states[f"{e['unit']}|yes|{l}"] for e in test if e["outcome"]=="yes"]);tn=np.stack([states[f"{e['unit']}|no|{l}"] for e in test if e["outcome"]=="no"]);gaps=((ty-tn)@v).astype(float).tolist()
        result["representation"][str(l)]={"train_yes_projection_mean":ym,"train_no_projection_mean":nm,"heldout_balanced_accuracy":balanced_accuracy(ty,tn,v,ym,nm),"heldout_pair_projection_gaps":gaps,"heldout_pair_ordering_accuracy":sum(g>0 for g in gaps)/len(gaps)}
    _checkpoint(a.out,result)
    existing_base={r["unit"]+"|"+r["outcome"] for r in result["baseline"]};missing=[e for e in test if e["unit"]+"|"+e["outcome"] not in existing_base]
    if missing:
        for e,(raw,value) in zip(missing,generate_batch(model,tok,layers,missing,batch_size=a.batch_size),strict=True):result["baseline"].append({"unit":e["unit"],"outcome":e["outcome"],"raw":raw,"value":value,"prompt_sha256":e["prompt_sha256"]})
        _checkpoint(a.out,result)
    print("baseline complete",flush=True);existing={(r["unit"],r["target"],r["layer"],r["axis_kind"]) for r in result["patches"]}
    for l in LAYERS:
        for kind in ("outcome","orthogonal"):
            axis=axes[l,kind]
            for target,source in (("no","yes"),("yes","no")):
                group=[by[i,target] for i in split["test"] if (pairs[i]["independent_unit_id"],target,l,kind) not in existing];ds=[float((states[f"{e['unit']}|{source}|{l}"]-states[f"{e['unit']}|{target}|{l}"])@axis) for e in group]
                gen=generate_answer_patch(model,tok,layers,group,batch_size=a.batch_size,layer=l,axis=axis,deltas=ds)
                for e,d,(raw,value) in zip(group,ds,gen,strict=True):result["patches"].append({"unit":e["unit"],"layer":l,"axis_kind":kind,"target":target,"source":source,"projection_delta":d,"raw":raw,"value":value})
                _checkpoint(a.out,result)
        print(f"layer {l} complete",flush=True)
    print(json.dumps({"out":str(a.out),"states":str(a.states),"records":len(result["patches"])}));return 0
if __name__=="__main__":raise SystemExit(main())
