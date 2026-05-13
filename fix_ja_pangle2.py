#!/usr/bin/env python3
"""
修复 JA pangle-ads.html 中的剩余"サービス"占位符
根据英文原文翻译成日文
"""
filepath = 'ja/blog/pangle-ads.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 修复 article-meta (第613行附近的"サービス")
old_meta = '''<div class="article-meta">
      サービス
    </div>'''
new_meta = '''<div class="article-meta">
      <span class="article-category">アプリマネタイズ</span>
      <span class="article-date">2026年4月23日</span>
      <span class="article-read-time">7分読み</span>
    </div>'''
content = content.replace(old_meta, new_meta)
print(f"✓ Fixed article-meta")

# 2. 修复段落占位符 - 第676行
content = content.replace('<p>サービス</p>\n<h2 id="getting-started"></h2>', '''<p>特に<strong>トップティア広告主が全広告費の90%を占めています</strong>—これはインベントリの品質が高く、予算が十分であることを意味します。</p>
    <h2 id="getting-started">Pangleを始める</h2>''')
print(f"✓ Fixed paragraph 676")

# 3. 修复 takeaways (5个li)
old_takeaways = '''<li>サービス</li>
<li>サービス</li>
<li>サービス</li>
<li>サービス</li>
<li>サービス</li>
</ul>'''

new_takeaways = '''<li><strong>Pangleは8億人以上のユーザー</strong>に到達し、1日630億件の広告リクエストと1,100億件のインプレッションを提供します—グローバルモバイル広告ネットワークの中で上位3位以内。</li>
      <li><strong>7つの広告フォーマット</strong>（フィード、バナー、インタースティシャル、スプラッシュ、リワード動画、フルスクリーン、イマーシブ）は、ブランド認知からダイレクトレスポンスまですべてのキャンペーン目標をカバーします。</li>
      <li><strong>oCPCおよびoCPM入札</strong>は、実際のコンバージョンに向けて最適化されるパフォーマンス中心キャンペーンを可能にします。</li>
      <li><strong>リワード動画</strong>は、ゲーム、EdTech、サブスクリプションアプリのユーザー獲得に最適です—最高の完了率、完全なオプトイン、プレミアムブランドセーフ環境。</li>
      <li><strong>グローバルリーチ</strong>は、中国キャンペーンだけでなく、新興市場をターゲットするすべての国際モバイルマーケティング戦略においてPangleを関連的にします。</li>
    </ul>'''

if old_takeaways in content:
    content = content.replace(old_takeaways, new_takeaways)
    print(f"✓ Fixed takeaways")
else:
    print(f"✗ takeaways pattern not found")

# 4. 修复 sidebar-cta
old_sidebar = '<div class="sidebar-cta">\n       サービス\n      </div>'
new_sidebar = '''<div class="sidebar-cta">
        <p>Pangle広告を運用したり、計画中ですか？ 国際ブランドのためのTMGキャンペーン管理。</p>
        <a href="https://www.tuyuesouxin.cn/ja/contact" class="btn btn--primary">お問い合わせ</a>
      </div>'''
content = content.replace(old_sidebar, new_sidebar)
print(f"✓ Fixed sidebar-cta")

# 5. 修复 related-card__cat (2处)
content = content.replace('<div class="related-card__cat">サービス</div>', '<div class="related-card__cat">Douyin / Ocean Engine</div>', 2)
print(f"✓ Fixed related-card__cat")

# 6. 修复 related-card__title (2处)
content = content.replace('<div class="related-card__title">サービス</div>', '<div class="related-card__title">Douyin広告 — TMG Service</div>', 2)
print(f"✓ Fixed related-card__title")

# 写入文件
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✅ Fixed remaining placeholders in {filepath}")
print(f"⚠️ 注意：还有段落内容需要翻译，请手动修复剩余部分")
