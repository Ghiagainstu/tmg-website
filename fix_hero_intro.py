import re
from pathlib import Path

WEBSITE = Path(r"C:\Users\fireh\WorkBuddy\20260326144402\tmg-website")

# Template texts to replace
TEMPLATE_INTROS = {
    'en': "Everything you need to know about Xiaohongshu advertising: Jiguang platform, KOL/KOC marketing, search ads, content strategy, and targeting.",
    'ja': "小紅書広告について知っておくべきすべて：聚光プラットフォーム、KOL/KOCマーケティング、検索広告、コンテンツ戦略、ターゲティング。",
    'ko': "샤오홍슈 광고에 대해 알아야 할 모든 것: 쥐광 플랫폼, KOL/KOC 마케팅, 검색 광고, 콘텐츠 전략, 타겟팅.",
}

def extract_first_paragraph(html_content, max_len=250):
    """Extract first <p> content from article body."""
    body_match = re.search(r'article-content reveal">(.*?)</article>', html_content, re.DOTALL)
    if not body_match:
        return None
    
    body = body_match.group(1)
    # Find first <p> tag
    p_match = re.search(r'<p>([^<]+(?:<[^>]+>[^<]*)*)</p>', body)
    if p_match:
        text = re.sub(r'<[^>]+>', '', p_match.group(1))
        if len(text) > max_len:
            text = text[:max_len].rsplit(' ', 1)[0] + '...'
        return text
    return None

def fix_hero_intro(html_path, lang):
    """Fix hero intro for a single article."""
    content = html_path.read_text(encoding='utf-8')
    
    template = TEMPLATE_INTROS.get(lang, '')
    if not template:
        return False
    
    # Check if this article has the template text
    if template not in content:
        return False
    
    # Extract first paragraph from article body
    new_intro = extract_first_paragraph(content)
    if not new_intro:
        return False
    
    # Replace template text
    content = content.replace(template, new_intro)
    html_path.write_text(content, encoding='utf-8')
    return True

# Process all batch articles
batch_prefixes = ['baidu-', 'bilibili-', 'bing-china-', 'douyin-search-', 'douyin-content-', 
                  'douyin-brand-', 'douyin-ecommerce-', 'douyin-local-', 'douyin-sem-', 'douyin-live-',
                  'wechat-brand-zone-', 'wechat-channels-', 'wechat-mini-program-', 'wechat-mini-store-',
                  'wechat-omni-', 'wechat-private-', 'wechat-search-ads-', 'wechat-search-creative-',
                  'wechat-search-funnel-', 'wechat-service-', 'xiaohongshu-brand-zone-', 'xiaohongshu-category-',
                  'xiaohongshu-local-', 'xiaohongshu-product-', 'xiaohongshu-search-ads-', 'xiaohongshu-search-creative-',
                  'xiaohongshu-search-funnel-', 'xiaohongshu-search-koc-', 'xiaohongshu-search-omni-', 'xiaohongshu-search-seo-']

fixed = 0
for lang, lang_dir in [('en', 'blog'), ('ja', 'ja/blog'), ('ko', 'ko/blog')]:
    for prefix in batch_prefixes:
        for html in (WEBSITE / lang_dir).glob(f'{prefix}*.html'):
            if fix_hero_intro(html, lang):
                fixed += 1

print(f"Fixed {fixed} articles")
