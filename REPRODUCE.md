# 废弃题的归档核验说明

整个 Unring the Bell 题已永久废弃。此页只用于检查已有档案，不授权启动新 inference、材料构造或延伸研究。原 reproduction guide 原文见[快照](archive/abandoned_unring_the_bell_2026_09_30/snapshots/REPRODUCE.md.txt)；其中生成实验的命令是历史记录。

## G33 最终结果

- 冻结材料：[selected.jsonl](data/items/g33_final/selected.jsonl)，200 families；SHA256 `66bf60f5fe7a2fba12c698fb0adcabe4b8d93882be7f610b886fe045127e6e8c`。
- 最终原始结果仅为 `results/raw/{qwen3-8b,gemma3-12b,mistral-small-24b}_g33_final_v1.jsonl`，每个 14,400 cell。
- [analysis JSON](results/g33/g33_analysis.json)保存最终 raw SHA256、完整统计和候选判断。[execution notes](results/g33/g33_execution_notes.md)保存每次执行修复及来源。
- `*_tail_failed_concurrent.jsonl` 整段排除；smoke 和重复保存的成功 tail 不计入分析。不可对所有 raw 文件作 glob 后混合统计。
- 只重算已有分析：`/home/xiang/miniconda3/envs/verl-clean/bin/python scripts/analyze_g33_final.py`。此命令检查完整 cell、冻结 prompt/material hashes、概率及实际标签，再重算 10,000 次 claim-cluster bootstrap；不加载模型或调用 API。
- 分片 merge 已完成，最终 canonical 文件是 14,400 行，**不要再次直接运行 merge**；那个历史工具要求独立 7,200 行 head/tail 输入。

## 其他历史记录

[归档资产地图](archive/abandoned_unring_the_bell_2026_09_30/README.md)索引 ConfA/ConfB、G28–G32、旧 mechanism/Stage-5、注册和材料审查。原文件路径保留，以维持脚本与 provenance 链；它们均不是活跃研究方向。
