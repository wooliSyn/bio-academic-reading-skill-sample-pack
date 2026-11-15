**文献信息：** Glycosylation and importins liquefy the FG barrier in live nuclear pores. Miao Yu (于淼), Maziar Heidari, Karen Palacio-Rodriguez, Hao Ruan (阮浩), Sara Mingu, Yu Chen (陈宇), Xu-Zhuo Gou (缑绪卓), Pingkai Shen (沈平恺), Songzi Liu (刘松子), Si-Yu Chen (陈思宇), Alam Ahmad Hidayat, Mathis Bode, Mateusz Sikora, Ai-Hui Tang (唐爱辉), Gerhard Hummer & Edward A. Lemke. Nature, 文章号 s41586-026-11258-0, DOI 10.1038/s41586-026-11258-0 (2026). 第一作者单位：武汉大学生命科学学院/泰康生命医学中心（复杂生物体代谢与调控全国重点实验室）与美因茨约翰内斯·古腾堡大学生物中心（Biocenter）；通讯作者：Gerhard Hummer（马克斯·普朗克生物物理研究所理论生物物理部/法兰克福歌德大学生物物理研究所）与 Edward A. Lemke（美因茨大学生物中心/美因茨分子生物学研究所 IMB）。作者贡献脚注9逐字为："These authors contributed equally: Miao Yu, Maziar Heidari."——即第一署名作者 Yu 与第二署名作者 Heidari 等贡献；本文按脚注原文转述，不作"共同第一作者"的升格表述。Received 6 March 2025；Accepted 6 October 2026；PDF 首页 "Published online: xx xx xxxx" 为占位符，不具权威性；经 EuropePMC REST 核证 firstPublicationDate = 2026-11-11，即在线发表日期为 2026 年 11 月 11 日。Open Access（CC BY 4.0）。

**一句话概括：** 核孔通透屏障的物理态不是"体外水凝胶那样的固体"，而是活细胞内由 importin-β 与 O-GlcNAc 糖基化共同维持的纳秒级类液态 FG 链段网络——本文用位点特异标记+时间分辨荧光各向异性直接测得活细胞 FG 结构域 ρslow 约 57–108 ns 且 2 h 稳定，而体外凝聚体 1 h 内液-固转变，并以实验匹配的多尺度模拟给出"importin-β 偏环周、伸展 FG 占中央"的径向屏障组织，解释 MINFLUX 环周偏好轨迹，为 FG-NUP 相关癌症、病毒感染与神经退行疾病提供"细胞环境 tuning 无序蛋白材料态"的框架。

**解读说明：** 本解读基于所给 31 页 PDF 全文（正文 Article 含 Abstract、引言、7 个 Results 小节、Discussion；Methods；Extended Data Fig. 1–9；Nature Portfolio Reporting Summary）完成。主文 Fig. 1–5 共 39 个 panel（Fig.1=10、Fig.2=7、Fig.3=7、Fig.4=9、Fig.5=6），Extended Data Fig. 1–9 共 45 个 panel（ED1=5、ED2=10、ED3=5、ED4=3、ED5=4、ED6=3、ED7=3、ED8=6、ED9=6），全部按四字段模板解读（平行 panel 依合并规则合并条目但逐 panel 说明差异）。补充材料（Supplementary Figs. 1–20、Supplementary Videos 1–9、Supplementary Tables 1–6、Supplementary Text）**未随本 PDF 提供**，凡正文引用处均以括注标明其内容角色，不对其视觉细节作断言。图表视觉细节通过 PyMuPDF 按图区裁剪渲染（主图约 140 dpi、ED 约 110 dpi、Fig.4 统计括号局部 300 dpi）后逐图目视核对获得；坐标轴刻度、配色与括号归属均以渲染图为准。原文未提供的定量数据（如免疫印迹灰度定量、MINFLUX 单孔定位数）一律如实标注"原文未提供"。在线发表日期以 EuropePMC firstPublicationDate 核证（2026-11-11），不采信 PDF 首页占位符。

---

一、<基础概念注释>

**核孔复合体与运输机器**

- **核孔复合体（nuclear pore complex, NPC）：** 镶嵌于核被膜、介导核质间分子交换的超大蛋白组装体，由约 30 种核孔蛋白（nucleoporins, NUPs）以八重对称构成支架（scaffold），中央通道内填充无序 FG 结构域形成通透屏障。本文的全部测量与模拟都围绕"活细胞 NPC 中央通道内 FG 屏障的物理态与空间组织"展开；模拟几何取自人源收缩态 NPC 结构（PDB 7R5K）。
- **FG-NUPs（FG-rich nucleoporins，富含苯丙氨酸-甘氨酸重复的核孔蛋白）：** 一类含内在无序 FG 重复结构域的 NUPs（本文模拟包含 NUP54、NUP58、NUP62、NUP98、NUP214、NUP358、POM121、NUP153），其 FG  motifs 通过多价弱相互作用形成屏障并选择性结合运输受体。本文的核心对象；其"液态还是固态"是全文争议焦点。
- **NUP98：** 本文聚焦的关键 FG-NUP。结构域排布（Fig.1d）：1st FG（约 1–157）、GLEBS 结构域（约 157–214，结合 mRNA 输出因子 Rae1/Gle2 的结构化区）、2nd FG（约 214–505）、自蛋白水解切割位点（cleavage site）、Anchor 锚定域（约 595–863）与 C 端（863–920）；切割后 FG 段以锚定段 tether 于支架。体外构建体为残基 1–505 且删除 GLEBS（157–213），以避免变性剂快速稀释时结构化区误折叠。NUP98 是后生动物中 O-GlcNAc 修饰最重的蛋白之一，也是白血病融合癌蛋白（NUP98 融合）与神经退行相关 FG 聚集研究的模式分子。
- **NUP96：** NPC 支架（外环/内环连接区）组分，本文用内源 NUP96-mEGFP 敲入细胞系（U-2 OS-CRISPR-NUP96-mEGFP）作为 MINFLUX 的"支架参考通道"：以其定位点定义孔中心与八重参考系，再分析 importin-β 的径向分布。注意它只给参考系，不直接解析内环直径（作者自陈局限）。
- **核运输受体（nuclear transport receptor, NTR）/karyopherin：** 识别 cargo 核定位/输出信号并携带其穿越 NPC 的受体家族；与 FG motifs 的多价弱结合是其"选择性通行证"。本文以 importin-β 为代表研究 NTR 对屏障材料态的反向调控。
- **importin-β（KPNB1）：** 主要核输入受体，HEAT 重复超螺旋结构（模拟用 PDB 3W5K，去除 Snail1 配体），表面多条 FG 结合沟槽；在 NPC 处局部浓度达毫摩尔级（本文以自由染料滴定估得）。既往被提出具"分子伴侣样"性质（refs 36–38）；本文证明它在链段水平稀释 FG–FG 接触、延缓液-固转变，并塑造屏障径向组织。
- **选择性相/水凝胶模型（selective phase / hydrogel model）：** Görlich 学派提出 FG 重复序列体外形成饱和水凝胶，其通透选择性可复现 NPC（refs 5,6,13）；屏障被视为 cohesive FG 网络（偏固态）。本文的体外凝聚体老化实验正对应该模型的"固体端"，而活细胞数据对其提出限定。
- **虚拟门控/聚合物刷/柔性链模型（virtual gating / polymer brush / flexible chain）：** 另一极模型，把 FG 链视为熵排斥的柔性聚合物或刷（refs 9,15,24,25），屏障偏"动态液态/熵性"。本文活细胞纳秒链段运动支持动态端，但强调 tethering 与 confinement 造成的位置梯度。
- **karyopherin 中心模型（karyopherin-centric model）：** Lim 学派提出 NTR 占据度与多价结合动力学本身调控屏障（refs 10,52）；本文 importin-β 液化与径向组织为该模型提供链段级与空间级证据。
- **中央栓/中央密度（central plug / central density）：** 电镜与高速 AFM 在 NPC 中央观察到的栓状密度（refs 55,56,21），身份长期不明；本文径向组织提示中央轴并非 importin-β 主位置，并提出"双路线"假说解释中央密度可能为瞬态 cargo/运输复合物（推测）。
- **被动扩散与 facilitated 转运：** 小分子可被动穿过屏障，大 cargo 须结合 NTR 才能快速选择性通过；本文以 LINuS 报告子测的"核输入速率"即 facilitated 转运的功能读数。

**无序蛋白物理态与相变**

- **内在无序蛋白（intrinsically disordered protein, IDP）：** 缺乏稳定三维结构、以构象系综行使功能的蛋白；FG-NUPs 是典型 IDP。本文方法论意义在于证明 IDP 的"材料态"可由细胞环境（PTM、NTR、纳米限域）tuning。
- **生物分子凝聚体（biomolecular condensate）/液-液相分离（LLPS）：** 多价弱相互作用驱动的无膜浓缩相；本文体外 FG 凝聚体由纯化 NUP98 FG 快速稀释诱导相分离形成，是"体外屏障替代体系"。
- **液-固转变/分子老化（liquid-to-solid transition / molecular ageing）：** 凝聚体随时间从动态液态转为固态水凝胶/淀粉样态的过程；本文 Fig.1j、2c 显示体外 FG 凝聚体 1 h 内 ρslow 从约 100 ns 升至拟合上限 1000 ns，而活细胞 2 h 稳定——全文核心对比。
- **水凝胶（hydrogel）：** 交联网络持水的软固体；FG 水凝胶是选择性相模型的物质基础（refs 5,13,48）；本文以 ThT 与 ρslow 上限判定体外凝聚体成熟为水凝胶。
- **淀粉样相互作用（amyloid-like interactions）/硫黄素 T（thioflavin-T, ThT）：** 跨链 β 片层堆叠的有序聚集；ThT 结合淀粉样结构后荧光增强，本文用作凝聚体老化的独立结构读数（Fig.1j 插图：5 min 无信号→60 min 强黄色）。
- **聚集倾向段 85–124（aggregation-prone segment）：** NMR 与 cryo-EM 鉴定的人 NUP98 FG 内淀粉样倾向核心段（ref 11）；本文残基 100 位于其中，是老化最敏感位点，也是 importin-β 稀释效应与糖基化保护效应的"报告位点"。
- **链段运动（segmental motion）vs 整体旋转（overall rotation）：** IDP 局部链段（约 ≤50 残基关联长度）的纳秒摆动不同于整蛋白旋转；本文 ρslow 读前者，是"屏障是否液态"的直接动力学判据。
- **均方根残基间距 R\_E 与标度律：** 同链残基对距离的均方根随序列间隔 N\_res 的增长（R\_E ∝ N\_res^ν）反映链伸展度；本文以 Martini 模拟 R\_E 对比前作 in situ FLIM–FRET（ref 26）校准糖基化水平与相互作用强度。
- **相分离临界点（critical point）：** 凝聚体形成/消失的边界；本文 Martini 模型中 FG-NUPs 处于临界点附近（α\_c ≈ 0.55，实验匹配 α ≈ 0.6），故微小相互作用变化即可大幅改变组织——"细胞 tuning 材料态"的物理基础。
- **去混合（demixing）/选择性分配：** 修饰状态不同的 FG 组装体彼此不混溶；本文模拟+探针分配实验显示 O-GlcNAc 差异促进 demixing（Supplementary Figs. 16–18），提示 PTM 差异可 opposes mixing、塑造屏障分区。
- **纳米限域与 tethering/grafting：** FG 链一端锚定于支架、被限制在纳米通道内；锚定点附近 confinement 更强→链段更慢（Fig.1g 梯度），grafting 几何决定 FG 密度近壁偏高→importin-β 偏环周（Fig.3）。

**背景补注：FG 水凝胶与液-固相变这条研究线——"固体屏障"模型如何开创，本文站在哪一步**

这条线的史前史可溯至 1950s 电镜确立"核膜上有孔"的形态学事实（Callan & Tomlin 1950；Afzelius 1955，仅书目级），Feldherr 1965 胶体金显微注射给出"孔对大分子有筛分作用"的经典功能证据；Wente、Rout & Blobel 1992 鉴定酵母 FG-NUP 家族（JCB 119:705–723），Denning 2003 证明其 FG 重复天然无序（PNAS 100:2450–2455）——"无序、多价、可结合受体"的分子图像由此确立，但留下"无序链在孔内到底形成什么物理态"的缺口（谱系细节详见同源背景解读 A.3，已核证）。

**谁开创：Görlich 学派的凝聚态/固体端。** Frey, Richter & Görlich Science 2006（ref 13）首次证明 FG 富集重复序列体外自组装成具水凝胶样性质的三维网架；Frey & Görlich Cell 2007（ref 5）进一步证明单一 Nup98 FG 结构域的饱和水凝胶即可复现 NPC 通透选择性——importin-β 进入比同尺寸惰性分子快 >1000 倍、cargo 内流加速 >20000 倍、凝胶内扩散约 12 ms 即可穿过 NPC（数值详见同源背景解读，已核证）。Hülsmann 2012（ref 6）在爪蟾卵提取物重构 NPC 中证明 Nup98 多价 FG 内聚为屏障所必需；Schmidt & Görlich 2015（eLife 4:e04251）证明从哺乳类到 excavates 九类生物的 Nup98 FG 结构域都能自发相分离成具 NPC 典型分选选择性的"FG 颗粒"。这条线把"FG 相"提升为普适运输原理，Görlich 因此获 2025 年 Lasker 基础医学研究奖（详见同源背景解读）。

**对立面：熵刷/虚拟门与 karyopherin 中心模型。** Rout & Chait 提出"布朗亲和门控"（Rout 2000, JCB 148:635–651）与"虚拟门"（Rout 2003, Trends Cell Biol 13:622–628；ref 9）：FG 链形成熵刷，受体结合降低熵垒而无需稳定结构；Lim 2007（ref 15）以纳米力学证明 Kapβ1 使人 Nup153 FG 塌缩成紧凑构象、RanGTP 使其回到刷状熵垒；Lim 学派 Kapinos 2014/2017（refs 10,52）发展为"karyopherin 中心"占有模型——NTR 占有度与多价结合动力学本身调控屏障。两派证据几乎全部来自体外或透化体系，解释空间当年并未闭合。

**结构与老化线：液→固轨迹如何被一步步看清。** Ader 2010（ref 12）用固态 NMR 在 Nsp1 水凝胶中鉴定瞬态疏水接触与分子间 β-折叠（淀粉样相互作用）；Milles 2013（ref 36）证明拥挤把 FG 淀粉样聚集加速数个数量级、NTR 可抑制；Ibáñez de Opakua 2022（ref 11）以 NMR+cryo-EM 解析 NUP98 聚集倾向段 85–124 的淀粉样纤维多晶型并证明其低稳定、可逆；Najbauer 2022（ref 8）用 TRACT 证明 FG 在相分离态与可溶态都保持纳秒级旋转动态（尽管 FRAP 平移扩散慢）——局部链段运动与宏观材料态是不同时间尺度层级。更广的凝聚体领域，"液-固转变/分子老化"自 Patel 2015（Cell 162:1066–1077，FUS，ALS 突变加速）确立为普遍轨迹，ThT 淀粉样染色、流变学与 FRAP 是其标准读数（课本级常识）。

**遗留缺口与本文借鉴。** 缺口正在于：天然屏障在活细胞内的物理态从未被直接测量，"水凝胶/淀粉样"图像可能是失去细胞守护后的老化轨迹而非屏障本征态。本文的体外 FG 凝聚体老化对照（Fig.1j、2c：ρslow 1 h 内升至 1000 ns 拟合上限 + ThT 转阳）直接继承这条线的材料态读数与它鉴定的 85–124 敏感段（ref 11），以残基 100 为报告位点；同时以活细胞 TRFA 证明纳秒类液态、2 h 稳定——站在"用活细胞直接动力学重裁体外共识"这一步，把固体端模型重新定位为"病理老化偏离"而非简单否定。（阅读深度：本块谱系事实复用同源背景解读 A.3 已核证内容；refs 13/5 为摘要+本文转述级，refs 8/11/12 为 PMC 定向核读级，Patel 2015 为本次升级 EuropePMC 新核证书目+摘要级；深度作者谱系与跨文献证据分级详见同源背景解读。）

**糖基化与细胞调控**

- **O-GlcNAc（O-linked β-N-acetylglucosamine，O-连接 β-N-乙酰葡萄糖胺）：** 单个 GlcNAc 以 O-糖苷键连于 Ser/Thr 的可逆 PTM，营养/应激感应器；FG-NUPs 是后生动物中修饰最重的蛋白类群之一。本文证明它弱化 FG–FG 有效吸引、维持纳秒流动性并延缓老化。
- **OGT（O-GlcNAc transferase）：** 添加 O-GlcNAc 的酶；本文用其抑制剂 OSMI-4 降低细胞 O-GlcNAc，并用重组 OGT1+UDP-GlcNAc 体外酶法糖基化纯化 FG（10 µM FG + 1 µM OGT1 + 1 mM UDP-GlcNAc，室温 16 h）。
- **OGA（O-GlcNAcase）/Thiamet-G：** 去除 O-GlcNAc 的酶及其抑制剂；Thiamet-G 升高 O-GlcNAc。本文 Thiamet-G 几乎不再加速链段运动（多数位点 P > 0.29），说明内源修饰已"足够"——重要的负性/弱阳性限定。
- **OSMI-4：** OGT 抑制剂（本文 10 µM）；降低全局 O-GlcNAc（RL2 印迹变浅）、减慢第二 FG 域多位点链段运动并减慢核输入（P = 0.0053）。
- **RL2 抗体：** 识别 O-GlcNAc 修饰的单抗（Invitrogen MA1-072），本文以全细胞裂解液印迹读全局 O-GlcNAc 水平（Fig.4b）。
- **磷酸化对照（phosphorylation）：** 另一 FG 调控 PTM；NUP98 超磷酸化促 NPC 有丝分裂解聚（ref 54），但活细胞选择性扰动困难；本文以 O-GlcNAc 为可操作切入点（Discussion 第 3 层）。
- **YinOYang / O-GlcNAc Database v2.0：** 糖基化位点预测工具与注释数据库；本文 Martini 模型以 YinOYang 概率阈值选位点（fgly = N\_gly/N\_total，N\_total = 58,768 个 Ser/Thr），ED8a 以数据库注释第二 FG 域位点。

**背景补注：O-GlcNAc 糖基化这条研究线——在核孔上发现的营养感应器，与糖基化的"防老化"后果线**

**发现：O-GlcNAc 的出生地就是核孔。** 1980s 中期 Hart 学派最早在核孔糖蛋白上检测到末端 GlcNAc（Torres & Hart 1984, JBC；本次 EuropePMC 检索未获，卷期页码待核、书目参考提供），Holt & Hart 1986（JBC 261:8049–8057）确证这是一种新型蛋白-糖连接——O-连接 GlcNAc，即 O-GlcNAc。本文回到 FG-NUP 糖基化，正是这条线的"回乡"。

