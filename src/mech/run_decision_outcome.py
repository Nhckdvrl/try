"""Run G14 answer-position outcome-axis causal interchange."""
from __future__ import annotations
import argparse,json,subprocess,sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]; sys.path.insert(0,str(ROOT/"src"))
import numpy as np  # noqa: E402
import torch  # noqa: E402
from adapters.btf3_donor_outcome import assignment_digest,build_donor_pairs  # noqa: E402
from information_set_schema import file_sha256,load_jsonl  # noqa: E402
from mech.shared_outcome import LAYERS,balanced_accuracy,frozen_split,learn_axis,orthogonal_axis,split_digest  # noqa: E402
from mech.run_shared_outcome import build_entries,decoder_layers,pad_batch,_checkpoint,_raw_records  # noqa: E402
from run_information_set import parse_probability  # noqa: E402


@torch.inference_mode()
def capture_answer_states(model,layers,entries,batch_size,pad_id):
    store={}; device=next(model.parameters()).device; text_model=model.model.language_model
    for start in range(0,len(entries),batch_size):
        batch=entries[start:start+batch_size]; ids,mask,_=pad_batch(batch,pad_id,device,left=False)
        captured={}; handles=[]
        lengths=[len(e["ids"]) for e in batch]
        for layer in LAYERS:
            def hook(module,inputs,output,layer=layer):
                hidden=output[0] if isinstance(output,tuple) else output
                captured[layer]=torch.stack([hidden[b,n-1].float().detach().cpu() for b,n in enumerate(lengths)])
            handles.append(layers[layer].register_forward_hook(hook))
        text_model(input_ids=ids,attention_mask=mask,use_cache=False,return_dict=True)
        for h in handles:h.remove()
        for b,e in enumerate(batch):
            for layer in LAYERS:store[f"{e['unit']}|{e['outcome']}|{layer}"]=captured[layer][b].numpy()
        if min(start+batch_size,len(entries))%32==0 or start+batch_size>=len(entries):
            print(f"capture {min(start+batch_size,len(entries))}/{len(entries)}",flush=True)
    return store


@torch.inference_mode()
def generate_answer_patch(model,tokenizer,layers,entries,*,batch_size,layer,axis,deltas):
    device=next(model.parameters()).device; pad_id=tokenizer.pad_token_id if tokenizer.pad_token_id is not None else tokenizer.eos_token_id
    outputs=[]
    for start in range(0,len(entries),batch_size):
        batch=entries[start:start+batch_size]; ids,mask,_=pad_batch(batch,pad_id,device,left=True)
        vector=torch.tensor(axis,device=device,dtype=next(model.parameters()).dtype)
        ds=torch.tensor(deltas[start:start+len(batch)],device=device,dtype=vector.dtype)
        def hook(module,inputs,output):
            hidden=output[0] if isinstance(output,tuple) else output
            if hidden.shape[1]>1:
                hidden=hidden.clone(); hidden[:,-1,:]+=ds[:,None]*vector[None,:]
            return (hidden,)+output[1:] if isinstance(output,tuple) else hidden
        handle=layers[layer].register_forward_hook(hook)
        generated=model.generate(input_ids=ids,attention_mask=mask,do_sample=False,max_new_tokens=8,
                                 pad_token_id=pad_id,eos_token_id=tokenizer.eos_token_id,use_cache=True)
        handle.remove(); continuation=generated[:,ids.shape[1]:]
        for row in continuation:
            raw=tokenizer.decode(row,skip_special_tokens=True); outputs.append((raw,parse_probability(raw)))
    return outputs


