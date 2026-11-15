# 《Multimodal single-cell epigenomic and 3D genome atlas of the human basal ganglia》文献解读

**文献信息：** Ding W, Klein A, Báez-Becerra CT, Rink JA, Bartlett A, Wang R, …… Ren B, Behrens MM, Ecker JR. Multimodal single-cell epigenomic and 3D genome atlas of the human basal ganglia. Cell, 189, 7386–7405（2026 年 11 月 12 日出版）。DOI: 10.1016/j.cell.2026.10.019。第一署名作者 Wubin Ding 与 Amit Klein 脚注标注等贡献（原文仅写这两位 contributed equally，不升格为共同一作）；通讯作者 Behrens 与 Ecker，后者为 lead contact。主要单位为 Salk 研究所、UCSD、Allen Institute 等 BICAN 联盟成员。

**一句话概括：** 本文不是又一份表达图谱，而是把人类基底神经节八个亚区的单细胞 DNA 甲基化（261,331 核）与单细胞 3D 基因组构象（229,286 核）铺成同一坐标系的调控层图谱：鉴定数百万个细胞类型特异差异甲基化区域（DMR），刻画 POU6F2+ STR D2 SMYD2-HTR7 投射神经元亚型，把 DMR 中的转录因子 motif 与 ABC 模型预测的增强子-启动子连接组装成细胞类型特异基因调控网络（GRN）并在帕金森病（PD）相关 SNCA 位点提名候选调控机制，最后用 MERFISH 与跨物种 Patch-seq 揭示 matrix–striosome 边界两侧快放电中间神经元的分子与电生理差异，为 PD、亨廷顿病等疾病的细胞类型易感性提供检索框架。

**解读说明：** 本解读基于正式发表版 PDF 全文（SUMMARY、INTRODUCTION、RESULTS 六小节、DISCUSSION 含独立 Limitations 小节、STAR★METHODS、147 条 REFERENCES）完成；主文 Fig. 1–6（共 68 个 panel：Fig.1 共 7 个、Fig.2 共 11 个、Fig.3 共 10 个、Fig.4 共 15 个、Fig.5 共 10 个、Fig.6 共 15 个）逐 panel 四字段解读并嵌入逐节精读。所给 36 页 PDF 的主文图版在第 4、6、8、10、12、14 页（已逐页实读），第 25 页起为 STAR Methods 文本，即该 PDF 未随附补充图 S1–S11 图版页，S 图按正文与 caption 中的角色整合，不做视觉核对。定量数据全部以 paper.txt 原文为准；图上读出的近似值标注"读自图"，原文未提供者如实说明。

---

## 一、<基础概念注释>

### （一）BG 解剖与神经元类型

1. **基底神经节（Basal Ganglia, BG，基底核）：** 深部皮层下核团群，含纹状体（STR：尾状核 Ca、壳核 Pu、伏隔核 NAC）、苍白球外/内段（GPe/GPi）、底丘脑核（STH）与黑质（SN），主导运动控制与行动-奖赏处理，功能障碍对应 PD、成瘾、亨廷顿病等（Introduction 第 1 段，ref3–8）。本文对其八个亚区做全细胞类型普查（Fig. 1A）。
2. **纹状体（Striatum, STR）：** BG 输入节点（ref10）。本文按 CaH/CaB/CaT、Pu、NAC 分别解剖（STAR Methods），并报告 NAC 的 SPN 域尺寸最小、insulation 最高而 CaT 相反（Section 4，fig. S7I）。
3. **中棘投射神经元（spiny projection neuron, SPN）：** 纹状体主要细胞类型，按多巴胺受体分 D1（直接通路：纹状体→GPi/SNr→丘脑）与 D2（间接通路：经 GPe、STH）（ref10,12,13）。本文用甲基化再分 matrix/striosome/ventral 亚群与 D2 SMYD2 新亚型（Fig. 4A）。
4. **eSPN 与 NUDAP：** eccentric SPN 指带 D1/D2 双特征的奇异亚群；本文分为 STR D1D2 eSPN（DRD1 与 DRD2 同时低甲基化）与 STRv D1 NUDAP eSPN（NUDAP 为 accumbens/putamen 内化学定义独特域）（Fig. 4A）。
5. **matrix–striosome（MS）区室：** 背侧纹状体交替镶嵌的两组织学区室；SPN 按定位分 D1M/D2M 与 D1S/D2S。本文 MERFISH 用 200 µm 半径 SPN 邻域组成向量加 K-means（K=3）计算 MS score 划界（STAR Methods；Fig. 6A）。
6. **快放电中间神经元（fast-spiking, FS）：** PVALB 阳性 GABA 能中间神经元，放电快、动作电位窄；焦点群 STR FS PTHLH-PVALB GABA 在 matrix/striosome 间呈分子与电生理双重差异（Fig. 6N–O）。
7. **CN ST18 GABA 与 CN LAMP5-CXCL14 GABA：** 前者为 MGE 谱系（ST18 决定 GPi 投射神经元命运，ref20），主要由 STR TAC3-PLPP4 GABA 驱动、富集 matrix；后者为 CGE 谱系，与星形胶质细胞一起富集 striosome（Fig. 6B）。
8. **胆碱能（Chl）与多巴胺能（Dopa）神经元：** 标记分别为 CHAT/SLC5A7 与 TH/SLC6A3；Chl 的 LHX6/LHX8 低甲基化对应 MGE 起源，M Dopa 在 group 层分 GAD2/SOX6/CALB1 三亚型（Fig. 2G、2I）。
9. **神经节隆起（ganglionic eminence，LGE/MGE/CGE）：** 端脑腹侧胚胎分区；LGE 产出 SPN 与 CN MEIS2 系（MEIS2 为 LGE 标志），MGE 产出胆碱能与 PVALB/SST 谱系，CGE 产出 VIP/LAMP5 谱系。发育起源是解释区域化与 motif 的核心框架（Section 2、6）。
10. **MGM1 与 RN GATA3 GABA：** MGM1 为中脑灰质样本，混合 VTR、SN 与红核（RN）；因 HMBA 参考只含 SN-VTR，本文检出独立群 RN GATA3 GABA 并以相邻 MERFISH 切片支持其 RN 起源（fig. S3G–S3H）。

### （二）单细胞组学与 DNA 甲基化

11. **5-甲基胞嘧啶（5-methylcytosine, 5mC）：** 胞嘧啶甲基化修饰，参与分化、疾病与衰老（ref22–28）；在有丝分裂中稳定传递，可作持久细胞身份指纹（ref34–36）。本文以之为不依赖 RNA 的身份与调控读数。
12. **mCG（CpG methylation）：** CpG 背景甲基化，全组织普遍。本文 100-kb mCG 主要承载非神经元聚类信号（fig. S2D–S2E）。
13. **mCH（non-CpG methylation，CH 背景）：** CHG/CHH 非对称甲基化，分裂后神经元中丰度最高（ref29）。本文中 mCH 给出最高 silhouette 分数，最能分辨 D1/D2 SPN 等精细亚型（Section 1）。
14. **单核测序（single-nucleus, sn-）：** 冻存死后人脑只能解离核。本文 NeuN 阳/阴性核按 80%/20% 混合，25% 入 snm3C-seq，75% 给伴文 Paired-Tag（STAR Methods）。
15. **snm3C-seq（single-nucleus methyl-3C sequencing）：** 同一核内联合测 DNA 甲基化（亚硫酸氢盐路径）与 3D 染色质接触（3C 路径）的技术（ref37）。本文全部甲基化与 HiC 数据皆由它产出。
16. **亚硫酸氢盐转换与 hisat-3n（ref84）：** 未甲基化 C 转 U/T 而甲基化 C 保留，比对后估计位点甲基化分数；hisat-3n 为三碱基转换序列比对器，比对到供体特异参考基因组（STAR Methods）。
17. **DMR（differentially methylated region）：** 细胞类型间甲基化差异区域，ALLCools 调用（Δβ≥0.3 且 ≥2 差异位点），分 hypo/hyper；subclass 层共 2,361,659 个 hypo 与 1,296,880 个 hyper-DMR（Section 2）。
18. **DMG（differentially methylated gene）：** 基因体 ±2 kb 甲基化差异基因；神经元内以 mCH、非神经元内以 mCG 呈标记基因低甲基化（fig. S4D–S4F）。
19. **FANS 与 NeuN：** 以 Alexa Fluor 488 抗 NeuN 抗体加 Hoechst 流式分选富集神经元核；是样本神经元占 80% 的来源，也是解读非神经元 3D 结果时的分选偏倚（Limitations 第 1 条）。
20. **mCCC fraction（QC 指标）：** snm3C-seq 质控阈值之一（<0.05），与 mCH<0.2、mCG>0.5、reads 5×10⁵–10⁷ 共同界定高质量细胞（STAR Methods）。
21. **pseudobulk（伪批量）：** 把同型细胞信号聚合为一份批量样本再统计；DMR、ABC、LDSC、MS-DEGs 均在其上完成，后者按供体+技术重复聚合（STAR Methods）。
22. **100-kb bin：** 以 100-kb 窗口统计 mCG/mCH 或接触数，是甲基化聚类与区室分析的基本分辨率，也是作者自陈的 3D 分析主要局限（Limitations 第 2 条）。

### （三）3D 基因组

23. **Hi-C：** 交联-酶切-连接-测序普查基因组空间接触的技术（ref31）；单细胞版数据稀疏，需 scHiCluster（ref86）插值后降维。
24. **A/B 区室（compartments）：** 染色质在 Mb 尺度按互作偏好分的活性 A 与非活性 B 两类；本文以距离归一化 pseudobulk 接触矩阵的 PC1 为区室分数，CpG 富集方向定为 A 正向（STAR Methods）。
25. **TAD 与 domain boundary：** 亚 Mb 尺度局部自互作结构域；25-kb 分辨率用 TopDom（ref121）调域，用 insulation score（滑窗跨界接触比例，越低=边界越强）刻画边界（STAR Methods）。
26. **染色质环（chromatin loop）：** 10-kb 分辨率点对点富集接触，经全局与局部双背景校正且经验 FDR<0.1 才保留（STAR Methods）；全文报告 147,791 个差异环（Section 3）。
27. **superdomain：** 相邻同型区室合并成的更大结构；神经元更少更大，非神经元更小且富集长程接触（fig. S6H）。
28. **APA（aggregate peak analysis）：** 把一组差异环叠合到某细胞类型插值接触矩阵求平均，检验环信号真实性与特异性；对角线强于非对角即支持（Fig. 3H）。
29. **saddle plot 与 compartment strength：** 把 bin 按区室分数排序分 50 档后平均接触频率作图，量化 AA+BB 与 AB+BA 之比；OPC-Oligo 与免疫细胞区室化最强，Glut Sero Dopa 最弱（fig. S6A–S6E）。
30. **短程/长程接触：** 以 5 Mb 为界；神经元以短程为主（M Dopa 长程仅 12.4%），非神经元更多（Vascular 44.4%、Lymphocyte 51.7%）（Fig. 3A）。
31. **mappability 与死后样本陷阱：** 单细胞 HiC 受覆盖与比对唯一性影响，死后组织另有降解风险；本文以 ENCODE blacklist（ref83）、排除 chrM/X/Y 与 NA bin 分类规避（STAR Methods；Fig. 3B 的 NA bin 嗅觉富集解释）。

### （四）调控组学与统计框架

32. **增强子与 promoter-TSS：** 顺式调控元件。本文 hyper-DMR 显著富集于 promoter-TSS（χ² 检验 p<0.05、odds ratio>2，Fig. 2B），hypo-DMR 更多位于远端增强子样区域。
33. **ATAC-seq：** 转座酶可及性测序，度量开放染色质；数据来自伴文 10x Multiome（ref38）与 Paired-Tag（ref39），用于 ABC 输入与跨模态检验（Fig. 3C）。
34. **H3K27ac/H3K27me3/H3K9me3：** 分别标记活性增强子/启动子、Polycomb 抑制域与异染色质；用 Droplet Paired-Tag（ref39,110,111）同细胞联测 RNA 与三者，检验与 DMG/DMR/区室一致性（fig. S7D、S8B–S8D）。
35. **CUT&Tag 与 Paired-Tag：** CUT&Tag 类方法以抗体导向在位酶标记天然染色质修饰；Paired-Tag 为其液滴单细胞版并同读 RNA（ref110,111）。本文组蛋白数据全部来自 Paired-Tag 伴文。
36. **ABC 模型（Activity-by-Contact，ref89,124）：** 以增强子活性与接触频率之积预测 E-P 连接。本文取最强 ATAC 峰 150,000 个、5 Mb 窗、阈值 0.021，得 108,203 条 subclass 级连接，其中 9,158 条具三重证据（Section 5）。
37. **GRN 与 motif 富集（Cluster-Buster ref118；pycistarget ref90）：** GRN 即基因调控网络；以 hypo-DMR 内 motif 富集（NES>3 且 ≥10 hits）→TF 表达→ABC E-P→甲基化相关 |r|≥0.7 四级过滤构建（Fig. 5A）。本文用 SCENIC+ 框架中的 pycistarget 模块，未用 pySCENIC 本体（ref90）。
38. **LDSC（LD score regression，ref91,144）：** 把性状 GWAS 遗传力按 LD 分数回归分配到功能注释（本文为 DMR 或环锚点）；小注释（基因组覆盖 <1%）易假阳性，作者显式设防（Limitations 第 5 条）。
39. **GSEA/KEGG（clusterProfiler ref116；GSEApy ref117）：** 基因集富集框架。SPN hypo-DMG 富集吗啡/可卡因成瘾、多巴胺能突触、LTP 与昼夜节律通路；退行性疾病通路富集于 CN ONECUT1 GABA 等群的 hypo-DMG 与小胶质/淋巴/内皮的 hyper-DMG（Fig. 2F）。
40. **motifbreakR（ref68）：** R 包，按位置权重矩阵计算等位基因对 motif 匹配分的影响；用于证明 rs1372518 强化 RUNX3 motif（等位效应 0.158，Fig. 5J）。
41. **ENCODE blacklist（ref83）：** 人基因组中因重复/异常信号需排除的区域名单；本文在 100-kb bin 特征、DMR 与环调用中系统性排除（STAR Methods）。
42. **Mann-Whitney U、χ² 与置换检验：** 本文三大检验家族：DMG 用 MWU+BH 校正；DMR 注释富集用 χ²（附 odds ratio）；差异域边界与收敛基因富集用 10,000 次 Monte Carlo 置换（23.6 倍、p≤1×10⁻⁴）（STAR Methods）。

### （五）空间组学与跨模态整合

43. **MERFISH（multiplexed error-robust FISH）：** 多重错误校正荧光原位杂交，以编码探针加多轮成像逐分子计数组织切片上数百至上千基因的 mRNA（Chen et al. 2015, DOI 10.1126/science.aaa6090）。本文用 Vizgen MERSCOPE Ultra 与 920 基因 panel，QC 后 1,482,528 个细胞（Section 6）。
44. **邻域组成向量与 MS score：** 以每个 SPN 周围 200 µm 内其他 SPN 组型计数向量做 K-means（K=3）归类邻域环境；MERFISH 为单分子成像而非 spot 混样，此法规避 spot 式空间转录组的解卷积伪迹（STAR Methods；Fig. 6A）。
45. **label transfer 与 CCA 整合（Seurat anchors；Harmony ref88）：** 以锚点把 RNA 参考标签迁移到甲基化或 MERFISH 数据，Harmony 校正供体/批次；HMBA BG 共识分类（ref38）为所有模态共享坐标系。
46. **Patch-seq（ref53,71）：** 膜片钳电生理与单细胞 RNA 测序联合的方法。本文取 89 个猕猴 STR FS PTHLH-PVALB GABA 神经元，经两次独立整合推断区室定位（9 个 striosome、72 个 matrix、8 个冲突剔除）后比电生理（Section 6）。
47. **UMAP 与 silhouette score：** 降维可视化与聚类分离度指标。本文在信息量匹配的 PCA 空间比较 mCG/mCH/RNA/HiC 四模态，神经元内 mCH 最优、单细胞 HiC 只分非神经元（fig. S2D–S2E）。
48. **供体特异参考基因组（GATK，ref95,109）：** 用 WGS 与 GATK 把每供体纯合 SNP 嵌入 hg38，避免供体变异被误读为甲基化或接触差异；死后人脑单细胞表观组学的关键细节（STAR Methods）。
49. **HMBA、BICAN 与 HBA：** Human and Mammalian Brain Atlas（ref38）提供 BG 共识分类；BRAIN Initiative Cell Atlas Network（ref21）为联盟框架与经费来源；Human Brain Atlas（ref33）贡献 3 名复用供体 snm3C 数据（GSE215353，64,328 细胞），与本文 197,003 个新测 BICAN 细胞合并为 261,331 个高质量细胞（Section 1）。