**酶学与感应：单糖基化、双酶循环。** 与分泌通路的复杂糖链不同，O-GlcNAc 是单个 GlcNAc 以 O-糖苷键连于核质蛋白 Ser/Thr 的可逆修饰，由 OGT 添加、OGA 移除：Kreppel, Blomberg & Hart 1997（JBC 272:9308–9315）克隆含多个三十四肽重复（TPR）的 OGT，Gao et al. 2001（JBC 276:9838–9845）克隆中性胞质 OGA。供体 UDP-GlcNAc 处于己糖胺生物合成通路汇合点，整合葡萄糖、氨基酸、脂肪酸与核苷酸代谢流，故 O-GlcNAc 循环被视为营养/应激感应器；其失调与癌症、神经退行（含 tau）、糖尿病/胰岛素抵抗相连（Bond & Hanover 2013, Annu Rev Nutr 33:205–229；课本级常识）。

**FG-NUP 糖基化线：本文的直接前作。** FG-NUPs 是后生动物细胞中 O-GlcNAc 修饰最重的蛋白类群之一（本文引言；Li & Kohler 2014 综述，ref 47）。两项关键前作：Labokha 2013（ref 48）系统分析 10 个爪蟾 FG 结构域水凝胶，发现 Nup98 凝胶筛分最严（阻 GFP 尺寸惰性物、容 NTF2、把 importin-β 型 NTR 阻在表面），Nup98 携带 46 个 O-GlcNAc 位点，糖基化可解除这种表面阻滞、容大 NTR·cargo 进入，且固态 NMR 显示糖基化凝胶缺乏未修饰凝胶中主导刚性区的淀粉样 β-结构——"糖基化防固化"在材料态层面已被证明；Yoo & Mitchison 2021（ref 49）用光控核输入报告子 LINuS 证明 O-GlcNAc 水平双向调节核质双向转运速率。但二者都未触及活细胞内纳秒链段动力学。

**糖基化后果属哪条线、本文如何借鉴。** 后果落在两条线的交汇处：在"材料态/老化"线上，它弱化 FG–FG 有效吸引、维持动态、防淀粉样老化（继承 Labokha 的 β-结构观察）；在"运输功能"线上，它设定选择性转运速率（继承 Yoo & Mitchison）。本文操作设计直接借鉴二者：OSMI-4 抑 OGT 降糖基化→第二 FG 域多位点链段运动减慢、核输入减慢（P = 0.0053），确立必要性；Thiamet-G 抑 OGA 升糖基化却几乎不再加速（多数位点 P > 0.29）——"内源修饰已近足够"的重要负性限定；体外酶法糖基化（OGT1+UDP-GlcNAc，质谱确认约 17 GlcNAc/链）延缓凝聚体老化，与 importin-β 联合重现活细胞 ρslow 谱（221 位点 72 ± 3 vs 59 ± 14 ns）；Martini 显式糖基化预测人源 48 位点、与爪蟾 46（ref 48）互证。疾病后果方面，FG-NUP 功能障碍与白血病 NUP98 融合癌蛋白相分离（Ahn 2021, Nature 595:591–595）、tau 破坏核质运输（Eftekharzadeh 2018, Neuron 99:925–940）、C9orf72 重复扩张（Freibaum 2015, Nature 525:129–133）及衰老相关 NPC 退化（D'Angelo 2009, ref 58）相连——本文把"糖基化+importin-β 维持类液态"提名为对抗这些病理老化的守护轴，但疾病模型检验仍属设想（跨文献证据分级详见同源背景解读）。（阅读深度：refs 48/49 为 PMC 全文定向核读级；Holt 1986/Kreppel 1997/Gao 2001/Bond 2013 为本次升级 EuropePMC 新核证书目+摘要级；Torres 1984 参考提供/待核；疾病线事实复用同源背景解读已核证内容。）

**荧光标记、成像与光学技术**

- **遗传密码扩展（genetic code expansion, GCE）/琥珀密码子抑制（amber suppression）：** 把终止密码子 TAG 重指派为non-canonical 氨基酸（ncAA）插入位点；本文在 NUP98 特定位点（如 221）插入 ncAA 实现单点标记。
- **GCE-OTO（synthetic orthogonally translating organelles-enabled GCE）：** Lemke 组建立的"合成正交翻译细胞器"策略，在膜样细胞器上分离正交翻译机器，提高 ncAA 插入效率与保真（refs 26,27）；本文活细胞标记的地基技术。
- **BCN / BOC：** BCN = bicyclo[6.1.0]nonyne-lysine，含环炔、可点击的反应性 ncAA；BOC = t-butyloxycarbonyl-L-lysine，不可点击的对照 ncAA。BOC 对照消除"染料非特异结合/自发荧光"解释（Fig.1b、ED1a）。
- **点击化学/四嗪连接（click chemistry / tetrazine ligation）：** 环炔（BCN）与四嗪染料的生物正交逆电子需求 Diels–Alder 反应；本文以此把小分子染料共价连到 ncAA 位点。
- **HD653（HDye653）：** 硅罗丹明衍生物，带自淬灭四嗪：未反应时荧光被淬灭、与 BCN 反应后点亮→免洗、低背景；短 linker 限制染料独立旋转→各向异性对链段运动敏感（ref 28）。本文活细胞 TRFA 探针。
- **Cy3B：** 刚性、光物理表征成熟的经典各向异性染料；本文体外 FG 标记探针，并作为 HD653 的验证对照（ED1c）。
- **时间分辨荧光各向异性（time-resolved fluorescence anisotropy, TRFA）：** 偏振脉冲激发后，分别记录平行/垂直偏振发射随时间衰减，r(t) = (I∥ − G·I⊥)/((1−3L2)I∥ + (2−3L1)G·I⊥)；染料随链段转动越快，r(t) 衰减越快→"液态"读数。本文核心测量。
- **ρfast / ρslow / r\_p / r\_0 / βslow：** 双指数模型 r(t) = r\_0[(1−r\_p/r\_0)e^(−t/ρfast) + (r\_p/r\_0)e^(−t/ρslow)] 中：ρfast = 染料/linker 局部运动；r\_p = 快运动后残余各向异性；ρslow = 慢组分时间尺度，本文定义为"表观链段运动度量"（apparent segmental-motion metric），**不是**精确绝对旋转相关时间；βslow = r\_p/r\_0 为慢组分相对振幅。ρslow 越小=运动越快=越液态。
- **荧光寿命/TCSPC/IRF 再卷积：** HD653 寿命约 4 ns；HydraHarp 400 以 16 ps 分辨率记录单光子到达时间（time-correlated single-photon counting, TCSPC）；仪器响应函数（IRF）每日以赤藓红 B/KI 测得并用于再卷积拟合；约 4 ns 处原始曲线的小不连续来自光路弱反射，已由再卷积处理（作者自陈）。
- **G 因子与 L1/L2 偏振混合因子：** G 校正两偏振通道探测效率差（以各向同性旋转的 [Ru(bpy)3]Cl2 测）；L1/L2 校正高 NA 物镜引起的偏振混合（以已知 ρ = 16 ns 的 YFP 全局拟合测）。二者是 r(t) 定量可信的前提。
- **FLIM–FRET（荧光寿命成像–Förster 共振能量转移）：** 以 donor 寿命缩短读 FRET 效率→链内距离/构象偏好；前作 ref 26 在透化细胞测得 NUP98 构象偏好与 R\_E，本文用作模拟校准基准，但前作不报活细胞动力学——本文 TRFA 的增量所在。
- **DNA-PAINT：** 染料标记的短 DNA"imager"链与靶上"docking"链瞬态结合产生闪烁定位点，实现超分辨；本文以 D1/D3 两套 docking/imager 顺序成像双色。
- **MINFLUX：** 以结构化激发（中心零点）定位单分子，达纳米级精度；本文用二维 MINFLUX 在固定细胞对 NUP96 与 importin-β 双色成像（n = 460 NPCs），读径向组织；前作 ref 14 用三维 MINFLUX 追踪透化细胞 cargo 轨迹。
- **纳米抗体/ALFA 标签/mEGFP：** 抗 GFP 与抗 ALFA 纳米抗体（偶联 docking 链）分别识别内源 NUP96-mEGFP 与诱导表达 importin-β-3×FLAG-ALFA；小尺寸纳米抗体降低 linkage error。
- **LINuS（light-inducible nuclear localization signal）：** 光控核输入报告子：LOV2 光氧电压域 2 的 Jα 螺旋在暗态笼蔽 NLS（NES 占优→胞质定位），蓝光使 Jα 解笼→NLS 激活→核输入；本文以 mCherry 核强度累积曲线拟合 y = 1 + (b−1)(1−e^(−kt)) 得表观输入速率常数 k（ref 49 体系）。
- **高速 AFM/FCS/FRAP 的局限：** 单分子追踪、FCS、FRAP 读整体扩散而非 tethered 链局部构象运动；AFM 只能及表面组装体（refs 3,19–21）——本文 TRFA 的方法学缺口定位。
- **bootstrap 重采样：** 单细胞各向异性曲线噪声大，本文以 200 次有放回重采样单细胞曲线、加和光子后拟合，提高信噪比与拟合稳健性；并以双侧 bootstrap 假设检验给 P 值。

**背景补注：TRFA/荧光各向异性测链段运动这条方法线——ρslow 的方法学原点**

荧光各向异性是 Perrin 与 Weber 在 1920s–1950s 确立的经典工具：偏振脉冲激发后，分子在荧光寿命期内转动使发射偏振去极化，r(t) 衰减快慢报告转动运动（课本级常识；本文 ref 32 即 Lakowicz 教科书）。对折叠蛋白它读整体翻滚；IDP 的方法学转折由 Milles & Lemke 2014（ref 31, Angew Chem Int Ed 53:7364–7367）完成：把大型 IDP 复合物的各向异性衰减分解为快组分（染料/linker 局部运动）与慢组分（链段运动），用后者映射多价性与差异亲和力——因为 IDP 的结构关联通常不超过约 50 残基（本文引 refs 31,33），慢组分读的是局部链段动力学而非整体旋转。Jain 2016（ref 33, Biophys J 111:768–774）进一步用皮秒时间分辨去偏振在单 Trp α-synuclein 变体上直接映射无序蛋白骨架扭转运动。方法的固有边界是各向异性时间窗受荧光寿命（约 ns）限制，更慢的旋转扩散须以偏振 FCS 互补（Loman 2010, ref 35），而 FRAP/FCS 读平移扩散、AFM 只及表面——这正是本文对单分子追踪/FCS/FRAP/AFM 的方法学缺口定位。本文的继承：GCE-OTO 单点 BCN 插入 + fluorogenic HD653 短 linker（ref 28，限制染料独立旋转）+ TCSPC 16 ps 单光子记录 + 200 次 bootstrap 重采样，把 ρslow 明确定义为"表观链段运动度量"而非绝对旋转相关时间——15 位点活细胞扫描是这条方法线首次系统落到活细胞内 tethered IDP 上。（阅读深度：ref 31 为摘要+本文转述级；refs 33/35 复用同源背景解读 B.5 已核证内容。）

**背景补注：MINFLUX 开发史——从诺奖背景到核孔径向组织的纳米级成像**

**背景与开创。** MINFLUX 的概念背景是超分辨荧光显微——Hell 因 STED 等获 2014 年诺贝尔化学奖（与 Betzig、Moerner 共享，课本级常识）。MINFLUX 由 Hell 组提出：Balzarotti, Eilers et al. Science（2016-12-22 在线/2017 卷期 355:606–612）引入"最小光子通量"定位——用中心强度为零的结构化激发图案（donut），把零点迭代瞄准单分子位置，以极少光子数推断发射体位置，融合 STED 的图案化激发与单分子定位（PALM/STORM）两类概念，达约 1 nm 定位精度、光子需求较相机定位降低约 22 倍（详见同源背景解读，已核证）。

**演进。** Gwosch et al. Nat Methods 2020（17:217–224，2020-01-13 在线）把 MINFLUX 推进到细胞内 3D、多色纳米级分辨成像；技术已由 Abberior Instruments 商业化（本文 Methods 即商用 MINFLUX/Olympus IX83 平台）。它与 DNA-PAINT 是互补而非竞争：DNA-PAINT 以 imager/docking 链瞬态结合提供单分子闪烁，MINFLUX 给每次闪烁以纳米级定位精度——本文双色成像正是"DNA-PAINT 闪烁 + MINFLUX 定位"的组合。孔内径向密度峰距孔中心仅约 20 nm，分辨这种孔内径向组织需要纳米级定位精度，这是常规 DNA-PAINT（精度约 10–20 nm，课本级常识）难以胜任的（基于两种方法精度量级的推断）。

**核孔应用线与国内落地。** 把 MINFLUX 带进核孔的线：Chowdhury, Sau & Musser 2022（ref 42, Nat Cell Biol 24:112–122）实现 cargo 穿核孔的超分辨 3D 追踪；Sau 2025（ref 14, Nature 640:821–827）在透化细胞以双色 3D MINFLUX 同时追踪输入/输出，发现转位复合物偏好约 40–50 nm 直径环带（2678 轨迹/48603 定位，详见同源背景解读）——即本文径向组织要解释的"环周偏好轨迹"。国内方面，唐爱辉（Tang A-H）组把 MINFLUX 带进中国（USTC/合肥综合性国家科学中心人工智能研究院，从 2016 年 Nature 跨突触纳米柱走向核孔成像；作者谱系详见同源背景解读），本文作者贡献声明为"contributed MINFLUX expertise and resources"。

**最终如何落实到本研究（Fig.3f,g、Fig.5）。** 固定 U-2 OS 细胞，内源 NUP96-mEGFP 作支架参考通道 + 强力霉素诱导 importin-β-3×FLAG-ALFA（总 KPNB1 近内源），抗 GFP/抗 ALFA 纳米抗体偶联 docking 链（降低 linkage error），D1/D3 两套 imager 顺序双色二维 MINFLUX（顺序成像+链交换约 4 h/样），250 nm 金颗粒基准标记主动漂移校正（亚纳米横向稳定）；n = 460 NPCs，以 NUP96 定位点定义孔中心与八重参考系（z8 = ⟨e^(i8θ)⟩ 对齐），importin-β 径向 bin + 环面积校正 + 归一化 + 平滑 + 旋转对称化，并以同流程处理的 2D 均匀随机零模型排除几何伪影——得到约 20 nm 环周密度峰与中央 depletion，直接验证模拟的"importin-β 环周、FG 中央"径向组织并支撑双路线假说。边界：固定细胞（可能锁定状态）、2D 投影（丢轴向信息）、NUP96 参考未解析内环直径（不能排除 NPC 扩张/收缩影响）——活细胞 3D 追踪是下一步（详见同源背景解读 B.4）。（阅读深度：Balzarotti 2016/2017 作者串与 Gwosch 2020 为本次升级 EuropePMC 新核证书目+摘要级；ref 14 为全文精读级、ref 42 为摘要级；Tang 谱系复用同源背景解读已核证内容。）

**模拟、统计与数据**

- **残基级粗粒化模型（residue-level coarse-grained model）：** 每个氨基酸一 bead、核被膜为固定膜粒子、溶剂隐式；Lennard-Jones 强度 ε~ 参数化（FG–FG 在 NPC 内 0.42、孤立链/bulk 凝聚体 0.5；FG–Imp-β 0.42），FENE 键（k\_FE = 30 k\_BT, R\_FE = 1.5σ），σ = 0.6 nm；LAMMPS 运行。本文用于 importin-β 分配、溶胀、径向组织与通量。
- **Martini 2.2 近原子粗粒化模型：** 约 4 重原子一 bead 的化学细节力场，可显式挂糖；本文以 α（蛋白–蛋白）、λ（蛋白–糖）、γ（糖–糖）重缩放相互作用（α = 0.78 为 bulk 最优、λ = 0.15、γ = 0.5），GROMACS 运行，显式 O-GlcNAc 四水平（fgly = 0/0.18/0.3/0.6）。
- **键矢量自相关（bond-vector autocorrelation）：** ⟨b\_i(t0+t)·b\_i(t0)⟩ 读相邻残基键取向松弛，是模拟端与 TRFA 链段运动对应的量；双指数拟合给 τfast/τslow。
- **MSD/扩散系数 D/首通时间（mean first-passage time）：** 均方位移线性区斜率给 D；本文以凝聚体内 importin-β 的 D 估算穿越 NPC 的首通时间（1–10 ms），与实验核转运速率吻合。
- **分配系数（partition coefficient）：** c\_dense/c\_dilute；本文模拟外推无限稀释极限得 ε~ = 0.40 时 16.5 ± 6、0.42 时 1120 ± 364，与蛋白质组学估的 NPC 内 400–1300 对照以锁定 ε~ = 0.42。
- **Welch t 检验/Holm 校正/bootstrap 假设检验：** 核输入速率常数比较用双侧 Welch t + Holm 多重校正（Fig.4f）；活细胞 TRFA 条件比较用双侧 bootstrap 检验（Fig.4a,c）；体外 TRFA 为 n = 3 独立重复 mean ± s.d.。
- **LAMMPS/GROMACS/VMD/PAM-TauFit：** 模拟引擎（LAMMPS 2021Sep、GROMACS 2020.6/2025.2）、可视化（VMD 1.9.3）与荧光拟合框架（PAM v1.4 的 TauFit，2\_exp\_rot 模型）；MINFLUX 分析用 MATLAB R2024a 改编 MINFLUX\_NPC\_Tracking 流程。
- **PDB 7R5K / 3W5K / Zenodo：** 人源收缩态 NPC 支架结构（ref 39）与 importin-β 结构（ref 73）；模拟初始构型与轨迹存 Zenodo（10.5281/zenodo.15025565 LAMMPS；10.5281/zenodo.17588507 GROMACS，CC BY 4.0）。

---

二、<核心问题与方案>

**生物学问题（原文表述）：**

- "How this functional barrier forms inside the nanochannel of the NPC remains unresolved."（引言第 1 段末）——功能性屏障如何在 NPC 纳米通道内形成仍未解决。
- "Direct measurements of local FG-NUP conformational dynamics inside living NPCs remain challenging."（引言第 2 段首）——活 NPC 内局部 FG 构象动力学的直接测量仍困难。
- "Whether the native barrier is predominantly liquid-like or more solid-like therefore remains debated."（引言第 2 段末）——天然屏障偏液态还是偏固态因此仍有争议。
- "Our previous FLIM–FRET measurements defined conformational preferences of FG-NUPs in permeabilized cells but did not directly report dynamics in live NPCs."（引言第 3 段）——前作只给透化细胞构象偏好，未给活细胞动力学。
- "…raising the important question of what physiological factors prevent FG-NUPs from maturing into a gel-like state in their native environment."（Results 第 3 节末）——什么生理因素阻止 FG-NUPs 在原位成熟为凝胶态。

