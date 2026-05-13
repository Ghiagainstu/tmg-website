#!/usr/bin/env python3
"""
批量修复 KO 博客文章的英文 og:description
翻译成韩文
"""
import os
import re

# 定义正确的韩文 og:description
translations = {
    'ad-billing-models-explained.html': '유료 미디어의 광고 과금 모델 실용 가이드: CPM, CPC, CPA, oCPM 등. 어떤 가격 모델이 캠페인 목표에 맞는지 알아보세요.',
    'attribution-models-guide.html': '라스트 클릭, 퍼스트 클릭, 데이터 기반—어떤 어트리뷰션 모델이 캠페인에 맞습니까? 중국에서 광고하는 국제 브랜드를 위한 실용 가이드.',
    'baidu-demographics-who-are-these-735m-users.html': '바이두 검색 사용자 인구통계: 7.35억+ MAU, 3.22억 AI 검색 사용자. 2026년 중국 최대 검색 엔진을 타겟팅하는 광고주를 위한 데이터 중심 인사이트.',
    'bilibili-demographics-who-are-these-gen-z-users.html': 'Bilibili의 3.66억 MAU: 26세 평균 연령, 50% 이상 포스트00세대, Tier 1-3 도시. 높은 참여도(107분/일)로 젊년 마케팅.',
    'bilibili-genz-marketing.html': '서구 마케터가 TikTok에 집중하는 동안, Bilibili는 중국 가장 영향력 있는 젊년 인구통계에 더 깊은 참여를 제공합니다.',
    'bing-china-ads.html': '75% 이상 대학 교육, 더 높은 소득, 더 젊은, 도시 중심—중국 프리미엄 소비자에게 도달하기 위한 Bing China의 데이터 중심 인구통계 분석.',
    'china-internet-and-ad-market-2026.html': 'QuestMobile의 2026년 봄 보고서가 중국 12.76억 인터넷 사용자, 월 192시간 화면 시간, 1,680억 Q1 광고 시장, 및 브랜드가 중국에 진출할 때의 의미를 분석합니다.'
}

fixed = 0
for filename, new_desc in translations.items():
    filepath = f'ko/blog/{filename}'
    if not os.path.exists(filepath):
        print(f"⚠️  File not found: {filepath}")
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 查找英文 og:description 并替换
    # 使用正则表达式匹配 property="og:description" 的内容
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

print(f"\n✅ Fixed {fixed} files")