---

## 二、<核心问题与方案>

**生物学问题（原文表述）：**

- "While individual BG cell groups have been characterized, cell-type-resolved epigenomic maps of the human BG remain limited."（Introduction 第 1 段末）
- "BG lesions can manifest as cell-type-specific cell death that imbalances striatocortical circuitry, so delineating the susceptible cell types is an important step toward defining disease mechanisms and targeting therapeutics."（Introduction 第 1 段，疾病层面）
- "5mC, a stable mark propagated through cell divisions, provides durable cell-type-specific signatures."（Introduction 第 2 段，方法层面）
- "Coupling methylation and 3D contacts with transcriptional atlases enables the study of the epigenetic control of cell states."（Introduction 第 2 段，调控层面）

**背景矛盾（研究切入点）：** 表达侧图谱（BICAN/HMBA ref21,38 与全脑 snRNA ref40）已给出 BG 细胞类型清单，但 mRNA 是不稳定读数，且回答不了"哪段调控 DNA 在哪个细胞里开启哪个基因"；而单细胞甲基化与 3D 基因组在小鼠全脑与人类皮层已有先例（ref32,33,85），人类 BG 恰是 PD、亨廷顿病等易感核心区却无对应图谱。本文的切入点是绕开"再画一张表达图谱"，直接把 5mC 稳定指纹加 3D 接触铺到 BG 八区，并强制对齐 HMBA 共识分类，使结论可与 RNA、ATAC、组蛋白、空间与跨物种电生理交叉验证。

**解决方案（技术路线）：**

- 模型系统：7 名健康成年死后供体（4 名新收集 UCI2424/UCI4723/UCI5224/UWA7648，男女各半，PMI 16.3–25.5 h，RIN>6；3 名复用 HBA），8 个解剖亚区，神经元富集 80%。选死后人脑因 BG 疾病为人类高发，且 BICAN 标本门户保障解剖一致性。
- 实验设计：1）各区显微解剖后核解离、NeuN FANS、80/20 混合，25% 入 snm3C-seq，使同一组织同时产出甲基化与 3D 接触并与伴文共享材料；2）每供体 WGS 建参考基因组排除 SNP 干扰；3）BICAN 与 HBA 细胞联合聚类并 Harmony 校正，产出 12 class、31 subclass、59 group；4）分层调用 DMR/DMG 并做 motif 富集与 LDSC；5）100-kb 区室、25-kb 域边界、10-kb 环三层 3D 分析并用 APA 排除全局压缩解释；6）ABC 预测 E-P 并以 enhancer-AAV 工具箱做基准回收；7）MERFISH 加邻域 MS score 调用 matrix/striosome，以免疫组化与跨物种 Patch-seq 复证。
- 功能验证：本文属图谱类资源论文，验证体现为三处正交校验，即 enhancer-AAV 回收（68.2%/50.0%，Fig. 5E）、单供体 CaB 免疫组化（SLC22A3+/FGF13+/VIP−，Fig. 6C）与猕猴 Patch-seq 电生理方向一致（Fig. 6N）。作者明确说明 D2 SMYD2 尚需扰动验证、GRN 与 E-P 多为计算预测（Limitations 第 3、4、7 条），本文不美化这些边界。
- 机制解析：从"细胞类型清单"到"稳定甲基化指纹"（Fig. 1–2），到"3D 构象差异"（Fig. 3），到"SPN 亚型与区域程序"（Fig. 4），到"候选增强子与疾病位点"（Fig. 5），再到"空间微环境差异"（Fig. 6），是从相关性逐级逼近调控假设的递进链。

**验证层级：**

聚类一致性（Fig. 1C–E；fig. S1–S2）→ 区域特异性（Fig. 1F）→ DMR/DMG 与 TF motif（Fig. 2A–D）→ 疾病遗传力（Fig. 2E）→ 区室/域/环（Fig. 3A–I）→ SPN 亚型多模态一致（Fig. 4A–J）→ E-P 与增强子回收（Fig. 5B–H）→ SNCA 位点提名（Fig. 5I–J）→ MS 空间差异（Fig. 6A–L）→ 跨物种电生理（Fig. 6M–O）。

**统计与生信框架（Methods 要点）：**

- QC 与比对：mCCC<0.05、mCH<0.2、mCG>0.5、唯一比对 reads 5×10⁵–10⁷；PNCC 1.2/0.8 外判 doublet；hisat-3n 比对到供体特异 hg38（GATK，ref95,109）。
- 聚类与整合：Scanpy PCA 加 ALLCools significant_pc_test（KS p=0.1）与 Leiden、ConsensusClustering；Harmony（ref88）校正批次；Seurat 式锚点整合做标签迁移。
- DMR/DMG：ALLCools（Δβ≥0.3、≥2 DMS）；DMG 用 MWU+BH 且 AUC≥0.8；motif 用 Cluster-Buster 加 pycistarget（NES>3）；富集用 clusterProfiler/GSEApy。
- 3D：scHiCluster 插值（100/25/10 kb）；区室 PC1 与 dcHiC（ref119）差异区室；TopDom 与 insulation；环需双背景 FDR<0.1；APA 21×21 窗；每 subclass 伪批量细胞数上限 1,500。
- ABC 与 GRN：前 150,000 ATAC 峰、5 Mb 窗、score>0.021，另需靶基因上调/低甲基化/高可及性三条件之一（FDR≤0.05）；TF-靶基因 |r|≥0.7 且靶基因低甲基化。
- LDSC：19 个性状 GWAS 汇总统计（ref125–143），1000G Phase 3 注释；小注释假阳性设防（ref144）。
- MERFISH：Cellpose-SAM（ref100）与 Proseg（ref101）分割、Deconwolf 去卷积（ref98）；MS-DEGs 用 PyDESeq2 伪批量（~donor+group，FDR<0.001、|log2FC|>0.5、≥2 区方向一致）；电生理用 rank-biserial 效应量加 Mann-Whitney U（FDR 0.1；因 striosome 细胞少无一通过，按效应量排序——受限结果如实报告）。
- 数据可及性：NeMO 存档、GEO GSE320293、AWS Open Data、MERFISH BIL DOI 10.35077/g.1194、代码 GitHub DingWB/BG_snm3C-seq 与 Zenodo DOI 10.5281/zenodo.23267620；门户 basalganglia.epigenomes.net 与 SCMDAP。

---

## 课本化背景补注①：单细胞 DNA 甲基化测序——从"测全基因组"到"每个核自带三维折叠"

单细胞 DNA 甲基化的技术史，是一条「覆盖度—通量—模态」逐级抬升的台阶，每一步都在回答上一步留下的瓶颈。bulk 全基因组重亚硫酸盐测序先确立了哺乳动物脑甲基组的整体图景：Lister 等 2013（ref22）扫过脑发育全程，发现非 CpG 甲基化（mCH）在分裂后神经元中大量积累——从这一刻起，甲基化才从「启动子开关」升格为「细胞身份的终身记录仪」；Schultz 等 2015（ref29）的人体表观基因组图谱把这一坐标系铺到全身组织作参照。分水岭是单细胞化：Mo 等 2015（ref115）与 Luo 等 2017（ref114）把单细胞重亚硫酸盐测序用于哺乳动物皮层，证明单个细胞的甲基化组足以分辨神经元亚型并提名调控元件；Liu 等 2021（ref85）随后在小鼠全脑尺度铺成单细胞甲基化图谱。方法学的另一半在流程端成熟：Zhang 等 2021（ref84）的 HISAT-3N 专为核苷酸转换类 reads 提速对齐，让数十万核的处理变得现实。模态合流是最近一步：Lee 等 2019（ref37）的 snm3C-seq 在同一个核内同时读出 DNA 甲基化与三维构象，Liu 等 2023（ref32）与 Tian 等 2023（ref33）把该体系推成全脑尺度的「甲基化 × 3D」图谱。本文站在这条链的末端：不发明新测序方法，而是把「同一批核双模态」的做法推进到此前空白的基底节八个亚区（261,331 核甲基化 + 229,286 核 3D），并与空间转录组咬合。

与本文同思路的铺垫研究清晰可数。Liu 等 2023（ref32）与 Tian 等 2023（ref33）已确立「单细胞甲基化 + 3D 架构」这一范式，BICAN 社区框架（ref21）则把人类与哺乳动物脑细胞图谱定为共同目标——本文填补的正是这张大图上深部核团的位置：基底节是帕金森病、亨廷顿病的病变核心，却因取样难长期停留在 bulk 或小样本分辨率。差异化也在这里：本文的贡献是「把范式推进到新解剖区 + 叠加空间坐标」，而不是方法发明。

读甲基化数据有三个常设陷阱：信息量与每核覆盖度呈平方根关系，稀亚型的 DMR 判定依赖 pseudobulk 与插值，覆盖不足时结论只到「群体混合」层级；postmortem 组织里甲基化确实是终身记录仪，但同一批核的 3D 构象只是采样时刻的快照，两者时间尺度不同；doublet 与批次效应靠 PNCC 过滤与 Harmony 校正压制，残余伪影要对照 LIMITATIONS 逐条核对。

- 来源与阅读深度：技术史各节点依据本文参考文献表 ref22/29/114/115/84/85/37/32/33 的题录与正文陈述定向核读；前作原文未逐篇通读。
## 课本化背景补注②：3D 基因组与染色质区室化——先解决"测得到"，再解决"信不信"

单细胞水平的 3D 基因组学，先解决「测得到」，再解决「信不信」。群体 Hi-C 时代建立了 A/B 区室与 TAD 的坐标系，但那是百万个核的平均像；单细胞 Hi-C 出现后反而带来信任危机——单个核的接触矩阵极度稀疏，聚类与区室判定高度依赖插值算法，Zhou 等 2019（ref86）的卷积加随机游走插值就是为这一步而生。转折点是 Lee 等 2019（ref37）的 snm3C-seq：在同一个单核里同时测 3D 构象与 DNA 甲基化，让「三维折叠」第一次拥有一个同源且正交的对照读数——空间上弱、甲基化上清晰的细胞类型，可以用后者为前者背书。Liu 等 2023（ref32）与 Tian 等 2023（ref33）随后把该体系推成全脑尺度图谱；本文再把 229,286 个核落在基底节，并按细胞类型计算 mCG 内在的 A/B 区室。

同思路的铺垫同样是 ref32 与 ref33：全脑尺度的单细胞「甲基化 × 3D」图谱已经提示神经元区室强度偏弱、但细胞类型之间仍可分辨。本文的差异在三点：解剖区（基底节深部核团，此前无人做过单细胞 3D）、模态组合（叠加空间转录组与 Paired-Tag 蛋白组）与问题取向——本文把 3D 读数主要用作「细胞身份的正交确认」与基因体区室判定，而不是把结构发现本身当主结论。

判读有两条边界要随身携带：一是「稀疏 vs 伪影」——神经元不再分裂，区室弱既可能是终末分化的属性，也可能是接触稀疏的技术后果，本文用与甲基化区室的一致性来区分，但 imputation 补出的接触不能当作真实染色质环来读；二是 mappability 与拷贝数——非整倍体或比对空洞会在接触矩阵上制造假结构，读者复核时应优先看原始接触热图的比对质量，而非只看区室得分。

- 来源与阅读深度：方法谱系依据 ref37/86/32/33 题录与正文、STAR Methods 定向核读；区室判定的具体参数以论文原文为准。
## 课本化背景补注③：空间转录组——两条路线合流之后，"谁挨着谁"才变成可计算的量

空间转录组走的是两条互补的路线，本文处在两条路线合流之后的阶段。spot 测序路线（Visium 一类）转录组覆盖全，但一个 spot 通常装着好几种细胞，分辨率换通量；成像路线以 MERFISH 为代表，用组合条形码加多轮成像在组织原位读单分子 RNA，基因数受 panel 上限约束，换来的是真正单细胞分辨率的原位坐标。两条路线各自成熟后，领域的问题才从「画表达地图」推进到「量化细胞邻域」——把每个 spot 的细胞类型组成变成向量，「谁挨着谁」才成为可计算的对象。本文用的正是这一步之后的形态：以 MERFISH panel 读出细胞组成，再把「小岛还是基质」做成邻域变量——对每个 SPN 细胞取 200 μm 半径内的邻居组成向量，K-Means（K=3，同时覆盖背腹轴与小岛—基质轴）聚类后人工注释定轴，再以 D1S/D2S SPN 先验驱动的 matrix score 给逐 spot 打分。

与本文同思路的铺垫研究要分两层看。人类纹状体的细胞多样性此前靠解离测序建立：Muñoz-Manchado 等 2018（ref71）与 Garma 等 2024（ref14，重点在中间神经元多样性）立起了细胞类型清单，但解离天然丢掉空间坐标——「细胞类型有多多样」和「细胞类型怎么排布」是两个问题。把两者合到小岛—基质问题上，本文属于早期实践：用分子先验驱动空间打分，再回查非 SPN 细胞在两侧的分布差异（如 CN ST18 GABA 富集于基质侧）。

读空间数据有一条绕不开的边界：spot 混细胞意味着「MS 高」永远不是「这个细胞属于基质」，而是「该邻域富集基质特征」；分区轴的判定质量依赖 SPN 先验与人工注释的稳定性，换一套先验重跑，边界位置可能移动。解离图谱（ref71/14）与空间数据是互补证据，前者给细胞类型字典，后者给排布，不能互相替代。

- 来源与阅读深度：路线与本文参数（200 μm、K=3、MERFISH panel）依据正文与 STAR Methods；ref71/14 题录定向核读，前作未通读。
## 课本化背景补注④：纹状体基质—小岛（striosome–matrix）——从组织学名词到可计算的变量

小岛—基质是纹状体里资格最老的「分子分区」，它的研究史几乎就是纹状体解剖学的缩影。分区由 Graybiel 学派以组织化学对比定义——乙酰胆碱酯酶低染的斑块区即小岛，其余为基质；此后数十年，小鼠遗传学与环路追踪不断给这个分区填入功能含义，但「分区」始终是组织学名词，不是可计算的变量。分子分型时代换了一套语言：Muñoz-Manchado 等 2018（ref71）与 Garma 等 2024（ref14）的单细胞图谱确认人类纹状体细胞类型远比经典组织学丰富，而「小岛/基质」与「分子亚型」如何对应，仍是悬而未决的问题。本文把对应关系往前推了一步：用 D1S/D2S SPN 分子先验构造 matrix score，在空间数据上把分区变成逐 spot 的连续变量，并发现 MS 差异「不止于 SPN 身份」——CN ST18 GABA 等非 SPN 细胞也携带分区信号。

这条线里还有一条与本文同思路的铺垫：把发育来源当分子读数。本文观察到 D2 SMYD2 亚型共享 POU6F2 与 ZFPM2 而缺 PAX5，据此推断其起源更接近 LGE（端脑腹侧）而非后脑——这正是「用标志基因把解剖学区隔翻译成发育谱系」的思路在单细胞数据上的延续，也呼应了小岛—基质在发育上分批产生的经典认识。Graybiel 的原始组织学论文未出现在本文参考文献表中，本补注不引其具体图号（编号待核）。

本文对这条线的贡献，是把分区从「切面上看出来的斑块」变成空间数据上可检验、可复算的变量；边界同样清楚——MS score 由 SPN 先验驱动，非 SPN 细胞的分区信号是「先定轴、再回查」所得，不是独立定义的第二分区系统。若未来有小岛/基质特异的遗传标记工具，这条轴才谈得上因果检验。