**背景矛盾（研究切入点）：** 矛盾双方：一方是体外重构体系（饱和 FG 水凝胶、老化凝聚体、淀粉样 NMR/cryo-EM 证据，refs 4,5,11–13）指向"固体/凝胶屏障"；另一方是活细胞功能需求（毫秒级 cargo 穿越需数千次瞬态 FG–NTR 接触的快速交换，refs 24,25）与单分子/AFM 动态观察（refs 3,19–21）指向"动态液态屏障"。隐含假设是"体外凝聚体的材料态可外推到活细胞 NPC"。本文切入点：绕过该假设，直接在活细胞内以单点标记+皮秒 TRFA 测 tethered FG 链的纳秒链段运动（而非整体扩散或静态构象），并把体外体系作为"会老化的对照"而非"天然屏障的等价物"；再追索"细胞内什么因素维持液态"，锁定 importin-β 与 O-GlcNAc 两个可扰动因子，并以实验匹配的多尺度模拟把材料态与空间组织统一。

**解决方案（技术路线）：**

- **模型系统：** 活 COS-7 细胞（GCE-OTO 标记 NUP98 15 位点）；固定 U-2 OS-CRISPR-NUP96-mEGFP + 强力霉素诱导 importin-β-3×FLAG-ALFA 细胞（双色 DNA-PAINT MINFLUX）；纯化人 NUP98 FG(1–505, ΔGLEBS) 体外凝聚体（±importin-β、±酶法 O-GlcNAc）；残基级粗粒化 NPC 模型（LAMMPS）与 Martini 2.2 显式糖基化 NPC 模型（GROMACS，几何取 PDB 7R5K）。选 COS-7 因转染/标记效率高、核 rim 清晰；选 U-2 OS 敲入系因内源 NUP96 提供八重参考系；选 NUP98 因其 vital、重糖基化、且含聚集倾向段 85–124 可作敏感报告位点。
- **实验设计：** (1) 15 个 BCN 位点横跨 1st/2nd FG（36,67,100,136,151,221,251,283,312,338,362,387,426,458,482），HD653 标记活细胞 TRFA，n = 41–69 细胞/位点、3 次独立实验；(2) BOC 不可点击对照 + SiR-tz/JF646-tz 染料对照（ED1a）+ 内源 importin-β 免疫荧光确认标记不扰动定位（ED1b）+ EGFP-BCN39 的 HD653/Cy3B 水动力半径验证（ED1c）；(3) 活细胞 2 h 时间窗稳定性（Fig.1i, n = 54, 5 次实验）vs 体外凝聚体 1 h 成熟（Fig.1j, n = 3）+ ThT 染色；(4) importin-β 共相分离摩尔比 1:1/1:2/1:4 与"成熟 1 h 后补加"对照（Fig.2e）；(5) 10 µM Thiamet-G / OSMI-4 扰动 O-GlcNAc（RL2 印迹验证）+ OSMI-4 背景下 importin-β 过表达回补（Fig.4c）；(6) LINuS 核输入速率（n = 67/69/105/88 细胞）；(7) 体外酶法糖基化（质谱确认约 17 GlcNAc/链）±importin-β 共相分离（25 µM 糖基化 FG + 10 µM importin-β）；(8) MINFLUX n = 460 NPCs 径向密度 + 2D 随机零模型对照。
- **功能验证：** 必要性——OSMI-4 降 O-GlcNAc 减慢链段运动与核输入（确立 O-GlcNAc 维持动态/功能的必要性）；充分性/回补——糖基化+importin-β 体外重现活细胞 ρslow 谱（72 ± 3 vs 59 ± 14 ns）、importin-β 过表达部分回补 OSMI-4 表型（确立两因子联合的充分性与 modulatory 角色）；区分竞争解释——BOC 对照排除非特异染料信号；Thiamet-G 弱效排除"内源修饰不足"解释；"成熟后补加 importin-β 无效"排除"importin-β 可逆液化任何状态"的过强解释；2D 随机零模型排除"径向几何本身造成中央 depletion"的几何解释。
- **机制解析：** 从"活细胞液态 vs 体外老化"的现象对比 → 单因子（importin-β 或糖基化）体外延缓老化 → 双因子联合重现活细胞谱 → 模拟机制（importin-β 稀释 85–124 接触、溶胀凝聚体；糖基化弱化 FG–FG 有效吸引、使链伸展入中央）→ 空间组织（ε~ 匹配下 importin-β 偏环周、FG 占中央；ε~ ±20% 破坏组织）→ 功能闭环（首通时间 1–10 ms、通量在 ε~ ≈ 0.40–0.42 达峰、O-GlcNAc/importin-β 扰动改变核输入）。

**验证层级：** 活细胞链段运动基线（Fig.1e–g）→ 体外老化对照与位置敏感性（Fig.1h–j, 2c）→ importin-β 剂量依赖液化与不可逆性限定（Fig.2a–e）→ 模拟稀释/溶胀机制（Fig.2f,g, ED3）→ 分配/扩散/通量参数化与最优亲和力（ED4–6）→ 径向组织预测与 MINFLUX 验证（Fig.3, ED7）→ O-GlcNAc 细胞扰动+功能读数+回补（Fig.4a–f）→ 体外糖基化±importin-β 重现活细胞谱（Fig.4g–i, ED8f）→ Martini 显式糖基化构象/动力学/临界点（Fig.5, ED9）。

**统计与生信框架（Methods 要点）：** 活细胞 TRFA 以 200 次 bootstrap 重采样加和光子后以 TauFit 2\_exp\_rot 模型再卷积拟合；ρslow 接近拟合上限 1000 ns 判为"极慢、未定量解析"；条件比较用双侧 bootstrap 假设检验（P = null 重采样中绝对差 ≥ 观测效应的比例），百分位置信区间；Fig.1i 逐细胞拟合读时间趋势；体外 TRFA 每 5 min 分析、n = 3 独立重复 mean ± s.d.；核输入速率常数用双侧 Welch t + Holm 校正；MINFLUX 以几何 QC 选孔、八重序参量 z8 = ⟨e^(i8θ)⟩ 对齐、径向 bin + 环面积校正 + 归一化 + 平滑 + 旋转对称化，并以同流程处理的 2D 均匀随机零模型对照；模拟重复数/轨迹块按收敛与复现性选定（如 ED3/4 n = 45,000 snapshots、Fig.5e n = 400 snapshots/4×150 ns 块、Fig.2g n = 300 snapshots）。样本量非正式功效计算而基于经验（Reporting Summary 自陈）；无随机化、无盲法（自陈）。**原文未提供 GEO/公共测序 accession（本研究以成像、生化与模拟数据为主，无高通量测序数据）**；结构取自 PDB 7R5K/3W5K；模拟轨迹存 Zenodo（见概念注释）；O-GlcNAc 位点注释取 O-GlcNAc Database v2.0；未裁剪印迹见 Supplementary Fig. 20（未提供）。

---

三、<逐节精读>

本节按原文 7 个 Results 小标题逐一展开：每节先给完整"内容逻辑"叙事，随后以"→ Figure X"嵌入该节关联主图的四字段解读；Extended Data 图按其内容角色在对应节内以"→ Extended Data Fig. X"嵌入，平行 panel 合并条目但逐 panel 说明差异；未提供的 Supplementary 图/视频以括注标明内容角色。

**Section 1：Site-specific labelling of NUP98 in live cells（活细胞 NUP98 的位点特异标记）**

内容逻辑：本节回答全文的方法学前提——能否在活细胞内以"单点精度、不扰动蛋白行为"的方式给 FG-NUP 装上各向异性探针。作者继承前作 GCE-OTO 遗传密码扩展（refs 26,27），把琥珀密码子 TAG 重指派插入环炔 ncAA BCN，再经四嗪点击连接小分子染料；但前作以多种活细胞染料标记 NUP98 时信噪比低、限制测量精度（ref 26），故本节改用新开发的硅罗丹明 HD653：其四嗪自淬灭、与 BCN 反应后才点亮，从源头压低未反应/非特异染料背景，且短 linker 限制染料独立旋转、使各向异性对链段运动敏感（refs 28,29）。验证链有三环：其一，NUP98A221TAG 在 COS-7 表达后与 HD653 反应给出清晰核 rim 信号（Fig.1b），而不可点击 BOC 对照信号消失——排除"染料非特异吸附/自发荧光"解释；其二，ED1a 以 SiR-tz 与 JF646-tz 两种染料重复 BCN/BOC 对照，ED1b 以抗 KPNB1 免疫荧光确认点击标记后内源 importin-β 仍定位核被膜——排除"标记扰动 NPC 组成"解释；其三，ED1c 以已知旋转性质的球状 EGFP（BCN39）分别标 HD653 与经典各向异性染料 Cy3B，TRFA 拟合水动力半径与野生型 EGFP 一致（约 2.78–2.79 nm）——确立 HD653 作为各向异性探针的定量可信性。本节贡献是把"活细胞单点 TRFA"从概念变为可执行、已验证的测量平台，为 Section 2 的 15 位点扫描埋下伏笔；其分寸在于只验证了探针与标记，尚未给出任何动力学结论。

→ Figure 1 标题为 "Site-specific labelling and segmental dynamics of NUP98 in live cells and in vitro"，旨在建立活细胞/体外 FG 链段运动的测量平台与基线。由 a 至 j 共 10 部分构成：a 标记策略示意、b 标记验证、c TRFA 原理示意、d 位点图谱、e/f 两 FG 域代表衰减、g 15 位点 ρslow 谱、h 三态衰减对比、i 活细胞稳定性、j 体外老化，形成"标记→原理→基线→体内外对比"的证据链。

(A) GCE-OTO 位点标记示意
图片解释：示意图展示含 UAG（橙）的 NUP98 mRNA 经 GCE-OTO 翻译出带 ncAA（黄星）的 NUP98 链（灰珠），有丝分裂后 NPC 重装、NUP98 dock 入支架（淡紫），再与可点击活细胞染料（红色硅罗丹明-四嗪结构式）反应得位点标记 NUP98（红染料连黄星）。无定量数据（示意）。
横纵轴定义：无坐标轴（流程示意）。阅读方向：从左至右为"mRNA→ncAA 蛋白→NPC 重装→点击标记"。
颜色含义：橙 = UAG 密码子；黄星 = ncAA/标记位点；灰珠 = NUP98 链；淡紫 = NPC 支架；红 = HD653 染料。
核心结论：单点精度标记可在 NPC 功能态内完成（策略改编自 ref 26）。

(B) BCN vs BOC 标记验证
图片解释：COS-7 表达 NUP98A221TAG 后与 HD653 反应的荧光显微图：BCN 行见清晰核 rim 环状信号，BOC 行几乎全黑。代表性图像，独立重复 ≥3 次；原文未提供定量灰度/信噪比数值。标尺 10 µm。
横纵轴定义：无坐标轴（荧光显微图）。阅读方向：上下两行对比同一细胞区域的 rim 信号有无。
颜色含义：灰度荧光，越亮 = 标记越多；上 = BCN（可标记）、下 = BOC（对照）。
核心结论：信号依赖可点击 ncAA，排除非特异染料背景（另见 ED1a,b 染料与定位对照）。

(C) TRFA 原理示意
图片解释：偏振激发（红竖直箭头）下，"更动态"链（灰链+红染料，旋转箭头）使发射去偏振（红箭头各向）、"较不动态"链保持偏振（竖直箭头）；中为 r(t) 衰减示意：蓝曲线（less dynamic）含慢组分 ρslow、红曲线（more dynamic）衰减快，快组分 ρfast 归染料局部运动；右为 ρslow 箱式示意：Sample 1 低 = fast motion、Sample 2 高 = slow motion。
横纵轴定义：中图横 = 时间、纵 = 各向异性（无单位刻度，示意）；右图横 = 样品、纵 = 表观 ρslow (ns)。阅读方向：衰减越快/ρslow 越低 = 链段越动态。
颜色含义：红 = 偏振光/更动态样品；蓝 = 较不动态样品；灰 = FG 链；红点 = 染料。
核心结论：ρslow 被定义为"表观链段运动度量"而非绝对旋转时间——全文读数的操作定义（Methods 式 5–6）。

(D) 15 个标记位点图谱
图片解释：NUP98 线性域图：1st FG（橙，1–157）、GLEBS（灰，157–214）、2nd FG（橙，214–505）、切割位点（虚线）、Anchor（紫，595–863）、C 端（863–920）；红色"棒棒糖"标 15 个 BCN 位点分布于两 FG 域。
横纵轴定义：无坐标轴（线性域图），横 = 残基序号 1–920。阅读方向：左 = N 端（伸向孔中心）、右 = 锚定端。
颜色含义：橙 = FG 域；灰 = GLEBS/连接区；紫 = Anchor；红棒棒糖 = 标记位点。
核心结论：位点扫描覆盖"中心伸展区→锚定区"全梯度，使位置依赖动力学可测。

(E)(F) 第一/第二 FG 域代表 TRFA 衰减（合并解读）
图片解释：e 为 1st FG 五位点（36 深红、67 红橙、100 橙、136 黄橙、151 黄）活细胞 TRFA 散点衰减；f 为 2nd FG 十位点（221 黄→482 紫的绿-蓝-紫渐变）衰减。各曲线自 r ≈ 0.35–0.4 快速初衰后进入慢平台；e 平台约 0.23–0.26、f 约 0.23–0.27。定量：拟合 ρslow 57 ± 2 至 108 ± 5 ns（见 g）。
横纵轴定义：横 = 时间 (ns)，0–15；纵 = 各向异性 r(t)，0–0.4。阅读方向：曲线平台越高/慢衰越慢 = 链段越受限；比较同图各色曲线平台与慢衰斜率。
颜色含义：逐位点配色（e 红→黄；f 黄→绿→蓝→紫），与 g 箱图同色系对应位点。
核心结论：活细胞 FG 链在纳秒尺度存在可分辨的慢链段组分，且两 FG 域行为不同（为 g 的位置梯度铺垫）。

(G) 15 位点表观 ρslow 谱
图片解释：箱图（中线 = 中位数、中方 = 均值、箱 = IQR、须 = 1.5×IQR 内数据）横排 15 位点，151 与 221 间有轴断点；1st FG 位点 ρslow 约 75–85 ns，2nd FG 自 221 约 57 ns 渐升至 362–482 约 104–108 ns。n = 41,44,45,45,44,58,69,60,57,46,42,47,57,43,53 细胞（左至右），3 次独立实验；200 bootstrap 重采样拟合。
横纵轴定义：横 = 标记位点（残基号，N→C）；纵 = 表观 ρslow (ns)，40–140。阅读方向：从左到右 = 从孔中心伸展区到锚定区；值越低 = 越快 = 越液态。
颜色含义：与 e/f 同色系逐位点渐变（红→黄→绿→蓝→紫），无额外通道含义。
核心结论：存在位置梯度——近 N 端（伸向孔中心）链段更快、近锚定域更受限，与 tethering/confinement 预期一致（refs 3,34）；这是"活细胞 FG 呈类液态链段运动"的核心基线。

(H) 残基 221 三态衰减对比
图片解释：同一标记位点 221 在三种环境的 r(t)：紫 = 溶液孤立 FG 链（10 nM，衰减最快至约 0.05）、橙 = 活细胞 NPC（平台约 0.24）、绿 = 新形成 FG 凝聚体（平台最高约 0.28–0.30）。
横纵轴定义：横 = 时间 (ns) 0–15；纵 = 各向异性 0–0.4。阅读方向：比较三条曲线慢平台高度与衰减速度：溶液 < NPC < 凝聚体（受限程度）。
颜色含义：紫 = in solution；橙 = in the NPC；绿 = in condensate（图例明示）。
核心结论：活细胞 NPC 内链段运动介于自由链与体外凝聚体之间——既非完全自由也非固化，且更接近"动态"端；为 Section 3 的老化对比设基线。

(I) 活细胞 2 h 稳定性
图片解释：残基 221 逐细胞 ρslow 随成像时间（0–120 min）散点，围绕约 59 ns 虚线平稳波动（约 40–80 ns），无上升趋势。n = 54 细胞、5 次独立实验。
横纵轴定义：横 = 时间 (min) 0–120；纵 = 表观 ρslow (ns) 0–300+。阅读方向：看散点是否随时间上漂（上漂 = 固化）；此处平稳。
颜色含义：橙散点 = 单细胞拟合值；橙虚线 = 趋势/均值参考。
核心结论：活细胞 FG 链段运动在 2 h 窗内稳定——与 j 的体外老化形成全文核心对比。

(J) 体外凝聚体 1 h 液-固转变 + ThT
图片解释：残基 221 凝聚体 ρslow 随成熟时间自约 100 ns 单调升至约 250–260 ns（mean ± s.d., n = 3）；顶部白→绿渐变箭头条标注 "Liquid-like → Solid-like"；插图为 ThT 染色 5/20/40/60 min：5 min 几乎无信号、60 min 强黄色液滴状荧光（标尺 10 µm）。
横纵轴定义：横 = 成熟时间 (min) 0–60；纵 = 表观 ρslow (ns) 0–300+。阅读方向：随时间上升 = 链段越来越慢 = 液→固；插图随时间变亮 = 淀粉样结构涌现。
颜色含义：绿散点/误差棒 = ρslow 均值±s.d.；渐变条 = 材料态从液到固；插图黄荧光 = ThT 结合淀粉样结构。
核心结论：体外 FG 凝聚体发生时间依赖液-固转变并伴淀粉样化（与 ref 4 老化观察一致），而活细胞无此转变——提出"什么生理因素维持液态"的核心问题（Supplementary Video 1 记录该过程，未提供）。

→ Extended Data Fig. 1 标题为 "Validation of site-specific labelling and TRFA for NUP98 dynamics in cells and in vitro"，旨在为 Section 1–3 提供标记/探针/参数对照。由 a 至 e 共 5 部分。

(A) 两种染料的 BCN/BOC 对照
图片解释：2×2 灰度荧光图：行 = SiR-tz、JF646-tz；列 = BCN（可标记，见核 rim 环）/BOC（不可标记，rim 消失、仅胞质 puncta 背景）。标尺 10 µm；代表性图像 ≥3 次重复。
横纵轴定义：无坐标轴（荧光显微图）。阅读方向：同行左右对比 rim 有无；同列上下对比染料种类。
颜色含义：灰度荧光亮度 = 染料标记量。
核心结论：rim 信号依赖可点击 ncAA 而非染料种类，HD653 结论可推广。

(B) 标记后内源 importin-β 定位
图片解释：左 = NUP98-HD653 灰度 rim；右 = 抗 KPNB1/Alexa488 免疫荧光（青绿）rim，二者均呈核被膜环状。标尺 10 µm。
横纵轴定义：无坐标轴（双通道荧光图）。阅读方向：左右对比同一核的 rim 共定位。
颜色含义：灰 = HD653-NUP98；青绿 = 内源 importin-β。
核心结论：点击标记不扰动内源 importin-β 的 NPC 定位——排除标记伪影。

