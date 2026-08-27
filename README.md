# Can LLMs Unring the Bell?

> **Working research plan — 2026-08-27**  
> 核心问题：LLM 明明知道某条信息/证据“不得用于判断”，甚至能正确复述这条规则，但这条信息是否仍会对最终判断产生可测的因果影响？进一步，“事先知道不能用”与“看过以后才被告知不能用”是否存在系统性的时间不对称？

## 0. 先说结论：只证明现象还不够，论文必须继续往下走

如果最后只得到下面一句话：

> LLM 知道证据不能用，但还是被证据影响。

这本身是一个干净的 behavioral finding，但还不足以形成我们真正想做的完整题目。因为它会很容易被归入 instruction-following failure、anchoring、irrelevant-context robustness、belief revision 或 in-context forgetting 的邻近问题。

**真正值得推进的主线应该是：**

1. **Phenomenon**：证明 `rule knowledge != decision implementation`，并检验 Post-exclusion 是否系统性比 Pre-exclusion 更差。
2. **Generality**：证明这不是“陪审团 prompt 特例”，而是跨任务、跨 exclusion reason、跨模型的 **known-but-disallowed information gating failure**。
3. **Mechanism**：区分失败到底发生在：
   - 没有表示“这条信息无效”；
   - 表示了无效规则，但没有正确绑定到对应证据；
   - 证据和无效标签都表示了，但最终 decision readout 仍读取了证据。
4. **Intervention**：验证这个失败能否通过 context sanitation、structured evidence gating、causal masking，乃至专门的 counterfactual training 修复。

如果四步能连起来，论文不再是“LLM 也有人类 cognitive bias”，而是：

> **LLM 对已知但禁止使用的信息存在选择性门控失败；这种失败具有明确的时间结构、可定位的内部信息通路，并可以被针对性修复。**

---

# 1. 从法律场景出发：为什么这个母题是自然的

最直观的场景是陪审团：

1. 陪审员先听到一条强证据；
2. 法官随后裁定该证据不可采纳，明确要求不能用于最终判断；
3. 最终判决理论上应该和“从未听到该证据”接近。

这就是经典的 **Unring the Bell**：已经进入认知系统的信息，能不能在之后被“取消使用”？

人类端，这个现象不是零散 anecdote：

- Steblay et al. (2006) 的 meta-analysis 汇总 **48 项研究、8,474 名参与者、175 个 hypothesis tests**，总体发现 inadmissible evidence 会显著影响 verdict，而 judicial instruction 通常不能完全消除影响。
- Kassin & Sommers (1997) 进一步发现，**排除原因会改变是否能够忽略**：如果 wiretap 因为“不可靠”而被排除，人更容易不使用；如果内容可能是真的，只是因为程序违法而不可采纳，人更容易继续受影响。
- Engel, Golder & Rahal (2026) 的 1,432 人在线实验再次说明不能假设任何 inadmissible evidence 都会产生同样效应：prior-conviction character evidence 在他们的设计里没有稳定 bias，但 illegal wiretap confession 有很强的 effect；四种 debiasing intervention 虽然能降低 bias，却都没有完全消除。

这三点对我们的数据设计非常关键：

> **不能“先认定现象存在，再挑数据证明”。必须先验证 critical evidence 本身真的足以改变判断，然后冻结 item，最后才看 exclusion 是否失败。**

---

# 2. 我们真正研究的不是 “forgetting”

需要和已有工作划清边界。

## 2.1 In-context forgetting（ICF-Bench）

ICF-Bench（ICLR 2026）研究的是：上下文中已经给过的信息，后来要求模型“forget”，模型还能不能表现得像不知道这条信息。

典型结构更接近：

> Tom likes blue → forget Tom's favorite color → What color does Tom like?

这里希望的是信息本身不再可访问。

**我们的任务不同。**

法庭里的合格 decision maker 完全可以继续记得：

> “我知道证人说了什么。”

但同时必须做到：

> “这条证据不可采纳，所以不能让它影响我的最终判断。”

