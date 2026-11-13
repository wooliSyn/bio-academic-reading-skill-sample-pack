# -*- coding: utf-8 -*-
"""交付物结构与引用一致性检查。

用法: python check_deliverable.py <解读.md> [--lit|--bg]
  --lit 文献解读：五模块 + 四字段 + 延伸清单 + 背景补注
  --bg  背景解读：Pillar A/B + refs used-vs-defined 全定义全引用
默认按文件名自动判断（_文献解读 / _背景解读）。
"""
import re, sys, io, os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

if len(sys.argv) < 2:
    print('usage: check_deliverable.py <解读.md> [--lit|--bg]')
    sys.exit(1)

p = sys.argv[1]
if len(sys.argv) > 2:
    mode = sys.argv[2]
else:
    mode = '--lit' if '文献解读' in os.path.basename(p) else '--bg'

t = open(p, encoding='utf-8').read()
print('file:', os.path.basename(p))
print('chars:', len(t), '| lines:', t.count('\n') + 1, '| mode:', mode)

if mode == '--lit':
    for mod in ['一、<基础概念注释>', '二、<核心问题与方案>', '三、<逐节精读>',
                '四、<Discussion结构分析>', '五、<重点思考>', '解读完成度声明',
                '延伸文献', '背景补注']:
        print(mod, '->', t.count(mod))
    for f in ['图片解释', '横纵轴', '内容逻辑', '核心结论']:
        print('四字段', f, '->', t.count(f))
else:
    for k in ['Pillar A', 'Pillar B', 'References', '诚实收尾', '阅读顺序', '索引表']:
        print(k, '->', t.count(k))
    used = set(int(x) for x in re.findall(r'\[(\d{1,3})\]', t))
    defined = set(int(x) for x in re.findall(r'^\[(\d{1,3})\]', t, flags=re.M))
    print('refs used:', len(used), '| defined:', len(defined))
    print('used but undefined (bad if non-empty):', sorted(used - defined))
    print('defined but uncited (check):', sorted(defined - used))

print('escaped stars:', t.count('\\*'), '| bold-label ：**:', len(re.findall(r'：\*\*', t)))