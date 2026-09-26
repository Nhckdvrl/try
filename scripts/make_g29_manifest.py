"""Checksummed provenance map for G29 and G29B."""

import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"results/g29/g29_manifest_v1.json"
TAGS=("mistral-small-24b","qwen3-8b","gemma3-12b")


def sha(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda:f.read(1<<20),b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    paths=[
        "data/items/g29_candidate_pool_v1.jsonl",
        "data/items/g29_selected_v1.jsonl",
        "data/items/g29b_irrelevant_candidates_v1.jsonl",
        "data/items/g29b_irrelevant_selected_v1.jsonl",
        "results/discovery/g29_revocation_status_registration.md",
        "results/discovery/g29b_excluded_content_registration.md",
        "results/audits/g29_material_audit_v1.md",
        "results/audits/g29b_irrelevance_audit_v1.md",
        "results/g29/g29_revocation_analysis_v1.md",
        "results/g29/g29b_excluded_content_analysis_v1.md",
        "results/g29/g29_g29b_integrated_assessment.md",
        "figures/g29_status_content_v1.pdf",
        "figures/g29_status_content_v1.png",
    ]
    paths += [f"data/items/g29_blind_audit_v1/{name}_{b:02d}.jsonl"
              for name in ("blind","audit") for b in range(1,9)]
    paths += [f"data/items/g29b_blind_irrelevance_v1/{name}_{b:02d}.jsonl"
              for name in ("blind","audit") for b in range(1,5)]
    paths += [f"scripts/{name}" for name in (
        "prepare_g29_materials.py","freeze_g29_after_audit.py",
        "run_g29_revocation.py","run_g29_revocation.sh","analyze_g29_revocation.py",
        "prepare_g29b_irrelevant.py","freeze_g29b_irrelevant.py",
        "run_g29b_irrelevant.py","run_g29b_irrelevant.sh","analyze_g29b_irrelevant.py",
        "make_g29_manifest.py")]
    paths.append("scripts/plot_g29_status_content.py")
    paths += [f"results/raw/{tag}_{kind}.jsonl" for tag in TAGS
              for kind in ("g29_revocation_v1","g29b_irrelevant_v1")]
    paths.append("results/raw/qwen3-8b_g29_revocation_v1_smoke.jsonl")
    records={}
    for name in paths:
        p=ROOT/name
        assert p.exists(),name
        rec={"sha256":sha(p),"bytes":p.stat().st_size}
        if p.suffix==".jsonl":
            with p.open() as f:
                rec["rows"]=sum(1 for line in f if line.strip())
        records[name]=rec
    manifest={
        "base_head_before_g29": "5853aa5ca33fa3b40c292b1e17aeed775bcc02d2",
        "vitaminc_source_revision": "be6febb761b0b2807687e61e0b5282e459df2fa0",
        "vitaminc_source_sha256": {
            "train":"7461c6fd1a13459590317c5ccdc8651dd2daf7c1ad8ae4b10ccd88d164fccd5a",
            "dev":"544934677f5d133873e6d38f4557f8966f4efa5d3d70874ffe6913f2091b86b5",
            "test":"7ad1808dbc30c62e0a1427a53022d0dfaff668a1fde3c4b612a2d266edd753ad",
        },
        "gpu_host":"fvcrc10",
        "gpu_ids":[0,2,3],
        "run_environment":"/home/xiang/miniconda3/envs/verl-clean",
        "model_snapshots":{
            "mistral-small-24b":"data/mistral_small_24b_hf",
            "qwen3-8b":"b968826d9c46dd6066d109eabc6255188de91218",
            "gemma3-12b":"96b6f1eccf38110c56df3a15bffe176da04bfd80",
        },
        "files":records,
    }
    OUT.parent.mkdir(parents=True,exist_ok=True)
    OUT.write_text(json.dumps(manifest,indent=2,ensure_ascii=False)+"\n")
    print(OUT,len(records),"files")


if __name__=="__main__":main()
