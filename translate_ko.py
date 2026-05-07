#!/usr/bin/env python3
"""
Complete Korean translation for TMG website (ko/).
Dictionary-based string replacement - preserves HTML formatting.
Add new entries to KO dict, then re-run.
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
"Read More": "더 보기",
"View All": "전체 보기",
"Subscribe": "구독하기",
"お問い合わせ": "문의하기",

# ===== Footer =====
"About TMG": "TMG 소개",
"Quick Links": "바로가기",
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
"China Digital Advertising Agency | Baidu, WeChat, Douyin | TMG":
    "중국 디지털 광고 에이전시 | Baidu, WeChat, Douyin | TMG",
"© 2026 Tuyue Media Gateway. All rights reserved.":
    "© 2026 Tuyue Media Gateway. 모든 권리 보유.",
"Let's discuss how TMG can help your agency access China's digital advertising market.":
    "TMG가 귀사의 중국 디지털 광고 시장 진출을 어떻게 지원할 수 있는지 상담해보세요.",
"Your single point of access to China's $100B digital advertising market. We help international agencies navigate Chinese platforms and maximize ROI.":
    "중국 1,000억 달러 디지털 광고 시장으로의 단일 액세스 포인트. 국제 에이전시가 중국 플랫폼을 탐색하고 ROI를 극대화할 수 있도록 지원합니다.",
"Thank you for reaching out to TMG.":
    "TMG에 문의해 주셔서 감사합니다.",
"We've received your inquiry and will get back to you within":
    "문의가 접수되었습니다. 다음 시간 내에 연락드리겠습니다:",
"Keep an eye on your inbox at the email you provided.":
    "제공하신 이메일 주소의 받은편지함을 확인해주세요.",
"NO. 599 WANZHEN ROAD, SHANGHAI, CHINA":
    "중국 상하이시 자딩구 완전로 599호 2F202",
"New: 中国GEO サービス — Get Cited in AI Answers":
    "신규: 중국 GEO 서비스 — AI 답변에서 인용받기",
"No matching questions found.":
    "일치하는 질문이 없습니다.",
"business hours.":
    "업무 시간 내.",

# ===== Homepage =====
"AI-assisted optimization to cut wasted spend":
    "AI 기반 최적화로 불필요한 지출 절감",
"Can I open a Baidu account without a Chinese domestic company?":
    "중국 현지 회사 없이 Baidu 계정을 개설할 수 있나요?",
"Baidu supports account opening for foreign companies and entities. You don't need a Chinese domestic business license to get started.":
    "Baidu는 외국 기업 및 법인의 계정 개설을 지원합니다. 시작하는 데 중국 현지 영업 허가증이 필요하지 않습니다.",
"Are there fees besides the advertising budget?":
    "광고 예산 외에 비용이 있나요?",
"Does Baidu support post-payment?":
    "Baidu는 후불제를 지원하나요?",
"Baidu only supports pre-payment. You must have sufficient account balance before your ads can run. No credit or post-payment options are available for standard accounts.":
    "Baidu는 선불제만 지원합니다. 광고 게재 전에 계정 잔액이 충분해야 합니다. 표준 계정에는 신용 또는 후불 옵션이 없습니다.",
"Can foreign companies advertise on 小紅書（RED）?":
    "외국 기업이 샤오홍슈(RED)에서 광고할 수 있나요?",

# ===== Service Pages - Hero =====
"Baidu SEM | Tuyue Media Gateway":
    "Baidu SEM | Tuyue Media Gateway",
"You need a Chinese business license or a partnership": "중국 영업 허가증 또는 파트너십이 필요합니다",
"Key Audience Segments": "주요 타겟 세그먼트",
"Key Audience Segments (Baidu Marketing Platform)": "주요 타겟 세그먼트 (Baidu 마케팅 플랫폼)",
"Why WeChat for Your Brand?": "우리 브랜드에 WeChat이 필요한 이유",
"Why Douyin for Your Brand?": "우리 브랜드에 Douyin이 필요한 이유",
"Why Bilibili for Your Brand?": "우리 브랜드에 Bilibili가 필요한 이유",
"WeChat reaches across every demographic in China": "WeChat은 중국의 모든 연령대에 도달합니다",
"Douyin reaches across every demographic in China": "Douyin은 중국의 모든 연령대에 도달합니다",
"Who Uses Bilibili?": "Bilibili 사용자는 누구인가요?",
"Gender & Geography": "성별 및 지역",
"Engagement & Spending": "참여도 및 지출",
"Key Audience Segments": "주요 타겟 세그먼트",
"Industry-Leading Research": "업계 선도적 연구",
"Our insights are backed by China's most trusted research institutions and official platform data.":
    "당사의 인사이트는 중국에서 가장 신뢰받는 연구 기관과 공식 플랫폼 데이터에 기반합니다.",

# ===== Baidu SEM page =====
"Baidu検索結果に表示されるクリック課金型広告。 Target customers actively searching for your products, services, or brand keywords in Chinese.":
    "Baidu 검색 결과에 표시되는 클릭당 지불 광고입니다. 중국어로 제품, 서비스 또는 브랜드 키워드를 검색하는 고객을 타겟팅합니다.",
"Reach users across Baidu's network of 800M+ devices through banner ads, native feeds, and programmatic display placements.":
    "Baidu의 8억+ 기기 네트워크 전반에 걸쳐 배너 광고, 네이티브 피드, 프로그래매틱 디스플레이 배치를 통해 사용자에게 도달하세요.",
"Baidu Marketing Cloud": "Baidu 마케팅 클라우드",
"Leverage Baidu's proprietary data engine to run AI-powered campaigns, cross-channel attribution, and advanced audience segmentation.":
    "Baidu의 독점 데이터 엔진을 활용하여 AI 기반 캠페인, 교차 채널 기여 분석, 고급 오디언스 세분화를 실행하세요.",
"Knowledge Elite — High education, high income, deep info seekers":
    "지식 엘리트 — 고학력, 고소득, 정보 탐색자",
"Gen Z — Digital natives born 1995–2009": "Z세대 — 1995~2009년 출생 디지털 네이티브",
"Working Professionals — Urban office workers": "직장인 — 도시 오피스 워커",
"New Parents — Infant stage family builders": "신규 부모 — 영유아기 가족 형성층",
"Silver Gen — Pre-retirees, stable savings, open to spending":
    "실버 세대 — 은퇴 전, 안정적인 저축, 소비 의향 있음",
"Students — Online active, early adopters": "학생 — 온라인 활동적, 얼리 어답터",
"Fashion Forward — Appearance-conscious, trend-driven":
    "패션 선도층 — 외모 중시, 트렌드 주도",
"Newlyweds — Young couples starting families": "신혼부부 — 가족을 시작하는 젊은 커플",
"Outbound travel — Middle-High spenders": "해외 여행 — 중고액 소비자",
"Middle-class consumers": "중산층 소비자",
"Complete purchase on Baidu App": "Baidu 앱에서 구매 완료",

# ===== Douyin page =====
"ユーザーのコンテンツストリームにシームレスに溶け込むネイティブ広告。 Highly engaging and interruptive-free brand storytelling.":
    "사용자 콘텐츠 스트림에 자연스럽게 통합되는 네이티브 광고. 참여도가 높고 방해하지 않는 브랜드 스토리텔링.",
"In-stream product showcase": "인스트림 제품 쇼케이스",
"Build brand awareness at scale with branded hashtag challenges, AR filters, and influencer partnerships through Douyin's discovery-driven content ecosystem.":
    "Douyin의 발견 기반 콘텐츠 생태계를 통해 브랜드 해시태그 챌린지, AR 필터, 인플루언서 파트너십으로 대규모 브랜드 인지도를 구축하세요.",
"ARレンズ＆フィルターブランディング for interactive engagement":
    "AR 렌즈 및 필터 브랜딩 — 인터랙티브 참여",
"UGC増幅 & user participation campaigns": "UGC 증폭 및 사용자 참여 캠페인",
"Affluent Millennials (25–40)": "부유한 밀레니얼(25~40세)",
"女性 Impulse Shoppers": "여성 충동구매자",
"Live Commerce Enthusiasts": "라이브 커머스 애호가",
"Douyin is China's most comprehensive advertising channel —":
    "Douyin은 중국에서 가장 포괄적인 광고 채널입니다 —",
"every age, every income tier, every city level":
    "모든 연령, 모든 소득 계층, 모든 도시 수준",
"No other platform matches its combination of reach, engagement depth (125+ min/day), and direct commerce integration that Douyin offers.":
    "Douyin이 제공하는 도달 범위, 참여 깊이(하루 125분+), 직접 커머스 통합의 조합을 따라올 플랫폼은 없습니다.",
"Tier 1 (Beijing/Shanghai/Guangzhou/Shenzhen)": "Tier 1 (베이징/상하이/광저우/선전)",
"Tier 2 (New First-tier Cities)": "Tier 2 (신1선 도시)",
"Tier 3–5 (Sinking Market)": "Tier 3~5 (침강 시장)",
"College Degree or Higher": "대학 학위 이상",
"White‑Collar Professionals": "화이트칼라 전문직",

# ===== WeChat page =====
"Build brand presence in WeChat's content ecosystem. Reach subscribers through articles, updates, and native advertising.":
    "WeChat의 콘텐츠 생태계에서 브랜드 입지를 구축하세요. 기사, 업데이트, 네이티브 광고를 통해 구독자에게 도달합니다.",
"In-article ad placements": "기사 내 광고 배치",
"Lightweight apps inside WeChat for e-commerce, lead generation, and customer engagement — no downloads required.":
    "WeChat 내 경량 앱으로 전자상거래, 리드 생성, 고객 참여 — 다운로드 불필요.",
"In-WeChat app store advertising": "WeChat 앱스토어 내 광고",
"Direct access from 公式アカウント": "공식 계정에서 직접 액세스",
"Decision-Makers — Senior professionals with high purchasing power":
    "의사결정권자 — 높은 구매력을 가진 시니어 전문직",
"Digital Natives — Gen Z & Millennials, heavy social & content consumers":
    "디지털 네이티브 — Z세대 및 밀레니얼, 소셜 및 콘텐츠 헤비 유저",
"E-Commerce Shoppers — WeChat Pay users, impulse & habitual buyers":
    "전자상거래 쇼퍼 — WeChat Pay 사용자, 충동 및 습관적 구매자",
"Senior Professionals — 40-55 age group, B2B decision influencers":
    "시니어 전문직 — 40~55세, B2B 의사결정 영향력자",
"Unlike transactional platforms, WeChat is a": "거래형 플랫폼과 달리 WeChat은",
"relationship ecosystem": "관계 구축 생태계",
"Users spend 70+ minutes daily communicating, reading, shopping, and paying — all within one app.":
    "사용자는 매일 70분 이상을 커뮤니케이션, 독서, 쇼핑, 결제에 할애합니다 — 모두 하나의 앱 안에서.",
"No platform switching, no lost attention.": "플랫폼 전환 불필요, 주의 분산 없음.",
"The Demographic Advantage": "인구통계학적 우위",
"Why WeChat Is Different": "WeChat이 다른 이유",
"Unlike entertainment platforms, WeChat is where decisions happen — in corporate chat groups, payment approvals, and long-form reading sessions.":
    "엔터테인먼트 플랫폼과 달리 WeChat은 결정이 이루어지는 곳입니다 — 기업 채팅 그룹, 결제 승인, 장문 독서 세션에서.",
"The Professional Hub": "프로페셔널 허브",
'WeChat is the "LinkedIn of China." 50%+ of Official Account readers hold university degrees.':
    'WeChat은 "중국의 LinkedIn"입니다. 공식 계정 독자의 50% 이상이 대학 학위를 보유하고 있습니다.',
"University degree holders": "대학 학위 보유자",
"25-40 (Core professionals)": "25~40세 (핵심 전문직)",
"High-income users": "고소득 사용자",
"WeChat Pay active users": "WeChat Pay 활성 사용자",
"Mini Program annual transactions": "미니 프로그램 연간 거래액",
"Content marketing campaigns": "콘텐츠 마케팅 캠페인",
"Moments & Search Ads": "모먼트 및 검색 광고",
"Reach users natively in Moments feed, WeChat Search, and the Snap Moment ad format — driven by Tencent's data engine.":
    "모먼트 피드, WeChat 검색, 스냅 모먼트 광고 형식에서 네이티브하게 사용자에게 도달 — Tencent의 데이터 엔진 기반.",
"Moments native advertising": "모먼트 네이티브 광고",
"WeChat Search brand keywords": "WeChat 검색 브랜드 키워드",
"Tencent DMP audience targeting": "Tencent DMP 오디언스 타겟팅",

# ===== Bilibili page =====
"Bilibili is where China's next generation of consumers lives. 366 million users, 82% under age 35, spending 107 minutes per day across 22 interest communities.":
    "Bilibili는 중국 차세대 소비자가 모이는 곳입니다. 3억 6,600만 사용자, 82%가 35세 미만, 22개 관심 커뮤니티에서 하루 107분을 보냅니다.",
"80%+ top content over 10min": "상위 콘텐츠의 80%+가 10분 초과",
"Monthly active (30+ days)": "월간 활성(30일 이상)",
"Gen Z Power Users — 18-25, heavy daily engagement, 107min+ sessions":
    "Z세대 파워 유저 — 18~25세, 높은 일일 참여도, 107분+ 세션",
"Tech-Savvy Early Adopters — first to buy new products and share reviews":
    "테크에 능숙한 얼리 어답터 — 신제품을 가장 먼저 구매하고 리뷰 공유",
"ゲーム & Anime Community — strong in categories like 3C, ACG, and lifestyle":
    "게임 및 애니메이션 커뮤니티 — 3C, ACG, 라이프스타일 카테고리에서 강세",
"Bilibili is not about": "Bilibili는",
"quick impressions": "빠른 노출",
"community trust, not brand interruption": "브랜드 방해가 아닌 커뮤니티 신뢰",
"Users follow creators they trust, engage deeply with long-form content, and convert because of":
    "사용자는 신뢰하는 크리에이터를 팔로우하고, 장문 콘텐츠에 깊이 참여하며, 다음 이유로 전환합니다:",
"80%+ 12-month retention means your message compounds over time rather than disappearing after one campaign.":
    "80%+ 12개월 유지율은 메시지가 한 번의 캠페인 후 사라지는 것이 아니라 시간이 지남에 따라 축적된다는 것을 의미합니다.",
"The Bilibili Advantage": "Bilibili의 강점",
"Unlike short-form platforms built on quick hits, Bilibili earns real attention.":
    "빠른 히트를 노리는 숏폼 플랫폼과 달리 Bilibili는 진정한 관심을 얻습니다.",
"Nearly 70% of China's post-90s generation (including Gen Z) is active on Bilibili.":
    "중국 90년대 이후 세대(Z세대 포함)의 약 70%가 Bilibili에서 활동합니다.",
"Post-90s on Bilibili": "Bilibili의 90년대 이후 세대",
"New user average age": "신규 사용자 평균 연령",
"Most platforms lose users fast. Bilibili keeps them.":
    "대부분의 플랫폼은 사용자를 빠르게 잃습니다. Bilibili는 사용자를 유지합니다.",
"This isn't a platform for 15-second clips. Bilibili's top content is 10+ minutes on average.":
    "15초 클립을 위한 플랫폼이 아닙니다. Bilibili의 상위 콘텐츠는 평균 10분 이상입니다.",
"Monthly paying users": "월간 결제 사용자",
"Avg interests per user": "사용자당 평균 관심사",
"Let's talk about how Bilibili fits your China marketing strategy.":
    "Bilibili가 귀사의 중국 마케팅 전략에 어떻게 적합한지 상담해보세요.",

# ===== Bing page =====
"Capture high-intent users actively researching your product category on Bing China.":
    "Bing China에서 제품 카테고리를 적극적으로 조사하는 구매 의도가 높은 사용자를 포착하세요.",
"Reach Bing China's premium audience across the Microsoft Advertisingネットワーク — display banners, in-feed native ads, and co-branded content solutions.":
    "Microsoft Advertising 네트워크 전반에 걸쳐 Bing China의 프리미엄 오디언스에 도달 — 디스플레이 배너, 인피드 네이티브 광고, 공동 브랜드 콘텐츠 솔루션.",
"Display Advertising": "디스플레이 광고",
"Tech-Savvy Professionals — 68% AI interest, early adopters":
    "테크에 능숙한 전문직 — AI 관심도 68%, 얼리 어답터",
"White-Collar Urban Workers — Tier 1–3 cities":
    "화이트칼라 도시 근로자 — Tier 1~3 도시",
"教育-Focused Parents — 72% plan education spending":
    "교육 중시 부모 — 72%가 교육비 계획",
"Rational Consumers — Research-first, planned spending":
    "합리적 소비자 — 리서치 우선, 계획적 지출",
"B2B Decision Makers — Professional, high-authority":
    "B2B 의사결정권자 — 전문적, 높은 권한",
"Why Bing China Over Baidu?": "Baidu 대신 Bing China를 선택해야 하는 이유",
"Ready to Reach Bing China's Premium Audience?":
    "Bing China의 프리미엄 오디언스에 도달할 준비가 되셨나요?",
"Avg monthly consumption": "월평균 소비액",

# ===== Xiaohongshu page =====
"Native-feeling ads that appear in the user's feed alongside organic content.":
    "오가닉 콘텐츠와 함께 사용자 피드에 표시되는 네이티브 광고.",
"小紅書で特定の商品、ブランド、カテゴリーを検索する購買意欲の高いユーザーを獲得。":
    "샤오홍슈에서 특정 제품, 브랜드, 카테고리를 검색하는 구매 의도가 높은 사용자 확보.",
"Leverage Xiaohongshu's creator ecosystem for authentic brand endorsements.":
    "샤오홍슈의 크리에이터 생태계를 활용한 진정성 있는 브랜드 추천.",
"95后 (Post-95 Millennials)": "95후 (포스트95 밀레니얼)",
"Usage Engagement": "사용자 참여",
"Daily Use — General Users (120M+)": "일일 사용자 — 일반 사용자(1.2억+)",
"Daily Use — Tier 3+ Users (190M+)": "일일 사용자 — Tier 3+ (1.9억+)",
"Interest communities": "관심 커뮤니티",
"Top Interest Categories — Monthly Active Reach": "주요 관심 카테고리 — 월간 활성 도달",
"Beauty / Cosmetics — 190M+": "뷰티/화장품 — 1.9억+",
"Parenting & Maternity — 190M+": "육아/출산 — 1.9억+",
"Health Supplements — 190M+": "건강 보조제 — 1.9억+",
"Fitness & Wellness — +276% YoY": "피트니스/웰니스 — 전년 대비 +276%",
"Mountain Running — +208%": "트레일 러닝 — 전년 대비 +208%",

# ===== Services overview =====
"— Your single point of access to China's $100B digital advertising market. We help international agencies navigate Chinese platforms and maximize ROI.":
    "— 중국 1,000억 달러 디지털 광고 시장으로의 단일 액세스 포인트. 국제 에이전시가 중국 플랫폼을 탐색하고 ROI를 극대화할 수 있도록 지원합니다.",
"1.3 billion users. 公式アカウント, ミニプログラム, Moments Ads, and Search — all connected within a single ecosystem.":
    "13억 사용자. 공식 계정, 미니 프로그램, 모먼트 광고, 검색 — 모두 하나의 생태계에 연결.",

# ===== GEO page =====
"While the West debates AI search, China's already living in it. 1 billion users, 47% of all search behavior migrated to AI assistants. GEO — Generative Engine Optimization — is the new SEM. We help you get cited, get cited fast.":
    "서구가 AI 검색을 논의하는 동안 중국은 이미 AI 검색을 일상적으로 사용하고 있습니다. 10억 사용자, 전체 검색 행동의 47%가 AI 어시스턴트로 전환. GEO(생성 엔진 최적화)가 새로운 SEM입니다. 인용받으세요, 빠르게 인용받으세요.",
"従来のSEO gets you found. GEO gets you cited inside AI answers — before the user ever clicks a link.":
    "기존 SEO는 발견되게 합니다. GEO는 사용자가 링크를 클릭하기 전에 AI 답변 내에서 인용되게 합니다.",
"Google, Baidu, Bing": "Google, Baidu, Bing",
"DeepSeek, Douyin AI, Kimi, Wenxin, ChatGPT-CN":
    "DeepSeek, Douyin AI, Kimi, 원신, ChatGPT-CN",
"Baidu still matters, but declining": "Baidu는 여전히 중요하지만 감소 추세",
"China's AI search is fragmented — and that's the opportunity":
    "중국의 AI 검색은 파편화되어 있습니다 — 그것이 기회입니다",
"Data: QuestMobile, November 2025.": "데이터: QuestMobile, 2025년 11월.",
"GEO Content Strategy": "GEO 콘텐츠 전략",
"Structured data optimization (FAQ, HowTo, Article schema)":
    "구조화된 데이터 최적화 (FAQ, HowTo, 아티클 스키마)",
"Brand citation signal building": "브랜드 인용 신호 구축",
"Cross-platform content adaptation (Chinese + English)":
    "플랫폼 간 콘텐츠 적응 (중국어 + 영어)",
"Entity clarity and knowledge graph optimization":
    "엔티티 명확화 및 지식 그래프 최적화",
"Citation monitoring and rank tracking": "인용 모니터링 및 순위 추적",
"AI Search Advertising": "AI 검색 광고",
"AI answer context ads (in-chat placements)": "AI 답변 컨텍스트 광고(채팅 내 배치)",
"Kimi brand search integrations": "Kimi 브랜드 검색 통합",

# ===== Pricing =====
"All platforms included": "모든 플랫폼 포함",
"Setup Fee: 〜 $100+ (one-time)": "설정 수수료: 약 $100+ (일회성)",
"広告費の + one-time setup fee": "광고비 + 일회성 설정 수수료",
"お問い合わせ us for platform-specific pricing":
    "플랫폼별 가격은 문의해주세요",

# ===== About =====
"China's digital advertising market is massive, complex, and largely inaccessible to international agencies.":
    "중국의 디지털 광고 시장은 거대하고 복잡하며, 국제 에이전시가 접근하기 어렵습니다.",
"We're not interested in one-off transactions. Our average client relationship spans 6+ years because we invest in your long-term success.":
    "저희는 일회성 거래에 관심이 없습니다. 평균 고객 관계는 6년 이상이며, 이는 귀하의 장기적 성공에 투자하기 때문입니다.",

# ===== Client Stories =====
"導入前の課題: Breaking into China's Regulated Gaming Market":
    "도입 전 과제: 중국 규제 게임 시장 진출",
"Our Strategic Approach": "당사의 전략적 접근 방식",
"The Outcome: Six-Year Partnership and Sustained Growth":
    "결과: 6년 파트너십 및 지속적 성장",
"Overcoming platform rejections in China's regulated gaming advertising market to achieve sustained growth across multiple Chinese platforms.":
    "중국 규제 게임 광고 시장에서 플랫폼 거부를 극복하고 여러 중국 플랫폼에서 지속적 성장 달성.",

# ===== Blog =====
"Expert analysis on China's digital advertising landscape — SEM strategies, platform updates, market insights, and case studies from the TMG team.":
    "중국 디지털 광고 환경에 대한 전문가 분석 — SEM 전략, 플랫폼 업데이트, 시장 인사이트, TMG 팀의 사례 연구.",

# ===== FAQ page labels =====
"Account & Setup": "계정 및 설정",
"Fees & Budget": "수수료 및 예산",
"Billing & CPC": "청구 및 CPC",
"Compliance & Review": "규정 준수 및 검토",
"Strategy & Targeting": "전략 및 타겟팅",
"GEO Basics": "GEO 기초",
"GEO Pricing & Budget": "GEO 가격 및 예산",
"GEO Service & Delivery": "GEO 서비스 및 제공",
"GEO vs SEO & Strategy": "GEO vs SEO 및 전략",
"Baidu SEM FAQ": "Baidu SEM FAQ",
"Xiaohongshu FAQ": "샤오홍슈(RED) FAQ",
"WeChat Ads FAQ": "WeChat 광고 FAQ",
"Douyin / Ocean Engine FAQ": "Douyin / Ocean Engine FAQ",
"Bilibili FAQ": "Bilibili FAQ",
"Bing China FAQ": "Bing China FAQ",
"China GEO FAQ": "중국 GEO FAQ",

# ===== Contact page =====
"Or Use the Form": "또는 양식 사용하기",
"Message us directly on WhatsApp. We reply within 1 business day.":
    "WhatsApp으로 직접 메시지를 보내주세요. 1영업일 이내에 답변드립니다.",

# ===== Additional content translations =====
# Homepage
"The West debates AI search, China's already living in it. 1 billion users, 47% of all search behavior migrated to AI assistants. GEO — Generative Engine Optimization — is the new SEM.":
    "서구가 AI 검색을 논의하는 동안 중국은 이미 AI 검색을 일상적으로 사용합니다. 10억 사용자, 전체 검색 행동의 47%가 AI 어시스턴트로 전환. GEO(생성 엔진 최적화)가 새로운 SEM입니다.",
"Baidu's official minimum is": "Baidu의 공식 최소 금액은",
"To save on transaction fees and reduce transfer time, we recommend":
    "송금 수수료를 절약하고 입금 시간을 단축하기 위해 다음을 권장합니다:",
"Annual account authentication fee of CNY 600":
    "연간 계정 인증 수수료 600위안",
". For new users, this fee is refunded to your ad account after the first year, making it free for year one.":
    "신규 사용자의 경우 이 수수료는 1년 후 광고 계정으로 환불되어 첫해는 무료입니다.",

# GEO additional
"Weekly reports + real-time monitoring dashboard":
    "주간 리포트 + 실시간 모니터링 대시보드",
"For ongoing, full-funnel GEO operations with maximum flexibility":
    "지속적인 전체 퍼널 GEO 운영, 최대 유연성",
"100 keywords (prompt phrases), editable monthly":
    "100개 키워드(프롬프트 구문), 월별 편집 가능",
"Full access to review every content asset published":
    "게시된 모든 콘텐츠 자산 검토를 위한 전체 액세스",
"Sentiment monitoring &amp; reputation management":
    "센티먼트 모니터링 및 평판 관리",
"Monthly citation reports + competitive benchmarking":
    "월간 인용 리포트 + 경쟁사 벤치마킹",
"Dedicated GEO strategist on retainer":
    "전담 GEO 전략가(리테이너 방식)",
"What is GEO and how does it differ from SEO?":
    "GEO란 무엇이며 SEO와 어떻게 다른가요?",
"How long does it take to see GEO results?":
    "GEO 결과를 보려면 얼마나 걸리나요?",

# Client Stories - Farmskins
"The platform's unique value proposition of skin trading and marketplace operations fell into regulatory gray areas.":
    "스킨 거래 및 마켓플레이스 운영이라는 독특한 가치 제안은 규제 회색 지대에 속했습니다.",
"Regulatory compliance is non-negotiable": "규제 준수는 양보할 수 없는 조건",
"but can be navigated with the right expertise": "하지만 적절한 전문 지식으로 해결 가능",
"Platform rejections are often starting points": "플랫폼 거부는 종종",
"for deeper engagement, not final decisions": "최종 결정이 아닌 더 깊은 관여의 시작점",
"Cultural and linguistic adaptation": "문화적, 언어적 적응",
"is essential for successful market entry": "성공적인 시장 진입에 필수적",
"Six-year ongoing partnership": "6년간의 지속적인 파트너십",
"with consistent advertising campaigns across multiple Chinese platforms":
    "여러 중국 플랫폼에서의 일관된 광고 캠페인",
"Continuous optimization": "지속적 최적화",
"of advertising strategies based on performance data and market feedback":
    "성과 데이터 및 시장 피드백에 기반한 광고 전략 최적화",

# Client Stories - AI Semiconductor
"One agency, one point of contact, clearer reporting, and a more efficient way to manage complex paid media activity.":
    "하나의 에이전시, 하나의 연락 창구, 명확한 보고, 복잡한 유료 미디어 활동을 관리하는 더 효율적인 방법.",
"Global AI & Semiconductor Brand": "글로벌 AI 및 반도체 브랜드",
"Multi-Platform Management": "멀티 플랫폼 관리",
"When paid media becomes too fragmented": "유료 미디어가 너무 분산될 때",
"For large B2B brands, paid media should support growth — not create operational complexity.":
    "대규모 B2B 브랜드의 경우, 유료 미디어는 성장을 지원해야 하며 운영 복잡성을 만들어서는 안 됩니다.",

# FAQ Key Questions
"What are the common reasons for Baidu ad rejection?":
    "Baidu 광고 거부의 일반적인 이유는 무엇인가요?",
"What are common prohibited words in Baidu ads?":
    "Baidu 광고에서 흔한 금지어는 무엇인가요?",
"Do healthcare and finance industries have special requirements on Baidu?":
    "의료 및 금융 업종은 Baidu에서 특별 요구사항이 있나요?",
"Can foreign companies run ads on Xiaohongshu?":
    "외국 기업이 샤오홍슈에서 광고할 수 있나요?",
"What documents are needed to advertise on Xiaohongshu?":
    "샤오홍슈에서 광고하는 데 필요한 서류는 무엇인가요?",
"How long does Xiaohongshu account approval take?":
    "샤오홍슈 계정 승인에는 얼마나 걸리나요?",
"What are the rules for the Xiaohongshu account name?":
    "샤오홍슈 계정 이름의 규칙은 무엇인가요?",
"How does Xiaohongshu advertising charge?":
    "샤오홍슈 광고 요금은 어떻게 부과되나요?",
"What is the minimum budget to advertise on Xiaohongshu?":
    "샤오홍슈에서 광고하는 최소 예산은 얼마인가요?",
"Are there any fees besides the advertising spend on Xiaohongshu?":
    "샤오홍슈의 광고 지출 외에 다른 수수료가 있나요?",
"How much does a click cost on Xiaohongshu?":
    "샤오홍슈에서 클릭당 비용은 얼마인가요?",
"Why is my Xiaohongshu ad spend not going through?":
    "샤오홍슈 광고 비용이 집행되지 않는 이유는 무엇인가요?",
"Can foreign companies advertise on WeChat?":
    "외국 기업이 WeChat에서 광고할 수 있나요?",
"What is the minimum budget to advertise on WeChat?":
    "WeChat에서 광고하는 최소 예산은 얼마인가요?",
"Can overseas companies advertise on Douyin?":
    "해외 기업이 Douyin에서 광고할 수 있나요?",
"What is the minimum budget for Ocean Engine?": "Ocean Engine의 최소 예산은 얼마인가요?",
"How does Ocean Engine charge for advertising?":
    "Ocean Engine의 광고 요금은 어떻게 부과되나요?",
"Can foreign companies advertise on Bilibili?":
    "외국 기업이 Bilibili에서 광고할 수 있나요?",
"What is the minimum budget for Bilibili advertising?":
    "Bilibili 광고의 최소 예산은 얼마인가요?",
"Does Bilibili offer post-payment or credit terms?":
    "Bilibili는 후불 또는 신용 조건을 제공하나요?",

# Blog post cards
"Doubao Goes Paid: What This Means for GEO in China":
    "Doubao 유료화: 중국 GEO에 미치는 영향",
"Expert analysis on China's digital advertising landscape":
    "중국 디지털 광고 환경에 대한 전문가 분석",
"Bing China Demographics: Who Are These High-Value Users?":
    "Bing China 인구통계: 이 고가치 사용자는 누구인가요?",
"Kuaishou (Kwai) Demographics": "Kuaishou (Kwai) 인구통계",
"Xiaohongshu (RED) Demographics": "샤오홍슈(RED) 인구통계",
"Baidu Search Demographics": "Baidu 검색 인구통계",
"Bilibili Demographics": "Bilibili 인구통계",
"Attribution Models in Paid Media": "유료 미디어의 기여 모델",
"Ad Billing Models Explained": "광고 청구 모델 설명",
"Smart Bidding Strategies": "스마트 입찰 전략",
"China Market Insights": "중국 시장 인사이트",
"Is a Rising CPM Really That Bad?": "CPM 상승이 정말 나쁜가요?",
"CPM, oCPM, eCPM: The Three Metrics Every Paid Media Buyer Gets Wrong":
    "CPM, oCPM, eCPM: 모든 유료 미디어 바이어가 혼동하는 세 가지 지표",
"GEO Channel Weight Update 2026": "GEO 채널 가중치 업데이트 2026",

# Common remaining
"Your single point of access to China's $100B digital advertising market. We help international agencies navigate Chinese platforms with ease.":
    "중국 1,000억 달러 디지털 광고 시장으로의 단일 액세스 포인트. 국제 에이전시가 중국 플랫폼을 쉽게 탐색할 수 있도록 지원합니다.",
"How we can help": "당사가 도울 수 있는 방법",
"Get in touch": "문의하기",
"Send Message": "메시지 보내기",
"Your Name": "이름",
"Your Email": "이메일",
"Your Message": "메시지",
"Submit": "제출",
"Loading": "로딩 중",
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
