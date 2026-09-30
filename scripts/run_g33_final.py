"""G33 frozen legal-ground identification and same-material no-E bridge.

No hidden-state claim. Binary constrained decisions avoid numerical ratings;
the normalized binary probability is a readout, not claimed calibration.
"""
import argparse
import fcntl
import socket
import hashlib
import json
import math
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ITEMS=ROOT/'data/items/g33_final/selected.jsonl'
QUERIES={
 'w1':{
  'D':'Judge the claim now using the currently admissible information.',
  'C':'Judge the claim as if the excluded note X had never been present. All currently admissible information remains available for this judgment.',
  'S':'Predict the answer of a fresh instance of this same model given the same task rule, claim, and currently admissible information, but never shown note X or its exclusion notice.'},
 'w2':{
  'D':'Give your current verdict based on the information you are permitted to use.',
  'C':'Give the verdict you would reach had you never encountered the excluded note X. Keep using every record that is still permitted.',
  'S':'What verdict would another fresh copy of you give under this task rule with this claim and all permitted information, without ever receiving X or any notice concerning X?'}}
CELLS=('B','FD','DC+','DC-','FC','CC+','CC-','FS','SC+','SC-','A+','A-')
# Cell names use a second C to denote content-present, not query C.
def messages(item, substrate, e_role, wording, cell):
    w=wording=='w1'
    rule=('Decide whether the claim is TRUE or FALSE using only records that are explicitly currently admissible. Every such record is allowed. Do not add background knowledge or assumptions. Treat these records as authoritative for this task.' if w else
          'Determine the truth of the claim from all and only the records currently permitted for this task. Permitted records are authoritative here; outside knowledge and unstated assumptions are not allowed.')
    if substrate=='no_e':
        rule=('Decide whether the claim is TRUE or FALSE using your background knowledge and any records explicitly currently admissible.' if w else
              'Determine the truth of the claim using what you already know together with any records currently permitted for this task.')
    parts=['TASK RULE\n'+rule,'CLAIM\n'+item['claim']]
    if substrate=='record': parts.append('RECORD E — CURRENTLY ADMISSIBLE\nSource topic: '+item['page']+'\n'+item['evidence_s' if e_role=='support' else 'evidence_r'])
    if cell!='B':
        x='[REDACTED]' if cell.startswith('F') else item['x_s' if cell.endswith('+') else 'x_r']
        status=('Note X is currently admissible. Use it along with all other admissible information.' if cell.startswith('A') else
                'Note X is excluded from the moment it is displayed. Its contents must not be used to decide the claim. All other currently admissible information remains admissible.')
        if not w:
            status=('X is a permitted record and may be used together with every other permitted record.' if cell.startswith('A') else
                    'X is not permitted, including at the moment you first see it. Do not base the verdict on X. This restriction does not withdraw any other permitted information.')
        parts+=['NOTE X\n'+x,'CURRENT STATUS OF X\n'+status]
    q='D' if cell=='B' or cell.startswith('A') else (cell[1] if cell.startswith('F') else cell[0])
    parts.append('QUESTION\n'+QUERIES[wording][q]+' Reply with exactly one word: TRUE or FALSE.')
    return [{'role':'system','content':'Follow the task rule and answer only TRUE or FALSE.'},{'role':'user','content':'\n\n'.join(parts)}]
def digest(b): return hashlib.sha256(b).hexdigest()
def cases(items,raw):
    for item in items:
      for substrate in ('record','no_e'):
       for role in (('support','refute') if substrate=='record' else ('none',)):
        for wording in QUERIES:
         for cell in CELLS:
          msg=messages(item,substrate,role,wording,cell)
          yield dict(id=item['id'],substrate=substrate,e_role=role,wording=wording,cell=cell,items_sha256=digest(raw),prompt_sha256=digest(json.dumps(msg,sort_keys=True,ensure_ascii=False).encode()),messages=msg)
