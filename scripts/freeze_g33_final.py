"""Select by predeclared independent material audits; never read model outputs."""
import collections,hashlib,json
from pathlib import Path
R=Path(__file__).resolve().parents[1];D=R/'data/items/g33_final'
def read(p):return [json.loads(s) for s in p.read_text().splitlines() if s]
def main():
 candidates=read(D/'candidates.jsonl');selected=[];ledger=[];counts=collections.Counter()
 challenges={}
 for cp in sorted(D.glob('challenge_[0-9][0-9].jsonl')):
  rows=read(cp);inp=read(D/f'challenge_input_{cp.stem.split("_")[-1]}.jsonl');assert {x['id'] for x in rows}=={x['id'] for x in inp} and len(rows)==len(inp)
  for row in rows: assert row['id'] not in challenges;challenges[row['id']]=row
 manual={x['id']:x['reason'] for x in read(D/'manual_exclusions.jsonl')}
 missing_challenges=0
 pending_ids=[]
 for batch in range(1,len(candidates)//20+1):
  ip=D/f'input_{batch:02d}.jsonl';gp=D/f'generated_{batch:02d}.jsonl';ap=D/f'audit_{batch:02d}.jsonl'
  if not gp.exists() or not ap.exists():break
  ins={x['id']:x for x in read(ip)};gens={x['id']:x for x in read(gp)};aud={x['id']:x for x in read(ap)}
  assert len(ins)==len(gens)==len(aud)==20 and ins.keys()==gens.keys()==aud.keys()
  for src in candidates[(batch-1)*20:batch*20]:
   k=src['id'];i,g,a=ins[k],gens[k],aud[k]
   roles=('support','refute') if i['evidence_a']==src['evidence_s'] else ('refute','support')
   assert i['evidence_a'] in (src['evidence_s'],src['evidence_r'])
   checks={'generation_source':g['source_valid'],'generation_roles':(g['a_relation'],g['b_relation'])==roles,'audit_source':a['source_valid'],'audit_E_roles':(a['e_a_relation'],a['e_b_relation'])==roles,'audit_X_roles':(a['x_a_relation'],a['x_b_relation'])==roles,'audit_faithfulness':a['faithful'],'audit_naturalness':a['natural'],'audit_accept':a['accept'],'nonempty_X':bool(g['x_a'].strip() and g['x_b'].strip())}
   base_ok=all(checks.values())
   if base_ok:
    counts.update(['provisional_eligible'])
    ch=challenges.get(k)
    if ch is None:
     missing_challenges+=1
     if k not in manual:pending_ids.append(k)
    else: counts.update(['source_challenged'])
    checks['challenge_complete']=ch is not None
    checks['challenge_roles']=ch is not None and (ch['a_relation'],ch['b_relation'])==roles
    checks['challenge_decisive']=ch is not None and ch['decisive']
    checks['challenge_scope']=ch is not None and ch['clear_scope']
    checks['challenge_readable']=ch is not None and ch['readable']
   checks['manual_clear']=k not in manual
   ok=all(checks.values());counts.update(['accepted' if ok else ('pending' if k in pending_ids else 'rejected')]);counts.update('fails_'+q for q,v in checks.items() if not v)
   ledger.append(dict(id=k,batch=batch,accepted=ok,checks=checks,generation_reason=g['reason'],audit_reason=a['reason'],source_challenge_reason=challenges.get(k,{}).get('reason'),manual_exclusion_reason=manual.get(k)))
   if ok:
    x_s,x_r=(g['x_a'],g['x_b']) if roles[0]=='support' else (g['x_b'],g['x_a'])
    selected.append(dict(src,x_s=x_s,x_r=x_r,material_batch=batch))
 print(json.dumps(dict(counts),indent=2))
 (D/'selection_ledger.jsonl').write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in ledger))
 report={'audited':len(ledger),'counts':dict(counts),'selection':'first 200 accepted in seeded candidate order','complete_batches':len(ledger)//20,'missing_source_challenges':missing_challenges,'manual_exclusions':manual}
 order={x['id']:n for n,x in enumerate(candidates)}
 blocking_pending=len(selected)<200 or any(order[k]<order[selected[199]['id']] for k in pending_ids)
 report['pending_ids']=pending_ids
 report['pending_before_selection_boundary']=blocking_pending
 if blocking_pending:
  report['frozen']=False;(D/'selection_report.json').write_text(json.dumps(report,indent=2)+'\n');raise SystemExit('Not enough independently accepted families; no smaller convenience sample frozen.')
 # Preserve seeded order even if batches finish in arbitrary order.
 order={x['id']:n for n,x in enumerate(candidates)};selected.sort(key=lambda x:order[x['id']]);selected=selected[:200]
 assert len({x['page'] for x in selected})==200
 payload=''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in selected).encode()
 report.update(frozen=True,selected=200,items_sha256=hashlib.sha256(payload).hexdigest(),selected_ids=[x['id'] for x in selected])
 (D/'selected.jsonl').write_bytes(payload);(D/'selection_report.json').write_text(json.dumps(report,indent=2)+'\n')
if __name__=='__main__':main()
