#!/usr/bin/env python3
"""
Final sweep: Translate ALL remaining English text fragments in ko/ pages.
Uses regex-based text extraction and replacement - safe for HTML.
"""
import re, os, html as htmlmod

BASE = os.path.dirname(os.path.abspath(__file__))

# Large translation dictionary for remaining fragments
KO = {
# FAQ Baidu fragments
"No functional difference. The only distinction is in the ad display: the company name shown at the bottom of your ads will be either your foreign company name or your Chinese entity name, depending on which type of account you use.":
    "기능적 차이는 없습니다. 유일한 차이는 광고 표시에 있습니다: 광고 하단에 표시되는 회사 이름이 사용하는 계정 유형에 따라 외국 회사 이름 또는 중국 법인 이름이 됩니다.",
"(c) Bank account certificate + translated document from designated institution (stamped with company seal), such as bank transfer records, bank statements, or account opening certificates.":
    "(c) 은행 계좌 증명서 + 지정 기관의 번역 문서(회사 직인 날인)(예: 은행 송금 기록, 은행 거래 명세서 또는 계좌 개설 증명서).",
"Follow these steps: (1) Read the review notes carefully; (2) Revise the specific content flagged; (3) Re-submit for review; (4) If you believe the rejection was in error, contact your agency for clarification.":
    "다음 단계를 따르세요: (1) 검토 의견을 주의 깊게 읽으십시오; (2) 지적된 특정 내용을 수정하십시오; (3) 재검토를 위해 다시 제출하십시오; (4) 거부가 오류라고 생각되면 에이전시에 문의하여 확인하십시오.",
"Pre-paid advertising fee: minimum CNY 2,400. Service fee: starting from USD 100, which includes document translation, document review, and submission to the Baidu platform on your behalf.":
    "선불 광고비: 최소 2,400위안. 서비스 수수료: USD 100부터 시작하며, 문서 번역, 문서 검토, Baidu 플랫폼 제출 대행이 포함됩니다.",
"Cost per click: There is no uniform price. Low-competition keywords may cost a few yuan per click. In highly competitive industries, popular keywords can cost significantly more — sometimes CNY 50–100+ per click.":
    "클릭당 비용: 균일한 가격은 없습니다. 경쟁이 낮은 키워드는 클릭당 몇 위안일 수 있습니다. 경쟁이 치열한 업종에서는 인기 키워드의 비용이 상당히 높아질 수 있습니다 — 때로는 클릭당 50~100위안 이상.",

# FAQ WeChat fragments  
"Yes. Foreign companies can run ads on WeChat through a certified agency partner. WeChat requires a Chinese business license for direct registration, but TMG can facilitate the process as an authorized reseller.":
    "네. 외국 기업은 공인 에이전시 파트너를 통해 WeChat에서 광고할 수 있습니다. WeChat은 직접 등록을 위해 중국 영업 허가증이 필요하지만, TMG가 공인 리셀러로서 프로세스를 지원할 수 있습니다.",
"At minimum, you need a Chinese business license or a partnership with a certified WeChat advertising agency. Depending on your industry and ad content, you may also need trademark certificates, ICP filing, or industry licenses.":
    "최소한 중국 영업 허가증 또는 공인 WeChat 광고 에이전시와의 파트너십이 필요합니다. 업종 및 광고 내용에 따라 상표 증명서, ICP 등록 또는 업종 라이선스가 추가로 필요할 수 있습니다.",
"Foreign entities typically need a BR or CR certificate (Hong Kong companies) or equivalent documentation for other jurisdictions, such as a certificate of incorporation or business registration.":
    "외국 법인은 일반적으로 BR 또는 CR 증명서(홍콩 기업) 또는 설립 증명서나 사업자 등록증과 같은 기타 관할권에 대한 이에 상응하는 서류가 필요합니다.",
"Most advertisers start with CPM or CPC. The right choice depends on your campaign objective — we can advise on which model fits your goal during onboarding.":
    "대부분의 광고주는 CPM 또는 CPC로 시작합니다. 올바른 선택은 캠페인 목표에 따라 다릅니다 — 온보딩 중에 어떤 모델이 목표에 맞는지 조언해 드릴 수 있습니다.",
"With regular CPC, you pay for each click regardless of what happens after. With oCPC, you define a conversion event and the system optimizes toward users most likely to complete that action.":
    "일반 CPC는 이후에 무슨 일이 일어나든 각 클릭에 대해 비용을 지불합니다. oCPC를 사용하면 전환 이벤트를 정의하고 시스템이 해당 작업을 완료할 가능성이 가장 높은 사용자를 대상으로 최적화합니다.",
"Use oCPC when you want to focus on results, not just traffic. The catch: you need enough conversion data for the algorithm to optimize effectively.":
    "트래픽뿐만 아니라 결과에 집중하려면 oCPC를 사용하세요. 단점: 알고리즘이 효과적으로 최적화하려면 충분한 전환 데이터가 필요합니다.",
"There is no official minimum budget published by WeChat, but in practice you need at least CNY 5,000 to 10,000 for meaningful testing and initial campaigns. Once you have data, you can optimize and scale up.":
    "WeChat이 공식적으로 발표한 최소 예산은 없지만, 실제로 의미 있는 테스트와 초기 캠페인을 위해 최소 5,000~10,000위안이 필요합니다. 데이터가 확보되면 최적화하고 확장할 수 있습니다.",
"WeChat ads work well for brands that want to build awareness within specific Moments feed placements, drive traffic to mini programs, or retarget users who have interacted with their brand.":
    "WeChat 광고는 특정 모먼트 피드 배치 내에서 인지도를 구축하거나, 미니 프로그램으로 트래픽을 유도하거나, 브랜드와 상호작용한 사용자를 리타겟팅하려는 브랜드에 효과적입니다.",
"There is no fixed CPC — it varies by industry, targeting, and ad placement. WeChat Moments ads tend to have higher CPCs than in-article placements. Competitive categories can be significantly more expensive.":
    "고정 CPC는 없습니다 — 업종, 타겟팅, 광고 배치에 따라 다릅니다. WeChat 모먼트 광고는 기사 내 배치보다 CPC가 높은 경향이 있습니다. 경쟁 카테고리는 상당히 더 비쌀 수 있습니다.",
"We will share benchmark data for your specific industry during our onboarding call. This helps you set realistic expectations and competitive bids from day one.":
    "온보딩 통화 중 귀하의 특정 업종에 대한 벤치마크 데이터를 공유해 드립니다. 이를 통해 첫날부터 현실적인 기대치와 경쟁력 있는 입찰가를 설정할 수 있습니다.",
"We will recommend the right mix based on your target audience and campaign goals. Our team has experience across all Tencent Ads formats and can optimize your portfolio.":
    "타겟 오디언스와 캠페인 목표에 따라 적절한 조합을 추천해 드립니다. 당사 팀은 모든 Tencent Ads 형식에 대한 경험이 있으며 포트폴리오를 최적화할 수 있습니다.",

# GEO remaining
"SEO (Search Engine Optimization) aims to rank your website high in traditional search results — users click a link to reach you. GEO (Generative Engine Optimization) aims to get your brand mentioned inside AI answers — before the user ever clicks a link.":
    "SEO(검색 엔진 최적화)는 전통적인 검색 결과에서 웹사이트 순위를 높이는 것을 목표로 합니다 — 사용자가 링크를 클릭하여 도달합니다. GEO(생성 엔진 최적화)는 사용자가 링크를 클릭하기 전에 AI 답변 내에서 브랜드가 언급되도록 하는 것을 목표로 합니다.",
"Most clients see measurable results within 1–2 weeks. Initial citation improvements can appear within 3–5 business days after deployment. For competitive or high-volume keywords, full stabilization typically takes 1–3 months.":
    "대부분의 클라이언트는 1~2주 이내에 측정 가능한 결과를 확인합니다. 배포 후 3~5영업일 이내에 초기 인용 개선이 나타날 수 있습니다. 경쟁이 치열하거나 볼륨이 많은 키워드의 경우 완전한 안정화는 일반적으로 1~3개월이 소요됩니다.",

# Misc remaining  
"More representative of general population": "일반 인구를 더 잘 대표함",
"Additionally, 62% of users show greater willingness to engage with ads compared to average users. This makes Bing China ideal for brands seeking quality engagement over raw volume.":
    "또한 62%의 사용자가 평균 사용자보다 광고에 참여할 의사가 더 높습니다. 이는 Bing China를 원시 볼륨보다 품질 참여를 원하는 브랜드에 이상적으로 만듭니다.",
"Response time: Within 24 hours (weekdays)": "응답 시간: 24시간 이내(평일 기준)",
"Languages: English, Mandarin, Cantonese": "언어: 영어, 중국어, 광둥어",
"Business License Number: 91310114MADKG4UF0G": "사업자 등록 번호: 91310114MADKG4UF0G",
"TUYUE SOUXIN (SHANGHAI) INFORMATION TECHNOLOGY CO., LTD.":
    "TUYUE SOUXIN (SHANGHAI) INFORMATION TECHNOLOGY CO., LTD.",

# Xiaohongshu remaining
"Some industries need special approval before they can run ads. Check with us before you plan your campaign — it saves time.":
    "일부 업종은 광고를 게재하기 전에 특별 승인이 필요합니다. 캠페인을 계획하기 전에 문의해 주세요 — 시간을 절약할 수 있습니다.",
}

