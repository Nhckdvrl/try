# G26A Phase-A pool — build report (v1)

- date: 2026-09-24 (zero-model build)
- items: `data/items/g26_phasea_pool_v1.jsonl` n=3640 sha256=`ad0ac715a609f49f9ad98af5cf6a3022a1b1e6f904d7a1f22ae2d490a7e2c95c`
- order: frozen HoVer train file order (O4/O9)
- audit: results/audits/hover_structural_v1.json sha256=`7723e8ef5ef6b01e` — 23/23 field assertions OK
- funnel train: candidates 6153 -> materialized 6082 -> oriented 3782 -> survivors 3642 (pin 3642)
- labels: {'train/NOT_SUPPORTED': 1136, 'train/SUPPORTED': 2506, 'dev/SUPPORTED': 195, 'dev/NOT_SUPPORTED': 268}
- clusters train: 2320 title-pair / 2339 hpqa
- orientation: reversed survivors train 69 / dev 3 / pooled 72 (prereg §2 cites 75)
- fillers: bank 68 sentences / 816 words; max rule->judgment distance spread per tokenizer: {'admit_gemma3-12b': 10, 'admit_llama31-8b': 10, 'admit_qwen3-8b': 10, 'admit_qwen35-9b': 9, 'excl_gemma3-12b': 10, 'excl_llama31-8b': 10, 'excl_qwen3-8b': 10, 'excl_qwen35-9b': 9} (limit 10)
- feasibility gate: structural census 3642 -> feasible N_A = 3640, excluded 2 (tokenizer-geometry, zero-model, outcome-blind): ['3dbe1a3e-b448-4dc0-b1d6-2e3a2ada88bc', '4b84c748-0cf2-4981-b526-bab6e8759040']
- id disjointness from G0/G23/G24/G25 pools: OK
