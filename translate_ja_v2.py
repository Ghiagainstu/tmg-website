#!/usr/bin/env python3
"""
Batch 2: Translate remaining English in Japanese HTML pages.
Uses BeautifulSoup for safe HTML text node replacement.
"""

import re, os
from bs4 import BeautifulSoup

BASE = os.path.dirname(os.path.abspath(__file__))

# ====== TRANSLATIONS ======

FAQ_T = {
    "Account & Setup": "アカウントと設定",
    "Fees & Budget": "料金と予算",
    "Billing & CPC": "請求とCPC",
    "Compliance & Review": "コンプライアンスと審査",
    "Strategy & Targeting": "戦略とターゲティング",
    "GEO Basics": "GEOの基礎",
    "GEO Pricing & Budget": "GEOの料金と予算",
    "GEO Service & Delivery": "GEOのサービスと納品",
    "GEO vs SEO & Strategy": "GEO vs SEOと戦略",
    "Baidu SEM FAQ": "Baidu SEM FAQ",
    "Xiaohongshu FAQ": "小紅書（RED）FAQ",
    "WeChat Ads FAQ": "WeChat広告FAQ",
    "Douyin / Ocean Engine FAQ": "Douyin / Ocean Engine FAQ",
    "I am getting impressions but no conversions on Xiaohongshu. What is wrong?":
        "インプレッションは得られているが小紅書でコンバージョンがない。何が問題ですか？",
    "Impressions without conversions usually point to an audience mismatch or a landing page problem. Either you are reaching people who are not your real target audience, or the landing page fails to convince them to take action. Review your targeting settings and run an A/B test on your landing page.":
        "インプレッションのみでコンバージョンがない場合、オーディエンスのミスマッチかランディングページの問題が通常の原因です。実際のターゲットオーディエンスにリーチできていないか、ランディングページがアクションを促せていません。ターゲティング設定を見直し、ランディングページのA/Bテストを実施してください。",
    "What gets ads rejected on Xiaohongshu?":
        "小紅書で広告が否認される理由は？",
    "Are there industries that cannot advertise on Xiaohongshu?":
        "小紅書で広告が出せない業種はありますか？",
    "Yes. Financial services (securities, private equity, cryptocurrency, P2P lending), gambling, tobacco, and certain health/medical categories are either fully restricted or heavily regulated on Xiaohongshu.":
        "はい。金融サービス（証券、プライベートエクイティ、暗号通貨、P2Pレンディング）、ギャンブル、タバコ、特定の健康/医療カテゴリは全面的に制限されるか、厳しく規制されています。",
    "Some industries need special approval before they can run ads. Check with us before you plan your campaign — it saves time.":
        "一部の業種は広告配信に特別な承認が必要です。キャンペーン計画の前にお問い合わせください — 時間の節約になります。",
    "What should I know about trademark use in Xiaohongshu ads?":
        "小紅書広告での商標使用について知っておくべきことは？",
    "If the account name references a trademark, you need to prove you own it or have authorization. Own it? A registration certificate, electronic copy, or screenshot of the official trademark database. Authorized by the owner? A signed authorization letter.":
        "アカウント名が商標を参照する場合、所有権または使用許可の証明が必要です。自社保有の場合：登録証明書、電子コピー、公式商標データベースのスクリーンショット。権利者から許可を得ている場合：署名済みの許可証。",
    "My Xiaohongshu ad mentions a website. Do I need an ICP filing?":
        "小紅書広告でウェブサイトに言及する場合、ICP登録は必要ですか？",
    "Yes. If your account name or ad content references a website, Xiaohongshu requires a screenshot of the ICP filing (MIIT) from China's MIIT. One hard rule: the ICP must match the trademark owner's name or the advertiser's company name.":
        "はい。アカウント名や広告コンテンツがウェブサイトを参照する場合、小紅書は中国MIITのICP登録のスクリーンショットを要求します。厳格なルール：ICPは商標所有者名または広告主の会社名と一致する必要があります。",
    "How does Xiaohongshu ad targeting work?":
        "小紅書の広告ターゲティングはどのように機能しますか？",
    "Xiaohongshu offers targeting by demographics (age, gender, location), interests (beauty, fashion, parenting, etc.), device type, and user behavior. You can also target by specific keywords users search for on the platform.":
        "小紅書はデモグラフィック（年齢、性別、地域）、興味関心（美容、ファッション、育児など）、デバイス種別、ユーザー行動によるターゲティングを提供。プラットフォーム上でユーザーが検索する特定キーワードでもターゲティング可能。",
    "Does Xiaohongshu support programmatic buying?":
        "小紅書はプログラマティック購入に対応していますか？",
    "Xiaohongshu primarily uses its own ad platform (Xiaohongshu Ads Manager). It does not offer open programmatic exchange access like Baidu's platform. All campaigns are managed through the platform's native tools, which TMG can handle on your behalf.":
        "小紅書は主に独自の広告プラットフォーム（小紅書広告マネージャー）を使用しています。Baiduのようなオープンなプログラマティックエクスチェンジアクセスは提供していません。すべてのキャンペーンはプラットフォームのネイティブツールを通じて管理され、TMGが代行できます。",
    "Can I run video ads on Xiaohongshu?":
        "小紅書で動画広告は出せますか？",
    "Yes. Xiaohongshu supports video ads in-feed (up to 60 seconds), as well as short video content for brand takeovers. Video performance on the platform is generally strong because users prefer visual, tutorial-style content over static images.":
        "はい。小紅書はインフィード動画広告（最大60秒）やブランドテイクオーバーのショート動画に対応。ユーザーが静止画よりも視覚的でチュートリアル形式のコンテンツを好むため、動画パフォーマンスは一般的に良好です。",
    "How do I measure success on Xiaohongshu?":
        "小紅書での成功をどう測定しますか？",
    "Key metrics include: impressions, clicks, CTR, CPC, engagement rate (likes, comments, saves), follower growth, and search ranking improvements. For conversion campaigns, track CVR, CPA, and ROAS through the platform's pixel tracking.":
        "主要指標：インプレッション、クリック数、CTR、CPC、エンゲージメント率（いいね、コメント、保存）、フォロワー増加数、検索ランキング向上。コンバージョンキャンペーンでは、プラットフォームのピクセルトラッキングを通じてCVR、CPA、ROASを追跡。",
}

