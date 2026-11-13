# PRIMPOL 背景解读：技能差距分析与回归报告

**比对对象**：参考报告 `%USERPROFILE%\Downloads\report_primpol_background_zh.md`（检索截止 2026-11-13，32 篇关键文献证据索引）vs 本会话产出《The molecular basis of replication fork restart via repriming by PRIMPOL_背景解读.md》（v1.1 技能产出）与配套《..._文献解读.md》（v6.1 技能产出）。
**任务链**：分析不足 → 生成本报告 → 修改 skill → 回归调用更新后 skill 修订两份解读 → 回归比对（§4–§6，回归执行后追加）。
**方法**：逐节对照参考报告与两份产出；对参考报告提出的每一项新事实做独立外部核证（机构页/学位论文记录/ EuropePMC core / RCSB / 实验室官网），核证结果决定差距定性（"我错"/"我漏"/"参考亦未证"）。

---

## 1. 总体判定

参考报告与本产出是**两种互补的强项结构**，不是简单的优劣关系。

参考报告强在**历史纵深与训练谱系的完整性**：把领域史前推到 1968（Rupp–Howard-Flanders 复制后缺口）与 2011（Elvers 纤维≠连续性），把"缺口命运/补缺网络"（Tirman 2021、Piberger 2020、Mellor 2024、Bai 2020）作为独立概念层，把作者训练核到学位论文与个人 CV 级（Bustamante、Salas+Blanco、Stillman 年限、Park 的 GIST/SNU），并给出阅读顺序、逐文献阅读深度声明与"四类陈述"证据分类。其最锋利的一条精度纠正是：**等贡献 footnote 只覆盖 Lynch 与 Blanco-Romero，不等于与 Park 共同一作**——这正是本产出的事实性错误。

本产出强在**结构/资助/机制分级的核证深度**：RCSB 逐条目核对（30AR 无 DNA、ZnF/RBM 不可见、DNA 路径为 5L2X+7PFO 叠合模型、Fig. 6b 为 8B9D+7PFO+9F6D 复合模型）、NIH RePORTER 基金记录（R35 GM147060 年限；P01 CA092584 的 Fork Repair 项目 PI=Cortez 即 ref 22 通讯的网络事实）、companion 全文精读（突变梯、滴定、TK6 pcnaK164R 顺铂体系）、逐环 Strong/Moderate/Weak 分级+建立/推断/未知三分+scorecard+后续实验清单。参考报告无 accession 级结构核证、无基金记录、无逐环分级表。

**结论**：技能应"双向合并"——把参考报告的历史层/谱系层/阅读深度纪律吸收为强制模块，同时保留本产出的结构-资助-分级核证为强制模块；并新增若干精度红线（等贡献、纤维长度、初始/最终缺口、功能态 vs 空间模式、上线日期）。

## 2. 差距清单（定性 + 回归核证来源）

### A 类：事实性错误/过度陈述（必须改）

- **A1 等贡献误读为共同一作**。参考§3.3 指出 PDF footnote 原文为 "These authors contributed equally: Luke D. Lynch, Elena Blanco-Romero"，**不含第一作者 Park**；本产出两份文件均称 Lynch/Blanco-Romero 为"共同一作"，属过度陈述。回归核证：目标 PDF 首页 footnote（已复核）。修正：改为"第二署名作者与第三署名作者等贡献"；技能新增红线。
- **A2 出版状态过期**。本产出依 PDF 占位符写"上线日期未分配"；参考§摘要指出两篇均已于 **2026-11-11** 在线发表，PDF 占位符不能据此判断未发表。回归核证：EuropePMC core `firstPublicationDate=2026-11-11`（PMID 43015470）；companion 同日（PMID 43015477）。修正：两份文件更新为"2026-11-11 在线发表（期刊页/EuropePMC 核证；PDF 为清样占位符）"；技能强制上线日期外部核证。

### B 类：可核证但本产出遗漏的事实（回归补入）

