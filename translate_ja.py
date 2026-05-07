#!/usr/bin/env python3
"""
Translate remaining English visible text in Japanese HTML pages to Japanese.
Uses simple string replacement to preserve HTML formatting.
"""

import os, re

BASE = os.path.dirname(os.path.abspath(__file__))

# ===== TRANSLATION DICTIONARIES =====

COMMON = {
    "Let's discuss how TMG can help your agency access China's digital advertising market.":
        "TMGがどのように御社の中国デジタル広告市場へのアクセスを支援できるか、ぜひご相談ください。",
    "Your single point of access to China's $100B digital advertising market. We help international agencies navigate Chinese platforms and maximize ROI.":
        "中国の1,000億ドル規模のデジタル広告市場へのシングルアクセスポイント。国際エージェンシーが中国プラットフォームをナビゲートし、ROIを最大化するお手伝いをします。",
    "Your single point of access to China's $100B digital advertising market. We help international agencies navigate Chinese platforms and maximize ROI":
        "中国の1,000億ドル規模のデジタル広告市場へのシングルアクセスポイント。国際エージェンシーが中国プラットフォームをナビゲートし、ROIを最大化するお手伝いをします。",
    "NO. 599 WANZHEN ROAD, SHANGHAI, CHINA":
        "中国上海市嘉定区万镇路599号2F202",
    "© 2026 Tuyue Media Gateway. All rights reserved.":
        "© 2026 Tuyue Media Gateway. 無断転載を禁じます。",
    "Thank you for reaching out to TMG.":
        "TMGにお問い合わせいただきありがとうございます。",
    "We've received your inquiry and will get back to you within":
        "お問い合わせを受け付けました。以下の時間内にご連絡いたします：",
    "Keep an eye on your inbox at the email you provided.":
        "ご登録いただいたメールアドレスの受信トレイをご確認ください。",
    "No matching questions found.":
        "該当する質問が見つかりませんでした。",
    "business hours.":
        "営業時間内。",
    "Baidu, WeChat, Xiaohongshu, Douyin, Bilibili &amp; 中国GEO":
        "Baidu、WeChat、小紅書、Douyin、Bilibili、中国GEO",
    "Most clients see measurable results within 1–2 weeks. Initial citation improvements can appear within days for competitive queries.":
        "ほとんどのクライアントは1〜2週間以内に測定可能な結果を確認できます。競合の少ないクエリでは、数日以内に引用改善が見られる場合があります。",
    "What do I need to provide to get started?":
        "開始するために何を提供する必要がありますか？",
}

BAIDU_FAQ = {
    "What are the common reasons for Baidu ad rejection?":
        "Baidu広告が否認されるよくある理由は？",
    "Common reasons include: non-compliant ad copy (prohibited words, missing disclaimers), non-compliant landing page (broken links, mismatched content), and missing or incorrect industry qualification documents.":
        "よくある理由：不適切な広告文（禁止用語、免責表示の欠落）、不適切なランディングページ（リンク切れ、内容不一致）、業界資格証明書の欠落または誤り。",
    "What are common prohibited words in Baidu ads?":
        "Baidu広告でよくある禁止用語は？",
    "Common prohibited words include absolute claims such as:":
        "よくある禁止用語には以下のような絶対的表現が含まれます：",
    "cheapest, number one in the country, 100% effective, guaranteed results,国家级, 最, 第一, 首个, and similar superlatives. Also prohibited are terms related to medical efficacy (unless you have a medical license), unsubstantiated comparative claims, and content that violates Chinese laws or social norms.":
        "最安値、全国No.1、100%効果的、結果保証、国家级、最、第一、首个などの最上級表現。また、医療効能に関する用語（医療ライセンスがない場合）、根拠のない比較主張、中国の法律や社会規範に違反するコンテンツも禁止されています。",
    "Do healthcare and finance industries have special requirements on Baidu?":
        "医療・金融業界はBaiduで特別な要件がありますか？",
    "Yes. Regulated industries such as healthcare and finance must provide industry-specific licenses, avoid efficacy claims or promises of returns, and comply with strict ad copy review standards. Baidu also restricts certain keywords entirely for these categories.":
        "はい。医療や金融などの規制業界は、業界固有のライセンスを提出し、効能や収益保証を避け、厳格な広告文審査基準に準拠する必要があります。またBaiduはこれらのカテゴリについて特定のキーワードを全面的に制限しています。",
    "Cost-per-click (CPC):":
        "クリック課金（CPC）：",
    "You are charged only when a user clicks your ad. The approximate formula is: your cost per click = (next highest bidder's rank) / (your quality score) + 0.01. Higher quality scores mean lower costs.":
        "ユーザーが広告をクリックした場合のみ課金。おおよその計算式：クリック単価 =（次点入札者のランク）/（自社の品質スコア）+ 0.01。品質スコアが高いほどコストが低くなります。",
    "Baidu's official rule is a minimum top-up of CNY 2,400. However, to save on transaction fees and reduce transfer time, ":
        "Baiduの公式ルールでは最低チャージ額は2,400元です。ただし、振込手数料を節約し入金時間を短縮するため、",
}

