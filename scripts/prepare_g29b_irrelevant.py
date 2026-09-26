"""Mechanically nominate natural-source irrelevant E1 candidates for G29B."""

import json
import random
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "data/items/g29_selected_v1.jsonl"
OUT = ROOT / "data/items/g29b_irrelevant_candidates_v1.jsonl"
AUDIT = ROOT / "data/items/g29b_blind_irrelevance_v1"

STOP = set("the a an is was were are to of in on at by for with and or as from had has have this that its it his her their more than after before one two".split())


def words(s):
    return {w for w in re.findall(r"[a-zA-Z]+", s.casefold()) if len(w) >= 3 and w not in STOP}


def main():
    source = [json.loads(s) for s in SOURCE.read_text().splitlines() if s]
    assert len(source) == 80
    rows=[]
    for target in source:
        tw=words(target["claim"])
        options=[]
        for donor in source:
            if donor["id"] == target["id"] or donor["page"] == target["page"]:
                continue
            overlap=len(tw & words(donor["evidence_s"]))
            if overlap:
                continue
            options.append((donor["id"], donor["evidence_s"]))
        rng=random.Random("g29b-irrelevant-v1-"+target["id"])
        rng.shuffle(options)
        assert len(options)>=3,target["id"]
        rows.append({"id":target["id"],"claim":target["claim"],
                     "candidates":[{"donor_id":did,"text":txt} for did,txt in options[:3]]})
    OUT.write_text("".join(json.dumps(r,ensure_ascii=False)+"\n" for r in rows))
    AUDIT.mkdir(parents=True,exist_ok=True)
    for b in range(4):
        (AUDIT/f"blind_{b+1:02d}.jsonl").write_text("".join(
            json.dumps(r,ensure_ascii=False)+"\n" for r in rows[b*20:(b+1)*20]))
    print("80 frozen claims, 3 candidates each, four blind batches")


if __name__=="__main__":
    main()
