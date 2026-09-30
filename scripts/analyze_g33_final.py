"""Registered claim-cluster analysis, integrity checked against frozen compiler."""
import hashlib,json,sys
from pathlib import Path
import numpy as np
from run_g33_final import ITEMS,cases
R=Path(__file__).resolve().parents[1]
def main():
 raw=ITEMS.read_bytes();items=[json.loads(s) for s in raw.splitlines() if s];ids=[x['id'] for x in items];expected=list(cases(items,raw))
 key=lambda r:(r['id'],r['substrate'],r['e_role'],r['wording'],r['cell'])
 exp={key(r):r for r in expected};assert len(exp)==len(expected)==14400 and len(ids)==200
 boot=np.random.default_rng(20260930).integers(0,len(ids),(10000,len(ids)))
 def stat(v):
  v=np.array(v,dtype=float);assert v.shape==(200,) and np.isfinite(v).all();lo,hi=np.quantile(v[boot].mean(1),[.025,.975]);return dict(mean=float(v.mean()),ci95=[float(lo),float(hi)])
 summary={};itemmetrics=[]; integrity={}
 for tag in ('qwen3-8b','gemma3-12b','mistral-small-24b'):
  path=R/f'results/raw/{tag}_g33_final_v1.jsonl';content=path.read_bytes();rows=[json.loads(s) for s in content.splitlines() if s];lookup={key(r):r for r in rows};assert len(rows)==len(lookup)==len(exp) and lookup.keys()==exp.keys()
  for k,r in lookup.items():
   ref=exp[k];assert all(r[f]==ref[f] for f in ('items_sha256','prompt_sha256','messages'));assert r['model_tag']==tag and 0<=r['p_true']<=1 and r['verdict'] in ('TRUE','FALSE')
   assert abs(r['p_true']-.5)<1e-12 or (r['verdict']=='TRUE')==(r['p_true']>=.5)
  integrity[tag]={'rows':len(rows),'raw_sha256':hashlib.sha256(content).hexdigest()}
  def arr(substrate,role,w,c,f='p_true'):return np.array([lookup[(i,substrate,role,w,c)][f] if f=='p_true' else lookup[(i,substrate,role,w,c)]['verdict']=='TRUE' for i in ids],dtype=float)
  def avg(a):return np.mean(a,axis=0)
  def accuracy(w,c):return avg([arr('record','support',w,c,'verdict'),1-arr('record','refute',w,c,'verdict')])
  def acc(c):return avg([accuracy(w,c) for w in ('w1','w2')])
  def sens(sub,q,absolute=True,wordings=('w1','w2'),field='p_true'):
   roles=('support','refute') if sub=='record' else ('none',)
   dif=[arr(sub,e,w,q+'C+',field)-arr(sub,e,w,q+'C-',field) for e in roles for w in wordings]
   return avg([abs(d) for d in dif] if absolute else dif)
  costs={q:acc('F'+q)-avg([acc(q+'C+'),acc(q+'C-')]) for q in ('D','C','S')}
  h=costs['C']-costs['D'];metrics={'B_accuracy':stat(acc('B')),'H_C_minus_D_legal_cost':stat(h),'H_S_minus_D_legal_cost':stat(costs['S']-costs['D']),'C_minus_D_absolute_X_sensitivity':stat(sens('record','C')-sens('record','D')),'C_minus_D_binary_X_sensitivity':stat(sens('record','C',field='verdict')-sens('record','D',field='verdict'))}
  for w in ('w1','w2'):
   wd=accuracy(w,'FD')-avg([accuracy(w,'DC+'),accuracy(w,'DC-')]);wc=accuracy(w,'FC')-avg([accuracy(w,'CC+'),accuracy(w,'CC-')]);metrics['H_'+w]=stat(wc-wd)
  for q in ('D','C','S'):
   metrics['G_'+q]=stat(costs[q]);metrics['accuracy_'+q]=stat(avg([acc(q+'C+'),acc(q+'C-')]))
   metrics['accuracy_F'+q]=stat(acc('F'+q));metrics['frame_cost_'+q]=stat(acc('B')-acc('F'+q))
   metrics['X_binary_abs_'+q]=stat(sens('record',q,field='verdict'));metrics['X_abs_'+q]=stat(sens('record',q));metrics['X_signed_'+q]=stat(sens('record',q,False))
   metrics['E_leverage_'+q]=stat(avg([arr('record','support',w,q+'C'+x)-arr('record','refute',w,q+'C'+x) for w in ('w1','w2') for x in ('+','-')]))
   for sub in ('record','no_e'):
    roles=('support','refute') if sub=='record' else ('none',)
    restore=avg([abs(arr(sub,e,w,q+'C'+x)-arr(sub,e,w,'B')) for e in roles for w in ('w1','w2') for x in ('+','-')])
    flips=avg([abs(arr(sub,e,w,q+'C'+x,'verdict')-arr(sub,e,w,'B','verdict')) for e in roles for w in ('w1','w2') for x in ('+','-')])
    frame=avg([abs(arr(sub,e,w,'F'+q)-arr(sub,e,w,'B')) for e in roles for w in ('w1','w2')])
    metrics[sub+'_restore_'+q]=stat(restore);metrics[sub+'_B_flips_'+q]=stat(flips);metrics[sub+'_frame_shift_'+q]=stat(frame)
    metrics[sub+'_X_abs_'+q]=stat(sens(sub,q));metrics[sub+'_X_signed_'+q]=stat(sens(sub,q,False))
  metrics['E_leverage_B']=stat(avg([arr('record','support',w,'B')-arr('record','refute',w,'B') for w in ('w1','w2')]))
  for sub in ('record','no_e'):
   roles=('support','refute') if sub=='record' else ('none',)
   metrics[sub+'_active_X_abs']=stat(avg([abs(arr(sub,e,w,'A+')-arr(sub,e,w,'A-')) for e in roles for w in ('w1','w2')]))
  m=lambda k:metrics[k]['mean']
  eligible=m('B_accuracy')>=.8 and m('E_leverage_B')>=.5
  meets=eligible and m('H_C_minus_D_legal_cost')>=.05 and metrics['H_C_minus_D_legal_cost']['ci95'][0]>0 and m('H_w1')>0 and m('H_w2')>0 and m('C_minus_D_absolute_X_sensitivity')<=.02 and m('C_minus_D_binary_X_sensitivity')<=.02
  summary[tag]={'metrics':metrics,'substrate_eligible':eligible,'registered_candidate_criteria':bool(meets)}
  for n,i in enumerate(ids):itemmetrics.append(dict(id=i,model_tag=tag,H=float(h[n]),G_D=float(costs['D'][n]),G_C=float(costs['C'][n]),G_S=float(costs['S'][n])))
 report={'items_sha256':hashlib.sha256(raw).hexdigest(),'items':len(ids),'bootstrap':'10000 paired claim resamples, seed 20260930','integrity':integrity,'models':summary,'candidate_models':sum(s['registered_candidate_criteria'] for s in summary.values())}
 dest=R/'results/g33';dest.mkdir(exist_ok=True,parents=True);(dest/'g33_analysis.json').write_text(json.dumps(report,indent=2)+'\n');(dest/'g33_item_metrics.jsonl').write_text(''.join(json.dumps(r)+'\n' for r in itemmetrics))
 def fmt(v):return f"{100*v['mean']:.2f} [{100*v['ci95'][0]:.2f}, {100*v['ci95'][1]:.2f}]"
 keys=('B_accuracy','E_leverage_B','accuracy_D','accuracy_C','accuracy_S','G_D','G_C','G_S','H_C_minus_D_legal_cost','H_w1','H_w2','C_minus_D_absolute_X_sensitivity','C_minus_D_binary_X_sensitivity','X_binary_abs_D','X_binary_abs_C','X_binary_abs_S','X_abs_D','X_abs_C','X_abs_S','frame_cost_D','frame_cost_C','frame_cost_S','no_e_restore_D','no_e_restore_C','no_e_restore_S','no_e_frame_shift_D','no_e_frame_shift_C','no_e_frame_shift_S')
 table=['# G33 registered summaries','', 'All values are percentage points; intervals are paired claim-cluster bootstrap 95% intervals. Normalized TRUE probability is a constrained-choice readout, not calibrated belief.', '', '| Estimand | Qwen3-8B | Gemma3-12B | Mistral-Small-24B |','|---|---:|---:|---:|']
 for k in keys:table.append('| '+k+' | '+' | '.join(fmt(summary[t]['metrics'][k]) for t in summary)+' |')
 table+=['',f"Models satisfying the registered candidate criteria: {report['candidate_models']}/3. This is a diagnostic gate, not automatic novelty or equivalence.",'']
 (dest/'g33_registered_summaries.md').write_text('\n'.join(table));print(json.dumps({'candidate_models':report['candidate_models'],'integrity':integrity},indent=2))
if __name__=='__main__':main()
