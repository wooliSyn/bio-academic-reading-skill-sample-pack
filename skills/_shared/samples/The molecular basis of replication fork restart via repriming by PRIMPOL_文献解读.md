**文献信息：** The molecular basis of replication fork restart via repriming by PRIMPOL. Jinho Park, Luke D. Lynch, Elena Blanco-Romero, Roberto Masdemont-Maestro, Juan Méndez & Gheorghe Chistol. *Nature*, Article（2026-11-11在线发表，经EuropePMC firstPublicationDate核证；所给PDF清样首页"Published online: xx xx xxxx"为占位符、不具权威性，Received 14 May 2026, Accepted 7 October 2026）, DOI 10.1038/s41586-026-11276-y (2026). 第一作者单位：Stanford School of Medicine, Chemical and Systems Biology Department（Jinho Park）；第二署名作者 Luke D. Lynch（Stanford, Biochemistry）与第三署名作者 Elena Blanco-Romero（CNIO, Madrid）贡献相等（PDF等贡献脚注仅覆盖此二人，不含第一作者Park，故非"共同一作"）；通讯作者 Gheorghe Chistol（Stanford School of Medicine / Stanford Cancer Institute）；细胞与DNA fibre部分由 Juan Méndez 团队（Spanish National Cancer Research Centre, CNIO, DNA Replication Group, Molecular Oncology Programme）完成。Open access（CC BY-NC-ND 4.0）；同行评审信息：Nature 感谢 Luis Blanco 及匿名审稿人（Peer review information 页）。

**一句话概括：** 单分子成像证明：PRIMPOL（引物酶-聚合酶）的叉重启不是单链DNA上的随机重新引发，而是"双锚定"——N端结合CMG（CDC45–MCM2–7–GINS）的MCM4、C端结合复制蛋白A（RPA），在解偶联解旋酶后方合成前导链引物并交给聚合酶ε；高浓度或检查点激酶1（CHK1）磷酸化才启用远离CMG引发、聚合酶δ延伸的次模式，为肿瘤治疗提供新靶点。

**解读说明：** 本解读基于所给PDF的正文（Abstract、Introduction、Results 8个小节、Discussion）、Methods、Reporting Summary，主文 Fig. 1–5（共46个panel：Fig. 1 = 11、Fig. 2 = 8、Fig. 3 = 9、Fig. 4 = 6、Fig. 5 = 12），以及随同一PDF提供的 Extended Data Fig. 1–7（共48个panel：ED1 = 9、ED2 = 5、ED3 = 10、ED4 = 8、ED5 = 3、ED6 = 6、ED7 = 7）；ED图按内容角色在对应Section内整合解读。Supplementary Tables 1–4（IP–MS结果、引物列表、抗体列表、全部精确P值）与 Supplementary Data 未随本PDF提供，一律标注"未提供"。图表经150 DPI逐页渲染后视觉审读并与caption交叉核对；kymograph（时间-位置图）均注明阅读方向；免疫印迹与自显影为代表性图像，原文未提供灰度定量数值（co-IP有Fig. 3e定量、ensemble复制有Fig. 1k/3g定量除外），凡未提供者如实标注。本文为已通过同行评审的Nature在刊文章（2026-11-11在线发表，EuropePMC核证），非预印本。模式判定：模式A（研究型论文）。

---

一、<基础概念注释>

**复制与复制应激核心概念**

- **复制应激（RS, replication stress，复制应激）：** 指任何阻碍复制叉正常前进的内源或外源干扰（DNA损伤、癌基因激活、化疗药物等），导致复制叉停滞甚至崩塌（Introduction第1段，ref 5）。本文用两种正交手段在体外制造RS：免疫耗竭Pol α、以及在前导链模板上放置位点特异性肽加合物；另用aphidicolin作为"抑制复制聚合酶"的工具性RS对照。
- **复制叉重启（replication fork restart，复制叉重启）：** 停滞的复制叉恢复DNA合成与前进的过程。本文的操作性定义是单分子kymograph上CMG（或RPA tract）从慢速（~30 nt/min）突然切换回快速（~300 nt/min）并伴随新生DNA标记积累（Fig. 1e,h）；细胞层面则用DNA fibre上UV-C后IdU掺入来定义（Fig. 3h,i）。
- **Repriming（重新引发，重引发）：** 2013年发现的RS耐受通路：不在损伤处继续合成，而是由PRIMPOL在损伤下游的ssDNA上重新合成一段引物、跳过损伤留下ssDNA gap（Introduction第1段，refs 1–4）。本文的核心贡献是给这一通路补上"在哪里引发、引物交给谁、如何被调控"的分子机制。
- **CMG解偶联（helicase–polymerase uncoupling，解旋酶-聚合酶解偶联）：** 前导链聚合酶停滞而CMG解旋酶继续解链，产生长段RPA包被ssDNA的状态（Introduction第2段，refs 25–28）。本文以"CMG速度从~300降到~30 nt/min且无新生DNA信号"作为解偶联的单分子判据（Fig. 1c,d,g,h）；解偶联是双锚定机制得以成立的前提——只有解偶联叉后方才同时存在RPA–ssDNA与裸露的CMG docking位点。
- **前导链/后随链与冈崎片段（leading/lagging strand, Okazaki fragments）：** 前导链连续合成（Pol ε），后随链不连续合成（Pol α引发、Pol δ延伸冈崎片段）（Introduction第2段，ref 24）。后随链损伤可被不连续合成天然绕过，前导链损伤则使Pol ε停滞而CMG继续解链——这一不对称性是"PRIMPOL主要作为前导链引物酶"假说的生物学基础（ref 2提出、本文Fig. 2a与Fig. 4d证实）。
- **ssDNA gaps（单链DNA缺口）：** repriming跳过损伤后留在子代DNA上的单链区（refs 16,17）。其临床意义在于使细胞对PARP抑制剂敏感（refs 18–20），是repriming作为肿瘤治疗靶点的逻辑起点（Introduction第1段）。
- **Fork reversal（复制叉反转）：** 另一条RS耐受通路，新生链回退配对形成"鸡爪"结构（ref 6）。与repriming存在竞争关系：阻断反转会增强repriming（refs 7,21,22），提示细胞优先使用高保真通路（Introduction第1段）。本文未直接研究反转，但Discussion的治疗策略置于这一通路竞争背景下。
- **TLS（translesion synthesis，跨损伤合成）：** 由低保真聚合酶直接在损伤对面合成以绕过损伤的通路（ref 6）。本文中损伤底物在无PRIMPOL时约7%的低效重启被归因于TLS（Fig. 1f，refs 47,48），作为repriming的背景对照。
- **Origin licensing / firing（复制起点许可/激活）：** G1期MCM2–7双六聚体装载到DNA（licensing），S期组装成CMG并启动复制（firing）（Fig. 1a，ref 32）。本文用HSS（只支持licensing）与NPE（支持firing与延伸）两步灌流在体外重建细胞周期顺序；checkpoint激活会抑制firing（Extended Data Fig. 2d的CDC45 blot），这是解释ensemble assay中DNA合成总量不完全回补的关键。
- **DNA损伤检查点（ATR–CHK1 checkpoint，DNA损伤检查点）：** 感知RPA–ssDNA并经ATR磷酸化CHK1（Ser345）的信号 cascade（ref 28）。已知CHK1磷酸化PRIMPOL Ser255促进repriming（ref 22）。本文发现检查点激活对主模式（CMG依赖）非必需、只上调次模式（CMG非依赖）（Fig. 4e,f；ED7）。
- **Primer handover（引物交接）：** 引发酶合成的短引物被复制聚合酶捕获并延伸的过程。本文区分两种交接路径：PRIMPOL→Pol ε（CMG依赖主模式）与PRIMPOL→Pol δ（CMG非依赖次模式），用聚合酶耗竭+回补的遗传上位性设计判定（Fig. 4d）。

**关键蛋白与复合物**

- **PRIMPOL（primase–polymerase，引物酶-聚合酶）：** 兼具引物酶与DNA聚合酶活性、无校对功能的酶，错误率10⁻²–10⁻⁴，与TLS聚合酶相当（Introduction第1段，refs 9,10）；2013年被鉴定为repriming执行者（refs 1–4）。本文全部机制围绕它展开：爪蟾卵提取物中检测不到内源PRIMPOL（ED1a,b），故补充重组人PRIMPOL（3–100 nM）重建通路；人细胞内源浓度约17 nM（OpenCell，ref 49），本文称10–30 nM为近生理浓度。
- **PRIMPOL N端MCM4互作界面（残基29–35，含Arg29/Arg31/Lys34）：** 位于N端无序区（Mod N/N helix之间）的一段碱性残基，AlphaFold3预测与MCM4酸性残基形成盐桥（Fig. 3a,b；ED4a,b）。本文证明该界面是PRIMPOL被募集到停滞叉、以及高效重启所必需（Fig. 3c–i），是全文的机制核心与"抑制repriming"的药物设计落点。
- **PRIMPOL催化中心（D114/E116）：** 引物酶与聚合酶共用的催化酸性残基；D114A/E116A（AxA）使两种活性同时丧失（refs 2,3；ED1c,d）。在本文中用作"催化死但保留全部互作"的解耦工具。
- **PRIMPOL C端RPA互作界面（D519/F522/D551/I554）：** 与RPA结合的C端界面（ref 30）；四突变（ΔRPA）保留催化活性但丧失RPA结合与染色质募集（ED1d；ED2d,e）。在本文中用作"有活性但无募集"的解耦工具，与AxA互补。
- **PRIMPOL自抑制环（残基201–260，含Ser255）：** ref 22提出的无序自抑制loop，CHK1磷酸化Ser255解除自抑制。本文用Δ201–260（loop换柔性linker）与S255E/D/A磷酸化突变体检验，发现该调控只作用于CMG非依赖次模式（Fig. 4e,f）。
- **CMG（CDC45–MCM2–7–GINS，复制解旋酶）：** 真核复制解旋酶，解开亲代DNA并与Pol ε功能偶联（refs 23,24）。本文中CMG既是解偶联信号的来源，又是PRIMPOL的募集平台（经MCM4/MCM7）；用GINS–LD655荧光标记追踪其位置与速度（Fig. 1）。
- **MCM4 / MCM7：** CMG六聚体环中相邻的两个亚基。AF3预测PRIMPOL N端同时接触MCM4（主）与MCM7（辅）（Fig. 3a；ED4a,b）；MCM4界面突变（3A/DED/Linker）显著削弱结合与重启，而3A的温和表型被归因于MCM7接触的残留（Fig. 3f,g；Discussion未展开）。MCM7 C端还是CTF18的结合位点（ref 45），被作者用作"正常复制时PRIMPOL docking位点被遮蔽"假说的结构依据（推测）。
- **Pol ε（polymerase ε，DNA聚合酶ε）：** 前导链复制聚合酶，物理拴系于CMG（refs 54–56）。本文证明CMG依赖重启的引物由Pol ε延伸：耗竭Pol ε消除该模式、回补100 nM（人细胞浓度，ref 49）完全回补（Fig. 4d）。
- **Pol δ（polymerase δ，DNA聚合酶δ）：** 后随链复制聚合酶（ref 24）。本文证明CMG非依赖重启的引物由Pol δ延伸：耗竭Pol δ消除该模式、回补400 nM（人细胞浓度）完全回补（Fig. 4d）；且该模式合成速度~700 nt/min快于CMG依赖的~300 nt/min（Fig. 4c）。
- **Pol α（polymerase α–primase，DNA聚合酶α-引物酶）：** 负责起始与后随链引发（ref 24）。本文免疫耗竭Pol α制造RS（前导链合成无法建立，refs 42,43），耗竭后残留<1% Pol α用10 µM CD437抑制（Methods；ED2c）；Pol α耗竭同时激活检查点（ED2c pChk1），是ensemble回补不完全的原因。
- **RPA（replication protein A，复制蛋白A）：** 真核ssDNA结合蛋白，快速包被解偶联产生的ssDNA（ref 28）。与PRIMPOL的关系存在文献矛盾：高浓度RPA抑制PRIMPOL（ref 30）vs RPA刺激PRIMPOL并与Pol ε协同（ref 31）。本文用RPA–mCherryXL实时显示ssDNA范围，并以"双锚定+RPA瞬态解离"模型调和矛盾（Fig. 2a；Fig. 5）。
- **PCNA（proliferating cell nuclear antigen，增殖细胞核抗原）：** 滑动夹，新生DNA的标志（refs 44,45）。本文用PCNA–LD655作为FEN1–KikG的正交验证（ED1g），并解释FEN1信号依赖PCNA而非FEN1酶活（ED1h,i）。
- **FEN1（flap endonuclease 1，瓣状内切酶1）：** 冈崎片段成熟因子，经与PCNA互作被募集到新生DNA（ref 36），其酶活非标记所必需（ref 37）。本文以FEN1–KikG融合蛋白作为新生DNA报告子（信噪比优于PCNA–LD655，Methods）；FFAA突变（F343A/F344A）破坏PCNA结合后信号消失但重启不受影响（ED1h,i），完成标记 validity 验证。
- **CTF18-RFC：** 替代PCNA装载复合物，可在前导链新生DNA上装载PCNA（ED6b caption）。本文用它解释"Pol α+Pol δ双耗竭（后随链阻断）时FEN1仍积累在重启叉后方"的现象（ED6b）；Discussion另用CTF18结合MCM7 C端（ref 45）推测正常复制时PRIMPOL docking位点被空间遮蔽（推测）。
- **Twinkle / mtSSB / Pol γ（线粒体对照系统）：** 线粒体解旋酶、ssDNA结合蛋白与复制聚合酶。Discussion指出PRIMPOL与Twinkle、mtSSB、Pol γ互作（refs 9,61），与核内CMG/RPA/Pol ε-δ形成平行类比，并据此提出"CMG非依赖repriming可能是PRIMPOL为mtDNA后随链引发的原始功能残留"的假说（推测，refs 61,62）。

**突变体与工具试剂**

- **PRIMPOL(AxA)（D114A/E116A）：** 催化死突变体（refs 2,3）。保留RPA与MCM4结合、能募集到染色质（ED2d,e），但不能重启；在单分子上表现为"反复结合停滞叉却不重启"，故fork-proximal结合频率最高（Fig. 2d）。设计价值：把"催化"与"募集/结合"解耦。
- **PRIMPOL(ΔRPA)（D519R/F522A/D551R/I554A）：** RPA结合缺陷突变体（ref 30）。有催化活性（ED1d）但几乎不结合ssDNA–RPA（Fig. 2d,e，与游离AF647背景无异）、不上染色质（ED2d,e）、不重启。设计价值：把"RPA募集"与"催化"解耦，确立RPA互作的必要性。
- **PRIMPOL(3A)（R29A/R31A/K34A）：** MCM4界面中性化突变。fork-proximal结合时长缩短（Fig. 3c）、co-IP减弱（Fig. 3d,e）、ensemble重启温和缺陷（Fig. 3f,g）、细胞fibre重启下降但重复间变异大致NS（Fig. 3i）。设计价值：检验MCM4盐桥预测；温和表型提示MCM7接触残留。
- **PRIMPOL(DED)（R29D/R31E/K34D）：** MCM4界面电荷反转突变。结合时长、co-IP、ensemble与细胞fibre均显著缺陷（Fig. 3c–i），但保留CMG非依赖重启（Fig. 4b；ED5）。设计价值：比3A更强的界面破坏，且作为"两种重启模式解耦"的关键试剂。
- **PRIMPOL(29–35:Linker)（29–35替换为GGGSGGGS）：** 删除界面侧链、保留长度的linker替换突变。表型与DED类似（Fig. 3c–i）；细胞中表达量较低、接近内源水平（ED4g），作者如实注明。设计价值：排除"点突变破坏局部折叠"的替代解释（整段侧链删除仍缺陷）。
- **PRIMPOL(EREDED)（K8E/E13R/R15E/R29D/R31E/K34D）：** 同时破坏MCM4与MCM7预测接触的六突变。体外酶活下降（ED4d），作者放弃进一步研究（原文如实报告的负性结果）。设计价值与局限：本想一步双界面解耦，但因催化受损无法区分"互作缺陷"与"酶活缺陷"。
- **PRIMPOL(Δ201–260)（201–260替换为SGSETPGTSESATPES）：** 自抑制loop删除、表型模拟磷酸化（ref 22）。CMG依赖重启与WT相当（~80–90%），CMG非依赖重启最高（~70%，30 nM）（Fig. 4e,f）。设计价值：把"解除自抑制"的效应定位到次模式。
- **PRIMPOL磷酸化突变体（S255E / S255D / S255A）：** 磷酸模拟（E/D）与磷酸死（A）（ref 22）。30 nM下CMG依赖重启均与WT相当；CMG非依赖重启S255E/D居中（~40%）、S255A与WT同（~25%）（Fig. 4e）。设计价值：证明CHK1位点只调控次模式；S255A≈WT与"flow-cell内检查点不激活"自洽（ED7f caption）。
- **FEN1(FFAA)（F343A/F344A）：** 破坏FEN1–PCNA互作的突变（ED1h）。FEN1–KikG信号消失但重启效率不变（ED1i，N=114 vs 234，ns），证明标记信号来自PCNA募集而非FEN1酶活或 nonspecific 结合。
- **Aphidicolin（APH，蚜肠菌素）：** B家族聚合酶（α/ε/δ）抑制剂，不抑制PRIMPOL（ED1d）。本文用10–15 µM制造"聚合酶全抑"型RS（Fig. 1c标10 µM、正文15 µM；ED4e 15 µM；ED2e染色质分级用100 µM）；该条件下加PRIMPOL不能重启（ED1e），因为引物无人延伸——用作"重启需要复制聚合酶延伸"的逻辑对照，也用作让PRIMPOL反复结合而不重启的"结合时长测量窗口"（Fig. 3c）。
- **AZD6738（ATR抑制剂）：** 阻断CHK1 Ser345磷酸化（ED7a）。3 µM处理Pol α耗竭提取物反而增强PRIMPOL依赖的DNA合成（ED7b,c），证明检查点激活非repriming所必需、且检查点通过抑制origin firing压低总合成量。
- **CD437：** Pol α抑制剂，10 µM用于压制免疫耗竭后残留的<1% Pol α（Methods；ED2c）；作者用ensemble assay验证该浓度不损伤PRIMPOL活性。
- **肽加合物 / DPC（DNA–protein crosslink，DNA-蛋白交联）：** 本文的位点特异性前导链损伤：30 kb λ DNA两端各~10 kb处放置DPC，经proteinase K消化留下~4 aa肽加合物（ED2a；Methods，ref 25）。小尺寸可穿过CMG中央通道（ref 46）而不堵解旋酶，只停滞Pol ε，从而精确制造"前导链损伤型解偶联"；与Pol α耗竭互为正交RS来源。

**模型系统与实验技术**