- 来源与阅读深度：本文 ref14、ref71 定向核读；发育来源推断依据正文；Graybiel 原始文献不在本文参考文献表，图号「编号待核」。

---

**引导段：** 本模块按原文 RESULTS 六个小节展开，每节先给出以「内容逻辑：」领起的连贯叙事段（含设计理由、推理链、关键定量、竞争性解释鉴别与前后衔接），随后以「→ Figure X」嵌入该节主图的逐 panel 四字段解读；补充图 S1–S11 按其在正文与 caption 中的角色整合进对应 panel（原 PDF 未随附 S 图版，细节以 caption 与正文为准；凡图上读出的近似值均标注"读自图"）。

## 三、<逐节精读>

### Section 1：Single-nucleus DNA methylation and 3D genome architecture atlas of the human BG（人 BG 单核 DNA 甲基化与 3D 基因组架构图谱）

内容逻辑：本节把数据集骨架立起来，回答"测了什么、分出了什么、有多可信"。设计上，作者对八个 BG 亚区（CaH、CaB、CaT、Pu、NAC、GP、STH 与混合 VTR-SN-RN 的 MGM1）做神经元富集 snm3C-seq，把 197,003 个 BICAN 新测细胞与 HBA（ref33）的 64,328 个细胞合并迭代聚类，得到 261,331 个高质量细胞，其中 229,286 个同时有 3D 数据；并入而非重测既省稀缺的人类组织，又检验跨研究可重复性。推理链三步：先用全基因组 mCG/mCH 水平加标记评分粗分神经元与非神经元（fig. S1B–S1C）；再把神经元对齐 HMBA 共识分类（ref38），得 12 class、31 subclass、59 group，并把高度异质的 splatter 簇拆成 17 个 subclass（fig. S1D–S1H）；最后做一致性审计——subclass 注释与 HBA 标签强一致（fig. S2A–S2B），独立用 100-kb mCG+mCH 与 HiC 嵌入再聚类仍得一致注释（fig. S2C）。竞争性解释方面，作者检验"3D 数据能否独立分型"：神经元内 mCH 的 silhouette 最高、能分开 D1/D2 SPN，而单细胞 HiC 嵌入只能分离非神经元（fig. S2D–S2E），排除了"任何模态都同等分型"的隐含假设，并为 Section 3 的 3D 分工埋下伏笔。区域特异性（Fig. 1F）显示腹侧 SPN 限于 NAC、M Dopa 与 F M Glut 等限于 MGM1/STH、CN MEIS2 与 CN ONECUT1 GABA 限于 GP（超几何检验 p<0.05），与解剖一致；跨模态整合（fig. S2H–S2I）唯一新增群是 RN GATA3 GABA，作者用"我们的 MGM1 解剖含 RN 而 HMBA 参考不含"解释，并以相邻 MERFISH 切片支持（fig. S3G–S3H）。配套 MERFISH 数据取自相邻组织块（920 基因 panel），QC 后 1,482,528 个细胞，其中 1,159,607 与 1,068,878 个分别在 subclass 与 group 层获高置信注释（Fig. 1G），唯一缺口是 UWA7648 的 CaT 组织不足。本节的贡献是确立全后续分析的分类坐标系与各模态可信度边界：甲基化分型最细、3D 最粗、空间补区域与区室。

→ Figure 1 标题为"Single-nucleus DNA methylation and 3D genome architecture atlas of the human BG"，旨在展示数据全貌。由 A 至 G 共 7 部分构成：A 解剖与取样示意，B–E 同一 UMAP 的区域/class/subclass/group 四层着色，F 表观组学分类树，G NAC 的 MERFISH 样例，形成"空间-分子-层级"互锁的总览结构。

(A) BG 结构与亚区取样示意
图片解释：脑渲染图以彩色高亮 BG 各核团，右侧对应 UMAP 按解剖区域着色并叠加区域特异细胞密度。定量数据：标注八亚区缩写（CaH/CaB/CaT/Pu/NAC/GP/GPe/STH/MGM1(VTR-SN-RN)），比例尺 1.0 mm（读自图）。
横纵轴定义：无坐标轴（解剖示意与 UMAP）；阅读方向为先看脑图定位、再看 UMAP 对应色群。
颜色含义：CaH/CaB/CaT 红-深红、Pu 橙、NAC 蓝、GP/GPe 绿、STH 淡蓝、MGM1 红框标签，颜色即解剖区域。
核心结论：八个亚区全部成功取样并对应 UMAP 独立群体，确立图谱空间覆盖（fig. S1A 解剖判据）。

(B) 按解剖区域着色的 UMAP
图片解释：全部高质量核的 UMAP，每点一核，颜色为解剖区域归属。定量数据：总细胞数 261,331（229,286 有 3D 数据）；图例列九个区域。
横纵轴定义：无坐标轴（UMAP）；阅读方向为看色群分离与混杂。
颜色含义：每色一个解剖区域（图例）。
核心结论：区域信息在甲基化空间中清晰保留，区域特异性是数据集的显性结构（fig. S2F–S2G 区域组成定量）。

(C) 按 12 个 class 着色的 UMAP
图片解释：同一 UMAP 按 class 着色：神经元一侧分 Subpallium GABA、Glut Sero Dopa、Subpallium GABA-Glut，另一侧 Nonneuron（Astro-Epen、OPC-Oligo、Immune、Vascular）。定量数据：12 个 class（图例）。
横纵轴定义：无坐标轴（UMAP）；阅读方向为看神经元/非神经元两大域分离。
颜色含义：每色一个 class；神经元亚域用蓝、粉、绿色系，非神经元用灰紫系。
核心结论：甲基化数据先按谱系（发育来源与神经元/胶质）分层，与解剖和发育逻辑一致。

(D) 按 31 个 subclass 着色的 UMAP
图片解释：同一 UMAP 按 subclass 着色并逐一标注 STR D1 SPN、STR D2 SPN、Oligodendrocyte、M Dopa、Immune、VLMC、Pericyte、SMC、Cholinergic、CN MEIS2 等。定量数据：31 个 subclass；splatter 再拆 17 个（fig. S1D–S1H）。
横纵轴定义：无坐标轴（UMAP）；阅读方向为看 D1/D2 SPN 等近缘亚型的可分性。
颜色含义：每色一个 subclass，标签颜色对应色群。
核心结论：mCH 主导的聚类能分辨 D1/D2 SPN 等精细亚型，是"甲基化分型最细"的直接证据（fig. S2D–S2E silhouette 对比）。

(E) 按 59 个 group 着色的 UMAP
图片解释：同一 UMAP 按 group 着色，各群以编号圆圈标注（1–59），图例逐行列出群名（如 20 STR FS PTHLH-PVALB GABA、51 STR D1D2 eSPN、53 STR D2 SMYD2-HTR7 SPN、56–59 为背侧 D1/D2 的 Matrix/Striosome SPN）。定量数据：59 个 group（Tables S2–S3）。
横纵轴定义：无坐标轴（UMAP）；阅读方向为对照图例定位后文引用的群编号。
颜色含义：每色一个 group，编号即后文图中的索引。
核心结论：group 层已含本文两个焦点群（D2 SMYD2 与 STR FS PTHLH-PVALB GABA），为 Section 4 与 6 预置对象。

(F) 表观组学分类树
图片解释：左为 group 层树状图，随后多列依次为 subclass 归属、区域组成、中位 mCG、中位 mCH、BICAN 与 HBA 细胞数（log2）、cis/trans 接触比、短/长程接触比。定量数据：色标 mCGFrac 0.78–0.88、mCHFrac 0.010–0.100、CisRatio 0.220–0.330、TransRatio 0.150–0.220（读自图内色标）。
横纵轴定义：纵向为 59 个 group，横向为各度量列；阅读方向为逐列比较。
颜色含义：区域组成列按解剖区域配色，mCG/mCH 色阶蓝到红为低到高。
核心结论：神经元 mCH 高、非神经元 mCG 高而 mCH 低；各群区域组成与接触特征互异，形成可检索参考表（Tables S2–S4）。

(G) NAC 的 MERFISH 样例
图片解释：左为 NAC 样本 zoomed-out 视野，SPN 按 group 着色；右为 zoomed-in 视野，DAPI 与细胞边界底图上叠加 DRD1 与 DRD2 转录点。定量数据：比例尺 zoomed-out 1 mm、zoomed-in 50 µm（读自图）；panel 920 基因（Table S5）。
横纵轴定义：无坐标轴（显微成像）；阅读方向为左看区室全景、右看单细胞内转录点。
颜色含义：DRD1 点青色、DRD2 点红色（图例），底图 DAPI 白/灰。
核心结论：D1 与 D2 SPN 在 NAC 内空间上各自成群，MERFISH 与甲基化分类互洽，为 Section 6 提供方法可行性背书（fig. S3）。

补充材料角色：fig. S1 为解剖、QC 与 splatter 拆分；fig. S2 为与 HBA 的注释一致性、跨模态 silhouette 与区域组成；fig. S3 为 MERFISH 覆盖、QC、重复相关性与 RN GATA3 GABA 空间支持。

### Section 2：Cell-type-specific DNA methylation landscapes reveal candidate regulators and disease associations（细胞类型特异甲基化景观揭示候选调控因子与疾病关联）

内容逻辑：本节把分类坐标变成调控与疾病两份可检索资源，推理从粗到细。第一步调用 DMR：stringent 过滤后得 2,361,659 个 hypo-DMR 与 1,296,880 个 hyper-DMR，其中 471,826 与 366,655 个为单一 subclass 或 group 独有的 cell-type-specific hypo-DMR（原文如此表述；Fig. 2A）；DMR 内通常含多个差异 CpG，SPN 各亚型间模式相似是例外（fig. S4A）。第二步功能注释：hyper-DMR 显著富集于 promoter-TSS（χ² 检验 p<0.05、odds ratio>2，Fig. 2B），对应甲基化抑制启动子的经典角色。第三步 motif 反演调控因子：MEIS2（LGE 标志）在 CN MEIS2 GABA 与 D1/D2 SPN、PAX7 在 IP、ONECUT1 在同名群、PITX2 在 STH PVALB-PITX2 Glut、POU6F2 在 STR D2 SMYD2-HTR7 SPN 中富集（Fig. 2C–D）；FOXP1、PBX3、MEIS2 与 POU2F2 motif 在 hyper-DMR 中富集，作者以"部分 TF 可结合甲基化 DNA"（ref41,42）解释，排除"富集到 hyper-DMR 即不可能"的隐含假设。第四步接疾病：LDSC 显示 F M GATA3 GABA 与 SPN 的 hypo-DMR 关联 PD、智力、双相与精神分裂症遗传力（Fig. 2E），SPN 相关而非 Dopa 相关的 PD 结果出人意料，作者在 Discussion 坦承未检出多巴胺能神经元的预期富集并归因采样限制。第五步 DMG 与通路：SPN hypo-DMG 富集吗啡/可卡因成瘾、多巴胺能突触、LTP 与昼夜节律 KEGG 通路；退行性疾病通路富集于 CN ONECUT1 GABA、F Glut、CN GABA-Glut 的 hypo-DMG 与小胶质/淋巴/内皮的 hyper-DMG，MAPT、APP、APOE 在 CN ONECUT1 GABA 低甲基化且表达，SV2A 低甲基化对应 GPi 核心投射神经元的高囊泡周转（Fig. 2F；fig. S5）。第六步到 group 层：M Dopa 分 GAD2/SOX6/CALB1 三亚型且 LMX1A motif 与其低甲基化互洽（Fig. 2G–I）；星形胶质细胞四亚型区域归属与伴文研究（ref44）的 GM STR/WM 亚组对上（Fig. 2J–K）；小胶质-2 出现在 60 岁以上供体，作者立即声明供体少且年龄-性别混杂、不可下强结论，仅援引独立老化研究（ref45）作旁证（fig. S5L）。本节的贡献是把甲基化差异从描述升级为可检索的 TF 候选与疾病-细胞类型配对，并逐处设防（提名不等于因果验证、LDSC 为相关）。

→ Figure 2 标题为"Cell-type-specific DNA methylation landscapes reveal candidate regulators and disease associations"，旨在呈现 DMR 全景、TF motif 反演与 LDSC/GSEA 下游。由 A 至 K 共 11 部分构成：A DMR 热图，B 注释条形，C–D motif 与表达，E LDSC，F GSEA，G–I 基因体甲基化与 motif，J–K 星形胶质细胞验证，形成"差异→调控→疾病→案例"漏斗。

(A) subclass 与 group 层 top 500 hypo-DMR 的甲基化热图
图片解释：行按 subclass 与 group 层各取差异最大的 500 个 hypo-DMR，列为对应细胞类型，颜色为 DMR 内 mCG 分数。定量数据：色标 0.1–1.2（读自图）；全图共 2,361,659 hypo 与 1,296,880 hyper-DMR（正文）。
横纵轴定义：纵向为 DMR（按细胞类型分块），横向为细胞类型（先 subclass 后 group）；阅读方向为找每列变蓝的行块。
颜色含义：黄/红为高 mCG、蓝为低 mCG。
核心结论：多数细胞类型有清晰特异低甲基化块，SPN 各亚型例外地彼此相似，成为 Section 4 的伏笔（fig. S4A）。

(B) cell-type-specific hyper 与 hypo-DMR 的基因组注释
图片解释：上下两组堆叠条形图统计 hyper/hypo-DMR 落在 intergenic、intron、exon、TTS、promoter-TSS 的比例，并给 log2 计数。定量数据：%Annotation 纵轴 5–15（log2 #DMR）；hyper-DMR 富集 promoter-TSS 的 χ² 检验 p<0.05、odds ratio>2（正文）。
横纵轴定义：横向为细胞类型，纵向为 %Annotation；条形组高为 log2 计数（5–15）；阅读方向为比较两类 DMR 在 promoter-TSS 行的占比。
颜色含义：五种注释各一色（图例）。
核心结论：hyper-DMR 系统性偏向启动子-TSS，hypo-DMR 更多在远端，与经典图景一致。

(C) subclass DMR 的 TF motif 富集
图片解释：热图行为 subclass、列为候选 TF（每 subclass 取上调前三位 TF 的 motif），格内为富集信号。定量数据：hypo-DMR ±250 bp 序列经 Cluster-Buster 与 pycistarget（NES>3 阈值，STAR Methods）。
横纵轴定义：纵向为 31 个 subclass（按谱系着色），横向为 TF 名；阅读方向为找每行最深格。
颜色含义：色深表示 motif 富集强度（caption 未给 NES 数值范围）。
核心结论：MEIS2、PAX7、ONECUT1、PITX2、POU6F2 等按谱系精准复现，POU6F2 为 Section 4 埋伏笔（fig. S4B–S4C）。

(D) (C) 中 TF 的表达点图
图片解释：点图验证 (C) 的 TF 是否真在其对应细胞类型高表达，点大小为 frac（检出比例），颜色为 Mean(log CPM)。定量数据：色标 −1 至 1，点大小 0.2–1.0（读自图例）。
横纵轴定义：纵向为 TF（红色标注对应细胞类型），横向为 subclass；阅读方向为沿对角找"同群同 TF"的深色大点。
颜色含义：白到红为 log CPM 低到高。
核心结论：motif 富集与 TF 表达双向一致，支持"低甲基化 motif+高表达 TF"作为活性调控判据。

(E) LDSC：subclass hypo 与 hyper-DMR 的性状遗传力富集
图片解释：左右两张热图分别为 hypo 与 hyper-DMR 注释下 19 项性状/疾病的富集，行为性状（ADHD、Educational Attainment、Neuroticism、Schizophrenia、Bipolar Disorder、Intelligence 及 PD 等疾病块），列为 subclass。定量数据：色标 −log10(p) 1.30–4.85；显著性 \*\* 为 FDR<0.01、\* 为 FDR<0.05（Benjamini-Hochberg 校正，caption）。
横纵轴定义：纵向为性状，横向为 subclass；阅读方向为在每行找带星号的深色格。
颜色含义：白到红为 −log10(p) 低到高，星号即显著性层级。
核心结论：SPN 与 F M GATA3 GABA 的 hypo-DMR 关联 PD 与精神性状，预期中的 Dopa 未显著，作者以采样限制解释并保留其相关性质（Discussion 与 Limitations 第 5 条）。

