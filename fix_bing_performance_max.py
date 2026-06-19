import re, yaml, markdown
from pathlib import Path

WEBSITE = Path(r"C:\Users\fireh\WorkBuddy\20260326144402\tmg-website")
OBSIDIAN = Path(r"D:\WorkBuddy\Obsidian\TMG-Blog")

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
    # Find Obsidian source
    obsidian_path = OBSIDIAN / 'BingChina' / 'Bing China Performance Max- Automated Campaign Optimization' / f'{lang.upper()}.md'
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
    article_pattern = re.compile(r'(<article class="article-content reveal">)(.*?)(</article>)', re.DOTALL)
    
    if article_pattern.search(html_content):
        html_content = article_pattern.sub(f'\\1\n{html_body}\n\\3', html_content)
        html_path.write_text(html_content, encoding='utf-8')
        return True
    
    return False

# Fix the article
slug = 'bing-china-performance-max-2026'
lang = 'ja'
print(f'Fixing {slug} ({lang})...')
if fix_article(slug, lang):
    print('Fixed')
else:
    print('Skipped')
