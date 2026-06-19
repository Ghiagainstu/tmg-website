import re
from pathlib import Path

WEBSITE = Path(r"C:\Users\fireh\WorkBuddy\20260326144402\tmg-website")

# Title translations (same as index titles)
TITLE_TRANSLATIONS = {
    'ja': {
        'baidu-ai-search-ads-2026': 'Baidu AI検索広告：検索広告の新時代',
        'baidu-brand-zone-2026': 'Baiduブランドゾーン2026：検索結果ページを支配する',
        'baidu-ecommerce-search-ads-2026': 'Baidu EC検索広告：AI時代の競争',
        'baidu-local-service-search-ads': 'Baiduローカルサービス広告：近隣顧客を獲得する',
        'baidu-search-creative-automation': 'Baidu検索クリエイティブ自動化：AI搭載広告作成',
        'baidu-search-keyword-expansion-ai': 'Baidu検索のAIキーワード拡張',
        'baidu-search-offline-to-online': 'Baidu検索：オフラインからオンラインへのブリッジ',
        'baidu-search-privacy-compliance-2026': 'Baidu検索プライバシー準拠：広告主が知るべきこと',
        'baidu-search-quality-score-advanced': 'Baidu品質スコア最適化の高度な戦略',
        'baidu-smart-mini-program-search-ads': 'Baiduスマートミニプログラム検索広告',
        'bilibili-brand-search-2026': 'Bilibiliブランド検索2026：Z世代の認知を支配する',
        'bilibili-creator-search-strategy': 'Bilibiliクリエイター検索戦略',
        'bilibili-ecommerce-search-ads': 'Bilibili EC検索広告：Z世代への販売',
        'bilibili-gaming-search-ads': 'Bilibiliゲーム検索広告',
        'bilibili-search-ads-2026': 'Bilibili検索広告2026：完全ガイド',
        'bilibili-search-content-matching': 'Bilibili検索コンテンツマッチング',
        'bilibili-search-creative-lab': 'Bilibili検索クリエイティブラボ',
        'bilibili-search-funnel-guide': 'Bilibili検索ファネルガイド',
        'bilibili-search-performance-2026': 'Bilibili検索パフォーマンス2026',
        'bilibili-youth-search-ads': 'Bilibiliユース検索広告',
        'bing-china-b2b-search-2026': 'Bing中国B2B検索2026',
        'bing-china-brand-search-2026': 'Bing中国ブランド検索2026',
        'bing-china-copilot-search-ads': 'Bing中国Copilot検索広告',
        'bing-china-cross-border-search-ads': 'Bing中国越境検索広告',
        'bing-china-education-search-ads': 'Bing中国教育検索広告',
        'bing-china-local-search-ads': 'Bing中国ローカル検索広告',
        'bing-china-performance-max-2026': 'Bing中国Performance Max 2026',
        'bing-china-premium-audience-guide': 'Bing中国プレミアムオーディエンスガイド',
        'bing-china-retail-search-ads': 'Bing中国小売検索広告',
        'bing-china-search-creative-guide': 'Bing中国検索クリエイティブガイド',
        'bing-china-travel-search-ads': 'Bing中国旅行検索広告',
        'douyin-brand-search-2026': '抖音ブランド検索2026',
        'douyin-content-search-discovery': '抖音コンテンツ検索ディスカバリー',
        'douyin-ecommerce-search-2026': '抖音EC検索広告2026',
        'douyin-live-search-conversion': '抖音ライブ検索コンバージョン',
        'douyin-local-life-search-ads': '抖音ローカルライフ検索広告',
        'douyin-search-ads-ranking-2026': '抖音検索広告ランキング2026',
        'douyin-search-competitive-analysis': '抖音検索競合分析',
        'douyin-search-creative-lab': '抖音検索クリエイティブラボ',
        'douyin-search-omni-funnel': '抖音検索オムニファネル',
        'douyin-sem-vs-search-feed-2026': '抖音SEM vs 検索フィード2026',
        'wechat-brand-zone-search-2026': 'WeChatブランドゾーン検索2026',
        'wechat-channels-search-discovery': 'WeChat Channels検索ディスカバリー',
        'wechat-mini-program-search-ads': 'WeChatミニプログラム検索広告',
        'wechat-mini-store-search-ads': 'WeChatミニストア検索広告',
        'wechat-omni-search-brand-strategy': 'WeChatオムニ検索ブランド戦略',
        'wechat-private-domain-search-retention': 'WeChatプライベートドメイン検索リテンション',
        'wechat-search-ads-2026': 'WeChat検索広告2026',
        'wechat-search-creative-testing': 'WeChat検索クリエイティブテスト',
        'wechat-search-funnel-optimization': 'WeChat検索ファネル最適化',
        'wechat-service-search-conversion': 'WeChatサービス検索コンバージョン',
        'xiaohongshu-brand-zone-search': '小紅書ブランドゾーン検索',
        'xiaohongshu-category-search-growth': '小紅書カテゴリ検索成長',
        'xiaohongshu-local-business-search': '小紅書ローカルビジネス検索',
        'xiaohongshu-product-search-ads': '小紅書プロダクト検索広告',
        'xiaohongshu-search-ads-2026': '小紅書検索広告2026',
        'xiaohongshu-search-creative-testing': '小紅書検索クリエイティブテスト',
        'xiaohongshu-search-funnel-2026': '小紅書検索ファネル2026',
        'xiaohongshu-search-koc-strategy': '小紅書KOC検索戦略',
        'xiaohongshu-search-omni-attribution': '小紅書検索オムニアトリビューション',
        'xiaohongshu-search-seo-vs-sem': '小紅書SEO vs SEM',
    },
    'ko': {
        'baidu-ai-search-ads-2026': '바이두 AI 검색 광고: 검색 광고의 새로운 시대',
        'baidu-brand-zone-2026': '바이두 브랜드 존 2026: 검색 결과 페이지를 지배하다',
        'baidu-ecommerce-search-ads-2026': '바이두 이커머스 검색 광고: AI 시대의 경쟁',
        'baidu-local-service-search-ads': '바이두 로컬 서비스 광고: 인근 고객 확보',
        'baidu-search-creative-automation': '바이두 검색 크리에이티브 자동화: AI 기반 광고 제작',
        'baidu-search-keyword-expansion-ai': '바이두 검색의 AI 키워드 확장',
        'baidu-search-offline-to-online': '바이두 검색: 오프라인에서 온라인으로의 연결',
        'baidu-search-privacy-compliance-2026': '바이두 검색 프라이버시 준수: 광고주가 알아야 할 것',
        'baidu-search-quality-score-advanced': '바이두 품질 점수 최적화의 고급 전략',
        'baidu-smart-mini-program-search-ads': '바이두 스마트 미니프로그램 검색 광고',
        'bilibili-brand-search-2026': '빌리빌리 브랜드 검색 2026: Z세대 인지도 지배',
        'bilibili-creator-search-strategy': '빌리빌리 크리에이터 검색 전략',
        'bilibili-ecommerce-search-ads': '빌리빌리 이커머스 검색 광고: Z세대에게 판매',
        'bilibili-gaming-search-ads': '빌리빌리 게임 검색 광고',
        'bilibili-search-ads-2026': '빌리빌리 검색 광고 2026: 완전 가이드',
        'bilibili-search-content-matching': '빌리빌리 검색 콘텐츠 매칭',
        'bilibili-search-creative-lab': '빌리빌리 검색 크리에이티브 랩',
        'bilibili-search-funnel-guide': '빌리빌리 검색 퍼널 가이드',
        'bilibili-search-performance-2026': '빌리빌리 검색 성과 2026',
        'bilibili-youth-search-ads': '빌리빌리 유스 검색 광고',
        'bing-china-b2b-search-2026': '빙 중국 B2B 검색 2026',
        'bing-china-brand-search-2026': '빙 중국 브랜드 검색 2026',
        'bing-china-copilot-search-ads': '빙 중국 코파일럿 검색 광고',
        'bing-china-cross-border-search-ads': '빙 중국 국경 간 검색 광고',
        'bing-china-education-search-ads': '빙 중국 교육 검색 광고',
        'bing-china-local-search-ads': '빙 중국 로컬 검색 광고',
        'bing-china-performance-max-2026': '빙 중국 퍼포먼스 맥스 2026',
        'bing-china-premium-audience-guide': '빙 중국 프리미엄 오디언스 가이드',
        'bing-china-retail-search-ads': '빙 중국 리테일 검색 광고',
        'bing-china-search-creative-guide': '빙 중국 검색 크리에이티브 가이드',
        'bing-china-travel-search-ads': '빙 중국 여행 검색 광고',
        'douyin-brand-search-2026': '더우인 브랜드 검색 2026',
        'douyin-content-search-discovery': '더우인 콘텐츠 검색 디스커버리',
        'douyin-ecommerce-search-2026': '더우인 이커머스 검색 광고 2026',
        'douyin-live-search-conversion': '더우인 라이브 검색 전환',
        'douyin-local-life-search-ads': '더우인 로컬 라이프 검색 광고',
        'douyin-search-ads-ranking-2026': '더우인 검색 광고 랭킹 2026',
        'douyin-search-competitive-analysis': '더우인 검색 경쟁 분석',
        'douyin-search-creative-lab': '더우인 검색 크리에이티브 랩',
        'douyin-search-omni-funnel': '더우인 검색 옴니 퍼널',
        'douyin-sem-vs-search-feed-2026': '더우인 SEM vs 검색 피드 2026',
        'wechat-brand-zone-search-2026': '위챗 브랜드 존 검색 2026',
        'wechat-channels-search-discovery': '위챗 채널 검색 디스커버리',
        'wechat-mini-program-search-ads': '위챗 미니프로그램 검색 광고',
        'wechat-mini-store-search-ads': '위챗 미니스토어 검색 광고',
        'wechat-omni-search-brand-strategy': '위챗 옴니 검색 브랜드 전략',
        'wechat-private-domain-search-retention': '위챗 프라이빗 도메인 검색 리텐션',
        'wechat-search-ads-2026': '위챗 검색 광고 2026',
        'wechat-search-creative-testing': '위챗 검색 크리에이티브 테스팅',
        'wechat-search-funnel-optimization': '위챗 검색 퍼널 최적화',
        'wechat-service-search-conversion': '위챗 서비스 검색 전환',
        'xiaohongshu-brand-zone-search': '샤오홍슈 브랜드 존 검색',
        'xiaohongshu-category-search-growth': '샤오홍슈 카테고리 검색 성장',
        'xiaohongshu-local-business-search': '샤오홍슈 로컬 비즈니스 검색',
        'xiaohongshu-product-search-ads': '샤오홍슈 제품 검색 광고',
        'xiaohongshu-search-ads-2026': '샤오홍슈 검색 광고 2026',
        'xiaohongshu-search-creative-testing': '샤오홍슈 검색 크리에이티브 테스팅',
        'xiaohongshu-search-funnel-2026': '샤오홍슈 검색 퍼널 2026',
        'xiaohongshu-search-koc-strategy': '샤오홍슈 KOC 검색 전략',
        'xiaohongshu-search-omni-attribution': '샤오홍슈 검색 옴니 어트리뷰션',
        'xiaohongshu-search-seo-vs-sem': '샤오홍슈 SEO vs SEM',
    }
}

