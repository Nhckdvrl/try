"""Freeze first approved natural irrelevant sentence per G29 claim."""

import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT/"data/items/g29b_blind_irrelevance_v1"
OUT=ROOT/"data/items/g29b_irrelevant_selected_v1.jsonl"
REPORT=ROOT/"results/audits/g29b_irrelevance_audit_v1.md"


def read(path):
    return [json.loads(s) for s in path.read_text().splitlines() if s]


def main():
    source=read(ROOT/"data/items/g29b_irrelevant_candidates_v1.jsonl")
    assert len(source)==80
    selected=[]
    counts={0:0,1:0,2:0,-1:0}
    for b in range(4):
        blind=read(BASE/f"blind_{b+1:02d}.jsonl")
        audit=read(BASE/f"audit_{b+1:02d}.jsonl")
        assert len(blind)==len(audit)==20
        for original, rec, verdict in zip(source[b*20:(b+1)*20],blind,audit):
            assert rec==original
            assert verdict["id"]==rec["id"]
            assert verdict["selected_index"] in (-1,0,1,2)
            assert isinstance(verdict["issue"],str) and verdict["issue"].strip()
            idx=verdict["selected_index"]
            counts[idx]+=1
            assert idx>=0,rec["id"]
            chosen=rec["candidates"][idx]
            selected.append({"id":rec["id"],"irrelevant_e1":chosen["text"],
                             "donor_id":chosen["donor_id"],"candidate_index":idx})
    assert len(selected)==80
    OUT.write_text("".join(json.dumps(r,ensure_ascii=False)+"\n" for r in selected))
    REPORT.parent.mkdir(parents=True,exist_ok=True)
    REPORT.write_text("# G29B blind irrelevant-control audit\n\n"
        "Registered after G29 results, before any G29B model inference. "
        "Deterministic candidates are source sentences from other frozen claims, screened for zero non-stopword overlap with the target claim. "
        "Local OpenCode Longcat 2.5 Preview examined all 80 target claims and selected the first natural, decision-irrelevant sentence among three blind candidates. "
        "This is LLM-assisted review, not human gold.\n\n"
        f"- First candidate approved: {counts[0]}\n- Second candidate approved: {counts[1]}\n"
        f"- Third candidate approved: {counts[2]}\n- No candidate approved: {counts[-1]}\n"
        "- Every frozen G29 claim retained; no model-output filtering.\n")
    print("frozen 80 irrelevant controls",counts)


if __name__=="__main__":main()
