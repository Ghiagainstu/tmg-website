#!/usr/bin/env python3
"""
Add hreflang tags to JA and KO blog articles.
EN articles should already have hreflang (check first).
"""
import os
import re

BASE = 'https://www.tuyuesouxin.cn'

def add_hreflang(filepath, lang):
    with open(filepath, 'r', encoding='utf-8') as f:
        c = f.read()
    
    # Check if hreflang already exists
    if 'hreflang=' in c:
        return False, 'already has hreflang'
    
    slug = os.path.basename(filepath).replace('.html', '')
    if slug == 'index':
        return False, 'index page (skip)'
    
    # Build hreflang tags
    tags = []
    if lang == 'ja':
        tags = [
            f'<link href="{BASE}/ja/blog/{slug}/" hreflang="ja" rel="alternate"/>',
            f'<link href="{BASE}/blog/{slug}/" hreflang="en" rel="alternate"/>',
            f'<link href="{BASE}/blog/{slug}/" hreflang="x-default" rel="alternate"/>',
        ]
    elif lang == 'ko':
        tags = [
            f'<link href="{BASE}/ko/blog/{slug}/" hreflang="ko" rel="alternate"/>',
            f'<link href="{BASE}/blog/{slug}/" hreflang="en" rel="alternate"/>',
            f'<link href="{BASE}/blog/{slug}/" hreflang="x-default" rel="alternate"/>',
        ]
    
    if not tags:
        return False, 'no tags'
    
    # Insert after <title> tag
    title_end = c.find('</title>')
    if title_end == -1:
        return False, 'no title tag'
    
    insert_pos = title_end + len('</title>')
    tags_str = '\n  ' + '\n  '.join(tags)
    c = c[:insert_pos] + tags_str + c[insert_pos:]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(c)
    return True, f'added {len(tags)} hreflang tags'

# Process JA articles
print('=== JA Blog Articles ===')
ja_count = 0
for f in sorted(os.listdir('ja/blog/')):
    if not f.endswith('.html') or f == 'index.html':
        continue
    fp = os.path.join('ja/blog', f)
    ok, msg = add_hreflang(fp, 'ja')
    if ok:
        print(f'  ✅ {f}')
        ja_count += 1
    else:
        print(f'  ⚠️  {f}: {msg}')

print(f'\nAdded hreflang to {ja_count} JA articles')

# Process KO articles
print('\n=== KO Blog Articles ===')
ko_count = 0
for f in sorted(os.listdir('ko/blog/')):
    if not f.endswith('.html') or f == 'index.html':
        continue
    fp = os.path.join('ko/blog', f)
    ok, msg = add_hreflang(fp, 'ko')
    if ok:
        print(f'  ✅ {f}')
        ko_count += 1
    else:
        print(f'  ⚠️  {f}: {msg}')

print(f'\nAdded hreflang to {ko_count} KO articles')
print('\nDone!')
