#!/usr/bin/env python3
"""Translate blog card descriptions and run existing translations on new blog articles."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

BLOG_KO = {
'Doubao just introduced paid tiers at 68-500 RMB/month. With 140M+ DAU, this signals AI platforms are now real, monetized channels — and GEO is no longer optional for brands entering China.':
    'Doubao가 월 68-500위안의 유료 등급을 도입했습니다. 1억 4,000만+ DAU로, AI 플랫폼이 이제 실제 수익 창출 채널이 되었으며 — 중국에 진출하는 브랜드에게 GEO는 더 이상 선택 사항이 아닙니다.',
"Discover why Bing China's educated, affluent user base (75%+ college-educated, 62% ad engagement) is a goldmine for international brands targeting China's premium market.":
    "Bing China의 교육 수준이 높고 부유한 사용자 기반(75%+ 대학 교육, 62% 광고 참여)이 중국 프리미엄 시장을 타겟팅하는 국제 브랜드에게 금광인 이유를 알아보세요.",
"Confused by attribution models in China's paid media? We break down 7 models, platform differences, and how to choose the right one for your campaign goals.":
    "중국 유료 미디어의 기여 모델이 혼란스러우신가요? 7가지 모델, 플랫폼 차이점, 캠페인 목표에 맞는 올바른 선택 방법을 설명합니다.",
"Plain-English guide to smart bidding strategies in China's paid media landscape: oCPC, tROI, cost cap, and more. Learn when to use each bid type and how to avoid common pitfalls.":
    "중국 유료 미디어 환경의 스마트 입찰 전략에 대한 실용 가이드: oCPC, tROI, 비용 상한 등. 각 입찰 유형을 사용해야 하는 시기와 일반적인 함정을 피하는 방법을 알아보세요.",
'Behind every ad campaign is a billing model that determines how you pay — and whether you get the result you paid for. A practical guide to picking the right one.':
    '모든 광고 캠페인 뒤에는 지불 방식을 결정하는 청구 모델이 있습니다 — 그리고 지불한 결과를 얻을 수 있는지 여부. 올바른 모델 선택을 위한 실용 가이드.',
'April 2026 testing across Doubao, DeepSeek, and Kimi shows AI platforms rewrote their channel weights. Compliant vertical sites and local government media are up. Small self-media, cluttered forums, and pure AI content are out.':
    'Doubao, DeepSeek, Kimi에서 2026년 4월 테스트 결과, AI 플랫폼이 채널 가중치를 재작성했습니다. 규정 준수 수직 사이트와 지역 정부 미디어가 상승하고, 소형 셀프미디어, 혼잡한 포럼, 순수 AI 콘텐츠는 하락했습니다.',
'CPM is what you pay. oCPM is how you bid. eCPM is how the system ranks you. Mix them up and you are optimizing for the wrong number. A practical breakdown of the three metrics that look the same but are nothing alike.':
    'CPM은 지불하는 금액입니다. oCPM은 입찰 방식입니다. eCPM은 시스템이 순위를 매기는 방식입니다. 혼동하면 잘못된 숫자에 대해 최적화하게 됩니다. 같아 보이지만 전혀 다른 세 가지 지표에 대한 실용적 분석.',
'CPM goes up and everyone panics. But in real programmatic campaigns — from Baidu to Douyin — a higher CPM can mean better audiences and a lower CPA. Here is when to worry and when to double down.':
    'CPM이 오르면 모두가 당황합니다. 하지만 Baidu에서 Douyin까지 실제 프로그래매틱 캠페인에서 더 높은 CPM은 더 나은 오디언스와 더 낮은 CPA를 의미할 수 있습니다. 걱정해야 할 때와 더 투자해야 할 때를 알려드립니다.',
"1.28 billion users, 192 hours per month of screen time, a ¥168 billion Q1 ad market, and AI-native apps at 413M monthly users — QuestMobile's Spring 2026 report paints a picture of a market that is both mature and shifting fast.":
    "12.8억 사용자, 월 192시간의 화면 시간, 1,680억 위안의 1분기 광고 시장, 4억 1,300만 월간 사용자의 AI 네이티브 앱 — QuestMobile의 2026년 봄 보고서는 성숙하면서도 빠르게 변화하는 시장의 모습을 보여줍니다.",
'ByteDance has embedded an AI assistant directly into the Ocean Engine App. It offers smart Q&A, multi-account analysis, natural-language data queries, and one-click diagnostic tools for Douyin advertisers.':
    'ByteDance가 Ocean Engine 앱에 AI 어시스턴트를 직접 내장했습니다. 스마트 Q&A, 다중 계정 분석, 자연어 데이터 쿼리, Douyin 광고주를 위한 원클릭 진단 도구를 제공합니다.',
"How ByteDance's dedicated local marketing tool helps brick-and-mortar businesses reach nearby customers through short video and live streaming ads—with minimal operational overhead.":
    "ByteDance의 전용 로컬 마케팅 도구가 오프라인 비즈니스가 최소한의 운영 부담으로 숏폼 비디오 및 라이브 스트리밍 광고를 통해 주변 고객에게 도달하는 방법.",
'What every international brand needs to know about Douyin Enterprise Accounts—the verified business profile that unlocks Blue V status, audience insights, and 600M+ daily active users.':
    '모든 국제 브랜드가 Douyin 기업 계정에 대해 알아야 할 사항 — 블루 V 상태, 오디언스 인사이트, 6억+ 일간 활성 사용자를 잠금 해제하는 인증된 비즈니스 프로필.',
"800M+ users reached, 63B daily ad requests, 110B daily impressions—Pangle is ByteDance's global app network that advertisers can access through Ocean Engine.":
    "8억+ 사용자 도달, 630억 일일 광고 요청, 1,100억 일일 노출 — Pangle은 광고주가 Ocean Engine을 통해 액세스할 수 있는 ByteDance의 글로벌 앱 네트워크입니다.",
"While international advertisers rush to Douyin, they're overlooking the platform where China's Generation Z spends 107 minutes daily: 366M users, 70% post-90s, and unmatched youth engagement.":
    "국제 광고주들이 Douyin으로 몰려드는 동안, 중국 Z세대가 매일 107분을 보내는 플랫폼을 간과하고 있습니다: 3억 6,600만 사용자, 70% 90년대 이후 세대, 비교할 수 없는 젊은층 참여.",
}

def translate_blog():
    fp = os.path.join(BASE, 'ko/blog/index.html')
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    total = 0
    for eng, kor in sorted(BLOG_KO.items(), key=lambda x: -len(x[0])):
        if eng in content:
            content = content.replace(eng, kor)
            total += 1
    
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'Blog index: {total} replacements')
    return total

def run_existing_scripts():
    """Run existing translation scripts on new blog articles."""
    import subprocess
    print('\nRunning existing translation scripts on all ko/ files...')
    for script in ['translate_ko.py', 'translate_ko_r11.py', 'translate_ko_final2.py']:
        result = subprocess.run(['python3', script], capture_output=True, text=True)
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')
            for line in lines:
                if 'Total:' in line:
                    print(f'  {script}: {line}')
        else:
            print(f'  {script}: ERROR - {result.stderr[:100]}')

if __name__ == '__main__':
    translate_blog()
    run_existing_scripts()
