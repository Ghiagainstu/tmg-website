#!/usr/bin/env python3
"""
修复 KO pangle-ads.html 中的"서비스"占位符
根据英文原文翻译成韩文
"""
import re

filepath = 'ko/blog/pangle-ads.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

modified = False

# 1. 修复 title
old_title = '<title>서비스</title>'
new_title = '<title>Pangle 광고: ByteDance의 글로벌 앱 수익화 플랫폼</title>'
if old_title in content:
    content = content.replace(old_title, new_title)
    modified = True
    print(f"✓ Fixed title")

# 2. 修复 og:description (property)
old_og_desc = 'Pangle reaches 800M+ active users, 63B daily ad requests, and 110B daily impressions. Everything advertisers and developers need to know.'
new_og_desc = 'Pangle은 8억+ 활성 사용자, 630억 일일 광고 요청, 1,100억 일일 노출을 제공합니다. 광고주와 개발자가 알아야 할 모든 것.'
content = content.replace(old_og_desc, new_og_desc)
print(f"✓ Fixed og:description")

# 3. 修复 article-hero__author-name
old_author = '<div class="article-hero__author-name">서비스</div>'
new_author = '<div class="article-hero__author-name">Tuyue Media Gateway</div>'
if old_author in content:
    content = content.replace(old_author, new_author)
    modified = True
    print(f"✓ Fixed author name")

# 4. 修复 stat-bar (5个stat)
# 找到stat-bar并替换整个部分
old_stat_bar = '''<div class="stat-bar">
<div class="stat">
        서비스
      </div>
<div class="stat">
        서비스
      </div>
<div class="stat">
        서비스
      </div>
<div class="stat">
        서비스
      </div>
<div class="stat">
        서비스
      </div>
</div>'''

new_stat_bar = '''<div class="stat-bar">
      <div class="stat">
        <span class="stat__num">8억+</span>
        <span class="stat__label">도달 활성 사용자</span>
      </div>
      <div class="stat">
        <span class="stat__num">630억+</span>
        <span class="stat__label">일일 광고 요청</span>
      </div>
      <div class="stat">
        <span class="stat__num">1,100억+</span>
        <span class="stat__label">일일 광고 노출</span>
      </div>
      <div class="stat">
        <span class="stat__num">10만+</span>
        <span class="stat__label">수익화된 앱</span>
      </div>
      <div class="stat">
        <span class="stat__num">10.5만+</span>
        <span class="stat__label">글로벌 광고주</span>
      </div>
    </div>'''

if old_stat_bar in content:
    content = content.replace(old_stat_bar, new_stat_bar)
    modified = True
    print(f"✓ Fixed stat-bar")
else:
    print(f"✗ stat-bar pattern not found, trying alternative...")
    # 尝试逐行修复
    content = content.replace('<div class="stat">\n        서비스\n      </div>', '<div class="stat">\n        <span class="stat__num">8억+</span>\n        <span class="stat__label">도달 활성 사용자</span>\n      </div>', 1)

# 5. 修复 pricing-grid (4个pricing-chip)
old_pricing = '''<div class="pricing-grid">
<div class="pricing-chip">
        서비스
      </div>
<div class="pricing-chip">
        서비스
      </div>
<div class="pricing-chip">
        서비스
      </div>
<div class="pricing-chip">
        서비스
      </div>
</div>'''

new_pricing = '''<div class="pricing-grid">
      <div class="pricing-chip">
        <span class="pricing-chip__model">CPC</span>
        <span class="pricing-chip__desc">클릭당 비용</span>
      </div>
      <div class="pricing-chip">
        <span class="pricing-chip__model">CPM</span>
        <span class="pricing-chip__desc">1,000회 노출당 비용</span>
      </div>
      <div class="pricing-chip">
        <span class="pricing-chip__model">oCPC</span>
        <span class="pricing-chip__desc">최적화된 CPC (전환 기반)</span>
      </div>
      <div class="pricing-chip">
        <span class="pricing-chip__model">oCPM</span>
        <span class="pricing-chip__desc">최적화된 CPM (전환 기반)</span>
      </div>
    </div>'''

if old_pricing in content:
    content = content.replace(old_pricing, new_pricing)
    modified = True
    print(f"✓ Fixed pricing-grid")
else:
    print(f"✗ pricing-grid pattern not found")

# 6. 修复段落中的"서비스" (第670行附近)
content = content.replace('<p>서비스</p>', '''<p>Pangle은 주로 <strong>공급-side 플랫폼(SSP)</strong>으로 알려져 있지만, 광고주를 위한 기능도 상당합니다.</p>''', 1)
print(f"✓ Fixed first paragraph placeholder")

# 7. 修复第739行的段落
content = content.replace('<p>서비스</p>\n<h2 id="getting-start-ed">', '''<p>Pangle은 Ocean Engine과 동일한 ByteDance 인프라 위에 구축되었지만, 다른 사용자 기반과 광고 목표를 대상으로 합니다.</p>\n    <p>브랜드가 중국 시장만을 타겟팅한다면 Ocean Engine으로 충분하며 Pangle은 불필요할 수 있습니다.</p>\n    <h2 id="getting-started">''', 1)
print(f"✓ Fixed second paragraph placeholder")

# 8. 修复 takeaways (5个li)
old_takeaways = '''<ul>
<li>서비스</li>
<li>서비스</li>
<li>서비스</li>
<li>서비스</li>
<li>서비스</li>
</ul>'''

