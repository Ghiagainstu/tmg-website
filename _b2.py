# -*- coding: utf-8 -*-
import re, os

files = [
    'ad-billing-models-explained.html',
    'attribution-models-guide.html',
]
BASE = r'C:\Users\fireh\WorkBuddy\20260326144402\tmg-website\ja\blog'

for fn in files:
    fp = os.path.join(BASE, fn)
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    title_match = re.search(r'<title>(.*?)</title>', content)
    desc_match = re.search(r'<meta name="description" content="(.*?)">', content)
    
    start = content.find('<article class="article-content reveal">')
    end = content.find('</article>', start)
    body = content[start:end] if start > 0 else ''
    
    print('='*60)
    print('File:', fn)
    print('Title:', title_match.group(1) if title_match else '?')
    print('Desc:', desc_match.group(1)[:120] if desc_match else '?')
    print('Body len:', len(body))
    # Show article body content (skip CSS, just text)
    body_start = body.find('>\n') + 2
    print('Body start:', body[body_start:body_start+500])
    print()
