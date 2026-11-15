# 文献精读 skill sample pack（生物医学 / 生命科学）

一套可移植的"论文精读 + 背景解读"技能与标杆样例（源论文 PDF 因版权不随包分发，按 `_shared/papers/README.md` 的 DOI 自行下载）。换 AI、换电脑、分享给他人时，**按你所用 AI 的默认方式装入**，即可让接收方 AI **盲跑 → 对标 → 自我调优**，复现同等质量的解读。本包不绑定任何特定产品。

## 给 AI 的执行须知（先读这段）

装好技能后，务必做到：

1. **加载需求记忆**：`<技能目录>/_shared/requirement-memory.md`。它规定文体、深度、格式、完成度与精度红线，是质量基准。
2. **成对产出**：精读一篇论文时，按 `paired-paper-reading-orchestration` 同时产出 `_文献解读.md` + `_背景解读.md`（不可只交其一）。
3. **真正跑盲跑对标自训练**（见下节）：先按 `_shared/papers/README.md` 的 DOI 下载源 PDF 放入 `_shared/papers/`，再盲跑并对照 `_shared/samples/` 标杆，按自己的理解改技能。**不能只装技能、不读配套文件、不训练。**

## 安装（按你的 AI 默认方式，不强制特定目录）

`<技能目录>` 指**你所用 AI 存放技能 / 插件的目录**，依 AI 而定：有的用固定技能目录（如 `~/.claude/skills/`、`~/.<ai>/skills/`），有的用配置 / 规则目录或技能管理界面导入。遵循该 AI 的默认约定，**不要强行创建某个特定产品的目录**。

把 `skills/` 下**全部内容**（4 个技能目录 + `_shared/`）装入 `<技能目录>/`：

```bash
cp -r skills/* <技能目录>/     # 路径以你的 AI 为准
```

装好后应含：`academic-paper-reading/`、`paper-background-research/`、`paired-paper-reading-orchestration/`、`skill-regression-training/`、`_shared/`。**`_shared/` 不可漏装**（需求记忆 + 源 PDF 下载指引 + 标杆 + 差距范例都在其中）。

| 技能 | 作用 |
| --- | --- |
| **academic-paper-reading** (v6.4) | PDF 内逐节逐图精读 → `_文献解读.md`（五模块 + 四字段图解读 + 课本化背景补注 + 延伸图引清单） |
| **paper-background-research** (v1.4) | PDF 外作者谱系 / 研究传承 / 跨文献证据分级 → `_背景解读.md`（Pillar A + B） |
| **paired-paper-reading-orchestration** (v1.0.1) | 成对子代理编排 + 确定性校验脚本（星号转义 / 引用对账 / 交付物检查） |
| **skill-regression-training** | 盲跑对标自训练闭环 + sample pack 导出规范 |

## 递归自训练（盲跑对标协议）——必须实际执行

目标：让接收方 AI 把技能调到"**自己能稳定跑出标杆质量**"。不是机械复制补丁，而是**按自己的理解**把条款改成适合本 AI 能力与风格的样子。

准备：按 `_shared/papers/README.md` 的 DOI 下载源 PDF 放入 `_shared/papers/`；`_shared/samples/` 有标杆解读。**盲跑阶段不要先看标杆解读。**

**轮 1（训练篇 = PRIMPOL）**

1. **盲跑**：用当前技能对 `_shared/papers/` 的 PRIMPOL 主 PDF（+ companion）成对精读，产出自己的文献解读 + 背景解读（不看标杆）。
2. **对照**：Read `_shared/samples/` 的 PRIMPOL 标杆对，逐节解析差距（A 事实错误 / B 遗漏 / C 概念层 / D 方法缺口）。
3. **生成分析文件** `gap-analysis-round1.md`：差距清单 + 标杆证据摘录 + 我方现状 + 拟改条款。
4. **按自己的理解改技能**：clause 级 patch（grep 确认 old_string）+ 版本三处同步 + grep 落位校验。
5. **回归**：用改后技能重跑 PRIMPOL，生成 `gap-analysis-round1-regression.md`，比对差距是否闭合。

**轮 2（验证篇 = UNC13A）**

6. 盲跑 UNC13A → 对照 UNC13A 标杆 → 生成 `gap-analysis-round2.md`。
7. 达标 → 收敛；仍不足 → 分析问题 → 继续改技能 → 再回归（每轮生成 `gap-analysis-roundN.md`）。