- **爪蟾卵提取物（Xenopus laevis egg extract；HSS / NPE）：** 含全部可溶性核蛋白、支持高效复制与多种RS通路的无细胞体系（refs 32,33）。HSS（high-speed supernatant）支持licensing不支持firing（模拟G1）；NPE（nucleoplasmic extract）支持firing、延伸与RS响应（模拟S）。选它的理由：可免疫耗竭/回补任意因子、可单分子成像、且不含内源PRIMPOL（ED1a,b）从而允许"干净地"补充人PRIMPOL及其突变体。
- **KERMIT（kinetics of eukaryotic replication via molecular imaging and tracking）与TIRF（total internal reflection fluorescence，全内反射荧光显微镜）：** 本课题组建立的单分子复制成像 assay（refs 25,34）：双 tether λ DNA + 两步提取物灌流 + 实时TIRF（只激发盖玻片表面~百纳米层以获得单分子信噪比），读出CMG速度、新生DNA积累与蛋白结合事件。本文将其扩展到RS与repriming，并加三色通道（PRIMPOL–AF647 / RPA–mCherryXL / FEN1–KikG）。本文TIRF参数：TIRF臂9000（~67°），EM gain 150；GINS–LD655 1 s曝光/10% 640 nm（~150 µW），PRIMPOL–AF647 500 ms/25% 640 nm（~380 µW），FEN1–KikG 500 ms/8% 488 nm（~70 µW），RPA–mCherry 1 s/10% 561 nm（~70 µW）；每帧15–60 s内顺序采4–10个视野（Methods）。
- **Kymograph（时间-位置图）：** 沿DNA分子把每帧荧光强度排成一行、随时间堆叠的图。本文阅读方向：横轴=DNA位置（kb），纵轴=时间（向下）；斜线斜率=速度（陡=慢、缓=快），"慢→快"折点即重启。CMG/RPA tract边缘的线性/双线性/三线性拟合给出速度（Methods）。
- **双tether λ DNA底物：** 生物素化λ DNA两端固定于链霉亲和素盖玻片，拉伸至轮廓长度80–90%（分析只取80–95%），加20 pM streptavidin–AF647作对焦fiducial（Methods）。速度换算：斜率×160 nm/pixel ÷0.34 nm/bp ÷0.85（拉伸校正）。
- **免疫耗竭与回补（immunodepletion / add-back）：** 用抗体把提取物中某因子移除（本文Pol α、Pol δ、Pol ε、GINS、PCNA），再回补重组蛋白验证特异性（Methods抗体验证）。本文的因果推断骨架：耗竭消除表型+回补恢复表型=该因子必需（Fig. 4d）。
- **Ensemble质粒复制 assay：** 3 kb pBluescript II SK(+) 在HSS中licensing、NPE中复制，α-³²P-dCTP掺入，0.8%天然琼脂糖凝胶分离超螺旋/切口/连环/部分复制中间体，磷屏成像（Fig. 1j；Methods）。读out为90 min总DNA合成与超螺旋产物，归一化到30 nM WT（Fig. 1k）或WT对照（Fig. 3g）。
- **染色质分级（chromatin fractionation）：** 精子染色质（1000 sperm/µl）licensing 30 min + NPE 45–60 min后，经0.25 M蔗糖+0.2% Triton裂解、0.5 M蔗糖垫15,000g离心沉淀染色质，blot检测结合蛋白（ED2d,e；Methods）。用于验证WT/AxA上染色质而ΔRPA不上。
- **Co-IP（co-immunoprecipitation，共免疫沉淀）：** 本文用Flag–SNAP–PRIMPOL(1–60)（N端60 aa bait）固定于anti-Flag磁珠（200 pmol bait / 3 µl珠），与稀释5倍的NPE:HSS=1:1提取物孵育1 h，blot MCM7读MCM2–7共沉淀（Fig. 3d,e；Methods）。设计价值：只含N端界面的bait即可拉下CMG，且界面突变削弱共沉淀，直接验证AF3预测的物理互作。
- **DNA fibre assay（DNA纤维 assay）：** 细胞水平重启读out：CldU 50 µM 20 min标记进行叉 → UV-C 30 J/m²停滞 → 恢复30 min → IdU 250 µM 20 min只标记重启叉；铺片、3 M HCl变性、抗BrdU双色免疫荧光（CldU红/IdU绿），每条件每重复计500个复制结构（Fig. 3h,i；ED4h；Methods，ref 1）。
- **SNAP-tag荧光标记与染料：** 人PRIMPOL带SNAP-tag，用SNAP-Surface AF647以1.5倍摩尔比过夜标记（标记效率89–100%，ED3a），不纯化直接用于单分子；GINS/PCNA用LD655（PCNA经SFP synthase酶法标记），FEN1融合KikG，RPA融合mCherry-XL（亮版mCherry，refs 50,51）。标记不损伤PRIMPOL重启活性（ED3b,c）。
- **GLRT（generalized likelihood ratio test，广义似然比检验）：** 本课题组前作建立的单分子事件检测算法（ref 71）：5像素滑窗区分噪声与信号，把图像二值化后分割结合事件，给出结合/解离时刻（Δt1）与解离-重启延迟（Δt2）（Methods）。fork-proximal定义为结合位置距叉≤1 pixel（160 nm）。
- **AlphaFold3 / Predictomes：** AF3（ref 53）预测蛋白互作；Predictomes（ref 52）为分类器 curated 的AF互作数据库。本文交叉比对人与蛙蛋白的AF3预测，筛出PRIMPOL–MCM4（及MCM7）候选界面（Fig. 3a；ED4a,b），再用人–蛙盐桥对应残基设计突变；预测后被co-IP与功能实验证实，且与并行工作的cryo-EM结构高度一致（Discussion，ref 60）。
- **PDB 7PFO：** 已发表的人核心replisome cryo-EM结构（ref 54）。本文把AF3的PRIMPOL–MCM4模型叠合其上，检查PRIMPOL docking位点与Pol ε拴系位置是否空间兼容（Fig. 3a右），结论是Pol ε的存在不应阻碍PRIMPOL结合MCM4。
- **SYBR Green I引物酶-聚合酶 assay：** 体外酶活读out：T36CCTGT20 ssDNA模板30 nM，1 mM MnCl₂、10 µM dNTP、SYBR Green I 1:20,000，PRIMPOL 1–100 nM，室温1 h，Ex497/Em520读双链产物荧光（ED1d；ED4d；ED7e；Methods，ref 68）。不含RPA或其他复制因子，故只测催化、不测募集。
- **LC–MS/MS（Orbitrap Exploris 480 / Byonic）：** 用于证明卵提取物无内源PRIMPOL：IP–MS与直接酶解，Byonic v5.1.1搜UniProt爪蟾库，12 ppm容差、1% FDR（target-decoy）（Methods；ED1a,b；Supplementary Table 1未提供）。
- **统计框架（bootstrap 95% CI / KS / t检验）：** 单分子分布偏态，报中位数+bootstrap 95% CI；分布比较用two-sample two-sided Kolmogorov–Smirnov检验；ensemble/co-IP/fibre用two-tailed Student t检验；每条件n≈100–200分子/事件、≥2次独立提取物制备，ensemble/co-IP/fibre 3–4次独立重复；无盲法/随机化（Reporting Summary）；精确P值列于Supplementary Table 4（未提供）。

---

二、<核心问题与方案>

**生物学问题（原文表述）：**

- "However, the molecular mechanism that underlies repriming remains poorly understood, and it is unclear how PRIMPOL is precisely targeted to stalled forks, where along single-stranded DNA PRIMPOL binds and how PRIMPOL is regulated to minimize error-prone DNA synthesis."（Abstract；同旨见Introduction第3段）——然而repriming的分子机制仍知之甚少：PRIMPOL如何被精确靶向停滞叉、沿ssDNA究竟结合在哪里、以及如何被调控以最小化易错DNA合成，均不清楚。
- "The notion that PRIMPOL may reprime leading strand synthesis was hypothesized at the time of its discovery2, and discussed in later work7,16,29, but there is no direct evidence for this idea."（Introduction第2段末）——PRIMPOL重新引发前导链合成的想法在发现之初即被提出，但一直没有直接证据。
- "although RPA recruits PRIMPOL to ssDNA30,31, it is unclear why PRIMPOL acts at stalled forks, but not on ssDNA generated by other processes (transcription, recombination)."（Introduction第3段）——既然RPA把PRIMPOL募集到ssDNA，为何PRIMPOL只作用于停滞叉、而不作用于转录/重组等过程产生的ssDNA？
- "It remains unclear how repriming occurs in the nucleus, where RPA is abundant and rapidly coats exposed ssDNA."（Introduction第3段）——在RPA丰富、瞬间包被ssDNA的核内，repriming如何发生？
- "Although PRIMPOL is a known target of checkpoint kinase 1 (CHK1)22, how the DNA damage checkpoint regulates repriming remains poorly understood. Finally, it is unclear how PRIMPOL is regulated to minimize mutagenic DNA synthesis during repriming."（Introduction第3段末）——检查点如何调控repriming、以及repriming如何被限制以减少突变合成，均不清楚。

**背景矛盾（研究切入点）：** 矛盾一方是"RPA–PRIMPOL互作足以解释募集"的既有模型（refs 30,31）：RPA在任何ssDNA上都存在，按此模型PRIMPOL应在转录泡、重组中间体等处同样引发，且ref 30报告高浓度RPA完全包被ssDNA会抑制PRIMPOL、ref 31却报告RPA刺激PRIMPOL——两条文献直接冲突；矛盾另一方是细胞与遗传学观察：PRIMPOL只在停滞叉处发挥作用、repriming是受控的RS耐受通路而非全局易错合成。叠加第三重张力：PRIMPOL错误率高达10⁻²–10⁻⁴，细胞却把它当作基因组维护通路使用，说明必有机制把它的易错合成压缩到最短。本文的切入点是绕过"RPA募集即充分"的隐含假设，在近生理提取物中直接可视化PRIMPOL的结合位置、停留时长与生产性，追问"叉附近是否存在额外的稳定化互作"，并进一步追索引物合成后的去向（交给谁延伸），从而把空间靶向、保真控制与检查点调控三个问题一次解开。

**解决方案（技术路线）：**

- **模型系统：** 爪蟾卵核提取物（HSS+NPE）——支持完整复制与RS响应、可任意耗竭/回补、且经IP–MS与双抗体western证明不含内源PRIMPOL（ED1a,b），故补充重组人PRIMPOL即可"干净"重建通路（人PRIMPOL高度保守、突变体已有表征、细菌表达好，Methods给出三条理由）；细胞层面用Méndez实验室建立的PRIMPOL-KO HCT116做 transient 回补（Fig. 3h,i）。
- **实验设计：** (1) KERMIT双tether λ DNA + GINS–LD655（CMG）+ FEN1–KikG（新生DNA）实时TIRF，建立"慢→快速度切换=重启"的单分子读out（Fig. 1a–e）；(2) 两种正交RS来源：Pol α免疫耗竭（+10 µM CD437压残留）与30 kb λ上前导链位点特异性肽加合物（~4 aa，可穿CMG通道），另以APH作"聚合酶全抑"对照证明重启需复制聚合酶延伸（Fig. 1c–i；ED1e）；(3) PRIMPOL浓度梯度3–100 nM覆盖近生理（10–30 nM，人细胞~17 nM，ref 49）到过表达模拟（Fig. 1j,k；Fig. 4b,f）；(4) 三色单分子（PRIMPOL–AF647 / RPA–mCherryXL / FEN1–KikG）在15 s/帧与3 s/帧两个时间分辨率下测结合位置、时长与生产性（Fig. 2）；(5) ensemble 3 kb质粒复制（α-³²P-dCTP、天然胶）做高通量定量与突变体表型（Fig. 1j,k；Fig. 3f,g）；(6) Pol α+Pol δ 或 Pol α+Pol ε 双耗竭 + 回补400 nM Pol δ / 100 nM Pol ε（人细胞浓度）判定引物交接去向（Fig. 4d）；(7) ATR抑制剂AZD6738（3 µM）+ 四个磷酸化突变体（S255A/E/D、Δ201–260）解析检查点调控（ED7；Fig. 4e,f）；(8) Flag–SNAP–PRIMPOL(1–60) bait co-IP验证N端–CMG物理互作（Fig. 3d,e）；(9) HCT116 PRIMPOL-KO回补 + CldU/IdU fibre（UV-C 30 J/m²）做细胞水平验证（Fig. 3h,i）。
- **功能验证：** 确立必要性——Pol α/δ/ε耗竭、PRIMPOL催化死（AxA）、RPA结合死（ΔRPA）、MCM4界面突变（3A/DED/Linker）均消除或削弱重启；确立充分性——回补重组Pol ε/Pol δ完全恢复对应模式、回补WT PRIMPOL恢复重启；区分竞争解释——AxA vs ΔRPA解耦"催化 vs 募集"；3A/DED/Linker三种独立界面破坏方式互证MCM4界面（排除单点突变折叠伪影）；Pol δ vs Pol ε耗竭解耦"交接给谁"；S255A vs S255E/D vs Δ201–260解耦"检查点作用于哪个模式"；FEN1(FFAA)与PCNA–LD655解耦"标记信号 vs 真实合成"。
- **机制解析：** 从"重启现象（速度切换+新生DNA）"到"结合空间学（fork-proximal长停留~3 min、>99%远端结合非生产性）"到"稳定化互作（AF3跨物种筛选→MCM4盐桥→结合时长/co-IP/ensemble/fibre四重验证）"到"引物去向（聚合酶耗竭上位性→Pol ε主/Pol δ次）"到"调控归属（检查点非必需于主模式、CHK1只上调次模式）"到"模型整合（双锚定+RPA瞬态解离，Fig. 5）"。

**验证层级：** 重启现象与正交RS（Fig. 1a–i）→ ensemble定量与催化/募集解耦（Fig. 1j,k；ED2d,e）→ 结合位置/时长/生产性（Fig. 2；ED3）→ 界面预测与物理互作（Fig. 3a–e；ED4a,b）→ 界面的提取物体外与细胞内必要性（Fig. 3f–i）→ 两模式解耦与速度差异（Fig. 4a–c；ED5）→ 引物交接去向（Fig. 4d；ED6）→ 检查点非必需与模式特异调控（ED7a–c；Fig. 4e,f）→ 双锚定模型（Fig. 5）。

**统计与生信框架（Methods要点）：** 单分子数据报中位数+bootstrap 95% CI（MATLAB内置bootstrap），分布比较用two-sample two-sided KS检验；ensemble/co-IP/fibre用two-tailed Student t检验，3–4次独立重复；每条件n≈100–200个分子/事件，≥2次独立提取物制备；无预确定样本量、无盲法与随机化（Reporting Summary如实声明）；精确P值在Supplementary Table 4（未提供）。事件检测用GLRT（5像素滑窗，ref 71）；速度用线性/双线性/三线性拟合斜率×160 nm/pixel÷0.34 nm/bp÷0.85；CMG非依赖重启用OTSU阈值分割FEN1 tract边缘拟合；fork-proximal=距叉≤1 pixel（160 nm）；fork-distal频率按ssDNA长度与观察时长归一（kb⁻¹ min⁻¹），fork-proximal按观察时长归一（min⁻¹）。MS：Orbitrap Exploris 480、Byonic v5.1.1、12 ppm、1% FDR。结构预测：AlphaFold3（ref 53）+ Predictomes（ref 52），叠合PDB 7PFO（ref 54）；本文未自产cryo-EM数据，无新PDB/EMDB deposition。原文未提供GEO/公共测序accession（本研究以生化、单分子成像与细胞fibre数据为主，无高通量测序数据）；原始数据与自研MATLAB代码存Stanford Digital Repository（DOI 10.25740/hy921dn6469）。

---

三、<逐节精读>

本节按原文Results的8个小标题逐一展开：每节先给出完整"内容逻辑"叙事，随后以"→ Figure X"嵌入该节关联主图的四字段解读；随PDF提供的Extended Data图按内容角色在对应panel后以整合段说明。Fig. 5为Discussion提出的模型图，其逐panel解读置于模块四第1层。

**课本化背景补注｜PRIMPOL与repriming：为什么细胞需要一条"跳过损伤"的专用引发通路**

它是什么、为什么重要。复制叉沿基因组前进时会不断撞上内源与外源损伤（紫外光产物、化疗药加合物、癌基因激活导致的异常结构等）。高保真的复制聚合酶一旦在损伤处停滞，细胞面临两难：要么让叉崩塌（产生双链断裂、基因组重排），要么动用"复制应激耐受"通路绕过损伤继续复制。Repriming（重新引发）是2013年才被确立的一条耐受通路：不在损伤处硬合成，而是由专用引物酶PRIMPOL在损伤下游的单链DNA（ssDNA）上重新合成一段引物、跳过损伤，代价是在子代DNA上留下一段ssDNA缺口（gap）（Introduction第1段，refs 1–4）。它的重要性在于：这是细胞耐受化疗与癌基因应激的核心手段之一，留下的缺口又使细胞对PARP抑制剂敏感，因此PRIMPOL既是基因组维护因子，也是肿瘤治疗的潜在靶点（refs 14–20）。

分子性质。PRIMPOL（primase–polymerase）属于古菌-真核引物酶（AEP）超家族，是一个"双功能"酶：N端结构域兼具引物酶（合成短RNA/DNA引物）与DNA聚合酶（延伸引物）活性，共用D114/E116催化中心；C端为解旋酶样结构域（无解链活性，介导蛋白互作，含RPA结合界面）。它没有3'→5'校对功能，错误率高达10⁻²–10⁻⁴，与跨损伤合成（TLS）聚合酶相当（refs 9,10）；在核内与线粒体均有分布，人细胞内源浓度约17 nM（OpenCell图谱，ref 49），属低丰度蛋白。

缺失或异常的后果。敲除PRIMPOL的细胞与小鼠可以存活，但对紫外、顺铂、链终止核苷酸等损伤明显敏感，复制叉重启缺陷、基因组不稳定性升高（refs 1–4,8,13）；反之，在癌基因（如KRAS）激活或BRCA缺陷的细胞中PRIMPOL常被上调/依赖，帮助细胞耐受复制应激（refs 14,15）。这说明它不是必需复制因子，而是"应激时才被倚重"的备份系统。

前人如何研究它。2013年四篇论文几乎同时确立该通路：Mourón等（Nat. Struct. Mol. Biol.，ref 1）用纯化酶生化+人细胞DNA fibre证明PrimPol在停滞叉下游重新引发；García-Gómez等（Mol. Cell，ref 2）鉴定其为"古老"引物酶/聚合酶并提出"前导链重新引发"假说；Bianchi等（Mol. Cell，ref 3）用紫外损伤模型证明其绕过光产物；Wan等（EMBO Rep.，ref 4）证明其维护基因组完整性。这些工作确立了"现象与执行者"，但留下三个机制缺口：PRIMPOL究竟被靶向到哪里、引物交给谁延伸、易错合成如何被限制。此后Guilliam等（ref 9）定量其易错性并发现RPA调控，Guilliam等（ref 30）定位RPA募集界面，Mehta等（ref 22）发现CHK1磷酸化Ser255促进repriming——但"在哪里引发、交给谁"始终没有直接证据。

