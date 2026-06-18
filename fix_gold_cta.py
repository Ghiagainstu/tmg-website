import re
from pathlib import Path

WEBSITE = Path(r"C:\Users\fireh\WorkBuddy\20260326144402\tmg-website")

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
            content = html.read_text(encoding='utf-8')
            if old_cta_css in content:
                content = content.replace(old_cta_css, new_cta_css)
                html.write_text(content, encoding='utf-8')
                fixed += 1

print(f"Fixed {fixed} articles")