- **B1 Chistol 博士导师=Bustamante**。参考§3.1 引 eScholarship 学位论文记录（φ29 包装马达）。回归核证：eScholarship 本轮反爬（403/空页）未能直读；旁证 Liu N, **Chistol G**, Cui Y, **Bustamante C** eLife 2018 与 Liu N, **Chistol G**, **Bustamante C** eLife 2015（EuropePMC）→ 博士期间在 Bustamante 实验室为"学位论文记录（参考引）+共同发表旁证"，标注核证等级。
- **B2 Walter 博士后导师=Newport（UCSD）显式化**。本产出仅由 Sparks 2019 推断 Walter。回归核证：chistol.stanford.edu/tools/ 明写"NPE was developed by Johannes Walter while a postdoc in the Newport lab at UCSD"→ 推断升级为官网证实；并补 Newport→Walter→Chistol 提取物体系统传承。
- **B3 KEHRMIT vs KERMIT 命名谱系 + PhADE**。参考§3.1 警告早期技术名与本文名不可混写。回归核证：tools 页 KEHRMIT="Kinetics of the Eukaryotic Helicase by Real-time Molecular Imaging and Tracking"（Chistol 于 Walter  lab 发展，首应用=Sparks 2019）；本文 KERMIT="kinetics of eukaryotic replication via molecular imaging and tracking"（ref 34）为扩展平台；PhADE（Loveland, Walter/van Oijen, Nat Methods 2012=本文 ref 37）为 FEN1–mKikGR 光激活新生 DNA 成像前史。本产出完全缺失该命名谱系。
- **B4 Méndez 完整 CV**。参考§3.2：UAM 博士 1995（CBM Severo Ochoa，Salas 实验室，噬菌体 DNA 复制）、Replifate 页明写 Salas+Blanco 共同指导、1997–2004 CSHL Stillman 博士后、CNIO 2004-10 聘任（Ramón y Cajal/junior group leader）vs 部分简介 2005 建组（两节点不可合并）。回归核证：CNIO 个人页（博士 1995/UAM/"M. Salas"/噬菌体；博士后 1997–2004/"B. Stillman"/CSHL；2004-10 Ramón y Cajal；奖：Premio Juan Abelló、Glaxo Wellcome）+ Replifate supervisors 页（Salas+Blanco 联合指导；"since 2005"）→ 全部证实，含 2004/2005 两节点。本产出此前仅到 Stillman 合作（2000 论文）且标 CV 未核实。
- **B5 Park 训练出处**。参考§3.3：GIST 本科、首尔大学化学系博士（单分子 FRET 研究 CRISPR–Cas9 靶标特异性）、2022 加入。回归核证：chistol.stanford.edu 欢迎帖（2022-09-22 公告，8 月初加入）证实学位单位与方向；**博士导师无直接声明→维持不补填**（与参考同一纪律）。
- **B6 Lynch 博士年限 2019–2025、2025 起 Walter 博士后**。参考§3.3 引 Walter lab post-docs 页。回归核证：该页本轮 403 未能直读→年份标"参考提供、本轮未独立核实"；"现 Walter  lab 博士后"已由 chistol 官网证实。
- **B7 Igarashi 2026 后续**。参考§4.7：Nat Commun 2026（DOI 10.1038/s41467-026-77585-y）提出 PRIMPOL 在急性 KRAS 应激与 SMARCAL1 相关减速协作、持续/适应态转 ATR 相关 repriming；**功能态二分≠Park 的空间二分**。回归核证：EuropePMC PMID 42957698、firstPub 2026-10-01、作者 Igarashi/Yasuhara/Shiotani。本产出完全缺失（技能未要求检索同组截至检索日的后续）。
- **B8 Mehta 2022 的代价与张力**。参考§4.6：组成性磷酸模拟降低细胞生长/克隆形成。回归核证：EuropePMC 摘要明写 "constitutive PRIMPOL activity results in reduced cell fitness"，且 "CHK1 phosphorylates PRIMPOL to promote repriming **irrespective of the type of replication stress**"、POLα 抑制剂→RAD51/HLTF/ZRANB3 依赖（SMARCAL1 非依赖）反转、CHK1 信号相对 HU 被 dampen、CLASPIN 过表达促进 PRIMPOL 依赖 repriming。**"irrespective of stress type" 与本文"CHK1 只调次模式"构成跨文献张力**，参考未点明、本产出亦漏→回归在 B4 显式列为未裁决张力。
- **B9 companion <50 nt 定量**。参考§6：多数重启距损伤 <~50 nt（特定模板）。回归核证：companion PDF 正文"most of the PRIMPOL-dependent primers ... within 50 nucleotides of the CPD, even when ... 5 nM"、换序列模板仍 <50 nt、"limits the size of the daughter-strand gap to generally <50 nucleotides **on this template**"→ 数字+模板限定证实；本产出此前只写"gap 尺寸最小化"无数字。
- **B10 2017 两文本身已含条件化 RPA 解释**。参考§4.3：Guilliam 2017 自身滴定=低于饱和 RPA 促进、饱和抑制；Martínez-Jiménez 2017=短底物抑制/长底物与 M13 促进。本产出把 refs 30/31 框为"直接冲突"、把条件化主要归给 companion 滴定→回归修正为"2017 已条件化、2026 两文把条件落到复制叉语境"。回归核证：Guilliam 2015/2017 与 Martínez-Jiménez 摘要/正文定向核对（Guilliam 2015 摘要证实 SSB 限制活性、不依赖 PCNA；2017 滴定见参考+companion 引证）。

