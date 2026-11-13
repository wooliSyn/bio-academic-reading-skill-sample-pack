---
name: paired-paper-reading-orchestration
description: 单篇论文精读成对产出的子代理编排流程：选篇→并行委派文献解读（academic-paper-reading）+背景解读（paper-background-research）两个子代理→主线程grep抽查→确定性星号转义→token记录。当用户要求精读一篇论文、要求"两个skill同时运行/成对产出"、或从周报TOP选篇精读时使用；周报批量检索本身不触发本技能。
version: 1.0.1
---

# 成对精读编排（paired-paper-reading-orchestration）

版本 v1.0.1（2026-11-14；可移植性泛化 + _shared 配套资产接线；源自 PRIMPOL/UNC13A 成对精读会话的稳定流水线）。

## 定位与边界

- 本技能是**编排层**，不是内容标准：内容质量以 `academic-paper-reading`（文献解读）与 `paper-background-research`（背景解读）各自 SKILL.md 为准。两个内容技能已强制"单篇深度精读默认双技能成对产出、不可只交其一"，本技能提供执行方法（HOW）。
- 分工不重复：文献解读 = PDF 内逐图精读 + 自足概念背景（课本化补注）；背景解读 = 作者谱系 / 研究传承 / 跨文献证据分级。两者交叉引用。
- 主线程纪律：**只做调度 / 抽查 / 决策，重型读写全部进子代理**（context-hiding）。这是单篇精读最大的 token/上下文节省手段。

## 工作流总览

```
- [ ] 0 加载配套资产（需求记忆+标杆，强制）
- [ ] 1 选篇（完整PDF必须存在）
- [ ] 2 轻量准备（一次提取复用，只回显统计）
- [ ] 3 并行委派（同一消息两个Agent调用）
- [ ] 4 主线程抽查（grep定位+targeted read，绝不整读）
- [ ] 5 星号转义（确定性脚本，两篇各跑一次）
- [ ] 6 token_log 记录
- [ ] 7 成对交付（PDF同目录）
```

## 步骤 0 — 加载配套资产（强制）

- 加载 `<技能目录>/_shared/requirement-memory.md`（任务质量需求 / 避坑 / 完成度要求），作为本次精读的质量基准。`<技能目录>` = 你所用 AI 存放技能的目录（依 AI 而定，不强制特定产品路径）。
- 质量对标参考 `<技能目录>/_shared/samples/` 的 PRIMPOL 标杆对（文献解读 + 背景解读）；新产出应达到同等深度（课本化背景补注 / figure 零基础自足 / 延伸图引清单 / 精度红线）。
- 若本次是"升级 / 回归"任务，转 `skill-regression-training` 闭环，并 Read `_shared/gap-report-example.md` 学差距清单格式。
- 子代理 prompt 中须写明"先加载 requirement-memory.md 与对应内容技能"，避免子代理漏载质量需求。

## 步骤 1 — 选篇

- 用户指定 PDF → 直接用。
- "精读周报 TOP / 文件夹里那几篇" → grep 周报导读定位优先级：pattern `重点精读|TOP|首选|优先精读|精读优先级|最值得|头条|封面`，确认对应 PDF 已在归档目录。
- 无完整 PDF → 不启动精读，标"待下载/待全文精读"，不得用摘要代替逐图精读。
- 多篇批量：逐篇成对；可多篇并行子代理、共享周报卡片线索减少重复检索（预算见 reference.md）。

## 步骤 2 — 轻量准备（主线程）

在 workspace 建 `<论文短名>/` 子目录：

- `fulltext.txt`：pymupdf 一次提取（pypdf 兜底），带 `===== PAGE N =====` 页标记；Bash 只回显页数/字符数，并记录各 PAGE 行号偏移供子代理 targeted read。**绝不把全文贴进主线程。**
- `figs/`：图页按需渲染（主图 ~140dpi、ED ~110dpi、局部 crop 300dpi）；补充材料未提供就不渲染。
- 已有 fulltext.txt（如此前试水产物）→ 直接复用，不重复提取。A/B 两子代理共享这份资产。

## 步骤 3 — 并行委派（核心）

**必须在同一消息内发出两个 Agent 调用**（并行，不是顺序）：

- 子代理 A：技能加载机制加载 `academic-paper-reading` → 产出 `<标题>_文献解读.md`
- 子代理 B：技能加载机制加载 `paper-background-research` → 产出 `<标题>_背景解读.md`

prompt 骨架（完整四变体模板见 [reference.md](reference.md)）：

