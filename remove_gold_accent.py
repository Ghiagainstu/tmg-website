#!/usr/bin/env python3
"""Remove gold accent border-left from sidebar-cta in all batch articles."""
import re
from pathlib import Path

WEBSITE = Path('.')

def fix_file(filepath):
    content = filepath.read_text(encoding='utf-8')
    
    # Pattern: border: 1px solid var(--color-border); border-left: 3px solid var(--color-accent);
    old = 'border: 1px solid var(--color-border); border-left: 3px solid var(--color-accent);'
    new = 'border: 1px solid var(--color-border);'
    
    if old in content:
        content = content.replace(old, new)
        filepath.write_text(content, encoding='utf-8')
        return True
    return False

fixed = 0
for lang in ['ja', 'ko', 'blog']:
    pattern = f'{lang}/*.html' if lang == 'blog' else f'{lang}/blog/*.html'
    for filepath in WEBSITE.glob(pattern):
        if fix_file(filepath):
            fixed += 1

print(f'Fixed {fixed} files')
