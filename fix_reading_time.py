import re
from pathlib import Path

WEBSITE = Path(r"C:\Users\fireh\WorkBuddy\20260326144402\tmg-website")

def fix_article(html_path):
    content = html_path.read_text(encoding='utf-8')
    changed = False
    
    # 1. Fix reading time based on word count
    body_match = re.search(r'article-content reveal\">(.*?)</article>', content, re.DOTALL)
    if body_match:
        body = body_match.group(1)
        text = re.sub(r'<[^>]+>', '', body)
        words = len(text.split())
        # For CJK characters, count characters instead of words
        cjk_chars = len(re.findall(r'[\u4e00-\u9fff\u3040-\u309f\u30a0-\u30ff\uac00-\ud7af]', text))
        if cjk_chars > 0:
            # CJK reading speed: ~400-500 characters per minute
            minutes = max(1, round(cjk_chars / 400))
        else:
            # English reading speed: ~200 words per minute
            minutes = max(1, round(words / 200))
        
        # Update reading time
        old_time = re.search(r'article-read-time">[^<]*', content)
        if old_time:
            new_time = f'article-read-time">{minutes} min read'
            content = content[:old_time.start()] + new_time + content[old_time.end():]
            changed = True
    
    # 2. Add gold accent to sidebar CTA
    # Check if sidebar-cta already has gold accent
    if 'sidebar-cta' in content and 'border-left: 3px solid var(--color-accent)' not in content:
        # Add gold accent border
        old_cta_css = '''    .sidebar-cta {
      margin-top: var(--space-6); background: var(--color-bg-card);
      border: 1px solid var(--color-border); border-radius: var(--radius-lg);
      padding: var(--space-5); text-align: center;
    }'''
        new_cta_css = '''    .sidebar-cta {
      margin-top: var(--space-6); background: var(--color-bg-card);
      border: 1px solid var(--color-border); border-left: 3px solid var(--color-accent);
      border-radius: var(--radius-lg); padding: var(--space-5); text-align: center;
    }'''
        
        if old_cta_css in content:
            content = content.replace(old_cta_css, new_cta_css)
            changed = True
    
    if changed:
        html_path.write_text(content, encoding='utf-8')
        return True
    return False

# Process all batch articles
batch_prefixes = ['baidu-', 'bilibili-', 'bing-china-', 'douyin-search-', 'douyin-content-', 
                  'douyin-brand-', 'douyin-ecommerce-', 'douyin-local-', 'douyin-sem-', 'douyin-live-',
                  'wechat-brand-zone-', 'wechat-channels-', 'wechat-mini-program-', 'wechat-mini-store-',
                  'wechat-omni-', 'wechat-private-', 'wechat-search-ads-', 'wechat-search-creative-',
                  'wechat-search-funnel-', 'wechat-service-', 'xiaohongshu-brand-zone-', 'xiaohongshu-category-',
                  'xiaohongshu-local-', 'xiaohongshu-product-', 'xiaohongshu-search-ads-', 'xiaohongshu-search-creative-',
                  'xiaohongshu-search-funnel-', 'xiaohongshu-search-koc-', 'xiaohongshu-search-omni-', 'xiaohongshu-search-seo-']

fixed = 0
for lang_dir in ['blog', 'ja/blog', 'ko/blog']:
    for prefix in batch_prefixes:
        for html in (WEBSITE / lang_dir).glob(f'{prefix}*.html'):
            if fix_article(html):
                fixed += 1

print(f"Fixed {fixed} articles")
