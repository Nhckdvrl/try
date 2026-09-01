import hashlib
from pathlib import Path
import sys

import numpy as np

ROOT=Path(__file__).resolve().parents[1]; sys.path.insert(0,str(ROOT/"src"))
from adapters.btf3_donor_outcome import build_donor_pairs
from information_set_schema import load_jsonl
from mech.shared_outcome import balanced_accuracy,frozen_split,learn_axis,orthogonal_axis,split_digest
from mech.analyze_shared_outcome import analyze
from mech.run_decision_outcome import generate_answer_patch


def test_frozen_split_is_exact_and_donor_disjoint():
    items=load_jsonl(ROOT/"data/external/review/btf3_temporal_large_replication_v1.jsonl")
    pairs=build_donor_pairs(items); split=frozen_split(pairs)
    assert {k:len(v) for k,v in split.items()}=={"train":190,"test":64,"buffer":2}
    assert split_digest(pairs,split)=="9141b929425aa1bcb6b393eab767b93e19113e78aabab7d3eb16f3ae96b13dcb"
    donors=lambda ids:{pairs[i][s]["donor_unit_id"] for i in ids for s in ("yes","no")}
    assert donors(split["train"]).isdisjoint(donors(split["test"]))
    assert sorted(split["train"]+split["test"]+split["buffer"])==list(range(256))


def test_axis_readout_and_orthogonal_control():
    yes=np.array([[2.,1.,0.],[3.,-1.,0.]],dtype=np.float32)
    no=np.array([[-2.,1.,0.],[-3.,-1.,0.]],dtype=np.float32)
    v,ym,nm=learn_axis(yes,no)
    assert balanced_accuracy(yes,no,v,ym,nm)==1.0
    w=orthogonal_axis(v,layer=11)
    assert abs(float(v@w))<1e-6 and abs(float(np.linalg.norm(w))-1)<1e-6


def test_analyzer_requires_adjacent_transfer_and_specificity():
    units=[f"u{i}" for i in range(64)]
    data={"representation":{str(l):{"heldout_balanced_accuracy":.9} for l in (5,11,17,23,29,35,41,47)},
          "baseline":[],"patches":[]}
    for i,u in enumerate(units):
        data["baseline"] += [{"unit":u,"outcome":"no","value":30.0},{"unit":u,"outcome":"yes","value":50.0}]
        for l in (5,11,17,23,29,35,41,47):
            strong=l in (17,23); shift=5.0 if strong else 0.0
            for kind in ("outcome","orthogonal"):
                s=shift if kind=="outcome" else 0.0
                data["patches"] += [{"unit":u,"layer":l,"axis_kind":kind,"target":"no","value":30+s},
                                    {"unit":u,"layer":l,"axis_kind":kind,"target":"yes","value":50-s}]
    report=analyze(data)
    assert report["verdict"]=="shared-causal-outcome-variable"
    assert report["causal"]["adjacent_windows"]==[(17,23)]


def test_g14_reuses_exact_g13_test_baseline():
    path=ROOT/"results/mech/g13_shared_outcome.json"
    if not path.exists(): return
    raw=__import__("json").loads(path.read_text()); rows=raw["baseline"]
    assert len(rows)==128
    assert sum(r["outcome"]=="yes" for r in rows)==64
    assert sum(r["outcome"]=="no" for r in rows)==64
    assert len({r["unit"] for r in rows})==64