XHS_FAQ = {
    "Can foreign companies run ads on Xiaohongshu?":
        "外国企業は小紅書（RED）で広告を出せますか？",
    "Yes, but the process is not as straightforward as Baidu. Xiaohongshu requires a Chinese business license for direct account opening. However, foreign entities can advertise through TMG as a certified agency partner. Companies registered in Hong Kong, Japan, South Korea, or Taiwan can apply with additional documentation. For all other foreign entities, an agency partnership is required.":
        "はい、ただしBaiduほど簡単ではありません。小紅書は直接アカウント開設に中国の営業許可証を必要としますが、外国企業はTMGの認定代理店パートナーを通じて広告出稿が可能です。香港、日本、韓国、台湾の企業は追加書類で申請可能。その他の外国企業は代理店パートナーシップが必要です。",
    "What documents are needed to advertise on Xiaohongshu?":
        "小紅書で広告を出すにはどのような書類が必要ですか？",
    "At minimum, you need a Chinese business license (if registering directly) or a partnership agreement with a certified agency (recommended for foreign entities). Foreign entities need to provide a BR or CR certificate (Hong Kong) or a declaration letter (Japan, South Korea, Taiwan) in lieu of a Chinese business license.":
        "最低限必要なのは、中国の営業許可証（直接登録の場合）または認定代理店とのパートナーシップ契約（外国企業推奨）です。外国企業は中国の営業許可証の代わりに、BR/CR証明書（香港）または宣誓書（日本、韓国、台湾）を提出します。",
    "How long does Xiaohongshu account approval take?":
        "小紅書のアカウント承認にはどのくらい時間がかかりますか？",
    "The review process on Xiaohongshu's professional account takes up to 30 days. The platform charges a one-time review fee of CNY 600 (non-refundable) regardless of approval outcome.":
        "小紅書プロフェッショナルアカウントの審査には最大30日。審査結果に関わらず、600元の一回限りの審査料（返金不可）がかかります。",
    "What are the rules for the Xiaohongshu account name?":
        "小紅書のアカウント名のルールは？",
    "The account name must relate to your registered business name, trademark, or website/app name. It cannot be vague, impersonate others, use sensitive terms, or exceed 12 Chinese characters (24 characters). Special symbols are limited to . · - ( ) — 《 》":
        "アカウント名は登録事業者名、商標、ウェブサイト/アプリ名に関連が必要。曖昧な名称、他者を装うもの、センシティブ用語、12文字（24文字）超えは禁止。使用可能記号は . · - ( ) — 《 》に限られます。",
    "How does Xiaohongshu advertising charge?":
        "小紅書の広告料金体系は？",
    "Two options: CPC (cost per click) and CPM (cost per thousand impressions). You pick the model that fits your goal. CPC minizes costs for traffic, CPM provides maximum visibility for brand awareness.":
        "2つのオプション：CPC（クリック課金）とCPM（インプレッション課金）。目標に合わせて選択。CPCはトラフィック獲得、CPMはブランド認知に最適。",
    "What is the minimum budget to advertise on Xiaohongshu?":
        "小紅書で広告を出す最低予算は？",
    "There is no hard minimum published by the platform, but in practice you need at least a few thousand CNY to test and gather meaningful data. Most campaigns start at around 5,000–10,000 CNY per month.":
        "プラットフォーム公表の最低額はありませんが、実務上は数千元が必要。ほとんどのキャンペーンは月額5,000〜10,000元から開始します。",
    "Are there any fees besides the advertising spend on Xiaohongshu?":
        "小紅書の広告費以外に費用はかかりますか？",
    "Yes. The professional account review fee is CNY 600 (one-time, non-refundable). If you work through an agency, there is typically a service fee (percentage of ad spend or fixed monthly retainer).":
        "はい。プロフェッショナルアカウント審査料600元（一回限り、返金不可）。代理店を通じて運用する場合、通常はサービス料（広告費の%または定額月額）が発生します。",
    "How much does a click cost on Xiaohongshu?":
        "小紅書のクリック単価はいくらですか？",
    "It varies a lot by industry and targeting. Low-competition niches might see CPCs of a few yuan. Competitive categories like beauty and skincare can see CPCs of 10–30+ CNY.":
        "業界やターゲティングによって大きく異なります。競合の少ないニッチでは数元、美容・スキンケアなどの競争の激しいカテゴリでは10〜30元以上。",
    "Why is my Xiaohongshu ad spend not going through?":
        "小紅書の広告費が使われないのはなぜですか？",
    "Three things to check: your bid might be too low (raise it), your targeting might be too narrow (loosen it), or your creative may need to be refreshed (update it). Also check that your account balance is sufficient.":
        "3つの確認ポイント：入札額が低すぎる（上げる）、ターゲティングが狭すぎる（広げる）、クリエイティブの更新が必要（更新する）。アカウント残高もご確認ください。",
    "Companies registered in Hong Kong, Japan, South Korea, or Taiwan can apply with additional documentation. For all other foreign entities, an agency partnership is required.":
        "香港、日本、韓国、台湾に登録されている企業は追加書類で申請できます。その他の外国企業は代理店パートナーシップが必要です。",
}

