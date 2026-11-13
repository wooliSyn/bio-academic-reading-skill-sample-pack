# UNC13A splice correction rescues synaptic dysfunction induced by TDP-43 loss — 背景解读（深度模式）

> 配套文件：同源《UNC13A splice correction rescues synaptic dysfunction induced by TDP-43 loss_文献解读.md》（下称"文献解读"）已完成 PDF 内逐图精读（主文 Fig. 1–4 共 43 panel 四字段 + ED Fig. 1–11 共 84 panel 紧凑整合）。本背景解读负责 PDF 之外的作者谱系、研究传承、创新定位与跨文献问题精研，两者交叉引用、不重复逐图。凡涉及"本文做了什么/本文图怎么读"，一律以文献解读为准；本文件只补充外部上下文与跨文献综合。

---

## 0. 范围、方法与证据分类

**检索截止日：2026-11-14。** 核证通道：EuropePMC REST（core，批量约 60 次查询，核证题录/作者串/摘要/`firstPublicationDate`）、ORCID 公共 API（5 位关键作者的 education/employment 记录）、ClinicalTrials.gov API v2（TRCN-1023 试验）、WebFetch（KCL 官方页、Trace Neuroscience 公司页；UCL profiles 为 JS 应用、FMP 组页与 Dundee/UCL 学位论文库返回 403/404，未能读取，如实标注）。PDF 全文复用 workspace/unc13a/fulltext.txt（43 页，前次精读已提取），未重复提取。纳入关键外部文献约 60 篇（含预印本），其中完整摘要级约 40 篇、仅书目级约 8 篇、本文全文定向核读 1 篇。

**这是聚焦叙述性检索，不是系统综述；未做效应量合并、未做偏倚风险评估。** 证据按四类组织，行文中不混用"证明"：(i) 实验直接观察（如本文膜片钳/MEA/成像读数、前作 Western/RT–PCR）；(ii) 由缺失/回补支持的功能机制（如 CE DEL/ASO rescue 支持的单事件因果）；(iii) 作者提出的解释模型（如"功能性死亡"、E/I 偏移假说、30% 阈值外推）；(iv) 尚待验证的治疗/转化设想（如 ≥30% 蛋白即有益、TRCN-1023 临床疾病修饰）。每篇外部文献的实际阅读深度在 §A8 索引表逐条标注；**仅书目或摘要级来源不承载超出其摘要的实验细节**，未读到的图号一律标"编号待核"，不编造。

**版本与日期纪律：** 本文在线发表日期以 EuropePMC `firstPublicationDate` 核证为 2026-11-11（PMID 43015463），PDF 首页"Published online: xx xx xxxx"为占位符、非权威；本文尚无卷期（online ahead of print）。历史文献在线年与卷期年不一致处双标注（如 Diekstra 在线 2011/卷期 2012）。预印本与正式发表版差异处注明。

**一处周报卡片更正：** 同目录《CNS生物物理周报_2026-11-13_导读.md》🥇UNC13A 段称"ASO 在人源化小鼠与患者来源神经元中恢复释放概率与网络同步"。据 PDF 与文献解读，本文**未使用患者来源神经元**（全部功能实验用健康 WTC11 与肿瘤系），且人源化小鼠体内**仅分子剪接药效、无功能/行为读出**。本背景解读以 PDF 为准，周报该句不准确。

---

# Pillar A · 背景简报

## A1. 一瞥：一篇把"剪接噪声"收敛成"可药靶点"的 Nature

**完整题录：** Keuss MJ, Harley P, Ryadnov E, Jackson RE, … Burrone J & Fratta P. UNC13A splice correction rescues synaptic dysfunction induced by TDP-43 loss. *Nature* (2026). DOI 10.1038/s41586-026-11256-2；PMID 43015463；在线 2026-11-11（EuropePMC 核证），尚无卷期；Open Access（CC BY 4.0）；Article，非预印本形态发表 [1]。首页脚注逐字："These authors contributed equally: Matthew J. Keuss, Peter Harley, Eugeni Ryadnov, Rachel E. Jackson"——即**前四位署名作者等贡献**；通讯四人：Keuss、Harley、Burrone、Fratta（✉ m.keuss@ucl.ac.uk; p.harley@ucl.ac.uk; juan.burrone@kcl.ac.uk; p.fratta@ucl.ac.uk）[1]。Received 18 June 2024 / Accepted 6 October 2026（PDF）[1]。

**预印本历史：** 本工作以 "Loss of TDP-43 induces synaptic dysfunction that is rescued by UNC13A splice-switching ASOs" 于 2024-06-24 首次上传 bioRxiv（DOI 10.1101/2024.06.20.599684），与 Nature 投稿（2024-06-18 received）几乎同步；正式发表标题改为现题 [2]。从预印本到接收历时约 2 年 4 个月，提示审稿周期长（与体内功能数据缺失、单事件充分性主张的审慎评估一致，推测）。

**公共数据：** 本文**无 GEO/公共测序 accession**——Reporting Summary 明确"No Omics datasets were generated or used in this study"，原始数据以 source data 随文提供；代码四个 GitHub 仓库（电生理 MATLAB+突触密度 Fiji 宏 jburrone/Keuss-Harley-Ryadnov-Jackson-et-al.-Nature-2026、iGluSnFR3 管线 f-hamidlab/iGluSNFR3 publication_branch、QIAxcelR、Log1pGaussianLMM）[1,74]。材料经 MTA 获取（细胞系/小鼠/AAV，见文献解读§7）。

**一句话核心主张：** TDP-43 核缺失先把人神经元推入"结构完好但突触通讯崩溃"的前退化态；在数百个隐匿剪接事件中，仅 UNC13A 内含子 20 的一个隐匿外显子就是突触失效的主驱动，基因组删除或 splice-switching ASO 单点纠错即可恢复释放与网络同步——为约 97% ALS 与约 50% TDP-43 病理型 FTD 提供遗传学锚定的治疗策略 [1]。

## A2. 作者谱系：一条经营了十余年的"TDP-43 剪接致病→核酸干预"弧线

### Pietro Fratta（资深通讯）：从临床神经科医生到 UNC13A 治疗公司的科学创始人

Fratta 是 UCL Queen Square 神经病学研究所（Institute of Neurology）/ UCL Queen Square MND Centre 教授，兼 Francis Crick Institute 研究员、National Hospital for Neurology and Neurosurgery 顾问神经科医生；M.D. 取自米兰、Ph.D. 取自 UCL、2015 年建立独立实验室（Trace Neuroscience 公司创始人页自述）[3]；ORCID 0000-0002-8762-8188 仅列 UCL 任职，未列学位年份与导师 [4]。**其博士导师未在可读取的公开来源中声明，本解读不据合作论文补填。** 奖项未在本次检索核到顶级奖项记录，不写。

他定义/推动的子方向是**"TDP-43 核缺失→隐匿剪接→ALS/FTD"的 RNA 致病机制及其核酸干预**。标志性前作是 Brown et al. *Nature* 2022（本组主导，Fratta 资深作者）：确立 TDP-43 缺失诱导 UNC13A 隐匿外显子 inclusion→NMD→蛋白耗竭，且 ALS/FTD 风险 SNP 与 TDP-43 结合位点重叠、加剧 inclusion [28]。这条轴线随后被本组系统推进：Seddighi et al. *Sci Transl Med* 2024 证明隐匿外显子可翻译成 de novo 蛋白/肽并在患者 CSF 检出（把"剪接噪声"变成生物标志物与潜在新抗原）[51]；Wilkins et al. *Science* 2024 开发 TDP-REG/SpliceNouveau，把隐匿剪接本身改造成"只在 TDP-43 功能缺失时/处才表达治疗蛋白"的精准医学开关，并演示在 TDP-LOF 触发下用 prime editing 消融 UNC13A 隐匿供体位点 [52]；Bryce-Smith et al. *Nat Neurosci* 2025 把后果谱从隐匿外显子扩展到隐匿选择性多聚腺苷酸化（cryptic APA）[45]；Scialò et al. *Neuron* 2025 证明 TDP-43 种子样聚集可诱导其功能缺失（把"聚集"与"核缺失"两条病理线 mechanistically 连接）[53]。**本文正是这条弧线的"功能因果+治疗落地"一步**：从"描述剪接紊乱"推进到"证明单事件足以驱动突触失效、且可被 ASO 单点纠正"，并直接孵化了公司的临床管线（见下）。

**产业转化（有记录支撑）：** Fratta 是 Trace Neuroscience 的科学创始人/顾问/持股人；该公司 2025 年以 1.01 亿美元 A 轮亮相、入选 Fierce 15，使命自称"把基因组医学从 2% 扩展到 97% 的 ALS 患者"，领先管线 TRCN-1023 为靶向 UNC13A 的剪接纠错 ASO [3]。本文竞争利益声明：Fratta/Keuss/Wilkins 已申请 ASO 纠正 UNC13A 隐匿剪接专利（US 12,522,826 B2、EP 4 444 321 A1）；Fratta 与 Burrone 实验室受 Trace 资助；Green/Morrie/Miller 为 Trace 雇员 [1]。**本文与该临床管线是同一转化弧线的产物（funding/COI 有记录）；但本文化合物（M21-4/M18-17）与临床候选物 TRCN-1023 的具体对应关系未在本文声明，属同管线推断。**

### Matthew J. Keuss（共同一作 + 共同通讯）：从 NEDD8/泛素生物学到 UNC13A 剪接治疗

Keuss 现为 UCL Senior Research Fellow（ORCID 0000-0002-2628-4115，2020–）[5]。其发表记录落在两条线：早期（2016–2019）在 Dundee/Glasgow 的 Kurz/Trost 圈做 NEDD8/泛素生物学——2016 *J Cell Sci* DCN 型 NEDD8 E3 连接酶家族（署名单位 University of Dundee, MRC PPU）[6]、2019 *EMBO J* 非锚定 tri-NEDD8 抑制 PARP-1（署名单位 University of Glasgow）[7]，另以共同作者参与 Johns Hopkins Dawson 圈的 Thorase 缺血神经保护工作（2018/2019 *JCBFM*）[8]；2020 年后转入 UCL Fratta 圈，成为 Brown 2022 的共同作者并主导本文 [28,1]。**其博士训练机构未在 ORCID 声明，Dundee/Glasgow 学位论文库本次检索受限（403）未核到论文记录；导师姓名不补填，仅以发表记录旁证并标注推断。** 他是 Trace 顾问/持股人、专利共同发明人、Sigrid Rausing Neurogenetic Therapies Programme 受资助者 [1,3]。

### Peter Harley（共同一作 + 共同通讯）：从 KCL 神经肌肉回路到 UCL 的兴奋性/AIS 生理

Harley 现为 UCL Research Fellow（ORCID 0000-0001-6689-0227，2022–；自述"previously at King's College London"）[9]。其前作集中在 KCL 的 Lieberam/Burrone 圈：Harley et al. *Cell Rep* 2023 证明 ALS hiPSC 运动神经元轴突起始段（AIS）可塑性异常与内在兴奋性动态变化（早期超兴奋→晚期低兴奋）[10]，另有神经肌肉共培养/类器官平台系列（2019–2023，书目级）。本文获 Wellcome Trust Early-Career Award Fellowship（331827/Z/25/Z）资助 [1]——提示其正走向独立。他是 Trace 顾问 [1]。**博士导师未核到直接声明，不补填。**

### Juan Burrone（共同通讯）：发育神经生理与突触释放成像平台的提供者

