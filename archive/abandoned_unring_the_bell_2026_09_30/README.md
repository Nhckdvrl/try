# 垃圾题档案：整个 Unring the Bell 题永久废弃

**最终决定：2026-09-30，用户明确将整个 Unring the Bell 题定义为“垃圾题”，彻底报废。** 不是只淘汰 G33、某个实验、某个 prompt 或当前 framing。Prospective/retrospective exclusion、retraction、suppression–restoration、selective evidence control、S/R/P、eligibility/final-set，以及从本题延伸的机制、方法、evaluation 和 agent 路线全部终止。**活跃分支为零，下一步实验为空。** [机器可读决定](decision.json)。

历史中的“lead”“active”“next”“paper center”全部失效。不得通过换名、换数据集、增加模型、mechanism、LoRA、agent 或 benchmark 包装复活本题。只有用户明确撤销整题废弃决定才可重新启动；档案存在本身不构成授权。

## 终止依据与最终实验

[最终 G33 科学判断](../../results/g33/g33_integrated_assessment.md)记录这轮实际完成的最后尝试。200 新自然 claim families，三模型，43,200 唯一 cell；材料经逐条构造、不同模型独立检查和额外 source-only 质疑审查。模型能够基本使用合法 records，但“as-if 排除会因 X 内容而额外损害仍合法依据”的主交互为 −0.25、−1.88、−0.56 点，候选条件 0/3。Qwen 表面 suppression/accuracy tradeoff 已被无内容问法 frame 差异解释，不能升级为新机制或规律。

原有 suppression–restoration gap 的母结论已接近 Self-Blinding；其他失败或模型特异结果不能被统一改写为新 law。当前缺乏独立 novelty 与值得继续投入的叙事。用户据此终止**整题**。分类针对研究题和投入决策；原实验的真实数值、失败确认、探索身份和 provenance 如实保存。

## 资产地图

保留原数据/结果/代码路径，避免破坏注册、分析脚本、材料与 raw 的对应关系。归档是终止状态与完整索引，不是把材料散搬到新目录后丢失引用。

| 档案 | 入口与内容 | 归档身份 |
|---|---|---|
| 最后 G33 | [综合判断](../../results/g33/g33_integrated_assessment.md)、[完整统计](../../results/g33/g33_registered_summaries.md)、[JSON/校验](../../results/g33/g33_analysis.json)、[逐 item 交互](../../results/g33/g33_item_metrics.jsonl) | 已完成；不推进 |
| G33 冻结材料 | [200 selected](../../data/items/g33_final/selected.jsonl)、[材料报告](../../results/g33/g33_material_report.md)、[manifest](../../results/g33/g33_material_manifest.json)、[注册](../../registrations/g33_final_identification_v1.md) | 新材料；LLM-assisted 审查，保留全部候选与拒绝 |
| G33 执行记录 | [execution notes](../../results/g33/g33_execution_notes.md)、[保留 prefix hashes](../../results/g33/g33_preserved_prefixes.json)、[并发失败记录](../../results/g33/g33_concurrent_write_failure.json)、`logs/g33_*` | 基础设施失败与修复；不当作模型行为 |
| 最终 raw | `results/raw/{qwen3-8b,gemma3-12b,mistral-small-24b}_g33_final_v1.jsonl` | 仅这三个最终文件进入 G33 分析，共 43,200 cell |
| G33 非分析 raw | `*_g33_final_v1_smoke*`、成功 tail/recovery、`*_tail_failed_concurrent.jsonl` | smoke、重复保存或整段失败文件；不得混入样本 |
| ConfB | [held-out 分析](../../results/g24a/g24a_confb_analysis_v1.md)、[restoration 控制](../../results/audits/g24a_confb_restoration_controls_v1.md)、[材料复审](../../results/audits/g24a_confb_reaudit/reaudit_summary.md) | 可靠历史观测；不再是活跃 paper center |
| ConfA | [原分析](../../results/g24a/g24a_confa_analysis_v1.md)、[post-hoc 复分析](../../results/g24a/g24a_confa_final_set_reanalysis_v1.md) | prospective headline 失败；post-hoc 不改写为确认 |
| G28 / G29 | [G28 综合](../../results/g28a/g28a_g28b_integrated_assessment.md)、[G29/G29B 综合](../../results/g29/g29_g29b_integrated_assessment.md) | exploration 与后续否定/边界；不再保留 path lead |
| G30 / G31 | [G30 综合](../../results/g30/g30_integrated_assessment.md)、[factorial 诊断](../../results/g30/g30_factorial_diagnostic_v1.md)、[G31 综合](../../results/g31/g31_integrated_assessment.md) | 模型特异/未支持 general preservation；不继续机制或 P benchmark |
| G32 | [construct pilot](../../results/g32/g32_construct_identification_assessment.md) | query/frame observation，scope ambiguity；不是三能力分离 |
| 文献与科学诊断 | [9/27 audit](../../results/audits/research_audit_2026_09_27.md)、[9/28 literature](../../results/audits/literature_diagnosis_2026_09_28.md)、[9/30 reassessment](../../results/audits/project_reassessment_2026_09_30.md) | 保留当时论证；所有继续推进建议均已失效 |
| 完整实验史 | [EXPERIMENTS](../../EXPERIMENTS.md)、[RESEARCH_HISTORY](../../RESEARCH_HISTORY.md)、[原 preregistrations](../../preregistrations/README.md) | 原冻结与失败史，不能救回已死 headline |
| 旧 Stage-5 / G18 / G23C / G24B 等 | [stages](../../stages/README.md)、[旧根目录档案](../legacy_root_docs_2026_09_27/README.md)、`results/mech/`、原注册及 Git history | 全部历史资产；G18 trivial claim 不复活，不作为自动 mechanism 起点 |

## 快照、清单与核验

- `snapshots/*.txt` 是归档前七个入口文档的逐字原文，包括当时仍残留的 active/next 建议。采用 `.txt` 防止把旧相对链接当作当前导航。
- [snapshot_manifest.json](snapshot_manifest.json)保存原路径、快照路径、SHA256 和归档前 Git HEAD。
- `tracked_asset_inventory.json` 保存归档提交前已暂存资产的 Git blob identities；它描述已保存的 Git 资产，不是外部模型权重备份，也不声称包含所有本地未跟踪临时文件。
- [核验说明](../../REPRODUCE.md)只分析已有材料与结果；不授权重新生成实验。
- 外部原始语料与大型模型权重按已有 pinned source/checkpoint 元数据重建，不纳入 Git。原有无关本地改动和未跟踪历史临时日志保持原样。

Git history、原 registrations、raw 输出及 material audits 不删除、不重写。历史资产只用于核查这个失败题究竟发生了什么；没有待执行任务或保留的研究对策。
