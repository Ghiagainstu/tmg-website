#!/usr/bin/env python3
"""
Visual enhancement for douao-ads-geo-still-worth-it.html
Fixes class names and adds visual elements correctly.
"""
import re

filepath = 'blog/doubao-ads-geo-still-worth-it.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

modified = False

# 1. Fix old CSS class names (CRITICAL: order matters!)
# callout classes
old_new = [
    ('class="article-callout article-callout--info"', 'class="callout callout--accent"'),
    ('class="article-callout article-callout--warning"', 'class="callout"'),
    ('class="article-callout article-callout--tip"', 'class="callout"'),
    ('class="article-callout"', 'class="callout"'),
]
for old, new in old_new:
    if old in content:
        content = content.replace(old, new)
        modified = True
        print(f'  Fixed: {old[:40]}...')

# callout inner h4 → callout__label div
if '<h4>' in content:
    content = re.sub(r'<h4>(.*?)</h4>', r'<div class="callout__label">\1</div>', content)
    modified = True
    print('  Fixed: callout inner h4 → callout__label')

# stats-grid → feature-grid (order: specific before generic)
old_new2 = [
    ('class="stats-grid"', 'class="feature-grid"'),
    ('class="stat-card__number"', 'class="feature-card__num"'),
    ('class="stat-card__label"', 'class="feature-card__desc"'),
    ('class="stat-card"', 'class="feature-card"'),
]
for old, new in old_new2:
    if old in content:
        content = content.replace(old, new)
        modified = True
        print(f'  Fixed: {old}')

# 2. Add emojis to h2 headings
emoji_map = [
    ('>Every medium has two types of traffic</h2>', '>📊 Every medium has two types of traffic</h2>'),
    ('>Paid traffic scales results — Organic traffic cuts costs</h2>', '>📈 Paid traffic scales results — Organic traffic cuts costs</h2>'),
    ('>The earlier you start, the bigger the advantage</h2>', '>⏰ The earlier you start, the bigger the advantage</h2>'),
    ('>Walk on two legs: Paid + Organic</h2>', '>🦶 Walk on two legs: Paid + Organic</h2>'),
    ('>The Bottom Line</h2>', '>🎯 The Bottom Line</h2>'),
]
for old, new in emoji_map:
    if old in content and new not in content:
        content = content.replace(old, new)
        modified = True
        print(f'  Added emoji: {old[1:30]}...')

# 3. Insert feature-grid before "Paid traffic: short-term scaling" h3
# (Only if not already present)
feature_grid = '''        <div class="feature-grid">
            <div class="feature-card">
                <div class="feature-card__num">💰</div>
                <div class="feature-card__title">Paid Traffic</div>
                <div class="feature-card__desc">Rented — stop paying, it vanishes. Best for quick market tests and lead generation. Costs rise as competition increases.</div>
            </div>
            <div class="feature-card">
                <div class="feature-card__num">🏗️</div>
                <div class="feature-card__title">Organic Traffic (GEO)</div>
                <div class="feature-card__desc">An asset you build over time. Fixed upfront cost, ongoing AI recommendations. Nobody can take it away.</div>
            </div>
            <div class="feature-card">
                <div class="feature-card__num">⚡</div>
                <div class="feature-card__title">Short-term Impact</div>
                <div class="feature-card__desc">Paid traffic delivers results today. Ideal for campaigns, product launches, and seasonal pushes.</div>
            </div>
            <div class="feature-card">
                <div class="feature-card__num">📈</div>
                <div class="feature-card__title">Long-term Value</div>
                <div class="feature-card__desc">GEO compounds over time. Each piece of optimized content keeps earning AI recommendations indefinitely.</div>
            </div>
        </div>
'''

marker_h3 = '<h3>Paid traffic: short-term scaling</h3>'
if marker_h3 in content and '💰' not in content:
    content = content.replace(marker_h3, feature_grid + '\n        ' + marker_h3)
    modified = True
    print('  Inserted feature-grid (paid vs organic)')
elif '💰' in content:
    print('  feature-grid already present, skipping')

# 4. Insert scenario-list before "Use GEO data to guide ad targeting" h3
scenario_list = '''        <ul class="scenario-list">
            <li>
                <div class="scenario-list__icon">🟢</div>
                <div class="scenario-list__content">
                    <strong>Start GEO now</strong>
                    <span>Trust assets take 3-6 months to build. Begin now to establish your AI search presence before competitors.</span>
                </div>
            </li>
            <li>
                <div class="scenario-list__icon">🟡</div>
                <div class="scenario-list__content">
                    <strong>Monitor Doubao ad pricing</strong>
                    <span>AI ad CPMs are likely to mirror ChatGPT's trajectory — $60+ CPM. Factor this into your media budget planning.</span>
                </div>
            </li>
            <li>
                <div class="scenario-list__icon">🔵</div>
                <div class="scenario-list__content">
                    <strong>Run paid + organic together</strong>
                    <span>Use paid campaigns for immediate reach while GEO builds your long-term AI trust assets. The two channels reinforce each other.</span>
                </div>
            </li>
        </ul>
'''

marker_h3_2 = '<h3>Use GEO data to guide ad targeting</h3>'
if marker_h3_2 in content and '🟢' not in content:
    content = content.replace(marker_h3_2, scenario_list + '\n        ' + marker_h3_2)
    modified = True
    print('  Inserted scenario-list')
elif '🟢' in content:
    print('  scenario-list already present, skipping')

if not marker_h3_2 in content:
    print('  WARNING: marker "Use GEO data to guide ad targeting" not found!')

# Write back
if modified:
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'\n✅ {filepath} updated successfully!')
else:
    print(f'\nℹ️  No changes needed for {filepath}')
