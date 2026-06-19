#!/usr/bin/env python3
"""Fix markdown in excerpts."""
import re
from pathlib import Path

WEBSITE = Path('.')

def fix_file(filepath):
    content = filepath.read_text(encoding='utf-8')
    
    # Find all excerpts with markdown
    pattern = r'post-card__excerpt">\*([^<]*)\*</p>'
    
    def replace_excerpt(match):
        excerpt = match.group(1)
        # Remove markdown formatting
        excerpt = excerpt.replace('*', '')
        return f'post-card__excerpt">{excerpt}</p>'
    
    new_content = re.sub(pattern, replace_excerpt, content)
    
    if new_content != content:
        filepath.write_text(new_content, encoding='utf-8')
        return True
    return False

fixed = 0
for lang in ['ja', 'ko']:
    filepath = WEBSITE / f'{lang}/blog/index.html'
    if filepath.exists():
        if fix_file(filepath):
            fixed += 1
            print(f'Fixed {lang}/blog/index.html')

print(f'\nTotal fixed: {fixed}')
