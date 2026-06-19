import re
from pathlib import Path

WEBSITE = Path(r"C:\Users\fireh\WorkBuddy\20260326144402\tmg-website")

def get_article_title(html_path):
    """Extract title from article HTML."""
    content = html_path.read_text(encoding='utf-8')
    # Pattern: <title>... | TMG</title> or <h1 class="article-hero__title">...</h1>
    title_match = re.search(r'<title>([^|<]+)', content)
    if title_match:
        return title_match.group(1).strip()
    return None

def fix_index_titles(index_path, lang):
    """Fix English titles in index with translated titles from article files."""
    content = index_path.read_text(encoding='utf-8')
    changed = False
    
    # Find all post-card titles
    title_pattern = re.compile(r'post-card__title">([^<]+)')
    
    def replace_title(m):
        nonlocal changed
        en_title = m.group(1)
        
        # Skip if already in Japanese/Korean (contains CJK characters)
        if re.search(r'[\u4e00-\u9fff\u3040-\u309f\u30a0-\u30ff\uac00-\ud7af]', en_title):
            return m.group(0)
        
        # Find the corresponding article file
        # Extract slug from the href before this title
        # Pattern: href="/lang/blog/slug/" ... post-card__title">title
        return m.group(0)
    
    # Process each batch article
    batch_prefixes = ['baidu-', 'bilibili-', 'bing-china-', 'douyin-', 'wechat-', 'xiaohongshu-']
    
    for prefix in batch_prefixes:
        # Find all articles with this prefix in the index
        for match in re.finditer(rf'href="/{lang}/blog/({prefix}[^"]*)/"[^>]*>.*?post-card__title">([^<]+)', content, re.DOTALL):
            slug = match.group(1)
            en_title = match.group(2)
            
            # Skip if already translated
            if re.search(r'[\u4e00-\u9fff\u3040-\u309f\u30a0-\u30ff\uac00-\ud7af]', en_title):
                continue
            
            # Find the article file
            article_path = WEBSITE / f'{lang}/blog/{slug}.html'
            if not article_path.exists():
                continue
            
            # Get the translated title
            ja_title = get_article_title(article_path)
            if not ja_title or ja_title == en_title:
                continue
            
            # Replace in index
            old_pattern = f'post-card__title">{en_title}'
            new_pattern = f'post-card__title">{ja_title}'
            
            if old_pattern in content:
                content = content.replace(old_pattern, new_pattern)
                changed = True
    
    if changed:
        index_path.write_text(content, encoding='utf-8')
        return True
    return False

# Fix JA and KO indexes
for lang in ['ja', 'ko']:
    idx = WEBSITE / f'{lang}/blog/index.html'
    if idx.exists():
        if fix_index_titles(idx, lang):
            print(f"Fixed {lang} index")
        else:
            print(f"No changes needed for {lang} index")
