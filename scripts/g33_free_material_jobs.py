"""Independent OpenCode free-model material jobs, four isolated output files at a time."""
import argparse
import concurrent.futures
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT/'data/items/g33_final'
MODELS = ('opencode/mimo-v2.6-flash-free', 'opencode/longcat-2.5-preview-free')

def read(p):
    return [json.loads(x) for x in p.read_text().splitlines() if x.strip()]

def valid(p, ids, stage):
    try:
        rows = read(p)
        assert len(rows) == len(ids) and {x['id'] for x in rows} == set(ids)
        for x in rows:
            assert isinstance(x['source_valid'], bool) and x['reason'].strip()
            if stage == 'audit':
                assert all(isinstance(x[k], bool) for k in ('faithful', 'natural', 'accept'))
                assert all(x[k] in ('support', 'refute', 'unclear') for k in ('e_a_relation', 'e_b_relation', 'x_a_relation', 'x_b_relation'))
            else:
                assert x['a_relation'] in ('support', 'refute', 'unclear') and x['b_relation'] in ('support', 'refute', 'unclear')
                assert isinstance(x['x_a'], str) and isinstance(x['x_b'], str)
        return True
    except (FileNotFoundError, ValueError, AssertionError, KeyError, TypeError):
        return False

def job(batch, stage):
    inp = BASE/f'input_{batch:02d}.jsonl'
    ids = [x['id'] for x in read(inp)]
    prefix = 'generated' if stage == 'construct' else 'audit'
    target = BASE/f'{prefix}_{batch:02d}.jsonl'
    if valid(target, ids, stage):
        print(f'{stage} batch {batch:02d}: existing complete output', flush=True)
        return True
    if stage == 'audit':
        gen = {x['id']:x for x in read(BASE/f'generated_{batch:02d}.jsonl')}
        review = [dict(a, x_a=gen[a['id']]['x_a'], x_b=gen[a['id']]['x_b']) for a in read(inp)]
        inp = BASE/f'review_{batch:02d}.jsonl'
        inp.write_text(''.join(json.dumps(a, ensure_ascii=False)+'\n' for a in review))
    for attempt in range(1, 3):
        # Audit uses a different model from construction whenever its provenance is available.
        if stage == 'audit':
            meta = BASE/f'construct_{batch:02d}_provenance.json'
            gen_model = json.loads(meta.read_text())['model'] if meta.exists() else MODELS[0]
            model = MODELS[1] if gen_model == MODELS[0] else MODELS[0]
        else:
            model = MODELS[(attempt-1)%2]
        attempt_out = BASE/f'{prefix}_{batch:02d}_attempt{attempt}.jsonl'
        instruction = BASE/('CONSTRUCTION.md' if stage == 'construct' else 'AUDIT.md')
        message = (f'Read {instruction.relative_to(ROOT)} and {inp.relative_to(ROOT)} only. '
                   f'Process every row according to the instructions. Write {attempt_out.relative_to(ROOT)}. '
                   'Verify JSON row count and IDs. Do not read any research results or other judgments.')
        log = BASE/f'{stage}_{batch:02d}_attempt{attempt}.log'
        try:
            with log.open('w') as stream:
                p = subprocess.run(['opencode', 'run', '--model', model, message], cwd=ROOT,
                                   stdout=stream, stderr=subprocess.STDOUT, timeout=600)
            code = p.returncode
        except subprocess.TimeoutExpired:
            code = 'timeout'
        if valid(attempt_out, ids, stage):
            target.write_bytes(attempt_out.read_bytes())
            (BASE/f'{stage}_{batch:02d}_provenance.json').write_text(json.dumps({'model':model, 'attempt':attempt,
                            'output':attempt_out.name, 'returncode':code}, indent=2)+'\n')
            print(f'{stage} batch {batch:02d}: complete, {model}', flush=True)
            return True
        print(f'{stage} batch {batch:02d}: attempt {attempt} incomplete ({code})', flush=True)
    return False

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--stage', choices=['construct', 'audit'], required=True)
    ap.add_argument('--first', type=int, default=1)
    ap.add_argument('--last', type=int, default=20)
    args = ap.parse_args()
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
        done = list(ex.map(lambda b:job(b,args.stage), range(args.first, args.last+1)))
    print(json.dumps({'stage':args.stage, 'complete_batches':sum(done), 'requested_batches':len(done)}), flush=True)
    if not all(done): raise SystemExit(1)

if __name__ == '__main__': main()
