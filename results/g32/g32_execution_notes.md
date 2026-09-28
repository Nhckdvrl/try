# G32 execution and reproducibility notes

The material audit, 56-item selection, task-contract prompt compiler, and frozen estimands were committed to GitHub main at `957f5f8` before full inference. A one-item smoke (36 prompt cells per checkpoint) discovered a Mistral tokenizer-regex warning; a conditional `fix_mistral_regex=True` on external prompt tokenization and its exact rationale were committed at `72f2006` **before full inference**. Smoke rows are retained in `results/raw/*_g32_construct_identification_v1_smoke.jsonl` and excluded from every reported statistic. No G32 item was selected or replaced on model behavior.

The current `fvcrc20` GPUs were occupied by another user's process, so inference ran on available `fvcrc10` GPUs 0/1/2, one checkpoint per card: Qwen3-8B, Gemma3-12B, Mistral-Small-24B respectively. The same previously used local checkpoint paths are in `scripts/run_g32_construct_identification.sh`; no model substitution was made. vLLM 0.11.0, Transformers 4.57.6, PyTorch 2.8.0+cu128, bfloat16, temperature 0, max 24 generated tokens, exact chat-template token IDs, and no thinking mode where supported. Each model completed the exact 56 × 2 contracts × 2 E polarities × 9 cells = 2016 output grid. Model stdout had ordinary Torch/Gloo shutdown warnings. Mistral's vLLM-internal decoder tokenizer still printed an incorrect-regex warning, but input prompt IDs came from the external tokenizer with `fix_mistral_regex=True`; the distinction is important and should not be silently erased.

Strict one-line `PROBABILITY:` parsing succeeded in 2016/2016 Qwen, 2016/2016 Gemma, and 2015/2016 Mistral. Mistral's single malformed line was `PROBABABILITY: 100` in `g29_127`, open-world, E+, D−. It remains a missing value in the registered complete-claim analysis. The analysis checks all row keys, item hashes, prompt hashes and exact rendered messages against the committed compiler. Claim-cluster bootstrap uses 5000 draws. No model output was re-requested or repaired.

| Raw file | SHA-256 |
|---|---|
| Qwen3-8B | `81c2c34af84a04d12f7f1994ce0da4cda85dc65f1c329f68218fbe84f2a89796` |
| Gemma3-12B | `fa5d4cb74fa44073b8c4b40d804e5ce4e0b481e32e32d7b90f1533752d855948` |
| Mistral-Small-24B | `1f014e79f4e25f5944aa80474b0924b1767cb1c0e3b4ce5ce78decdf024bc4b3` |

The machine-readable analysis is `results/g32/g32_construct_identification_v1.json`. The interpretive report is [here](g32_construct_identification_assessment.md). The registered sample is exploratory, source-overlapping, and primarily numeric. The one-item smoke output hashes are not needed for the inferential analysis but its files preserve the technical sequence.