Burrone 是 KCL 发育神经生理学教授（Professor of Developmental Neurophysiology，Centre for Developmental Neurobiology / MRC Centre for Neurodevelopmental Disorders）[11]。ORCID 0000-0003-1233-668X 给出机构级训练轨迹：Bristol 本科（1992–1995）→ Cambridge 博士（1995–1999）→ Harvard 博士后（2000–2005）→ KCL Lecturer（2005）/Senior Lecturer（2008）/Professor（2011）[12]；**导师姓名未在 ORCID/官方页声明，不补填**。实验室主线为发育中神经回路的组装与稳定、兴奋/抑制平衡、轴突-轴突（chandelier cell）突触与稳态可塑性 [11]。本文的自突触微岛、iGluSnFR3 单突触 Pr 成像、MEA 网络同步与突触密度分析平台主要出自其圈（文献解读§6 已锚定方法来源；GitHub 电生理管线即 jburrone 仓库）[1,74]。**与 Fratta 有联合资助记录：** MRC programme grant MR/Z505353/1（J.B., P.F., M.S.）与 MNDA Burrone/Jul24/2457-797（J.B., P.F., M.S.），本文 funding 声明列名——本文是这些联合项目的直接产物 [1]。另受 Wellcome 215508/Z/19/Z、BBSRC BB/S000526/1、Trace 资助 [1]。

### Noa Lipstein（FMP Berlin 资深作者，非通讯）：Munc13 priming 生物物理 + UNC13A 人类遗传学

Lipstein 是 Leibniz-FMP Berlin junior group leader（ORCID 0000-0002-0755-5899，2020–）；训练轨迹：Tel Aviv University B.Sc（2001–2004）/PhD（2006–2013）→ Max Planck Institute of Experimental Medicine（Göttingen）博士后（2013–2020）→ FMP [13]；**导师姓名未在 ORCID 声明，不补填**（Göttingen 阶段与 Brose/Rosenmund 圈的合作有发表记录旁证，标注推断）。其主线正是本文效应分子 Munc13-1 的 priming 调控：Lin et al. *J Physiol* 2025 用动力学建模区分 priming 状态与融合概率 [62]、López-Murcia et al. *Cell Rep* 2026 的 Ca2+-磷脂依赖 Munc13-1 调控（书目级）、Ranjan et al. *Sci Adv* 2026 的 Munc13-1 偶联 DAG/Ca2+ 信号（与 Südhof 合作，书目级）；并主导 Asadollahi et al. *Nat Genet* 2025 的 UNC13A 致病变异神经发育综合征人类遗传学 [37]。本文第二细胞类型（iPS 来源脊髓运动神经元 iMN）与第二实验室（FMP）验证由其提供；受 DFG Excellence Strategy EXC-2049、CRC 1286 A11、Target ALS 产业联盟"Correcting Aberrant Splicing of UNC13A as a Therapeutic Approach for ALS and FTD"资助 [1]。她是 Trace 顾问/持股人 [1,3]。

### 其他贡献者与模块（据 PDF 署名/贡献声明）

Schiavo（UK DRI at UCL，轴突运输；Wellcome 223022/Z/21/Z）、Isaacs（UK DRI）、Fisher（UCL 遗传学）、Shah（UCL Pharmacology，与 Fratta/Burrone 联合 MRC）、Oliver（Nucleic Acid Therapy Accelerator, Harwell，ASO 化学/递送）、Ward（WTC11 iPS 系惠赠者，NIH；Trace 共同创始人）、Green/Morrie/Miller（Trace 雇员，化合物/AAV）、Davies（Crick，小鼠 ES 靶向）、Hamid（KCL，iGluSnFR3 管线）、Ryadnov（UCL）与 Jackson（KCL/Open University）为等贡献共同一作但非通讯 [1,3]。概念化：P.F., J.B., M.J.K., P.H., O.G.W., G.S.；监督含 N.L., G.S., E.M.C.F., P.L.O., M.S., F.H., B.D., A.M.I. [1]。

**等贡献范围纪律：** 脚注只把 Keuss/Harley/Ryadnov/Jackson 四人标为等贡献，**不等于**其余作者共同一作；通讯为另外明确的四人（Keuss/Harley/Burrone/Fratta）。Ryadnov 与 Jackson 是等贡献共同一作、但不是通讯，二者身份不互相升格 [1]。

## A3. 研究谱系：领域经历了六次问题转换，本文站在第六次的治疗落点上

### 史前层：分子被鉴定之前，现象与概念早已存在

**TDP-43 的"功能不明"前史。** TDP-43 最初于 1995 年作为结合 HIV-1 TAR DNA 序列的细胞蛋白被克隆（Ou et al. *J Virol*，书目级）[14]，此后十余年其正常功能与疾病意义不明。2006 年之前，FTLD-U 与 ALS 中"泛素阳性、tau/α-syn 阴性"的包涵体已是已知病理现象，但其蛋白成分未明——这正是 Neumann/Arai 两篇发现论文摘要所交代的背景 [16,17]。**unc-13 的遗传学前史。** unc-13 基因名源自 Brenner 1974 年线虫遗传学奠基论文（*Genetics*，书目级）[15]；"unc"（uncoordinated）表型先于分子鉴定数十年。这两条前史提醒：本文的"突触沉默"与"TDP-43 功能缺失"都不是凭空概念，而是把经典遗传学/病理学现象补上分子与功能因果。

**"结构完好≠功能完好"的突触前史。** 在 TDP-43 之前，Munc13 敲除小鼠已确立"突触结构正常但释放归零"的范式：Augustin et al. *Nature* 1999 证明 Munc13-1 缺失使谷氨酸能突触超微结构正常、但小泡循环停在成熟（priming）步，动作电位/钙离子载体/高渗蔗糖均不能触发释放（α-latrotoxin 可绕过）[33]；Varoqueaux et al. *PNAS* 2002 进一步证明 Munc13-1/2 双敲除自发与诱发释放全部消失、但突触发生与超微结构正常 [34]。**这是本文"功能性死亡"概念最直接的突触生理学前身**——结构完整而通讯崩溃并非新现象，本文的新意在于把它放到 TDP-43 核缺失的 disease context 并证明可逆。疾病侧的前身是 Devlin et al. *Nat Commun* 2015：患者 iPSC 运动神经元"功能失调但存活"，先超兴奋后进行性丢失动作电位输出与突触活动，而无明显存活率变化 [42]。

**核心因子的课本化背景（与文献解读概念注释互补）。** TDP-43 是核 RNA 结合蛋白，含两个 RRM、一个介导寡聚化的 N 端结构域（NTD）与一个低复杂度/朊病毒样 C 端域；正常核定位、调控剪接/稳定性/运输，并自调控其合成 [14,20,21,60]。Zbinden et al. 2026（预印本）进一步区分：NTD 在单体状态结合 UG-rich RNA，但 RNA 结合与寡聚化竞争同一界面，**寡聚化（而非 NTD-RNA 结合）才是抑制隐匿外显子所必需** [60]——这为"核内功能性 TDP-43 寡聚体缺失→隐匿剪接"提供了分子层面的最新限定。UNC13A/Munc13-1 是突触前活性区 priming 因子（Augustin 称其为"脑特异性突触前 phorbol ester 受体"）[33]，含功能必需的 MUN 域与 CaM 调控域 [63]，受 RIM [36]、DAG/PKC [62]、Ca2+/钙调素 [63] 调控，把突触小泡从 docking 推进到 fusion-competent；Imig et al. *Neuron* 2014 用冷冻固定+电子断层扫描论证 docking/priming/trans-SNARE 组装是同一过程的形态/功能/分子三面 [35]。人类遗传学上，UNC13A 既是 ALS/FTD 风险位点（常见非编码变异）[23–26]，其罕见编码/剪接变异又可致神经发育综合征（Asadollahi 2025，含 LoF/GoF/调控三类机制、A–C 三亚型）[37]——**同一基因的双重遗传身份是理解"剂量阈值"与"单事件权重"的关键背景**。

### 问题转换 1（2006→2008）：从病理蛋白到致病基因

2006 年两篇独立论文把 TDP-43 鉴定为 FTLD-U/ALS 的主要病理蛋白，但回答的问题不同：Neumann et al. *Science*（生化纯化+质谱，证明病理 TDP-43 过度磷酸化/泛素化/切割为 C 端片段，仅累及受累 CNS 区）[16]；Arai et al. *BBRC*（生化+免疫组化，证明 TDP-43 是泛素阳性 tau 阴性包涵体成分、异常磷酸化，提出"TDP-43 蛋白病"分类）[17]。二者同年、互补，不可压缩为"同一件事被重复发现"。2008 年 TARDBP 突变把 TDP-43 从"病理标志"升级为"致病基因"：Sreedharan et al. *Science*（M337V 在家系内共分离、全基因组扫描锁定 1p36、突变体体外更易片段化/ chick 胚胎神经凋亡）[18] 与 Kabashi et al. *Nat Genet*（9 个体 8 个错义突变、散发+家族）[19] 并行、证据类型不同（连锁 vs 关联）。

### 问题转换 2（2011）：核功能缺失→剪接紊乱

2011-02-27 同日 *Nat Neurosci* 两篇把机制焦点从"胞质聚集毒性"转向"核功能缺失"：Polymenidou et al.（Cleveland 圈；ASO 敲低成年小鼠脑 TDP-43 + CLIP-seq，6304 基因结合、601 mRNA 水平变化、965 剪接事件；最易耗竭的 RNA 来自超长内含子/突触活性基因；TDP-43 自调控）[20]；Tollervey et al.（Ule 圈；人脑 iCLIP，UG-rich 长簇结合、位置依赖的 Nova 样剪接调控、**沉默外显子下游深内含子处的异常长 TDP-43 结合簇**）[21]。后者正是"隐匿外显子抑制"的概念种子——深内含子结合簇暗示 TDP-43 在压制本不该用的剪接位点。

### 问题转换 3（2015）：隐匿外显子作为疾病机制

Ling et al. *Science* 2015（Wong 圈）确立：TDP-43 抑制**非保守**隐匿外显子以维持内含子完整性；缺失后隐匿外显子被并入 mRNA、常破坏读框/触发 NMD；强制抑制隐匿外显子可防止 TDP-43 缺失细胞死亡；ALS-FTD 病例中该抑制受损 [22]。这把"广泛剪接噪声"提升为"可致细胞死亡的机制"，并埋下"纠正隐匿剪接能否治病"的问题——本文是这个问题在突触功能层的答案。

### 问题转换 4（2009–2021 遗传锚定，与机制线并行）：UNC13A 从 GWAS 位点到可药靶点

van Es et al. *Nat Genet* 2009 首次把 UNC13A（19p13.3, rs12608932）定为散发 ALS 易感位点（两阶段合并 P=2.53×10⁻¹⁴）[23]；Diekstra et al. *Neurobiol Aging*（在线 2011-11-25/卷期 2012）证明 rs12608932 次要等位基因不仅关联易感、还关联**更短生存**（荷兰人群队列+GWAS 队列）[24]；van Rheenen et al. *Nat Genet* 2021（29,612 患者/122,656 对照，15 个风险位点，囊泡运输/自噬与谷氨酸能神经元细胞自主起始）[25]。Willemse et al. *JNNP* 2023 综述把这条遗传线收束为治疗靶点论证：rs12608932 C/C 纯合者更可能球部起病、认知障碍/FTD、生存更短；TDP-43 缺失下风险变异→隐匿外显子→NMD→蛋白丢失→传递受损；并提到当时已有碳酸锂确认性试验在进行、ASO 在考虑中 [26]。**本文"第二强 GWAS 信号""纯合生存缩短 5–12 个月"等表述是对 refs 14–16,33–36 的概括（本文 Discussion），其中"5–12 个月"具体数值未在本次摘要级来源中独立核到，按本文概括引用、不另赋精确出处。**

### 问题转换 5（2019→2022→2023）：单转录本功能因果 + UNC13A 机制 + ASO 纠正先例

**STMN2（2019，同日两篇，问题不同）：** Klim et al. *Nat Neurosci*（Eggan 圈；人运动神经元 TDP-43 敲低/错定位→STMN2 下降，STMN2 为轴突生长/再生所必需，转录后稳定化 STMN2 可 rescue  neurite 生长/轴突再生）[30]；Melamed et al. *Nat Neurosci*（Cleveland 圈；机制——TDP-43 结合 stathmin-2 第一内含子、缺失后暴露隐匿 polyA 位点→截短无功能 mRNA；患者成纤维细胞/iPSC MN/尸检组织验证；rescue stathmin-2 恢复轴突再生）[31]。二者确立"单个隐匿事件→特定神经元功能缺陷→可回补"的范式，但落点是**轴突再生**而非突触传递。