(F) subclass 级 DMG 的 KEGG 通路 GSEA
图片解释：点热图，行为 KEGG 通路（可卡因/吗啡成瘾、多巴胺能突触、LTP、昼夜节律、神经退行性疾病通路、帕金森病、亨廷顿病等），列为 subclass，红为 hyper-DMG 富集、蓝为 hypo-DMG 富集。定量数据：色标 FDR 0–0.05，点大小为 GeneRatio（读自图例与 caption）。
横纵轴定义：纵向为通路，横向为 subclass（顶部按 Neighborhood 着色）；阅读方向为找每行的蓝/红大点。
颜色含义：红=hyper 富集、蓝=hypo 富集，色深为 FDR 强度。
核心结论：SPN 低甲基化基因集中成瘾与突触可塑性通路，退行性疾病通路集中特定 GABA 能与非神经元群（fig. S5A–S5E）。

(G) 区分 SPN、Dopa 与 Chl 的 top hypo-DMG 及其 motif TF
图片解释：点热图，列为 D1、D2、Eccentric SPN、Dopa、Chl 五群，行为基因体 mCH（标记基因与 top hypo-DMG），motif 富集 TF 以红色标注。定量数据：色标 Mean mCH 0.00–1.50，点大小 frac 0–1（读自图例）。
横纵轴定义：纵向为基因（按群分块），横向为五个细胞群；阅读方向为找每块内变蓝的行。
颜色含义：蓝=低 mCH（活跃），红=高 mCH；红字为对应 DMR 内富集 TF。
核心结论：SPN 特异低甲基化 MEIS2/FOSL2/FOXO3 靶基因，Dopa 特异 NR4A2，Chl 特异 LHX6/LHX8，与发育起源互洽（fig. S5F–S5G）。

(H) 各群 hypo-DMR 中富集 motif 且自身低甲基化的 TF 列表
图片解释：按群列出 TF 名单（NFIA、RFX4、RUNX1/ETV6、MEIS2、LHX6、NR4A2 等），为 (G) 的 TF 视角汇总。定量数据：入列标准为 motif NES>3 且 TF 自身低甲基化（正文与 STAR Methods）。
横纵轴定义：无坐标轴（名录式版面）；阅读方向为按群块扫描候选 TF。
颜色含义：无渐变（纯文本名录）。
核心结论：低甲基化的 TF 自身正是其 motif 富集群的候选主控，构成 Section 5 GRN 的候选池。

(I) M Dopa 三亚型（group 层）的 top hypo-DMG
图片解释：与 (G) 同构的点热图，列为 GAD2、SOX6、CALB1 三群，行为各群 top hypo-DMG，LMX1A 等红字标注。定量数据：色标 Mean mCH 0–1.5，frac 0–0.99（读自图例）。
横纵轴定义：纵向为基因，横向为三群；阅读方向为比较三列蓝色块差异。
颜色含义：蓝=低 mCH；红字=motif 富集 TF。
核心结论：M Dopa 在 group 层解出三个调控身份不同的亚型，LMX1A motif 与其低甲基化和表达三方一致（fig. S5H–S5I）。

(J) 星形胶质细胞亚型的区域 Sankey 图
图片解释：Sankey 流向图，左侧 Astrocyte-1 至 4 四群，右侧 CaH/CaB/CaT/Pu/NAC/GPe/MGM1 各区域，带宽为细胞流比例。定量数据：定性流向，配套比例见 fig. S5J。
横纵轴定义：无坐标轴（Sankey）；阅读方向为看每群流向哪个区域更宽。
颜色含义：沿用全图区域配色。
核心结论：Astrocyte-2/3/4 富集纹状体，Astrocyte-1 富集 GPe 与 MGM1，星形胶质细胞同样具区域特化。

(K) 与伴文 HMBA 星形胶质细胞研究的混淆矩阵
图片解释：矩阵列为本文 Astrocyte-1 至 4，行为伴文研究（ref44）的 GM STR、GM exSTRd、WM 亚组，格内为归属比例。定量数据：格值如 0.0037/0.47/0.53、0.27/0.73、0.97 等，fraction 色标 0.0003–0.9960（读自图）。
横纵轴定义：纵向为伴文亚组，横向为本文 group；阅读方向为找每行最大格。
颜色含义：白到红为比例低到高。
核心结论：本文 Astrocyte-3/4 与伴文 GM STR/WM 亚组一一对应，独立数据源验证 group 层拆分真实性。

补充材料角色：fig. S4 为 DMR 细节、SPN 相似性、POU6F2 一步对余比较与 DMG 背景；fig. S5 为 GSEA 细节、Dopa 亚型、星形胶质细胞与小胶利亚群及年龄模式。

### Section 3：Cell-type-specific compartmentalization and 3D genome architecture in the human BG（人 BG 细胞类型特异区室化与 3D 基因组架构）

内容逻辑：本节把 229,286 个带 3D 数据的核按三个尺度解剖，论证策略是"先分层、再排伪、后接疾病"。第一层区室：Glut Sero Dopa 神经元区室化最弱，OPC-Oligo 与免疫细胞最强（fig. S6A–S6B）；BB/AA 比在免疫细胞（class 层）与 CN ONECUT1 GABA、M Dopa（subclass 层）升高，mCG saddle plot 显示区室特异甲基化主要在免疫细胞可见（fig. S6C–S6E）。第二层距离结构：非神经元接触距离更长（fig. S6F），按区室组合分层后神经元以 <5 Mb 短程为主；Fig. 3A 给出量化——M Dopa 仅 22.2% 的 A-B 接触为长程，而 Vascular 44.4%、Lymphocyte 51.7%，长程接触比例从 M Dopa 12.4% 递增到 Immune 56.2%，神经元 superdomain 更少更大（fig. S6H）。第三层功能解读：免疫细胞在 A 区室表达基因最多，M Dopa、GPi 与 Chl 在 B 区室表达最多（fig. S6I）；A 区室基因富集动态调控与管家过程，B 区室基因富集早期神经与胶质发育过程，作者解读为成熟神经元维持发育基因的 B 区室沉默；NA bin 富集嗅觉转导，作者立即给出机制解释（嗅觉受体簇位于重复 DNA，ref47–49）并排除"嗅觉在 BG 特异表达"的误读。竞争性解释排除在两处：区室分数与 H3K27ac 的相关神经元（r=0.42）低于非神经元（r=0.53），H3K9me3 为 −0.36 对 −0.44，说明神经元内区室-调控偶联更弱而非不存在（Fig. 3C）；APA 显示对角线强于非对角且矩阵不对称，证明差异环是 subclass 特异的而非全局压缩（Fig. 3H）。第四层域与环：共 2,110 个差异域边界与 147,791 个差异环，75 个（3.55%）边界重叠"同群既低甲基化又上调"的基因，富集 23.6 倍（置换检验 p≤1×10⁻⁴），案例为 SORCS2（亨廷顿病中错误定位并损害 SPN 的 NR2A 转运，ref50）与 FOXP2（eSPN 标记，在 eSPN 处于 A 区室而在 D1/D2 处于 B 区室）（Fig. 3E–G）。第五层疾病与亚型：LDSC 用环锚点做注释，智力、精神分裂症、双相关联 LGE/CGE/MGE 系 GABA 神经元环锚点，PD 关联 STR SST-CHODL GRIN2A GABA，多发性硬化关联淋巴细胞（fig. S6O）；SPN 三亚型边界 74%–79% 共享、环私有比例更高（D1 10.9%、D2 12.5%、eSPN 19.8%），作者明确声明此对比只说明环分辨率更细，不构成"环携带更多生物信号"的证明（Fig. 3J）。本节的贡献是建立"神经元紧凑、非神经元松散且区室化强"的 BG 3D 基准，并把 3D 与调控层焊在一起。

→ Figure 3 标题为"Cell-type-specific compartmentalization and 3D genome architecture in the human BG"，按区室、功能、域、环四层呈现 3D 差异。由 A 至 J 共 10 部分构成：A 弦图组，B 富集点图，C 相关箱线，D circos，E 差异边界热图，F–G 案例位点，H APA 矩阵，I 结构度量箱线组，J Venn，形成"全景-机制-案例-质控"结构。

(A) 12 个 class 的 chr10 弦图
图片解释：每 class 取 100 个细胞，把 chr10 接触按锚点区室组合（A|A、A|B、B|B、Other）与距离（短/长程）画成弦图；标题百分比为 A-B 接触中长程占比。定量数据：M Dopa 22.2%、F M Glut 24.7%、CN GABA-Glut 26.8%、F M GABA 27.0%、CN MGE GABA 31.8%、CN LGE GABA 33.7%、CN CGE GABA 40.1%、Astro-Epen 48.4%、OPC-Oligo 54.8%、Immune 56.2%、Vascular 57.6%；各类内另标 Short/Long 与 A|A、A|B、B|B 比例（如 M Dopa：Short 87.6%、A|A 34.9%、A|B 24.9%、B|B 37.9%）。
横纵轴定义：无坐标轴（弦图）；chr10 按 0–130 Mb 环状排布；阅读方向为比较各图标题百分比与弦粗细。
颜色含义：弦按锚点区室着色（A/B/NA 三色图例，读自图）。
核心结论：从 Glut Sero Dopa 到 Immune，长程与 A-B 接触比例单调上升，神经元/非神经元两大 3D 状态成立（fig. S6F–S6H）。

(B) A、B、NA 区室基因的 GO 与 KEGG 富集
图片解释：点图，行为 Biological Process、Molecular Function 与 KEGG 词条，列为 A、B、NA 三类区室基因。定量数据：GeneRatio 0–0.13，色标 −log10(p.adjust) 1.301–5.000（读自图例）。
横纵轴定义：纵向为词条（嗅觉转导、吞噬体、细胞周期、神经退行性疾病通路等），横向为 A/B/NA；阅读方向为逐列读主题。
颜色含义：点色深浅为显著性，点大小为 GeneRatio。
核心结论：A 区室基因富集动态调控与管家过程，B 区室富集早期神经与胶质发育过程；NA bin 因嗅觉受体簇位于重复 DNA 而富集嗅觉转导，作者主动定性为技术性伪迹（ref47–49）。

(C) 区室分数与各模态信号的全基因组相关
图片解释：箱线图组，横轴按模态分块（mCG、mCH、ATAC、H3K27ac、H3K27me3、H3K9me3），每箱为一个 subclass 的全基因组 Pearson 相关值，按 Neighborhood 着色。定量数据：H3K27ac 非神经元 r=0.53 对神经元 r=0.42；H3K9me3 平均 −0.44 对 −0.36（正文）；纵轴 −0.6 至 0.6。
横纵轴定义：横轴为六种模态分组，纵轴为相关系数；阅读方向为比较每块内 Nonneuron 与三类神经元的箱位。
颜色含义：四类 Neighborhood 各一色（读自图例）。
核心结论：神经元内区室分数与活性/抑制组蛋白标记的偶联系统性弱于非神经元，100-kb 区室在神经元内的调控解读需谨慎。

(D) 各细胞类型 chr10 平均 5-kb mCG 的 circos 图
图片解释：环状图外圈为 chr10 的 5-kb mCG 颜色环，叠加免疫细胞（外）与 M Dopa（内）的 A/B 区室轨道。定量数据：mCG 色标 0.22–1.22（读自图）。
横纵轴定义：无坐标轴（circos）；阅读方向为沿环比较区室轨道与甲基化条的对应。
颜色含义：绿-红色阶为 mCG 低-高；A/B 轨道为环形条带。
核心结论：低甲基化区段与 A 区室在非神经元中更对应，直观呈现甲基化-区室耦合的细胞类型差异。

(E) 差异域边界跨 subclass 热图
图片解释：热图行为 2,110 个差异域边界（25-kb bin），列为各 subclass，格值为边界占据率，右侧标注重叠基因（GRIK2、PBX1、SV2B、……、FOXP2、SORCS2 等）。定量数据：色标 normalized probability 0–1（读自图）；75 个边界与收敛基因重叠、23.6 倍富集、p≤1×10⁻⁴（正文）。
横纵轴定义：纵向为差异边界，横向为 subclass（顶部按 Neighborhood 着色）；阅读方向为找每行唯一变色的列。
颜色含义：蓝-红色阶为边界占据率低-高。
核心结论：域边界具细胞类型特异性，且特异边界显著富集"低甲基化+上调"基因，把 3D 边界与调控状态焊接（fig. S6M）。

(F) SORCS2 位点的差异域边界
图片解释：chr4 上 SORCS2 区段（约 7,200–7,800 kb，读自图）四行接触热图（STR D1 SPN、D2 SPN、D1D2 eSPN、STRv D1 NUDAP eSPN），色阶为接触分数，基因位置标注于底。定量数据：色标 0–0.012（读自图）；SORCS2 在 STR D1D2 eSPN 低甲基化且上调（正文）。
横纵轴定义：横向为 chr4 坐标（kb），纵向为四个 SPN 群；阅读方向为看 eSPN 行基因体内接触增强。
颜色含义：蓝-红色阶为接触频率低-高。
核心结论：eSPN 特异边界与基因体内互作升高对应 SORCS2 高表达，且该基因在亨廷顿病中错误定位（ref50），构成疾病关联案例。

(G) FOXP2 位点的差异域与环
图片解释：chr7 上 FOXP2 区段（114,100–114,700 kb，读自图），顶部为区室分数轨道（A/B 标注），下为 STR D1、D2、Eccentric SPN 三行接触热图与环弧。定量数据：色标 0–0.009（读自图）；FOXP2 在 eSPN 处于 A 区室、在 D1/D2 处于 B 区室（正文）。
横纵轴定义：横向为 chr7 坐标，纵向为三个 SPN 群；阅读方向为比较 eSPN 行与 D1/D2 行的环与接触。
颜色含义：接触热图蓝-红为低-高；环弧按组着色。
核心结论：FOXP2 的区室归属随 SPN 亚型切换，是同一基因在不同细胞类型有不同 3D 状态的直证（fig. S6N 的 RELN 同理）。

(H) 跨细胞类型 APA 矩阵
图片解释：矩阵行为 Signal contact matrix Q（提供接触图的群），列为 Diff-loop set（提供差异环集合的群），格值为 APA 强度；虚线框按 Neighborhood 分块。定量数据：色标 APA strength 1.000–2.863（读自图）；对角线强于非对角（正文）。
横纵轴定义：行=接触矩阵来源群，列=差异环来源群；阅读方向为比较对角与非对角格深浅。
颜色含义：蓝-红色阶为 APA 强度低-高。
核心结论：差异环是 subclass 特异的真实局部接触而非全局压缩产物；矩阵不对称提示神经元的差异环在非神经元图中几乎无信号、反向有残留，与谱系嵌套一致。

(I) subclass 级 3D 结构度量箱线组
图片解释：八行箱线图逐 subclass 比较 RNA 平均计数、ATAC、差异环数、差异边界数、log2(短/长接触比)、环距离、insulation score、域尺寸。定量数据：纵轴范围 RNA 0–4、ATAC 0–4、差异环 100–20,000、差异边界 5–500、log2 比 −1–3、环距离 0.1–2.0 Mb、insulation 0.1–0.3、域尺寸 0.50–1.00 Mb（读自图）。
横纵轴定义：每行横轴为 subclass（按谱系着色），纵轴为对应度量；阅读方向为逐行比较神经元与非神经元箱位。
颜色含义：同 (C) 的 Neighborhood 配色。
核心结论：非神经元域更大、insulation 更低但环距离更短，神经元差异边界与环更多、可及性与表达更高；NAC 的 SPN 域最小而 CaT 相反（Section 4，fig. S7I）。

(J) SPN 三亚型高置信边界与环的 Venn 图
图片解释：左右两个三集合 Venn，分别为 STR D1、D2、Eccentric SPN 的高置信 TAD 边界 bin 与高置信环。定量数据：边界 Venn 三元共享核心 24,720 个 bin，D1/D2/eSPN 独有扇区读自图约 3,043/1,800/3,300；环 Venn 共享核心 116,087 个环，与正文私有比例 D1 10.9%、D2 12.5%、eSPN 19.8% 相符（每 subclass 边界约 32,000）。
横纵轴定义：无坐标轴（Venn）；阅读方向为比较共享核心与私有扇区相对大小。
颜色含义：三色半透明扇区代表 D1、D2、eSPN。
核心结论：SPN 边界高度共享（74%–79%）而环私有比例更高；作者明确此对比源于分辨率差异，不构成信号强度结论——限定性结果如实呈现。

