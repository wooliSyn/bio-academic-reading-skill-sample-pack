# 把"凝胶"重新液化：活细胞核孔 FG 屏障的物理态之争，与一条被糖基化和 importin 守护的类液态网络

> 配套深度背景解读（Pillar A 背景简报 + Pillar B 问题精研）。同源《Glycosylation and importins liquefy the FG barrier in live nuclear pores_文献解读.md》负责 PDF 内逐图四字段精读；本文件只补 PDF 之外的作者谱系、研究传承、创新定位与跨文献问题精研，两者交叉引用、不重复逐图。凡涉及"本文做了什么"的陈述均锚定 PDF（fulltext.txt）并与同源文献解读一致；凡涉及"领域/作者/前作"的陈述均带外部来源编号 [n]，文末统一列 References。

---

## 0. 范围、方法与证据分类

**检索截止日：2026-11-14。** 核证通道：EuropePMC REST（resultType=core，批量脚本一次查询约 120 条，存 JSON 后定向读取；在线发表日期一律以 `firstPublicationDate` 为准）、ORCID 公共 API（作者教育/任职记录）、RCSB PDB（结构条目逐条核对）、机构官方页（MPI Biophysics、IMB Mainz、USTC 教师主页、武汉大学泰康中心、JGU 新闻稿）。作者谱系严格区分导师关系/技术传承/同领域团队/本次合作；凡官方记录未载明导师姓名者，一律留空白并注明"未核实"，不由共同署名推断师承。结构主张区分"实验解析结构"与"粗粒化/近原子模型"；富集≠化学计量；药理学抑制≠基因敲除；过表达≠生理水平。

**纳入关键外部文献约 90 篇**（含史前概念层、模型分歧各派、方法源流、同组最新后续），另含官方页/数据库记录约 15 条。本文件是聚焦叙述性检索而非系统综述，未做效应量合并。

**四类陈述分类（不混用"证明"）：**
- **(i) 实验直接观察**：活细胞 TRFA 测得 NUP98 FG 结构域 ρslow ≈ 57–108 ns 且 2 h 稳定；体外 FG 凝聚体 1 h 内液-固转变伴 ThT 增强；importin-β 剂量依赖加速链段运动；OSMI-4 减慢链段运动与核输入；Thiamet-G 几乎无额外效应；importin-β 过表达部分回补；双色 DNA-PAINT MINFLUX 在固定细胞测得 importin-β 径向密度峰约 20 nm（n=460 NPCs）；质谱确认体外糖基化约 17 个 GlcNAc/链。
- **(ii) 由缺失/回补支持的功能机制**：OSMI-4 全局降低 O-GlcNAc → 动力学与运输同时变慢，importin-β 过表达部分回补二者 → 支持"O-GlcNAc 与 importin-β 共同维持类液态"的功能机制，但药理学全局扰动不是 NUP98 位点特异敲除，回补是"部分"而非"完全"，故为支持性而非唯一因果证明。
- **(iii) 作者提出的解释模型**：径向组织（importin-β 偏环周、伸展 FG 占中央）由残基级粗粒化 MD 与 Martini 2.2 近原子模型给出，并被 MINFLUX 与 Sau 2025 轨迹间接支持；importin-β 稀释 85–124 易聚集段、O-GlcNAc 削弱有效 FG–FG 吸引（α 重标度）、体系近临界点、PTM 差异驱动去混合——均为模型推断；"双路径组织"（小/中 cargo 走环周、大/慢 cargo 走中央）在 Discussion 中明确写为"one possible framework"，是假说。
- **(iv) 尚待验证的转化设想**：Discussion 把框架外推到癌症（NUP98 融合）、病毒感染（HIV 衣壳）、神经退行（tau/C9orf72），本文未在这些疾病模型中检验，属设想。

**逐文献阅读深度声明**：每篇外部文献在 §索引表中标注"全文定向核读 / 完整摘要 / 仅书目"。本文件对外部文献的实际阅读以 EuropePMC core 完整摘要为主，部分辅以 PMC 图注核证（图号已核实者注明）；**摘要级来源不承载超出其摘要的实验细节，仅书目来源不补写未读到的实验细节**。唯一全文定向核读的是目标 PDF 本身。外部文献图未嵌入正文：PMC/Springer 图床下载通道受阻（403/404），故改为在"阅读顺序"与"索引表"中给出已核实的图号供读者按图索骥，不重做本文图。

---

# Pillar A：背景简报

## A.1 一瞥（The paper at a glance）

**完整题录**：Yu M (于淼), Heidari M, Palacio-Rodriguez K, Ruan H (阮浩), Mingu S, Chen Y (陈宇), Gou X-Z (缑绪卓), Shen P (沈平恺), Liu S (刘松子), Chen S-Y (陈思宇), Hidayat AA, Bode M, Sikora M, Tang A-H (唐爱辉), Hummer G ✉ & Lemke EA ✉. *Glycosylation and importins liquefy the FG barrier in live nuclear pores.* Nature (2026). DOI 10.1038/s41586-026-11258-0；PMID 43015467 [15]。

**出版状态（经核证，非占位符）**：PDF 首页 "Published online: xx xx xxxx" 是清样占位符，不具权威性。经 EuropePMC core 核证 `firstPublicationDate = 2026-11-11`，即 2026 年 11 月 11 日在线发表（brand new，尚无卷期页码）；Received 6 March 2025，Accepted 6 October 2026。Open Access，CC BY 4.0 [15]。

**预印本历史**：bioRxiv 2025-12-11 首次上传，题为 *O-GlcNAcylation and an importin-β radial gradient keep the FG barrier liquid in live-cell nuclear pores*，DOI 10.64898/2025.12.09.693204 [16]。值得注意的版本差异：预印本作者串为 Yu, Heidari, Palacio-Rodriguez, Ruan, Mingu, Hidayat, Bode, Sikora, Hummer, Lemke——**不含 Tang 与武汉大学团队（Chen Y、Shen P、Liu S、Gou X-Z、Chen S-Y）**；正式版新增唐爱辉组的 MINFLUX 成像与武大团队，标题亦改为现名。这意味着"活细胞 TRFA + 体外重构 + MD"是预印本已就的核心，而"固定细胞双色 MINFLUX 径向组织验证"是评审阶段补入的关键实验。直接前作 Yu 2023 亦有预印本（bioRxiv 2022-07-08，*Deciphering the conformations and dynamics of FG-nucleoporins in situ*，DOI 10.1101/2022.07.07.499201）[18]。

**公共数据**：MD 初始构型与轨迹开放于 Zenodo——LAMMPS 库 10.5281/zenodo.15025565 [122]、GROMACS 库 10.5281/zenodo.17588507 [123]（CC BY 4.0）；O-GlcNAc 位点注释取自 O-GlcNAc Database v2.0 [79]；模拟所用结构取自 PDB 7R5K（人 NPC 收缩态支架，冷冻电镜）[34] 与 3W5K（Snail1–importin-β 复合物晶体，X 射线，2.5 Å；本文移除 Snail1 配体后把 importin-β 作刚体）[35][33]。**注意：7R5K 是实验解析的支架结构，但本文的 FG-NUP 构象与 importin-β 分布是粗粒化/近原子模拟产物，不是解析结构**（详见 A.5 与 B.5）。

**通讯作者**：PDF ✉ 标记与 "Correspondence and requests for materials should be addressed to Gerhard Hummer or Edward A. Lemke" 一致——**通讯作者仅 Hummer 与 Lemke 两人**。唐爱辉（Tang A-H）是资深作者（16 人中第 14 位），作者贡献声明为 "contributed MINFLUX expertise and resources"，**并非通讯作者**；任务清单中"通讯/资深作者 Tang"应理解为"资深作者"，此处按 PDF 原文厘清。

## A.2 作者谱系（The authors）

### Gerhard Hummer —— 把统计力学装进分子模拟的理论生物物理学家

官方 CV（MPI Biophysics 部门页）逐字载明 [1]：1990 年维也纳大学物理 Mag. rer. nat.；1992 年维也纳大学物理 Dr. rer. nat.（博士）；1993–1996 洛斯阿拉莫斯国家实验室（LANL）博士后；1996–1999 LANL Technical Staff Member (PI)/Team Leader；1999–2013 NIH/NIDDK 化学物理实验室 Investigator→Senior Investigator→Section Chief→Deputy Laboratory Chief；2013 年起 MPI Biophysics 理论生物物理部主任（Director）；2016 年起法兰克福歌德大学物理系生物物理教授；2015 年起 FIAS Senior Fellow；2018–2019 MPI Biophysics 执行主任。**CV 未列出博士/博士后导师姓名，故本文不填导师**（不据传闻补写）。在 NIH 期间与 Attila Szabo 长期合作（非师承，二人同为化学物理实验室研究者），合著如 Hummer & Szabo 2017 *Dynamics of the Orientational Factor in Fluorescence Resonance Energy Transfer* [120]——这条"荧光取向因子动力学"的理论线正是本文 TRFA 各向异性分析的方法学远源。2023 年入选 Clarivate Web of Science 高被引研究者（MPI 官方新闻，2023-11-21，正文记为 cross-field 类别）[3]。

Hummer 组的研究主线是"用匹配实验的粗粒化模型把 IDP/膜/运输机器的介观行为算出来"：FUS 凝聚体的 Martini 重平衡策略（Benayad 2021，本文 ref 70）[29]、Martini 蛋白–糖相互作用按渗透第二维里系数精修（Heidari 2024，本文 ref 83）[30]、人 NPC 支架的 AI 辅助整合结构（Mosalaganti 2022 Science，Hummer 为共同作者，7R5K 即出于此）[28]。本文的"实验匹配 ε̃ + 多尺度模拟"骨架正是这条线的第 N 步。组内现任成员页确认 **Maziar Heidari 与 Karen Palacio Rodriguez 均为该部博士后**，Zakarya Benayad（[29] 一作）亦在组 [2]。

### Edward A. Lemke —— 用合成生物学给活细胞 IDP"点灯"的化学生物学家

IMB 官方传记页逐字载明 [4]：2001 年柏林工业大学化学 Diploma、2001 年俄克拉荷马大学化学 MSc；2005 年马普生物物理化学研究所/哥廷根大学化学博士；2005–2008 Scripps 研究所（La Jolla）Research Associate；2009–2017 EMBL Heidelberg 组长（2018 起 visiting）；2018 起 IMB 兼职主任（Adjunct Director）兼美因茨约翰内斯·古腾堡大学（JGU）合成生物物理教授。**官方页未列博士导师与博士后合作导师姓名**；博士后阶段在 Peter Schultz 组属发表记录旁证（Lemke 一作、Schultz 通讯的 Nat Chem Biol 2007 光笼氨基酸论文 [121]，与 2005–2008 Scripps 任职期吻合），本文标注为推断而非官方导师声明。现任状态经 JGU 2026-06-23 新闻稿核证：仍为 JGU 合成生物物理教授/IMB 兼职主任，并获第二个 ERC Advanced Grant "Molecular Shape Microscopy (MShapeM)"（约 300 万欧元，2026）；此前获 ERC Consolidator（2015）与 ERC Advanced（2019）[5]。本文基金所列 ERC-ADG "MultiOrganelleDesign" 即 2019 年那个 Advanced Grant（与新闻稿"2019 年第二个 Advanced"时间线一致）[5][15]。

Lemke 的标志性方向是"基因密码扩展 + 正交翻译细胞器 + 荧光探针"三位一体的活细胞 IDP 观测：正交翻译膜细胞器 GCE-OTO（Reinkemeier 2019 Science [20]、2021 Cell，本文 ref 27）[19]、近距淬灭荧光原染料 HDyes（Werther 2021 ACS Cent Sci，本文 ref 28，HD653 即出于此，武大/美因茨团队含 Yu M）[21]、IDP 节段运动分析（Milles & Lemke 2014 Angew，本文 ref 31）[22]、FG–NTR 超快结合的可塑性（Milles 2015 Cell，本文 ref 24）[23]。本文把这套"位点特异标记 + 时间分辨荧光"工具箱从 FRET（测构象）推进到 TRFA（测纳秒动力学），是同一工具弧线的自然延伸。

### Ai-Hui Tang（唐爱辉）—— 把 MINFLUX 带进中国、从突触纳米柱走向核孔的超分辨成像学家

USTC 教师主页与 ORCID 记录互证 [6][7]：北京大学生命科学学院学士（1998–2002）与博士（2002–2007，生物物理方向；主页本科结束年"2022"显系录入笔误，ORCID 记 2002-07 毕业，本文以 ORCID 为准）；2007-10–2010-06 马里兰大学医学院博士后；2010–2015 该校副研（Research Associate）；2015–2018 研究助理教授；2018-07 起 USTC 特任教授，2025-01 起生命科学与医学部教授；兼合肥综合性国家科学中心人工智能研究院研究员。**官方记录未列博士/博士后导师姓名，本文不填**。其 2016 年 Nature 跨突触纳米柱论文（Tang 一作、Blanpied 通讯）[39] 完成于马里兰任研究助理教授期间——Thomas Blanpied 是该论文通讯作者与同机构合作者，但官方记录未声明师承，本文不据共同署名认定导师关系。研究主线为单分子超分辨成像（MINFLUX）与成像型空间多组学及其神经科学应用；国家创新人才青年项目获得者 [6][14]。本文贡献为 MINFLUX  expertise 与资源（合肥人工智能研究院多模态成像中心），U-2 OS 细胞系由 Y. Li 提供（致谢）。**Tang 组截至检索日的 MINFLUX 后续以本文为标志**（EuropePMC 作者检索未见其他 2023–2026 MINFLUX 核孔论文，检索边界见诚实收尾）。

### Miao Yu（于淼）—— 从声学/微流控转向 IDP 活细胞成像的共同第一作者

武汉大学泰康中心官方页逐字载明 [8]：2007–2011 南京大学声学学士；2011–2015 香港科技大学生物工程博士；2015–2018 港理工/港科大博士后；2018-10–2023-11 美因茨大学（Lemke 组）博士后；2023-12 起武汉大学生命科学学院教授/博导、泰康生命医学中心 PI。**官方页未列导师姓名**；博士后阶段在 Lemke 组属发表记录旁证（代表作 Nature 2023 通讯作者为 Lemke，且本文作者贡献声明 "M.Y. designed the experimental study"）[8][15][17]。荣誉：2023 国家海外高层次人才计划、2023 湖北省海外高层次人才计划、2020 玛丽·居里学者（页面记为欧洲委员会/ERC 授予）、2020 美国生物物理学会优秀博士后奖、2019 洪堡学者（均按页面原文转述）[8]。发表记录横跨微流控（Lab Chip 2015、Small 2018）、凝聚态物理（PRL 2018、PNAS 2019 裂纹工程）与 IDP 相分离（Mol Cell 2019/2023 评论、Biophys J 2021），以及 FG-NUP 多功能性综述（Heinß 2020，Yu M 共同作者）[27]——这条"物理/工程→IDP 活细胞定量成像"的跨界轨迹解释了本文为何能把 TRFA 光子统计、bootstrap 拟合与微流控式体外重构揉在一起。本文基金中 M.Y. 名下的国家重点研发计划（2025YFA1309700）、NSFC（32471521）、中央高校基本科研业务费（2042025kf0029）与湖北省自然科学基金（2025AFA021）与其武大独立 PI 身份一致 [15]。

### Maziar Heidari —— 聚合物理论出身、专攻糖–蛋白模拟的共同第一作者

