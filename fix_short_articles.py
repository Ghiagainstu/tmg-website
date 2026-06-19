import re, yaml, markdown
from pathlib import Path

WEBSITE = Path(r"C:\Users\fireh\WorkBuddy\20260326144402\tmg-website")
OBSIDIAN = Path(r"D:\WorkBuddy\Obsidian\TMG-Blog")

# Map slugs to Obsidian folder names
SLUG_TO_FOLDER = {
    'bilibili-search-content-matching': 'Bilibili Search Content Matching',
    'bilibili-search-creative-lab': 'Bilibili Search Creative Lab',
    'bilibili-search-funnel-guide': 'Bilibili Search Funnel Guide- Awareness to Conversion',
    'bilibili-search-performance-2026': 'Bilibili Search Performance 2026',
    'bilibili-youth-search-ads': 'Bilibili Youth Search Ads',
    'bing-china-b2b-search-2026': 'Bing China B2B Search Ads- The Enterprise Opportunity',
    'bing-china-brand-search-2026': 'Bing China Brand Search 2026- Premium Placement Strategy',
    'bing-china-copilot-search-ads': 'Bing China Copilot Search Ads- AI-Native Advertising',
    'bing-china-cross-border-search-ads': 'Bing China Cross-Border Search Ads',
    'bing-china-education-search-ads': 'Bing China Education Search Ads- Reaching Students',
    'bing-china-local-search-ads': 'Bing China Local Search Ads- Geo-Targeted Advertising',
    'bing-china-performance-max-2026': 'Bing China Performance Max- Automated Campaign Optimization',
    'bing-china-retail-search-ads': 'Bing China Retail Search Ads- E-Commerce on Microsoft',
    'bing-china-search-creative-guide': 'Bing China Search Creative Guide- Best Practices',
    'bing-china-travel-search-ads': 'Bing China Travel Search Ads',
}

# Map slugs to platform folders
SLUG_TO_PLATFORM = {
    'bilibili-': 'Bilibili',
    'bing-china-': 'BingChina',
}

def get_platform_folder(slug):
    for prefix, platform in SLUG_TO_PLATFORM.items():
        if slug.startswith(prefix):
            return platform
    return None

def parse_frontmatter(content):
    if content.startswith('---') or content.startswith('\ufeff---'):
        start = content.index('---')
        end = content.index('---', start + 3)
        fm = yaml.safe_load(content[start+3:end])
        body = content[end+3:].strip()
        return fm, body
    return {}, content

def convert_md_to_html(md_content):
    """Convert markdown to HTML with proper formatting."""
    # Convert markdown to HTML
    html = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])
    
    # Add TMG-specific CSS classes
    html = html.replace('<table>', '<table class="article-table">')
    html = html.replace('<blockquote>', '<blockquote class="callout callout--accent">')
    
    return html

def fix_article(slug, lang):
    """Fix a single article by reading from Obsidian and updating HTML."""
    # Find Obsidian source
    platform = get_platform_folder(slug)
    if not platform:
        return False
    
    folder_name = SLUG_TO_FOLDER.get(slug)
    if not folder_name:
        return False
    
    obsidian_path = OBSIDIAN / platform / folder_name / f'{lang.upper()}.md'
    if not obsidian_path.exists():
        print(f'  Obsidian not found: {obsidian_path}')
        return False
    
    # Read Obsidian source
    md_content = obsidian_path.read_text(encoding='utf-8-sig')
    fm, body = parse_frontmatter(md_content)
    
    # Convert to HTML
    html_body = convert_md_to_html(body)
    
    # Read existing HTML file
    html_path = WEBSITE / f'{lang}/blog/{slug}.html'
    if not html_path.exists():
        print(f'  HTML not found: {html_path}')
        return False
    
    html_content = html_path.read_text(encoding='utf-8')
    
    # Find and replace article content
    # Pattern: <article class="article-content reveal">...</article>
    article_pattern = re.compile(r'(<article class="article-content reveal">)(.*?)(</article>)', re.DOTALL)
    
    if article_pattern.search(html_content):
        html_content = article_pattern.sub(f'\\1\n{html_body}\n\\3', html_content)
        html_path.write_text(html_content, encoding='utf-8')
        return True
    
    return False

# Fix all short articles
fixed = 0
for slug in SLUG_TO_FOLDER.keys():
    for lang in ['ja', 'ko']:
        print(f'Fixing {slug} ({lang})...')
        if fix_article(slug, lang):
            fixed += 1
            print(f'  Fixed')
        else:
            print(f'  Skipped')

print(f'\nFixed {fixed} articles')
