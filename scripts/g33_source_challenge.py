"""A stricter, source-only objection pass; output-blind material curation."""
import argparse,concurrent.futures,json,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];D=ROOT/'data/items/g33_final'
def read(p):return [json.loads(s) for s in p.read_text().splitlines() if s]
def prepare():
 candidates=read(D/'candidates.jsonl');valid=[];blinds={}
 for batch in range(1,len(candidates)//20+1):
  gp=D/f'generated_{batch:02d}.jsonl';ap=D/f'audit_{batch:02d}.jsonl'
  if not gp.exists() or not ap.exists():break
  ins={x['id']:x for x in read(D/f'input_{batch:02d}.jsonl')};g={x['id']:x for x in read(gp)};a={x['id']:x for x in read(ap)}
  for src in candidates[(batch-1)*20:batch*20]:
   k=src['id'];i=ins[k];gg=g[k];aa=a[k];roles=('support','refute') if i['evidence_a']==src['evidence_s'] else ('refute','support')
   if gg['source_valid'] and (gg['a_relation'],gg['b_relation'])==roles and all(aa[x] for x in ('source_valid','faithful','natural','accept')) and (aa['e_a_relation'],aa['e_b_relation'])==roles and (aa['x_a_relation'],aa['x_b_relation'])==roles and gg['x_a'] and gg['x_b']:
    valid.append(i);blinds[k]=roles
 # Append-only groups: reruns preserve existing groups even as candidate prefix grows.
 used=set()
 for p in D.glob('challenge_input_*.jsonl'):used.update(x['id'] for x in read(p))
 remaining=[x for x in valid if x['id'] not in used];nextbatch=len(list(D.glob('challenge_input_*.jsonl')))+1
 for start in range(0,len(remaining),20):
  group=remaining[start:start+20];(D/f'challenge_input_{nextbatch:02d}.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in group));nextbatch+=1
 print(json.dumps({'previous':len(used),'new':len(remaining),'groups':nextbatch-1}),flush=True)
def valid(p,ids):
 try:
  r=read(p);assert len(r)==len(ids) and {x['id'] for x in r}==set(ids)
  for x in r:
   assert all(isinstance(x[k],bool) for k in ('decisive','clear_scope','readable')) and x['reason'].strip()
   assert all(x[k] in ('support','refute','unclear') for k in ('a_relation','b_relation'))
  return True
 except (ValueError,AssertionError,KeyError,FileNotFoundError,TypeError):return False
def job(inp):
 b=inp.stem.split('_')[-1];ids=[x['id'] for x in read(inp)];out=D/f'challenge_{b}.jsonl'
 if valid(out,ids):print('challenge',b,'existing',flush=True);return True
 for attempt,model in enumerate(('opencode/muse-spark-1.3-contributor-free','opencode/longcat-2.5-preview-free'),1):
  dest=D/f'challenge_{b}_attempt{attempt}.jsonl';log=D/f'challenge_{b}_attempt{attempt}.log'
  msg=f'Read data/items/g33_final/SOURCE_CHALLENGE.md and {inp.relative_to(ROOT)} ONLY. Challenge each source pair independently. Write {dest.relative_to(ROOT)}. Verify IDs and count. Do not read X summaries, previous audits or research results.'
  try:
   with log.open('w') as f:p=subprocess.run(['opencode','run','--model',model,msg],cwd=ROOT,stdout=f,stderr=subprocess.STDOUT,timeout=600)
   code=p.returncode
  except subprocess.TimeoutExpired:code='timeout'
  if valid(dest,ids):
   out.write_bytes(dest.read_bytes());(D/f'challenge_{b}_provenance.json').write_text(json.dumps({'model':model,'attempt':attempt,'output':dest.name,'returncode':code},indent=2)+'\n');print('challenge',b,'complete',model,flush=True);return True
  print('challenge',b,'incomplete',code,flush=True)
 return False
def main():
 ap=argparse.ArgumentParser();ap.add_argument('--prepare',action='store_true');a=ap.parse_args()
 if a.prepare:prepare()
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:okay=list(ex.map(job,sorted(D.glob('challenge_input_*.jsonl'))))
 if not all(okay):raise SystemExit(1)
if __name__=='__main__':main()
