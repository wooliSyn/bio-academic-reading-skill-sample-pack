文献信息：UNC13A splice correction rescues synaptic dysfunction induced by TDP-43 loss. Matthew J. Keuss, Peter Harley, Eugeni Ryadnov, Rachel E. Jackson, Moritz Boll, Matteo Zanovello, Oscar G. Wilkins, … Juan Burrone & Pietro Fratta（共34位作者；首页脚注逐字为"These authors contributed equally: Matthew J. Keuss, Peter Harley, Eugeni Ryadnov, Rachel E. Jackson"，即前四位署名作者等贡献，通讯为 Keuss、Harley、Burrone、Fratta 四人）. Nature, DOI 10.1038/s41586-026-11256-2 (2026). 第一/通讯单位：UCL Queen Square Motor Neuron Disease Centre / Institute of Neurology（Keuss、Harley、Fratta）；King's College London（Burrone）；另含 Leibniz-FMP Berlin、Francis Crick Institute、UK DRI at UCL、Trace Neuroscience、Nucleic Acid Therapy Accelerator 等。Received 18 June 2024；Accepted 6 October 2026；所给 PDF 首页"Published online"栏为占位符"xx xx xxxx"，不具权威性，在线发表状态以期刊文章页为准（任务提供上线日期为 2026-11-11，待期刊页核证）。Open access（CC BY 4.0）。本文为 Nature 已接收在刊文章（Article），非预印本。

一句话概括：本文证明 TDP-43 核缺失不是只制造"广泛剪接噪声"，而是把人神经元推入结构完好却突触通讯崩溃的"功能性死亡"前退化状态；在数百个隐匿剪接事件中，仅 UNC13A 内含子 20 的一个隐匿外显子就是突触失效的主驱动——基因组删除该外显子或用 splice-switching ASO 单点纠错即可恢复自发/诱发释放与网络同步，为约 97% 的 ALS 与约 50% 的 TDP-43 病理型 FTD 患者提供遗传学锚定的治疗策略。

解读说明：本解读基于所给 PDF 的正文（Abstract、Introduction、Results 六个小节、Discussion）、Methods、参考文献 1–74、主文 Fig. 1–4（共 43 个 panel）、Extended Data Fig. 1–11（共 84 个 panel，随主文在同一 PDF 内，按内容角色以紧凑方式整合进对应 Section 并在完成度声明中逐图汇总）完成。Supplementary Fig. 1–10（未裁剪凝胶）与 Supplementary Table 1–7（试剂/ASO 序列/引物/抗体/软件清单）未随本 PDF 提供，一律标"未提供"，不虚构其内容；Nature Portfolio Reporting Summary 随 PDF 提供（第 38–43 页），其统计/盲法/样本量声明已纳入解读。图表视觉细节以 110–140 DPI 渲染主图与关键 ED 图页目视核对（另对 Fig. 4a,b 标尺做 300 DPI 局部放大），灰度条带强弱以原文定量 panel 为准、未自行重测灰度；凡原文未提供定量数值处如实标注。模式判定：模式 A（研究型论文）。本版另按课本化深度标准在核心因子/关键引用首次出现处增补背景补注（TDP-43 蛋白病、ALS/FTD 疾病谱系、隐匿剪接先例、UNC13A/priming、splice-switching ASO 范式，及 HaloPROTAC、NGN2 iNeuron、自突触微岛、iGluSnFR3 四平台），原文内容未删改；未列入本文 refs 的外部经典文献以 Author+年标注并注阅读深度（"确立结论级"指基于领域确立结论/摘要级知识、本次未复核全文），教科书级共识事实径行陈述。

---

一、<基础概念注释>

疾病与遗传背景

- **ALS（amyotrophic lateral sclerosis，肌萎缩侧索硬化）：** 快速进展、致死的运动神经元退行性疾病，皮层运动神经元与脊髓运动神经元相继丢失。本文的疾病落点：约 97% 患者无 SOD1/FUS 突变、但存在 TDP-43 病理，是本文治疗策略的目标人群。
- **FTD（frontotemporal dementia，额颞叶痴呆）／FTLD-TDP：** 以额颞叶萎缩为特征的痴呆谱系；约 50% 的 FTD（以及约 50% 的阿尔茨海默病）脑内存在 TDP-43 聚集病理。本文把 UNC13A 纠错策略的适用人群扩展到 TDP-43 病理型 FTD。
- **TDP-43 蛋白病（TDP-43 proteinopathy）：** 以 TDP-43 从细胞核错定位到细胞质并形成聚集为标志的病理状态；核内 TDP-43 减少即"核功能缺失"。本文用急性降解 TDP-43 模拟该核缺失，而不模拟聚集本身（作者自陈局限）。
- **GWAS（genome-wide association study，全基因组关联研究）：** 在人群水平比较 SNP 频率与疾病/表型的关联。本文的遗传学锚点：UNC13A 位点是 ALS/FTLD-TDP 第二强 GWAS 信号（refs 14–16），且风险 SNP 纯合携带者中位生存期缩短 5–12 个月（refs 15,16,33–36）。
- **风险 SNP rs12608932 / rs12973192：** 位于 UNC13A 隐匿外显子内部及附近的两个 ALS 风险单核苷酸多态性。正常生理条件下不引起隐匿外显子 inclusion；TDP-43 缺失后加剧隐匿剪接、加速功能转录本与蛋白丢失（refs 6,7）。本文所用 WTC11 iPS 系与 hUNC13A 小鼠均携带风险等位基因（杂合/人源内含子含风险碱基），故 ASO 需同时纠错参考与风险等位基因（ED Fig. 9i）。

关键分子与剪接事件

- **TDP-43（TAR DNA binding protein-43，基因名 TARDBP）：** 正常定位于核的 RNA 结合蛋白，调控剪接、稳定性与运输。本文的核心操作对象：用 HaloTag-PROTAC 或 CRISPRi/gapmer 在成熟神经元中急性去除它，制造"核功能缺失"。
- **核功能缺失（nuclear loss of function, LoF）：** TDP-43 错定位后核内功能丧失，导致隐匿外显子 inclusion、隐匿选择性多聚腺苷酸化、外显子跳跃等数百转录本异常（refs 3–8）。本文要回答的是：这些事件中哪一个真正驱动突触失效。
- **隐匿外显子（cryptic exon）：** 正常时被剪接机器跳过、仅在调控因子（此处 TDP-43）缺失时才被并入成熟 mRNA 的"隐藏"外显子；其 inclusion 常引入提前终止密码子或破坏读框，使功能转录本减少。本文特指 UNC13A 内含子 20 的隐匿外显子。
- **UNC13A 隐匿外显子（intron 20 cryptic exon，长/短两型）：** TDP-43 缺失后在 UNC13A 内含子 20 被 inclusion 的隐匿外显子，存在共用 5′ 供体位点、不同 3′ 受体位点的"长/短"两种形式；另伴内含子 31 保留等低频异常（refs 6,7）。本文的因果手术对象：233 nt 纯合删除同时去掉两个受体位点与共用供体位点。
- **隐匿选择性多聚腺苷酸化（cryptic alternative polyadenylation）：** TDP-43 缺失后在转录本内部提前加尾截短 mRNA 的事件，典型为 STMN2（refs 4,5）。本文用作"特异性对照"：删除 UNC13A 隐匿外显子不 rescue STMN2 截短（ED Fig. 5f–i），证明 rescue 是事件特异而非全局剪接恢复。
- **UNC13A / Munc13-1：** 突触前活性区蛋白，负责把突触小泡"对接并 priming（启动）"到可融合状态；小鼠 Unc13a 敲除使自发与诱发谷氨酸能传递下降约 90%（refs 18–20），null 鼠出生即死于呼吸衰竭。本文的核心效应分子：其蛋白剂量决定突触是否"沉默"。
- **突触小泡 docking/priming/活性区（active zone）：** 小泡先被拴系（docking）再经 Munc13 等蛋白 priming 获得钙触发融合能力；活性区是突触前膜上执行释放的分子机器平台。本文把 UNC13A 丢失定位到"priming 失败→释放概率下降"，而非小泡数量或 postsynaptic 受体问题。
- **PSI（percentage spliced in，剪接纳入百分比）：** 某剪接异构体条带占该位点全部异构体条带的百分比，本文用 RT–PCR 条带定量计算。读法：Correct PSI 越高=正常剪接越多；TDP-43 KD 后 Correct PSI 从约 100% 跌到约 15–40%，Short/Long cryptic PSI 上升。
- **AMPA 受体／NMDA 受体：** 介导快/慢兴奋性突触传递的谷氨酸受体。本文 mEPSC 被 CNQX 完全阻断，证明记录到的事件是 AMPA 受体介导的快谷氨酸能传递（ED Fig. 3a）；TDP-43 KD 不改变两类受体亚基 RNA 水平（ED Fig. 2g），把缺陷定位到突触前。

模型系统与遗传操作工具

- **iPS 细胞（induced pluripotent stem cell，诱导多能干细胞）／WTC11（GM25256）：** 健康人来源、可无限扩增并定向分化的干细胞系；本文用 WTC11（AAVS1 位点整合 dox 诱导 NGN2、CLYBL 位点整合 dCas9-BFP-KRAB，M. Ward 惠赠，ref 51），且该系杂合携带 UNC13A 风险 SNP。选它是因为可在人源基因组上做精确编辑并分化成成熟神经元。
- **iNeuron（NGN2 诱导神经元）：** 过表达转录因子 NGN2 快速定向分化出的兴奋性皮层样神经元；本文鉴定为 layer V 标志 CTIP2 阳性、抑制性标志 NKX2.1 阴性、祖细胞标志 PAX6 阴性（ED Fig. 1h）。是本文电生理与成像的主体系。
- **iMN（iPS 来源脊髓运动神经元）：** 经发育信号三维分化 14 天再成熟的运动神经元，表达 Islet-1 与 VAChT；本身释放乙酰胆碱且无 postsynaptic 烟碱受体、彼此不形成突触连接，故本文外源表达 VGlut1-EGFP 使其获得谷氨酸释放能力后再记录（Methods，refs 7,55,56）。作为第二细胞类型、第二实验室（FMP Berlin）的独立验证。
- **HaloTag／HaloPROTAC-E／PROTAC（proteolysis targeting chimera，蛋白降解靶向嵌合体）：** HaloTag 是共价结合氯代烷配体的工程蛋白标签；HaloPROTAC 一端结合 HaloTag、一端招募 E3 泛素连接酶，把目标蛋白送进蛋白酶体降解（ref 21）。本文用 CRISPR–Cas12 把 HaloTag 敲入内源 TARDBP  exon 2 起始处，成熟神经元加 30 nM HaloPROTAC-E 即急性降解 TDP-43，避开从干细胞期敲除造成的发育混杂；降解可被蛋白酶体抑制剂 MG132 与 NEDD8 E1 抑制剂 MLN4924 阻断（ED Fig. 1e–g）。
- **CRISPRi（CRISPR interference，CRISPR 干扰）：** dCas9-KRAB 融合蛋白被 sgRNA 带到启动子区抑制转录，实现基因敲低而不切割 DNA。本文用作 TDP-43 与 UNC13A 敲低的独立手段（sgTARDBP、sgUNC13A、sgCTRL），与 HaloPROTAC 结果互证（ED Fig. 2b–f, h）。
- **CRISPR–Cas9/Cas12 编辑与 HDR bridging oligo：** Cas9/Cas12 核酸酶在 sgRNA/crRNA 指引下切割基因组，靠同源定向修复（HDR）模板引入精确改变。本文 Cas12 用于 HaloTag 敲入；Cas9 双 sgRNA + 含简并碱基 B/D 的 bridging oligo 模板用于 233 nt 隐匿外显子纯合删除；编辑后均做 amplicon 测序、低深度全基因组测序（CNVkit/Manhattan 图）与 off-target PCR 验证（ED Fig. 1a–d, 4a–b, 5a–e, 6）。
- **SH-SY5Y / SK-N-BE(2)（shTARDBP 稳定系）：** 人神经母细胞瘤系，整合 dox 诱导 shRNA 靶向 TARDBP（来自 ref 6 体系）。本文用作 ASO 高通量筛选平台（转染 ASO 后 RT–PCR 读剪接），因其易转染、可快速读 PSI；神经元验证再回到 HaloTDP iNeurons。
- **自突触微岛培养（autaptic micro-island culture）：** 把单个神经元种在直径约 250 µm 的胶质细胞微岛上，使其轴突回连自身形成"自突触"（refs 26,27）。价值：一个细胞即一个完整突触回路，诱发 eEPSC 时突触前/后为同一细胞，便于分离释放变量；本文 UCL 与 FMP 两实验室分别用其记录 iNeuron 与 iMN 的诱发释放。
- **大鼠星形胶质细胞共培养：** E18 Wistar 大鼠皮层来源的原代星形胶质细胞铺底，支持人神经元成熟与突触形成。本文电生理、成像、MEA 均在此共培养体系上进行，是"人神经元+鼠胶质"的标准化成熟平台。
- **hUNC13A reporter 小鼠：** 用 817 bp/1462 bp 同源臂把小鼠 Unc13a 内含子 20 替换为含风险 SNP（rs12973192 G、rs12608932 C）的人源内含子 20 的人源化小鼠；因小鼠本底不产生该人特异隐匿剪接，只有人源化后才能在小鼠体内复现并测试 ASO。注意：实际所用系为"异常靶向系"——同源重组伴随载体串联重复、部分骨架落入内含子 23，但人源内含子位置与剪接正确（Methods 自陈）。
- **AAV PHP.eB／合成 microRNA／ICV／ACSF：** PHP.eB 是跨血脑屏障能力强的 AAV 衣壳；本文尾静脉注射 1.4×10^12 vg 表达靶向小鼠 Tardbp 的合成 microRNA 实现体内 TDP-43 敲低；同日脑室（ICV）注射 ASO（30 mg/ml、10 µl、Mg2+:ASO=3:1）或人工脑脊液（ACSF）对照；3 周后取脊髓读剪接。

电生理与网络功能读出

- **全细胞膜片钳（whole-cell patch clamp）／电压钳：** 玻璃微电极吸破细胞膜形成全细胞通路，钳制膜电位（本文 −70 mV）并记录跨膜电流；电流向下的小尖峰即兴奋性突触后电流。物理量是皮安（pA）级离子流，反映突触受体开放程度。
- **mEPSC（miniature excitatory postsynaptic current，微小兴奋性突触后电流）：** 在 TTX（阻断动作电位）+ gabazine（阻断 GABA_A）条件下记录到的单小泡自发融合事件。频率反映"突触前释放速率×功能突触数"，幅度反映 postsynaptic 受体对单量子谷氨酸的反应；因此频率降=突触前缺陷、幅度降=postsynaptic 缺陷。本文核心功能读出。
- **eEPSC（evoked EPSC，诱发兴奋性突触后电流）：** 给突触前一个动作电位刺激所引发的同步多小泡释放电流（nA 级），代表生理回路工作模式；幅度取决于释放概率 Pr、量子幅度与突触数三者。本文在自突触上以 80 mV/1 ms（UCL）或 −70→0 mV/1 ms（FMP）刺激诱发。
- **释放概率（release probability, Pr）／量子（quantal）：** 单个动作电位到达时一个突触释放小泡的概率；单量子=一个小泡的内容物。本文用 iGluSnFR3 活细胞成像在单突触水平直接数"45 次刺激中几次有释放"来算 Pr，把 eEPSC 幅度下降分解为 Pr 与突触数两个成分。
- **CNQX／NBQX／AP-V／gabazine／TTX：** 分别为 AMPA 受体阻断剂（CNQX/NBQX）、NMDA 受体阻断剂（AP-V）、GABA_A 阻断剂（gabazine）、钠通道/动作电位阻断剂（TTX）。本文用 CNQX 证明 mEPSC 与网络同步依赖快 AMPA 传递（ED Fig. 3a,f）；用 NBQX+AP-V+gabazine 阻断回返活动以隔离单突触 Pr 成像。
- **MEA（multi-electrode array，多电极阵列）／网络同步性（network synchrony）：** 培养皿底嵌 96 孔×多电极，细胞外记录群体放电；本文同步性=电极间归一化互相关（20 ms 同步窗）的曲线下面积，衡量"全网络是否一起爆发"。读法：同步性高=网络协同放电；TDP-43/UNC13A 缺失后电极仍放电但彼此失协（异步）。
- **raster plot／电极爆发／网络爆发：** raster 图每行一个电极、每个竖 tick 一次 spike；蓝色=单电极 burst（≥5 spike、间隔≤100 ms），粉色=网络 burst（≥35% 电极参与）。CTRL 呈整齐粉色竖列（同步爆发），KD 呈散乱点（异步）。
- **iGluSnFR3／ΔF/F0：** 基因编码的膜锚定谷氨酸荧光探针（ref 28），结合谷氨酸后荧光增强；ΔF/F0=荧光相对基线的变化分数，正比于局部谷氨酸释放量。本文以 100 Hz 成像、场刺激 1 Hz×45 次，按像素聚类出单突触 ROI 并计算 Pr；成像者对处理组盲法。
- **Synapsin1／Homer1：** 突触前小泡结合蛋白与 postsynaptic 支架蛋白，免疫荧光共定位定义"一个兴奋性突触"。本文用二者共定位计数树突上突触密度（tdTomato 标记树突），证明 TDP-43 KD 减少突触数且该减少不被 UNC13A 纠错 rescue（ED Fig. 7c,d, 11b）。
- **CTIP2／NKX2.1／PAX6／Islet-1／VAChT／MAP2／NeuN：** 分别为皮层深层兴奋性、抑制性、神经祖细胞、运动神经元、胆碱能突触、神经元树突、成熟神经元核的标志物。本文用于鉴定 iNeuron 与 iMN 身份及存活计数（NeuN/DAPI）。

分子检测、ASO 化学与统计

