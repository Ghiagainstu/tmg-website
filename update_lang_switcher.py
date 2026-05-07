#!/usr/bin/env python3
"""
Replace all individual language switcher links with a unified dropdown + flag icons.
Applies to ALL 54 pages (English root, ja/, ko/).
"""
import os, re

BASE = os.path.dirname(os.path.abspath(__file__))

# CSS to add before </style>
LANG_CSS = """
    /* ── Language Switcher Dropdown ── */
    .header__lang-wrap {
      position: relative;
      display: inline-flex;
      align-items: center;
      margin-left: 8px;
    }
    .header__lang-btn {
      display: inline-flex;
      align-items: center;
      gap: 5px;
      padding: 4px 10px;
      font-family: inherit;
      font-size: 12px;
      font-weight: 600;
      color: var(--c-accent, #c9a84c);
      background: transparent;
      border: 1px solid var(--c-accent, #c9a84c);
      border-radius: 6px;
      cursor: pointer;
      transition: background .15s;
      line-height: 1.4;
    }
    .header__lang-btn:hover { background: rgba(201,168,76,.1); }
    .header__lang-btn svg { transition: transform .15s; }
    .header__lang-wrap:hover .header__lang-btn svg,
    .header__lang-wrap.active .header__lang-btn svg { transform: rotate(180deg); }
    .header__lang-menu {
      position: absolute;
      top: calc(100% + 6px);
      right: 0;
      min-width: 140px;
      background: #111827;
      border: 1px solid #1e2d45;
      border-radius: 8px;
      padding: 4px;
      display: none;
      opacity: 0;
      box-shadow: 0 4px 20px rgba(0,0,0,.4);
      z-index: 300;
    }
    .header__lang-wrap:hover .header__lang-menu,
    .header__lang-wrap.active .header__lang-menu {
      display: flex;
      flex-direction: column;
      opacity: 1;
    }
    .header__lang-item {
      display: flex;
      align-items: center;
      gap: 6px;
      padding: 7px 10px;
      font-size: 12px;
      font-weight: 500;
      color: #a3b1cc;
      text-decoration: none;
      border-radius: 5px;
      transition: background .15s, color .15s;
      white-space: nowrap;
    }
    .header__lang-item:hover {
      background: rgba(201,168,76,.1);
      color: #e8c87a;
      text-decoration: none;
    }
    .header__lang-item--cur {
      color: #e8c87a;
      background: rgba(201,168,76,.08);
    }
    .header__lang-flag { font-size: 15px; line-height: 1; }
"""

# All language configs
LANG_CONFIG = {
    'en': {'label': 'English', 'flag': '🇺🇸', 'url': 'https://www.tuyuesouxin.cn'},
    'ja': {'label': '日本語',  'flag': '🇯🇵', 'url': 'https://www.tuyuesouxin.cn/ja'},
    'ko': {'label': '한국어',  'flag': '🇰🇷', 'url': 'https://www.tuyuesouxin.cn/ko'},
}

# Map file path → current language
def detect_lang(filepath):
    rel = filepath.replace(BASE + os.sep, '').replace('\\', '/')
    if rel.startswith('ja/'): return 'ja'
    if rel.startswith('ko/'): return 'ko'
    return 'en'

def build_dropdown(current_lang):
    """Build the dropdown HTML. Current language shown as button + not in dropdown."""
    items_html = ''
    for code, cfg in LANG_CONFIG.items():
        if code == current_lang:
            # Current lang: show as button
            btn = f'<span class="header__lang-flag">{cfg["flag"]}</span>{cfg["label"]}'
        else:
            items_html += f'<a href="{cfg["url"]}" class="header__lang-item"><span class="header__lang-flag">{cfg["flag"]}</span>{cfg["label"]}</a>\n          '
    
    return f'''<div class="header__lang-wrap">
        <button class="header__lang-btn" onclick="this.parentElement.classList.toggle('active')">
          {btn}
          <svg width="10" height="10" viewBox="0 0 10 10" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"><path d="M2 3.5l3 4 3-4"/></svg>
        </button>
        <div class="header__lang-menu">
          {items_html.strip()}
        </div>
      </div>'''

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    cur_lang = detect_lang(filepath)
    orig = content
    
    # 1. Add CSS before </style>
    if LANG_CSS.strip() not in content:
        content = content.replace('</style>', LANG_CSS + '\n  </style>', 1)
    
    # 2. Replace language switcher links
    dropdown_html = build_dropdown(cur_lang)
    
    # Replace the entire block between </nav> and header__cta with dropdown
    # First find the position of </nav> and <div class="header__cta">
    nav_end = content.find('</nav>')
    cta_start = content.find('<div class="header__cta">')
    
    if nav_end > 0 and cta_start > nav_end:
        # Extract the block between them
        block = content[nav_end + 6:cta_start]  # +6 for '</nav>'
        
        # Check if this block contains language switcher links
        if 'header__nav-link' in block and ('English' in block or '日本語' in block or '한국어' in block):
            # Replace the block with just the dropdown
            before = content[:nav_end + 6]
            after = content[cta_start:]
            content = before + '\n        ' + dropdown_html + '\n        ' + after
            modified = True
        else:
            modified = False
    else:
        modified = False
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def main():
    # Collect ALL HTML files across all three language directories
    all_files = []
    for root_dir in [BASE, os.path.join(BASE, 'ja'), os.path.join(BASE, 'ko')]:
        for root, dirs, files in os.walk(root_dir):
            for fn in files:
                if fn.endswith('.html'):
                    all_files.append(os.path.join(root, fn))
    
    # Only include files in root, ja/, ko/ (not deeper if any)
    filtered = []
    for fp in all_files:
        rel = fp.replace(BASE + os.sep, '').replace('\\', '/')
        if rel.startswith('ja/') or rel.startswith('ko/') or '/' not in rel:
            filtered.append(fp)
        elif rel.count('/') == 1 and not rel.startswith(('ja/', 'ko/')):
            filtered.append(fp)
    
    print(f'Processing {len(filtered)} files...')
    ok = 0
    fail = 0
    for fp in sorted(filtered):
        try:
            if process_file(fp):
                rel = fp.replace(BASE + os.sep, '').replace('\\', '/')
                print(f'  ✅ {rel}')
                ok += 1
            else:
                rel = fp.replace(BASE + os.sep, '').replace('\\', '/')
                print(f'  ℹ️ {rel} (no change)')
        except Exception as e:
            rel = fp.replace(BASE + os.sep, '').replace('\\', '/')
            print(f'  ❌ {rel}: {e}')
            fail += 1
    
    print(f'\nDone: {ok} updated, {fail} failed')

if __name__ == '__main__':
    main()
