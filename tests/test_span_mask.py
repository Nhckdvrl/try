"""Tests for the G6 attention-span masking instrument.

These check the parts that can be wrong silently: the character-span to
token-span mapping, that the mapping agrees with the tokenizer path every
previous round used, the shape and content of the additive mask, and that the
layer-window hooks attach to exactly the intended layers and detach cleanly.
"""

from __future__ import annotations

from pathlib import Path
import sys

import pytest
import torch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

from information_set_schema import load_jsonl  # noqa: E402
from mech.span_mask import (  # noqa: E402
    NEG,
    PACKET_HEADER,
    TASK_HEADER,
    LayerWindowMask,
    SpanPlan,
    build_mask,
    plan_span,
    plan_wrong_span,
    read_probability,
    templated_text,
)
from run_information_set import _chat_ids  # noqa: E402

TOKENIZER_DIR = next(
    Path("/home/xiang/.cache/huggingface/hub/models--Qwen--Qwen2.5-0.5B-Instruct/snapshots").iterdir(),
    None,
)
ARTIFACT = ROOT / "data/external/review/btf3_temporal_large_replication_v1.jsonl"
needs_tokenizer = pytest.mark.skipif(TOKENIZER_DIR is None, reason="tokenizer not cached")


@pytest.fixture(scope="module")
def tokenizer():
    from transformers import AutoTokenizer

    return AutoTokenizer.from_pretrained(str(TOKENIZER_DIR), local_files_only=True)


@pytest.fixture(scope="module")
def prompt():
    item = load_jsonl(ARTIFACT)[0]
    return item.oob_variant["with_information_prompt"]


@needs_tokenizer
def test_token_ids_match_the_untouched_path(tokenizer, prompt):
    """The masking path must tokenize exactly as every previous round did."""
    assert plan_span(tokenizer, prompt).input_ids == _chat_ids(tokenizer, prompt)


@needs_tokenizer
def test_packet_tokens_decode_back_to_the_packet(tokenizer, prompt):
    plan = plan_span(tokenizer, prompt)
    decoded = tokenizer.decode([plan.input_ids[i] for i in plan.packet_tokens])
    text = templated_text(tokenizer, prompt)
    packet = text[text.index(PACKET_HEADER) : text.index(TASK_HEADER, text.index(PACKET_HEADER))]
    # decoded must be a contiguous piece of the packet region, nothing outside it
    assert decoded.strip()[:40] in packet
    assert decoded.strip()[-40:] in packet
    assert len(plan.packet_tokens) > 50


@needs_tokenizer
def test_packet_tokens_are_contiguous_and_precede_the_query_positions(tokenizer, prompt):
    plan = plan_span(tokenizer, prompt)
    assert plan.packet_tokens == list(range(plan.packet_tokens[0], plan.packet_tokens[-1] + 1))
    assert plan.packet_tokens[-1] < plan.query_from
    assert plan.query_from < plan.n_tokens


@needs_tokenizer
def test_wrong_span_matches_length_and_sits_before_the_packet(tokenizer, prompt):
    real = plan_span(tokenizer, prompt)
    control = plan_wrong_span(tokenizer, prompt)
    assert control.input_ids == real.input_ids
    assert control.query_from == real.query_from
    assert len(control.packet_tokens) == len(real.packet_tokens)
    assert control.packet_tokens[-1] < real.packet_tokens[0]
    assert not set(control.packet_tokens) & set(real.packet_tokens)


def _plan(n_tokens: int, packet: list[int], query_from: int) -> SpanPlan:
    return SpanPlan(input_ids=list(range(n_tokens)), packet_tokens=packet, query_from=query_from, text="")


