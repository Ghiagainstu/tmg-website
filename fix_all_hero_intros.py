#!/usr/bin/env python3
"""Fix hero intros with English mixed in."""
import re
from pathlib import Path

WEBSITE = Path('.')

# Map of file patterns to Japanese hero intros
HERO_INTROS = {
    'bilibili-search-creative-lab': 'Bilibili検索広告のクリエイティブテスト：Z世代に効果のあるもの。主要データ：Z世代のクリエイティブ嗜好；本物 vs 洗練されたクリエイティブ；A/Bテストフレームワーク。',
    'bilibili-search-funnel-guide': 'Bilibiliでブランド認知から購入コンバージョンまでの完全な検索ファネルを構築。主要データ：フルファネル検索戦略；マルチステップアトリビューション；クロスフォーマットファネル最適化。',
    'bilibili-youth-search-ads': 'Bilibili検索で中国の若者にリーチ：トレンド、行動、広告戦略。主要データ：若者の検索行動データ；キャンパス・教育パス・教育広告ターゲティング；検索による若者ブランド構築。',
    'bing-china-brand-search-2026': 'Bing中国でのブランド検索は、Baiduより低い競争率でプレミアム配置を提供。主要データ：Baiduより低いCPC；プレミアム層の人口統計；越境検索クエリ。',
    'bing-china-cross-border-search-ads': 'Bing中国は国際商品を購入する中国消費者の越境ショッピング検索をキャプチャ。主要データ：越境ECクエリ；国際ブランド発見；多言語検索ターゲティング。',
    'bing-china-education-search-ads': 'Bing中国での教育関連検索は、コースや資格を求める学生やプロフェッショナルにリーチ。主要データ：教育検索ボリューム；コース・資格ターゲティング；学生層のリーチ。',
    'bing-china-local-search-ads': 'Bing中国でのローカル検索広告は、近隣のサービスやビジネスを検索するユーザーをターゲット。主要データ：ロケーションベースターゲティング；マップ統合；ローカルビジネス広告フォーマット。',
    'bing-china-retail-search-ads': 'Bing中国での小売検索広告は、商品を検索するショッパーとブランドを接続。主要データ：商品リスティング広告；ショッピングキャンペーンフォーマット；小売特化ターゲティング。',
    'bing-china-search-creative-guide': 'Bing中国検索広告のクリエイティブベストプラクティス：見出し、説明文、拡張機能、レスポンシブ広告。主要データ：レスポンシブ検索広告フォーマット；広告拡張戦略；クリエイティブテスト方法論。',
    'bing-china-travel-search-ads': 'Bing中国での旅行検索広告は、旅行計画、ホテル予約、目的地調査を行うユーザーにリーチ。主要データ：旅行検索意図データ；ホテル・航空券広告フォーマット；季節旅行ターゲティング。',
}

fixed = 0
for slug, new_intro in HERO_INTROS.items():
    # Find files matching the slug
    for lang in ['ja', 'ko']:
        filepath = WEBSITE / f'{lang}/blog/{slug}.html'
        if not filepath.exists():
            continue
        
        content = filepath.read_text(encoding='utf-8')
        
        # Find the hero intro
        pattern = r'article-hero__intro">[^<]*'
        match = re.search(pattern, content)
        if match:
            old_intro = match.group(0)
            # Check if it has English
            if re.search(r'[A-Z][a-z]+ [a-z]+ [a-z]+ [a-z]+', old_intro):
                new_content = content.replace(old_intro, f'article-hero__intro">{new_intro}')
                filepath.write_text(new_content, encoding='utf-8')
                fixed += 1
                print(f'Fixed {lang}/{slug}')

print(f'\nTotal fixed: {fixed}')
