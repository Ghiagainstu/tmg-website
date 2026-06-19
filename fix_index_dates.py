#!/usr/bin/env python3
"""Update dates in index pages."""
import re
from pathlib import Path

WEBSITE = Path('.')

# Date mapping for index pages
DATE_MAP = {
    # 618 Festival articles - June 16, 2026
    '618-2026-ai-takedown-shopping-festival': 'June 16, 2026',
    '618-2026-final-push-ai-everywhere': 'June 16, 2026',
    '618-2026-geo-goes-mainstream': 'June 16, 2026',
    '618-ai-native-era-2026-first-round-report': 'June 16, 2026',
    '618-ai-shopping-search-war-2026': 'June 16, 2026',
    '618-data-review-2026': 'June 16, 2026',
    
    # Q1 2026 earnings - April 2026
    'baidu-q1-2026-ai-revenue': 'April 29, 2026',
    'tencent-ad-revenue-ai-deep-dive-2026': 'April 28, 2026',
    
    # Spring 2026 data - April 2026
    'china-mobile-internet-spring-2026': 'April 30, 2026',
    
    # Alipay Abao launch - June 17, 2026
    'alipay-abao-ai-launch-2026': 'June 17, 2026',
    
    # ByteDance vs Alibaba - June 2026
    'byte-jump-vs-alibaba-content-agent-war': 'June 13, 2026',
    
    # China big tech AI - June 2026
    'china-big-tech-ai-monetization-2026': 'June 17, 2026',
    
    # DeepSeek articles - May-June 2026
    'deepseek-v4-price-cut-geo': 'May 29, 2026',
    'deepseek-image-recognition-geo': 'June 5, 2026',
    
    # Doubao articles - May-June 2026
    'doubao-ads-geo-still-worth-it': 'June 2, 2026',
    'doubao-paid-what-it-means-for-geo': 'May 23, 2026',
    
    # GEO articles - May-June 2026
    'geo-channel-weight-2026': 'June 8, 2026',
    'geo-market-2026-midyear': 'June 11, 2026',
    
    # Tencent articles - May-June 2026
    'tencent-hy-memory': 'June 1, 2026',
    'tencent-ai-pivot-yuanbao-workbuddy': 'June 12, 2026',
    
    # WeChat AI agent - June 2026
    'wechat-ai-agent-coming-for-advertisers': 'June 9, 2026',
    'wechat-ai-ecosystem-opens-to-developers': 'June 11, 2026',
    'wechat-vs-alipay-ai-payment-agent-war': 'June 16, 2026',
    
    # Ocean Engine articles - April 2026
    'ocean-engine-ai-assistant': 'April 23, 2026',
    'ocean-engine-local-reach': 'April 23, 2026',
    'ocean-engine-overview': 'April 23, 2026',
    
    # Pangle ads - April 2026
    'pangle-ads': 'April 23, 2026',
    
    # Pentagon blacklist - May 2026
    'pentagon-blacklists-alibaba-baidu-advertisers': 'May 6, 2026',
    
    # Xiaohongshu 618 guide - June 2026
    'xiaohongshu-618-guide-for-international-brands': 'June 16, 2026',
    
    # Ad billing models - May 2026
    'ad-billing-models-explained': 'May 4, 2026',
    
    # Smart bidding - May 2026
    'smart-bidding-strategies-explained': 'May 4, 2026',
    
    # Attribution models - May 2026
    'attribution-models-guide': 'May 4, 2026',
    
    # CPM articles - May 2026
    'cpm-is-rising-bad': 'May 10, 2026',
    'cpm-ocpm-ecpm-explained': 'May 10, 2026',
    
    # Demographics articles - May 2026
    'baidu-demographics-who-are-these-735m-users': 'May 4, 2026',
    'bilibili-demographics-who-are-these-gen-z-users': 'May 4, 2026',
    'bing-china-demographics-who-are-these-users': 'May 4, 2026',
    'xiaohongshu-demographics-who-are-these-350m-users': 'May 4, 2026',
    'kuaishou-demographics-who-are-these-400m-users': 'May 4, 2026',
    
    # Bilibili GenZ marketing - April 2026
    'bilibili-genz-marketing': 'April 23, 2026',
    
    # Douyin enterprise account - April 2026
    'douyin-enterprise-account': 'April 23, 2026',
    
    # Bing China premium audience - May 2026
    'bing-china-premium-audience-guide': 'May 18, 2026',
    
    # Chinese influencer marketing - May 2026
    'chinese-influencer-marketing': 'May 18, 2026',
    
    # Mass to personal - May 2026
    'mass-to-personal': 'May 18, 2026',
    
    # Search new storefront - May 2026
    'search-new-storefront': 'May 18, 2026',
    
    # Tencent ads home furnishing - May 2026
    'tencent-ads-home-furnishing': 'May 18, 2026',
    
    # Tencent aimplus - May 2026
    'tencent-aimplus': 'May 18, 2026',
    
    # WeChat channels consumer electronics - May 2026
    'wechat-channels-consumer-electronics': 'May 18, 2026',
    
    # WeChat mini games desktop - May 2026
    'wechat-mini-games-desktop': 'May 18, 2026',
    
    # WeChat moments ads - May 2026
    'wechat-moments-ads': 'May 18, 2026',
    
    # Batch platform articles - June 17-18, 2026
    'baidu-advertising-complete-guide-2026': 'June 17, 2026',
    'baidu-ai-search-ads-2026': 'June 18, 2026',
    'baidu-brand-zone-2026': 'June 18, 2026',
    'baidu-ecommerce-search-ads-2026': 'June 18, 2026',
    'baidu-local-service-search-ads': 'June 18, 2026',
    'baidu-search-creative-automation': 'June 18, 2026',
    'baidu-search-keyword-expansion-ai': 'June 18, 2026',
    'baidu-search-offline-to-online': 'June 18, 2026',
    'baidu-search-privacy-compliance-2026': 'June 18, 2026',
    'baidu-search-quality-score-advanced': 'June 18, 2026',
    'baidu-smart-mini-program-search-ads': 'June 18, 2026',
    'bilibili-brand-search-2026': 'June 18, 2026',
    'bilibili-creator-search-strategy': 'June 18, 2026',
    'bilibili-ecommerce-search-ads': 'June 18, 2026',
    'bilibili-gaming-search-ads': 'June 18, 2026',
    'bilibili-search-ads-2026': 'June 18, 2026',
    'bilibili-search-content-matching': 'June 18, 2026',
    'bilibili-search-creative-lab': 'June 18, 2026',
    'bilibili-search-funnel-guide': 'June 18, 2026',
    'bilibili-search-performance-2026': 'June 18, 2026',
    'bilibili-youth-search-ads': 'June 18, 2026',
    'bing-china-b2b-search-2026': 'June 18, 2026',
    'bing-china-brand-search-2026': 'June 18, 2026',
    'bing-china-copilot-search-ads': 'June 18, 2026',
    'bing-china-cross-border-search-ads': 'June 18, 2026',
    'bing-china-education-search-ads': 'June 18, 2026',
    'bing-china-local-search-ads': 'June 18, 2026',
    'bing-china-performance-max-2026': 'June 18, 2026',
    'bing-china-retail-search-ads': 'June 18, 2026',
    'bing-china-search-creative-guide': 'June 18, 2026',
    'bing-china-travel-search-ads': 'June 18, 2026',
    'douyin-advertising-complete-guide-2026': 'June 17, 2026',
    'douyin-brand-search-2026': 'June 17, 2026',
    'douyin-content-search-discovery': 'June 17, 2026',
    'douyin-ecommerce-search-2026': 'June 17, 2026',
    'douyin-live-search-conversion': 'June 17, 2026',
    'douyin-local-life-search-ads': 'June 17, 2026',
    'douyin-search-ads-ranking-2026': 'June 17, 2026',
    'douyin-search-competitive-analysis': 'June 17, 2026',
    'douyin-search-creative-lab': 'June 17, 2026',
    'douyin-search-omni-funnel': 'June 17, 2026',
    'douyin-sem-vs-search-feed-2026': 'June 17, 2026',
    'wechat-advertising-complete-guide-2026': 'June 17, 2026',
    'wechat-brand-zone-search-2026': 'June 17, 2026',
    'wechat-channels-search-discovery': 'June 17, 2026',
    'wechat-mini-program-search-ads': 'June 17, 2026',
    'wechat-mini-store-search-ads': 'June 17, 2026',
    'wechat-omni-search-brand-strategy': 'June 17, 2026',
    'wechat-private-domain-search-retention': 'June 17, 2026',
    'wechat-search-ads-2026': 'June 17, 2026',
    'wechat-search-creative-testing': 'June 17, 2026',
    'wechat-search-funnel-optimization': 'June 17, 2026',
    'wechat-service-search-conversion': 'June 17, 2026',
    'xiaohongshu-advertising-complete-guide-2026': 'June 18, 2026',
    'xiaohongshu-brand-zone-search': 'June 18, 2026',
    'xiaohongshu-category-search-growth': 'June 18, 2026',
    'xiaohongshu-local-business-search': 'June 18, 2026',
    'xiaohongshu-product-search-ads': 'June 18, 2026',
    'xiaohongshu-search-ads-2026': 'June 18, 2026',
    'xiaohongshu-search-creative-testing': 'June 18, 2026',
    'xiaohongshu-search-funnel-2026': 'June 18, 2026',
    'xiaohongshu-search-koc-strategy': 'June 18, 2026',
    'xiaohongshu-search-omni-attribution': 'June 18, 2026',
    'xiaohongshu-search-seo-vs-sem': 'June 18, 2026',
}