与本文的关系。本文正是补上这三个缺口：用单分子成像直接看见重启、用双锚定模型解释空间靶向、用聚合酶上位性判定引物去向、用磷酸化突变体给检查点效应划定作用域。

（来源：本文refs 1–4,8–10,13–20,22,30,49及课本级综述ref 24。阅读深度：ref 2的"前导链假说"段落与ref 30的互作定位建议精读，其余可只读摘要与结论；深度作者谱系见同源《背景解读》。）

**课本化背景补注｜CMG解旋酶：复制叉的"发动机"与解偶联信号**

它是什么、为什么重要。CMG是真核生物的复制解旋酶，负责在聚合酶前方解开亲代DNA双链，是整个复制叉的发动机；没有它，复制无法起始与延伸。它也是复制应激信号的源头：当聚合酶停滞而解旋酶继续解链（"解偶联"）时，暴露的长段ssDNA成为检查点激活与本文双锚定机制的共同平台。

分子性质。CMG由三部分组成：CDC45、MCM2–7异源六聚体（AAA+ ATP酶马达环，沿前导链模板3'→5'移位、中央通道穿过ssDNA）与GINS四聚体（Psf1–3/Sld5，结构支架）（refs 23,24,46）。前导链聚合酶Pol ε物理拴系在CMG上随之移动（refs 54–56）。本文用GINS亚基偶联LD655染料追踪CMG，其单分子速度签名是：正常复制~300 nt/min，解偶联空转~30 nt/min（约慢10倍）——这一"快/慢"切换就是重启读out的物理基础。

缺失或异常的后果。解旋酶失活导致叉崩塌与基因组不稳定；MCM亚基的亚效突变在人类引起Meier-Gorlin综合征（小头/身材矮小/免疫缺陷，课本级背景）；解偶联本身则持续产生RPA–ssDNA，激活ATR–CHK1检查点（ref 28）。

前人如何研究它。CMG的架构由cryo-EM确立（refs 23,46）；Taylor与Yeeles（refs 26,27）用纯化酵母replisome证明前导链损伤可诱导解偶联、后随链合成继续；Sparks等（Cell 2019，ref 25）在爪蟾卵提取物中用单分子成像证明CMG能绕过前导链上的DNA-蛋白交联（DPC）——小肽加合物可穿过中央通道、不堵解旋酶而只停滞Pol ε——该文同时建立了KERMIT成像雏形与本文所用的位点特异性损伤底物。遗留缺口：绕过/停滞之后，前导链合成由谁、在哪里重新建立？

与本文的关系。本文继承ref 25的损伤底物与成像平台，把CMG从"被观察的发动机"升级为"PRIMPOL的募集平台"（MCM4/MCM7 docking位点），并以速度签名作为重启的单分子判据。

（来源：本文refs 23–28,46,54–56；Meier-Gorlin关联为课本级背景。阅读深度：ref 25建议精读其单分子方法与DPC底物设计；refs 26,27可只读结论。）

**课本化背景补注｜复制聚合酶分工：Pol ε、Pol δ、Pol α与"引物交给谁"为什么是个问题**

分工是什么。真核复制叉上三种聚合酶各司其职：Pol ε负责前导链连续合成，物理拴系于CMG、带3'→5'校对、保真度高；Pol δ负责后随链冈崎片段延伸，同样带校对；Pol α–引物酶复合物负责"从头引发"（起始与每个冈崎片段），先合成短RNA引物再延伸一小段DNA，无校对、保真度低（ref 24）。引发酶做出的引物必须被复制聚合酶捕获并延伸（"聚合酶切换/引物交接"），复制才能继续。

为什么"交给谁"是问题。在复制起始时，Pol α引物先交给Pol δ/ε建立前导链（refs 42,43,57）——即存在"Pol δ中间体"路径。因此当PRIMPOL在停滞叉做出新引物时，有两种竞争解释：直接交给CMG拴系的Pol ε（前导链路径），或先经Pol δ再转交（类似起始路径）。这不是文字游戏：两条路径对应不同的空间位置、速度与保真后果，必须用实验裁决。

缺失或异常的后果。POLE/POLD1校对结构域突变导致超突变结直肠癌等（课本级背景）；Pol ε/δ功能缺陷使复制无法完成。本文用免疫耗竭+生理浓度回补（100 nM Pol ε、400 nM Pol δ，取自人细胞浓度ref 49）做上位性判定。

前人如何研究它。分工框架由Burgers与Kunkel综述确立（ref 24）；Aria与Yeeles（ref 42）用纯化酵母体系证明双向起始时前导链建立需Pol α/δ参与；Zhou等（ref 57）证明Pol δ参与前导链起始与终止；人replisome cryo-EM结构（refs 54–56）直接显示Pol ε拴系于CMG。缺口：停滞叉重启时的引物交接从未被直接判定。

与本文的关系。本文Fig. 4d的双耗竭上位性干净分离两条路径：CMG依赖模式专一依赖Pol ε、CMG非依赖模式专一依赖Pol δ，从而把"PRIMPOL是前导链引物酶"从假说变成因果结论。

（来源：本文refs 24,42,43,49,54–57；癌症关联为课本级背景。阅读深度：ref 24建议通读其分工示意图；refs 42,57可只读结论。）

**课本化背景补注｜TLS vs repriming：两条损伤绕过路线的本质区别**

区别在哪里。跨损伤合成（TLS）与repriming都能让复制"绕过"损伤，但策略相反：TLS由低保真专用聚合酶（Pol η/ι/κ/Rev1等）直接在损伤对面合成、不留下缺口，代价是可能把错误碱基固定在损伤位点（点突变）；repriming则跳过损伤、在下游重新引发，把损伤"留待复制后处理"，代价是留下ssDNA缺口（refs 6,7）。两者与复制叉反转（fork reversal）共同构成RS耐受网络，且彼此竞争：阻断反转会增强repriming（refs 7,21,22），提示细胞在通路间做权衡。

为什么重要。通路选择决定突变特征与化疗响应：TLS倾向产生点突变，repriming倾向产生缺口（进而依赖复制后修复或HR）。本文损伤底物上无PRIMPOL时约7%的低效重启被归因于TLS背景（Fig. 1f，refs 47,48），作为repriming的对照——这一"背景值"的诚实标注防止把全部重启都归功于PRIMPOL。

与本文的关系。本文不直接研究TLS，但双锚定模型解释了为什么repriming被限定在停滞叉、而TLS可在任何损伤处发生；Discussion的治疗策略置于这一通路竞争背景下。

（来源：本文refs 6,7,21,22,47,48及课本级综述。阅读深度：ref 7综述建议通读其通路选择框架。）

**课本化背景补注｜复制后缺口的命运：repriming为什么与PARP抑制剂敏感性挂钩**

缺口从哪里来、到哪里去。Repriming跳过损伤后，子代DNA上留下一段ssDNA缺口。这些缺口在复制后被处理：一条路线是无错的同源重组/模板切换（以姐妹染色单体为模板补齐，ref 12证明PrimPol依赖的缺口介导大加合物处的HR）；另一条是TLS聚合酶回填（可能引入突变）。若缺口未被及时修复而持续存在，细胞对PARP抑制剂敏感——这正是"BRCAness"与缺口生物学的核心（refs 18–20）；在BRCA缺陷细胞中，PRIMPOL介导的repriming抑制叉反转、产生缺口，反而成为PARPi敏感性的来源（ref 15）。

为什么重要。这把repriming从"复制机制问题"升级为"肿瘤治疗问题"：抑制PRIMPOL可减少缺口、改变肿瘤细胞对化疗/PARPi的响应；反之，PRIMPOL过表达帮助肿瘤耐受应激（refs 14,15）。目前尚无小分子PRIMPOL抑制剂（refs 17,63），本文据此提议以N端MCM4界面阻断肽抑制repriming。

与本文的关系。本文的双锚定机制（把易错合成压缩为短引物、缺口最小化）为"靶向PRIMPOL–CMG互作"提供了精确的药物设计落点；但缺口的后续修复命运本文未测（见Discussion未讨论清单）。

（来源：本文refs 12,14–20,63。阅读深度：refs 18–20为综述，建议只读其缺口–PARPi逻辑段落；ref 12可只读结论。）

**方法平台补注｜为什么用单分子TIRF/KERMIT：把"重启"变成一部可逐帧审读的电影**

为什么用它。Ensemble（群体）生化assay把成千上万个叉的信号平均掉，无法回答"PRIMPOL结合在哪个位置、停留多久、这次结合是否生产性"这类空间-动力学问题；而>99%的结合是非生产性的稀有事件判别，恰恰需要单分子分辨率。单分子TIRF（全内反射荧光）只激发盖玻片表面约百纳米厚的倏逝场层，背景极低，能在近生理蛋白浓度下看见单个荧光分子。KERMIT是本课题组建立的复制成像平台（refs 25,34,70）：双tether λ DNA固定在表面、HSS/NPE两步灌流重建G1→S顺序、实时多色成像，读出CMG速度、新生DNA积累与蛋白结合事件。

为什么选爪蟾卵提取物。它含全部可溶性核蛋白、支持完整复制与RS响应，可免疫耗竭/回补任意因子做因果判定，且不含内源PRIMPOL（ED1a,b）——补充重组人PRIMPOL即可"干净"重建通路。体系特性需对照验证：荧光标记不损伤活性（ED3b,c）、低DNA浓度使检查点不激活（ED7a，ref 58阈值~1 ng/µl）、高帧率排除扩散伪影（Fig. 2g,h）——本文均已做。

（来源：本文refs 25,34,58,70与Methods。阅读深度：ref 34/70为方法协议，做同类实验者精读，否则可跳过。）

Section 1：Direct observation of PRIMPOL-mediated fork restart（PRIMPOL介导复制叉重启的直接观察）

内容逻辑：本节回答全文的第一个问题——repriming能否在保留基因组维护能力的核提取物中被"看见"，以及"看见"的读out是否可信。作者面临两个前置障碍：其一，爪蟾卵提取物中经IP–MS与两株非重叠抗原抗体western均检测不到内源PRIMPOL（ED1a,b；Supplementary Table 1未提供），这既是障碍也是机会——补充重组人PRIMPOL即可在无内源背景干扰下重建通路；其二，如何制造RS而不把复制聚合酶一起抑掉。APH虽能制造解偶联（CMG慢~10倍、无FEN1信号），但它同时抑制Pol ε/δ，使PRIMPOL引物无人延伸，故30 nM WT PRIMPOL在APH中不能重启（ED1e）——这一"负性结果"被作者用作逻辑对照：重启不仅需要引发，还需要复制聚合酶延伸。于是作者设计两种正交RS：Pol α免疫耗竭（前导链合成无法建立，CMG ~30 nt/min空转）与30 kb λ上前导链模板的~4 aa肽加合物（可穿CMG通道、只停滞Pol ε）。两者都给出"慢→快"速度切换伴随FEN1–KikG积累的重启事件：Pol α耗竭+30 nM WT约75%重启 vs buffer约5%；损伤底物+30 nM WT约50% vs buffer约7%（后者归因TLS）。为确认"快=合成"而非解旋酶本身变速，作者做三重标记验证：PCNA–LD655与FEN1–KikG同样积累在重启叉后（ED1g）；破坏FEN1–PCNA互作的FFAA突变消除FEN1信号但不影响重启（ED1h,i）；故FEN1信号是PCNA募集的新生DNA报告子，且因信噪比优于PCNA被选为主标记。值得注意的是损伤底物实验在内源Pol α存在下完成，排除了"重启只是Pol α耗竭体系伪影"的替代解释。本节的贡献是建立可信的单分子重启读out与两种正交RS模型，并确立"重启=引发+复制聚合酶延伸"的双组分逻辑；后续所有机制问题都在此读out上展开，而Pol α耗竭因通量高、易转ensemble被选为主力体系（为Section 2埋下伏笔）。

→ Figure 1 标题为"PRIMPOL promotes efficient restart of stalled forks in Xenopus nuclear extract"，旨在建立单分子重启读out并通过两种正交RS证明PRIMPOL的充分性。由a至k共11部分构成：a流程、b–e与g,i kymograph、f重启效率、h速度分布、j–k ensemble定量，形成"读out建立→正交验证→定量确认"的证据链。

(A) 单分子成像工作流程示意图
图片解释：双tether λ DNA先入HSS完成origin licensing（G1模拟），洗去可溶蛋白保留DNA结合MCM2–7，再入NPE启动firing与延伸（S模拟）；GINS–LD655标CMG、FEN1–KikG标新生DNA，实时TIRF成像。定量数据：无（示意图）。
横纵轴定义：无坐标轴（流程示意图），阅读方向自上而下为实验时间顺序。
颜色含义：CMG/GINS橙色、FEN1蓝色、RPA绿色、Pol ε/δ/α灰色（与后续kymograph配色一致）。
核心结论：两步提取物灌流在体外重建G1→S顺序，使"许可—激活—延伸—应激"可在同一分子上连续观察。

(B) 未扰动叉的CMG动力学（mock + DMSO）
图片解释：本图为kymograph（时间-位置图）——把沿DNA分子每一帧的荧光强度排成一行、按时间逐帧向下堆叠而成；每个亮点的横坐标是荧光分子在DNA上的位置、纵坐标是成像时刻，一条斜线即一个分子的运动轨迹，斜率=速度。橙色亮点来自偶联LD655染料的GINS（CMG亚基，故橙=解旋酶位置），蓝色来自FEN1–KikG融合蛋白（被PCNA募集到新生DNA，故蓝=新合成DNA的间接报告）。两条分叉CMG橙色轨迹以~300 nt/min背向行进，FEN1–KikG蓝色信号在解旋酶后方积累；标尺5 kb、2 min。定量数据：~300 nt/min（正文；h中位数读自Fig. 1h约300）。
横纵轴定义：横轴DNA位置（kb），纵轴时间（向下）；斜率越缓速度越快。换算：斜率×160 nm/pixel÷0.34 nm/bp÷0.85（拉伸校正）=nt/min。读图方向：沿轨迹看斜率变化，'陡→缓'折点=加速（重启），'缓→陡'=停滞。
颜色含义：橙=GINS–LD655（CMG），蓝=FEN1–KikG（新生DNA）。
核心结论：正常复制时CMG快速且与合成偶联，FEN1信号紧随叉后，确立"快+蓝=健康叉"的基线。

(C) APH处理提取物的CMG动力学
图片解释：10 µM APH（图标注；正文述15 µM）下CMG橙色轨迹明显变陡（~30 nt/min，约慢10倍），无蓝色FEN1信号。定量数据：~10倍减速（正文）。
横纵轴定义：同B。
颜色含义：同B；蓝色缺失即无DNA合成。
核心结论：聚合酶被抑时CMG解偶联空转，确立"慢+无蓝=解偶联"的RS判据。

(D) Pol α耗竭提取物的CMG动力学
图片解释：无PRIMPOL时CMG慢速（~30 nt/min）且无FEN1积累，与APH表型类似但聚合酶ε/δ未被抑制。定量数据：~30 nt/min（正文）。
横纵轴定义：同B。
颜色含义：同B。
核心结论：Pol α耗竭在不抑制Pol ε/δ的前提下制造解偶联，为PRIMPOL重启留出延伸能力。

(E) Pol α耗竭 + 30 nM WT PRIMPOL
图片解释：慢速CMG突然加速至~300 nt/min（白箭头），切换点后方出现FEN1蓝色积累；内嵌放大框显示切换细节。定量数据：~75%叉重启（f）。
横纵轴定义：同B；"慢→快"折点即重启时刻。
颜色含义：同B；白箭头=PRIMPOL依赖重启事件。
核心结论：速度切换与新生DNA合成同时发生，单分子层面直接看见repriming驱动的重启。

(F) 重启效率定量
图片解释：Pol α耗竭+buffer约0.05–0.07、+PRIMPOL约0.73；损伤底物+buffer约0.07、+PRIMPOL约0.50；n=192、304、143、155（叉数），两组比较均\*\*\*\*（P<0.0001），误差棒为bootstrap 95% CI。定量数据：~75% vs ~5%、~50% vs ~7%（正文）。
横纵轴定义：Y=重启叉比例（0–1），X=四种条件分组。读法：每根柱=该条件下发生重启的叉所占比例；误差棒=bootstrap 95% CI（对叉数重抽样估计的不确定度）；柱上星号=两组比例差异显著性（\*\*\*\*对应P<0.0001）。
颜色含义：绿色柱=各条件重启效率。
核心结论：两种正交RS下PRIMPOL都显著提升重启效率，且损伤底物在内源Pol α存在下成立。

(G) 损伤底物 + buffer
图片解释：CMG快速行进至肽加合物处立即减速（黄箭头），此后维持慢速；上方卡通显示加合物位于前导链模板、CMG穿过后解偶联。定量数据：~300→30 nt/min（正文；h）。
横纵轴定义：同B；黄箭头=损伤处停滞。
颜色含义：橙=CMG，蓝=FEN1；卡通中加合物红色标记。
核心结论：位点特异性前导链损伤精确制造解偶联，停滞位置可预知，便于后续结合位置分析。

(H) 各条件CMG速度分布
图片解释：小提琴/散点图读法：每个黑点=一个CMG分子轨迹拟合出的速度值，轮廓=分布密度，蓝线=中位数、阴影=bootstrap 95% CI。七组：+DMSO ctrl（n=147，中位~300）、+APH ctrl（n=93，~30）、Pol α耗竭重启前（n=140，~30）/重启后（n=140，~300）、损伤停滞前（n=137，~300）/停滞中（n=155，~30）/重启后（n=78，~300）；蓝线为中位数、阴影为bootstrap 95% CI；显著性\*\*\*\*、NS、\*\*\*\*、\*、\*\*\*\*。定量数据：重启后速度恢复至未扰动水平（~300 nt/min）。
横纵轴定义：Y=CMG速度（nt/min，0–700），X=条件分组。
颜色含义：黑点=单个CMG分子，蓝线=中位数。
核心结论：重启不是部分加速而是完全恢复偶联速度，支持"重新建立完整replisome"而非解旋酶自身变速。

(I) 损伤底物 + 30 nM WT PRIMPOL
图片解释：快→慢（黄箭头停滞）→快（白箭头重启）三段式轨迹，重启后FEN1蓝色恢复。定量数据：~50%重启（f）。
横纵轴定义：同B。
颜色含义：同B/G。
核心结论：在生理性损伤情境下PRIMPOL同样驱动重启，与Pol α耗竭结论互证。