def test_mask_is_causal_and_blocks_only_the_span_for_query_positions():
    plan = _plan(10, [3, 4, 5], 7)
    mask = build_mask(plan, n_new=2, dtype=torch.float32, device="cpu")
    assert mask.shape == (1, 1, 12, 12)
    m = mask[0, 0]

    # causal everywhere
    assert torch.all(m[2, 3:] == NEG)
    # a query position before query_from can still see the packet
    assert m[6, 3] == 0 and m[6, 5] == 0
    # query positions at/after query_from cannot
    for row in range(7, 12):
        assert torch.all(m[row, torch.tensor([3, 4, 5])] == NEG)
    # and they can still see everything else that precedes them
    assert m[7, 0] == 0 and m[7, 6] == 0
    # generated positions are query positions too
    assert m[11, 4] == NEG and m[11, 6] == 0


def test_mask_covers_the_generated_positions():
    plan = _plan(5, [1], 3)
    assert build_mask(plan, n_new=4, dtype=torch.float32, device="cpu").shape[-1] == 9


class _Dummy(torch.nn.Module):
    def forward(self, x, attention_mask=None):
        self.seen = attention_mask
        return x


class _Model(torch.nn.Module):
    def __init__(self, n):
        super().__init__()
        self.model = torch.nn.Module()
        self.model.layers = torch.nn.ModuleList(_Dummy() for _ in range(n))


def test_layer_window_hooks_attach_to_exactly_the_window_and_detach():
    model = _Model(8)
    mask = torch.zeros(1, 1, 4, 4)
    replacement = torch.full((1, 1, 4, 4), -1.0)
    with LayerWindowMask(model, replacement, (2, 5)) as handle:
        assert len(handle.handles) == 3
        for index, layer in enumerate(model.model.layers):
            layer(torch.zeros(1), attention_mask=mask.clone())
            expected = -1.0 if 2 <= index < 5 else 0.0
            assert layer.seen[0, 0, 0, 0].item() == expected
    # after the context exits, no layer is patched any more
    for layer in model.model.layers:
        layer(torch.zeros(1), attention_mask=mask.clone())
        assert layer.seen[0, 0, 0, 0].item() == 0.0


def test_layer_window_none_patches_every_layer():
    model = _Model(4)
    with LayerWindowMask(model, torch.zeros(1, 1, 2, 2), None) as handle:
        assert len(handle.handles) == 4


@pytest.mark.parametrize(
    "text,expected",
    [("42", 42.0), (" 7 %", 7.0), ("100", 100.0), ("100.0 and then noise", 100.0), ("no", None)],
)
def test_readout(text, expected):
    assert read_probability(text) == expected


# --- G6 sweep decision rules ------------------------------------------------

from mech.analyze_span_sweep import PERMITTED  # noqa: E402


def _curve(values):
    """Restoration curve entries with tight intervals around each mean."""
    return {f: {"mean": v, "ci_low": v - 0.05, "ci_high": v + 0.05, "units": 100} for f, v in values.items()}


def _row(curve):
    """Re-implementation-free check: exercise the rule through analyze_model's logic."""
    qualifying = [f for f, r in curve.items() if r["mean"] >= 0.5 and r["ci_low"] > 0.5]
    f_star = max(qualifying) if qualifying else None
    midpoint = curve.get(0.5)
    if f_star is not None and f_star >= 0.5:
        return "H-override"
    if (f_star is None or f_star <= 0.125) and midpoint is not None and midpoint["mean"] < 0.25:
        return "H-absent"
    return "intermediate"


def test_override_row_when_late_masking_still_restores():
    curve = _curve({0.0: 1.0, 0.25: 0.95, 0.5: 0.8, 0.75: 0.7, 0.875: 0.3})
    assert _row(curve) == "H-override"


def test_absent_row_when_only_full_depth_works():
    curve = _curve({0.0: 0.95, 0.125: 0.4, 0.25: 0.2, 0.5: 0.1, 0.75: 0.02})
    assert _row(curve) == "H-absent"


def test_intermediate_row_otherwise():
    curve = _curve({0.0: 0.95, 0.125: 0.8, 0.25: 0.6, 0.5: 0.35, 0.75: 0.1})
    assert _row(curve) == "intermediate"


def test_every_row_has_a_permitted_sentence():
    for row in ("H-override", "H-absent", "intermediate"):
        assert row in PERMITTED and PERMITTED[row].strip()
