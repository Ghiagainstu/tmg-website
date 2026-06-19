import re
from pathlib import Path

WEBSITE = Path(r"C:\Users\fireh\WorkBuddy\20260326144402\tmg-website")

def get_read_time(html_path):
    """Extract read time from article HTML."""
    content = html_path.read_text(encoding='utf-8')
    match = re.search(r'article-read-time">([^<]+)', content)
    if match:
        return match.group(1)
    return None

def fix_index_cards(index_path, lang):
    """Fix batch article cards in index to include read-time."""
    content = index_path.read_text(encoding='utf-8')
    changed = False
    
    # Find all batch article cards with read-more but no read-time
    # Pattern: post-card__excerpt">...</p>\s*<span class="post-card__read-more">続きを読む →</span>\s*</a>
    pattern = re.compile(
        r'(post-card__excerpt">[^<]*</p>\s*)(<span class="post-card__read-more">続きを読む →</span>\s*</a>)',
        re.DOTALL
    )
    
    def fix_card(m):
        nonlocal changed
        before = m.group(1)
        after = m.group(2)
        
        # Extract slug from the href before this card
        # We need to find the slug from the surrounding context
        # For now, we'll skip this and use a different approach
        return m.group(0)
    
    # Alternative approach: find all cards and fix them
    # Pattern: href="/lang/blog/slug/" ... post-card__excerpt">...</p>\s*<span class="post-card__read-more">続きを読む →</span>\s*</a>
    pattern2 = re.compile(
        rf'(href="/{lang}/blog/([^"]*)/"[^>]*>.*?post-card__excerpt">[^<]*</p>\s*)(<span class="post-card__read-more">続きを読む →</span>\s*</a>)',
        re.DOTALL
    )
    
    def fix_card2(m):
        nonlocal changed
        before = m.group(1)
        slug = m.group(2)
        after = m.group(3)
        
        # Check if read-time already exists
        if 'post-card__read-time' in before:
            return m.group(0)
        
        # Get read time from article
        article_path = WEBSITE / f'{lang}/blog/{slug}.html'
        if not article_path.exists():
            return m.group(0)
        
        read_time = get_read_time(article_path)
        if not read_time:
            return m.group(0)
        
        # Replace read-more with read-time + arrow
        changed = True
        new_after = f'<span class="post-card__read-time">{read_time}</span>\n    <span class="post-card__arrow">続きを読む →</span>\n  </a>'
        return f'{before}{new_after}'
    
    content = pattern2.sub(fix_card2, content)
    
    if changed:
        index_path.write_text(content, encoding='utf-8')
        return True
    return False

# Fix JA and KO indexes
for lang in ['ja', 'ko']:
    idx = WEBSITE / f'{lang}/blog/index.html'
    if idx.exists():
        if fix_index_cards(idx, lang):
            print(f'Fixed {lang} index')
        else:
            print(f'No changes needed for {lang} index')