ORCID 记录 [9]：2008–2011 谢里夫理工大学硕士；2015–2019 马普聚合物研究所（Mainz）Polymer Theory 方向博士候选人；2019–2021 ESPCI Paris（记录未注角色）；2021-10 起 MPI Biophysics（Hummer 组，官方成员页确认为博士后）[2][9]。**官方记录未列博士导师姓名，本文不填**。其方法学贡献直接落在本文糖基化建模：Heidari–Sikora–Hummer 2024 精修 Martini 蛋白–糖相互作用（本文 ref 83）[30]，并参与 HIV 衣壳核孔进入的模拟（Kreysing 2025 Cell，Heidari 共同作者）[92]。本文作者贡献："M.H. and K.P.-R. performed the molecular-dynamics simulations"，且 M.H. 与 M.Y. 共同分析数据、合写初稿 [15]。

### 其他关键贡献者（按 PDF 作者贡献与单位）

- **Karen Palacio-Rodriguez**（MPI Biophysics 博士后，ORCID：安蒂奥基亚大学化学学士/硕士，索邦大学材料物理化学博士 2019–2022，2022-12 起 Hummer 组博士后）[10][2]：与 Heidari 共同执行 MD；近期工作转向膜/ESCRT（LEM2 核膜封闭、DFCP1 膜屏障等 2026 预印本）[10]。
- **Mateusz Sikora**（Dioscuri 中心主任）：MPI 官方 Dioscuri 页载明其轨迹——克拉科夫雅盖隆大学求学、华沙波兰科学院物理研究所博士、2012 IST Austria 博士后、2017 起 Hummer 组（FWF Erwin Schrödinger 奖学金）、2023-05 起在雅盖隆大学 Małopolska 生物技术中心建立"翻译后修饰建模 Dioscuri 中心"，德方伙伴即 Hummer [11]。本文糖基化 Martini 参数（λ=0.15、γ=0.5 匹配糖溶液渗透第二维里系数）正来自 Sikora–Hummer 合作线（Schmalhorst 2017 [31]、Heidari 2024 [30]）。**官方页未列其博士/博士后导师姓名，本文不填**。
- **Hao Ruan（阮浩）、Sara Mingu**（美因茨 Lemke 组）：参与实验；Ruan 也是 NUP98-HOXA9 癌蛋白凝聚体论文（Ruan 2025 Nat Commun）一作 [96]，Mingu 为 Yu 2023 共同作者 [17]。
- **Yu Chen（陈宇）、Pingkai Shen（沈平恺）、Songzi Liu（刘松子）**（武汉大学，单位 1）：参与实验（致谢武大生科院仪器共享平台 M. Li 提供光学成像支持）[15]。
- **Xu-Zhuo Gou（缑绪卓）、Si-Yu Chen（陈思宇）**（USTC，单位 4）：参与实验（MINFLUX）[15]。
- **Alam Ahmad Hidayat**（MPI + 雅盖隆，Dioscuri）：糖基化建模协助；**Mathis Bode**（于利希超算中心）：JUPITER 超算使用协助（JUREAP 早期访问计划）[15]。

**等贡献脚注逐字范围**：PDF 脚注 9 原文为 "These authors contributed equally: Miao Yu, Maziar Heidari."——**覆盖且仅覆盖第一、第二署名作者**，即等贡献范围为 Yu 与 Heidari 二人（通常所称共同第一作者），不扩展至任何其他署名作者。本文件与同源文献解读一致按脚注原文转述。作为对照，前作 Yu 2023 的等贡献脚注覆盖四人（"Miao Yu, Maziar Heidari, Sofya Mikhaleva, Piau Siong Tan"，经 PMC 全文 XML 核证）[17]——可见"等贡献范围"逐篇不同，不可跨篇套用。

**资助与"本文是谁的项目"**：E.A.L. 与 G.H. 共同构思（"E.A.L. and G.H. conceived the project"）；二人共同受 DFG CRC 1507"膜相关蛋白组装体"与 SCALE 资助（DFG 项目号 450648163、533751785）[15]。这是 Lemke（实验/标记）与 Hummer（模拟）长期合作弧线的直接产物，叠加 Lemke 的 ERC-ADG MultiOrganelleDesign 与 CRC1551"细胞功能中的聚合物概念"（464588647）、Hummer 组的马普学会支持、Sikora 的 Dioscuri（马普+波兰 NCN 联合）、Palacio-Rodriguez 的 Hessen Horizon MSCA、以及于利希 JUPITER 超算 [15]。

## A.3 研究谱系（The scientific lineage）

### 史前概念层：在"FG-NUP"这个词出现之前

核孔通透屏障的问题史前史可分三段，且各有体系边界：
- **形态学发现（1950s）**：Callan & Tomlin 1950 用电子显微镜研究两栖类卵母细胞核膜结构（Proc R Soc B 137:367–378）[97]；Afzelius 1955 在海胆卵母细胞核膜上描述环形孔/annuli（Exp Cell Res 8:147–158）[98]。这两篇确立了"核膜上有孔"的形态学事实，但**尚未涉及选择性通透的分子机制**（仅书目级，摘要未获取，本文不补写其实验细节）。
- **功能通透性（1960s）**：Feldherr 1965 把 PVP 包被的胶体金（25–170 Å）显微注射进变形虫（*Amoeba proteus*）胞质，检验核环孔电子致密物质对核质交换的调控（JCB 25:43–53）[99]——这是"核孔对大分子有筛分作用"的经典功能证据，体系是无脊椎动物/原生生物，不能直接倒推脊椎动物 FG-NUP 机制。
- **信号与体外重构（1980s–1994）**：Blobel 1980"细胞内蛋白质拓扑发生"（PNAS 77:1496–1500）确立信号假说框架 [100]；Dingwall & Laskey 1986 综述核输入 [101]；Newmeyer & Forbes 1988 在体外把核输入拆成"信号依赖的孔结合"与"ATP 依赖的转位"两步（Cell 52:641–653）[102]；Görlich 1994 从爪蟾卵纯化出核输入第一步必需的胞质蛋白 importin（Cell 79:767–778）[103]。**importin-β 作为"受体"的分子身份由此确立，但当时无人知道它后来会被证明还是屏障的'液化剂'与'伴侣'**——这正是本文的概念反转点。

### FG-NUP 的发现与"无序"定性（1992–2003）

Wente、Rout、Blobel 1992 鉴定酵母核孔蛋白新家族 NUP49/NUP100/NUP116，其 N 端含 GLFG 重复、间隔区富含 Gln/Asn/Ser/Thr（JCB 119:705–723）[104]——FG-NUP 的分子发现。Rout 2000 给出酵母 NPC 全组分清单与"布朗亲和门控"（Brownian affinity gating）模型（JCB 148:635–651，Chait 共同作者）[51]。Denning 2003 用生物物理+序列分析证明酵母 FG-NUP 是"天然无序"蛋白，且在纯化核内原位即无序（PNAS 100:2450–2455，Rexach 组）[53]；Denning & Rexach 2007 进一步以快速演化划定 FG 结构域边界（MCP 6:272–282）[54]；Patel & Rexach 2008 用 bead halo 法快速发现核孔新相互作用（MCP 7:121–131，在线 2007-09-26、卷期 2008，双年份）[55]。**这条 Rexach/Wente 遗传学+生物化学线确立了"FG 是无序、多价、可结合受体"的分子图像，但留下'无序链在孔内到底形成什么物理态'的缺口**。

> 任务清单中"Milburn/Wente"未能匹配到具体论文（疑为 Milles 或 Strawn 之误，未裁决）；Wente 谱系由 Wente 1992 [104]、Strawn 2004 [105]、Timney 2016 [60]（Wente 共同作者）覆盖。Strawn 2004 系统敲除酵母 11 个 FG-NUP 的 FG 结构域组合，发现超过一半 FG 质量可删除而不失屏障，且对称 FG 组合对 Kap104 输入必需——提示多条转位路径（Nat Cell Biol 6:197–206）[105]。这是"FG 冗余/多路径"的遗传学地基，与本文"双路径"假说遥相呼应。

### 模型分歧与问题转换（2003–2025）：领域经历了四次问题转换

**第一次转换：从"孔里有什么"到"屏障是什么物理态"。** 2003 年 Rout/Chait 提出"虚拟门"（virtual gating）：FG 链形成熵刷，受体结合降低熵垒而无需稳定结构（TCB 13:622–628）[52]。2006–2007 年 Görlich 组把问题推向"凝聚态"：Frey 2006 证明 FG 重复形成三维网架、具水凝胶性质（Science 314:815–817）[40]；Frey & Görlich 2007 证明单一 Nup98 FG 结构域的饱和水凝胶即可重现 NPC 通透性——importin-β 进入比同尺寸惰性分子快 >1000 倍，cargo  influx 加速 >20000 倍，凝胶内扩散约 12 ms 即可穿过 NPC（Cell 130:512–523）[41]。**同年（2007）Lim 组给出相反方向的纳米力学图像**：Kapβ1 使人 Nup153 FG 结构域塌缩成紧凑构象，RanGTP 使其回到聚合物刷状熵垒，爪蟾卵母细胞原位亦然（Science 318:640–643）[57]。2007 年这两篇不是"同一件事被重复发现"，而是回答了不同问题：Frey 问"体外 FG 能否形成选择性筛"（答：能，水凝胶），Lim 问"受体结合如何改变 FG 构象"（答：可逆塌缩/刷状）——前者指向 cohesive 凝聚体，后者指向受体调控的聚合物刷，解释空间当年并未闭合。

**第二次转换：从"均一无序网"到"序列编码的异质结构"。** Yamada 2010（Rexach 组）发现 FG 结构域并非均一无规线团，而是 collapsed coil（低电荷）与 extended coil（高电荷）两类沿链双峰分布（MCP 9:2205–2224）[56]。Ader 2010 用固态 NMR 在 Nsp1 水凝胶中鉴定出瞬态疏水接触与 Asn 富集间隔区的分子间 β-折叠（后者是凝胶内动力学最稳定结构，亦见于神经包涵体）（PNAS 107:6281–6285）[42]。Hülsmann 2012 在爪蟾卵提取物重构的 NPC 中证明 Nup98 的多价 FG 内聚（含靠近锚定点的 cohesive 重复）为屏障所必需，排除"仅靠 FG–NTR 相互作用"的模型（Cell 150:738–751）[43]。Labokha 2013 系统分析 10 个爪蟾 FG 结构域水凝胶，发现 Nup98 凝胶筛分最严（阻 GFP 尺寸惰性物、容 NTF2、把 importin-β 型 NTR 阻在表面），而 **O-GlcNAc 修饰 Nup98 可解除这种表面阻滞、容大 NTR·cargo 进入，且固态 NMR 显示糖基化凝胶缺乏未修饰凝胶中主导刚性区的淀粉样 β-结构**（EMBO J 32:204–218）[44]——这是本文"糖基化液化"最直接的前作地基。Schmidt & Görlich 2015 证明从哺乳类到 excavates 九类生物的 Nup98 FG 结构域都能从亚微摩尔溶液自发相分离成"FG 颗粒"，具 NPC 典型分选选择性（eLife 4:e04251）[45]。

**第三次转换：从"体外凝聚体"到"活细胞原位构象/动力学"。** 单分子与 NMR 线：Milles 2013 证明模拟 NPC 的拥挤条件可把 FG 聚集/淀粉样形成加速数个数量级，而 NTR 可抑制聚集，电镜显示水凝胶是被淀粉样纤维缠结的网络（EMBO Rep 14:178–183）[24]；Milles 2015 用单分子荧光+模拟+NMR 证明 FG–NTR 结合近扩散限制 on-rate、多价低亲和 motif 快速交换、结合态仍高度可塑（Cell 163:734–745）[23]；Hough 2015（Cowburn/Rout）用 NMR 证明 FG 是被细胞环境稳定的高动态 IDP，快速 on/off 支撑快速特异运输（eLife 4:e10027）[65]；Raveh 2016 用 Anton 全原子模拟提出 slide-and-exchange（PNAS 113:E2489–E2497）[66]。成像线：Sakiyama 2016 用高速 AFM（~100 ms）在爪蟾卵母细胞 NPC 上看到胞质口 FG 快速伸缩、中央通道瞬态缠结而非紧交联网（Nat Nanotechnol 11:719–723）[58]；Atkinson 2013 用偏振荧光发现 FG 结构域有取向有序、依赖 NPC 内位置而不依赖主动运输（Biophys J 104:37–50）[59]；Timney 2016 用数千次活细胞时间分辨测量证明被动扩散无硬性 30–60 kD 阈值，而是随质量渐增的"软屏障"（熵排斥）（JCB 215:57–76）[60]。**Yu 2023（本团队）是这条线的关键一步**：用 GCE-OTO 位点特异标记 + FLIM-FRET 在透化细胞原位测 NUP98 的 18 个链段距离分布，发现 NPC 内 FG 呈"良溶剂"膨胀构象（标度指数 ν=0.56±0.03，与体外凝聚体 ν=0.56±0.04 一致），并配粗粒化 MD（Nature 617:162–169；Fig 2 FLIM-FRET 管线、Fig 3 标度律、Fig 4 CG MD，图号经 PMC 图注核证）[17]。但 Yu 2023 测的是**构象（距离分布）**，不是**动力学（时间尺度）**，且主要在透化细胞——本文正是补上"活细胞 + 纳秒动力学"这一格。

**第四次转换：从"物理态标签"到"时间尺度分层 + 细胞上下文调控"。** 2022 年两篇 NMR/冷冻电镜把"凝聚体内部到底多有序"推到原子尺度，但回答的问题不同：Najbauer 2022（Görlich/Andreas）用工程化完美重复序列 + TRACT 证明 FG 重复在**相分离态与可溶态都保持纳秒级旋转相关时间、均无序**，尽管 FRAP 显示相分离态平移扩散慢，且呈 LCST 行为（Nat Commun 13:1494）[46]；Ibáñez de Opakua 2022（Zweckstetter）用 NMR+冷冻电镜鉴定 Nup98 FG 中瞬态 β-结构段与被 mRNA 输出因子识别的稳定预成 α-螺旋，并解析高聚集倾向段（85–124）形成的淀粉样纤维（Nup98FG85 多晶型 1–4），证明这些淀粉样聚集体**低稳定、可逆**（Nat Chem 14:1278–1285；Fig 2 ThT/负染 EM、Fig 3 纤维冷冻电镜、Fig 5 腔腔对比 α-syn 6XYO/Aβ 6SHS、Fig 6 低稳定性，图号经 PMC 图注核证）[47]。**这两篇与本文构成关键张力**（详见 B.1）：Najbauer 已证明凝聚态 FG 局部仍是纳秒动态，本文则证明体外凝聚体随时间（1 h）整体老化变固、而活细胞不老化——二者并不矛盾，而是把"局部链段运动"与"宏观材料态/平移扩散"分成不同时间尺度层级。2025 年 Kozai（Lim 组）用高速 AFM（ms）把屏障分成"快速涨落的环周区 + 高移动性中央塞"两区，并证明 DNA origami 纳米孔（NuPOD）+ Kap95 + 正确锚定 FG 可重现 NPC 行为、而体外 FG 水凝胶是静态的（Nat Cell Biol 27:2089–2101；Fig 1 两区、Fig 4 静态水凝胶、Fig 5 NuPOD+Kap95 重建中央塞，图号经 PMC 图注核证）[64]；同年 Sau（Musser 组）用 3D MINFLUX 在透化细胞同时追踪输入/输出，发现二者在中央孔重叠区进行，转位复合物偏好约 40–50 nm 直径环带、周向运动极小（Nature 640:821–827；Fig 1 NUP96 支架、Fig 2 双向追踪、Fig 4 环周径向密度，2678 轨迹/48603 定位，图号经 PMC 图注核证）[36]。本文的径向组织正是对 Sau 2025 环周偏好轨迹的机制解释，并以固定细胞双色 MINFLUX 直接成像 importin-β 加以支持。

### 产物命运/路径网络层：FG 凝聚体的"老化"去向与细胞的守护机制