因此我们要求的不是 memory deletion，而是：

> **Selective non-use of known information in a downstream decision.**

这是整篇工作最重要的概念边界。

## 2.2 Belief revision / knowledge conflict

Belief-R（EMNLP 2024）、TRACK（EACL 2026）等研究的是新信息要求模型修改旧结论，或 contextual knowledge 与 parametric knowledge 冲突时如何传播更新。

我们的 setting 不一定改变“事实真假”：

- 一条 illegal wiretap confession 可以是真的，但法律上不能用；
- 一条 confidential report 可以是真的，但当前决策者无权用；
- 一个事后 outcome 可以是真的，但评价 ex-ante decision quality 时逻辑上不能用。

所以我们研究的是 **epistemic state 与 decision policy 的分离**。

## 2.3 Anchoring / irrelevant context

LLM 已被证明会有 anchoring、evidence-order effect，并且 “ignore previous” 一类 prompt 往往不能稳定消除影响。2026 年的 legal-decision study 也发现 GPT-4o / GPT-5.2 对证据顺序敏感，prompt engineering 不能稳定消除这种 procedural sensitivity。

这些工作说明“先出现的信息会留下影响”是 plausible 的，但它们通常没有同时要求：

1. 模型明确识别某条具体信息不能使用；
2. 测量这条信息对另一个 downstream judgment 的残余效应；
3. 比较 exclusion 在 evidence 之前/之后；
4. 进一步定位内部的 gating failure。

这就是我们的空间。

---

# 3. 正式定义：不要只比较一个 Post-exclusion prompt

令：

- `B`：基础信息（base context）
- `E`：critical evidence / critical information
- `R_excl`：明确规定 E 不得用于判断的 rule
- `R_admit`：明确规定 E 可以使用的 rule/order control
- `Y`：最终 judgment（例如 0–100 guilt probability / suitability score / estimated mean）

正式实验建议至少使用五种条件：

| 条件 | 顺序 | 作用 |
|---|---|---|
| **Base** | `B → Y` | 没有 critical evidence 的基线 |
| **Admit-Pre** | `B → R_admit → E → Y` | 合法证据 + rule 在前 |
| **Admit-Post** | `B → E → R_admit → Y` | 合法证据 + rule 在后，控制一般 order/recency |
| **Exclude-Pre** | `B → R_excl → E → Y` | 一开始就知道 E 不能用 |
| **Exclude-Post** | `B → E → R_excl → Y` | 先看 E，再要求取消其影响 |

G0 为了节省计算，可以先用 `Base / Admit / Exclude-Pre / Exclude-Post` 四条件；正式实验再补齐 Admit 的顺序 control。

## 3.1 Rule comprehension 必须独立测

不要在同一次 trial 里先问：

> “这条证据可以使用吗？”

然后再让模型判断案件。这个 probe 本身会成为一次额外 reminder，改变后续 decision。

正确做法：

- **Decision run**：只做最终判断；
- **Rule probe run**：相同 context 的独立调用，只问 evidence 是否允许使用；
- **Memory probe run**：如果需要，再独立检查模型是否还能复述 E。

于是我们可以真正观察：

> Rule accuracy 很高；E 也仍然被记得；但 decision 仍被 E 推动。

这才是 `knowing not to use ≠ not using`。

---

# 4. 指标：把“残余影响”定义清楚

对每个 item，先统一 critical evidence 的方向。

设：

\[
L = Y_{admit} - Y_{base}
\]

只有当 `|L|` 足够大时，这条 item 才有能力测试 exclusion；否则连正常使用 E 都没有效果，谈不上“是否成功排除”。

为了让正向/负向 evidence 可以一起分析，令：

\[
s = \operatorname{sign}(L)
\]

对任意条件 c 定义 sign-aligned shift：

\[
D_c = s\,(Y_c-Y_{base})
\]

再定义 **Residual Evidence Influence (REI)**：

\[
REI_c = \frac{D_c}{|L|}
\]

解释：

