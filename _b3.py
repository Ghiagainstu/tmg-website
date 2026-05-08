# -*- coding: utf-8 -*-
import re, os, sys

# Fix stdout encoding
sys.stdout.reconfigure(encoding='utf-8')

files = [
    'ad-billing-models-explained.html',
    'attribution-models-guide.html',
]
BASE = r'C:\Users\fireh\WorkBuddy\20260326144402\tmg-website\ja\blog'
OUT = r'C:\Users\fireh\WorkBuddy\20260326144402\tmg-website\_body_dump.txt'

lines = []
for fn in files:
    fp = os.path.join(BASE, fn)
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    title_match = re.search(r'<title>(.*?)</title>', content)
    desc_match = re.search(r'<meta name="description" content="(.*?)">', content)
    
    # Try different article markers
    for marker in ['<article class="article-content reveal">', '<article class="article-content">', '<article>']:
        start = content.find(marker)
        if start > 0:
            break
    
    if start < 0:
        lines.append("=== %s: NO <article> TAG FOUND ===" % fn)
        # Show what HTML tags are around the body area
        body_idx = content.find('<body>')
        if body_idx > 0:
            after_body = content[body_idx:body_idx+2000]
            lines.append("After <body>: " + after_body[:300])
        lines.append("")
        continue
    
    end = content.find('</article>', start)
    body = content[start:end] if end > start else ''
    
    lines.append("="*60)
    lines.append("File: %s" % fn)
    lines.append("Title: %s" % (title_match.group(1) if title_match else '?'))
    lines.append("Desc: %s" % (desc_match.group(1)[:120] if desc_match else '?'))
    lines.append("Body len: %d" % len(body))
    
    # Get body after opening tag
    tag_end = body.find('>') + 1
    body_text = body[tag_end:].strip()
    lines.append("Body start: %s" % body_text[:400])
    lines.append("Body end: ...%s" % body_text[-200:])
    lines.append("")

with open(OUT, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print("Written to _body_dump.txt")