本文的"产物"是 FG 凝聚体/聚集体，其后续命运构成一张竞争网络，阅读时须守住几条原则：
- **初始凝聚 ≠ 最终材料态**：体外新鲜 FG 凝聚体（前 5 min）类液，1 h 内老化成类固水凝胶并现淀粉样 ThT 信号（本文 Fig 1j、Fig 2c）；这条"液→固"轨迹与 Ader 2010 的 β-折叠 [42]、Milles 2013 的淀粉样纤维缠结 [24]、Ibáñez 2022 的可逆低稳定纤维 [47] 相连。**但"体外会老化"不等于"体内会老化"**——本文活细胞 2 h 稳定（Fig 1i），且 importin-β 与 O-GlcNAc 各自部分抑制老化、合用近乎重现活细胞动力学（Fig 4i）。
- **局部链段运动 ≠ 平移扩散 ≠ 宏观材料态**：Najbauer 2022 的纳秒旋转动态与慢 FRAP 平移共存 [46]；本文 ρslow 是"表观链段运动度量"而非精确旋转相关时间，且对 >荧光寿命（HD653 约 4 ns）的慢成分靠模型拟合外推（Methods）。**ρslow 变大（链段变慢）不自动等于"凝胶化"，须与 ThT/形态/平移扩散合看**。
- **抑制老化 ≠ 溶解已老化聚集体**：本文 Fig 2e 显示凝聚体成熟 1 h 后再加 importin-β 不能完全再液化——守护机制是"预防"而非"逆转"，这与 Ibáñez 2022 纤维"可逆"的结论形成条件依赖的张力（B.3 详述）。
- **生理守护 vs 病理失守**：NPC 支架是极长寿命蛋白（Savas 2012 大鼠脑 ELLP [85]；D'Angelo 2009 衰老相关 NPC 退化、核渗漏、氧化损伤 [84]），FG-NUP 又重度 O-GlcNAc 化 [77][79]。一旦守护失效，FG 的淀粉样倾向与疾病相连：C9orf72 G4C2 重复扩张通过 DPR 损害核质运输（Freibaum 2015 Nature，18 个 NPC/输出修饰因子）[86]；tau 直接结合 NUP、损害输入输出、Nup98 在缠结神经元胞体聚集并促 tau 聚集（Eftekharzadeh 2018 Neuron 99:925–940）[87]；NUP98-HOXA9 融合癌蛋白的 FG-IDR 相分离为白血病转化所必需（Ahn 2021 Nature 595:591–595）[88]。**本文把"糖基化+importin 维持类液态"提名为对抗这些病理老化的守护轴，但疾病模型检验属设想（第四类陈述）**。

### 同一年多篇的差异化（不可压缩为"重复发现"）

- **2007**：Frey & Görlich（水凝胶重现通透性）[41] vs Lim（受体诱导 FG 可逆塌缩/刷状）[57]——凝聚体 vs 聚合物刷，问题不同。
- **2022**：Najbauer（凝聚态 FG 局部纳秒动态、LCST）[46] vs Ibáñez（FG 淀粉样纤维原子结构、低稳定可逆）[47]——溶液/凝聚态动力学 vs 纤维结构，尺度不同。
- **2025**：Kozai（HS-AFM 两区 + 中央塞高移动 + NuPOD 重建）[64] vs Sau（3D MINFLUX 输入输出重叠 + 环带偏好）[36]——酵母/原位力学 vs 哺乳动物/活细胞轨迹，体系与读出不同。本文（2026）把二者整合进"径向组织 + 类液态守护"框架。

## A.4 新在哪（What's genuinely new）

1. **读出量的推进：从构象到活细胞纳秒动力学。** 相对 Yu 2023（FLIM-FRET 测距离分布、主要透化细胞）[17]，本文用位点特异 GCE-OTO 标记 + 皮秒 TRFA 在**活哺乳动物细胞**直接测 NUP98 FG 的表观链段运动（ρslow 57–108 ns，15 个位点，2 h 稳定），并给出沿链的空间梯度（近 N 端/孔中央更快、近锚定域更慢）。这是"活细胞原位 FG 动力学"的首次系统时间分辨测量（相对 Sakiyama 的 ~100 ms AFM [58]、Najbauer 的体外 NMR [46]，时间窗与体系都不同）。
2. **物理态争议的重新框定：体外老化是偏离，而非屏障本征态。** 本文证明体外 FG 凝聚体 1 h 液-固转变（ThT 阳性、85–124 段最显著），而活细胞不老化——把"FG 屏障是水凝胶/淀粉样"的体外图像重新定位为"失去细胞守护后的病理老化轨迹"，与 Görlich 水凝胶线 [40–45] 形成显式张力而非简单否定。
3. **两个守护因子的分子机制：importin-β 的"伴侣样稀释" + O-GlcNAc 的"削弱内聚"。** 相对 Jäkel 2002（importin 作为碱性蛋白胞质伴侣）[75]、Milles 2013（NTR 抑制拥挤诱导聚集）[24]、Lowe 2015（impβ·Nup153 Ran 调控网）[76]，本文在**链段尺度**证明 importin-β 剂量依赖加速 FG 运动、稀释 85–124 易聚集段、溶胀凝聚体（CG MD），并把 O-GlcNAc 从"运输调节"（Yoo 2021 [78]、Labokha 2013 [44]）推进到"纳秒动力学调节 + 抑制淀粉样老化"。
4. **最小体外体系重现活细胞动力学。** 糖基化 FG（约 17 GlcNAc/链）+ importin-β 合用，在 residue 221 给出 72±3 ns（体外）vs 59±14 ns（活细胞）的匹配——这是"细胞上下文可被两个因子最小重构"的定量证据，超出 Celetti 2020 微流控液滴（仅证明液态可重现通透性，未匹配纳秒动力学）[26]。
5. **径向组织：importin-β 偏环周、伸展 FG 占中央。** 实验匹配 ε̃FG–Imp-β=0.42 的 MD 自发产生径向分层，被固定细胞双色 MINFLUX（峰约 20 nm，n=460）与 Sau 2025 环带轨迹支持 [36]；并给出亲和力的" finely balanced"敏感性（+20% → importin-β 聚中央；−20% → 全孔离域）。这把 Kapinos 的 karyopherin-centric 占有模型 [61][62]、Kalita 的 Kap 加固屏障 [63] 推进到**空间分辨的径向组织**。
6. **多尺度模拟框架的方法学增量。** 残基级 CG（LAMMPS，ε̃ 匹配分配/FLIM-FRET）+ Martini 2.2 近原子（GROMACS，显式 O-GlcNAc，α/λ/γ 匹配 smFRET/渗透维里系数）双轨，且 Martini 糖参数来自 Heidari 2024 [30]/Schmalhorst 2017 [31] 的精修——把"糖基化 IDP 在纳米腔中的模拟"做成可复用框架（Discussion 明确外推到其他 IDP/凝聚体）。
7. **运输功能与动力学的偶联证据。** OSMI-4 同时减慢链段运动与 LINuS 核输入，importin-β 过表达部分回补二者——把"材料态"与"运输速率"在同一扰动下挂钩（相对 Yoo 2021 仅测运输 [78]）。

## A.5 须留意的局限（Caveats）

- **ρslow 是表观度量，不是精确旋转相关时间。** HD653 荧光寿命约 4 ns，慢成分靠双指数模型拟合外推；接近上拟合界 1000 ns 的值"未被定量分辨"（Methods 明示）。三指数模型评估后未改善拟合。因此"57–108 ns"是相对比较量，跨体系绝对值比较须谨慎。
- **标记与拟合扰动。** 单细胞拟合噪声大，靠 200 次 bootstrap 重采样求和光子计数再拟合；活细胞 n=41–69/位点、3 次独立实验；体外 n=3。bootstrap 深度经收敛分析（Supp Fig 2）。HD653 短连接子经 EGFP 验证（流体动力学半径与野生型一致，ED Fig 1c），但染料/连接子仍可能微扰局部运动；BOC 不可点击对照排除非特异信号。
- **药理学全局扰动 ≠ 位点特异遗传操作。** OSMI-4/Thiamet-G 改变全局 O-GlcNAc（RL2 blot 验证），不是 NUP98 特异位点敲除；观察到的运输减慢可能含其他 O-GlcNAc 底物的贡献。importin-β 过表达虽经 blot 示总 KPNB1 近内源水平（Supp Figs 19–20），但"过表达"与"生理化学计量"仍有差距；回补是部分的（residue 100）。
- **模型 ≠ 解析结构。** 7R5K 是实验支架结构 [34]，但 FG 构象/importin-β 分布/糖基化效应均为 CG 或 Martini 模拟产物；Martini 2.2 对 IDP 二级结构倾向与糖–蛋白相互作用有已知偏差（Robustelli 2018 证明所测力场无一同时准确描述折叠/无序蛋白 [111]；Schmalhorst 2017 [31]、Stark 2013 [32] 证明原始 Martini 高估蛋白–蛋白/糖聚集，需重标度）。本文用 α=0.78、λ=0.15、γ=0.5 匹配实验，但"近临界点"等结论依赖参数化。
- **固定细胞 2D MINFLUX ≠ 活细胞 3D 运输。** 本文 MINFLUX 在固定 U-2 OS 细胞、2D、以 NUP96 为支架参考（未直接分辨内环直径），不能排除 NPC 扩张/收缩对 apparent importin-β 分布的影响（Discussion 明示）；Sau 2025 是透化细胞 3D 追踪 NTR 结合 cargo（Impα），二者读出不同。NUP358 长远端胞质侧的高密度区未被模拟捕获。
- **体外浓度/条件映射。** 体外糖基化 FG 用 25 μM（WT 10 μM）以匹配凝聚体尺寸；残余 GdmCl 约 80 mM；糖基化仅约 17 GlcNAc/链（部分修饰）。这些与细胞内化学计量/拥挤的映射是推断。
- **疾病外推未检验。** 癌症/病毒/神经退行仅在 Discussion 提及，本文无疾病模型数据（第四类陈述）。
- **中央塞/双路径是假说。** "双路径组织"明确写为 one possible framework；本文数据不排除 importin-β 存在于中央塞样密度，只表明中央轴不是其主要位置。

## A.6 收束（In short）

本文是 **Lemke（活细胞 IDP 标记/荧光）与 Hummer（实验匹配多尺度模拟）合作弧线**把 Yu 2023"原位构象"推进到"活细胞纳秒动力学 + 材料态守护"的一步——主张**核孔 FG 屏障的本征态是被 importin-β 与 O-GlcNAc 共同守护的类液态网络，体外水凝胶/淀粉样老化是失去守护的偏离**，并以此解释 MINFLUX 环周偏好轨迹、把 karyopherin-centric 与选择性相/虚拟门模型收进一个"径向组织 + 时间尺度分层"的统一框架，为 FG-NUP 相关癌症、感染与神经退行提供"守护轴失守"的机制入口。

---

# Pillar B：面向读者的问题精研

## B.0 问题清单（先行）

从本文逻辑缺口提炼五个读者最可能追问的问题（无用户预设清单）：
- **Q1**：纳秒"类液态"就等于"液体屏障"吗？TRFA ρslow 与选择性相/虚拟门/刷/凝聚体各模型如何对应、何处冲突？
- **Q2**：importin-β 与 O-GlcNAc 究竟如何在分子层面"液化"？伴侣样稀释、竞争结合、糖的位阻/静电各占多少？MD 证据有多硬？
- **Q3**：体外液-固转变（老化）能映射到体内吗？细胞为何不老化？与 NPC 衰老、神经退行、NUP98 融合癌有何关系？
- **Q4**：径向组织（importin-β 偏环周、FG 占中央）如何与选择性、毫秒运输、中央塞共存？"双路径"假说有多可信？
- **Q5**：方法学边界——ρslow 到底测什么？标记/拟合/力场/固定细胞各引入多大不确定性？

## B.1 Q1：纳秒类液态 ≠ 宏观液体——把"物理态"拆成时间尺度层级

**分层拆解**：(a) 局部链段/侧链运动（ps–ns，TRFA/NMR 旋转相关）；(b) 链段间接触交换与平移扩散（μs–ms，FRAP/单分子追踪）；(c) 宏观材料态（液/凝胶/玻璃/淀粉样，流变/ThT/形态）；(d) 屏障功能（选择性+速度）。四个尺度不可互相替代。

**跨文献证据与逐环分级**：
- 局部纳秒动态在凝聚态中依然存在：Najbauer 2022 用 TRACT 证明工程化 FG 重复在相分离态与可溶态都有纳秒旋转相关时间、均无序，但 FRAP 平移慢，且 LCST [46]——**Strong（原子分辨 NMR，但体系是工程化完美重复序列，非天然异质 FG）**。本文活细胞 ρslow 57–108 ns 与之同量级，互相支持。
- 宏观老化确实发生（体外）：本文 Fig 1j/2c 的 ρslow 随 1 h 增大 + ThT 增强；Ader 2010 固态 NMR 的 β-折叠 [42]；Ibáñez 2022 的淀粉样纤维结构 [47]——**Strong（多手段一致），但限于体外**。
- 活细胞不老化：本文 Fig 1i 2 h 稳定；Yu 2023 原位良溶剂构象 ν=0.56 [17]；Sakiyama 2016 原位 FG 快速涨落、非紧交联 [58]；Hough 2015 NMR"被细胞环境稳定的高动态 IDP"[65]——**Moderate-to-strong（活细胞 TRFA 是直接证据，但时间窗 2 h 远短于 NPC 生理寿命；AFM/NMR 体系各异）**。
- 功能层：Frey 2007 水凝胶重现通透性（>1000× 选择性、~12 ms）[41]、Celetti 2020 液滴重现通透性 [26]、Timney 2016 软屏障 [60]——**Strong（功能重构），但"哪种物理态在体内承担功能"未由这些体外实验裁决**。

**建立/推断/未知三分**：
- 建立：活细胞 FG 有纳秒级表观链段运动且 2 h 稳定；体外凝聚体 1 h 老化；凝聚态 FG 局部仍可纳秒动态（Najbauer）。
- 推断：把"纳秒动态"等同于"液体屏障"是推断——液体/凝胶的宏观区分需平移扩散与流变，本文未测活细胞平移扩散或流变。
- 未知：活细胞 FG 的宏观材料态（是否近临界、是否有屈服应力）；μs–ms 尺度运动（本文建议用偏振 FCS [107] 补）；天然异质 FG 是否如工程化重复一样保持纳秒动态。

**最强单一实验 + 限度**：本文活细胞 15 位点 TRFA + 2 h 稳定性（Fig 1g,i）是"活细胞类液态"最有力证据；限度是 ρslow 为表观量、时间窗 2 h、未测平移扩散，不能排除"局部液、宏观凝胶"的共存（Najbauer 正是这种共存）。

**同组最新后续必查**：Lemke 组 Michels–Caria–Lemke 2026（Adv Sci）提出统一相分离与 β-折叠老化的含时多组分缔合聚合物热力学模型，把"老化增加黏性→驱动相分离"与"相分离→促老化"纳入同一第二定律框架 [95]——这正是对本文"液-固转变"的理论化后续；同组 Brzezinski 2025（Biomacromolecules，Yu M 共同作者）证明 PEG 拥挤加速 Nup98 成熟/β-折叠/凝胶化 [94]，提示本文体外老化速率受拥挤剂选择影响。Görlich 组 Ng 2023 证明缩短 inter-FG 间隔增强内聚/相密度/屏障 [48]，Fu 2024/2025 把 FG 相框架扩展到 HIV 衣壳"像 NTR 一样穿核孔" [49][50]——Görlich 线仍在"FG 相"框架内深化，而非接受"体内是纯液体"。

