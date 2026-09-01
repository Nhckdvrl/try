"""Run G12 paired redacted YES/NO donor conditions."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import subprocess

try:
    from .information_set_schema import file_sha256, load_jsonl
    from .adapters.btf3_donor_outcome import assignment_digest, build_donor_pairs
    from .adapters.btf3_packet_swap import PAIRING_SEED
    from .run_information_set import SYSTEM_PROMPT, _chat_ids, boundary_probe, parse_probability, parse_yesno
except ImportError:
    from information_set_schema import file_sha256, load_jsonl
    from adapters.btf3_donor_outcome import assignment_digest, build_donor_pairs
    from adapters.btf3_packet_swap import PAIRING_SEED
    from run_information_set import SYSTEM_PROMPT, _chat_ids, boundary_probe, parse_probability, parse_yesno


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--artifact", type=Path, default=Path("data/external/review/btf3_temporal_large_replication_v1.jsonl"))
    p.add_argument("--model", required=True); p.add_argument("--model-id", required=True)
    p.add_argument("--model-revision", required=True); p.add_argument("--tag", required=True)
    p.add_argument("--out", type=Path, required=True)
    p.add_argument("--gpu-frac", type=float, default=0.85); p.add_argument("--max-model-len", type=int, default=8192)
    p.add_argument("--max-num-seqs", type=int, default=0); p.add_argument("--enforce-eager", action="store_true")
    p.add_argument("--tokenizer-mode", choices=("auto", "hf", "slow", "mistral"), default="auto")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()

    from transformers import AutoTokenizer
    if not args.dry_run:
        from vllm import LLM, SamplingParams
        try:
            from transformers.tokenization_mistral_common import MistralCommonBackend
            if not hasattr(MistralCommonBackend, "is_fast"):
                MistralCommonBackend.is_fast = False
        except ImportError:
            pass
    items = load_jsonl(args.artifact)
    pairs = build_donor_pairs(items)
    digest = assignment_digest(pairs)
    tok = AutoTokenizer.from_pretrained(args.model, local_files_only=True)
    records = []
    for pair in pairs:
        for outcome in ("yes", "no"):
            e = pair[outcome]; prompt = e["prompt"]
            records.append({
                "record_type":"decision", "independent_unit_id":pair["independent_unit_id"],
                "condition":f"redacted_donor_{outcome}", "donor_unit_id":e["donor_unit_id"],
                "donor_outcome":outcome.upper(), "recipient_direction":pair["recipient_direction"],
                "verdict_sentences_removed":e["verdict_sentences_removed"],
                "clauses_preserved":e["clauses_preserved"],
                "prompt_sha256":hashlib.sha256(prompt.encode()).hexdigest(), "prompt_ids":_chat_ids(tok,prompt),
            })
            probe = boundary_probe(prompt, expected="NO")
            records.append({
                "record_type":"boundary_probe", "independent_unit_id":pair["independent_unit_id"],
                "condition":f"boundary_redacted_donor_{outcome}", "donor_unit_id":e["donor_unit_id"],
                "donor_outcome":outcome.upper(), "expected":"NO",
                "prompt_sha256":hashlib.sha256(probe.encode()).hexdigest(), "prompt_ids":_chat_ids(tok,probe),
            })
    longest=max(len(r["prompt_ids"]) for r in records)
    audit={"units":len(items),"prompts":len(records),"longest_prompt_tokens":longest,
           "assignment_sha256":digest,"seed":PAIRING_SEED,
           "removed_sentences":sum(pair[o]["verdict_sentences_removed"] for pair in pairs for o in ("yes","no")),
           "unchanged_packets":sum(pair[o]["verdict_sentences_removed"]==0 for pair in pairs for o in ("yes","no"))}
    if longest+8>args.max_model_len: raise ValueError("prompt exceeds max_model_len")
    if args.dry_run: print(json.dumps(audit,indent=2)); return 0
    llm=LLM(model=args.model,gpu_memory_utilization=args.gpu_frac,max_model_len=args.max_model_len,
            dtype="bfloat16",disable_log_stats=True,enforce_eager=args.enforce_eager,
            tokenizer_mode=args.tokenizer_mode,**({"max_num_seqs":args.max_num_seqs} if args.max_num_seqs else {}))
    outputs=llm.generate([{"prompt_token_ids":r["prompt_ids"]} for r in records],
                         SamplingParams(temperature=0.0,max_tokens=8,seed=0))
    args.out.parent.mkdir(parents=True,exist_ok=True)
    with args.out.open("w",encoding="utf-8") as h:
        h.write(json.dumps({"record_type":"metadata","artifact":str(args.artifact),
            "artifact_sha256":file_sha256(args.artifact),"git_commit":subprocess.check_output(["git","rev-parse","HEAD"],text=True).strip(),
            "assignment_sha256":digest,"model_id":args.model_id,"model_revision":args.model_revision,
            "model_path":args.model,"model_tag":args.tag,"system_prompt":SYSTEM_PROMPT,"audit":audit},ensure_ascii=False)+"\n")
        for record,output in zip(records,outputs,strict=True):
            raw=output.outputs[0].text; result={k:v for k,v in record.items() if k!="prompt_ids"}; result["raw"]=raw
            if record["record_type"]=="decision": result["value"]=parse_probability(raw)
            else:
                result["answer"]=parse_yesno(raw); result["correct"]=result["answer"]==record["expected"]
            result["model_tag"]=args.tag; h.write(json.dumps(result,ensure_ascii=False)+"\n")
    print(json.dumps(audit)); return 0

if __name__=="__main__": raise SystemExit(main())