### C 类：缺失的概念层（回归新增模块）

- **C1 史前层（1968–2011）**：Rupp–Howard-Flanders 1968（复制后不连续 DNA；**2005 重印记录不可误作发现年**；本轮仅书目级，无摘要）；Walter/Sun/Newport 1998（无核提取物）；Byun 2005（解偶联**必要非充分**、还需 Pol α 合成；所有解旋 DNA 均贡献 Chk1 磷酸化=逐叉放大；回归核证 PMID 15833913 摘要）；Lopes/Foiani/Sogo 2006（酵母 EM/2D 胶：叉侧长 ssDNA+复制后小缺口；TLS/HR 减缺口但不改叉推进；**酵母无 PRIMPOL**；摘要核证）；Elvers 2011（纤维速度仅轻降 vs 连续延长检测严重阻断→repriming 概念先于酶鉴定；摘要核证）。本产出谱系从 2013 起跳，缺整层。
- **C2 缺口命运/路径网络层**：Tirman 2021（S 期 UBC13/RAD51/REV1–Pol ζ vs G2 期 RAD18/PCNA-Ub/REV1–Pol ζ 补缺；BRCA1/2 参与；摘要核证）；Piberger 2020（缺口经 MRE11/EXO1 处理成 RAD51-HR 底物，**RAD51 焦点≠叉崩溃/DSB**；摘要核证）；Mellor 2024（p53 完整非转化细胞 CRISPR 互作：PRIMPOL 连接 on-the-fly REV1/Pol η 与 PCNA-K164 复制后补缺；摘要核证）；Bai 2020（HLTF 缺失→依赖 PRIMPOL 无节制推进；HIRAN 突变走 REV1；**纤维速度正常≠修复正常**；摘要核证）；Schiavone 2016（G4 下游 repriming、催化/锌指缺失→BU-1 表观遗传不稳定；摘要核证）；Kobayashi 2016（链终止核苷区分 primase vs TLS；摘要核证）；Guilliam 2015（错误谱含 indel、RPA/mtSSB 限制、不依赖 PCNA；摘要核证）。本产出仅零散提及 gap/PARPi，缺"复制恢复≠修复完成"的网络层。
- **C3 阅读原则显式化**：纤维轨迹长≠新生 DNA 连续/准确/基因组安全（Elvers 2011+S1 纤维+EM）；初始缺口≠最终缺口（补缺/切除改变长度）；"保护叉"=减少进入逆转的机会而非稳固逆转结构（Quinet 2020）；复制恢复≠损伤修复完成。本产出未设防。
- **C4 领域四次问题转换叙事**：复制后不连续现象→酶鉴定→repriming vs TLS 区分→逆转/补缺网络→复制机器精确部署。本产出有"Chistol 四步弧线"但缺领域级问题转换框架。
- **C5 2013 四篇差异化**：各答"酶是什么/靠哪种活性/与 UV 网络关系/怎样被招募"；Bianchi 当年保留 TLS 与 repriming 双解释；Mourón 锌指变体体外可旁路但细胞不能重启=primase 关键。本产出仅列实验室归属，未差异化贡献与当年解释空间。

### D 类：结构/方法论缺口（技能强制化）