WECHAT = {
    "Build brand presence in WeChat's content ecosystem. Reach subscribers through articles, updates, and native advertising.":
        "WeChatのコンテンツエコシステムでブランドプレゼンスを構築。記事、アップデート、ネイティブ広告で購読者にリーチ。",
    "In-article ad placements":
        "記事内広告配置",
    "Lightweight apps inside WeChat for e-commerce, lead generation, and customer engagement — no downloads required.":
        "WeChat内の軽量アプリでEC、リード獲得、顧客エンゲージメントを実現 — ダウンロード不要。",
    "In-WeChat app store advertising":
        "WeChatアプリストア内広告",
    "Direct access from 公式アカウント":
        "公式アカウントからの直接アクセス",
    "Key Audience Segments":
        "主要オーディエンスセグメント",
    "Decision-Makers — Senior professionals with high purchasing power":
        "意思決定者 — 高い購買力を持つシニアプロフェッショナル",
    "Digital Natives — Gen Z & Millennials, heavy social & content consumers":
        "デジタルネイティブ — Z世代＆ミレニアル、ソーシャル＆コンテンツのヘビーユーザー",
    "E-Commerce Shoppers — WeChat Pay users, impulse & habitual buyers":
        "ECショッパー — WeChat Payユーザー、衝動的＆習慣的購入者",
    "Senior Professionals — 40-55 age group, B2B decision influencers":
        "シニアプロフェッショナル — 40〜55歳、B2B意思決定への影響力保有者",
    "Why WeChat for Your Brand?":
        "ブランドにWeChatが必要な理由",
    "Unlike transactional platforms, WeChat is a":
        "取引型プラットフォームとは異なり、WeChatは",
    "relationship ecosystem":
        "関係構築エコシステム",
    "Users spend 70+ minutes daily communicating, reading, shopping, and paying — all within one app. This means your brand can build genuine connections rather than competing for attention in a feed.":
        "ユーザーは毎日70分以上をコミュニケーション、読書、ショッピング、決済に — すべて1つのアプリ内で過ごします。ブランドはフィード内で注目を競うのではなく、真の繋がりを構築できます。",
    "No platform switching, no lost attention.":
        "プラットフォーム切り替え不要、注意散漫になりません。",
    "The Demographic Advantage":
        "人口統計的優位性",
    "Why WeChat Is Different":
        "WeChatの特異性",
    "Unlike entertainment platforms, WeChat is where decisions happen — in corporate chat groups, payment approvals, and long-form reading sessions.":
        "エンタメプラットフォームとは異なり、WeChatは意思決定の場 — 企業チャットグループ、支払い承認、長文読書の中で。",
    "The Professional Hub":
        "プロフェッショナルハブ",
    'WeChat is the "LinkedIn of China." 50%+ of Official Account readers hold university degrees — your direct line to C-suite and procurement buyers.':
        'WeChatは「中国版LinkedIn」。公式アカウント読者の50%以上が大学学位保有者 — Cスイートや購買担当者へのダイレクトライン。',
}

DOUYIN = {
    "ユーザーのコンテンツストリームにシームレスに溶け込むネイティブ広告。 Highly engaging and interruptive-free brand storytelling.":
        "ユーザーのコンテンツストリームにシームレスに溶け込むネイティブ広告。エンゲージメントが高く、中断のないブランドストーリーテリング。",
    "In-stream product showcase":
        "インフィードプロダクトショーケース",
    "Build brand awareness at scale with branded hashtag challenges, AR filters, and influencer partnerships through Douyin's discovery-driven content ecosystem.":
        "Douyinの発見駆動型コンテンツエコシステムを通じて、ブランドハッシュタグチャレンジ、ARフィルター、インフルエンサーパートナーシップで大規模ブランド認知を構築。",
    "ARレンズ＆フィルターブランディング for interactive engagement":
        "ARレンズ＆フィルターブランディング — インタラクティブなエンゲージメント",
    "UGC増幅 & user participation campaigns":
        "UGC増幅＆ユーザー参加型キャンペーン",
    "Affluent Millennials (25–40)":
        "富裕層ミレニアル（25〜40歳）",
    "女性 Impulse Shoppers":
        "女性衝動買いショッパー",
    "Live Commerce Enthusiasts":
        "ライブコマース愛好家",
    "Why Douyin for Your Brand?":
        "ブランドにDouyinが必要な理由",
    "Douyin is China's most comprehensive advertising channel —":
        "Douyinは中国で最も包括的な広告チャンネル —",
    "every age, every income tier, every city level":
        "あらゆる年齢、所得層、都市レベル",
    "No other platform matches its combination of reach, engagement depth (125+ min/day), and direct commerce integration that Douyin offers.":
        "Douyinのリーチ、エンゲージメント深度（1日125分+）、ダイレクトコマース統合の組み合わせに匹敵するプラットフォームは他にありません。",
    "Official Platform Report · 2024":
        "公式プラットフォームレポート · 2024",
    "DAU (600M+), daily searches (500M+), interest e-commerce metrics, and brand audience assets (O‑5A model).":
        "DAU（6億+）、1日検索数（5億+）、興味関心EC指標、ブランドオーディエンスアセット（O-5Aモデル）。",
    "China Mobile Internet Report · Q3 2023":
        "中国モバイルインターネットレポート · Q3 2023",
    "Average daily usage time (125+ min), age distribution, city tier penetration, and cross‑app user overlap.":
        "平均利用時間（125分+）、年齢分布、都市ティア浸透率、クロスアプリユーザー重複。",
    "53rd Statistical Report · March 2024":
        "第53次統計報告 · 2024年3月",
    "National short video user scale, online shopping penetration, and overall internet adoption rates.":
        "全国ショートビデオユーザー規模、オンラインショッピング浸透率、インターネット普及率。",
    "Industry-Leading Research":
        "業界最先端リサーチ",
    "Our insights are backed by China's most trusted research institutions and official platform data.":
        "当社のインサイトは中国で最も信頼されている研究機関と公式プラットフォームデータに基づいています。",
    "Data sources: OceanEngine Official Platform Report 2024, QuestMobile China Mobile Internet Report Q3 2023, CNNIC（中国互联网络信息中心）53rd Report.":
        "データソース：OceanEngine公式プラットフォームレポート2024、QuestMobile中国モバイルインターネットレポートQ3 2023、CNNIC（中国互联网络信息中心）第53次報告書。",
    "Douyin reaches across every demographic in China — from Gen Z to affluent millennials, silver economy seniors to impulse buyers.":
        "Douyinは中国のあらゆる層にリーチ — Z世代から富裕層ミレニアル、シルバーエコノミーのシニアから衝動買い層まで。",
    "Tier 1 (Beijing/Shanghai/Guangzhou/Shenzhen)":
        "Tier 1（北京/上海/広州/深圳）",
    "Tier 2 (New First-tier Cities)":
        "Tier 2（新一線都市）",
    "Tier 3–5 (Sinking Market)":
        "Tier 3〜5（下沉市場）",
    "College Degree or Higher":
        "大学学位以上",
    "White‑Collar Professionals":
        "ホワイトカラープロフェッショナル",
}