补充材料角色：fig. S6 为区室强度 saddle、BB/AA、接触距离分层、superdomain、区室-表达、SORCS2/RELN 细节与环锚点 LDSC，是本节定量声明的展开位。

---

### Section 4：DNA methylation resolves SPN subtypes and regional signatures in the striatum（DNA 甲基化解析纹状体 SPN 亚型与区域签名）

内容逻辑：本节回答"甲基化能否在最相似的细胞家族里再往下分"。上节已确认 SPN 各亚型 hypo-DMR 模式彼此最相似，竞争性解释是"SPN 分型只是噪声或批次差异"；本节用三重证据钉死。其一，group 层把 D1/D2 SPN 注释为 matrix（D1M/D2M）、striosome（D1S/D2S）与 ventral（D1V/D2V），依据整合分析与标记基因体 ±2 kb 的 mCH 低甲基化（fig. S7A），并获解剖支持：ventral SPN 主要来自 NAC，背侧来自 Ca/Pu（Fig. 4B–C）。其二，刻画新亚型 STR D2 SMYD2-HTR7 SPN（由 HMBA 共识分类独立定义并被三套伴文支持，ref38,39,52,53）：它在 mCG+mCH 与 3D 两种嵌入中都最靠近 D2 striosome（PCA 质心距离量化，单侧 Mann-Whitney U 检验），说明其全局身份是"D2 谱系、偏 striosome"；但仅用 group 特异判别性 CG hypo-DMR 聚类时又紧邻 eSPN，与猕猴 Patch-seq 报告的中间形态-电生理属性一致（ref53）——两种嵌入的分歧本身携带信息，说明 D2 SMYD2 位于 D2 与 eSPN 之间的中间调控位置。需排除的替代解释是"HiC 嵌入分不开 D1/D2，所以 3D 数据没用"：作者先在 fig. S2D–S2E 基准里承认这一点，再展示 3D 嵌入仍能粗分背/腹、matrix/striosome/eccentric（Fig. 4D），并援引伴文中 ATAC 与 H3K9me3 同样分不开 D1/D2（ref38,39），把负性结果转化为对模态分辨力的诚实界定。其三，差异甲基化给出各群标记：D2 SMYD2 的 hyper-DMG 最多、NUDAP 的 hypo-DMG 最多（Fig. 4F）；群特异 hypo-DMG 包括 DRD1/RELN（D1）、DRD2/ADORA2A（D2）、TSHZ1/FOXP2（eSPN）、EPHA4/STXBP6（matrix）、BACH2（striosome）、SRGAP3/CMIP/GDA（ventral）、EYA2/RXFP1（NUDAP）、CASZ1（D1D2），与已发表 RNA 数据互洽（ref11,38），其中 CLMP（多发性硬化 ref54）、SULF2（阿尔茨海默病 ref55）、SMYD2（卒中 ref56,57）为疾病相关；SMYD2 与 SULF2 在 D2 SMYD2 呈 CG 与 CH 双低甲基化、可及性与 HiC 接触升高、H3K27ac 强而 H3K27me3/H3K9me3 降低的多模态一致（fig. S7D）。TF 层：POU6F2 motif 在两种比较（对余与对其他 SPN）均富集，POU6F2 基因座本身呈群特异低甲基化、可及性与 H3K27ac 升高、TAD 内接触与 E-P 连接增多（Fig. 4H、4J）；POU6F2 已被报告为后脑来源 SNr subclass 标记（ref58），D2 SMYD2 共享 POU6F2 与 ZFPM2 但缺 PAX5，指向 LGE 端脑起源。区域签名：CADM1 在 NAC 全部 SPN 群低甲基化，表达与 CH 甲基化从腹侧前部到后部 CaT 呈梯度（Fig. 4L–N），3D 接触频率在 D1D2 eSPN 中给出匹配梯度（Fig. 4M）；PDE8B（ADSD 关联基因，ref59,60）呈相反梯度；NAC 的 SPN 域最小、insulation 最高而 CaT 相反（fig. S7I）。作者同时声明区域程序是否连续仍是开放问题。本节的贡献是把 SPN 从两个亚型推进为带区域梯度的亚型谱系，并确立 D2 SMYD2 为多模态一致的新刻画对象（扰动验证留待后续）。

→ Figure 4 标题为"DNA methylation resolves SPN subtypes and regional signatures in the striatum"，展示 SPN 亚型的多模态解析。由 A 至 O 共 15 部分构成：A–D 四种嵌入与流向，E–I 差异甲基化与 TF，J POU6F2 位点多模态，K–O 区域梯度，形成"分型-调控-空间"三段结构。

(A) SPN 的 100-kb mCG/mCH UMAP（按 group 着色）
图片解释：SPN 亚群 UMAP，标注 STRd D1/D2 Matrix、Striosome、STRv D1/D2、STR D1D2 eSPN、STRv D1 NUDAP 与 D2 SMYD2-HTR7 各群。定量数据：输入特征为 100-kb mCG 与 mCH。
横纵轴定义：无坐标轴（UMAP）；阅读方向为看 D2 SMYD2 相对 D2 Striosome 与 Matrix 的落位。
颜色含义：每色一个 group，标签嵌在色群上（读自图）。
核心结论：甲基化嵌入已把 SPN 分到 matrix/striosome/ventral/eSPN/NUDAP/D2 SMYD2 群级结构（fig. S7A 支持注释）。

(B) 同一 UMAP 按解剖区域着色
图片解释：与 (A) 同一嵌入，颜色改为解剖区域（CaH/CaB/CaT/Pu/NAC 等）。定量数据：区域列表同 Fig. 1B。
横纵轴定义：无坐标轴（UMAP）；阅读方向为看 ventral 群与 NAC、背侧群与 Ca/Pu 的对应。
颜色含义：区域配色沿用全文方案（读自图例）。
核心结论：SPN 亚群的空间身份在甲基化嵌入中保留，支持区域梯度分析的前提。

(C) 解剖区域到 group 注释的 Sankey 图
图片解释：Sankey 流向图，左列 CaH/CaB/CaT/Pu/NAC 区域，右列 SPN 各 group，带宽为细胞流比例。定量数据：定性流向（fig. S7 配套）。
横纵轴定义：无坐标轴（Sankey）；阅读方向为找每区域最宽流出带。
颜色含义：左列按区域配色。
核心结论：ventral SPN 主要源自 NAC，背侧 matrix/striosome 群源自 Ca 与 Pu，注释获解剖学正交支持。

(D) SPN 的 100-kb HiC UMAP
图片解释：SPN 的单细胞 HiC 嵌入 UMAP，按 group 着色。定量数据：100-kb 接触插值嵌入（scHiCluster）；D1/D2 分离弱、背/腹与 matrix/striosome/eccentric 粗分可见（正文）。
横纵轴定义：无坐标轴（UMAP）；阅读方向为与 (A) 对比各群聚合度。
颜色含义：与 (A) 相同的 group 配色。
核心结论：3D 数据的 SPN 分辨力低于甲基化但能恢复粗层级，此负性结果与跨模态基准（fig. S2D–S2E）和伴文一致，界定模态边界。

(E) group 特异判别性 CG-only hypo-DMR 的分层聚类
图片解释：以"一群对其余 SPN"的判别 hypo-DMR 做 SPN group 聚类热图，颜色为 mCG。定量数据：色标 0–1（读自图）；D2 SMYD2 聚类紧邻 eSPN（正文）。
横纵轴定义：纵向为 SPN group（顶部树状图），横向为 hypo-DMR；阅读方向为看树状图分支顺序。
颜色含义：黄-蓝色阶为 mCG 高-低。
核心结论：D2 SMYD2 的判别性甲基化模式靠近 eSPN，与其在猕猴 Patch-seq 中的中间形态-电生理属性一致（ref53）。

(F) 各 SPN 群的 CH hyper 与 hypo-DMG 数量
图片解释：横向条形图，行为 SPN 各群，两条为 CH hyper 与 hypo-DMG 计数。定量数据：D2 SMYD2 hyper-DMG 最多、NUDAP hypo-DMG 最多（正文）；具体计数原文未在正文给出。
横纵轴定义：横轴为 DMG 数量，纵轴为 SPN 群；阅读方向为比较两色条长。
颜色含义：橙=hyper、蓝=hypo（读自图例）。
核心结论：D2 SMYD2 与 NUDAP 分别是甲基化最"保守化"与最"开放"的两端，框定亚型谱系极值。

(G) 各 SPN 群标记基因与 top hypo-DMG 的基因体甲基化
图片解释：点热图，列为 SPN 各 group，行为标记与 top hypo-DMG（POU3F1、EPHA4、TSHZ1、FOXP2、DRD1、DRD2、ADORA2A、SLC35D3、STXBP6、BACH2、KIRREL3、CASZ1、EYA2、RXFP1、SMYD2、SULF2、TACR1、HTR7 等）。定量数据：色标 Mean mCH 0–1，点大小 frac 0–1（读自图例）。
横纵轴定义：纵向为基因（按群分块），横向为 SPN group；阅读方向为找每块的蓝色列块。
颜色含义：蓝=低 mCH（活跃），红=高 mCH。
核心结论：各群 hypo-DMG 与已知 RNA 标记互洽（ref11,38），并新增 CLMP/SULF2/SMYD2 等疾病相关基因（ref54–57）。

(H) SPN 各群 hypo-DMR 的富集 motif logo
图片解释：网格排布的 motif 序列 logo，每行为一个 SPN 群，列为其富集 TF（MEIS1/2、ONECUT2、RFX、NFATC2、POU6F2、ONECUT1、NFIB、DLX1 等）。定量数据：NES>3 且 ≥10 motif hits 的入列标准（STAR Methods）。
横纵轴定义：无坐标轴（logo 网格）；阅读方向为按行找各群代表 motif。
颜色含义：碱基按 A/C/G/T 标准四色。
核心结论：matrix 的 ONECUT2、D2 SMYD2 的 POU6F2、NUDAP 的 NFIB、striosome 的 BACH2、ventral 的 RFX3 各自成对出现于 motif 与 TF 低甲基化（Fig. 4I 支持表达）。

(I) POU6F2 与 NFIB 在 HMBA 中的表达小提琴图
图片解释：两张小提琴图分别为 POU6F2 与 NFIB 的表达，横轴为 SPN group（D2M、D1S、D1V、D2V、NUDAP、D2 SMYD2 等），数据来自 HMBA RNA 数据集。定量数据：纵轴 Mean(log CPM)，约 0–3（读自图）。
横纵轴定义：横轴为 group，纵轴为 Mean(log CPM)；阅读方向为找最高的小提琴。
颜色含义：各群一色。
核心结论：POU6F2 与 NFIB 分别在其对应群（D2 SMYD2 与 NUDAP）选择性表达，motif-甲基化-表达三方闭环。

(J) POU6F2 位点的多模态聚集证据
图片解释：chr7 上 POU6F2 区段（约 36,100–36,500 kb，读自图）多轨道图：mCG、mCH（按 SPN group 分行）、ATAC、H3K27ac、E-P 连接弧，黑框标注候选调控元件；下半为 STR D2 Matrix、D2 Striosome、STRv D2、D2 SMYD2 的接触热图与 ABC-E-P 分数条。定量数据：坐标读自图；接触热图色阶为 ABC-E-P Score。
横纵轴定义：横向为 chr7 坐标，纵向为 group 分行轨道；阅读方向为看 D2 SMYD2 行在黑框区域的信号。
颜色含义：mCG/mCH 蓝-红为高-低，ATAC/H3K27ac 峰为信号条，接触图蓝-黄-红为低-高。
核心结论：POU6F2 座位在 D2 SMYD2 呈低甲基化、高可及性、强 H3K27ac、TAD 内接触与 E-P 连接的五重一致，是该亚型的核心调控证据。

(K) SPN 各群的区域差异甲基化基因
图片解释：点热图，行为区域 DMG（CADM1 红字突出），列为 group×region 组合（顶部色条标区域）。定量数据：色标 Mean mCH 0–1.2，点大小 frac 0–1（读自图例）。
横纵轴定义：纵向为基因，横向为群-区域组合；阅读方向为沿 CADM1 行看 NAC 列变蓝。
颜色含义：蓝=低 mCH；顶部色条为区域标签。
核心结论：CADM1 在 NAC 的所有 SPN 群低甲基化且表达升高，区域甲基化签名真实存在（fig. S7G）。

(L) CADM1 的 mCH 与 RNA 前后梯度
图片解释：双纵轴折线图，横轴为 NAC/CaH/CaB/CaT（前后轴），左轴为 CH 基因体 mCH（约 1–1.4），右轴为 RNA log2(CPM)；三条线为 D1M、D2M、Eccentric SPN，点为中位数，误差棒 ±1 SD。定量数据：Paired-Tag 表达与甲基化（caption）。
横纵轴定义：横轴为区域，左纵轴 mCH、右纵轴 log2(CPM)；阅读方向为看两轴的反向趋势。
颜色含义：三色线对应三个 SPN 群（读自图例）。
核心结论：CADM1 表达与 mCH 从腹侧前部到后部 CaT 呈系统梯度，表达-甲基化负相关跨区域成立。

(M) CADM1 位点的 3D 接触频率梯度
图片解释：chr11 上 CADM1 区段的接触热图五行（NAC/CaH/CaB/Pu/CaT），来自 STR D1D2 eSPN。定量数据：色标 0–0.006（读自图）。
横纵轴定义：横向为 chr11 坐标，纵向为五个解剖区域；阅读方向为比较各行基因座位的接触强度。
颜色含义：蓝-黄-红为接触低-高。
核心结论：CADM1 的区域表达梯度匹配 3D 接触频率梯度，把 Section 3 的 3D 框架落到区域生物学。

(N) CADM1 的空间验证（供体 UCI5224）
图片解释：上排五个区域切片（CaT/Pu/CaH/CaB/NAC）的 CADM1 RNA 空间图，下排为 imputed 基因体 mCH 空间图。定量数据：比例尺 1.0 mm；RNA 色标约 0–1.1，mCH 色标读自图。
横纵轴定义：无坐标轴（空间切片）；阅读方向为左右比较各区域表达/甲基化强度。
颜色含义：RNA 热图橙-红高，mCH 热图蓝色阶。
核心结论：MERFISH 空间图复现 CADM1 的 NAC 高表达与甲基化梯度，独立供体支持（fig. S7G）。

(O) PDE8B 的反向梯度
图片解释：与 (L) 同构的双轴折线图，对象为 PDE8B，横轴自后部 CaT 到前部 CaH 与腹侧 NAC。定量数据：轴设定同 (L)；PDE8B 为 ADSD 关联基因（ref59,60）。
横纵轴定义：同 (L)；阅读方向为看与 CADM1 相反的斜率。
颜色含义：同 (L)。
核心结论：PDE8B 呈相反的前后梯度，提示区域甲基化程序与疾病易感性（ADSD）的空间对应（fig. S7G–S7H）。

补充材料角色：fig. S7 为 SPN 注释支持（S7A）、HiC 嵌入（S7B–S7C）、D2 SMYD2 多模态一致性（S7D）、突触组织富集（S7E）、PBX1 motif（S7F）、区域 DMG 与域尺寸（S7G–S7I）。

### Section 5：Multi-omic integration predicts cell-type-specific GRNs（多组学整合预测细胞类型特异 GRN）