**UNC13A 隐匿外显子（2022-02-23 同日 Nature 背靠背，直接地基）：** Ma et al.（Gitler 圈；TDP-43 直接抑制 UNC13A 隐匿外显子，人脑/细胞系/iPSC MN 中核缺失→inclusion→蛋白下降；FTD/ALS 顶级风险变异位于该内含子、在 TDP-43 功能障碍时加剧 inclusion）[27]；Brown et al.（Fratta 圈；TDP-43 缺失→隐匿外显子→NMD→UNC13A 蛋白耗竭；两个常见内含子风险多态与 TDP-43 结合位点重叠、在培养细胞与患者脑/脊髓中加剧 inclusion；明确提"治疗靶点"）[28]。二者预印本亦同日（2021-04-02 bioRxiv）[27,28]。**注意版本：Brown 2022 有 2024-07-01 Author Correction（Nature 631:E7, DOI 10.1038/s41586-024-07577-9），更正内容本次未核到全文，本文引用的是经更正后的机制结论** [29]。这两篇把 UNC13A 从 GWAS 位点变成"机制明确的 RNA 调控节点"，但**留下两个缺口：突触功能因果未证、单事件是否足以驱动表型未证**——本文正是补这两环。

**ASO 纠正隐匿事件的方法学先例（2023）：** Baughn et al. *Science*（Cleveland + Ionis；机制——TDP-43 结合 GU-rich 区空间位阻阻断 STMN2 隐匿 3′ 剪接位点识别；dCasRx 或 ASO 抑制隐匿剪接→恢复轴突再生与 stathmin-2 依赖的溶酶体运输；人源化 Stmn2 小鼠 CSF 注射 ASO 在体纠正、不依赖 TDP-43 结合）[32]。**这是本文"splice-switching ASO 单点纠错"策略的同族直接先例**，本文把同一策略从 STMN2/轴突再生移植到 UNC13A/突触传递，并叠加遗传因果锚定。

**临床先例（监管/给药路径参照）：** nusinersen（SMN2 exon 7 剪接纠正）——Rigo et al. *JCB* 2012 研发历程视角 [38] + Finkel et al. *NEJM* 2017 ENDEAR III 期（婴儿型 SMA，运动里程碑应答 51% vs 0%，死亡/永久通气 HR 0.53，总生存 HR 0.37；早治获益更大）[39]，证明剪接切换 ASO 可在临床改变病程。但**同族教训同样重要**：tofersen（SOD1 ALS）VALOR III 期（Miller et al. *NEJM* 2022）28 周主要终点 ALSFRS-R 未达（差 1.2 分，P=0.97）、次要临床终点亦无显著差异，虽 CSF SOD1/血浆 NfL 下降、52 周 early-start vs delayed-start 差 3.5 分（95% CI 0.4–6.7，未做多重性校正），结论自陈"未改善临床终点" [40]；FUS ASO（ION363）仅有单例患者初步证据 [41]。**"剪接/沉默 ASO 能降靶标≠可证临床获益"是本文转化主张必须面对的先例边界。**

### 问题转换 6（2025–2026）：从单事件到功能因果，以及"单靶 vs 多靶"的正面张力

本文（2026-11）把 UNC13A 单事件的**突触功能因果充分性**与**可给药纠错**一并证明。但同期领域并未收敛到"单靶万能"，而是出现必须并列的张力：

- **Gitler 圈多事件线：** Guo et al. *Sci Transl Med* 2026（本文 ref 40，与本文共享 FMP 的 Ilic/Boll 与 Trace 的 Morrie/Miller/Green 等作者）鉴定 KALRN/RAP1GAP/SYT7/KCNQ2 等新的突触/兴奋性隐匿靶点，**单个 ASO 部分恢复、联合靶向几乎完全 rescue** TDP-43 缺失的突触缺陷 [47]。这与本文"单 UNC13A 事件 rescue 约 80% 频率"互补但口径不同（见 Pillar B1）。
- **Wong 圈在体张力线（最直接）：** Peethambaran Mallika et al. bioRxiv 2026-09-18（脊髓运动神经元特异 TDP-43 敲除小鼠）：**单独排除 Unc13a 隐匿外显子不能缓解运动神经元病；恢复多个隐匿靶点（含 Unc13a）才减轻运动神经元丢失**；且脊髓运动神经元积累的 Unc13a 隐匿外显子显著低于脑神经元（小鼠与人）[48]。同圈 Cao et al. bioRxiv 2026-09-15（前脑神经元特异 TDP-43 敲除小鼠）：**单独消融 Unc13a 隐匿外显子足以保存记忆/认知**，多靶点额外减轻神经元丢失 [49]。**两篇合起来的图景是"脑/认知：单靶够；脊髓/运动神经元病：单靶不够"——与本文"人皮层 iNeuron 单点 rescue 成立、体内脊髓仅分子药效"形成必须显式并列的跨文献张力（未裁决，见 B1/B4）。**
- **疾病态前退化线：** Gautier et al. *Cell* 2026（Gitler 圈；SOD1-G93A 小鼠纵向单核转录组+空间转录组）定义"疾病相关运动神经元（DMs）"态先于细胞死亡出现、有人类保守签名与 ALS 风险变异富集 [50]——这是"前退化态"在转录组/在体层的平行概念化，与本文"功能性死亡"在电生理层互补（分类轴不同：细胞状态 vs 突触功能，不可互相替代）。
- **本组后续（同组最新后续必查）：** Mehta et al. bioRxiv 2025-11-30（Fratta/Burrone/Ruepp；U7 snRNA 剪接切换治疗 STMN2+UNC13A，人 iPSC 神经元功能 rescue + 在体靶标 engagement）[54]——本文 ASO 的下一代模态；Brown et al. bioRxiv 2025-11-23（隐匿外显子的生物标志物潜力取决于对 TDP-43 缺失的敏感性与降解抵抗，书目级）[65]；Dattilo et al. bioRxiv 2026-09-20（TDP-43 功能障碍诱导隐匿环状 RNA，书目级）[64]；El-Agamy/Mattedi/Fratta *Annu Rev Genomics Hum Genet* 2026 综述把隐匿剪接收束为"蛋白稳态正反馈环路→治疗机会" [61]。
- **Gitler/Cleveland 圈后续：** Koike et al. *PLoS Biol* 2023（TDP-43 极端 N 端抑制 UNC13A 隐匿外显子；hnRNP L/A1/A2B1 独立于 TDP-43 参与抑制；hnRNP L 水平与患者脑隐匿负荷负相关——疾病修饰因子）[56]；Zeng et al. *Nat Neurosci* 2025（TDP-43 核缺失→广泛 APA 改变，与 Bryce-Smith 2025 同期平行）[46]；Quadros et al. *Acta Neuropathol* 2024（AD 中 STMN2/UNC13A 隐匿外显子与 TDP-43 病理负荷相关、与 Aβ/tau 无关；**STMN2 比 UNC13A 对 TDP-43 缺失更敏感**）[57]；Gomberg et al. bioRxiv 2025-12-03（Cleveland/Yeo；双靶 snRNA 基因治疗同时纠正 STMN2+UNC13A，AAV 在体）[55]。
- **机制精修与疾病扩展：** Watanabe et al. *EMBO J* 2025（MATR3/FUS/hnRNPA1 通过下调转录抑制因子 REST 促进 UNC13A 转录——UNC13A 调控的第二层，转录层）[59]；Zbinden 2026（NTD/寡聚化，见上）[60]；Reeves et al. *Alzheimers Res Ther* 2026（AD 杏仁核 UNC13A 隐匿 RNA 比风险 SNP 更能预测认知下降，STMN2 无此关联——把 UNC13A 治疗相关性扩展到 AD/LATE）[58]；Joseph et al. *Nat Neurosci* 2025（Kiskinis 主导、Fratta/Burrone 参与；KCNQ2 孔域外显子跳跃→无功能蛋白 ER 聚集→内在超兴奋，ASO 可 dampen——与本文"沉默"表型构成兴奋性悖论的另一半，见 B4）[44]。

### 产物命运/路径网络层：隐匿剪接的下游不止"蛋白丢失"一条路

本文把 UNC13A 隐匿外显子当作"→NMD→蛋白丢失→priming 失败"的线性病因。但领域已证明隐匿剪接产物有多种命运，阅读时须显式区分，避免把"剪接纠错"等同于"恢复全部 TDP-43 功能"：

1. **NMD→转录本/蛋白丢失**（UNC13A 主路，Brown 2022/本文）[28,1]；
2. **逃逸 NMD→翻译成 de novo 蛋白/肽**，改变蛋白相互作用、可在患者 CSF 检出（Seddighi 2024，65 肽/12 隐匿外显子，18 肽/13 基因入 CSF）[51]——隐匿剪接不仅是功能缺失，还可能产生新抗原/生物标志物；
3. **隐匿环状 RNA**（Dattilo 2026，书目级）[64]；
4. **隐匿 APA→截短 mRNA**（STMN2，Klim/Melamed/Baughn）[30–32]，或 **3′UTR 延伸→稳定性/翻译增加**（Bryce-Smith 2025——并非所有隐匿事件都是功能缺失！）[45]；
5. **逃逸 NMD→无功能蛋白聚集→显性负性样效应**（KCNQ2，Joseph 2025）[44]。

**阅读原则（本文语境下的"复制恢复≠修复完成"类比）：**
- **剪接纠错 ≠ TDP-43 功能恢复。** 本文 CE DEL/ASO 只修 UNC13A 一个事件；STMN2 提前加尾不被 rescue（ED Fig. 5f–i，文献解读），其余数百事件仍在。rescue 是"事件特异"的，不是"全局剪接恢复"。
- **PSI 恢复 ≠ 蛋白满额 ≠ 功能满额。** 剪接 >90% 纠正只换来 30–50%（M21-4）至 >50%（M18-17）蛋白；而功能 rescue 在 ≥30% 蛋白即可发生（阈值见 B2）。三个量不可互相替代。
- **结构完整 ≠ 功能完整；突触前 rescue ≠ 回路 E/I 恢复。** 突触密度下降与 mEPSC 幅度残余下降不被 UNC13A 纠错 rescue（ED Fig. 7/11，文献解读）；纯兴奋性培养无法评估抑制性回路（见 B4）。
- **体外均质缺失 ≠ 患者马赛克；急性降解核缺失 ≠ 聚集本身。** Scialò 2025 证明聚集可诱导核缺失 [53]，但本文未用该模型，二者不可混同。

## A4. 新在哪：相对前作的真正增量（编号）

1. **首次在人神经元中确立 TDP-43 核缺失的"前退化态/功能性死亡"。** 相对 Devlin 2015（突变 MN 的进行性离子通道丢失）[42] 与 Gautier 2026（SOD1 小鼠转录组 DM 态）[50]，本文用成熟神经元急性蛋白降解（避开发育混杂）+ 存活/结构/功能三层并置，证明"结构完好、存活正常、突触通讯崩溃"且**可逆**——把治疗窗口从"阻止死亡"前移到"唤醒沉默神经元"（概念创新，体外成立）。
2. **单隐匿外显子的因果充分性。** 相对 Brown/Ma 2022 的分子机制 [27,28]，本文用 233 nt 纯合删除（同时去掉双受体+共用供体）在 TDP-43 仍缺失背景下 rescue 约 80% mEPSC 频率与网络同步，并以 STMN2 不 rescue 作事件特异内对照——把 UNC13A 从 GWAS 关联位点升级为功能因果节点，把"上百转录本紊乱"收敛到一个可药靶点（机制创新）。
3. **可给药的单点纠错 + 多体系功能收敛。** 三代 splice-switching ASO（LNA 21-nt→MOE 21-nt→18-nt MOE walk），剪接 >90%、蛋白 30–50%→>50%、参考与风险两等位基因均纠错；皮层 iNeuron 与脊髓 iMN、UCL 与 FMP 两实验室、PROTAC 与 gapmer 两种敲低、自发/诱发/单突触/网络四层级读出同向（转化型增量）。相对 Baughn 2023（STMN2/轴突再生）[32]，本文把策略移植到突触传递并叠加遗传因果锚定。
4. **人源化体内剪接药效平台。** hUNC13A reporter 小鼠（人源内含子 20 含风险 SNP）+ AAV-miR-Tardbp + ICV ASO 双给药，证明体内单点纠错可行（模型创新；但仅分子读出，见 caveats）。
5. **"rescue 不必满额"的剂量预测。** 以小鼠/人杂合遗传学 + 两个 rescue 水平（约 30% 与 >50%）支持"恢复 ≥30% 蛋白即可能有益"，调和"部分蛋白 rescue 是否够"的疑问（转化预测，非完整剂量-反应，见 B2）。
6. **诚实划界本身是贡献。** 明确把 mEPSC 幅度/突触密度/活性突触数归为 UNC13A 非依赖成分，保留 Pr rescue P=0.052 的趋势性、体内 partially rescued——防止把 UNC13A 夸大为唯一解释（见 A5）。