(C) HD653 vs Cy3B 水动力半径验证
图片解释：EGFP（BCN39）分别标 Cy3B 与 HD653 的 TRFA 水动力半径箱图：Cy3B 约 2.79 nm、HD653 约 2.78 nm，n = 4 独立重复散点叠加；上方为 EGFP β-桶结构示意带染料星。
横纵轴定义：横 = 染料种类；纵 = 水动力半径 (nm) 2.6–3.0。阅读方向：两箱是否与野生型 EGFP 已知半径一致。
颜色含义：橙箱 = Cy3B；红/粉箱 = HD653；蓝桶 = EGFP 结构；星 = 染料。
核心结论：HD653 不改变球状蛋白旋转扩散→是可靠各向异性探针（式 8 由 ρslow 反推 R\_h）。

(D) 全位点 TRFA 参数汇总（5 行合并解读）
图片解释：五行箱图横排 15 位点：稳态各向异性 r\_ss（约 0.27–0.29）、基本各向异性 r\_0（约 0.34–0.37）、残余各向异性 r\_p（约 0.27–0.30）、局部旋转 ρfast（约 0.15–0.35 ns）、慢组分相对振幅 βslow（约 0.78–0.84）。样本量/统计同 Fig.1g。
横纵轴定义：横 = 位点；纵依次为 r\_ss、r\_0、r\_p（无单位）、ρfast (ns)、βslow（无单位）。阅读方向：逐行看参数随位点的变化幅度（均较平稳，说明 ρslow 差异非探针光物理伪影）。
颜色含义：与 Fig.1g 同色系逐位点渐变。
核心结论：光物理参数跨位点稳定，ρslow 的位置梯度反映真实链段动力学差异。

(E) 五位点三态衰减（合并解读）
图片解释：残基 36、100、312、387、482 各一面板，三色衰减：紫 = 溶液、橙 = NPC、绿 = 新凝聚体；所有位点均呈"溶液最快、NPC 居中、凝聚体最慢"层级。
横纵轴定义：横 = 时间 (ns) 0–15；纵 = 各向异性 0–0.4。阅读方向：每面板内比较三色平台/衰速。
颜色含义：紫/橙/绿 = solution/NPC/condensate（图例）。
核心结论：Fig.1h 的三态层级是位点普适的，非 221 特例。

**Section 2：Segmental motion of NUP98 in live cells（活细胞 NUP98 的链段运动）**

内容逻辑：本节把 Section 1 的平台转化为全文第一个实质性结论：活细胞 NPC 内 FG 结构域呈纳秒级类液态链段运动，且存在空间梯度。作者以 15 位点扫描（Fig.1d–g）系统采集 TRFA，拟合慢组分得 ρslow 57 ± 2 至 108 ± 5 ns；关键推理是"ρslow 读什么"：因 HD653 寿命仅约 4 ns，慢于寿命的组分不能直接被荧光衰减分辨，须靠模型拟合估计，故作者明确把 ρslow 定义为表观链段运动度量、只作相对比较（Methods 式 5–6、refs 63,64）；又因 IDP 结构关联长度通常 ≤50 残基（refs 31,33），该读数主要反映局部链段而非整链运动。竞争性解释的鉴别在于：若信号来自染料独立旋转或整体蛋白旋转，则 ρfast/水动力半径对照（ED1c,d）应异常，而实际光物理参数跨位点平稳；若 FG 在细胞内已固化，则 ρslow 应接近拟合上限且随时间上漂，而实际为 57–108 ns 且 2 h 稳定（Fig.1i）。位置梯度（N 端快、锚定端慢）与"近支架 tethering 更强 confinement"的既往观察一致（refs 3,34），把动力学读数锚定到 NPC 几何。作者同时诚实划定边界：微秒尺度运动需偏振 FCS 等互补技术（ref 35），本文不覆盖。本节贡献是确立"活细胞 FG = 动态液态链段网络"的直接实验基线，并以梯度暗示空间组织问题，为 Section 5 的径向组织埋下伏笔。

→ Figure 1（e–g 已在本节引用，四字段见 Section 1；此处不重复）。本节核心数据即 Fig.1e–g 与 ED1d：ρslow 57 ± 2–108 ± 5 ns、n = 41–69 细胞/位点、3 次独立实验、200 bootstrap；位置梯度与 2 h 稳定性（Fig.1i）共同支撑"类液态"结论。补充图角色：Supplementary Figs. 1–2 提供各位置衰减与 bootstrap 深度收敛分析（未提供）。

**Section 3：Segmental motion of FG domains in vitro（体外 FG 结构域的链段运动）**

内容逻辑：本节设置全文的"对照世界"：纯化 NUP98 FG 在溶液与凝聚体两态的 TRFA。推理链：若体外凝聚体是天然屏障的等价物，则其链段运动应与活细胞相近且稳定；实测新形成凝聚体（前 5 min）ρslow 与活细胞相近，但 1 h 内单调升至约 250–260 ns（残基 221），ThT 由阴转阳（Fig.1j），即发生液-固转变/分子老化——与 ref 4 的 FG 凝聚体老化、refs 12,36 的淀粉样 NMR/EM 观察一致。位点扫描（Fig.2c）显示所有测试位点随成熟变慢，其中残基 100 最敏感：它正落在 NMR 鉴定的聚集倾向段 85–124（ref 11），故"最慢位点=最易聚集段"不是离群而是机制自洽。竞争性解释鉴别：解释 A"体外老化是 FG 的本征命运、细胞内亦然"被 Fig.1i 的 2 h 稳定否定；解释 B"老化只是染料/光物理伪影"被 ThT 独立结构读数与多位点一致性否定。由此本节把矛盾 sharpen 为"为什么细胞内不老化"，直接引出 Section 4–6 的因子追索。本节贡献是确立体外体系的"会老化"属性，从而剥夺其作为天然屏障等价物的资格，并给出残基 100 这一敏感报告位点。

→ Figure 1（h–j 四字段见 Section 1）。本节另首引 Fig.2c（六位点老化时间 course，四字段见 Section 4）：残基 100 约 15–20 min 即达拟合上限 1000 ns，36/312/387/482 约 30–45 min 达上限，221 最慢仅升至约 250 ns——位置敏感性与 85–124 聚集倾向对应。补充角色：Supplementary Video 1 记录凝聚体成熟（未提供）。

**Section 4：Importin-β tunes segmental motion of NUP98（importin-β 调控 NUP98 链段运动）**

内容逻辑：本节追索第一个生理液化因子。立论依据：importin-β 在 NPC 处丰度达毫摩尔级（ED2a 自由染料滴定：100 µM 自由 AF488 下 rim 仍可辨、1 mM 时被淹没）、结合 FG motifs、且被提出具伴侣样性质（refs 36–38）。体外共相分离实验显示剂量依赖效应：importin-β:FG 从 1:1 到 4:1，凝聚体变大、变"稀"（Fig.2a 同强度标尺下亮度下降）、残基 221 ρslow 从 120 ± 24 ns 降至 80 ± 7 ns，向活细胞值 59 ± 14 ns 靠近（Fig.2b,d）；效应跨所有测试位点包括聚集倾向段内的 100（ED2f–j），提示 importin-β 普遍削弱分子间 FG–FG 接触而非位点特例。关键限定（负性结果）：凝聚体成熟 1 h 后再补加 importin-β 不能恢复液态（Fig.2e，100 已钉在 1000 ns 上限、221 仅微升）——说明 importin-β 是"延缓/预防老化"而非"逆转固化"，防止把其夸大为通用解聚酶。机制由残基级模拟给出：以实验分配数据参数化得 ε~FG–Imp-β = 0.42（ED3e 灰带约束 0.4 < ε~ < 0.5；ED4c 外推分配系数 1120 ± 364 落在蛋白质组学估的 400–1300 带内），该值同时等于 NPC 内 FG–FG 强度 0.42、弱于 bulk 所需 0.5；模拟中 importin-β 进入凝聚体使其溶胀（Fig.2f）、并把 85–124 段局部密度稀释至纯凝聚体的约 0.8→0.3（Fig.2g，15 nm 探针球、n = 300 snapshots）——"稀释+统计分离淀粉样倾向段"为延缓老化提供机制解释。本节贡献是确立 importin-β 的链段级液化作用与其不可逆性边界，并把相互作用强度锁定到实验匹配值，为 Section 5 的空间组织模拟提供参数地基。

→ Figure 2 标题为 "Importin-β enhances FG-domain dynamics and stabilizes liquid-like states"，旨在证明 importin-β 剂量依赖液化 FG 凝聚体并给出模拟机制。由 a 至 g 共 7 部分，形成"形态→动力学→位点普适→不可逆限定→模拟机制"的证据链。

(A) 共相分离形态（剂量依赖）
图片解释：四幅同强度标尺灰度共聚焦图：NUP98 only（小而亮液滴）、1:1（较大较暗）、1:2（更大更暗）、1:4（大而融合、最暗）——亮度下降 = 局部 FG 浓度下降 = 溶胀。标尺 10 µm；代表性图像 ≥3 次重复；原文未提供定量灰度。
横纵轴定义：无坐标轴（荧光显微图）。阅读方向：左→右 = importin-β 剂量递增；比较液滴尺寸与亮度。
颜色含义：灰度 = FG 荧光强度（越亮 = FG 越浓）。
核心结论：importin-β 使凝聚体溶胀、FG 局部浓度降低——液化的形态学证据。

(B) 1 h TRFA 衰减族（剂量依赖）
图片解释：四面板（only/1:1/1:2/1:4）各含 5–60 min 每 5 min 一条 r(t)（配色 5 min 深紫→60 min 黄）：only 面板晚时点曲线平台明显高于早时点（变慢）；加 importin-β 后各时点曲线几乎重合（稳定）。纵 0.22–0.38。
横纵轴定义：横 = 时间 (ns) 0–15；纵 = 各向异性。阅读方向：面板内比较早/晚时点曲线分离程度（分离 = 老化）；面板间比较分离是否被 importin-β 压制。
颜色含义：紫→蓝→绿→黄 = 成熟时间 5→60 min（图例逐时点）。
核心结论：importin-β 压制凝聚体的时间依赖变慢——液化的动力学证据。

(C) 六位点老化时间 course（NUP98 only）
图片解释：ρslow vs 0–60 min，六色：36 蓝方、100 粉红圆、221 绿三角、312 紫倒三角、387 黄菱、482 灰左三角；100 约 15–20 min 达上限 1000 ns（灰虚线 "Upper fit bound"），其余 30–45 min 达上限，221 仅至约 250 ns。mean ± s.d., n = 3。
横纵轴定义：横 = 成熟时间 (min)；纵 = 表观 ρslow (ns) 0–1000。阅读方向：上升越快 = 该位点越易固化；触顶 = 极慢、未定量解析（非精确 1000 ns）。
颜色含义：逐残基配色（图例）；灰虚线 = 拟合上限。
核心结论：老化是位点普适但敏感度不同，100（85–124 段）最敏感——与 ref 11 聚集倾向自洽。

(D) 共相分离下六位点时间 course
图片解释：同 c 位点/配色，但 FG 与 importin-β 共相分离：所有位点 ρslow 维持低位（约 100–200 ns），仅 100 缓升至约 400–530 ns；无触顶。mean ± s.d., n = 3。
横纵轴定义：同 c。阅读方向：与 c 同位点同时间对比上升幅度。
颜色含义：同 c。
核心结论：importin-β 跨位点延缓老化（包括 100），支持普遍削弱 FG–FG 接触。

(E) 成熟后补加 importin-β（不可逆限定）
图片解释：0–60 min NUP98 only（100 粉红已触顶 1000、221 绿约 250），60 min 补加 importin-β（蓝 shaded 区 60–120 min，箭头 "Imp-β added"）：100 维持上限、221 仅微升至约 330–380 ns，无回落。
横纵轴定义：横 = 时间 (min) 0–120；纵 = ρslow (ns) 0–1000。阅读方向：看蓝区是否出现下降（下降 = 再液化）；此处无。
颜色含义：粉红 = 100、绿 = 221；蓝 shaded = 补加后窗口。
核心结论：成熟凝聚体不能被 importin-β 完全再液化——液化作用是预防/延缓而非逆转（重要负性限定）。

(F) 模拟溶胀与分配
图片解释：四幅 slab 几何模拟终构型（N\_Imp-β/N\_NUP98 = 0, 0.2, 0.4, 0.6）：灰 = FG 凝聚体 slab、红 = importin-β；随比例增加 slab 变宽（溶胀）、红分子进入 slab 内部；ε~FG–Imp-β = 0.42、ε~FG–FG = 0.5。标尺 20 nm。
横纵轴定义：无坐标轴（模拟快照）。阅读方向：左→右/上→下 = 比例递增；比较 slab 宽度与红分子位置。
颜色含义：灰 = NUP98 FG；红 = importin-β；蓝框 = 模拟盒边界。
核心结论：实验匹配强度下 importin-β 分配入凝聚体并致溶胀，复现 a 的形态效应（Supplementary Video 2，未提供）。

(G) 85–124 段稀释定量
图片解释：凝聚体中心 15 nm 探针球内 85–124 段相对密度 n\_aa85–124（相对纯 FG 凝聚体）随 N\_Imp-β/N\_NUP98 自约 0.82（0.2）单调降至约 0.33（2.0）；蓝点 + 误差棒（mean ± s.d., n = 300 snapshots，每 500τ 采样、末 15×10⁴τ）+ 虚线趋势。
横纵轴定义：横 = importin-β/FG 摩尔比 0–2；纵 = 相对段密度 0.2–1.0。阅读方向：下降 = 聚集倾向段被稀释/统计分离。
颜色含义：蓝点/虚线 = 模拟均值与趋势；无多通道。
核心结论：importin-β 稀释淀粉样倾向段——延缓液-固转变的机制解释。

→ Extended Data Fig. 2 标题为 "Cellular abundance of importin-β and its modulation of NUP98 FG-domain dynamics in vitro"，旨在给 importin-β 的生理丰度与体外效应提供对照。由 a 至 j 共 10 部分。

(A) NPC 处 importin-β 浓度滴定
图片解释：四幅灰度图：免疫染色（Alexa488 抗 KPNB1）后加入 1 µM/10 µM/100 µM/1 mM 自由 AF488；1–100 µM 下核 rim/核内信号仍可辨，1 mM 时完全被背景淹没。标尺 10 µm。
横纵轴定义：无坐标轴（荧光图）。阅读方向：左→右 = 自由染料浓度递增；信号何时被淹没 = 局部浓度量级估计。
颜色含义：灰度 = 荧光强度。
核心结论：NPC 处 importin-β 有效局部浓度达毫摩尔级——其液化作用在生理丰度下可行。

(B–E) 共相分离 TRFA 参数（合并解读）
图片解释：四面板时间 course（0–60 min）：b ρslow（only 深绿升至约 250 ns，1:1/1:2/1:4 浅绿平约 100–130 ns，含 0–20 min 放大插图）；c r\_0 平约 0.35；d r\_p 平约 0.31；e ρfast 约 0.2–0.5 ns 波动。mean ± s.d., n = 3。
横纵轴定义：横 = 时间 (min)；纵依次为 ρslow (ns)、r\_0、r\_p（无单位）、ρfast (ns)。阅读方向：b 看 only 与加药组分离；c–e 看光物理参数是否随条件漂移（应平稳）。
颜色含义：深绿 = NUP98 only；浅绿渐变 = 1:1/1:2/1:4。
核心结论：importin-β 只改慢链段组分、不改探针光物理——效应真实且特异。

(F–J) 五位点 ±importin-β 老化对照（合并解读）
图片解释：五面板（残基 36/100/312/387/482）各两条时间 course：深绿 = NUP98 only（升至 1000 ns 上限，36/100 约 15 min、312/387/482 约 30–40 min）、浅绿 = 1:1 importin-β（平约 100–250 ns）。mean ± s.d., n = 3。
横纵轴定义：横 = 时间 (min) 0–60；纵 = ρslow (ns) 0–1000（灰虚线 = 上限）。阅读方向：每面板深/浅绿对比 = 该位点老化是否被压制。
颜色含义：深绿 = only；浅绿 = +importin-β 1:1。
核心结论：液化效应跨位点普适（含 100），非单点伪影。

→ Extended Data Fig. 3 标题为 "Simulation of condensation of NUP98 FG domains with importin-β"，旨在以实验约束模拟相互作用强度。由 a 至 e 共 5 部分。

(A) 共凝聚快照（比例×强度）
图片解释：四幅 slab 快照（比例 0.4 与 1.0 × ε~ 0.4 与 0.42）：灰 FG slab + 红 importin-β；ε~ = 0.42 时红更多进入 slab、slab 更宽。标尺 20 nm。
横纵轴定义：无坐标轴（快照）。阅读方向：比较同比例下 ε~ 0.4 vs 0.42 的红分子分配与 slab 宽度。
颜色含义：灰 = FG；红 = importin-β。
核心结论：强度微增（0.4→0.42）显著改变分配——参数敏感，需实验约束。

(B) FG 浓度剖面族（合并解读）
图片解释：六面板（比例 0.2–2.0）c\_FG (mg/mL) vs x (nm)：slab 平台随比例增加而变宽、随 ε~ 增加而变矮；六色 = ε~ 0.35 蓝/0.40 橙/0.42 绿/0.44 红/0.47 紫/0.50 棕；实线 = 双误差函数拟合；n = 45,000 snapshots（每 10τ、末 4.5×10⁵τ）mean ± s.e.。
横纵轴定义：横 = 盒内位置 x (nm) −100–100；纵 = c\_FG (mg/mL) 0–400。阅读方向：平台宽度 = 溶胀程度；平台高度 = 密相浓度。
颜色含义：逐 ε~ 配色（图例）。
核心结论：溶胀与密相稀释是 ε~ 与比例的联合函数——提供参数化观测量。

(C) 实验密相浓度
图片解释：散点 + 误差棒（mean ± s.d., n = 5）：NUP98 only 约 500 mg/mL、1:0.5 约 240、1:1 约 200、1:2 约 150 mg/mL（Alexa594 示踪 + 自由染料标定 + 量子产率校正）。
横纵轴定义：横 = FG:importin-β 比例（only/1:0.5/1:1/1:2）；纵 = 浓度 (mg/mL) 100–500。阅读方向：随比例下降 = 密相被稀释。
颜色含义：红 = only、蓝 = 1:0.5、黄 = 1:1、绿 = 1:2。
核心结论：实验密相浓度随 importin-β 单调下降——模拟约束的目标数据。

(D) 实验稀相浓度
图片解释：散点（n = 5）：only 约 0.023 mg/mL（因无 importin-β 时稀相存在纳米簇而偏高）、1:1 约 0.008、1:2 约 0.017、1:4 约 0.033 mg/mL。
横纵轴定义：横 = 比例；纵 = 浓度 (mg/mL) 0–0.04。阅读方向：only 偏高提示稀相纳米簇（ED3d 自陈）。
颜色含义：同 c 比例配色。
核心结论：稀相行为非单调，提示纳米簇存在——参数化时需考虑（诚实细节）。