- **RT–PCR／TapeStation／QIAxcel：** 先逆转录 RNA 为 cDNA，再跨外显子 19–22 扩增 UNC13A 剪接区；产物按长度在毛细管电泳/凝胶上分离成条带（Correct 约 300 bp、Short/Long cryptic 更大），条带亮度/面积正比于该异构体量。本文剪接表型的核心读法；未裁剪凝胶见 Supplementary Fig. 1–10（未提供）。
- **RT–qPCR／ΔΔCt：** 实时荧光定量 PCR，用 Ct 值差（ΔΔCt）算相对表达；本文用 exon 20–21  junction 特异 assay 只量"正确剪接"的 UNC13A mRNA，以及 TDP-43、STMN2、受体亚基等。
- **Western blot（免疫印迹）／上样对照：** 蛋白按分子量电泳分离、转膜、抗体识别、化学发光成像；条带越深=该蛋白越多。本文以 Tubulin（UCL）或 Vinculin/总蛋白染色（FMP）作上样对照归一化；UNC13A 条带约 185 kDa（ED Fig. 10j 标注）、TDP-43 约 50–70 kDa。
- **免疫荧光／Airyscan 共聚焦：** 抗体偶联荧光染料标记目标蛋白，共聚焦显微镜逐层成像；本文 Zeiss 980 Airyscan ×63 拍突触 z-stack（7×0.5 µm），在 synapsin 阳性 ROI 内量 UNC13A 荧光强度（选 ROI 时对 UNC13A 通道盲法）。
- **ASO（antisense oligonucleotide，反义寡核苷酸）／splice-switching：** 短合成核酸，靠碱基互补结合目标 RNA；splice-switching ASO 不降解 RNA，而是空间占位剪接位点/调控元件，把剪接"扳"回正常异构体。本文治疗工具：占位 UNC13A 隐匿外显子 5′ 供体位点，阻止其 inclusion。
- **LNA（locked nucleic acid，锁核酸）／MOE（2′-O-methoxyethyl，2′-O-甲氧乙基）／gapmer：** LNA 与 MOE 是核糖 2′ 位化学修饰，提高亲和力/核酸酶稳定性；MOE 全修饰耐受性更好。gapmer 是"两翼 MOE+中间 DNA"的 RNase H 降解型 ASO（本文 FMP 用其敲低 TDP-43，与 splice-switching 机制不同）。本文先筛 LNA 21-nt，再转 MOE 21-nt（M21-4/5），再做 18-nt MOE walk（M18 系列）。
- **ASO walk／M21-4、M21-5、M21-6、M18-17：** 沿目标位点逐核苷酸平移设计一组 ASO 以找最优结合窗（walk）。M21-4/M21-5 为 21-nt MOE 领先化合物（蛋白 rescue 30–50%）；M18-17 为 18-nt MOE 领先化合物（蛋白 rescue >50%）；M21-6 为 FMP 在 iMN 所用 21-nt MOE 化合物。神经元内以 1 µM 自由摄取给药（MEA 为 0.5 µM、每两周一次）。
- **amplicon 测序／Minimap2／IGV：** 对 PCR 产物做长读长测序（Plasmidsaurus），Minimap2（-x splice）比对、SAMtools 转 BAM、IGV 可视化；本文用于验证编辑精确性、off-target 无编辑、以及 ASO 对参考/风险两等位基因的特异性 rescue（ED Fig. 9i）。
- **低深度全基因组测序／CNVkit／Manhattan 图：** 约 10× 覆盖度 WGS，bwa-mem2 比对 GRCh38、CNVkit 20-kb bin 做拷贝数分析；Manhattan 图按染色体位置画拷贝数/信号，用于确认编辑系无大染色体 rearrangement（ED Fig. 1b, 5c, 6c）。
- **LMM（linear mixed-effects model，线性混合效应模型）／Satterthwaite／配对比率 t 检验／重复测量 ANOVA：** 本文合并多批次电生理/成像数据用 log1p 转换后的高斯 LMM，批次作随机截距（ICC 0–0.4451），P 值经 Satterthwaite 自由度校正；残差偏离正态（Shapiro–Wilk W<0.90）时用 Gamma GLMM 复核结论一致。MEA 用原始 AUC 的配对比率 t 检验；Western 用 log 转换、上样归一化后的重复测量 ANOVA+Tukey（Geisser–Greenhouse 校正）。

---

二、<核心问题与方案>

**生物学问题（原文表述）：**

- "However, no therapies that directly target TDP-43 are available, leaving the underlying nuclear loss of function (LoF) unaddressed."（Introduction 第 1 段末）——然而尚无直接靶向 TDP-43 的疗法，其核功能缺失这一根本问题未被处理。
- "Whereas the impact of STMN2 mis-splicing on axonal regeneration and KCNQ2 exon skipping on intrinsic excitability has been studied, the direct impact of TDP-43 LoF on synaptic function has not been addressed."（Introduction 第 1 段末）——STMN2 错剪接对轴突再生、KCNQ2 外显子跳跃对内在兴奋性的影响已被研究，但 TDP-43 核缺失对突触功能的直接影响未被回答。
- "Although the UNC13A genetic association strongly implicates this event in ALS pathogenesis, the contribution of TDP-43 LoF to synaptic dysfunction and the role of UNC13A cryptic splicing—particularly in the context of many mis-splicing events in other synaptic transcripts—is unaddressed."（Introduction 第 2 段）——尽管 UNC13A 遗传关联强烈提示该事件参与 ALS 发病，但在其他突触转录本众多错剪接事件的背景下，TDP-43 核缺失对突触功能障碍的贡献、以及 UNC13A 隐匿剪接的角色，仍未被回答。
- "Resolving these outstanding questions is crucial for establishing whether correcting UNC13A splicing represents a viable therapeutic approach for restoring normal neuronal function."（Introduction 第 2 段末）——回答这些问题是确立"纠正 UNC13A 剪接能否作为恢复神经元功能的治疗路径"的关键。

**背景补注：TDP-43 与 TDP-43 蛋白病——为什么整个领域要"治疗"这个蛋白**

上文 Introduction 第 1 段末"no therapies that directly target TDP-43"之所以构成一个临床缺口，须先把 TDP-43 放回疾病语境讲透。

**①它是什么、为什么重要。** TDP-43（TAR DNA binding protein-43，基因名 TARDBP）是广泛表达的 RNA 结合蛋白。它成为治疗靶点，是因为其病理聚集是 ALS 与额颞叶变性最常见的分子病变：除 SOD1/FUS 突变型（合计不足 3%）外，约 97% 的 ALS 患者神经元内存在 TDP-43 聚集；约 50% 的 FTD 与约 50% 的阿尔茨海默病脑内同样存在该病理（本文 Introduction，refs 1,2,11）。换言之，"治疗 TDP-43"不是治疗一个罕见突变基因，而是治疗绝大多数 ALS/FTD 共享的病理枢纽——这正是本文立论的疾病分量。

**②蛋白性质。** TDP-43 约 43 kDa（故名），全长 414 个氨基酸；结构域排布为 N 端核定位信号（NLS，维持正常核内分布）、串联 RNA 识别基序 RRM1/RRM2（识别 UG 富集 RNA motif）、C 端甘氨酸富集低复杂度域（介导蛋白互作与相分离，也是聚集倾向与多数 TARDBP 病理突变所在）（结构域排布为教科书级共识；功能综述见 refs 12,13）。生理下 TDP-43 主要定位于核，调控前体 mRNA 剪接（尤其抑制隐匿外显子）、mRNA 稳定性与轴突运输，并参与应激颗粒动态（refs 3,12,13）。

**③缺失或异常的后果。** TDP-43 蛋白病的标志病理是"核清除＋胞质聚集"：核内 TDP-43 耗竭，胞质出现泛素化、超磷酸化（如 S409/410，教科书级病理共识）的不溶性包涵体（Neumann et al., Science 2006，ref 1）。核清除即核功能缺失（nuclear LoF），在数百个转录本上造成隐匿外显子 inclusion、隐匿选择性多聚腺苷酸化与外显子跳跃（refs 3–8），受累者包括 STMN2（轴突再生）、UNC13A（突触释放）、KCNQ2（内在兴奋性）等关键神经元基因；胞质聚集是否另具毒性功能获得仍是争论点，本文未建模聚集本身（作者自陈局限）。

**④前人如何研究它。** 2006 年 Neumann 等（Science，ref 1）与 Arai 等（Biochem Biophys Res Commun 2006；外部文献，阅读深度：确立结论级，本次未复核全文）分别以患者脑不溶性组分的生化纯化＋质谱鉴定，独立证明 FTLD-U/ALS 泛素化包涵体的主要成分是 TDP-43，确立"TDP-43 蛋白病"概念；2008 年 Sreedharan 等（Science）与 Kabashi 等（Nat Genet）（均为外部文献，阅读深度：确立结论级）在家族性 ALS 中发现 TARDBP 突变，把 TDP-43 从病理旁观者升级为致病因子。机制层面：Polymenidou 等（Nat Neurosci 2011，ref 12）以小鼠神经元 TDP-43 敲低＋全转录组剪接分析确立"核 LoF→广泛错剪接"；Ling 等（Science 2015，ref 3）证明 TDP-43 正常抑制非保守隐匿外显子、该抑制在 ALS-FTD 患者脑失效；Klim/Melamed 等（Nat Neurosci 2019，refs 4,5）确立 STMN2 隐匿多聚腺苷酸化；Brown/Ma 等（Nature 2022，refs 6,7）确立 UNC13A 隐匿外显子与风险 SNP 加剧效应（详见下文隐匿剪接补注）。人神经元层面，携带 TARDBP 或 C9ORF72 突变的 iPS 来源运动神经元已显示兴奋性与突触缺陷（refs 37–39），但未确立隐匿外显子 inclusion 或 UNC13A 蛋白改变的机制角色（Discussion 原文）。遗留缺口有二：聚集的上游触发事件未知，"直接纠正错定位/聚集"无从下手；数百个错剪接事件中谁主导突触失效未被回答。

**⑤与本文的关系。** "直接靶向 TDP-43"之难，在于聚集毒性与核 LoF 双重机制叠加、聚集触发机制未知（Discussion 原文："The cellular events that lead to TDP-43 aggregation in ALS are unknown"），且 TDP-43 作为 RNA 结合蛋白缺乏经典酶学活性口袋、C 端低复杂度域本身易聚集，成药性差。本文的治疗逻辑因此是"绕过枢纽、直纠执行者"：不恢复 TDP-43 本身，而以基因组删除或 splice-switching ASO 纠正其下游功能权重最大的单个剪接事件（UNC13A 内含子 20 隐匿外显子）。模型上用成熟神经元急性降解只模拟核 LoF、不模拟聚集——既是因果干净性的来源，也是作者自陈的保真度边界。

**背景补注：ALS/FTD 疾病谱系与未满足的临床需求**

**疾病是什么。** ALS（肌萎缩侧索硬化）是皮层上运动神经元与脊髓/脑干下运动神经元相继退行的致死性疾病，表现为进行性肌无力、肌萎缩，多最终因呼吸衰竭死亡，自发病起中位生存期约 3–5 年（外部教科书级事实，阅读深度：确立结论级；本文 Introduction 仅表述为"rapidly progressive and fatal"）。FTD（额颞叶痴呆）是以额颞叶萎缩为特征的痴呆谱系，主要亚型为行为变异型（bvFTD）与原发性进行性失语（PPA）（亚型划分为教科书级共识），其病理半数属 FTLD-TDP。ALS 与 FTD 在临床、遗传与病理上构成连续谱系：共享 TDP-43 蛋白病机制与部分致病基因（如 C9ORF72 重复扩增——ALS/FTD 最常见的遗传病因，外部确立结论级；本文 ref 37 即涉及 C9ORF72 突变患者神经元）。

**遗传学与治疗现状。** 单基因型（SOD1、FUS 突变）合计不足 ALS 患者的 3%；靶向 SOD1 的 tofersen（Miller et al., NEJM 2022，ref 9）与靶向 FUS 的 ASO（ref 10）已在临床试验显示早期希望，但只覆盖突变携带者，其余约 97% 患者无对因疗法（Introduction 原文）。人群遗传学为广谱策略提供锚点：GWAS 把 UNC13A 内含子 20 隐匿外显子内/附近的 SNP 定位为 ALS 与 FTLD-TDP 的第二强关联信号（van Es 2009 首报，ref 14；van Rheenen 2021，ref 16；FTLD-TDP 侧 refs 30–32），且风险 SNP（rs12608932/rs12973192）纯合携带者中位生存期缩短 5–12 个月（refs 15,16,33–36；FTD 生存修饰见 ref 32）——该位点不仅关联发病风险，还修饰疾病进程。

**与本文的关系。** 本文目标人群正是这约 97% 的 ALS 与约 50% 的 TDP-43 病理型 FTD；其治疗主张不是纯机制推演，而是"GWAS 关联＋生存修饰＋单事件因果＋可给药分子"四重锚定。理解这一点，才能理解作者为何反复强调 UNC13A 是"genetically validated"靶点。

**背景矛盾（研究切入点）：** 矛盾双方是：(A) TDP-43 核缺失在数百个转录本上制造隐匿剪接/提前加尾/外显子跳跃，其中不少是突触基因，直觉上突触失效应是"多基因联合打击"；(B) 人群遗传学却把第二强 ALS/FTD 信号精确指向 UNC13A 内含子 20 的一个隐匿外显子，且风险 SNP 只在 TDP-43 缺失后才加剧其 inclusion——暗示单事件可能有超比例权重。两侧都成立但互不衔接：关联不等于因果，广泛错剪接也不等于每个事件都重要。本文的切入点是绕过"必须纠正全部剪接才能恢复功能"的隐含假设，用两把刀直接检验单事件的充分性：一把是基因组刀（纯合删除 233 nt 隐匿外显子，在 TDP-43 仍缺失的背景下问"只修这一个事件够不够"），一把是化学刀（splice-switching ASO 占位隐匿供体位点，问"不改动基因组、只给药能否复现基因组刀的 rescue"）。再叠加"急性降解成熟神经元 TDP-43"的时间控制，把发育混杂与退化性死亡排除在表型之外。

**背景补注：隐匿剪接（cryptic splicing）——概念、机制与 STMN2/UNC13A 先例**

**概念。** 隐匿外显子（cryptic exon）是内含子中一段平时被剪接调控因子主动抑制、因而不并入成熟 mRNA 的序列；只有当抑制因子（此处为核 TDP-43）缺失时，剪接机器才把它当作外显子 inclusion。后果通常是灾难性的：引入提前终止密码子或破坏读框，转录本被无义介导的衰变（NMD）清除或产生截短蛋白，功能转录本与蛋白随之耗竭（NMD 为教科书级机制；本文 Introduction 表述为"increased loss of functional RNA transcripts and protein"）。另一类是隐匿选择性多聚腺苷酸化（cryptic APA）：在内含子内部提前切割加尾产生截短 mRNA，典型为 STMN2。TDP-43 的抑制机制是经 RRM 结合隐匿剪接位点附近的 UG 富集 motif 阻遏 inclusion（refs 3,12；Ma et al. 2022 证明其直接结合 UNC13A 内含子 20，ref 7）。

**先例时间线（前人如何研究）。** Ling 等（Science 2015，ref 3）首次系统证明 TDP-43 抑制非保守隐匿外显子、该抑制在 ALS-FTD 患者脑失效；Klim 等与 Melamed 等（Nat Neurosci 2019，refs 4,5）以 iPS 来源运动神经元与患者组织确立 STMN2 隐匿 APA→stathmin-2 蛋白丢失→轴突再生受损；Joseph 等（Nat Neurosci 2025，ref 8）确立 KCNQ2 外显子跳跃→内在超兴奋。UNC13A 侧：Brown 等与 Ma 等（Nature 2022 双篇，refs 6,7）独立确立内含子 20 隐匿外显子（长/短两型，共用 5′ 供体、不同 3′ 受体），并证明 ALS 风险 SNP 正常条件下不触发 inclusion、只在 TDP-43 缺失后加剧 inclusion 与转录本/蛋白耗竭——把 2009 年以来的 GWAS 关联（ref 14）落到具体 RNA 机制。患者证据：FANS 分选死后皮层核的转录组显示，缺核 TDP-43 的细胞群中 >90% 的 UNC13A 转录本含隐匿外显子（refs 6,41；Discussion）。

**遗留缺口与本文关系。** 上述工作确立了"数百个错剪接事件"的图谱与个别事件的分子机制，但止于相关性或单基因分子表型：在突触功能层面哪个事件占主权重、单事件纠正是否足以恢复功能，从未被因果检验。本文的 233 nt 纯合删除正是把 UNC13A 这一个变量从数百个事件中单独摘除的因果刀，并以 STMN2 不被 rescue 作事件特异性内对照（ED Fig. 5f–i）——把隐匿剪接研究从"图谱相关"推进到"单事件因果权重排序"。

**解决方案（技术路线）：**

- **模型系统：** 主体系为 HaloTag-TDP-43 WTC11 iPS 分化的成熟兴奋性皮层样 iNeurons（CTIP2+、NKX2.1−、PAX6−，大鼠星形胶质细胞共培养）；第二体系为 FMP Berlin 的 iPS 来源脊髓运动神经元（Islet-1+/VAChT+，外源 VGlut1-EGFP 赋予谷氨酸释放）；筛选体系为 shTARDBP SH-SY5Y 与 SK-N-BE(2)；体内体系为 hUNC13A reporter 小鼠（人源内含子 20 含风险 SNP）。选这些体系是因为：人源基因组保留人特异隐匿剪接与风险等位基因、成熟神经元避开发育期 TDP-43 必需性、两细胞类型覆盖 ALS/FTD 受累神经元、小鼠提供体内剪接药效学。
- **实验设计：** (1) TDP-43 急性缺失：DIV14 起 30 nM HaloPROTAC-E（早期 KD）或 DIV33 起（晚期 KD，网络已成熟），蛋白时间 course 1/2/4/7/10 天；平行 CRISPRi（sgTARDBP）与 FMP gapmer（DIV45，2–4 µM、每周一次×3 周）互证。(2) 因果删除：Cas9 双 sgRNA+bridging oligo 在 SH-SY5Y 与 WTC11 做 233 nt 纯合删除（CE DEL），再在 CE DEL 系上 Cas12 敲入 HaloTag，实现"TDP-43 缺失+单事件已修"的组合。(3) ASO 筛选三级：LNA 21-nt 覆盖隐匿受体/供体位点→SK-N-BE(2) 转染筛→MOE 21-nt（M21-4/5）在 HaloTDP iNeurons 1 µM 自由摄取验证→18-nt MOE walk（合成 24 条、按 off-target 与二级结构筛选后测试）在 SH-SY5Y 10/50 nM 筛→领先化合物回 iNeurons/iMN。(4) 体内：8 周龄 hUNC13A 小鼠尾静脉 AAV PHP.eB-miR-Tardbp 1.4×10^12 vg + 同日 ICV M21-4（30 mg/ml、10 µl）或 ACSF，3 周后脊髓 RT–PCR/RT–qPCR；n：WT NT 4、WT KD 3、hUNC13A NT 5、ACSF 7、ASO 9（ASO 组 6 雌 3 雄、ACSF 组 5 雌 2 雄）。(5) 功能读出分层：mEPSC（4 周成熟）、自突触 eEPSC（UCL 10 周 / FMP DIV60–70）、iGluSnFR3 单突触 Pr（5–6 周、45 次 1 Hz 场刺激、盲法）、MEA 纵向网络同步（DIV14/33 起 KD，0.5 µM ASO 每两周）。(6) 对照与混杂排除：scrambled ASO、ACSF、NT、CE DEL 单独组、CNQX 阻断、被动膜特性、突触密度（Synapsin1/Homer1）、存活（Incucyte+NeuN/DAPI）、电极覆盖（phase-contrast）、off-target 与拷贝数验证。
- **功能验证：** 确立必要性——CRISPRi 直接敲低 UNC13A 复现 TDP-43 KD 的 mEPSC 频率下降与网络失协（Fig. 1i,k,l），说明 UNC13A 丢失本身足以致表型；确立充分性——CE DEL 在 TDP-43 仍缺失时 rescue 约 80% mEPSC 频率与网络同步（Fig. 2i–l），ASO 复现之（Fig. 4）；区分竞争解释——CE DEL 不 rescue STMN2 提前加尾（ED Fig. 5f–i）、不 rescue mEPSC 幅度残余下降与突触密度下降（ED Fig. 7a,c,d）、不 rescue 活性突触数（ED Fig. 11a），从而把 rescue 限定为"UNC13A 特异的突触前释放功能"，而非全局剪接恢复或结构恢复。
- **机制解析：** 从"核 TDP-43 消失"到"UNC13A 隐匿外显子 inclusion（PSI 翻转）"到"正确剪接 mRNA 丢失"到"UNC13A 蛋白 10 天降至 <5%"到"突触前 UNC13A puncta 消失"到"单小泡自发释放频率下降、诱发 eEPSC 下降、单突触 Pr 下降"到"网络同步崩溃"；再反向用单外显子删除/ASO 逐层回补，形成闭环因果链。

