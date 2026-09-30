# 当前项目重新判断：有可靠资产，尚无成立的主线贡献

日期：2026-09-30。针对 HEAD `122704193872025c07c37022b642e955e28693af`，重新核对 G32 的实际 compiler、registration、结果，ConfB compiler，G29/G31 对照，以及 Self-Blinding 正文 §3.2、Figure 3 和 Appendix A。本轮没有启动新 inference。本文件更新研究判断，保留所有历史设计、数据与结果。

## 直接判断

项目目前积累了可靠的现象和有价值的否证，但还没有找到相对于最近 prior 足够新的中心结论。应从“等待下一轮升格的 mainline candidate”退回“需要重新选择研究贡献的 search lead”。这不是统计结果归零，也不意味着原始问题不重要；它意味着现有证据没有给继续扩大实验规模提供足够的科学理由。不能再用“一个新边界也许能出现”作为默认推进依据。

最稳的是 ConfB：在固定实验流程下，证据极性效应大幅缩小，而同模型同 claim 的 clean-context 回答没有恢复。它是可靠的行为资产。Self-Blinding 已有相近的核心对照，而且 **已经同时测过 direct ignore 与 counterfactual self-prediction，后者相对 blinded baseline 的误差更大**。因此不只 S/R 的口号被 prior 占有；“两种问法可能反映不同能力”也不能单独作为我们的新贡献。G32 的 matched redacted frames 和交叉 E/X 是更细的识别设计，但设计更细不自动等于认识更新。

## 项目为何越来越不像同一个项目

过去被拒绝的是不同东西：ConfA 没支持旧的统一 prospective signed effect；G18 的旧 headline 因 triviality 降级；ConfB 现象稳定但 novelty 被强 prior 限制；G29/G30/G31 没支持几个更强的解释。将它们统一叙述为“现象反复不存在”不准确。更严重的问题是每次解释失败后，研究对象也一起移动：从指令时序，到负证据，到撤销元信息，到后续反向增强，到 preservation，再到 hypothetical self。实验看似围绕同一个 X，实际目标输出、有效信息、排除操作和判断任务发生了变化。

这些研究有局部信息价值，却没有逐步逼近一个共同的可预测结构。一个反例迫使解释收窄是正常科研；每次收窄后立刻为剩余差异赋予一个新的 paper-level 名称，会产生“总有下一轮关键实验”的错觉。Outcome-robust 的问题要求不同结果都改变一个重要认识；它不保证每种结果都能重开一条可发表路线。

## G32 真正增加的认识与限制

G32 是一次合理的诊断探索，并非失败的确认实验。Qwen open-world 的 F_S−F_D=+13.36 确实发生在 X 内容不存在时；hypothetical 查询的误差高于直接判断，合法 E 的平均作用也被改变。因此不能把所有 restoration 分数都归因于 X 内容的继续使用。Gemma/Mistral 没有同样大的偏移，说明这是有边界的结果。Direct X effect 仍非零，E 的 itemwise leverage 也有变化，所以它没有证明“真实 selective non-use 已经良好，而只有 self-simulation 坏掉”。

三种所谓构念还没有完整分离。Q=F_S−F_D 是查询处理的行为对照；不能凭它区分 hypothetical 自我预测能力、任务语用、默认答案改变等解释。“judgment-rule shift”又可能是前两种条件下的过程描述，并非独立的第三种能力。G32 当前证明了输出差异的某些来源，尚未证明三个可独立测量的潜在能力，更未证明现有实践因此得出了错误的模型/干预排序。

代码还暴露一个须明确的 scope 歧义：record_only contract 写着 `using only the ADMISSIBLE RECORD`，E 是唯一以这个 header 标记的记录；A 格却另称 `The temporary note is admissible along with record E.` 读者可能按前者排除 X，也可能按后者扩展允许集合。故 record-only 的 active-X 数值不能被视为无歧义 task contract 下的纯校准分母。这不影响 open-world 的 F_S/F_D 对照，也不使整个 G32 无效，但它削弱了 record-only 抑制程度的解释。后续若重新使用该设计，先明确允许的记录集合。历史 prompt 与结果不作改写。

此外，44/56 claims 为数值/阈值材料，输出多靠近 0/100，41/56 已用于 G31，X 是构造便条。可验证的独立因子赋值并不等于两个独立的自然证据来源。这些事实约束外推，不能只靠更大的 n 修复。

## 撤回上次默认推荐的下一主线

上次以 Mistral 的 ConfB 大 restoration error 和 G32 小 error 为由，优先推荐“先允许、后撤销”的资格历史对照。这个差异同时混合了材料、有效 E、问法、读出与会话格式；没有资格将其归于某一项。尤其 ConfB 的 CF compiler 只是 `CLAIM → EVIDENCE E → CF RULING` 在一次 rendered prompt 内出现：**没有先呈现 ADMIT_RULE，没有实际先行依据 X 的模型决策，也没有持续状态更新**。称它为已确认的“先采用信息后撤销失败”超过了实验。

G29 已经在更明确的 initially-admissible/never-admissible histories 上测过 R/N；它没有支持预期的统一 signed 撤销特异效应。该结果不证明 R 与 N 等价，也不否决所有 query×history 交互，但新研究必须利用这项约束。一个 G32 同材料的时序桥接可以做技术性归因，**不能默认成为有较高 paper ceiling 的 scientific route**。我撤回“现在应自动执行该实验”的优先判断。

## 现在能够负责任地作出的研究决策

ConfB 可保留为 replication/extension 资产，G32 保留为构念诊断，G29–G31保留为否证与边界，旧机制工作保留为技术资产。S/R/P 是可用的测量词汇，但不是已建立的新理论。这些内容不应被硬串成几十轮实验共同支持同一个发现。

目前没有足够证据选择机制、方法、agent 包装、更多模型或新的 preservation benchmark 为主线。也没有理由承诺“已有 core 其实够强，只差 targeted extension”。以我们要求的问题选择标准，我目前无法从已有结果提出一个同时 **非平凡、区别于 strongest prior、被现有证据支持** 的中心新句子。承认这一点，比再为一个小模型差异拟定标题更有价值。

原始自然问题仍值得：信息仍可读、可记时，模型能否按当前决定的使用权限选择依据？但自然重要的问题不自动是未被研究的新问题。重新投入实验前，候选贡献必须指出此前哪项重要推断缺失、什么结果会改变它，并明确哪些已有结果已经限制它。这个判断可以来自 idea、机制、视角、研究对象、研究策略或方法；无需给类别排优先级。若没有这样的候选对象，停止扩张这条主线是合理的研究投资选择；不能把历史投入当作继续投入的证据。

近邻 primary sources：[Self-Blinding 正文](https://matanmazor.github.io/files/papers/christian2026blinding.pdf)，[Hypothetical Consistency](https://arxiv.org/html/2305.14279v4)。它们限制创新主张；它们没有证明所有 evidence-eligibility 研究空间都已封闭。
