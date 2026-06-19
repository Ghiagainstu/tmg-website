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
    """Add read-time to batch article cards in index."""
    content = index_path.read_text(encoding='utf-8')
    changed = False
    
    # Find all batch article cards
    batch_prefixes = ['baidu-', 'bilibili-', 'bing-china-', 'douyin-', 'wechat-', 'xiaohongshu-']
    
    for prefix in batch_prefixes:
        # Find cards with this prefix
        pattern = re.compile(
            rf'(href="/{lang}/blog/({prefix}[^"]*)/"[^>]*>.*?post-card__excerpt">[^<]*</p>\s*)(</a>)',
            re.DOTALL
        )
        
        def add_readtime(m):
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
            
            # Add read-time before closing </a>
            changed = True
            return f'{before}<span class="post-card__read-time">{read_time}</span>\n    <span class="post-card__arrow">続きを読む →</span>\n  {after}'
        
        content = pattern.sub(add_readtime, content)
    
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