BILIBILI = {
    "Who Uses Bilibili?":
        "Bilibiliのユーザー層",
    "Gender & Geography":
        "性別と地域",
    "Engagement & Spending":
        "エンゲージメントと消費",
    "80%+ top content over 10min":
        "上位コンテンツの80%以上が10分超",
    "Monthly active (30+ days)":
        "月間アクティブ（30日以上）",
    "Gen Z Power Users — 18-25, heavy daily engagement, 107min+ sessions":
        "Z世代パワーユーザー — 18〜25歳、高いデイリーエンゲージメント、107分以上の利用",
    "Tech-Savvy Early Adopters — first to buy new products and share reviews":
        "テクノロジー精通のアーリーアダプター — 新製品をいち早く購入しレビュー共有",
    "ゲーム & Anime Community — strong in categories like 3C, ACG, and lifestyle":
        "ゲーム＆アニメコミュニティ — 3C、ACG、ライフスタイルカテゴリで強い",
    "Why Bilibili for Your Brand?":
        "ブランドにBilibiliが必要な理由",
    "Bilibili is not about":
        "Bilibiliは",
    "quick impressions":
        "一瞬のインプレッション",
    "community trust, not brand interruption":
        "ブランドの割り込みではなく、コミュニティの信頼",
    "Users follow creators they trust, engage deeply with long-form content, and convert because of":
        "ユーザーは信頼するクリエイターをフォローし、長尺コンテンツに深くエンゲージし、以下の理由でコンバージョンします：",
    "80%+ 12-month retention means your message compounds over time rather than disappearing after one campaign. If your brand targets young, engaged, high-retention audiences, this is the platform.":
        "80%以上の12ヶ月定着率は、メッセージが一度のキャンペーンで消えず、時間とともに蓄積されることを意味します。若く、エンゲージメントが高く、定着率の高いオーディエンスをターゲットにするブランドに最適なプラットフォームです。",
    "The Bilibili Advantage":
        "Bilibiliの優位性",
    "Unlike short-form platforms built on quick hits, Bilibili earns real attention. 人気コンテンツの80%以上が10分超。ユーザーは購読、コメント、シェアを積極的に行います。":
        "短時間のヒットを狙うショートフォームプラットフォームとは異なり、Bilibiliは真の注目を獲得します。人気コンテンツの80%以上が10分超。ユーザーは購読、コメント、シェアを積極的に行います。",
    "Nearly 70% of China's post-90s generation (including Gen Z) is active on Bilibili. If your audience skews young, this is where you need to be.":
        "中国の90年代以降生まれ（Z世代含む）の約70%がBilibiliを利用。オーディエンスが若年層の場合、ここは必須のプラットフォームです。",
    "Post-90s on Bilibili":
        "Bilibili上の90年代以降生まれ",
    "New user average age":
        "新規ユーザー平均年齢",
    "Most platforms lose users fast. Bilibili keeps them. 90%が月30日以上ログイン。84%が毎日アクセス。1年後も80%が定着。":
        "多くのプラットフォームはすぐにユーザーを失いますが、Bilibiliは引き止めます。90%が月30日以上ログイン、84%が毎日アクセス、1年後も80%が定着。",
    "This isn't a platform for 15-second clips. Bilibili's top content is 10+ minutes on average. Users follow creators, debate in comments, and build genuine communities.":
        "15秒クリップのプラットフォームではありません。Bilibiliの上位コンテンツは平均10分以上。ユーザーはクリエイターをフォローし、コメントで議論し、本物のコミュニティを築きます。",
    "Monthly paying users":
        "月間課金ユーザー",
    "Avg interests per user":
        "ユーザーあたり平均関心数",
    "月間3,566万人の課金ユーザー。受動的なスクローラーではなく、クリエイターを直接支援する熱心なファンです。 A platform where users spend money on content they love is a platform where they'll spend money on your brand.":
        "月間3,566万人の課金ユーザー。受動的なスクローラーではなく、クリエイターを直接支援する熱心なファンです。ユーザーが好きなコンテンツにお金を使うプラットフォームは、ブランドにもお金を使ってくれるプラットフォームです。",
}