- `REI ≈ 0`：和 Base 一样，基本成功忽略；
- `REI ≈ 1`：和正常使用 evidence 差不多，排除几乎没作用；
- `0 < REI < 1`：存在部分残留；
- `REI < 0`：出现 overcorrection。

核心 temporal metric：

\[
\Delta_{time}=REI_{post}-REI_{pre}
\]

正式五条件下，再计算一个 order-adjusted interaction：

\[
UTB=(Y_{ExcludePost}-Y_{ExcludePre})-(Y_{AdmitPost}-Y_{AdmitPre})
\]

它用来扣除普通的 instruction-position / recency effect。

---

# 5. 第一阶段数据：先证明是不是 LLM 的普遍现象

## 5.1 不要按“行业”堆五个 domain；要按 task family + exclusion reason 做 generality

如果只做：

- 法律
- 招聘
- 医疗
- 金融

reviewer 仍可以说它们只是几个相似的自然语言 judgement vignette。

更强的 generality 应同时跨越：

### Task family

1. **Legal/evidence judgment**：根据信息判断 guilt/liability。
2. **Numerical aggregation**：从多份数值报告估计总体均值。
3. **Ranking / selection**：候选人/供应商/项目多属性选择。
4. **Evidence-based inference**：根据多个 likelihood-bearing observations 判断故障/类别概率。
5. **Ex-ante decision evaluation**：评价当时决策质量，不得使用后来 outcome。

### Exclusion reason

1. **Epistemic invalidation**：信息后来被确认错误/不可靠。
2. **Procedural exclusion**：信息可能为真，但规则不允许使用（法庭）。
3. **Access-control / confidentiality**：信息可能为真，但当前决策者无权使用。
4. **Temporal irrelevance**：信息为真，但在所评价的 decision time 之后才出现。

这两个轴一起出现，才能支持“一般的 information gating failure”。

---

# 6. 数据到底从哪来，哪些真的易得

## 6.1 Legal：用人类范式做 seed，但不要指望有一个现成的大型 NLP benchmark

可用来源：

- **Steblay et al. (2006)**：给出非常大的文献地图，帮助整理 evidence type / ruling type。
- **Kassin & Sommers (1997)**：wiretap 的 `unreliable` vs `illegally obtained` 是特别好的 reason-control。
- **Engel et al. (2026)**：1,432 人，character evidence vs wiretap，并尝试四种 debiasing；论文声明 materials/data/code 均公开在 OSF。
- **Saul Kassin 的公开 research page** 提供多套历史 trial stimulus materials，可用于理解真实法律心理学 vignette 的写法。

### 我们如何实际构造

不要把旧论文的长 stimulus 大段复制进 benchmark。做法应是：

1. 从公开人类范式中抽取 **结构**，不是逐字复制；
2. 自己写新的简化案件；
3. 保持基本证据 `B` 模棱两可；
4. 增加方向明确且足够强的 `E`；
5. 用明确 judge ruling 决定 `E` 可用/不可用。

候选 evidence type 可以包括：

- illegal wiretap confession；
- illegally obtained location/search evidence；
- privileged attorney-client communication；
- excluded hearsay / witness statement；
- prior-act / character evidence；
- civil case 中规则明确禁止使用的 settlement-related information。

但必须遵守 **evidence-leverage screening**：某个 E 如果在 Admit 条件下都推不动 judgment，就不能拿它测 exclusion。

Engel et al. (2026) 中 prior-conviction manipulation 没有稳定 bias，而 wiretap 很强，正好说明 screening 是必要的。

## 6.2 Numerical invalidation：最容易，完全可以自己无限生成

Ramsey et al. (2024) 的五个实验就是很好的自然依据：参与者看从 Gaussian distribution 采样的一串数值，其中出现 invalid outlier；即使他们能检测出 invalid value，最终估计仍被它拉偏。该研究公开了 data、analysis 和 example experimental code。

我们可以直接程序生成：

```text
Reports: 48, 51, 52, 47, 50
Critical report: 82
Task: estimate the underlying typical value.
```

条件：