**跨文献张力（显式并列，未裁决）**：
- Najbauer 2022（凝聚态 FG 局部纳秒动态、无序）[46] vs 本文（体外凝聚体 1 h 老化变固）+ Ader 2010（β-折叠）[42]：前者测新鲜/平衡凝聚态的局部旋转，后者测随时间的老化与刚性结构——**相容分工：局部链段运动与宏观老化是不同尺度/时间窗；但"老化后局部是否仍纳秒动态"未被本文直接测（本文 ρslow 老化后接近上拟合界，提示局部也变慢）**。未裁决。
- Sakiyama 2016 / Kozai 2025（原位 FG 动态、非紧交联、中央塞高移动）[58][64] vs Frey 2007 / Hülsmann 2012（体外水凝胶/重构 NPC 需 FG 内聚）[41][43]：原位 vs 体外、是否含完整守护因子——本文以"importin+O-GlcNAc 守护"调和，但 Hülsmann 的"靠近锚定点的 cohesive 重复为屏障必需"提示内聚并非全被液化消除。未裁决。

**下一步**：活细胞偏振 FCS 测 μs–ms 旋转/平移 [107]；活细胞 FRAP/单分子追踪测 FG 平移扩散；对老化不同时间点同时测 TRFA（局部）+ FRAP（平移）+ ThT/流变（宏观），建立尺度耦合曲线。

## B.2 Q2：液化机制——伴侣样稀释 vs 竞争结合 vs 糖的位阻/静电

**分层拆解**：(a) importin-β 是"结合并稀释 FG–FG 接触"还是"竞争性占据 FG motif"？(b) O-GlcNAc 是削弱 FG–FG 吸引（热力学）还是增加链柔性（动力学）？(c) 二者是加和还是协同？(d) 位点/化学计量依赖？

**跨文献证据与逐环分级**：
- importin-β 的伴侣样角色有前作地基：Jäkel 2002 证明 importin 家族作为碱性蛋白（核糖体蛋白/组蛋白）的胞质伴侣 [75]；Milles 2013 证明 NTR 抑制拥挤诱导的 FG 聚集 [24]；Lowe 2015 证明 impβ（非 TRN1）以 Ran 依赖方式改变 NPC 通透性、与 Nup153 形成高阶复合物 [76]——**Moderate-to-strong（功能/结合证据，但非链段动力学）**。本文把效应推进到 ρslow 剂量依赖下降（1:1→4:1，120±24→80±7 ns）与 CG MD 的 85–124 段稀释（Fig 2d,g）——**Moderate（体外 TRFA 直接，但 MD 稀释是模型推断；活细胞仅 residue 100 部分回补）**。
- O-GlcNAc 削弱内聚/抑淀粉样：Labokha 2013 证明糖基化 Nup98 凝胶缺乏淀粉样 β-结构、解除 importin-β 表面阻滞 [44]；Yoo 2021 证明 O-GlcNAc 加速双向运输且富集于 FG 屏障 [78]；本文 OSMI-4 减慢动力学+运输、糖基化 FG 延迟老化、Martini 显式糖使链膨胀（fgly=0.3 最匹配 FLIM-FRET，预测 48 位点 vs 爪蟾实验 46 位点）——**Moderate-to-strong（体外+细胞+模拟一致，但 OSMI-4 全局扰动、Martini 糖参数依赖）**。
- 协同：本文糖基化+importin-β 合用近乎重现活细胞 ρslow 剖面（221 位 72±3 vs 59±14 ns）——**Moderate（最小体系匹配是强支持，但"协同"的分子非加和性未被单独量化）**。

**建立/推断/未知三分**：
- 建立：importin-β 剂量依赖加速体外 FG 链段运动、溶胀凝聚体；糖基化延迟体外老化；OSMI-4 减慢活细胞动力学与运输；二者合用匹配活细胞剖面。
- 推断：importin-β"稀释 85–124 易聚集段"是 CG MD 推断（ε̃FG–Imp-β=0.42 匹配分配实验，但稀释本身无直接结构实验）；O-GlcNAc"削弱有效 FG–FG 吸引"由 Martini α 重标度等效再现，是模型推断；"近临界点"依赖参数化。
- 未知：importin-β 与 FG 的结合化学计量/位点分辨结构（3W5K 是 Snail1–importin-β 晶体 [33][35]，不是 FG–importin-β 复合物结构）；O-GlcNAc 的位点特异效应（哪些 Ser/Thr 关键）；糖与 importin 是否竞争同一 motif。

**最强单一实验 + 限度**：糖基化+importin-β 最小体系重现活细胞 ρslow 剖面（Fig 4i）是最有力的"充分性"证据；限度是约 17 GlcNAc/链的部分修饰、25 μM FG/10 μM importin-β 的体外浓度、未分离单个糖位点贡献、未证明体内化学计量相同。

**同组最新后续必查**：Heidari–Sikora–Hummer 2024 精修 Martini 蛋白–糖相互作用（匹配渗透第二维里系数，发现糖主要作拥挤剂而非强结合）[30]——本文 λ=0.15、γ=0.5 即出于此，意味着模拟中糖–蛋白弱相互作用、糖主要通过削弱 FG–FG/拥挤起效，这与"糖直接竞争 FG motif"的替代解释形成张力。Sikora 的 Dioscuri 中心专攻 PTM 建模 [11]，是该线的持续后续。

**跨文献张力（未裁决）**：Labokha 2013（糖基化解除 importin-β 在 Nup98 凝胶表面的阻滞）[44] vs Kapinos 2014（Nup98 GLFG 形成部分可穿透 cohesive 层，与 FxFG 型 Nup214/62/153 不同）[61]：糖基化是否把 Nup98 从"cohesive 层"调向"可穿透"？本文支持糖削弱内聚，但 Nup98 与其他 FG-NUP 的差异化响应未被本文逐一分解。

**下一步**：位点特异 O-GlcNAc 掺入（基因密码扩展糖基化 Ser/Thr 或 OGT 靶向融合）+ TRFA + 运输，分离单位点贡献；FG–importin-β 复合物的 NMR/冷冻电镜（区分竞争 vs 稀释）；RanGTP 滴定检验 importin-β 效应的 Ran 依赖（呼应 Lowe 2015 [76]）。

## B.3 Q3：体外老化映射体内吗？守护轴与疾病

**分层拆解**：(a) 体外老化是否体内屏障的本征倾向？(b) 细胞靠什么防止老化（importin+O-GlcNAc 是否充分）？(c) 老化是否可逆？(d) 守护失守如何连接 NPC 衰老与疾病？

**跨文献证据与逐环分级**：
- 体外老化是真实倾向：本文 1 h 液-固 + ThT；Milles 2013 拥挤加速聚集数个数量级、水凝胶为淀粉样纤维缠结 [24]；Ader 2010 β-折叠 [42]；Ibáñez 2022 纤维结构 [47]——**Strong**。
- 体内不老化（本文时间窗内）：Fig 1i 2 h 稳定；NPC 支架极长寿命（Savas 2012 [85]、D'Angelo 2009 [84]）说明屏障须长期维持动态——**Moderate（2 h 远短于生理寿命；长寿命本身不证明 FG 不老化）**。
- 守护机制：importin+O-GlcNAc 各自部分抑老化、合用匹配活细胞（本文）；Labokha 2013 糖抑 β-结构 [44]；Milles 2013 NTR 抑聚集 [24]——**Moderate-to-strong（体外充分性支持，体内必要性靠 OSMI-4 部分回补，非完全遗传证明）**。
- 可逆性张力：本文 Fig 2e 成熟 1 h 后加 importin-β 不能完全再液化；Ibáñez 2022 纤维低稳定、可逆 [47]——**条件依赖，未裁决**（见下）。
- 疾病连接：D'Angelo 2009 衰老 NPC 退化/核渗漏/氧化损伤 [84]；Freibaum 2015 C9orf72 DPR 损害运输 [86]；Eftekharzadeh 2018 tau 结合 NUP、Nup98 促 tau 聚集 [87]；Ahn 2021 NUP98-HOXA9 LLPS 致白血病 [88]——**Moderate（疾病模型证据，但"守护轴失守→这些疾病"的因果链本文未检验）**。

**建立/推断/未知三分**：
- 建立：体外 FG 老化、活细胞（2 h）不老化、importin+O-GlcNAc 体外抑老化、OSMI-4 减慢活细胞动力学与运输。
- 推断：把体外老化视为"体内潜在病理轨迹"、把 importin+O-GlcNAc 视为"生理守护轴"是推断；疾病外推是设想。
- 未知：体内长时程（天–年）FG 是否老化；守护轴在衰老/疾病中是否定量失守；老化在体内是否可逆。

**最强单一实验 + 限度**：本文"活细胞 2 h 稳定 vs 体外 1 h 老化"的对照（Fig 1i vs 1j）是最有力的"细胞上下文守护"证据；限度是时间窗不对称（2 h vs 1 h）、体外无完整守护因子、未测体内长时程。

**同组最新后续必查**：Lemke 组 Ruan 2025（Nat Commun）证明 NUP98-HOXA9 癌蛋白 FG 结构域在单体/寡聚/凝聚态有不同构象紧致度，寡聚体呈 micelle 样、DNA 结合域暴露外周 [96]——把本文"FG 构象随组装态变化"延伸到癌蛋白；Michels 2026 热力学模型 [95] 提供老化的统一理论；Brzezinski 2025 拥挤加速老化 [94] 提示体外条件敏感性。Görlich 组 Fu 2024/2025 [49][50] 则把 FG 相作为 HIV 衣壳的"受体样"通道——疾病/感染方向的另一条活跃线。

**跨文献张力（显式并列，未裁决）**：本文 Fig 2e（成熟凝聚体不可被 importin-β 完全再液化）vs Ibáñez 2022（FG 淀粉样纤维低稳定、可逆）[47]：差异可能来自老化程度/纤维多晶型/是否含 RanGTP/糖基化状态——本文未加 RanGTP，Ibáñez 的"可逆"是热力学稳定性而非动力学溶解速率。**相容分工：早期老化可被守护因子预防/部分逆转，成熟淀粉样纤维动力学上难溶；但"体内是否存在不可逆老化阈值"未裁决**。

**下一步**：在神经元/衰老模型测 FG TRFA 动力学 + O-GlcNAc/importin 水平；NUP98-HOXA9 凝聚体在守护因子扰动下的动力学（连接 Ruan 2025 [96] + Ahn 2021 [88]）；tau/C9orf72 DPR 对 FG 老化的影响；长时程活细胞/类器官追踪。

## B.4 Q4：径向组织、选择性与中央塞——双路径假说有多可信？

**分层拆解**：(a) importin-β 为何偏环周（嫁接几何 vs 亲和力 vs 占有）？(b) 中央 FG 伸展如何维持选择性？(c) 毫秒运输与高亲和占有如何兼容？(d) 中央塞是货物还是结构？(e) 双路径是否成立？

**跨文献证据与逐环分级**：
- 径向组织：本文 CG MD（ε̃=0.42）自发产生 importin-β 环周富集 + 中央伸展 FG（Fig 3a,b），固定细胞双色 MINFLUX 峰约 20 nm、2D 随机零模型排除纯几何（Fig 3f,g，n=460）；Sau 2025 3D MINFLUX 转位复合物偏好 40–50 nm 环带 [36]——**Moderate-to-strong（模拟+固定细胞成像+独立透化细胞追踪三方一致；但固定 2D vs 活 3D、importin-β 本身 vs NTR-cargo 读出不同）**。
- 嫁接几何/局部 FG 密度驱动：本文 Discussion 归因于 FG-NUP 嫁接位置与近壁 FG 密度；Kapinos 2014/2017 的占有/动力学模型 [61][62]、Kalita 2022 Kap 加固屏障 [63]、Dekker 2025 的 GLFG 环 + 低移动 Kap 涂层 + 动态中央网 [70]——**Moderate（模型一致，但"几何驱动"的直接实验扰动未做）**。
- 毫秒运输与选择性兼容：本文平均首通时间 1–10 ms，匹配 Ribbeck 2001（~100 MDa/s、~10³ 事件/s）[80]、Kubitscheck 2005（NTF2/transportin 停留 5.8/7.1 ms）[81]、Lowe 2010 单 cargo 亚扩散 [82]、Frey 2007 ~12 ms [41]；Milles 2015 近扩散限制 on-rate [23]、Raveh 2016 slide-and-exchange [66]、Raveh 2025 整合布朗动力学 [67]、Cowburn 2023"受限浓缩体" [68]——**Strong（多体系动力学一致），但本文 1–10 ms 是模拟值，非直接单分子测量**。
- 中央塞：Akey 1993 冷冻电镜中央锥形柱 [117]、Beck 2004 冷冻电子断层中央塞/转运体体积位置可变、支持"在途货物" [116]、Kozai 2025 中央塞高移动 [64]——**Moderate（形态学+动态支持"货物/动态组装"而非刚性结构）**。本文数据不排除 importin-β 在中央塞样密度中，只表明中央轴非其主要位置。
- 双路径：本文 Discussion 明确为"one possible framework"；Strawn 2004 遗传学多路径 [105]、Lowe 2010 多亚步 [82] 旁证——**Coherent but retrospective（假说，未直接检验）**。

**建立/推断/未知三分**：
- 建立：固定细胞 importin-β 径向密度峰约 20 nm（n=460，零模型对照）；Sau 2025 环带偏好；模拟径向分层与亲和力敏感性（±20%）。
- 推断：径向组织由嫁接几何/局部密度驱动；双路径组织；中央密度部分为瞬态货物。
- 未知：活细胞运输态下的径向组织（固定可能锁定状态）；NPC 扩张/收缩对分布的影响；NUP358 远端胞质侧高密度区的来源。

**最强单一实验 + 限度**：本文双色 MINFLUX + 2D 随机零模型（Fig 3g）是"中央 importin-β  depleted 非几何假象"最有力证据；限度是固定细胞、2D、NUP96 参考未分辨内环直径、过表达 importin-β（虽近内源总量）。

**同组最新后续必查**：Hummer/Beck 组 Hoffmann 2025（Mol Cell）证明 NPC 扩张态调控通透性与压力依赖的"多孔流"（porous flow，区别于经典运输）[93]——直接关系本文"未排除 NPC 扩张/收缩影响"的 caveat；Kreysing 2025（Cell，Heidari 共同作者）证明 HIV 衣壳穿过 NPC 时使其"开裂"、衣壳晶格 largely 完整 [92]——大 cargo 对屏障的力学扰动。Lim 组 Feng 2024（Sci Adv）用可编程直径 DNA 纳米孔证明 60 nm 孔中 Nup62 成跨通道屏障、79 nm 孔中局部成簇，importin-β1 改变 Nup62 动态 [71]；de Vries 2026（Nat Commun）用 de novo 设计 FG-NUP 系统变化重复间距/电荷疏水比解析选择性 [72]——径向/几何调控的合成生物学后续。

**跨文献张力（未裁决）**：本文（importin-β 偏环周、中央 depleted）vs Akey 1993/Beck 2004 中央塞密度 [117][116]：若中央塞是货物/动态组装，则与"中央轴非 importin-β 主要位置"相容；若中央塞含稳定 importin-β 结构，则张力。Kozai 2025 中央塞高移动 [64] 支持前者。本文未直接分辨中央塞成分，未裁决。

**下一步**：活细胞 3D MINFLUX 追踪 importin-β（非固定 2D）+ NUP96 内环直径读出；渗透压扰动控制扩张态（呼应 Hoffmann 2025 [93]）；选择性改变 FG–importin-β 亲和力（本文预测 ±20% 移位）的直接实验；中央塞成分的单分子/冷冻电镜关联。

## B.5 Q5：方法学边界——ρslow 测什么、扰动多大