def translate_all():
    """Process all ko/ HTML files"""
    files = []
    for root, dirs, filenames in os.walk(os.path.join(BASE, 'ko')):
        for fn in filenames:
            if fn.endswith('.html'):
                files.append(os.path.join(root, fn))
    
    total = 0
    for fp in sorted(files):
        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()
        
        orig = content
        # Apply dictionary translations
        for eng, kor in sorted(KO.items(), key=lambda x: -len(x[0])):
            if eng in content:
                content = content.replace(eng, kor)
                total += 1
        
        # Now find remaining English text between > and < tags
        # and translate inline for visible content
        def replace_english(match):
            text = match.group(1)
            decoded = htmlmod.unescape(text)
            eng = len(re.findall(r'[a-zA-Z]', decoded))
            jp_ko = len(re.findall(r'[\uac00-\ud7af\u3130-\u318f\u3040-\u309f\u30a0-\u30ff\u4e00-\u9fff]', decoded))
            
            # Only translate if clearly English and not already in KO dict
            if eng > 30 and jp_ko < 2:
                # Skip if starts with obvious code patterns
                if any(decoded.startswith(p) for p in ['var ', 'function', 'return', 'if ', 'for ', 'const ', 'let ']):
                    return match.group(0)
                
                # Translate the decoded text
                translation = translate_text(decoded)
                if translation and translation != decoded:
                    return '>' + translation + '<'
            
            return match.group(0)
        
        if total > 0 or content != orig:
            with open(fp, 'w', encoding='utf-8') as f:
                f.write(content)
        
        rel = fp.replace(BASE + os.sep, '').replace(os.sep, '/')
        print(f'  {rel}: {total} replacements')
    
    print(f'\nTotal: {total}')
    return total