## A5. 须留意的局限（不软化）

**本文自陈/数据层（与文献解读一致）：**
- 单突触 Pr rescue **P=0.052**（n=66 突触，趋势，未标星）；活性突触数不 rescue（ED Fig. 11a）；Fig. 1l 配对 P=0.0508、ED Fig. 3f 放电率 P=0.0687 亦未过门槛。
- 体内**仅分子剪接药效、partially rescued**（Fig. 3h–k），无在体电生理/行为/生存；"ASO 恢复体内回路功能"是外推。
- **HaloTag 标签本身有轻度功能代价**（ED Fig. 1i），需 CRISPRi 互证。
- **hUNC13A 系为串联重复异常靶向系**（同源重组伴载体串联重复、部分骨架落入内含子 23；Methods 自陈，但人源内含子位置/剪接正确）——药效解读的模型保真度边界。
- **急性降解模拟核缺失、不模拟聚集本身**；均质缺失比患者马赛克更极端；纯兴奋性培养无抑制性中间神经元，无法评估超兴奋/E-I。
- **无患者来源神经元**；患者 UNC13A 蛋白数据不可得，仅 FANS 转录组间接支持（缺核 TDP-43 细胞群 >90% UNC13A 转录本含隐匿外显子，本文 refs 6,41）[1,28,43]。
- 30% 阈值引自小鼠/人遗传学（refs 20,25），本文只测两个 rescue 水平、**无人源蛋白剂量梯度**；ASO 转录组 off-target 仅序列预筛、无 RNA-seq 级全谱；18-nt 优于 21-nt 无结合动力学/结构解释（经验 walk）。

**跨文献/转化层（本背景解读补充）：**
- **在体单靶充分性存在正面反证：** Wong 圈脊髓 MN 模型显示单独 Unc13a 纠错不缓解运动神经元病、需多靶，且脊髓 MN 的 Unc13a 隐匿负荷低于脑 [48]。本文 iMN 的体外 rescue 不能外推为"脊髓在体单靶够"。这是本文治疗主张最重要的未裁决张力（B1）。
- **临床先例并非全胜：** tofersen VALOR 主要终点阴性 [40]；"降靶标/生物标志物≠临床获益"。TRCN-1023 仅 Phase 1/2（n≈30）[73]，疾病修饰未证。
- **人类遗传学剂量 nuance：** Asadollahi 2025 摘要同时报告杂合编码/剪接变异可致 NDD（含 LoF 型突触强度下降）[37]，与本文"杂合 LoF 个体无神经生理异常"的引用（ref 25）需在变异分层层面调和（B2）。
- **版本：** Brown 2022 有 2024 Author Correction，更正内容未核 [29]；本文与 TRCN-1023 的化合物对应关系未声明（推断）。

## A6. 收束

本文是 **Fratta/Burrone/Lipstein 联盟**把经营十余年的"TDP-43 核缺失→隐匿剪接"框架（2011/2015 概念→2022 UNC13A 机制+遗传→2023 ASO 先例）推进到**"单事件功能因果 + 可给药纠错 + 临床管线"**的 territory：核心 reframe 是"TDP-43 蛋白病的突触失效由一个可药剪接节点主导，神经元先功能性死亡、后物理死亡，而唤醒它们只需部分蛋白恢复"。它以此解释为何 UNC13A 剪接纠错 ASO 值得覆盖约 97% ALS/约 50% FTD（乃至 AD/LATE [58]），并直接孵化了 Trace 的 TRCN-1023 Phase 1/2 [3,73]。但其"单靶够"的边界被在体脊髓数据 [48] 与多事件联合 rescue 数据 [47] 明确限定——**这是一篇把治疗哲学从"修全部剪接"改写为"抓主节点"的论文，而主节点能否独自撑起在体疾病修饰，仍是开放问题。**

---

# Pillar B · 面向读者的问题精研

## 问题清单（吸收文献解读"问题 seeding"六问 + 任务四问，合并为五）

1. **B1｜单点 UNC13A 纠错为何能 rescue 突触功能，而 STMN2 不 rescue 突触、脊髓在体又需多靶？**（事件特异 vs 全局；剩余 20% 频率 + 幅度/密度归谁；单靶 vs 多靶张力）
2. **B2｜≥30% 蛋白阈值是可靠治疗窗吗？**（小鼠/人遗传学外推；Asadollahi 变异分层 nuance；剂量-反应缺口）
3. **B3｜ASO 能否映射临床？**（nusinersen/tofersen/FUS 先例；TRCN-1023 Phase 1/2；递送/剂量/时程/生物标志物缺口；U7/snRNA 下一代）
4. **B4｜前退化态是可逆窗口吗？突触沉默如何与临床皮层超兴奋共存？**（时间维度；E/I 偏移；聚集 vs 核缺失；马赛克）
5. **B5｜Pr rescue P=0.052 是真实效应还是 power 不足？priming 恢复有无直接证据？18-nt 为何优于 21-nt？**（统计/机制/化学三小问）

每问按"分层拆解→跨文献证据与分级→建立/推断/未知→最强单一实验及其限度→同组后续与张力→下一步"展开。分级用语：Strong / Moderate-to-strong / Moderate / Coherent-but-retrospective / Weak / Unknown，并说明凭什么。

## B1. 一个剪接事件凭什么扛起 80% 的突触功能？——权重、特异性与"单靶 vs 多靶"的正面张力

**分层拆解：** (a) 为什么 UNC13A 权重这么大？(b) 为什么 rescue 是事件特异而非全局？(c) 剩余约 20% 频率 + 幅度/密度下降归谁？(d) 单靶在体到底够不够？

**跨文献证据与分级：**
- **(a) UNC13A 高权重的三重理由（Moderate-to-strong，机制推断+实验支持）：** 其一，蛋白剂量-功能阈值——Unc13a 低于约 30% 才出现强突触缺陷（本文引 refs 20,25）[36,37]，而 TDP-43 缺失使 UNC13A 蛋白 10 天降至 <5%（本文）[1]，即把蛋白压到阈值以下最深处；其二，priming 是释放的瓶颈步——Munc13 缺失使释放几乎归零而结构正常（Augustin/Varoqueaux）[33,34]，故 UNC13A 是"单点故障"型节点；其三，遗传学独立佐证其权重——UNC13A 是 ALS 第二强 GWAS 信号且修饰生存 [23–26]，AD 中其隐匿 RNA 比 SNP 更能预测认知下降、STMN2 无此关联 [58]。**凭什么不是 Strong：** 权重排序是跨文献推断，本文未做全转录本权重分解实验。
- **(b) 事件特异性（Strong，本文直接证据）：** CE DEL 不 rescue STMN2 提前加尾（ED Fig. 5f–i）、不 rescue mEPSC 幅度残余下降与突触密度下降（ED Fig. 7）、不 rescue 活性突触数（ED Fig. 11a）[1,文献解读]。这是干净的负性内对照，证明 rescue 不是全局剪接恢复。
- **(c) 剩余成分归谁（Moderate，方向已知、分子未定）：** 本文把幅度/密度归因于其他错剪接转录本（指向 ref 40）[1]。Guo 2026 给出候选：KALRN/RAP1GAP/SYT7/KCNQ2，单 ASO 部分恢复、联合几乎完全 rescue [47]；Joseph 2025 的 KCNQ2 影响内在兴奋性而非量子幅度 [44]。**未知：** 驱动 postsynaptic 量子幅度与突触丢失的具体转录本未被本文鉴定。
- **(d) 单靶在体够不够（跨文献张力，未裁决）：** 本文体外人皮层 iNeuron 单点 rescue 约 80% 频率 [1]；Guo 2026 人干细胞神经元联合 ASO 几乎完全 rescue [47]；Wong 圈小鼠脊髓 MN 单 Unc13a 不缓解疾病、多靶才减轻 MN 丢失，且脊髓 MN 隐匿负荷低于脑 [48]；同圈前脑单 Unc13a 足以保存记忆 [49]。**并列条件：** 物种（人 iPSC vs 小鼠）、细胞类型（皮层兴奋性 vs 脊髓 MN vs 前脑）、读出（突触功能 vs MN 存活/疾病 vs 记忆）、缺失模式（急性均质 vs 发育期敲除）各不相同。一个相容的分工模型是：**UNC13A 单靶足以恢复"脑/皮层突触通讯与认知"，但不足以独自阻止"脊髓运动神经元丢失"，后者需多靶**——但这只是推断，三套体系未在同一实验内对勘，**未裁决**。

**建立/推断/未知：** 建立——单事件对体外突触频率/同步的因果充分性、事件特异性。推断——UNC13A 高权重的阈值/瓶颈解释、"脑单靶够/脊髓需多靶"分工。未知——剩余 20% 与幅度/密度的分子身份、在体单靶对脊髓疾病修饰的充分性。

**最强单一实验 + 限度：** 本文 CE DEL（233 nt 纯合删除）在 TDP-43 仍缺失背景下 rescue 80% 频率 + STMN2 不 rescue 内对照——这是单事件充分性最干净的一枚实验。**限度：** 组成型删除不能模拟"病程中给药"的时间维度（由 ASO 补）；只在体外均质缺失、纯兴奋性培养成立；不能回答在体脊髓疾病修饰。

**同组后续与张力：** 本组 Mehta U7 2025 已把策略扩到 STMN2+UNC13A 双靶 [54]，Gitler/Cleveland 的 Guo 2026 [47]/Gomberg 2025 [55] 走联合/双靶——**领域实际方向是"以 UNC13A 为锚的多靶"，而非纯单靶**；这与本文标题的单点叙事形成口径差，须并列。

**下一步（最有信息量）：** 在同一人源体系做 UNC13A ASO ± STMN2/KCNQ2/KALRN ASO 的头对头，分解频率/幅度/密度/存活各成分的权重；在 hUNC13A 小鼠补脊髓在体功能/行为/生存读出，直接检验 Wong 张力。

## B2. 30% 蛋白阈值：治疗窗还是插值推测？

**分层拆解：** (a) 阈值从哪来？(b) 人源证据够不够？(c) 变异类型是否破坏"单调剂量阈值"假设？(d) 能否外推到患者给药剂量？