(J) Ensemble质粒复制自显影
图片解释：测什么：复制反应掺入的α-³²P-dCTP使新生DNA带放射性，磷屏成像记录放射性强度——条带越深=该构象DNA越多；天然琼脂糖凝胶按DNA拓扑构象分离（超螺旋=完成复制的闭环质粒、迁移最快，切口环状次之，连环体与部分复制中间体最慢）。mock（i）30/60/90 min强超螺旋带；Pol α耗竭+buffer（ii）仅弱部分复制带；3 nM（iii）、10 nM（iv）、30 nM（v）WT PRIMPOL剂量依赖恢复；30 nM AxA（vi）与ΔRPA（vii）不恢复；左侧卡通标出连环、 fully replicated nicked/supercoiled、部分解旋/复制中间体对应条带。定量数据：此为代表性自显影，灰度定量见k；原文未提供该胶的灰度数值。
横纵轴定义：无坐标轴（自显影）。横向为条件/时间泳道，纵向为DNA构象迁移位置（超螺旋最快、连环最慢）。阅读方向：比较同一构象带在各泳道的强弱。
颜色含义：灰度条带，越深代表³²P掺入的DNA越多；卡通中蓝色=新生DNA。
核心结论：单分子结论在ensemble水平复现，且重启依赖PRIMPOL催化活性与RPA互作两者。

(K) Ensemble定量（90 min）
图片解释：总DNA合成（深灰）与超螺旋（浅灰）归一化到30 nM WT：mock约3；耗竭buffer约0.45；3/10/30 nM约0.7/0.85/1.0；AxA约0.45、ΔRPA约0.5；超螺旋组分对WT剂量依赖、对两突变体几乎缺失；n=3独立重复，mean±s.d.，t检验（\*\*、\*\*\*\*、NS等标注）。定量数据：30 nM WT未完全回补至mock（正文归因检查点抑制firing，见Section 2与ED2c,d）。
横纵轴定义：Y=90 min DNA强度（归一化，0–4，轴断裂），X=条件。
颜色含义：深灰=总合成，浅灰=超螺旋（完成复制）产物。
核心结论：近生理浓度PRIMPOL剂量依赖回补DNA合成；催化与RPA互作缺一不可；"不完全回补"留下检查点伏笔。

Extended Data Fig. 1（整合解读，PRIMPOL缺失证明与标记/读out验证）：(a) 两株非重叠抗原（N端/C端）抗体blot HSS/NPE与IVTT表达爪蟾PRIMPOL阳性对照：IVTT带迁移~95 kDa（预测~77 kDa），HSS/NPE无该位置条带（N端抗体在~55 kDa的带为交叉带，caption以IVTT迁移位置为判据）；(b) 成体组织（心/肝/脾/肺，XenBase已知表达PRIMPOL）阳性而卵提取物阴性，β-actin为载量对照——确立"提取物无内源PRIMPOL"；(c) Coomassie显示纯化的SNAP-tag人PRIMPOL WT/AxA/ΔRPA（~95 kDa）；(d) SYBR Green I酶活曲线（SYBR Green I嵌入双链DNA后荧光增强，故荧光上升=引物延伸产物积累；体系不含RPA/复制因子，只测催化、不测募集）：WT与WT+APH重合（15 µM APH不抑PRIMPOL）、ΔRPA有活性、AxA平坦近背景（n=3，SD）——把"催化"与"RPA结合"在生化层面解耦；(e) mock+10 µM APH+30 nM WT的三条kymograph均无重启（引物无人延伸）；(f) 两次独立提取物制备的重启效率重复（Pol α耗竭：192/134 vs 304/392；损伤：143/79 vs 155/109；buffer vs PRIMPOL均\*\*\*\*，重复间ns）；(g) PCNA–LD655（红）与FEN1–KikG（蓝）共同积累在重启叉后（RPA绿）；(h) FEN1(FFAA)时蓝信号消失而红PCNA仍在；(i) FEN1^WT vs FEN1^FFAA重启效率~0.87 vs ~0.89（N=114/234，ns）——完成" FEN1信号=PCNA募集的新生DNA"的标记validity闭环。

Extended Data Fig. 2a,b（整合解读，损伤底物与速度重复）：(a) DPC经proteinase K消化留~4 aa肽加合物的底物设计示意，及30 nM WT下双叉停滞、单叉重启的代表kymograph（黄箭头停滞、白箭头重启）；(b) Fig. 1h全部七组速度的两次独立重复（N=147/143、93/258、140/127、140/127、137/97、155/109、78/61），组间\*\*\*\*、重复间ns——速度读out的生物学可重复性。

**方法平台补注｜为什么用ensemble质粒复制assay：给单分子发现配上可统计的"批量秤"**

为什么用它。单分子成像通量低、每条件仅百余分子，难以做剂量梯度与突变体筛选的精确统计；ensemble复制assay把数千个质粒模板的复制信号汇总，用放射性掺入定量总DNA合成与完成复制的产物比例，配合3–4次独立重复与t检验，给出可比较的效应量。本文用3 kb pBluescript质粒在HSS中licensing、NPE中复制，α-³²P-dCTP掺入使新生DNA带放射性，0.8%天然琼脂糖凝胶按拓扑构象分离（超螺旋=完成复制的闭环质粒，迁移最快；切口环状、连环体与部分复制中间体依次变慢），磷屏成像读out（Fig. 1j,k；Methods）。

怎么读、注意什么。条带越深=该构象的³²P-DNA越多；比较同一构象带在各泳道的强弱即得剂量/突变体效应。两个读out要分开看：总合成反映"引发了多少"，超螺旋组分反映"完成了多少"——界面突变对后者的损害更甚（Fig. 3g），提示重启效率缺陷而非单纯延伸减慢。体系 caveat：Pol α耗竭激活检查点、抑制origin firing，使总合成上限被压低（ED2c,d），故30 nM WT不能完全回补至mock——这不是PRIMPOL失效，Section 7用ATR抑制剂直接证实。

（来源：本文Methods、refs 32,64,65与ED2c,d。阅读深度：做提取物复制者精读ref 65协议；其余读者理解"总合成vs超螺旋"双读out即可。）

Section 2：Monitoring PRIMPOL-dependent fork restart（PRIMPOL依赖重启的ensemble监测）

内容逻辑：本节把单分子现象转化为可高通量定量的生化assay，并回答"回补是否真的由PRIMPOL的酶活与RPA互作介导"。3 kb质粒在Pol α耗竭提取物中合成被强烈抑制（Fig. 1j ii vs i），残留合成被归因于逃过耗竭的<1% Pol α（ED2c dark exposure）；3–30 nM WT PRIMPOL剂量依赖回补，而30 nM仍未达mock水平。作者对这一"不完全回补"给出机制解释而非含糊带过：Pol α耗竭激活检查点（ED2c pChk1阳性），检查点抑制origin firing使叉数减少（ED2d CDC45 blot减弱），故总合成量上限被压低——这一解释在Section 7被ATR抑制剂实验直接证实（抑制检查点反而增强合成），形成前后呼应的论证闭环。两个先前表征的突变体在此接受检验：AxA（催化死）与ΔRPA（RPA结合死、催化活）都不能回补（Fig. 1j vi–vii, k），与染色质分级结果自洽——WT与AxA能上染色质、ΔRPA不能（ED2d,e；APH条件下同样，ED2e）。由此本节确立"Pol α耗竭提取物忠实复现PRIMPOL依赖重启"的模型地位：它同时要求催化与RPA募集，与细胞遗传学文献（refs 1,4,30,31）一致。本节的贡献是把repriming研究从"看见"推进到"可定量、可突变体筛选"的平台，并埋下两条伏笔：检查点为何压低总合成（Section 7），以及RPA募集之外是否还有叉特异性靶向机制（Section 3–4）。

→ Figure 1（j,k） 见Section 1中(J)(K)四字段解读（该两panel按正文顺序归属本节）：j为代表性自显影、k为三次独立重复定量，共同支撑"催化+RPA互作双必需、剂量依赖、检查点压低上限"三个论点。

Extended Data Fig. 2c–e（整合解读）：(c) Fig. 1j反应45 min样品的blot：POLA1在mock强、耗竭泳道仅痕量（dark exposure可见<1%残留）；pChk1在全部耗竭泳道阳性而mock阴性（检查点激活的直接证据）；总Chk1载量均一；hPP在30 nM WT/AxA/ΔRPA泳道可见——把"不完全回补"归因检查点而非PRIMPOL失效；(d) 染色质分级（测什么：复制中的DNA与结合蛋白经蔗糖垫离心沉淀为染色质组分，blot检测沉淀即'该蛋白是否装载到复制中的DNA上'）：hPP与RPA32在耗竭+WT/AxA泳道富集、buffer/ΔRPA不富集；CDC45在耗竭组减弱（叉数减少）；H3载量均一；(e) 未耗竭提取物+DMSO vs +APH（100 µM）：hPP只在APH+WT/AxA上染色质——证明募集是RS依赖的、且不需要催化活性，与单分子结合数据（Section 3）互证。

**课本化背景补注｜RPA：ssDNA的"包装蛋白"与它的双重角色**

它是什么、为什么重要。RPA（replication protein A）是真核细胞最主要的ssDNA结合蛋白，由RPA1/2/3（RPA70/32/14）三个亚基组成，通过多个OB折叠结构域结合ssDNA。凡有ssDNA暴露的地方——复制、修复、重组——RPA都迅速包被上去：保护ssDNA不被核酸酶降解、去除二级结构、并作为平台招募下游因子。它也是ATR检查点的信号源：RPA–ssDNA被ATR识别后启动CHK1磷酸化（ref 28）。因此RPA既是复制的必需因子，又是应激信号的"天线"。

分子性质与矛盾所在。RPA在核内丰度高、结合ssDNA极快，解偶联产生的长段ssDNA瞬间被其包被。这带来本文Introduction的核心矛盾：既然RPA把PRIMPOL募集到ssDNA（refs 30,31），为什么PRIMPOL只作用于停滞叉、而不作用于转录/重组产生的ssDNA？更棘手的是两条文献直接冲突：Guilliam等（ref 30）报告高浓度RPA完全包被ssDNA会抑制PRIMPOL接近；Martínez-Jiménez等（Blanco组，ref 31）却报告RPA刺激PRIMPOL活性并与Pol ε协同。

缺失或异常的后果。RPA耗竭导致"复制灾难"（ssDNA裸露、叉大规模崩塌，课本级背景）；RPA1亚效突变引起基因组不稳定。本文不耗竭RPA，而是用RPA–mCherryXL实时显示ssDNA范围，把RPA从"背景蛋白"变成可测量的空间标尺。

前人如何研究它。Guilliam等（Nat. Commun. 2017，ref 30）用纯化蛋白定位PRIMPOL的C端RPA结合基序、证明RPA募集PrimPol到ssDNA并发现高RPA抑制；Martínez-Jiménez等（Sci. Rep. 2017，ref 31）用酶活assay证明RPA刺激；Kemmerich等（NAR 2016，ref 59）用磁镊单分子测得RPA在叉上的力依赖动力学（koff=0.006 s⁻¹）——后者被本文Fig. 5j引用为"RPA瞬态解离"的机会窗口。缺口：这些都在纯化体系，核内RPA丰富情境下repriming如何发生从未被直接观察。

与本文的关系。本文用"双锚定+RPA瞬态解离"模型调和矛盾：叉附近双锚定让PRIMPOL在RPA包被前接触模板（解释ref 31的刺激），远端完全包被的ssDNA上PRIMPOL只能瞬态结合（解释ref 30的抑制）；重启后RPA信号减半（Fig. 2a）则成为"只重新引发前导链"的空间证据。

（来源：本文refs 28,30,31,59；复制灾难为课本级背景。阅读深度：ref 30建议精读其互作定位与抑制实验，ref 31可只读结论，ref 59只需其koff数值。）

Section 3：Long-lived PRIMPOL binding near stalled forks（停滞叉附近的长停留PRIMPOL结合）

内容逻辑：本节回答Introduction的核心空间问题——PRIMPOL沿RPA–ssDNA究竟结合在哪里、哪类结合是生产性的。既有模型（RPA募集，refs 4,30）预测PRIMPOL应均匀分布于ssDNA；作者用三色单分子（3 nM PRIMPOL–AF647、15 s/帧）直接检验：远端（fork-distal）结合事件随机分布且~84%只持续一帧（≤15 s）、90%≤0.5 min；而叉附近（≤1 pixel=160 nm）的结合显著更长（71%≤0.25 min、90%≤2.5 min），且长停留fork-proximal结合先于约70±10%的重启事件发生。一个关键的伴随观察是重启后RPA信号强度下降约一半（Fig. 2a底部积分曲线2×→1×）：ssDNA tract变快但RPA量减半，提示只有一条链（前导链）被重新引发——这是"前导链引物酶"假说的第一个直接空间证据（最终由Fig. 4d的Pol ε依赖性确证）。为区分"长停留=生产性"与"长停留=催化死陷阱"，作者比较WT与AxA：AxA的fork-proximal结合频率最高（可反复结合却不重启），但WT与AxA的结合时长分布无统计差异——说明长停留本身不是催化的结果，而是叉环境提供的稳定化；生产性与否取决于催化而非停留。ΔRPA则几乎无结合（与游离AF647背景无异），确立RPA互作是任何结合的前提。时间分辨率对照是本节的方法学亮点：15 s/帧下"连续帧邻近位置结合"可能被误读为单分子沿ssDNA扩散；提速到3 s/帧后看到这些其实是不同分子在非连续帧的短暂结合（86%/84%事件≤3 s），从而排除长程扩散解释（短程扩散不能排除，作者如实保留）。损伤底物上生产性结合同样~3 min，且PRIMPOL解离后3–5 min叉才重启（ED3j）——这段延迟被解释为复制聚合酶捕获引物与replisome重组装所需时间，为Section 6的"引物交接"埋下伏笔。本节的贡献是确立">99%结合非生产性、生产性结合=叉附近长停留"的空间-动力学判据，并把问题从"RPA募集"推进到"叉上还有什么稳定了PRIMPOL"。

→ Figure 2 标题为"PRIMPOL exhibits long-lived binding near stalled forks"，旨在解析PRIMPOL结合的位置、时长与生产性。由a至h共8部分构成：a–b三色kymograph、c–f结合统计、g–h高帧率对照，形成"现象→定量→替代解释排除"的论证结构。

(A) 三色kymograph与RPA积分曲线
图片解释：三色同时成像——品红亮点=单个AF647标记的PRIMPOL分子（结合事件），绿色连续区=RPA–mCherryXL包被的ssDNA范围，蓝色=FEN1报告的新生DNA。Pol α耗竭+3 nM PRIMPOL(WT)–AF647；RPA–mCherryXL绿色tract先慢速双向生长（解偶联），重启后快速生长但强度降约一半；PRIMPOL品红信号中远端短事件（橙三角）与叉附近长停留（白括弧）并存，白箭头=重启；底部插图为RPA积分强度沿DNA的分布（把绿色荧光沿位置积分，曲线高度∝该处RPA量；重启后~50%下降=只有一条链的ssDNA被填补）。定量数据：RPA信号~2倍下降；~70±10%重启 preceded by 长停留（正文）。
横纵轴定义：横轴DNA位置（kb，0–15），纵轴时间；灰点线=解偶联CMG边界、灰虚线=重启叉边界。
颜色含义：绿=RPA–mCherryXL（ssDNA），蓝=FEN1–KikG（新生DNA），品红=PRIMPOL–AF647。
核心结论：重启只清除一条链的RPA（前导链重新引发的空间证据），且生产性结合集中在叉附近。

(B) 结合-解离-重启时序与"扩散？"对照
图片解释：三个kymograph例配右侧卡通时序（PRIMPOL募集→解离→引物→Pol ε重启）；浅蓝椭圆标出连续帧邻近位置结合（"Diffusion?"候选）。定量数据：无（代表性事件）。
横纵轴定义：同A。
颜色含义：同A；白圈=待鉴别的结合序列。
核心结论：提出"单分子扩散 vs 多分子短暂结合"的竞争解释，交由g的高帧率实验裁决。

(C) 结合时长累积分布（15 s/帧，±APH）
图片解释：fork-distal ΔPolα（n=507）与+APH（n=356）曲线重合（NS），fork-proximal ΔPolα（n=193）与+APH（n=151）重合（NS）；proximal显著长于distal（\*\*、\*）；标注84% distal≤0.25 min、90%≤0.50 min、71% proximal≤0.25 min、90%≤2.5 min。定量数据：如标注。
横纵轴定义：X=结合事件时长（min，0–10），Y=累积概率（0.65–1.00）。累积分布读法：Y=时长≤X的事件所占比例，曲线越靠右=长停留事件越多；注意Y轴自0.65起（截断轴），只展示分布上尾部差异。
颜色含义：深灰=proximal、浅灰=distal；实线=ΔPolα、虚线=APH。
核心结论：长停留是叉位置的属性而非RS类型或催化的属性；APH不改变时长但允许反复结合（为Fig. 3c测量窗口铺垫）。

(D) Fork-proximal结合频率
图片解释：mock WT约0.01 min⁻¹、游离AF647约0、耗竭WT约0.055、AxA约0.08（最高）、ΔRPA约0.005 min⁻¹；n（叉数）=56、63、70、61、56；bootstrap 95% CI；WT vs AxA \*\*、其余\*\*\*\*、mock vs AF647 NS。定量数据：AxA>WT>ΔRPA≈背景。
横纵轴定义：Y=单位时间fork-proximal事件数（min⁻¹，把不同观察时长的叉归一到同一尺度），X=条件。点=单个叉的值，柱=均值，误差棒=bootstrap 95% CI。
颜色含义：浅蓝柱=各条件均值，点=单叉值。
核心结论：正常叉几乎不结合PRIMPOL；催化死突变体因"结合而不重启"积累最多叉附近事件——长停留非催化产物。

(E) Fork-distal结合频率（按ssDNA长度归一）
图片解释：WT与AxA约0.10 kb⁻¹ min⁻¹且彼此NS；mock、AF647、ΔRPA均近背景（\*\*\*\*差异）。定量数据：如读自图（约0.10）。
横纵轴定义：Y=kb⁻¹ min⁻¹归一事件数，X=条件。为何双重归一：远端结合机会随ssDNA变长而增多，除以ssDNA长度与观察时长后才能比较'单位DNA上的结合倾向'。
颜色含义：浅灰柱+单叉点。
核心结论：远端结合只依赖RPA互作、与催化无关，且在任何RPA–ssDNA上均匀发生——衬托叉附近稳定化的特异性。

(F) WT vs AxA时长分布
图片解释：proximal WT（n=193）vs AxA（n=317）NS、distal WT（n=507）vs AxA（n=556）NS；proximal vs distal \*\*/\*\*\*\*。定量数据：无显著时长差异。
横纵轴定义：同C。
颜色含义：深灰=WT、橙=AxA；实线proximal、虚线distal。
核心结论：催化与否不影响停留时长——稳定化来自叉环境（互作），而非酶活本身。

