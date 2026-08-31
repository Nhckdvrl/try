"""Attention-span masking on the frozen BTF-3 prompts.

Tooling for the mechanism phase and for the enforcement method it motivates.
Given a prompt and the character span of the out-of-set packet, this module

* maps that character span to token indices under the model's own chat
  template, verifying the mapping against the untouched tokenizer path;
* builds an additive attention mask that forbids chosen query positions from
  attending to those packet columns;
* applies that mask either to every layer or to a layer window, via forward
  pre-hooks that substitute the mask the decoder layer receives;
* greedily decodes the short numeric answer under the mask.

The point of masking rather than deleting: deletion changes the prompt, so the
model can no longer be asked about the packet at all. Masking leaves the text in
context — the model still answers the boundary probe about it — while removing
its causal path into the decision. That is exactly the contract the project
measures, ``memory(E)`` retained and ``causal_effect(E -> decision)`` removed,
which is why the method is stated this way and not as "drop the packet".

Nothing here re-authors a prompt: prompts come from the frozen artifact.
"""
from __future__ import annotations

from dataclasses import dataclass
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "src"))

import torch  # noqa: E402

from run_information_set import SYSTEM_PROMPT, parse_probability  # noqa: E402

PACKET_HEADER = "\n\nLATER RESOLUTION PACKET\n"
TASK_HEADER = "\n\nTASK\n"
NEG = torch.finfo(torch.float32).min


@dataclass
class SpanPlan:
    """Token-level plan for one masked forward pass."""

    input_ids: list[int]
    packet_tokens: list[int]
    query_from: int
    text: str

    @property
    def n_tokens(self) -> int:
        return len(self.input_ids)


def templated_text(tokenizer, prompt: str, system: str = SYSTEM_PROMPT) -> str:
    messages = [{"role": "system", "content": system}, {"role": "user", "content": prompt}]
    try:
        return tokenizer.apply_chat_template(
            messages, tokenize=False, add_generation_prompt=True, enable_thinking=False
        )
    except TypeError:
        return tokenizer.apply_chat_template(messages, tokenize=False, add_generation_prompt=True)


def plan_span(tokenizer, prompt: str, *, query_from: str = "task") -> SpanPlan:
    """Locate the packet's tokens and the first query position that is masked.

    ``query_from='task'`` masks only positions from the TASK header onward — the
    positions that actually compose the answer — leaving earlier positions free
    to read the packet. ``query_from='packet'`` masks every position after the
    packet.
    """
    text = templated_text(tokenizer, prompt)
    if PACKET_HEADER not in text:
        raise ValueError("prompt has no LATER RESOLUTION PACKET section")
    packet_start = text.index(PACKET_HEADER)
    packet_end = text.index(TASK_HEADER, packet_start)

    encoded = tokenizer(text, add_special_tokens=False, return_offsets_mapping=True)
    ids = list(encoded["input_ids"])
    offsets = list(encoded["offset_mapping"])

    packet_tokens = [
        index
        for index, (start, end) in enumerate(offsets)
        if start >= packet_start and end <= packet_end and end > start
    ]
    if not packet_tokens:
        raise ValueError("packet span mapped to zero tokens")

    boundary = packet_end if query_from == "task" else packet_end
    if query_from == "packet":
        boundary = packet_start + len(PACKET_HEADER)
    first_query = next(
        (index for index, (start, _) in enumerate(offsets) if start >= boundary), len(ids) - 1
    )
    return SpanPlan(input_ids=ids, packet_tokens=packet_tokens, query_from=first_query, text=text)


def plan_wrong_span(tokenizer, prompt: str) -> SpanPlan:
    """Control plan: block the same number of tokens, taken from before the packet.

    The control span is the run of tokens immediately preceding the packet
    header, matched in length to the packet's token count. It is background
    text the model is licensed to use, so blocking it is a test of whether the
    method is selective: enforcement should need the packet span specifically,
    not merely the removal of some equally long region.
    """
    real = plan_span(tokenizer, prompt)
    first_packet = real.packet_tokens[0]
    n = len(real.packet_tokens)
    start = max(0, first_packet - n)
    control = list(range(start, first_packet))
    if not control:
        raise ValueError("no control span available before the packet")
    return SpanPlan(
        input_ids=real.input_ids,
        packet_tokens=control,
        query_from=real.query_from,
        text=real.text,
    )


