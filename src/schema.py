"""Item schema + deterministic prompt compiler.

An `Item` is a *structured* description of one latent decision problem.  All five
experimental conditions are compiled from it deterministically, so that the only
thing that differs between conditions is (a) whether the exclusion/admission rule
is present and (b) where it sits relative to the critical evidence.  Nothing is
ever re-written by an LLM.
"""
from dataclasses import dataclass, field, asdict
from typing import Optional
import json

CONDITIONS = ["base", "admit_pre", "admit_post", "exclude_pre", "exclude_post"]
PROBES = ["rule_probe_exclude_pre", "rule_probe_exclude_post",
          "rule_probe_admit_post", "memory_probe_exclude_post"]


@dataclass
class Item:
    item_id: str
    task_family: str
    surface_domain: str
    base_context: str
    critical_evidence: str          # rendered as a standalone context block
    critical_label: str             # short referring expression, e.g. "the recorded phone call"
    critical_direction: str         # "increase" | "decrease"  (effect on Y when admitted)
    exclusion_reason: str           # epistemic_invalidation | procedural_illegality |
                                    # access_control | temporal_irrelevance
    evidence_truth: str             # "true_but_forbidden" | "false_or_unreliable"
    admit_rule: str
    exclude_rule: str
    question: str
    output_spec: str                # instruction for the parseable answer
    memory_question: str
    rule_probe_question: str
    ground_truth: Optional[float] = None   # only for the verifiable families
    meta: dict = field(default_factory=dict)

    def to_json(self):
        return json.dumps(asdict(self), ensure_ascii=False)


SYSTEM = ("You are a careful decision maker. Follow every instruction in the "
          "context exactly. Answer with the requested format and nothing else.")

_SEP = "\n\n"


def _blocks(item: Item, cond: str):
    """Ordered list of context blocks for one condition."""
    B = ("BACKGROUND\n" + item.base_context)
    E = ("ADDITIONAL INFORMATION\n" + item.critical_evidence)
    Radm = ("RULING\n" + item.admit_rule)
    Rexc = ("RULING\n" + item.exclude_rule)
    if cond == "base":
        return [B]
    if cond == "admit_pre":
        return [B, Radm, E]
    if cond == "admit_post":
        return [B, E, Radm]
    if cond == "exclude_pre":
        return [B, Rexc, E]
    if cond == "exclude_post":
        return [B, E, Rexc]
    raise ValueError(cond)


ANSWER_FORMATS = {
    # One-token readout. Cheap, but a pilot showed a model can reason its way to one
    # answer and emit the opposite digit when forced to answer immediately, so this is
    # kept only for the mechanism experiments.
    "direct": "Output only the answer and nothing else.",
    # Primary readout: a short, greedily decoded rationale, then the answer is read off
    # the next-token distribution at a fixed position.
    "reasoned": ("Think in at most two short sentences. Then write a final line of exactly "
                 "this form:\nANSWER: <your answer>"),
}
ANSWER_CUE = "ANSWER:"


def compile_prompt(item: Item, cond: str, mode: str = "reasoned") -> str:
    """Decision prompt. Contains ONLY the final judgment question."""
    blocks = _blocks(item, cond)
    return (_SEP.join(blocks) + _SEP + "TASK\n" + item.question + "\n" + item.output_spec
            + "\n" + ANSWER_FORMATS[mode])


def compile_probe(item: Item, probe: str) -> str:
    """Probe prompts are always issued as *separate* calls so that they cannot
    act as an extra reminder inside a decision run (README section 3.1)."""
    if probe == "rule_probe_exclude_pre":
        blocks = _blocks(item, "exclude_pre")
        q = item.rule_probe_question
    elif probe == "rule_probe_exclude_post":
        blocks = _blocks(item, "exclude_post")
        q = item.rule_probe_question
    elif probe == "rule_probe_admit_post":
        blocks = _blocks(item, "admit_post")
        q = item.rule_probe_question
    elif probe == "memory_probe_exclude_post":
        blocks = _blocks(item, "exclude_post")
        q = item.memory_question
    else:
        raise ValueError(probe)
    return _SEP.join(blocks) + _SEP + "TASK\n" + q


def load_items(path):
    out = []
    with open(path) as f:
        for line in f:
            line = line.strip()
            if line:
                out.append(Item(**json.loads(line)))
    return out