- Base：没有 82；
- Admit：82 是有效报告；
- Exclude-Pre：先说某个指定报告来自坏掉的 sensor、不得使用，再展示；
- Exclude-Post：先展示 82，再告知 82 来自坏掉的 sensor、不得使用。

优点：

- ground truth 可计算；
- 数据可无限生成；
- 不需要 LLM judge；
- 能把完全相同的数字换成 sensor、prices、lab measurements、delivery-time reports 等 surface form。

## 6.3 Ranking / selection：底层程序生成，表面再渲染

构造两个 borderline candidate：

```text
Vendor A: price 8, reliability 6, delivery 7, support 6
Vendor B: price 6, reliability 8, delivery 6, support 7
```

底层固定 scoring rule：

\[
S=w^Tx
\]

只保留 `|S_A-S_B|` 较小的 pair，再加入强 critical information，例如：

> Internal report: Vendor A reliability = 2/10.

然后分别把它设成：

- verified & usable；
- confidential & forbidden；
- mistaken record；
- 在 exposure 后才宣布不得使用。

同一个 latent problem 可以渲染成 vendor / applicant / apartment / project selection，避免“不同 domain 其实底层难度也不同”的混淆。

## 6.4 Hiring：有现成 5,118 份 synthetic resumes，可作为 naturalistic base

`Resume Bias Public`（2026）公开：

- 5,118 份 base synthetic resumes；
- structured jobs / work history；
- O*NET task lists；
- pipeline code；
- MIT license。

我们不使用 demographic manipulation 作为主实验，因为现代 alignment 训练可能把“不要根据 race/gender”变成特殊安全策略。

更适合我们的 `E` 是：

> Preliminary reference says the candidate repeatedly missed deadlines.

然后设定：

- approved reference：可用；
- unauthorized reference：是真的，但 hiring policy 禁止使用；
- mistaken reference：后来确认属于另一个人。

这样可以比较 **true-but-forbidden** 与 **false-and-invalid**。

## 6.5 Outcome evaluation：开放材料易得，适合作为完全不同的 exclusion reason

Aiyer et al. (2023) 对 Baron & Hershey outcome-bias paradigm 做了 preregistered replication（N=692），即使 participant 明确表示 outcome 不应该被纳入 decision-quality evaluation，仍观察到明显 bias；materials/data/code 在 OSF 开放。

我们的结构：

1. 给出做决定时所有可用信息；
2. 描述 decision；
3. 再给 success/failure outcome；
4. 明确要求“只评价当时 decision quality，不得使用事后 outcome”。

这里 outcome **是真的**，但对 ex-ante quality judgement **逻辑上无关**。如果这里也有 Post residue，就比“坏 sensor 数据撤回失败”更能说明 general gating problem。

---

# 7. 建议的数据 schema

所有 task family 统一存成结构化 item，而不是直接存四段手写 prompt：

```json
{
  "item_id": "legal_001",
  "task_family": "legal_judgment",
  "surface_domain": "criminal_trial",
  "base_context": "...",
  "critical_evidence": "...",
  "critical_direction": "increase",
  "exclusion_reason": "procedural_illegality",
  "admit_rule": "...",
  "exclude_rule": "...",
  "question": "Rate probability of guilt from 0 to 100.",
  "output_type": "integer_0_100"
}
```

再由 compiler deterministic 地生成：

- `base`
- `admit_pre`
- `admit_post`
- `exclude_pre`
- `exclude_post`
- `rule_probe`
- `memory_probe`（可选）

这样可以保证条件之间真正只改变 rule/order，而不是每个 prompt 都被 LLM 改写得不一样。

---

# 8. 数据筛选必须在看 Pre/Post 结果之前完成

这是整个实验能否经得住 reviewer 的关键。

## 8.1 Screening rule

对候选 item，只用 `Base + Admit` 和独立 rule probe 做筛选。

建议：