(E) 模拟密相 vs 实验灰带
图片解释：c\_FG 密相随比例下降曲线族（ε~ 0.37–0.50 八色），灰 shaded = c 的实验 mean ± s.d.；仅 ε~ 0.4–0.5 区间曲线落入灰带。
横纵轴定义：横 = 比例 0.5–2；纵 = c\_FG (mg/mL) 100–400。阅读方向：看哪些 ε~ 曲线与灰带重叠。
颜色含义：逐 ε~ 配色；灰带 = 实验约束。
核心结论：实验把 ε~FG–Imp-β 约束到 0.4–0.5，结合 ED4 锁定 0.42。

**Section 5：Importin-β shapes NPC permeability barrier（importin-β 塑造 NPC 通透屏障）**

内容逻辑：本节把"液化"升级为"空间组织"，回答 importin-β 在运输 competent 网络中如何分布。推理链：先以凝聚体内 importin-β 扩散系数（ED5 MSD 线性拟合、ED6b D/D0）估算穿越 NPC 的平均首通时间，得 1–10 ms，与实验核转运速率吻合（refs 24,42–46）；ED6c 进一步显示扩散通量 J 在 ε~ ≈ 0.40–0.42 达峰——亲和力"足够结合以保选择性、又足够快以保效率"的最优平衡（ED6）。再以实验匹配强度（ε~FG–FG = ε~FG–Imp-β = 0.42）模拟负载 100 个 importin-β 的 NPC，得 striking 径向组织：importin-β 偏环周（r ≈ ±20 nm）、中央轴相对 depleted（Fig.3a,b 左）；但中央并非空孔——仍被高动态、伸展的 FG 占据（Fig.3b 右），其 R\_E 与前作 in-cell FLIM–FRET 吻合（Supplementary Fig. 6）；grafting 几何造成近壁 FG 密度偏高是组织成因。细胞验证用双色 DNA-PAINT MINFLUX（固定 U-2 OS，NUP96-mEGFP 定八重参考系）：importin-β 径向密度峰在约 20 nm、向中心下降（Fig.3f,g），与模拟及 ref 14 的环周偏好轨迹一致；2D 随机零模型排除"纯径向几何造成中央 depletion"的几何解释。敏感性分析：ε~ +20%（0.5）→ importin-β 凝入孔中心（Fig.3c）；−20%（0.35）→ 全孔 delocalize（Supplementary Fig. 5）——组织对亲和力精细平衡敏感。动力学异质性：模拟轨迹中 importin-β 在孔中心运动最快（Supplementary Fig. 8），与 ref 14 一致，解释为中央 FG 更稀更伸展→结合位点交换更快。作者诚实标注两处未解释：ref 14 报道的胞质远端高密度区未被模拟捕获（需 NUP358 长链精细建模）；ε~ ±20% 的预测尚待实验直接检验。本节贡献是把材料态结论扩展为"径向组织"框架，统一模拟与 MINFLUX，并为 Discussion 的 central plug/dual-route 讨论提供地基。

→ Figure 3 标题为 "Importin-β shapes the FG-NUP permeability barrier of the NPC"，旨在给出屏障径向组织的模拟预测与细胞验证。由 a 至 g 共 7 部分，形成"模拟组织→强度敏感性→标记策略→MINFLUX 验证→零模型对照"的证据链。

(A) 负载 importin-β 的 NPC 模拟终构型
图片解释：上 = 胞质侧俯视（金色膜平面、绿支架、灰 FG、红 importin-β 点偏外周散布）；下 = 横截面侧视（胞质在上、核在下，金色膜线，红 importin-β 近壁/环周、灰 FG 填中央）；仅显示 |z| < 66 nm 分子；100 个 importin-β，ε~FG–FG = ε~FG–Imp-β = 0.42。标尺 20 nm。
横纵轴定义：无坐标轴（三维快照）。阅读方向：俯视看红点相对环的径向位置；侧视看红点相对中央轴/近壁分布。
颜色含义：红 = importin-β；灰 = FG-NUPs；绿 = 支架；金 = 核被膜。
核心结论：实验匹配强度下 importin-β 自发偏环周、FG 占中央——径向组织的模拟预测。

(B) 匹配强度浓度图（ε~ = 0.42）
图片解释：左 = importin-β 浓度 (r,z) 图（白→红 0–150 mg/mL）：两条红弧位于 r ≈ ±20 nm、z ≈ 0–40，中央轴白（depleted）；右 = FG 浓度图（白→蓝 0–200 mg/mL + 虚线等值线 50/100/150）：中央蓝（FG 富集、伸展）、两侧灰影 = 支架；末 5×10⁴τ、每 10²τ 采样平均。
横纵轴定义：横 = 径向距离 r (nm) −40–40；纵 = 轴向高度 z (nm) −40–40（z>0 = 胞质侧）。阅读方向：左图看红弧位置与中央白区；右图看蓝区是否填中央。
颜色含义：左白→红 = importin-β 浓度递增；右白→蓝 = FG 浓度递增；灰 = 支架轮廓；虚线 = 等浓度线。
核心结论：importin-β 环周富集与 FG 中央占据互补——中央 depletion 不等于空孔。

(C) 增强强度浓度图（ε~ = 0.5）
图片解释：同 b 布局但 ε~FG–Imp-β = 0.5（+20%）：左图中央出现深红块（importin-β 凝入孔中心）+ 顶部两弧；右图 FG 被挤向周缘/顶部、中央蓝度下降。
横纵轴定义：同 b。阅读方向：与 b 对比中央红/蓝变化。
颜色含义：同 b。
核心结论：亲和力仅 +20% 即把 importin-β 从环周驱入中心——组织处于精细平衡（Supplementary Video 4，未提供）。

(D) 双色标记/成像策略示意
图片解释：NPC 八重环（灰）上 NUP96-mEGFP（蓝筒+绿球）经抗 GFP 纳米抗体-D1 docking 链 + 绿 imager D1\* 标记；中央 importin-β-ALFA（红筒+橙/紫球）经抗 ALFA 纳米抗体-D3 + 红 imager D3\* 标记；r 箭头自孔中心向外。
横纵轴定义：无坐标轴（示意）。阅读方向：环 = 支架参考通道；中央 = 待测通道；r = 径向坐标定义。
颜色含义：绿 = NUP96 通道；红 = importin-β 通道；蓝/红筒 = 蛋白；星 = imager 染料。
核心结论：以支架为参考系的双色顺序 DNA-PAINT MINFLUX 可测 importin-β 相对孔中心的径向分布。

(E) MINFLUX 定位图
图片解释：左 = 宽视场定位点（绿 NUP96 环 + 红 importin-β），框 1–6；右 = 六个单孔放大：绿八重环 + 红点位于环内中间半径。标尺左 500 nm、右 50 nm。
横纵轴定义：无坐标轴（定位点图）。阅读方向：左找孔、右看单孔内红点相对绿环的径向位置。
颜色含义：绿 = NUP96 定位；红 = importin-β 定位。
核心结论：单孔水平 importin-β 位于环内中间半径而非中心——径向组织的直接成像证据。

(F) 平均定位密度图（n = 460 NPCs）
图片解释：三图：NUP96 八重平均（灰度八瓣环，色标 0–2.0+ a.u.）、importin-β 径向平均（灰度径向盘：中间半径亮环、中心暗孔，色标 0–0.08 a.u.）、Overlay（红径向盘 + 绿八重环叠加）。标尺 50 nm。
横纵轴定义：无坐标轴（二维密度图），隐含横纵 = 孔平面 x/y (nm)。阅读方向：看 importin-β 亮环半径与中心暗区；overlay 看两通道相对位置。
颜色含义：灰度 = 相对定位密度；overlay 红 = importin-β、绿 = NUP96。
核心结论：群体水平 importin-β 呈中间半径环状富集、中央相对 depleted。

(G) 对称化径向密度剖面 + 零模型
图片解释：归一化径向剖面：绿 NUP96 峰于 r ≈ ±60 nm；红 importin-β 峰于 r ≈ ±20 nm、r=0 处谷（约 0.6）；蓝水平虚线 = 匹配 2D 随机零模型（=1.0）。实线 = 均值、shaded = s.e.m.。
横纵轴定义：横 = r (nm) −100–100；纵 = 归一化相对密度 0–1.2。阅读方向：比较红峰位置与中心谷；红中心谷低于蓝零模型线 = 非几何伪影。
颜色含义：绿 = NUP96；红 = importin-β；蓝虚线 = 2D 随机零模型。
核心结论：中央 importin-β depletion 不能由径向几何 alone 解释——真实组织特征，与模拟及 ref 14 一致。

→ Extended Data Fig. 4 标题为 "Partitioning of importin-β into NUP98 FG condensates"，旨在以分配数据锁定 ε~。由 a 至 c 共 3 部分。

(A) importin-β 浓度剖面族（合并解读）
图片解释：六面板（比例 0.2–2.0）c\_Imp-β (mg/mL) vs x (nm)，八色 ε~ 0.35–0.50；ε~ ≥ 0.44 时稀相浓度近 0（几乎全吸收）；实线 = 双误差函数拟合；n = 45,000 snapshots mean ± s.e.。
横纵轴定义：横 = x (nm) −100–100；纵 = c\_Imp-β (mg/mL) 0–400。阅读方向：看 slab 内平台与稀相基线随 ε~ 的变化。
颜色含义：逐 ε~ 配色（图例）。
核心结论：ε~ ≥ 0.44 全吸收→分配系数外推远超 1000、超出蛋白质组学预期范围。

(B) 分配相图
图片解释：ε~FG–Imp-β (纵 0.40–0.50) vs importin-β 浓度 (mg/mL, 横 0–400)，六色曲线 = 比例 0.2–2.0；呈 U 形/交叉族。
横纵轴定义：横 = importin-β 浓度 (mg/mL)；纵 = ε~。阅读方向：沿某比例曲线看密/稀相浓度随强度变化。
颜色含义：逐比例配色（顶部标注）。
核心结论：分配行为对 ε~ 与比例联合敏感——相图式参数约束。

(C) 分配系数外推 vs 蛋白质组学带
图片解释：log 纵（10⁰–10³）分配系数 vs 比例：绿 ε~ = 0.42 自约 400（0.4）降至约 3（2.0）、橙 ε~ = 0.40 自约 15 降至约 1.5；虚线 = ae^(bN) 拟合（0.5 ≤ 比例 ≤ 1）；深灰矩形 = 蛋白质组学估 NPC 内 400–1300，浅灰 = 向下扩 10 倍（crowding 不确定）。
横纵轴定义：横 = 比例 0–2；纵 = 分配系数（log）。阅读方向：看绿曲线外推（比例→0）是否落入灰带。
颜色含义：绿 = 0.42；橙 = 0.40；灰带 = 蛋白质组学约束。
核心结论：ε~ = 0.42 外推 1120 ± 364 落在 400–1300 带内（0.40 仅 16.5 ± 6 不符）——锁定 0.42。

→ Extended Data Fig. 5 标题为 "Diffusion of importin-β inside NUP98 FG condensates"，旨在给扩散系数/首通时间提供模拟测量。由 a 至 d 共 4 部分。

(A) 单 importin-β 凝聚体快照
图片解释：38σ 立方盒内灰白 FG 凝聚体 + 红单 importin-β；蓝框 = 盒边界。
横纵轴定义：无坐标轴（快照）。阅读方向：红分子在灰凝聚体内的位置。
颜色含义：灰白 = FG beads；红 = importin-β。
核心结论：单分子 MSD 测量的体系设置。

(B) slab 多分子体系与 bin 划分
图片解释：360σ×90σ×90σ slab，沿 x 划 9 个 40σ（≡24 nm）bin（黑竖线）；红 importin-β 分布于 slab 内外。
横纵轴定义：无坐标轴（快照）；标注 40σ ≡ 24 nm 给出长度换算。阅读方向：中央 bin（−20σ<x<20σ）用于 MSD 平均。
颜色含义：灰 = FG；红 = importin-β；黑线 = bin 边界；蓝框 = 盒。
核心结论：以中央 bin 分子读"凝聚体内部"扩散，避免界面伪影。

(C) 单分子 MSD vs ε~
图片解释：MSD (σ²) vs t (10³τ) 0–10，十色 ε~ 0.3–0.5；黑虚线 = t > 6×10³τ 线性拟合（斜率→D）。
横纵轴定义：横 = t (10³τ)；纵 = MSD (σ²)。阅读方向：线性区斜率越大 = 扩散越快；比较 ε~ 间斜率。
颜色含义：逐 ε~ 配色（图例）；黑虚线 = 线性拟合。
核心结论：扩散系数随 ε~ 增加而下降——亲和力- mobility 权衡的原始数据。

(D) 多分子 MSD 三分量（合并解读）
图片解释：三面板 = x/y/z 分量 MSD vs t (10³τ) 0–60+，六色比例 0.2–2.0；黑虚线 = t > 15×10³τ 线性拟合；ε~ = 0.42、ε~FG–FG = 0.5；4.8×10⁵τ 测量。
横纵轴定义：横 = t (10³τ)；纵 = MSD (σ²) 0–100。阅读方向：y/z（平行界面）斜率用于 D = (Dy+Dz)/2；x 受 slab 限域影响。
颜色含义：逐比例配色（图例）。
核心结论：取平行界面分量得凝聚体内 D，供首通时间与通量估算。

→ Extended Data Fig. 6 标题为 "Estimated diffusive flux of importin-β inside NUP98 FG condensate"，旨在证明亲和力对通量的最优平衡。由 a 至 c 共 3 部分。

(A) 密相 importin-β 浓度 vs ε~
图片解释：log 纵（10⁻¹–10³ mg/mL）c\_dense vs ε~ 0.35–0.5，六色比例；约 0.38–0.42 处陡升；实线 = ae^(bε~) 拟合（0.42–0.5）；n = 45,000 snapshots mean ± s.e.。
横纵轴定义：横 = ε~；纵 = c\_dense (mg/mL, log)。阅读方向：陡升区 = 吸收阈值。
颜色含义：逐比例配色。
核心结论：密相浓度对 ε~ 高度非线性——临界样敏感。

(B) 归一化扩散系数 D/D0 vs ε~
图片解释：log 纵（10⁻⁵–10⁰）D/D0 vs ε~：黄 = 单 importin-β（约 0.07–0.1 近平）、其余比例自约 0.1–0.3 随 ε~ 降至 10⁻³–10⁻²；实线 = 指数拟合；D0 = 51 µm²/s（自由溶液）。
横纵轴定义：横 = ε~；纵 = D/D0（log）。阅读方向：下降 = 结合越强移动越慢。
颜色含义：逐比例配色 + 黄 = 单分子。
核心结论：mobility 随亲和力单调下降——与 a 的浓度上升构成权衡两臂。

(C) 跨 NPC 扩散通量 J vs ε~
图片解释：J\_Imp-β (s⁻¹) vs ε~ 0.37–0.5，六色比例；各曲线在 ε~ ≈ 0.40–0.42 达峰（约 100–340 s⁻¹）、两侧下降；J = A×c\_dense×D，几何预因子 V\_NPC/H\_NPC² 换算（R\_NPC = 0.05 µm、H\_NPC = 0.1 µm）。
横纵轴定义：横 = ε~；纵 = J (s⁻¹) 0–400。阅读方向：峰位 = 最优亲和力；与实验匹配值 0.42 对照。
颜色含义：逐比例配色。
核心结论：通量在实验匹配亲和力附近最大——FG–importin-β 相互作用"被优化以增强净 cargo 运输"。

→ Extended Data Fig. 7 标题为 "Bond-vector relaxation of NUP98 FG chains in solution, condensates and the NPC"，旨在以模拟键矢量松弛对照 TRFA 层级。由 a 至 c 共 3 部分。

(A) 15 位点键矢量自相关（合并解读）
图片解释：15 面板（残基 36–482）log 纵（10⁻²–10⁰）⟨b\_i(t0+t)·b\_i(t0)⟩ vs t (τ) 0–100：紫 = 单链（最快）、橙 = NPC 含 importin-β（中）、绿 = 凝聚体无 importin-β（最慢）；虚线 = 早 [0,10τ]/晚 [25τ,100τ] 双指数拟合；4 次独立运行；单链 10⁵τ、凝聚体/NPC 10⁴τ；NPC ε~ = 0.42/0.42、单链/凝聚体 ε~FG–FG = 0.5。
横纵轴定义：横 = t (τ)；纵 = 键矢量自相关（log）。阅读方向：曲线越高 = 松弛越慢 = 越受限；比较三色层级。
颜色含义：紫 = single chain；橙 = NPC with imp-β；绿 = condensate no imp-β。
核心结论：模拟复现"单链 > NPC > 凝聚体"的链段动力学层级，与 Fig.1h 实验趋势平行。

(B) 慢松弛时间 τslow vs 位点
图片解释：绿（凝聚体）约 115–120τ 平、橙（NPC）约 90–120τ、紫（单链）约 40–80τ（100 处峰约 80τ）；mean ± s.e.m.（4 runs）。
横纵轴定义：横 = 残基号；纵 = τslow (τ) 40–120。阅读方向：三色高低 = 受限层级；紫在 100 的峰 = 聚集倾向段局部慢。
颜色含义：同 a。
核心结论：慢组分层级与实验 ρslow 层级一致；100 的局部慢在模拟中亦现。

(C) 快松弛时间 τfast vs 位点
图片解释：绿约 6.1τ、橙约 4.8–5.0τ、紫约 4.2–4.5τ，跨位点近平。
横纵轴定义：横 = 残基号；纵 = τfast (τ) 4.0–6.0。阅读方向：比较三色快组分。
颜色含义：同 a。
核心结论：快组分亦呈层级但幅度小——confinement 主要影响慢链段组分。

**Section 6：O-GlcNAcylation tunes NUP98 dynamics（O-GlcNAc 糖基化调控 NUP98 动力学）**