GEO_T = {
    "For teams exploring GEO for the first time":
        "GEOを初めて検討するチーム向け",
    "GEO readiness audit across your current content":
        "現在のコンテンツ全体のGEO対応状況監査",
    "Multi-platform citation audit (Douyin, DeepSeek, Kimi, Wenxin)":
        "マルチプラットフォーム引用監査（Douyin、DeepSeek、Kimi、文心一言）",
    "GEO opportunity score by platform":
        "プラットフォーム別GEO機会スコア",
    "30-day roadmap with prioritized recommendations":
        "優先順位付き推奨事項を含む30日間ロードマップ",
    "2-hour strategy call included":
        "2時間の戦略ミーティング付き",
    "For brands ready to enter China AI search at scale":
        "中国AI検索に本格参入する準備ができたブランド向け",
    "30 keywords (prompt phrases) optimized":
        "30キーワード（プロンプトフレーズ）最適化",
    "AI-friendly content creation & distribution":
        "AIフレンドリーなコンテンツ作成と配信",
    "Proprietary brand knowledge base built by our content team":
        "コンテンツチームによる独自ブランドナレッジベース構築",
    "KPI guarantee: ≥50% brand visibility by month 3–6":
        "KPI保証：3〜6ヶ月目までにブランド可視性50%以上",
    "No hidden fees. No platform lock-in. Start with the package that fits your current goals.":
        "隠れた料金なし。プラットフォームロックインなし。現在の目標に合ったパッケージから開始。",
    "Douyin AI content recommendation feeds":
        "Douyin AIコンテンツレコメンドフィード",
    "A/B testing of copy, format, and placement":
        "コピー、フォーマット、配置のA/Bテスト",
}

FARMSKINS_T = {
    "Six-year ongoing partnership": "6年にわたる継続的パートナーシップ",
    "with consistent advertising campaigns across multiple Chinese platforms":
        "複数の中国プラットフォームでの一貫した広告キャンペーン",
    "in the Chinese market despite initial regulatory challenges":
        "当初の規制上の課題を乗り越えての中国市場での成功",
    "of complex platform policies and regulatory requirements":
        "複雑なプラットフォームポリシーと規制要件の克服",
    "on platforms that initially rejected Farmskins' business model":
        "当初Farmskinsのビジネスモデルを拒否したプラットフォームでの成果",
    "Continuous optimization": "継続的最適化",
    "of advertising strategies based on performance data and market feedback":
        "パフォーマンスデータと市場フィードバックに基づく広告戦略の最適化",
    "Most importantly, Farmskins achieved what many international gaming platforms struggle with: establishing a compliant, sustainable presence in China's gaming advertising market.":
        "最も重要なのは、Farmskinsが多くの国際ゲームプラットフォームが苦戦することを達成したことです：中国のゲーム広告市場でコンプライアンスを遵守した持続可能なプレゼンスを確立したことです。",
    "Key Learnings for International Gaming Platforms":
        "国際ゲームプラットフォームへの重要教訓",
    "The Farmskins case demonstrates several critical principles for international gaming companies seeking to enter the Chinese market:":
        "Farmskinsのケースは、中国市場への参入を目指す国際ゲーム企業にとってのいくつかの重要な原則を示しています：",
}

