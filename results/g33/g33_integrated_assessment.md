# G33：最后一次识别实验后的科学判断——关闭当前主线

2026-09-30。完整分析 200 个新 claim family × 3 个模型，43,200 个冻结 cell。**最终项目决定：整个 Unring the Bell 题按用户指示定义为“垃圾题”，彻底报废。** 范围包括 exclusion、retraction、restoration、eligibility，以及由此派生的机制、方法、agent 和 evaluation 分支。没有保留候选方向，没有下一轮实验。可靠的历史观测仍按原样保存，不能用它们为这个题换名复活。

## 我们真正尝试提升的是什么

不能再把“忽略得不错，但回不到 never-seen 判断”当作新贡献。[Self-Blinding](https://matanmazor.github.io/files/papers/christian2026blinding.pdf) 已有 blinded baseline、direct ignore、hypothetical-self 对照及恢复差异；[Hypothetical Consistency](https://arxiv.org/html/2305.14279v4) 已研究预测另一个 context 下自己的回答；[Compared to What?](https://arxiv.org/html/2605.01048) 已覆盖 counterfactual prompting 的 baseline/control 问题。新的数据、二元读出、更多控制，以及 S/R/P 命名都不能替代新的结论。

G33 因此只尝试识别更强的一步：**要求“仿佛没见过 X”是否会在局部排除 X 不更差时，因为实际 X 的存在而额外损害仍合法 E 的使用？** 若跨模型、跨问法成立，会得到一个实际决策的冲突：局部排除能力与合法依据使用不能被同一个成功分数概括。这里关键不是一般 hypothetical query 有代价，而是与 X 内容相关的额外合法依据损失。

设计独立交叉 E+/E−、X+/X−，比较直接判断 D、as-if 判断 C、fresh-self 预测 S；每个问法都有同问法 redacted frame F。Record-only 所有合法 records 明确可用且 authoritative，修复 G32 scope ambiguity。另设同材料 no-E/open-world bridge。两套冻结 wording，实际 TRUE/FALSE 决策及归一化二元概率。**不是 staged retraction：X 从首次展示就被排除，没有初次 admission 或先前模型判断。**

## 数据与完成度

[材料报告](g33_material_report.md)、[manifest](g33_material_manifest.json)、[registration](../../registrations/g33_final_identification_v1.md) 保留完整来历。来自真实 Wikipedia revision/VitaminC source family，排除历史 claim/case pool，200 个不同 claim/case/page。22,190 个机械合格 pairs → 固定种子 800 候选 → 720 完成构造和不同模型独立检查 → 347 接受额外 source-only 质疑审查 → 首 200 个全部合格 family 冻结。

OpenCode 免费 MiMo、Longcat、Muse Spark 逐条构造和检查。额外 source-only pass 必不可少：初步人工抽查发现“两所大学”“另一个最晒城市”“另一次 DNA 实验”等并不严格互斥的假 refutation。最终材料加入严格 exact-claim/scope 审查；所有 tentative、拒绝、pending、失败调用及理由保留。第三 pass 有时复用前一个 provider，不能称三个独立专家。E 是源文本，X 是忠实实验 paraphrase，不能称独立收集的真实文献。自动审查仍可能犯错，不是人工裁决 gold。

200 个独立 claim 是区间的统计单位，43,200 不是独立样本量。全矩阵通过 exact prompt/item hash、cell coverage、概率范围、实际标签一致性校验。启动、概率报告及并发写入故障及完整重跑见 [execution notes](g33_execution_notes.md)；失败混合文件整段排除，没有择优选输出。

## 关键结果

以下为百分点，95% claim-cluster bootstrap 区间；概率量不是 calibrated belief。

| 量 | Qwen3-8B | Gemma3-12B | Mistral-Small-24B |
|---|---:|---:|---:|
| Clean B accuracy | 91.12 | 93.50 | 93.75 |
| Clean E probability leverage | 81.08 | 86.88 | 82.09 |
| Direct accuracy | 83.19 | 93.50 | 90.50 |
| As-if accuracy | 80.19 | 94.12 | 91.69 |
| Direct X binary flip rate | 17.88 | 5.00 | 10.50 |
| As-if X binary flip rate | 12.12 | 2.50 | 7.62 |
| G_D：实际 X 相对同问法 frame 的准确率损失 | 5.31 | 0.00 | 4.00 |
| G_C：同上，as-if | 5.06 | −1.88 | 3.44 |
| **H = G_C−G_D** | **−0.25 [−2.44,1.88]** | **−1.88 [−3.38,−0.38]** | **−0.56 [−1.88,0.75]** |
| H，wording 1 | 0.00 | −3.12 | −1.38 |
| H，wording 2 | −0.50 | −0.62 | 0.25 |

全部三个模型满足 substrate 可用标准；不是任务整体做不出来。全部三个模型的 as-if X 概率敏感性及实际 X flip rate 都比 direct 小。然而没有所需的额外合法依据损失。候选推进条件 **0/3**；primary H 的三个区间上界均低于预设有实质意义的 +5 点。这不等于逐 item 没有差异或证明精确等价。

**最容易被误读的是 Qwen。** As-if 的正确率比 direct 低 3.00 点，X flip rate 却低 5.75 点，乍看像理想的“排除更好但有效信息使用受损”。但没有 X 内容的 FD accuracy 是 88.50，FC 是 85.25，已经相差 3.25 点。分解为：

`accuracy(D) − accuracy(C) = accuracy(FD) − accuracy(FC) + H = 3.25 − 0.25 = 3.00`。

因此该表面 tradeoff 没有识别出 X 导致的 collateral legal-ground cost；问法/frame 的差异已足以解释它。不能把它升级为 eligibility mechanism、一般 judgment-rule law，或继续为它造新名词。Gemma、Mistral 方向也不同：as-if 减少 X 泄漏且实际合法决策略改善。Gemma 的负 H 不是改写成新的 universal protection law 的理由。

S 的 secondary H_S−D 为 Qwen −1.69 [−3.56,0.12]、Gemma −0.88 [−2.06,0.31]、Mistral +1.38 [0.06,2.75]。Mistral 的小幅显著增加如实保留；它不是跨模型构念分离，也不能作为事后 rescue。S 对 E gold 的 utility 与预测 clean B 的 fidelity 不是同一个指标，完整分析同时报告后者的实际 label flips。

## 旧现象没有消失，但没有成为新贡献

No-E bridge 的 D restoration probability error 是 Qwen 30.45、Gemma 31.81、Mistral 11.74。Gemma 的 active X absolute sensitivity 为 90.55，excluded D 为 5.81，同时 restoration error 31.81：局部抑制与 same-item 恢复仍可明显不同。Qwen 的 no-E residual X effect 本身很大，不能声称它已经做到干净 non-use。

这支持继续把 ConfB 当作可靠资产，**不提供一条新母结论**。新的读出不能与 ConfB rating 数字直接拼接；no-E bridge 同时改变了 E availability 和 task contract，不能宣布“record-only 成功、open-world 失败”已经识别 judgment-rule boundary，更不能宣称“合法证据恢复失忆能力”。要证明这种 law 还需要新问题与能独立识别的对照；当前结果没有给出值得继续投资的依据。

## 为什么在这里终止

先前失败的 prospective leakage、negative-evidence stickiness、meta-evidence 主解释、revocation-specific overcorrection、universal preservation failure 都不复活。旧 G18 是 claim 太 trivial 而被淘汰，干净复现也不改变这点。Old Stage-5 的 late suppression、patching 等资产不能解释一个尚未成立的新 behavioral object。

当前留下的是：一项与强 prior 紧邻的可靠 suppression–restoration gap，若干 frame/context/model-dependent differences，以及一些被后续实验否掉的漂亮解释。G33 已认真尝试让它升格为“局部排除与有效决策冲突”的可识别结论，结果没有支持。继续追加模型、自然材料、Preservation benchmark、mechanism 或 restoration LoRA，主要会增加工程和测量深度，尚无理由认为会增加所要求的 idea novelty。

**科学判断是这轮没有建立值得继续投资的独立新贡献；用户最终决定是整个 Unring the Bell 题永久废弃，分类为“垃圾题”。** 不改写成 CRE benchmark，不转机制、LoRA、agent 或其他包装，不开启 G34，不保留同题候选分支。保留源码、冻结数据、真实结果及失败史，只作为档案；历史投入和已有资产不构成继续研究的理由。

完整统计见 [registered summaries](g33_registered_summaries.md) 和 [machine-readable analysis](g33_analysis.json)。整个题的终止范围与归档规则见 [永久废弃索引](../../archive/abandoned_unring_the_bell_2026_09_30/README.md)。分类是研究题的最终投入决策，不篡改任何历史实验的数值、有效性或 provenance。