def build_mask(plan: SpanPlan, *, n_new: int, dtype, device) -> torch.Tensor:
    """Causal mask of shape (1, 1, T, T) with the packet columns blocked.

    ``n_new`` extends the mask to cover the tokens that will be generated; the
    generated positions are treated as query positions and are also blocked, so
    the whole answer is produced without reading the packet.
    """
    total = plan.n_tokens + n_new
    mask = torch.full((total, total), NEG, dtype=torch.float32, device=device)
    mask = torch.triu(mask, diagonal=1)  # causal
    blocked = torch.tensor(plan.packet_tokens, device=device, dtype=torch.long)
    mask[plan.query_from :, blocked] = NEG
    return mask.to(dtype)[None, None]


def _layers(model):
    for attribute in ("model.layers", "model.language_model.layers", "transformer.h"):
        node = model
        try:
            for part in attribute.split("."):
                node = getattr(node, part)
            return node
        except AttributeError:
            continue
    raise AttributeError("could not locate decoder layers on this architecture")


class LayerWindowMask:
    """Substitute the attention mask only inside a layer window.

    Registered as forward pre-hooks on the decoder layers. Outside the window
    each layer keeps whatever mask the model built for it, so a window result is
    never confounded with a different masking implementation.
    """

    def __init__(self, model, mask: torch.Tensor, window: tuple[int, int] | None):
        self.handles = []
        layers = _layers(model)
        lo, hi = window if window is not None else (0, len(layers))
        for index, layer in enumerate(layers):
            if lo <= index < hi:
                self.handles.append(
                    layer.register_forward_pre_hook(self._make(mask), with_kwargs=True)
                )

    @staticmethod
    def _make(mask):
        def hook(module, args, kwargs):
            if "attention_mask" in kwargs and kwargs["attention_mask"] is not None:
                current = kwargs["attention_mask"]
                q, kv = current.shape[-2], current.shape[-1]
                # With a KV cache the layer sees only the last q query rows of a
                # kv-long prefix, so the rows to substitute are [kv - q, kv) --
                # which reduces to [0, kv) when there is no cache.
                kwargs["attention_mask"] = mask[..., kv - q : kv, :kv].to(current.dtype)
            return args, kwargs

        return hook

    def __enter__(self):
        return self

    def __exit__(self, *exc):
        for handle in self.handles:
            handle.remove()
        self.handles.clear()
        return False


@torch.no_grad()
def generate_masked(
    model,
    tokenizer,
    plan: SpanPlan,
    *,
    max_new_tokens: int = 8,
    window: tuple[int, int] | None = None,
    apply_mask: bool = True,
) -> str:
    """Greedy decode under the span mask (or without it, when apply_mask=False).

    Uses a KV cache: the prompt is processed once and each further token is a
    one-row query against the cached prefix. The mask slice handed to the model
    is the row block ``[kv - q, kv)``, which is the whole causal mask on the
    first step and the single new row afterwards.
    """
    device = next(model.parameters()).device
    dtype = next(model.parameters()).dtype
    ids = torch.tensor([plan.input_ids], device=device)
    mask = build_mask(plan, n_new=max_new_tokens, dtype=dtype, device=device) if apply_mask else None

    produced: list[int] = []
    cache = None
    step_input = ids
    seen = 0
    for _ in range(max_new_tokens):
        q = step_input.shape[1]
        kv = seen + q
        kwargs = {"use_cache": True}
        if cache is not None:
            kwargs["past_key_values"] = cache
        if mask is not None:
            sliced = mask[:, :, kv - q : kv, :kv]
            if window is None:
                kwargs["attention_mask"] = sliced
                out = model(step_input, **kwargs)
            else:
                with LayerWindowMask(model, mask, window):
                    out = model(step_input, **kwargs)
        else:
            out = model(step_input, **kwargs)
        cache = out.past_key_values
        seen = kv
        token = out.logits[0, -1, :].argmax().item()
        produced.append(token)
        if tokenizer.eos_token_id is not None and token == tokenizer.eos_token_id:
            break
        step_input = torch.tensor([[token]], device=device)
    return tokenizer.decode(produced, skip_special_tokens=True)


def read_probability(text: str) -> float | None:
    """The frozen strict readout, tolerant only of trailing generation."""
    match = re.match(r"\s*(100(?:\.0+)?|\d{1,2}(?:\.\d+)?)\s*%?", text)
    if not match:
        return None
    value = float(match.group(1))
    return value if 0.0 <= value <= 100.0 else None


__all__ = [
    "LayerWindowMask",
    "SpanPlan",
    "build_mask",
    "generate_masked",
    "plan_span",
    "plan_wrong_span",
    "read_probability",
    "templated_text",
]