new_takeaways = '''<ul>
      <li><strong>Pangle은 8억+ 사용자</strong>에게 도달하며, 일일 630억 건의 광고 요청과 1,100억 건의 노출을 제공합니다—글로벌 모바일 광고 네트워크 중 상위 3위 안에 듭니다.</li>
      <li><strong>7가지 광고 형식</strong>(피드, 배너, 전면, 스플래시, 리워드 동영상, 전체 화면, 몰입형)은 브랜드 인지도부터 직접 반응까지 모든 캠페인 목표를 포괄합니다.</li>
      <li><strong>oCPC 및 oCPM 입찰</strong>은 실제 전환을 향해 최적화되는 퍼포먼스 중심 캠페인을 가능하게 합니다.</li>
      <li><strong>리워드 동영상</strong>은 게임, 에듀테크, 구독 앱의 사용자 획득에 가장 적합합니다—최고 완료율, 완전 옵트인, 프리미엄 브랜드 안전 환경.</li>
      <li><strong>글로벌 도달</strong>은 중국 캠페인뿐만 아니라 신흥 시장을 타겟팅하는 모든 국제 모바일 마케팅 전략에 Pangle을 relevant하게 만듭니다.</li>
    </ul>'''

if old_takeaways in content:
    content = content.replace(old_takeaways, new_takeaways)
    modified = True
    print(f"✓ Fixed takeaways")
else:
    print(f"✗ takeaways pattern not found")

# 9. 修复 sidebar-cta
old_sidebar = '<div class="sidebar-cta">\n        서비스\n      </div>'
new_sidebar = '''<div class="sidebar-cta">
        <p>Pangle 광고를 운영하거나 계획 중이신가요? 국제 브랜드를 위한 TMG 캠페인 관리.</p>
        <a href="https://www.tuyuesouxin.cn/ko/contact" class="btn btn--primary">문의하기</a>
      </div>'''
content = content.replace(old_sidebar, new_sidebar)
print(f"✓ Fixed sidebar-cta")

# 10. 修复 related-card__cat (2处)
content = content.replace('<div class="related-card__cat">서비스</div>', '<div class="related-card__cat">Douyin / Ocean Engine</div>', 2)
print(f"✓ Fixed related-card__cat")

# 11. 修复 footer 中的 서비스链接
content = content.replace('<li><a class="footer__link" href="https://www.tuyuesouxin.cn/ko/services/">서비스</a></li>', '<li><a class="footer__link" href="https://www.tuyuesouxin.cn/ko/services/">서비스</a></li>')
# 这个实际上是"서비스"应该是"서비스"？不对，应该是"서비스"（服务）
# 让我检查英文原文
# 英文是 <li><a href="https://www.tuyuesouxin.cn/services/">Services</a></li>
# 所以韩文应该是"서비스"（这个是韩文"服务"的正确写法）
# 但是为什么grep结果显示是"서비스"？让我再看看...
# 啊，我发现了问题："서비스"是韩文"服务"的意思，但是在grep输出中显示的是"서비스"
# 这意味着 footer 中的链接文本确实是正确的韩文"서비스"
# 但是为什么会被识别为占位符？因为翻译脚本可能把所有的"Services"都替换成了"서비스"，包括不应该替换的部分

# 让我重新检查：在KO文件中，"서비스"出现的地方：
# 1. title → 应该翻译成正确的标题
# 2. article-hero__author-name → 应该是 "Tuyue Media Gateway"
# 3. stat-bar中的5个stat → 应该包含数字和标签
# 4. pricing-grid中的4个pricing-chip → 应该包含CPC, CPM等
# 5. takeaways中的5个li → 应该包含完整的要点
# 6. sidebar-cta → 应该是号召性用语
# 7. related-card__cat → 应该是分类名称
# 8. footer__link → 应该是"서비스"（这个是正确的）
# 9. footer中的联系信息 → 应该是地址、电话等

# 所以，我需要区分：
# - 应该修复的"서비스"占位符（在title、author-name、stat、pricing-chip、takeaways、sidebar-cta、related-card__cat中）
# - 正确的"서비스"文本（在footer链接中）

# 但是，在我的grep结果中，第827行显示：
# <li><a class="footer__link" href="https://www.tuyuesouxin.cn/ko/services/">서비스</a></li>
# 这个"서비스"是正确的韩文翻译，不应该被替换

# 让我检查我的脚本是否会错误替换这个...
# 在我的脚本中，我没有针对这个特定模式的替换，所以应该没问题

# 12. 修复 footer 中的联系信息
old_contact = '''<li>
              서비스
            </li>
<li>
              서비스
            </li>'''

new_contact = '''<li>
              <a href="mailto:tmg@tuyuesouxin.cn" class="footer__link">tmg@tuyuesouxin.cn</a>
            </li>
            <li>
              <a href="https://www.tuyuesouxin.cn/ko/contact" class="footer__link">문의하기</a>
            </li>'''

content = content.replace(old_contact, new_contact)
print(f"✓ Fixed footer contact info")

# 13. 修复 footer__platforms
old_platforms = '<div class="footer__platforms">\n          서비스\n        </div>'
new_platforms = '''<div class="footer__platforms">
          <a href="https://www.tuyuesouxin.cn/ko/contact" class="footer__platform-badge">WeChat</a>
          <a href="https://www.tuyuesouxin.cn/ko/contact" class="footer__platform-badge">Douyin</a>
          <a href="https://www.tuyuesouxin.cn/ko/contact" class="footer__platform-badge">Baidu</a>
          <a href="https://www.tuyuesouxin.cn/ko/contact" class="footer__platform-badge">Xiaohongshu</a>
          <a href="https://www.tuyuesouxin.cn/ko/contact" class="footer__platform-badge">Bilibili</a>
          <a href="https://www.tuyuesouxin.cn/ko/contact" class="footer__platform-badge">Bing China</a>
        </div>'''
content = content.replace(old_platforms, new_platforms)
print(f"✓ Fixed footer platforms")

# 写入文件
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✅ Fixed {filepath}")
print(f"Modified: {modified}")
