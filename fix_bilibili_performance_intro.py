#!/usr/bin/env python3
"""Fix hero intro for bilibili-search-performance-2026."""
import re
from pathlib import Path

WEBSITE = Path('.')
filepath = WEBSITE / 'ja/blog/bilibili-search-performance-2026.html'
content = filepath.read_text(encoding='utf-8')

# Old hero intro with English
old_intro = 'article-hero__intro">Performance optimization techniques for Bilibili search ads: bidding, targeting, and creative rotation. 主要データ：Performance benchmarks；Bid optimization strategies；Creative rotation best practices。'

# New hero intro in pure Japanese
new_intro = 'article-hero__intro">Bilibili検索広告のパフォーマンス最適化：入札、ターゲティング、クリエイティブローテーション。主要データ：パフォーマンスベンチマーク；入札最適化戦略；クリエイティブローテーションのベストプラクティス。'

if old_intro in content:
    content = content.replace(old_intro, new_intro)
    filepath.write_text(content, encoding='utf-8')
    print('Fixed hero intro')
else:
    print('Hero intro not found')