**分层拆解**：(a) TRFA 各向异性衰减的物理来源；(b) ρslow 的拟合可辨识性；(c) 标记/染料扰动；(d) 力场/粗粒化偏差；(e) 固定 vs 活细胞、2D vs 3D。

**跨文献证据与逐环分级**：
- TRFA 原理：各向异性 r(t) 由平行/垂直发射差定义，IDP 用双指数（快=染料/连接子局部运动，慢=链段运动）；Jain 2016 用皮秒时间分辨荧光去偏振在单 Trp α-synuclein 变体上直接映射骨架扭转运动（本文 ref 33 的方法源）[106]；Milles & Lemke 2014 把 FCS+时间分辨偏振用于 Nup153 节段运动（本文 ref 31）[22]——**Strong（方法学成熟）**。本文 ρslow 是"表观链段运动度量"，非精确旋转相关时间（Methods 明示）。
- 慢成分外推：HD653 寿命约 4 ns，>寿命的旋转成分靠模型拟合估计，精度随相关时间超出寿命而下降（本文引 Feinstein 2003、Wahl 1977，二者 EuropePMC 检索未获，仅书目）；Loman 2010 偏振 FCS 可测远长于寿命的旋转扩散（本文 ref 35，建议互补）[107]——**Moderate（外推有原理支撑，但绝对值不确定度大；上拟合界 1000 ns 的值未定量分辨）**。
- 染料验证：HD653 短连接子经 EGFP 流体动力学半径验证（ED Fig 1c）；Sindbert 2011 证明连接子长度/刚性显著影响 FRET 距离精度（本文 ref 29）[109]；Teijeiro-Gonzalez 2021 用 TRFA+MD 表征 GFP homo-FRET（本文 ref 66）[110]——**Moderate-to-strong（球状蛋白验证支持，但 IDP 局部环境不同）**。Werther 2021 HDyes 设计（近距四嗪淬灭、电子交换机制）[21]、Reinkemeier 2021 GCE-OTO [19] 是标记平台源流。
- 力场偏差：Robustelli 2018 证明所测六个力场无一同时准确描述折叠蛋白/无序蛋白尺寸/二级结构倾向 [111]；Stark 2013 [32]、Schmalhorst 2017 [31] 证明原始 Martini 高估蛋白–蛋白/糖聚集（渗透第二维里系数偏负数个量级），需重标度；Benayad 2021 重平衡 Martini 匹配 FUS 转移自由能 [29]；Heidari 2024 精修蛋白–糖 [30]；Monticelli 2008 [112]/Marrink 2007 [113] 是 Martini 蛋白/力场源——**Strong（偏差有定量基准），本文用 α/λ/γ 匹配实验缓解，但残余偏差未知**。
- 统计：200 bootstrap、双侧 bootstrap 检验、Welch t + Holm 校正（运输速率）；Schrimpf 2018 PAM 框架（本文 ref 62）[108] 是拟合工具源。活细胞 n=41–69/位点、3 次独立实验；体外 n=3——**Moderate（bootstrap 提升信噪，但单细胞拟合噪声大；n=3 体外重复偏少）**。
- 固定 vs 活：本文 MINFLUX 固定 2D；Sau 2025 透化 3D [36]；Balzarotti 2017 MINFLUX 原理（~1 nm 精度、光子需求降 22 倍）[37]；Chowdhury 2022 超分辨 3D 追踪 [38]——**固定可能锁定/改变分布，2D 投影丢失轴向信息**。

**建立/推断/未知三分**：
- 建立：TRFA 方法学成熟、HD653 经球状蛋白验证、bootstrap 统计流程、Martini 偏差有基准且经重标度。
- 推断：ρslow 绝对值跨体系可比；固定细胞径向分布代表活细胞；模拟糖基化效应定量准确。
- 未知：IDP 局部染料运动对 ρslow 的定量贡献；>寿命慢成分的真实分布；活细胞运输态径向组织。

**最强单一实验 + 限度**：EGFP-HD653/Cy3B 流体动力学半径对照（ED Fig 1c）是探针可靠性最有力证据；限度是球状蛋白 ≠ IDP 局部环境，不能排除染料在 FG 链上的异常局部运动。

**同组最新后续必查**：Heidari 2024 [30] 与 Benayad 2021 [29] 是本文力场参数的直接来源与持续精修线；Dekker 2026 预印本（Onck 组）提出 2BPA-HB 模型，结合显式方向性骨架氢键与残基特异侧链作用中心，在微秒尺度模拟无序/凝聚/淀粉样态转变并重现 Nup98 纤维多晶型 [73]——这是对本文"未模拟分子老化"缺口的直接方法学后续。

**跨文献张力（未裁决）**：本文 Martini"糖主要削弱 FG–FG/拥挤起效"（λ=0.15 弱蛋白–糖）[30] vs 糖可能直接竞争 FG motif 的替代解释——Heidari 2024 的弱蛋白–糖结论支持前者，但体内 O-GlcNAc 的位点特异效应未被本文分离。

**下一步**：偏振 FCS 补 μs–ms [107]；多染料/多连接子对照分离染料局部运动；全原子 IDP 力场（如 Robustelli 2018 修正型 [111]）交叉验证 Martini；活细胞 3D MINFLUX。

## B.6 Summary scorecard（机制链记分牌）

| 链中一环 | 关键证据 | 分级 |
| --- | --- | --- |
| 活细胞 FG 纳秒表观链段运动（ρslow 57–108 ns，2 h 稳定） | 本文 15 位点 TRFA + bootstrap（Fig 1g,i）；Najbauer 2022 凝聚态纳秒动态 [46] | Strong（直接测量；绝对值为表观量） |
| 体外 FG 凝聚体 1 h 液-固老化 | 本文 ρslow↑ + ThT（Fig 1j,2c）；Ader 2010 β-折叠 [42]；Ibáñez 2022 纤维 [47] | Strong（体外多手段） |
| 活细胞不老化（守护存在） | 本文 Fig 1i vs 1j；Yu 2023 原位良溶剂 [17]；Sakiyama 2016 [58] | Moderate-to-strong（时间窗 2 h 限制） |
| importin-β 加速链段运动/溶胀凝聚体 | 本文剂量依赖 TRFA（Fig 2d）；Jäkel 2002 [75]、Milles 2013 [24]、Lowe 2015 [76] | Moderate-to-strong（体外直接） |
| importin-β 稀释 85–124 易聚集段 | 本文 CG MD（Fig 2g），ε̃ 匹配分配 | Moderate（模型推断，无直接结构） |
| O-GlcNAc 削弱内聚/抑淀粉样老化 | 本文 OSMI-4/糖基化（Fig 4）；Labokha 2013 [44]；Yoo 2021 [78] | Moderate-to-strong（全局药理限制） |
| 糖+importin 合用重现活细胞剖面 | 本文 Fig 4i（221 位 72±3 vs 59±14 ns） | Moderate（最小体系充分性，浓度/化学计量推断） |
| O-GlcNAc 动力学↔运输偶联 | 本文 OSMI-4 减慢二者 + importin 部分回补（Fig 4c,e,f） | Moderate（部分回补，非完全因果） |
| 径向组织（importin 环周/FG 中央） | 本文 MD + 固定 2D MINFLUX（Fig 3，n=460，零模型）；Sau 2025 [36] | Moderate-to-strong（固定/2D/过表达限制） |
| 亲和力 finely balanced（±20% 移位） | 本文 MD 敏感性（Fig 3c，Supp Fig 5） | Moderate（纯模拟预测，未实验检验） |
| 毫秒运输与选择性兼容 | 本文模拟首通 1–10 ms；Ribbeck 2001 [80]、Kubitscheck 2005 [81]、Milles 2015 [23] | Strong（动力学一致；本文为模拟值） |
| 双路径组织/中央塞=瞬态货物 | 本文 Discussion 假说；Beck 2004 [116]、Kozai 2025 [64]、Strawn 2004 [105] | Coherent but retrospective（假说） |
| 守护轴失守→疾病 | D'Angelo 2009 [84]、Freibaum 2015 [86]、Eftekharzadeh 2018 [87]、Ahn 2021 [88] | 推断/设想（本文未检验） |

## B.7 最有价值的后续实验（Most valuable next experiments）

1. **NUP98 位点特异 O-GlcNAc 操控 + TRFA + 运输**：用基因密码扩展掺入糖基化 Ser/Thr 或 OGT 靶向融合，分离单位点贡献，把 OSMI-4 全局药理升级为位点特异因果，检验"哪些糖位点关键、是否充分"。
2. **活细胞 3D MINFLUX 追踪 importin-β + 内环直径读出 + 渗透压扰动**：在运输态而非固定态检验径向组织，控制 NPC 扩张/收缩（呼应 Hoffmann 2025 [93]），并直接检验本文 ±20% 亲和力移位预测（用 FG–importin 亲和力突变/小分子）。
3. **老化多尺度耦合曲线 + RanGTP 逆转实验**：对体外凝聚体不同老化时间同时测 TRFA（局部）+ FRAP（平移）+ ThT/流变（宏观），并加 RanGTP±importin-β 检验成熟聚集体能否溶解，裁决本文 Fig 2e 与 Ibáñez 2022 [47] 的可逆性张力。
4. **疾病模型中的守护轴检验**：在 NUP98-HOXA9 白血病模型（连接 Ruan 2025 [96] + Ahn 2021 [88]）与 tau/C9orf72 神经元模型中测 FG TRFA 动力学 + O-GlcNAc/importin 水平，检验"守护轴失守→病理老化"的因果链，把第四类设想升级为可检验机制。

---

## 建议阅读顺序（精确到 Fig，图号已核实者注明）

**第一轮·主干（以最少文献建立完整逻辑）**
1. Cowburn & Rout 2023 综述 [68]——读它为了拿到"虚拟门/选择性相/刷/凝聚体"模型分类与"受限浓缩体"共识框架（综述，无单一关键图）。
2. Frey & Görlich 2007 [41]——读它为了理解"水凝胶重现通透性"的原始定量（>1000× 选择性、~12 ms）；重点图编号待核（非 OA，图号未核实）。
3. Hülsmann 2012 [43]——读它为了理解"重构 NPC 中 FG 内聚为屏障必需"；重点图编号待核。
4. Yu 2023 [17]——重点看 **Fig 2**（FLIM-FRET 管线）、**Fig 3**（标度律 ν=0.56±0.03，良溶剂）、**Fig 4**（CG MD）：本文构象地基（图号经 PMC 图注核证）。
5. Najbauer 2022 [46] + Ibáñez 2022 [47] 并读——前者纳秒动态/FRAP 慢平移（图号待核），后者重点看 **Fig 2**（ThT/EM）、**Fig 3**（纤维冷冻电镜多晶型）、**Fig 6**（低稳定性）：理解"局部动态 vs 宏观老化"张力（图号经核证）。
6. 本文 + 同源《文献解读》——TRFA 活细胞动力学 + 守护因子 + 径向组织（本文 Fig 1–5 逐图见文献解读）。
7. Sau 2025 [36]——重点看 **Fig 1**（NUP96 支架）、**Fig 2**（双向追踪）、**Fig 4**（环周径向密度，2678 轨迹）：本文径向组织的独立轨迹支持（图号经核证）。
8. Kozai 2025 [64]——重点看 **Fig 1**（环周涨落区+中央塞两区）、**Fig 4**（静态水凝胶）、**Fig 5**（NuPOD+Kap95 重建中央塞）：原位力学与合成重构（图号经核证）。

**第二轮·按兴趣分支**
- 物理态/聚合物：Yamada 2010 [56]（双峰构象）、Lim 2007 [57]（受体诱导塌缩/刷）、Atkinson 2013 [59]（取向有序）、Timney 2016 [60]（软屏障）、Raveh 2016 [66]（slide-and-exchange）、Winogradoff 2022 [69]（percolation）、Dekker 2025 [70]（Kap-centric 氨基酸分辨）；图号多待核。
- O-GlcNAc：Labokha 2013 [44] 重点 **Fig 5/6/7**（Nup98 凝胶分析/WGA 阻滞/固态 NMR，图号经核证）、Yoo 2021 [78] 重点 **Fig 2/4/5**（O-GlcNAc 依赖运输/中央通道富集/通透性，图号经核证）、Li & Kohler 2014 [77]（综述）。
- importin-β：Jäkel 2002 [75]、Lowe 2015 [76]、Kalita 2022 [63]、Kapinos 2014/2017 [61][62]；图号待核。
- 方法：Jain 2016 [106]（骨架扭转）、Loman 2010 [107]（偏振 FCS）、Werther 2021 [21] 重点 **Fig 1/2**（探针设计/淬灭光物理，图号经核证）、Reinkemeier 2021 [19]（GCE-OTO）、Balzarotti 2017 [37]（MINFLUX）、Heidari 2024 [30]/Benayad 2021 [29]/Robustelli 2018 [111]（力场）。
- 疾病/衰老：D'Angelo 2009 [84]、Savas 2012 [85]、Freibaum 2015 [86]、Eftekharzadeh 2018 [87]、Ahn 2021 [88]、Ruan 2025 [96]；图号待核。
- 史前：Callan 1950 [97]、Afzelius 1955 [98]、Feldherr 1965 [99]、Wente 1992 [104]、Denning 2003 [53]、Rout 2000 [51]（仅书目/摘要级，按概念读）。

> 与同源《文献解读》文末"延伸文献与图引清单"互补：后者侧重本文哪图值得摘/讲，本清单侧重外部前作哪图建立逻辑。外部图未嵌入（图床下载受阻），图号供按图索骥；凡未核实图号一律标"编号待核"，不编造。

---

## 逐文献证据索引表（含阅读深度）

> 声明：正文定向核读不表示逐段审计全部补充材料；"完整摘要"行不承载超出完整摘要的实验细节；"仅书目"行不补写未读到的实验细节。图号经 PMC 图注核证者注明，否则"编号待核"。官方页/数据库记录单列。阅读深度针对外部文献的实际阅读（EuropePMC core 摘要为主）；目标 PDF 为唯一全文定向核读。

