#!/usr/bin/env python3
"""
手动修复剩余两篇 KO 博客文章的英文 og:description
"""
import re

translations = {
    'ko/blog/bing-china-demographics-who-are-these-users.html': '75% 이상 대학 교육, 높은 소득, 젊은, 도시 중심—광고주를 위한 Bing China 프리미엄 오디언스의 데이터 중심 인구통계 분석.',
    'ko/blog/bing-china-premium-audience-guide.html': '75% 이상 대학 교육, 더 높은 광고 참여도, 더 낮은 경쟁—중국 프리미엄 소비자에게 도달하기 위한 Bing China가 최고의 비밀일 수 있는 이유.'
}

for filepath, new_desc in translations.items():
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找 og:description 标签
    pattern = r'<meta content=".*?" property="og:description"/>'
    match = re.search(pattern, content)
    
    if match:
        old_tag = match.group(0)
        new_tag = f'<meta content="{new_desc}" property="og:description"/>'
        content = content.replace(old_tag, new_tag)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✓ Fixed: {filepath}")
    else:
        print(f"⚠️  og:description not found: {filepath}")

print(f"\n✅ Fixed remaining OG descriptions")