# Inline translation helper for small text fragments
def translate_text(text):
    """Translate a text fragment to Korean. Returns translated text or original."""
    t = text.strip()
    
    # Skip very short text
    if len(t) < 5:
        return text
    
    translations = {
        # Common remaining fragments
        "No functional difference. The only distinction is in the ad display: the company name shown at the bottom of your ads":
            "기능적 차이는 없습니다. 유일한 차이는 광고 표시에 있습니다: 광고 하단에 표시되는 회사 이름이",
        "with consistent advertising campaigns across multiple Chinese platforms, achieving sustained growth in a once-closed market.":
            "여러 중국 플랫폼에서의 일관된 광고 캠페인으로, 한때 폐쇄되었던 시장에서 지속적 성장을 달성했습니다.",
        "in the Chinese market despite initial regulatory challenges, proving that the right partner makes all the difference.":
            "초기 규제 문제에도 불구하고 중국 시장에서, 올바른 파트너가 모든 차이를 만든다는 것을 증명했습니다.",
        "of complex platform policies and regulatory requirements, turning barriers into competitive advantages.":
            "복잡한 플랫폼 정책 및 규제 요구사항을 장벽에서 경쟁 우위로 전환했습니다.",
        "on platforms that initially rejected Farmskins' business model, demonstrating that persistence and expertise pay off.":
            "초기에 Farmskins의 비즈니스 모델을 거부했던 플랫폼에서, 인내와 전문성이 결실을 맺음을 입증했습니다.",
        "of advertising strategies based on performance data and market feedback, ensuring campaigns remain effective over time.":
            "성과 데이터 및 시장 피드백에 기반한 광고 전략을 최적화하여 캠페인이 시간이 지나도 효과적으로 유지되도록 보장했습니다.",
        "Bing China's user base represents a premium audience: highly educated, urban, and with above-average income levels. More than 75% hold college degrees.":
            "Bing China의 사용자 기반은 프리미엄 오디언스를 대표합니다: 고학력, 도시 거주, 평균 이상의 소득 수준. 75% 이상이 대학 학위를 보유하고 있습니다.",
        "This makes Bing China users ideal for brands targeting educated professionals, urban consumers, and high-value segments.":
            "이는 Bing China 사용자를 교육받은 전문직, 도시 소비자, 고가치 세그먼트를 타겟팅하는 브랜드에 이상적으로 만듭니다.",
        "Bing China attracts a younger, more educated, and higher-income demographic compared to Baidu's broader, more diversified user base.":
            "Bing China는 Baidu의 더 넓고 다양한 사용자 기반에 비해 더 젊고, 교육 수준이 높고, 소득이 높은 인구통계를 유치합니다.",
        "For international advertisers, this means Bing China offers a more premium audience, while Baidu provides maximum reach.":
            "국제 광고주에게 이는 Bing China가 더 프리미엄한 오디언스를 제공하는 반면, Baidu는 최대 도달 범위를 제공한다는 것을 의미합니다.",
        "Bing China users show strong purchasing intent across several categories, with average planned spending of ¥3,040.1 per month.":
            "Bing China 사용자는 여러 카테고리에서 강한 구매 의도를 보이며, 월평균 계획 지출액은 ¥3,040.1입니다.",
        "Additionally, 68% express interest in AI technology, making them early adopters for tech products and services.":
            "또한 68%가 AI 기술에 관심을 표현하여 기술 제품 및 서비스의 얼리 어답터입니다.",
        "What advertising formats work best on Bing China?":
            "Bing China에서 가장 효과적인 광고 형식은 무엇인가요?",
        "Based on user behavior data, the following ad formats perform well:":
            "사용자 행동 데이터에 따르면, 다음 광고 형식이 효과적입니다:",
        "59% of users research products before purchase, making search ads effective for capturing intent":
            "사용자의 59%가 구매 전 제품을 조사하므로, 검색 광고가 의도 포착에 효과적입니다",
        "With 68% interest in AI, technology-focused display ads see higher engagement":
            "AI 관심도 68%로, 기술 중심 디스플레이 광고가 더 높은 참여도를 보입니다",
        "Education and professional service promotions:":
            "교육 및 전문 서비스 프로모션:",
        "Over 75% college educated, with planned education spending averaging ¥3,040.1":
            "75% 이상 대학 교육, 계획된 교육 지출 평균 ¥3,040.1",
        "Higher income levels support premium product advertising":
            "높은 소득 수준이 프리미엄 제품 광고를 지원합니다",
        "Which industries are best suited for Bing China advertising?":
            "Bing China 광고에 가장 적합한 업종은 무엇인가요?",
        "68% interest in AI, high education level": "AI 관심도 68%, 높은 교육 수준",
        "High disposable income": "높은 가처분 소득",
        "Professional user base with decision-making authority":
            "의사결정 권한을 가진 전문 사용자 기반",
        "These categories align with the demographic and behavioral characteristics of Bing China users.":
            "이러한 카테고리는 Bing China 사용자의 인구통계학적 및 행동 특성과 일치합니다.",
        "Baidu SEM reaches users who are actively searching right now":
            "Baidu SEM은 지금 바로 적극적으로 검색하는 사용자에게 도달합니다",
        "Think of SEM as paying for a spot at the front of the line":
            "SEM은 줄 앞자리에 돈을 내는 것과 같습니다",
        "GEO is trying to become the name the waiter recommends":
            "GEO는 웨이터가 추천하는 이름이 되는 것입니다",
        "SEO first, in most cases. A functioning SEO foundation is table stakes for GEO.":
            "대부분의 경우 SEO가 먼저입니다. 기능하는 SEO 기반은 GEO의 기본 요건입니다.",
        "If you have no website or a site that is technically broken, fix that before paying for GEO.":
            "웹사이트가 없거나 기술적으로 손상된 사이트가 있는 경우, GEO에 비용을 지불하기 전에 수정하세요.",
        "We sometimes run both in parallel for clients with existing infrastructure, as the content work often overlaps significantly.":
            "기존 인프라가 있는 클라이언트의 경우 콘텐츠 작업이 종종 상당히 중복되므로 두 가지를 병렬로 실행하기도 합니다.",
        "Can GEO replace my existing SEO efforts?":
            "GEO가 기존 SEO 노력을 대체할 수 있나요?",
        "No. AI-generated answers do not replace search engine results pages":
            "아니요. AI 생성 답변은 검색 엔진 결과 페이지를 대체하지 않습니다",
        "GEO is an additional channel, not a replacement":
            "GEO는 추가 채널이지 대체가 아닙니다",
        "Cutting SEO to fund GEO would likely hurt your overall visibility in the long run.":
            "SEO를 줄여 GEO에 자금을 대면 장기적으로 전체 가시성을 해칠 가능성이 높습니다.",
    }
    
    if t in translations:
        return translations[t]
    
    return text

if __name__ == '__main__':
    print('Final Korean translation sweep...')
    translate_all()
