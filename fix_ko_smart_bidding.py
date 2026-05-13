#!/usr/bin/env python3
"""
修复 KO smart-bidding-strategies-explained.html 中的"서비스"占位符
根据英文原文翻译成韩文
"""
filepath = 'ko/blog/smart-bidding-strategies-explained.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

modified = False

# 1. 修复 title
old_title = '<title>서비스</title>'
new_title = '<title>스마트 입찰 전략: oCPM에서 tROI까지 — 모든 캠페인을 위한 올바른 입찰 선택</title>'
if old_title in content:
    content = content.replace(old_title, new_title)
    modified = True
    print(f"✓ Fixed title")

# 2. 修复 og:description (如果还是英文)
old_og_desc = 'content="Plain-English guide to smart bidding in China\'s paid media: oCPC, tROI, cost cap, and more. Learn when to use each bid type." property="og:description"/>'
new_og_desc = 'content="중국 유료 미디어의 스마트 입찰 전략에 대한 가이드: oCPC, tROI, 비용 상한 등. 각 입찰 유형을 언제 사용할지 알아보세요." property="og:description"/>'
content = content.replace(old_og_desc, new_og_desc)
print(f"✓ Fixed og:description")

# 3. 修复 article-hero__author-name 和 author-role
old_author = '<div class="article-hero__author-name">서비스</div>'
new_author = '<div class="article-hero__author-name">Tuyue Media Gateway</div>'
if old_author in content:
    content = content.replace(old_author, new_author)
    modified = True
    print(f"✓ Fixed author name")

old_role = '<div class="article-hero__author-role">서비스</div>'
new_role = '<div class="article-hero__author-role">Paid Media Team · Shanghai</div>'
if old_role in content:
    content = content.replace(old_role, new_role)
    modified = True
    print(f"✓ Fixed author role")

# 4. 修复 article-meta (第556行附近的"서비스")
# 需要先读取这部分内容，看看具体结构
# 暂时跳过，稍后处理

# 5. 修复 sidebar-cta
old_sidebar = '<div class="sidebar-cta">\n        서비스\n      </div>'
new_sidebar = '''<div class="sidebar-cta">
        <p>스마트 입찰에 대해 궁금하신가요? TMG가 캠페인 최적화를 도와드립니다.</p>
        <a href="https://www.tuyuesouxin.cn/ko/contact" class="btn btn--primary">문의하기</a>
      </div>'''
content = content.replace(old_sidebar, new_sidebar)
print(f"✓ Fixed sidebar-cta")

# 6. 修复 related-card__excerpt (3处)
content = content.replace('<p class="related-card__excerpt">서비스</p>', '<p class="related-card__excerpt">스마트 입찰 전략에 대한 상세 가이드.</p>', 3)
print(f"✓ Fixed related-card excerpts")

# 7. 修复 footer 中的联系信息
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

# 8. 修复 footer__platforms
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
print(f"\n⚠️ 注意：还有多个段落和表格内容需要翻译，请手动修复剩余部分")