**升级**：连续多轮仍不达标，或差距源于现有标杆未覆盖的维度 → **向用户请求更多标杆**（说明缺哪类样例 / 哪类论文）。`samples/` 会随精读案例持续更新：目前除 PRIMPOL（训练）与 UNC13A（验证）外，已扩充核孔 FG 屏障（*Nature*）与基底神经节单细胞多组学图谱（*Cell*）两对标杆，可作为第三轮起的训练/验证素材（源 PDF 的 DOI 见 `papers/README.md`）。

**铁律**：每次回归调用都必须生成一份分析文件留痕；盲跑先于对标；改技能按本 AI 理解而非照抄。完整规程见 `skill-regression-training/SKILL.md` + `reference.md`；`gap-report-example.md` 是历史实例。

## 内容清单

```
skill-sample-pack/
├── README.md
└── skills/
    ├── academic-paper-reading/SKILL.md           (v6.4)
    ├── paper-background-research/SKILL.md        (v1.4)
    ├── paired-paper-reading-orchestration/       (SKILL.md v1.0.1 + reference.md + scripts/)
    ├── skill-regression-training/                (SKILL.md + reference.md)
    └── _shared/
        ├── requirement-memory.md                 # ★需求记忆（任务需求/避坑/完成度，非个人）
        ├── gap-report-example.md                 # 自训练历史实例
        ├── papers/                               # ★源 PDF 下载指引（盲跑用）
        │   └── README.md                         # 5 篇论文 DOI + 放置文件名（PDF 因版权不随包分发）
        └── samples/
            ├── ...PRIMPOL_文献解读.md + _背景解读.md   # ★标杆对（训练篇）
            ├── PRIMPOL_背景解读_companionFig4.png      # 仅 figure+图注（已裁剪）
            ├── ...UNC13A_文献解读.md + _背景解读.md    # 验证篇标杆
            ├── ...FG barrier..._文献解读.md + _背景解读.md        # 扩充标杆对（*Nature* 2026，核孔 FG 屏障）
            └── ...basal ganglia atlas..._文献解读.md + _背景解读.md # 扩充标杆对（*Cell* 2026，单细胞多组学图谱）
```

## 截图 / 嵌图规范（尤其注意）

嵌入文献图时**只截 figure 本身 + 对应图注 / 解读**，**不要截含大量正文的整页**。整页渲染须裁剪到图区（含图注），去掉下方正文段落。本包 `companionFig4.png` 已按此裁剪（仅 Fig.4 a–d + 图注）。

## Token 效率（经验教训）

核心教训：**主线程亲自精读会撑爆上下文**（PRIMPOL 首轮即触发压缩）。改为子代理委派后主线程保持精简。

| 环节 | 量级 | 说明 |
| --- | --- | --- |
| 单篇成对（文献 + 背景） | ≈ 3×10⁵ token | 文献子代理 ~1.2–1.8×10⁵ + 背景子代理 ~0.8–1.6×10⁵，并行 |
| 主线程（调度 / 抽查 / patch） | ~5–12k | 只收摘要 + 指标，不整读交付物 |
| 大型 Resource / 图谱 | 3–5×10⁵ / 篇 | 分图块多子代理，或先做筛选级背景 |

**最耗环节**：长文写作 + Edit 结果回显（占一半以上）；真正不可省的只有生成解读文本本身。

**节省铁律**：重型读写进子代理；一次 Write 成稿优于多次 Edit；grep 定位 + 定向 Read 抽查；PDF 文本提取一次复用；确定性校验用脚本；EuropePMC REST 批量优于 WebSearch；延伸清单前人图号可标"编号待核"省 20–40k（需要时另派轻量子代理补★条目）。

## 诚实与精度

通道受阻项保守标"参考提供 / 编号待核"，不编造图号 / 日期 / 贡献声明；弱效应（P=0.052）不美化；PDF 日期占位符非权威；等贡献脚注不升格为共同一作；成品不自我引用技能内部红线编号。详见 `_shared/requirement-memory.md` §6。

## 已知事项

- `check_stars.py`（v2）先剥离合法 markup（已转义 / 加粗 / 英文斜体 / 中文斜体≤300）再判裸星，消除 `：**` 标签与期刊斜体假阳性；四份标杆样例均 PASS。
- `fix_asterisks.py`（v2）保护优先：先修复历史误转义的加粗开头、再保护加粗 / 斜体跨度、只转义保护圈外显著性星号；以加粗标签 / 跨度计数前后一致为安全断言，中止即不写盘，不得绕过。