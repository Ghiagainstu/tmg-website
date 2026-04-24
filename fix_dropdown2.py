#!/usr/bin/env python3
"""Fix dropdown left:50% centering across all TMG HTML files."""
import os, re

# Files that have the old left:50% pattern
# We'll use a targeted replace on the specific line

files_to_fix = [
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
    'blog/ocean-engine-overview.html',
    'blog/ocean-engine-local-reach.html',
    'blog/ocean-engine-ai-assistant.html',
    'blog/index.html',
    'blog/douyin-enterprise-account.html',
    'blog/bilibili-genz-marketing.html',
    'about/index.html',
]

# Pattern 1: single-line CSS (services pages)
# Pattern 2: multi-line CSS (blog pages)

count = 0
for filepath in files_to_fix:
    if not os.path.exists(filepath):
        print(f"  SKIP: {filepath} (not found)")
        continue
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Multi-line: replace top: 100%; left: 50%; transform: translateX(-50%)
    # with top: calc(100% + 8px); left: 0;
    # Also remove transform from the :hover rule
    content = re.sub(
        r'top:\s*100%;\s*left:\s*50%;\s*transform:\s*translateX\(-50%\);',
        'top: calc(100% + 8px); left: 0;',
        content
    )

    # Remove translateX(-50%) from :hover rules
    content = re.sub(
        r'transform:\s*translateX\(-50%\)\s*translateY\(0\);',
        'transform: translateY(0);',
        content
    )

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  FIXED: {filepath}")
        count += 1
    else:
        print(f"  SKIP: {filepath} (no match)")

print(f"\nDone: fixed {count} files")