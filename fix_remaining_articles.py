import re, yaml, markdown
from pathlib import Path

WEBSITE = Path(r"C:\Users\fireh\WorkBuddy\20260326144402\tmg-website")
OBSIDIAN = Path(r"D:\WorkBuddy\Obsidian\TMG-Blog")

# Map slugs to Obsidian folder names (corrected)
SLUG_TO_FOLDER = {
    'bilibili-youth-search-ads': 'Youth Search Ads on Bilibili- Capturing the Next Generation',
    'bing-china-cross-border-search-ads': 'Cross-Border Search Ads on Bing China',
    'bing-china-travel-search-ads': 'Bing China Travel Search Ads- Reaching Travelers',
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
    html = markdown.markdown(md_content, extensions=['tables', 'fenced_code'])
    html = html.replace('<table>', '<table class="article-table">')
    html = html.replace('<blockquote>', '<blockquote class="callout callout--accent">')
    return html

def fix_article(slug, lang):
    """Fix a single article by reading from Obsidian and updating HTML."""
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
    
    md_content = obsidian_path.read_text(encoding='utf-8-sig')
    fm, body = parse_frontmatter(md_content)
    html_body = convert_md_to_html(body)
    
    html_path = WEBSITE / f'{lang}/blog/{slug}.html'
    if not html_path.exists():
        print(f'  HTML not found: {html_path}')
        return False
    
    html_content = html_path.read_text(encoding='utf-8')
    article_pattern = re.compile(r'(<article class="article-content reveal">)(.*?)(</article>)', re.DOTALL)
    
    if article_pattern.search(html_content):
        html_content = article_pattern.sub(f'\\1\n{html_body}\n\\3', html_content)
        html_path.write_text(html_content, encoding='utf-8')
        return True
    
    return False

# Fix remaining articles
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
