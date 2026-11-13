# Reference — 成对精读编排

SKILL.md 的详细参考：四变体子代理 prompt 模板、抽查模式清单、token 预算细则、核证通道避坑、token_log 模板。占位符用 `{}` 标注，委派前全部替换为实际值。

## 1. 子代理 prompt 模板（四变体）

### 1A. 文献解读 — 新产出

```
你是文献精读执行子代理。任务：用 academic-paper-reading skill 对一篇 {期刊} 论文做完整逐图精读，产出中文《文献解读.md》。高效执行。

## 第一步：加载技能
用技能加载机制加载 `academic-paper-reading`。严格遵循其五模块结构与四字段图解读模板。若 技能加载机制不可用，直接 Read 技能文件 <技能目录>\academic-paper-reading\SKILL.md。

## 目标论文
PDF: {PDF_PATH}
{TITLE}. {期刊} {年份}, DOI {DOI}。

## 共享资产（已备好，复用，勿重复提取）
全文: {WORKDIR}\fulltext.txt（===== PAGE N ===== 标记，{N}页/{CHARS}字符；各PAGE行号偏移：{OFFSETS}）
图资产: {WORKDIR}\figs\（主图+ED已渲染；缺图按需 pymupdf 渲染：主图~140dpi、ED~110dpi、局部crop 300dpi）

## 输出
{OUT_PATH}（PDF同目录 <标题>_文献解读.md）
五模块齐全：一、基础概念注释 / 二、核心问题与方案 / 三、逐节精读（每panel四字段：图片解释/横纵轴/内容逻辑/核心结论）/ 四、Discussion结构分析 / 五、重点思考（含面向阅读的核心提问seeding + 文末延伸文献与图引清单）+ 解读完成度声明。
核心因子/前人工作给课本化背景补注；figure解读通过"技术零基础自足性"检验；统计显著性星号写字面 \*；保持学术密度，大白话直觉是补充非替代。

## 效率要求
- 复用 fulltext.txt，按 PAGE 行号 targeted read，不反复整文件 Read。
- 一次 Write 成稿，尽量少 Edit（Edit 会回显大段更新后文本）。
- 图按需渲染，不全页渲染；未提供的补充材料不渲染、在完成度声明中注明。
- 需联网核证时用 EuropePMC REST 批量（python urllib 脚本一次查多篇存JSON），不用 WebSearch。

## 返回格式（重要）
只回紧凑指标：产出字符数/行数、主图X幅Y panel四字段、ED Z panel、概念N条、延伸清单N条(★N)、token估算、未竟项/诚实声明要点。不要回传解读全文。
```

### 1B. 文献解读 — 升级/修订（文件已存在）

```
你是文献精读升级子代理。任务：把已完成的《文献解读.md》升级到 academic-paper-reading skill v{X} 标准。高效执行。

## 加载技能
技能加载机制加载 `academic-paper-reading`（v{X}），重点 {目标条款，如：§1.7 课本化背景补注/星号转义/文体平衡、§4.2三 figure技术零基础自足性、重点思考(四)延伸文献图引清单}。兜底 Read 路径同上。

## 目标文件（已存在，先重新 Read 当前磁盘版 + 备份到 {WORKDIR}）
{OUT_PATH}（约{CHARS}字符，{现状摘要：模块/panel/概念数/已有与缺失}）
PDF原文: {PDF_PATH}；全文提取: {WORKDIR}\fulltext.txt（复用）

## 修订纪律
- 增量打磨，不整文件重写；只改差异处。
- 补注用锚点唯一性插入脚本：先校验锚点 count==1 与可逆性，再一次写盘；写前备份。
- 保持已转义星号(\*)与加粗标签(：**) intact；新增统计星号同样写 \*。

## 效率要求 / 返回格式
同新产出模板（一次Write/少Edit、只回指标：增量字符数、补注处数、转义星号数、token估算）。
```

### 1C. 背景解读 — 新产出

