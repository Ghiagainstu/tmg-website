#!/usr/bin/env python3
"""Layer 1 batch fix for TMG blog articles.
Fixes: hero intro, sidebar CTA, related posts, meta description, excerpts.
"""
import re, yaml
from pathlib import Path

WEBSITE = Path(r"C:\Users\fireh\WorkBuddy\20260326144402\tmg-website")
BATCH = Path(r"D:\WorkBuddy\Obsidian\TMG-Blog\Platform Topic Batch")

# Platform-specific CTA text
CTA = {
    'Baidu': {
        'en': {'title': 'Need help with Baidu ads?', 'text': 'TMG helps brands optimize Baidu search campaigns for maximum ROI.'},
        'ja': {'title': '百度広告でお困りですか？', 'text': 'TMGは百度検索キャンペーンの最適化をサポートします。'},
        'ko': {'title': '바이두 광고가 필요하신가요?', 'text': 'TMG는 바이두 검색 캠페인 최적화를 도와드립니다.'},
    },
    'Bilibili': {
        'en': {'title': 'Need help with Bilibili ads?', 'text': 'TMG helps brands reach Gen-Z audiences on Bilibili.'},
        'ja': {'title': 'Bilibili広告でお困りですか？', 'text': 'TMGはBilibiliでのZ世代リーチをサポートします。'},
        'ko': {'title': '빌리빌리 광고가 필요하신가요?', 'text': 'TMG는 빌리빌리에서 Z세대 도달을 도와드립니다.'},
    },
    'BingChina': {
        'en': {'title': 'Need help with Bing China ads?', 'text': 'TMG helps brands access China\'s premium audience via Bing.'},
        'ja': {'title': 'Bing中国広告でお困りですか？', 'text': 'TMGはBing経由での中国プレミアムオーディエンスへのアクセスをサポートします。'},
        'ko': {'title': '빙 중국 광고가 필요하신가요?', 'text': 'TMG는 빙을 통한 중국 프리미엄 오디언스 접근을 도와드립니다.'},
    },
    'Douyin': {
        'en': {'title': 'Need help with Douyin ads?', 'text': 'TMG helps brands run high-performance Douyin campaigns.'},
        'ja': {'title': '抖音広告でお困りですか？', 'text': 'TMGは高パフォーマンスの抖音キャンペーンをサポートします。'},
        'ko': {'title': '더우인 광고가 필요하신가요?', 'text': 'TMG는 고성능 더우인 캠페인을 도와드립니다.'},
    },
    'WeChat': {
        'en': {'title': 'Need help with WeChat ads?', 'text': 'TMG helps brands navigate WeChat advertising ecosystem.'},
        'ja': {'title': 'WeChat広告でお困りですか？', 'text': 'TMGはWeChat広告エコシステムのナビゲーションをサポートします。'},
        'ko': {'title': '위챗 광고가 필요하신가요?', 'text': 'TMG는 위챗 광고 생태계 탐색을 도와드립니다.'},
    },
    'Xiaohongshu': {
        'en': {'title': 'Need help with Xiaohongshu ads?', 'text': 'TMG helps brands build presence on China\'s top lifestyle platform.'},
        'ja': {'title': '小紅書広告でお困りですか？', 'text': 'TMGは中国最大のライフスタイルプラットフォームでのプレゼンス構築をサポートします。'},
        'ko': {'title': '샤오홍슈 광고가 필요하신가요?', 'text': 'TMG는 중국 최고의 라이프스타일 플랫폼에서의 프레즌스 구축을 도와드립니다.'},
    },
}

# Platform slug prefixes for related posts
PLATFORM_SLUGS = {
    'Baidu': 'baidu-',
    'Bilibili': 'bilibili-',
    'BingChina': 'bing-china-',
    'Douyin': 'douyin-',
    'WeChat': 'wechat-',
    'Xiaohongshu': 'xiaohongshu-',
}

def get_existing_articles():
    """Get all existing articles with their metadata."""
    articles = {}
    for html in WEBSITE.glob('blog/*.html'):
        if html.name == 'index.html':
            continue
        content = html.read_text(encoding='utf-8-sig')
        cat = re.search(r'article-category\">([^<]+)', content)
        title = re.search(r'<title>([^<|]+)', content)
        slug = html.stem
        if cat and title:
            articles[slug] = {
                'category': cat.group(1).strip(),
                'title': title.group(1).strip(),
                'slug': slug,
            }
    return articles

def clean_excerpt(text, max_len=200):
    """Strip markdown/HTML and create clean excerpt."""
    clean = re.sub(r'<[^>]+>', '', text)
    clean = re.sub(r'^#+\s+', '', clean, flags=re.MULTILINE)
    clean = re.sub(r'\*\*([^*]+)\*\*', r'\1', clean)
    clean = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', clean)
    clean = re.sub(r'\n\s*\n', ' ', clean)
    clean = clean.strip()
    if len(clean) > max_len:
        clean = clean[:max_len].rsplit(' ', 1)[0] + '...'
    return clean