1. **Base 不要极端**：例如 rating 落在 20–80，避免 floor/ceiling。
2. **Evidence leverage 足够大**：例如 `|Y_admit-Y_base| >= 10/15`。
3. **Critical direction 稳定**：多个 prompt paraphrase 下方向一致。
4. **Rule comprehension 足够高**：模型能明确判断该 evidence 是否允许使用。
5. **正/负 evidence 平衡**。
6. **冻结 dataset 后，才第一次跑 Exclude-Pre / Exclude-Post。**

绝不能：

> 先跑 Post，然后把“有 Unring-the-Bell effect”的 item 留下来。

那会直接把现象写进 dataset selection。

---

# 9. G0：先回答“这个现象到底在 LLM 中存在吗？”

## G0-A：Legal anchor

建议先做 **60 个 legal base items**：

- 至少 4–6 种 evidence type；
- inculpatory / exculpatory 平衡；
- unreliable / procedural / privilege 等不同 exclusion reason；
- 四条件 `Base / Admit / Pre / Post`。

总计：

\[
60 \times 4 = 240\text{ prompts/model}
\]

## G0-B：Controlled generality

再做：

| Task family | base items |
|---|---:|
| Numerical aggregation | 30 |
| Ranking / selection | 30 |
| Evidence inference | 30 |
| Outcome evaluation | 30 |
| **Total** | **120** |

四条件共：

\[
120\times4=480\text{ prompts/model}
\]

第一轮可以直接跑 Qwen3-8B / 14B / 32B。主输出全部限制成 deterministic parseable score/choice，不使用 LLM judge。

## 9.1 第一阶段晋级线

不要只看总平均。

我们希望看到：

### H1 — Rule knowledge

模型在独立 probe 中高概率知道 E 不可使用。

### H2 — Residual influence

\[
REI_{post}>0
\]

且不是由少量 extreme item 驱动。

### H3 — Temporal asymmetry

\[
REI_{post}>REI_{pre}
\]

至少在法律 + 多个 controlled task family 中稳定。

### H4 — Not mere order effect

正式五条件后：

\[
UTB>0
\]

也就是 Exclude 的 Pre/Post 差异大于 Admit 的普通 order 差异。

统计上优先使用 item-level paired bootstrap CI；正式版可以再加 mixed-effects model，把 item / surface template 作为随机效应。

---

# 10. 如果现象成立，下一步最重要：到底哪里坏了？

这才是这个题从 benchmark 走向 interpretability 的地方。

需要区分三个机制假设。

## M1 — Invalidation representation failure

模型根本没有稳定形成：

> “E 是 invalid / forbidden”

的内部状态。

**预测：** rule probe 虽然文字输出可能正确，但内部 validity representation 弱、不稳定，或仅出现在末层。

## M2 — Rule–evidence binding failure

模型同时知道：

- E 的内容；
- 有一条 exclusion rule；

但没有正确把“invalid”绑定到对应 evidence span。

这在多条 evidence、只有一条被 strike 的 setting 中尤其容易测试。

## M3 — Decision gating / readout failure

最有意思的情况：

- E 的内容在内部可解码；
- `E-is-invalid` 也可解码；
- 但最终 judgment 仍然因果依赖 E。

这说明问题不是“不懂规则”，而是 **final decision computation 没有执行选择性门控**。

---

# 11. 机制实验怎么做

只在 G0 中 effect 最稳定的 1–2 个 open-weight model 上做，不要一开始全模型上 SAE。

## 11.1 Layer-wise probing

分别 probe：

1. critical evidence 的方向/内容；
2. evidence 的 admissible/invalid status；
3. 最终 decision direction。

比较 `Admit / Pre / Post` 随 layer 的变化。

重要：**“E 仍然可解码”本身不是失败。** 我们本来就允许模型记得 E。真正要看的是 validity state 是否出现、以及它是否改变 downstream decision representation。

## 11.2 Activation patching

构造 matched pairs：

- `Post` vs `Base`
- `Post` vs `Pre`
- `Post` vs `Admit`

对 evidence span、rule span、judgment-position residual stream 做 activation patching，观察 final score/logit margin 是否向另一条件移动。

目标不是画一堆 heatmap，而是回答：