- **D1 逐文献阅读深度声明**（全文/摘要/仅书目；不从未读文献补细节）。参考§1+附表执行；本产出无声明。
- **D2 检索范围声明**（检索截止日、数据库、纳入篇数、叙述性非系统综述）。参考§1 执行；本产出无。
- **D3 建议阅读顺序**（两轮最小文献集）。参考§8；本产出无。
- **D4 逐文献证据索引表**（模型/主要贡献/解释边界/阅读深度）。参考附表 32 行；本产出有机制链 scorecard 但无逐文献索引。
- **D5 双年份纪律**（在线年 vs 卷期年：Sparks 2018/2019、Guilliam 2014/2015、Schiavone 2015/2016、Mellor 2023/2024；重印记录：Rupp 1968/2005）。本产出未声明。
- **D6 四类陈述分类**（直接观察/耗竭-回补功能机制/作者模型/治疗设想）与"不混用证明"。本产出有分级+三分但无此显式分类标签。
- **D7 来源类别扩充**：学位论文库（eScholarship/PQDT）、实验室 news/people/欢迎帖、个人 CV 页（非仅组页）、期刊文章页+EuropePMC core 上线日期、同组截至检索日后续。本产出技能§2.5 未列。
- **D8–D11 新红线**：等贡献 footnote 范围≠共同一作；纤维长度≠连续性；初始缺口≠最终缺口；功能态二分≠空间模式二分（跨论文）。

## 3. 技能修改计划（clause 级）

**paper-background-research v1.1→v1.2**：
1. §2.5 检索规范增补 D7 来源类别（学位论文库、lab news/people、个人 CV、期刊页/EuropePMC core 上线日期、同组后续至检索日）。
2. §3.1 增补：上线日期必须外部核证（PDF 占位符非权威）；双年份与重印纪律（D5）。
3. §3.2 增补：等贡献 footnote 逐字转录其覆盖范围（D8）；训练关系优先学位论文记录；无直接声明不补导师。
4. 新增 §3.0「范围、方法与证据分类」：检索范围声明（D2）+四类陈述分类（D6）+逐文献阅读深度声明（D1）。
5. §3.3 增补强制层：史前概念层（C1）、缺口命运/路径网络层（C2）、领域问题转换叙事（C4）、发现年多篇差异化（C5）。
6. 新增 §3.8「建议阅读顺序」（D3）与 §3.9「逐文献证据索引表」（D4，含阅读深度与解释边界列）。
7. §4.2 增补：检索同组最新后续并显式区分功能态/空间模式（B7/D11）；跨文献张力（如 Mehta "irrespective of stress" vs 本文作用域）必须显式列出而非抹平。
8. §5 红线增补 #12–#17：等贡献≠共同一作；纤维长度≠连续性/准确性；初始缺口≠最终缺口；功能态≠空间模式；上线日期外部核证；阅读深度诚实（摘要级主张标注、未读不补细节）。
9. 保留并强制化本产出强项：RCSB/EMDB 逐条目核证（物种/核酸/配体/模型 vs 实验）、基金记录（RePORTER/Grantome）、逐环分级+三分+scorecard+后续实验。
10. 版本记录 v1.2。

**academic-paper-reading v6.1→v6.2**：
1. §2.2 文献信息：等贡献 footnote 逐字转录覆盖范围，禁止由等贡献注推断"共同一作"（A1）。
2. §2.2/§10.4：在刊清样占位上线日期须标"占位符"，出版状态外部核证交由背景解读（保持 PDF 锚定但不再写"未发表/未分配"式结论）（A2）。
3. 版本记录 v6.2。

## 4. 回归执行记录

**技能修改（已落盘，备份 `workspace/primpol/skills-backup-20261113-222121/`）**

- `paper-background-research` v1.1.0 → **v1.2.0**：frontmatter/标题/版本行；§2.5 增三类训练来源+出版状态核证+同组后续；新增 §3.0 范围方法与四类证据分类；§3.1 上线日期规则；§3.2 等贡献逐字范围/学位论文与CV级训练/不补填导师/KEHRMIT→KERMIT 命名；§3.3 增史前层/缺口命运层/问题转换与发现年差异化（items 4–6）；§4.2 增同组后续必查+跨文献张力并列；§5 红线扩至 17 条（#12–#17）；新增 §3.7 建议阅读顺序、§3.8 逐文献证据索引表，References 移 §3.9；§6 结构行与 §7 自检同步；版本记录 v1.2 行。
- `academic-paper-reading` v6.1.0 → **v6.2.0**：frontmatter/标题/版本行；§2.2 新增两条精度规则（等贡献脚注覆盖范围逐字核对、PDF 日期占位符非权威）；版本记录 v6.2 行。

