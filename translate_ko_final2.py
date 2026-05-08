#!/usr/bin/env python3
"""
FINAL: Translate ALL remaining visible English across ALL Korean pages.
Massive dictionary covering all unmatched text.
"""
import re, os, html as htmlmod

BASE = os.path.dirname(os.path.abspath(__file__))

KO = {
# ===== Common UI labels =====
"How does Baidu advertising charge?": "Baidu 광고 요금은 어떻게 부과되나요?",
"Compliance & Review": "규정 준수 및 검토",
"Frequently Asked Questions": "자주 묻는 질문",
"Talk to an Expert": "전문가와 상담하기",
"Real Success Stories": "실제 성공 사례",
"Start Your Success Story": "성공 사례 시작하기",
"See the Platforms": "플랫폼 보기",
"Monthly Active Users": "월간 활성 사용자",
"Daily Active Users": "일간 활성 사용자",
"Avg. Daily Time Spent": "평균 일일 사용 시간",
"Age Distribution": "연령 분포",
"City Tier Distribution": "도시 계층 분포",
"Gender & Geography": "성별 및 지역",
"Engagement & Spending": "참여 및 지출",
"Audience Insights": "오디언스 인사이트",
"Who Uses Douyin?": "Douyin 사용자는 누구인가요?",
"Who Uses WeChat?": "WeChat 사용자는 누구인가요?",
"Who Searches on Baidu?": "Baidu에서 검색하는 사람은 누구인가요?",
"Who Searches on Bing China?": "Bing China에서 검색하는 사람은 누구인가요?",
"Monthly Active Users": "월간 활성 사용자",
"Daily Time Spent": "일일 사용 시간",
"Average User Age": "평균 사용자 연령",
"Monthly Paying Users": "월간 결제 사용자",
"T1 & T2 city coverage": "T1 및 T2 도시 커버리지",
"WeChat Pay merchants": "WeChat Pay 가맹점",
"Chinese Netizen Coverage": "중국 네티즌 커버리지",
"AI Search Monthly Users": "AI 검색 월간 사용자",
"College Educated (vs 57% avg)": "대학 교육(57% 평균 대비)",
"AI Technology Interest": "AI 기술 관심도",
"Willing to Engage with Ads": "광고 참여 의향",
"Research Before Purchase": "구매 전 리서치",
"T1/T2 City Coverage": "T1/T2 도시 커버리지",
"Search Monthly Rate": "월간 검색률",
"Active Purchase Intent": "활성 구매 의도",
"Daily Usage — Tier 3+ Cities": "일일 사용 — Tier 3+ 도시",
"Analytics Platform": "분석 플랫폼",
"3. Multi-platform operational support": "3. 멀티 플랫폼 운영 지원",
"5. Competitive service packaging": "5. 경쟁력 있는 서비스 패키징",
"The client gained:": "클라이언트가 얻은 것:",
"Our approach included:": "당사의 접근 방식:",
"They wanted an agency that could:": "그들은 다음을 할 수 있는 에이전시를 원했습니다:",
"Why they chose to work with us": "그들이 우리를 선택한 이유",
"KPI-focused execution": "KPI 중심 실행",
"Multi-platform campaign management": "멀티 플랫폼 캠페인 관리",
"Before vs. With TMG": "TMG 도입 전 vs 후",
"All rights reserved.": "모든 권리 보유.",
"Sustained user growth": "지속적인 사용자 성장",
"Successful navigation": "성공적인 탐색",
"Established presence": "구축된 입지",
"Patience and persistence": "인내와 지속성",
"Long-term partnerships": "장기 파트너십",
"Transparency First": "투명성 우선",
"Six-year partnership": "6년 파트너십",

# ===== Service page features =====
"Programmatic display ads": "프로그래매틱 디스플레이 광고",
"Native feed advertising": "네이티브 피드 광고",
"Audience targeting & retargeting": "오디언스 타겟팅 및 리타겟팅",
"AI-powered campaign optimization": "AI 기반 캠페인 최적화",
"Cross-channel analytics": "교차 채널 분석",
"Custom audience modeling": "맞춤 오디언스 모델링",
"Video Feed Advertising": "비디오 피드 광고",
"Native video placements": "네이티브 비디오 배치",
"Brand takeover ads": "브랜드 테이크오버 광고",
"TopView premium placement": "TopView 프리미엄 배치",
"Live Stream & Commerce": "라이브 스트림 및 커머스",
"Live streaming ad formats": "라이브 스트리밍 광고 형식",
"KOL live commerce integration": "KOL 라이브 커머스 통합",
"Brand & Awareness Campaigns": "브랜드 및 인지도 캠페인",
"Microsoft Advertising network": "Microsoft Advertising 네트워크",
"Contextual & keyword targeting": "컨텍스추얼 및 키워드 타겟팅",
"Retargeting & audience segments": "리타겟팅 및 오디언스 세그먼트",
"Bing CN + Baidu Integration": "Bing CN + Baidu 통합",
"Cross-platform keyword alignment": "플랫폼 간 키워드 정렬",
"Unified reporting & attribution": "통합 보고 및 기여 분석",
"Budget allocation optimization": "예산 할당 최적화",
"Search Advertising": "검색 광고",
"Creator matching & outreach": "크리에이터 매칭 및 아웃리치",
"Campaign performance tracking": "캠페인 성과 추적",
"Official Accounts": "공식 계정",
"Subscription & Service accounts": "구독 및 서비스 계정",
"End-to-end Mini Program setup": "종단간 미니 프로그램 설정",
"Direct access from Official Accounts": "공식 계정에서 직접 액세스",
"Three integrated modules designed to eliminate complexity and maximize efficiency when accessing China's digital advertising market.":
    "중국 디지털 광고 시장에 접근할 때 복잡성을 제거하고 효율성을 극대화하도록 설계된 세 가지 통합 모듈.",
"Direct access — no middlemen": "직접 액세스 — 중개인 없음",
"AI-assisted optimization": "AI 기반 최적화",
"Performance reporting": "성과 보고",
"Tap China's Largest Social Ecosystem": "중국 최대 소셜 생태계 활용",
"1.3 billion users. Official Accounts, Mini Programs, Moments Ads, and Search — all connected within a single ecosystem.":
    "13억 사용자. 공식 계정, 미니 프로그램, 모먼트 광고, 검색 — 모두 하나의 생태계에 연결.",
"Moments & Search Ads": "모먼트 및 검색 광고",

# ===== Blog tags =====
"China Ad Platforms": "중국 광고 플랫폼",
"China Search Ads": "중국 검색 광고",
"Paid Media Strategy": "유료 미디어 전략",
"Douyin / Ocean Engine": "Douyin / Ocean Engine",

# ===== GEO page =====
"Get Your Brand Cited in DeepSeek, Douyin & Beyond":
    "DeepSeek, Douyin 등에서 브랜드를 인용받으세요",
"GEO (Generative Engine Optimization)": "GEO (생성 엔진 최적화)",
"Rank high in search results": "검색 결과에서 높은 순위",
"Get cited inside AI-generated answers": "AI 생성 답변 내에서 인용",
"Target platforms": "타겟 플랫폼",
"Google, Baidu, Bing": "Google, Baidu, Bing",
"Keywords, backlinks, meta tags": "키워드, 백링크, 메타 태그",
"User clicks a link": "사용자가 링크 클릭",
"China market relevance": "중국 시장 관련성",
"Simple, transparent pricing": "간단하고 투명한 가격",
"TMG GEO Service Stack": "TMG GEO 서비스 스택",
"Monthly Active Users": "월간 활성 사용자",
"Douyin AI (Doubao)": "Douyin AI (Doubao)",
"No single AI platform dominates. Each has its own user base, strengths, and citation logic. You need a multi-platform strategy.":
    "단일 AI 플랫폼이 지배하지 않습니다. 각 플랫폼은 고유한 사용자 기반, 강점, 인용 로직을 가지고 있습니다. 멀티 플랫폼 전략이 필요합니다.",

# ===== About =====
"Let's Start a Conversation": "대화를 시작해 보세요",
"Whether you have a specific project in mind or just want to learn more about how we can help, we'd love to hear from you.":
    "구체적인 프로젝트가 있거나 당사가 어떻게 도울 수 있는지 자세히 알아보고 싶다면, 연락 주시기 바랍니다.",
"599-2F202 Wanzhen Road": "완전로 599-2F202",
"Jiading District, Shanghai 201824": "상하이시 자딩구 201824",
"Monday - Friday: 9:00 AM - 6:00 PM CST": "월~금: 오전 9시 ~ 오후 6시 (중국 시간)",

# ===== Client stories =====
"Facing platform rejection in China's regulated gaming advertising market.":
    "중국 규제 게임 광고 시장에서 플랫폼 거부에 직면.",
"Every major Chinese platform rejected them initially.":
    "모든 주요 중국 플랫폼이 초기에 거부했습니다.",
"Simplifying Multi-Platform Paid Media Management":
    "멀티 플랫폼 유료 미디어 관리 단순화",
"Managing too many paid media platforms through multiple agencies, with limited transparency and high costs.":
    "제한된 투명성과 높은 비용으로 여러 에이전시를 통해 너무 많은 유료 미디어 플랫폼을 관리.",
"Consolidated multi-platform management": "통합 멀티 플랫폼 관리",
"under one agency, with transparent account access, single point of contact, and competitive bundled pricing.":
    "하나의 에이전시 아래, 투명한 계정 액세스, 단일 연락 창구, 경쟁력 있는 번들 가격.",
"See how we've helped global companies navigate and succeed in China's digital advertising landscape.":
    "당사가 글로벌 기업이 중국 디지털 광고 환경을 탐색하고 성공하도록 도운 방법을 확인하세요.",

# ===== Age/city labels =====
"Ages 25–45 (Core Buyers)": "25~45세 (핵심 구매자)",
"Under 18 (Minors)": "18세 미만",
"25-35 (Young Professionals)": "25~35세 (젊은 전문직)",
"35+ (Mature Users)": "35세 이상",
"25–30 (Young Millennials)": "25~30세 (젊은 밀레니얼)",
"Mid-age Adults (26–35)": "중년 성인 (26~35세)",
"Young Users Total (120M+)": "젊은 사용자 총계 (1.2억+)",
"Post-90s generation": "90년대 이후 세대",
"Decision-makers reached": "도달한 의사결정권자",
"T1 & T2 city coverage": "T1 및 T2 도시 커버리지",
"T1/T2 City Coverage": "T1/T2 도시 커버리지",
"Daily Usage — Tier 3+ Cities": "일일 사용 — Tier 3+ 도시",
"170M Users Research Products Before Buying Every Month":
    "월 1억 7,000만 사용자가 구매 전 제품 리서치",
"XHS users don't just browse — they": "샤오홍슈 사용자는 브라우징만 하지 않습니다 —",
". A typical purchase decision involves studying": "일반적인 구매 결정에는 다음 연구가 포함됩니다",
"across three stages": "세 단계에 걸쳐",
"See how we transform your China advertising experience from complex to simple.":
    "중국 광고 경험을 복잡함에서 단순함으로 변화시키는 방법을 확인하세요.",

# ===== WeChat page =====
"WeChat Is China's \"OS for Life\"":
    "WeChat은 중국의 \"생활 운영체제\"입니다",
"WeChat is the \"LinkedIn of China.\" 50%+ of Official Account readers hold university degrees — your direct line to C-suite executives and decision-makers.":
    "WeChat은 \"중국의 LinkedIn\"입니다. 공식 계정 독자의 50% 이상이 대학 학위를 보유하고 있습니다 — 경영진 및 의사결정권자와의 직접 연결 통로.",

# ===== Bing page =====
"Bing China reaches a uniquely educated and high-income urban audience — 75%+ hold college degrees, 68% are AI-interested, and 59% research products before purchase.":
    "Bing China는 독특하게 교육 수준이 높고 고소득인 도시 오디언스에 도달합니다 — 75%+ 대학 학위, 68% AI 관심, 59% 구매 전 제품 조사.",
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
        
        short = fp.replace(BASE + os.sep, '').replace(os.sep, '/')
        print(f'  {short}: {replacements}')
        total += replacements
    
    print(f'\nTotal: {total}')

if __name__ == '__main__':
    print('FINAL Korean translation sweep...')
    translate()
