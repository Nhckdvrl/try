from collections import Counter
from pathlib import Path
import sys
ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/"src"))
from adapters.btf3_donor_outcome import assignment_digest,build_donor_pairs
from adapters.btf3_packet_swap import PACKET_HEADER,TASK_HEADER,derangement
from adapters.btf3_hindsight_depth import residual_verdict_hits
from information_set_schema import load_jsonl
ART=ROOT/"data/external/review/btf3_temporal_large_replication_v1.jsonl"

def test_pairing_is_balanced_fresh_and_deterministic():
    items=load_jsonl(ART); a=build_donor_pairs(items); b=build_donor_pairs(items)
    assert assignment_digest(a)==assignment_digest(b)
    old=derangement(256)
    ids=[x.independent_unit_id for x in items]
    for outcome in ("yes","no"):
        donors=[r[outcome]["donor_unit_id"] for r in a]; assert set(Counter(donors).values())=={2}
    for i,r in enumerate(a):
        assert r["yes"]["donor_unit_id"]!=r["independent_unit_id"]
        assert r["no"]["donor_unit_id"]!=r["independent_unit_id"]
        assert r["yes"]["donor_unit_id"]!=ids[old[i]] and r["no"]["donor_unit_id"]!=ids[old[i]]

def test_prompts_differ_only_in_packet_and_have_opposite_donor_outcomes():
    items=load_jsonl(ART); pairs=build_donor_pairs(items); sign={x.independent_unit_id:int(x.reference_context["outcome_alignment_sign"]) for x in items}
    for r in pairs:
        y,n=r["yes"]["prompt"],r["no"]["prompt"]
        ys=y.index(PACKET_HEADER)+len(PACKET_HEADER); ye=y.index(TASK_HEADER,ys)
        ns=n.index(PACKET_HEADER)+len(PACKET_HEADER); ne=n.index(TASK_HEADER,ns)
        assert y[:ys]==n[:ns] and y[ye:]==n[ne:]
        assert sign[r["yes"]["donor_unit_id"]]==1 and sign[r["no"]["donor_unit_id"]]==-1
        for prompt,start,end in ((y,ys,ye),(n,ns,ne)):
            assert not [h for h in residual_verdict_hits(prompt[start:end]) if h["assertive"]]