**验证层级：** 急性核缺失表型（Fig. 1a–h；ED Fig. 1–2）→ 突触与网络功能失效（Fig. 1i–m；ED Fig. 3）→ 单事件因果充分性（Fig. 2a–h；ED Fig. 4–6）→ 功能 rescue 与特异性边界（Fig. 2i–l；ED Fig. 7）→ 可给药单点纠错（Fig. 3a–f；ED Fig. 8–9）→ 体内人源化剪接药效（Fig. 3g–k）→ 跨细胞类型/跨实验室功能 rescue 与单突触机制（Fig. 4；ED Fig. 10–11）。

**统计与生信框架（Methods 要点）：** 合并批次电生理/成像数据：log1p 转换+高斯 LMM（lme4/lmerTest，R 4.4.1），实验批次为随机截距（ICC 0–0.4451，似然比检验确认），Satterthwaite 校正 t 检验；预设比较以 TDP-43 KD 为参考基线，非预设比较用 Tukey；残差 Shapiro–Wilk W 0.85–0.99，W<0.90 者以 Gamma GLMM（glmmTMB）复核一致。Western：log10 转换、上样对照归一化后重复测量单因素 ANOVA+Tukey（Geisser–Greenhouse）。MEA：原始数据 AUC 的两侧配对比率 t 检验（图中 log2[FC] 仅作展示）。RT–qPCR：ΔΔCt（ref 61）。剪接条带：TapeStation 4200 v3.2 / QIAxcel（QIAxcelR v0.1）。测序：amplicon 长读长（Plasmidsaurus）→Minimap2 v2.26（-x splice）→SAMtools v1.21→IGV；SNP 定量用自定义 Python；低深度 WGS 约 10×→fastp v0.23.4→bwa-mem2 v2.2.1（GRCh38）→CNVkit v0.9.12（20-kb bin、--drop-low-coverage、CBS 分段）。off-target：Cas-OFFinder（LB Cas12、PAM TTTV、bulge 1、mismatch 3）+ IDT gRNA checker。**原文未提供 GEO/公共测序 accession**——Reporting Summary 明确"No Omics datasets were generated or used in this study"，原始数据以 source data 随文提供；代码四个 GitHub 仓库（见重点思考第 7 问）。

---

三、<逐节精读>

本节按原文 Results 六个小标题逐一展开：每节先给完整"内容逻辑"叙事（设计理由、竞争解释、定量数据、前后衔接），随后以"→ Figure X"嵌入该节关联主图 panel 的四字段解读；Extended Data 图按其内容角色在对应 panel 或节末以紧凑括注整合，未裁剪凝胶（Supplementary Fig. 1–10）未随 PDF 提供、仅按 caption 指引注明。

Section 1：Loss of TDP-43 depletes synaptic UNC13A（TDP-43 丢失耗竭突触 UNC13A）

**背景补注（方法平台）：为什么用 HaloPROTAC 急性降解，而不是从干细胞期敲除**

TDP-43 对发育必需（Results 原文："TDP-43 plays important roles in development"），若从 iPS 期组成型敲除，成熟神经元表型将混入发育缺陷，无法回答"成人发病的核缺失"这一疾病问题。HaloPROTAC 平台（Tovell et al., ACS Chem Biol 2019，ref 21）解决的正是"成熟后急性、剂量/时间可控、可逆地去除内源蛋白"：先把 HaloTag 敲入内源 TARDBP 双等位基因（保持生理表达水平），再在成熟神经元加双功能分子 HaloPROTAC-E——一端共价结合 HaloTag、一端招募 E3 泛素连接酶，把目标蛋白送入蛋白酶体（本文 ED Fig. 1e–g 以剂量依赖与 MG132/MLN4924 阻断验证该途径）。30 nM、数天内 TDP-43 即清除，时间窗与病程模拟均可控；"快速可逆"特性来自 ref 21 的平台标定。代价是标签本身轻度影响 TDP-43 功能（ED Fig. 1i），故本文以无标签 CRISPRi 敲低互证（ED Fig. 2b–f），把"标签假象"从竞争解释中排除。

**背景补注（方法平台）：为什么用 NGN2 iNeurons 作为主体系**

电生理与网络读出需要大量、均质、成熟的人兴奋性神经元；经发育信号逐步分化耗时且异质。NGN2 正向编程（Fernandopulle et al., 2018，ref 52；Nehme et al., Cell Rep 2018，ref 53）以 dox 诱导转录因子 NGN2 把 iPS 细胞快速、同步地定向为皮层样兴奋性神经元，数周即可成熟放电。本文 WTC11 系在 AAVS1 位点整合 dox-NGN2、CLYBL 位点整合 dCas9-BFP-KRAB（M. Ward 惠赠；CRISPRi 平台见 Tian et al., Neuron 2019，ref 51），一套基因组同时支持"快速神经元生产"与"无切割基因敲低"；所得 iNeurons 为 layer V 兴奋性身份（CTIP2+、NKX2.1−、PAX6−，ED Fig. 1h），且杂合携带 UNC13A 风险 SNP，等位基因背景贴近患者。边界：纯兴奋性、无抑制性中间神经元，故网络表型只能表现为失同步而非超兴奋（作者自陈局限）。

内容逻辑：本节回答全文的第一个前提问题——在成熟人神经元中急性去掉核 TDP-43，UNC13A 到底会不会丢、丢在哪里。设计上的第一个关键是时间控制：TDP-43 对发育必需，若从 iPS 期敲除会把"成熟缺陷"与"发育缺陷"混在一起，故作者用 CRISPR–Cas12 把 HaloTag 敲入内源 TARDBP 双等位基因 exon 2 起始处，先正常分化成成熟 iNeurons，再加 HaloPROTAC 急性降解（Fig. 1a,b；ED Fig. 1a–d 验证编辑精确、无大染色体 rearrangement、off-target 无编辑）。第二个关键是标签本身的功能代价：HaloTag 部分影响 TDP-43 功能（ED Fig. 1i 显示未加药即有轻度隐匿 inclusion），作者如实承认这一点，并用两条独立证据链排除"表型来自标签而非 TDP-43 缺失"的竞争解释——其一，UNC13A 隐匿剪接与 mRNA 下调只在加 HaloPROTAC 后稳健出现（Fig. 1c,d；ED Fig. 2a）；其二，完全不带标签的 CRISPRi 敲低复现同一表型（ED Fig. 2b–f）。降解机制本身也被验证：剂量依赖、且被蛋白酶体抑制剂 MG132 与 NEDD8 E1 抑制剂 MLN4924 阻断（ED Fig. 1e–g），确认走泛素-蛋白酶体途径。定量上，30 nM HaloPROTAC-E 处理 10 天后 UNC13A 蛋白残留 <5%（Fig. 1e,f），且 TDP-43 在 1–2 天内先消失、UNC13A 随后数天渐降——这一时间差符合"先失剪接调控、再耗竭既有蛋白"的因果顺序，而非同时崩溃。空间上，免疫荧光显示 synapsin 阳性突触 puncta 上的 UNC13A 信号丢失而 synapsin 本身保留（Fig. 1g,h；control n=116、KD n=115 突触，\*\*\*\*），把丢失定位到突触前末梢而非整个神经元。最后作者排除 postsynaptic 受体转录补偿/下调的替代解释：NMDA 与 AMPA 受体亚基 RNA 水平不变（ED Fig. 2g），同 panel 中 CamK2B 隐匿外显子与 STMN2 隐匿加尾则如预期下降，说明剪接缺陷是转录本特异的。本节的贡献是确立"急性核 TDP-43 缺失→突触前 UNC13A 蛋白耗竭"这一分子表型，并把它与发育混杂、标签假象、受体转录变化三者解耦，为下一节的功能测量埋下伏笔：蛋白丢在突触前，功能缺陷应当首先是突触前的。

→ Figure 1 标题为"Loss of TDP-43 or UNC13A impairs synapse function"，旨在建立"TDP-43 或 UNC13A 缺失→突触与网络功能失效"的表型基线。由 a 至 m 共 13 部分构成：a–h 为分子/细胞表型（编辑验证、核定位、剪接、蛋白时间 course、突触定位），i–j 为单细胞自发释放电生理，k–m 为网络水平 MEA，形成"分子丢失→单突触功能→网络功能"的三级表型证据链。

(A) HaloTag 敲入示意图与基因组 PCR 验证
图片解释：左为示意图：人 TARDBP 基因 exon 1–6（蓝色框），绿色 HaloTag 盒插入 exon 2 起始处；右为基因组 PCR 电泳图（n=1）。PCR 的物理原理是：以基因组 DNA 为模板扩增跨插入位点的片段，片段越长在胶/毛细管中迁移越慢、位置越靠上；WT 等位基因产物约 200 bp，敲入 HaloTag（约 800 bp 外源序列）后产物跳到约 1,000 bp，故"Edit"泳道单一条带位于 1,000 bp 附近即证明纯合敲入。定量数据：bp 标记 200/300/400/500/700/1,000；WT 带约 200 bp、Edit 带约 1,000 bp；n=1（代表性凝胶，未给灰度定量）。
横纵轴定义：无坐标轴（示意图+电泳凝胶）。横向为不同基因型泳道（WT / Halo Edit），纵向为 DNA 片段长度（bp，上长下短）。阅读方向：比较同一行各泳道条带位置——条带上移=插入成功。
颜色含义：示意图中蓝色=内源外显子、绿色=HaloTag 插入盒；凝胶为灰度条带，越深代表该长度 DNA 产物越多。
核心结论：内源 TARDBP 双等位基因被精确加上 HaloTag，为成熟期急性降解 TDP-43 提供遗传学开关（编辑精确性另见 ED Fig. 1a–d）。

(B) 核 TDP-43 定位免疫荧光
图片解释：免疫荧光是用抗体偶联荧光染料"点亮"特定蛋白：Map2 标记树突（品红通道）、TDP-43 抗体标记 TDP-43（黄通道）、DAPI 染 DNA 标核（青通道）。上排 NT（未处理）：黄信号与青核重叠，呈核内定位；下排 HaloPROTAC 处理后黄通道几乎全黑、青核仍在，证明 TDP-43 蛋白被降解而非错位。n=3。定量数据：原文未给荧光强度数值，以代表性图像展示核信号消失。
横纵轴定义：无坐标轴（荧光显微图）。横向为通道（Map2 / TDP-43 / DAPI / 合并），纵向为处理条件（NT / HaloPROTAC）。阅读方向：比较同一通道上下两排亮度——TDP-43 通道由亮变黑=降解成功；合并图看黄+青是否共定位成白核。
颜色含义：品红=Map2（树突形态）、黄=TDP-43、青=DAPI（核）；合并图中黄青重叠=核内 TDP-43。配色理由：三通道光谱分离便于判断共定位。
核心结论：HaloTDP iNeurons 中 TDP-43 正常入核，HaloPROTAC 可将其清除，模型具备"核缺失"前提。

(C) UNC13A 剪接 RT–PCR 凝胶
图片解释：RT–PCR 先把它 RNA 逆转录成 cDNA，再用跨 exon 19–22 的引物扩增剪接区；不同剪接异构体长度不同，在电泳上分成不同位置的条带：Correct（正常 exon 20–21 连接）约 300 bp，Short cryptic 约 400–500 bp，Long cryptic 约 500 bp 以上。CTRL 泳道只有 Correct 带；TDP-43 KD 泳道 Correct 带变浅、Short/Long 带出现且深，即隐匿外显子被 inclusion。定量数据：bp 标记 300/400/500；代表性凝胶，灰度定量见 d。
横纵轴定义：无坐标轴（电泳凝胶）。横向为条件泳道（CTRL / TDP-43 KD），纵向为产物长度（bp）。阅读方向：比较两泳道条带"位置+深浅"——新出现的上位条带=隐匿异构体，下位 Correct 带变浅=正常转录本丢失。
颜色含义：灰度条带，越深代表该剪接异构体产物越多。
核心结论：TDP-43 缺失把 UNC13A 剪接从"几乎全 Correct"翻转为"以 cryptic 为主"。

(D) 剪接 PSI 定量
图片解释：PSI=某异构体条带占全部异构体的百分比，把 c 的凝胶数字化。CTRL 的 Correct PSI 约 100%；TDP-43 KD 后 Correct 跌到约 15–20%、Short 升到约 70%、Long 约 10%。n=12 生物学重复、3 次实验；Correct 组间 \*\*\*\*（P<0.0001，两侧 Student's t）。
横纵轴定义：X 轴为异构体类别（Correct / Short / Long），Y 轴为 PSI（%，0–100）。为什么用 PSI 而非绝对量：它归一化了上样与扩增差异，直接读"剪接选择"。阅读方向：同一类别内比较蓝（CTRL）紫（KD）柱高。
颜色含义：蓝=CTRL，紫=TDP-43 KD；散点为独立生物学重复。
核心结论：隐匿剪接翻转是稳健、可定量的主表型（\*\*\*\*），而非个别克隆现象。

(E) 蛋白时间 course Western blot
图片解释：免疫印迹把蛋白按分子量分离后以抗体识别、化学发光显影：条带越深=该蛋白越多。30 nM HaloPROTAC-E 处理 NT/1/2/4/7/10 天：TDP-43 带（约 50–70 kDa）在 1–2 天即消失；UNC13A 带（约 185–250 kDa 区间，ED Fig. 10j 标 185 kDa）逐日变浅、10 天几乎不可见；Tubulin（约 50 kDa）各泳道均一，作上样对照。定量数据：n=2 生物学重复（代表性 blot，灰度定量见 f）。
横纵轴定义：无坐标轴（免疫印迹）。横向为处理天数泳道（NT→10 d），纵向为蛋白分子量（kDa，标记 250/100/70/50）。阅读方向：沿同一行（同一蛋白）从左到右看条带衰减速度。
颜色含义：灰度条带，越深代表该蛋白越多；Tubulin 行均一证明上样可比。
核心结论：TDP-43 先失、UNC13A 后耗，符合"剪接调控丧失→既有蛋白渐耗"的因果时序。

(F) 蛋白衰减曲线
图片解释：把 e 的条带灰度归一化到 NT 画成时间曲线。TDP-43（黑）1–2 天降至近 0；UNC13A（紫）渐降，10 天残留 <5%。n=2。
横纵轴定义：X 轴为 HaloPROTAC 处理天数（0–10 d），Y 轴为相对表达（%，NT=100）。为什么用时间轴：区分"调控因子消失"与"效应蛋白耗竭"两个时间尺度。阅读方向：看两条曲线下降先后与斜率。
颜色含义：黑=TDP-43，紫=UNC13A；误差棒 mean±s.e.m.。
核心结论：10 天急性缺失造成 UNC13A 近完全耗竭（<5%），达到文献中"低于 30% 即突触失效"阈值之下（refs 20,25）。

(G) 突触 UNC13A 免疫荧光
图片解释：4 周成熟 iNeurons（大鼠星形胶质细胞共培养）经 2 周 TDP-43 缺失后固定染色：synapsin（青通道）标记突触前末梢 puncta，UNC13A（品红通道）标记活性区蛋白。CTRL 排两通道 puncta 共定位；KD 排 synapsin puncta 仍在而 UNC13A puncta 几乎消失——突触结构还在、UNC13A 没了。标尺 10 µm。
横纵轴定义：无坐标轴（荧光显微图）。横向为通道（Synapsin / UNC13A / 合并），纵向为条件（CTRL / TDP-43 KD）。阅读方向：比较合并图上下排品红 puncta 的有无，青 puncta 作"突触仍在"的内对照。
颜色含义：青=Synapsin（突触前末梢）、品红=UNC13A；共定位 puncta 呈白/叠色。
核心结论：UNC13A 丢失发生在突触前末梢水平，且突触结构保留——"结构在、分子没"的前退化状态初现。

(H) 突触 UNC13A 强度定量
图片解释：每个散点=一个 synapsin 阳性 ROI（一个突触）内 UNC13A 荧光积分强度（归一化）。CTRL n=116、KD n=115 突触、3 次实验；CTRL 约 1.0、KD 约 0.2–0.3，\*\*\*\*（高斯 LMM+Satterthwaite）。选 ROI 时对 UNC13A 通道盲法，且 ROI 大小两组无差异（P=0.68，Methods），排除"选点偏倚"。
横纵轴定义：X 轴为条件（CTRL / TDP-43 KD），Y 轴为突触 UNC13A 强度（归一化，0–2.0）。为什么以突触为单位：把"蛋白丢失"定位到功能位点而非全细胞平均。阅读方向：比较两群散点中心与分布。
颜色含义：蓝=CTRL，紫=TDP-43 KD；点=单突触。
核心结论：突触前 UNC13A 剂量显著下降（\*\*\*\*），为功能缺陷提供分子定位。

