#!/usr/bin/env python3
"""Fix dropdown left:50% centering issue across all TMG HTML files."""
import os, re

files = [
    'why-tmg/index.html',
    'services/xiaohongshu/index.html',
    'services/wechat/index.html',
    'services/index.html',
    'services/douyin/index.html',
    'services/bing/index.html',
    'services/bilibili/index.html',
    'services/baidu/index.html',
    'pricing/index.html',
    'geo/index.html',
    'contact/index.html',
    'client-stories/index.html',
    'blog/xiaohongshu-consumer-research.html',
    'blog/pangle-ads.html',
    'blog/ocean-engine-overview.html',
    'blog/ocean-engine-local-reach.html',
    'blog/ocean-engine-ai-assistant.html',
    'blog/index.html',
    'blog/douyin-enterprise-account.html',
    'blog/bilibili-genz-marketing.html',
    'about/index.html',
]

# The OLD dropdown CSS pattern (left: 50%) - homepage version
old_dropdown = """    .header__dropdown-menu {
      position: absolute;
      top: 100%;
      left: 50%;
      transform: translateX(-50%);
      background: var(--color-bg-card);
      border: 1px solid var(--color-border);
      border-radius: 10px;
      padding: 8px var(--space-2) var(--space-2);
      min-width: 180px;
      display: none;
      opacity: 0;
      box-shadow: var(--shadow-lg);
      transition: opacity var(--transition-fast), transform var(--transition-fast);
      z-index: 100;
    }

    .header__dropdown:hover .header__dropdown-menu,
    .header__dropdown:focus-within .header__dropdown-menu,
    .header__dropdown.open .header__dropdown-menu {
      display: flex;
      flex-direction: column;
      opacity: 1;
      transform: translateX(-50%) translateY(0);
      transition: opacity var(--transition-fast), transform var(--transition-fast);
    }"""

# Blog pages use rgba(0,0,0,.4) shadow instead of var(--shadow-lg)
old_dropdown_blog = """    .header__dropdown-menu {
      position: absolute;
      top: 100%;
      left: 50%;
      transform: translateX(-50%);
      background: var(--color-bg-card);
      border: 1px solid var(--color-border);
      border-radius: 10px;
      padding: 8px var(--space-2) var(--space-2);
      min-width: 180px;
      display: none;
      flex-direction: column;
      opacity: 0;
      box-shadow: 0 8px 32px rgba(0,0,0,.4);
      transition: opacity var(--transition-fast);
      z-index: 100;
    }

    .header__dropdown:hover .header__dropdown-menu,
    .header__dropdown.open .header__dropdown-menu {
      display: flex;
      flex-direction: column;
      opacity: 1;
    }"""

new_dropdown = """    .header__dropdown-menu {
      position: absolute;
      top: calc(100% + 8px);
      left: 0;
      background: var(--color-bg-card);
      border: 1px solid var(--color-border);
      border-radius: 10px;
      padding: 8px var(--space-2) var(--space-2);
      min-width: 180px;
      display: none;
      opacity: 0;
      box-shadow: var(--shadow-lg);
      transition: opacity var(--transition-fast), transform var(--transition-fast);
      z-index: 100;
    }

    .header__dropdown:hover .header__dropdown-menu,
    .header__dropdown:focus-within .header__dropdown-menu,
    .header__dropdown.open .header__dropdown-menu {
      display: flex;
      flex-direction: column;
      opacity: 1;
      transform: translateY(0);
      transition: opacity var(--transition-fast), transform var(--transition-fast);
    }"""

new_dropdown_blog = """    .header__dropdown-menu {
      position: absolute;
      top: calc(100% + 8px);
      left: 0;
      background: var(--color-bg-card);
      border: 1px solid var(--color-border);
      border-radius: 10px;
      padding: 8px var(--space-2) var(--space-2);
      min-width: 180px;
      display: none;
      flex-direction: column;
      opacity: 0;
      box-shadow: 0 8px 32px rgba(0,0,0,.4);
      transition: opacity var(--transition-fast);
      z-index: 100;
    }

    .header__dropdown:hover .header__dropdown-menu,
    .header__dropdown.open .header__dropdown-menu {
      display: flex;
      flex-direction: column;
      opacity: 1;
    }"""

count = 0
for filepath in files:
    full = filepath  # paths are relative to tmg-website/
    if not os.path.exists(full):
        print(f"  SKIP: {filepath} (not found)")
        continue
    with open(full, 'r', encoding='utf-8') as f:
        content = f.read()

    # Try blog pattern first, then main pattern
    new_content = content.replace(old_dropdown_blog, new_dropdown_blog)
    replaced = new_content != content
    if not replaced:
        new_content = content.replace(old_dropdown, new_dropdown)
        replaced = new_content != content

    if replaced:
        with open(full, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"  FIXED: {filepath}")
        count += 1
    else:
        print(f"  SKIP: {filepath} (no match)")

print(f"\nDone: fixed {count} files")