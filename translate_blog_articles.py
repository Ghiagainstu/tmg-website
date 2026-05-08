#!/usr/bin/env python3
"""
Translate ALL Korean blog article content.
Runs existing translation scripts first, then handles remaining article content.
"""
import re, os, html as htmlmod, subprocess

BASE = os.path.dirname(os.path.abspath(__file__))

BLOG_KO = {
# ===== Article titles / H1 =====
"Doubao Goes Paid: What This Means for GEO in China":
    "Doubao 유료화: 중국 GEO에 미치는 영향",
"Kuaishou (Kwai) Demographics: Understanding the 400M+ User Base in 2026":
    "Kuaishou (Kwai) 인구통계: 2026년 4억+ 사용자 기반 이해하기",
"Xiaohongshu (RED) Demographics: Who Are These 350M+ Users in 2026?":
    "샤오홍슈(RED) 인구통계: 2026년 이 3.5억+ 사용자는 누구인가요?",
"Baidu Search Demographics: Who Are These 735M+ Users?":
    "Baidu 검색 인구통계: 이 7.35억+ 사용자는 누구인가요?",
"Bilibili Demographics: Who Are These Gen Z Users?":
    "Bilibili 인구통계: 이 Z세대 사용자는 누구인가요?",
"Bing China Demographics: Who Are These High-Value Users?":
    "Bing China 인구통계: 이 고가치 사용자는 누구인가요?",
"Bing China's Premium Audience: Why Smart Brands Are Advertising Here":
    "Bing China의 프리미엄 오디언스: 똑똑한 브랜드가 여기서 광고하는 이유",
"Attribution Models in Paid Media: Why Your Campaign Data Might Be Lying to You":
    "유료 미디어의 기여 모델: 캠페인 데이터가 거짓말할 수 있는 이유",
"Smart Bidding Strategies: From oCPM to tROI — How to Pick the Right Bid for Every Campaign":
    "스마트 입찰 전략: oCPM에서 tROI까지 — 모든 캠페인에 맞는 올바른 입찰 선택 방법",
"Ad Billing Models Explained: CPM, CPC, CPA, oCPM and When to Use Each":
    "광고 청구 모델 설명: CPM, CPC, CPA, oCPM 및 각각 사용 시기",
"GEO Channel Weight Update 2026: 2 Types Rising, 3 Downgraded by AI":
    "GEO 채널 가중치 업데이트 2026: 2개 유형 상승, 3개 AI에 의해 하락",
"CPM, oCPM, eCPM: The Three Metrics Every Paid Media Buyer Gets Wrong":
    "CPM, oCPM, eCPM: 모든 유료 미디어 바이어가 혼동하는 세 가지 지표",
"Is a Rising CPM Really That Bad?":
    "CPM 상승이 정말 나쁜가요?",
"China's Internet Landscape in Spring 2026":
    "2026년 봄 중국 인터넷 환경",
"Meet Zhitu Xing: Ocean Engine's Built-In AI Advertising Assistant":
    "Zhitu Xing 소개: Ocean Engine의 내장 AI 광고 어시스턴트",
"Ocean Engine Local Reach: Douyin's All-in-One Local Marketing Platform":
    "Ocean Engine Local Reach: Douyin의 올인원 로컬 마케팅 플랫폼",
"Ocean Engine: Douyin's Unified Digital Marketing Platform Explained":
    "Ocean Engine: Douyin의 통합 디지털 마케팅 플랫폼 설명",
"Douyin Enterprise Accounts: The Complete Guide for International Brands":
    "Douyin 기업 계정: 국제 브랜드를 위한 완벽 가이드",
"Pangle Ads: ByteDance's Global App Monetization Platform":
    "Pangle 광고: ByteDance의 글로벌 앱 수익화 플랫폼",
"Why Bilibili is China's Most Undervalued Marketing Platform for Gen Z":
    "Bilibili가 Z세대를 위한 중국에서 가장 과소평가된 마케팅 플랫폼인 이유",

# ===== Common blog section headers =====
"Key Takeaways": "주요 내용",
"Introduction": "소개",
"Conclusion": "결론",
"What This Means for Advertisers": "광고주를 위한 의미",
"Quick Summary": "요약",
"Demographic Snapshot": "인구통계 스냅샷",
"Age Distribution": "연령 분포",
"Gender Ratio": "성비",
"Geographic Distribution": "지역 분포",
"Income & Education": "소득 및 교육",
"Education Level": "교육 수준",
"Monthly Income": "월 소득",
"Top Cities": "주요 도시",
"Usage Behavior": "사용 행동",
"Daily Active Time": "일일 활성 시간",
"Peak Usage Hours": "최대 사용 시간",
"Device Preference": "기기 선호도",
"Advertising Potential": "광고 가능성",
"Ad Format Performance": "광고 형식 성과",
"Industry Suitability": "업종 적합성",
"Key Metrics": "주요 지표",
"Data Sources": "데이터 출처",
"Methodology": "방법론",
"Related Reading": "관련 자료",
"Share This Article": "이 기사 공유하기",
"Table of Contents": "목차",

# ===== Common blog phrases =====
"Monthly Active Users": "월간 활성 사용자",
"Daily Active Users": "일간 활성 사용자",
"Average Time Spent": "평균 사용 시간",
"billion": "억",
"million": "백만",
"thousand": "천",
"users aged": "세 사용자",
"age group": "연령대",
"year-over-year": "전년 대비",
"Data current as of": "데이터 기준일",
"Source:": "출처:",
"Note:": "참고:",
"according to": "에 따르면",
"Click to share on": "클릭하여 공유",
"Share on": "공유하기",

# ===== Demographics article common =====
"Understanding the User Base": "사용자 기반 이해하기",
"Who Uses This Platform?": "이 플랫폼을 사용하는 사람은 누구인가요?",
"User Demographics at a Glance": "한눈에 보는 사용자 인구통계",
"What makes this platform unique": "이 플랫폼의 독특한 점",
"Key demographics": "주요 인구통계",
"Advertiser Takeaways": "광고주를 위한 시사점",
"Platform Overview": "플랫폼 개요",
"User Growth Trends": "사용자 성장 추세",
"Competitive Landscape": "경쟁 환경",
}