# JA date format mapping
JA_DATE_MAP = {
    'April 23, 2026': '2026年4月23日',
    'April 28, 2026': '2026年4月28日',
    'April 29, 2026': '2026年4月29日',
    'April 30, 2026': '2026年4月30日',
    'May 3, 2026': '2026年5月3日',
    'May 4, 2026': '2026年5月4日',
    'May 6, 2026': '2026年5月6日',
    'May 10, 2026': '2026年5月10日',
    'May 18, 2026': '2026年5月18日',
    'May 23, 2026': '2026年5月23日',
    'May 29, 2026': '2026年5月29日',
    'June 1, 2026': '2026年6月1日',
    'June 2, 2026': '2026年6月2日',
    'June 5, 2026': '2026年6月5日',
    'June 8, 2026': '2026年6月8日',
    'June 9, 2026': '2026年6月9日',
    'June 11, 2026': '2026年6月11日',
    'June 12, 2026': '2026年6月12日',
    'June 13, 2026': '2026年6月13日',
    'June 16, 2026': '2026年6月16日',
    'June 17, 2026': '2026年6月17日',
    'June 18, 2026': '2026年6月18日',
}

# KO date format mapping
KO_DATE_MAP = {
    'April 23, 2026': '2026년 4월 23일',
    'April 28, 2026': '2026년 4월 28일',
    'April 29, 2026': '2026년 4월 29일',
    'April 30, 2026': '2026년 4월 30일',
    'May 3, 2026': '2026년 5월 3일',
    'May 4, 2026': '2026년 5월 4일',
    'May 6, 2026': '2026년 5월 6일',
    'May 10, 2026': '2026년 5월 10일',
    'May 18, 2026': '2026년 5월 18일',
    'May 23, 2026': '2026년 5월 23일',
    'May 29, 2026': '2026년 5월 29일',
    'June 1, 2026': '2026년 6월 1일',
    'June 2, 2026': '2026년 6월 2일',
    'June 5, 2026': '2026년 6월 5일',
    'June 8, 2026': '2026년 6월 8일',
    'June 9, 2026': '2026년 6월 9일',
    'June 11, 2026': '2026년 6월 11일',
    'June 12, 2026': '2026년 6월 12일',
    'June 13, 2026': '2026년 6월 13일',
    'June 16, 2026': '2026년 6월 16일',
    'June 17, 2026': '2026년 6월 17일',
    'June 18, 2026': '2026년 6월 18일',
}

