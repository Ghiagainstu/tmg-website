import re
from pathlib import Path

WEBSITE = Path(r"C:\Users\fireh\WorkBuddy\20260326144402\tmg-website")

def fix_index_card_footer(index_path, lang):
    """Add post-card__footer div to batch article cards."""
    content = index_path.read_text(encoding='utf-8')
    changed = False
    
    # Find cards without footer div
    # Pattern: post-card__excerpt">...</p>\s*<span class="post-card__read-time">...\s*<span class="post-card__arrow">...</span>\s*</a>
    # Should be: post-card__excerpt">...</p>\s*<div class="post-card__footer">\s*<span class="post-card__read-time">...\s*<span class="post-card__arrow">...</span>\s*</div>\s*</a>
    
    # Find all cards with read-time but no footer div
    pattern = re.compile(
        r'(post-card__excerpt">[^<]*</p>\s*)(<span class="post-card__read-time">[^<]*</span>\s*<span class="post-card__arrow">[^<]*</span>\s*</a>)',
        re.DOTALL
    )
    
    def add_footer(m):
        nonlocal changed
        before = m.group(1)
        after = m.group(2)
        
        # Check if footer div already exists
        if 'post-card__footer' in before:
            return m.group(0)
        
        # Add footer div
        changed = True
        return f'{before}<div class="post-card__footer">\n        {after.replace("</a>", "</div>\n    </a>")}'
    
    content = pattern.sub(add_footer, content)
    
    if changed:
        index_path.write_text(content, encoding='utf-8')
        return True
    return False

# Fix JA and KO indexes
for lang in ['ja', 'ko']:
    idx = WEBSITE / f'{lang}/blog/index.html'
    if idx.exists():
        if fix_index_card_footer(idx, lang):
            print(f'Fixed {lang} index')
        else:
            print(f'No changes needed for {lang} index')
