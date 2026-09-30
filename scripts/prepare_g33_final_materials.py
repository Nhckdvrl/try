"""Final-round source-only shortlist: fresh natural, nonnumeric revision pairs."""
import argparse
import csv
import hashlib
import json
import random
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'data/items/g33_final'
SHAS = {'train': '7461c6fd1a13459590317c5ccdc8651dd2daf7c1ad8ae4b10ccd88d164fccd5a',
        'dev': '544934677f5d133873e6d38f4557f8966f4efa5d3d70874ffe6913f2091b86b5',
        'test': '7ad1808dbc30c62e0a1427a53022d0dfaff668a1fde3c4b612a2d266edd753ad'}

def norm(s):
    return re.sub(r'\s+', ' ', s).strip().casefold().rstrip(' .')

def render(s):
    s = re.sub(r'\s+', ' ', s).strip()
    s = re.sub(r'\s+([,.;:!?])', r'\1', s)
    s = re.sub(r"\s+('s)\b", r'\1', s)
    s = s.replace('`` ', '“').replace(" ''", '”')
    return s

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--count',type=int,default=600);args=ap.parse_args();assert args.count%20==0
    old_cases, old_claims = set(), set()
    paths = list((ROOT/'data/items').glob('*.jsonl')) + list((ROOT/'data/items').glob('*.csv'))
    paths += list((ROOT/'results/pilots/vitaminc_pilot_r1').glob('pool*.jsonl'))
    for p in paths:
        if p.suffix == '.csv':
            rows = csv.DictReader(p.open())
        else:
            rows = (json.loads(x) for x in p.open() if x.strip())
        for a in rows:
            case = a.get('case_id') or a.get('meta', {}).get('case_id')
            if case: old_cases.add(str(case))
            claim = a.get('claim') or a.get('base_context')
            if isinstance(claim, str): old_claims.add(norm(claim))
    groups = defaultdict(lambda: {'SUPPORTS': [], 'REFUTES': []})
    for split, expected in SHAS.items():
        p = ROOT / f'data/external/raw/vitaminc/{split}.jsonl'
        assert hashlib.sha256(p.read_bytes()).hexdigest() == expected
        for line_no, line in enumerate(p.open(), 1):
            a = json.loads(line)
            if a.get('revision_type') != 'real' or a.get('FEVER_id'): continue
            if a.get('label') not in ('SUPPORTS', 'REFUTES'): continue
            c, s = a['claim'], a['evidence']
            if str(a['case_id']) in old_cases or norm(c) in old_claims: continue
            if re.search(r'\d|%|\b(?:less than|more than|fewer than|at least|at most)\b', c, re.I): continue
            if re.search(r'^(?:The (?:film|song|album|show|band|series)\b|It\b|He\b|She\b|They\b|This\b|That\b|His\b|Her\b)', c): continue
            if not (20 <= len(c) <= 220 and 35 <= len(s) <= 500): continue
            if not c.isascii() or not s.isascii(): continue
            if re.search(r'http|citation needed|\[|\]|[{}<>]|-LRB-|-RRB-', c+s, re.I): continue
            groups[(str(a['case_id']), c, a.get('page', ''))][a['label']].append((s, split, line_no, a['unique_id']))
    candidates = []
    for (case, claim, page), pair in sorted(groups.items()):
        s = {a[0]: a for a in pair['SUPPORTS']}; r = {a[0]: a for a in pair['REFUTES']}
        if len(s) != 1 or len(r) != 1: continue
        sa, ra = next(iter(s.values())), next(iter(r.values()))
        if sa[0] == ra[0]: continue
        candidates.append({'case_id': case, 'page': page, 'claim_raw': claim,
                           'claim': render(claim), 'evidence_s_raw': sa[0], 'evidence_r_raw': ra[0],
                           'evidence_s': render(sa[0]), 'evidence_r': render(ra[0]),
                           'source_s': {'split': sa[1], 'line': sa[2], 'unique_id': sa[3]},
                           'source_r': {'split': ra[1], 'line': ra[2], 'unique_id': ra[3]}})
    random.Random(20260930).shuffle(candidates)
    chosen, cases, pages, claims = [], set(), set(), set()
    for a in candidates:
        if a['case_id'] in cases or a['page'] in pages or norm(a['claim']) in claims: continue
        cases.add(a['case_id']); pages.add(a['page']); claims.add(norm(a['claim']))
        a['id'] = f'g33_{len(chosen):04d}'; chosen.append(a)
        if len(chosen) == args.count: break
    assert len(chosen) == args.count, len(chosen)
    old_path=OUT/'candidates.jsonl'
    if old_path.exists():
        old=[json.loads(s) for s in old_path.read_text().splitlines() if s]
        assert len(old)<=len(chosen) and chosen[:len(old)]==old, 'Existing seeded prefix must stay byte-equivalent in content.'
    OUT.mkdir(parents=True, exist_ok=True)
    (OUT/'candidates.jsonl').write_text(''.join(json.dumps(a, ensure_ascii=False)+'\n' for a in chosen))
    for j in range(0, len(chosen), 20):
        batch = []
        for a in chosen[j:j+20]:
            swap = int(hashlib.sha256(a['id'].encode()).hexdigest(), 16)%2
            batch.append({'id':a['id'], 'page':a['page'], 'claim':a['claim'],
                          'evidence_a':a['evidence_r'] if swap else a['evidence_s'],
                          'evidence_b':a['evidence_s'] if swap else a['evidence_r']})
        (OUT/f'input_{j//20+1:02d}.jsonl').write_text(''.join(json.dumps(a, ensure_ascii=False)+'\n' for a in batch))
    report = {'mechanical_pairs':len(candidates), 'shortlist':len(chosen), 'historical_cases_excluded':len(old_cases),
              'historical_claims_excluded':len(old_claims), 'source_hashes':SHAS,
              'candidates_sha256':hashlib.sha256((OUT/'candidates.jsonl').read_bytes()).hexdigest()}
    (OUT/'source_report.json').write_text(json.dumps(report, indent=2)+'\n')
    print(json.dumps(report, indent=2))

if __name__ == '__main__': main()
