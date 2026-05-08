# -*- coding: utf-8 -*-
import re, os

files = [
    'attribution-models-guide.html',
    'baidu-demographics-who-are-these-735m-users.html',
    'bilibili-demographics-who-are-these-gen-z-users.html',
]
BASE = r'C:\Users\fireh\WorkBuddy\20260326144402\tmg-website\ja\blog'
OUT = r'C:\Users\fireh\WorkBuddy\20260326144402\tmg-website\_batch_bodies.txt'

lines = []
for fn in files:
    fp = os.path.join(BASE, fn)
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    title_m = re.search(r'<title>(.*?)</title>', content)
    desc_m = re.search(r'<meta name="description" content="(.*?)">', content)
    
    # Find article body
    start = content.find('<article')
    end = content.find('</article>', start) if start > 0 else -1
    
    lines.append("="*70)
    lines.append("FILE: " + fn)
    lines.append("TITLE: " + (title_m.group(1) if title_m else '?'))
    lines.append("DESC: " + (desc_m.group(1)[:200] if desc_m else '?'))
    lines.append("BODY_START_OFFSET: %d" % start)
    lines.append("BODY_END_OFFSET: %d" % end)
    
    if start > 0 and end > start:
        body = content[start:end]
        tag_end = body.find('>') + 1
        body_text = body[tag_end:].strip()
        lines.append("BODY_LEN: %d" % len(body_text))
        # Show first 400 chars
        lines.append("BODY_PREVIEW: " + body_text[:500])
        lines.append("")
    else:
        lines.append("BODY: NOT FOUND")
        lines.append("")

with open(OUT, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))
print("Written to _batch_bodies.txt")