内容逻辑：本节追索第二个液化因子并做功能闭环。立论：importin-β 仅延缓而非阻止体外固化（Fig.2d），故必有其他机制；O-GlcNAc 最 compelling——FG-NUPs 为后生动物修饰最重类群、NUP98 本身重修饰（refs 47,48），既往已联系 FG 水凝胶材料性质与核转运速率（refs 48,49），但对纳秒链段动力学的作用未知。细胞扰动：OSMI-4（10 µM）降全局 O-GlcNAc（RL2 印迹变浅，Fig.4b）并减慢第二 FG 域多位点链段运动（Fig.4a：7/10 位点 P ≤ 0.0003，426/458/482 不显著——如实呈现"several positions"而非全位点）；空间模式 broadly 跟随预测修饰倾向（ED8a）。关键负性结果：Thiamet-G 升 O-GlcNAc 几乎不再加速（多数位点 P = 0.296–0.987；仅 426 P = 0.031 呈弱加速）——说明内源修饰已足够支持生理纳秒柔性，防止把 O-GlcNAc 夸大为"越多越好"的限速旋钮。功能闭环：LINuS 核输入速率 OSMI-4 显著减慢（vs control P = 0.0053）、Thiamet-G 与对照相当（P = 0.0709）（Fig.4e,f）——把链段动力学变化落到 NPC 功能。体外最小体系：酶法糖基化（约 17 GlcNAc/链，ED8c,e）显著延缓成熟、维持液态（Fig.4g,h），100 位点保护尤显，但单因子不完全重现细胞谱。联合体系：糖基化 + importin-β 共相分离高度动态、抗 slowdown，跨位点谱 closely match 活细胞（221：72 ± 3 vs 59 ± 14 ns；Fig.4i、ED8f）——即"重现活细胞谱"的体外最小系统。细胞回补：OSMI-4 背景下过表达 importin-β 部分恢复 100 位点链段运动（P = 0.0099）并改善核输入（P = 0.0005；vs control P = 0.4664 即回对照水平）（Fig.4c,e,f）——确立 importin-β 在 FG–FG 增强时的 modulatory/补偿角色。本节贡献：确立两因子互补液化、把动力学与转运功能因果链接，并以"部分回补/弱效"诚实划定权重边界。

→ Figure 4 标题为 "O-GlcNAcylation modulates FG-NUP dynamics and nuclear transport"，旨在把 O-GlcNAc 扰动落到链段动力学与转运功能并做联合/回补验证。由 a 至 i 共 9 部分。

(A) 十位点 ±Thiamet-G/OSMI-4 箱图
图片解释：10 面板（221–482）各三箱：Control 橙、+Thiamet-G 绿、+OSMI-4 紫；OSMI-4 使 ρslow 上移（如 221 约 57→72、362 约 107→150），Thiamet-G 与对照近同。P（OSMI vs control）：221/251/283/312/338/387 < 0.0001、362 = 0.0003、426 = 0.208、458 = 0.307、482 = 0.123；P（Thiamet vs control）：0.957/0.678/0.987/0.296/0.344/0.509/0.404/0.031(426)/0.379/0.474。n（Thiamet）= 44,45,46,46,46,42,48,46,46,46；n（OSMI）= 44,45,46,47,45,40,46,47,47,42；control 同 Fig.1g；3 次独立实验；200 bootstrap；双侧 bootstrap 检验。
横纵轴定义：横 = 三条件；纵 = 表观 ρslow (ns)（各面板量程不同，约 50–200）。阅读方向：紫 vs 橙 = 降修饰效应；绿 vs 橙 = 升修饰效应；括号 P 值对应比较。
颜色含义：橙 = Control；绿 = +Thiamet-G；紫 = +OSMI-4。
核心结论：降 O-GlcNAc 减慢链段运动（7/10 位点显著）、升修饰几乎无额外加速——内源修饰已足够（负性限定）。

(B) 全局 O-GlcNAc 免疫印迹
图片解释：RL2（O-GlcNAc）印迹：Marker、Control、+Thiamet-G、+OSMI-4 四泳道；RL2 呈 25–140+ kDa  smear；Thiamet-G 泳道 smear 加深、OSMI-4 变浅；GAPDH（约 40 kDa）上样均一。代表性图像 ≥3 次重复；原文未提供定量灰度数值。
横纵轴定义：无坐标轴（免疫印迹）。横 = 条件泳道；纵 = 分子量 (kDa)，标记 15–140。阅读方向：比较同分子量区间 smear 深浅 = 全局 O-GlcNAc 水平。
颜色含义：灰度条带，越深 = O-GlcNAc 修饰蛋白越多；GAPDH = 上样对照。
核心结论：药物确实双向改变全局 O-GlcNAc——扰动的生化验证。

(C) importin-β 过表达回补（残基 100）
图片解释：三箱：Control 橙约 85 ns、+OSMI-4 紫约 101 ns、+OSMI-4+Imp-β 蓝约 88 ns；P < 0.0001（control vs OSMI）、P = 0.0099（OSMI vs OSMI+Imp-β）。n = 80/109/74 细胞、3 次独立实验、200 bootstrap。
横纵轴定义：横 = 三条件；纵 = 表观 ρslow (ns) 80–140。阅读方向：蓝 vs 紫 = 回补幅度；蓝 vs 橙 = 是否完全恢复（此处部分）。
颜色含义：橙 = Control；紫 = +OSMI-4；蓝 = +OSMI-4+Imp-β。
核心结论：importin-β 过表达部分恢复降修饰导致的链段变慢——modulatory/补偿角色（部分而非完全回补，诚实限定）。

(D) LINuS 报告子示意
图片解释：暗态 LOV2 core（紫）笼蔽 Jα（紫）-NLS（绿），NES 占优→胞质定位（mCherry 红团在胞质）；蓝光（闪电）使 Jα 解笼、NLS 激活→核输入；右侧 Off/250 s/500 s/750 s 红荧光核累积图 + 核强度累积曲线示意（kImport 箭头）+ import rate 箱示意。标尺 10 µm。
横纵轴定义：示意无坐标轴；曲线横 = 时间 (s)、纵 = 归一化核强度。阅读方向：暗→光 = 报告子激活；核强度上升斜率 = 输入速率。
颜色含义：紫 = LOV2/Jα；绿 = NLS；红 = mCherry 报告子；蓝闪电 = 激活光。
核心结论：光控核输入报告子把"屏障功能"量化为表观输入速率常数 k。

(E) 核输入累积曲线
图片解释：四色曲线（Control 橙、+Thiamet-G 绿、+OSMI-4 紫、+OSMI-4+Imp-β 蓝）归一化核强度自 1.0 升至约 1.8–1.9（800 s）；紫曲线最低（约 1.65）、蓝回升近橙/绿；shaded = s.e.m.；n = 67/69/105/88 细胞。
横纵轴定义：横 = 时间 (s) 0–800；纵 = 归一化核强度 (a.u.) 1.0–2.0。阅读方向：曲线越低/越慢 = 输入越慢；比较紫与橙/蓝。
颜色含义：橙/绿/紫/蓝 = 四条件（图例）。
核心结论：降 O-GlcNAc 减慢核输入、importin-β 回补改善——动力学-功能链接。

(F) 表观输入速率常数箱图
图片解释：四箱 k (min⁻¹)：Control 约 0.13、+Thiamet-G 约 0.14、+OSMI-4 约 0.10、+OSMI-4+Imp-β 约 0.13；单点 = 单细胞；P = 0.4664（control vs OSMI+Imp-β）、P = 0.0053（control vs OSMI）、P = 0.0709（control vs Thiamet）、P = 0.0005（OSMI vs OSMI+Imp-β）；双侧 Welch t + Holm 校正；指数拟合 y = 1+(b−1)(1−e^(−kt))。
横纵轴定义：横 = 四条件；纵 = 表观输入速率常数 (min⁻¹) 0–0.5。阅读方向：箱高低 = 输入快慢；括号 P 对应比较。
颜色含义：橙/绿/紫/蓝 = 四条件。
核心结论：OSMI-4 显著减慢输入（P = 0.0053）、Thiamet-G 无显著差异（P = 0.0709）、回补显著改善（P = 0.0005）且回到对照水平（P = 0.4664）。

(G) 体外糖基化 ±importin-β 相分离时间 lapse
图片解释：3 行 × 5 时点（3/6/9/12/15 min）灰度图：WT（液滴随时间粗化/融合、亮而少）、GlcNAcylated（大量小液滴/网络持续、抗粗化）、GlcNAcylated+Imp-β（大而融合的液态网络）。标尺 10 µm；糖基化 FG 25 µM（vs WT 10 µM）以得可比尺寸。
横纵轴定义：无坐标轴（时间 lapse 荧光图）。横 = 时间递增；纵 = 三条件行。阅读方向：同行看液滴粗化程度（粗化 = 老化/融合）；行间比较抗老化能力。
颜色含义：灰度 = FG 荧光；越亮越集中 = 液滴越粗化。
核心结论：糖基化延缓成熟、加 importin-β 维持液态网络——体外最小体系的材料态调控。

(H) 糖基化凝聚体六位点老化 course
图片解释：ρslow vs 0–60 min，六色（36 蓝/100 粉红/221 绿/312 紫/387 黄/482 灰）：自约 60–80 ns 缓升至约 95–180 ns（387 最高约 180、221 最低约 95），无触顶；mean ± s.d., n = 3。
横纵轴定义：横 = 时间 (min)；纵 = ρslow (ns) 0–200。阅读方向：与 Fig.2c（未糖基化、触顶 1000）对比上升幅度。
颜色含义：逐残基配色（图例）。
核心结论：部分糖基化（约 17 GlcNAc/链）即显著延缓老化、维持液态——局部修饰足以抑制分子间 FG–FG 病理接触。

(I) 糖基化 + importin-β 六位点 course
图片解释：同 h 位点/配色但加 importin-β：ρslow 全时程平约 65–110 ns（387 约 100–110、221 约 70），几乎无上升；mean ± s.d., n = 3。
横纵轴定义：同 h。阅读方向：与 h 对比是否进一步压平；与 Fig.1g 活细胞谱对比形状。
颜色含义：同 h。
核心结论：双因子联合体外重现活细胞表观链段运动谱（221：72 ± 3 vs 59 ± 14 ns）——"细胞样液态"的最小体外系统（ED8f、Supplementary Video 1）。

→ Extended Data Fig. 8 标题为 "Characterisation of O-GlcNAcylated NUP98 FG domains"，旨在给糖基化体系提供位点/质谱/形态/谱对照。由 a 至 f 共 6 部分。

(A) 第二 FG 域预测修饰位点序列图
图片解释：NUP98 1–505 序列（FG motifs 橙、Ser/Thr 及预测修饰位点蓝标、序列上方点标记位点位置）+ 顶部域图；caption 注明蓝 = 依 O-GlcNAc Database v2.0 注释的预测 O-GlcNAc 位点。
横纵轴定义：无坐标轴（序列图），横 = 残基序号 1–505（每行 40 残基）。阅读方向：看蓝标/点标记在第二 FG 域的分布 = OSMI-4 敏感性的空间预期。
颜色含义：橙 = FG motifs；蓝 = Ser/Thr/预测修饰位点；点 = 位点标记。
核心结论：OSMI-4 敏感位点的空间模式 broadly 跟随预测修饰倾向——效应与修饰位置自洽。

(B–C) 野生型/糖基化质谱（合并解读）
图片解释：b WT 主峰 43797.0 Da（伴 43776/43755/43869/43817/43890/43941）；c 糖基化峰包络 47049–47663 Da（主峰约 47252/47049），每个 GlcNAc +203.08 Da；主峰差约 3455 Da ≈ 17 × 203.08 → 约 17 GlcNAc/链（部分修饰）。
横纵轴定义：横 = 质量 (Da)（b 43700–44100；c 30000–80000）；纵 = 相对丰度 (%) 0–100。阅读方向：b 单峰 vs c 峰包络 = 修饰异质性；峰差/203.08 = 糖数。
颜色含义：黑谱线 = 质谱峰；无多通道。
核心结论：酶法糖基化成功但为部分修饰（约 17/链）——"部分修饰即足够"的定量前提。

(D) 糖基化 10 µM 相分离时间 lapse
图片解释：3–15 min 五幅灰度图：大量小液滴持续存在、抗粗化；标尺 10 µm。caption 注明 TRFA 用 25 µM 以得与未糖基化可比尺寸。
横纵轴定义：无坐标轴（时间 lapse）。横 = 时间递增。阅读方向：液滴是否粗化融合。
颜色含义：灰度 = FG 荧光。
核心结论：糖基化降低相分离倾向/延缓粗化——与 Fig.4g 行 2 一致。

(E) Coomassie SDS-PAGE
图片解释：三泳道：Marker（蓝带 10–140 kDa）、O-GlcNAc −（约 40–45 kDa 带）、+（迁移更慢约 45–50 kDa smear）——糖基化增重致迁移变慢。
横纵轴定义：无坐标轴（凝胶）。横 = 泳道；纵 = 分子量 (kDa)。阅读方向：比较 −/+ 泳道带位置（+ 更靠上 = 更重）。
颜色含义：蓝 = Coomassie 蛋白带；越深 = 蛋白越多。
核心结论：糖基化蛋白完整且增重——生化验证（代表性凝胶，原文未提供定量）。

(F) 活细胞 vs 体外各条件 ρslow 谱对比
图片解释：横排 15 位点散点：红 = in the NPC、黄 = WT-FG 凝聚体 (first 5 min)、绿 = O-GlcNAc-FG 凝聚体 (first 5 min)、紫红 = WT-FG & imp-β (first 5 min)、浅紫 = O-GlcNAc-FG & imp-β (first 5 min)、开紫 = O-GlcNAc-FG & imp-β (after 1 h)；开紫（双因子 1 h）谱形最接近红（NPC）。
横纵轴定义：横 = 位点；纵 = 表观 ρslow (ns) 0–300。阅读方向：比较各条件散点谱与红 NPC 谱的形状/高度接近度。
颜色含义：逐条件配色（图例）。
核心结论：糖基化 + importin-β 即使 1 h 后仍 closest recapitulate 活细胞谱——联合充分性的谱级证据。

**Section 7：O-GlcNAcylation tunes FG-NUP condensation（O-GlcNAc 糖基化调控 FG-NUP 凝聚）**

内容逻辑：本节以显式化学细节的 Martini 2.2 模拟把糖基化效应机制化。模型取人源收缩态 NPC（PDB 7R5K），FG-NUPs 含 NUP54/58/62/98/214/358/POM121，糖基化四水平 fgly = 0/0.18/0.3/0.6（YinOYang 阈值选位点，N\_total = 58,768 Ser/Thr）；蛋白–蛋白/蛋白–糖/糖–糖相互作用以 α/λ/γ 重缩放并对实验校准（α = 0.78 匹配单链 smFRET 与凝聚体密相密度；λ = 0.15、γ = 0.5 匹配糖水溶液渗透第二维里系数）。结果：fgly = 0 时 FG 塌缩为包绕支架的致密表面凝聚体、留大中央空腔，且 NUP98 链伸展与前作 in situ FLIM–FRET 不符（Fig.5a,e）；随 fgly 增加 FG 渐进伸展入中央通道（Fig.5b–d）；fgly = 0.3 最匹配实验 R\_E（Fig.5e）并预测 48 个修饰位点、与爪蟾 NUP98 实验鉴定的 46 位点 closely match（ref 48）——模拟与实验的独立互证。动力学上糖基化加速键矢量松弛，复现"NPC 内快于未糖基化体外凝聚体、慢于孤立链"的实验层级（Fig.5f）。机制等价性：显式糖基化效应可由隐式弱化 FG–FG 吸引（重缩放 α）复现（ED9）；把 R\_E 匹配到 FLIM–FRET 时 FG-NUPs 处于相分离临界点附近（α\_c ≈ 0.55、实验匹配 α ≈ 0.6）——微小有效相互作用变化即可大幅改变组织，确认前作残基级模型观察（ref 26）。延伸：修饰状态差异促进 FG 组装体间 demixing（模拟 + 选择性分配实验，Supplementary Figs. 16–18），提示后生动物 O-GlcNAc、酵母 O-甘露糖化/磷酸化等 PTM 差异可 tuning FG–FG 强度以 opposes mixing（ref 21）。本节贡献是把"糖基化液化"落到化学细节与临界点物理，给出位点数互证与 demixing 延伸，完成"材料态 + 空间组织 + 化学调控"的统一框架。

→ Figure 5 标题为 "O-GlcNAcylation controls FG-NUP fluidity in the NPC"，旨在以显式糖基化 Martini 模拟给出构象/动力学/临界点机制。由 a 至 f 共 6 部分。

(A–D) 四糖基化水平 NPC 快照 + 浓度图（合并解读）
图片解释：四列 fgly = 0/0.18/0.3/0.6，每列三行：上 = 胞质侧俯视（fgly=0 灰 FG 环包支架、中央大白空腔；随 fgly 增加黄糖珠出现、FG 填入中央）；中 = 横截面侧视（胞质上/核下，绿支架、灰 FG、黄糖）；下 = 方位角平均 FG 浓度图（r 0–40+ nm、z −50–50 nm；白→红 0–50 mg/mL、>50 统一深红；bin Δr=Δz=3 nm；末 600 ns 平均；排除糖珠与 NUP358 长链）：fgly=0 红集中于 r ≈ 20–30 环带、中央白空腔；随 fgly 增加红向 r=0 扩展、中央被填。总模拟时长 3.5 µs (a)、2 µs (b–d)。标尺 20 nm。
横纵轴定义：下排横 = r (nm)、纵 = z (nm)；上/中排无坐标轴（快照）。阅读方向：列间比较中央空腔是否被 FG 填、红区是否向轴扩展。
颜色含义：灰 = FG-NUPs；黄 = 糖基化 Ser/Thr；绿 = 支架；白→红 = FG 浓度 0→50+ mg/mL。
核心结论：糖基化剂量依赖地把 FG 从"表面凝聚体+中央空腔"推向"伸展入中央"——液化/伸展的构象机制。

(E) R\_E vs 序列间隔（四水平 + 实验）
图片解释：R\_E (Å) vs N\_res (aa) 0–300：蓝 fgly=0.6 最高（约 180 Å @300）、橙 fgly=0.3（约 140）、绿 fgly=0.18（约 135）、红 fgly=0 最低（约 115）；黑实心圆 = 实验 FLIM–FRET（ref 26，约 135–140）与橙/绿重合；开方 + 误差棒 = mean ± s.e.，n = 400 snapshots（每 1.5 ns、4×150 ns 块）。
横纵轴定义：横 = 序列间隔 N\_res (aa)；纵 = R\_E (Å) 0–250。阅读方向：曲线越高 = 链越伸展；看哪色与黑实验点重合。
颜色含义：蓝/橙/绿/红 = fgly 0.6/0.3/0.18/0；黑 = 实验。
核心结论：fgly = 0.3 最匹配 in situ 构象——糖基化水平的实验校准（并预测 48 位点 vs 爪蟾 46）。

(F) 键矢量自相关（四体系）
图片解释：log 纵（4×10⁻¹–10⁰）⟨b\_221(t0+t)·b\_221(t0)⟩ vs t (ps) 0–500：紫 = 孤立链（最快，至约 5×10⁻¹）、橙 = NPC fgly=0.3（约 6×10⁻¹）、绿 = 凝聚体（约 6.5–7×10⁻¹）、银 = NPC fgly=0（最慢约 7×10⁻¹）；虚线 = [0,50 ps]/[50,500 ps] 双指数拟合（参数 Supplementary Table 6）；4×100 ns、1 ps 采样。
横纵轴定义：横 = t (ps)；纵 = 键矢量自相关（log）。阅读方向：曲线越低 = 松弛越快 = 越动态；比较四色层级。
颜色含义：紫 = single chain；绿 = condensate；银 = NPC fgly=0；橙 = NPC fgly=0.3。
核心结论：糖基化加速链段松弛、复现实验层级（NPC 糖基化 > 凝聚体；单链最快）——动力学机制互证。

