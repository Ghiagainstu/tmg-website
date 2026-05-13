#!/usr/bin/env python3
"""
修复 KO pangle-ads.html 中剩余的"서비스"占位符
"""
filepath = 'ko/blog/pangle-ads.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 修复 article-meta (第612行)
old_meta = '''<div class="article-meta">
      서비스
    </div>'''
new_meta = '''<div class="article-meta">
      <span class="article-category">앱 수익화</span>
      <span class="article-date">2026년 4월 23일</span>
      <span class="article-read-time">7분 읽기</span>
    </div>'''
content = content.replace(old_meta, new_meta)
print(f"✓ Fixed article-meta")

# 2. 修复第748行的段落
# 参照英文原文第708-709行
content = content.replace('<p>서비스</p>\n<h2 id="getting-start-ed"></h2>', '''<p>특히 <strong>상위 광고주가 전체 광고비의 90%를 차지합니다</strong>—이는 인벤토리 품질이 높고 예산이 충분함을 의미합니다.</p>
    <h2 id="getting-start-ed">Pangle 시작하기</h2>''')
print(f"✓ Fixed paragraph 748")

# 3. 修复第761行的li (在What This Means for Advertisers部分)
old_li = '''<li>서비스</li>
</ul>
<div class="takeaways">'''
new_li = '''<li><strong>oCPC/oCPM 최적화</strong>는 실제 비즈니스 성과를 향해 입찰할 수 있게 해줍니다—표면적 수치가 아닌.</li>
    </ul>
    <div class="takeaways">'''
content = content.replace(old_li, new_li)
print(f"✓ Fixed li 761")

# 写入文件
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✅ Fixed remaining placeholders in {filepath}")
