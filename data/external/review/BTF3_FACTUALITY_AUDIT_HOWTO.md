# 事实性审计操作手册（BTF-3 packet factuality audit v1）

给外部审计者的完整流程。协议正文：`PROTOCOL_BTF3_PACKET_FACTUALITY_AUDIT.md`。

## 0. 这件事在回答什么

数据集里每条题目都带一段 `resolution_explanation`（下称 packet），它是**机器生成**的，
源数据集自己声明只做过部分抽查。我们在选样时对它做过一道"事实有效性"门，但那道门
**没有打开任何 citation**（ledger 里明确写了 `No external lookup was used`）。

所以审稿人可以问：你凭什么说这 256 条 packet 事实上成立？

这次审计就是去打开引用、真的核对。**它不改变样本**——查出错也不删题。

## 1. 三条硬规则

1. **不许看模型输出。** 不要打开 `results/raw/` 下的任何文件。
2. **不许改样本。** 审计结论不会移除或替换 256 条中的任何一条。
3. **不许改抽样。** 这 64 条是在任何 citation 被打开之前用哈希固定的
   （`SHA256("btf3-factual-audit-v1:" + question_id)`，每个结果桶取前 32），
   已经提交并打了 tag `g2-packet-factuality-audit-protocol-v1`。不要增删。

## 2. 文件

| 文件 | 用途 |
|---|---|
| `btf3_factuality_audit_v1_remaining.md` | **从这里开始**：48 条尚无判定的题目，含题面、判定标准、packet 全文和勾选框 |
| `btf3_factuality_audit_v1_verdicts.md` | **判定写在这里**（唯一被程序解析的文件） |
| `btf3_factuality_audit_v1_sample.json` | 抽样清单与哈希，只读 |
| `btf3_factuality_audit_v1_{yes,no}.md` | 完整 64 条（含已审的 16 条），备查 |

已完成 16 条（全部 realized YES 桶的前段），结果 16 PASS。**剩余 48 条**：
realized YES 16 条 + realized NO 32 条。

## 3. 每条怎么审

先读题面和判定标准，再读 packet，然后**打开 packet 自己引用的来源**核对五项：

1. 记录的结果（YES/NO）对不对；
2. 引用的来源是否真的存在、是否真的支持 packet 说它支持的内容；
3. packet 依赖的证据有没有晚于该题的结算截止时间；
4. packet 内部有没有时间逻辑错误；
5. 判定标准与所称结果是否真的对得上。

**效率建议**：先查那个能一锤定音的事实（选举谁赢了、利率有没有加、法院有没有判），
一般一两次检索就够；只有当结果本身可疑时才逐条追引用。单条大约 5–10 分钟。

对"没有发生某事"类的 NO 题：确认在窗口内确实没有发生该事件即可，**不要求**穷尽证明；
packet 若声称某个 tracker/官方索引覆盖了窗口，就去核对那个来源的更新日期。

## 4. 判定与写法

三选一，**每条只勾一个**：

- `PASS` —— 没有实质错误。**表述性瑕疵不算实质**（例：数字笔误、日期差一天、
  措辞松散），发现了写进 Note 即可。
- `MATERIAL_ERROR` —— 有一项或多项检查不通过，且**足以改变结果或抽掉其支撑**
  （例：结果本身写反、引用的报道不存在、关键证据晚于截止日）。
- `UNVERIFIABLE` —— 引用的来源打不开或已消失，无法核对。

写进 `btf3_factuality_audit_v1_verdicts.md`，格式必须**逐字**如下（脚本按这个解析）：

```markdown
### NO-1. `d2c5fcaa-b273-5787-9846-32c25c11f11b`
- Verdict: `[x] PASS  [ ] MATERIAL_ERROR  [ ] UNVERIFIABLE`

### NO-2. `987d2afa-...`
- Verdict: `[ ] PASS  [x] MATERIAL_ERROR  [ ] UNVERIFIABLE`
- Reason: 一行原因，MATERIAL_ERROR 和 UNVERIFIABLE 必填。
```

编号与 `question_id` 必须和抽样清单一致，不要重新编号。

审计者请在文件抬头补上：**姓名/身份、审计日期、可用的检索手段**（能不能上网、
有没有付费墙来源）。这一行不写，整份 ledger 在审稿人眼里没有价值。

## 5. 审完之后

```bash
python scripts/analyze_btf3_factuality_audit.py --results results/raw/isr_*_btf3_large_replication_v1.jsonl
```

脚本会解析 ledger、按预注册规则给出行动建议，并算一个**二级**敏感性分析
（把被标记的题剔除后重算 intrusion，仅作稳健性展示，永远不替代主结果）。

预注册的行动规则（`E` = MATERIAL_ERROR 条数）：

| 结果 | 行动 |
|---|---|
| `E ≤ 2` | 可接受，报告原始数字，不扩大审计 |
| `3 ≤ E ≤ 6` | 报告数字并给出剔除敏感性分析，样本仍不变 |
| `E ≥ 7` | 停下来，做 256 条全量外部审计，并把错误率写进 limitations |

`UNVERIFIABLE` 单独统计，不计入 `E`；若超过 8/64，则作为"可核验性"的局限报告。

## 6. 论文里怎么写

允许：*"The preregistered audit did not trigger expanded review (E/64 material
errors, exact binomial 95% CI […])."* 并附原始计数。

禁止：*"factual validity was established."* ——2/64 的精确二项上界仍有约 10.8%，
这个审计能证明的是"没有触发扩大审查"，不是"packet 事实上都对"。