```
你是[文献精读/背景研究]执行子代理。任务：…。高效执行。
## 加载技能：技能加载机制加载 `…`；不可用则直接 Read <技能目录>\<name>\SKILL.md
## 目标论文：PDF绝对路径 + 标题/期刊/年份/DOI
## 共享资产：workspace/<论文>/fulltext.txt（已提取，PAGE标记）+ figs/（复用，勿重复提取）
## 目标文件：输出路径（PDF同目录）；已存在 → 先重新Read当前磁盘版+备份到workspace再改
## 效率要求：复用提取文本；一次Write成稿少Edit；EuropePMC REST批量核证不用WebSearch；图按需渲染
## 返回格式：只回紧凑指标（字符/行数/panel数/概念数/refs数/token估算/未竟项），不回全文
## 核证通道：EuropePMC REST最稳；官方页urllib 403→WebFetch；CNIO需ssl放宽+429重试
```

- 新产出模式：B 独立从 PDF 提取 Pillar B 问题；若文献解读已存在，prompt 中给出路径令 B 吸收其 §五(三) 问题 seeding。
- 升级/修订模式：prompt 强调"增量打磨、不整文件重写"，列明目标版本差异条款；补注用锚点唯一性脚本插入。
- 子代理失败/超时：主线程只补做缺口部分，不接管整篇重写。

## 步骤 4 — 主线程抽查（grep 优先）

按 reference.md 的模式清单逐项：

1. 结构：grep `^#{1,3} ` 确认五模块（文献）/ Pillar A+B（背景）齐全。
2. 背景补注：grep `背景补注`（文献，课本化深度而非一两句话）。
3. 延伸清单：grep `延伸文献|对应本文Fig|一句话讲点`（文献文末）。
4. 引用一致性：`python scripts/check_deliverable.py <背景解读.md>`（refs used-vs-defined 全定义全引用）。
5. 事实抽查：grep fulltext.txt 核关键断言（作者串/PDB 码/关键数字）。
6. targeted read：只读 1–2 个 panel + 延伸清单，验"技术零基础自足性"。

发现问题 → 脚本/小段 Edit 定点修，或退回子代理修订；**不在主线程整文件重写**。

## 步骤 5 — 星号转义（确定性脚本，不让 LLM 手工转义）

```bash
python scripts/fix_asterisks.py "<目标md>" "<workspace备份目录>"
python scripts/check_stars.py "<目标md>"
```

- 原理：仅对"统计显著性语境"（前邻标点/数字/空白，后邻标点/数字/P</vs/NS 等）的 1–4 连星串转义为 `\*`；词邻的加粗/斜体不动。
- 安全：先备份；`：**` 加粗标签计数与加粗跨度计数前后一致，不一致即中止不写盘。
- 验收：raw 3+ 星号串 = 0；P/< 前裸星 = 0；剥离加粗/斜体/已转义后剩余裸星 = 0（或逐条人工确认属有意 markup）。
- **脚本中止（BOLD INTEGRITY BROKEN）= 存在可能被误伤的加粗**（如数字紧邻闭合 `**` 后接标点）：不写盘是正确行为。人工定位该处，先把显著性星号手动转义或改写加粗内容，再重跑；不得绕过断言。
- 两份交付物各跑一次。

## 步骤 6 — token_log 记录

写 `workspace/<论文>/token_log.md`（模板见 reference.md）：A/B 回报指标 + 分环节估算（提取/图渲染/技能加载/写作+Edit回显/核证）。

预算速查：**单篇成对 ≈ 3×10⁵ token**（A ~1.2–1.8e5，B ~0.8–1.6e5，两子代理并行）；主线程 ~5–12k。大型 Resource/图谱 3–5e5，分图块多子代理或先做筛选级背景。

节省铁律：重型读写进子代理；一次提取复用；grep 优于全读；Write 优于多次 Edit；EuropePMC 批量优于 WebSearch；星号转义用脚本；延伸清单前人图号可标"编号待核"省 20–40k（需要时另派轻量核证子代理补★条目图号）。

## 步骤 7 — 交付

- 两份 md 落在 PDF 同目录：`<标题>_文献解读.md` + `<标题>_背景解读.md`。
- file:// 链接 + 简短摘要（核心结论一句话 + 成对增量），不贴长文。
- **只产出其一 = 违反成对条款**，必须补齐另一份再交付。

## 关键陷阱

- 只交其一：用户说"精读这篇"即默认双份，不要问"要不要背景解读"。
- 主线程整读交付物：50–70k 字符整读即上下文膨胀；抽查永远 grep + targeted read。
- LLM 手工转义星号：漏转/误伤加粗不可避免，用确定性脚本。
- Edit 回显：大文件每次 Edit 回显巨量更新后文本；子代理须一次 Write 成稿、控制 Edit 次数。
- 子代理回传全文：prompt 必须写明"只回指标"。
- WebSearch 核证：SEO 垃圾浪费 token，用 EuropePMC REST 批量。
- 顺序委派：两个 Agent 调用分两条消息发就失去并行意义。

## 辅助文件

- [reference.md](reference.md)：四变体 prompt 模板、抽查 grep 模式清单、token 预算细则、核证通道避坑、token_log 模板。
- `scripts/fix_asterisks.py`、`scripts/check_stars.py`、`scripts/check_deliverable.py`：**执行**，不是阅读参考。