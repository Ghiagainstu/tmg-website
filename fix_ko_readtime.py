import re
from pathlib import Path

idx = Path('ko/blog/index.html')
content = idx.read_text(encoding='utf-8')

# Replace read-more with read-time + arrow
pattern = re.compile(r'href="/ko/blog/([^"]*)/"[^>]*>.*?post-card__excerpt">[^<]*</p>\s*<span class="post-card__read-more">続きを読む →</span>\s*</a>', re.DOTALL)

def fix_card(m):
    slug = m.group(1)
    article_path = Path(f'ko/blog/{slug}.html')
    if not article_path.exists():
        return m.group(0)
    
    article_content = article_path.read_text(encoding='utf-8')
    read_time_match = re.search(r'article-read-time">([^<]+)', article_content)
    if not read_time_match:
        return m.group(0)
    
    read_time = read_time_match.group(1)
    
    old = '<span class="post-card__read-more">続きを読む →</span>'
    new = f'<span class="post-card__read-time">{read_time}</span>\n    <span class="post-card__arrow">続きを読む →</span>'
    
    return m.group(0).replace(old, new)

content = pattern.sub(fix_card, content)
idx.write_text(content, encoding='utf-8')
print('Fixed KO index')
