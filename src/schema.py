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
import conditions_g17 as g17
import conditions_g18 as g18
import conditions_g23a as g23a
import conditions_g23b as g23b
import conditions_g24a as g24a
import conditions_g24p1 as g24p1
import conditions_g24p3 as g24p3
import conditions_g24p4 as g24p4
import conditions_g24meta as g24meta
import conditions_g25 as g25
import conditions_g26a as g26
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
G17_CONDITIONS = g17.G17_CONDITIONS
G18_CONDITIONS = g18.G18_CONDITIONS

# G23A: weighting vs categorical gating, on fresh items (g23a_v1.jsonl)
G23A_CONDITIONS = g23a.G23A_CONDITIONS

# G23B: standing gate vs retrospective cancellation, fresh legal items
# (g23b_v1.jsonl); 4 carrier cells + 3 rule cells, no probes
G23B_CONDITIONS = g23b.G23B_CONDITIONS

# G25A: near-zero sweep over G24A natural materials (g25_v1.jsonl; 16 cells,
# dispatch on condition name — see conditions_g25)
G25A_CONDITIONS = g25.G25A_CONDITIONS

# G26A: load-bearing ruling test over fresh HoVer pool (g26_phasea_pool_v1.jsonl;
# 10 cells = 4 no-rule carriers + 2 rule arms x 3 timings — see
# conditions_g26a; prereg G26A §3, O3 amendment "11 -> 10")
G26A_CONDITIONS = g26.G26A_CONDITIONS

# Pilot P1: two new post-admit retraction operators over G24A-family items
# (g24a_p1_v1.jsonl; dispatch on condition name — see conditions_g24p1)
G24P1_CONDITIONS = g24p1.G24P1_CONDITIONS

# Pilot P3: operator-only control, evidence content never rendered
# (g24a_p3_v1.jsonl; dispatch on condition name — see conditions_g24p3;
# registration §11)
G24P3_CONDITIONS = g24p3.G24P3_CONDITIONS
# Pilot P4 irrelevant-visible cells (g24a_p4_v1.jsonl; dispatch on condition
# name — see conditions_g24p4; registration §12).
G24P4_CONDITIONS = g24p4.G24P4_CONDITIONS
# §14 RQ3 explanation experiment: second-order retraction operators
# (meta_neutral_post / random_reason_post; dispatch on condition name — see
# conditions_g24meta; registration §14).
G24META_CONDITIONS = g24meta.G24META_CONDITIONS

# Stage 4A agentic system -> tool -> answer
AGENT_CONDITIONS = ag.CONDITIONS

# external held-out materials
EXT_CONDITIONS = ext.EXT_RAMSEY_CONDITIONS
PROBES = (["rule_probe_exclude_pre", "rule_probe_exclude_post",
           "rule_probe_admit_post", "memory_probe_exclude_post",
           "wprobe_pre", "wprobe_post"]
          + g23a.G23A_PROBES + g25.G25A_PROBES + g26.G26A_PROBES)


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
    # G25A near-zero sweep: dispatch on the condition name FIRST — the sweep
    # runs over G24A-family items but owns its own 16 cells (prereg G25A §3);
    # every existing condition name misses this branch, so all other item
    # files keep their current prompts bit-for-bit.
    if g25.is_g25(cond):
        return g25.blocks(item, cond)
    # G26A load-bearing ruling cells: own item pool (g26_phasea_pool_v1.jsonl) and
    # own 10 cells — dispatch on the condition name first (prereg G26A §3);
    # no existing condition name collides, so every other item file keeps
    # its prompts bit-for-bit.
    if g26.is_g26(cond):
        return g26.blocks(item, cond)
    # Pilot P1 retraction operators: dispatch on the condition name FIRST —
    # the pilot runs over G24A-family items (same CLAIM / EVIDENCE E /
    # RULING layout) but owns its two new post-admit cells; every existing
    # condition name misses this branch, so every other item file keeps its
    # prompts bit-for-bit.  base / admit_post / exclude_post fall through to
    # the G24A branch below and stay character-identical to G24A.
    if g24p1.is_g24p1(cond):
        return g24p1.blocks(item, cond)
    # Pilot P3 operator-only control: dispatch on the condition name FIRST —
    # the four frame-only cells run over the same g24a_vitaminc items (no
    # arms; the withheld block reads a module constant, never the item's
    # evidence).  Every existing condition name misses this branch, so every
    # other item file keeps its prompts bit-for-bit; `base` falls through to
    # the G24A branch below and is byte-identical to P2's Base by
    # construction (registration §11).
    if g24p3.is_g24p3(cond):
        return g24p3.blocks(item, cond)
    # Pilot P4 irrelevant-visible control: dispatch on the condition name
    # FIRST — the two cells run over the same g24a_vitaminc items but render
    # a screened decision-irrelevant EVIDENCE E (item.critical_evidence,
    # filled by the build script per registration §12's frozen material rule).
    # Every existing condition name misses this branch, so every other item
    # file keeps its prompts bit-for-bit (registration §12).
    if g24p4.is_g24p4(cond):
        return g24p4.blocks(item, cond)
    # §14 second-order retraction operators: dispatch on the condition name
    # FIRST — the two cells run over the same g24a_* items (CLAIM / EVIDENCE E
    # / RULING layout); every existing condition name misses this branch, so
    # every other item file keeps its prompts bit-for-bit (registration §14).
    if g24meta.is_g24meta(cond):
        return g24meta.blocks(item, cond)
    # G24A natural-evidence items re-render the five standard conditions over
    # CLAIM / EVIDENCE E blocks; dispatch on task_family so every existing
    # item file keeps its current prompts bit-for-bit (prereg G24A §3, §9.3).
    if g24a.is_g24a(item):
        return g24a.blocks(item, cond)
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
    if cond in g23a.G23A_CONDITIONS:
        return g23a.blocks(item, cond, B, E)
    if cond in g23b.G23B_CONDITIONS:
        return g23b.blocks(item, cond, B, E)
    if cond in g18.G18_CONDITIONS:
        return g18.blocks(item, cond, B, E)
    if cond in g17.G17_CONDITIONS:
        return g17.blocks(item, cond, B, E)
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
    elif probe.startswith("wprobe_g23a_"):
        # wprobe_g23a_<arm>_<wkey> — the model states the weight it was asked for
        _, _, arm, wkey = probe.split("_")
        blocks = _blocks(item, f"g23a_{arm}_{wkey}")
        q = v3.WEIGHT_PROBE_Q.format(lab=item.critical_label)
    elif probe.startswith("rule_probe_g23a_"):
        # rule_probe_g23a_<wkey>_<arm> — may the evidence influence the judgment?
        *_, wkey, arm = probe.split("_")
        blocks = _blocks(item, f"g23a_{arm}_{wkey}")
        q = item.rule_probe_question
    elif probe.startswith("wprobe_g25_"):
        # wprobe_g25_<arm>_<wkey> — G23A-style requested-weight-access probe,
        # pre arm only at w000/w100 (G25A O3); same question text as G23A
        _, _, arm, wkey = probe.split("_")
        blocks = _blocks(item, f"g25_{arm}_{wkey}")
        q = v3.WEIGHT_PROBE_Q.format(lab=item.critical_label)
    elif probe in g26.G26A_PROBES:
        # G26A legibility probes, layout pinned to own rule type's T0 cell
        # (one probe per rule type per item per model — §0 amendment c)
        arm = "excl" if probe.endswith("excl") else "admit"
        blocks = _blocks(item, f"g26_{arm}_t0")
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