BING = {
    "Capture high-intent users actively researching your product category on Bing China. Reach the research-oriented audience that makes informed, higher-value purchasing decisions.":
        "Bing Chinaで製品カテゴリを積極的に調査する購買意欲の高いユーザーを獲得。情報に基づいた高額購買決定を行うリサーチ志向のオーディエンスにリーチ。",
    "Reach Bing China's premium audience across the Microsoft Advertisingネットワーク — display banners, in-feed native ads, and co-branded content solutions.":
        "Microsoft Advertisingネットワーク全体でBing Chinaのプレミアムオーディエンスにリーチ — ディスプレイバナー、インフィードネイティブ広告、コラボコンテンツソリューション。",
    "Display Advertising":
        "ディスプレイ広告",
    "Tech-Savvy Professionals — 68% AI interest, early adopters":
        "テクノロジー精通プロフェッショナル — AI関心度68%、アーリーアダプター",
    "White-Collar Urban Workers — Tier 1–3 cities":
        "ホワイトカラー都市労働者 — Tier 1〜3都市",
    "教育-Focused Parents — 72% plan education spending":
        "教育重視の親 — 72%が教育費を計画",
    "Rational Consumers — Research-first, planned spending":
        "合理的消費者 — リサーチ優先、計画的な支出",
    "B2B Decision Makers — Professional, high-authority":
        "B2B意思決定者 — プロフェッショナル、高い権限",
    "Why Bing China Over Baidu?":
        "BaiduでなくBing Chinaを選ぶ理由",
    "Bing China's audience is":
        "Bing Chinaのオーディエンスは",
    "18 percentage points more educated":
        "18%ポイント教育水準が高く",
    "(59% pre-purchase search) and":
        "（59%が購入前にリサーチ）、",
    "(62% willing to interact with ads). Better for brands targeting quality leads in tech, education, finance, and premium retail.":
        "（62%が広告とのインタラクションに積極的）。テクノロジー、教育、金融、プレミアムリテールで質の高いリードをターゲットにするブランドに最適。",
    "Ready to Reach Bing China's Premium Audience?":
        "Bing Chinaのプレミアムオーディエンスにリーチしませんか？",
    "Let's discuss how Bing CN advertising fits into your China search strategy — alongside or as an alternative to Baidu.":
        "Bing中国広告がBaiduと並んで、または代替としてどのように中国検索戦略に適合するか、ご相談ください。",
}

BAIDU_PAGE = {
    "Baidu検索結果に表示されるクリック課金型広告。 Target customers actively searching for your products, services, or brand keywords in Chinese.":
        "Baidu検索結果に表示されるクリック課金型広告。中国語で製品、サービス、ブランドキーワードを検索している顧客をターゲットに。",
    "Reach users across Baidu's network of 800M+ devices through banner ads, native feeds, and programmatic display placements.":
        "Baiduの8億+デバイスネットワーク全体で、バナー広告、ネイティブフィード、プログラマティックディスプレイ配置を通じてユーザーにリーチ。",
    "Baidu Marketing Cloud":
        "Baidu Marketing Cloud",
    "Leverage Baidu's proprietary data engine to run AI-powered campaigns, cross-channel attribution, and advanced audience segmentation.":
        "Baidu独自のデータエンジンを活用して、AI駆動型キャンペーン、クロスチャネルアトリビューション、高度なオーディエンスセグメンテーションを実行。",
    "Key Audience Segments (Baidu Marketing Platform)":
        "主要オーディエンスセグメント（Baidu Marketing Platform）",
    "Knowledge Elite — High education, high income, deep info seekers":
        "知識エリート — 高学歴、高所得、情報探求者",
    "Gen Z — Digital natives born 1995–2009":
        "Z世代 — 1995〜2009年生まれのデジタルネイティブ",
    "Working Professionals — Urban office workers":
        "ワーキングプロフェッショナル — 都市部オフィスワーカー",
    "New Parents — Infant stage family builders":
        "新米親 — 乳児期の家族形成層",
    "Silver Gen — Pre-retirees, stable savings, open to spending":
        "シニア世代 — 退職前、安定貯蓄、消費意欲あり",
    "Students — Online active, early adopters":
        "学生 — オンライン活動的、アーリーアダプター",
    "Fashion Forward — Appearance-conscious, trend-driven":
        "ファッション先進層 — 外見重視、トレンド志向",
    "Newlyweds — Young couples starting families":
        "新婚層 — 家族を始める若いカップル",
    "Outbound travel — Middle-High spenders":
        "海外旅行 — 中高額消費者",
    "Middle-class consumers":
        "中流階級消費者",
    "Complete purchase on Baidu App":
        "Baiduアプリで購入完了",
    "Baidu reaches across every demographic in China — from Gen Z students to senior professionals. Here's what we know about the people you can reach through the platform:":
        "Baiduは中国のあらゆる層にリーチ — Z世代の学生からシニアプロフェッショナルまで。プラットフォームを通じてリーチできる人々についてのデータをご紹介します：",
}