**跨文献证据与分级：**
- **(a) 阈值来源（Moderate，小鼠为主）：** 本文引 Zarebidaki 2020（RIM/Munc13 剂量-传递，小鼠培养 hippocampal 神经元）[36] 与 Asadollahi 2025 [37]，称"低于约 30% 才出现强突触缺陷"；杂合小鼠/杂合 LoF 人无神经生理异常（本文引 refs 18,25）[33,37]。**注意：** Zarebidaki 摘要未给"30%"具体数值，该数字是本文对 refs 20,25 的概括，原始剂量-反应曲线需全文核（本次未读全文，标推断）。
- **(b) 本文人源证据（Moderate，两点非曲线）：** M21-4（约 30% 蛋白）与 M18-17（>50%）均 rescue mEPSC 频率 [1]。这是两个离散 rescue 水平、**非完整剂量-反应**；"≥30% 即有益"在人体系是插值。
- **(c) 变异分层 nuance（跨文献张力）：** Asadollahi 2025 摘要报告 UNC13A 生殖系编码/剪接变异致 NDD，含三类机制——LoF 型突触强度下降、GoF 型传递增强、第二信使调控受损，分 A–C 亚型 [37]。**这与本文"杂合 LoF 个体无神经生理异常"的引用并不在摘要层直接矛盾，但提示"剂量阈值"不是单调的：某些杂合 LoF 变异致病、某些良性，取决于变异类别与位置。** 哪些 LoF 变异良性、哪些致病，需 Asadollahi 全文变异级数据裁决（本次摘要级，未裁决）。
- **(d) 临床剂量学（Unknown）：** 本文未给患者剂量梯度；nusinersen/tofersen 的剂量方案不能直接迁移（不同靶标/化学/递送）[39,40]。

**建立/推断/未知：** 建立——小鼠 Munc13 剂量-传递关系、本文两个 rescue 水平有效。推断——"≥30% 人源蛋白即有益"、杂合良性。未知——人源完整剂量-反应、变异分层阈值、患者给药剂量。

**最强单一实验 + 限度：** 本文 M21-4（约 30%）rescue 频率——证明"部分恢复够"的最直接一枚。**限度：** 单点、无梯度、无患者细胞、阈值原始出处为小鼠。

**同组后续：** 本组未发人源剂量梯度后续（检索边界内）；Asadollahi 2025 的变异分层是阈值精修的关键外部资源 [37]。

**下一步：** 人神经元蛋白剂量梯度（10/30/50/80%）× 功能读出完整曲线；按 Asadollahi 变异类别分层检验"良性杂合"边界；把阈值与 TRCN-1023 临床剂量-靶标 engagement 桥接。

## B3. ASO 能否映射临床？——先例、管线与未闭合的转化链

**分层拆解：** (a) 剪接切换 ASO 的临床先例证明了什么、没证明什么？(b) 本文管线到哪一步？(c) 递送/剂量/时程/生物标志物缺口？(d) 下一代模态？

**跨文献证据与分级：**
- **(a) 先例（Strong 于"可成药"，Weak 于"必然临床获益"）：** nusinersen ENDEAR 证明剪接切换 ASO 可改变 SMA 病程（运动里程碑 51% vs 0%，生存 HR 0.37）[39]，Rigo 2012 记录研发路径 [38]。但 tofersen VALOR 主要终点阴性（P=0.97）、结论自陈未改善临床终点，仅生物标志物下降 + 52 周 early-start 非校正信号 [40]；FUS ION363 仅单例 [41]。**教训：靶标 engagement/生物标志物≠临床获益；越早治可能越好（nusinersen/tofersen early-start 一致暗示）。**
- **(b) 本文管线（Moderate，临床前→早期临床）：** 本文交付 M21-4/M18-17 + hUNC13A 体内分子药效 [1]；Trace TRCN-1023（UNC13A 剪接纠错 ASO）已启动 **FUNCtion ALS：NCT07674667，随机双盲安慰剂对照 Phase 1/2，鞘内注射 TRCN-1023 vs aCSF，成人 ALS，估计 n=30，2026-08-20 启动、招募中**（ClinicalTrials.gov 核证）[73]；公司页称进入人体试验 [3]。**本文化合物与 TRCN-1023 的对应关系未声明（同管线推断）。**
- **(c) 缺口（Unknown）：** 本文单次 ICV 30 mg/ml×10 µl、3 周终点，无慢性给药、脊髓/皮层分布定量、剂量-PSI 曲线 [1,文献解读]；ASO 转录组 off-target 无 RNA-seq 全谱；患者来源神经元未验证。生物标志物侧有外部资源：Seddighi 2024 CSF 隐匿肽 [51]、Brown 2025 隐匿外显子生物标志物潜力 [65]、NfL（tofersen 用）[40]。
- **(d) 下一代模态（Moderate，临床前）：** 本组 Mehta U7 snRNA 双靶（STMN2+UNC13A，在体 engagement）[54]；Cleveland/Yeo Gomberg 双靶 snRNA 基因治疗（AAV 在体）[55]；Wilkins TDP-REG 疾病态触发表达/prime editing [52]。**模态从"反复鞘内 ASO"向"一次性基因治疗/疾病态触发"演进，但均在临床前。**

**建立/推断/未知：** 建立——剪接切换 ASO 可成药（SMA）、TRCN-1023 进入 Phase 1/2。推断——本文→TRCN-1023 同管线、早治获益。未知——UNC13A ASO 的临床疾病修饰、患者剂量方案、长期安全性。

**最强单一实验 + 限度：** ENDEAR（nusinersen）是剪接切换 ASO 临床概念验证的最强一枚。**限度：** SMA 是单基因、发育期、SMN2 剂量明确的疾病；ALS 是散发/多因素、成人、TDP-43 马赛克——迁移是推断，tofersen 已警示。

**同组后续：** Mehta U7 [54]、Wilkins TDP-REG [52] 是本组对"ASO 之后"的回答；TRACE 管线 [3,73] 是转化落地。

**下一步：** TRCN-1023 Phase 1/2 读出（靶标 engagement/CSF 隐匿肽/NfL/安全性）；慢性给药 PK/PD + 脊髓分布；患者 iPSC 神经元 rescue 幅度保守性检验；early-vs-late 分层设计。

## B4. 前退化态是可逆窗口吗？——沉默与超兴奋悖论、时间维度与模型保真

**分层拆解：** (a) "功能性死亡"可逆吗、窗口多长？(b) 突触沉默如何与临床皮层超兴奋共存？(c) 核缺失 vs 聚集、均质 vs 马赛克的外推边界？

**跨文献证据与分级：**
- **(a) 可逆性（Moderate，体外）：** 本文成熟网络（DIV33 晚期 KD）ASO rescue 网络同步大于早期（\*\*\*，文献解读）[1]，支持"成熟沉默网络可被唤醒"；但无长期随访、无在体功能、无患者细胞。Devlin 2015 的"功能失调但存活" [42] 与 Gautier 2026 的"DM 态先于死亡" [50] 从疾病侧支持"存在可干预的前退化窗口"，但分类轴不同（突触功能 vs 细胞状态），不可互替。
- **(b) 沉默 vs 超兴奋（Weak→Moderate，电路推断+外部机制证据）：** 临床 TMS 见 ALS 早期皮层超兴奋且随进展加重、与差生存相关（Menon 2020，444 患者）[66]；本文 UNC13A 丢失致突触沉默 [1]。悖论的电路解释：**兴奋性输出下降→前馈抑制减弱→E/I 比偏移→网络超兴奋**。外部机制支撑：Dos Santos 2023（Stxbp1 单倍不足小鼠，兴奋性突触无法招募抑制性中间神经元→超兴奋，ampakine CX516 恢复招募）[67]；Engel 2016（双等位 MUNC13-1 截短，RRP 耗竭但量子释放概率正常、终板结构正常，皮层超兴奋+致命肌无力）[68]；Asadollahi 2025（UNC13A 变异致癫痫）[37]；Joseph 2025（KCNQ2 错剪接→内在超兴奋，独立于 UNC13A）[44]；Harley 2023（ALS MN 早期超兴奋→晚期低兴奋）[10]、Devlin 2015 同向 [42]。**本文纯兴奋性培养只能表现失同步、不能表现超兴奋，E/I 假说在本文体系内不可证伪（作者自陈）。**
- **(c) 模型保真（Moderate，边界明确）：** 急性降解模拟核缺失而非聚集（Scialò 2025 证明聚集可诱导核缺失，但本文未用）[53]；均质缺失比患者马赛克极端；hUNC13A 串联重复异常靶向系（剪接正确但结构异常）[1]。

**建立/推断/未知：** 建立——体外沉默可逆、临床超兴奋存在、KCNQ2 独立致超兴奋。推断——E/I 偏移解释沉默-超兴奋共存、前退化窗口可干预。未知——患者马赛克背景下可逆比例与窗口时长、在体超兴奋与 UNC13A 的因果、聚集模型的 rescue。

**最强单一实验 + 限度：** 本文晚期 KD（DIV33）ASO rescue 同步大于早期——支持"成熟网络可唤醒"的最强一枚。**限度：** 体外、纯兴奋性、无在体、无长期随访。

**同组后续与张力：** Scialò 2025（聚集→核缺失）[53] 是补"聚集"短板的本组资源；Joseph 2025（KCNQ2 超兴奋）[44] 与本文沉默构成同组内的表型互补；Wong 圈前脑/脊髓差异 [48,49] 提示"窗口"可能脑区依赖。

**下一步：** 引入抑制性中间神经元的共培养/类器官检验 E/I 偏移；Scialò 种子聚集模型 + ASO 检验"聚集背景下"可逆性；患者马赛克模型；hUNC13A 小鼠在体 EEG/行为检验超兴奋-沉默关系。

## B5. Pr rescue P=0.052：真实效应还是 power 不足？priming 有无直接证据？18-nt 为何更优？

**分层拆解：** (a) P=0.052 怎么读？(b) priming 恢复是直接证据还是功能推断？(c) 18-nt > 21-nt 的化学 rationale？

**跨文献证据与分级：**
- **(a) 统计（Weak-to-Moderate）：** n=66 突触、P=0.052、方向与 eEPSC/mEPSC rescue 一致（本文）[1,文献解读]。这是趋势而非过门槛证据；多读出同向提高可信度，但单突触 Pr 本身未达显著。**不能把"方向一致"当作"Pr rescue 已证"。**
- **(b) priming 直接证据（Moderate，功能推断；缺结构/生化直接测量）：** 本文把缺陷定位到 priming 是基于 Munc13 生物学（Augustin/Varoqueaux/Imig）[33–35] 的功能推断，**未直接测 primed 小泡池**。外部框架：Imig 2014 论证 docking=priming 的形态学对应（冷冻固定+电子断层）[35]；Lin 2025 用动力学建模+NTF 区分 priming 状态与融合概率、证明 Munc13/PKC 激活增加成熟 primed 小泡丰度 [62]；Zarebidaki 2020 区分 RIM/Munc13 在定位/priming 的重叠与独立作用 [36]；Jusyte 2023（果蝇 NMJ，Unc13A CaM 域调控 STF/PHP）[63]——**注意跨物种：果蝇 Unc13A 结论迁移到人 UNC13A 是推断**。本文活性突触数不 rescue（ED Fig. 11a）[1] 提示 rescue 限于"剩余突触的释放机器"，而非突触数量。
- **(c) 18-nt vs 21-nt（Moderate，经验性；Unknown 机制）：** 本文 18-nt MOE walk（M18-17）蛋白 rescue >50% 优于 21-nt（M21-4/5，30–50%），按 off-target 与二级结构预筛 [1,文献解读]；**无结合动力学/结构解释**。LNA→MOE 的化学切换出于耐受性（文献解读），18-nt 更优的具体亲和力/剪接切换效率 rationale 未明。

**建立/推断/未知：** 建立——KD 降 Pr、ASO 升 Pr 趋势、多读出同向。推断——priming 恢复（功能推断）、18-nt 更优的经验事实。未知——primed 池直接测量、Pr rescue 的显著性、18-nt 的化学/结构机制。

**最强单一实验 + 限度：** iGluSnFR3 单突触 Pr 成像（盲法、45 次 1 Hz 场刺激）是把 eEPSC 分解为 Pr×量子×突触数的最强一枚。**限度：** P=0.052、活性突触数不 rescue、无 primed 池生化/结构对照。

**同组后续：** 本组未发 primed 池直接测量后续（检索边界内）；Lipstein 圈 Lin 2025 [62]/Ranjan 2026（书目级）提供 priming 状态的方法学框架。

**下一步：** 蔗糖释放池（RRP）+ 电镜 docked/primed 计数 + MK-801 使用依赖阻断，在 ASO 处理人神经元直接测 priming；扩大 n 闭合 P=0.052；18-nt/21-nt 结合动力学（如 SPR/荧光偏振）与剪接切换效率定量，解释长度-效力关系。