内容逻辑：本节把前四节的三种证据（DMR、TF motif、3D 接触）合成可检索的调控网络，方法论核心是"每一步都加阈值、每一步都给正交基准"。先做跨模态校准：把基因分 DMG-only、DEG-only、DMG&DEG 与背景四组比较，发现基因体低甲基化只在 DMG-only 与 DMG&DEG 组显著而不在 DEG-only 组（fig. S8A），证明甲基化与表达捕捉的是部分不相交的基因集合——这直接为"用甲基化补 RNA 之短"的立论提供量化根据；mCH 在抑制性组蛋白峰上呈非单调轮廓（fig. S8B），DMR 与组蛋白/可及性关系见 fig. S8C–S8D。GRN 构建的四道滤网是：hypo-DMR 内 motif 富集（NES>3）、ABC 模型 E-P 连接（score>0.021，得 108,203 条 subclass 级连接，其中 9,158 条同时具备上调、低甲基化与高可及性）、TF-靶基因体甲基化相关 |r|≥0.7、靶基因低甲基化（Fig. 5A–C）。竞争性解释的排除靠基准测试：与 enhancer-AAV 工具箱（ref61，病毒实验验证的纹状体细胞类型特异增强子）比对，本文预测回收 68.2% 的增强子层与 50.0% 的 E-P 层验证元件（Fig. 5E），并给出 AiE0445h/AiE0444h/AiE0612h@DRD2、AiE0617h@ADORA2A（D2 SPN）、AiE0873m@SLC5A7（Chl）、POU3F1（pan-SPN）与 SLC35D3（D1 SPN）等案例（Fig. 5F–H）；作者坦承这些元件在体内验证于其他物种/组织，人类 BG 内的特异性仍需 NHP 或 CRISPRi 验证（Limitations 第 4 条）。疾病层落在 SNCA：八个 PD 风险 GWAS SNP 与小胶质及多巴胺亚型增强子重叠（Fig. 5I）；rs2737024 与 rs2583959（ref65）位于 SN-VTR GAD2 Dopa 活性增强子内，风险单倍型 rs2737004/rs2619356 所在增强子已在小胶质中被功能表征（风险等位改变 CTCF/RAD21 与 CEBPB 结合，ref66），本文新贡献是显示它在 PD 易感的 SN SOX6 Dopa 神经元中同样可及且在接触中——作者明确写这是"提名共享调控模块"而非"建立机制"（Discussion）；motifbreakR 进一步给出 rs1372518（Lewy body 痴呆 ref69）强化 RUNX3 motif（等位效应 0.158，Fig. 5J），RUNX3 基线低表达而在 MPTP 模型中上调（ref70），提示潜伏位点。本节的贡献是把图谱资源推到"细胞类型特异候选增强子与疾病位点"的可检索层，同时守住预测与验证的边界。

→ Figure 5 标题为"Multi-omic integration predicts cell-type-specific GRNs"，展示 GRN 构建框架、基准回收与 SNCA 案例。由 A 至 J 共 10 部分构成：A 框架示意，B–C 分布与阈值，D GRN 网络，E 回收率，F–H 三个位点，I SNCA，J 单 SNP motif，形成"方法-验证-疾病"结构。

(A) GRN 构建框架示意
图片解释：流程图：DMR（绿色三角）经 motif 富集指向 TF（红色节点），TF 与靶基因（蓝色节点）经 ABC 模型连出 E-P links，另以甲基化相关作为 TF-靶基因边权。定量数据：四级阈值 NES>3、ABC>0.021、|r|≥0.7、靶基因低甲基化（正文与 STAR Methods）。
横纵轴定义：无坐标轴（流程示意）；阅读方向为从 DMR 起沿箭头走完全流程。
颜色含义：绿=DMR 输入、红=TF、蓝=靶基因（读自图）。
核心结论：网络每条边由两类以上证据支撑，避免纯 motif 推断的假阳性。

(B) 预测 E-P 连接的 ABC 分数分布
图片解释：密度直方图，横轴为 ABC score（0–0.300），红色虚线在 0.021 处标出保留阈值。定量数据：阈值 0.021（官方 ABC 指南）；保留连接 108,203 条（正文）。
横纵轴定义：横轴 ABC score，纵轴密度；阅读方向为看虚线右侧的保留区。
颜色含义：蓝色分布曲线，红色虚线为阈值。
核心结论：绝大多数连接低于阈值被舍弃，保留集是高置信尾部。

(C) TF-靶基因体甲基化相关分布
图片解释：直方图，横轴为 Pearson 相关系数（−1.0 至 1.0），红色虚线在 ±0.7 处。定量数据：保留 |r|≥0.7 的 TF-靶基因对（正文）。
横纵轴定义：横轴相关系数，纵轴计数；阅读方向为看两端保留区。
颜色含义：深蓝直方，红色虚线为阈值。
核心结论：甲基化相关过滤把候选对限制在跨细胞类型强协变的少数对，网络稀疏而可信。

(D) M Dopa 的预测 GRN 网络
图片解释：力导向网络图，红色节点为 TF（NR4A1 居中，另含 NR4A2、EBF3 等），蓝色节点为靶基因（TH、SLC18A2 等），边宽为 TF-靶基因甲基化相关，节点大小为低甲基化显著性。定量数据：NR4A1 被预测调控 M Dopa 的多个靶基因（正文）。
横纵轴定义：无坐标轴（网络图）；阅读方向为从中心红节点向外读调控扇形。
颜色含义：红=TF、蓝=靶基因（caption 明示）。
核心结论：NR4A1 是 M Dopa 的枢纽候选 TF，网络给出可直接检验的调控假设。

(E) enhancer-AAV 工具箱回收率
图片解释：两根柱：Enhancer 层 68.2% 与 E-P link 层 50.0%，柱上标注计数（读自图约 n=1,529 与 n=726）。定量数据：68.2%/50.0%（正文）；比对仅在同型细胞内计数（STAR Methods）。
横纵轴定义：横轴为两个回收层级，纵轴为回收百分比（0–80%，读自图）。
颜色含义：蓝与橙两柱。
核心结论：预测体系在独立病毒验证增强子上达三分之二回收，E-P 层的 50% 反映更严格的"同靶基因"要求。

(F) DRD2 位点的 E-P 连接与增强子回收
图片解释：DRD2 位点（chr11，坐标读自图）多轨道图：各细胞类型（STR D1/D2 SPN、Dopa 等）的 mCG、mCH、ATAC、H3K27ac 轨道，E-P 连接弧，紫块为 enhancer-AAV 工具箱元件（AiE0444h、AiE0612h 等），圈号为 hypo-DMR 的 motif 分组，红色箭头标 D2 SPN 的额外候选增强子；底部为 ABC-E-P 分数热图条。定量数据：轨道为 pseudobulk 信号；工具箱元件名读自图。
横纵轴定义：横向为基因组坐标，纵向为细胞类型轨道；阅读方向为找紫块与弧的交汇。
颜色含义：紫=工具箱增强子，峰图为信号强度，弧=E-P 连接（读自图例）。
核心结论：DRD2 的多个验证增强子被 ABC 连接复现，且 hypo-DMR 内富集 FOSL2、MEIS2、PBX3/MEIS3 motif（正文）。

(G) ADORA2A 位点的 E-P 连接与增强子回收
图片解释：ADORA2A 位点（chr22，约 24,200–25,000 kb，读自图）与 (F) 同构的多轨道图：紫块 AiE0617h 在 D2 SPN 特异活性，圈号 hypo-DMR 与 E-P 弧共同指向 ADORA2A，底部为 ABC-E-P 分数条。定量数据：坐标与轨道设定同 (F)。
横纵轴定义：同 (F)；阅读方向为看紫块与弧的交汇。
颜色含义：同 (F)。
核心结论：D2 SPN 的第二个验证增强子案例，回收覆盖两个经典 D2 标记基因。

(H) SLC5A7 位点的 E-P 连接与增强子回收
图片解释：SLC5A7 位点（chr5，约 267,800–270,000 kb，读自图）与 (F) 同构的多轨道图：紫块 AiE0873m 对应 CN Cholinergic GABA，轨道含胆碱能特异信号，ABC-E-P 分数条展示连接。定量数据：同 (F)。
横纵轴定义：同 (F)；阅读方向为看胆碱能轨道与紫块的对应。
颜色含义：同 (F)。
核心结论：回收跨胆碱能谱系成立，证明体系不限于 SPN。

(I) SNCA 位点的细胞类型特异增强子景观
图片解释：SNCA 位点（chr4，约 89,600–90,100 kb，读自图）多轨道图：小胶质与 M Dopa 亚型（SN-VTR GAD2、SOX6、CALB1）的 mCG、mCH、ATAC、H3K27ac、E-P 连接弧，八条红色竖线为 PD 风险 GWAS SNP（rs2737024、rs2583959、rs2737004、rs2619356 等标注）。定量数据：八个 PD 风险 SNP 与增强子重叠（caption）。
横纵轴定义：横向为 chr4 坐标，纵向为细胞类型轨道；阅读方向为找红竖线与增强子弧的交点。
颜色含义：红竖线=GWAS SNP，其余同 (F)。
核心结论：PD 风险变异落在小胶质与多巴胺亚型共享的候选增强子内，把 Section 2 的 LDSC 关联落到具体位点。

(J) rs1372518 对 RUNX3 motif 的等位效应
图片解释：上为 RUNX3 的 PWM logo，下为参考（A）与替代（C）等位的侧翼序列行，风险等位 C 强化 motif 匹配；标注 chr4:89,836,140 A>C 与 motifbreakR 等位效应 0.158。定量数据：效应 0.158（caption）。
横纵轴定义：无坐标轴（序列/logo 图）；阅读方向为对比两行序列中 motif 核心碱基。
颜色含义：碱基标准四色，等位差异位高亮。
核心结论：Lewy body 痴呆关联 SNP 通过增强 RUNX3 motif 提名一个疾病状态依赖的潜伏调控位点（ref69,70）。

补充材料角色：fig. S8 为 DMG/DEG 分组（S8A）、组蛋白/DMR 轮廓（S8B–S8D）、三证据连接数（S8E）、POU3F1/SLC35D3/DRD2 motif（S8F）与 GATA3 案例（S8G）。

### Section 6：MERFISH reveals MS compartmental differences in the striatum that extend beyond SPN identity（MERFISH 揭示纹状体 matrix–striosome 差异超越 SPN 身份）

内容逻辑：本节回答"matrix 与 striosome 的差异是否只是 SPN 分型在空间上的重述"。方法链是：先用 SPN 邻域组成向量（200 µm 半径内其他 SPN 的 group 计数向量）加 K-means（K=3）调用 MS score，再用连通域（≥5 细胞）凸包加 50 µm buffer 圈出两区室（STAR Methods）；该设计以 canonical D1S/D2S SPN 为先验锚，把区室定义与 SPN 身份解耦后回查其他细胞类型。核心发现三层。第一层细胞类型分布：沿 MS 梯度的分布符合 canonical SPN 预期（Fig. 6A），但也出现非 SPN 的区室偏置——MGE 来源的 CN ST18 GABA 富集 matrix（主要由 STR TAC3-PLPP4 GABA 驱动，Fig. 6B），CGE 来源的 CN LAMP5-CXCL14 GABA 与星形胶质细胞富集 striosome（fig. S10D–S10E）；D2 SMYD2 向 striosome 呈非显著趋势（Fig. 6B，弱效应如实报告），与 Section 4 的"striosome-leaning"全局身份呼应但不到显著。免疫组化复证（单供体 CaB，SLC22A3+/FGF13+/VIP− 组合因 TAC3 蛋白不限于胞体而采用）显示该群在 matrix 约为 striosome 的数倍（Fig. 6C）。第二层转录与表观：striosome 富集 TH、PDYN、SEMA3C、COL25A1、BACH2，matrix 富集 PCDH11X、SAMD5、GLP1R、HS3ST4、KIRREL3（Fig. 6D）；MS-DEGs 用区室分层 pseudobulk 加 PyDESeq2（供体协变量，FDR<0.001、|log2FC|>0.5、至少 2 区方向一致）调用，subclass 层 SPN 与 CN ST18 GABA 最多，group 层 striosome SPN 之后是 STR FS PTHLH-PVALB GABA（Fig. 6E–F）；SPN 的 RNA logFC 与 matrix-minus-striosome 基因体 mCH 差强负相关（r=−0.75，Fig. 6G），空间图确认 PDYN 在 NAC 例外（Fig. 6I）。第三层 FS 神经元的功能意义：对 MS-DEG 最多的非 SPN 群 STR FS PTHLH-PVALB GABA 重聚类，在 MERFISH、snm3C 与 HMBA 三个数据集检出一致的 striosome 富集亚型（fig. S11A–S11C）；89 个猕猴 Patch-seq 神经元经双重整合推断定位（9 个 striosome、72 个 matrix、8 个冲突剔除），matrix 细胞倾向更快放电、更窄动作电位（Fig. 6M–N），striosome 细胞更高表达 SCN9A（Nav1.7，调控兴奋性 ref72）与 CACNA1I（T 型钙通道，调控簇放电 ref73）（Fig. 6O）；作者如实声明电生理差异按效应量排序呈现，因 striosome 细胞数少无一特征通过 FDR 0.1——本节最重要的限定。MOXD1 亚型被首次赋予 striosome 解剖学意义（fig. S11H–S11I，呼应 ref14 曾报告的缺空间数据的 MOXD1 亚型）。本节的贡献是把组织学经典的 MS 结构升级为多细胞类型微环境：区室差异不仅是 SPN 身份，还包括中间神经元组成、星形胶质细胞分布与局部表达程序。

→ Figure 6 标题为"MERFISH reveals MS compartmental differences in the striatum that extend beyond SPN identity"，展示区室调用、富集验证、MS-DEG 与跨物种电生理。由 A 至 O 共 15 部分构成：A–D 分布与转录富集，E–G MS-DEG 总量与相关，H–L 区域模式与案例，M–O Patch-seq 与电生理，形成"空间-分子-功能"三段结构。

(A) 神经元 group 沿 MS 梯度的分布
图片解释：热图行 40 bins 从 S（striosome）到 M（matrix），行为神经元 group，格值为归一化细胞密度；行标签红字为 canonical striosome SPN、蓝字为 canonical matrix SPN。定量数据：每行 40 bins、逐行归一化（caption）；920 基因 panel。
横纵轴定义：横轴为梯度 bins（S→M），纵轴为 group；阅读方向为找每行密度峰位置。
颜色含义：蓝-白-红色阶为细胞密度低-高（读自图内色条）。
核心结论：canonical SPN 校准梯度方向，同时暴露 CN ST18 GABA 与 LAMP5-CXCL14 GABA 的区室偏置，为 (B) 提供靶标。

(B) group 层的区室富集森林图
图片解释：森林图，行为 group（粗体为显著的：STR TAC3-PLPP4 GABA、STR D1/D2 Matrix SPN、AMY-SLEA-BNST GABA、OT ICJ Granule、Astrocyte、LAMP5-CXCL14 GABA、STR D1 Striosome SPN 等），点为 log2FC 均值，横线为跨区域/供体/重复的 95% CI。定量数据：显著性 \*p<0.01、\*\*p<0.001、\*\*\*p<0.0001（FDR 校正，caption）；x 轴 −0.4 至 0.4。
横纵轴定义：横轴为 log2 fold-change（右正=matrix 富集，左侧标 S），纵轴为 group；阅读方向为看点相对 0 的位置与 CI 是否跨 0。
颜色含义：M/S 轴标签标示两侧方向，点色按 group。
核心结论：TAC3-PLPP4 GABA 显著 matrix 富集，LAMP5-CXCL14 GABA 显著 striosome 富集；D2 SMYD2 的 striosome 趋势不显著（如实保留）。

(C) 免疫组化的区室计数
图片解释：柱状图，横轴为 matrix/striosome/WM 三区，纵轴为 DAPI+ 细胞中 SLC22A3+/FGF13+/VIP− 细胞的百分比；单供体 CaB 实验。定量数据：读自图 matrix 约 1.2%、striosome 约 0.17%、WM 约 0.15%（原文未给精确数值）。
横纵轴定义：横轴为区室，纵轴为 % of total cells（0–1.4，读自图）；阅读方向为比较三柱高度。
颜色含义：三柱一色系。
核心结论：抗体层面独立方法复现 TAC3-PLPP4 GABA 的 matrix 富集；局限为单供体、抗体由 RNA 推断选择（Limitations 第 6 条）。

