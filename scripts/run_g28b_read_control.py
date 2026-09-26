"""G28B irrelevant-read control matched to G28A RR histories."""

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from run_model import digit_expectation
from schema import ANSWER_CUE, SYSTEM
from run_g28a_path import first_read, load_data, second, sha


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True)
    ap.add_argument("--tag", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--gpu-frac", type=float, default=.85)
    args = ap.parse_args()
    pairs, controls = load_data(ROOT / "data/items/g24a_confb_selected_v1.jsonl")
    from transformers import AutoTokenizer
    from vllm import LLM, SamplingParams
    tok = AutoTokenizer.from_pretrained(args.model)

    def chat_ids(messages):
        full = [{"role": "system", "content": SYSTEM}] + messages
        kw = dict(tokenize=True, add_generation_prompt=True)
        try:
            enc = tok.apply_chat_template(full, enable_thinking=False, **kw)
        except TypeError:
            enc = tok.apply_chat_template(full, **kw)
        ids = enc["input_ids"] if hasattr(enc, "keys") else enc
        return list(ids[0]) if ids and isinstance(ids[0], (list, tuple)) else list(ids)

    llm = LLM(model=args.model, tensor_parallel_size=1, gpu_memory_utilization=args.gpu_frac,
              max_model_len=4096, dtype="bfloat16", max_logprobs=40,
              disable_log_stats=True, enforce_eager=True)

    rows = []
    for p in pairs:
        cid, claim = p["cfb_id"], p["claim"]
        for role, e2 in (("support", p["evidence_s"]), ("refute", p["evidence_r"])):
            messages = [{"role": "user", "content": first_read(claim, controls[cid])},
                        {"role": "assistant", "content": "Understood."},
                        {"role": "user", "content": second(e2)}]
            ids = chat_ids(messages)
            rows.append({"cfb_id": cid, "model_tag": args.tag, "stage": "final",
                         "condition": "IR", "final_role": role, "messages": messages,
                         "n_prompt_tokens": len(ids),
                         "prompt_sha256": sha(json.dumps(messages, ensure_ascii=False, sort_keys=True)),
                         "ids": ids})
    assert len(rows) == 400
    out1 = llm.generate([{"prompt_token_ids": r["ids"]} for r in rows],
                        SamplingParams(temperature=0, max_tokens=110, stop=[ANSWER_CUE]),
                        use_tqdm=False)
    for r, o in zip(rows, out1):
        r["reasoning"] = o.outputs[0].text
        r["reason_truncated"] = o.outputs[0].finish_reason != "stop"
        cue = r["reasoning"].rstrip() + "\n" + ANSWER_CUE + " "
        r["ids2"] = r["ids"] + tok(cue, add_special_tokens=False)["input_ids"]
    out2 = llm.generate([{"prompt_token_ids": r["ids2"]} for r in rows],
                        SamplingParams(temperature=0, max_tokens=1, logprobs=40),
                        use_tqdm=False)
    for r, o in zip(rows, out2):
        r["raw"] = o.outputs[0].text
        r["value"], r["mass"] = digit_expectation(o)
        del r["ids"], r["ids2"]
    path = Path(args.out)
    path.parent.mkdir(exist_ok=True, parents=True)
    path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows))
    print("wrote", len(rows), "IR rows ->", path)
    print("unparsed", sum(r["value"] is None for r in rows),
          "digit-mass<0.5", sum(r["mass"] < .5 for r in rows),
          "rationale caps", sum(r["reason_truncated"] for r in rows))


if __name__ == "__main__":
    main()