| 文献（在线/卷期年） | 模型与主要贡献 | 解释边界 | 阅读深度 |
| --- | --- | --- | --- |
| Yu 2023 Nature 617:162–169（2023-04-26）[17] | 活/透化细胞 FLIM-FRET 测 NUP98 18 链段，ν=0.56 良溶剂，CG MD | 测构象非动力学；主要透化细胞 | 完整摘要+图注核证 |
| Yu 2023 预印本 bioRxiv（2022-07-08）[18] | 同上预印本 | 版本差异 | 完整摘要 |
| 本文预印本 bioRxiv（2025-12-11）[16] | 核心 TRFA+体外+MD；无 Tang/武大团队 | 正式版新增 MINFLUX | 完整摘要 |
| Reinkemeier 2019 Science 363:eaaw2644 [20] | 设计膜less细胞器重指派密码子 | 平台源流 | 完整摘要 |
| Reinkemeier 2021 Cell 184:4886 [19] | GCE-OTO 双正交翻译膜细胞器 | 平台源流 | 完整摘要 |
| Werther 2021 ACS Cent Sci 7:1561 [21] | HDyes 近距淬灭荧光原染料（HD653） | 探针光物理 | 完整摘要+图注核证 |
| Milles & Lemke 2014 Angew 53:7364 [22] | FCS+时间分辨偏振测 Nup153 节段运动 | 方法源流 | 完整摘要 |
| Milles 2015 Cell 163:734 [23] | FG–NTR 近扩散限制 on-rate、结合态可塑 | 体外+单分子 | 完整摘要 |
| Milles 2013 EMBO Rep 14:178 [24] | 拥挤加速 FG 聚集、NTR 抑制、水凝胶=纤维缠结 | 体外 | 完整摘要 |
| Aramburu & Lemke 2017 Semin Cell Dev Biol 68:34 [25] | FG–NTR 相互作用机制综述 | 综述 | 完整摘要 |
| Celetti 2020 JCB 219:e201907157 [26] | 微流控 FG 液滴重现通透性 | 液态功能重构，未测纳秒动力学 | 完整摘要 |
| Heinß 2020 Biochem Soc Trans 48:2603 [27] | F-rich NUP 多功能性综述（Yu M 共同作者） | 综述 | 完整摘要 |
| Mosalaganti 2022 Science 376:eabm9506 [28] | AI 辅助人 NPC 整合结构（7R5K，收缩/扩张） | 支架实验结构；FG 为模型 | 完整摘要 |
| Benayad 2021 JCTC 17:525 [29] | Martini 重平衡匹配 FUS 转移自由能 | 力场参数化 | 完整摘要 |
| Heidari 2024 JCTC 20:10259 [30] | Martini 蛋白–糖按渗透维里系数精修（弱蛋白–糖） | 力场参数化 | 完整摘要 |
| Schmalhorst 2017 JCTC 13:5039 [31] | Martini 多糖高估聚集，需修正 | 力场偏差基准 | 完整摘要 |
| Stark 2013 JCTC 9:4176 [32] | Martini 蛋白–蛋白高估（B22 偏负） | 力场偏差基准 | 完整摘要 |
| Choi 2014 Acta Cryst D 70:1050 [33] | Snail1–importin-β 晶体 2.5 Å（3W5K） | 非 FG–importin 复合物 | 完整摘要 |
| Sau 2025 Nature 640:821（2025-03-19）[36] | 3D MINFLUX 输入输出重叠、40–50 nm 环带偏好 | 透化细胞、NTR-cargo | 完整摘要+图注核证 |
| Balzarotti 2017 Science 355:606 [37] | MINFLUX ~1 nm、光子需求降 22 倍 | 方法原理 | 完整摘要 |
| Chowdhury 2022 Nat Cell Biol 24:112 [38] | 超分辨 3D cargo 追踪 | 方法 | 完整摘要 |
| Tang 2016 Nature 536:210 [39] | 跨突触纳米柱（Tang 一作/Blanpied 通讯） | 作者谱系旁证 | 完整摘要 |
| Frey 2006 Science 314:815 [40] | FG 三维网架水凝胶 | 体外 | 完整摘要 |
| Frey & Görlich 2007 Cell 130:512 [41] | 饱和水凝胶重现通透性（>1000×、~12 ms） | 体外 | 完整摘要 |
| Ader 2010 PNAS 107:6281 [42] | 固态 NMR：FG 凝胶 β-折叠/瞬态疏水 | 体外 | 完整摘要 |
| Hülsmann 2012 Cell 150:738 [43] | 重构 NPC 需 Nup98 多价 FG 内聚 | 体外重构 | 完整摘要 |
| Labokha 2013 EMBO J 32:204（2012-11-30）[44] | 10 爪蟾 FG 凝胶；O-GlcNAc 抑 β-结构/解阻滞 | 体外；爪蟾 | 完整摘要+图注核证 |
| Schmidt & Görlich 2015 eLife 4:e04251 [45] | 九类生物 Nup98 FG 自发相分离、NPC 选择性 | 体外 | 完整摘要 |
| Najbauer 2022 Nat Commun 13:1494 [46] | 凝聚态 FG 纳秒旋转动态、FRAP 慢、LCST | 工程化重复序列 | 完整摘要 |
| Ibáñez de Opakua 2022 Nat Chem 14:1278 [47] | FG 瞬态 β/预成 α；85–124 纤维低稳定可逆 | 体外纤维 | 完整摘要+图注核证 |
| Ng 2023 Nat Commun 14:747 [48] | inter-FG 间隔缩短增强内聚/屏障 | 体外 | 完整摘要 |
| Fu 2024 Nature 626:843 [49] | HIV 衣壳像 NTR 进入 FG 相 | 体外+细胞 | 完整摘要 |
| Fu 2025 NSMB 32:2476 [50] | 衣壳表面氨基酸组成驱动 NTR 样行为 | 机制 | 完整摘要 |
| Rout 2000 JCB 148:635 [51] | 酵母 NPC 组分清单、布朗亲和门控 | 酵母 | 完整摘要 |
| Rout 2003 TCB 13:622 [52] | 虚拟门模型 | 模型 | 完整摘要 |
| Denning 2003 PNAS 100:2450 [53] | FG-NUP 天然无序、原位无序 | 酵母 | 完整摘要 |
| Denning & Rexach 2007 MCP 6:272 [54] | 快速演化划定 FG 结构域边界 | 酵母/演化 | 完整摘要 |
| Patel & Rexach 2008 MCP 7:121（2007-09-26）[55] | bead halo 法发现核孔相互作用 | 方法 | 完整摘要 |
| Yamada 2010 MCP 9:2205 [56] | FG 双峰 collapsed/extended coil | 体外构象 | 完整摘要 |
| Lim 2007 Science 318:640 [57] | Kapβ1 塌缩 Nup153 FG、RanGTP 回刷状 | 体外+爪蟾原位 | 完整摘要 |
| Sakiyama 2016 Nat Nanotechnol 11:719 [58] | HS-AFM ~100 ms FG 涨落、非紧交联 | 爪蟾卵母细胞 | 完整摘要 |
| Atkinson 2013 Biophys J 104:37 [59] | 偏振荧光 FG 取向有序、位置依赖 | 活细胞 | 完整摘要 |
| Timney 2016 JCB 215:57 [60] | 软屏障、无硬阈值、熵排斥 | 活细胞+BD | 完整摘要 |
| Kapinos 2014 Biophys J 106:1751 [61] | SPR：FxFG 容 Kap、Nup98 GLFG cohesive 层 | 体外 | 完整摘要 |
| Kapinos 2017 JCB 216:3609 [62] | Kap 调控屏障/运输 | 体外+细胞 | 完整摘要 |
| Kalita 2022 JCB 221:e202108107 [63] | Kapβ1+CRM1 加固屏障、CRM1 补偿 | 活细胞 | 完整摘要 |
| Kozai 2025 Nat Cell Biol 27:2089（2025-12-02）[64] | HS-AFM 两区+中央塞高移动；NuPOD 重建 | 酵母+合成 | 完整摘要+图注核证 |
| Hough 2015 eLife 4:e10027 [65] | NMR：FG 高动态、细胞环境稳定、快 on/off | NMR | 完整摘要 |
| Raveh 2016 PNAS 113:E2489 [66] | Anton 全原子 slide-and-exchange | 模拟+NMR | 完整摘要 |
| Raveh 2025 PNAS 122:e2507559122 [67] | 整合布朗动力学+细胞动力学模型 | 模型 | 完整摘要 |
| Cowburn & Rout 2023 Biochem Soc Trans 51:871 [68] | "受限浓缩体"共识综述 | 综述 | 完整摘要 |
| Winogradoff 2022 Nat Commun 13:5138 [69] | 瞬态空洞/percolation 尺寸阈值 | 模拟 | 完整摘要 |
| Dekker 2025 Nat Commun 16:11497（2025-12-12）[70] | 氨基酸分辨 Nsp1、GLFG 环+Kap 涂层+中央网 | 模拟 | 完整摘要 |
| Feng 2024 Sci Adv 10:eadq8773 [71] | DNA 纳米孔直径调控 Nup62 屏障 | 合成 | 完整摘要 |
| de Vries 2026 Nat Commun 17:11379（2026-09-28）[72] | de novo FG-NUP 间距/电荷疏水比→选择性 | 合成 | 完整摘要 |
| Dekker 2026 预印本（2026-04-08）[73] | 2BPA-HB 模拟无序/凝聚/淀粉样转变 | 模型预印本 | 完整摘要 |
| Baumann 2025 Nucleus 16:2510106 [74] | NPC 纳米组织/动态会议综述 | 综述 | 完整摘要 |
| Jäkel 2002 EMBO J 21:377 [75] | importin 作碱性蛋白胞质伴侣 | 体外/细胞 | 完整摘要 |
| Lowe 2015 eLife 4:e04052 [76] | impβ·Nup153 Ran 调控网、impβ 改通透性 | 体外+细胞 | 完整摘要 |
| Li & Kohler 2014 Traffic 15:347 [77] | 核孔 O-GlcNAc 综述 | 综述 | 完整摘要 |
| Yoo & Mitchison 2021 JCB 220:e202010141 [78] | O-GlcNAc 加速双向运输、富集 FG 屏障 | 活细胞 | 完整摘要+图注核证 |
| Wulff-Fuentes 2021 Sci Data 8:25 [79] | O-GlcNAcome 5000 蛋白/7002 位点数据库 | 数据库 | 完整摘要 |
| Ribbeck & Görlich 2001 EMBO J 20:1320 [80] | ~100 MDa/s、~10³ 事件/s、选择性相 | 动力学 | 完整摘要 |
| Kubitscheck 2005 JCB 168:233 [81] | NTF2/transportin 停留 5.8/7.1 ms | 单分子 | 完整摘要 |
| Lowe 2010 Nature 467:600 [82] | 单 cargo 亚扩散、多亚步、Ran 定向 | 单分子 | 完整摘要 |
| Grünwald 2011 Nature 475:333 [83] | RNA 输出动态综述（含 proteomics 推断） | 综述 | 完整摘要 |
| D'Angelo 2009 Cell 136:284 [84] | NPC 衰老退化、核渗漏、氧化损伤 | 衰老模型 | 完整摘要 |
| Savas 2012 Science 335:942 [85] | 大鼠脑 ELLP（NPC+染色质）不更新 | 大鼠 | 完整摘要 |
| Freibaum 2015 Nature 525:129（2015-08-26）[86] | C9orf72 G4C2 果蝇、18 个 NPC/输出修饰因子 | 果蝇 | 完整摘要 |
| Eftekharzadeh 2018 Neuron 99:925（2018-09-01）[87] | tau 结合 NUP、Nup98 促 tau 聚集 | 小鼠+AD 脑 | 完整摘要 |
| Ahn 2021 Nature 595:591（2021-06-23）[88] | NUP98-HOXA9 LLPS 致白血病、超增强子样 | 癌症模型 | 完整摘要 |
| Fare & Rothstein 2024 Nucleus 15:2314297 [89] | NPC 功能障碍与疾病综述 | 综述 | 完整摘要 |
| Laurell 2011 Cell 144:539 [90] | Nup98 有丝分裂超磷酸化（CDK1/Nek）驱动 NPC 解体 | 细胞 | 完整摘要 |
| Mishra 2019 IJMS 20:596 [91] | FG 磷酸化对选择性的一珠一氨基酸 MD | 模拟（仅题录） | 仅书目 |
| Kreysing 2025 Cell 188:930（2025-01-17）[92] | HIV 衣壳穿 NPC 使其开裂、晶格完整 | 巨噬细胞+模拟 | 完整摘要 |
| Hoffmann 2025 Mol Cell 85:537（2024-12-26）[93] | NPC 扩张态调控通透性/压力依赖多孔流 | 盘基网柄菌 | 完整摘要 |
| Brzezinski 2025 Biomacromolecules 26:2060（2024-12-08）[94] | PEG 拥挤加速 Nup98 成熟/凝胶化 | 体外 | 完整摘要 |
| Michels 2026 Adv Sci 13:e76691（2026-07-20）[95] | 统一相分离+β-折叠老化的含时热力学模型 | 理论 | 完整摘要 |
| Ruan 2025 Nat Commun 16:10117（2025-11-18）[96] | NUP98-HOXA9 FG 构象随组装态变化、micelle 样寡聚 | 实验+模拟 | 完整摘要 |
| Callan & Tomlin 1950 Proc R Soc B 137:367 [97] | 两栖卵母细胞核膜 EM 结构 | 形态学；摘要未获 | 仅书目 |
| Afzelius 1955 Exp Cell Res 8:147 [98] | 海胆卵母细胞核膜孔/annuli | 形态学；摘要未获 | 仅书目 |
| Feldherr 1965 JCB 25:43 [99] | 胶体金微注射检验核环孔筛分 | 变形虫 | 完整摘要 |
| Blobel 1980 PNAS 77:1496 [100] | 细胞内蛋白质拓扑发生（信号假说） | 框架；摘要未获 | 仅书目 |
| Dingwall & Laskey 1986 Annu Rev Cell Biol 2:367 [101] | 核输入综述 | 综述；摘要未获 | 仅书目 |
| Newmeyer & Forbes 1988 Cell 52:641 [102] | 核输入拆为结合+ATP 依赖转位 | 体外 | 完整摘要 |
| Görlich 1994 Cell 79:767 [103] | 纯化 importin（核输入第一步必需） | 爪蟾 | 完整摘要 |
| Wente 1992 JCB 119:705 [104] | 酵母 FG-NUP 家族 NUP49/100/116（GLFG） | 酵母遗传 | 完整摘要 |
| Strawn 2004 Nat Cell Biol 6:197 [105] | FG 结构域组合敲除、冗余/多路径 | 酵母遗传 | 完整摘要 |
| Jain 2016 Biophys J 111:768 [106] | 皮秒去偏振映射 α-syn 骨架扭转 | 方法 | 完整摘要 |
| Loman 2010 Photochem Photobiol Sci 9:627（2009-12-04）[107] | 偏振 FCS 测远长于寿命的旋转扩散 | 方法 | 完整摘要 |
| Schrimpf 2018 Biophys J 114:1518 [108] | PAM 荧光分析框架 | 软件 | 完整摘要 |
| Sindbert 2011 JACS 133:2463 [109] | 染料连接子长度/刚性影响 FRET 精度 | 方法 | 完整摘要 |
| Teijeiro-Gonzalez 2021 Biophys J 120:254（2020-12-18）[110] | TRFA+MD 表征 GFP homo-FRET | 方法 | 完整摘要 |
| Robustelli 2018 PNAS 115:E4758 [111] | 六力场无一同时准确描述折叠/无序蛋白 | 力场基准 | 完整摘要 |
| Monticelli 2008 JCTC 4:819 [112] | Martini 蛋白扩展 | 力场 | 完整摘要 |
| Marrink 2007 JPCB 111:7812 [113] | Martini 力场 | 力场 | 完整摘要 |
| Rabut 2004 Nat Cell Biol 6:1114 [114] | 活细胞 NPC 亚基停留时间跨五数量级 | 活细胞 | 完整摘要 |
| Cardarelli 2012 PNAS 109:9863 [115] | FCS+单 NPC 追踪：Nup153 离散交换 | 活细胞 | 完整摘要 |
| Beck 2004 Science 306:1387 [116] | 冷冻电子断层：中央塞/转运体=在途货物 | 盘基网柄菌 | 完整摘要 |
| Akey & Radermacher 1993 JCB 122:1 [117] | 爪蟾 NPC 冷冻电镜、中央锥形柱 | 爪蟾 | 完整摘要 |
| Beck & Hurt 2017 NRMCA 18:73（2016-12-21）[118] | NPC 结构功能综述 | 综述 | 完整摘要 |
| Lin & Hoelz 2019 Annu Rev Biochem 88:725 [119] | NPC 结构更新综述 | 综述 | 完整摘要 |
| Hummer & Szabo 2017 JPCB 121（2016-10-10）[120] | FRET 取向因子动力学 | 理论（谱系旁证） | 完整摘要 |
| Lemke 2007 Nat Chem Biol 3:769（2007-10-28）[121] | 光笼氨基酸控制磷酸化（Schultz 通讯） | 谱系旁证 | 完整摘要 |
| Schaffer 1999 / Koshioka 1995 / Feinstein 2003 / Wahl 1977（PDF refs 61/60/63/64） | TRFA 方法学经典（YFP ρ=16 ns 等由 PDF Methods 转述） | EuropePMC 检索未获 | 仅书目（PDF 转引） |

