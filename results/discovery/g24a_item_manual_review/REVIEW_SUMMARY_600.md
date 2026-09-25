# G24A 人工判读全量汇总（600/600）

判读文件：`batch_001_100.md` … `batch_006_600.md`（逐条 OK / ⚠ / ✗ / FIX / flip / DROP）；
处置台账：`dispositions.jsonl`（56 条，全部 item_id 经字节核对存在于 `data/items/g24a_v1.jsonl`）。

判定线（batch 3 起成文并严格执行）：
(a) 证据**正面断言**与 claim 冲突/覆盖 → OK；
(b) 术语变体、回指、页面语境可合理绑定 → OK（注明）；
(c) claim 的具体事实在证据中缺席、时态/范围/对象错位 → FIX（改写到证据正面冲突，措辞自然）；
证据实际**支持**被标为 REFUTES 的 claim（或反之）→ flip（只改 `critical_direction`，prompt 不动）。

## 一、总量

| 项 | 数量 |
|---|---|
| 判读条目 | 600 / 600（6 批 × 100） |
| 保持原样（OK，含带注明） | **544**（其中带注明 44） |
| flip_direction（只改方向元数据，prompt 不变，**raw 行有效**） | **4** |
| fix_claim（claim 改写，**prompt 变 → 旧行陈旧**） | **52** |
| drop | **0** |

分层与方向（设计是完全平衡的）：

| stratum | n | label 方向 | FIX | flip |
|---|---|---|---|---|
| fever/SUPPORTS | 200 | increase | 11 | 2 |
| fever/REFUTES | 200 | decrease | 13 | 2 |
| scifact/SUPPORT | 100 | increase | 22 | 0 |
| scifact/CONTRADICT | 100 | decrease | 6 | 0 |
| 合计 | 600 | 300↑/300↓ | **52** | **4** |

## 二、方向倒置（flip ×4）——只出现在 FEVER，且两个标签方向各 2 条

| item | stratum | 原方向 → 新方向 | 证据实际语义 |
|---|---|---|---|
| g24a_fever_20847 (#66) | fever/SUPPORTS | increase → decrease | 包含/从属方向反读（证据不支持 claim） |
| g24a_fever_90151 (#86) | fever/SUPPORTS | increase → decrease | 时间先后关系反读 |
| g24a_fever_24795 (#225) | fever/REFUTES | decrease → increase | 证据两次年度第一 → claim 为真（FEVER REFUTES 与其自身证据冲突） |
| g24a_fever_58608 (#320) | fever/REFUTES | decrease → increase | 六年 > 半个十年 → claim 为真 |

**聚类结论**：方向倒置 4/4 全在 FEVER，SciFact 0 条；且在 FEVER 内对 SUPPORTS 与 REFUTES 两个标签**对称出现**（各 2 条）——不是单向标注偏差，而是 FEVER 上游 label 与证据语义的零散脱钩（0.4%–1% 量级）。flip 条目 prompt 未变，现有 raw 行全部有效，分析时只改 E 符号。

## 三、claim 改写（fix ×52）——按缺陷类别

| 类别 | 约计 | 例 |
|---|---|---|
| 错字/拼写/正字法 | 15 | the the、a a、effects→affects、Lice→Live、10EB→10E8、An Educated→An Education、indictivate、coavtivator、PKG/PGK 倒置 ×2 |
| 具体事实超出证据（时间、数量、人群、部位、机制、剂量、比较对象） | 24 | 1992、90th、American、elderly、hemodialysis、2001、brain/animals、locomotor→axonal transport、RhoA、tonic signaling、H3K9me3、40mg/2mg |
| 对象/命题错位（证据沉默或谈另一件事） | 13 | 时态错位（#303 had vs 现行描述）、范围错位（#334 州 vs 山脉）、预测 vs 治疗（#519）、clomiphene vs DES（#547）、ubiquitination vs phosphorylation（#581）、出血 vs 心血管（#588）、平凡真（#347） |

分层修复率：SciFact SUPPORT 22%（信息密度最高——一条 claim 常含 3–4 个可核查点，证据块只承载核心关系）；SciFact CONTRADICT 6%；FEVER 约 6%。
**SciFact 源式希腊字母转写（av-Beta3=αvβ3 等）判为上游系统格式，不逐条改。**

## 四、交叉印证

- **#323**（`is 8 years old` 相对日期断言）人工判读认定时间脆弱 → 改绝对年份；这正是数据质量审计 temp-0 重测实证 rationale 翻转（6 年→false / 8 年→true）的那一条。人工/机器两条线独立收敛到同一缺陷。
- FEVER 可疑 claim 的 provenance 抽查（#104/#119/#125/#136/#157）全部 FEVER 原文 → 缺陷在上游，不在构造。
- 对偶条目（同 claim 支持/矛盾双版本，如 #415/544、#425/576、#460/562、#464/567、#490/578、#491/577、#497/583）是 G24A 设计特征，非重复缺陷。

## 五、数据影响与待决事项

1. **52 条陈旧行**：fix_claim 使 prompt 文本改变，现有 raw 行跑的是旧 claim，**当前分析一律不可用**。待用户裁决：
   - 方案 A：小型补测重跑（52 条 × 现有 5 模型，GPU 量很小）补齐；
   - 方案 B：分析时整条剔除（等价于 600 → 548）。
2. **4 条 flip**：prompt 未变，raw 行完全有效；分析时按新方向计算 E 符号即可，无需重跑。
3. **0 条 drop**：没有不可修复项。
4. 若执行方案 A，需在结果文件中区分「原跑」与「补跑」行的批次标记（建议 run 时间戳或 `repair=true` 字段），并在读取层强制 fix_claim 条目只认补跑行。
