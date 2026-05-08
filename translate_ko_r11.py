#!/usr/bin/env python3
"""
Round 11: Translate all remaining Korean homepage + visible English across all ko/ pages.
Uses exact HTML string replacement.
"""
import re, os, html as htmlmod

BASE = os.path.dirname(os.path.abspath(__file__))

KO = {
# ===== Homepage visible English =====
"China's Digital Ad Market": "중국 디지털 광고 시장",
"Start Your Journey": "여정 시작하기",
"Direct access to": "직접 액세스",
"From Complexity to Simplicity": "복잡성에서 단순함으로",
"5-7 different agencies to manage": "관리해야 할 5-7개의 다른 에이전시",
"Time zone & language barriers": "시차 및 언어 장벽",
"2-3 months to get started": "시작하는 데 2-3개월",
"Scattered data & inconsistent reports": "분산된 데이터 및 일관성 없는 보고서",
"Policy changes = blind spots": "정책 변경 = 사각지대",
"One dedicated point of contact": "전담 단일 연락 창구",
"Trilingual team, 7×12 response": "3개 언어 팀, 7×12 응답",
"Launch in 1-2 weeks": "1-2주 내 출시",
"Unified dashboard & reports": "통합 대시보드 및 보고서",
"Proactive policy alerts": "사전 정책 알림",
"Everything You Need in One Place": "한 곳에 모든 것",
"All major platforms supported": "모든 주요 플랫폼 지원",
"Multi-currency payment": "다중 통화 결제",
"Transparent transaction": "투명한 거래",
"Fast processing 2-3 business days": "2-3영업일 내 빠른 처리",
"Platform registration": "플랫폼 등록",
"Blue V certification": "블루 V 인증",
"Industry qualifications": "업종 자격",
"Document preparation": "서류 준비",
"Account Management": "계정 관리",
"Performance reporting in plain English": "일반 영어로 된 성과 보고서",
"One contact who actually picks up": "실제로 전화를 받는 한 연락처",
"Results You Can Count On": "신뢰할 수 있는 결과",
"The TMG Difference": "TMG의 차별점",
"Less Communication Time": "더 적은 커뮤니케이션 시간",
"Lower Trial Costs": "더 낮은 시험 비용",
"We handle the learning curve for you": "학습 곡선을 대신 처리해 드립니다",
"Launch in 1-2 weeks instead of months": "몇 개월이 아닌 1-2주 내 출시",
"Higher Efficiency": "더 높은 효율성",
"Simple, Transparent 요금": "간단하고 투명한 요금",
"Ad recharge only": "광고 충전 전용",
"All platforms supported": "모든 플랫폼 지원",
"No account management": "계정 관리 없음",
"Below industry average rates": "업계 평균 이하 요금",
"Setup + Recharge": "설정 + 충전",
"of ad spend + one-time setup fee": "광고비 + 일회성 설정 수수료",
"Setup Fee: Starts from $100+ (one-time)": "설정 수수료: $100+부터 (일회성)",
"Documentation support": "서류 지원",
"Low setup fee with minimal commitment": "최소 약정의 낮은 설정 수수료",
"AI Powered Full Service": "AI 기반 풀 서비스",
"of ad spend + setup fee": "광고비 + 설정 수수료",
"Everything in Setup + Recharge": "설정 + 충전의 모든 것",
"Account management": "계정 관리",
"Campaign optimization": "캠페인 최적화",
"Reporting & analytics": "보고 및 분석",
"Competitive full-service rate": "경쟁력 있는 풀 서비스 요금",
"$200K–$400K USD per year": "연간 $200K~$400K USD",
"Built by People Who Get It": "이해하는 사람들이 만든",
"Ready to Expand to China?": "중국으로 확장할 준비가 되셨나요?",
"tmg@tuyuesouxin.cn": "tmg@tuyuesouxin.cn",
"WhatsApp (scan below qr)": "WhatsApp (아래 QR 스캔)",
"Scan to Add Us on WhatsApp": "WhatsApp에 추가하려면 스캔하세요",
"Inquiry Received!": "문의 접수 완료!",
"Email us directly:": "이메일 직접 보내기:",
"For urgent matters:": "긴급 문의:",
"WhatsApp us via QR code below": "아래 QR 코드로 WhatsApp 문의",
"제출 Another Inquiry": "다른 문의 제출",
"Select your title": "직함 선택",
"Select your role": "역할 선택",
"Advertising Agency": "광고 에이전시",
"Select service type": "서비스 유형 선택",
"Other / Not Sure": "기타 / 확실하지 않음",
"Comments (Optional)": "댓글 (선택사항)",
"WhatsApp (Click to scan)": "WhatsApp (클릭하여 스캔)",
"Tuyue Media Gateway": "Tuyue Media Gateway",
"We built TMG to be the bridge we wished we had—one unified interface, transparent operations, and a team that speaks your language and understands China's digital landscape inside out.":
    "TMG는 우리가 원했던 다리 역할을 위해 구축되었습니다—통합된 인터페이스, 투명한 운영, 귀하의 언어를 구사하고 중국의 디지털 환경을 속속들이 이해하는 팀.",
"annual account authentication fee of CNY 600": "연간 계정 인증 수수료 600위안",
"Baidu only supports pre-payment. You must have sufficient account balance before your ads can run. No credit or post-pay option available.":
    "Baidu는 선불 결제만 지원합니다. 광고를 게재하려면 계정에 충분한 잔액이 있어야 합니다. 신용 또는 후불 옵션은 없습니다.",
"Select your title": "직함 선택",
"Select your role": "역할 선택",

# ===== About page =====
"About Us": "회사 소개",
"Our mission is simple": "우리의 사명은 간단합니다",
"10+ years": "10+년",
"Average client relationship": "평균 고객 관계 기간",

# ===== Services page =====
"Platform Registration": "플랫폼 등록",
"Account opening & qualification filing": "계정 개설 및 자격 신청",
"Campaign Management": "캠페인 관리",
"End-to-end campaign operations": "종단간 캠페인 운영",
"Performance & Reporting": "성과 및 보고",
"Transparent analytics & optimization": "투명한 분석 및 최적화",

# ===== Pricing page =====
"Simple, Transparent Pricing": "간단하고 투명한 요금",
"Platform Setup": "플랫폼 설정",
"Full Account Management": "전체 계정 관리",
"AI-Powered Optimization": "AI 기반 최적화",
"Custom Solutions": "맞춤 솔루션",
"Contact us for custom pricing": "맞춤 견적은 문의해 주세요",
"Best for testing": "테스트에 최적",
"Best for growing": "성장에 최적",
"Best for scaling": "확장에 최적",
"Most popular": "가장 인기 있음",

# ===== Contact page =====
"Get in Touch": "문의하기",
"We'd love to hear from you": "의견을 들려주세요",
"Send us a message": "메시지 보내기",
"Your Name": "이름",
"Email Address": "이메일 주소",
"Phone Number": "전화번호",
"Company Name": "회사명",
"Message": "메시지",
"Send Message": "메시지 보내기",
"Submit Inquiry": "문의 제출",
"Or use the form below": "또는 아래 양식을 사용하세요",

# ===== GEO page =====
"SEO is table stakes": "SEO는 기본입니다",
"GEO is where the game is won": "GEO가 게임의 승부처입니다", 
"Traditional SEO gets you found": "기존 SEO는 발견되게 합니다",
"GEO gets you cited inside AI answers": "GEO는 AI 답변 내에서 인용되게 합니다",
"Source figures are estimates": "출처 수치는 추정치입니다",
"based on publicly reported data": "공개적으로 보고된 데이터에 기반",
"No hidden fees": "숨은 수수료 없음",
"No platform lock-in": "플랫폼 종속 없음",
"Start with the package that fits your current goals":
    "현재 목표에 맞는 패키지로 시작하세요",
"GEO readiness audit": "GEO 준비 상태 감사",
"across your current content": "현재 콘텐츠 전체",

# ===== Blog page =====
"Latest Insights": "최신 인사이트",
"China Market Insights": "중국 시장 인사이트",
"SEM Strategies": "SEM 전략",
"Platform Updates": "플랫폼 업데이트",
"Case Studies": "사례 연구",
"AI & Innovation": "AI 및 혁신",
"Subscribe to our newsletter": "뉴스레터 구독하기",
"Get the latest China digital marketing insights delivered to your inbox.":
    "최신 중국 디지털 마케팅 인사이트를 받은편지함으로 받아보세요.",
"Your email address": "이메일 주소",

# ===== Footer =====
"Follow Us": "팔로우",
"Privacy Policy": "개인정보처리방침",
"Terms of Service": "이용약관",
"Cookie Policy": "쿠키 정책",

# ===== About page =====
"Your Bridge to China's Digital Market": "중국 디지털 시장으로의 다리",
"We're a team of programmatic experts and China market specialists helping international agencies unlock China's $100B digital advertising ecosystem.":
    "저희는 국제 에이전시가 중국의 1,000억 달러 디지털 광고 생태계를 개척할 수 있도록 돕는 프로그래매틱 전문가 및 중국 시장 전문가 팀입니다.",
"China Digital Ad Market": "중국 디지털 광고 시장",
"Average Client Partnership": "평균 고객 파트너십",
"These principles guide every decision we make and every partnership we build.":
    "이 원칙들은 우리의 모든 결정과 모든 파트너십을 안내합니다.",
"Long-term Partnership": "장기 파트너십",
"Expertise You Can Trust": "신뢰할 수 있는 전문성",
"Our team combines deep programmatic knowledge with native understanding of China's platforms. When we say something is possible, we know how to make it happen.":
    "당사 팀은 깊은 프로그래매틱 지식과 중국 플랫폼에 대한 현지 이해를 결합합니다. 어떤 것이 가능하다고 말할 때, 그것을 실현하는 방법을 알고 있습니다.",

# ===== Blog page =====
"Insights & Perspectives": "인사이트 및 관점",
"Douyin / Ocean Engine": "Douyin / Ocean Engine",
"Bilibili / Gen Z Marketing": "Bilibili / Z세대 마케팅",
"Doubao just introduced paid tiers at 68-500 RMB/month. With 140M+ DAU, this signals AI platforms are now real, monetized channels — and GEO is no longer optional.":
    "Doubao가 월 68-500위안의 유료 등급을 도입했습니다. 1억 4,000만+ DAU로, AI 플랫폼이 이제 실제 수익 창출 채널이 되었음을 의미합니다 — GEO는 더 이상 선택 사항이 아닙니다.",
"Discover why Bing China's educated, affluent user base (75%+ college-educated, 62% ad engagement) is a goldmine for international brands targeting Chinese consumers.":
    "Bing China의 교육 수준이 높고 부유한 사용자 기반(75%+ 대학 교육, 62% 광고 참여)이 중국 소비자를 타겟팅하는 국제 브랜드에게 금광인 이유를 알아보세요.",
"Confused by attribution models in China's paid media? We break down 7 models, platform differences, and how to choose the right one for your campaigns.":
    "중국 유료 미디어의 기여 모델이 혼란스러우신가요? 7가지 모델, 플랫폼 차이점, 캠페인에 맞는 올바른 선택 방법을 설명합니다.",
"Plain-English guide to smart bidding strategies in China's paid media landscape: oCPC, tROI, cost cap, and more. Learn when to use each bid type and how to optimize for your goals.":
    "중국 유료 미디어 환경의 스마트 입찰 전략에 대한 실용 가이드: oCPC, tROI, 비용 상한 등. 각 입찰 유형을 사용해야 하는 시기와 목표에 맞게 최적화하는 방법을 알아보세요.",
"Behind every ad campaign is a billing model that determines how you pay — and whether you get the result you paid for. A practical guide to picking the right model.":
    "모든 광고 캠페인 뒤에는 지불 방식을 결정하는 청구 모델이 있습니다 — 그리고 지불한 결과를 얻을 수 있는지 여부. 올바른 모델 선택을 위한 실용 가이드.",
"April 2026 testing across Doubao, DeepSeek, and Kimi shows AI platforms rewrote their channel weights. Compliant vertical sites and local government media are rising, while generic content platforms are losing ground.":
    "Doubao, DeepSeek, Kimi에서 2026년 4월 테스트 결과, AI 플랫폼이 채널 가중치를 재작성한 것으로 나타났습니다. 규정 준수 사이트와 지역 정부 미디어가 상승하는 반면, 일반 콘텐츠 플랫폼은 입지를 잃고 있습니다.",
"CPM is what you pay. oCPM is how you bid. eCPM is how the system ranks you. Mix them up and you are optimizing for the wrong number. A practical breakdown of the three metrics every media buyer needs to understand.":
    "CPM은 지불하는 금액입니다. oCPM은 입찰 방식입니다. eCPM은 시스템이 순위를 매기는 방식입니다. 혼동하면 잘못된 숫자에 대해 최적화하게 됩니다. 모든 미디어 바이어가 이해해야 하는 세 가지 지표에 대한 실용적 분석.",
"CPM goes up and everyone panics. But in real programmatic campaigns — from Baidu to Douyin — a higher CPM can mean better audiences and a lower CPA. Here's why.":
    "CPM이 오르면 모두가 당황합니다. 하지만 Baidu에서 Douyin까지 실제 프로그래매틱 캠페인에서 더 높은 CPM은 더 나은 오디언스와 더 낮은 CPA를 의미할 수 있습니다. 그 이유를 설명합니다.",
"1.28 billion users, 192 hours per month of screen time, a ¥168 billion Q1 ad market, and AI-native apps at 413M monthly users — QuestMobile's Spring 2026 report.":
    "12.8억 사용자, 월 192시간의 화면 시간, 1,680억 위안의 1분기 광고 시장, 4억 1,300만 월간 사용자의 AI 네이티브 앱 — QuestMobile의 2026년 봄 보고서.",
"ByteDance has embedded an AI assistant directly into the Ocean Engine App. It offers smart Q&A, multi-account analysis, natural-language data queries, and automated campaign optimization suggestions.":
    "ByteDance가 Ocean Engine 앱에 AI 어시스턴트를 직접 내장했습니다. 스마트 Q&A, 다중 계정 분석, 자연어 데이터 쿼리, 자동화된 캠페인 최적화 제안을 제공합니다.",
"How ByteDance's dedicated local marketing tool helps brick-and-mortar businesses reach nearby customers through short video and live streaming ads.":
    "ByteDance의 전용 로컬 마케팅 도구가 오프라인 비즈니스가 숏폼 비디오 및 라이브 스트리밍 광고를 통해 주변 고객에게 도달하는 방법.",
"From Douyin and Toutiao to Xigua Video, Pangle, and 懂车帝—Ocean Engine is ByteDance's all-in-one ad platform covering 10+ products and 600M+ users.":
    "Douyin, Toutiao에서 Xigua Video, Pangle, 懂车帝까지 — Ocean Engine은 10개 이상의 제품과 6억+ 사용자를 포괄하는 ByteDance의 올인원 광고 플랫폼입니다.",
"What every international brand needs to know about Douyin Enterprise Accounts—the verified business profile that unlocks Blue V status, audience insights, and marketing tools.":
    "모든 국제 브랜드가 Douyin 기업 계정에 대해 알아야 할 사항 — 블루 V 상태, 오디언스 인사이트, 마케팅 도구를 잠금 해제하는 인증된 비즈니스 프로필.",
"800M+ users reached, 63B daily ad requests, 110B daily impressions—Pangle is ByteDance's global app network that advertisers can access through Ocean Engine to reach users outside China.":
    "8억+ 사용자 도달, 630억 일일 광고 요청, 1,100억 일일 노출 — Pangle은 광고주가 Ocean Engine을 통해 중국 외 사용자에게 도달할 수 있는 ByteDance의 글로벌 앱 네트워크입니다.",
"While international advertisers rush to Douyin, they're overlooking the platform where China's Generation Z spends 107 minutes daily: 366M users, 70% of China's post-00s generation, and a 1:1 gender ratio.":
    "국제 광고주들이 Douyin으로 몰려드는 동안, 중국 Z세대가 매일 107분을 보내는 플랫폼을 간과하고 있습니다: 3억 6,600만 사용자, 중국 00년대생의 70%, 1:1 성비.",
"All rights reserved.": "모든 권리 보유.",

# ===== Service pages remaining =====
"Baidu SEM | Tuyue Media Gateway": "Baidu SEM | Tuyue Media Gateway",
"Bing China (Bing CN) 광고 | Tuyue Media Gateway": "Bing China (Bing CN) 광고 | Tuyue Media Gateway",
"Capture High-Intent Customers on China's #1 Search Engine":
    "중국 1위 검색 엔진에서 구매 의도가 높은 고객을 포착하세요",
"735M monthly active users + 322M AI search users. Baidu holds 97.5% coverage of Chinese internet users and processes 60 billion searches daily.":
    "7억 3,500만 월간 활성 사용자 + 3억 2,200만 AI 검색 사용자. Baidu는 중국 인터넷 사용자의 97.5%를 커버하며 일일 600억 건의 검색을 처리합니다.",
"Search Advertising (PPC)": "검색 광고 (PPC)",
"Pay-per-click ads on Baidu's search results. Target customers actively searching for your products, services, or brand keywords in Chinese.":
    "Baidu 검색 결과의 클릭당 지불 광고. 중국어로 제품, 서비스 또는 브랜드 키워드를 검색하는 고객을 타겟팅합니다.",
"Keyword strategy & expansion": "키워드 전략 및 확장",
"Ad copy creation & optimization": "광고 카피 제작 및 최적화",
"Quality score improvement": "품질 점수 개선",
"Bid management & CPC control": "입찰 관리 및 CPC 제어",
"Display & Feed Advertising": "디스플레이 및 피드 광고",
"Bing China Advertising": "Bing China 광고",
"Search Advertising (SEM)": "검색 광고 (SEM)",
"Keyword strategy & expansion": "키워드 전략 및 확장",
"Ad copy in Chinese & English": "중국어 및 영어 광고 카피",
"Quality score optimization": "품질 점수 최적화",
"Bid management & CPC control": "입찰 관리 및 CPC 제어",
"Display & Native Advertising": "디스플레이 및 네이티브 광고",
"Reach Bing China's premium audience across the Microsoft Advertising network — display banners, in-feed native ads, and contextual placements on high-authority sites.":
    "Microsoft Advertising 네트워크 전반에 걸쳐 Bing China의 프리미엄 오디언스에 도달 — 디스플레이 배너, 인피드 네이티브 광고, 권위 있는 사이트의 컨텍스추얼 배치.",
"China's #1 Product Research Platform": "중국 1위 제품 리서치 플랫폼",
"Community & Discovery Ads": "커뮤니티 및 발견 광고",
"In-feed native placements": "인피드 네이티브 배치",
"Product showcase cards": "제품 쇼케이스 카드",
"UGC-style branded content": "UGC 스타일 브랜드 콘텐츠",
"Keyword-targeted search ads": "키워드 타겟 검색 광고",
"Brand term protection": "브랜드 용어 보호",
"Category intent targeting": "카테고리 의도 타겟팅",
"KOL & Creator Partnerships": "KOL 및 크리에이터 파트너십",
"KOL campaign strategy": "KOL 캠페인 전략",

# ===== GEO remaining =====
"Baidu SEM | Tuyue Media Gateway": "Baidu SEM | Tuyue Media Gateway",
"Capture High-Intent Customers on China's #1 Search Engine":
    "중국 1위 검색 엔진에서 구매 의도가 높은 고객을 포착하세요",

# ===== Final few =====
"TUYUE SOUXIN (SHANGHAI) INFORMATION TECHNOLOGY CO., LTD.":
    "TUYUE SOUXIN (SHANGHAI) INFORMATION TECHNOLOGY CO., LTD.",
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
        print(f'  {rel}: {replacements}')
        total += replacements
    
    print(f'\nTotal: {total}')

if __name__ == '__main__':
    print('Round 11: Remaining Korean translations...')
    translate()