(D) 区室富集 top 30 转录本
图片解释：热图行 40 bins、行为基因（TH、PDYN、SEMA3C、COL25A1、BACH2 标 striosome 侧，KIRREL3、GLP1R、SAMD5、PCDH11X 标 matrix 侧），右侧条为 −log10 FDR，箭头标每侧前五。定量数据：top30（caption）。
横纵轴定义：横轴为梯度 bins，纵轴为转录本；阅读方向为比较左（S）右（M）两端行的深浅。
颜色含义：红-蓝色阶为基因区室侧别（读自图例），热图深浅为富集强度。
核心结论：区室转录签名明确且方向可复用为标记集。

(E) subclass 层 MS-DEG 数量
图片解释：横向条形图，行为 subclass（STR D1 SPN、STR D2 SPN、CN ST18 GABA、STR Eccentric SPN、CN VIP GABA、Microglia、Astrocyte），长为显著 MS-DEG 数。定量数据：读自图 STR D1 SPN 约 25 个居首（原文未给精确值）。
横纵轴定义：横轴为 MS-DEG 数（0–25，读自图），纵轴为 subclass；阅读方向为比较条长。
颜色含义：条色按 Neighborhood。
核心结论：SPN 与 CN ST18 GABA 是区室差异最大的两个 subclass，后者把非 SPN 群带入焦点。

(F) group 层 MS-DEG 数量
图片解释：与 (E) 同构，行为 group（STR D1 Striosome SPN、STR FS PTHLH-PVALB GABA、STRv D1 NUDAP SPN、Microglia、Astrocyte 等）。定量数据：读自图 striosome SPN 约 24、FS PTHLH-PVALB 约 17（原文未给精确值）。
横纵轴定义：同 (E)；阅读方向为找第二名的 FS 群。
颜色含义：同 (E)。
核心结论：STR FS PTHLH-PVALB GABA 是 MS-DEG 最多的非 SPN 神经元群，为 (J)–(O) 的功能分析选定对象。

(G) RNA logFC 与 mCH 差的相关散点
图片解释：散点图，横轴为 RNA logFC（M/S），纵轴为 matrix-minus-striosome 基因体 mCH 差，点为区域特异 subclass MS-DEGs，色为基因-区域对计数。定量数据：r=−0.75（caption 与正文）。
横纵轴定义：横轴 RNA 变化、纵轴 mCH 变化；阅读方向为看整体负斜率。
颜色含义：点密度色阶（读自图内色条）。
核心结论：区室表达差异与基因体低甲基化方向强一致，把 Section 2 的"低甲基化=活跃"规则推广到区室尺度。

(H) STR D1 SPN 的区域 MS-DEG 热图
图片解释：热图，行为按效应大小排序的 MS-DEGs（PCDH11X、IGFBP5 等），列为五个区域，格值为表达 log2FC 绝对值。定量数据：列色 brown=CaH、pink=CaB、orange=Pu、blue=NAC（caption）。
横纵轴定义：纵向为基因，横向为区域；阅读方向为逐行比较区域列。
颜色含义：红蓝为 matrix/striosome 富集方向（caption），列头色为区域。
核心结论：MS-DEG 的区室方向随区域变化，区域异质性真实存在。

(I) STR D1 SPN 的空间基因图
图片解释：上排五区（Pu/CaH/CaB/CaT/NAC）PDYN RNA 空间图，下排为 imputed PCDH11X 基因体 mCH 空间图；striosome 以黑线勾出。定量数据：比例尺 1.0 mm；RNA 色标约 0–1.1（读自图）。
横纵轴定义：无坐标轴（空间切片）；阅读方向为对照黑线轮廓看信号落位。
颜色含义：RNA 橙红高，mCH 蓝色阶。
核心结论：PDYN 除 NAC 外 striosome 富集，PCDH11X 在 matrix 低甲基化——空间、表达、表观三方互洽。

(J) STR FS PTHLH-PVALB GABA 的区域 log2FC 热图
图片解释：与 (H) 同构，行为该群 MS-DEGs（GLP1R、IGF2R、EPHA4、GRIK1、ZMAT4、ADRA1D、CALB2 等）。定量数据：同 (H)。
横纵轴定义：同 (H)；阅读方向为找 matrix 富集（GLP1R）与 striosome 富集行。
颜色含义：同 (H)。
核心结论：FS 群同样有清晰的区室转录程序，且含离子通道与受体基因。

(K) FS 群的空间案例图
图片解释：上排 GLP1R RNA 空间图（matrix 富集），下排 imputed CALB2 基因体 mCH 空间图（striosome 低甲基化，NAC 例外），黑线为 striosome 轮廓。定量数据：比例尺 1.0 mm。
横纵轴定义：同 (I)；阅读方向为对照轮廓。
颜色含义：同 (I)。
核心结论：FS 群的区室模式在空间上可直读，CALB2 的 NAC 例外提示区室-区域交互。

(L) FS 群 MS-DEGs 的 RNA-mCH 一致性散点
图片解释：散点，横轴为平均 RNA logFC（matrix/striosome），纵轴为平均 matrix-minus-striosome mCH 差，色为 concordance score，象限标注基因名（ALK、GALR2；ZMAT4、GRIK1、EPHA4 等）。定量数据：跨供体与区域平均后作图（caption）。
横纵轴定义：横轴 RNA 变化、纵轴 mCH 变化；阅读方向为看一致与不一致象限。
颜色含义：concordance score 色阶（读自图内色条）。
核心结论：多数 MS-DEG 两层一致，少数不一致者被点名，为后续机制研究提供分层清单。

(M) 猕猴 Patch-seq 神经元与 snm3C 的整合图
图片解释：UMAP 上小点为 snm3C 的 STR FS PTHLH-PVALB GABA 细胞，大圈点为 89 个猕猴 Patch-seq 细胞，颜色为预测区室（M/S）。定量数据：9 个 striosome、72 个 matrix、8 个冲突剔除（正文）。
横纵轴定义：无坐标轴（UMAP）；阅读方向为看大点颜色分布。
颜色含义：M 蓝、S 红（读自图例）。
核心结论：跨物种整合把电生理数据挂到区室标签上，两套独立整合（snm3C 桥与 HMBA 桥）一致才保留。

(N) 区室预测的电生理差异
图片解释：两组箱线/散点：左为平均最大放电率（avg rate max），右为 hero sweep 动作电位峰宽（width hero），横轴均为 M/S；点为细胞，条为中位数。定量数据：avg rate max r=0.63、width hero r=−0.58（rank-biserial 效应量，caption）；M 组更快更窄（正文）。
横纵轴定义：左图纵轴约 0–250（读自图），右图纵轴约 0.3–0.9 ms（读自图）；阅读方向为比较 M 与 S 中位线。
颜色含义：M 蓝、S 红。
核心结论：matrix FS 神经元倾向更快放电、更窄动作电位；因 striosome n=9，无特征通过 FDR 0.1，按效应量呈现——负性/受限结果如实声明。

(O) SCN9A 与 CACNA1I 的表达与甲基化
图片解释：两簇柱图（SCN9A、CACNA1I），每簇左为 HMBA 表达（M 蓝、S 红，带显著性星号）与右为 snm3C 基因体 mCH（斜纹柱），双纵轴。定量数据：HMBA 比较显著（读自图 \*\*\*；具体 FDR 值原文未提供）；snm3C mCH 呈 striosome 低甲基化（读自图）。
横纵轴定义：左纵轴为基因表达，右纵轴为 genebody mCH（约 0–0.08，读自图）；阅读方向为同簇两轴对照。
颜色含义：实心=HMBA 表达、斜纹=snm3C mCH；蓝=M、红=S。
核心结论：striosome FS 神经元高表达 SCN9A（Nav1.7，兴奋性 ref72）与 CACNA1I（T 型钙通道，簇放电 ref73），为 (N) 的电生理差异提供分子解释候选。

补充材料角色：fig. S9 为 MERFISH 注释与 D2 SMYD2 注释分；fig. S10 为白质调用、MS 区室调用、区室富集细节与免疫组化复证；fig. S11 为 FS 群重聚类（S11A–S11C）、Patch-seq 整合细节（S11D–S11I）与电生理全特征（S11J–S11K）。

---
（模块四、五与完成度声明见卷三：rerun_L3.md）

---

## 四、<Discussion结构分析>

**第 1 层：作者自陈主张（总括层）。** Discussion 开篇把本文定位为 BICAN 框架下的人类 BG 多组学图谱（ref21），以共识分类（ref38）为坐标系、可跨 RNA、ATAC、DNA 甲基化、HiC 与组蛋白修饰直接比较。三条主张最显眼：其一是"SPN 在细胞类型特异 hypo-DMR 模式上彼此最相似"，据此提出参与不同输出通路的 SPN 亚型在表观遗传上高度相近——这既是资源性发现，也限定了解读（防止把 SPN 亚型差异夸大为表观根本分歧）；其二是 GP 样本中捕获的 SPN 很可能来自相邻的 Pu 与腹侧 NAC，是对解剖混合效应的坦率承认；其三是 LDSC 未在多巴胺能神经元检出预期的 PD 遗传力富集（归因采样限制），却检出 F M GATA3 GABA 的关联，作者给出两条候选解释——经 SN GATA3-PVALB GABA 功能异常（ref74,75）或经 RN GATA3 GABA（红核代偿机制可掩盖 PD 症状，ref76）——并明确写"这些联系是否因果尚待确定"。此层的写法特征是把正性与负性结果并列陈述，不给负性结果找补。

**第 2 层：证据支撑层。** 第二段为 PD 与 SST 中间神经元的关联补外部证据：SST+ 中间神经元与 SST mRNA 在 PARK2 突变 iPSC 来源 GABA 神经元中减少（ref77），PARK2 突变还损害其线粒体功能（ref78），生长抑素调制 SPN 间反馈抑制（ref79），使 STR SST-CHODL GRIN2A GABA 环锚点的 PD 富集（fig. S6O）有跨文献支撑但仍是相关层面。3D 段承接并扩展既有观察：神经元染色体局部更紧、大尺度更松（ref51），非神经元接触距离更长，神经元长程互作集中于 A-B 区室间接触——作者据此提出"神经元长程连接性主要由区室间混合驱动"；同时引用伴文与本文一致显示 ATAC 与 H3K9me3 分不开 D1/D2 SPN（ref38,39），把模态分辨力边界写成集体结论。作者还主动指出 B 区室基因出现表达可能只是 100-kb 分辨率超过多数基因与调控域尺寸所致（ref80），防止读者把区室-表达错配读成生物学信号。区域层面以 PDE8B（ADSD，ref59,60）与 CADM1（PD 运动进展关联，ref81）两个疾病基因的前后梯度收尾，机制悬念留给功能研究。

**第 3 层：与既有图谱的差异。** 相对小鼠全脑单细胞甲基化图谱（ref85）与成年小鼠脑甲基化-3D 联合图谱（ref32），本文第一次把"甲基化+3D"双模态铺到人类深部核团；相对人类脑图谱 HBA（ref33），本文新增 BG 八区、并入 HBA 三供体数据统一重处理，把比较单位从"区域"细化到"区室与亚型"。与同期 BICAN 伴文的分工在 Discussion 中显式化：HMBA BG 共识分类（ref38）提供坐标系，Droplet Paired-Tag（ref39）提供组蛋白与 RNA 对照层，空间转录组伴文（ref52）提供跨物种空间参照，灵长类纹状体形态-电生理图谱（ref53）为 D2 SMYD2 的中间属性与 FS 群区室推断提供跨物种支点，enhancer-AAV 工具箱（ref61）为 GRN 提供病毒验证基准。作者还以 POU6F2 一例展示与既有知识的衔接：POU6F2 已被报告为后脑来源 SNr subclass 标记（与 PAX5、ZFPM2 共表达，ref58），而 D2 SMYD2 共享 POU6F2 与 ZFPM2 但缺 PAX5，据此判定其 LGE 端脑起源——是"继承前人标记、修正谱系归属"的范例。总体而言，本文在图谱生态中的位置是"调控层补位"而非重复造轮子。

**第 4 层：作者自陈局限（Limitations of the study 逐条列出）。** 原文设独立小节，共七条：第一条，snm3C-seq 数据来自七名年龄与性别不同的死后供体，统计功效不足以分离供体变异与年龄/性别效应，且样本神经元富集 80%；第二条，100-kb HiC 分辨率可能漏掉近缘亚型间更精细的架构差异；第三条，D2 SMYD2 虽多模态一致，仍需扰动式功能验证；第四条，E-P 连接与 TF-靶网络为计算预测，所回收的 enhancer-AAV 元件是在体内验证的，确认其在人类 BG 的特异性需非人灵长类体内实验或 iPSC 纹状体神经元的 CRISPRi 扰动；第五条，LDSC 富集是相关性的，对 DMR 覆盖基因组比例小的细胞类型可能产生假阳性；第六条，MERFISH 基因 panel 有限、CaT 切片含少量 striosome 斑块、免疫组化仅单供体且抗体选择依赖 RNA 来源标记、Patch-seq 数据来自猕猴；第七条，尽管关键发现有正交验证（TAC3-PLPP4 GABA 的免疫组化与 FS 群的跨物种 Patch-seq），多数调控关系仍是相关性的、需要功能检验。这七条分别对应样本设计、分辨率、新亚型、预测层、统计方法、空间技术与人种属外推六个维度的系统性边界。

**第 5 层：未回答的问题（Discussion 之外仍悬置的具体缺口）。** 其一，D2 SMYD2 亚型的功能必要性完全未验证——是否有独特的电生理或回路输入尚无任何直接测量，扰动实验（敲降/过表达 POU6F2）是第一优先；其二，LDSC 与疾病位点的因果链未建立：SNCA 增强子在 SN SOX6 Dopa 的可及性只是"提名共享调控模块"，等位特异功能只在小胶质中确立（ref66）；其三，SPN 的背-腹区域梯度是否构成连续区域程序仍是开放问题（作者原话）；其四，MS 区室差异的回路后果未测：CN ST18 GABA 的 matrix 富集与 FS 神经元的区室电生理差异如何影响 striosome/matrix 行为分工无任何功能性证据；其五，Dopa 群 LDSC 阴性的真实原因（采样、注释粒度或甲基化覆盖）未解析；其六，星形胶质细胞与 CN LAMP5-CXCL14 GABA 的 striosome 偏置机制（区室吸引还是谱系发育定位）未讨论；其七，人类与猕猴 FS 群电生理差异未做直接跨物种同特征比较，猕猴数据只用于区室归属推断；其八，GRN 中 TF-靶甲基化相关 |r|≥0.7 是跨细胞类型伪批量相关，不等于细胞内调控关系，其细胞水平验证完全缺位。

---

## 五、<重点思考>

### （一）核心概念/方法/通路/模型概括解读

- **核心概念——多模态表观基因组图谱：** 内涵是以同一分类坐标对齐 DNA 甲基化、3D 基因组、可及性、组蛋白修饰、表达与空间六层读数。重要之处在于疾病遗传学的解释单位是"细胞类型×调控元件"，单层图谱无法完成；本文推进在于给出人类 BG 的首个此类资源并附在线门户（basalganglia.epigenomes.net 与 SCMDAP）。边界：死后供体七人、神经元富集 80%，供体水平推断力有限。
- **核心方法——snm3C-seq 与共识分类对齐：** snm3C-seq（ref37）让同一核内甲基化与 3D 接触同测；本文的推进是把 HBA 数据统一重处理并与 HMBA 共识分类对齐（ref38），用跨模态 silhouette 基准量化各模态分辨力（fig. S2D–S2E）。边界：100-kb 分辨率与单细胞 HiC 稀疏性使 3D 层只能到亚型群粗层级。
- **核心通路——DMR→motif→ABC E-P→GRN：** 把低甲基化区域当候选增强子、用 motif 反演 TF、以接触频率与活性之积连接靶基因（ref89）。本文推进在于四级阈值过滤加 enhancer-AAV 基准（68.2%/50.0%）与 SNCA 位点的疾病落点（Fig. 5I–J）。边界：全链为计算预测，功能验证留给 CRISPRi/病毒时代。
- **核心模型——MS 微环境模型：** matrix 与 striosome 的差异不止于 SPN 身份，还包括中间神经元组成、星形胶质细胞分布与局部表达程序（Fig. 6）。本文推进在于用邻域组成向量把区室定义与 SPN 先验解耦后回查全部细胞类型，并以免疫组化与跨物种 Patch-seq 双重复证。边界：区室调用依赖 D1S/D2S 先验，电生理差异因 striosome n=9 未过显著性阈值。