(G) 3 s/帧高帧率kymograph
图片解释：白椭圆标出非连续帧的不同分子短暂结合（15 s/帧下会被误读为扩散）；白括弧仍见先于重启的长停留；橙箭头=短事件。定量数据：86%/84%事件≤3 s、95%/91%≤6 s（h）。
横纵轴定义：同A，时间分辨率提高5倍。
颜色含义：同A。
核心结论：排除长程扩散解释；绝大多数结合是秒级瞬态，长停留是稀有但生产性的亚群。

(H) 3 s/帧时长累积分布
图片解释：distal（n=1,929）与proximal（n=654）曲线在秒级尺度上接近（NS），标注86%/84%≤3 s、95%/91%≤6 s。定量数据：如标注。
横纵轴定义：X=时长（min，0–1.0），Y=累积概率。
颜色含义：浅/深点线=distal/proximal。
核心结论：在真实时间尺度上"短命结合"占绝对多数，>99%非生产性；生产性长停留是叉特异的稀有事件。

Extended Data Fig. 3（整合解读，标记验证与动力学细节）：(a) SNAP-AF647标记滴定与PSF3–AF647标准品对照，1.5×摩尔比标记效率89–100%；(b,c) 标记与未标记WT PRIMPOL在ensemble中回补相当（90 min定量ns，n=3）——荧光标记不损伤功能；(d) 30 nM标记PRIMPOL事件过密无法分辨单分子（故主实验用3 nM）；(e) 3 nM下重启前后RPA tract速度~30→~250/230 nt/min（N=108/49，重复间ns）；(f,g,h) ΔRPA几乎无结合、AxA大量长停留、mock几乎无结合的代表kymograph；(i) 3 nM标记WT重启~40%/36%（两次重复）显著高于buffer/AF647/AxA/ΔRPA（\*\*\*\*），且低于30 nM未标记的~75%——浓度依赖与Fig. 4b衔接；(j) 生产性结合的Δt1（结合-解离）中位~3 min、Δt2（解离-重启）在Pol α耗竭中位~5 min、损伤底物~3 min（N=116/34；Δt1组间ns、Δt2 \*）——"PRIMPOL先走、叉后重启"的3–5 min延迟是引物交接假说的动力学依据。

**方法平台补注｜为什么用co-IP、DNA fibre与cryo-EM叠合模型：三种证据各自的能与不能**

co-IP（共免疫沉淀）——为什么用它。要证明AF3预测的PRIMPOL–MCM4互作真实存在，需要在近生理环境中做物理结合验证。本文把仅含N端1–60残基的Flag–SNAP–PRIMPOL bait固定在抗Flag磁珠上，与提取物孵育、洗涤后blot检测共沉淀的MCM7（代表整个MCM2–7六聚体）：若最小bait即可拉下CMG、且界面突变削弱共沉淀，则互作成立且界面特异（Fig. 3d,e）。能：证明物理互作与界面必要性。不能：条带深浅是相对富集量，受bait载量、洗涤严格度与CMG丰度影响，不代表化学计量比或亲和力——故需Flag归一、Mock珠对照与n=3重复，且不能据此断言"一个PRIMPOL结合几个CMG"。

DNA fibre（DNA纤维assay）——为什么用它。提取物体外结论必须回到人细胞验证。Fibre把细胞基因组DNA铺展成单根纤维，用两种卤代核苷酸类似物分时标记：CldU（红，UV停滞前合成）→UV-C 30 J/m²停滞→恢复→IdU（绿，重启后合成），双色免疫荧光下"红+绿接续"=该叉重启、"仅红"=未重启，每条件每次重复计500个复制结构（Fig. 3h,i；ref 1）。它提供单叉分辨率的细胞水平功能读out，配合PRIMPOL-KO HCT116回补做必要/充分判定。局限：3A突变体因重复间变异大未达显著（作者如实注明），且fibre只给功能、不给机制。

cryo-EM叠合模型——模型不等于实验结构。本文Fig. 3a的PRIMPOL–MCM4复合物是AlphaFold3计算预测（非本文实验结构），叠合的底色是已发表的人replisome实验cryo-EM结构PDB 7PFO（Jones等，ref 54），目的是检验预测docking位点与Pol ε拴系是否空间兼容。须分清三层：7PFO是实验结构；本文AF3模型是预测；并行工作（ref 60，companion）的CMG–PRIMPOL实验结构（PDB 30AR/EMD-57512）本身不含DNA，其DNA路径是把PRIMPOL–DNA晶体结构5L2X（Rechkoblit等2016）与7PFO的叉DNA叠合上去的模型（companion Fig. 4d）。因此"DNA从CMG出口走到PRIMPOL"的路径在两项工作中都是模型级推断，而非直接观测——本文"RPA包被前捕获模板"的空间精度应在此边界内理解。

（来源：本文Methods、refs 1,54,60；companion Fig. 4与Data availability。阅读深度：ref 54建议看其replisome整体结构图；companion Fig. 4建议精读；5L2X只需知其提供PRIMPOL–DNA相对取向。）

Section 4：Recruitment to stalled forks via interaction with CMG（经与CMG互作募集到停滞叉）

内容逻辑：本节回答"叉附近什么稳定了PRIMPOL"。作者从AF3/Predictomes出发交叉比对人与蛙蛋白预测，筛出PRIMPOL N端（残基28–40）与MCM4（蛙466–479、670–689两段）的盐桥预测：人R29/R31/K34对应蛙MCM4 E469/D678/E674（人MCM4则为E474/D683/E679，ED4a），并把模型叠合到人replisome cryo-EM结构PDB 7PFO上确认与Pol ε拴系空间兼容。三种独立界面破坏方式（3A中性化、DED电荷反转、29–35:Linker整段侧链删除）构成互证设计：若表型一致则排除单点折叠伪影。第一重证据是结合时长：在APH窗口（允许反复结合而不重启）中三突变体fork-proximal停留均显著短于WT（Fig. 3c）；第二重是物理互作：仅含N端1–60的bait即可从提取物共沉淀MCM2–7，三突变体bait共沉淀效率均下降（Fig. 3d,e，MCM7/Flag归一WT=1，突变体约0.3–0.5）；第三重是功能：ensemble中DED与Linker显著缺陷、3A温和缺陷（Fig. 3f,g），而三突变体体外酶活与WT相当（ED4d）——缺陷只能归因互作而非催化。3A的温和表型被AF3的另一预测（PRIMPOL–MCM7接触，ED4a,b保守性比对支持）解释为残留接触；作者试图用六突变EREDED同时破坏双界面，但其酶活受损（ED4d）而放弃——这一负性结果如实报告，也划定了"双界面解耦"的证据边界。第四重证据落到人细胞：PRIMPOL-KO HCT116回补WT/3A/DED/Linker后做CldU/IdU fibre（UV-C 30 J/m²），DED与Linker显著损害重启、3A下降但重复间变异大致NS（Fig. 3i；作者如实注明）；表达量对照显示DED/3A与WT相当、Linker偏低接近内源（ED4g）。本节的贡献是把"叉附近长停留"归因于一个可预测、可破坏、可在细胞内验证的物理界面（PRIMPOL–MCM4），完成从相关性到因果性的跨越；同时留下两个悬念：MCM7接触的贡献未被干净解耦（EREDED失败），以及该界面是否决定引物去向（Section 6）。

→ Figure 3 标题为"PRIMPOL is recruited to stalled forks through a direct interaction with CMG"，旨在建立PRIMPOL–MCM4界面的预测—互作—功能—细胞四重证据。由a至i共9部分构成：a结构预测、b突变设计、c结合时长、d–e co-IP、f–g ensemble、h–i细胞fibre，形成"预测→物理互作→体外功能→细胞功能"的因果链。

(A) AF3预测界面与replisome叠合
图片解释：左为人PRIMPOL 28–40（品红）与爪蟾MCM4 466–479/670–689（绿）的盐桥模型（R29–E469、R31–D678、K34–E674，青虚线）；右上示意PRIMPOL位于CMG ssDNA出口附近、Pol ε在下方；右下为模型叠合PDB 7PFO（PRIMPOL品红、MCM4绿、GINS橙、Pol ε灰）。定量数据：无（预测模型；置信度指标原文未提供PLDDT/PAE数值）。模型vs实验结构：品红/绿的PRIMPOL–MCM4为AlphaFold3计算预测（非本文实验结构），底色为已发表的人replisome实验cryo-EM结构PDB 7PFO（ref 54）；叠合目的是检验预测docking位点与Pol ε拴系的空间兼容性。本文未自产cryo-EM数据；并行工作（ref 60）的CMG–PRIMPOL实验结构（PDB 30AR）本身不含DNA，其DNA路径亦为5L2X（PRIMPOL–DNA）+7PFO（CMG–叉DNA）叠合模型（companion Fig. 4d）——'DNA路径'在两项工作中均为模型级而非直接观测。
横纵轴定义：无坐标轴（三维结构模型）。阅读方向：观察PRIMPOL N端相对CMG出口通道与Pol ε的落位。
颜色含义：品红=PRIMPOL，绿=MCM4，橙=GINS，灰=Pol ε，黑线=DNA。
核心结论：N端界面把PRIMPOL定位在CMG出口通道旁、且不与其上Pol ε冲突——为"双锚定+即时交接"模型提供结构可行性。

(B) 界面突变设计示意
图片解释：WT N helix–R29/R31/K34–Mod N排列；3A（A/A/A）、DED（D/E/D）、29–35:Linker（GGGSGGGS波浪线）三种破坏方式。定量数据：无（设计图）。
横纵轴定义：无坐标轴（线性结构域示意），横轴为残基位置。
颜色含义：品红框=结构域/模块，蓝tick=WT碱性残基，红tick=电荷反转。
核心结论：三种正交破坏方式互证，排除单点突变折叠伪影的替代解释。

(C) APH窗口中fork-proximal结合时长
图片解释：WT（n=151）曲线右移（长停留），DED（n=234）、3A（n=185）、Linker（n=294）均左移；\*\*\* / \*\* / \*\*\*显著。定量数据：n值如标；时长中位数原文未给具体数值（读图WT长尾至~8–10 min）。
横纵轴定义：X=结合时长（min，0–10），Y=累积概率（0.65–1.00）。累积分布读法同Fig. 2c：曲线右移=停留更长。
颜色含义：蓝=WT、红=DED、灰=3A、黑=Linker。
核心结论：界面破坏缩短叉附近停留——MCM4互作是长停留的稳定化来源。

(D) Co-IP代表性western
图片解释：co-IP测什么：把bait蛋白固定在抗Flag磁珠上、与提取物孵育后洗涤，珠上保留者即'与bait物理结合'的蛋白；再以抗MCM7抗体blot检测共沉淀的CMG（MCM7条带代表整个MCM2–7六聚体）。Flag–SNAP–PRIMPOL(1–60) WT/3A/DED/Linker固定于anti-Flag珠后与提取物孵育；MCM7（~95 kDa）WT强、三突变体弱、extract input强；Flag（~43/34 kDa）bait载量各泳道相当；Mock珠无MCM7。定量数据：代表性条带，灰度定量见e；原文未提供该blot灰度数值。
横纵轴定义：无坐标轴（免疫印迹）。横向为bait条件泳道，纵向为蛋白分子量（kDa）。阅读方向：比较同一MCM7行各泳道条带强弱。
颜色含义：灰度条带，越深代表共沉淀的MCM2–7越多。
核心结论：N端60 aa足以拉下CMG，且界面突变削弱共沉淀——物理互作成立且界面特异。

(E) Co-IP定量
图片解释：MCM7/Flag强度归一WT=1：Mock约0.07、3A约0.34、DED约0.28、Linker约0.46；n=3，mean±s.d.，t检验\*\*\*\*/\*\*\* / \*\*。定量数据：如读自图（约值）。注意：该比值为相对富集效率（受bait载量/洗涤严格度/CMG丰度影响），不是化学计量比或亲和力；Mock珠与Flag归一为其对照。
横纵轴定义：Y=MCM7/Flag强度（0–1.0），X=bait条件。
颜色含义：蓝=WT，灰/黑=突变体与Mock，点=独立重复。
核心结论：三突变体共沉淀效率降至WT的约30–50%，与结合时长缺陷方向一致。

(F) 突变体ensemble复制自显影
图片解释：mock 30/60/90强带；耗竭buffer弱；WT强超螺旋；3A中等；DED与Linker弱（接近buffer）。定量数据：代表性自显影，定量见g。
横纵轴定义：无坐标轴（自显影），横向条件/时间、纵向DNA构象迁移。
颜色含义：灰度越深=³²P-DNA越多。
核心结论：MCM4界面为高效重启所必需，且破坏程度与界面破坏强度排序一致（DED≈Linker>3A）。

(G) Ensemble定量
图片解释：总合成归一WT=1：buffer约0.5、3A约0.85、DED约0.6、Linker约0.7；超螺旋组分WT约0.65、3A约0.4、DED约0.2、Linker约0.3；n=3，t检验（\*\*/\*\*、\*\*\*/\*、\*/NS等）。定量数据：如读自图（约值）。
横纵轴定义：Y=90 min DNA强度（归一化，轴断裂），X=条件。
颜色含义：深灰=总合成、浅灰=超螺旋。
核心结论：界面突变损害完成复制的产物比例更甚于总合成——重启效率缺陷而非单纯延伸减慢。

(H) DNA fibre assay设计与代表纤维
图片解释：DNA fibre测什么：把细胞基因组DNA温和裂解铺展成单根纤维，掺入的卤代核苷酸类似物被抗体识别——CldU与IdU分别由两种抗体显示为红/绿，荧光轨迹长度∝合成量、先后∝合成时序。KO细胞转染48 h→CldU 20 min（红）→UV-C 30 J/m²→恢复30 min→IdU 20 min（绿）；代表纤维：重启=红+绿接续、未重启=仅红。定量数据：500结构/条件/重复（Methods）。
横纵轴定义：无坐标轴（流程+荧光纤维图）。阅读方向：沿纤维看红绿接续。
颜色含义：红=CldU（停滞前合成），绿=IdU（重启后合成）。
核心结论：细胞水平重启读out建立，红绿接续=重启的操作性定义。

(I) 细胞重启效率
图片解释：WT约0.73、KO约0.30、KO+WT约0.53、KO+3A约0.44、KO+DED约0.35、KO+Linker约0.32；n=4（WT/KO/KO+WT）或3（突变体）；\*\*\*\*（WT vs KO、KO vs KO+WT）、NS（KO+WT vs 3A）、\*\*\*（vs DED、vs Linker）。定量数据：如读自图（约值）；3A因重复间变异大未达显著（正文如实注明）。
横纵轴定义：Y=重启叉/总叉（0–1.0），X=回补条件。每点=一次独立重复（每次计500个复制结构）的重启比例，柱=均值。
颜色含义：紫系柱=各条件，点=独立重复。
核心结论：MCM4界面在人细胞内同样为高效重启所需——跨物种、跨体系保守。

Extended Data Fig. 4（整合解读，预测保守性与突变体validation）：(a) AF3盐桥对应表：人PRIMPOL–人MCM4 R29↔E474/R31↔D683/K34↔E679；人PRIMPOL–蛙MCM4 R29↔E469/R31↔D678/K34↔E674——跨物种界面设计依据；(b) 人/蛙/鼠/鸡PRIMPOL N端碱性残基与MCM7/MCM4酸性残基的多序列比对（红框+黄连线），鸡MCM7序列不可得（如实注明）——界面残基保守；(c) 全长WT/3A/DED/Linker/EREDED Coomassie纯度相当；(d) 酶活：3A/DED/Linker与WT同量级（100 nM约520–700 a.u.），EREDED明显降低（约300 a.u.）——界面突变不伤催化、EREDED伤催化故弃用；(e) APH停滞叉上WT反复结合的代表kymograph（RPA–mKikGR绿）；(f) bait蛋白Coomassie载量对照；(g) 转染表达blot：WT/DED/3A相当、Linker偏低近内源，GAPDH与Ponceau S载量对照；(h) 六条件代表fibre图（白箭头重启、黄箭头未重启，标尺25 µm）。

Section 5：PRIMPOL also supports CMG-independent restart（PRIMPOL还支持CMG非依赖重启）

内容逻辑：本节发现并解耦第二种重启模式。低浓度（3 nM）下重启几乎全部经MCM4锚定（CMG依赖）；但>10 nM时出现一类发生在叉后方远处的重启事件（Fig. 4a白星号），其频率随WT浓度成比例上升——浓度依赖提示它同样是repriming而非伪影。关键解耦试剂是DED：它几乎丧失CMG依赖重启（30 nM约0.14 vs WT约0.80），却保留与WT相当的CMG非依赖重启（30 nM约0.15–0.24、100 nM约0.24–0.42，组间NS；ED5a,b）——证明远端重启不需要MCM4界面，是机制上独立的一类事件。速度差异提供第二重解耦：CMG非依赖重启期间新生DNA tract以~700 nt/min生长，显著快于CMG依赖的~300 nt/min（Fig. 4c；ED5c），且该速度在WT与DED间无差异。作者对速度差给出两种竞争解释并如实保留：该过程不需要模板解旋（在已解开的ssDNA上合成），或Pol δ本身比Pol ε快——本文未裁决（Discussion亦未）。本节的贡献是确立"主模式=低浓度、CMG锚定；次模式=高浓度（模拟过表达）、CMG非依赖"的双模式框架，把PRIMPOL过表达文献（refs 14,15）纳入机制解释，并为Section 6的"两种引物去向"与Section 8的"检查点只调次模式"铺路。

→ Figure 4（a–c） 标题为"PRIMPOL restarts forks through two distinct mechanisms: CMG dependent and CMG independent"（全图含d–f，见后两节），旨在发现并解耦两种重启模式。a–c构成"现象→浓度/突变解耦→速度解耦"的证据链。

(A) 双模式kymograph与卡通
图片解释：30 nM未标记WT下双向复制泡：白箭头=CMG依赖重启（叉处慢→快），白星号=CMG非依赖重启（叉后方内部新生DNA tract起点）；两类事件都清除一条亲代链的RPA；左侧卡通：上（绿框）CMG依赖、不受CHK1影响，下（红框）CMG非依赖、受CHK1刺激；虚线框放大显示内部tract（在复制泡内部、而非叉边缘新出现的蓝色生长区，起点远离CMG，其斜率给出独立合成速度）。定量数据：无（代表事件）；Methods注明两模式效率可加和>1（同一泡两叉均CMG依赖重启+额外独立事件）。
横纵轴定义：横轴DNA位置、纵轴时间；内部tract斜率=独立重启合成速度。
颜色含义：绿=RPA–mCherryXL，蓝=FEN1–KikG；白箭头/星号区分两模式。
核心结论：同一分子上可同时看见两种重启，空间位置（叉处 vs 远端）是模式判据。