```
你是文献背景研究子代理。任务：为 {TITLE} 论文产出配套的《背景解读.md》（深度模式）。用 paper-background-research skill。高效执行。

## 加载技能
用技能加载机制加载 `paper-background-research`，按 Pillar A（范围方法四类证据/一瞥/作者谱系/研究谱系含史前层与缺口命运层/新在哪/caveats/收束/阅读顺序精确到fig/逐文献证据索引表/References）+ Pillar B（问题精研+每问建立/推断/未知三分+scorecard+后续实验）完整展开。若 技能加载机制不可用，直接 Read <技能目录>\paper-background-research\SKILL.md。

## 目标论文
PDF: {PDF_PATH}；{TITLE}. {期刊} {年份}, DOI {DOI}。
共享资产: {WORKDIR}\fulltext.txt + figs\（复用，勿重复提取）。

## 成对分工
同源《文献解读.md》负责 PDF 内逐图精读；本文件只补 PDF 之外的作者谱系、研究传承、创新定位与跨文献问题精研，交叉引用、不重复逐图。
{若文献解读已完成：吸收其 §五(三) 问题 seeding，路径 {LIT_PATH}；否则：独立从 PDF 提取 Pillar B 问题，主线程事后对齐交叉引用。}

## 核证通道
- EuropePMC REST（resultType=core，批量脚本一次查N篇存JSON）：题录/作者串/摘要/firstPublicationDate。
- 作者谱系用机构/实验室官方页、CV、学位论文记录；严格区分导师关系/技术传承/同领域团队/本次合作，不由共同署名推断师承；核不到留空白，不编造。
- 官方页 urllib 403 → 改 WebFetch；CNIO 需 ssl 放宽 + 429 重试。
- 不用 WebSearch 做主力核证（SEO垃圾）。

## 输出
{OUT_PATH}（PDF同目录 <标题>_背景解读.md）。统计显著性星号写字面 \*；成品不自引技能红线编号；每篇外部文献标阅读深度；图号核不到写"编号待核"。

## 效率要求
批量核证（一个python脚本查完存JSON再读）；一次 Write 成稿少 Edit；嵌入外部图才渲染，不重做本文图。

## 返回格式（重要）
只回指标：字符数/行数/refs数、Pillar A/B 节齐全度、核证查询数与成功率、未裁决缺口列表、token估算。不要回传全文。
```

### 1D. 背景解读 — 升级/修订

```
你是文献背景研究升级子代理。任务：把已完成的《背景解读.md》升级到 paper-background-research skill v{X} 标准（{现状：已是vY版、结构齐全度}，本次主要是增量打磨）。高效执行。

## 加载技能
技能加载机制加载 `paper-background-research`（v{X}），重点 {目标条款，如：§6文体 星号转义/学术平衡、§3.7阅读顺序精确到fig、§3.0四类证据、Pillar A课本化背景}。兜底 Read 路径同上。

## 目标文件（已存在，先重新 Read 当前磁盘版 + 备份）
{OUT_PATH}（约{CHARS}字符/{LINES}行/{REFS}条References，{已有结构摘要}）
PDF: {PDF_PATH}；fulltext: {WORKDIR}\fulltext.txt；配套文献解读: {LIT_PATH}

## 修订纪律
增量打磨不整写；新增引用先批量核证再写入；refs 编号连续且 used==defined（脚本校验）；保持学术密度与全部数据，不删细节。

## 效率要求 / 返回格式
同新产出模板（只回指标：增量字符、新增refs、核证成功率、token估算）。
```

## 2. 主线程抽查 grep 模式清单

| 检查项 | 文件 | 模式/命令 | 通过标准 |
| --- | --- | --- | --- |
| 模块结构 | 文献解读 | `^#{1,3} ` | 五模块标题齐全 |
| 模块结构 | 背景解读 | `Pillar A|Pillar B|References|诚实收尾` | 各≥1 |
| 课本化补注 | 文献解读 | `背景补注` | 核心因子处均有，非一两句话 |
| 延伸清单 | 文献解读 | `延伸文献|对应本文Fig|一句话讲点|编号待核` | 文末清单存在、六列紧凑表 |
| 星号 | 两篇 | `[（(，,]\s*\*{1,4}|\*{1,4}\s*[）)]` | 命中→交脚本转义 |
| 引用一致性 | 背景解读 | `python scripts/check_deliverable.py <md> --bg` | used−defined=∅ 且 defined−used=∅ |
| 事实抽查 | fulltext.txt | 作者姓/PDB码/关键数字（如 `5L2X|7PFO|30AR`） | 解读断言与原文一致 |
| 加粗完整 | 两篇 | `：**` 计数 | 转义前后一致 |
| 质量抽读 | 两篇 | targeted read 1–2 panel + 延伸清单 | 技术零基础自足 |

## 3. Token 预算与节省细则（实测锚点：UNC13A/PRIMPOL，2026-11-13/14）