AISEMI_T = {
    "Helping a Global AI and Semiconductor Brand Simplify Multi-Platform Paid Media":
        "グローバルAI・半導体ブランドのマルチプラットフォーム広告運用をシンプルに",
    "One agency, one point of contact, clearer reporting, and a more efficient way to manage complex paid media activity.":
        "1つの代理店、1つの窓口、明確なレポーティング、複雑な広告運用をより効率的に管理。",
    "Global AI & Semiconductor Brand": "グローバルAI＆半導体ブランド",
    "Multi-Platform Management": "マルチプラットフォーム管理",
    "When paid media becomes too fragmented": "広告運用が断片化しすぎた時",
    "For large B2B brands, paid media should support growth — not create operational complexity.":
        "大規模B2Bブランドにとって、広告運用は成長を支援すべきであり、運用の複雑さを生み出すべきではありません。",
    "They needed a more efficient way forward: one agency partner that could manage multiple platforms, provide full visibility across campaigns, and simplify reporting.":
        "彼らはより効率的な方法を必要としていました：複数のプラットフォームを管理し、キャンペーン全体の完全な可視性を提供し、レポーティングを簡素化できる1つの代理店パートナーです。",
    "導入前 working with us, the client faced several common but critical issues:":
        "当社と協業する前、クライアントはいくつかの一般的だが深刻な問題に直面していました：",
    "Too many paid media channels being managed separately":
        "多数の広告チャネルが個別に管理されている",
    "Multiple agency and media contacts to coordinate":
        "調整すべき複数の代理店とメディア窓口",
    "Limited transparency on some platforms, including restricted access to ad accounts":
        "一部プラットフォームでの透明性の低さ（広告アカウントへのアクセス制限を含む）",
    "Concerns around data visibility and reporting accuracy":
        "データの可視性とレポート精度に関する懸念",
    "High service fees spread across multiple partners":
        "複数パートナーに分散する高額なサービス料",
    "Unnecessary time spent on external communication and vendor management":
        "外部コミュニケーションとベンダー管理に費やされる不必要な時間",
    "In short, the client was not only looking for campaign delivery. They were looking for a more transparent, centralised, and efficient operating model.":
        "要するに、クライアントは単なるキャンペーン配信だけでなく、より透明で中央集権的で効率的な運用モデルを求めていました。",
    "They wanted an agency that could:": "彼らは以下のことができる代理店を求めていました：",
    "Provide a single point of contact across multiple paid media platforms":
        "複数の広告プラットフォームにわたる単一窓口の提供",
    "Offer full access to ad accounts and clearer reporting":
        "広告アカウントへの完全アクセスと明確なレポーティング",
    "Manage campaigns across different media channels under one roof":
        "異なるメディアチャネルのキャンペーンを一元管理",
    "Package services in a more competitive and efficient way":
        "より競争力と効率性の高いサービスパッケージ",
    "Support budget planning and platform recommendations based on performance and business needs":
        "パフォーマンスとビジネスニーズに基づく予算計画とプラットフォーム推奨",
    "Why they chose to work with us": "彼らが当社を選んだ理由",
    "We already had experience in search marketing and a strong understanding of the client's business environment, audience, and competitive landscape.":
        "当社は検索マーケティングの経験と、クライアントのビジネス環境、オーディエンス、競合状況に対する深い理解をすでに有していました。",
    "Multi-platform campaign management": "マルチプラットフォームキャンペーン管理",
}