## Summary scorecard（机制链逐环）

| 链中一环 | 关键证据 | 分级 |
| --- | --- | --- |
| TDP-43 核缺失 → UNC13A 隐匿外显子 inclusion | Brown/Ma 2022 + 本文 PSI 翻转 [27,28,1] | Strong |
| inclusion → NMD → mRNA/蛋白耗竭（10 天 <5%） | Brown 2022 + 本文 Western [28,1] | Strong |
| UNC13A 丢失 → priming 失败 | Munc13 生物学推断；无 primed 池直接测量 [33–35,1] | Moderate（功能推断） |
| priming 失败 → Pr↓ → mEPSC/eEPSC↓ | iGluSnFR3 Pr↓；rescue P=0.052 [1] | Strong（缺陷）/ Weak-Moderate（rescue） |
| 单事件对频率/同步的因果充分性 | CE DEL 80% rescue + STMN2 不 rescue 内对照 [1] | Strong（体外） |
| 幅度/密度/活性突触数 UNC13A 非依赖 | ED Fig. 7/11 负性结果 [1] | Strong（负性） |
| ASO → 剪接>90% → 蛋白 30–>50% → 功能 rescue | 多体系/多实验室/多读出收敛 [1] | Strong（体外） |
| 体内单点纠错 | hUNC13A 小鼠 partially rescued，仅分子读出 [1] | Moderate（分子）/ Unknown（功能） |
| ≥30% 蛋白治疗阈值 | 小鼠遗传学 + 本文两点；Asadollahi 变异 nuance [36,37,1] | Moderate（外推） |
| 前退化态可逆 | 晚期 KD rescue 更大；无在体/患者/长期 [1] | Moderate（体外） |
| 单靶在体疾病修饰充分性 | Wong 脊髓反证 + Guo 多靶联合 [48,47] | Unknown（未裁决张力） |
| 临床疾病修饰 | TRCN-1023 Phase 1/2 进行中；tofersen 警示 [73,40] | Unknown |

## 最有价值的后续实验（闭合因果缺口）

1. **在体功能闭环：** hUNC13A 小鼠脊髓在体电生理/NMJ/运动行为/生存 + 慢性 ASO 剂量-PSI 曲线 + 脊髓 vs 皮层分布定量——直接检验 Wong 脊髓张力 [48] 与本文"体内仅分子"缺口。
2. **priming 直接测量：** 蔗糖 RRP + 电镜 docked/primed 计数 + MK-801  progressive block，在 ASO 人神经元闭合 P=0.052 与"priming 恢复"功能推断。
3. **患者与模型保真：**  sporadic ALS/FTD 患者 iPSC MN/皮层神经元（按风险 SNP 分层）+ 马赛克缺失 + Scialò 种子聚集模型 [53]，检验 rescue 幅度保守性与可逆窗口。
4. **单靶 vs 多靶头对头 + off-target 全谱：** 同一人源体系 UNC13A ASO ± STMN2/KCNQ2/KALRN ASO，分解频率/幅度/密度/存活权重（调和 Guo [47]/Wong [48]）；RNA-seq 级全转录本剪接 off-target。
5. **人源剂量-反应 + 临床桥接：** 蛋白 10/30/50/80% 梯度 × 功能曲线，按 Asadollahi 变异类别分层 [37]；CSF 隐匿肽 [51]/NfL 桥接 TRCN-1023 Phase 1/2 [73]。

---

## A7. 建议阅读顺序（以最少文献建立完整逻辑）

**第一轮·主干（发现→核缺失→隐匿外显子→遗传锚定→UNC13A 机制→priming 基线→ASO 先例→本文与张力并读）：**

1. Neumann 2006 + Arai 2006 [16,17]——读它为了回答"TDP-43 凭什么成为 ALS/FTD 的共同病理蛋白"。重点看其病理蛋白鉴定/磷酸化图（编号待核）。
2. Polymenidou 2011 + Tollervey 2011 [20,21]——"核缺失如何变成剪接紊乱"。Tollervey 重点看深内含子 UG 结合簇/位置依赖剪接图（编号待核，隐匿外显子抑制的概念种子）。
3. Ling 2015 [22]——"隐匿外显子为何能致病"。重点看 NMD/强制抑制防死亡图（编号待核）。
4. van Es 2009 + Diekstra 2012 + Willemse 2023 [23,24,26]——"UNC13A 的人群遗传与治疗靶点论证"。重点看 GWAS 信号/生存修饰图（编号待核）。
5. Ma 2022 + Brown 2022 [27,28]——**直接地基**，"TDP-43 抑制 UNC13A 隐匿外显子 + 风险 SNP 加剧"。Brown 重点看风险 SNP/患者组织图、Ma 重点看 TDP-43 结合/抑制图（编号待核）；注意 Brown 2024 更正 [29]。
6. Augustin 1999 + Varoqueaux 2002 [33,34]——"没有 Munc13，结构正常但释放归零"。重点看 null 小鼠电生理/超微结构图（编号待核）。
7. Baughn 2023 [32]——"ASO 纠正隐匿事件的同族先例"。重点看 STMN2 机制/ASO 纠正/人源化小鼠图（编号待核）。
8. **本文 + 文献解读**——Fig. 1（急性核缺失表型）、Fig. 2（CE DEL 单事件因果）、Fig. 3（ASO 优化+体内）、Fig. 4（多体系功能 rescue）；逐图四字段见文献解读，不在此重做。
9. Guo 2026 + Peethambaran 2026 + Cao 2026 [47,48,49]——**与本文并读的张力**，"单靶 vs 多靶、脑 vs 脊髓"。重点看联合 ASO rescue/脊髓 MN 疾病/记忆图（编号待核）。

**第二轮·按兴趣分支：**
- **priming 机制/剂量：** Imig 2014 [35]、Zarebidaki 2020 [36]、Lin 2025 [62]、Asadollahi 2025 [37]（重点看剂量-传递/变异功能图，编号待核）。
- **临床转化：** Finkel 2017 [39]、Miller 2022 [40]、Rigo 2012 [38]、Willemse 2023 [26]、NCT07674667 [73]（重点看 ENDEAR/VALOR 临床终点图，编号待核）。
- **实验平台：** Tovell 2019（HaloPROTAC）[69]、Aggarwal 2023（iGluSnFR3）[70]、Meijer 2019/Bekkers 1991（自突触）[71,72]（重点看降解曲线/探针动力学/微岛图，编号待核）。
- **产物命运/疾病扩展：** Seddighi 2024 [51]、Bryce-Smith 2025 [45]、Joseph 2025 [44]、Reeves 2026 [58]、Gautier 2026 [50]（重点看 de novo 肽/隐匿 APA/KCNQ2/AD 认知/DM 态图，编号待核）。
- **同组后续/下一代：** Wilkins 2024 [52]、Mehta U7 2025 [54]、Gomberg 2025 [55]、Zbinden 2026 [60]（重点看 TDP-REG/U7/双靶 snRNA/NTD-寡聚化图，编号待核）。

（与文献解读文末"延伸文献与图引清单"互补：后者侧重哪篇哪图值得摘/讲，本节侧重以最少文献建立逻辑链。外部图号凡未核到一律"编号待核"，不编造。）

## A8. 逐文献证据索引表

声明：本文"全文定向核读"指复用 fulltext.txt 并定向核对题录/结果/讨论/方法/资助/COI，不表示逐段审计全部补充材料；"完整摘要"行不承载超出完整摘要的实验细节；"仅书目"行不补写未读到的实验细节；外部图号未核实处标"编号待核"。

