# Research diagnosis at 3ae666e — 2026-09-28

本诊断基于 main HEAD `3ae666e235583dccf51ad595db737a71d1b8eacc` 的研究记录、关键分析、prompt/compiler、load-bearing raw 检查和外部论文正文。没有启动模型 inference、训练或 GPU 实验。新计算全部是既有 ConfB 的 exploratory/post-hoc 重分析；没有修改历史 registration 或把失败 confirmation 改写为成功。

配套材料：

- `literature_diagnosis_2026_09_28.md`：prior 的实际干预、对照、贡献边界与阅读限制。
- `confb_joint_diagnosis_20260928.json`：新分析结果、输入 hash、bootstrap 和 raw 核验。
- [analyze_confb_joint_diagnosis_20260928.py](../../scripts/analyze_confb_joint_diagnosis_20260928.py)：可复算程序。

## 先给判断

这个项目有一个可靠、值得保留的经验事实，但不能再把“suppression 不等于 restoration”本身当作尚无人提出的 paper-level idea。最接近的竞争者不只是 unlearning 的一般理念，而是 Christian & Mazor 的 [Self-Blinding](https://arxiv.org/abs/2601.14553)：其具体实验已经有减少受禁止属性的作用，却没有恢复同一情境 blinded 判断的对照。

这不判死项目。它改变了需要完成的 intellectual step：从“发现 gap”转向说明这个 gap 揭示了什么此前没有识别的计算、评估错误或能力区别。Idea、视角、研究对象、识别设计、机制、规律和方法都可能完成这一步；没有规定必须是机制或方法。

我目前优先追问：**当模型不再跟随被排除证据的方向时，它究竟改变了判断过程的哪一部分？**

这个问题还不能直接当论文标题。它的价值在于把几个会导致相似分数的对象区分开：改变证据权重、改变默认判断/任务理解、不能预测自己的反事实回答，以及损害剩余理由的作用。如果没有形成新区别或新解释，只剩“context changes answers”，应该停止这条扩张。

特别纠正 G18：它的旧 headline 被放下，关键不是数据不可靠，而是“更具体地告诉模型要忽略什么，更容易忽略”过于理所当然。未被 falsify 不是重启理由。G18 不进入本次推荐主线；source/proposition scope 也不会因为换了抽象词就自动升级。

## Evidence ledger：什么站住了，什么没有

| 证据 | Provenance / 支持的实际结论 | 不支持什么 |
|---|---|---|
| ConfB，fresh 200 pairs × 6 models × 7 cells | 强 held-out evidence：signed polarity separation 62.95→8.33，同时同 item center restoration MAE 29.96，arm MAE 30.88 | 不是 86.8% 的所有因果影响消失；不是 30 点都由被撤销内容的语义造成；没有识别内部不可逆性 |
| ConfB W/I controls | 同样撤销 framing、无可用内容时 W error 21.03；无关内容 I error 25.82；CF center excess over I 4.14，CI 排除零 | 不能据此把 30 点拆成“25.82 framing + 4.14 semantic”的因果份额；也不能说 CF 与 I 近似相同 |
| ConfB material audit | post-hoc 最严格 142 subset：admit 67.83、CF 9.36、restoration 30.09；明显不是少数坏 pair 的产物 | LLM-assisted audit 不是独立人工 gold；subset robustness 不是新的 confirmation |
| ConfA，fresh 500 × 6 | 原 preregistered prospective signed effect −0.15，CI 跨零；旧 universal prospective-leak headline 失败 | post-hoc absolute movement 19.50 不能救活 signed headline；AdmitPre 自身 movement 17.06，不能把所有偏移叫 excluded-semantics contamination |
| §14 MNR / random-reason discovery | 改写撤销理由不修复 absolute restoration；MNR 增加 residual polarity separation | 不支持 meta-evidence 是主因或这类解释是有效修复；也没证明所有元信息作用严格为零 |
| G28，复用 ConfB items | 在 particular opposed-evidence histories 中看到 reverse enhancement；有 judged/read-history 差别 | X 与 E2 极性反向锁定，不能独立识别有效 E2 sensitivity，更不能说明 revocation-specific effect |
| G29，fresh 80 × 3 | R−N 没有稳定预期 signed effect；abs R−N 约 5.08，binary disagreement 6.2% | CI 跨零不是 R=N 的 equivalence 证明，但足以放弃 universal revocation-specific overcorrection headline |
| G29B，post-hoc 同 80 items 的 I 扩展 | natural opposed-evidence setting 有 N−I graded signal，跨模型不一致 | 不是跨任务、跨模型的通用反向增强规律 |
| G30，40 controlled cases × 3 | N−I 无统一 signed 增强；Gemma 的 R 有 prior/complement response regime、reliability sensitivity collapse | pooled R−N +6.38 不是共享 retraction law；也不能据此把全部模型归为 Bayes subtraction failure |
| G31，60 reused claims × 3、全交叉 X/E2 | signed cancellation 再现；abs X influence 25.56→15.78；N−D error 17.27，I−D 12.73 | semantic-specific incremental preservation contrast 1.38 [−5.59,8.54] 不支持一般 P failure；N 是 never-admissible，不是已证实的撤销专属机制 |
| G18 | semantic targeting 的 effect 本身有 prospective confirmation；其 preview 也已经提供实质证据 | 旧 headline trivial；不能声称非证据性的 target knowledge 已足够；不能因为实验干净就恢复为中心 |
| Stage 5 / G23C / G24B | 特定模型/任务下 policy/target-conditioned activation transfer 有因果作用；有可复用的固定干预与对照技术 | 没有解释 ConfB restoration；没有证明通用 eligibility operator；失败的 shared steering 不能写成通用控制向量 |

另外两个很重要的边界：

1. ConfB 是一个包含 evidence 和 ruling 的 rendered prompt，再生成 rationale 并在固定位置读取答案；不是先让模型作出一次判断、再撤销、再观察持久神经状态。它可以研究上下文内 counterfactual control，不能直接证明已经形成的内部 belief state 无法逆转。
2. Y0 是同模型 clean-context 行为，不是规范性 truth oracle。恢复 fidelity、正确性、决策效用是不同目标；即使 Y0 错，也可能准确测到 fidelity failure。

## 本次新计算改变了哪些判断

所有 8,400 个 CSV 值已逐一与 18 个 frozen raw 文件核对；不存在重复/缺失 cells。每个 bootstrap 单位为 claim，六个模型一起移动，5,000 次；CI 不把六个模型当成六个随机抽取的总体样本。

### 1. 87% 是 signed suppression，不是全部 itemwise influence

对每个 model×claim 先取绝对值：

| Quantity | Estimate |
|---|---:|
| mean \|A+−A−\| | 65.79 |
| mean \|CF+−CF−\| | 18.04 [16.50,19.60] |
| absolute-contrast reduction | 72.6% [69.9%,75.0%] |
| CF 两臂均处在 Y0 同一侧 | 86.9% [84.8%,89.0%] |

所以 robust statement 仍成立，但“近乎没有 direct influence”说得太满。ConfB 自己也有 signed cancellation，不能只拿 G31 提醒别人。

### 2. Gap 主要落在两臂共同的位置变化上，但这还不是机制

记

\[
b=\frac{CF_++CF_-}{2}-Y_0,\qquad d=\frac{CF_+-CF_-}{2}.
\]

那么逐 item 有两个精确恒等式：

\[
\frac{|CF_+-Y_0|+|CF_--Y_0|}{2}=\max(|b|,|d|),
\]

\[
\frac{(CF_+-Y_0)^2+(CF_--Y_0)^2}{2}=b^2+d^2.
\]

84.4% [82.3%,86.3%] 的 squared restoration error 落在 b²，而不是 polarity contrast d²。这个分解说明下一步不能只追“哪种 evidence 更 sticky”。但 b 包含 framing、内容共同部分、原始两臂相对 Y0 的不对称以及 readout 变化；不能叫作“84% 是 evidence-independent”或一个已识别的 epistemic reset。

在 CF 两臂相差 ≤5 点的 594 个 cells 中，center restoration error 仍为 28.25。这能说明 gap 不只是跨 item signed averaging 造成，但按 outcome 选出的 subset 是 descriptive，不能宣称“成功 suppression 导致 restoration failure”。两种文本也不构成对所有被排除内容的 invariance 证明。

### 3. 两个容易误读的 control / scaling 事实

CF arms 与同 item I 的直接 MAE 是 **23.00**，虽然它们到 Y0 的 MAE 只差约四点。两个点距离同一原点差不多，完全可以互相相距很远。因此差分绝对误差是 operational excess，不是语义贡献的因果分解。

原来 claim-level corr≈0.635、slope≈0.320 是先把六模型平均的结果。它不能直接当成各模型都实行同一个 contraction map 的证据。按模型用其他 claims 训练 affine inverse、五折预测 held-out Y0，没有得到稳定恢复：pooled MAE 约 30.37，对应原 center MAE 29.96。更复杂的 nonlinear map 没有被排除；本测试也不是方法提案。

### 4. “只是剩下一点 evidence weight”过于简单

测试一个明确但很受限的候选：每个模型只有一个剩余权重 λ，且

\[
CF_\pm=Y_0+\lambda(A_\pm-Y_0),\quad 0\leq\lambda\leq1.
\]

在四折数据上只用 polarity contrasts 拟合 λ，然后预测第五折的两臂位置。该模型预测的平均 center shift 仅约 **4.64**，实际为 **29.96**；held-out arm prediction MAE 约 **28.74**。因此“保留一个统一比例的原证据作用”不能解释中心偏移。这个结果不排除 item-dependent/nonlinear leakage，也不是新理论的确认。

### 5. Gap 不是概率期望读数独有

改用 raw 中实际 greedy 生成的 0–9 数字，映射到 0–100，arm restoration MAE 仍为 **32.44**。在 4/5 之间划分类别，CF 与 Y0 的 arm-average disagreement 为 **35.8%**，I 与 Y0 为 **28.6%**。这只是 readout robustness；给 rating 加 threshold 不能包装成 downstream action experiment。

## 如何处理 S/R/P

保留为分析工具，撤掉它作为“三种新能力”的中心地位。

设 clean response 为 f(E)，排除 X 后为 g(E,X)，restoration error 为 r(E,X)=g(E,X)−f(E)。那么：

- X 两种取值的 suppression contrast 是 r(E,X+)−r(E,X−)。
- 有效 E 两种取值的 preservation distortion 是 r(E+,X)−r(E−,X)。
- Restoration 是上述 error surface 在某一坐标的水平，而不是有限差分。

因此在覆盖所有这些条件、同一个响应尺度的前提下，若每处 restoration error 都 ≤ε，相应 suppression residual 与 preservation distortion 都 ≤2ε。单一 E、单一 score 的 R 不保证所有条件的 P；分布层面的目标还需要分布层面的检查。

这个关系没有提供新 theorem-level contribution，却能防止错误 framing：S/R/P 是对同一响应关系的不同测量切片。S 很小而 R 大可能只是两臂一起移位；P 很小而 R 大可能只是 bias 在两种 E 下相同。因此不能把 G31 的 P null 当作急需“补出第三个 failure”的缺口。

更值得的 conceptual distinction 是：**目标内容的作用是否改变、原判断是否恢复、以及当前测量是否真的在识别前者。** 这与 self-simulation、decision policy 和合法信息使用的关系可能成为新视角，但必须通过实际对照获得内容。

## Prior 对 ceiling 的实际影响

当前 ConfB 的可信度高于很多 exploratory findings；问题不是再加两个模型能否让 CI 更窄。问题是 reader 学到的中心句太接近已有结果。

Self-Blinding 已经有本地属性影响与 clean-counterfactual fidelity 的分离；in-context edit reversal 已经以恢复原输出为目标；人类 retraction 已经有 never-seen baseline、等信息量更新和后续学习；distraction 已经有 confidence、任务选择和内部通路的干预。因此以下单独作为 headline 都很弱：

- “不知道/不使用/不输出不是一回事”；
- “history matters”或“explicit ignore 不够”；
- “成功 suppression 不保证 restoration”；
- “内部仍可 decode”；
- “用 clean context 再算一遍可以修复”；
- “旧答案把撤销内容带到下游”。

这些 prior 没有替我们解释 ConfB，也没有证明所有 evidence-eligibility 问题都解决了。不能机械逐 component 判死。真正有空间的是一个不同的可检验区别，或者一个解释现有 gap 的新发现。

**我的 ceiling 判断：**现有材料有严肃 replication/extension 和完整 behavioral evidence 的价值；但以当前中心句直接包装为强 Main，novelty 风险明显，不足以承诺 Sasano/Outstanding taste。并非必须再做 mechanism：一个改变既有解释的构念识别或 evaluation finding 也可以升档。反之，哪怕做了很多 patching，如果结论仍是“late suppression”，也不会升档。

## 四条真正不同的路线

以下是研究投资选项，不是假装已经发现四个 novel ideas。每条都有必须产生的额外认识；没有它就降级或停止。

### A. 识别设计 / evaluation：把 non-use 与 counterfactual self-simulation 分开

**Mother question：**恢复不了“自己没见过时会怎么回答”，是否真的说明仍在使用被排除信息？

**值得知道的原因：**这决定我们测到的是权限执行、上下文敏感性，还是反事实自我预测。现有研究和本项目都容易把这些解释连在一起。创新若成立，在 construct 和 research strategy；不要求新方法。

**与 prior 的差别：**不是再添加 clean baseline；Self-Blinding 已有。需要同一明确 task contract 下，分别干预信息是否出现、是否有 exclusion/self-simulation 指令，检验哪一个因素导致所谓 failure。保留信息的正确使用须同时可测，避免用 constant output 假装 non-use。

**已有 support：**W/I 的大 error、ConfA AdmitPre movement、G31 的 P control，以及 ConfB 两臂共同偏移。它们提示测量混合，但尚未识别。

**最便宜 decisive step：**先对 ConfB 与 Self-Blinding 的实际 prompt/operator 作 estimand 对照；随后小规模做直接 exclusion 与 hypothetical self-prediction、同一指令下的 clean/redacted/included content 交叉。重点不是增加 control 数量，而是让两种“失败解释”产生不同预测。不要用两个 MAE 的差充当语义因果份额。

**结果分别教什么：**若 matched-task 下 selective non-use 与正常合法信息使用都成立，而 self-prediction 仍差，则现有 gap 至少部分被误归因；若简单 non-use 仍差，则 gap 不是自我预测问题的替身；若 instruction 和 content 都作用且有交互，必须给出两个 construct 的不同失败边界。只有改变真实评估结论、模型/干预比较或部署选择，才超过“指标不一样”。

**成功时最强句：**“常用的反事实恢复测试混合了信息排除与反事实自我预测；把它们分别干预后，对模型控制能力的结论发生了可复现的改变。”

**Ceiling：**明确反转已有认识可成为强 evaluation/construct Main；只再说需要更多 metrics，低。它是我推荐先做的识别工作，但不是预先认定会成功的 paper。

### B. 行为解释：识别撤销之后采用的判断规则

**Mother question：**撤销是在降低一条证据的权重，还是使模型换了一套判断规则？

**值得知道的原因：**这能把相反方向的 residual effects 放到同一个可检验问题里，而不是逐个追负方向、过度补偿或 confidence drop。

**与 prior 的差别：**Self-Blinding 已观察整体偏移；Bayesian/context work 已观察 confidence 改变。仅命名“reset”或“policy shift”没有新意。需要一个可复用的 factorization，或者一个新的条件区别，能解释同 item 的结果，而不是只拟合 pooled mean。

**已有 support：**本次 b/d 分解、两个简单候选拟合失败、G30 的特殊 response regime。后者说明“采用另一种回答规则”确实是可能性，但不能外推为六模型通用机制。G31 的 P null 也约束了 universal global damping 解释。

**最便宜 decisive step：**在少量简单自然材料中独立改变仍有效理由、被排除内容和判断任务。至少区分开放知识判断与仅根据明确有效记录作判断。用独立 clean 条件估计任务默认回答，再比较：残留证据加权、向任务默认值回归、反事实查询改变任务三种解释。对 held-out items/wording 预测整个响应关系；不为每个 item 拟合一个自由 λ。

**结果分别教什么：**如果一个简洁映射能跨 wording/item 预测，进入行为解释路线；若只有开放知识任务失效，可研究 parametric/contextual grounds 的具体边界，但“更明确提示更好”不足以成稿；若偏移全由 ordinary task restatement 解释，结束 exclusion-specific headline；若没有可迁移结构，不继续扩大 phenomenology 收集。

**成功时最强句：**“排除指令改变的不只是目标证据权重；我们识别了决定它何时改变整套判断规则的条件，并预测了此前方向不一致的结果。”这是待证句，不是当前结论。

**Ceiling：**新视角加稳定预测/清楚边界可以成为强 Main，未必需要 internal mechanism。现在还没有证据支持一个普遍 law。

### C. 内部计算：干预控制关系，而不是寻找‘遗忘’位置

**Mother question：**模型把‘此信息可用于此判断’编码为可组合的控制关系，还是把 exclusion 变成某种回答倾向？

**为什么不只是 probe：**只有改变这个候选控制关系能选择性改变 X 的作用、同时保持 task 和合法 E 的作用，才提供新的机制认识。读取到 policy 标签或把答案 patch 回 Y0 都不够。

**与 prior 的差别：**Takashiro 的 late `forgot`、superficial-editing 的旧答案恢复以及 contextual entrainment 都没有自动回答这一控制关系的组织方式。机制创新可能本身是核心，不必先有 universal behavioral law；但必须解释一个稳定、明确的新对照。

**已有 support：**Stage 5/G23C/G24B 有可复用的因果交换技术与 target-conditioned effects；没有 ConfB 的机制答案。它们是工具和局部证据，不是继承下来的 headline。

**最便宜 decisive step：**A/B 明确一个行为分离后，在一个模型上固定相同内容与答案 readout，只交换匹配的 policy/task 状态；加入同目标/异目标以及 admit/irrelevant donor。检验是否能转移控制规则而不是直接转移某个 verdict，并在未用于选择 intervention 的 items 上测试。

**结果分别教什么：**可迁移的关系性干预支持 compositional control；只转移答案倾向支持 readout/task-state解释；干预普遍损坏则没有识别机制，不能把 null 解释成“distributed representation”；模型间不同可以是重要结果，前提是比较同一个已定义的计算对象。

**成功时最强句：**“我们因果分离了证据内容与它在当前判断中的使用权限，并说明 restoration 在哪一步失败。”

**Ceiling：**潜在高，但当前 expected value 低于先识别行为对象。不要立即启动大 patch sweep，也不要以旧 G18 的 empirical strength 为重启理由。

### D. 决策后果：局部去影响是否改变了合法决策边界

**Mother question：**一种看起来成功的 exclusion 会不会系统改变仍由有效信息决定的实际选择？

**与 prior 的差别：**Self-Blinding 已有 loan/promotion 等选择情景；Garcia 的 abstract 已报告撤销后的数值载体；memory-revocation work 已有 unsafe actions。因此换成 recommendation/action 或串两个 agent 不够。

**值得投入的新增内容：**识别原有 S 指标会选择某种干预，而该干预在同一合法决策问题中系统改变阈值、排序或错误类型；能解释什么时候 disagreement 是 harmless calibration、什么时候改变 substantive choice。需要独立合法 grounds 或可核查记录，不能只把 0–9 切成两类。

**已有 support：**ConfB greedy readout 的大 disagreement 证明不只 expectation artifact；G31 对 valid E 的剩余作用给出设计经验。但尚没有自然 action utility 的 decisive result。

**最便宜 decisive step：**一个短的、可核验的记录决策任务，选定两种确实供人使用的 exclusion 策略，成对评估被禁止内容的效应和基于有效记录的实际选择。先找有没有系统的 intervention-ranking reversal，而不是堆场景。

**结果分别教什么：**若 S 越好但合法选择越差且可解释，形成 consequential evaluation；若不同 readout 下选择一致，CRE 的用途应收窄；若所有变化与普通额外上下文相当，则没有 exclusion-specific downstream contribution。

**成功时最强句：**“按排除成功率选择的干预会系统损害基于合法信息的选择；我们指出这种评价何时给出相反建议。”

**Ceiling：**可以单独成为扎实 Main，不强求机制；但只展示一些答案翻转，低。优先级在 A/B 后，因为它们决定应该测何种后果。

## 推荐的投入顺序与转向条件

**第一优先是 A 的 construct identification，服务于 B 的解释，而不是直接宣布新 benchmark。** 原因不是它最容易成功，而是它能决定当前约 30 点 gap 究竟值得被哪一个研究领域解释。机制实验、方法训练和 downstream scaling 都依赖这一判断。

第一步已有一部分完成：核验 raw、拆开 signed/absolute、拆开 shared/polarity components、检查生成数字、检验最简单的残留权重和 affine calibration。下一项工作应把两个具体实验问题区分开：

1. 在固定判断任务与合法信息下，被排除内容的变化是否仍改变回答？
2. 在没有这条内容时，单独要求 counterfactual self-reconstruction 是否已改变回答？

用少量 paired cases 和少数模型做因子交叉足够作为诊断。首先固定“可以依据什么”和“最终问什么”；不是靠多写几遍 ignore 来改善。然后让仍有效证据至少有两个独立取值，以排除所有条件都输出同一默认值的假成功。直接 exclusion 与 self-reconstruction 使用同一 task contract。Clean/redacted control 保持指令和查询框架；额外文本的存在效应与内容替换效应分开估计。少量重复 clean 和 placebo cells 提供本设置自己的变动尺度，不能借用 P3 的 1.84 当严格匹配噪声。

这些条件不是新的 S/R/P checklist。它们服务于一个识别问题：**现有 gap 是内容选择失败、反事实回答失败，还是任务/判断规则改变？**

只有以下结果才进入第二步：

- 若两种能力可清楚分离，而且会改变对已有 exclusion 策略的结论：发展 A，优先做针对已有研究的实质性 evaluation audit。
- 若存在可复用的响应规则或新边界：发展 B；随后选择一个机制干预或一个自然决策后果来深化，而非两者都做。
- 若存在稳定的 policy-specific 行为对照但行为拟合解释不了：C 可以成为主线，不要求先编出一个行为规律。
- 若效果只剩 ordinary framing、task ambiguity 或 stronger prompt helps：停止当前 explanatory expansion；ConfB 作为诚实的 replication/extension 资产保存，不再靠重新命名硬撑。
- 若以上都没有出现：需要承认尚未找到足够强的新研究对象。Outcome-robust research 是不同结果都改善判断，不是每种结果都保证有 paper。

暂不做 restoration LoRA、G32 preservation benchmark、更多模型 breadth、泛化的 source-scope 再确认、无差别 activation sweep 或 agent 包装。简单 clean-context replay 可作 comparator；它的成功本身不是方法创新。

## Taste anchor 的真正约束

这些强论文没有共同要求“再多一个 mechanism”。Response Sampling 的新因子分解、Value-Action 的 paired construct、CoT Faithfulness 的干预策略、Sensitive Functions 的解释理论、Long-ICL 的结构探索，是不同形式的 intellectual advance。

对本项目最有用的要求是：去掉实验编号、新名字和数据规模之后，能否说清读者以前会混淆什么、现在可以区分什么；以前不能解释/预测/检验什么、现在可以。当前 ConfB 提供值得解释的事实，Self-Blinding 提供不能回避的最近比较，而 G18 的教训要求我们拒绝把显然的理想行为本身当创新。

我不建议现在把项目收成“CRE benchmark”，也不建议因为一个相近 prior 放弃全部 assets。值得集中投入的未知数已经比较清楚：排除指令实现的究竟是哪一种判断变换，以及现有评估对它作了什么错误推断。只有这个问题获得新的经验内容，才是下一篇论文真正的开始。
