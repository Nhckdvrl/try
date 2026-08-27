# Stage 4A — the same failure in an agent

Real chat roles: `SYSTEM` carries a persistent policy about a document that has
not been retrieved yet, the document arrives in a `TOOL` message, the assistant
then answers. The policy varies in how much of the target it specifies, and the
retrieved document varies in whether it matches the policy in proposition and in
identifier. REI is anchored on `ag_base` (document not retrieved) and
`ag_padmit_same_d7` (retrieved and endorsed). 75 items, legal + inference.

| condition | Qwen3-8B | Gemma-3-12B | Phi-4-mini |
|---|---|---|---|
| no policy at all (naive) | +0.991 | +0.839 | +1.038 |
| **system policy names D7 only** | **+1.014** | +0.386 | **+0.940** |
| system policy names D7 + a gist of it | +0.870 | +0.751 | +1.064 |
| **system policy names D7 + its full proposition** | **+0.602** | +0.454 | **+0.753** |
| **same policy delivered AFTER the tool output** | **+0.380** | **+0.191** | **−0.156** |
| ID-only policy, D7 arrives paraphrased | +0.666 | +0.317 | +0.324 |
| proposition policy, D7 arrives paraphrased | +0.720 | +0.372 | +0.810 |
| ID-only policy, D7 carries a *different* proposition | +0.910 | +0.445 | +1.050 |
| proposition policy, D7 carries a *different* proposition | +1.008 | +0.572 | +0.979 |
| **ID-only policy, same proposition arrives as D9** | **+0.906** | **+0.851** | **+0.849** |
| **proposition policy, same proposition arrives as D9** | **+0.678** | **+0.424** | **+0.712** |

Four things carry over from the vignette setting, and one is new.

**A system-level identifier policy can do nothing at all.** In Qwen3-8B and
Phi-4-mini, `Document D7 must not influence any answer in this session` placed in
the system message leaves the document's influence exactly where it was with no
policy (+1.014 vs +0.991; +0.940 vs +1.038). This is the highest-authority,
persistent instruction the interface offers, given before retrieval, and it is
worth nothing. Gemma-3-12B is the exception (+0.386 against +0.839).

**The temporal reversal transfers.** Delivering the identical policy after the
tool output rather than in the system message is better in all three models, by a
lot: +0.380 vs +1.014, +0.191 vs +0.386, −0.156 vs +0.940.

**Putting the proposition in the policy helps** in two of three (+0.602 vs +1.014;
+0.753 vs +0.940), and a gist does not (+0.870, +1.064). Gemma again differs, its
ID-only policy already being its better one.

**Suppression follows the proposition, not the identifier.** The last two rows are
the agent version of the Stage-3D 2×2. When the same content arrives under a
*different* identifier, D9, an identifier-only policy is helpless (+0.906, +0.851,
+0.849 — near the naive level in all three) but a policy that stated the
proposition still suppresses it (+0.678, +0.424, +0.712), even though D9 is not
the document the policy names. Conversely, a document carrying the policy's
identifier but a different proposition leaks in every model and under both policy
types.

**What is new here** is the practical shape of the failure. A deployed policy of
the form "document X must not influence the answer", written before retrieval, is
the natural way to express an information-flow constraint in an agent, and it is
the form that fails. What works is either stating the content the policy is about
— which requires knowing it in advance, defeating the purpose — or re-asserting
the policy after the documents arrive.
