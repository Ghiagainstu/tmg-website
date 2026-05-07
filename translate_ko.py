#!/usr/bin/env python3
"""
Korean translation for TMG website (ko/).
Dictionary-based string replacement - preserves HTML formatting.
"""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

KO = {
# ===== Navigation =====
"Services": "서비스",
"Pricing": "요금",
"Client Stories": "고객 사례", 
"Blog": "블로그",
"FAQ": "FAQ",
"About": "회사 소개",
"Why TMG": "TMG를 선택해야 하는 이유",
"Contact": "문의하기",
"About Us": "회사 소개",
"All Services": "전체 서비스",
"WeChat Ads": "WeChat 광고",
"Douyin Ads": "Douyin 광고",
"Baidu SEM": "Baidu SEM",
"Bing China": "Bing China",
"Xiaohongshu": "샤오홍슈(RED)",
"Bilibili Ads": "Bilibili 광고",
"China GEO": "중국 GEO",
"New": "신규",
"Get Started": "시작하기",
"お問い合わせ": "문의하기",
"Read More": "더 보기",
"View All": "전체 보기",
"Subscribe": "구독하기",

# ===== Footer =====
"About TMG": "TMG 소개",
"Quick Links": "바로가기",
"Services": "서비스",
"Contact": "문의하기",
"Legal": "법적 고지",
"Privacy Policy": "개인정보처리방침",
"Terms of Service": "이용약관",
"Cookie Policy": "쿠키 정책",
"Follow Us": "팔로우",
"WeChat": "WeChat",
"Douyin": "Douyin",
"Baidu": "Baidu",
"Bilibili": "Bilibili",

# ===== Common =====
"Get Your Brand Cited in AI Answers": "AI 답변에서 브랜드를 인용받으세요",
"China Digital Advertising Agency | Baidu, WeChat, Douyin | TMG": "중국 디지털 광고 에이전시 | Baidu, WeChat, Douyin | TMG",
}

def translate():
    files = []
    for root, dirs, filenames in os.walk(os.path.join(BASE, 'ko')):
        for fn in filenames:
            if fn.endswith('.html'):
                files.append(os.path.join(root, fn))
    
    total = 0
    for fp in sorted(files):
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()
        
        replacements = 0
        for eng, kor in sorted(KO.items(), key=lambda x: -len(x[0])):
            if eng in content:
                content = content.replace(eng, kor)
                replacements += 1
        
        if replacements > 0:
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(content)
        
        rel = fp.replace(BASE + os.sep, '').replace(os.sep, '/')
        print(f'  {rel}: {replacements} replacements')
        total += replacements
    
    print(f'\nTotal: {total} replacements')
    return total

if __name__ == '__main__':
    print('Translating ko/ pages...')
    translate()