(B) 浓度×突变体双模式效率
图片解释：WT：buffer绿约0.10/灰约0.03；3 nM绿约0.40/灰约0.02；10 nM绿约0.66/灰约0.06；30 nM绿约0.80/灰约0.24；100 nM绿约0.83/灰约0.42。DED：绿3–100 nM约0.04–0.16（显著低于WT），灰30/100 nM约0.15/0.24与WT相当（NS；100 nM灰\*）；n=438、288、154、320、164、416、258、262、278；bootstrap 95% CI，KS检验。定量数据：如读自图（约值）。
横纵轴定义：Y=重启效率（0–1.0），X=浓度×蛋白分组。
颜色含义：绿=CMG依赖，灰=CMG非依赖。
核心结论：CMG依赖模式在低浓度即高效且需MCM4界面；CMG非依赖模式浓度驱动、界面非必需——两模式遗传解耦。

(C) 两模式合成速度
图片解释：速度来自RPA/FEN1 tract边缘的位置-时间线性拟合（同kymograph斜率法；CMG非依赖事件用OTSU阈值分割FEN1 tract后拟合其生长边缘）。重启前~50 nt/min（n=158）、CMG依赖重启后~300（n=158）、CMG非依赖~700（WT n=59、DED n=38）；\*\*\*\*（前 vs 依赖、依赖 vs 非依赖）、NS（WT vs DED非依赖）；蓝线中位数、阴影bootstrap 95% CI。定量数据：~300 vs ~700 nt/min（正文）。
横纵轴定义：Y=RPA（或FEN1）tract生长速度（nt/min，0–1400），X=事件类型。
颜色含义：黑=重启前，蓝系=CMG依赖/WT非依赖，红系=DED非依赖。
核心结论：非依赖模式合成更快且与界面无关——机制distinct的第二重证据；速度差原因本文未裁决（如实保留两解释）。

Extended Data Fig. 5（整合解读）：(a) 30 nM DED代表kymograph：无CMG依赖重启但保留白星号非依赖事件，卡通标MCM4界面红×与Pol δ延伸；(b) Fig. 4b两次重复（N\_Exp1/Exp2逐条件列出，如438/312、288/161等），灰柱WT vs DED在30/100 nM ns；(c) Fig. 4c两次重复（158/145、158/145、59/35、38/34），非依赖速度WT vs DED ns——双模式解耦的生物学可重复性。

Section 6：Pol ε is required for CMG-dependent fork restart（Pol ε为CMG依赖重启所必需）

内容逻辑：本节回答"引物交给谁"。MCM4锚定把PRIMPOL放在CMG出口旁，而Pol ε物理拴系于CMG（refs 54–56）且叠合模型显示二者空间兼容（Fig. 3a），由此提出竞争假说：解释A，PRIMPOL引物直接交给Pol ε（前导链路径）；解释B，先由Pol δ延伸再交给Pol ε（类似复制起始时前导链建立的路径，refs 42,57）。裁决设计是双耗竭上位性：Pol α+Pol δ耗竭只轻微降低CMG依赖重启（约0.67–0.72 vs mock约0.85，NS/温和），而Pol α+Pol ε耗竭几乎消除它（约0.12）；回补100 nM重组Pol ε（人细胞浓度，ref 49）完全恢复（约0.83）——解释B被排除（若Pol δ是必需中间体，耗竭Pol δ应消除重启），解释A成立。镜像地，CMG非依赖重启被Pol δ耗竭消除（"No restart events detected"）、被400 nM Pol δ回补完全恢复（约0.19–0.22），而Pol ε耗竭不影响它——两模式的引物去向干净分离。一个意外的观察被作者如实记录并解释：Pol α+Pol δ双耗竭（后随链完全阻断）时FEN1–KikG仍积累在重启叉后方（ED6b），最可能是CTF18-RFC在前导链新生DNA上装载PCNA所致——这既维护了FEN1标记的有效性，也侧面印证重启后合成发生在前导链。耗竭效率由flow-cell直接取样blot确认（ED6f：POLD1/POLE1在对应双耗竭泳道消失）。本节的贡献是确立"PRIMPOL主要作为前导链引物酶、引物直接交接Pol ε"的核心结论，把Section 3的RPA减半空间证据升级为因果证据；同时把次模式定义为Pol δ延伸的、类似后随链引发的过程，为Discussion的线粒体原始功能假说提供类比基础。

→ Figure 4（d） 见Figure 4引导语（全图）。(D) 聚合酶耗竭/回补双模式效率
图片解释：Pol α+mock耗竭：+buffer绿约0.08/灰约0.02，+30 nM WT绿约0.85/灰约0.24；Pol α+Pol δ耗竭：绿约0.67（NS vs mock）、灰"No restart events detected"，+400 nM Pol δ绿约0.72/灰约0.19（恢复）；Pol α+Pol ε耗竭：绿约0.12（\*\*\*\*下降）、灰约0.11（NS），+100 nM Pol ε绿约0.83（\*\*\*\*恢复）/灰约0.22；n=134、110、76、76、164、122；KS检验。定量数据：如读自图（约值）；回补浓度100/400 nM取自人细胞浓度（ref 49）。
横纵轴定义：Y=重启效率（0–1.0），X=耗竭×回补分组。
颜色含义：绿=CMG依赖，灰=CMG非依赖。
核心结论：CMG依赖重启专一依赖Pol ε、CMG非依赖专一依赖Pol δ——引物交接去向的因果判定，且回补浓度具生理参照。

Extended Data Fig. 6（整合解读）：(a) Fig. 4d两次重复（134/254、110/124、76/68、76/96、164/48、122/74），"No Restart Events Detected"标注于Pol δ耗竭灰柱；(b) Pol α+Pol δ耗竭代表kymograph：白箭头CMG依赖重启后FEN1蓝仍积累（后随链阻断下）——CTF18-RFC前导链PCNA装载解释；(c) Pol α+Pol ε耗竭代表kymograph：无CMG依赖重启、仅白星号非依赖事件；(d,e) 重组爪蟾Pol ε（POLE1–4）与Pol δ（POLD1–3）Coomassie纯度；(f) flow-cell终点取样blot：POLA1全耗竭泳道阴性、POLD1在α+δ耗竭消失、POLE1在α+ε耗竭消失、H3与hPP对照——耗竭特异性与回补实验的内部validity。

**课本化背景补注｜ATR–CHK1检查点：从"全局开关"到"模式特异性放大器"**

它是什么、为什么重要。ATR–CHK1是真核细胞应对复制应激的主检查点激酶级联：ATR被RPA–ssDNA（经ATRIP/9-1-1/TOPBP1）激活后磷酸化CHK1（Ser345为其激活标志），CHK1再磷酸化众多底物以保护复制叉、抑制晚复制起点激活（origin firing）、促进修复。它之所以重要，是因为检查点决定细胞在应激下"暂停还是继续"，是肿瘤治疗的重要靶点（ATR/CHK1抑制剂已在临床试验，课本级背景）。

分子性质与本文的两个磷酸化位点。要区分两个位点：CHK1自身的Ser345磷酸化=检查点是否激活的标志（本文ED7a用pChk1 S345 blot监测）；PRIMPOL的Ser255磷酸化=CHK1对PRIMPOL的直接调控位点，位于其无序自抑制环（残基201–260）内，磷酸化解除自抑制（ref 22）。检查点激活有DNA浓度阈值：爪蟾体系中约需~1 ng/µl DNA（ref 58），而本文单分子flow-cell的DNA浓度仅10⁻³–10⁻² ng/µl，远低于阈值——故flow-cell中检查点不激活（ED7a实测pChk1阴性）。

缺失或异常的后果。检查点缺陷导致叉崩塌、过早进入有丝分裂与基因组不稳定；ATR亚效突变引起Seckel综合征（小头侏儒，课本级背景）。

前人如何研究它。Byun等（Genes Dev. 2005，ref 28）在爪蟾提取物中证明解偶联产生的RPA–ssDNA激活ATR检查点，确立"解偶联=检查点信号"；Peng等（ref 58）定量了激活阈值；Mehta等（Sci. Adv. 2022，ref 22）用细胞+体外激酶反应证明CHK1磷酸化PRIMPOL Ser255、解除自抑制环、促进repriming与RS耐受——但其效应是在Pol α抑制剂处理的细胞中观察到的，未区分作用于哪种重启模式。缺口：检查点到底是repriming的"必需开关"还是"放大器"？作用于哪条路径？

与本文的关系。本文把检查点从"开关"降级为"次模式放大器"：主模式（CMG依赖）在检查点不激活时仍稳健重启、抑制检查点反而增强合成（ED7b,c）；CHK1–S255轴只上调CMG非依赖次模式（Fig. 4e,f）。并指出ref 22的细胞情境（Pol α抑制→叉后长段ssDNA）恰是次模式的理想底物，故文献效应与本文定位一致——这是"给文献效应划定作用域"而非推翻文献。

（来源：本文refs 22,28,58与ED7；Seckel/临床关联为课本级背景。阅读深度：ref 22建议精读其S255位点与细胞情境，ref 28可只读结论。）

Section 7：CHK1 activation is not required for repriming（CHK1激活非repriming所必需）

内容逻辑：本节处理检查点问题的第一半：主模式是否需要检查点。文献背景是ref 22报告CHK1磷酸化S255促进repriming与RS耐受，隐含"检查点驱动repriming"的印象。作者用两条独立证据反驳其对主模式的适用性：其一，ensemble中Pol α耗竭激活检查点（pChk1阳性），加ATR抑制剂AZD6738（3 µM）阻断CHK1磷酸化后PRIMPOL依赖的DNA合成反而增强（ED7b vi vs v、7c）——若检查点为repriming所必需，抑制它应降低合成；增强效应同时解释了Fig. 1j的"不完全回补"：检查点压低的是origin firing（叉数），不是重启本身。其二，单分子flow-cell中DNA浓度仅10⁻³–10⁻² ng/µl，远低于检查点激活阈值~1 ng/µl（ref 58），flow-cell取样blot确认pChk1阴性（ED7a flow-cell泳道）——即Fig. 1f/2/4中所有稳健重启都发生在检查点不激活的条件下。两条证据一正（抑制检查点增强合成）一反（无检查点仍重启）夹逼出"主模式检查点非必需"。值得注意的是作者并未否定ref 22：细胞内CHK1确实促进repriming，本文将在Section 8把该效应重新定位到次模式——这种"不推翻文献、而是给文献效应划定作用域"的处理是本文论证的分寸所在。本节的贡献是把检查点从"repriming开关"降级为"次模式放大器"，并闭合Section 2留下的总合成量伏笔。

（本节无独立主图；证据来自Extended Data Fig. 7a–c，按四字段解读如下。）

(ED7a) 检查点状态blot
图片解释：mock（i,ii）与Pol α耗竭（iii–vi）及flow-cell样品：Pol α仅mock阳性；S345-pChk1在iii（耗竭+buffer）与v（耗竭+PRIMPOL）阳性、iv与vi（+AZD6738）阴性、flow-cell阴性；总Chk1各泳道均一；PRIMPOL在v、vi与flow-cell阳性。定量数据：代表性blot，原文未提供灰度定量。
横纵轴定义：无坐标轴（免疫印迹）。横向为条件泳道，纵向为蛋白分子量（kDa：180/72/72/95）。阅读方向：比较pChk1行各泳道有无。
颜色含义：灰度条带，越深代表磷酸化CHK1越多。
核心结论：AZD6738有效阻断检查点；单分子flow-cell中检查点不激活——主模式重启发生在无检查点信号条件下。

(ED7b) ATR抑制下的ensemble复制
图片解释：mock i/ii与耗竭iii–vi（buffer/ATRi/PRIMPOL/ATRi+PRIMPOL）30/60/90 min自显影：vi（ATRi+PRIMPOL）超螺旋带最强，甚至超过mock水平。定量数据：代表性胶，定量见c。
横纵轴定义：无坐标轴（自显影），横向条件/时间、纵向DNA构象。
颜色含义：灰度越深=³²P-DNA越多。
核心结论：阻断检查点增强PRIMPOL依赖合成——检查点激活非repriming所必需，且是总合成的压制因素。

(ED7c) Ensemble定量
图片解释：mock约3/2.5（无/有ATRi，ns）；耗竭buffer约0.3/0.1；+ATRi约0.9/0.5（\*/\*\*\*\*）；+PRIMPOL约1.0/0.8；+ATRi+PRIMPOL约4.2/3.4（\*\*\*/\*\*\*\*）；n=3，mean±s.d.，t检验；归一化到耗竭+PRIMPOL无ATRi对照。定量数据：如读自图（约值）。
横纵轴定义：Y=90 min新生DNA信号（0–6），X=条件。
颜色含义：深灰=总合成、浅灰=超螺旋。
核心结论：检查点抑制把PRIMPOL回补上限抬高约4倍——"叉数压制"解释获定量证实。

Section 8：CHK1 upregulates CMG-independent repriming（CHK1上调CMG非依赖repriming）

内容逻辑：本节处理检查点问题的第二半：既然主模式不需要检查点，ref 22的CHK1效应作用于何处？作者用四个先前表征的磷酸化突变体（S255A磷酸死、S255E/D磷酸模拟、Δ201–260表型模拟磷酸化）在30 nM近生理浓度下测双模式：四个突变体的CMG依赖重启均与WT相当（80–90%），而CMG非依赖重启分层明显——WT与S255A最低（~25%）、S255E/D居中（~40%）、Δ201–260最高（~70%）（Fig. 4e）。浓度梯度进一步显示Δ201–260在10与30 nM即显著高于WT的次模式效率（Fig. 4f），即解除自抑制等效于"把次模式的浓度阈值下移"。两个自洽性检查值得注意：S255A≈WT与"flow-cell检查点不激活"（ED7a）自洽——无磷酸化时WT本就处于"未刺激"基线（ED7f caption明确点出）；磷酸化突变体体外酶活与WT同量级（ED7e；S255A读图略低），排除"催化差异解释效率分层"。作者还把本文结论与ref 22的细胞实验条件对齐：该研究的CHK1刺激效应是在Pol α抑制剂处理细胞中观察到的——Pol α抑制产生叉后长段ssDNA，恰是CMG非依赖repriming的理想底物，故文献效应与本文"次模式放大器"定位一致。本节的贡献是完成检查点调控的模式归属：CHK1–S255轴不控制主模式、只放大次模式，从而把"检查点促进repriming"的旧结论精确化为"检查点促进远端、Pol δ延伸的repriming"；与Section 5–6合并，双模式框架（浓度、界面、聚合酶、检查点四维解耦）至此闭合，直接导出Fig. 5模型。

→ Figure 4（e,f） 见Figure 4引导语。(E) 磷酸化突变体双模式效率（30 nM）
图片解释：buffer绿约0.11/灰约0.03；WT绿约0.80/灰约0.25；Δ201–260绿约0.89/灰约0.66；S255E绿约0.84/灰约0.40；S255D绿约0.88/灰约0.43；S255A绿约0.88/灰约0.25；n=438、320、130、174、148、248；灰柱WT vs Δ201–260 \*\*\*\*、vs S255E/D \*\*、vs S255A NS；绿柱组间NS。定量数据：80–90% CMG依赖；~25%/~40%/~70%次模式分层（正文）。
横纵轴定义：Y=重启效率（0–1.0），X=突变体。
颜色含义：绿=CMG依赖，灰=CMG非依赖。
核心结论：CHK1位点/自抑制环只调控次模式——检查点效应的模式归属。

(F) Δ201–260浓度梯度
图片解释：WT 3/10/30 nM绿约0.39/0.66/0.80、灰约0.02/0.06/0.25；Δ201–260绿约0.46/0.74/0.88（NS）、灰约0.08/0.38/0.66（10与30 nM \*\*\*\*）；n=438、288、154、320、174、108、130。定量数据：如读自图（约值）。
横纵轴定义：Y=重启效率，X=浓度×蛋白。
颜色含义：绿/灰同E。
核心结论：解除自抑制使次模式在近生理浓度即被启用——等效于过表达/磷酸化的效果，支撑"次模式=过表达/检查点解锁"模型。

Extended Data Fig. 7d–g（整合解读）：(d) 磷酸化突变体Coomassie纯度；(e) 酶活曲线与WT同量级（100 nM：WT约670、Δ201–260约640、S255D约540、S255E约520、S255A约450 a.u.，读自图；n=3 SD）——效率分层非催化差异；(f) Fig. 4e两次重复（438/312、320/220、130/148、174/84、148/178、248/126），caption点明S255A≈WT因flow-cell无检查点活性；(g) Fig. 4f两次重复（438/312、288/161、154/156、320/220、174/222、108/140、130/148），次模式差异\*\*/\*\*\*\*、绿柱ns。

---

四、<Discussion结构分析>

**第1层：四步主模式模型与双模式总图（Fig. 5，已证实为主、细节含推测）。** Discussion开篇把全部结果整合为Fig. 5的12 panel模型：正常复制时Pol ε/δ紧随CMG、叉后无RPA–ssDNA，PRIMPOL无处结合（a）；RS解偶联产生RPA–ssDNA（b）；PRIMPOL在远端瞬态结合、几乎不生产（c）；在叉附近先经RPA结合（d）、再经MCM4双锚定延长停留（e）；长停留使其在CMG正后方、RPA包被前捕获前导链模板合成短引物（f）；PRIMPOL解离后Pol ε捕获引物（g）并延伸重启（h）；高浓度时大量瞬态结合（i）等待RPA瞬态解离露出ssDNA（j）、在远端引发（k）、由Pol δ延伸（l）。蓝底b–h=CMG依赖、低浓度高效、CHK1非必需；红底i–l=CMG非依赖、高浓度/CHK1磷酸化启用。该层的态度标注：a–h各步有Fig. 1–4的直接功能证据支撑（已证实），但"同时双锚定"与"RPA包被前捕获模板"是模型推断（见第2层与重点思考提问1）；i–l中RPA瞬态解离步骤引用体外单分子koff=0.006 s⁻¹（ref 59）而非本文直接观察（推测成分）。

→ Figure 5 标题为"Proposed model of PRIMPOL-dependent replication fork restart"，旨在整合双模式机制。由a至l共12部分构成，形成"正常→应激→主模式四步→次模式四步"的机制叙事。

(A) 未扰动复制
图片解释：Pol ε/δ紧随CMG合成两链，RPA仅少量存在于后随链模板；PRIMPOL（品红）被红×标出无法结合CMG或ssDNA。定量数据：无（模型卡通）。
横纵轴定义：无坐标轴（机制示意图）。阅读方向：沿DNA看聚合酶与CMG的偶联状态。
颜色含义：绿=RPA，品红=PRIMPOL，灰=CMG/聚合酶，蓝=新生DNA；绿底=正常状态。
核心结论：正常叉后无RPA–ssDNA且docking位点可能被遮蔽——解释PRIMPOL为何不干扰正常复制（Fig. 2d mock近零结合）。