XHS_PAGE = {
    "Native-feeling ads that appear in the user's feed alongside organic content. Perfect for brand awareness, product launches, and seasonal campaigns.":
        "オーガニックコンテンツと並んでユーザーフィードに表示されるネイティブ広告。ブランド認知、商品ローンチ、シーズナルキャンペーンに最適。",
    "小紅書で特定の商品、ブランド、カテゴリーを検索する購買意欲の高いユーザーを獲得。 Appear at the exact moment users are actively researching.":
        "小紅書で特定の商品、ブランド、カテゴリーを検索する購買意欲の高いユーザーを獲得。ユーザーが積極的にリサーチしている瞬間に表示。",
    "Leverage Xiaohongshu's creator ecosystem for authentic brand endorsements. From mega-influencers to niche micro-creators, we connect your brand with the right voices.":
        "小紅書のクリエイターエコシステムを活用した本物のブランドエンドースメント。メガインフルエンサーからニッチなマイクロクリエイターまで、適切な声とのマッチング。",
    "XHS users don't just browse — they":
        "小紅書ユーザーは閲覧するだけではありません —",
    "research": "リサーチ",
    "across three stages: broad exploration (\"how to find a nanny?\"), narrow filtering (\"what requirements to set?\"), and final validation (\"which agency to pick?\").":
        "幅広い探索（「ベビーシッターの見つけ方は？」）、絞り込み（「どんな条件？」）、最終検証（「どの代理店？」）の3段階。",
    "95后 (Post-95 Millennials)":
        "95後（ポスト95ミレニアル）",
    "Usage Engagement":
        "利用エンゲージメント",
    "Daily Use — General Users (120M+)":
        "デイリーユーザー — 一般ユーザー（1.2億+）",
    "Daily Use — Tier 3+ Users (190M+)":
        "デイリーユーザー — Tier 3以上（1.9億+）",
    "Interest communities":
        "インタレストコミュニティ",
    "Top Interest Categories — Monthly Active Reach":
        "トップ関心カテゴリ — 月間アクティブリーチ",
    "Beauty / Cosmetics — 190M+":
        "美容/化粧品 — 1.9億+",
    "Parenting & Maternity — 190M+":
        "育児/マタニティ — 1.9億+",
    "Health Supplements — 190M+":
        "健康サプリメント — 1.9億+",
    "Fitness & Wellness — +276% YoY":
        "フィットネス/ウェルネス — 前年比+276%",
    "Mountain Running — +208%":
        "トレイルランニング — 前年比+208%",
    "A typical purchase decision involves studying":
        "典型的な購買決定では、以下の内容を研究します：",
    ". A typical purchase decision involves studying":
        "典型的な購買決定では、以下の内容を研究します：",
}

PRICING = {
    "広告費の + one-time setup fee":
        "広告費＋初期設定料",
    "Setup Fee: 〜 $100+ (one-time)":
        "設定料：約$100+（一回限り）",
    "お問い合わせ us for platform-specific pricing":
        "各プラットフォームの料金についてはお問い合わせください",
}

HOMEPAGE = {
    "AI-assisted optimization to cut wasted spend":
        "AI支援最適化で無駄な支出を削減",
    "Annual account authentication fee of CNY 600":
        "年間アカウント認証料600元",
    ". For new users, this fee is refunded to your ad account after the first year, making it free for year one.":
        "新規ユーザーの場合、この料金は1年後に広告アカウントに返金され、初年度は実質無料。",
    "Baidu's official minimum is":
        "Baiduの公式最低入金額は",
    ". To save on transaction fees and reduce transfer time, we recommend":
        "振込手数料節約と入金時間短縮のため、以下をお勧めします：",
    "Baidu only supports pre-payment.":
        "Baiduは事前支払いのみ対応。",
    "You must have sufficient account balance before your ads can run. No credit or post-payment options are available for standard accounts.":
        "広告配信前に十分なアカウント残高が必要。標準アカウントではクレジットや後払いオプションは利用不可。",
    "Can foreign companies advertise on 小紅書（RED）?":
        "外国企業は小紅書（RED）で広告を出せますか？",
    "Does Baidu support post-payment?":
        "Baiduは後払いに対応していますか？",
    "Can I open a Baidu account without a Chinese domestic company?":
        "中国国内企業なしでBaiduアカウントを開設できますか？",
    "Baidu supports account opening for foreign companies and entities. You don't need a Chinese domestic business license to get started.":
        "Baiduは外国企業や法人のアカウント開設をサポートしています。開始に中国国内の営業許可証は必要ありません。",
    "Are there fees besides the advertising budget?":
        "広告予算以外に費用はかかりますか？",
}