Section 1 关联 Extended Data（紧凑整合）：ED Fig. 1（a–i，9 panel）承担模型质控——amplicon 测序确认 HaloTag 编辑（a）、低深度 WGS Manhattan 图无大 rearrangement（b）、off-target PCR+IGV 无编辑（c,d）、HaloPROTAC 剂量依赖降解（e,f，n=3）、MG132/MLN4924 阻断降解证明蛋白酶体途径（g，n=2）、DIV28 标志物鉴定皮层深层兴奋性身份（h）、以及如实承认 HaloTag 本身致轻度 TDP-43 功能丧失与个别转录本隐匿 inclusion（i，n=2）。ED Fig. 2（a–h，8 panel）承担敲低互证与特异性——HaloPROTAC 后正确剪接 UNC13A mRNA 下降（a，n=10）；CRISPRi TDP-43 KD 复现隐匿剪接（b,c，n=6）、mRNA 下降（d，n=12）、蛋白剧降（e,f，n=7）；受体亚基 RNA 不变而 CamK2B/STMN2 异常剪接下降（g，n=8，Bonferroni 校正）；CRISPRi UNC13A KD 的蛋白验证（h，n=3）。

Section 2：Loss of TDP-43 impairs synapse function（TDP-43 丢失损害突触功能）

**背景补注：UNC13A/Munc13-1 与突触小泡 priming——为什么它是突触失效的关键执行者**

**①是什么、为什么重要。** UNC13A 编码 Munc13-1，是突触前活性区（active zone）核心蛋白，执行突触小泡从对接（docking）到启动（priming）的关键一步：只有经 Munc13 priming 的小泡才获得钙触发融合能力。递质释放是回路功能的最终共同通路，Munc13-1 是谷氨酸能突触释放的必需执行者——这使它既是 TDP-43 核 LoF 致突触失效的头号候选执行者，也是 ALS 第二强 GWAS 信号所在基因（Discussion，refs 14–16）。

**②分子性质。** Munc13-1 为约 185 kDa 的大蛋白（本文 ED Fig. 10j 标注），结构域排布为 N 端 C2A–C1–C2B–中央 MUN–C 端 C2C（排布为领域共识；C1C2B 区膜结合调控见 ref 58）：C1 域结合 DAG/佛波酯、C2B 域结合钙与磷脂，共同调控 priming；中央 MUN 域是催化核心，负责打开 syntaxin-1、促进 SNARE 复合体组装（SNARE 机制为教科书级共识；priming 的形态与分子定义见 Imig et al., Neuron 2014，ref 17）。Munc13-1 主要表达于脑、富集于兴奋性突触活性区，与 RIM 等活性区蛋白协同（refs 17,20）。

**③缺失的后果与前人研究。** Augustin 等（Nature 1999，ref 18）建立 Munc13-1 null 小鼠：出生即死于呼吸衰竭，原代皮层培养发育正常但自发与诱发谷氨酸能传递下降约 90%；Varoqueaux 等（PNAS 2002，ref 19）进一步证明 null 突触"传递完全停摆而突触发生正常"——结构在、功能没。Imig 等（Neuron 2014，ref 17）以电镜把缺陷定位到 priming 步骤（docked 小泡不能转为 primed）。剂量层面：Zarebidaki 等（J Neurosci 2020，ref 20）与 Asadollahi 等（Nat Genet 2025，ref 25）确立"低于正常约 30% 才出现强突触缺陷"的阈值，杂合小鼠与携带杂合 LoF 突变的人均存活且神经生理正常；双等位致病突变则致神经发育综合征（癫痫、皮层超兴奋、重症肌无力等，refs 25,44,45）。

**④遗留缺口。** 上述经典几乎全部来自啮齿类原代神经元与小鼠遗传学，人神经元证据有限（Results 原文："Previous investigations... mainly conducted using primary rodent neurons with limited studies in human neurons"）；且 UNC13A 丢失是否主导 TDP-43 核 LoF 的突触表型、在数百个错剪接事件中权重如何，未被检验。

**⑤与本文的关系。** 本文在人 iNeurons 中补上这一环：直接 CRISPRi 敲低 UNC13A 镜像 TDP-43 缺失的突触前表型（Fig. 1i,j），单外显子删除 rescue 约 80% 频率（Fig. 2i–l），并借 30% 阈值把"部分蛋白回补即有效"转化为 ASO 剂量预测（Fig. 4a,b）。概念上，本文"功能性死亡"（结构完好、存活正常但突触通讯崩溃）正是 Varoqueaux 2002"传递停摆而突触发生正常"这一经典观察在 TDP-43 蛋白病语境下的延伸——并进一步证明该状态可被单点纠错逆转。

内容逻辑：本节把分子表型翻译成功能表型，回答"UNC13A 丢在突触前，突触到底坏没坏、坏在哪一侧"。作者先补一个领域缺口：UNC13A 生理功能既往主要在啮齿类原代神经元研究（refs 18–20,22），人神经元证据有限，故直接在人 iNeurons 上做全细胞膜片钳。逻辑链分三步：第一步，CRISPRi 直接敲低 UNC13A 使 mEPSC 频率下降而幅度不变（Fig. 1i；ED Fig. 3b），符合"纯突触前缺陷"的经典判读（频率=释放×突触数，幅度=postsynaptic 量子反应），与既往啮齿类工作一致（refs 19,20）；第二步，HaloPROTAC 降解 TDP-43 复现频率下降（Fig. 1j），但幅度有轻度下降（ED Fig. 3c）——作者如实保留这一"不完全重合"：它提示 TDP-43 缺失还有 UNC13A 之外的 postsynaptic 成分，为后文"单事件 rescue 不能解释全部表型"埋下伏笔；第三步，把单细胞缺陷放大到网络：MEA 显示 UNC13A 或 TDP-43 缺失都使网络同步性（电极互相关）崩溃，而活性电极数与细胞覆盖不变（ED Fig. 3g,h），排除"细胞死了/电极没覆盖"的替代解释；CNQX 阻断对照证明同步性依赖快 AMPA 传递（ED Fig. 3f）。值得诚实指出的弱效应：UNC13A KD 的网络同步配对比率检验 P=0.0508（Fig. 1l），恰在 0.05 门槛之外，作者未将其标星；TDP-43 KD 则显著（Fig. 1m，\*）。这一分寸防止把"UNC13A 单基因敲低足以完全复现网络表型"夸大为无条件结论。被动膜特性两组可比（ED Fig. 3d,e；TDP-43 KD 电容轻度下降 \*），排除兴奋性/健康度混杂。本节的贡献是确立"TDP-43 缺失→快谷氨酸能传递与网络同步 substantially 受损，且表型与直接 UNC13A 丢失高度镜像"，从而把下一节的因果问题逼出来：镜像是否意味着单事件驱动？

→ Figure 1（续）i–m 为功能表型部分，与 a–h 共同构成 Fig. 1 的 13 panel。

(I) UNC13A 敲低的 mEPSC
图片解释：膜片钳在 −70 mV 钳制下记录自发单小泡事件：TTX 阻断动作电位、gabazine 阻断抑制性电流，故每个向下尖峰=一个突触小泡自发融合引起的 AMPA 电流（pA 级）。左为 2.5 s 代表迹线：CTRL（青）密集尖峰、UNC13A KD（紫）几乎平坦；右为平均单事件（1 ms/10 pA）两条件幅度相近。下方频率柱：CTRL 约 2 Hz、KD 约 0.2 Hz（\*\*，n=12/13 细胞、3 次实验）；累积事件间隔曲线 KD 右移=等待下一次事件的时间变长。
横纵轴定义：迹线 X=时间（s）、Y=电流（pA，向下为兴奋性 inward 电流）；频率图 X=条件、Y=频率（Hz，0–8）；累积图 X=事件间隔（ms，0–1×10^5）、Y=累积频率（%）。为什么用频率+累积间隔双读出：频率给均值、累积分布给全分布形状，避免均值掩盖异质性。阅读方向：迹线数尖峰密度；累积曲线越靠左=事件越频繁。
颜色含义：青=CTRL，紫=UNC13A KD；散点=单细胞。
核心结论：UNC13A 丢失选择性降低自发释放频率（突触前缺陷），幅度不变（ED Fig. 3b）。

(J) TDP-43 敲低的 mEPSC
图片解释：同 I 的读法，比较 CTRL（蓝）与 TDP-43 KD（紫）：代表迹线尖峰密度骤降；频率 CTRL 约 0.2 Hz、KD 约 0.05 Hz（\*\*，n=20/22、3 次实验）；累积间隔曲线右移。平均事件幅度轻度减小（ED Fig. 3c，\*\*），提示额外 postsynaptic 成分。
横纵轴定义：同 I（频率轴 0–1.5 Hz；累积间隔 0–2×10^5 ms）。阅读方向：同 I。
颜色含义：蓝=CTRL，紫=TDP-43 KD。
核心结论：TDP-43 缺失镜像 UNC13A 丢失的突触前自发释放缺陷，且伴轻度幅度下降（后者 UNC13A 非依赖）。

(K) MEA 代表 raster 图
图片解释：MEA 在培养孔底以多电极细胞外记录群体放电：raster 图每行=一个电极、每个竖 tick=一次 spike；蓝色 tick 簇=单电极 burst，粉色框=网络 burst（≥35% 电极在窗内共同放电）。CTRL（DIV38）呈整齐粉色竖列=全网络同步爆发；UNC13A KD（DIV32）与 TDP-43 KD（DIV38）tick 散乱、粉色框稀少=电极仍放电但彼此失协。展示 60 s。
横纵轴定义：X=时间（60 s）、Y=电极编号（行）。为什么用 raster：一眼区分"放电少了"与"放电不协同了"——本表型是后者。阅读方向：看粉色竖列是否贯穿多数行。
颜色含义：蓝=电极 burst，粉=网络 burst，灰/黑=单 spike；caption 明确注明该配色。
核心结论：缺失导致网络异步化，而非单纯放电率下降。

(L) UNC13A 敲低网络同步时间 course 与配对 fold change
图片解释：左为归一化互相关 AUC 随天数（DIV15–35）曲线：CTRL（青）随成熟升到约 100，UNC13A KD（紫）徘徊约 10–20；右为同板平行分化的配对 log2[FC] 连线图，各点落在 −1 至 −2.5，配对比率 t 检验 P=0.0508（未标星）。n=18 孔、3 次实验；符号=独立实验，线连同板平行分化。
横纵轴定义：左 X=天数（DIV）、Y=归一化互相关 AUC（0–150）；右 X=条件（CTRL→KD）、Y=log2[FC]（−5–0，虚线 0=无变化）。为什么用配对：同板平行分化消除板间差异。阅读方向：左看两曲线分离程度；右看连线是否一致向下。
颜色含义：青=CTRL，紫=UNC13A KD。
核心结论：UNC13A 缺失使网络同步发育失败；配对检验 P=0.0508 为边缘性弱效应，如实保留、不夸大。

(M) TDP-43 敲低网络同步时间 course 与配对 fold change
图片解释：同 L 读法：CTRL（蓝）DIV40 前后升到约 100，TDP-43 KD（紫）贴底；配对 log2[FC] 点约 −2.4/−4.2/−4.6，\*（P<0.05）。n=18 孔、3 次实验。
横纵轴定义：同 L（左 X 轴 DIV20–40+）。阅读方向：同 L。
颜色含义：蓝=CTRL，紫=TDP-43 KD。
核心结论：TDP-43 缺失显著破坏网络同步（\*），效应量大于 UNC13A 单敲低，提示多事件叠加但 UNC13A 占主权重（待 Section 4 检验）。

Section 2 关联 Extended Data（紧凑整合）：ED Fig. 3（a–h，8 panel）——CNQX 完全消除 mEPSC（a，证明 AMPA 介导）；UNC13A KD 幅度 ns（b）而 TDP-43 KD 幅度轻度降 \*\*（c，约 33→24 pA 读自图）；被动膜特性 UNC13A KD 全 ns（d）、TDP-43 KD 仅电容轻度降 \*（e）；CNQX 消除网络同步而对平均放电率影响小（f，同步 \*\*、放电率 P=0.0687）；多 MEA 指标点图显示同步性/AUCC 是最大且最一致的变化（g）；phase-contrast 覆盖可比（h，标尺 350 µm）。

Section 3：Genomic deletion of UNC13A cryptic exon（基因组删除 UNC13A 隐匿外显子）

内容逻辑：本节是全文的因果枢纽，回答"UNC13A 蛋白丢失究竟是不是那个隐匿外显子造成的"。竞争解释有二：解释 A，内含子 20 隐匿外显子 inclusion 是蛋白丢失的主因；解释 B，内含子 31 保留或其他低频剪接异常、乃至 TDP-43 对 UNC13A 的其他调控（稳定性/运输）才是主因。作者的鉴别设计是基因组刀：在 SH-SY5Y 用双 sgRNA 做 233 nt 纯合删除，同时去掉长/短隐匿外显子的两个 3′ 受体位点与共用 5′ 供体位点——这样即使 TDP-43 缺失、剪接机器想 inclusion 也无序列可用，从而把"隐匿外显子"这一个变量从数百个错剪接事件中单独摘除。结果：WT 系 TDP-43 KD 后隐匿剪接稳健出现，CE DEL 系完全检不出 cryptic（ED Fig. 4c,d），正确剪接 mRNA 被 rescue、蛋白 rescue 约 75%（ED Fig. 4e–g）——注意是约 75% 而非 100%，作者如实保留这一缺口，暗示其余剪接异常或调控仍有小权重。随后把同一删除搬进 iPS 细胞（ED Fig. 5a–e 质控），在 CRISPRi TDP-43 KD 背景下复现 RNA/蛋白 rescue（ED Fig. 5f–k），并关键性地显示 STMN2 隐匿加尾不被 rescue（ED Fig. 5f,h,i）——证明 rescue 是 UNC13A 事件特异，而非"删除改善了全局剪接"。最后在 CE DEL 系上再敲入 HaloTag（ED Fig. 6），得到"可急性降解 TDP-43 + 单事件已修"的双编辑 iNeurons：DIV28、14 天 HaloPROTAC 后，exon 20–21 剪接、mRNA、突触前蛋白均被 rescue（Fig. 2a–h）。本节的贡献是确立"内含子 20 隐匿外显子是 TDP-43 依赖性 UNC13A 丢失的主驱动"，并把因果刀递到功能层面：下一节问"只修这一个事件，突触功能够不够恢复"。

→ Figure 2 标题为"Genomic deletion of UNC13A cryptic exon rescues synapse function following TDP-43 loss"，旨在证明单外显子删除对分子与功能表型的 rescue。由 a 至 l 共 12 部分构成：a–h 为分子 rescue（示意图、剪接、RNA、蛋白、突触定位），i–l 为功能 rescue（mEPSC、MEA），形成"单事件纠正→分子回补→功能回补"的因果证据链。

(A) 隐匿外显子删除示意图
图片解释：示意 UNC13A 基因组 exon 20（蓝）与 exon 21（蓝）之间的内含子（灰）：深蓝色长隐匿外显子内嵌短隐匿外显子（虚线分界），黄色小盒=风险 SNP 位置，红色三角=gRNA1/gRNA2 切割位点（分别位于长隐匿外显子受体上游 45 bp 与供体下游 10 bp）。删除 233 nt 后两个受体与共用供体一并移除。
横纵轴定义：无坐标轴（基因组示意图）。横向为基因组位置（exon 20→intron→exon 21）。阅读方向：从左到右看切割位点夹住的区段=被删除区。
颜色含义：蓝= constitutive 外显子，深蓝=隐匿外显子（长/短），黄=风险 SNP，红三角=gRNA 切点。
核心结论：删除设计从序列上根除隐匿剪接的可能，是"单变量因果刀"。

(B) WT 与 CE DEL 的剪接 RT–PCR
图片解释：四泳道（WT CTRL / WT TDP-43 KD / CE DEL CTRL / CE DEL TDP-43 KD），DIV28、14 天 HaloPROTAC。WT CTRL 仅 Correct 带（约 300 bp）；WT KD 出现 Long/Short 带；CE DEL 两条件均仅 Correct 带——TDP-43 缺失也无法制造 cryptic。
横纵轴定义：无坐标轴（电泳凝胶）。横向为基因型×处理泳道，纵向为产物长度（bp，300/400/500）。阅读方向：比较 WT KD 与 CE DEL KD 泳道有无上位 cryptic 带。
颜色含义：灰度条带，越深=该异构体越多。
核心结论：删除使隐匿剪接"无序列可用"，因果变量被干净摘除。

(C) PSI 定量（四组）
图片解释：Correct PSI：CTRL 约 100、TDP-43 KD 约 40、CE DEL 约 100、CE DEL+KD 约 100（\*\*\*\* CTRL vs KD；NS CE DEL vs CE DEL+KD）；Short/Long PSI 在 CE DEL 两条件近 0。n=6 生物学重复、3 次实验；单因素 ANOVA+Tukey。
横纵轴定义：X=异构体（Correct/Short/Long），Y=PSI（%，0–100）。阅读方向：同类别内四色柱比较。
颜色含义：蓝紫=CTRL，紫=TDP-43 KD，青=CE DEL，绿=CE DEL+TDP-43 KD（全文四组统一配色）。
核心结论：单外显子删除在 TDP-43 缺失背景下完全维持正常剪接选择。

(D) 正确剪接 UNC13A mRNA 定量
图片解释：RT–qPCR（exon 20–21 junction assay）相对表达：CTRL 约 100、KD 约 15（\*\*\*\*）、CE DEL 约 100、CE DEL+KD 约 100（NS）。n=6、3 次实验。
横纵轴定义：X=四条件，Y=相对 RNA 表达（%，0–150）。阅读方向：看 KD 柱是否被 CE DEL 拉回。
颜色含义：同 C 四色。
核心结论：mRNA 丢失被单事件删除完全 rescue。

(E) 蛋白 rescue Western blot
图片解释：四泳道（WT−/WT+/CE DEL−/CE DEL+，+=TDP-43 KD）：UNC13A（约 185–250 kDa）WT+ 几乎消失、CE DEL+ 保留强带；TDP-43（约 70 kDa）+ 泳道消失证明降解有效；STMN2（约 25–55 kDa）+ 泳道两基因型均下降——内对照显示删除不 rescue STMN2；Tubulin（55 kDa）均一。
横纵轴定义：无坐标轴（免疫印迹）。横向为基因型×处理泳道，纵向为分子量（kDa，250/70/25/55）。阅读方向：沿 UNC13A 行比较四泳道；沿 STMN2 行确认特异性边界。
颜色含义：灰度条带，越深=蛋白越多。
核心结论：蛋白 rescue 是 UNC13A 特异的（STMN2 不 rescue），排除全局剪接改善的解释。