def apply_fallback_translations(content):
    """Apply translations that use regex for partial matching."""
    # Translate "X years old" patterns
    content = re.sub(r'(\d+)[–-](\d+) years old', r'\1~\2세', content)
    content = re.sub(r'(\d+)[–-](\d+) year-olds', r'\1~\2세', content)
    content = re.sub(r'aged (\d+) to (\d+)', r'\1~\2세', content)
    content = re.sub(r'under (\d+)', r'\1세 미만', content)
    content = re.sub(r'over (\d+)', r'\1세 이상', content)
    
    # Translate "X billion" patterns
    content = re.sub(r'(\d+\.?\d*) billion', r'\1억', content)
    content = re.sub(r'(\d+\.?\d*) million', r'\1백만', content)
    
    # Translate "X% of users" patterns
    content = re.sub(r'(\d+\.?\d*)% of users', r'사용자의 \1%', content)
    content = re.sub(r'(\d+\.?\d*)% are', r'\1%는', content)
    
    return content

def main():
    # Step 1: Run existing scripts
    print("=== Running existing translation scripts ===")
    for script in ['translate_ko.py', 'translate_ko_r11.py', 'translate_ko_final2.py']:
        result = subprocess.run(['python3', script], capture_output=True, text=True)
        for line in result.stdout.split('\n'):
            if 'Total:' in line:
                print(f'  {script}: {line.strip()}')
    
    # Step 2: Apply blog-specific dictionary
    print("\n=== Applying blog translations ===")
    total = 0
    blog_files = [f for f in os.listdir(os.path.join(BASE, 'ko/blog')) 
                  if f.endswith('.html') and f != 'index.html']
    
    for fn in sorted(blog_files):
        fp = os.path.join(BASE, 'ko/blog', fn)
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()
        
        orig = content
        
        # Dictionary replacements
        for eng, kor in sorted(BLOG_KO.items(), key=lambda x: -len(x[0])):
            if eng in content:
                content = content.replace(eng, kor)
        
        # Regex-based fallback translations
        content = apply_fallback_translations(content)
        
        if content != orig:
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(content)
        
        # Count changes
        with open(fp, 'r', encoding='utf-8') as f:
            new_content = f.read()
        
        # Count remaining English
        clean = re.sub(r'<style[^>]*>.*?</style>', '', new_content, flags=re.DOTALL)
        clean = re.sub(r'<script[^>]*>.*?</script>', '', clean, flags=re.DOTALL)
        remaining = 0
        seen = set()
        for m in re.finditer(r'>([^<]{30,500})<', clean):
            t = m.group(1).strip()
            if not t: continue
            d = htmlmod.unescape(t)
            e = len(re.findall(r'[a-zA-Z]', d))
            k = len(re.findall(r'[\uac00-\ud7af\u3130-\u318f]', d))
            if e > 20 and k < 3 and d not in seen:
                seen.add(d)
                remaining += 1
        
        done = '✅' if remaining <= 20 else '⚠️'
        print(f'  {done} {fn}: {remaining} remaining')
        total += remaining
    
    print(f'\nTotal remaining English blocks: {total}')

if __name__ == '__main__':
    main()