**官方页/数据库记录（非独立论文）**：MPI Hummer CV [1]、Hummer 组成员页 [2]、MPI 高被引新闻 [3]、IMB Lemke 传记 [4]、JGU ERC 新闻 [5]、USTC Tang 主页 [6]、Tang ORCID [7]、WHU Yu Miao 页 [8]、Heidari ORCID [9]、Palacio-Rodriguez ORCID [10]、MPI Dioscuri/Sikora 页 [11]、MPG Lasker 新闻 [12]、Görlich JAMA Lasker  essay [13]、SUSTech Tang 讲座简介 [14]、RCSB 7R5K [34]/3W5K [35]、Zenodo LAMMPS [122]/GROMACS [123]。这些是作者/结构/数据记录，非独立研究论文。

---

## References（编号带 URL）

[1] MPI Biophysics, Gerhard Hummer CV (Department of Theoretical Biophysics). https://www.biophys.mpg.de/2588123/gerhard-hummer
[2] MPI Biophysics, Hummer Department Members. https://www.biophys.mpg.de/research/gerhard-hummer-theoretical-biophysics/members
[3] MPI Biophysics News (2023-11-21), Gerhard Hummer Belongs to the Highly Cited Researchers. https://www.biophys.mpg.de/2784467/Gerhard-Hummer-highly-cited-researcher
[4] IMB Mainz, Lemke Lab Biography. https://www.imb.de/research/lemke/biography/
[5] JGU/EurekAlert (2026-06-23), ERC Advanced Grants for two researchers of Mainz (Lemke MShapeM). https://www.eurekalert.org/news-releases/1133164
[6] USTC 教师主页, 唐爱辉. https://faculty.ustc.edu.cn/tangaihui/zh_CN/index.htm
[7] ORCID, Ai-Hui Tang (0000-0003-3715-6714). https://orcid.org/0000-0003-3715-6714
[8] 武汉大学泰康生命医学中心, 于淼. https://tkclms.whu.edu.cn/info/1178/4306.htm
[9] ORCID, Maziar Heidari (0000-0002-8081-6602). https://orcid.org/0000-0002-8081-6602
[10] ORCID, Karen Palacio-Rodriguez (0000-0003-4327-8478). https://orcid.org/0000-0003-4327-8478
[11] MPI Biophysics, Dioscuri Centre for Modelling of Posttranslational Modifications (Mateusz Sikora). https://www.biophys.mpg.de/dioscuri-centre-for-modelling-of-posttranslational-modifications
[12] Max-Planck-Gesellschaft News (2025-09-11), Lasker Award 2025 for Dirk Görlich. https://www.mpg.de/25367852/0910-bich-lasker-award-2025-17216463-x
[13] Görlich D. The FG Phase—A Biomolecular Condensate That Governs Transport Through Nuclear Pores: 2025 Albert Lasker Basic Medical Research Award. JAMA (2025). https://doi.org/10.1001/jama.2025.16179
[14] 南方科技大学生物系讲座简介, 唐爱辉：纳米尺度下的突触组织与动态. https://bio.sustech.edu.cn/lecture/detail/id/704.html
[15] Yu M, et al. Glycosylation and importins liquefy the FG barrier in live nuclear pores. Nature (2026), firstPublicationDate 2026-11-11, PMID 43015467. https://doi.org/10.1038/s41586-026-11258-0
[16] Yu M, et al. O-GlcNAcylation and an importin-β radial gradient keep the FG barrier liquid in live-cell nuclear pores. bioRxiv (2025-12-11). https://doi.org/10.64898/2025.12.09.693204
[17] Yu M, et al. Visualizing the disordered nuclear transport machinery in situ. Nature 617:162–169 (2023-04-26), PMC10156602. https://doi.org/10.1038/s41586-023-05990-0
[18] Yu M, et al. Deciphering the conformations and dynamics of FG-nucleoporins in situ. bioRxiv (2022-07-08). https://doi.org/10.1101/2022.07.07.499201
[19] Reinkemeier CD & Lemke EA. Dual film-like organelles enable spatial separation of orthogonal eukaryotic translation. Cell 184:4886–4903 (2021-08-24). https://doi.org/10.1016/j.cell.2021.08.001
[20] Reinkemeier CD, Girona GE, Lemke EA. Designer membraneless organelles enable codon reassignment of selected mRNAs in eukaryotes. Science 363:eaaw2644 (2019-03-01). https://doi.org/10.1126/science.aaw2644
[21] Werther P, et al. Bio-orthogonal red and far-red fluorogenic probes for wash-free live-cell and super-resolution microscopy. ACS Cent Sci 7:1561–1571 (2021-08-20), PMC8461766. https://doi.org/10.1021/acscentsci.1c00703
[22] Milles S & Lemke EA. Mapping multivalency and differential affinities within large intrinsically disordered protein complexes with segmental motion analysis. Angew Chem Int Ed 53:7364–7367 (2014-06-04). https://doi.org/10.1002/anie.201403694
[23] Milles S, et al. Plasticity of an ultrafast interaction between nucleoporins and nuclear transport receptors. Cell 163:734–745 (2015-10-08). https://doi.org/10.1016/j.cell.2015.09.047
[24] Milles S, et al. Facilitated aggregation of FG nucleoporins under molecular crowding conditions. EMBO Rep 14:178–183 (2012-12-14). https://doi.org/10.1038/embor.2012.204
[25] Aramburu IV & Lemke EA. Floppy but not sloppy: interaction mechanism of FG-nucleoporins and nuclear transport receptors. Semin Cell Dev Biol 68:34–41 (2017-06-30). https://doi.org/10.1016/j.semcdb.2017.06.026
[26] Celetti G, et al. The liquid state of FG-nucleoporins mimics permeability barrier properties of nuclear pore complexes. J Cell Biol 219:e201907157 (2020-01-01). https://doi.org/10.1083/jcb.201907157
[27] Heinß N, Sushkin M, Yu M, Lemke EA. Multifunctionality of F-rich nucleoporins. Biochem Soc Trans 48:2603–2614 (2020-12-01). https://doi.org/10.1042/BST20200357
[28] Mosalaganti S, et al. AI-based structure prediction empowers integrative structural analysis of human nuclear pores. Science 376:eabm9506 (2022-06-10). https://doi.org/10.1126/science.abm9506
[29] Benayad Z, von Bülow S, Stelzl LS, Hummer G. Simulation of FUS protein condensates with an adapted coarse-grained model. J Chem Theory Comput 17:525–537 (2020-12-13). https://doi.org/10.1021/acs.jctc.0c01064
[30] Heidari M, Sikora M, Hummer G. Refined protein–sugar interactions in the Martini force field. J Chem Theory Comput 20:10259–10265 (2024-11-08). https://doi.org/10.1021/acs.jctc.4c01092
[31] Schmalhorst PS, Deluweit F, Scherrers R, Heisenberg CP, Sikora M. Overcoming the limitations of the MARTINI force field in simulations of polysaccharides. J Chem Theory Comput 13:5039–5053 (2017-09-08). https://doi.org/10.1021/acs.jctc.7b00374
[32] Stark AC, Andrews CT, Elcock AH. Toward optimized potential functions for protein–protein interactions in aqueous solutions. J Chem Theory Comput 9:4176–4185 (2013-09-01). https://doi.org/10.1021/ct400008p
[33] Choi S, et al. Structural basis for the selective nuclear import of the C2H2 zinc-finger protein Snail by importin β. Acta Crystallogr D 70:1050–1060 (2014-03-19). https://doi.org/10.1107/S1399004714000972
[34] RCSB PDB 7R5K, Human nuclear pore complex (constricted), ELECTRON MICROSCOPY, released 2022-06-22. https://www.rcsb.org/structure/7R5K
[35] RCSB PDB 3W5K, Crystal structure of Snail1 and importin beta complex, X-RAY DIFFRACTION, released 2014-03-05. https://www.rcsb.org/structure/3W5K
[36] Sau A, et al. Overlapping nuclear import and export paths unveiled by two-colour MINFLUX. Nature 640:821–827 (2025-03-19), PMC12003200. https://doi.org/10.1038/s41586-025-08738-0
[37] Balzarotti F, et al. Nanometer resolution imaging and tracking of fluorescent molecules with minimal photon fluxes. Science 355:606–612 (2016-12-22). https://doi.org/10.1126/science.aak9913
[38] Chowdhury R, Sau A, Musser SM. Super-resolved 3D tracking of cargo transport through nuclear pore complexes. Nat Cell Biol 24:112–122 (2022-01-10). https://doi.org/10.1038/s41556-021-00815-6
[39] Tang AH, Chen H, Li TP, Metzbower SR, MacGillavry HD, Blanpied TA. A trans-synaptic nanocolumn aligns neurotransmitter release to receptors. Nature 536:210–214 (2016-07-27). https://doi.org/10.1038/nature19058
[40] Frey S, Richter RP, Görlich D. FG-rich repeats of nuclear pore proteins form a three-dimensional meshwork with hydrogel-like properties. Science 314:815–817 (2006-11-01). https://doi.org/10.1126/science.1132516
[41] Frey S & Görlich D. A saturated FG-repeat hydrogel can reproduce the permeability properties of nuclear pore complexes. Cell 130:512–523 (2007-08-01). https://doi.org/10.1016/j.cell.2007.06.024
[42] Ader C, et al. Amyloid-like interactions within nucleoporin FG hydrogels. Proc Natl Acad Sci USA 107:6281–6285 (2010-03-18). https://doi.org/10.1073/pnas.0910163107
[43] Hülsmann BB, Labokha AA, Görlich D. The permeability of reconstituted nuclear pores provides direct evidence for the selective phase model. Cell 150:738–751 (2012-08-01). https://doi.org/10.1016/j.cell.2012.07.019
[44] Labokha AA, et al. Systematic analysis of barrier-forming FG hydrogels from Xenopus nuclear pore complexes. EMBO J 32:204–218 (2012-11-30), PMC3553378. https://doi.org/10.1038/emboj.2012.302
[45] Schmidt HB & Görlich D. Nup98 FG domains from diverse species spontaneously phase-separate into particles with nuclear pore-like permselectivity. eLife 4:e04251 (2015-01-06). https://doi.org/10.7554/eLife.04251
[46] Najbauer EE, Ng SC, Griesinger C, Görlich D, Andreas LB. Atomic resolution dynamics of cohesive interactions in phase-separated Nup98 FG domains. Nat Commun 13:1494 (2022-03-21). https://doi.org/10.1038/s41467-022-28821-8
[47] Ibáñez de Opakua A, et al. Molecular interactions of FG nucleoporin repeats at high resolution. Nat Chem 14:1278–1285 (2022-09-22), PMC9630130. https://doi.org/10.1038/s41557-022-01035-7
[48] Ng SC, et al. Barrier properties of Nup98 FG phases ruled by FG motif identity and inter-FG spacer length. Nat Commun 14:747 (2023-02-10). https://doi.org/10.1038/s41467-023-36331-4
[49] Fu L, et al. HIV-1 capsids enter the FG phase of nuclear pores like a transport receptor. Nature 626:843–851 (2024-01-24). https://doi.org/10.1038/s41586-023-06966-w
[50] Fu L, et al. Nuclear pore passage of the HIV capsid is driven by its unusual surface amino acid composition. Nat Struct Mol Biol 32:2476–2491 (2025-10-09). https://doi.org/10.1038/s41594-025-01684-5
[51] Rout MP, Aitchison JD, Suprapto A, Hjertaas K, Zhao Y, Chait BT. The yeast nuclear pore complex: composition, architecture, and transport mechanism. J Cell Biol 148:635–651 (2000-02-01). https://doi.org/10.1083/jcb.148.4.635
[52] Rout MP, Aitchison JD, Magnasco MO, Chait BT. Virtual gating and nuclear transport: the hole picture. Trends Cell Biol 13:622–628 (2003-12-01). https://doi.org/10.1016/j.tcb.2003.10.007
[53] Denning DP, Patel SS, Uversky V, Fink AL, Rexach M. Disorder in the nuclear pore complex: the FG repeat regions of nucleoporins are natively unfolded. Proc Natl Acad Sci USA 100:2450–2455 (2003-02-25). https://doi.org/10.1073/pnas.0437902100
[54] Denning DP & Rexach MF. Rapid evolution exposes the boundaries of domain structure and function in natively unfolded FG nucleoporins. Mol Cell Proteomics 6:272–282 (2006-11-01). https://doi.org/10.1074/mcp.M600309-MCP200
[55] Patel SS & Rexach MF. Discovering novel interactions at the nuclear pore complex using bead halo. Mol Cell Proteomics 7:121–131 (2007-09-26). https://doi.org/10.1074/mcp.M700407-MCP200
[56] Yamada J, et al. A bimodal distribution of two distinct categories of intrinsically disordered structures with separate functions in FG nucleoporins. Mol Cell Proteomics 9:2205–2224 (2010-04-05). https://doi.org/10.1074/mcp.M000035-MCP201
[57] Lim RY, et al. Nanomechanical basis of selective gating by the nuclear pore complex. Science 318:640–643 (2007-10-04). https://doi.org/10.1126/science.1145980
[58] Sakiyama Y, Mazur A, Kapinos LE, Lim RYH. Spatiotemporal dynamics of the nuclear pore complex transport barrier resolved by high-speed atomic force microscopy. Nat Nanotechnol 11:719–723 (2016-05-02). https://doi.org/10.1038/nnano.2016.62
[59] Atkinson CE, Mattheyses AL, Kampmann M, Simon SM. Conserved spatial organization of FG domains in the nuclear pore complex. Biophys J 104:37–50 (2013-01-08). https://doi.org/10.1016/j.bpj.2012.11.3823
[60] Timney BL, et al. Simple rules for passive diffusion through the nuclear pore complex. J Cell Biol 215:57–76 (2016-10-03). https://doi.org/10.1083/jcb.201601004
[61] Kapinos LE, Schoch RL, Wagner RS, Schleicher KD, Lim RYH. Karyopherin-centric control of nuclear pores based on molecular occupancy and kinetic analysis of multivalent binding with FG nucleoporins. Biophys J 106:1751–1762 (2014-04-01). https://doi.org/10.1016/j.bpj.2014.02.021
[62] Kapinos LE, Huang B, Rencurel C, Lim RYH. Karyopherins regulate nuclear pore complex barrier and transport function. J Cell Biol 216:3609–3624 (2017-09-01). https://doi.org/10.1083/jcb.201702092
[63] Kalita J, et al. Karyopherin enrichment and compensation fortifies the nuclear pore complex against nucleocytoplasmic leakage. J Cell Biol 221:e202108107 (2022-01-28). https://doi.org/10.1083/jcb.202108107
[64] Kozai T, et al. Karyopherins remodel the dynamic organization of the nuclear pore complex transport barrier. Nat Cell Biol 27:2089–2101 (2025-12-02), PMC12717009. https://doi.org/10.1038/s41556-025-01812-9
[65] Hough LE, et al. The molecular mechanism of nuclear transport revealed by atomic-scale measurements. eLife 4:e10027 (2015-09-15). https://doi.org/10.7554/eLife.10027
[66] Raveh B, et al. Slide-and-exchange mechanism for rapid and selective transport through the nuclear pore complex. Proc Natl Acad Sci USA 113:E2489–E2497 (2016-04-18). https://doi.org/10.1073/pnas.1522663113
[67] Raveh B, et al. Integrative mapping reveals molecular features underlying the mechanism of nucleocytoplasmic transport. Proc Natl Acad Sci USA 122:e2507559122 (2025-10-16). https://doi.org/10.1073/pnas.2507559122
[68] Cowburn D & Rout M. Improving the hole picture: towards a consensus on the mechanism of nuclear transport. Biochem Soc Trans 51:871–886 (2023-04-01). https://doi.org/10.1042/BST20220494
[69] Winogradoff D, Chou HY, Maffeo C, Aksimentiev A. Percolation transition prescribes protein size-specific barrier to passive transport through the nuclear pore complex. Nat Commun 13:5138 (2022-09-01). https://doi.org/10.1038/s41467-022-32857-1
[70] Dekker M, et al. Kap-centric Nsp1-mediated nuclear transport at full amino acid resolution. Nat Commun 16:11497 (2025-12-12). https://doi.org/10.1038/s41467-025-66329-z
[71] Feng Q, et al. Channel width modulates the permeability of DNA origami-based nuclear pore mimics. Sci Adv 10:eadq8773 (2024-11-13). https://doi.org/10.1126/sciadv.adq8773
[72] de Vries HW, et al. Spatial control of karyopherin binding avidity within NPC mimics revealed by designer FG-nucleoporins. Nat Commun 17:11379 (2026-09-28). https://doi.org/10.1038/s41467-026-77818-0
[73] Dekker M, Hou Chen SM, Adupa V, Onck PR. Modeling disorder, secondary structure formation, and amyloid growth in FG-nucleoporins. bioRxiv (2026-04-08). https://doi.org/10.64898/2026.04.07.716937
[74] Baumann KN, Bertosin E, Barth A, Dekker C, Lim RYH. Elucidating the nanoscopic organization and dynamics of the nuclear pore complex. Nucleus 16:2510106 (2025-06-04). https://doi.org/10.1080/19491034.2025.2510106
[75] Jäkel S, Mingot JM, Schwarzmaier P, Hartmann E, Görlich D. Importins fulfil a dual function as nuclear import receptors and cytoplasmic chaperones for exposed basic domains. EMBO J 21:377–386 (2002-02-01). https://doi.org/10.1093/emboj/21.3.377
[76] Lowe AR, et al. Importin-β modulates the permeability of the nuclear pore complex in a Ran-dependent manner. eLife 4:e04052 (2015-03-06). https://doi.org/10.7554/eLife.04052
[77] Li B & Kohler JJ. Glycosylation of the nuclear pore. Traffic 15:347–361 (2014-02-13). https://doi.org/10.1111/tra.12150
[78] Yoo TY & Mitchison TJ. O-GlcNAc modification of nuclear pore complexes accelerates bidirectional transport. J Cell Biol 220:e202010141 (2021-07-01), PMC8091080. https://doi.org/10.1083/jcb.202010141
[79] Wulff-Fuentes E, et al. The human O-GlcNAcome database and meta-analysis. Sci Data 8:25 (2021-01-21). https://doi.org/10.1038/s41597-021-00810-4
[80] Ribbeck K & Görlich D. Kinetic analysis of translocation through nuclear pore complexes. EMBO J 20:1320–1330 (2001-03-01). https://doi.org/10.1093/emboj/20.6.1320
[81] Kubitscheck U, et al. Nuclear transport of single molecules: dwell times at the nuclear pore complex. J Cell Biol 168:233–243 (2005-01-01). https://doi.org/10.1083/jcb.200411005
[82] Lowe AR, et al. Selectivity mechanism of the nuclear pore complex characterized by single cargo tracking. Nature 467:600–603 (2010-09-01). https://doi.org/10.1038/nature09285
[83] Grünwald D, Singer RH, Rout M. Nuclear export dynamics of RNA-protein complexes. Nature 475:333–341 (2011-07-20). https://doi.org/10.1038/nature10318
[84] D'Angelo MA, Raices M, Panowski SH, Hetzer MW. Age-dependent deterioration of nuclear pore complexes causes a loss of nuclear integrity in postmitotic cells. Cell 136:284–295 (2009-01-01). https://doi.org/10.1016/j.cell.2008.11.037
[85] Savas JN, Toyama BH, Xu T, Yates JR, Hetzer MW. Extremely long-lived nuclear pore proteins in the rat brain. Science 335:942 (2012-02-02). https://doi.org/10.1126/science.1217421
[86] Freibaum BD, et al. GGGGCC repeat expansion in C9orf72 compromises nucleocytoplasmic transport. Nature 525:129–133 (2015-08-26). https://doi.org/10.1038/nature14974
[87] Eftekharzadeh B, et al. Tau protein disrupts nucleocytoplasmic transport in Alzheimer's disease. Neuron 99:925–940.e7 (2018-09-01). https://doi.org/10.1016/j.neuron.2018.07.039
[88] Ahn JH, et al. Phase separation drives aberrant chromatin looping and cancer development. Nature 595:591–595 (2021-06-23). https://doi.org/10.1038/s41586-021-03662-5
[89] Fare CM & Rothstein JD. Nuclear pore dysfunction and disease: a complex opportunity. Nucleus 15:2314297 (2024-02-21). https://doi.org/10.1080/19491034.2024.2314297
[90] Laurell E, et al. Phosphorylation of Nup98 by multiple kinases is crucial for NPC disassembly during mitotic entry. Cell 144:539–550 (2011-02-01). https://doi.org/10.1016/j.cell.2011.01.012
[91] Mishra A, Sipma W, Veenhoff LM, Van der Giessen E, Onck PR. The effect of FG-nup phosphorylation on NPC selectivity: a one-bead-per-amino-acid molecular dynamics study. Int J Mol Sci 20:596 (2019-01-30). https://doi.org/10.3390/ijms20030596
[92] Kreysing JP, Heidari M, et al. Passage of the HIV capsid cracks the nuclear pore. Cell 188:930–943.e21 (2025-01-17). https://doi.org/10.1016/j.cell.2024.12.008
[93] Hoffmann PC, et al. Nuclear pore permeability and fluid flow are modulated by its dilation state. Mol Cell 85:537–554.e11 (2024-12-26). https://doi.org/10.1016/j.molcel.2024.11.038
[94] Brzezinski M, et al. Protein-specific crowding accelerates aging in protein condensates. Biomacromolecules 26:2060–2075 (2024-12-08). https://doi.org/10.1021/acs.biomac.4c00609
[95] Michels JJ, Caria J, Lemke EA. A unifying thermodynamic model for phase separation and aging of biopolymers. Adv Sci 13:e76691 (2026-07-20). https://doi.org/10.1002/advs.76691
[96] Ruan H, et al. Differential conformational expansion of NUP98-HOXA9 oncoprotein from nanosized assemblies to macrophases. Nat Commun 16:10117 (2025-11-18). https://doi.org/10.1038/s41467-025-66327-1
[97] Callan HG & Tomlin SG. Experimental studies on amphibian oocyte nuclei. I. Investigation of the structure of the nuclear membrane by means of the electron microscope. Proc R Soc Lond B 137:367–378 (1950-10-01). https://doi.org/10.1098/rspb.1950.0047
[98] Afzelius BA. The ultrastructure of the nuclear membrane of the sea urchin oocyte as studied with the electron microscope. Exp Cell Res 8:147–158 (1955-02-01). https://doi.org/10.1016/0014-4827(55)90051-3
[99] Feldherr CM. The effect of the electron-opaque pore material on exchanges through the nuclear annuli. J Cell Biol 25:43–53 (1965-04-01). https://doi.org/10.1083/jcb.25.1.43
[100] Blobel G. Intracellular protein topogenesis. Proc Natl Acad Sci USA 77:1496–1500 (1980-03-01). https://doi.org/10.1073/pnas.77.3.1496
[101] Dingwall C & Laskey RA. Protein import into the cell nucleus. Annu Rev Cell Biol 2:367–390 (1986). https://doi.org/10.1146/annurev.cb.02.110186.002055
[102] Newmeyer DD & Forbes DJ. Nuclear import can be separated into distinct steps in vitro: nuclear pore binding and translocation. Cell 52:641–653 (1988-03-01). https://doi.org/10.1016/0092-8674(88)90402-3
[103] Görlich D, Prehn S, Laskey RA, Hartmann E. Isolation of a protein that is essential for the first step of nuclear protein import. Cell 79:767–778 (1994-12-01). https://doi.org/10.1016/0092-8674(94)90067-1
[104] Wente SR, Rout MP, Blobel G. A new family of yeast nuclear pore complex proteins. J Cell Biol 119:705–723 (1992-11-01). https://doi.org/10.1083/jcb.119.4.705
[105] Strawn LA, Shen T, Shulga N, Goldfarb DS, Wente SR. Minimal nuclear pore complexes define FG repeat domains essential for transport. Nat Cell Biol 6:197–206 (2004-02-22). https://doi.org/10.1038/ncb1097
[106] Jain N, et al. Direct observation of the intrinsic backbone torsional mobility of disordered proteins. Biophys J 111:768–774 (2016-08-01). https://doi.org/10.1016/j.bpj.2016.07.023
[107] Loman A, Gregor I, Stutz C, Mund M, Enderlein J. Measuring rotational diffusion of macromolecules by fluorescence correlation spectroscopy. Photochem Photobiol Sci 9:627–636 (2009-12-04). https://doi.org/10.1039/b9pp00029a
[108] Schrimpf W, Barth A, Hendrix J, Lamb DC. PAM: a framework for integrated analysis of imaging, single-molecule, and ensemble fluorescence data. Biophys J 114:1518–1528 (2018-04-01). https://doi.org/10.1016/j.bpj.2018.02.035
[109] Sindbert S, et al. Accurate distance determination of nucleic acids via Förster resonance energy transfer: implications of dye linker length and rigidity. J Am Chem Soc 133:2463–2480 (2011-02-03). https://doi.org/10.1021/ja105725e
[110] Teijeiro-Gonzalez Y, et al. Time-resolved fluorescence anisotropy and molecular dynamics analysis of a novel GFP homo-FRET dimer. Biophys J 120:254–269 (2020-12-18). https://doi.org/10.1016/j.bpj.2020.11.2275
[111] Robustelli P, Piana S, Shaw DE. Developing a molecular dynamics force field for both folded and disordered protein states. Proc Natl Acad Sci USA 115:E4758–E4766 (2018-05-07). https://doi.org/10.1073/pnas.1800690115
[112] Monticelli L, et al. The MARTINI coarse-grained force field: extension to proteins. J Chem Theory Comput 4:819–834 (2008-05-01). https://doi.org/10.1021/ct700324x
[113] Marrink SJ, Risselada HJ, Yefimov S, Tieleman DP, de Vries AH. The MARTINI force field: coarse grained model for biomolecular simulations. J Phys Chem B 111:7812–7824 (2007-06-15). https://doi.org/10.1021/jp071097f
[114] Rabut G, Doye V, Ellenberg J. Mapping the dynamic organization of the nuclear pore complex inside single living cells. Nat Cell Biol 6:1114–1121 (2004-10-24). https://doi.org/10.1038/ncb1184
[115] Cardarelli F, Lanzano L, Gratton E. Capturing directed molecular motion in the nuclear pore complex of live cells. Proc Natl Acad Sci USA 109:9863–9868 (2012-06-04). https://doi.org/10.1073/pnas.1200486109
[116] Beck M, et al. Nuclear pore complex structure and dynamics revealed by cryoelectron tomography. Science 306:1387–1390 (2004-10-28). https://doi.org/10.1126/science.1104808
[117] Akey CW & Radermacher M. Architecture of the Xenopus nuclear pore complex revealed by three-dimensional cryo-electron microscopy. J Cell Biol 122:1–19 (1993-07-01). https://doi.org/10.1083/jcb.122.1.1
[118] Beck M & Hurt E. The nuclear pore complex: understanding its function through structural insight. Nat Rev Mol Cell Biol 18:73–89 (2016-12-21). https://doi.org/10.1038/nrm.2016.147
[119] Lin DH & Hoelz A. The structure of the nuclear pore complex (an update). Annu Rev Biochem 88:725–783 (2019-03-18). https://doi.org/10.1146/annurev-biochem-062917-011901
[120] Hummer G & Szabo A. Dynamics of the orientational factor in fluorescence resonance energy transfer. J Phys Chem B (2016-10-10). https://doi.org/10.1021/acs.jpcb.6b08345
[121] Lemke EA, Summerer D, Geierstanger BH, Brittain SM, Schultz PG. Control of protein phosphorylation with a genetically encoded photocaged amino acid. Nat Chem Biol 3:769–772 (2007-10-28). https://doi.org/10.1038/nchembio.2007.44
[122] Yu M, et al. LAMMPS file repository for 'Glycosylation and importins liquefy the FG barrier in live nuclear pores'. Zenodo (2026). https://doi.org/10.5281/zenodo.15025565
[123] Yu M, et al. GROMACS repository for 'Glycosylation and importins liquefy the FG barrier in live nuclear pores'. Zenodo (2026). https://doi.org/10.5281/zenodo.17588507