(F) 蛋白定量
图片解释：TDP-43 相对蛋白：CTRL 约 95、KD 约 10（\*\*）、CE DEL 约 90、CE DEL+KD 约 10（\*\*）——降解效率两组一致；UNC13A：CTRL 约 90、KD 约 10（\*）、CE DEL 约 110、CE DEL+KD 约 95（NS）。n=6、3 次实验；重复测量 ANOVA（log 转换、上样归一化）+Tukey。
横纵轴定义：X=四条件（分 TDP-43 与 UNC13A 两面板），Y=相对蛋白表达（%，0–150）。阅读方向：比较 KD 与 CE DEL+KD 的 UNC13A 柱。
颜色含义：同 C 四色。
核心结论：在 TDP-43 仍缺失时，单事件删除把 UNC13A 蛋白拉回接近正常（NS vs CE DEL）。

(G) 突触定位免疫荧光（四组）
图片解释：四排（CTRL / TDP-43 KD / CE DEL / CE DEL+KD）×三通道（Synapsin 灰 / UNC13A 灰 / 合并青-品红）：KD 排品红 puncta 消失，CE DEL+KD 排品红 puncta 恢复且与青共定位。4 周成熟、2 周 KD；标尺 10 µm。
横纵轴定义：无坐标轴（荧光显微图）。横向为通道，纵向为四条件。阅读方向：比较合并图第二排与第四排品红 puncta。
颜色含义：青=Synapsin，品红=UNC13A。
核心结论：rescue 发生在突触前末梢的功能位点，而非仅全细胞蛋白量。

(H) 突触 UNC13A 强度（四组）
图片解释：归一化强度：CTRL 约 1.0、KD 约 0.6、CE DEL 约 1.0、CE DEL+KD 约 0.95；n=71/71/66/75 突触、3 次实验；\*\*\*\* CTRL vs KD 与 KD vs CE DEL+KD，CE DEL+KD 与 CTRL/CE DEL 无显著差（LMM+Satterthwaite）。
横纵轴定义：X=四条件，Y=归一化突触 UNC13A 强度（0–2.5）。阅读方向：看 KD 凹陷是否被 CE DEL+KD 填平。
颜色含义：同 C 四色；点=单突触。
核心结论：单事件删除恢复突触前 UNC13A 剂量至对照水平。

Section 3 关联 Extended Data（紧凑整合）：ED Fig. 4（a–g，7 panel）SH-SY5Y 删除系质控与 rescue（基因组 PCR a、amplicon b、剪接 c,d n=8、RNA e n=8、蛋白 f,g n=5，蛋白 rescue 约 75%）；ED Fig. 5（a–k，11 panel）iPS 删除系质控（a–e：PCR、amplicon、Manhattan、off-target PCR、IGV）与 CRISPRi 背景下 rescue（f–k：剪接 g n=6、STMN2 不 rescue h、RNA i、蛋白 j,k n=4）；ED Fig. 6（a–e，5 panel）CE DEL 系上 HaloTag 二次编辑质控（PCR、amplicon、Manhattan、off-target、IGV）。

Section 4：UNC13A cryptic exon drives synapse dysfunction（UNC13A 隐匿外显子驱动突触功能障碍）

内容逻辑：本节回答全文最核心的因果问题：TDP-43 有数百个验证过的 RNA 靶标，调控几乎每个神经元功能层面的剪接、稳定性与运输，因此突触传递下降完全可能是"多基因联合打击"（解释 B：囊泡运输、钙信号、活性区组织等多通路叠加）；而解释 A 认为单个 UNC13A 隐匿外显子就占主权重。鉴别手段即上一节造好的 CE DEL 双编辑系：在 TDP-43 仍被降解的背景下做膜片钳与 MEA。结果支持解释 A 为主：单外显子删除使 mEPSC 频率恢复约 80%（Fig. 2i,j；n=17/22/15/28 细胞），MEA 网络同步恢复（Fig. 2k,l；n=4 独立实验，\*），且同步性是 rescue 最稳健的 MEA 指标（ED Fig. 7f）。但作者同时如实划界：mEPSC 幅度仍残留约 10% 下降（ED Fig. 7a），突触密度下降也不被删除 rescue（ED Fig. 7c,d：树突单位面积突触数 CTRL 约 0.05/µm²、KD 约 0.025、CE DEL+KD 仍低），活性电极数与细胞覆盖可比（ED Fig. 7f,g），存活无差异（ED Fig. 7h：Incucyte 纵向计数与 NeuN/DAPI 高内容计数四组重叠）。这些负性/弱阳性结果共同限定结论：UNC13A 单事件解释的是"剩余突触的功能强度"，而非突触数量或 postsynaptic 量子幅度——即 rescue 是功能性的、突触前的，结构丢失另有驱动基因。由此本节确立"单隐匿外显子 inclusion 足以驱动 TDP-43 缺失性突触失效的主成分"，并把问题推向转化：既然基因组删除够，那么不改基因组、只给一个占位剪接位点的药（ASO）够不够？

→ Figure 2（续）i–l 为功能 rescue 部分，与 a–h 共同构成 Fig. 2 的 12 panel。

(I) 四组 mEPSC 代表与平均迹线
图片解释：读法同 Fig. 1i：−70 mV 电压钳、TTX+gabazine 下每个向下尖峰=单小泡自发融合。四条件迹线：CTRL（蓝）密集、TDP-43 KD（紫）几乎平坦、CE DEL（青）密集、CE DEL+KD（绿）恢复大部分尖峰；右侧平均单事件（1 ms/10 pA）四组幅度相近（KD 略小）。标尺 50 pA/2.5 s。
横纵轴定义：迹线 X=时间（s）、Y=电流（pA）；平均事件 X=ms、Y=pA。阅读方向：数四条迹线尖峰密度，再看平均事件幅度是否齐平。
颜色含义：蓝=CTRL，紫=TDP-43 KD，青=CE DEL，绿=CE DEL+KD。
核心结论：单外显子删除在 TDP-43 缺失背景下恢复自发释放事件密度。

(J) mEPSC 频率与累积事件间隔（四组）
图片解释：频率柱：CTRL 约 0.6 Hz、KD 约 0.1（\*\*）、CE DEL 约 0.6、CE DEL+KD 约 0.4（\* vs KD），即约 80% 频率恢复（正文表述）；累积间隔曲线绿线回到蓝/青线附近、远离紫线。n=17/22/15/28 细胞、3 次实验；LMM+Satterthwaite。
横纵轴定义：频率图 X=四条件、Y=Hz（0–4）；累积图 X=事件间隔（ms，0–2×10^5）、Y=累积频率（%）。阅读方向：频率看绿柱相对紫柱回升幅度；累积看绿线左移回蓝线。
颜色含义：同 I 四色；点=单细胞。
核心结论：单事件纠正恢复约 80% 自发释放频率——突触前功能缺陷的主成分被单事件解释。

(K) 四组 MEA 代表 raster
图片解释：读法同 Fig. 1k：每行一个电极、tick=spike，蓝=电极 burst、粉=网络 burst，60 s（DIV39）。CTRL 与 CE DEL 呈贯穿多行的粉色竖列（同步爆发）；TDP-43 KD 散乱异步；CE DEL+KD 恢复粉色竖列。
横纵轴定义：X=时间（60 s）、Y=电极行。阅读方向：比较四幅图粉色竖列的密度与贯穿度。
颜色含义：蓝=电极 burst，粉=网络 burst（caption 注明）。
核心结论：单事件删除恢复网络级同步爆发，即释放恢复足以支撑信号跨网络传播。

(L) 网络同步配对 fold change
图片解释：同板平行分化配对 log2[FC]：TDP-43 KD 点约 −1.1/−1.5/−3.4，CE DEL+KD 点约 −0.3/−0.4/−1.0，连线一致上移，\*（两侧配对比率 t，n=4 独立实验）。虚线 0=与对照无差。
横纵轴定义：X=条件（TDP-43 KD→CE DEL+KD）、Y=网络同步 log2[FC]（−4–1）。为什么配对：消除 MEA 板间差异。阅读方向：看连线斜率是否一致向上。
颜色含义：紫=TDP-43 KD，绿=CE DEL+KD。
核心结论：单事件删除显著回补网络同步（\*），是 rescue 最稳健的网络指标（ED Fig. 7f）。

Section 4 关联 Extended Data（紧凑整合）：ED Fig. 7（a–h，8 panel）——mEPSC 幅度四组：CTRL 约 41 pA、KD 约 31（\*）、CE DEL 约 38、CE DEL+KD 约 33，即幅度残余下降不被 rescue（a）；被动膜特性电容/接入电阻有组间小差异（b，\* / \*\*）；树突突触密度（c，n=17/17/16/16 细胞）与全视野突触数（d，n=21/20/12/22 视野）均显示 KD 下降且 CE DEL 不 rescue（\*\*\* / \*\* / \*）；网络同步时间 course CE DEL vs CE DEL+KD 分离（e）；多 MEA 指标中同步性 rescue 最稳健（f）；电极覆盖可比（g，标尺 350 µm）；Incucyte 纵向细胞计数与 Opera NeuN+ 百分比四组重叠、无存活差异（h，n=3）。

Section 5：UNC13A splice-switching ASOs（UNC13A 剪接切换 ASO）

**背景补注：splice-switching ASO 治疗范式——从 SMA 临床先例到本文 UNC13A 策略**

**ASO 是什么、两种机制。** 反义寡核苷酸（ASO）是长约 15–25 nt 的合成核酸，靠 Watson–Crick 碱基互补结合目标 RNA；硫代磷酸酯骨架与核糖 2′ 位修饰（LNA、MOE 等）赋予核酸酶稳定性、亲和力与药代性质。按机制分两类：gapmer 型（两翼修饰＋中间 DNA）招募 RNase H 降解目标 RNA，用于"敲低"；splice-switching 型（全修饰、不招募 RNase H）以空间占位封锁剪接位点或调控元件，把剪接"扳"向目标异构体而不降解 RNA——本文用的是后者。

**临床先例：SMA 与 nusinersen。** 脊髓性肌萎缩（SMA）由 SMN1 缺失致病，旁系同源 SMN2 因外显子 7 剪接沉默只能产生少量功能蛋白；nusinersen 占位 SMN2 内含子 7 的 ISS-N1 元件恢复外显子 7 inclusion（策略综述见 Rigo et al., J Cell Biol 2012，ref 23），ENDEAR 随机对照试验证明其改善婴儿型 SMA 运动里程碑（Finkel et al., NEJM 2017，ref 50），并于 2016 年获批成为首个上市的剪接切换 ASO（获批年份与 nusinersen 18-nt 全 MOE 化学为外部事实，阅读深度：确立结论级）。其鞘内给药路径（ASO 不跨血脑屏障）亦为本文 ICV 给药提供参照。

**TDP-43 蛋白病内的同族先例。** Baughn 等（Science 2023，ref 24）解析 STMN2 隐匿剪接-多聚腺苷酸化机制并用 splice-switching ASO 在 TDP-43 缺失背景下恢复全长 STMN2——本文策略最直接的方法学前作：同一范式（占位隐匿事件、恢复生理转录本），不同靶基因。与之对照，tofersen（SOD1，ref 9）与 FUS ASO（ref 10）属降解型、且只覆盖突变携带者。

**本文策略的定位与优势。** 本文把该范式移植到 UNC13A：占位隐匿外显子 5′ 供体位点，阻止 inclusion、恢复 exon 20–21 正确连接。转化优势有三（Discussion）：恢复生理转录本水平、无过表达风险；靶点有 GWAS＋生存修饰的人群锚定；单点占位即可、无需纠正全部错剪接。化学上先 LNA 21-nt 初筛、再转全 MOE 21-nt（耐受性）、再 18-nt MOE walk（效力）；神经元以 1 µM 自由摄取给药（免转染、贴近临床给药方式），体内经 ICV 递送至人源化小鼠脊髓。

内容逻辑：本节把因果发现转化为可给药分子，回答"不改基因组、只用寡核苷酸占位，能否复现基因组刀的 rescue"。策略借鉴两个成功先例：SMA 的 SMN2 剪接纠正（nusinersen，refs 23,50）与 TDP-43 蛋白病中 STMN2 隐匿剪接-加尾的 ASO 纠正（ref 24）——后者与本文同属"纠正 TDP-43 依赖性隐匿事件"，是直接方法学前作（ref 24 证明 splice-switching ASO 可在 TDP-43 缺失背景下恢复 STMN2 全长转录本）。设计逻辑分三代：第一代 LNA 修饰 21-nt ASO 覆盖隐匿外显子受体/供体位点，在 SK-N-BE(2) 转染筛选，发现靶向供体位点的 21-nt 能恢复 exon 20–21 剪接（ED Fig. 8a,b）；第二代为改善治疗耐受性把领先化合物改为全 MOE 核糖修饰（M21-4/M21-5），在 HaloTDP iNeurons 以 1 µM 自由摄取给药（神经元难转染，自由摄取是转化相关给药方式），剪接恢复 >90%、蛋白恢复 30–50%（Fig. 3a–c；ED Fig. 8h），且 M21-4 提升突触前 UNC13A puncta 强度（Fig. 3d；n=88/96 突触，\*\*\*\*）；第三代为把蛋白 rescue 推过 50%，沿隐匿供体位点做 18-nt MOE walk（合成 24 条、按序列驱动 off-target 与二级结构预筛），在 SH-SY5Y 读剪接后回神经元验证：领先 18-nt（M18-14/16/17/18 等）剪接 >90%、蛋白 >50%（Fig. 3e,f；ED Fig. 9c–h）。amplicon 测序进一步证明 ASO 对参考与风险两等位基因均纠错（ED Fig. 9i，n=1）——对杂合风险 SNP 携带者（如 WTC11）这一点是转化必需。体内验证用人源化小鼠：小鼠本底无该人特异隐匿剪接，故把小鼠内含子 20 替换为含风险 SNP 的人源内含子（hUNC13A reporter）；尾静脉 AAV PHP.eB 递送靶向 Tardbp 的合成 microRNA 制造体内 TDP-43 缺失，同日 ICV 给 M21-4 或 ACSF，3 周后脊髓 RT–PCR 显示：WT 鼠无 cryptic、reporter 鼠 KD 后 cryptic 稳健出现、ASO 部分 rescue（Fig. 3h–k；PSI 约 75→约 95，cryptic RNA 约 100→约 30）。作者如实使用"partially rescued"：体内是剪接分子药效学证据，而非功能/行为 rescue。本节的贡献是确立"单点占位即可在体外神经元与体内人源化脊髓复现基因组刀的分子 rescue"，并给出蛋白 rescue 30–50%（21-nt）与 >50%（18-nt）两个剂量级，为下一节"多少蛋白够救功能"埋下伏笔。

→ Figure 3 标题为"UNC13A splice-switching ASOs rescue UNC13A expression following TDP-43 loss"，旨在展示 ASO 设计、体外剪接/蛋白 rescue 与体内人源化药效。由 a 至 k 共 11 部分构成：a–f 为体外 ASO 化学与分子 rescue，g–k 为体内实验设计与脊髓剪接读出，形成"设计→筛选→优化→体内验证"的转化证据链。

(A) ASO 靶位示意图
图片解释：绿色盒=隐匿外显子（内含黄色风险 SNP），箭头=隐匿 5′ 剪接供体位点，上方蓝短线=TDP-43 结合 motif；下方给出靶 RNA 序列（AAG GAUGGAUGGAGAGAGUGGGUAGUA CAUGGAUGGAUAGAUGGAU）与各 ASO 的结合窗横线：M21-4（青）、M21-5（品红）覆盖供体区，M18-1/12/14/16/17/18（蓝绿系）沿供体区逐核苷酸平移。原理一句话：ASO 靠碱基互补占住供体位点，剪接机器无法识别该位点，隐匿外显子被跳过、exon 20 直接连 exon 21。
横纵轴定义：无坐标轴（序列示意图）。横向为 RNA 序列位置（5′→3′）。阅读方向：看各横线覆盖区与箭头（供体）的重叠程度。
颜色含义：绿=隐匿外显子，黄=风险 SNP，蓝短线=TDP-43 motif，青/品红/蓝绿横线=各 ASO 结合窗。
核心结论：靶点选择集中在隐匿供体位点——占位一个位点即可切换剪接命运。

(B) 21-nt MOE ASO 剪接 rescue（RT–PCR+PSI）
图片解释：凝胶五泳道（CTRL / NT / ASO CTRL / M21-4 / M21-5，后四者 TDP-43 KD）：NT 与 ASO CTRL 以 cryptic 带为主，M21-4/5 恢复 Correct 带（约 300 bp）。PSI 柱：CTRL 约 95、KD 约 30、ASO CTRL 约 35、M21-4 约 90、M21-5 约 95（\*\*\*\* 等）。n=6 生物学重复、3 次实验；ANOVA+Tukey。
横纵轴定义：凝胶无坐标轴（横=泳道、纵=bp 300/400/500）；PSI 图 X=条件、Y=Correct PSI（%，0–100）。阅读方向：凝胶看 Correct 带回归；柱图看 M21 两柱是否回到 CTRL 高度。
颜色含义：灰=CTRL，紫=TDP-43 KD，蓝紫=ASO CTRL，青=M21-4，品红=M21-5。
核心结论：21-nt MOE ASO 把正确剪接恢复到 >90%。

(C) 21-nt ASO 蛋白 rescue（Western+定量）
图片解释：五泳道 blot：UNC13A（约 185–250 kDa）CTRL 强、NT/KD/ASO CTRL 近无、M21-4 中等、M21-5 较强；TDP-43（约 70 kDa）仅 CTRL 有带（证明 KD 有效且 ASO 不恢复 TDP-43）；Tubulin（55 kDa）均一。定量：UNC13A 相对蛋白 CTRL 100、KD 约 5、ASO CTRL 约 5、M21-4 约 35（\*\*\*）、M21-5 约 50（\*\*）。n=5、3 次实验；重复测量 ANOVA+Tukey。
横纵轴定义：无坐标轴（免疫印迹；横=泳道、纵=kDa 250/70/55）；定量图 X=条件、Y=相对蛋白（%，0–100+）。阅读方向：沿 UNC13A 行看 M21 泳道带强回升幅度。
颜色含义：灰度条带越深=蛋白越多；定量柱配色同 B。
核心结论：剪接纠正转化为蛋白回补 30–50%，且 TDP-43 仍缺失——rescue 不依赖恢复 TDP-43。

