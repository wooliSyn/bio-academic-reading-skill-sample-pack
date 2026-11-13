# skill-regression-training 参考模板与脚本

本文件是 SKILL.md 的配套模板库。按需取用对应小节，不必全读。

## 1. 差距清单模板

```markdown
# 差距清单：{技能名} v{旧} → v{新}（对标：{标杆文件名}）

| 差距ID | 分类 | 标杆证据（摘录+位置） | 我方现状（摘录+位置） | 拟修订条款位置 | 优先级 |
|--------|------|----------------------|----------------------|----------------|--------|
| G1 | A事实错误 | "……"（标杆§2） | "……"（交付物L120） | §2.2 精度规则 | 高 |
| G2 | B遗漏 | 标杆有"延伸文献清单"节 | 无此节 | §重点思考（四） | 高 |
| G3 | C概念层 | 标题为问题/判断句 | 标题为干标签 | §1.7 文体 | 中 |
| G4 | D方法缺口 | 引用编号全部对账 | 无对账步骤 | §自检清单 | 中 |
```

分类定义：
- **A 事实错误**：与证据不符（作者贡献、日期、数值、图号）。修订方向=精度规则条款。
- **B 内容遗漏**：标杆有而我方无的模块/要素。修订方向=结构条款+完成度声明要素。
- **C 概念层**：文体、深度、可读性、技术零基础自足性。修订方向=文体/深度原则条款。
- **D 方法缺口**：流程/校验/工具缺失。修订方向=流程步骤+确定性校验脚本。

判定规则：只有"条款能防住"的差距进 patch；偶发执行失误记 pitfalls，不改条款。

## 2. 备份命名与版本格式

备份目录与文件：
```
workspace/{task}/skills-backup-v{旧A}-v{旧B}/
├── {技能A名}_SKILL.md
└── {技能B名}_SKILL.md
workspace/{task}/upgrade-backup/
└── {交付物名}_pre-v{新版本}.md
```

版本号三处同步示例（patch old→new）：
```
old: metadata:\n  version: 6.2.0\n---\n\n## 学术文献精读 Skill v6.2\n\n版本：v6.2（2026-11-13；v6.0 2026-10-11）
new: metadata:\n  version: 6.3.0\n---\n\n## 学术文献精读 Skill v6.3\n\n版本：v6.3（2026-11-13；v6.2 2026-11-13；v6.0 2026-10-11）
```

版本表行格式（长行，patch时用唯一尾部锚点）：
```
| v6.3 | 2026-11-13 | ①文体平衡原则 ②figure零基础自足性检验 ③延伸文献与图引清单 ④完成度声明要素同步。（与paper-background-research v1.3对齐） |
```

落位校验命令示例：
```bash
grep -nE "version: 6.3.0|Skill v6.3|新条款关键词|v6.3 \| 2026" "<技能目录>/{name}/SKILL.md"
```

## 3. 回归子代理 prompt 骨架

```
你是回归执行子代理。任务：{回归用例描述}。

1. 用技能加载机制加载 {技能名}（当前 vX.Y）。args 注明："重点检验 vX.Y 新条款：{条款列表}"。
   若 技能加载机制不可用，直接 Read {技能绝对路径}/SKILL.md 并严格遵循，且在产出中注明降级。
2. 目标交付物若已存在：先重新 Read 当前磁盘版，并备份到 {备份路径}，再增量修订（只增补不重写）。
3. 新写交付物一次 Write 成稿；确定性校验（引用对账/星号）用脚本。
4. 核证通道受阻的信息保守标"参考提供/编号待核"，不编造。
5. 返回：产出文件路径 + 摘要 + 关键指标（字数/引用数/新条款命中位置）。不要返回全文。
```

## 4. 增量修订脚本骨架（锚点唯一 + 可逆 + 一次写盘）

```python
import shutil, pathlib
SRC = pathlib.Path("交付物.md")
BAK = SRC.with_name(SRC.stem + "_before_fix.md")
shutil.copy(SRC, BAK)                      # 先备份
s = SRC.read_text(encoding="utf-8")
orig = s

INSERTS = [  # (锚点, 插入位置after/before, 补注文本)
    ("唯一锚点文本", "after", "\n\n> 补注：……"),
]
for anchor, pos, note in INSERTS:
    assert s.count(anchor) == 1, f"锚点失配/不唯一: {anchor!r} count={s.count(anchor)}"
    i = s.index(anchor) + (len(anchor) if pos == "after" else 0)
    s = s[:i] + note + s[i:]

# 可逆性校验：移除全部补注后必须还原为原文（证明只增不改）
t = s
for _, _, note in INSERTS:
    assert t.count(note) == 1
    t = t.replace(note, "", 1)
assert t == orig, "可逆性校验失败：发生了增补之外的改动"

SRC.write_text(s, encoding="utf-8")        # 一次写盘
```

精确替换（spot-fix）同样先断言唯一：
```python
FIXES = [("/ *；iMN", "/ \\*；iMN")]
for a, b in FIXES:
    assert s.count(a) == 1, a
    s = s.replace(a, b)
```

