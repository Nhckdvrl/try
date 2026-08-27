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
import conditions_v2 as v2
import conditions_v3 as v3
import conditions_v4 as v4
import routing_blocks as rt
import conditions_v5 as v5
import linear_blocks as lb
import conditions_v6 as v6
import conditions_v7 as v7
import conditions_agent as ag
import external_blocks as ext

CONDITIONS = ["base", "admit_pre", "admit_post", "exclude_pre", "exclude_post"]

# Stage-1 follow-ups: mechanism probes at the prompt level, plus the two
# structural mitigations from the plan (context sanitation, evidence ledger).
EXTRA_CONDITIONS = [
    "exclude_pre_repeat",     # B -> R -> E -> R : is Pre failure just rule distance?
    "admit_pre_repeat",       # matched order control for the above
    "exclude_post_reencode",  # B -> E -> R -> [E restated as excluded]
    "sanitation",             # B only, with the excluded item removed from the record
    "ledger",                 # explicit [ADMISSIBLE] / [EXCLUDED] ledger
]

# Stage-2 families (see conditions_v2): rule-position factorial, ID binding,
# requested-weight sweep.
V2_CONDITIONS = v2.ALL_V2

# Stage-3A families (see conditions_v3)
V3_CONDITIONS = v3.ALL_V3
V3_PROBES = v3.WEIGHT_PROBES

# Ruling paraphrases
V4_CONDITIONS = v4.PP_CONDITIONS

# Stage-3B: prospective selective routing over a stream of tagged evidence
ROUTING_CONDITIONS = rt.ROUTING_CONDITIONS

# Stage-3C adversarial tests
V5_CONDITIONS = v5.ALL_V5

# P0-2 verifiable linear weighting task (separate item file)
LINEAR_CONDITIONS = lb.LINEAR_CONDITIONS

# P0.5 semantic addressability
V6_CONDITIONS = v6.ALL_V6

# Stage 3E duplicate control + proposition relation matrix
V7_CONDITIONS = v7.ALL_V7

# Stage 4A agentic system -> tool -> answer
AGENT_CONDITIONS = ag.CONDITIONS

# external held-out materials
EXT_CONDITIONS = ext.EXT_RAMSEY_CONDITIONS
PROBES = ["rule_probe_exclude_pre", "rule_probe_exclude_post",
          "rule_probe_admit_post", "memory_probe_exclude_post",
          "wprobe_pre", "wprobe_post"]


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
    if cond == "exclude_pre_repeat":
        return [B, Rexc, E, Rexc]
    if cond == "admit_pre_repeat":
        return [B, Radm, E, Radm]
    if cond == "exclude_post_reencode":
        return [B, E, Rexc,
                ("EXCLUDED ITEM — RESTATED\n" + item.critical_evidence
                 + "\nThis item is excluded. It must not be used in your answer.")]
    if cond == "sanitation":
        # the excluded item is simply not in the record the decision is made from
        return [B, ("RECORD NOTE\nOne item of information was ruled inadmissible and has been "
                    "removed from this record. It is not available to you.")]
    if cond in ext.EXT_RAMSEY_CONDITIONS and item.task_family == "ext_ramsey":
        return ext.ramsey_blocks(item, cond)
    if cond in v7.ALL_V7:
        return v7.blocks(item, cond, B)
    if cond in v6.ALL_V6:
        return v6.blocks(item, cond, B)
    if cond in lb.LINEAR_CONDITIONS:
        return lb.blocks(item, cond)
    if cond in v5.ALL_V5:
        ID_B = "BACKGROUND\n" + item.base_context + "\n" + v2.ID_PREAMBLE
        return v5.blocks(item, cond, B, E, ID_B)
    if cond in rt.ROUTING_CONDITIONS:
        return rt.blocks(item, cond)
    if cond in v4.PP_CONDITIONS:
        return v4.blocks(item, cond, B, E)
    if cond in v3.ALL_V3:
        ID_B = "BACKGROUND\n" + item.base_context + "\n" + v2.ID_PREAMBLE
        ID_E = "EVIDENCE E7\n" + item.critical_evidence
        return v3.blocks(item, cond, B, E, ID_B, ID_E, v2.ID_ADMIT)
    if cond in v2.POSITION_CONDITIONS:
        return v2.position_blocks(item, B, E, Radm, Rexc, cond)
    if cond in v2.IDBIND_CONDITIONS:
        return v2.idbind_blocks(item, cond)
    if cond in v2.WEIGHT_CONDITIONS:
        return v2.weight_blocks(item, B, E, cond)
    if cond == "ledger":
        return [("EVIDENCE LEDGER\n\n[ADMISSIBLE]\n" + item.base_context
                 + "\n\n[EXCLUDED — must not be used]\n" + item.critical_evidence
                 + "\nReason: " + item.exclude_rule)]
    raise ValueError(cond)


ANSWER_FORMATS = {
    # One-token readout. Cheap, but a pilot showed a model can reason its way to one
    # answer and emit the opposite digit when forced to answer immediately, so this is
    # kept only for the mechanism experiments.
    "direct": "Output only the answer and nothing else.",
    # Same fixed readout position as `direct`, but with the answer cue written into
    # the prompt so that a causal LM and a masked diffusion LM can be read at the
    # identical position.
    "cued": "Reply with the answer only, in exactly this form:\nANSWER: <your answer>",
    # Primary readout: a short, greedily decoded rationale, then the answer is read off
    # the next-token distribution at a fixed position.
    "reasoned": ("Think in at most two short sentences. Then write a final line of exactly "
                 "this form:\nANSWER: <your answer>"),
}
ANSWER_CUE = "ANSWER:"


def rule_char_offset(item: Item, cond: str, mode: str = "reasoned"):
    """Character index at which the RULING block starts, so the runner can record
    how far the rule sits from the answer in tokens."""
    p = compile_prompt(item, cond, mode)
    i = p.rfind("\nRULING\n")
    return None if i < 0 else i + 1


def compile_prompt(item: Item, cond: str, mode: str = "reasoned") -> str:
    """Decision prompt. Contains ONLY the final judgment question."""
    blocks = _blocks(item, cond)
    tail = ANSWER_FORMATS[mode]
    if cond in v5.SC_CONDITIONS + v5.OP_CONDITIONS:
        # the model must first write the policy state it will act on
        tail = v5.SC_TWOLINE if not cond.startswith("sc_a") else ANSWER_FORMATS["reasoned"]
    return (_SEP.join(blocks) + _SEP + "TASK\n" + item.question + "\n" + item.output_spec
            + "\n" + tail)


def compile_messages(item: Item, cond: str, mode: str = "reasoned"):
    """Multi-role message list for the agent conditions. The answer format is
    appended to the last user-side turn so the readout position is unchanged."""
    msgs = ag.messages(item, cond, SYSTEM)
    msgs[1]["content"] += "\n" + ANSWER_FORMATS[mode]
    return msgs


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
    elif probe in v3.WEIGHT_PROBES:
        arm = probe.split("_")[1]
        blocks = _blocks(item, f"nz0000_{arm}")
        q = v3.WEIGHT_PROBE_Q.format(lab=item.critical_label)
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