WECHAT_SVC_T = {
    "WeChat reaches across every demographic in China — from Gen Z to senior executives. Here's what we know about the people you can reach:":
        "WeChatは中国のあらゆる層にリーチ — Z世代からシニアエグゼクティブまで。リーチ可能な人々についてのデータをご紹介します：",
    "25-40 (Core professionals)": "25〜40歳（コアプロフェッショナル）",
    "High-income users": "高所得ユーザー",
    "Decision-makers reached": "リーチ可能な意思決定者",
    "WeChat Pay active users": "WeChat Payアクティブユーザー",
    "Mini Program annual transactions": "ミニプログラム年間取引数",
    "University degree holders": "大学学位保有者",
    "content marketing campaigns": "コンテンツマーケティングキャンペーン",
    "Moments & Search Ads": "モーメンツ＆検索広告",
    "Reach users natively in Moments feed, WeChat Search, and the Snap Moment ad format — driven by Tencent's data engine.":
        "モーメンツフィード、WeChat検索、スナップモーメント広告フォーマットでネイティブにユーザーにリーチ — Tencentのデータエンジンによる精准配信。",
    "Moments native advertising": "モーメンツネイティブ広告",
    "WeChat Search brand keywords": "WeChat検索ブランドキーワード",
    "Tencent DMP audience targeting": "Tencent DMPオーディエンスターゲティング",
}

BILIBILI_SVC_T = {
    "Let's talk about how Bilibili fits your China marketing strategy.":
        "Bilibiliがあなたの中国マーケティング戦略にどのように適合するか、ご相談ください。",
}

DOUYIN_SVC_T = {
    "Short Video Marketing Whitepaper · 2023‑2024":
        "ショートビデオマーケティングホワイトペーパー · 2023‑2024",
    "Silver economy purchasing power, Tier 3‑5 market consumption trends, and vertical industry ROI benchmarks.":
        "シルバーエコノミー購買力、Tier 3〜5市場消費動向、垂直産業ROIベンチマーク。",
}

BING_SVC_T = {
    "Bing China's user base is uniquely premium — highly educated, affluent, and research-driven. Here's what makes them different:":
        "Bing Chinaのユーザーベースは特異的にプレミアム — 高学歴、高所得、リサーチ志向。以下がその特長です：",
    "Avg monthly consumption": "平均月間消費額",
    "Research 導入前 Purchase": "購入前のリサーチ",
}

def translate_with_bs4(filepath, translations):
    """Use BeautifulSoup to find and replace English text."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    soup = BeautifulSoup(content, 'html.parser')
    
    # Process body only
    body = soup.find('body')
    if not body:
        return 0
    
    replacements = 0
    
    # Process text nodes in content tags
    for tag_name in ['p', 'li', 'summary', 'span', 'div', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'strong', 'em', 'b', 'i', 'td', 'th', 'blockquote', 'label', 'button', 'small', 'figcaption', 'cite']:
        for elem in body.find_all(tag_name):
            # Check full text content
            text = elem.get_text(strip=True)
            if text and text in translations:
                # Clear all children and set new text
                for child in list(elem.children):
                    child.decompose()
                elem.string = translations[text]
                replacements += 1
                continue
            
            # Also check direct text children (for mixed content)
            for child in list(elem.children):
                if child.name is None:  # text node
                    t = str(child).strip()
                    if t and t in translations:
                        child.replace_with(translations[t])
                        replacements += 1
    
    if replacements > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(str(soup))
    
    return replacements


if __name__ == '__main__':
    print("=" * 50)
    print("TMG 日语页面翻译 V2 (BS4 文本节点替换)")
    print("=" * 50)
    
    tasks = [
        ('ja/faqs/index.html', FAQ_T),
        ('ja/geo/index.html', GEO_T),
        ('ja/services/wechat/index.html', WECHAT_SVC_T),
        ('ja/services/douyin/index.html', DOUYIN_SVC_T),
        ('ja/services/bilibili/index.html', BILIBILI_SVC_T),
        ('ja/services/bing/index.html', BING_SVC_T),
        ('ja/client-stories/farmskins/index.html', FARMSKINS_T),
        ('ja/client-stories/ai-semiconductor/index.html', AISEMI_T),
    ]
    
    total = 0
    for rel_path, translations in tasks:
        fp = os.path.join(BASE, rel_path)
        if not os.path.exists(fp):
            print(f"❌ {rel_path} — 不存在")
            continue
        r = translate_with_bs4(fp, translations)
        total += r
        if r > 0:
            print(f"✅ {rel_path} — {r} 处翻译")
        else:
            print(f"ℹ️ {rel_path} — 无匹配")
    
    print(f"\n总计: {total} 处翻译")