def update_index_dates(index_file, date_map):
    """Update dates in index file."""
    content = index_file.read_text(encoding='utf-8')
    fixed = 0
    
    for slug, new_date in date_map.items():
        # Find the card for this slug
        pattern = rf'href="/[^"]*/{slug}/"[^>]*>.*?post-card__date">([^<]+)</span>'
        match = re.search(pattern, content, re.DOTALL)
        if match:
            current_date = match.group(1)
            if current_date != new_date:
                # Replace the date
                old_date_str = f'post-card__date">{current_date}</span>'
                new_date_str = f'post-card__date">{new_date}</span>'
                content = content.replace(old_date_str, new_date_str, 1)
                fixed += 1
    
    if fixed > 0:
        index_file.write_text(content, encoding='utf-8')
    return fixed

# Update EN index
en_fixed = update_index_dates(WEBSITE / 'blog/index.html', DATE_MAP)
print(f'EN index: {en_fixed} dates updated')

# Update JA index
ja_date_map = {slug: JA_DATE_MAP.get(date, date) for slug, date in DATE_MAP.items()}
ja_fixed = update_index_dates(WEBSITE / 'ja/blog/index.html', ja_date_map)
print(f'JA index: {ja_fixed} dates updated')

# Update KO index
ko_date_map = {slug: KO_DATE_MAP.get(date, date) for slug, date in DATE_MAP.items()}
ko_fixed = update_index_dates(WEBSITE / 'ko/blog/index.html', ko_date_map)
print(f'KO index: {ko_fixed} dates updated')

print(f'\nTotal: {en_fixed + ja_fixed + ko_fixed} dates updated')