def fix_hero_title(html_path, lang, translations):
    """Fix English hero title with translated title."""
    content = html_path.read_text(encoding='utf-8')
    slug = html_path.stem
    
    if slug not in translations:
        return False
    
    new_title = translations[slug]
    
    # Find and replace hero title
    # Pattern: article-hero__title">en_title
    title_match = re.search(r'article-hero__title">([^<]+)', content)
    if not title_match:
        return False
    
    en_title = title_match.group(1)
    
    # Skip if already translated
    if re.search(r'[\u4e00-\u9fff\u3040-\u309f\u30a0-\u30ff\uac00-\ud7af]', en_title):
        return False
    
    # Replace
    old_pattern = f'article-hero__title">{en_title}'
    new_pattern = f'article-hero__title">{new_title}'
    
    if old_pattern in content:
        content = content.replace(old_pattern, new_pattern)
        html_path.write_text(content, encoding='utf-8')
        return True
    
    return False

# Process all batch articles
fixed = 0
for lang in ['ja', 'ko']:
    lang_dir = WEBSITE / f'{lang}/blog'
    translations = TITLE_TRANSLATIONS.get(lang, {})
    
    for slug in translations:
        html_path = lang_dir / f'{slug}.html'
        if html_path.exists():
            if fix_hero_title(html_path, lang, translations):
                fixed += 1

print(f"Fixed {fixed} articles")
