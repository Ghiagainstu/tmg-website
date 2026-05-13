#!/usr/bin/env python3
"""
修复 JA pangle-ads.html 中的"サービス"占位符
根据英文原文翻译成日文
"""
filepath = 'ja/blog/pangle-ads.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

modified = False

# 1. 修复 title
old_title = '<title>サービス</title>'
new_title = '<title>Pangle広告：ByteDanceのグローバルアプリマネタイズプラットフォーム</title>'
if old_title in content:
    content = content.replace(old_title, new_title)
    modified = True
    print(f"✓ Fixed title")

# 2. 修复 og:description (property)
old_og_desc = 'Pangle reaches 800M+ active users, 63B daily ad requests, and 110B daily impressions. Everything advertisers and developers need to know.'
new_og_desc = 'Pangleは8億人以上のアクティブユーザー、630億日間広告リクエスト、1,100億日間インプレッションを提供します。広告主と開発者が知るべきすべて。'
content = content.replace(old_og_desc, new_og_desc)
print(f"✓ Fixed og:description")

# 3. 修复 article-hero__author-name
old_author = '<div class="article-hero__author-name">サービス</div>'
new_author = '<div class="article-hero__author-name">Tuyue Media Gateway</div>'
if old_author in content:
    content = content.replace(old_author, new_author)
    modified = True
    print(f"✓ Fixed author name")

# 4. 修复 stat-bar (5个stat)
old_stat_bar = '''<div class="stat-bar">
<div class="stat">
        サービス
      </div>
<div class="stat">
        サービス
      </div>
<div class="stat">
        サービス
      </div>
<div class="stat">
        サービス
      </div>
<div class="stat">
        サービス
      </div>
</div>'''

new_stat_bar = '''<div class="stat-bar">
      <div class="stat">
        <span class="stat__num">8億+</span>
        <span class="stat__label">リーチアクティブユーザー</span>
      </div>
      <div class="stat">
        <span class="stat__num">630億+</span>
        <span class="stat__label">日間広告リクエスト</span>
      </div>
      <div class="stat">
        <span class="stat__num">1,100億+</span>
        <span class="stat__label">日間広告インプレッション</span>
      </div>
      <div class="stat">
        <span class="stat__num">10万+</span>
        <span class="stat__label">マネタイズされたアプリ</span>
      </div>
      <div class="stat">
        <span class="stat__num">10.5万+</span>
        <span class="stat__label">グローバル広告主</span>
      </div>
    </div>'''

if old_stat_bar in content:
    content = content.replace(old_stat_bar, new_stat_bar)
    modified = True
    print(f"✓ Fixed stat-bar")
else:
    print(f"✗ stat-bar pattern not found")

# 5. 修复 pricing-grid (4个pricing-chip)
old_pricing = '''<div class="pricing-grid">
<div class="pricing-chip">
        サービス
      </div>
<div class="pricing-chip">
        サービス
      </div>
<div class="pricing-chip">
        サービス
      </div>
<div class="pricing-chip">
        サービス
      </div>
</div>'''

new_pricing = '''<div class="pricing-grid">
      <div class="pricing-chip">
        <span class="pricing-chip__model">CPC</span>
        <span class="pricing-chip__desc">クリックあたりのコスト</span>
      </div>
      <div class="pricing-chip">
        <span class="pricing-chip__model">CPM</span>
        <span class="pricing-chip__desc">1,000インプレッションあたりのコスト</span>
      </div>
      <div class="pricing-chip">
        <span class="pricing-chip__model">oCPC</span>
        <span class="pricing-chip__desc">最適化されたCPC（コンバージョンベース）</span>
      </div>
      <div class="pricing-chip">
        <span class="pricing-chip__model">oCPM</span>
        <span class="pricing-chip__desc">最適化されたCPM（コンバージョンベース）</span>
      </div>
    </div>'''

if old_pricing in content:
    content = content.replace(old_pricing, new_pricing)
    modified = True
    print(f"✓ Fixed pricing-grid")
else:
    print(f"✗ pricing-grid pattern not found")

# 写入文件
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✅ Fixed {filepath}")
print(f"Modified: {modified}")
print(f"\n⚠️ 注意：还有多个段落和表格内容需要翻译，请手动修复剩余部分")