> **哪一段内部 computation 负责让 excluded evidence 继续进入最后 judgment？**

## 11.3 Evidence-span causal masking / ablation

Oracle experiment：在 Exclude-Post 中，rule 出现后，让 judgment token 无法继续从被排除 evidence span 读取信息（attention/span ablation），再看：

\[
Y_{post}^{masked}\rightarrow Y_{base}?
\]

如果明显回到 Base，这是很强的因果证据：residual influence 确实通过该 evidence information path 进入了 decision。

## 11.4 “Re-encoding” test：专门检验时间不对称的来源

Causal Transformer 中，Pre 与 Post 有一个天然结构差异：

- `R → E` 时，E token 的 contextual representation 在形成时已经可以看到 rule；
- `E → R` 时，E token 本身不能看到未来才出现的 R，后续只能在新的 token 中完成“E + invalid”绑定。

这**不是**说 Post exclusion 在 Transformer 中必然失败——最终 judgment token 可以同时 attend E 与 R。它只是给出一个可检验的机制假设：Post 需要额外的 downstream binding/gating。

可以设计：

> E → R → `[EXCLUDED E SUMMARY]` → judgment

即在 rule 之后重新呈现一个明确标记为 excluded 的 E 表征。

如果这样显著缩小 Post/Pre gap，支持“后验 binding / contextualization”机制。

---

# 12. 再下一步：不是只解释，要尝试修复

如果我们能定位 failure，最自然的贡献是 mitigation。

## 12.1 Context sanitation（最强 practical baseline）

当系统知道某段信息不能再用时，不只是给一句：

> ignore it

而是直接在 decision stage 构造新的 context：

> 只保留 admissible evidence。

如果 sanitation 几乎完全恢复 Base，而普通 natural-language exclusion 不行，说明高风险 agent / legal workflow 不应该把“不得使用”仅仅作为一句 prompt 指令。

## 12.2 Structured evidence ledger

将 context 显式拆成：

```text
[ADMISSIBLE]
E1
E2

[EXCLUDED]
E3 — reason: illegally obtained
```

或者两阶段：

1. classify admissibility；
2. rebuild decision context from admissible evidence only；
3. make judgment。

这比单纯 “please carefully ignore” 更接近实际系统设计。

## 12.3 Oracle causal mask

对于 open model，直接在 inference 中阻断 excluded span → decision 的信息流。

这个实验未必立刻是可部署方案，但能给出机制上限：

> 如果 model-side gating 完全解决，而 prompt 解决不了，那么问题确实在 information routing，而不是 task 本身不可解。

## 12.4 Counterfactual Exclusion Consistency training（如果前面都成立，这是最值得扩展的方法线）

Controlled synthetic task 的优势是有 verifier，可以训练：

- **Admit**：模型必须对 E 敏感；
- **Exclude**：输出应该和 Base 一致；
- **Rule probe**：必须正确判断 admissibility。

可定义目标：

\[
L_{inv}=D(p(y|B,E,R_{excl}),p(y|B))
\]

同时用可验证 synthetic task 保证 `Admit` 条件正确使用 E，防止模型学成“看到额外证据全部忽略”。

真正有价值的测试是：

> **只在 synthetic/verifiable task 上训练 selective gating，能否 OOD transfer 到从未训练过的 legal naturalistic cases？**

如果能，这会从“发现 bias”升级成一个清楚的方法贡献。

---

# 13. 结果出现不同情况时，怎么决定继续还是砍

