# Paper outline — prospective semantic exclusion

**Updated:** 2026-09-23.

## Working title

> **Can Language Models Commit to Ignore Future Evidence?**

---

## 1. Introduction

Natural setup: policies often precede the information they govern.

RQ:
> Can an LLM commit now to make future evidence causally irrelevant?

Contributions:
1. broad prospective-vs-retrospective exclusion reversal;
2. controls separating enforcement from policy access;
3. preregistered zero-instruction amplification;
4. causal target-conditioned policy-state mechanism, conditional on G23C.

---

## 2. G0 — broad phenomenon

Figure 1:
- Pre Exclude vs Post Exclude;
- matched Admit control;
- breadth across models and task families.

Main result:
prospective exclusion is systematically weaker.

---

## 3. Why this is not ordinary instruction forgetting

Compact control section:
- delay;
- wording;
- policy probes;
- arithmetic prospective zero;
- Admit.

Claim:
policy access is not sufficient for causal enforcement.

---

## 4. G23A — complete exclusion is structurally special

Main figure:
`Gap(w)` over `w={0,1,25,50,100}`.

Report:
- `Gap(0)=+13.86 [+8.54,+19.18]`;
- mean attenuation gap `+5.03 [+3.16,+6.83]`;
- `Δ_zero=+8.83 [+4.39,+13.33]`;
- 3/3 model deltas positive;
- `Gap(100)` near zero.

Claim:
generic prospective timing cost + extra zero-instruction penalty.

---

## 5. Failed factorization attempt — G23B

Brief methods/result, probably appendix or compact main-text paragraph.

Frozen Phase-A result:
`ProfferLeak=+8.07 [+4.86,+11.23]`.

Purpose:
show why exact semantic knowledge vs evidence-state presence cannot be cleanly separated
with the tested natural-language carrier.

Do not present as a main contribution.

---

## 6. Stage 5 — target availability changes rule-time causal state

Matched chronology:
```text
unrelated preview -> zero rule -> evidence
matched preview   -> zero rule -> evidence
```

Two-model causal replication:
- Qwen3-8B mid layers;
- Mistral-Small-24B mid layers.

Main point:
state is formed before later evidence is processed and is causally necessary for
successful suppression.

---

## 7. G23C — does the state carry policy value?

2×2:
- matched/unrelated target preview;
- zero/full policy.

Primary intervention:
bidirectional 0↔100 rule-end state interchange at frozen L14.

Primary estimands:
- `PolicyTransfer_M`;
- `PolicyTransfer_U`;
- `TargetConditioning = PolicyTransfer_M - PolicyTransfer_U`.

Desired mechanistic law:
> policy value becomes causally exchangeable when the semantic target is available
> during rule processing.

---

## 8. Related work

Four clean buckets:
1. instruction position / forgetting;
2. belief revision;
3. in-context unlearning / edit reversal;
4. contextualization race conditions + latent task/function states.

Keep the distinction:
knowledge availability / belief truth / instruction recency are not the same as causal
eligibility of evidence.

---

## 9. Discussion

Implication:
natural-language policy may not behave as an abstract future constraint simply because
the model can state it.

Limitations:
- controlled decisions rather than deployed agents;
- G23C mechanism scope limited to models whose direct readout reproduces the bridge;
- no claim of a reusable universal policy vector;
- no clean behavioral proof of standing gate vs retrospective cancellation.

---

## 10. Conclusion

One sentence:

> **LLMs can know a future evidence policy without reliably making that future evidence
> causally inert; complete exclusion shows an extra prospective timing cost, and the
> successful control state depends on target availability during policy processing.**
