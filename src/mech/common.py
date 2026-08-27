"""Shared plumbing for the mechanism experiments.

The behavioural runs read the answer after a generated rationale, whose length
varies by condition.  Causal work needs a FIXED readout position, so mechanism
prompts end with a cue and the answer is read from the next-token distribution
at the final token.  `validate_direct_readout.py` checks how far this immediate
readout tracks the behavioural one before any of it is interpreted.
"""
import os, sys, math, json
import torch

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from schema import load_items, compile_prompt, SYSTEM, ANSWER_CUE   # noqa: E402

ROOT = os.path.join(HERE, "..", "..")
MODEL = "Qwen/Qwen3-8B"


def load_model(model=MODEL, device="cuda"):
    from transformers import AutoTokenizer, AutoModelForCausalLM
    tok = AutoTokenizer.from_pretrained(model)
    m = AutoModelForCausalLM.from_pretrained(model, dtype=torch.bfloat16,
                                             attn_implementation="eager").to(device).eval()
    return tok, m


def decoder_layers(m):
    """The list of decoder blocks. Multimodal wrappers (Gemma-3) nest the text
    model one level deeper than a plain causal LM."""
    for path in (("model", "layers"), ("model", "language_model", "layers"),
                 ("language_model", "model", "layers"), ("model", "model", "layers")):
        o = m
        try:
            for a in path:
                o = getattr(o, a)
            if hasattr(o, "__len__") and len(o) > 1:
                return o
        except AttributeError:
            continue
    raise RuntimeError("could not locate decoder layers")


def mech_prompt(tok, item, cond):
    """Decision prompt in `direct` mode, ending at a fixed answer cue."""
    user = compile_prompt(item, cond, mode="direct")
    msgs = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": user}]
    kw = dict(tokenize=False, add_generation_prompt=True)
    try:
        text = tok.apply_chat_template(msgs, enable_thinking=False, **kw)
    except TypeError:
        text = tok.apply_chat_template(msgs, **kw)
    return text + ANSWER_CUE + " "


def digit_ids(tok):
    """Token ids for the ten digits as they appear right after `ANSWER: `."""
    ids = []
    for d in range(10):
        cand = tok.encode(str(d), add_special_tokens=False)
        assert len(cand) == 1, (d, cand)
        ids.append(cand[0])
    return torch.tensor(ids)


def digit_expectation(logits, dids):
    """logits: (..., vocab) at the answer position -> score in 0-100."""
    p = torch.softmax(logits[..., dids].float(), dim=-1)
    vals = torch.arange(10, device=p.device, dtype=p.dtype)
    return (p * vals).sum(-1) * 100.0 / 9.0


def frozen_items(families=None):
    items = {i.item_id: i for i in load_items(os.path.join(ROOT, "data", "items", "items_v1.jsonl"))}
    keep = json.load(open(os.path.join(ROOT, "data", "items", "frozen_v1.json")))
    out = [items[k] for k in keep]
    if families:
        out = [i for i in out if i.task_family in families]
    return out


def span_indices(tok, prompt, needle):
    """Token index range of `needle` inside `prompt`, found by character offsets."""
    c0 = prompt.index(needle)
    c1 = c0 + len(needle)
    enc = tok(prompt, return_offsets_mapping=True, add_special_tokens=False)
    lo = hi = None
    for i, (a, b) in enumerate(enc["offset_mapping"]):
        if b <= c0 or a >= c1:
            continue
        lo = i if lo is None else lo
        hi = i + 1
    return lo, hi