(D) M21-4 恢复突触前 UNC13A（免疫荧光+定量）
图片解释：TDP-43 KD iNeurons 给 MOE CTRL 或 M21-4 后染色：synapsin（青）puncta 两组均在，UNC13A（品红）puncta 在 M21-4 组明显更亮更多；定量归一化强度 ASO CTRL 约 0.8、M21-4 约 1.6（\*\*\*\*；n=88/96 突触；LMM）。标尺 10 µm。
横纵轴定义：显微图无坐标轴（横=通道、纵=处理）；定量 X=两条件、Y=归一化强度（0–4）。阅读方向：比较合并图品红 puncta 亮度与散点中心。
颜色含义：青=Synapsin，品红=UNC13A；定量灰=ASO CTRL、青=M21-4。
核心结论：ASO 把 UNC13A 送回突触前功能位点，而非仅提升全细胞蛋白。

(E) 18-nt MOE walk 剪接 rescue
图片解释：凝胶十泳道（CTRL / NT / ASO CTRL / M18-1 / -12 / -14 / -16 / -17 / -18，TDP-43 KD）：M18-1 恢复较弱、M18-12 起 Correct 带渐强、M18-14/16/17/18 接近 CTRL。PSI 柱：CTRL 约 95、KD 约 35、ASO CTRL 约 35、M18-1 约 75、M18-12 约 85、M18-14 约 90、M18-16 约 92、M18-17 约 93、M18-18 约 93（\*\*\*\* 等）。n=6、3 次实验。
横纵轴定义：凝胶无坐标轴（横=泳道、纵=bp）；PSI 图 X=条件、Y=%（0–100）。阅读方向：沿 walk 顺序看 PSI 递增趋势=结合窗优化轨迹。
颜色含义：灰=CTRL，紫=KD，蓝紫=ASO CTRL，蓝绿系=各 M18（与 a 横线配色对应）。
核心结论：18-nt walk 找到剪接 rescue >90% 的更短化合物窗。

(F) 18-nt ASO 蛋白 rescue
图片解释：十泳道 blot：UNC13A 带 M18-1 弱、M18-12 中弱、M18-14/16/17/18 中强；TDP-43 仅 CTRL 有带；Tubulin 均一。定量：CTRL 约 95、KD 约 5、ASO CTRL 约 5、M18-1 约 15、M18-12 约 25、M18-14 约 55、M18-16 约 60、M18-17 约 62、M18-18 约 50（\*\* 等）。n=5、3 次实验。
横纵轴定义：无坐标轴（免疫印迹；横=泳道、纵=kDa 250/70/55）；定量 X=条件、Y=相对蛋白（%，0–100）。阅读方向：沿 UNC13A 行比较各 M18 带强，确认 >50% 者。
颜色含义：灰度条带；定量柱配色同 E。
核心结论：18-nt 领先化合物把蛋白 rescue 推过 50%（M18-17 约 60%），高于 21-nt 的 30–50%。

(G) 体内实验示意图
图片解释：hUNC13A reporter 小鼠两处给药：脑室（ICV）注射 UNC13A ASO（脑内插管示意），尾静脉注射 AAV microRNA Tardbp（尾部插管示意）。原理：AAV PHP.eB 跨血脑屏障递送合成 microRNA 在小鼠全身/中枢敲低 Tardbp；ICV 把 ASO 直接送入脑脊液分布到脊髓。图改编自 NIH BioArt Source。
横纵轴定义：无坐标轴（动物实验示意图）。阅读方向：看两条给药路径分别对应"制造病因（TDP-43 KD）"与"施加治疗（ASO）"。
颜色含义：灰色小鼠躯体；注射器/管路示意给药部位；caption 未注明更多配色。
核心结论：体内"病因+治疗"双给药设计，可在同一动物检验剪接纠错药效。

(H) 脊髓剪接 RT–PCR
图片解释：五泳道（WT−/WT+（TDP-43 KD）/hUNC13A−/hUNC13A+ACSF/hUNC13A+ASO）：WT 两泳道仅 Correct 带（约 150–200 bp，小鼠本底不产生人特异 cryptic）；reporter 未 KD 仅 Correct；reporter+KD+ACSF 出现 Cryptic 带（约 300 bp）且 Correct 变浅；reporter+KD+ASO 的 Cryptic 带明显变浅、Correct 回升。
横纵轴定义：无坐标轴（电泳凝胶）。横向为基因型×处理泳道，纵向为产物长度（bp，100/200/300）。阅读方向：比较 reporter ACSF 与 ASO 泳道 Cryptic 带深浅。
颜色含义：灰度条带，越深=该异构体越多；箭头标 Cryptic/Correct。
核心结论：人源化小鼠在体内复现人特异隐匿剪接，且 ICV ASO 部分纠正之。

(I) 脊髓 Correct PSI 定量
图片解释：WT NT 约 100、WT KD 约 100（NS，小鼠无该事件）、hUNC13A NT 约 100、hUNC13A KD+ACSF 约 75（\*\*\*\*）、hUNC13A KD+ASO 约 95（\*\* vs ACSF）。n=4/3/5/7/9 只；ANOVA+Tukey。
横纵轴定义：X=五条件，Y=Correct PSI（%，0–100）。阅读方向：看 reporter ACSF 凹陷是否被 ASO 拉回。
颜色含义：深灰=WT NT，浅灰=WT KD，紫=reporter NT， magenta 系=reporter KD ACSF / KD ASO（图例区分）。
核心结论：体内 ASO 显著但部分地恢复正确剪接（约 75→约 95 PSI）。

(J) 脊髓 TDP-43 mRNA 定量
图片解释：RT–qPCR：WT NT 100、WT KD 约 50（\*\*\*\*）、reporter NT 约 100、KD+ACSF 约 50、KD+ASO 约 52（\*\*\*\* vs NT）——ASO 不改变 TDP-43 敲低效率，两组病因强度一致。n 同 I。
横纵轴定义：X=五条件，Y=相对 TDP-43 表达（%，0–100+）。阅读方向：确认 ACSF 与 ASO 组 TDP-43 同等下降（内对照）。
颜色含义：同 I。
核心结论：剪接 rescue 差异不是敲低效率差异造成的。

(K) 脊髓 UNC13A 隐匿外显子 RNA 定量
图片解释：cryptic exon 特异 RT–qPCR：WT 两条件与 reporter NT 近 0；reporter KD+ACSF 约 100（\*\*\*\*）；KD+ASO 约 30（\*\* vs ACSF）。n 同 I。
横纵轴定义：X=五条件，Y=UNC13A CE 相对表达（%，0–150）。阅读方向：看 ASO 柱相对 ACSF 柱下降幅度（约 70% 降幅）。
颜色含义：同 I。
核心结论：体内单点 ASO 把隐匿转录本压低约 70%，与 H/I 的 PSI 回升互证。

Section 5 关联 Extended Data（紧凑整合）：ED Fig. 8（a–h，8 panel）——LNA ASO 靶位示意（a）、SK-N-BE(2) 初筛 PSI（b，NT n=3）、SH-SY5Y 剪接凝胶与定量（c,d，n=3）、RNA rescue（e，n=4）、蛋白 rescue（f,g，n=3）、HaloTDP iNeurons RNA rescue（h，n=6）。ED Fig. 9（a–i，9 panel）——18-nt walk 示意（a）、SH-SY5Y 筛 PSI（b）、剪接凝胶与定量（c,d，n=4）、RNA（e，n=8）、蛋白（f,g，n=4）、iNeurons RNA（h，n=6）、以及 amplicon 测序显示参考与风险两等位基因 cryptic 均被压低（i，n=1，等位基因特异性 rescue 的直接证据）。

Section 6：UNC13A ASOs rescue synapse function（UNC13A ASO 恢复突触功能）

**背景补注（方法平台）：为什么用自突触微岛记录诱发释放**

eEPSC 幅度是释放概率 Pr、量子幅度与突触数三者的乘积；常规网络培养中突触前细胞身份与突触数高度异质，难以把"释放"单独分离。自突触（autapse）培养让单个神经元长在约 250 µm 的星形胶质细胞微岛上、轴突回连自身形成突触——突触前与突触后是同一个细胞，一个细胞即一个完整回路，诱发释放的突触前变量被干净隔离。该体系由 Bekkers & Stevens（PNAS 1991，ref 26）在海马培养确立，Meijer 等（Cell Rep 2019，ref 27）与 Fenske 等（Sci Rep 2019，ref 22）将其移植到人 iPS/iN 神经元。本文 UCL 与 FMP 两实验室分别用其记录皮层 iNeurons（10 周成熟）与脊髓 iMNs（DIV60–70）的 eEPSC 与双脉冲比，使 rescue 结论跨细胞类型、跨实验室成立（Fig. 4c,d）。

**背景补注（方法平台）：为什么用 iGluSnFR3 直接测单突触 Pr**

本文已证 TDP-43 缺失同时造成量子幅度与突触密度的 UNC13A 非依赖下降（ED Fig. 7a,c,d），故 eEPSC/mEPSC 变化无法单独归因于 Pr——需要在单突触水平直接"数释放事件"的读出。iGluSnFR3（Aggarwal et al., Nat Methods 2023，ref 28）是第三代基因编码谷氨酸探针，激活动力学与膜定位较前代改进，膜锚定表达后以 ΔF/F0 报告局部谷氨酸释放。本文以 100 Hz 成像、1 Hz 场刺激×45 次，按像素聚类出单突触 ROI，Pr=检出释放次数/45，把释放概率从电生理推断参数变成可直接计数的事件；成像者对处理组盲法，并以 NBQX/AP-V/gabazine 阻断回返活动隔离单突触事件（Fig. 4e、ED Fig. 11a）。

内容逻辑：本节回答转化链条的最后一环：蛋白只回补 30–50% 够不够救功能？作者先给出剂量-功能关系的文献锚点：Unc13a 杂合小鼠与携带杂合 LoF UNC13A 突变的人均存活且神经生理正常（refs 18,25），原代小鼠培养中只有 Unc13a 低于正常约 30% 才出现明确突触缺陷（refs 20,25）——即存在"30% 阈值"，恢复不必到 100%。据此预测 M21-4（约 30% 蛋白）与 M18-17（>50%）都应有效，实验证实：两者均提升 TDP-43 KD iNeurons 的 mEPSC 频率（Fig. 4a,b；n=19/19 与 17/18，\*），而幅度与被动膜特性不受 ASO 影响（ED Fig. 10a–d），再次确认 rescue 的突触前特异性。随后从自发释放推进到生理工作模式——诱发释放：在自突触微岛上记录 eEPSC，覆盖两种 ALS 受累细胞类型（CTIP2+ 皮层 iNeurons 与 Islet-1+/VAChT+ 脊髓 iMNs）、两个实验室、两种 TDP-43 缺失手段（DIV14 PROTAC 与 DIV45 gapmer）：两体系均见 eEPSC 幅度大幅下降且被 UNC13A ASO 部分 rescue（Fig. 4c,d；iNeuron n=11/6/6，\*\* / \*；iMN n=34/30/25，\*\*\*\* / \*\*\*）；iMN 的自发释放表型与 rescue 亦独立复现（ED Fig. 10g–k）。但 eEPSC 幅度是 Pr×量子幅度×突触数的乘积，而前文已证量子幅度与突触密度有 UNC13A 非依赖下降，故作者用 iGluSnFR3 活细胞成像在单突触水平直接分解：TDP-43 KD 既减少活性突触数（ED Fig. 11a：CTRL 约 10、KD 约 4，\*）又降低剩余突触的 Pr（Fig. 4e：CTRL 约 0.16、KD 约 0.08，\*\*\*\*）；ASO 不恢复活性突触数（ED Fig. 11a，与形态学突触密度不 rescue 一致，ED Fig. 7c,d, 11b），但提升剩余突触 Pr——该提升 P=0.052， narrowly missed significance，作者如实标注而不标星。最后网络层面：DIV14 早期 KD 时 M18-17 带来小而显著的同步 rescue（Fig. 4f,g 左，\*）；DIV33 晚期 KD（网络已成熟后缺失，更贴近成人发病）rescue 更大（Fig. 4f,g 右，\*\*\*）；同步性仍是所有 MEA 指标中 rescue 最一致者（ED Fig. 11h）。本节的贡献是完成"单点 ASO→单突触 Pr→自发/诱发释放→网络同步"的全层级功能 rescue，并以 30% 阈值文献与 P=0.052 的诚实标注划定结论边界：rescue 是功能性的、突触前的、剂量上不必满额的，但单突触 Pr 的直接证据仍差一步统计显著性。

→ Figure 4 标题为"UNC13A splice-switching ASOs rescue synapse function following TDP-43 loss"，旨在证明 ASO 在自发释放、诱发释放、单突触 Pr 与网络同步四个层级 rescue 突触功能。由 a 至 g 共 7 部分构成：a–b 自发释放、c–d 两细胞类型诱发释放、e 单突触 Pr、f–g 早/晚 KD 网络同步，形成"从单突触到网络"的功能 rescue 证据链。

(A) M18-17 rescue 自发释放
图片解释：TDP-43 KD iNeurons 给 CTRL ASO（绿）或 M18-17（黄绿）：代表迹线 M18-17 尖峰密度明显回升（标尺 50 pA；水平标尺原文印为"2.5 ms"，与迹线含数十个秒级事件不符，Fig. 1 同类迹线标 2.5 s，疑为原图标尺笔误，解读按秒级窗理解）；平均单事件 10 pA/1 ms 两组幅度相近。频率柱：ASO CTRL 约 0.2 Hz、M18-17 约 0.5 Hz（\*；n=19/19、3 次实验）；累积间隔曲线 M18-17 左移。
横纵轴定义：迹线 X=时间、Y=pA；频率 X=两条件、Y=Hz（0–3）；累积 X=间隔 ms（0–1×10^5）、Y=%。阅读方向：数尖峰密度+看频率柱回升。
颜色含义：绿=ASO CTRL，黄绿=M18-17。
核心结论：蛋白回补 >50% 的 18-nt ASO 显著恢复自发释放频率。

(B) M21-4 rescue 自发释放
图片解释：同 A 读法：MOE CTRL（蓝）迹线稀疏、M21-4（青绿）尖峰回升；频率 ASO CTRL 约 0.15 Hz、M21-4 约 0.4 Hz（\*；n=17/18）；累积曲线左移；平均事件幅度相近。
横纵轴定义：同 A。阅读方向：同 A。
颜色含义：蓝=MOE CTRL，青绿=M21-4。
核心结论：蛋白仅回补约 30% 的 M21-4 也显著 rescue——支持"30% 阈值"转化预测。

(C) 皮层 iNeuron 自突触诱发释放
图片解释：左下为自突触微岛 phase-contrast 图：单个神经元长在约 250 µm 胶质微岛上、轴突回连自身（标尺 100 µm）。上排 eEPSC 迹线：Control（蓝）大 downward 电流（约 −20 nA 级）、TDP-43 KD(PROTAC)（紫）几乎消失、KD+M21-4（青）部分恢复；标尺 2 nA/5 ms。幅度柱：CTRL 约 4 nA、KD 约 0.5（\*\*）、KD+M21-4 约 2（\*）；n=11/6/6、3 次独立分化。原理：自突触上一个 80 mV/1 ms 刺激引发自身轴突动作电位→自身末梢释放→记录到同步多小泡 eEPSC，故幅度直接读"诱发释放总量"。
横纵轴定义：迹线 X=ms、Y=nA；幅度 X=三条件、Y=nA（0–25）。阅读方向：比较三迹线峰值深度与柱高。
颜色含义：蓝=Control，紫=TDP-43 KD，青=KD+M21-4。
核心结论：ASO 部分恢复皮层神经元诱发释放（生理工作模式）。

(D) 脊髓 iMN 自突触诱发释放（第二实验室/第二敲低手段）
图片解释：FMP Berlin 体系：iMN 表达 VGlut1-EGFP 获得谷氨酸释放；gapmer DIV45 敲低 TDP-43。微岛图+迹线：Control（蓝）大 eEPSC、KD(GAPMER)（紫）小、KD+M21-6（青）回升；标尺 2 nA/20 ms。幅度柱：CTRL 约 5 nA、KD 约 1.5（\*\*\*\*）、KD+M21-6 约 3.5（\*\*\*）；n=34/30/25 神经元、3 次独立分化。
横纵轴定义：同 C（时间轴 20 ms 窗）。阅读方向：同 C。
颜色含义：蓝=Control，紫=KD，青=KD+M21-6。
核心结论：rescue 跨细胞类型（运动神经元）、跨实验室、跨敲低手段成立——非单一体系假象。

(E) iGluSnFR3 单突触释放概率
图片解释：左上示意：膜锚定谷氨酸探针（绿色）结合释放的谷氨酸（红点）后荧光增强；左中为表达 iGluSnFR3 的树突代表图，puncta 按 Pr 着色（色标 0–0.8，青=低 Pr→红=高 Pr）；左下为高 Pr（红标）与低 Pr（蓝标）突触的 ΔF/F0 迹线（标尺 0.05/2 s），虚线=1 Hz 场刺激时刻：高 Pr 突触几乎每次刺激都有荧光峰，低 Pr 突触多次刺激才一次。右柱：单突触 Pr=45 次刺激中检出释放的次数/45；CTRL 约 0.16（n=285 突触）、KD 约 0.08（n=71，\*\*\*\*）、KD+M21-4 约 0.14（n=66；vs KD 的 P=0.052，未标星）。成像者盲法；NBQX/AP-V/gabazine 阻断回返活动以隔离单突触事件。
横纵轴定义：迹线 X=时间（s）、Y=ΔF/F0（荧光相对基线变化分数，正比于局部谷氨酸量）；Pr 柱 X=三条件、Y=Pr（0–0.8）。为什么用 Pr 而非 eEPSC 幅度：把"每个突触每次刺激释放的概率"从突触数与量子幅度中分离。阅读方向：迹线数"刺激虚线后有峰"的比例；柱图看 KD 凹陷与 ASO 回升。
颜色含义：puncta 色标青→红=Pr 低→高；迹线标签红=High Pr、蓝=Low Pr；柱蓝=Control、紫=KD、青=KD+21-4。
核心结论：TDP-43 缺失降低单突触 Pr（\*\*\*\*）；ASO 提升剩余突触 Pr 但 P=0.052 边缘显著——机制方向明确、统计一步之遥，如实保留。