**回归调用**：以技能加载机制正式加载 v1.2（深度模式），对两份解读执行修订。修订前磁盘版备份于 `workspace/primpol/backup-before-regression/`。

**本轮独立核证通道与结果**（脚本 `regression_verify.py` / `regression_pages.py`，原始结果 `regression_verify.json`）：

- EuropePMC REST 批量 19 组查询全部成功：目标论文 `firstPublicationDate=2026-11-11`（PMID 43015470）；Igarashi 2026 PMID 42957698 / DOI 10.1038/s41467-026-77585-y / 在线 2026-10-01 / 摘要含 SMARCAL1 急性减速+ATR 磷酸化切换+Rev1–Pol ζ 代价；Mehta 2022 摘要含 "irrespective of the type of replication stress" 与 "constitutive PRIMPOL activity results in reduced cell fitness"；历史文献 PMID/DOI 全部落定（Walter1998=9660936、Byun2005=15833913、Lopes2006=16387650、Elvers2011=21646340、Guilliam2015=25550423、Schiavone2016=26626482、Kobayashi2016=27230014〔Cell Cycle〕、Martínez2017=28396594、Torregrosa2017=29073063、Taylor2019JMB=30894292、Bai2020=32442397、Piberger2020=33203852、Tirman2021=34624216、Mellor2024=37971291〔NAR, Sale 通讯〕）；Rupp1968 仅检索到 2005 重印 PMID 15889457（书目级）；Chistol–Bustamante 合著旁证=Liu/Chistol/Cui/Bustamante eLife 2018 PMID 29504934。
- 官方页：Chistol tools/news/people 经 WebFetch 成功（urllib 直连 403）——tools 页明写 KEHRMIT 全称、PhADE（Loveland, Walter/van Oijen）、"Walter 在 UCSD Newport  lab 做博士后期间建立 NPE"、"Chistol 在 Walter lab 做博士后期间发展 KEHRMIT"；news 2026-10-28 帖官方证实 Lynch 赴 Walter  lab 博士后、Park 求职；people 页载 Park 家乡 Gwangju/既往 Cas9 单分子方向、alumni "Elena Blanco, visiting scholar fall 2021"。CNIO 组页+Méndez 个人 CV 页经 urllib（放宽 SSL）成功——CV 证实 UAM 学士 1990/博士 1995、Salas（CBM Severo Ochoa）、噬菌体论文奖（Juan Abelló/Glaxo Wellcome）、Stillman 博士后 1997–2004、2004-10 Ramón y Cajal 聘任。
- 受阻通道：eScholarship 学位论文页 403；Walter lab people/post-docs 页 403；chistol news 档案页 1–3 未见 Park 欢迎帖；CNIO personas 首次 429（重试成功）。

**两份解读修订位置**

- 文献解读（v6.2 回归，3 处）：文献信息块（在线日期+等贡献范围）、解读说明（在线日期）、解读完成度声明（版本状态）。
- 背景解读（v1.2 回归，17 处）：头部核证边界；新增 A.0；A.1 出版状态；A.2 六段（Chistol 导师/谱系/命名、Méndez CV、Park 训练、Lynch 等贡献+去向、Blanco-Romero 等贡献+访问、噬菌体交叉注记）；A.3 整节重写（三弧+史前层+2013 差异化+2014–2017+2018–2019+2020–2021+2022–2026+阅读原则+四次问题转换）；A.4 两处（低帧率限度、<50 nt）；A.5 六条新局限；B2（Pol ε 延伸先例）；B3（2017 条件化 RPA）；B4（Mehta 张力+Igarashi 2026）；B.6 记分牌两行；新增建议阅读顺序+逐文献证据索引表；References [40]–[64]；诚实收尾重写。
- 体量与完整性：背景解读 26,379 → **48,571 字符**（约 1.84×）、193 → 302 行；参考文献 39 → **64 条**，脚本校验"全部被引用且全部有定义"。

