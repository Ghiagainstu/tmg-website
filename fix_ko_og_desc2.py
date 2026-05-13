#!/usr/bin/env python3
"""
修复剩余两篇 KO 博客文章的英文 og:description
"""
import re

translations = {
    'bing-china-demographics-who-are-these-users.html': '75% 이상 대학 교육, 높은 소득, 젊은 연령, 도시 중심—중국 프리미엄 소비자에게 도달하기 위한 Bing China의 인구통계 데이터.',
    'bing-china-premium-audience-guide.html': '75% 이상 대학 교육, 더 높은 광고 참여도, 더 낮은 경쟁—Bing China가 중국 프리미엄 소비자에게 도달하는 최고의 비밀일 수 있는 이유.'
}

fixed = 0
for filename, new_desc in translations.items():
    filepath = f'ko/blog/{filename}'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    pattern = r'content="([A-Za-z].*?)" property="og:description"/>'
    match = re.search(pattern, content)
    
    if match:
        old_desc = match.group(0)
        new_tag = f'content="{new_desc}" property="og:description"/>'
        content = content.replace(old_desc, new_tag)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        fixed += 1
        print(f"✓ Fixed: {filename}")
    else:
        print(f"⚠️  No English og:description found: {filename}")

print(f"\n✅ Fixed {fixed} more files")
