import re
from pathlib import Path

WEBSITE = Path(r"C:\Users\fireh\WorkBuddy\20260326144402\tmg-website")

def fix_toc(html_path, lang):
    """Fix TOC links to use translated h2 headers."""
    content = html_path.read_text(encoding='utf-8')
    
    # Extract h2 headers from article body
    h2_pattern = re.compile(r'<h2[^>]*id="([^"]*)"[^>]*>([^<]+)</h2>')
    h2_headers = h2_pattern.findall(content)
    
    if not h2_headers:
        return False
    
    # Build TOC from h2 headers
    toc_items = []
    for h2_id, h2_text in h2_headers:
        toc_items.append(f'<li><a href="#{h2_id}" class="toc__link">{h2_text}</li>')
    
    new_toc = '\n            '.join(toc_items)
    
    # Find and replace existing TOC
    toc_pattern = re.compile(r'<ul class="toc__list">(.*?)</ul>', re.DOTALL)
    
    if toc_pattern.search(content):
        content = toc_pattern.sub(f'<ul class="toc__list">\n            {new_toc}\n          </ul>', content)
        html_path.write_text(content, encoding='utf-8')
        return True
    
    return False

# Process all batch articles
batch_prefixes = ['baidu-', 'bilibili-', 'bing-china-', 'douyin-', 'wechat-', 'xiaohongshu-']

fixed = 0
for lang in ['ja', 'ko']:
    lang_dir = WEBSITE / f'{lang}/blog'
    for prefix in batch_prefixes:
        for html in lang_dir.glob(f'{prefix}*.html'):
            if fix_toc(html, lang):
                fixed += 1

print(f"Fixed {fixed} articles")
