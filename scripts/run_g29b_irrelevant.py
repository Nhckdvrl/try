"""Run the matched never-admissible irrelevant-history G29B condition."""

import argparse
import json
import re
import sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path[:0]=[str(ROOT/"src"),str(ROOT/"scripts")]
from run_model import digit_expectation
from schema import ANSWER_CUE,SYSTEM
from run_g29_revocation import BINARY_TASK,RATING_TASK,digest,messages


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--model",required=True)
    ap.add_argument("--tag",required=True)
    ap.add_argument("--out",required=True)
    ap.add_argument("--gpu-frac",type=float,default=.85)
    args=ap.parse_args()
    pairs=[json.loads(s) for s in (ROOT/"data/items/g29_selected_v1.jsonl").read_text().splitlines() if s]
    controls={r["id"]:r for r in map(json.loads,(ROOT/"data/items/g29b_irrelevant_selected_v1.jsonl").open())}
    assert len(pairs)==len(controls)==80
    from transformers import AutoTokenizer
    from vllm import LLM,SamplingParams
    tok=AutoTokenizer.from_pretrained(args.model)

    def chat_ids(msg):
        full=[{"role":"system","content":SYSTEM}]+msg
        kw=dict(tokenize=True,add_generation_prompt=True)
        try: enc=tok.apply_chat_template(full,enable_thinking=False,**kw)
        except TypeError: enc=tok.apply_chat_template(full,**kw)
        ids=enc["input_ids"] if hasattr(enc,"keys") else enc
        return list(ids[0]) if ids and isinstance(ids[0],(list,tuple)) else list(ids)

    rows=[]
    for p in pairs:
        e1=controls[p["id"]]["irrelevant_e1"]
        for role,e2 in (("support",p["evidence_s"]),("refute",p["evidence_r"])):
            for mode,task in (("binary",BINARY_TASK),("rating",RATING_TASK)):
                msg=messages(p["claim"],e1,e2,"N",task)
                rows.append(dict(id=p["id"],model_tag=args.tag,final_role=role,
                                 condition="I",mode=mode,messages=msg,
                                 prompt_sha256=digest(msg),ids=chat_ids(msg)))
    llm=LLM(model=args.model,tensor_parallel_size=1,
            gpu_memory_utilization=args.gpu_frac,max_model_len=4096,
            dtype="bfloat16",max_logprobs=40,disable_log_stats=True,enforce_eager=True)
    binary=[r for r in rows if r["mode"]=="binary"]
    rating=[r for r in rows if r["mode"]=="rating"]
    o=llm.generate([{"prompt_token_ids":r["ids"]} for r in binary],
                   SamplingParams(temperature=0,max_tokens=16),use_tqdm=False)
    for r,x in zip(binary,o):
        r["raw"]=x.outputs[0].text
        m=re.search(r"ANSWER\s*:\s*(TRUE|FALSE)\b",r["raw"],re.I)
        r["choice"]=m.group(1).upper() if m else None
        r["finish_reason"]=x.outputs[0].finish_reason
        del r["ids"]
    o=llm.generate([{"prompt_token_ids":r["ids"]} for r in rating],
                   SamplingParams(temperature=0,max_tokens=110,stop=[ANSWER_CUE]),use_tqdm=False)
    for r,x in zip(rating,o):
        r["reasoning"]=x.outputs[0].text
        r["reason_truncated"]=x.outputs[0].finish_reason!="stop"
        cue=r["reasoning"].rstrip()+"\n"+ANSWER_CUE+" "
        r["ids2"]=r["ids"]+tok(cue,add_special_tokens=False)["input_ids"]
    o=llm.generate([{"prompt_token_ids":r["ids2"]} for r in rating],
                   SamplingParams(temperature=0,max_tokens=1,logprobs=40),use_tqdm=False)
    for r,x in zip(rating,o):
        r["raw"]=x.outputs[0].text
        r["value"],r["mass"]=digit_expectation(x)
        del r["ids"],r["ids2"]
    out=Path(args.out)
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text("".join(json.dumps(r,ensure_ascii=False)+"\n" for r in rows))
    print(f"wrote {len(rows)} rows; binary unparsed={sum(r['choice'] is None for r in binary)}; "
          f"rating unparsed={sum(r['value'] is None for r in rating)}; "
          f"mass<.5={sum(r['mass']<.5 for r in rating)}; "
          f"rationale caps={sum(r['reason_truncated'] for r in rating)}")


if __name__=="__main__":main()
