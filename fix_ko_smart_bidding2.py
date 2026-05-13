#!/usr/bin/env python3
"""
修复 KO smart-bidding-strategies-explained.html 中的剩余占位符
1. article-meta
2. 段落占位符（先用英文原文，后续翻译成韩文）
"""
filepath = 'ko/blog/smart-bidding-strategies-explained.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 修复 article-meta
old_meta = '''<div class="article-hero__meta">
        서비스
      </div>'''
new_meta = '''<div class="article-hero__meta">
      <span class="article-category">유료 미디어</span>
      <span class="article-date">2026년 4월 16일</span>
      <span class="article-read-time">8분 읽기</span>
    </div>'''
content = content.replace(old_meta, new_meta)
print(f"✓ Fixed article-meta")

# 2. 修复段落占位符 - 先用英文原文替换，避免显示"서비스"
# 第679行附近 - Smart bidding introduction
content = content.replace('<p>서비스</p>\n<p>\n      예산 보호 역할을 하며', '<p>Smart bidding strategies let you tell the platform a goal instead of a bid. The platform\'s algorithm then adjusts your bid in real time for each auction, based on how likely that impression is to achieve your stated goal.</p>\n    <p>\n      예산 보호 역할을 하며', 1)
print(f"✓ Fixed paragraph 679")

# 写入文件
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✅ Fixed remaining placeholders in {filepath}")
print(f"⚠️ 注意：段落暂时用英文原文，需要后续翻译成韩文")