(B) 复制应激解偶联
图片解释：CMG继续解链、两链模板被RPA包被形成长ssDNA tract。定量数据：无。
横纵轴定义：无坐标轴。
颜色含义：蓝底=CMG依赖路径起点；绿=RPA。
核心结论：解偶联创造双锚定所需的两个配体（RPA–ssDNA与裸CMG）。

(C) 远端瞬态结合
图片解释：PRIMPOL在远离CMG处与RPA可逆结合（双向灰箭头），事件短命。定量数据：对应Fig. 2c/h（84–86%≤15 s/3 s）。
横纵轴定义：无坐标轴。
颜色含义：品红=PRIMPOL，绿=RPA。
核心结论：RPA互作 alone 只给瞬态结合——>99%非生产性。

(D) 叉附近RPA结合
图片解释：PRIMPOL结合到靠近CMG的RPA上。定量数据：对应Fig. 2d fork-proximal频率。
横纵轴定义：无坐标轴。
颜色含义：同C。
核心结论：空间接近是第一步，但尚不足以长停留。

(E) 双锚定（RPA+MCM4）
图片解释：PRIMPOL同时接触RPA（C端）与MCM4（N端），停留延长；MCM4文字标注。定量数据：对应Fig. 3c–e（界面突变缩短停留、削弱co-IP）。
横纵轴定义：无坐标轴。
颜色含义：同C；MCM4为CMG上标注亚基。
核心结论：双锚定是叉特异靶向与长停留的分子基础（模型核心；"同时"为推断）。

(F) CMG正后方合成引物
图片解释：PRIMPOL在CMG出口处、RPA包被前于前导链模板合成短引物（蓝短线）。定量数据：对应Fig. 2a RPA减半（单链引发）。
横纵轴定义：无坐标轴。
颜色含义：蓝=新合成引物/新生DNA。
核心结论：双锚定把PRIMPOL摆到"RPA来不及包被"的位置——调和核内RPA丰富矛盾。

(G) PRIMPOL解离、Pol ε捕获引物
图片解释：PRIMPOL离开，Pol ε接近引物3'端。定量数据：对应ED3j Δt2 3–5 min延迟。
横纵轴定义：无坐标轴。
颜色含义：灰蓝=Pol ε。
核心结论：交接存在时间窗口；解离触发机制未明（作者列两假说，见第6层）。

(H) Pol ε延伸重启前导链
图片解释：Pol ε沿前导链连续合成，RPA被清除、CMG恢复快速。定量数据：对应Fig. 4d Pol ε耗竭/回补。
横纵轴定义：无坐标轴。
颜色含义：蓝=新生前导链。
核心结论：主模式=前导链引物酶+Pol ε延伸，易错合成被压缩到一段短引物。

(I) 高浓度大量瞬态结合
图片解释：多个PRIMPOL分子散布于RPA–ssDNA。定量数据：对应Fig. 4b灰柱浓度依赖。
横纵轴定义：无坐标轴。
颜色含义：红底=CMG非依赖路径。
核心结论：浓度升高提高"等待RPA解离"的分子数——次模式的浓度阈值来源。

(J) RPA瞬态解离露出ssDNA
图片解释：一个RPA分子离开，局部ssDNA裸露于PRIMPOL附近。定量数据：引用ref 59 koff=0.006 s⁻¹（体外）。
横纵轴定义：无坐标轴。
颜色含义：绿=RPA（离开者以箭头标出）。
核心结论：次模式的机会窗口来自RPA自发解离（本文未直接观察，推测）。

(K) 远端引发
图片解释：PRIMPOL在远离CMG处合成引物。定量数据：对应Fig. 4a白星号内部tract。
横纵轴定义：无坐标轴。
颜色含义：蓝=引物。
核心结论：次模式不需要CMG锚定（DED保留该模式）。

(L) Pol δ延伸重启
图片解释：Pol δ捕获并延伸远端引物，独立于CMG恢复合成。定量数据：对应Fig. 4d Pol δ耗竭/回补与~700 nt/min。
横纵轴定义：无坐标轴。
颜色含义：灰=Pol δ。
核心结论：次模式=Pol δ延伸的、类后随链引发过程；与线粒体类比衔接（第3层）。

**第2层：双锚定模型对三个长期问题的"简单而优雅"回答（已证实的功能+推断的结构细节）。** 作者明确列出模型解释力：其一，PRIMPOL只有在不解偶联叉后才能同时遇到RPA与MCM4两个配体，故靶向停滞叉而非转录/重组ssDNA（回答Introduction第3段第一问）；其二，双锚定把PRIMPOL摆到CMG出口通道旁，使其在RPA包被前接触前导链模板，故核内RPA丰富仍允许repriming（回答第二问，并调和ref 30"高RPA抑制"与ref 31"RPA刺激"的矛盾——抑制发生在RPA完全包被的远端ssDNA，刺激发生在叉附近双锚定情境）；其三，CMG拴系的Pol ε就在引物旁，交接快、PRIMPOL易错合成被限制为短引物（回答保真控制问）。支撑证据为Fig. 2（空间）、Fig. 3（界面）、Fig. 4d（交接）；态度标注：功能层面已证实，"同时结合"与"包被前捕获"为结构推断（本文无共定位单分子或结构数据，并行工作ref 60的cryo-EM在Discussion被引为佐证但非本文数据）。

**第3层：次模式的生理意义与线粒体"原始功能残留"假说（推测）。** 作者把高浓度次模式与化疗/癌基因诱导的PRIMPOL过表达（refs 14,15）联系："tempting to speculate"过表达解锁CMG非依赖重启；并以RPA瞬态解离（koff=0.006 s⁻¹，ref 59）解释次模式的机会窗口。进一步类比线粒体：PRIMPOL与Twinkle/mtSSB/Pol γ互作（refs 9,61）、mtDNA损伤后重启需要PRIMPOL（ref 61）、Twinkle体外刺激其酶活（ref 62）、过表达增加mtDNA后随链引发——作者据此提出CMG非依赖repriming可能是PRIMPOL为mtDNA后随链引发的vestigial/primordial角色，平时被RPA/mtSSB压制、过表达或CHK1磷酸化时解锁。态度标注：明确speculative；本文无mtDNA实验，类比仅基于文献与本文次模式表型的相似性。

**第4层：正常叉为何不结合PRIMPOL——两种竞争解释（部分推测）。** 观察：mock中PRIMPOL结合可忽略（Fig. 2d,e；ED3h）。解释A：正常复制叉后无RPA–ssDNA（Fig. 5a），缺配体；解释B：docking位点被延伸因子空间遮蔽，例证CTF18结合MCM7 C端（ref 45，紧邻MCM4）。作者未裁决二者（"could be…Alternatively…"），态度标注：解释A有Fig. 2a/5a支持但非排他，解释B纯推测。该层为模型补上"不干扰正常复制"的安全性说明，也留下可检验预测（如CTF18耗竭是否允许正常叉结合PRIMPOL）。

**第5层：并行工作与领域定位、治疗策略（已证实的互证+提议）。** 作者披露撰稿期间得知Yeeles组（MRC LMB）并行研究（ref 60：Polo Rivera et al., Nature 2026, DOI 10.1038/s41586-026-11204-0）用纯化人蛋白重建PRIMPOL依赖重启并获得CMG–PRIMPOL cryo-EM结构，与本文AF3预测高度相似（personal communication）——两条独立路线（提取物单分子+遗传学 vs 纯化体系+结构）互证界面与机制。治疗层面：目前无小分子PRIMPOL抑制剂（refs 17,63），本文提议以结合PRIMPOL N端（MCM4界面）的肽或分子阻断PRIMPOL–CMG互作来抑制repriming——把机制发现直接转化为靶点策略（提议，未做化合物验证）。

**第6层：作者自陈的不确定与局限（承认不确定性）。** 逐条：(1) PRIMPOL在引物合成后、重启前解离的触发机制未明，列两假说——引物变长后脱离RPA、或瞬态脱离MCM4期间CMG募集了阻止其再结合的因子（Fig. 2b；ED3j延迟的现象学解释）；(2) 核内PRIMPOL真实浓度未知：OpenCell的~17 nM含线粒体池，核浓度无可靠估计且随细胞类型变化，故本文采样3–100 nM并以10–30 nM称"近生理"（Methods如实声明）；(3) EREDED六突变因酶活受损弃用，MCM7接触贡献未干净解耦（ED4d）；(4) 3A在细胞fibre中因重复间变异大未达显著（Fig. 3i）；(5) 次模式速度~700 nt/min的成因未裁决（无需解旋 vs Pol δ更快，Fig. 4c）；(6) 短程PRIMPOL扩散不能排除（Fig. 2g/h只排除长程）。

**Discussion没有讨论什么（局限性）：**

(1) 缺乏体内/疾病模型验证：细胞层面仅HCT116 fibre回补，无小鼠或肿瘤模型检验MCM4界面突变对RS耐受/化疗敏感性的影响，治疗策略（N端阻断肽）停留在提议——机制的生理权重与可药性未被体内证据支撑。
(2) 次模式的生理相关性未被直接测量：高浓度只是"模拟过表达"，本文未测癌基因/化疗细胞中内源PRIMPOL是否真的过表达、以及次模式在其中占比（refs 14,15仅被引用）——次模式可能主要是体外/过表达情境的现象。
(3) 引物交接与双锚定缺乏本文自产的直接结构/共定位证据：无cryo-EM、无PRIMPOL与MCM4/RPA的同时双色单分子共定位，"同时双锚定""Pol ε直接捕获"依赖遗传上位性与AF3/并行结构（ref 60）——因果链干净但结构细节是推断。
(4) 引物位置与链特异性的核苷酸级证据缺失：前导链归属来自RPA信号减半+Pol ε依赖+损伤底物设计，未对repriming引物做链特异/位置 mapping（如测序或核苷酸分辨率标记）——"CMG正后方、RPA包被前"的空间精度是模型级而非测量级。
(5) RPA瞬态解离窗口未在本文体系直接观察：koff引用体外单分子文献（ref 59），提取物中RPA密度/修饰可能不同；次模式的机会窗口假说缺直接成像证据。
(6) 检查点调控的生化直接性不足：本文用ATRi与磷酸化突变体推断CHK1–S255轴的作用域，但未在提取物中直接检测PRIMPOL S255磷酸化状态或做CHK1激酶反应——"磷酸化只调次模式"是遗传学结论而非生化结论。
(7) 跨物种界面的细胞内生化验证缺失：界面残基以人PRIMPOL–蛙MCM4盐桥设计、MSA保守性支持，人细胞中只有fibre功能读out，无人源co-IP/结构验证（并行ref 60为人源体系但非本文数据）。
(8) 与fork reversal/TLS/后随链gap修复的通路竞争未展开：Introduction提及反转与repriming竞争（refs 7,21,22），但本文体系未测反转或gap后续修复（HR/填充），双模式在完整RS网络中的权重未知。

---

五、<重点思考>

**（一）核心概念/方法/通路/模型概括解读：**

核心概念——Repriming作为受控的RS耐受通路：内涵是"跳过损伤、下游重新引发"而非损伤处合成；重要性在于它解释细胞如何耐受化疗/癌基因应激并产生PARP抑制剂敏感的ssDNA gaps；本文推进在于给它补上空间靶向（双锚定）、保真控制（短引物+Pol ε交接）与调控归属（CHK1只调次模式）三层机制；边界是本文体系为提取物+细胞fibre，体内权重未测。

核心概念——CMG解偶联作为"信号平台"：内涵是解旋酶与聚合酶速度失配产生RPA–ssDNA；重要性在于它既是检查点信号源也是本文双锚定的配体来源；本文推进在于证明解偶联叉同时提供RPA与裸MCM4两个配体、从而把PRIMPOL活性空间限定于停滞叉；边界是正常叉docking位点是否另被遮蔽（CTF18假说）未裁决。

核心模型——双锚定靶向与引物交接（Fig. 5e–h）：内涵是N端–MCM4+C端–RPA同时结合把PRIMPOL摆到CMG出口、引物直接交Pol ε；重要性在于一次回答靶向、RPA矛盾、保真三问；本文推进在于界面预测—co-IP—结合时长—ensemble—fibre五重验证；边界是"同时结合"为推断、结构细节依赖并行cryo-EM（ref 60）。

核心模型——CMG依赖/非依赖双模式（Fig. 4–5）：内涵是低浓度主模式（Pol ε）与高浓度/CHK1次模式（Pol δ）；重要性在于把过表达文献与检查点文献纳入统一框架、并给出速度/界面/聚合酶/磷酸化四维解耦；本文推进在于DED与磷酸化突变体的干净遗传解耦；边界是次模式生理相关性未直接测量。

核心方法——KERMIT提取物单分子成像+GLRT事件检测：内涵是双tether DNA+两步灌流+实时TIRF把复制/RS/重启变成单分子电影；重要性在于本文所有空间-动力学结论（长停留、非生产性 majority、解离-重启延迟）都依赖它；本文推进在于三色通道与3 s/帧高帧率对照排除扩散伪影；边界是荧光标记/低DNA浓度（检查点不激活）等体系特性需对照验证（本文已做）。

核心方法——AF3跨物种界面筛选+正交突变互证：内涵是用Predictomes/AF3在人–蛙间筛保守互作、以中性化/电荷反转/linker删除三种方式破坏界面；重要性在于把"预测"变成"可证伪的因果界面"；本文推进在于预测被co-IP与四重功能验证证实、且与并行cryo-EM一致；边界是EREDED失败显示多界面解耦仍受酶活混杂限制。

**（二）本篇文章发现的完整概括：**

本文从repriming机制的三个缺口出发——PRIMPOL如何靶向停滞叉、在RPA丰富的核内如何引发、易错合成如何被限制——在不含内源PRIMPOL的爪蟾卵核提取物中补充重组人PRIMPOL，用KERMIT单分子成像直接看见重启：两种正交应激下CMG从~30 nt/min解偶联空转恢复~300 nt/min并伴随新生DNA合成，效率从~5–7%升至~50–75%。三色单分子显示>99%结合为远端秒级瞬态、非生产性，生产性结合是叉附近~3 min长停留、先于约70%重启；重启后RPA减半提示只重新引发前导链。AlphaFold3跨物种筛选锁定N端R29/R31/K34–MCM4盐桥界面，三种正交突变在结合时长、co-IP、ensemble与人细胞fibre四层证明其必要性。聚合酶双耗竭+生理浓度回补判定引物去向：CMG依赖模式专一交Pol ε、CMG非依赖模式专一交Pol δ，后者仅>10 nM（模拟过表达）显著且更快（~700 nt/min）。检查点被重新定位：主模式不需检查点激活，CHK1–S255磷酸化只放大次模式（~25%→~40%→~70%分层）。最终整合为"双锚定靶向+即时Pol ε交接"主模式与"RPA瞬态解离+Pol δ延伸"次模式总模型，并提议N端界面阻断肽作为肿瘤治疗策略。同时以坦率态度划定边界：提取物与fibre的体系边界、"同时双锚定"的结构推断属性、次模式生理权重与核内真实浓度的未知。本文的领域贡献在于：其一，给十年历史的repriming通路补上空间靶向与引物交接的分子机制，直接证实"前导链引物酶"假说；其二，以双模式框架调和RPA抑制/刺激矛盾与CHK1文献效应的作用域；其三，把AF3预测界面转化为可药性靶点提议，并与并行纯化体系cryo-EM工作互证。

**1. 研究问题定位：**
学科交叉位置：DNA复制/基因组稳定性 × 单分子生物物理 × 结构预测 × 肿瘤治疗靶点。问题层级：分子机制/机器组装层级（募集界面、引物交接、调控归属），而非组学图谱或临床层级。工作类型：概念创新（双锚定+双模式模型）与技术性/结构性（KERMIT扩展、AF3界面验证）兼具，末段带转化提议。实验层级：体外无细胞重建（提取物单分子+ensemble）+ 人细胞fibre，无动物/临床。一句话核心定位：给一个发现十年却"只知现象不知机制"的RS耐受通路补上空间靶向、保真控制与调控归属的分子一环。

**2. 为什么能发Nature（证据链评估）：**
最扎实处有三。其一，读out与模型的多重正交验证：两种独立RS来源、两种新生DNA标记（FEN1/PCNA）加FFAA解耦、两次以上独立提取物重复、ensemble与单分子互证——使"看见重启"本身几乎无替代解释空间。其二，界面因果链的完整性：AF3预测→三种正交突变→结合时长/co-IP/ensemble/人细胞fibre四重表型一致，且突变体酶活对照排除催化混杂——预测被证伪风险高而未被证伪。其三，双模式的四维遗传解耦（浓度、MCM4界面、Pol ε/δ上位性、磷酸化突变体）干净分离两条路径，并把既有文献矛盾（RPA抑制vs刺激、CHK1效应）收编为模型的作用域而非反例。不足在于：本文自产证据止于功能遗传学与AF3模型，双锚定/交接的结构细节依赖并行工作（ref 60）；细胞验证仅fibre、3A未达显著；次模式生理权重与体内可药性未测。本文为已接收在刊文章（非预印本），其形态反映Nature对"机制闭环+领域问题收编"的偏好；并行结构工作同期发表亦说明该问题处于领域竞争热点。

**3. 创新点逐条列出：**
- [概念创新] 双锚定靶向模型：PRIMPOL经N端–MCM4与C端–RPA同时结合被限定于解偶联叉（Fig. 3、Fig. 5e）。
- [发现创新] 生产性结合的空间-动力学判据：>99%远端瞬态非生产、叉附近~3 min长停留先于~70%重启（Fig. 2；ED3j）。
- [发现创新] 前导链repriming的直接证据：重启后RPA减半+Pol ε专一依赖（Fig. 2a、Fig. 4d）。
- [机制创新] PRIMPOL–MCM4盐桥界面（R29/R31/K34）为募集与高效重启所必需，跨提取物与人细胞保守（Fig. 3）。
- [机制创新] 引物交接去向的模式分离：主模式Pol ε、次模式Pol δ（Fig. 4d）。
- [机制创新/调和性贡献] 检查点作用域重划：主模式CHK1非必需、CHK1–S255只放大次模式，收编ref 22与RPA矛盾文献（Fig. 4e,f；ED7）。
- [方法创新] KERMIT扩展至RS/三色/高帧率+GLRT事件动力学，排除扩散伪影（Fig. 2g,h；Methods）。
- [转化提议] 以N端界面阻断肽/分子抑制repriming的治疗策略（Discussion末段）。