### （二）本篇文章发现的完整概括

本文的出发点是人类 BG 一直缺少细胞类型分辨的表观基因组与 3D 基因组地图，而 PD、亨廷顿病、成瘾等疾病的细胞类型易感性亟需这张地图。作者以 snm3C-seq 覆盖八个 BG 亚区、七名供体，合并 HBA 数据后得到 261,331 个高质量细胞核（229,286 个带 3D 数据），在 HMBA 共识分类下产出 12 class、31 subclass、59 group 的表观组学分类，并用 silhouette 基准确立"mCH 分辨神经元亚型、HiC 只分非神经元"的模态边界。在甲基化层，鉴定出数百万个 DMR，经 motif 反演给出 MEIS2、POU6F2 等候选调控因子，经 LDSC 把 SPN 与 F M GATA3 GABA 的 hypo-DMR 接到 PD 等性状遗传力；在 3D 层，确立神经元短程紧凑、非神经元长程松散且区室化强的基准，并以 23.6 倍富集把差异域边界与"低甲基化+上调"基因焊接；在 SPN 层，把 D1/D2 细分为 matrix/striosome/ventral 并刻画 D2 SMYD2 亚型的中间调控位置与 POU6F2 五重调控证据；在调控层，构建 108,203 条 E-P 连接的 GRN，用增强子-AAV 工具箱回收 68.2%/50.0% 完成基准测试，并在 SNCA 位点为 PD 风险变异提名小胶质与多巴胺亚型共享的候选增强子；在空间层，MERFISH 邻域调用揭示 matrix/striosome 差异超越 SPN 身份，CN ST18 GABA 与星形胶质细胞分区分布，FS 中间神经元呈区室特异的分子与电生理差异。本文的领域贡献在于：给人类 BG 建立可检索的多模态调控资源与疾病-细胞类型配对框架；把纹状体经典组织学结构升级为多细胞类型微环境模型；以坦率的 Limitations 小节划定死后样本、分辨率与预测层的边界。须诚实声明：多数调控关系为相关性证据，功能机制有待扰动实验。

**七个子问题：**

**1. 研究问题定位：** 本文位于神经科学×表观基因组学×3D 基因组学交叉点，问题层级是"组学图谱与调控元件编目"层而非单分子机制层，工作类型为资源型兼概念推进（MS 微环境模型）；实验层级为死后人脑组织加计算分析，辅以单供体免疫组化与跨物种电生理再分析。一句话定位：为基底神经节疾病遗传学补上缺失的细胞类型×调控元件坐标系。

**2. 为什么能发 Cell（证据链评估）：** 最扎实处有三。其一，多模态互洽设计：D2 SMYD2 的刻画同时用了甲基化嵌入、3D 嵌入、判别 DMR 聚类与三套伴文数据（Fig. 4A–E；ref38,39,52,53），单一模态的结论不存在；其二，GRN 的正交基准：68.2%/50.0% 的 enhancer-AAV 回收率（Fig. 5E）是同类计算预测少有的量化基准，且两级定义（增强子层与 E-P 层）严格区分；其三，空间-表观-功能闭环：MS 区室调用、免疫组化复证与 Patch-seq 电生理方向一致（Fig. 6C、6N）。不足在功能落点：D2 SMYD2 无扰动验证，FS 电生理差异未过显著性阈值，E-P 预测未在人类组织做任何扰动检验。本文以正式发表版出现，BICAN 同期系列论文（ref38,39,44,52,53）互引构成证据生态，也是其发表形态的支撑。

**3. 创新点逐条列出：** 发现创新——人类 BG 八区首个单细胞甲基化与 3D 基因组联合图谱（Fig. 1）；发现创新——STR D2 SMYD2-HTR7 SPN 亚型的多模态刻画与 POU6F2 调控证据（Fig. 4I–J）；概念创新——MS 区室差异超越 SPN 身份的微环境模型（Fig. 6A–B）；方法创新——邻域组成向量调用 MS 区室并跨数据集推断 Patch-seq 细胞区室归属（Fig. 6M）；调和性贡献——把 3D 域边界与"低甲基化+上调"基因以 23.6 倍富集焊接（Fig. 3E–F）。

**4. 前置依赖：** 技术前置——snm3C-seq（ref37）、scHiCluster（ref86）、ALLCools（ref85）、Paired-Tag（ref110,111）、MERFISH 分割与去卷积工具（ref98,100,101）；生物学概念前置——BG 直接/间接通路（ref10,12,13）、神经节隆起发育谱系（ref20）、SPN 多样性（ref11,14）、MS 区室组织学；生信/统计前置——ABC 模型（ref89）、pycistarget/SCENIC+（ref90）、LDSC（ref91）、Harmony（ref88）、TopDom（ref121）、dcHiC（ref119）。

**5. 基因编辑/遗传操作细节：** 本文未涉及传统基因编辑；唯一的"操作"层为计算层面的供体特异参考基因组构建（WGS+GATK，把纯合 SNP 嵌入 hg38）与免疫组化标记组合（SLC22A3+/FGF13+/VIP−）的推理选择。设计价值：前者排除供体变异对甲基化与接触读数的混杂，后者绕开无经验证抗体的问题（TAC3 蛋白不限于胞体），但作者明示该组合由 RNA 推断且仅单供体。

**6. 与课题组/领域的关联：** 通讯作者 Behrens 与 Ecker 均在 Salk，长期合作产出单细胞甲基化图谱系列（ref32,33,85,114,115）；Ren（UCSD/Columbia）为 3D 基因组与 Paired-Tag 方向（ref89,110,111）；Allen Institute 成员（Hodge、Bakken、Lein）提供分类与解剖基建（ref38,107）。本文是 Ecker/Behrens 谱系"从皮层到深部核团、从单模态到多模态"的延伸（浅层谱系定位仅据 PDF 内引用关系，详细履历与传承见同源背景解读）。领域层面，BICAN 同期系列（ref21,38,39,44,52,53）与本文构成互引的共识生态。

**7. 数据与材料可及性：** snm3C-seq 原始与处理数据在 NeMO（assets.nemoarchive.org/dat-aw6czix）与 GEO GSE320293，另有 AWS Open Data 镜像；MERFISH 数据在 Brain Image Library（DOI 10.35077/g.1194）；代码在 GitHub DingWB/BG_snm3C-seq 并存档 Zenodo（DOI 10.5281/zenodo.23267620）；在线门户 basalganglia.epigenomes.net 与 neomorph.salk.edu/SCMDAP/BasalGanglia；伴文数据（HMBA 10x Multiome、Paired-Tag、猕猴 Patch-seq）在 NeMO 各自存档（STAR Methods Deposited data）。本文未生成新试剂；补充材料在线提供。

### （三）面向阅读的核心提问·问题 seeding

- **问题一：D2 SMYD2 是真实的细胞类型还是聚类的断裂产物？** 本文能答到什么程度：多模态一致（甲基化嵌入、判别 DMR、HMBA 定义、三套伴文与 POU6F2 五重调控证据，Fig. 4A–J），但无任何功能或扰动证据；证据强度初判：中（存在性与调控特征强，功能必要性为零）；交接：→ 待背景解读（paper-background-research）跨文献核对其在伴文 Patch-seq（ref53）中的形态-电生理属性细节。
- **问题二：PD 遗传力为何落在 SPN 与 F M GATA3 GABA 而不是多巴胺能神经元？** 本文能答到什么程度：作者只给"limited sampling"候选解释，并提示 F M GATA3 GABA 可能经 SN GATA3-PVALB（ref74,75）或 RN 代偿（ref76）；证据强度初判：弱（相关层面，且 LDSC 对小注释易假阳性）；交接：→ 待背景解读核证 RN 代偿文献链与 Dopa 注释覆盖度问题。
- **问题三：matrix/striosome 的 FS 电生理差异是区室效应还是细胞组成差异？** 本文能答到什么程度：同一 group（STR FS PTHLH-PVALB GABA）内部按预测区室比较（Fig. 6N），已控制类型身份，但 n=9 使无一特征通过 FDR 0.1，SCN9A/CACNA1I（Fig. 6O）只是分子候选；证据强度初判：中偏弱；交接：→ 待背景解读查伴文 Patch-seq（ref53）是否已有更大样本可复用。
- **问题四：SNCA 风险增强子在多巴胺神经元内是否真有等位特异功能？** 本文能答到什么程度：仅显示可及性与接触（Fig. 5I），作者明确写"提名共享调控模块而非建立机制"；等位功能只在小胶质确立（ref66）；证据强度初判：弱（提名级）；交接：→ 待背景解读综合 McClymont 2018（ref65）与 Booms 2024（ref66）的证据分级。

以上问题中，纯本文可答的已就地作答，其余转入同源《背景解读》做跨文献证据综合与分级。

### （四）延伸文献与图引清单

读者若需在组会或 PPT 中展开本文，下列文献按"论证依赖"与"方法来源"两类给出；前人图版 panel 编号未逐条核证，一律标"编号待核"，不编造。

**A. 论证依赖：**

| 序号 | 文献(年/刊/本文refNN) | 对应本文Fig/论点 | 重点前人Fig(panel) | 一句话讲点 | 获取/阅读深度 |
|---|---|---|---|---|---|
| ★A1 | Tian et al., Science 2023 (ref33) | Section 1 数据底座与 Fig. 1 分类 | 编号待核 | 人类脑单细胞甲基化与 3D 图谱首次覆盖多区域，本文直接并入其三供体数据 | 需订阅/本文定向核读 |
| ★A2 | Johansen et al., Cell 2026 (ref38) | 全文共识分类与 Fig. 4A D2 SMYD2 定义 | 编号待核 | HMBA BG 共识分类是所有模态对齐的坐标系 | 需订阅/仅书目 |
| A3 | Chang et al., Cell 2026 (ref39) | Fig. 3C/4 组蛋白对照层 | 编号待核 | Droplet Paired-Tag 提供同细胞 RNA 与三种组蛋白修饰对照 | 需订阅/仅书目 |
| ★A4 | Hunker et al., Neuron 2025 (ref61) | Fig. 5E 基准回收 | 编号待核 | 病毒验证的纹状体细胞类型特异增强子工具箱，是 GRN 的正交标尺 | 需订阅/仅书目 |
| A5 | Booms et al., iScience 2024 (ref66) | Fig. 5I SNCA 风险增强子 | 编号待核 | PD 风险等位在小胶质中改变 CTCF/RAD21 与 CEBPB 结合，等位功能唯一在体证据 | OA/仅书目 |
| A6 | Mendelsohn et al., Cell Rep 2025 (ref58) | Section 4/Discussion POU6F2 谱系 | 编号待核 | POU6F2 标记后脑来源 SNr 输出亚类，用于反推 D2 SMYD2 的 LGE 起源 | 需订阅/仅书目 |

**B. 方法来源：**

| 序号 | 文献(年/刊/本文refNN) | 对应本文Fig/论点 | 重点前人Fig(panel) | 一句话讲点 | 获取/阅读深度 |
|---|---|---|---|---|---|
| ★B1 | Lee et al., Nat Methods 2019 (ref37) | 全部甲基化与 3D 数据的物理基础 | 编号待核 | snm3C-seq 原始方法文：同一细胞核联合甲基化与 3C | 需订阅/本文定向核读 |
| B2 | Zhou et al., PNAS 2019 (ref86) | Fig. 3 全部 3D 分析 | 编号待核 | scHiCluster：单细胞 HiC 插值、聚类与环调用的算法基座 | OA/仅书目 |
| ★B3 | Fulco et al., Nat Genet 2019 (ref89) | Fig. 5 ABC 模型 | 编号待核 | ABC 模型以 CRISPR 扰动确立"活性×接触"预测 E-P 的定量规则 | 需订阅/仅书目 |
| B4 | Chen et al., Science 2015（DOI 10.1126/science.aaa6090） | Fig. 6 MERFISH 原理 | 编号待核 | MERFISH 用错误校正条码实现单分子多重 RNA 成像 | 需订阅/仅书目 |

---

## 解读完成度声明

**主图覆盖：** 主文 Fig. 1–6 全部 panel 共 68 个已按四字段模板（图片解释、横纵轴定义、颜色含义、核心结论）逐条解读，逐 Fig 分布为 Fig.1 共 7 个（A–G）、Fig.2 共 11 个（A–K）、Fig.3 共 10 个（A–J）、Fig.4 共 15 个（A–O）、Fig.5 共 10 个（A–J）、Fig.6 共 15 个（A–O）；Fig.5 的 (G)(H) 与 Fig.6 的多处 panel 因与同图前序 panel 版式同构，采用"同 (X)"式字段引用，四要素仍完整可读。

**补充材料处理方式：** fig. S1–S11 未随本 PDF 提供图版（已核实第 25–36 页为 STAR Methods 文本页，结构索引中"S 图版自 p25 起"的标注与实际不符），故各 S 图按正文与主图 caption 中的引用角色整合进对应 Section 的内容逻辑与 panel 核心结论，并在各 Section 末尾以"补充材料角色"汇总；Supplementary Tables S1–S11 未随附，文中引用的表号如实保留但未读其内容。

**视觉细节获取方式与局限：** 已用页面渲染图像实看 PDF 第 4、6、8、10、12、14 页（Fig.1–6 图版），panel 字母、坐标轴刻度、色标范围、比例尺与图例均据图核写并标注"读自图"；未逐页查看其余页面图像（正文文字以 paper.txt 为准）。sources\pages_hi 高清目录为空，实读使用 sources\pages 渲染图；图上无法辨认的个别数值（如 Fig.5E 柱上计数、Fig.6C 百分比）已标注"读自图约"或"原文未提供精确数值"。

**定量数据诚实声明：** 原文提供的定量（细胞数、DMR 计数、富集倍数、相关系数、百分比、P/FDR 阈值、效应量）全部原样引用；原文未提供的（多数图版单点底层数值、Fig.5E 计数、Fig.6C 精确百分比、电生理单特征 P 值）一律如实标注，未予虚构；电生理差异无特征通过 FDR 0.1 的负性结果、D2 SMYD2 的非显著 striosome 趋势与 Dopa LDSC 阴性均已如实呈现。

**公式/算法处理：** STAR Methods 中的 compartment strength 与 BB/AA 比值公式、区室富集统计框架与 rank-biserial 效应量公式以文字转述纳入本解读的统计框架段，未复现公式；算法参数（阈值、软件版本）按原文逐条转述。

**出版状态与 DOI：** 本文为正式发表版（Cell 189, 7386–7405，2026 年 11 月 12 日出版；DOI 10.1016/j.cell.2026.10.019；PMID 43020023，经 EuropePMC 核证）；其预印本版本（DOI 10.64898/2026.02.12.705594，2026-02-14 上线）已核证存在，本解读一律以正式版为准。

**延伸清单核证状态：** 延伸文献图引清单共 10 条（A 类 6 条、B 类 4 条），其中 9 条题录取自本文参考文献表（refNN 已核），1 条（Chen 2015 MERFISH）取自核证文件给出的 DOI；panel 编号 0 条已核实、10 条标注编号待核；阅读深度分两档，"本文定向核读"3 条、"仅书目"7 条。

**课本化背景补注汇总：** 共 4 节（单细胞 DNA 甲基化测序、3D 基因组与区室化、空间转录组、striosome–matrix 组织学与发育谱系），均独立成节并置于卷一（rerun_L1.md）模块二之后，每节六要素完整并以"来源与阅读深度"句收尾。

**figure 技术零基础自足自检：** 已逐 panel 核对"测什么物理量、信号来源、怎么读、颜色逐通道"四问：UMAP/热图/点图类说明输入特征与色阶物理含义；接触热图说明交联-连接信号来源与距离依赖读法；MERFISH 空间图说明荧光点即单分子转录本、DAPI 底图与细胞边界；弦图/circos/Venn/Sankey 说明阅读方向。通过。

**星号转义结论：** 全稿显著性星号均已写作字面转义形式（\*、\*\*、\*\*\*），加粗标记成对闭合，无裸露字面星号引发误渲染；本句内的转义符号本身即验证样例（\*）。