def main():
    p=argparse.ArgumentParser(); p.add_argument("--artifact",type=Path,default=ROOT/"data/external/review/btf3_temporal_large_replication_v1.jsonl")
    p.add_argument("--model",required=True);p.add_argument("--model-id",required=True);p.add_argument("--model-revision",required=True);p.add_argument("--tag",required=True)
    p.add_argument("--g13",type=Path,default=ROOT/"results/mech/g13_shared_outcome.json")
    p.add_argument("--out",type=Path,default=ROOT/"results/mech/g14_decision_outcome.json")
    p.add_argument("--states",type=Path,default=ROOT/"results/mech/g14_decision_outcome_states.npz")
    p.add_argument("--batch-size",type=int,default=2);p.add_argument("--dry-run",action="store_true");a=p.parse_args()
    from transformers import AutoModelForImageTextToText,AutoTokenizer
    tok=AutoTokenizer.from_pretrained(a.model,local_files_only=True);items=load_jsonl(a.artifact);pairs=build_donor_pairs(items);split=frozen_split(pairs);entries=build_entries(tok,pairs)
    g13=json.loads(a.g13.read_text());base=g13["baseline"]
    audit={"units":len(pairs),"entries":len(entries),"split_counts":{k:len(v) for k,v in split.items()},"split_sha256":split_digest(pairs,split),
           "assignment_sha256":assignment_digest(pairs),"reused_baselines":len(base),"baseline_cells":sorted([r["outcome"] for r in base]).count("yes")}
    if len(base)!=128 or sum(r["outcome"]=="yes" for r in base)!=64 or sum(r["outcome"]=="no" for r in base)!=64:raise ValueError("G13 baseline is not the frozen 64x2 bridge")
    expected={pairs[i]["independent_unit_id"] for i in split["test"]}
    if {r["unit"] for r in base}!=expected:raise ValueError("G13 baseline units differ from G14 test split")
    if a.dry_run:print(json.dumps(audit,indent=2));return 0
    model=AutoModelForImageTextToText.from_pretrained(a.model,local_files_only=True,dtype=torch.bfloat16,device_map="cuda",attn_implementation="eager").eval();layers=decoder_layers(model)
    pad=tok.pad_token_id if tok.pad_token_id is not None else tok.eos_token_id
    if a.states.exists():states={k:v for k,v in np.load(a.states).items()};print(f"loaded {len(states)} cached states",flush=True)
    else:
        states=capture_answer_states(model,layers,entries,a.batch_size,pad);a.states.parent.mkdir(parents=True,exist_ok=True);np.savez_compressed(a.states,**states)
    by={(e["index"],e["outcome"]):e for e in entries};train=[by[i,o] for i in split["train"] for o in ("yes","no")];test=[by[i,o] for i in split["test"] for o in ("yes","no")]
    result=_raw_records(a.out);result["baseline"]=base;result["metadata"]={"preregistration":"PREREGISTRATION_G14_DECISION_STATE.md","git_commit":subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip(),"artifact_sha256":file_sha256(a.artifact),"model_id":a.model_id,"model_revision":a.model_revision,"model_tag":a.tag,"layers":list(LAYERS),"site":"final_prompt_token","audit":audit}
    axes={}
    for l in LAYERS:
        y=np.stack([states[f"{e['unit']}|yes|{l}"] for e in train if e["outcome"]=="yes"]);n=np.stack([states[f"{e['unit']}|no|{l}"] for e in train if e["outcome"]=="no"])
        v,ym,nm=learn_axis(y,n);axes[l,"outcome"]=v;axes[l,"orthogonal"]=orthogonal_axis(v,layer=l)
        ty=np.stack([states[f"{e['unit']}|yes|{l}"] for e in test if e["outcome"]=="yes"]);tn=np.stack([states[f"{e['unit']}|no|{l}"] for e in test if e["outcome"]=="no"])
        result["representation"][str(l)]={"train_yes_projection_mean":ym,"train_no_projection_mean":nm,"heldout_balanced_accuracy":balanced_accuracy(ty,tn,v,ym,nm)}
    _checkpoint(a.out,result);existing={(r["unit"],r["target"],r["layer"],r["axis_kind"]) for r in result["patches"]}
    for l in LAYERS:
        for kind in ("outcome","orthogonal"):
            axis=axes[l,kind]
            for target,source in (("no","yes"),("yes","no")):
                group=[by[i,target] for i in split["test"] if (pairs[i]["independent_unit_id"],target,l,kind) not in existing]
                ds=[float((states[f"{e['unit']}|{source}|{l}"]-states[f"{e['unit']}|{target}|{l}"])@axis) for e in group]
                gen=generate_answer_patch(model,tok,layers,group,batch_size=a.batch_size,layer=l,axis=axis,deltas=ds)
                for e,d,(raw,value) in zip(group,ds,gen,strict=True):result["patches"].append({"unit":e["unit"],"layer":l,"axis_kind":kind,"target":target,"source":source,"projection_delta":d,"raw":raw,"value":value})
                _checkpoint(a.out,result)
        print(f"layer {l} complete",flush=True)
    print(json.dumps({"out":str(a.out),"states":str(a.states),"records":len(result["patches"])}));return 0
if __name__=="__main__":raise SystemExit(main())
