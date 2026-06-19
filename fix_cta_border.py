import re
from pathlib import Path

WEBSITE = Path(r"C:\Users\fireh\WorkBuddy\20260326144402\tmg-website")

def fix_cta_border(html_path):
    """Remove gold accent border from sidebar-cta to match reference article."""
    content = html_path.read_text(encoding='utf-8')
    
    # Pattern: sidebar-cta { ... border: 1px solid var(--color-border); border-left: 3px solid var(--color-accent); ... }
    old_pattern = 'border: 1px solid var(--color-border); border-left: 3px solid var(--color-accent);'
    new_pattern = 'border: 1px solid var(--color-border); border-radius: var(--radius-lg);'
    
    if old_pattern in content:
        # Only replace in sidebar-cta context
        # Find the sidebar-cta block
        cta_pattern = re.compile(r'(\.sidebar-cta \{[^}]*?)border: 1px solid var(--color-border); border-left: 3px solid var(--color-accent);([^}]*?\})', re.DOTALL)
        
        def replace_cta(m):
            return m.group(1) + 'border: 1px solid var(--color-border); border-radius: var(--radius-lg);' + m.group(2)
        
        content = cta_pattern.sub(replace_cta, content)
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
            if fix_cta_border(html):
                fixed += 1

print(f"Fixed {fixed} articles")