→ Extended Data Fig. 9 标题为 "Weakened FG–FG interactions mimicking O-GlcNAcylation place FG-NUPs near the critical point for condensate formation in Martini MD simulations"，旨在以隐式 α 重缩放复现糖基化效应并定位临界点。由 a 至 f 共 6 部分。

(A–D) 四 α 水平未糖基化 NPC（合并解读）
图片解释：四列 α = 0.5/0.6/0.7/0.78（α 越小 = 有效吸引越弱），每列三行：俯视/侧视快照（白 FG、绿支架）+ 方位角平均浓度图（白→红 0–50、>50 深红、bin 3 nm、末 600 ns、排除 NUP358）：α=0.5 FG 伸展填中央（红区宽、含近轴）、α=0.78 塌缩为环带表面凝聚体（中央白空腔）；模拟 2.5 µs。标尺 20 nm。
横纵轴定义：下排横 = r (nm)、纵 = z (nm)；快照无坐标轴。阅读方向：列间（α 递增 = 吸引增强）看中央是否被填/空腔是否出现。
颜色含义：白 = FG；绿 = 支架；白→红 = FG 浓度。
核心结论：隐式弱化吸引（低 α）复现显式糖基化的伸展效应——糖基化 ≈ 弱化 FG–FG 有效吸引。

(E) R\_E vs α（+ 实验）
图片解释：蓝 α=0.5 最高（约 185 Å @300）、橙 α=0.6（约 140）、绿 α=0.7（约 125）、红 α=0.78（约 115）；黑实验点与橙 α≈0.6 重合；n = 400 snapshots（19,200 链构象）/4×150 ns 块 mean ± s.e.。
横纵轴定义：横 = N\_res (aa)；纵 = R\_E (Å)。阅读方向：看哪色匹配黑点；α≈0.6 仅略高于临界 α\_c≈0.55。
颜色含义：蓝/橙/绿/红 = α 0.5/0.6/0.7/0.78；黑 = 实验 FLIM–FRET。
核心结论：实验匹配 α≈0.6、恰在临界点 α\_c≈0.55 之上——FG-NUPs 处于相分离临界附近。

(F) 密相浓度 vs α（NPC vs 凝聚体）
图片解释：蓝圆 = NPC c\_dens（取 r=21 nm、z=2.6 nm 内环处最大浓度）自约 100 (α0.5) 升至约 290 mg/mL (α0.78)；橙方 = NUP98 凝聚体 slab 中心浓度（约 215 @0.7、355 @0.78）；NPC n = 400 snapshots mean ± s.d.、凝聚体 n = 100 snapshots（每 15 ns、末 1.5 µs）。
横纵轴定义：横 = α 0.5–0.8；纵 = c\_dens (mg/mL) 100–350。阅读方向：曲线陡升区 = 临界附近敏感区。
颜色含义：蓝 = NPC；橙 = 凝聚体。
核心结论：临界点附近微小 α 变化→密相浓度大幅变化——"细胞 tuning 材料态"的物理放大机制。

---

四、<Discussion结构分析>

**第 1 层：活细胞液态 vs 体外老化的核心对比及其动力学语境。** 作者以 TRFA 直接监测活细胞 FG 构象动力学，指出 NUP98 即使在体外易聚集区（85–124）仍保持快速表观链段运动，与老化 FG 凝聚体转固态水凝胶形成 sharp contrast；后者与 NMR/EM 观察的淀粉样相互作用一致（refs 12,36）。进而提出关键问题：为何 FG 体外快速老化（refs 4,5,13）却在细胞最长寿命组装体之一（refs 19,51）内保持动态？作者把 TRFA 读数定位为"毫秒级 cargo 穿越所需数千次瞬态 FG–NTR 接触快速交换"的动力学语境（refs 24,25），并认定 importin-β 与 O-GlcNAc 为两个 tuning 因子（各部分抑制老化、联合重现细胞谱，ED8f）。态度：已证实（活细胞/体外对比与联合重现）；"动力学语境"为解释性框架（推测成分）。

**第 2 层：importin-β 的链段级伴侣作用与 karyopherin 中心模型。** 模拟显示 importin-β 稀释聚集倾向段、溶胀凝聚体、增强表观链段运动；既往虽提出伴侣样性质（refs 36–38），本文首次在链段水平展示其调控，尤其在 FG–FG 增强时，与 karyopherin 中心模型一致（refs 10,52）。态度：已证实（体外+模拟+细胞回补）；"伴侣"为类比性表述。

**第 3 层：PTM 调控层——O-GlcNAc 的可操作性优于磷酸化。** 磷酸化被提出调控 FG 动力学（ref 53）、NUP98 超磷酸化促 NPC 解聚（ref 54），但活细胞选择性扰动困难；NUP98 的重 O-GlcNAc 化（refs 47,48）使直接扰动成为可能；改变 O-GlcNAc 同时改变链段运动与核转运（Fig.4e,f），把 PTM tuning 落到 NPC 功能。态度：已证实（扰动+功能读数）；磷酸化对比为领域定位。

**第 4 层：径向组织的"意外"发现与中央栓/双路线假说。** 模拟在实验匹配强度下自发产生 importin-β 环周富集、FG 占中央；+20% 亲和力驱入中心（Fig.3b,c）。该组织与 ref 14 三维 MINFLUX 及本文二维 MINFLUX 一致；作者认为组织源于 grafting 几何与近壁 FG 密度偏高，并推测 importin-β 暴露沿 NUP98 位置变化→位置依赖回补（Fig.4c）。对电镜/高速 AFM 的中央栓（refs 55,56,21）给出互补视角：NPC 构象差异（in situ 收缩/扩张，ref 39）可能部分解释；AFM 中央栓高度移动（ref 21）符合动态运输相关组装而非刚性结构；本文数据不排除 importin-β 参与中央栓样密度，但中央轴非其主位置；提出"双路线"假说（小/中 cargo 走环周、大/慢 cargo 走中央；中央密度或为瞬态 cargo/复合物）——明确标注为推测框架。

**第 5 层：作者自陈局限（单独成层）。** (1) ref 14 报道的胞质远端 importin-β 高密度区未被模拟捕获，需对 NUP358 长链（有序域散布于长无序区）进一步实验表征以精化模型；(2) MINFLUX 以 NUP96 为支架参考、不直接解析内环直径，故不能排除 NPC 扩张/收缩对表观 importin-β 分布的影响；(3) 模拟未含分子老化，故不重现凝聚体长时间变慢（只给相对层级）；(4) ρslow 为表观参数、慢于寿命组分靠模型拟合，绝对旋转时间未定；(5) ε~ ±20% 的组织预测尚待"选择性改变 FG–importin-β 相互作用"的实验直接检验。态度：承认不确定性。

**第 6 层： broader IDP 框架与疾病意义。** 本研究示例细胞环境如何在拥挤环境中保存 IDP 功能动态，对 FG-NUP 功能障碍相关疾病（癌症、病毒感染、神经退行，refs 57,58）有启示；活细胞荧光+多尺度模拟为探天然环境 IDP 构象动力学的通用策略。态度：愿景/外推（推测）。

**Discussion 没有讨论什么（局限性）：**

(1) 无体内/疾病模型表型回补：O-GlcNAc/importin-β 扰动仅止于细胞系动力学与转运速率，未在任何动物或疾病模型（如神经退行、NUP98 融合白血病）验证"液化失衡→病理"的因果链，疾病意义停留在关联/愿景层。
(2) ρslow 的绝对物理意义未定：慢于 4 ns 寿命的组分靠模型拟合、精度随光子统计下降（refs 63,64），微秒尺度运动未测（需偏振 FCS，ref 35）；故"纳秒液态"不覆盖更慢的凝胶样模式是否存在。
(3) 糖基化位点化学计量/位置异构未解析：约 17 GlcNAc/链为部分修饰，哪些位点关键、是否需特定位置组合未做位点突变回补；"48 预测 vs 46 实验"为总数互证而非位点级互证。
(4) importin-β 回补的生理权重未定量：过表达为"近内源"水平（Supplementary Figs. 19–20）但回补仅部分；体外体系无 RanGTP/cargo 竞争，未讨论生理 cargo 负载下 importin-β 占用与液化作用的权衡。
(5) 径向组织的因果验证缺失：ε~ ±20% 仅模拟预测，未实验选择性改变亲和力；MINFLUX 为固定细胞二维，活细胞动态径向组织未直接验证。
(6) NUP358 长链与胞质远端高密度区未建模/未解释，模型对胞质侧屏障的覆盖不完整。
(7) 仅 NUP98 做活细胞 TRFA：其他 FG-NUPs（NUP62 复合物、NUP153、NUP214 等）的活细胞链段动力学未测；跨物种 PTM（酵母 O-甘露糖化/磷酸化）仅推测。
(8) 活细胞"无淀粉样化"缺直接结构证据：ThT/cryo-EM 仅体外；细胞内是否完全无有序聚集核心未以结构手段排除。
(9) 中央栓分子身份未定：dual-route 为假说，中央密度是否为瞬态 cargo 未直接成像验证。
(10) 老化不可逆的分子基础未解析：为何成熟后 importin-β 无效（淀粉样核心一旦形成即动力学陷阱？）未给结构/能量解释。

---

五、<重点思考>

**（一）核心概念/方法/通路/模型概括解读**

- **核心概念——表观链段运动度量 ρslow：** 内涵：TRFA 慢组分拟合时间尺度，读 IDP 局部（≤50 残基）链段纳秒摆动，而非整体旋转或绝对旋转时间。重要性：把"屏障液态/固态"从形态学/流变学争论变为可在活细胞单点测量的动力学判据。本文推进：首次给出活 NPC 内 15 位点 ρslow 谱（57–108 ns）与 2 h 稳定性，并证明体外凝聚体 ρslow 时间依赖升至拟合上限。边界：慢于寿命组分靠模型拟合、只作相对比较；微秒尺度不覆盖。
- **核心概念——FG 屏障的"细胞 tuning 材料态"：** 内涵：IDP 材料态非 intrinsic 固定，而由 PTM（O-GlcNAc）、NTR（importin-β）、纳米限域与 tethering 共同设定。重要性：统一液/固模型争议，并为 FG-NUP 疾病（癌症/病毒/神经退行）提供"液化失衡"机制入口。本文推进：双因子联合体外重现活细胞谱、临界点附近敏感性的物理放大机制。边界：体外最小体系仍不完全等于细胞（72 ± 3 vs 59 ± 14 ns）；疾病因果未验证。
- **核心方法——GCE-OTO + fluorogenic HD653 + 皮秒 TRFA：** 内涵：单点 ncAA 标记 + 自淬灭点亮染料 + 偏振分辨单光子计数，读活细胞 tethered IDP 链段运动。重要性：填补单分子追踪/FCS/FRAP/AFM 读不了"活细胞局部构象运动"的缺口。本文推进：15 位点扫描 + bootstrap 稳健拟合 + 全套光物理/标记对照。边界：光子统计限制慢组分精度；需逐位点构建体。
- **核心方法——双色 DNA-PAINT MINFLUX 径向组织分析：** 内涵：以支架（NUP96）八重参考系对齐、读另一通道（importin-β）径向密度，并以 2D 随机零模型排除几何伪影。重要性：把模拟预测的径向组织落到固定细胞纳米级成像。本文推进：n = 460 NPCs 的约 20 nm 峰 + 中央 depletion。边界：固定细胞、二维、不解析内环直径。
- **核心模型——实验匹配多尺度模拟（残基级 + Martini 2.2）：** 内涵：残基级模型做参数扫描/物理洞察（ε~ 匹配分配/密度/通量），Martini 加化学细节做显式糖基化（α/λ/γ 校准）。重要性：把材料态、空间组织、化学调控统一在一个可校准框架。本文推进：径向组织自发涌现、临界点定位、48 vs 46 位点互证。边界：未含老化；NUP358 长链/胞质远端未捕获；ε~ ±20% 预测待实验。
- **核心通路——O-GlcNAc/importin-β → FG–FG 有效吸引弱化 → 链段液化 + 径向组织 → 选择性快速转运：** 内涵：两因子互补弱化 cohesive FG 接触、维持动态网络与环周/中央分区，功能读数为毫秒穿越与 LINuS 输入速率。重要性：把 PTM/NTR 从"运输参与者"升级为"屏障材料态设定者"。本文推进：扰动-回补-功能闭环。边界：回补部分、位点级机制未解析。

**（二）本篇文章发现的完整概括：**

本文从"NPC 通透屏障物理态长期争议"出发，以位点特异遗传密码扩展标记 + 皮秒时间分辨荧光各向异性，首次直接测得活哺乳动物细胞 NPC 内 NUP98 FG 结构域呈纳秒级类液态链段运动（ρslow 57 ± 2–108 ± 5 ns，近 N 端快、近锚定端慢的位置梯度，2 h 稳定），而体外重构 FG 凝聚体在 1 h 内发生液-固转变并伴 ThT 阳性淀粉样化，聚集倾向段 85–124 内的残基 100 最敏感。追索维持液态的生理因子，发现 importin-β 以剂量依赖方式溶胀凝聚体、稀释聚集倾向段、跨位点延缓老化（1:1→4:1 使 221 位点 ρslow 120 ± 24→80 ± 7 ns），但成熟后补加无效（预防而非逆转）；O-GlcNAc 糖基化（约 17 GlcNAc/链的部分修饰即足够）同样延缓老化，降低细胞 O-GlcNAc 减慢链段运动与核输入、升高则几乎无额外效应（内源已足够），importin-β 过表达可部分回补降修饰表型；两因子联合在体外重现活细胞表观链段运动谱（221：72 ± 3 vs 59 ± 14 ns）。实验匹配的多尺度模拟进一步揭示：importin-β 偏环周富集、伸展 FG 占中央的径向组织自发涌现，对 FG–importin-β 亲和力精细平衡敏感（±20% 即破坏），并被固定细胞双色 MINFLUX（n = 460 NPCs，峰约 20 nm、中央 depletion 超随机零模型）验证；显式糖基化 Martini 模拟把 FG 从表面凝聚体推向中央伸展、匹配 in situ FLIM–FRET 构象并预测 48 位点（vs 爪蟾 46），且把 FG-NUPs 定位在相分离临界点附近。本文的领域贡献在于：(1) 以活细胞直接动力学测量裁决液/固模型争议，确立"细胞环境 tuning IDP 材料态"框架；(2) 把 importin-β 与 O-GlcNAc 从运输参与者升级为屏障材料态与空间组织的共同设定者，给出可校准的多尺度模拟框架；(3) 以径向组织统一 MINFLUX 环周轨迹与中央栓观察，提出双路线假说。同时以坦率态度划定边界：ρslow 为表观参数、体外体系不完全等于细胞、回补部分、径向组织因果与疾病意义待验证。

**1. 研究问题定位：**
交叉领域：细胞生物学 × 生物物理（荧光光谱/单分子成像）× 计算生物物理（多尺度 MD）× 糖生物学。问题层级：分子机制/机器组装层级（屏障材料态与空间组织），非组学图谱或临床层级。工作类型：概念创新（材料态裁决）+ 技术创新（活细胞单点 TRFA）+ 机制/结构性（多尺度模拟+MINFLUX）组合。实验层级：体外重构 + 活细胞/固定细胞 + 计算，无动物/临床。一句话核心定位：给"NPC 屏障是液还是固"的十年争议补上活细胞直接动力学证据，并把答案从"二选一"改写为"细胞环境设定的动态平衡"。

**2. 为什么能发 Nature（证据链评估）：**
最扎实处有三：其一，活细胞 vs 体外的对照设计本身——同一标记位点、同一读数（ρslow）在活细胞 2 h 稳定 vs 体外 1 h 老化 + ThT 独立结构读数，直接裁决争议而非间接推断；其二，参数化的闭环——模拟相互作用强度不是自由拟合而是被分配系数（ED3/4）、密相浓度、扩散/通量（ED5/6）、in situ FLIM–FRET 构象（Fig.5e）多重实验约束，且 48 vs 46 位点为独立互证；其三，扰动-回补-功能闭环——OSMI-4/Thiamet-G 双向扰动 + RL2 验证 + LINuS 功能读数 + importin-β 回补，把动力学落到功能。不足：ρslow 为表观参数、绝对物理意义受限；径向组织因果仅模拟预测（ε~ ±20% 未实验）；MINFLUX 固定细胞二维；疾病意义无体内验证；仅 NUP98 一种 FG-NUP 做活细胞测量。

**3. 创新点逐条列出：**
(1) 概念创新：活细胞 FG 屏障 = 纳秒类液态链段网络，体外凝聚体老化 ≠ 天然屏障（Fig.1h–j）。(2) 方法创新：GCE-OTO + fluorogenic HD653 + 皮秒 TRFA 的活细胞单点链段动力学平台（Fig.1a–g、ED1）。(3) 机制创新：importin-β 链段级液化 + 稀释聚集倾向段 + 不可逆性限定（Fig.2、ED2/3）。(4) 机制创新：O-GlcNAc 弱化 FG–FG 有效吸引、部分修饰即足够、内源已足够的负性限定（Fig.4a–c、ED8）。(5) 发现创新：importin-β 环周/FG 中央的径向组织自发涌现 + MINFLUX 验证 + 零模型对照（Fig.3）。(6) 调和性贡献：统一液/固模型、karyopherin 中心模型、MINFLUX 环周轨迹与中央栓观察，提出双路线假说（Discussion）。(7) 框架创新：临界点附近敏感性 + 显式糖基化 Martini 模型 + 48/46 位点互证（Fig.5、ED9）。

**4. 前置依赖：**
技术前置：GCE-OTO（refs 26,27）、fluorogenic HD653（ref 28）、TRFA/各向异性染料 Cy3B 与 segmental motion 分析（refs 30,31,32,33）、PAM-TauFit（ref 62）、MINFLUX\_NPC\_Tracking 流程（ref 14）、LINuS（ref 49）、Martini 2.2（refs 50,78）与蛋白–糖相互作用精化（refs 83,84）、LAMMPS/GROMACS（refs 68,69,80,81）。生物学概念前置：FG 水凝胶/选择性相（refs 5,6,13）、虚拟门控/刷（refs 9,15）、karyopherin 中心（refs 10,52）、聚集倾向段 85–124（ref 11）、淀粉样相互作用（ref 12）、O-GlcNAc 与 FG 水凝胶/转运（refs 47,48,49）、人源 NPC 结构（ref 39）、importin-β 结构（ref 73）。生信/进化前置：YinOYang 位点预测（ref 79）、O-GlcNAc Database v2.0（ref 92）、单链 smFRET/FLIM–FRET 构象基准（ref 26）。

