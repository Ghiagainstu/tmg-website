#!/usr/bin/env python3
"""Fix empty excerpts in KO index."""
import re
from pathlib import Path

WEBSITE = Path('.')

def get_excerpt_from_article(slug):
    """Get excerpt from article file."""
    filepath = WEBSITE / f'ko/blog/{slug}.html'
    if not filepath.exists():
        return None
    
    content = filepath.read_text(encoding='utf-8')
    
    # Try to get from article-hero__intro
    match = re.search(r'article-hero__intro">([^<]+)', content)
    if match and match.group(1).strip():
        return match.group(1).strip()
    
    # Try to get from first paragraph (skip empty ones)
    pattern = r'article-content reveal">\s*(?:<[^>]+>\s*)*<p>([^<]+)'
    match = re.search(pattern, content)
    if match and match.group(1).strip():
        return match.group(1).strip()
    
    return None

def fix_index():
    """Fix empty excerpts in index."""
    filepath = WEBSITE / 'ko/blog/index.html'
    content = filepath.read_text(encoding='utf-8')
    
    # Find all empty excerpts and get their slugs
    pattern = r'<a href="/ko/blog/([^"]*)/"[^>]*>.*?post-card__excerpt"></p>'
    
    def fix_match(match):
        slug = match.group(0).split('/ko/blog/')[1].split('/')[0]
        excerpt = get_excerpt_from_article(slug)
        if excerpt:
            # Truncate to 150 chars
            if len(excerpt) > 150:
                excerpt = excerpt[:147] + '...'
            return match.group(0).replace(
                'post-card__excerpt"></p>',
                f'post-card__excerpt">{excerpt}</p>'
            )
        return match.group(0)
    
    new_content = re.sub(pattern, fix_match, content, flags=re.DOTALL)
    
    if new_content != content:
        filepath.write_text(new_content, encoding='utf-8')
        return True
    return False

if fix_index():
    print('Fixed KO index')
else:
    print('No changes needed')