(F) 早/晚 KD 时间线与 MEA raster
图片解释：上为时间线：D0 铺板；D14 早期 TDP-43 KD 并开始 ASO 处理（黄字），D28–D49 为早期分析窗（蓝线）；D33 晚期 KD（紫字），D43–D63 为晚期分析窗（紫线）。下为四幅 60 s raster（DIV49 早期 / DIV45 晚期）：CTRL ASO 早期稀疏、M18-17 ASO 早期出现更多粉色网络 burst；晚期 CTRL ASO 散乱、M18-17 恢复部分粉色竖列。
横纵轴定义：时间线 X=天数（D0–D63）；raster X=60 s、Y=电极行。阅读方向：先看时间线确定 KD/给药/分析窗先后，再比较同代 CTRL vs M18-17 raster 的粉色竖列。
颜色含义：蓝=电极 burst，粉=网络 burst；时间线黄=ASO 处理、蓝=早期窗、紫=晚期窗。
核心结论：晚期（网络成熟后）缺失更贴近成人发病，且 ASO 在该窗口 rescue 更明显。

(G) 早/晚 KD 网络同步配对 rescue
图片解释：配对 log2[FC] 连线：早期 CTRL ASO 约 −3.5 至 −4.8 → M18-17 约 −2 至 −4.3（\*）；晚期 CTRL ASO 约 −3.5/−5 → M18-17 约 −2/−3.3（\*\*\*）；n=4 独立实验，线连同板平行分化；虚线 0=对照水平。
横纵轴定义：X=条件（CTRL ASO→M18-17）、Y=网络同步 log2[FC]（−6–0）。阅读方向：看连线上移幅度，晚期大于早期。
颜色含义：绿=CTRL ASO 点、黄绿=M18-17 点（图内两色点连线）。
核心结论：ASO 显著回补网络同步，晚期缺失 rescue 更大（\*\*\*）——支持"成熟网络功能性沉默可被单点纠错唤醒"。

Section 6 关联 Extended Data（紧凑整合）：ED Fig. 10（a–k，11 panel）——iNeuron ASO 后 mEPSC 幅度 ns（a,b）、被动膜特性 ns（c,d）、自突触双脉冲比 PPR ns（e，排除短期可塑性混杂）；iMN 标志物 IF（f：VAChT 品红/Islet-1 黄/VGluT1 绿/Map2 青，标尺 20 µm 与 2 µm inset）；iMN mEPSC 频率 CTRL 约 4.5 Hz、KD 约 1（\*\*\*\*）、KD+M21-6 约 2.5（\*）（g，n=21/31/23）、幅度 ns（h）、代表迹线（i）；iMN Western（j：UNC13A 185 kDa、Vinculin 115、TDP-43 50、Stathmin-2 25）与定量（k，n=3）：UNC13A 在 TDP-43 KD 降至约 0.2、KD+M21-6 回补至约 1.7（\*），而 Stathmin-2 不 rescue（特异性内对照）。ED Fig. 11（a–h，8 panel）——iGluSnFR3 分割流程示意与活性突触数（a：CTRL 约 10、KD 约 4 \*、KD+21-4 约 4 ns；示意改编自 ref 28）、ASO 后树突突触密度 ns（b，n=13/14/13）、早期同步时间 course（c）、晚期 KD raster（d）、晚期同步时间 course+配对 log2FC \*\*（e，n=6/分化×4）、晚期多 MEA 指标（f）、晚期 ASO 同步时间 course（g）、早/晚 ASO 多指标 rescue（h，同步性/AUCC 最一致）。

---

四、<Discussion结构分析>

**第 1 层：总论点——TDP-43 核缺失制造"功能性死亡"，单隐匿外显子是主驱动。** 作者开篇重述：TDP-43 LoF 在人神经元中造成自发与诱发传递的剧烈丢失与网络异步；在数百个隐匿错剪接中，UNC13A 内含子 20 单外显子被证明是突触崩溃的主驱动（Fig. 2 的 80% 频率 rescue 与 Fig. 4 的多层级 ASO rescue 为支撑）。态度标注：已证实（就本文体外体系而言）。与领域关系：把 refs 3–8,29 描述的"广泛错剪接图谱"从相关性推进到单事件因果权重排序。

**第 2 层：遗传学锚定——为什么是 UNC13A 而不是别的错剪接基因。** 该隐匿外显子所在内含子携带 ALS/FTLD-TDP 第二强 GWAS 信号（refs 14–16,30–32）；风险 SNP 纯合携带者中位生存期缩短 5–12 个月（refs 15,16,33–36）。作者据此论证"靶向该事件修饰疾病进程"有人群证据支撑。态度：遗传关联为已证实的人群事实，"修饰进程"的功能因果由本文体外因果实验补强；作者未声称本文证明了临床进程修饰。

**第 3 层：UNC13A priming 生物学与 30% 阈值——rescue 不必满额。** 引用 Unc13a-null 小鼠出生即呼吸衰竭死亡、原代培养发育正常但兴奋性传递剧降（refs 18–20），以及杂合小鼠/杂合 LoF 人无神经生理异常（refs 18,25）、蛋白低于约 30% 才出现强突触缺陷（refs 20,25）。本文据此把"恢复 ≥30% 蛋白即可能有益"作为转化预测，并通过 M21-4（约 30%）与 M18-17（>50%）均 rescue 予以支持（Fig. 4a,b）。态度：阈值来自前人小鼠/人遗传学（已证实于其体系），本文在人神经元中给出一致性证据但非完整剂量-反应曲线（推测性外推到患者剂量）。

**第 4 层：单事件解释的边界——UNC13A 非依赖成分被如实保留。** mEPSC 幅度下降不被直接 UNC13A 敲低复现、也不被 CE DEL rescue；突触密度下降 likewise（ED Fig. 7a,c,d）。作者明确把这些归因于其他错剪接转录本（postsynaptic 定位或突触周转相关，ref 40），并指出尽管密度下降，剩余突触的功能恢复仍稳健。态度：承认不确定性+已证实的负性结果并存；这一层防止把 UNC13A 夸大为 TDP-43 突触表型的唯一解释。

**第 5 层：患者相关性与模型保真度。** 患者神经元 UNC13A 蛋白数据不可得；但 FANS 分选死后皮层核的转录组显示，缺核 TDP-43 的细胞群中 >90% 的 UNC13A 转录本含隐匿外显子（refs 6,41），支持"iPS 模型中近完全 UNC13A 丢失"的疾病相关性。作者同时自陈：未来需要同时复现核缺失与胞质聚集的模型。态度：转录组证据为已发表事实，蛋白层面为预测（推测）。

**第 6 层：沉默 vs 超兴奋悖论——电路级推测。** 临床 TMS 见 ALS 早期皮层超兴奋且随进展加重、与差生存相关（refs 42,43）；而 UNC13A 丢失造成突触沉默。作者列举双等位 UNC13A 突变致癫痫/肌无力/皮层超兴奋个案（refs 25,44,45）及 STX1B/STXBP1/SNAP25B 等突触前 LoF 致超兴奋的先例（refs 46–48），提出"兴奋性输出下降→前馈抑制减弱→E/I 比偏移"的电路解释（ref 49）。态度：明确推测（speculative）；本文纯兴奋性培养只能表现失同步而非超兴奋，作者自陈需引入抑制性中间神经元、并提议 hUNC13A 小鼠作体内网络平台。

**第 7 层：均质 vs 马赛克缺失的外推边界（作者自陈）。** 本文所有神经元均质丢失 TDP-43，比患者马赛克模式更极端；作者推测在 postsynaptic 神经元未受累的连接中，突触前 rescue 可能足以恢复信号，但需更复杂模型验证。态度：推测+自陈局限。

**第 8 层：治疗定位——splice-switching 的"恢复生理剂量"优势与功能死亡窗口。** 以 SMA nusinersen 为先例（refs 23,50），指出剪接纠正 ASO 恢复生理转录本水平、无过表达风险；结合 GWAS 进程修饰证据（ref 15），把 UNC13A 列为剪接修饰治疗的关键候选。收束概念：TDP-43 相关退行存在"神经元先失去有意义突触通讯能力、后死亡"的阶段，这群结构完好的神经元构成可被单点 ASO 唤醒的治疗池。态度：转化愿景（推测性但机制锚定）。

**作者自陈局限（汇总层）：** (i) 纯兴奋性培养、无抑制性中间神经元，无法评估超兴奋/E-I 动态；(ii) 均质 TDP-43 缺失 vs 患者马赛克；(iii) 模型只有核缺失、无胞质聚集；(iv) 单突触 Pr rescue P=0.052 仅为趋势；(v) 患者 UNC13A 蛋白数据缺失、仅转录组间接支持。

**Discussion 没有讨论什么（局限性）：**

(1) 体内只有剪接分子药效、无功能/行为/生存 rescue：hUNC13A 小鼠仅读脊髓 RT–PCR/qPCR（Fig. 3h–k），未做体内电生理、运动行为或生存曲线——因此"ASO 能恢复体内回路功能"仍是外推，转化链条在动物功能层断开。
(2) 无患者来源神经元验证：全部功能实验用健康 WTC11（杂合风险 SNP）与肿瘤系；未用 sporadic ALS/FTD 患者 iPS 神经元检验 rescue 幅度是否保守——患者背景（遗传/表观/老化）可能改变阈值与药效。
(3) 单突触 Pr 的"最后一公里"未闭环：Pr rescue P=0.052，且未直接测量 primed 小泡池（如蔗糖释放池、电镜 docked/primed 小泡计数）——"UNC13A 回补→priming 恢复"仍是功能推断而非结构/生化直接证据。
(4) ASO 体内剂量-分布-时程未优化：单次 ICV 30 mg/ml×10 µl、3 周终点；未给慢性给药、脊髓/皮层分布定量、剂量-PSI 反应曲线——临床给药方案无从推导。
(5) 30% 阈值的人源剂量-反应未测：阈值引自小鼠（refs 20,25），本文只测了两个 rescue 水平（约 30% 与 >50%）均有效，未做人神经元蛋白剂量梯度——"≥30% 即有益"在人体系是插值推测。
(6) UNC13A 非依赖的幅度/密度下降机制未追：未鉴定驱动 postsynaptic 量子幅度与突触丢失的具体错剪接转录本（仅指向 ref 40 方向）——联合治疗是否需要第二个靶点未知。
(7) ASO 转录组 off-target 未谱析：仅按序列驱动 off-target 与二级结构预筛（Methods），未做 RNA-seq 级全转录本剪接 off-target 谱——长期安全性与隐匿外显子组-wide 影响未评估。
(8) 超兴奋悖论无实验检验：E/I 偏移假说（ref 49）纯推测，本文体系无法证伪——临床最相关的早期超兴奋表型与本文沉默表型的关系悬置。

---

五、<重点思考>

**（一）核心概念/方法/通路/模型概括解读：**

- **核心概念——"功能性死亡"（predegenerative synaptic silencing）：** 内涵：神经元结构完好、存活正常，但自发/诱发释放与网络同步崩溃，先于细胞死亡失去回路贡献能力。重要性：把治疗窗口从"阻止死亡"前移到"唤醒沉默神经元"。本文推进：以存活计数（ED Fig. 7h）、突触结构保留（ED Fig. 7c,d 密度下降但 puncta 仍在、Fig. 1g synapsin 保留）与功能崩溃（Fig. 1i–m）三者并置确立该状态，并证明其可被单点纠错逆转。边界：体外均质缺失体系，患者马赛克背景下该状态的比例与可逆性未知。
- **核心概念——隐匿外显子作为"单事件治疗节点"：** 内涵：数百个 TDP-43 依赖性错剪接中，个别事件因蛋白剂量-功能阈值而占超比例权重。重要性：为"广谱调控因子缺失"类疾病提供"抓主节点"的治疗哲学。本文推进：CE DEL 的 80% 频率 rescue + ASO 复现，把 UNC13A 从 GWAS 关联位点升级为功能因果节点。边界：幅度/密度成分不被解释，节点非唯一。
- **核心方法——HaloTag-PROTAC 成熟期急性蛋白降解：** 内涵：内源敲入 HaloTag 后用双功能分子招募 E3 降解目标蛋白。重要性：避开发育必需基因的早期敲除混杂，实现"成熟后急性缺失"。本文推进：30 nM、10 天 <5% 残留的剂量/时程标定，及 MG132/MLN4924 机制验证。边界：标签本身轻度损功能（ED Fig. 1i），需 CRISPRi 互证。
- **核心方法——基因组隐匿外显子删除作为因果刀：** 内涵：纯合删除 233 nt（双受体+共用供体）使隐匿剪接"无序列可用"。重要性：在调控因子仍缺失背景下单独摘除一个剪接变量，是单事件充分性的最干净检验。本文推进：SH-SY5Y→iPS→双编辑 iNeurons 三级递进+STMN2 不 rescue 的特异性内对照。边界：删除为组成型，不能模拟"病程中给药"的时间维度（由 ASO 补）。
- **核心方法——splice-switching MOE ASO 三代优化：** 内涵：LNA 21-nt 初筛→全 MOE 21-nt（耐受性）→18-nt MOE walk（效力），占位隐匿供体位点切换剪接。重要性：不改基因组、恢复生理剂量、可 ICV 给药。本文推进：剪接 >90%、蛋白 30–50%→>50%、两等位基因均纠错、体内部分 rescue。边界：体内仅分子药效；18-nt 优于 21-nt 的结构/化学 rationale 未解释（经验 walk）。
- **核心方法——iGluSnFR3 单突触 Pr 活细胞成像：** 内涵：膜锚定谷氨酸探针+100 Hz 成像+45 次 1 Hz 场刺激，按像素聚类单突触 ROI 数释放次数算 Pr。重要性：把 eEPSC 幅度分解为 Pr×量子×突触数，定位缺陷到单突触释放机器。本文推进：盲法成像+自定义 MATLAB 管线，证明 KD 降 Pr、ASO 升 Pr（P=0.052）。边界：Pr rescue 边缘显著；活性突触数不 rescue。
- **核心模型——hUNC13A reporter 小鼠：** 内涵：小鼠内含子 20 替换为含风险 SNP 的人源内含子，使小鼠复现人特异隐匿剪接。重要性：体内药效学必需（小鼠本底无该事件）。本文推进：AAV-miR-Tardbp+ICV ASO 双给药证明体内单点纠错可行。边界：所用系为串联重复异常靶向系（骨架落入内含子 23，作者自陈但剪接正确）；仅分子读出。
- **核心通路——TDP-43→UNC13A 剪接→priming→释放→同步轴：** 内涵：核 TDP-43 抑制隐匿外显子→正常 UNC13A mRNA/蛋白→活性区 priming→单小泡与诱发释放→网络同步。重要性：把 RNA 调控、突触生理、网络功能串成可干预因果链。本文推进：逐层缺失表型+逐层单点回补闭环。边界：priming 步骤为功能推断（无直接 primed 池测量）。

**（二）本篇文章发现的完整概括：**

本文从"约 97% 的 ALS 与约 50% 的 FTD 存在 TDP-43 核缺失、但无直接靶向疗法"这一临床缺口出发，先在人 iPS 来源成熟神经元中用 HaloTag-PROTAC 急性降解 TDP-43，证明核缺失在数天内耗竭突触前 UNC13A（10 天残留 <5%），并使神经元进入结构完好、存活正常却自发/诱发释放与网络同步崩溃的"功能性死亡"状态；膜片钳与 MEA 显示该表型与直接 UNC13A 敲低高度镜像。继而用 233 nt 纯合删除把 UNC13A 内含子 20 隐匿外显子从数百个错剪接事件中单独摘除，发现仅修这一个事件即恢复约 80% 的 mEPSC 频率与网络同步，而 STMN2 加尾、mEPSC 幅度残余下降与突触密度下降不被 rescue——确立单事件为主驱动、并诚实划出其解释边界。在此基础上开发三代 splice-switching ASO（LNA 21-nt→MOE 21-nt→18-nt MOE walk），以 1 µM 自由摄取把剪接恢复 >90%、蛋白恢复 30–50% 至 >50%，并在含风险 SNP 的人源化小鼠脊髓中实现体内部分剪接纠错；功能层面，ASO 在皮层 iNeurons 与脊髓 iMNs 两细胞类型、两实验室、两种敲低手段下恢复自发与诱发释放，单突触成像显示剩余突触 Pr 回升（P=0.052），成熟后缺失的网络同步 rescue 更大（\*\*\*）。结合"UNC13A 低于约 30% 才失效"的剂量阈值文献，本文提出恢复 ≥30% 蛋白即可能有益的治疗预测。本文的领域贡献在于：其一，把 TDP-43 蛋白病的突触表型从"广泛错剪接的相关性"推进到"单隐匿外显子的因果充分性"，提出并验证"功能性死亡"这一可逆前退化阶段；其二，提供遗传学锚定（GWAS+生存修饰）、机制定义（priming-释放-同步轴）、 genetically validated 的剪接纠错治疗范式，覆盖绝大多数 ALS/FTD 患者；其三，交付可推进的化合物（M21-4/M18-17）与人源化体内药效模型。同时以坦率态度划定边界：体内仅分子药效、Pr rescue 边缘显著、幅度/密度成分 UNC13A 非依赖、均质缺失与纯兴奋性培养外推受限。

**1. 研究问题定位：** 交叉位置：RNA 生物学（剪接调控）× 突触生理学（释放机器/网络动态）× 转化核酸药物（ASO 化学与给药）。问题层级：分子机制（单事件因果）+ 细胞/回路功能（多层级 rescue）+ 临床前转化（化合物+人源化小鼠），非临床层级。工作类型：概念创新（功能性死亡/单事件节点）+ 机制创新（因果刀设计）+ 转化型（ASO 优化与体内药效）三者兼具。实验层级：人 iPS 神经元/肿瘤系体外 + 小鼠体内分子药效；无患者组织功能实验、无行为学。一句话核心定位：给"TDP-43 核缺失如何杀死突触功能"这一长期悬置问题补上单事件因果一环，并把它直接转化为可给药的剪接纠错策略。

**2. 为什么能发 Nature（证据链评估）：** 最扎实处有三：其一，因果刀的干净性——233 nt 纯合删除同时移除双受体+共用供体，在 TDP-43 仍缺失背景下做 rescue，且以 STMN2 不 rescue 作事件特异性内对照（Fig. 2、ED Fig. 5），把"单事件充分性"从相关性中彻底解耦；其二，功能 rescue 的多体系收敛——皮层 iNeurons 与脊髓 iMNs、UCL 与 FMP 两实验室、PROTAC 与 gapmer 两种敲低、自发/诱发/单突触/网络四层级读出同向（Fig. 4、ED Fig. 10–11），排除单体系/单手段假象；其三，遗传-机制-转化三重锚定——GWAS 第二强信号+生存修饰（refs 14–16,33–36）、30% 剂量阈值（refs 20,25）、人源化小鼠体内药效（Fig. 3g–k）使治疗主张不悬空。不足在于：体内止于剪接分子读出、无功能/行为 rescue；单突触 Pr rescue P=0.052 未过显著门槛；无患者来源神经元；均质缺失+纯兴奋性培养限制对临床超兴奋/马赛克背景的外推；hUNC13A 系为异常靶向系（作者自陈）。非预印本（Nature 已接收在刊），故无预印本形态原因分析之需。