---

## 诚实收尾（检索边界与未核实项）

本背景解读检索截止 2026-11-14。外部文献阅读以 EuropePMC core 完整摘要为主、辅以 PMC 图注核证（图号已核实者注明），未对任何外部文献做逐段全文审计；目标 PDF 为唯一全文定向核读。以下各项保守标注、不编造：

- **导师关系**：Hummer（维也纳博士 1992）、Lemke（哥廷根博士 2005）、Tang（北大博士 2007）、Yu（港科大博士 2015）、Heidari（马普聚合物所博士）、Sikora（波兰科学院物理所博士）、Palacio-Rodriguez（索邦博士 2022）的官方 CV/ORCID/机构页**均未载明导师姓名**，本文一律留空白；Lemke 在 Schultz 组、Yu 在 Lemke 组仅以发表记录旁证并标注推断，不据共同署名认定师承。Tang 与 Blanpied 为同机构合作者（2016 Nature 通讯），未声明师承。
- **Tang 主页本科结束年"2022"为录入笔误**，以 ORCID（2002-07）为准；Tang 组 2023–2026 其他 MINFLUX 核孔论文经作者检索未见（检索边界：EuropePMC AUTH+MINFLUX）。
- **"Milburn/Wente"**（任务清单）未能匹配到具体论文，疑为 Milles/Strawn 之误，未裁决；Wente 谱系由 [104][105][60] 覆盖。
- **Rexach 组最新后续**：EuropePMC "Rexach M" 作者检索返回同名流行病学者噪声，未获 Rexach MF 本人 2020–2026 可靠后续，标注检索边界。
- **Schaffer 1999 / Koshioka 1995 / Feinstein 2003 / Wahl 1977 / Paine 1975**：EuropePMC 检索未获，按 PDF 参考文献仅书目转引，不补写实验细节（YFP ρ=16 ns 等数值由本文 Methods 转述，非直接核自原始文献）。
- **外部文献图未嵌入**：PMC bin（404）与 EuropePMC bin（403）、Springer media（404）下载通道受阻，故仅给出已核实图号；本文图（Fig 1–5、ED Fig 1–9）由同源《文献解读》逐图精读，本文件不重做。
- **结构主张**：7R5K（人 NPC 收缩态支架，冷冻电镜）与 3W5K（Snail1–importin-β 晶体）经 RCSB 逐条核对；本文 FG 构象/importin-β 分布/糖基化效应为粗粒化/Martini 模型，**非解析结构**；3W5K 非 FG–importin-β 复合物。
- **版本状态**：正式版 Nature 2026-11-11 在线（PMID 43015467，尚无卷期）；预印本 bioRxiv 2025-12-11（标题/作者串不同，正式版新增 Tang/武大团队与 MINFLUX）。在线日期以 EuropePMC firstPublicationDate 核证，PDF 占位符非权威。
- **统计**：本文 P 值按原文转述（如 OSMI-4 多位点 P < 0.0001、Thiamet-G 多位点 P > 0.05、运输速率 Welch t + Holm 校正），未美化弱阳性；体外 n=3、活细胞 n=41–69/位点（3 次独立实验）如实标注。