**4. 前置依赖：**
技术前置：KERMIT与提取物复制成像（refs 25,34,70）、GLRT事件检测与双向起始分析（ref 71）、卵提取物制备（refs 32,64,65）、DPC/肽加合物底物（ref 25）、DNA fibre重启assay（ref 1）、AF3（ref 53）与Predictomes（ref 52）、人replisome结构PDB 7PFO（refs 54–56）、SYBR Green I酶活assay（ref 68）、MultiBac杆状病毒表达（ref 67）。生物学概念前置：2013年repriming发现（refs 1–4）、RPA–PRIMPOL互作与矛盾（refs 30,31）、CHK1–S255与自抑制环（ref 22）、CMG解偶联与检查点阈值（refs 25–28,58）、前导链建立需Pol α/Pol δ参与（refs 42,43,57）、OpenCell蛋白浓度图谱（ref 49）、RPA解离动力学（ref 59）。生信/进化前置：AF3互作预测与跨物种MSA保守性（ED4b）、bootstrap/KS统计框架（Methods）、target-decoy MS FDR（ref 69）。

**5. 基因编辑/遗传操作细节：**
本文未进行新的基因编辑；细胞层面使用Méndez实验室已建立的PRIMPOL-KO HCT116做transient回补（pcDNA3.1/V5-PRIMPOL，Lipofectamine 2000），其"遗传操作"实为体外蛋白工程+回补互补。构建体清单与设计价值：AxA（催化死，解耦催化vs募集）；ΔRPA（RPA结合死、催化活，解耦募集vs催化）；3A/DED/29–35:Linker（MCM4界面三种正交破坏，互证排除折叠伪影）；EREDED（双界面六突变，因酶活受损弃用——负性结果如实报告）；Δ201–260与S255E/D/A（自抑制环/磷酸化位点，定位检查点作用域）；Flag–SNAP–PRIMPOL(1–60) bait（最小界面共沉淀，证明N端足以结合CMG）；FEN1–KikG与FEN1(FFAA)（标记validity解耦）；GINS–LD655、PCNA–LD655、RPA–mCherryXL（正交通道）。对照逻辑：每个突变体均配体外酶活对照（ED1d/4d/7e）与表达量对照（ED4g），确保表型归因于互作/调控而非催化或表达差异；KO+WT回补与KO空载构成细胞水平必要/充分对照。

**6. 与课题组/领域的关联：**
通讯作者Chistol团队的研究主线是"单分子看见复制与修复"：本文直接地基前作包括Sparks et al. Cell 2019（ref 25，CMG绕过DPC、KERMIT雏形）、Terui et al. Cell 2024（ref 71，GLRT与双向起始）、Berger & Chistol Methods Cell Biol 2023/2024（refs 34,70， assay协议）、以及同组Lynch, Park & Chistol Cell 2026（ref 66，后随链distributive合成；Methods中Pol δ克隆纯化流程引该文，Fig. 4d回补所用Pol δ/ε由Lynch表达纯化）——本文是该主线从"正常复制"向"复制应激与重启"的延伸。Méndez团队贡献PRIMPOL细胞遗传学平台：PRIMPOL-KO HCT116、人PRIMPOL单抗（106E/71D，Methods注明由Méndez实验室与CNIO单抗设施制备，ref 13）与fibre assay（Methods；established assay引ref 1），本文由CNIO成员（E.B.-R.、R.M.-M.）完成细胞部分——两条主线（单分子生物物理×PRIMPOL细胞遗传学）交汇。本文对"领域早已知然不知其所以然"的旧观察补机制：PRIMPOL只作用于停滞叉（refs 30,31矛盾）、前导链repriming假说无直接证据（ref 2）、CHK1促进repriming（ref 22）——三者分别被双锚定、RPA减半+Pol ε依赖、次模式归属解释。并行/互补工作：Yeeles组ref 60（Polo Rivera et al. Nature 2026，纯化人蛋白+CMG–PRIMPOL cryo-EM）在Discussion被明确披露为同期互证（companion PDF 可按 `_shared/papers/README.md` 的 DOI 自行获取，对照精读）。与读者研究方向的关联（示例）：对RNA结构生物学/核酸–蛋白互作方向，本文的方法论范式最具迁移价值——"AF3跨物种界面筛选→正交突变互证→单分子/ensemble双读out"可直接套用于RNA–蛋白互作界面研究；KERMIT的"速度切换作为功能读out"与GLRT瞬态事件检测对核酸酶单分子assay设计有参考意义；对表观遗传方向，本文属复制应激而非直接表观遗传，但复制叉–染色质维护耦合是表观遗传继承的细胞学背景，JC讨论时可从"复制应激下染色质/表观标记如何维持"切入提问。通讯作者详细履历、奖项与基金等PDF之外事实不在本解读断言（详见同源背景解读）。

**7. 数据与材料可及性：**
原始单分子/ensemble数据与自研MATLAB代码：Stanford Digital Repository，DOI 10.25740/hy921dn6469（https://purl.stanford.edu/hy921dn6469），公开；Source data随文提供。无GEO/测序accession（无高通量测序）；无新PDB/EMDB deposition（引用PDB 7PFO）。质粒：pJP/pGC/pLDL系列全列于Methods（如pJP012 WT、pJP057 AxA、pJP058 ΔRPA、pJP093/052/051界面突变、pJP013 Δ201–260、pJP102–104磷酸化突变、pJP084/095/085/097 bait、pLDL158 Pol ε/δ表达）；引物列Supplementary Table 2（未提供）。抗体：多为实验室自制（Chistol lab SU系列、Méndez lab 106E/71D、Biosynth L3754/3755），商业抗体（H3、CHK1、pCHK1 Ser345、FLAG）列Reporting Summary；完整抗体表Supplementary Table 3（未提供）。细胞系：HCT116 PRIMPOL-proficient/KO（Méndez lab）、Sf9/Tni（Expression Systems）、DH10EMBacY/DH5α/Rosetta(DE3)pLysS。试剂/蛋白"available on request from the corresponding author"。补充材料状态：ED Fig. 1–7随PDF提供；Supplementary Tables 1–4与Supplementary Data未随PDF提供（在线）。

**（三）面向阅读的核心提问：**

- **问题1：** "双锚定（同时结合RPA与MCM4）"是直接观察还是模型推断？本文能答到什么程度：co-IP证明N端–CMG物理互作、ΔRPA证明RPA互作必需、界面突变缩短叉附近停留——但三色实验无CMG通道，未做PRIMPOL与MCM4/RPA的同时共定位，"同时"与"RPA包被前捕获模板"是推断；并行ref 60的cryo-EM可补结构细节但非本文数据。证据强度初判：中（功能遗传学强、直接可视化弱）。交接：→ 待背景解读（paper-background-research）跨文献精研ref 60结构界面与本文模型的一致性。
- **问题2：** 引物交给Pol ε是"直接捕获"还是经Pol δ中间体？本文能答到什么程度：Pol δ耗竭仅轻微影响CMG依赖重启、Pol ε耗竭消除且回补恢复——遗传上位性干净排除Pol δ必需中间体；但无Pol ε荧光通道直接观察交接瞬间，ED3j的3–5 min延迟只给时间窗口。证据强度初判：中强。交接：→ 待背景解读结合ref 60结构与refs 42,57起始交接文献比较。
- **问题3：** 次模式（CMG非依赖/Pol δ）在真实癌细胞中占多大权重？本文能答到什么程度：仅浓度模拟过表达+磷酸化突变体分层，未测内源过表达细胞中次模式占比；refs 14,15被引但未实验衔接。证据强度初判：弱–中。交接：→ 待背景解读跨文献精研refs 14,15,22的细胞情境与本文体系的可比性。
- **问题4：** PRIMPOL为何在引物合成后、重启前3–5 min解离？本文能答到什么程度：仅现象学（ED3j Δt2）与两假说（引物变长脱离RPA；瞬态脱离MCM4期间再结合被阻），无判别实验。证据强度初判：弱。交接：→ 待背景解读结合同行结构/动力学文献提出可检验预测。
- **问题5：** 人PRIMPOL–蛙MCM4跨物种界面在人细胞内是否同样成立？本文能答到什么程度：MSA保守性（ED4b）+人细胞fibre中DED/Linker缺陷支持，但3A NS、无人源co-IP/结构；界面盐桥对应残基在人MCM4为E474/D683/E679（ED4a）仅预测级。证据强度初判：中。交接：→ 待背景解读以ref 60人源体系核证。
- **问题6：** "检查点非必需"是否只是flow-cell低DNA浓度的体系伪影？本文能答到什么程度：能就地作答——ensemble（高DNA、检查点激活）中PRIMPOL仍重启且ATRi进一步增强（ED7b,c），与flow-cell无检查点仍重启（ED7a）互证；阈值~1 ng/µl引用ref 58。证据强度初判：中强（本文体系内）。交接：纯本文可答，已就地作答。

以上问题中，纯本文可答的已全部就地作答，其余转入同源《背景解读》做跨文献证据综合与分级。

**（四）延伸文献与图引清单：**

以下清单服务于读完本文后的继续讲解/研究与PPT摘图：A类=本文论证直接依赖的前人工作，B类=方法学/技术来源。★为必读；图号已对EuropePMC OA全文核实（括注PMC号），核不到者标"编号待核"、不编造。深度作者谱系与跨文献证据分级见同源《背景解读》，本清单侧重"哪篇哪图值得摘/讲"，与其阅读顺序互补。

**A. 本文论证直接依赖的前人工作**

| 序号 | 文献(年/刊/本文ref) | 对应本文Fig/论点 | 重点前人Fig(panel) | 一句话讲点 | 获取/阅读深度 |
| --- | --- | --- | --- | --- | --- |
| A1 ★ | Mourón et al. 2013 Nat. Struct. Mol. Biol.（ref 1） | Introduction repriming立论；Fig. 3h,i fibre重启assay方法来源 | repriming发现与DNA fibre重启assay图（编号待核） | 停滞叉可由PrimPol在损伤下游"重新引发"——repriming通路的奠基观察 | 需订阅；精读摘要与fibre方法段，图号待核 |
| A2 ★ | García-Gómez et al. 2013 Mol. Cell（ref 2） | Introduction前导链repriming假说；Fig. 2a/4d前导链归属的论证对象 | Fig. 7（替代功能模型，含repriming/前导链假说）、Fig. 5（与Pol ε功能协同） | PrimPol是"古老"引物酶-聚合酶，前导链重新引发假说在发现之初即被提出 | OA（PMC3899013）；精读Fig. 7模型与讨论 |
| A3 | Bianchi et al. 2013 Mol. Cell（ref 3） | repriming生理底物背景（UV光产物）；与本文损伤底物正交 | Fig. 2（UV耐受、Pol η非依赖）、Fig. 3（UV损伤模板上叉前进，DT40 KO） | PrimPol为UV光产物耐受所需，且该通路独立于Pol η | OA（PMC4228047）；只读结论 |
| A4 | Wan et al. 2013 EMBO Rep.（ref 4） | PRIMPOL维护基因组完整性的功能背景 | 损伤敏感/基因组完整性图（编号待核） | hPrimpol1/CCDC111是维护基因组完整性所需的引物酶-聚合酶 | OA刊但EuropePMC全文不可得；读摘要，图号待核 |
| A5 ★ | Guilliam et al. 2017 Nat. Commun.（ref 30） | RPA募集/高RPA抑制矛盾一方；Fig. 2/5双锚定的概念前作 | Fig. 1（RBM结合RPA70N）、Fig. 5（RBM-A为重启所需）、Fig. 6（RPA在体内募集PrimPol到停滞叉）、Fig. 7（模型） | RPA经RBM把PrimPol募集到停滞叉——但完全包被的ssDNA反而抑制它 | OA（PMC5457501）；精读Fig. 1/5/6 |
| A6 | Martínez-Jiménez et al. 2017 Sci. Rep.（ref 31） | 矛盾另一方（RPA刺激+Pol ε协同）；Fig. 5模型调和对象 | Fig. 4（RPA刺激引物酶+聚合酶、与Pol ε协同）、Fig. 5（模型） | RPA增强PrimPol活性并与Pol ε协同——与ref 30直接冲突 | OA（PMC5429719）；读Fig. 4与讨论 |
| A7 ★ | Mehta et al. 2022 Sci. Adv.（ref 22） | CHK1–S255调控来源；Fig. 4e,f/ED7作用域重划对象 | Fig. 5（CHK1磷酸化S255）、Fig. 7（S255磷酸化为repriming所需）、Fig. 9（含S255无序区自抑制） | CHK1磷酸化PRIMPOL S255解除自抑制、促进repriming——本文把该效应重新定位到次模式 | OA（PMC8967226）；精读Fig. 5/7/9 |
| A8 ★ | Sparks et al. 2019 Cell（ref 25） | Fig. 1g,i损伤底物（DPC/肽加合物）与KERMIT雏形的方法来源；CMG绕过论点 | CMG绕过DPC的单分子kymograph与重启定量图（编号待核） | CMG能绕过前导链DPC——小加合物穿中央通道、不堵解旋酶而只停滞Pol ε | 需订阅（PMC6475077作者稿，全文不可得）；精读摘要与方法，图号待核 |
| A9 ★ | Polo Rivera et al. 2026 Nature（ref 60，companion） | Fig. 3a界面/Fig. 5模型的并行互证；cryo-EM结构细节来源 | Fig. 4a–d（CMG–PRIMPOL cryo-EM；4d DNA路径=5L2X+7PFO叠合模型） | 纯化人蛋白重建+cryo-EM独立验证双锚定界面——但DNA路径仍为模型 | OA（companion PDF在同文件夹）；精读Fig. 4 |

**B. 方法学/技术来源文献**

| 序号 | 文献(年/刊/本文ref) | 对应本文Fig/论点 | 重点前人Fig(panel) | 一句话讲点 | 获取/阅读深度 |
| --- | --- | --- | --- | --- | --- |
| B1 ★ | Terui et al. 2024 Cell（ref 71） | Fig. 2事件检测（GLRT）与双向起始分析的方法来源 | GLRT事件检测与双向起始分析图（编号待核） | GLRT把单分子结合事件从噪声中分辨出来——本文停留时长统计的算法地基 | 需订阅（PMC11283366全文不可得）；精读方法，图号待核 |
| B2 ★ | Lynch, Park & Chistol 2026 Cell（ref 66） | Fig. 4d回补所用Pol δ/ε蛋白来源；后随链distributive合成与速度差讨论背景 | 后随链distributive合成的单分子图（编号待核） | 后生动物后随链合成是distributive的——为本文提供Pol δ/ε蛋白平台与速度语境 | 需订阅（PMC13742137全文不可得）；读摘要与方法，图号待核 |
| B3 ★ | Jones et al. 2021 EMBO J（ref 54） | Fig. 3a叠合的实验结构地基（PDB 7PFO） | Fig. 1（人核心replisome cryo-EM结构）、Fig. 4（Pol ε非催化模块拴系）、Fig. 5（Pol ε催化域位置） | 人replisome结构显示Pol ε如何拴系CMG——本文叠合的空间兼容性检查基准 | OA（PMC8634136）；精读Fig. 1/4/5 |
| B4 | Rechkoblit et al. 2016 Sci. Adv.（companion ref 26；本文未直接引用） | DNA路径模型的PRIMPOL–DNA取向来源（PDB 5L2X） | Fig. 1（PrimPol–模板引物–dATP三元复合物结构）、Fig. 3（活性位点裂隙无法容纳UV损伤） | PrimPol–DNA晶体结构提供DNA路径模型的取向——并解释其为何不能在损伤对面直接合成 | OA（PMC5088642）；读Fig. 1/3 |
| B5 | Berger & Chistol 2023/2024 Methods Cell Biol.（refs 34,70） | KERMIT单分子成像协议（Fig. 1a工作流程） | 协议章节（方法书，无图号） | KERMIT全流程协议：双tether DNA+两步灌流+实时TIRF | 需订阅（Elsevier方法书）；做同类实验者通读 |

---

**解读完成度声明：** 主文Fig. 1–5全部panel（共46个panel：Fig. 1 = 11[a–k]、Fig. 2 = 8[a–h]、Fig. 3 = 9[a–i]、Fig. 4 = 6[a–f]、Fig. 5 = 12[a–l]）均已按四字段模板（图片解释/横纵轴定义/颜色含义/核心结论）解读；Fig. 1j,k按正文顺序归入Section 2、Fig. 4按panel归入Section 5/6/8、Fig. 5置于模块四第1层。随PDF提供的Extended Data Fig. 1–7（共48个panel：ED1 = 9[a–i]、ED2 = 5[a–e]、ED3 = 10[a–j]、ED4 = 8[a–h]、ED5 = 3[a–c]、ED6 = 6[a–f]、ED7 = 7[a–g]）已按内容角色在对应Section整合解读（ED1/ED2a,b→Section 1；ED2c–e→Section 2；ED3→Section 3；ED4→Section 4；ED5→Section 5；ED6→Section 6；ED7a–c→Section 7、ED7d–g→Section 8），其中Section 7因无主图而对ED7a–c采用四字段模板。Supplementary Tables 1–4（IP–MS、引物、抗体、精确P值）与Supplementary Data未随本PDF提供，相关处均标注"未提供"，未予虚构。图表经150 DPI渲染逐页视觉审读并与caption交叉核对；kymograph阅读方向（横=DNA位置、纵=时间、斜率=速度）与免疫印迹/自显影阅读方向均已注明；免疫印迹与自显影为代表性图像，原文未提供灰度定量数值（co-IP Fig. 3e与ensemble Fig. 1k/3g/ED3c/ED7c定量除外），凡未提供者一律如实标注；读自图的近似值均以"约"标注。公式/算法（速度换算160 nm/pixel÷0.34 nm/bp÷0.85、GLRT 5像素滑窗、OTSU阈值、bootstrap 95% CI、KS/t检验）已在模块二与概念注释中说明，未独立设模块。本文为Nature在刊文章（Accepted 7 October 2026，2026-11-11在线发表，经EuropePMC firstPublicationDate核证；所给PDF清样首页上线日期栏为占位符，不具权威性），非预印本，DOI 10.1038/s41586-026-11276-y；所有数据与结论严格基于该PDF版本。本次升级增补：12个主题（7类核心因子+5类方法平台）的课本化背景补注已插入首次出现处（PRIMPOL/repriming、CMG、聚合酶分工、TLS对比、缺口命运、RPA、CHK1，及单分子TIRF/KERMIT、ensemble复制、co-IP、DNA fibre、cryo-EM模型）；全部panel四字段已通过'技术零基础自足性'自检，并对kymograph、累积分布、频率归一、co-IP富集、ensemble凝胶、DNA fibre与cryo-EM叠合模型等18处补足技术primer；统计显著性星号已按字面转义（加粗markup完好）；延伸文献与图引清单已附（A论证依赖9条/B方法来源5条，含9条★必读，图号经EuropePMC OA全文核实或标注'编号待核'）。