| 结果 | 解释 | 下一步 |
|---|---|---|
| `RuleAcc 高 + Post residue 高 + Post > Pre`，跨任务成立 | 最理想：known-but-disallowed gating + temporal asymmetry | **全力推进：机制 + mitigation** |
| RuleAcc 高，Pre/Post 都有 residue，但二者差不多 | 一般 selective gating failure，时间不对称不成立 | 保留主问题，弱化 Unring-the-Bell timing claim |
| 只有法律成立，controlled task 不成立 | 更可能是 legal/evidence-specific bias | 不做“普遍 LLM 现象” claim；评估是否值得做法律应用论文 |
| Admit 本身推不动判断 | item 无效 | 在冻结 Pre/Post 前筛掉 |
| RuleAcc 低 | 更像 instruction misunderstanding | 不值得做 interpretability 主线 |
| Admit-Pre/Post 也有同等 order shift，`UTB≈0` | 普通 recency/position effect | temporal-exclusion claim 失败 |
| 强模型几乎 `Pre≈Post≈Base` | 当前模型能够正确 gate | 及时停题，除非小模型/特殊 setting 有明确理论价值 |
| False/unreliable 很容易排除，但 true-but-forbidden 明显残留 | 非常有意思：不是“不能更新”，而是 normative gating 特别难 | 加强 exclusion-reason 轴，形成第二核心发现 |

---

# 14. 我认为最理想的论文故事

## Behavioral finding

> LLMs can explicitly identify that evidence is disallowed, yet their final decisions remain causally sensitive to it.

## Temporal finding

> This residual influence is stronger when exclusion occurs after exposure than when the same rule is known before exposure, beyond generic order effects.

## Generality finding

> The effect appears across legal judgment, numerical aggregation, selection, evidence inference and ex-ante decision evaluation, with systematic differences between epistemic invalidation and true-but-forbidden information.

## Mechanistic finding

> Models often retain both the evidence and its invalidity status, but excluded evidence still contributes to decision representations/readout: the failure is better characterized as **gating/binding failure** than literal forgetting failure.

## Intervention finding

> Explicit context sanitation / structured evidence gating / model-side masking substantially reduces residual influence; counterfactual gating training can be tested for cross-domain transfer.

如果最终能得到这五段，题目就非常完整。

---

# 15. 当前推荐执行顺序

## Stage 0 — 先别做解释

1. 写 legal generator + 60 cases。
2. 写 numeric / ranking / inference / outcome generators，各 30 cases。
3. 只跑 `Base + Admit + RuleProbe` 做预筛。
4. 冻结 item。
5. 第一次跑 `Pre + Post`。
6. 看 Qwen3-8B / 14B / 32B 是否跨 family 稳定。

**在这之前不做 SAE、不做 patching。**

## Stage 1 — 行为实验正式化

1. 补 `Admit-Pre / Admit-Post` order control。
2. 加 2–3 个 wording paraphrase，确保不是某一句 ruling 的 wording artifact。
3. 加 exclusion-reason manipulation。
4. 做 naturalistic legal / hiring / outcome validation。

## Stage 2 — 机制

选择 effect 最强且最稳定的 open model：

1. probes；
2. activation patching；
3. evidence-span masking；
4. re-encoding test。

## Stage 3 — 修复

1. natural-language stronger instruction baseline；
2. structured evidence ledger；
3. context sanitation；
4. oracle mask；
5. 如果值得，再做 counterfactual exclusion training。

---

# 16. 暂定标题

### 更偏现象

**Can LLMs Unring the Bell? Temporal Asymmetry in Excluding Known Information**

### 更偏核心概念

**Knowing Not to Use Is Not the Same as Not Using: Evidence Gating Failures in Large Language Models**

### 如果最后机制很强

**Known but Disallowed: Tracing and Repairing Evidence-Gating Failures in Large Language Models**

---

# 17. References / directly relevant resources

## Human / decision science