def extract_first_paragraph(html_body):
    """Extract first <p> content from article body for hero intro."""
    match = re.search(r'<p>([^<]+(?:<[^>]+>[^<]*)*)</p>', html_body)
    if match:
        text = re.sub(r'<[^>]+>', '', match.group(1))
        if len(text) > 250:
            text = text[:250].rsplit(' ', 1)[0] + '...'
        return text
    return ''

def find_related_posts(slug, category, all_articles, count=3):
    """Find related posts from the same platform/category."""
    # Get platform prefix
    platform_prefix = None
    for platform, prefix in PLATFORM_SLUGS.items():
        if slug.startswith(prefix):
            platform_prefix = prefix
            break
    
    related = []
    for s, a in all_articles.items():
        if s == slug:
            continue
        # Prefer same platform
        if platform_prefix and s.startswith(platform_prefix):
            related.insert(0, a)
        # Then same category
        elif a['category'] == category:
            related.append(a)
    
    # If not enough, add from Paid Media Strategy
    if len(related) < count:
        for s, a in all_articles.items():
            if s == slug or a in related:
                continue
            if a['category'] == 'Paid Media Strategy':
                related.append(a)
            if len(related) >= count:
                break
    
    return related[:count]

def fix_article(html_path, platform, lang, all_articles):
    """Fix a single article HTML file."""
    content = html_path.read_text(encoding='utf-8-sig')
    slug = html_path.stem
    changed = False
    
    # 1. Fix hero intro - replace Xiaohongshu template text
    intro_match = re.search(r'(article-hero__intro">)([^<]+)', content)
    if intro_match and 'Xiaohongshu' in intro_match.group(2):
        # Extract from article body
        body_match = re.search(r'article-content reveal">(.*?)</article>', content, re.DOTALL)
        if body_match:
            new_intro = extract_first_paragraph(body_match.group(1))
            if new_intro:
                content = content[:intro_match.start(2)] + new_intro + content[intro_match.end(2):]
                changed = True
    
    # 2. Fix sidebar CTA
    cta_match = re.search(r'(sidebar-cta">)\s*<p>[^<]+</p>', content)
    if cta_match and platform in CTA and lang in CTA[platform]:
        cta_info = CTA[platform][lang]
        new_cta = f'{cta_match.group(1)}\n          <p>{cta_info["text"]}</p>'
        content = content[:cta_match.start()] + new_cta + content[cta_match.end():]
        changed = True
    
    # 3. Fix related posts
    related_match = re.search(r'(related__grid">)\s*(.*?)\s*(</div></div></section>)', content, re.DOTALL)
    if related_match:
        category = re.search(r'article-category">([^<]+)', content)
        category = category.group(1) if category else ''
        related = find_related_posts(slug, category, all_articles)
        
        if related:
            cards = []
            for r in related:
                r_cat = r['category']
                r_title = r['title']
                r_slug = r['slug']
                prefix = '/ja/' if lang == 'ja' else '/ko/' if lang == 'ko' else '/'
                cards.append(f'<a href="{prefix}blog/{r_slug}/" class="related-card"><div class="related-card__cat">{r_cat}</div><div class="related-card__title">{r_title}</div></a>')
            
            new_related = f'{related_match.group(1)}\n        ' + '\n        '.join(cards) + '\n    {related_match.group(3)}'
            content = content[:related_match.start()] + new_related + content[related_match.end():]
            changed = True
    
    # 4. Fix meta description - strip markdown
    meta_match = re.search(r'(meta name="description" content=")([^"]+)', content)
    if meta_match:
        desc = meta_match.group(2)
        if '#' in desc or '**' in desc:
            clean_desc = clean_excerpt(desc, 155)
            content = content[:meta_match.start(2)] + clean_desc + content[meta_match.end(2):]
            changed = True
    
    if changed:
        html_path.write_text(content, encoding='utf-8')
    
    return changed

def fix_index_excerpts(index_path, lang):
    """Fix excerpts in index.html - strip markdown."""
    content = index_path.read_text(encoding='utf-8-sig')
    changed = False
    
    # Find all excerpt spans
    def fix_excerpt_match(m):
        nonlocal changed
        excerpt = m.group(1)
        if '#' in excerpt or '**' in excerpt:
            clean = clean_excerpt(excerpt)
            changed = True
            return f'post-card__excerpt">{clean}'
        return m.group(0)
    
    content = re.sub(r'post-card__excerpt">([^<]+)', fix_excerpt_match, content)
    
    if changed:
        index_path.write_text(content, encoding='utf-8')
    
    return changed

