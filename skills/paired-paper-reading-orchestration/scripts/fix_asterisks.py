# -*- coding: utf-8 -*-
"""确定性星号转义 v2（保护优先 + 修复误转义的加粗开头）。

用法: python fix_asterisks.py <目标.md> <备份目录>

三步：
1 修复：把历史上被误转义的加粗开头 \\*\\*（后接编号/汉字/（ 且同行内有 ：** 闭合）还原为 **。
2 保护：加粗跨度 **…**（内容首字符非 ，；、）)空白*）与斜体 *…* 先替换为占位符，绝不改动。
3 转义：仅对保护圈外、统计显著性语境（前邻标点/数字/空白，后邻标点/数字/P</vs/NS/等）的 1–4 连星转义为 \\*。
安全：先备份；加粗标签(：**)与加粗跨度计数前后一致，不一致即中止不写盘。
"""
import re, sys, io, os, shutil

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

if len(sys.argv) < 3:
    print('usage: fix_asterisks.py <target.md> <backup_dir>')
    sys.exit(1)

p, bakdir = sys.argv[1], sys.argv[2]
os.makedirs(bakdir, exist_ok=True)
bak = os.path.join(bakdir, os.path.basename(p) + '.before_asterisk_fix')
shutil.copy(p, bak)
t = open(p, encoding='utf-8').read()

# 1) 修复被误转义的加粗开头（编号标题/汉字标题/（一）等，同行内有 ：** 闭合）
t = re.sub(r'\\\*\\\*(?=[0-9A-Za-z（(一二三四五六七八九十\u4e00-\u9fff][^\\\n*]{0,80}：\*\*)', '**', t)

bold_before = len(re.findall(r'：\*\*', t))
span_before = len(re.findall(r'\*\*[^*\n]+\*\*', t))
print('bold-label(：**) before:', bold_before, '| bold spans before:', span_before)

# 2) 保护加粗/斜体
store = []


def prot(m):
    store.append(m.group(0))
    return '\x01%d\x01' % (len(store) - 1)


s = re.sub(r'\*\*(?![，；、）)\s*])[^*\n]+?\*\*', prot, t)   # 加粗跨度
s = re.sub(r'\*[A-Za-z][A-Za-z0-9 .&/+-]*\*', prot, s)        # 英文斜体
s = re.sub(r'\*[^*\n]{1,300}\*', prot, s)                     # 中文/其他斜体

# 3) 保护圈外转义显著性星号
PUNCT_BEFORE = set('（(，,、；;0123456789 \t\n\x01')
PUNCT_AFTER = set('）)，,、；;0123456789 \t\n（\x01')


def esc(m):
    st = m.group(0)
    i, j = m.start(), m.end()
    before = s[i - 1] if i > 0 else '\n'
    after = s[j] if j < len(s) else '\n'
    tail = s[j:j + 4]
    if before in PUNCT_BEFORE and ((after in PUNCT_AFTER) or tail.startswith(('vs', 'P<', 'CTRL', 'NS')) or after == '等'):
        return '\\*' * len(st)
    return st


s = re.sub(r'\*{1,4}', esc, s)
new = re.sub(r'\x01(\d+)\x01', lambda m: store[int(m.group(1))], s)

bold_after = len(re.findall(r'：\*\*', new))
span_after = len(re.findall(r'\*\*[^*\n]+\*\*', new))
print('bold-label(：**) after :', bold_after, '| bold spans after:', span_after,
      '| escaped stars total:', new.count('\\*'))
assert bold_after == bold_before, 'BOLD LABEL INTEGRITY BROKEN — abort, no write'
assert span_after == span_before, 'BOLD SPAN INTEGRITY BROKEN — abort, no write'

open(p, 'w', encoding='utf-8').write(new)
print('OK written. backup:', bak)
for ln in new.split('\n'):
    if '\\*' in ln:
        print('sample:', ln[:90])
        break