**3. 创新点逐条列出：**
- [概念创新] "功能性死亡"前退化阶段：结构完好/存活正常但突触通讯崩溃且可逆（Fig. 1g–m、ED Fig. 7h）。
- [机制创新] 单隐匿外显子因果充分性：233 nt 删除在 TDP-43 缺失背景下 rescue 80% 频率与网络同步（Fig. 2i–l）。
- [方法创新] HaloTDP+CE DEL 双编辑 iPS 系：把"急性调控因子缺失"与"单事件已修"组合在同一人神经元基因组（Fig. 1a、Fig. 2a、ED Fig. 6）。
- [方法创新] 18-nt MOE ASO walk 把蛋白 rescue 推过 50%（M18-17），并验证两等位基因纠错（Fig. 3e,f、ED Fig. 9i）。
- [模型创新] hUNC13A reporter 小鼠+AAV-miR-Tardbp/ICV ASO 双给药体内剪接药效平台（Fig. 3g–k）。
- [转化/调和性贡献] 以 30% 阈值文献调和"部分蛋白 rescue 是否够"的疑问，给出 ≥30% 即可能有益的剂量预测（Fig. 4a,b）；并讨论沉默 vs 超兴奋悖论的电路解释（Discussion）。

**4. 前置依赖：** 技术前置：HaloPROTAC 降解平台（ref 21）；CRISPRi 人 iPS 神经元平台与 WTC11 系（ref 51）；NGN2 定向分化（refs 52,53）；自突触微岛（refs 26,27,22）；iGluSnFR3 探针（ref 28）；MEA 与 Neural Metric Tool；ASO 剪接纠正先例（refs 23,24,50）；HDR bridging oligo 编辑（ref 60）。生物学概念前置：TDP-43 隐匿剪接图谱（refs 3–8,29）；UNC13A 隐匿外显子+风险 SNP 机制（refs 6,7，直接地基）；Munc13 priming 与剂量阈值（refs 17–20,25）；UNC13A GWAS/生存修饰（refs 14–16,30–36）。生信/统计前置：Minimap2（ref 62）、SAMtools（ref 63）、IGV（ref 64）、fastp（ref 65）、bwa-mem2（ref 66）、CNVkit（ref 67）、Cas-OFFinder（ref 68）、Fiji（ref 69）、NeuronJ（ref 71）、lme4/lmerTest/glmmTMB（refs 72–74）、ΔΔCt（ref 61）。

**5. 基因编辑/遗传操作细节：** (1) Cas12 HaloTag 敲入：crRNA GGAAAAGTAAAAGATGTCTGAAT + 10 µg HDR 模板（M. Ward 惠赠）+ 20 µg 重组 Cas12，Lonza 4D CA-137 电转，HaloTag-TMR 配体筛选阳性克隆；设计价值：内源双等位标签避免过表达假象、成熟期才降解避开发育混杂。(2) Cas9 233 nt CE 删除：双 sgRNA（受体上游 45 bp / 供体下游 10 bp）+ 含简并碱基 B/D 的 bridging oligo HDR 模板，250 pmol sgRNA+20 µg Cas9+1 pmol 模板；设计价值：纯合删除双受体+共用供体使隐匿剪接无序列可用，单变量因果；简并碱基兼容两等位基因。(3) CE DEL 系上二次 Cas12 HaloTag 敲入（ED Fig. 6）：组合"病因可诱导+单事件已修"。(4) CRISPRi：sgCTRL/sgTARDBP/sgUNC13A（pU6-sgRNA EF1α-puro-T2A-BFP，Addgene 60955）慢病毒；设计价值：无切割、无标签的独立敲低互证。(5) 小鼠 ES 靶向：817/1462 bp 同源臂替换内含子 20（含 rs12973192 G/rs12608932 C），双 Cas9 pX459 + puro 筛选；实际系为串联重复异常靶向（骨架入内含子 23）但人源内含子位置/剪接正确——作者如实披露，设计价值与保真度边界并存。所有编辑系均做 amplicon 测序+低深度 WGS CNV+off-target PCR/测序质控。

**6. 与课题组/领域的关联：** 通讯谱系（PDF 内可锚定）：Fratta（UCL MND Centre）主线为 TDP-43/UNC13A 遗传与 RNA 机制——本文直接地基前作为 Brown et al. Nature 2022（ref 6）与 Ma et al. Nature 2022（ref 7）：二者确立"TDP-43 抑制 UNC13A 隐匿外显子、风险 SNP 在 TDP-43 缺失后加剧 inclusion 致转录本/蛋白丢失"，本文是该轴的功能因果+治疗学延伸（"第 2/3 步"）；Burrone（KCL）主线为突触释放与成像生理（自突触/iGluSnFR3 管线，本文 Fig. 4c–e 的方法来源）；Lipstein（FMP Berlin）主线为 Munc13 priming 与 UNC13A 人类遗传学（ref 25 为其相关前作），提供 iMN 第二体系；Schiavo/Isaacs/Fisher 等提供 UCL 神经退行与核酸治疗支撑。方法学平行前作：Baughn et al. Science 2023（ref 24）STMN2 隐匿剪接-加尾的 ASO 纠正——本文把同一策略移植到 UNC13A 并加上遗传因果锚定。本文补上机制的旧观察：UNC13A 自 2009 年 GWAS（ref 14）起"知其关联不知其所以然"，2022 双 Nature 补剪接机制，本文补突触功能因果与治疗可行性。产业关联（PDF 内）：Trace Neuroscience 资助/持股/专利（US 12,522,826 B2、EP 4 444 321 A1），化合物与 AAV 来自该公司——转化路径已公司化。对用户研究方向的参考：若读者方向为表观遗传/染色质剂量调控，本文提供"非编码剪接事件→蛋白剂量阈值→回路功能"的因果链范式与"单点纠错 rescue 剂量-功能"的定量思路，可类比于表观等位基因剂量补偿问题；若方向为神经退行/RNA 治疗，本文是 ASO 剪接纠错从靶点因果到体内药效的完整模板。详细作者履历/并行竞争等 PDF 外事实详见同源背景解读。

**7. 数据与材料可及性：** 测序/组学：原文未提供 GEO/公共 accession（Reporting Summary 明确无 Omics 数据集）；原始数据以 source data 随文提供。代码：GitHub jburrone/Keuss-Harley-Ryadnov-Jackson-et-al.-Nature-2026（电生理 MATLAB+突触密度 Fiji 宏）、f-hamidlab/iGluSNFR3（publication_branch）、Delayed-Gitification/QIAxcelR（v0.1）、peteharley95/Log1pGaussianLMM。材料：shTARDBP SH-SY5Y/SK-N-BE(2)、CE DEL SH-SY5Y/iPS、HaloTag-TDP-43 iPS 系经 UCL MTA 向 P.F. 获取；TDP-43 microRNA rAAV 经 Trace Neuroscience MTA；hUNC13A 小鼠经 Francis Crick Institute MTA。试剂：ASO 序列在 Supplementary Table 2（未提供）；抗体清单见 Reporting Summary（如 Munc13-1 WB Synaptic Systems 126103、IF 126104；TDP-43 WB Proteintech 10782-2-AP、IF Abcam ab104223）；iGluSnFR3 质粒 Addgene 178333（K. Podgorski 惠赠）。补充材料状态：Supplementary Fig. 1–10 与 Table 1–7 未随本 PDF 提供；Extended Data Fig. 1–11 与 Reporting Summary 随 PDF 提供。

**（三）面向阅读的核心提问（问题 seeding）：**

- **问题 1：UNC13A 单事件是"主驱动"还是"最大贡献者"？剩余约 20% 频率缺口与幅度/密度下降归谁？** 本文能答到：80% 频率 rescue+STMN2/幅度/密度不 rescue 划出边界，但未鉴定其余驱动转录本（仅指向 ref 40）。证据强度：中-强（因果充分性已证，权重分解未完成）。交接：→ 待背景解读跨文献精研（ref 40 及突触错剪接图谱）。
- **问题 2：Pr rescue P=0.052 是真实效应还是 power 不足？priming 恢复有无直接证据？** 本文能答到：n=66 突触的趋势+方向与 eEPSC/mEPSC rescue 一致；无 primed 池直接测量。证据强度：弱-中。交接：→ 待背景解读（Munc13 priming 生化/电镜文献）与后续实验。
- **问题 3：≥30% 蛋白阈值能否外推到患者给药剂量？** 本文能答到：两个 rescue 水平均有效+小鼠/人杂合正常文献；无人源剂量梯度、无患者细胞。证据强度：中。交接：→ 待背景解读（refs 20,25 剂量-反应与临床 ASO 剂量学）。
- **问题 4：突触沉默如何与临床皮层超兴奋共存？** 本文能答到：仅提出 E/I 偏移假说与突触前 LoF 致超兴奋先例；纯兴奋性培养无法检验。证据强度：弱（推测）。交接：→ 待背景解读（refs 42–49 电路文献）。
- **问题 5：hUNC13A 串联重复异常靶向系是否影响药效解读？体内部分 rescue 的缺口是剂量还是模型？** 本文能答到：作者自陈剪接正确、PSI 75→95；未给分布/剂量曲线。证据强度：中。交接：→ 待背景解读（小鼠系表征与 ASO CNS 分布文献）。
- **问题 6：18-nt MOE 为何优于 21-nt（蛋白 >50% vs 30–50%）？化学/结构 rationale 是什么？** 本文能答到：经验 walk 结果+off-target/二级结构预筛；无结合动力学/结构解释。证据强度：中（经验性）。交接：→ 待背景解读（ASO 化学-亲和力-剪接切换效率文献）。

以上问题中，纯本文可答的已全部就地作答，其余转入同源《背景解读》做跨文献证据综合与分级。

**（四）延伸文献与图引清单：**

读完本文后，组会/PPT 与继续研究最需要回补的是"UNC13A 隐匿外显子机制的地基双 Nature"、"Munc13 priming 与剂量阈值的电生理经典"、"splice-switching ASO 的方法与临床先例"、以及本文三个关键平台（HaloPROTAC、iGluSnFR3、自突触）的原始方法论文。下表分 A（论证依赖）/B（方法来源）两类，★为必读；前人 Figure 编号凡未能在本文 PDF 内锚定者一律标"编号待核"，不编造。

| 序号 | 文献(年/刊/本文ref) | 对应本文Fig/论点 | 重点前人Fig(panel) | 一句话讲点 | 获取/阅读深度 |
| --- | --- | --- | --- | --- | --- |
| A1 ★ | Brown et al., Nature 2022（ref 6） | Fig. 1c–f、Fig. 2、Fig. 3 的立论地基；风险 SNP 加剧 inclusion | 建议摘其 UNC13A 隐匿外显子鉴定与风险 SNP 加剧剪接/蛋白丢失图（编号待核） | TDP-43 缺失与 ALS 风险 SNP 共同驱动 UNC13A 隐匿剪接与转录本耗竭 | Nature（OA/订阅状态待核）；全文精读 |
| A2 ★ | Ma et al., Nature 2022（ref 7） | 同 A1 的并行独立证据；TDP-43 直接抑制该外显子 | 建议摘其 TDP-43 结合 UNC13A 内含子并抑制 cryptic inclusion 图（编号待核） | TDP-43 直接 repression UNC13A 隐匿外显子，是 FTD–ALS 基因的关键 RNA 调控节点 | Nature（OA/订阅状态待核）；全文精读 |
| A3 ★ | Augustin et al., Nature 1999（ref 18；并 Varoqueaux 2002 ref 19） | Fig. 1i–j、Fig. 4 的功能基线；~90% 传递丢失 | 建议摘其 Munc13-1 null 小鼠谷氨酸能传递近乎 abolishment 的电生理图（编号待核） | 没有 Munc13-1，小泡无法 priming，兴奋性传递几乎归零而突触结构正常 | 订阅（Nature/PNAS）；全文或关键图精读 |
| A4 | Zarebidaki et al., J Neurosci 2020（ref 20；并 Asadollahi Nat Genet 2025 ref 25） | Fig. 4a,b 的 30% 阈值与杂合正常 | 建议摘其 Unc13a 剂量梯度-传递曲线与杂合表型图（编号待核） | 突触失效只在 UNC13A 低于约 30% 时出现——定义"rescue 不必满额"的治疗阈值 | OA（J Neurosci）/订阅（Nat Genet）；关键图+结论 |
| A5 ★ | Baughn et al., Science 2023（ref 24） | Fig. 3 ASO 策略的直接方法学前作 | 建议摘其 STMN2 隐匿剪接-加尾机制与 ASO 纠正图（编号待核） | splice-switching ASO 已经能在 TDP-43 缺失背景下纠正隐匿事件——本文策略的同族先例 | 订阅（Science）；全文精读 |
| A6 | van Rheenen et al., Nat Genet 2021（ref 16；并 van Es 2009 ref 14、Diekstra 2012 ref 15） | Discussion 遗传锚定；第二强 GWAS 信号+生存修饰 | 建议摘其 UNC13A 位点关联信号与生存修饰图（编号待核） | UNC13A 是 ALS 第二强 GWAS 位点且修饰生存——单点治疗的人群证据 | 订阅/OA 待核；摘要+关键图 |
| B1 ★ | Tovell et al., ACS Chem Biol 2019（ref 21） | Fig. 1a–f 的 HaloPROTAC 平台 | 建议摘其 HaloPROTAC-E 剂量/时间降解曲线与可逆性图（编号待核） | HaloTag-PROTAC 让成熟神经元内源蛋白急性、可逆、剂量可控地消失 | OA（ACS Chem Biol）；方法+关键图 |
| B2 ★ | Aggarwal et al., Nat Methods 2023（ref 28） | Fig. 4e、ED Fig. 11a 的 iGluSnFR3 平台（ED11a 改编自该文） | 建议摘其探针动力学改进与单突触释放成像图（编号待核） | 第三代谷氨酸探针把"单突触释放概率"变成活细胞可数的事件 | OA（Nat Methods）；方法+关键图 |
| B3 | Meijer et al., Cell Rep 2019（ref 27；并 Bekkers & Stevens PNAS 1991 ref 26） | Fig. 4c–d 自突触微岛平台 | 建议摘其人 iN 自突触微岛构建与诱发释放验证图（编号待核） | 单神经元自突触把诱发释放的突触前变量隔离到一个人源细胞上 | OA（Cell Rep）/订阅（PNAS）；方法精读 |
| B4 | Rigo et al., J Cell Biol 2012（ref 23；并 Finkel NEJM 2017 ref 50） | Discussion 治疗定位；SMN2 剪接纠正临床先例 | 建议摘其 nusinersen 纠正 SMN2 exon 7 与临床运动功能改善图（编号待核） | 剪接切换 ASO 已在 SMA 临床验证——UNC13A ASO 的监管与给药路径参照 | OA（JCB）/订阅（NEJM）；综述+关键临床图 |

---

**解读完成度声明：** 主文 Fig. 1–4 全部 panel（共 43 个 panel：Fig. 1 = 13（a–m）、Fig. 2 = 12（a–l）、Fig. 3 = 11（a–k）、Fig. 4 = 7（a–g））均已按四字段模板（图片解释/横纵轴定义/颜色含义/核心结论）解读，并通过"技术零基础自足性"自检：膜片钳/mEPSC/eEPSC、MEA raster 与同步性、iGluSnFR3 单突触 Pr、RT–PCR 凝胶、RT–qPCR、Western、免疫荧光、ASO 占位原理等均从零交代信号来源、物理量、轴换算与读图方向、逐通道配色。Extended Data Fig. 1–11（共 84 个 panel：ED1=9、ED2=8、ED3=8、ED4=7、ED5=11、ED6=5、ED7=8、ED8=8、ED9=9、ED10=11、ED11=8）随主文在同一 PDF 内，已按内容角色以紧凑整合方式逐图说明并嵌入对应 Section（质控/互证/特异性边界/第二体系/平台流程），未逐 panel 展开四字段。Supplementary Fig. 1–10（未裁剪凝胶）与 Supplementary Table 1–7 未随本 PDF 提供，一律标"未提供"，仅按主文 caption 指引注明其角色；Reporting Summary 随 PDF 提供并已纳入统计/盲法/样本量声明。图表视觉细节以 110–140 DPI 渲染目视核对（Fig. 4a,b 标尺另做 300 DPI 局部放大）；灰度条带强弱以原文定量 panel 为准、未自行重测；凡原文未提供定量数值处（如部分代表性凝胶/IF）已如实标注。诚实保留的弱效应/负性结果：Fig. 1l 配对 P=0.0508（未标星）、Fig. 4e Pr rescue P=0.052（未标星）、ED Fig. 3f 放电率 P=0.0687、mEPSC 幅度残余约 10% 下降与突触密度不 rescue、体内"partially rescued"、HaloTag 轻度功能代价、hUNC13A 系串联重复异常靶向。原图疑点如实标注：Fig. 4a,b 代表迹线水平标尺印为"2.5 ms"，与秒级事件窗不符（Fig. 1 同类标 2.5 s），疑原图笔误。公式/算法处理：ΔΔCt、PSI、Pr=事件数/45、LMM/配对比率 t 等均已融入"核心问题与方案"与相应 panel，不设独立算法模块。出版状态：Nature 已接收在刊 Article（非预印本），Received 18 June 2024 / Accepted 6 October 2026，首页 Published online 为占位符"xx xx xxxx"，在线日期以期刊页核证为准（任务提供 2026-11-11）；DOI 10.1038/s41586-026-11256-2。延伸文献与图引清单已附（10 条，分 A/B 两类，★标必读；前人图号未核实处均标"编号待核"，未编造）。背景补注（v6.4修订）：新增 9 处课本化背景补注（模块二 3 处：TDP-43 蛋白病、ALS/FTD、隐匿剪接先例；Section 1 两处平台：HaloPROTAC、NGN2 iNeuron；Section 2 一处：UNC13A/Munc13-1 priming；Section 5 一处：ASO 范式；Section 6 两处平台：自突触微岛、iGluSnFR3），均为增补、未删改原有内容；外部事实标阅读深度，未引入新数据/图号，原有"编号待核"维持；另将原文遗留的 4 处未转义统计星号补转义为 \*（仅格式修正，内容不变）。