### 分环节实测（单篇文献解读子代理，4主图级 Nature 论文）

| 环节 | 量 | 估算 token |
| --- | --- | --- |
| PDF 全文提取（43页，一次提取复用） | 162,086 字符 | ~40,000 |
| 图渲染（主图4@140dpi + ED7@110dpi + crop1@300dpi） | 12 PNG | ~15,000 |
| 技能加载（SKILL.md 全文） | ~50 KB | ~15,000 |
| 长文写作 + Edit 回显 + 上下文累积 | 输出 56,561 字符 | ~100,000 |
| 子代理合计 | ~25 次工具调用 | ~1.8×10⁵ |

### 预算速查

- 单篇研究论文精读（4主图级）：子代理 ~1.5–2×10⁵；主线程 ~5–10k。
- 背景解读（联网核证）：~0.8–1.5×10⁵（视核证深度）。
- **单篇成对（文献+背景，两子代理并行）：≈3×10⁵**；主线程 ~8–12k（含 patch/脚本/抽查）。
- 大型 Resource/图谱（200+ refs/数十图）：3–5×10⁵，分图块多子代理或先做筛选级背景。
- 递归自训练一轮（差距分析+patch+回归）：~1–2×10⁵；回归只改差异处。
- 课本化深度背景使文献解读 +~17% 体量，属用户明确要求的必要成本。
- 三篇批量成对 ≈9×10⁵：三篇并行子代理、共享周报卡片线索减少重复检索。

### 七条节省策略

1. 重型读写进子代理，主线程只拿摘要+指标——总 token 不减，但主上下文不膨胀、不触发 compaction（压缩后丢细节需重读，反而更贵）。
2. Edit 回显是最大可省项：一次 Write 成稿或 Bash 追加；必须 Edit 时控制次数。
3. PDF 文本只提取一次复用，不反复整文件 Read。
4. 图按需渲染、适中 DPI；未提供的补充材料不渲染。
5. 抽查用 grep 定位 + targeted read，不整文件读。
6. 检索用 EuropePMC REST 批量，不用 WebSearch（SEO 垃圾）。
7. 延伸清单前人图号核证是可选增量（全核约 +20–40k）：默认标"编号待核"，需要时对★必读条目另派轻量核证子代理。

## 4. 核证通道避坑

- **EuropePMC REST**（最稳，批量主力）：`https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=...&format=json&pageSize=N&resultType=core`；query 支持 `DOI:"..."` / `EXT_ID:PMID` / `TITLE:"..."` / `AUTH:"..." AND PUB_YEAR:YYYY`。写一个 python 脚本批量查 N 篇存 JSON，再按需读字段。
- **NIH RePORTER**（基金/PI 核证）：`POST https://api.reporter.nih.gov/v2/projects/search`，criteria 用 `pi_names` 或 `project_nums`。
- **官方页**：urllib 带 Mozilla UA；403 → 改 WebFetch（实例：chistol.stanford.edu urllib 403 但 WebFetch 可达）；CNIO 需 `ssl._create_unverified_context()` + 429 sleep 重试；eScholarship/Walter lab 页 403 未破 → 相关内容标"未核实"，不编造。
- **WebSearch**：质量差（SEO 垃圾），仅最后手段。
- ORCID expanded-search 可旁证作者履历，但师承关系仍须官方页/新闻帖证实。

## 5. token_log.md 模板

```markdown
# {论文短名} 成对精读：Token 损耗记录

日期：{DATE} ｜ 技能：academic-paper-reading v{X} + paper-background-research v{Y} ｜ 执行方式：两子代理并行（context-hiding）

## 1. 子代理回报指标
| 子代理 | 产出 | 估算 token | 最耗环节 |
| --- | --- | --- | --- |
| A 文献解读 | {chars}字符/{lines}行；主图{X}幅{Y}panel四字段+ED{Z}panel；概念{N}条；延伸{M}条(★{K}) | ~{...} | {…} |
| B 背景解读 | {chars}字符/{refs}条refs；Pillar A+B | ~{...} | {…} |
| 主线程 | 准备+抽查+星号脚本+本记录 | ~{5–12k} | {…} |

## 2. 分环节估算
{提取/图渲染/技能加载/写作+Edit回显/核证，各给量与token}

## 3. 节省点与超支点
{本次做到/没做到的节省策略；超预算环节及原因}

## 4. 结论
{单篇成对总预算核对（基准≈3×10⁵）；下次改进}
```