- Steblay, N. et al. (2006). **The Impact on Juror Verdicts of Judicial Instruction to Disregard Inadmissible Evidence: A Meta-Analysis.** Law and Human Behavior. https://pubmed.ncbi.nlm.nih.gov/16906469/
- Kassin, S. M. & Sommers, S. R. (1997). **Inadmissible Testimony, Instructions to Disregard, and the Jury: Substantive Versus Procedural Considerations.** https://doi.org/10.1177/01461672972310005
- Golding, J. M. et al. (1990). **Instructions to disregard potentially useful information: The effects of pragmatics on evaluative judgments and recall.** https://doi.org/10.1016/0749-596X(90)90073-9
- Ramsey, A. T., Liu, Y., & Trueblood, J. S. (2024). **Can Invalid Information Be Ignored When It Is Detected?** Psychological Science. https://pubmed.ncbi.nlm.nih.gov/38483515/ — open materials/data/code: https://osf.io/9ybnx/
- Aiyer, S. et al. (2023). **Outcomes Affect Evaluations of Decision Quality: Replication and Extensions of Baron and Hershey’s (1988) Outcome Bias Experiment 1.** https://pmc.ncbi.nlm.nih.gov/articles/PMC12372742/ — materials/data/code: https://osf.io/knjhu/
- Engel, C., Golder, J., & Rahal, R.-M. (2026). **Who Is Afraid of the Pink Elephant? Evidence on (Not) Ignoring Inadmissible Evidence and Debiasing Interventions.** https://doi.org/10.1002/bdm.70064
- Saul Kassin research/stimulus archive: https://saulkassin.org/research/

## LLM adjacent work / novelty boundary

- Qian, Y. et al. (2026). **Do LLMs Forget What They Should? Evaluating In-Context Forgetting in Large Language Models.** ICLR 2026. https://proceedings.iclr.cc/paper_files/paper/2026/hash/b13d00a62d438856cfe6fbd13b6b2cb8-Abstract-Conference.html
- Wilie, B. et al. (2024). **Belief Revision: The Adaptability of Large Language Models Reasoning.** EMNLP 2024. https://aclanthology.org/2024.emnlp-main.586/
- Feng, Y. et al. (2026). **Tracking the Limits of Knowledge Propagation: How LLMs Fail at Multi-Step Reasoning with Conflicting Knowledge.** EACL 2026. https://aclanthology.org/2026.eacl-long.273/
- Takashiro, S. et al. (2025). **Answer When Needed, Forget When Not: Language Models Pretend to Forget via In-Context Knowledge Unlearning.** Findings ACL 2025. https://aclanthology.org/2025.findings-acl.1276/
- Nguyen, J. K. (2024). **Human bias in AI models? Anchoring effects and mitigation strategies in large language models.** https://doi.org/10.1016/j.jbef.2024.100971
- **Legal Decision Biases in GPT: A Comparison with Human Judgment** (2026). https://pmc.ncbi.nlm.nih.gov/articles/PMC13024114/
- Liu, Y. et al. (2024). **Instruction Position Matters in Sequence Generation with Large Language Models.** Findings ACL 2024. https://aclanthology.org/2024.findings-acl.693/
- Yang, M. et al. (2025). **How Is LLM Reasoning Distracted by Irrelevant Context? An Analysis Using a Controlled Benchmark.** EMNLP 2025. https://aclanthology.org/2025.emnlp-main.674/
- Yeo, W. J. et al. (2025). **Towards Faithful Natural Language Explanations: A Study Using Activation Patching in Large Language Models.** EMNLP 2025. https://aclanthology.org/2025.emnlp-main.529/

## Candidate naturalistic data

- Resume Bias Public (5,118 synthetic base resumes): https://huggingface.co/datasets/nghiemhnlp/bias_resume_public
- Companion pipeline/code: https://github.com/hnghiem-nlp/resume_bias_public
- Functional Ecology double-blind peer-review randomized-trial dataset (public domain): https://datadryad.org/dataset/doi%3A10.5061/dryad.m63xsj466

---

# 18. 最后一句研究判断

**现在最值得验证的并不是“LLM 也会被 inadmissible evidence 影响”这一条孤立结论。**

真正能把题目做大的，是下面这个更一般的命题：

> 当一个系统已经获取了一条对任务高度有用的信息，但随后又知道某条明确规则要求它不得在当前决策中使用这条信息时，LLM 是否能够把“知道”与“使用”分离？如果不能，失败是否取决于信息进入系统与 exclusion rule 出现的时间关系，失败具体发生在哪个内部阶段，又能否通过显式的信息门控机制修复？

**G0 的任务就是先决定这条命题在现实模型上到底是不是真的。只有它成立，后面的 interpretability 和 intervention 才值得做。**