GEO = {
    "Get Your Brand Cited in DeepSeek, Douyin & Beyond":
        "DeepSeek、Douyinなどでブランドを引用されるように",
    "While the West debates AI search, China's already living in it. 1 billion users, 47% of all search behavior migrated to AI-native platforms.":
        "西洋がAI検索を議論する間、中国はすでにAI検索を日常的に使用。10億ユーザー、全検索行動の47%がAIネイティブプラットフォームに移行。",
    "従来のSEO gets you found. GEO gets you cited inside AI answers — before the user ever clicks a link.":
        "従来のSEOは「見つけられる」ためのもの。GEOはユーザーがリンクをクリックする前に、AI回答内で引用されるためのもの。",
    "GEO（Generative Engine Optimization）":
        "GEO（生成エンジン最適化）",
    "Google, Baidu, Bing":
        "Google、Baidu、Bing",
    "DeepSeek, Douyin AI, Kimi, Wenxin, ChatGPT-CN":
        "DeepSeek、Douyin AI、Kimi、文心一言、ChatGPT-CN",
    "Baidu still matters, but declining":
        "Baiduはまだ重要だが減少傾向",
    "China's AI search is fragmented — and that's the opportunity":
        "中国のAI検索は断片化している — それがチャンス",
    "No single AI platform dominates. Each has its own user base, strengths, and citation logic. You need a multi-platform strategy.":
        "単一のAIプラットフォームが支配しているわけではありません。各プラットフォームに独自のユーザーベース、強み、引用ロジックがあります。マルチプラットフォーム戦略が必要です。",
    "Data: QuestMobile, November 2025. China's total AI assistant user base crossed 1 billion in November 2025.":
        "データ：QuestMobile、2025年11月。中国のAIアシスタント総ユーザー数は2025年11月に10億人を突破。",
    "Source figures are estimates based on publicly reported data.":
        "ソース数値は公開データに基づく推定値。",
    "Multi-platform ad spend management across China's top AI channels. We handle account setup, recharge, campaign optimization, and cross-platform reporting.":
        "中国の主要AIチャネル全体でのマルチプラットフォーム広告費管理。アカウント設定、チャージ、キャンペーン最適化、クロスプラットフォームレポートを対応。",
    "Douyin AI (Doubao) ad campaigns":
        "Douyin AI（豆包）広告キャンペーン",
    "DeepSeek native advertising":
        "DeepSeekネイティブ広告",
    "Kimi brand zones and content partnerships":
        "Kimiブランドゾーンとコンテンツパートナーシップ",
    "Wenxin (Baidu AI) ad products":
        "文心一言（Baidu AI）広告プロダクト",
    "Multi-currency billing, transparent rates":
        "多通貨請求、透明な料金",
    "GEO Content Strategy":
        "GEOコンテンツ戦略",
    "AI citation is earned through structured, authoritative content. We audit your existing materials and rebuild them for AI discoverability.":
        "AI引用は構造化された権威あるコンテンツを通じて獲得。既存素材を監査し、AI発見可能性を高めるために再構築。",
    "Structured data optimization (FAQ, HowTo, Article schema)":
        "構造化データ最適化（FAQ、HowTo、Articleスキーマ）",
    "Brand citation signal building":
        "ブランド引用シグナル構築",
    "Cross-platform content adaptation (Chinese + English)":
        "クロスプラットフォームコンテンツ適応（中国語＋英語）",
    "Entity clarity and knowledge graph optimization":
        "エンティティ明確化とナレッジグラフ最適化",
    "Citation monitoring and rank tracking":
        "引用モニタリングとランク追跡",
    "AI Search Advertising":
        "AI検索広告",
    "When organic GEO isn't fast enough, paid AI search placements get you in front of the right audience immediately.":
        "オーガニックGEOだけでは不十分な場合、有料AI検索広告で即座に適切なオーディエンスの前に。",
    "AI answer context ads (in-chat placements)":
        "AI回答コンテキスト広告（チャット内配置）",
    "Kimi brand search integrations":
        "Kimiブランド検索連携",
    "We built our SEM expertise across Baidu and Chinese platforms — now we're bringing the same playbook to AI search.":
        "当社はBaiduや中国プラットフォームでSEMの専門知識を構築してきました — 今、同じプレイブックをAI検索に適用しています。",
}

