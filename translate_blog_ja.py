#!/usr/bin/env python3
"""Translate Japanese blog index cards."""
import os

BASE = os.path.dirname(os.path.abspath(__file__))

JP = {
"Expert analysis on China's digital advertising landscape — SEM strategies, platform updates, market insights, and case studies from the TMG team.":
    "中国デジタル広告のエキスパート分析 — SEM戦略、プラットフォームアップデート、市場インサイト、TMGチームによるケーススタディ。",
"Doubao Goes Paid: What This Means for GEO in China":
    "Doubao有料化：中国GEOに与える影響",
"Kuaishou (Kwai) Demographics: Understanding the 400M+ User Base in 2026":
    "Kuaishou(Kwai)の人口統計：2026年の4億+ユーザーベースを理解する",
"Discover Kuaishou's user demographics: 400M+ users, 90M+ CNY shoppers, 64.2% video sharing growth.":
    "Kuaishouのユーザー人口統計：4億+ユーザー、9,000万+人民元ショッパー、64.2%の動画共有成長率。",
"Baidu Search Demographics: Who Are These 735M+ Users?":
    "Baidu検索の人口統計：7億3,500万+ユーザーとは？",
"735M+ MAU, 322M AI search users. Data-driven insights for advertisers targeting China's largest search engine.":
    "7億3,500万+ MAU、3億2,200万AI検索ユーザー。中国最大の検索エンジンをターゲットとする広告主向けのデータドリブンインサイト。",
"Bilibili Demographics: Who Are These Gen Z Users?":
    "Bilibiliの人口統計：Z世代ユーザーとは？",
"Discover Bilibili's unique user demographics: 26yo avg age, 50%+ post-00s, 1:1 gender ratio, 107min daily usage.":
    "Bilibiliのユニークなユーザー人口統計：平均年齢26歳、50%+が00年代生まれ、男女比1:1、1日107分利用。",
"Bing China Demographics: Who Are These High-Value Users?":
    "Bing Chinaの人口統計：高価値ユーザーとは？",
"Discover Bing China's premium user demographics: 75%+ college-educated, high income, urban-focused.":
    "Bing Chinaのプレミアムユーザー人口統計：75%+が大学教育を受け、高収入、都市部に集中。",
"Bing China's Premium Audience: Why Smart Brands Are Advertising Here":
    "Bing Chinaのプレミアムオーディエンス：賢いブランドがここで広告を出す理由",
"Attribution Models in Paid Media: Why Your Campaign Data Might Be Lying to You":
    "有料メディアのアトリビューションモデル：キャンペーンデータが嘘をつく理由",
"Smart Bidding Strategies: From oCPM to tROI":
    "スマート入札戦略：oCPMからtROIまで",
"Ad Billing Models Explained: CPM, CPC, CPA, oCPM and When to Use Each":
    "広告課金モデルの説明：CPM、CPC、CPA、oCPMとそれぞれの使用時期",
"GEO Channel Weight Update 2026: 2 Types Rising, 3 Downgraded by AI":
    "GEOチャネルウェイト更新2026：2タイプ上昇、3タイプがAIによって格下げ",
"CPM, oCPM, eCPM: The Three Metrics Every Paid Media Buyer Gets Wrong":
    "CPM、oCPM、eCPM：すべての有料メディアバイヤーが間違える3つの指標",
"Is a Rising CPM Really That Bad?":
    "CPMの上昇は本当に悪いことなのか？",
"China's Internet Landscape in Spring 2026":
    "2026年春の中国インターネット情勢",
"Meet Zhitu Xing: Ocean Engine's Built-In AI Advertising Assistant":
    "Zhitu Xingの紹介：Ocean Engineに組み込まれたAI広告アシスタント",
"Ocean Engine Local Reach: Douyin's All-in-One Local Marketing Platform":
    "Ocean Engine Local Reach：Douyinのオールインワンローカルマーケティングプラットフォーム",
"Ocean Engine: Douyin's Unified Digital Marketing Platform Explained":
    "Ocean Engine：Douyinの統合デジタルマーケティングプラットフォームの解説",
"Douyin Enterprise Accounts: The Complete Guide for International Brands":
    "Douyin企業アカウント：国際ブランドのための完全ガイド",
"Pangle Ads: ByteDance's Global App Monetization Platform":
    "Pangle広告：ByteDanceのグローバルアプリ収益化プラットフォーム",
"Why Bilibili is China's Most Undervalued Marketing Platform for Gen Z":
    "BilibiliがZ世代にとって中国で最も過小評価されているマーケティングプラットフォームである理由",
"Keyword strategies, bid optimization, and Baidu Quality Score breakdowns.":
    "キーワード戦略、入札最適化、Baidu品質スコアの分析。",
"How to get your brand cited in DeepSeek, Doubao, and Kimi responses.":
    "DeepSeek、Doubao、Kimiの応答でブランドを引用させる方法。",
}

def translate():
    fp = os.path.join(BASE, 'ja/blog/index.html')
    with open(fp, 'r', encoding='utf-8') as f:
        content = f.read()
    
    total = 0
    for eng, jpn in sorted(JP.items(), key=lambda x: -len(x[0])):
        if eng in content:
            content = content.replace(eng, jpn)
            total += 1
    
    with open(fp, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f'Translated {total} items')

if __name__ == '__main__':
    translate()
