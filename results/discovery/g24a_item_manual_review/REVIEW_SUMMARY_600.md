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
| fix_claim（claim 改写，**已写入条目文件**；prompt 变 → 全量重跑，见 §五） | **52** |
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

## 五、数据影响与处置（用户裁决 2026-09-25）

1. **52 条 fix_claim：改写保留，已写入条目文件。**（先口头定过「恢复原 claim」，随即被后续指令取代，撤销未执行即作废。）新 claim 已写入 `data/items/g24a_v1.jsonl` 的 `base_context`（52 行）；序列化往返字节校验通过，其余 548 行逐字节未动。台账 `claim_old` 按条目文件原文校正 1 条（#519 `g24a_scifact_855`，原台账记成 “among transplant patients”，实际为 “after solid organ transplantation.”）。
2. **4 条 flip：`critical_direction` 已写入条目文件**（4 行）。条目文件合计改动 56 行（git diff --numstat 56/56），事后程序校验：52 条 base_context == claim_new、4 条方向 == direction_new，0 例外。
3. **全部 600 条 × 5 模型用新条目全量重跑**（用户裁决，取代补测/剔除两个旧选项）；旧 raw（`results/raw/*_g24a.jsonl`）随重跑覆盖（git 历史保留旧版）。selection pass 跑的是未改动的 13,283 条候选池，不重跑。
4. **旧分析产出全部弃用并已删除**，重跑完成后从头重新生成：
   - `results/discovery/g24a_phenomenology_v1.{md,json}`、`_figs.json`、`_itemmodel.csv`、`results/discovery/figs/*.png`（现象学地图）；
   - `results/discovery/g24a_data_quality_audit_v1.{md,json}`（数据质量审计）；
   - `results/g24a/g24a_analysis_v1.{md,json}`（主分析）。
5. **0 条 drop**：没有不可修复项。
6. 人工判读记录（`batch_001_100.md` … `batch_006_600.md`、本文件、`dispositions.jsonl`）**保留**为审查依据：台账中 fix 条目存有原/新 claim 全文，是改写内容的唯一权威来源。
