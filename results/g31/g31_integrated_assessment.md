# G31: joint S/R/P pilot — complete, but no clean three-way dissociation

Date: 2026-09-27. Read the [pre-inference registration](../discovery/g31_srp_joint_registration.md), [material audit](../audits/g31_material_audit_v1.md), [complete metric table](g31_srp_joint_analysis_v1.md), [execution record](g31_execution_notes.md), and [checksummed manifest](g31_manifest_v1.json). The material and audit were frozen and pushed as `ce256f9` before the first successful model output. This is an exploratory experiment on 60 **reused G29** claims and natural source-evidence pairs, with 60 locally constructed and separately blind-audited temporary-note triplets. It is not a fresh independent confirmation.

## Question and design

The same claim receives both support and refute valid evidence E2, crossed with support and refute old notes X. The old note is either still admissible (**A**) or explicitly excluded from first exposure (**N**). An excluded irrelevant note (**I**) measures some history/frame cost; direct E2 (**D**) gives the no-X comparator. Each item has independent 0–100 probability and TRUE/FALSE prompts. Three models produced all 4,320 expected rows with zero parse failures; the analyzer reconstructs every message and verifies its prompt and selected-item SHA-256. Qwen3-8B and Gemma-3-12B ran as planned. A native NCCL query of this host's failed GPU 1 prevented Mistral-Small-24B from starting in tensor parallel mode even with P2P disabled, so the registered compatibility clause was used to substitute Llama-3.1-8B. No Mistral G31 response exists.

## What the crossed design finds

| Criterion, pooled over 60 paired claims and 3 models | Observed result | Interpretation |
|---|---:|---|
| Signed X separation, active A → excluded N | +14.32 → −4.80 | A mean-only score would suggest strong suppression, but N reverses rather than simply approaching zero. |
| Mean item-wise absolute X effect, A → N | 25.56 → 15.78; paired reduction 9.78 [3.94, 15.67] | Direct X sensitivity is reduced only partially; excluded X still changes many individual judgments. |
| Absolute N−D judgment error | 17.27 [13.68, 21.14] | Same final admissible evidence does not yield the direct-E2 output. |
| Absolute I−D error | 12.73 [9.18, 16.58] | A large part of that deviation also occurs with an excluded **irrelevant** note. |
| Paired excess absolute error, N−D over I−D | 4.54 [1.59, 7.72] | Incremental relevant-note cost is modest and most apparent in Llama; it is an exploratory derived contrast. |
| E2 leverage, D / I / N averaged over X polarities | 62.99 / 52.26 / 50.73 | Valid-evidence uptake is lower under both excluded-note frames. |
| Absolute E2-leverage error, D−I / N−I | 24.30 / 25.68 | Relevant excluded X does not establish a reliably larger **incremental** preservation loss than generic excluded context. |
| Paired excess leverage error, N−I over D−I | 1.38 [−5.59, 8.54] | The stronger semantic-specific preservation claim is unsupported here. |

The pooled X-polarity × E2 interaction in N is +7.09 [−2.92, 17.04]; its CI spans zero. Binary X-polarity disagreement falls from 24.7% in A to 16.7% in N, still far from full invariance. N/D decisions differ in 16.7% of matched cells; N/I decisions differ in 13.1%. These are item-wise differences, not a common signed decision shift.

Model differences matter. Qwen and Gemma have N signed X separation close to zero (−1.92 and −1.40), yet their absolute N X effects remain 12.07 and 10.87. Llama shows a **reversed** N signed separation of −11.07 and absolute N X effect of 24.41. N−D absolute error is 14.75, 13.27, and 23.80 for Qwen, Gemma, and Llama; the corresponding I−D errors are 12.97, 9.48, and 15.72. Thus pooling does not describe one uniform computation.

## Research decision

G31 demonstrates why the proposed suppression/restoration/preservation measurements must be made jointly and **item-wise**. It does **not** establish the hoped-for strong statement that a model first suppresses excluded X almost completely and then specifically corrupts valid E2 uptake. X was only weakly active compared with E2, exclusion retained substantial item-wise X sensitivity, and the irrelevant-note frame already accounts for much of both restoration and leverage error. Calling the smaller signed X mean “successful selective removal” would repeat the cancellation error seen in ConfA.

The robust ConfB suppression–restoration gap remains the paper's established center. G31 weakens a proposed general preservation finding while clarifying how to test it. The next high-value behavioral test, if pursued, should make the active X manipulation stronger and comparable to E2 **before** testing exclusion, use natural or transparently constructed X/E2 with independent item audit, and include a genuinely matched context-length/frame baseline. Another generic D/N/I/R benchmark without this balance would not resolve the current ambiguity. G31 supplies a complete negative boundary rather than a new headline.

The crossed prompts are real multi-turn chat messages but include a fixed assistant acknowledgement; they do not establish a persistent hidden-state operation. D is deliberately shorter than I/N, and I has different semantics from N. Therefore neither N−D nor N−I alone identifies a specific internal mechanism. The temporary X notes are experimental constructions, not source quotations, and the audit is LLM-assisted rather than human gold. All candidate/audit/selected files and all raw outputs remain available for inspection.