| 文献（在线/卷期） | 模型与主要贡献 | 解释边界 | 阅读深度 |
| --- | --- | --- | --- |
| 本文 Keuss 2026 Nature [1] | 人 iPSC 神经元+小鼠；单事件因果+ASO rescue | 体外均质/纯兴奋性；体内仅分子；Pr P=0.052 | 全文定向核读 |
| 本文预印本 bioRxiv 2024 [2] | 同题早期版本 | 与正式版标题/内容差异未逐句对勘 | 仅书目 |
| Ou 1995 J Virol [14] | TDP-43 作为 HIV TAR DNA 结合蛋白克隆 | 分子发现前史；无疾病功能 | 仅书目 |
| Brenner 1974 Genetics [15] | 线虫遗传学奠基（unc-13 命名） | 前史；物种线虫 | 仅书目 |
| Neumann 2006 Science [16] | 生化鉴定 TDP-43 为 FTLD-U/ALS 病理蛋白 | 病理鉴定，非功能因果 | 完整摘要 |
| Arai 2006 BBRC [17] | 免疫组化鉴定 TDP-43 包涵体成分 | 与 Neumann 互补 | 完整摘要 |
| Sreedharan 2008 Science [18] | TARDBP M337V 家系连锁 | 家族性；突变致病 | 完整摘要 |
| Kabashi 2008 Nat Genet [19] | TARDBP 8 错义/9 个体 | 关联，与 Sreedharan 并行 | 完整摘要 |
| Polymenidou 2011 Nat Neurosci [20] | 小鼠脑 ASO 敲低+CLIP，965 剪接事件 | 小鼠；核缺失→剪接 | 完整摘要 |
| Tollervey 2011 Nat Neurosci [21] | 人脑 iCLIP，位置依赖剪接/深内含子簇 | 人结合图谱；概念种子 | 完整摘要 |
| Ling 2015 Science [22] | 非保守隐匿外显子/NMD/防死亡 | 小鼠 ESC+病例；机制 | 完整摘要 |
| van Es 2009 Nat Genet [23] | UNC13A GWAS rs12608932 | 人群关联，非因果 | 完整摘要 |
| Diekstra 2012 Neurobiol Aging（在线 2011）[24] | UNC13A 生存修饰 | 关联；具体月数本文概括 | 完整摘要 |
| van Rheenen 2021 Nat Genet [25] | 15 风险位点/囊泡运输 | 人群；UNC13A 排序本文概括 | 完整摘要 |
| Willemse 2023 JNNP [26] | UNC13A 遗传→治疗靶点综述 | 综述；锂试验/ASO 提及 | 完整摘要 |
| Ma 2022 Nature [27] | TDP-43 直接抑制 UNC13A 隐匿外显子 | 分子机制；功能因果未证 | 完整摘要 |
| Brown 2022 Nature [28] | NMD/蛋白耗竭+风险 SNP+患者组织 | 分子机制；有 2024 更正 | 完整摘要 |
| Brown 2024 Author Correction [29] | 更正通知 | 更正内容未核 | 仅书目 |
| Klim 2019 Nat Neurosci [30] | STMN2/轴突再生（Eggan） | 轴突再生，非突触 | 完整摘要 |
| Melamed 2019 Nat Neurosci [31] | STMN2 隐匿 polyA 机制（Cleveland） | 机制；患者相关性 | 完整摘要 |
| Baughn 2023 Science [32] | STMN2 ASO 纠正+人源化小鼠 | 轴突再生；ASO 先例 | 完整摘要 |
| Augustin 1999 Nature [33] | Munc13-1 null 释放归零/结构正常 | 小鼠；priming 基线 | 完整摘要 |
| Varoqueaux 2002 PNAS [34] | Munc13-1/2 双敲/突触发生正常 | 小鼠；结构≠功能前身 | 完整摘要 |
| Imig 2014 Neuron [35] | 冷冻固定+电子断层，docking=priming | 小鼠超微结构 | 完整摘要 |
| Zarebidaki 2020 J Neurosci [36] | RIM/Munc13 定位/priming 区分 | 小鼠；30% 数值本文概括 | 完整摘要 |
| Asadollahi 2025 Nat Genet [37] | UNC13A 变异 NDD/三机制/A–C 亚型 | 人类遗传；变异分层 nuance | 完整摘要 |
| Rigo 2012 JCB [38] | SMA ASO 研发视角 | 综述/视角 | 完整摘要 |
| Finkel 2017 NEJM [39] | nusinersen ENDEAR III 期 | SMA 单基因；临床概念验证 | 完整摘要 |
| Miller 2022 NEJM [40] | tofersen VALOR III 期（主要终点阴性） | SOD1 ALS；临床警示 | 完整摘要 |
| Korobeynikov 2022 Nat Med [41] | FUS ASO ION363（小鼠+单例） | 单例患者；初步 | 完整摘要 |
| Devlin 2015 Nat Commun [42] | 患者 iPSC MN 功能失调但存活 | 突变 MN；前退化前身 | 完整摘要 |
| Liu 2019 Cell Rep [43] | FANS 分选核/LINE 去浓缩 | 人尸检；转录组方法 | 完整摘要 |
| Joseph 2025 Nat Neurosci [44] | KCNQ2 错剪接→内在超兴奋 | 与沉默互补；ASO 可 dampen | 完整摘要 |
| Bryce-Smith 2025 Nat Neurosci [45] | 隐匿 APA 图谱（Fratta） | 后果谱扩展；非全 LoF | 完整摘要 |
| Zeng 2025 Nat Neurosci [46] | APA 改变（Gitler，平行） | 与 Bryce-Smith 同期 | 完整摘要 |
| Guo 2026 Sci Transl Med [47] | KALRN/RAP1GAP/SYT7/KCNQ2；联合 ASO 几乎全 rescue | 多事件；与本文口径差 | 完整摘要 |
| Peethambaran Mallika 2026 bioRxiv [48] | 脊髓 MN：单 Unc13a 不够/多靶够 | 小鼠在体；预印本；张力 | 完整摘要 |
| Cao 2026 bioRxiv [49] | 前脑：单 Unc13a 保存记忆 | 小鼠在体；预印本；互补 | 完整摘要 |
| Gautier 2026 Cell [50] | DM 态先于死亡（SOD1 小鼠） | 转录组态；分类轴不同 | 完整摘要 |
| Seddighi 2024 Sci Transl Med [51] | 隐匿外显子→de novo 蛋白/CSF 肽 | 命运层；生物标志物 | 完整摘要 |
| Wilkins 2024 Science [52] | TDP-REG/SpliceNouveau 精准医学 | 疾病态触发；临床前 | 完整摘要 |
| Scialò 2025 Neuron [53] | 种子聚集→TDP-43 核缺失 | 连接聚集与核缺失 | 完整摘要 |
| Mehta U7 2025 bioRxiv [54] | U7 snRNA 双靶 STMN2+UNC13A | 本组后续；临床前 | 完整摘要 |
| Gomberg 2025 bioRxiv [55] | 双靶 snRNA 基因治疗（Cleveland/Yeo） | 临床前；AAV 在体 | 完整摘要 |
| Koike 2023 PLoS Biol [56] | hnRNP L/A1/A2B1 调控 UNC13A | 疾病修饰因子 | 完整摘要 |
| Quadros 2024 Acta Neuropathol [57] | AD 中 STMN2/UNC13A 隐匿；STMN2 更敏感 | 患者组织；敏感性问题 | 完整摘要 |
| Reeves 2026 Alz Res Ther [58] | AD 杏仁核 UNC13A 隐匿 RNA 预测认知 | 关联；扩展 AD/LATE | 完整摘要 |
| Watanabe 2025 EMBO J [59] | MATR3/FUS/hnRNPA1→REST→UNC13A 转录 | 转录层调控 | 完整摘要 |
| Zbinden 2026 bioRxiv [60] | NTD 单体结合 RNA/寡聚化抑制隐匿 | 机制精修；预印本 | 完整摘要 |
| El-Agamy 2026 Annu Rev [61] | 隐匿剪接→蛋白稳态环路综述（Fratta） | 综述 | 完整摘要 |
| Lin 2025 J Physiol [62] | priming 状态/融合概率区分（calyx） | 大鼠；方法框架 | 完整摘要 |
| Jusyte 2023 Cell Rep [63] | Unc13A CaM 域 STF/PHP（果蝇） | 跨物种；迁移推断 | 完整摘要 |
| Dattilo 2026 bioRxiv [64] | 隐匿环状 RNA | 命运层；预印本 | 仅书目 |
| Brown 2025 bioRxiv [65] | 隐匿外显子生物标志物潜力 | 预印本 | 仅书目 |
| Menon 2020 ACTN [66] | TMS 皮层超兴奋随进展加重 | 临床关联 | 完整摘要 |
| Dos Santos 2023 Cell Rep Med [67] | Stxbp1 兴奋→抑制招募失败→超兴奋 | 小鼠；电路机制 | 完整摘要 |
| Engel 2016 Neurol Genet [68] | 双等位 MUNC13-1 截短/超兴奋/肌无力 | 人类个案 | 完整摘要 |
| Tovell 2019 ACS Chem Biol [69] | HaloPROTAC-E 降解平台 | 方法；内源标签 | 完整摘要 |
| Aggarwal 2023 Nat Methods [70] | iGluSnFR3 探针 | 方法；单突触成像 | 完整摘要 |
| Meijer 2019 Cell Rep [71] | 人 iPSC 单细胞突触模型 | 方法 | 仅书目 |
| Bekkers & Stevens 1991 PNAS [72] | 自突触电流 | 方法 | 仅书目 |
| NCT07674667（FUNCtion ALS）[73] | TRCN-1023 Phase 1/2，鞘内，n≈30 | 早期临床；疾病修饰未证 | 登记库核证 |
| GitHub 代码仓库 [74] | 电生理/成像/QIAxcel/LMM 管线 | 代码 | 书目（本文声明） |
| Keuss 2016 JCS [6] / 2019 EMBO J [7] / Thorase 2019 JCBFM [8] | Keuss 早期 NEDD8/泛素轨迹 | 作者谱系旁证 | 完整摘要（[6][7]）/书目（[8]） |
| Trace 公司页 [3] / ORCID [4,5,9,12,13] / KCL 页 [11] | 作者履历/训练/管线 | 机构级；导师未声明 | 官方/登记库核证 |

## A9. References（编号带 URL）

