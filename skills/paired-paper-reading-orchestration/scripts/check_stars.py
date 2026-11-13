# -*- coding: utf-8 -*-
"""星号转义验证（v2：先剥离合法 markup 再判裸星，消除假阳性）。
用法: python check_stars.py <目标.md>

判定口径：先把合法 markup 掩掉——已转义 \\*、加粗跨度 **…**、英文期刊斜体 *X*、
中文/其他斜体 *…*(<=300字符)——再在剩余裸文本上检查：
  raw 3+星号串=0；星号紧邻 P/< =0；剩余裸星=0。
任一>0 即退出码1（可作门禁）；并打印上下文供人工裁决。
另独立输出加粗标签(：**)与加粗跨度计数，供与 fix_asterisks.py 的完整性锚点对账。
"""
import re, sys, io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

if len(sys.argv) < 2:
    print('usage: check_stars.py <target.md>')
    sys.exit(1)

t = open(sys.argv[1], encoding='utf-8').read()

# 完整性参考（原始文本上的合法 markup 计数）
print('bold-label(：**) count:', len(re.findall(r'：\*\*', t)))
print('bold ** pairs (raw):', t.count('**') // 2)


def mask_markup(s):
    s = s.replace('\\*', '\x00')                      # 已转义星号
    s = re.sub(r'\*\*[^*\n]+\*\*', '\x01', s)         # 加粗跨度（单行）
    s = re.sub(r'\*[A-Za-z][A-Za-z0-9 .&/+-]*\*', '\x02', s)  # 英文期刊斜体
    s = re.sub(r'\*[^*\n]{1,300}\*', '\x03', s)       # 中文/其他斜体 <=300
    return s


s = mask_markup(t)

runs = re.findall(r'\*{3,}', s)
print('raw 3+ asterisk runs after masking (bad if >0):', len(runs))

near = re.findall(r'.{0,12}\*[P<].{0,6}', s)
print('star before P/< after masking (bad if >0):', len(near))
for n in near[:10]:
    print('   ', n.replace('\n', ' '))

left = s.count('*')
print('remaining raw * after masking (bad if >0):', left)
for m in list(re.finditer(r'\*', s))[:15]:
    print('   leftover ctx:', s[max(0, m.start() - 25):m.start() + 25].replace('\n', ' '))

bad = len(runs) + len(near) + left
print('VERDICT:', 'PASS' if bad == 0 else 'FAIL(%d)' % bad)
sys.exit(0 if bad == 0 else 1)