CLIENT_STORIES = {
    "How a Global CS:GO Platform Found Its Footing in China":
        "世界的CS:GOプラットフォームが中国で足場を築いた方法",
    "Overcoming platform rejections in China's regulated gaming advertising market to achieve sustained growth across multiple Chinese platforms — a six-year partnership case study.":
        "中国の規制ゲーム広告市場でプラットフォーム拒否を克服し、複数の中国プラットフォームで持続的成長を達成 — 6年のパートナーシップケーススタディ。",
    "Turning platform rejections into a six-year partnership with ongoing campaigns across multiple Chinese platforms, achieving sustained growth in a once-closed market.":
        "プラットフォーム拒否を6年のパートナーシップに転換、複数の中国プラットフォームでキャンペーン継続。かつて閉ざされた市場で持続的成長を達成。",
    "導入前の課題: Breaking into China's Regulated Gaming Market":
        "導入前の課題：中国の規制ゲーム市場への参入",
    "Farmskins, a leading global CS:GO skin trading platform, faced a formidable challenge when attempting to enter the Chinese market.":
        "世界的なCS:GOスキン取引プラットフォームFarmskinsは、中国市場への参入時に大きな課題に直面しました。",
    "The platform's unique value proposition of skin trading and marketplace operations fell into regulatory gray areas that made platform compliance approvals difficult.":
        "スキン取引とマーケットプレイス運営という独自の価値提案は、規制のグレーゾーンに該当し、プラットフォームのコンプライアンス承認が困難でした。",
    "Why Platform Rejections Were Not the End of the Story":
        "プラットフォーム拒否が終わりではなかった理由",
    "Many international gaming companies would have viewed these rejections as insurmountable barriers. However, we recognized that each rejection was an opportunity to refine our approach and find compliant pathways.":
        "多くの国際ゲーム企業はこれらの拒否を乗り越えられない障壁と見なしたでしょう。しかし当社は、各拒否をアプローチを洗練し、コンプライアンス経路を見つける機会と捉えました。",
    "The key issues we needed to address included:":
        "対処すべき主要な課題は以下の通りです：",
    "Platform-specific content and advertising policies for gaming-related services":
        "ゲーム関連サービスのプラットフォーム別コンテンツ・広告ポリシー",
    "Regulatory compliance requirements for virtual item trading platforms":
        "仮想アイテム取引プラットフォームの規制コンプライアンス要件",
    "Cultural and linguistic adaptation of marketing materials":
        "マーケティング素材の文化的・言語的適応",
    "Building trust with platform representatives through transparent communication":
        "透明なコミュニケーションを通じたプラットフォーム担当者との信頼構築",
    "Developing compliant advertising strategies that respected local regulations":
        "現地規制を尊重したコンプライアンス広告戦略の開発",
    "Our Strategic Approach":
        "戦略的アプローチ",
    "Rather than taking a standardized approach, we developed a platform-by-platform strategy that respected each channel's unique requirements.":
        "標準化されたアプローチではなく、各チャネルの独自要件を尊重したプラットフォーム別戦略を開発しました。",
    "1. Platform-Specific Compliance Mapping":
        "1. プラットフォーム別コンプライアンスマッピング",
    "We conducted thorough research into each platform's advertising policies, identifying specific requirements and potential compliance pathways.":
        "各プラットフォームの広告ポリシーを徹底調査し、具体的な要件とコンプライアンス経路を特定。",
    "2. Content Adaptation and Localization":
        "2. コンテンツ適応とローカライゼーション",
    "We worked closely with Farmskins to adapt their messaging, ensuring it complied with local regulations while effectively communicating the brand's value proposition.":
        "Farmskinsと緊密に連携し、現地規制に準拠しながらブランドの価値提案を効果的に伝えるメッセージに適応。",
    "3. Direct Platform Engagement":
        "3. プラットフォームとの直接交渉",
    "We established direct relationships with platform representatives, presenting Farmskins' business model transparently and negotiating compliant advertising arrangements.":
        "プラットフォーム担当者と直接関係を構築し、Farmskinsのビジネスモデルを透明に提示、コンプライアンス広告契約を交渉。",
    "4. Phased Market Entry Strategy":
        "4. 段階的市场参入戦略",
    "We implemented a gradual approach, starting with more accessible channels and expanding to more restrictive platforms as compliance was established.":
        "アクセスしやすいチャネルから開始し、コンプライアンスが確立された段階でより制限の厳しいプラットフォームへ拡大。",
    "5. Ongoing Compliance Monitoring":
        "5. 継続的コンプライアンスモニタリング",
    "We established systems for continuous monitoring of regulatory changes and platform policy updates, ensuring long-term compliance.":
        "規制変更とプラットフォームポリシー更新の継続的モニタリング体制を構築し、長期的なコンプライアンスを確保。",
    "The Outcome: Six-Year Partnership and Sustained Growth":
        "結果：6年にわたるパートナーシップと持続的成長",
    "Through persistent, strategic engagement and a deep understanding of China's digital advertising landscape, we transformed what started as a series of rejections into a long-term, successful partnership.":
        "粘り強い戦略的エンゲージメントと中国デジタル広告市場への深い理解を通じて、一連の拒否から長期的で成功したパートナーシップへと変革。",
    "The results speak for themselves:":
        "結果は雄弁です：",
}


# File → translation mapping
FILES = [
    ('ja/index.html', {**HOMEPAGE, **COMMON}),
    ('ja/faqs/index.html', {**BAIDU_FAQ, **XHS_FAQ, **COMMON}),
    ('ja/geo/index.html', {**GEO, **COMMON}),
    ('ja/services/baidu/index.html', {**BAIDU_PAGE, **COMMON}),
    ('ja/services/wechat/index.html', {**WECHAT, **COMMON}),
    ('ja/services/douyin/index.html', {**DOUYIN, **COMMON}),
    ('ja/services/bilibili/index.html', {**BILIBILI, **COMMON}),
    ('ja/services/bing/index.html', {**BING, **COMMON}),
    ('ja/services/xiaohongshu/index.html', {**XHS_PAGE, **COMMON}),
    ('ja/services/index.html', {**COMMON}),
    ('ja/about/index.html', {**COMMON}),
    ('ja/why-tmg/index.html', {**COMMON}),
    ('ja/pricing/index.html', {**PRICING, **COMMON}),
    ('ja/contact/index.html', {**COMMON}),
    ('ja/client-stories/index.html', {**CLIENT_STORIES, **COMMON}),
    ('ja/client-stories/farmskins/index.html', {**CLIENT_STORIES, **COMMON}),
    ('ja/client-stories/ai-semiconductor/index.html', {**COMMON}),
    ('ja/blog/index.html', {**COMMON}),
]


def translate_file(filepath, translations):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    replacements = 0
    for eng, jp in sorted(translations.items(), key=lambda x: -len(x[0])):
        # Replace using exact string match (longest first to avoid partial matches)
        if eng in content:
            content = content.replace(eng, jp)
            replacements += 1
    
    if replacements > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    
    return replacements


if __name__ == '__main__':
    print("=" * 50)
    print("TMG 日语页面批量翻译")
    print("=" * 50)
    
    total = 0
    for rel_path, translations in FILES:
        fp = os.path.join(BASE, rel_path)
        if not os.path.exists(fp):
            print(f"❌ {rel_path} — 不存在")
            continue
        r = translate_file(fp, translations)
        total += r
        if r > 0:
            print(f"✅ {rel_path} — {r} 处替换")
        else:
            print(f"ℹ️ {rel_path} — 无匹配")
    
    print(f"\n总计: {total} 处翻译")