[1] Keuss MJ et al. UNC13A splice correction rescues synaptic dysfunction induced by TDP-43 loss. Nature (2026). https://doi.org/10.1038/s41586-026-11256-2 ; EuropePMC PMID 43015463 https://europepmc.org/article/MED/43015463
[2] Keuss MJ et al. Loss of TDP-43 induces synaptic dysfunction that is rescued by UNC13A splice-switching ASOs. bioRxiv (2024-06-24). https://doi.org/10.1101/2024.06.20.599684
[3] Trace Neuroscience（公司页/创始人/管线 TRCN-1023）. https://www.traceneuro.com
[4] Pietro Fratta ORCID 0000-0002-8762-8188. https://orcid.org/0000-0002-8762-8188
[5] Matthew Keuss ORCID 0000-0002-2628-4115. https://orcid.org/0000-0002-2628-4115
[6] Keuss MJ et al. Characterization of the mammalian family of DCN-type NEDD8 E3 ligases. J Cell Sci 129:1441–1454 (2016). https://doi.org/10.1242/jcs.181784
[7] Keuss MJ et al. Unanchored tri-NEDD8 inhibits PARP-1 to protect from oxidative stress-induced cell death. EMBO J 38:e100024 (2019). https://doi.org/10.15252/embj.2018100024
[8] Zhang J et al. The AAA+ ATPase Thorase is neuroprotective against ischemic injury. J Cereb Blood Flow Metab 39:1836–1848 (2019). https://doi.org/10.1177/0271678X18769770
[9] Peter Harley ORCID 0000-0001-6689-0227. https://orcid.org/0000-0001-6689-0227
[10] Harley P et al. Aberrant axon initial segment plasticity and intrinsic excitability of ALS hiPSC motor neurons. Cell Rep 42:113509 (2023). https://doi.org/10.1016/j.celrep.2023.113509
[11] Juan Burrone, King's College London 官方页. https://www.kcl.ac.uk/people/juan-burrone
[12] Juan Burrone ORCID 0000-0003-1233-668X. https://orcid.org/0000-0003-1233-668X
[13] Noa Lipstein ORCID 0000-0002-0755-5899. https://orcid.org/0000-0002-0755-5899
[14] Ou SH et al. Cloning and characterization of a novel cellular protein, TDP-43, that binds to HIV-1 TAR DNA sequence motifs. J Virol 69:3584–3596 (1995). https://doi.org/10.1128/jvi.69.6.3584-3596.1995
[15] Brenner S. The genetics of Caenorhabditis elegans. Genetics 77:71–94 (1974). https://doi.org/10.1093/genetics/77.1.71
[16] Neumann M et al. Ubiquitinated TDP-43 in frontotemporal lobar degeneration and amyotrophic lateral sclerosis. Science 314:130–133 (2006). https://doi.org/10.1126/science.1134108
[17] Arai T et al. TDP-43 is a component of ubiquitin-positive tau-negative inclusions in frontotemporal lobar degeneration and amyotrophic lateral sclerosis. BBRC 351:602–611 (2006). https://doi.org/10.1016/j.bbrc.2006.10.093
[18] Sreedharan J et al. TDP-43 mutations in familial and sporadic amyotrophic lateral sclerosis. Science 319:1668–1672 (2008). https://doi.org/10.1126/science.1154584
[19] Kabashi E et al. TARDBP mutations in individuals with sporadic and familial amyotrophic lateral sclerosis. Nat Genet 40:572–574 (2008). https://doi.org/10.1038/ng.132
[20] Polymenidou M et al. Long pre-mRNA depletion and RNA missplicing contribute to neuronal vulnerability from loss of TDP-43. Nat Neurosci 14:459–468 (2011). https://doi.org/10.1038/nn.2779
[21] Tollervey JR et al. Characterizing the RNA targets and position-dependent splicing regulation by TDP-43. Nat Neurosci 14:452–458 (2011). https://doi.org/10.1038/nn.2778
[22] Ling JP et al. TDP-43 repression of nonconserved cryptic exons is compromised in ALS-FTD. Science 349:650–655 (2015). https://doi.org/10.1126/science.aab0983
[23] van Es MA et al. Genome-wide association study identifies 19p13.3 (UNC13A) and 9p21.2 as susceptibility loci for sporadic ALS. Nat Genet 41:1083–1087 (2009). https://doi.org/10.1038/ng.442
[24] Diekstra FP et al. UNC13A is a modifier of survival in amyotrophic lateral sclerosis. Neurobiol Aging 33:630.e3–8 (2012; 在线 2011). https://doi.org/10.1016/j.neurobiolaging.2011.10.029
[25] van Rheenen W et al. Common and rare variant association analyses in ALS identify 15 risk loci with distinct genetic architectures and neuron-specific biology. Nat Genet 53:1636–1648 (2021). https://doi.org/10.1038/s41588-021-00973-1
[26] Willemse SW et al. UNC13A in amyotrophic lateral sclerosis: from genetic association to therapeutic target. JNNP 94:649–656 (2023). https://doi.org/10.1136/jnnp-2022-330504
[27] Ma XR et al. TDP-43 represses cryptic exon inclusion in the FTD–ALS gene UNC13A. Nature 603:124–130 (2022). https://doi.org/10.1038/s41586-022-04424-7
[28] Brown AL et al. TDP-43 loss and ALS-risk SNPs drive mis-splicing and depletion of UNC13A. Nature 603:131–137 (2022). https://doi.org/10.1038/s41586-022-04436-3
[29] Brown AL et al. Author Correction: TDP-43 loss and ALS-risk SNPs drive mis-splicing and depletion of UNC13A. Nature 631:E7 (2024). https://doi.org/10.1038/s41586-024-07577-9
[30] Klim JR et al. ALS-implicated protein TDP-43 sustains levels of STMN2, a mediator of motor neuron growth and repair. Nat Neurosci 22:167–179 (2019). https://doi.org/10.1038/s41593-018-0300-4
[31] Melamed Z et al. Premature polyadenylation-mediated loss of stathmin-2 is a hallmark of TDP-43-dependent neurodegeneration. Nat Neurosci 22:180–190 (2019). https://doi.org/10.1038/s41593-018-0293-z
[32] Baughn MW et al. Mechanism of STMN2 cryptic splice-polyadenylation and its correction for TDP-43 proteinopathies. Science 379:1140–1149 (2023). https://doi.org/10.1126/science.abq5622
[33] Augustin I et al. Munc13-1 is essential for fusion competence of glutamatergic synaptic vesicles. Nature 400:457–461 (1999). https://doi.org/10.1038/22768
[34] Varoqueaux F et al. Total arrest of spontaneous and evoked synaptic transmission but normal synaptogenesis in the absence of Munc13-mediated vesicle priming. PNAS 99:9037–9042 (2002). https://doi.org/10.1073/pnas.122623799
[35] Imig C et al. The morphological and molecular nature of synaptic vesicle priming at presynaptic active zones. Neuron 84:416–431 (2014). https://doi.org/10.1016/j.neuron.2014.10.009
[36] Zarebidaki F et al. Disentangling the roles of RIM and Munc13 in synaptic vesicle localization and neurotransmission. J Neurosci 40:9372–9385 (2020). https://doi.org/10.1523/JNEUROSCI.1922-20.2020
[37] Asadollahi R et al. Pathogenic UNC13A variants cause a neurodevelopmental syndrome by impairing synaptic function. Nat Genet 57:2691–2704 (2025). https://doi.org/10.1038/s41588-025-02361-5
[38] Rigo F et al. Antisense-based therapy for the treatment of spinal muscular atrophy. J Cell Biol 199:21–25 (2012). https://doi.org/10.1083/jcb.201207087
[39] Finkel RS et al. Nusinersen versus sham control in infantile-onset spinal muscular atrophy. NEJM 377:1723–1732 (2017). https://doi.org/10.1056/NEJMoa1702752
[40] Miller TM et al. Trial of antisense oligonucleotide tofersen for SOD1 ALS. NEJM 387:1099–1110 (2022). https://doi.org/10.1056/NEJMoa2204705
[41] Korobeynikov VA et al. Antisense oligonucleotide silencing of FUS expression as a therapeutic approach in ALS. Nat Med 28:104–116 (2022). https://doi.org/10.1038/s41591-021-01615-z
[42] Devlin AC et al. Human iPSC-derived motoneurons harbouring TARDBP or C9ORF72 ALS mutations are dysfunctional despite maintaining viability. Nat Commun 6:5999 (2015). https://doi.org/10.1038/ncomms6999
[43] Liu EY et al. Loss of nuclear TDP-43 is associated with decondensation of LINE retrotransposons. Cell Rep 27:1409–1421 (2019). https://doi.org/10.1016/j.celrep.2019.04.003
[44] Joseph BJ et al. TDP-43-dependent mis-splicing of KCNQ2 triggers intrinsic neuronal hyperexcitability in ALS/FTD. Nat Neurosci 28:2476–2492 (2025). https://doi.org/10.1038/s41593-025-02096-w
[45] Bryce-Smith S et al. TDP-43 loss induces cryptic polyadenylation in ALS/FTD. Nat Neurosci 28:2190–2200 (2025). https://doi.org/10.1038/s41593-025-02050-w
[46] Zeng Y et al. TDP-43 nuclear loss in FTD/ALS causes widespread alternative polyadenylation changes. Nat Neurosci 28:2180–2189 (2025). https://doi.org/10.1038/s41593-025-02049-3
[47] Guo C et al. Cryptic splicing in synaptic and membrane excitability genes links TDP-43 loss to neuronal dysfunction. Sci Transl Med 18:eaeb8517 (2026). https://doi.org/10.1126/scitranslmed.aeb8517
[48] Peethambaran Mallika A et al. Restoring multiple TDP-43 cryptic targets, but not solely Unc13a, rescues motor neuron disease. bioRxiv (2026-09-18). https://doi.org/10.64898/2026.09.11.751082
[49] Cao T et al. Prevention of Unc13a cryptic splicing is sufficient to preserve memory. bioRxiv (2026-09-15). https://doi.org/10.64898/2026.09.11.751031
[50] Gautier O et al. An emergent disease-associated motor neuron state precedes cell death in ALS. Cell 189:5044–5064 (2026). https://doi.org/10.1016/j.cell.2026.05.047
[51] Seddighi S et al. Mis-spliced transcripts generate de novo proteins in TDP-43-related ALS/FTD. Sci Transl Med 16:eadg7162 (2024). https://doi.org/10.1126/scitranslmed.adg7162
[52] Wilkins OG et al. Creation of de novo cryptic splicing for ALS and FTD precision medicine. Science 386:61–69 (2024). https://doi.org/10.1126/science.adk2539
[53] Scialò C et al. Seeded aggregation of TDP-43 induces its loss of function and reveals early pathological signatures. Neuron 113:1614–1628 (2025). https://doi.org/10.1016/j.neuron.2025.03.008
[54] Mehta PR et al. U7 small nuclear RNA splice-switching therapeutics for STMN2 and UNC13A in Amyotrophic Lateral Sclerosis. bioRxiv (2025-11-30). https://doi.org/10.1101/2025.11.26.690143
[55] Gomberg TA et al. Dual-targeting snRNA gene therapy rescues STMN2 and UNC13A splicing in TDP-43 proteinopathies. bioRxiv (2025-12-03). https://doi.org/10.64898/2025.12.01.691001
[56] Koike Y et al. TDP-43 and other hnRNPs regulate cryptic exon inclusion of a key ALS/FTD risk gene, UNC13A. PLoS Biol 21:e3002028 (2023). https://doi.org/10.1371/journal.pbio.3002028
[57] Agra Almeida Quadros AR et al. Cryptic splicing of stathmin-2 and UNC13A mRNAs is a pathological hallmark of TDP-43-associated Alzheimer's disease. Acta Neuropathol 147:9 (2024). https://doi.org/10.1007/s00401-023-02655-0
[58] Reeves MM et al. The UNC13A cryptic exon associates with cognitive impairment in Alzheimer's disease. Alzheimers Res Ther 18:187 (2026). https://doi.org/10.1186/s13195-026-02157-7
[59] Watanabe Y et al. ALS-associated RNA-binding proteins promote UNC13A transcription through REST downregulation. EMBO J 44:4745–4771 (2025). https://doi.org/10.1038/s44318-025-00506-0
[60] Zbinden A et al. Monomeric TDP-43 binds GU-rich RNA via its NTD but only its oligomers block cryptic exon inclusion. bioRxiv (2026-10-05). https://doi.org/10.64898/2026.10.01.755875
[61] El-Agamy SE, Mattedi F, Fratta P. Cryptic splicing in ALS: from driving disease progression to unlocking novel therapeutics. Annu Rev Genomics Hum Genet 27:277–303 (2026). https://doi.org/10.1146/annurev-genom-022024-011307
[62] Lin KH et al. Number and relative abundance of synaptic vesicles in functionally distinct priming states determine synaptic strength and short-term plasticity. J Physiol 603:6135–6160 (2025). https://doi.org/10.1113/JP286282
[63] Jusyte M et al. Unc13A dynamically stabilizes vesicle priming at synaptic release sites for short-term facilitation and homeostatic potentiation. Cell Rep 42:112541 (2023). https://doi.org/10.1016/j.celrep.2023.112541
[64] Dattilo D et al. TDP-43 dysfunction induces cryptic circular RNAs in ALS/FTD. bioRxiv (2026-09-20). https://doi.org/10.64898/2026.09.17.752342
[65] Brown A et al. Sensitivity to TDP-43 loss and degradation resistance determine cryptic exon biomarker potential. bioRxiv (2025-11-23). https://doi.org/10.1101/2025.11.23.689722
[66] Menon P et al. Cortical hyperexcitability evolves with disease progression in ALS. Ann Clin Transl Neurol 7:733–741 (2020). https://doi.org/10.1002/acn3.51039
[67] Dos Santos AB et al. Microcircuit failure in STXBP1 encephalopathy leads to hyperexcitability. Cell Rep Med 4:101308 (2023). https://doi.org/10.1016/j.xcrm.2023.101308
[68] Engel AG et al. Loss of MUNC13-1 function causes microcephaly, cortical hyperexcitability, and fatal myasthenia. Neurol Genet 2:e105 (2016). https://doi.org/10.1212/NXG.0000000000000105
[69] Tovell H et al. Rapid and reversible knockdown of endogenously tagged endosomal proteins via an optimized HaloPROTAC degrader. ACS Chem Biol 14:882–892 (2019). https://doi.org/10.1021/acschembio.8b01016
[70] Aggarwal A et al. Glutamate indicators with improved activation kinetics and localization for imaging synaptic transmission. Nat Methods 20:925–934 (2023). https://doi.org/10.1038/s41592-023-01863-6
[71] Meijer M et al. A single-cell model for synaptic transmission and plasticity in human iPSC-derived neurons. Cell Rep 27:2199–2211 (2019). https://doi.org/10.1016/j.celrep.2019.04.058
[72] Bekkers JM, Stevens CF. Excitatory and inhibitory autaptic currents in isolated hippocampal neurons maintained in cell culture. PNAS 88:7834–7838 (1991). https://doi.org/10.1073/pnas.88.17.7834
[73] FUNCtion ALS: Aiming to Restore UNC13A Function in People Living With ALS（TRCN-1023 Phase 1/2）. ClinicalTrials.gov NCT07674667. https://clinicaltrials.gov/study/NCT07674667
[74] 本文代码仓库：https://github.com/jburrone/Keuss-Harley-Ryadnov-Jackson-et-al.-Nature-2026 ; https://github.com/f-hamidlab/iGluSNFR3 (publication_branch) ; https://github.com/Delayed-Gitification/QIAxcelR ; https://github.com/peteharley95/Log1pGaussianLMM

---

## 诚实收尾：检索边界与未核实项

本背景解读基于 2026-11-14 前的公开来源（EuropePMC/ORCID/ClinicalTrials.gov/官方与公司页）与本文 PDF。**已核证：** 本文在线日期（2026-11-11, PMID 43015463）、作者串/等贡献脚注/通讯四人、Fratta 机构级履历（MD 米兰/PhD UCL/2015 建组，Trace 页）、Burrone/Lipstein/Harley/Keuss 机构级训练（ORCID）、Trace TRCN-1023 与 NCT07674667 Phase 1/2（n≈30，2026-08-20）、约 40 篇关键文献完整摘要、本文 funding/COI/专利号。

**未核实项（如实标注，不编造）：**
- **导师姓名一律未补填：** Fratta 博士导师、Keuss 博士导师/学位机构（ORCID 未声明，Dundee/Glasgow 学位论文库 403 未核到）、Burrone/Lipstein 导师均未在可读取来源声明；仅以 ORCID 机构记录+发表记录旁证（标注推断）。
- **UCL profiles（JS 应用）与 FMP Lipstein 组页（404）未能读取；** Fratta 顶级奖项未核到记录，不写。
- **Brown 2022 的 2024 Author Correction 更正内容未核到全文。**
- **本文化合物（M21-4/M18-17）与 TRCN-1023 的对应关系未在本文声明，属同管线推断。**
- **"纯合生存缩短 5–12 个月""第二强 GWAS 信号""30% 阈值"具体数值是本文对 refs 的概括，** 未在本次摘要级来源独立核到原始数字；Zarebidaki/Asadollahi 的剂量-反应曲线与变异分层需全文裁决。
- **所有外部文献 Figure 编号未核（标"编号待核"）；** 预印本（[2,48,49,54,55,60,64,65]）未经同行评审，结论强度低于正式发表；本文与预印本标题/内容差异未逐句对勘。
- **周报卡片"患者来源神经元"句已更正**（本文无患者神经元、体内仅分子药效）。

**核心未裁决张力（再次强调）：** 单 UNC13A 靶点能否独自支撑在体脊髓疾病修饰——本文体外人皮层单点 rescue [1] 与 Wong 圈脊髓在体"单靶不够/多靶够" [48]、Gitler 圈联合 ASO 几乎全 rescue [47] 并存，条件（物种/细胞类型/读出/缺失模式）不同，**未裁决**；这是后续实验与临床设计最该闭合的缺口。