#!/usr/bin/env python3
"""Fix callout labels and content in KO articles."""
import re
from pathlib import Path

WEBSITE = Path('.')

# Map of English callout content to Korean translations
CALLOUT_TRANSLATIONS = {
    'Search ranking algorithm factors in video completion rate, shares, comment sentiment. Optimizing these signals improves ad placement.':
        '검색 랭킹 알고리즘은 동영상 완료율, 공유, 댓글 감정을 고려합니다. 이러한 시그널을 최적화하면 광고 배치가 향상됩니다.',
    'Competitive analysis reveals winning content formats and ad creatives in your category. Use this intelligence to inform strategy.':
        '경쟁 분석은 카테고리에서 성공하는 콘텐츠 포맷과 광고 크리에이티브를揭示합니다. 이 인텔리전스를 전략 수립에 활용하세요.',
    'Omni-funnel strategy connects awareness videos, search ads, live commerce into single conversion path. Reduces CPA by 30-40%.':
        '옴니퍼널 전략은 인식 동영상, 검색 광고, 라이브 커머스를 단일 전환 경로로 연결합니다. CPA를 30-40% 절감합니다.',
    'Omni-search brand strategy ensures consistent presence across search, moments, channels. Integrated approach builds trust and recall.':
        '옴니검색 브랜드 전략은 검색, 모먼츠, 채널 전반에 걸쳐 일관된 존재감을 보장합니다. 통합 접근 방식은 신뢰와 회상을 구축합니다.',
    'Private domain search retention converts 5-8x better than cold traffic. Searchable mini-program or service account is foundation.':
        '프라이빗 도메인 검색 리텐션은 콜드 트래픽보다 5-8배 더 잘 전환됩니다. 검색 가능한 미니프로그램 또는 서비스 계정이 기반입니다.',
    'Creative testing on WeChat requires different approach. Social proof elements in ad creatives improve CTR by 20-30%.':
        '위챗에서의 크리에이티브 테스트는 다른 접근 방식이 필요합니다. 광고 크리에이티브의 소셜 프루프 요소는 CTR을 20-30% 향상시킵니다.',
    'Creative testing requires authentic user-generated aesthetic. Ads that look like native notes see 4x higher engagement.':
        '크리에이티브 테스트는 진정한 사용자 생성 미학이 필요합니다. 네이티브 노트처럼 보이는 광고는 4배 높은 참여도를 보입니다.',
    'KOC content generates 5x more organic reach than brand-produced content. Authentic voices drive real purchasing decisions.':
        'KOC 콘텐츠는 브랜드 제작 콘텐츠보다 5배 더 많은 오가닉 리치를 생성합니다. 진정한 목소리는 실제 구매 결정을推动합니다.',
    'Omni-attribution reveals true impact of content across discovery, search, conversion. Data-driven approach optimizes budget allocation.':
        '옴니어트리뷰션은 발견, 검색, 전환 전반에 걸친 콘텐츠의 진정한 영향을揭示합니다. 데이터 기반 접근 방식은 예산 배분을 최적화합니다.',
}

def fix_file(filepath):
    content = filepath.read_text(encoding='utf-8')
    
    # Fix Japanese label to Korean
    content = content.replace('callout__label">プロのヒント', 'callout__label">전문가 팁')
    
    # Fix English content to Korean
    for en, ko in CALLOUT_TRANSLATIONS.items():
        content = content.replace(f'<p>{en}</p>', f'<p>{ko}</p>')
    
    filepath.write_text(content, encoding='utf-8')
    return True

fixed = 0
for filepath in WEBSITE.glob('ko/blog/*.html'):
    if fix_file(filepath):
        fixed += 1

print(f'Fixed {fixed} files')