锚点失配排查：先 `print(repr(s[-120:]))` 看磁盘真实字符（直引号vs弯引号、全半角），再换 verified-unique 短尾锚点。

## 5. 引用编号对账脚本片段

```python
import re, pathlib
t = pathlib.Path("交付物.md").read_text(encoding="utf-8")
cited = set(int(x) for x in re.findall(r"\[(\d+)\]", t))
refsec = t.split("## References")[-1]      # 按实际文末标题调整
defined = set(int(x) for x in re.findall(r"^\[(\d+)\]", refsec, re.M))
print("cited-not-defined:", sorted(cited - defined))
print("defined-not-cited:", sorted(defined - cited))
print("CHARS:", len(t), "LINES:", t.count("\n") + 1)
```

删除/合并条目后需连续化重编号（补洞），重编号后再跑一次对账与星号检查。

## 6. 星号检查脚本片段与假阳性裁决

```python
import re, pathlib
t = pathlib.Path("交付物.md").read_text(encoding="utf-8")
runs = re.findall(r"(?<!\\)\*{3,}", t)          # 未转义的3+连星号
near = re.findall(r".{12}(?<!\\)\*[P<].{6}", t) # P值/< 附近的未转义星号
print("raw 3+ asterisk runs (bad if >0):", len(runs))
for m in near: print("REVIEW:", m)
```

裁决规则（命中必须逐条人工判定，不可直接宣布通过）：
- `**文字**，` → 合法加粗闭合，假阳性。
- `*Genetics*` → 期刊名斜体，假阳性。
- 星号紧邻标点/数字且表显著性（`（*；n=19/19`、`****P<0.0001`）→ 必须转义为 `\*`。
- 验收口径：加粗标签前后完好数 + 转义星号数 + 误伤数=0。

## 7. 比对表模板

```markdown
# 回归比对表：{技能名} v{新}（回归用例：{用例}）

| 差距ID | 核证来源 | 新条款位置 | 覆盖判定 |
|--------|----------|-----------|----------|
| G1 | 回归交付物L87："等贡献脚注逐字核对……" | §2.2 精度规则① | 已覆盖 |
| G2 | 回归交付物L490-510：延伸清单六列表 | §重点思考（四） | 已覆盖 |
| G3 | 标题仍为标签式（L12/L40） | §1.7 文体 | 部分覆盖（回归用例未暴露标题场景，需补用例） |
| G4 | 前人图号未联网核证 | §延伸清单 | 未覆盖（通道受阻，标"编号待核"，见残留声明） |
```

核证来源必须是具体位置（grep行号/段落摘录），禁止"我觉得覆盖了"。主线程抽查用 grep 定位 + 定向 Read 关键段，不全读。

## 8. sample pack 目录骨架与 README

```
skill-sample-pack/
├── skills/
│   ├── {技能A}/SKILL.md
│   └── {技能B}/SKILL.md
├── samples/
│   ├── {标杆}_文献解读.md + {标杆}_背景解读.md   # 标杆对
│   └── {样例}_文献解读.md + {样例}_背景解读.md   # 回归样例
├── gap-report-example.md    # 一份差距报告+比对表作范例
├── requirement-memory.md    # 需求记忆（非个人）
└── README.md
```

README 骨架：
```markdown
# {领域} skill sample pack

## 安装
把 skills/ 下各技能目录复制到 <技能目录>/
（Windows: <技能目录>\）。按所用 AI 的方式加载生效。

## 递归自训练（换AI/换电脑后如何继续进化）
跑技能产出交付物 → 对标标杆 → 差距清单(A/B/C/D) → 备份 → clause级patch
→ 子代理+技能加载机制正式加载回归 → 增量修订 → 比对表 → 残留差距声明。
完整规程见 skill-regression-training 技能；gap-report-example.md 是实例。

## 内容清单
（逐项列出文件与用途）
```

需求记忆边界清单：
- **只含**：质量标准（文体/深度/自足性）、避坑清单、完成度声明要求、格式要求（星号转义等）、核证通道偏好。
- **不含**：姓名/机构/私人路径等个人信息、私人数据、账号凭证。
- 目的：帮别的AI避坑、精准复现用户要的效果，而非携带用户画像。

## 9. token_log 表格式

```markdown
# token_log：{轮次}

| 环节 | 量 | 估算 token |
|------|----|-----------|
| PDF全文提取（一次提取复用） | {n}字符 | … |
| 图渲染（主图{n}@{dpi}dpi + crop） | {n} PNG | … |
| 技能加载 | {n}KB | … |
| 长文写作 + Edit回显 + 上下文累积 | 输出{n}字符 | … |

| 子代理 | 产出 | 估算 token | 最耗环节 |
|--------|------|-----------|----------|
| 子代理1 | … | … | 长文写作+Edit回显 |

结论：主线程 ~{n} vs 子代理 ~{n}；最耗环节诊断与下轮节省措施。
```

经验值：长文写作+Edit回显约占一半以上；真正不可省的只有生成文本本身。节省手段=一次Write、grep抽查、一次提取复用、重型任务进子代理。