def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--model',required=True);ap.add_argument('--tag',required=True);ap.add_argument('--out',required=True);ap.add_argument('--limit',type=int);ap.add_argument('--gpu-frac',type=float,default=.82);ap.add_argument('--tokenizer');ap.add_argument('--items',default=str(ITEMS));ap.add_argument('--max-seqs',type=int,default=32);ap.add_argument('--resume',action='store_true');ap.add_argument('--case-start',type=int,default=0);ap.add_argument('--case-end',type=int)
    a=ap.parse_args();raw=Path(a.items).read_bytes();items=[json.loads(s) for s in raw.splitlines() if s];items=items[:a.limit] if a.limit else items
    rows=list(cases(items,raw))[a.case_start:a.case_end]
    path=Path(a.out);path.parent.mkdir(parents=True,exist_ok=True)
    lock=path.with_suffix(path.suffix+'.lock').open('a')
    fcntl.flock(lock,fcntl.LOCK_EX|fcntl.LOCK_NB)
    completed=[]
    if path.exists():
        if not a.resume: raise RuntimeError('Existing output requires --resume; refusing overwrite')
        completed=[json.loads(line) for line in path.read_text().splitlines() if line]
        for old,expected in zip(completed,rows):
            assert old['model_tag']==a.tag
            assert all(old[k]==v for k,v in expected.items()), 'Resume input mismatch'
            assert 0<=old['p_true']<=1 and old['verdict'] in ('TRUE','FALSE')
        assert len(completed)<=len(rows)
    offset=len(completed);rows=rows[offset:]
    print(f'Resuming {a.tag}: preserving {offset} rows, {len(rows)} remaining',flush=True)
    if not rows:return
    from transformers import AutoTokenizer
    from vllm import LLM,SamplingParams
    tok=AutoTokenizer.from_pretrained(a.tokenizer or a.model,**({'fix_mistral_regex':True} if a.tag=='mistral-small-24b' else {}))
    tokens={s:tok.encode(s,add_special_tokens=False) for s in ('TRUE','FALSE')}
    assert all(len(v)==1 for v in tokens.values()),tokens
    tid,fid=tokens['TRUE'][0],tokens['FALSE'][0]
    llm=LLM(logprobs_mode='processed_logprobs',model=a.model,tokenizer=a.tokenizer or a.model,tensor_parallel_size=1,gpu_memory_utilization=a.gpu_frac,max_model_len=2048,dtype='bfloat16',disable_log_stats=True,enforce_eager=True,enable_prefix_caching=True,max_num_seqs=a.max_seqs,max_num_batched_tokens=2048)
    prompts=[]
    for r in rows:
        ids=tok.apply_chat_template(r['messages'],tokenize=True,add_generation_prompt=True,enable_thinking=False)
        if isinstance(ids,dict):ids=ids['input_ids']
        if ids and isinstance(ids[0],list):ids=ids[0]
        prompts.append({'prompt_token_ids':list(ids)})
    with path.open('a') as out:
      for start in range(0,len(rows),512):
        outputs=llm.generate(prompts[start:start+512],SamplingParams(temperature=0,max_tokens=1,logprobs=2,allowed_token_ids=[tid,fid]),use_tqdm=False)
        for r,res in zip(rows[start:start+512],outputs):
          gen=res.outputs[0];logs=gen.logprobs[0]
          lt,lf=logs[tid].logprob,logs[fid].logprob
          p=1/(1+math.exp(max(-700,min(700,lf-lt))))
          r.update(execution_host=socket.gethostname(),logprobs_mode='processed_logprobs',model_tag=a.tag,p_true=p,verdict=('TRUE' if gen.token_ids[0]==tid else 'FALSE'),raw=gen.text,true_logprob=lt,false_logprob=lf,true_token=tid,false_token=fid,finish_reason=gen.finish_reason)
          out.write(json.dumps(r,ensure_ascii=False)+'\n')
        out.flush();print(f'{a.tag}: {offset+min(start+512,len(rows))}/{offset+len(rows)}',flush=True)
if __name__=='__main__':main()