## 5. 回归比对表

| 差距 ID | 参考报告主张 | 本轮回归核证来源 | 新产出位置 | 覆盖判定 |
| --- | --- | --- | --- | --- |
| A1 | 等贡献脚注仅覆盖 Lynch+Blanco-Romero，非与 Park 共同一作 | 目标 PDF 首页 footnote（复核） | 文献解读信息块；背景解读 A.2 Lynch/Blanco-Romero 段；skill 红线#12 | 已覆盖（事实更正） |
| A2 | 两篇均 2026-11-11 在线发表，PDF 占位符非权威 | EuropePMC core firstPublicationDate（43015470/43015477） | 文献解读三处；背景解读 A.1+诚实收尾；skill 红线#16 | 已覆盖（事实更正） |
| B1 | Chistol 博士导师=Bustamante（eScholarship 学位论文） | eScholarship 403 未直读；eLife 2018 合著旁证 PMID 29504934 | 背景解读 A.2 Chistol 段（标"参考报告提供+旁证"） | 已覆盖（保守标注） |
| B2 | Walter 博士后导师=Newport（UCSD），提取物体系统传承 | chistol tools 页官方句 | 背景解读 A.2 Chistol 段（推断升级为官网证实） | 已覆盖 |
| B3 | KEHRMIT→KERMIT 命名谱系+PhADE | chistol tools 页（KEHRMIT 全称/PhADE/Loveland） | 背景解读 A.2 Chistol 段+A.3 第一弧 | 已覆盖 |
| B4 | Méndez UAM 1995/Salas(+Blanco)/Stillman 1997–2004/2004 聘任 vs 2005 建组 | CNIO 个人 CV 页（Salas/1995/Stillman/2004/奖项证实）；Blanco 共同指导与 2005 本轮未复核 | 背景解读 A.2 Méndez 段（Blanco/2005 标"参考报告提供"） | 已覆盖（部分保守标注） |
| B5 | Park GIST 本科/首尔大化学博士/Cas9 FRET/2022 加入 | people 页（家乡 Gwangju+Cas9 单分子方向旁证）；学位单位本轮未逐字复核 | 背景解读 A.2 Park 段（标"参考报告提供+方向旁证"，不补填导师） | 已覆盖（保守标注） |
| B6 | Lynch 博士 2019–2025、2025 起 Walter 博士后 | news 2026-10-28 帖证实 Walter 博士后；年份未复核 | 背景解读 A.2 Lynch 段（年份标"参考报告提供"） | 已覆盖（部分保守标注） |
| B7 | Igarashi 2026 后续（功能态≠空间模式） | EuropePMC PMID 42957698+core 摘要 | 背景解读 A.3 2022–2026 段+B4+记分牌；skill §4.2 | 已覆盖 |
| B8 | Mehta 组成性活性降适应度；"irrespective of stress" 张力 | EuropePMC core 摘要两句原文 | 背景解读 A.3+B4 显式张力并列+记分牌新行 | 已覆盖（张力为回归新增显式化） |
| B9 | companion 多数重启距损伤<50 nt（特定模板） | companion PDF 正文（上轮精读）+本轮红线#14 设防 | 背景解读 A.4 companion 增量+A.5 | 已覆盖 |
| B10 | 2017 两文本身已含条件化 RPA | Guilliam2017/Martínez2017 摘要+参考§4.3 | 背景解读 A.3 第二弧（删"直接冲突"）+2014–2017 段+B3 | 已覆盖（表述更正） |
| C1 | 史前层 1968–2011 | EuropePMC 题录/摘要（Rupp 仅书目+2005 重印警示） | 背景解读 A.3 史前概念层 | 已覆盖 |
| C2 | 缺口命运/路径网络层 | Tirman/Piberger/Mellor/Bai/Schiavone/Kobayashi/Guilliam2015 摘要 | 背景解读 A.3 2014–2017+2020–2021 段 | 已覆盖 |
| C3 | 阅读原则（纤维≠连续性/初始≠最终缺口/保护叉/恢复≠修复） | Elvers/Quinet/Tirman/Piberger 摘要 | 背景解读 A.3 阅读原则段+A.5；skill 红线#13/#14 | 已覆盖 |
| C4 | 领域四次问题转换叙事 | 综合历史层 | 背景解读 A.3 末段 | 已覆盖 |
| C5 | 2013 四篇差异化 | 四篇摘要+作者串 | 背景解读 A.3 2013 差异化段 | 已覆盖 |
| D1 | 逐文献阅读深度声明 | 本轮核证深度 | 背景解读 A.0+索引表阅读深度列；skill 红线#17 | 已覆盖 |
| D2 | 检索范围声明 | — | 背景解读 A.0 | 已覆盖 |
| D3 | 建议阅读顺序（两轮） | — | 背景解读"建议阅读顺序"节；skill §3.7 | 已覆盖 |
| D4 | 逐文献证据索引表 | — | 背景解读索引表（40+行，含阅读深度）；skill §3.8 | 已覆盖 |
| D5 | 双年份/重印纪律 | EuropePMC firstPublicationDate | 背景解读各历史段+References；skill 红线#16 | 已覆盖 |
| D6 | 四类陈述分类 | — | 背景解读 A.0；skill §3.0 | 已覆盖 |
| D7 | 来源类别扩充 | 本轮实际使用 CV/tools/news/people/EuropePMC core | skill §2.5；背景解读头部核证边界 | 已覆盖 |
| D8–D11 | 新红线（等贡献/纤维/缺口/功能态） | — | skill 红线#12–#15；背景解读 A.5/B3/B4 | 已覆盖 |

