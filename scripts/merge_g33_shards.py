"""Verify disjoint frozen case coverage and preserved prefixes before merging."""
import hashlib,json
from pathlib import Path
from run_g33_final import ITEMS,cases
R=Path(__file__).resolve().parents[1]
raw=ITEMS.read_bytes();expected=list(cases([json.loads(s) for s in raw.splitlines()],raw))
assert len(expected)==14400
prefixes=json.loads((R/'results/g33/g33_preserved_prefixes.json').read_text())
for tag in ('qwen3-8b','gemma3-12b','mistral-small-24b'):
 head=R/f'results/raw/{tag}_g33_final_v1.jsonl';tail=R/f'results/raw/{tag}_g33_final_tail.jsonl'
 a,b=head.read_bytes(),tail.read_bytes();ar=a.splitlines(keepends=True);br=b.splitlines(keepends=True)
 assert len(ar)==len(br)==7200,(tag,len(ar),len(br))
 preserved=prefixes[head.name];assert hashlib.sha256(b''.join(ar[:preserved['rows']])).hexdigest()==preserved['sha256']
 for line,ref in zip(ar+br,expected):
  row=json.loads(line);assert row['model_tag']==tag and all(row[k]==v for k,v in ref.items())
 merged=head.with_suffix('.merge.tmp');merged.write_bytes(a+b);merged.replace(head)
 print(f'{tag}: 14400 exact cases, preserved prefix verified')