def sort_index_cards(index_path, lang):
    """Sort index cards by date (newest first)."""
    content = index_path.read_text(encoding='utf-8-sig')
    
    # Find the posts-grid section
    grid_match = re.search(r'(<div class="posts-grid">)(.*?)(</div>\s*</section>)', content, re.DOTALL)
    if not grid_match:
        return False
    
    grid_content = grid_match.group(2)
    
    # Extract cards with dates
    cards = []
    for card_match in re.finditer(r'(<a href="[^"]*" class="post-card[^"]*">.*?</a>)', grid_content, re.DOTALL):
        card = card_match.group(1)
        date_match = re.search(r'post-card__date">([^<]+)', card)
        if date_match:
            date_str = date_match.group(1).strip()
            cards.append((date_str, card))
    
    # Sort by date (newest first)
    # Normalize date formats for comparison
    def date_sort_key(date_str):
        # Handle various formats: "June 18, 2026", "2026-06-18", "2026年6月18日", "2026년 6월 18일"
        months = {'January': 1, 'February': 2, 'March': 3, 'April': 4, 'May': 5, 'June': 6,
                  'July': 7, 'August': 8, 'September': 9, 'October': 10, 'November': 11, 'December': 12,
                  '1月': 1, '2月': 2, '3月': 3, '4月': 4, '5月': 5, '6월': 6,
                  '7월': 7, '8월': 8, '9월': 9, '10월': 10, '11월': 11, '12월': 12}
        
        # Try ISO format first
        iso_match = re.match(r'(\d{4})-(\d{2})-(\d{2})', date_str)
        if iso_match:
            return (int(iso_match.group(1)), int(iso_match.group(2)), int(iso_match.group(3)))
        
        # Try "Month DD, YYYY"
        en_match = re.match(r'(\w+)\s+(\d+),?\s+(\d{4})', date_str)
        if en_match and en_match.group(1) in months:
            return (int(en_match.group(3)), months[en_match.group(1)], int(en_match.group(2)))
        
        # Try "YYYY年M月D日"
        zh_match = re.match(r'(\d{4})年(\d+)月(\d+)日', date_str)
        if zh_match:
            return (int(zh_match.group(1)), int(zh_match.group(2)), int(zh_match.group(3)))
        
        # Try "YYYY년 M월 D일"
        ko_match = re.match(r'(\d{4})년\s*(\d+)월\s*(\d+)일', date_str)
        if ko_match:
            return (int(ko_match.group(1)), int(ko_match.group(2)), int(ko_match.group(3)))
        
        return (0, 0, 0)
    
    cards.sort(key=lambda x: date_sort_key(x[0]), reverse=True)
    
    # Rebuild grid
    new_grid = '\n'.join([card[1] for card in cards])
    new_content = (
        content[:grid_match.start()] +
        '<div class="posts-grid">\n' + new_grid + '\n' +
        '</div></section>' +
        content[grid_match.end():]
    )
    
    index_path.write_text(new_content, encoding='utf-8')
    return True

def main():
    all_articles = get_existing_articles()
    print(f"Found {len(all_articles)} existing articles")
    
    stats = {'hero': 0, 'cta': 0, 'related': 0, 'meta': 0}
    
    # Process each platform
    for platform in ['Baidu', 'Bilibili', 'BingChina', 'Douyin', 'WeChat', 'Xiaohongshu']:
        prefix = PLATFORM_SLUGS[platform]
        print(f"\n=== {platform} ===")
        
        for lang, lang_dir in [('en', 'blog'), ('ja', 'ja/blog'), ('ko', 'ko/blog')]:
            lang_path = WEBSITE / lang_dir
            for html in lang_path.glob(f'{prefix}*.html'):
                if fix_article(html, platform, lang, all_articles):
                    stats['hero'] += 1
                    print(f"  Fixed: {html.name}")
    
    # Fix index excerpts
    print(f"\n=== Fixing index excerpts ===")
    for lang, lang_dir in [('en', 'blog'), ('ja', 'ja/blog'), ('ko', 'ko/blog')]:
        idx = WEBSITE / lang_dir / 'index.html'
        if idx.exists():
            if fix_index_excerpts(idx, lang):
                stats['meta'] += 1
                print(f"  Fixed excerpts: {lang_dir}/index.html")
    
    # Sort index cards
    print(f"\n=== Sorting index cards ===")
    for lang, lang_dir in [('en', 'blog'), ('ja', 'ja/blog'), ('ko', 'ko/blog')]:
        idx = WEBSITE / lang_dir / 'index.html'
        if idx.exists():
            if sort_index_cards(idx, lang):
                print(f"  Sorted: {lang_dir}/index.html")
    
    print(f"\n{'='*60}")
    print(f"Summary:")
    print(f"  Articles fixed: {stats['hero']}")
    print(f"  Index excerpts fixed: {stats['meta']}")

if __name__ == "__main__":
    main()