**5. 基因编辑/遗传操作细节：**
其"遗传操作"实为体外蛋白工程 + 细胞系工程：(1) NUP98 15 个单点 TAG 构建体（A221TAG 等）用于 GCE 单点标记——设计价值：单点精度排除多标记/标签扰动，位点扫描读位置梯度；(2) BOC 对照 ncAA——排除非特异染料信号；(3) 体外 NUP98 FG(1–505) ΔGLEBS(157–213)——排除结构化区误折叠混杂；(4) 单 Cys 取代（36/100/221/312/387/482）用于 maleimide 染料标记——体外位点特异；(5) U-2 OS-CRISPR-NUP96-mEGFP 内源敲入 + 慢病毒 pTRIPZ-importin-β-3×FLAG-ALFA-P2A-tagBFP 诱导系——内源支架参考 + 近内源诱导表达（dox 0.5 µg/ml 24 h；总 KPNB1 无显著增加，Supplementary Figs. 19–20）排除过表达伪影；(6) 无传统基因敲除/敲入回补疾病模型——本文未涉及动物遗传操作。

**6. 与课题组/领域的关联：**
通讯作者 Lemke 主线为"遗传密码扩展 + 单分子/超分辨荧光读无序蛋白与核运输"（本文 GCE-OTO、TRFA、前作 ref 26 均其体系）；Hummer 主线为"生物分子模拟/粗粒化力场与凝聚体物理"（本文残基级 + Martini、蛋白–糖力场 ref 83 均其体系）；Tang 提供 MINFLUX 平台与资源。本文是两条主线（活细胞荧光测量 × 多尺度模拟）在 NPC 屏障问题上的交汇。研究谱系定位（PDF 内可锚定）：直接地基前作 = Yu et al. Nature 617, 162–169 (2023)（ref 26），确立"活细胞/透化细胞 NPC 内 NUP98 构象偏好 + GCE-OTO 标记 + 残基级 NPC 模型"；本文是其"从静态构象偏好到活细胞动力学 + 从单因子到双因子材料态调控 + 从构象到空间组织"的延伸。并行/互补工作：Sau et al. Nature 640, 821–827 (2025)（ref 14，MINFLUX 环周轨迹）、Kozai et al. Nat Cell Biol 27, 2089–2101 (2025)（ref 21，hsAFM 中央栓动态与 karyopherin 重塑）、Dekker et al. Nat Commun 16, 11497 (2025)（ref 40，酵母 Kap 中心全氨基酸分辨率模拟）、Raveh et al. PNAS 122, e2507559122 (2025)（ref 23，整合映射）。对读者方向参考：若研究 IDP/凝聚体材料态、核运输、糖基化或超分辨成像，本文提供"活细胞动力学读数 + 实验匹配模拟"的可迁移范式。（通讯作者详细履历/奖项/基金等 PDF 外事实详见同源背景解读。）

**7. 数据与材料可及性：**
结构：PDB 7R5K（人源 NPC 支架）、3W5K（importin-β）。模拟轨迹/初始构型：Zenodo 10.5281/zenodo.15025565（LAMMPS）、10.5281/zenodo.17588507（GROMACS），CC BY 4.0。测序：原文未提供 GEO/公共测序 accession（无高通量测序）。位点注释：O-GlcNAc Database v2.0 (https://www.oglcnac.mcw.edu/)。代码：PAM (gitlab.com/PAM-PIE/PAM v1.4)、MINFLUX\_NPC\_Tracking (github.com/npctat2021/MINFLUX\_NPC\_Tracking)、insane.py、BUMPy、martinize.py、DSSP、YinOYang；MATLAB R2024a 自定义分析。试剂/细胞：COS-7 (Sigma 87021302)、HEK293T (Beyotime C6008)、U-2 OS-CRISPR-NUP96-mEGFP (Cytion 300174, Y. Li 惠赠)；HD653 由 Wombacher 实验室惠赠；OGT 由 Dormann 实验室 S. Hutten 惠赠；抗体 RL2 (Invitrogen MA1-072)、抗 KPNB1 (Abcam ab2811)、抗 FLAG (Proteintech 66008-4-Ig)、抗 α-Tubulin (ABclonal AC012)；纳米抗体-DNA 偶联物 Massive Photonics 定制。补充材料：Supplementary Figs. 1–20、Videos 1–9、Tables 1–6、Text 未随本 PDF 提供；未裁剪印迹见 Supplementary Fig. 20；Source Data 随论文提供。

**（三）面向阅读的核心提问（问题 seeding）**

- **问题 1：液化是 importin-β/糖基化的直接因果，还是伴随现象？** 本文能答：体外共相分离 + 酶法糖基化 + 细胞双向扰动 + 回补构成因果链（Fig.2/4），但细胞回补仅部分（100 位点）、且无位点级机制。证据强度：强（体外）/中（细胞）。交接：位点级因果与生理权重 → 待背景解读跨文献精研。
- **问题 2：ρslow 到底测的是什么运动？能否跨研究比绝对值？** 本文能答：明确定义为表观链段度量、慢于寿命靠拟合、只作相对比较（Methods、ED1d）；微秒尺度未测。证据强度：中（自陈边界清晰）。交接：与偏振 FCS/单分子方法的绝对尺度对接 → 待背景解读。
- **问题 3：径向组织是否因果决定转运选择性/速率？** 本文能答：ε~ ±20% 仅模拟预测 + 固定细胞 MINFLUX 相关 + 通量峰在匹配值（ED6c）；无实验选择性改亲和力。证据强度：中-弱。交接：与 Sau 2025、Kozai 2025、Kapinos 2017 的跨文献因果证据综合 → 待背景解读。
- **问题 4：体外老化是否等于细胞内病理固化？神经退行关联有多实？** 本文能答：ThT/淀粉样仅体外；细胞内 2 h 无转变但无结构直接证据；疾病仅 refs 57,58 关联。证据强度：中（体外）/弱（疾病）。交接：FG 聚集与神经退行的跨文献证据分级 → 待背景解读。
- **问题 5：约 17 GlcNAc/链的部分修饰为何足够？哪些位点关键？** 本文能答：总数互证（48 vs 46）+ 空间模式跟随预测倾向（ED8a），但无位点突变回补。证据强度：弱-中。交接：Labokha 2013 位点级数据与 O-GlcNAc 数据库 → 待背景解读。
- **问题 6：中央栓的分子身份与 dual-route 假说能否成立？** 本文能答：中央轴非 importin-β 主位置 + AFM 中央栓高移动（ref 21）+ 构象差异（ref 39）；dual-route 明确为推测。证据强度：弱。交接：Akey 1993/Beck 2004/Kozai 2025 跨文献综合 → 待背景解读。
- **问题 7（听众视角）：核孔里塞满这么密的 FG 链，运输会不会堵塞？体外是凝胶/固体态，体内为何不堵？** 本文能答：这正是全文以最强证据回答的核心问题——活细胞 NUP98 FG ρslow 57–108 ns、2 h 稳定（Fig.1e–g,i），而体外凝聚体 1 h 内液-固转变并 ThT 淀粉样化（Fig.1j、2c）："堵"是失去细胞守护后的老化轨迹，而非天然态。守护者有二：importin-β 剂量依赖液化、稀释聚集倾向段 85–124（Fig.2），O-GlcNAc 弱化 FG–FG 有效吸引（Fig.4/5），二者联合在体外重现活细胞谱（221 位点 72 ± 3 vs 59 ± 14 ns，Fig.4i）。课本化背景：屏障不是静态筛子而是多价弱相互作用的动态网络，NTR·cargo 经数千次瞬态 FG 接触"溶入"网络通过（选择性相/虚拟门线，见上文背景补注），密度提供选择性、动态提供速度。功能闭环：模拟首通时间 1–10 ms 与实验转运速率吻合、通量在匹配亲和力处达峰（ED5/6）；OSMI-4 降糖基化即减慢核输入（P = 0.0053）。限定：2 h ≠ 终身——NPC 支架是极长寿命蛋白（Savas 2012, ref 51），衰老相关 NPC 退化与核渗漏（D'Angelo 2009, ref 58）提示"堵"在衰老/疾病中确会发生，本文未测体内长时程。证据强度：强（活细胞短时程+体外机制）/弱（长时程与疾病）。交接：体内长时程、衰老/疾病模型守护失效 → 待背景解读跨文献精研。
- **问题 8（听众视角）：cargo 到底走中央还是走边缘？** 本文能答：可给"优先走边缘、中央是屏障主体"的有边界回答——实验匹配亲和力（ε~ = 0.42）的模拟自发产生 importin-β 环周富集、伸展 FG 占中央通道（Fig.3a–c）；固定细胞双色 MINFLUX（n = 460 NPCs）直接测得 importin-β 径向密度峰约 20 nm、中央 depletion 超 2D 随机零模型（Fig.3f,g），与 Sau 2025（ref 14）透化细胞环周偏好轨迹一致。作者进而提出 dual-route 假说：与 NTR 高效结合的小/中 cargo 优先走环周，大或慢运 cargo 占中央通道，部分中央栓样密度可能是瞬态 cargo/运输复合物而非永久栓（Discussion 明确为推测）。须守三条边界：中央轴非 importin-β 主位置 ≠ 中央密度排除 importin-β；中央栓分子身份未定（Akey 1993 ref 55、Beck 2004 ref 56、Kozai 2025 ref 21 示其高移动）；固定细胞 2D 成像不能排除 NPC 扩张/收缩影响。证据强度：中（模拟+固定细胞相关+独立追踪三方一致，但无活细胞因果）；dual-route：弱（假说，未直接检验）。交接：活细胞 3D 追踪、中央栓成分、亲和力直接扰动实验 → 待背景解读 B.4。
- **问题 9（听众视角）：这么密的无序链，怎么让大分子快速通过？"密"不等于"慢"吗？** 本文能答：关键是"弱而快"而非"强而慢"——FG–NTR 是多价低亲和结合、on-rate 近扩散限制、快速交换（Milles 2015, ref 24），cargo 经数千次瞬态接触"溶入"FG 网络而非挤过固定孔洞；本文活细胞纳秒链段运动为这一图景提供直接动力学地基（Fig.1）。定量上：模拟估 importin-β 穿越凝聚体首通时间 1–10 ms，与实验核转运速率吻合（Ribbeck 2001 ref 43、Kubitscheck 2005 ref 45 单分子停留约 5.8/7.1 ms、Frey 2007 约 12 ms，详见同源背景解读）；且通量在 ε~ ≈ 0.40–0.42 达峰、亲和力 ±20% 即破坏组织——结合太强反而慢，"finely balanced"（ED6c、Fig.3）。课本化背景：选择性来自多价弱结合的分配而非尺寸筛孔，密度提供选择性、动态提供速度。证据强度：中-强（模拟+跨文献动力学一致；1–10 ms 为模拟值而非直接单分子测量）。交接：绝对速率标定与单分子停留时间测量 → 待背景解读。

以上问题中，纯本文可答的已全部就地作答，其余转入同源《背景解读》做跨文献证据综合与分级。问题 7–9 为组会听众/非本领域同行会脱口而出的直觉性大问题，已就地用本文证据与课本化背景作答。

**（四）延伸文献与图引清单**

下表给出读懂本文/继续研究/组会 PPT 摘图所必需的前人文献，分 A 论证依赖与 B 方法来源；★ 为必读。图号经 EuropePMC/PMC 全文 XML 核实者给出具体编号，核不到者标"编号待核"，不编造。

| 序号 | 文献(年/刊/本文ref) | 对应本文Fig/论点 | 重点前人Fig(panel) | 一句话讲点 | 获取/阅读深度 |
| --- | --- | --- | --- | --- | --- |
| 1 ★ | Yu et al., Nature 2023 (ref 26) | Fig.1a,d 标记策略；Fig.5e/ED9e R\_E 基准；全文地基 | Fig.1(a–d) GCE-OTO 单点标记；Fig.2 FLIM–FRET pipeline；Fig.3 标度律 ν=0.56±0.03；Fig.4 残基级 NPC 模型 | 活细胞 NPC 内 FG 链比体外凝聚体更伸展、构象偏好可由粗粒化模型复现——本文动力学测量的静态地基 | OA PMC10156602；全文精读 |
| 2 ★ | Sau et al., Nature 2025 (ref 14) | Fig.3f,g 径向组织对比；Discussion dual-route | Fig.4(a) 体积校正径向密度；Fig.3 导入/输出轨迹；Fig.2 双向追踪 | NTR-cargo 轨迹偏环周、中心快速通过——本文径向组织的独立活细胞/透化细胞锚点 | OA PMC12003200；全文精读 |
| 3 ★ | Frey, Richter & Görlich, Science 2006 (ref 13) | 引言液-固争议；Fig.1j 老化对照 | 建议摘其 FG 水凝胶网络/流变图（编号待核） | FG 重复序列体外自组装成水凝胶 meshwork——"固体屏障"模型的起点 | 订阅；摘要+本文转述 |
| 4 | Frey & Görlich, Cell 2007 (ref 5) | 选择性相模型；Fig.2 体外凝聚体背景 | 建议摘其饱和水凝胶通透选择性图（编号待核） | 饱和 FG 水凝胶可复现 NPC 通透选择性——但本文证明其会老化 | 订阅；摘要+本文转述 |
| 5 ★ | Ibáñez de Opakua et al., Nat Chem 2022 (ref 11) | Fig.1j/2c,d 残基 100 与 85–124 段 | Fig.3 cryo-EM 纤维多晶型；Fig.4 F102 跨链相互作用；Fig.6 低稳定性 | NUP98 85–124 是淀粉样倾向核心但其 FG 簇稳定性低——解释为何细胞内不固化 | OA PMC9630130；定向核读 |
| 6 ★ | Labokha et al., EMBO J 2013 (ref 48) | O-GlcNAc 立论；46 位点；Fig.4g–i | Fig.5 Nup98 水凝胶分析；Fig.6 WGA 阻断 O-GlcNAc 凝胶通透；Fig.7 ssNMR | 爪蟾 NUP98 46 个 O-GlcNAc 位点调控水凝胶材料性质——本文糖基化液化的直接前作 | OA PMC3553378；定向核读 |
| 7 | Yoo & Mitchison, JCB 2021 (ref 49) | Fig.4d–f LINuS 与转运速率 | Fig.1 LINuS 验证；Fig.2 O-GlcNAc 依赖速率；Fig.4 中央通道 O-GlcNAc 富集 | O-GlcNAc 水平双向调节核转运速率——本文把速率变化落到纳秒链段运动 | OA PMC8091080；定向核读 |
| 8 | Mosalaganti et al., Science 2022 (ref 39) | Fig.3/5 模拟支架几何 (7R5K) | 建议摘其整合结构/收缩态 NPC 图（编号待核） | AI 辅助整合结构给出人源 NPC 收缩态支架——本文模拟的几何地基 | 订阅；摘要+本文转述 |
| 9 | Werther et al., ACS Cent Sci 2021 (ref 28) | Fig.1b HD653 fluorogenic 标记 | Fig.1 近距淬灭设计；Fig.2 淬灭/光物理；Fig.5 HD653 STED | 四嗪自淬灭硅罗丹明 HD653 实现免洗活细胞标记——本文低背景 TRFA 的探针来源 | OA PMC8461766；定向核读 |
| 10 | Milles & Lemke, Angew Chem Int Ed 2014 (ref 31) | ρslow 方法学；≤50 残基关联长度 | 建议摘其 segmental motion 分析图（编号待核） | 用各向异性慢组分读 IDP 链段运动而非整体旋转——本文 ρslow 的方法学原点 | 订阅；摘要+本文转述 |

---

**解读完成度声明：** 主文 Fig. 1–5 全部 panel（共 39 个：Fig.1=10[a–j]、Fig.2=7[a–g]、Fig.3=7[a–g]、Fig.4=9[a–i]、Fig.5=6[a–f]）均已按四字段模板（图片解释/横纵轴定义/颜色含义/核心结论）解读；Extended Data Fig. 1–9 全部 45 个 panel（ED1=5、ED2=10、ED3=5、ED4=3、ED5=4、ED6=3、ED7=3、ED8=6、ED9=6）以合并条目覆盖并逐 panel 说明差异。补充材料（Supplementary Figs. 1–20、Videos 1–9、Tables 1–6、Text）**未随本 PDF 提供**，未渲染、未断言其视觉细节，仅在引用处括注内容角色（如 Supp Fig.1–2 衰减/收敛、Supp Fig.3–10 扩散/组织/动力学、Supp Fig.11–18 糖基化/demixing、Supp Fig.19–20 表达量/未裁剪印迹、Supp Table 6 拟合参数）。图表视觉细节经 PyMuPDF 图区裁剪渲染（主图约 140 dpi、ED 约 110 dpi、Fig.4 统计括号 300 dpi）目视核对；坐标轴、配色、P 值括号归属以渲染图为准。原文未提供定量数据处（免疫印迹/凝胶灰度、MINFLUX 单孔定位数、代表性图像 n/p）一律如实标注，未予虚构。公式（TRFA 式 1–8、LINuS 拟合、模拟势函数式 9）以文字+符号转述，未重排推导；ρslow 接近 1000 ns 上限者按原文判为"极慢、未定量解析"。出版状态：Nature 2026 在线发表，EuropePMC firstPublicationDate = 2026-11-11（PDF 首页日期栏为占位符，不采信）；DOI 10.1038/s41586-026-11258-0；等贡献脚注9逐字转述（Yu 与 Heidari），未升格共同一作。延伸文献与图引清单已附（10 条、★5，图号经 PMC 全文核实或标"编号待核"）；figure 解读已通过"技术零基础自足性"自检（每 panel 交代测量物理量/信号来源/轴与方向换算/逐通道颜色）；统计显著性星号与字面 \* 均已转义（如 \*\*\*\* 对应 P < 0.0001），本文 P 值以原文数值呈现。v6.5 升级说明：本轮在 v6.4 基础上新增研究传承线背景补注 4 条（FG 水凝胶与液-固相变线、O-GlcNAc 糖基化线、TRFA 链段运动方法线、MINFLUX 开发史线，插入“一、<基础概念注释>”对应分类末尾），并在重点思考（三）seeding 增补听众视角直觉性大问题 3 个（问题 7–9：核孔会不会堵/cargo 走中央还是边缘/密无序链何以快速通过），均就地以本文证据+课本化背景作答；新增外部事实（Holt & Hart 1986、Kreppel 1997、Gao 2001、Bond & Hanover 2013、Balzarotti 2016/2017 作者串、Gwosch 2020、Patel 2015）经 EuropePMC REST 核证，Torres & Hart 1984 标“参考提供/待核”；既有 54 条概念注释、69 条四字段图解读与延伸清单未改动。