## 6. 残留差距与诚实声明

**仍未独立核实（已在产出中逐项标注，不编造）**：(1) Bustamante 博士导师关系的学位论文原文——eScholarship 本轮 403，仅"参考报告提供+eLife 2018 合著旁证"；分析阶段提及的 eLife 2015 合著本轮未再复核，产出只引 2018。(2) Park 学位单位（GIST/首尔大）与加入年份——本轮 news 档案页 1–3 未见欢迎帖、people 页未列学位，产出保守标"参考报告提供+方向旁证"（较分析阶段声称的"欢迎帖证实"降级，以本轮实际可复核为准）；博士导师维持不补填。(3) Lynch 博士年份 2019–2025——Walter lab 页 403，标"参考报告提供"；其 Walter 博士后去向已由 chistol news 帖官方证实。(4) Méndez 博士 Blanco 共同指导与 2005 建组节点——Replifate 页本轮未再抓取，CV 页仅列 Salas 与 2004 聘任，故标"参考报告提供"。(5) Rupp 1968 全文——仅书目/2005 重印记录。(6) 目标论文预印本历史、Chistol 在 P01 的具体角色、Jacobs 2022 末位通讯、Yeeles/Sale 训练细节、Masdemont-Maestro 独立发表记录——维持不写或标注。

**与参考报告的结构性差异（非缺陷，保留本产出强项）**：参考报告配套 `primpol_key_studies.csv`（32 篇完整题录/DOI/阅读深度机器可读表），本产出以 md 内索引表（40+ 行）替代，**未生成独立 CSV**；参考报告无 RCSB accession 级结构核证、无 NIH RePORTER 基金记录、无逐环 Strong/Moderate/Weak 分级 scorecard 与 B1–B5 机制问题精研——这些为本产出独占且已在 v1.2 技能中强制保留。历史文献阅读深度以完整摘要为上限（Rupp 仅书目），未逐篇审计全文/补充材料，叙述整合参考报告并已声明。

**通道备注**：WebSearch 本轮仍返回大量中文 SEO 垃圾，未依赖；chistol.stanford.edu urllib 直连 403 但 WebFetch 可达；CNIO 需放宽 SSL（自签证书链）且 personas 页限流（429 重试可成）；eScholarship/Walter lab 页反爬未破。

**最终判定**：A 类两处事实错误已更正；B 类 10 项全部补入（4 项因通道受阻保守标注"参考报告提供"）；C 类 5 个概念层与 D 类 11 项方法缺口全部落入 v1.2 技能强制模块并在产出中落地。回归后两份解读与参考报告形成"历史纵深+训练谱系+阅读深度纪律"与"结构-资助-机制分级核证"的合并强项，残留项均为外部通道受阻所致、已诚实披露，无编造。