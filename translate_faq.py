#!/usr/bin/env python3
"""
Translate remaining FAQ English text. Uses exact HTML string replacement.
"""

import os, re

BASE = os.path.dirname(os.path.abspath(__file__))

D = {
# === WeChat FAQ ===
"Yes. Foreign companies can run ads on WeChat through a certified agency partner. WeChat requires a Chinese business license for direct account registration, but TMG can facilitate the process as an authorized reseller.":
"はい。外国企業は認定代理店パートナーを通じてWeChatで広告を出稿できます。WeChatは直接登録に中国の営業許可証が必要ですが、TMGが公認リセラーとして手続きを代行できます。",
"At minimum, you need a Chinese business license or a partnership with a certified WeChat advertising agency. Depending on your industry and ad content, you may also need:":
"最低限、中国の営業許可証または認定WeChat広告代理店とのパートナーシップが必要です。業界や広告内容によっては以下も必要です：",
"Foreign entities typically need a BR or CR certificate (Hong Kong companies) or equivalent documentation from their country of registration.":
"外国企業は通常、BR/CR証明書（香港企業）または登録国の同等の書類が必要です。",
"WeChat offers four pricing models. Choose based on your campaign goal:":
"WeChatは4つの料金モデルを提供。キャンペーン目標に基づいて選択：",
"— Pay per 1,000 impressions. Works best for brand awareness campaigns where reach matters more than clicks.":
"— 1,000インプレッションごとに課金。リーチがクリックより重要なブランド認知キャンペーンに最適。",
"— Pay only when someone clicks your ad. Better for driving traffic to your landing page, mini program, or app.":
"— クリックされた場合のみ課金。ランディングページ、ミニプログラム、アプリへのトラフィック誘導に最適。",
"— Used for influencer content (mutual selection ads). You pay a fixed fee per published article.":
"— インフルエンサーコンテンツ（相互選択広告）に使用。公開記事ごとに固定料金。",
"— Pay only when a sale is made. You set the commission percentage and pay out of actual revenue generated.":
"— 販売が成立した場合のみ課金。コミッション率を設定し、実際の売上から支払い。",
"Most advertisers start with CPM or CPC. The right choice depends on your campaign objective — we can help you decide.":
"ほとんどの広告主はCPMまたはCPCから開始します。適切な選択はキャンペーン目標によって異なります — 当社が決定をサポートします。",
"oCPC stands for Optimized Cost Per Click. It is an intelligent bidding mode where WeChat optimizes toward your defined conversion goal rather than just clicks.":
"oCPCは最適化クリック単価の略。クリック数だけでなく、設定したコンバージョン目標に向けてWeChatが最適化するインテリジェント入札モード。",
"With regular CPC, you pay for each click regardless of what happens after. With oCPC, you define a conversion action (like a purchase or form submission) and the system optimizes delivery toward users most likely to complete that action.":
"通常のCPCではクリックごとに課金され、その後の行動は問いません。oCPCではコンバージョンアクション（購入やフォーム送信など）を定義し、システムはそのアクションを完了する可能性が最も高いユーザーに向けて配信を最適化します。",
"Use oCPC when you want to focus on results, not just traffic. The catch: you need enough conversion data (typically 20+ conversions per week) for the algorithm to optimize effectively.":
"結果に焦点を当てたい場合にoCPCを使用。注意点：アルゴリズムが効果的に最適化するには、十分なコンバージョンデータ（通常週20件以上）が必要です。",
"How does WeChat recharge and deduct advertising fees?":
"WeChatの広告費のチャージと引き落とし方法は？",
"WeChat Ads runs on a pre-paid model. You deposit funds into your ad account before your ads go live.":
"WeChat広告はプリペイドモデル。広告配信前に広告アカウントに資金を入金します。",
"Recharge is done through the Tencent Ads platform (ads.e.qq.com) or through your agency partner. Minimum recharge amount varies but is typically around CNY 5,000 for new accounts.":
"チャージはTencent Adsプラットフォーム（ads.e.qq.com）または代理店パートナーを通じて行います。最低チャージ額は異なりますが、新規アカウントでは通常約5,000元。",
"Fees are deducted based on your chosen billing model (CPM, CPC, oCPC, etc.) and are calculated in real time. You can view your daily spend and remaining balance in the Tencent Ads dashboard.":
"料金は選択した課金モデル（CPM、CPC、oCPCなど）に基づいてリアルタイムで差し引かれます。Tencent Adsダッシュボードで日々の支出と残高を確認できます。",
"For foreign companies, working through a certified agency is usually the smoother option — the agency handles recharge, compliance, and billing on your behalf.":
"外国企業の場合、認定代理店を通じた運用が通常スムーズです — 代理店がチャージ、コンプライアンス、請求を代行します。",
"What is the minimum budget to advertise on WeChat?":
"WeChatで広告を出す最低予算は？",
"There is no official minimum budget published by WeChat, but in practice you need at least CNY 5,000 to 10,000 per month for meaningful testing.":
"WeChatが公表している公式の最低予算はありませんが、実務上は有意義なテストのために月額5,000〜10,000元程度が必要です。",
"WeChat ads work well for brands that want to build awareness within specific Moments feed placements, drive traffic to mini programs, or retarget users who have interacted with their brand.":
"WeChat広告は、特定のモーメンツフィード内で認知を構築したいブランド、ミニプログラムへのトラフィックを促進したい場合、ブランドと交流したユーザーをリターゲットしたい場合に効果的です。",
"What is the difference between auction ads and contract ads?":
"オークション広告と契約広告の違いは？",
"— Compete in real time with other advertisers. Higher bid plus better ad quality wins the slot. You set your budget and bid.":
"— 他の広告主とリアルタイムで競争。高い入札額＋優れた広告品質が枠を獲得。予算と入札額を設定。",
"— Negotiate a fixed price with the platform upfront for guaranteed placement. You get a fixed position for a fixed period.":
"— プラットフォームと事前に固定価格を交渉し、掲載を保証。一定期間、固定ポジションを確保。",
"Auction ads are simpler and more flexible. Contract ads are for when you need certainty. Most TMG clients start with auction and add contract for key campaigns.":
"オークション広告はよりシンプルで柔軟。契約広告は確実性が必要な場合に。ほとんどのTMGクライアントはオークションから開始し、主要キャンペーンには契約広告を追加。",
"Think of it as \"what you are paying for\":":
"「何に対して支払うか」と考えてください：",
"— Cost Per Mille. You pay per 1,000 impressions. 1,000 people see your ad, you get charged once.":
"— Cost Per Mille（CPM）。1,000インプレッションごとに課金。1,000人に広告が表示されたら1回課金。",
"— Cost Per Click. You pay only when someone clicks. No click, no charge.":
"— Cost Per Click（CPC）。クリックされた場合のみ課金。クリックなし、課金なし。",
"— Cost Per Action. You pay when someone completes a specific action, like downloading your app or signing up.":
"— Cost Per Action（CPA）。アプリのダウンロードやサインアップなど、特定のアクションが完了した場合に課金。",
"— Cost Per Time. You pay a fixed fee for a time slot, such as CNY 10,000 for one day. Common for reserved placements.":
"— Cost Per Time（CPT）。時間枠に対して固定料金を支払う（例：1日10,000元）。予約型配置に一般的。",
"— The smart versions. The system optimizes delivery toward users most likely to convert, which means you may pay more per event but get better overall ROAS.":
"— スマートバージョン。システムが最もコンバージョンしやすいユーザーに向けて配信を最適化。イベント単価は高くなる可能性があるが、全体的なROASは向上。",
"Different ad placements and campaign goals call for different billing models. You pick based on what aligns with your objective.":
"広告配置とキャンペーン目標によって適切な課金モデルは異なります。目標に合わせて選択してください。",
"Two factors determine whether your ad gets shown: your bid and your ad quality score.":
"広告が表示されるかどうかを決定する2つの要素：入札額と広告品質スコア。",
"— What you are willing to pay per action (click, impression, or conversion). You set this when creating your campaign.":
"— アクション（クリック、インプレッション、コンバージョン）ごとに支払う意思のある金額。キャンペーン作成時に設定。",
"— Calculated from relevance, click-through rate, and landing page experience. Higher quality ads can win auctions even with lower bids.":
"— 関連性、クリック率、ランディングページエクスペリエンスから計算。高品質な広告は低い入札額でもオークションに勝利可能。",
"It is not just about how much you spend. A well-crafted ad with strong relevance can outperform a competitor spending more.":
"支出額だけではありません。関連性の高いよく練られた広告は、より多く使っている競合を上回ることができます。",
"How does WeChat handle malicious clicks?":
"WeChatは不正クリックにどう対応していますか？",
"WeChat runs real-time monitoring for suspicious click activity. If the same user clicks your ad multiple times in a short period, the system automatically filters those clicks and does not charge you.":
"WeChatは不審なクリック活動をリアルタイムで監視。同じユーザーが短期間に広告を複数回クリックした場合、システムが自動的にフィルタリングし、課金しません。",
"The platform automatically flags patterns like rapid repeated clicks, automated bots, or other suspicious behavior by default.":
"プラットフォームはデフォルトで、高速な繰り返しクリック、自動化ボット、その他不審な行動パターンを自動的にフラグ付けします。",
"If you notice unusual activity in your dashboard, you can report it. Their team reviews reported cases and credits invalid clicks back to your account.":
"ダッシュボードで異常なアクティビティに気づいた場合は報告可能。チームが報告されたケースを審査し、無効なクリックをアカウントに返金します。",
"There is no fixed CPC — it varies by industry, targeting, and ad placement. WeChat Moments ads tend to have higher CPCs than in-article placements.":
"固定CPCはありません — 業界、ターゲティング、広告配置によって異なります。WeChatモーメンツ広告は記事内配置よりもCPCが高くなる傾向があります。",
"Low-competition niches might see CPCs of a few yuan. Competitive categories like beauty, fashion, or finance can see CPCs of 10–30+ CNY.":
"競合の少ないニッチでは数元のCPC。美容、ファッション、金融などの競争の激しいカテゴリでは10〜30元以上。",
"Tencent Ads is not just WeChat. It is an ecosystem that spans multiple platforms:":
"Tencent AdsはWeChatだけではありません。複数のプラットフォームにまたがるエコシステムです：",
"— The feed ads that appear between organic posts in WeChat. High engagement, strong brand presence.":
"— WeChatのオーガニック投稿の間に表示されるフィード広告。高いエンゲージメント、強力なブランドプレゼンス。",
"— Banner and article native ads inside public accounts. Good for building a subscriber base.":
"— 公式アカウント内のバナーと記事ネイティブ広告。購読者ベースの構築に効果的。",
"— Ads that drive users directly into WeChat mini programs. Ideal for e-commerce, services, and app-like experiences.":
"— ユーザーをWeChatミニプログラムに直接誘導する広告。EC、サービス、アプリのような体験に最適。",
"— Short video ads within WeChat's video feed. Growing fast as short-form content expands in China.":
"— WeChatのビデオフィード内のショート動画広告。中国でショートフォームコンテンツが拡大するにつれ急速に成長。",
"— Ads that appear in WeChat's internal search results. Catches users actively looking for something related to your brand.":
"— WeChatの内部検索結果に表示される広告。ブランドに関連するものを積極的に探しているユーザーを捕捉。",
"Beyond WeChat itself, Tencent Ads also covers":
"WeChat自体に加えて、Tencent Adsは以下もカバー：",
"(a network of partner apps and websites). If you want broad reach across China's internet, Tencent Ads gives you access to the full ecosystem.":
"（パートナーアプリとウェブサイトのネットワーク）。中国のインターネット全体に幅広くリーチしたい場合、Tencent Adsは完全なエコシステムへのアクセスを提供。",
"Yes. WeChat follows strict advertising regulations. Prohibited or heavily restricted industries include:":
"はい。WeChatは厳格な広告規制に従います。禁止または厳しく制限されている業種：",
"Finance: securities, private equity, cryptocurrency, P2P lending, online microlending;":
"金融：証券、プライベートエクイティ、暗号通貨、P2Pレンディング、オンラインマイクロレンディング；",
"Healthcare: certain medical treatments, prescription drugs, unapproved health products;":
"医療：特定の医療行為、処方薬、未承認の健康製品；",
"Content that violates WeChat community guidelines or Chinese advertising law.":
"WeChatコミュニティガイドラインまたは中国広告法に違反するコンテンツ。",
"What common mistakes cause WeChat ad rejection?":
"WeChat広告が否認されるよくあるミスは？",
"The most common reasons ads get rejected on WeChat:":
"WeChatで広告が否認される最も一般的な理由：",
"(1) Exaggerated or unverifiable claims — phrases like \"best,\" \"lowest price,\" or \"100% effective\" violate advertising regulations;":
"(1) 誇張または検証不可能な主張 — 「最高」「最安値」「100%効果的」などの表現は広告規制に違反；",
"(2) Missing or expired qualifications — your business license, trademark certificates, or industry licenses may be missing or expired;":
"(2) 資格証明書の欠落または期限切れ — 営業許可証、商標証明書、業界ライセンスが欠落または期限切れ；",
"(3) Landing page issues — the site must be hosted in mainland China with a valid ICP filing, and must match the ad content;":
"(3) ランディングページの問題 — サイトは中国本土でホストされ、有効なICP登録が必要で、広告内容と一致する必要があります；",
"(4) Prohibited content categories — the product or service itself may fall into restricted categories;":
"(4) 禁止コンテンツカテゴリ — 製品またはサービス自体が制限カテゴリに該当する可能性；",
"(5) Creative copy that feels like a hard sell rather than authentic content — WeChat reviewers pay close attention to how natural your ad feels.":
"(5) 本物のコンテンツではなくハードセルに感じられるコピー — WeChat審査者は広告がどれだけ自然かを重視。",

# === Douyin FAQ ===
"Can overseas companies advertise on Douyin?":
"海外企業はDouyinで広告を出せますか？",
"Yes. Overseas companies can advertise on Douyin through a certified Ocean Engine agency partner. Douyin is operated by ByteDance in China, while TikTok is the international version.":
"はい。海外企業は認定Ocean Engine代理店パートナーを通じてDouyinで広告を出稿できます。DouyinはByteDanceが中国で運営、TikTokは国際版です。",
"Ocean Engine offers bilingual support for international advertisers and has dedicated account management teams for cross-border campaigns.":
"Ocean Engineは国際的な広告主向けにバイリンガルサポートを提供し、クロスボーダーキャンペーン向けの専任アカウント管理チームがあります。",
"What is the difference between Douyin and TikTok Ads?":
"DouyinとTikTok広告の違いは？",
"Douyin is the Chinese domestic version of TikTok, operated by ByteDance. TikTok Ads is the international version for markets outside China.":
"DouyinはByteDanceが運営する中国国内版のTikTok。TikTok広告は中国国外市場向けの国際版。",
"Think of it this way: TikTok Ads reaches users outside China. Ocean Engine reaches the 700+ million daily active users inside China.":
"わかりやすく言えば：TikTok広告は中国国外のユーザーにリーチ。Ocean Engineは中国国内の7億人以上のデイリーアクティブユーザーにリーチ。",
"Some agencies offer both, letting you manage both markets from one interface, but the accounts and ad libraries are separate.":
"両方を提供する代理店もあり、1つのインターフェースで両市場を管理できますが、アカウントと広告ライブラリは別々です。",
"What documents do I need to open an Ocean Engine account?":
"Ocean Engineアカウント開設に必要な書類は？",
"For overseas companies working through an agency, the agency typically provides the qualification gateway. You will generally need:":
"海外企業が代理店を通じて運用する場合、代理店が通常資格ゲートウェイを提供。一般的に必要なもの：",
"(a) Company registration documents (business license, certificate of incorporation, or equivalent);":
"(a) 会社登録書類（営業許可証、設立証明書、または同等のもの）；",
"(b) Brand trademark registration certificate or authorization letter (if advertising a brand you do not own);":
"(b) ブランド商標登録証明書または許可証（非自社ブランドを広告する場合）；",
"(c) Landing page hosted in mainland China with a valid ICP filing (required for most product categories);":
"(c) 中国本土でホストされ、有効なICP登録があるランディングページ（ほとんどの製品カテゴリに必要）；",
"(d) Industry-specific licenses if applicable (healthcare, education, finance, and similar regulated sectors).":
"(d) 該当する場合の業界固有ライセンス（医療、教育、金融、および同様の規制セクター）。",
"The exact document list depends on your industry and product category.":
"正確な書類リストは業界と製品カテゴリによって異なります。",
"How long does account and ad review take?":
"アカウントと広告の審査にはどのくらいかかりますか？",
"Account review typically takes 1 to 3 business days for basic qualifications. Ad creative review is usually faster — 4 to 12 hours for standard content.":
"アカウント審査は基本的な資格で通常1〜3営業日。広告クリエイティブ審査は通常より速く、標準コンテンツで4〜12時間。",
"You cannot run ads until your account passes qualification review. Once approved, subsequent ad submissions get reviewed individually.":
"アカウントが資格審査に合格するまで広告は配信できません。承認後、後続の広告提出は個別に審査されます。",
"What is the minimum budget for Ocean Engine?":
"Ocean Engineの最低予算は？",
"The minimum daily budget per ad set is approximately USD 50 (or CNY equivalent). For meaningful testing, we recommend a monthly budget of at least USD 1,500 to 3,000.":
"広告セットあたりの最低日次予算は約50ドル（または相当する人民元）。有意義なテストには、月額最低1,500〜3,000ドルを推奨。",
"There is no mandatory monthly minimum published by the platform, but ad delivery can be constrained if budgets are too low.":
"プラットフォームが公表している強制的な月間最低額はありませんが、予算が低すぎると広告配信が制限される可能性があります。",
"How does Ocean Engine charge for advertising?":
"Ocean Engineの広告料金体系は？",
"Ocean Engine supports multiple billing models:":
"Ocean Engineは複数の課金モデルをサポート：",
"— Pay per 1,000 impressions. Good for brand awareness campaigns.":
"— 1,000インプレッションごとに課金。ブランド認知キャンペーンに適しています。",
"— Pay per click. Works well for driving traffic.":
"— クリックごとに課金。トラフィック誘導に効果的。",
"— The optimized versions. You define a conversion goal (app install, purchase, form fill) and the system optimizes delivery toward that goal.":
"— 最適化バージョン。コンバージョン目標（アプリインストール、購入、フォーム記入）を定義し、システムがその目標に向けて配信を最適化。",
"— Used for video ads. You pay when a user watches a defined duration of your video.":
"— 動画広告に使用。ユーザーが動画の定義された時間を視聴した場合に課金。",
"The platform runs on pre-paid billing for most international advertisers. You deposit funds and the system deducts based on actual consumption.":
"ほとんどの国際的な広告主はプリペイド課金。資金を入金し、実際の消費に基づいてシステムが差し引きます。",
"What are typical CPM and CPC rates on Douyin?":
"Douyinの一般的なCPMとCPCレートは？",
"Benchmarks vary widely by industry, targeting, and ad placement, but general ranges are:":
"ベンチマークは業界、ターゲティング、広告配置によって大きく異なりますが、一般的な範囲：",
"CPM: USD 3 to 10 (roughly CNY 22 to 72) per 1,000 impressions, depending on placement and competition. Brand takeovers cost more; in-feed ads are at the lower end.":
"CPM：1,000インプレッションあたり3〜10ドル（約22〜72元）、配置と競合による。ブランドテイクオーバーはより高く、インフィード広告は低め。",
"CPC: USD 0.50 to 1.50 (roughly CNY 3.5 to 11) per click. Competitive categories like beauty, fashion, and e-commerce tend to be higher.":
"CPC：クリックあたり0.50〜1.50ドル（約3.5〜11元）。美容、ファッション、ECなどの競争の激しいカテゴリは高め。",
"CPA / CPA goals through oCPM: typically USD 10 to 40 (CNY 70 to 290) depending on the conversion event and audience targeting.":
"CPA / oCPMによるCPA目標：通常10〜40ドル（70〜290元）、コンバージョンイベントとオーディエンスターゲティングによる。",
"These are indicative ranges, not guarantees. Actual costs depend on your targeting precision, creative quality, and industry competition.":
"これらは参考範囲であり、保証ではありません。実際のコストはターゲティング精度、クリエイティブ品質、業界競合によって異なります。",
"Does Ocean Engine support post-payment or credit terms?":
"Ocean Engineは後払いまたは与信枠をサポートしていますか？",
"Most international advertisers operate on a pre-paid basis. You deposit funds into your ad account before campaigns run.":
"ほとんどの国際的な広告主はプリペイド方式。キャンペーン配信前に広告アカウントに資金を入金。",
"Monthly billing (post-pay) may be available for established accounts with significant spend history and good standing.":
"月次請求（後払い）は、十分な支出履歴と良好なステータスを持つ確立されたアカウントで利用可能な場合があります。",
"How does the bidding system work on Ocean Engine?":
"Ocean Engineの入札システムはどのように機能しますか？",
"Ocean Engine uses a real-time auction system similar to other major ad platforms.":
"Ocean Engineは他の主要広告プラットフォームと同様のリアルタイムオークションシステムを使用。",
"You can also set bid caps (maximum cost per click or cost per thousand impressions) to control spending.":
"入札上限（クリック単価または1,000インプレッション単価の最大値）も設定可能。",
"What ad formats are available on Douyin?":
"Douyinで利用可能な広告フォーマットは？",
"Douyin offers a wide range of ad formats across its ecosystem:":
"Douyinはエコシステム全体で幅広い広告フォーマットを提供：",
"— Short video ads that appear in the user's main Douyin feed. The most common format. Skippable after a few seconds.":
"— ユーザーのメインDouyinフィードに表示されるショート動画広告。最も一般的なフォーマット。数秒後にスキップ可能。",
"— Full-screen video ad that plays automatically when users open Douyin. Premium placement, high impact, higher cost.":
"— ユーザーがDouyinを開いたときに自動再生されるフルスクリーン動画広告。プレミアム配置、高いインパクト、高コスト。",
"— Text and video ads that appear in Douyin's in-app search results for relevant keywords.":
"— Douyinのアプリ内検索結果に関連キーワードで表示されるテキストと動画広告。",
"— Ads placed in Douyin's trending content section.":
"— Douyinのトレンドコンテンツセクションに配置される広告。",
"— Display and video ads within Toutiao (ByteDance's news app).":
"— Toutiao（ByteDanceのニュースアプリ）内のディスプレイと動画広告。",
"Video creative is central to Douyin. Static image ads exist but video consistently outperforms them in engagement and conversion rates.":
"動画クリエイティブはDouyinの中心。静止画広告も存在しますが、動画はエンゲージメントとコンバージョン率で常に優れたパフォーマンスを発揮。",
"What industries are restricted on Douyin/Ocean Engine?":
"Douyin/Ocean Engineで制限されている業種は？",
"Like all major Chinese advertising platforms, Douyin restricts or prohibits advertising for:":
"すべての主要な中国広告プラットフォームと同様に、Douyinは以下を制限または禁止：",
"Finance: securities, private equity, cryptocurrency, P2P lending, microlending;":
"金融：証券、プライベートエクイティ、暗号通貨、P2Pレンディング、マイクロレンディング；",
"Healthcare: prescription drugs, unapproved medical treatments, medical devices requiring special approval;":
"医療：処方薬、未承認の医療行為、特別承認が必要な医療機器；",
"Content involving real-person testimonials (faces of non-consenting individuals);":
"実際の人物の証言（同意のない個人の顔）を含むコンテンツ；",
"Products or services requiring government-issued special permits;":
"政府発行の特別許可が必要な製品またはサービス；",
"Content that violates Chinese advertising law, including superlative claims (\"best,\" \"lowest price,\" etc.).":
"中国広告法に違反するコンテンツ（最上級表現「最高」「最安値」等を含む）。",
"Some restricted categories can advertise with special qualification approval. Check with us before planning your campaign.":
"一部の制限カテゴリは特別資格承認により広告可能。キャンペーン計画の前にお問い合わせください。",
"Under normal conditions, ad creative review takes 4 to 12 hours. During high-traffic periods (holidays, Double 11, etc.), it may extend to 24–48 hours.":
"通常、広告クリエイティブ審査は4〜12時間。高トラフィック期間（休日、ダブル11等）は24〜48時間に延長される場合があります。",
"Accounts with a clean history and previously approved creatives tend to get faster re-reviews. New accounts face longer initial reviews.":
"履歴が良好で以前承認されたクリエイティブがあるアカウントは再審査がより迅速。新規アカウントは初期審査に時間がかかります。",
"(1) Exaggerated or unverifiable claims — superlatives, guaranteed results, \"best\" language, and similar violations;":
"(1) 誇張または検証不可能な主張 — 最上級表現、結果保証、「最高」等の表現、および同様の違反；",
"(2) Landing page mismatch — the ad content must match the landing page;":
"(2) ランディングページの不一致 — 広告内容とランディングページの一致が必要；",
"(3) Missing or incomplete ICP filing — your landing page must be hosted in mainland China with a valid ICP filing;":
"(3) ICP登録の欠落または不完全 — ランディングページは中国本土でホストされ、有効なICP登録が必要；",
"(4) Content that mimics organic posts too closely — Douyin reviewers are sensitive to content that tricks users into thinking it is not an ad;":
"(4) オーガニック投稿に似すぎたコンテンツ — Douyin審査者は、広告でないとユーザーに誤認させるコンテンツに敏感；",
"(5) Restricted industry or product category without the required qualification documents.":
"(5) 必要な資格書類のない制限業種または製品カテゴリ。",
"We will audit your creative and landing page against Douyin's compliance guidelines before submission to minimize rejections.":
"提出前にDouyinのコンプライアンスガイドラインに照らしてクリエイティブとランディングページを監査し、否認を最小化します。",
"My TikTok creative is ready. Can I use it on Douyin?":
"TikTokのクリエイティブは準備済みです。Douyinで使用できますか？",
"You can repurpose TikTok creative for Douyin, but expect to need some modifications.":
"TikTokのクリエイティブをDouyinに転用できますが、修正が必要になることを想定してください。",
"— Add simplified Chinese subtitles. Some advertisers also add Chinese text overlays for brand name and key messaging.":
"— 簡体字中国語の字幕を追加。ブランド名とキーメッセージに中国語のテキストオーバーレイを追加する広告主も。",
"— If your TikTok ad has English voiceover, consider replacing it with Chinese voiceover or keeping it with Chinese subtitles.":
"— TikTok広告に英語のナレーションがある場合、中国語のナレーションに変更するか、中国語字幕付きで維持することを検討。",
"— Your TikTok ad likely links to a Western landing page. For Douyin, you need a mainland China-hosted landing page with ICP filing.":
"— TikTok広告は通常、欧米のランディングページにリンク。Douyinでは、中国本土でホストされICP登録されたランディングページが必要。",
"— Douyin has its own music library and popular tracks. Using trending Douyin sounds can improve organic reach and engagement.":
"— Douyinには独自の音楽ライブラリと人気トラックがあります。トレンドのDouyinサウンドを使用すると、オーガニックリーチとエンゲージメントが向上。",
"The creative concept and format translate well. The localization work is mainly in language, landing page, and cultural references.":
"クリエイティブのコンセプトとフォーマットは適応しやすい。ローカライズ作業は主に言語、ランディングページ、文化的参照。",
"How many Ocean Engine accounts can I manage on one device?":
"1台のデバイスでいくつのOcean Engineアカウントを管理できますか？",
"If you manage more than 5 accounts, you can grant access to additional accounts through the authorization center.":
"5つ以上のアカウントを管理する場合、認証センターを通じて追加アカウントへのアクセスを許可できます。",
"Where do I find Comment Management and Lead Management in the new Ocean Engine App?":
"新しいOcean Engineアプリでコメント管理とリード管理はどこにありますか？",
"After the latest app update, Comment Management and Lead Management have moved.":
"最新のアプリアップデート後、コメント管理とリード管理の場所が変わりました。",
"Both Comment Management and Lead Management are now grouped under Common Tools, along with other frequently used features.":
"コメント管理とリード管理は、他のよく使う機能とともに「共通ツール」の下にグループ化されました。",
"How do I adjust account budget in the Ocean Engine App?":
"Ocean Engineアプリでアカウント予算を調整する方法は？",
"There are two ways to modify account-level budget directly in the app:":
"アプリでアカウントレベルの予算を直接変更する2つの方法：",
"Path 1 supports both Juliangqianchuan (e-commerce) and Juliangmarketing (brand/performance) accounts.":
"方法1はJuliangqianchuan（EC）とJuliangmarketing（ブランド/パフォーマンス）の両方のアカウントをサポート。",
"How do I contact Ocean Engine customer support?":
"Ocean Engineのカスタマーサポートに連絡する方法は？",
"Within the Ocean Engine App, you can reach customer support via:":
"Ocean Engineアプリ内では、以下の方法でカスタマーサポートに連絡可能：",
"A live support agent is available through this channel for real-time troubleshooting.":
"このチャネルではリアルタイムトラブルシューティングのためのライブサポート担当者が利用可能。",

# === Bilibili FAQ ===
"Can foreign companies advertise on Bilibili?":
"外国企業はBilibiliで広告を出せますか？",
"Yes. Foreign companies can advertise on Bilibili, but the process requires working with a certified agency partner.":
"はい。外国企業はBilibiliで広告を出稿できますが、認定代理店パートナーとの連携が必要です。",
"Bilibili's advertising platform is called Bilibili MCN (member.bilibili.com/platform/ad), and the ad review process is managed through this platform.":
"Bilibiliの広告プラットフォームはBilibili MCNと呼ばれ、広告審査プロセスはこのプラットフォームを通じて管理されます。",
"What makes Bilibili different from other Chinese ad platforms?":
"Bilibiliが他の中国広告プラットフォームと違う点は？",
"Bilibili is a video-centric community with a highly engaged, younger audience (predominantly 18-35, 82% under 35).":
"Bilibiliは動画中心のコミュニティで、エンゲージメントの高い若年層（主に18〜35歳、82%が35歳未満）が特徴。",
"What documents are needed to open a Bilibili ad account?":
"Bilibili広告アカウント開設に必要な書類は？",
"For overseas companies working through an agency:":
"海外企業が代理店を通じて運用する場合：",
"(a) Company registration documents — business license, certificate of incorporation, or equivalent (translated into Chinese);":
"(a) 会社登録書類 — 営業許可証、設立証明書、または同等のもの（中国語翻訳付き）；",
"(b) Brand trademark registration certificate in China, or trademark authorization letter if you do not own the trademark;":
"(b) 中国でのブランド商標登録証明書、または非自社商標の場合は商標許可証；",
"(d) Industry-specific licenses if applicable — healthcare, education, finance, gaming, and other regulated sectors;":
"(d) 該当する場合の業界固有ライセンス — 医療、教育、金融、ゲーム、その他規制セクター；",
"(e) For HK/Macau/Taiwan companies: BR/CR certificate or equivalent identity document.":
"(e) 香港/マカオ/台湾企業の場合：BR/CR証明書または同等の身分証明書。",
"How long does Bilibili ad account approval take?":
"Bilibili広告アカウントの承認にはどのくらいかかりますか？",
"Account qualification review typically takes 1 to 5 business days, depending on document completeness and industry.":
"アカウント資格審査は通常1〜5営業日、書類の完全性と業界によって異なります。",
"Ad creative review is usually 4 to 12 hours for standard content.":
"広告クリエイティブ審査は標準コンテンツで通常4〜12時間。",
"What is the minimum budget for Bilibili advertising?":
"Bilibili広告の最低予算は？",
"The minimum daily budget per campaign is approximately USD 30 to 50 (CNY 200 to 350) depending on the ad format.":
"キャンペーンあたりの最低日次予算は約30〜50ドル（200〜350元）、広告フォーマットによる。",
"Note: Bilibili's auction system is often less crowded than Baidu or Douyin, which means lower CPM/CPC rates for early movers in your category.":
"注：BilibiliのオークションシステムはBaiduやDouyinより競争が少なく、カテゴリの先行者には低いCPM/CPCレートを意味します。",
"How does Bilibili charge for advertising?":
"Bilibiliの広告料金体系は？",
"Bilibili supports several billing models:":
"Bilibiliは複数の課金モデルをサポート：",
"— Pay per 1,000 impressions. Best for brand awareness campaigns.":
"— 1,000インプレッションごとに課金。ブランド認知キャンペーンに最適。",
"— Pay per click. Works for traffic-driving campaigns.":
"— クリックごとに課金。トラフィック誘導キャンペーンに効果的。",
"— Optimized models where you define a conversion goal and the algorithm optimizes delivery.":
"— コンバージョン目標を定義し、アルゴリズムが配信を最適化するモデル。",
"— Used for video ads, charged when a user watches a defined duration of your video.":
"— 動画広告に使用、ユーザーが定義された時間視聴した場合に課金。",
"Billing is pre-paid for most advertisers. Some established accounts with significant spend history may qualify for monthly invoicing.":
"ほとんどの広告主はプリペイド課金。支出履歴が十分にある確立されたアカウントは月次請求の対象となる場合があります。",
"What are typical CPM and CPC rates on Bilibili?":
"Bilibiliの一般的なCPMとCPCレートは？",
"Bilibili generally has lower rates than mainstream platforms because the auction is less competitive.":
"Bilibiliは一般的にメインプラットフォームより低いレート。オークションの競争が少ないため。",
"CPM: USD 2 to 8 (CNY 15 to 55) per 1,000 impressions, depending on placement and targeting.":
"CPM：1,000インプレッションあたり2〜8ドル（15〜55元）、配置とターゲティングによる。",
"CPC: USD 0.30 to 1.20 (CNY 2 to 8) per click. Gaming, tech, and anime-adjacent categories tend to have lower CPCs.":
"CPC：クリックあたり0.30〜1.20ドル（2〜8元）。ゲーム、テクノロジー、アニメ関連カテゴリは低め。",
"CPA through oCPM: USD 8 to 30 (CNY 55 to 210) depending on conversion event and audience fit.":
"oCPMによるCPA：8〜30ドル（55〜210元）、コンバージョンイベントとオーディエンスの適合性による。",
"These are indicative benchmarks. Actual costs depend on creative quality, audience targeting precision, and industry competition.":
"これらは参考ベンチマーク。実際のコストはクリエイティブ品質、オーディエンスターゲティング精度、業界競合によって異なります。",
"Does Bilibili offer post-payment or credit terms?":
"Bilibiliは後払いまたは与信枠を提供していますか？",
"Most new international advertisers operate on a pre-paid basis — you deposit funds before campaigns run.":
"ほとんどの新しい国際広告主はプリペイド方式 — キャンペーン配信前に資金を入金。",
"If credit terms are important to your operation, discuss this with us during onboarding.":
"与信枠が運用に重要な場合は、オンボーディング時にご相談ください。",
"What ad formats are available on Bilibili?":
"Bilibiliで利用可能な広告フォーマットは？",
"Bilibili offers a variety of formats, with video as the dominant format:":
"Bilibiliは多様なフォーマットを提供、動画が主要フォーマット：",
"— Short video ads that appear in the user's feed or between videos. The most common format.":
"— ユーザーのフィードまたは動画間に表示されるショート動画広告。最も一般的なフォーマット。",
"— Display banners on the Bilibili homepage and section pages.":
"— Bilibiliホームページとセクションページのディスプレイバナー。",
"— Sponsored content created by Bilibili creators. This is often the most effective format on Bilibili.":
"— Bilibiliクリエイターが作成するスポンサーコンテンツ。Bilibiliで最も効果的なフォーマット。",
"— A branded landing page experience for major campaigns.":
"— 主要キャンペーン向けのブランドランディングページ体験。",
"Video creative is central to Bilibili. Static ads exist but video consistently outperforms them, especially for engagement.":
"動画クリエイティブはBilibiliの中心。静止画広告も存在しますが、動画は特にエンゲージメントで常に優れたパフォーマンス。",
"Can I work with Bilibili creators (UP主) for advertising?":
"Bilibiliクリエイター（UP主）と広告で連携できますか？",
"Yes — and it is often the most effective approach on Bilibili.":
"はい — そしてそれはBilibiliで最も効果的なアプローチです。",
"Commercial collaboration through Bilibili's platform":
"Bilibiliのプラットフォームを通じた商業コラボレーション",
"— Working with creators directly through agencies or talent management (MCN) companies.":
"— 代理店またはタレントマネジメント（MCN）企業を通じてクリエイターと直接連携。",
"— Run platform ads + creator collaborations simultaneously for maximum reach and credibility.":
"— プラットフォーム広告＋クリエイターコラボレーションを同時に実施し、最大のリーチと信頼性を実現。",
"Bilibili's creator ecosystem covers virtually every interest: gaming, anime, tech, lifestyle, education, music, and more.":
"Bilibiliのクリエイターエコシステムは実質的にすべての興味をカバー：ゲーム、アニメ、テクノロジー、ライフスタイル、教育、音楽など。",
"What industries are restricted on Bilibili?":
"Bilibiliで制限されている業種は？",
"Bilibili restricts or prohibits advertising for:":
"Bilibiliは以下を制限または禁止：",
"Finance: P2P lending, cryptocurrency, private equity, microlending, securities trading platforms;":
"金融：P2Pレンディング、暗号通貨、プライベートエクイティ、マイクロレンディング、証券取引プラットフォーム；",
"Healthcare: Prescription drugs, unapproved medical devices or treatments, online pharmaceutical sales;":
"医療：処方薬、未承認の医療機器または治療、オンライン医薬品販売；",
"Products requiring government-issued special permits that are not provided;":
"政府発行の特別許可が提供されていない製品；",
"Content that violates Chinese advertising law, including superlative claims (\"best,\" \"lowest price,\" etc.).":
"中国広告法に違反するコンテンツ（最上級表現「最高」「最安値」等を含む）。",
"Some restricted categories may advertise with special qualification approval. Verify before planning campaigns.":
"一部の制限カテゴリは特別資格承認により広告可能。キャンペーン計画前に確認。",
"Bilibili's audience values authenticity, humor, and genuine knowledge sharing.":
"Bilibiliのオーディエンスは信頼性、ユーモア、本物の知識共有を重視。",
"(1) Educational/informational content with personality — tech reviews, tutorial-style content, deep dives into specific topics;":
"(1) 個性のある教育的/情報提供コンテンツ — テクノロジーレビュー、チュートリアル形式、特定トピックの深掘り；",
"(1) Direct hard-sell ads without context; (2) Content that feels templated or copied from other platforms;":
"(1) 文脈のない直接的なハードセル広告；(2) テンプレート化された、または他プラットフォームからコピーされたコンテンツ；",
"The best Bilibili campaigns usually involve some level of native content or creator collaboration, not just direct brand promotion.":
"最高のBilibiliキャンペーンは通常、ある程度のネイティブコンテンツまたはクリエイターコラボレーションを含み、単なる直接的なブランドプロモーションではありません。",
"Why are my Bilibili ads getting rejected?":
"Bilibili広告が否認される理由は？",
"(1) Exaggerated or superlative claims — \"best,\" \"lowest price,\" \"100% effective,\" and similar language;":
"(1) 誇張または最上級表現 — 「最高」「最安値」「100%効果的」および同様の表現；",
"(2) Content that mimics organic posts without proper advertising disclosure — Bilibili reviewers are strict about this;":
"(2) 適切な広告表示のないオーガニック投稿に似たコンテンツ — Bilibili審査者はこれに厳格；",
"(3) Landing page mismatch — ad content must match the landing page exactly;":
"(3) ランディングページの不一致 — 広告内容とランディングページが正確に一致する必要があります；",
"(4) Missing or invalid ICP filing for the landing page URL;":
"(4) ランディングページURLのICP登録の欠落または無効；",
"(5) References to Bilibili's IP, mascot (2233娘), or trademarked elements without authorization;":
"(5) BilibiliのIP、マスコット（2233娘）、または商標要素への無許可の言及；",
"(6) Content referencing gaming restrictions, age-gating, or other policy-sensitive topics without proper context;":
"(6) 適切な文脈のないゲーム規制、年齢制限、その他ポリシーに敏感なトピックへの言及；",
"(7) Content that could be perceived as exploiting youth audiences or controversial social topics.":
"(7) 若年層の搾取または物議を醸す社会的トピックとして受け取られる可能性のあるコンテンツ。",
"We audit creative against Bilibili's compliance guidelines before submission to minimize rejections.":
"提出前にBilibiliのコンプライアンスガイドラインに照らしてクリエイティブを監査し、否認を最小化。",
"Should I use Douyin/TikTok content on Bilibili?":
"Douyin/TikTokのコンテンツをBilibiliで使用すべきですか？",
"You can repurpose video content, but direct cross-posting without adaptation is not recommended.":
"動画コンテンツを転用できますが、適応なしの直接クロスポストは推奨されません。",
"— Bilibili users watch longer videos (5 to 30+ minutes). Short 15-60 second clips may not perform well.":
"— Bilibiliユーザーはより長い動画（5〜30分以上）を視聴。15〜60秒のショートクリップはパフォーマンスが低い可能性。",
"— Add simplified Chinese subtitles if your video has dialogue;":
"— 動画に台詞がある場合は簡体字中国語の字幕を追加；",
"— Adapt to Bilibili's informal, community-driven tone. Content with humor, self-deprecation, and genuine insight performs best.":
"— Bilibiliのインフォーマルでコミュニティ駆動のトーンに適応。ユーモア、自嘲、本物の洞察を含むコンテンツが最も効果的。",
"— Douyin's trending sounds may not resonate with Bilibili users, who have their own distinct audio culture.":
"— DouyinのトレンドサウンドはBilibiliユーザーには響かない可能性あり。Bilibiliには独自のオーディオ文化があります。",
"— If using creator content, work with Bilibili creators rather than porting Douyin creator collaborations directly.":
"— クリエイターコンテンツを使用する場合、Douyinのクリエイターコラボを直接移植するのではなく、Bilibiliクリエイターと連携。",
"For best results, create Bilibili-specific content or significantly adapt existing creative to fit the platform's style.":
"最良の結果を得るには、Bilibili固有のコンテンツを作成するか、既存のクリエイティブをプラットフォームのスタイルに大幅に適応。",

# === GEO FAQ ===
"GEO stands for Generative Engine Optimization. It is the practice of making your brand and content easy for AI systems to find, understand, and cite in their generated answers.":
"GEO（生成エンジン最適化）とは、AIシステムがブランドとコンテンツを発見、理解、生成回答で引用しやすくする実践です。",
"Where SEO targets search engine rankings, GEO targets AI-generated answers.":
"SEOが検索エンジンのランキングを対象とするのに対し、GEOはAI生成の回答を対象とします。",
"SEO and GEO serve different channels and produce different outcomes.":
"SEOとGEOは異なるチャネルにサービスを提供し、異なる結果を生み出します。",
"SEO puts your website higher in search engine results pages. Users still need to click through to your site.":
"SEOはウェブサイトを検索エンジン結果ページで上位に表示。ユーザーはサイトへのクリックが必要。",
"GEO aims to get your brand mentioned directly inside an AI answer. The user may never leave the AI interface.":
"GEOはAIの回答内でブランドが直接言及されることを目指します。ユーザーはAIインターフェースを離れる必要がないかもしれません。",
"Think of SEO as earning a spot on a menu. GEO is getting the waiter to recommend your dish by name.":
"SEOはメニューに載ること。GEOはウェイターがあなたの料理を名前で推薦すること。",
"Which AI platforms does GEO target in China?":
"中国GEOはどのAIプラットフォームをターゲットにしていますか？",
"Our GEO service focuses on the AI platforms most used by Chinese consumers:":
"当社のGEOサービスは中国消費者が最も使用するAIプラットフォームに焦点：",
"DeepSeek — fastest-growing reasoning model in China, widely adopted across industries":
"DeepSeek — 中国で最も急成長している推論モデル、業界全体で広く採用",
"Doubao (ByteDance) — integrated with Douyin, massive user base, frequently cited by younger audiences":
"豆包（ByteDance） — Douyinと統合、巨大なユーザーベース、若年層によく引用される",
"Kimi (Moonshot) — strong with professionals and knowledge workers":
"Kimi（Moonshot） — プロフェッショナルとナレッジワーカーに強い",
"Wenxin Yiyan (Baidu) — benefits from Baidu search data, relevant for users with commercial intent":
"文心一言（Baidu） — Baidu検索データの恩恵、商業目的のユーザーに関連",
"We track which platforms your target audience actually uses and prioritize accordingly.":
"ターゲットオーディエンスが実際に使用するプラットフォームを追跡し、それに応じて優先順位付け。",
"Audit &amp; Strategy — USD 1,500 for a one-time assessment and action plan.":
"Audit &amp; Strategy — 一回限りの評価とアクションプランで1,500ドル。",
"Enterprise — USD 4,500 per half-year. Includes content optimization, monthly performance reports, and strategy calls.":
"Enterprise — 半期4,500ドル。コンテンツ最適化、月次パフォーマンスレポート、戦略ミーティングを含む。",
"Professional — USD 18,000 per year. Everything in Enterprise, plus quarterly strategy reviews, priority support, and dedicated account management.":
"Professional — 年額18,000ドル。Enterpriseのすべてに加え、四半期戦略レビュー、優先サポート、専任アカウント管理。",
"It depends on what you compare. Entry-level GEO (Audit &amp; Strategy) is comparable to a basic SEO audit.":
"何と比較するかによります。エントリーレベルのGEO（Audit &amp; Strategy）は基本的なSEO監査に相当。",
"The difference is in the outcome: SEO brings users to your website, GEO gets your brand mentioned in AI answers.":
"違いは結果にあります：SEOはユーザーをウェブサイトに誘導、GEOはAI回答内でブランドを言及させます。",
"Unlike SEO, where rankings give you a clear number, GEO is harder to measure because AI platforms do not publish rankings.":
"SEOがランキングという明確な数値を提供するのに対し、GEOはAIプラットフォームがランキングを公開しないため測定が難しい。",
"We measure what we can: (1) Share of voice — how often your brand appears in AI responses;":
"当社は測定可能なものを測定：(1) シェア・オブ・ボイス — AI応答にブランドがどの程度表示されるか；",
"We provide monthly reports with trend charts. You should expect 3 to 6 months of data before seeing clear patterns.":
"月次レポートとトレンドチャートを提供。明確なパターンを確認するには3〜6ヶ月のデータが必要です。",
"GEO moves slower than paid ads. Most clients start seeing measurable changes within 3 to 6 months of consistent effort.":
"GEOは有料広告よりも効果が出るのが遅い。ほとんどのクライアントは一貫した取り組みから3〜6ヶ月で測定可能な変化を確認。",
"The reason: AI systems update their models periodically. Changes we make today may take weeks or months to be reflected.":
"理由：AIシステムは定期的にモデルを更新。今日行った変更が反映されるまでに数週間から数ヶ月かかる場合があります。",
"We will share early signals within the first month — internal testing results, preliminary probe checks, and baseline measurements.":
"最初の1ヶ月以内に初期シグナルを共有 — 内部テスト結果、予備プローブチェック、ベースライン測定。",
"A GEO audit report — your current visibility across DeepSeek, Doubao, Kimi, and Wenxin Yiyan, with actionable recommendations;":
"GEO監査レポート — DeepSeek、豆包、Kimi、文心一言での現在の可視性と実行可能な推奨事項；",
"Optimized content — rewritten or newly created articles, FAQ pages, and data points designed for AI citation;":
"最適化されたコンテンツ — AI引用向けに書き直された、または新規作成された記事、FAQページ、データポイント；",
"Monthly performance reports — share of voice trends, query coverage maps, and recommended next steps;":
"月次パフォーマンスレポート — シェア・オブ・ボイストレンド、クエリカバレッジマップ、推奨される次のステップ；",
"Strategy consultations — quarterly calls to align GEO work with your broader marketing and business objectives.":
"戦略コンサルテーション — GEOの取り組みを広範なマーケティングとビジネス目標に合わせるための四半期ミーティング。",
"Not necessarily, but it helps. AI systems do reference content from global websites — including English-language sites.":
"必ずしも必要ではありませんが、あると便利です。AIシステムはグローバルウェブサイト — 英語サイトを含む — のコンテンツを参照します。",
"That said, a Chinese-language website (or a properly configured subdomain) gives AI systems more signal to cite your brand in Chinese-language queries.":
"とはいえ、中国語のウェブサイト（または適切に設定されたサブドメイン）は、中国語クエリでブランドを引用するシグナルをAIシステムに与えます。",
"If you do not have a Chinese website yet, we can work with your existing site and recommend whether a Chinese site is needed.":
"まだ中国語ウェブサイトをお持ちでない場合、既存サイトで対応可能か、中国語サイトが必要かをお勧めします。",
"How often should GEO content be updated?":
"GEOコンテンツはどのくらいの頻度で更新すべきですか？",
"We recommend reviewing and refreshing content every 3 to 6 months.":
"3〜6ヶ月ごとにコンテンツを見直し、更新することを推奨。",
"Quarterly refreshes are standard for most clients. If your industry is fast-moving (tech, finance, healthcare), consider monthly updates.":
"四半期ごとの更新がほとんどのクライアントの標準。業界の動きが速い場合（テック、金融、ヘルスケア）は月次更新を検討。",
"SEO first, in most cases. A functioning SEO foundation — a crawlable website, structured content, proper metadata — is table stakes for GEO.":
"ほとんどの場合、SEOが先。機能するSEO基盤 — クロール可能なウェブサイト、構造化されたコンテンツ、適切なメタデータ — はGEOの前提条件。",
"If you have no website or a site that is technically broken, fix that before paying for GEO.":
"ウェブサイトがないか、技術的に壊れているサイトがある場合、GEOに費用を払う前に修正してください。",
"We sometimes run both in parallel for clients with existing infrastructure, as the content work often overlaps significantly.":
"既存インフラがあるクライアントには、両方を並行して実施することもあります。コンテンツ作業は多くの場合大幅に重複するため。",
"Can GEO replace my existing SEO efforts?":
"GEOは既存のSEO取り組みを置き換えられますか？",
"No. AI-generated answers do not replace search engine results pages — they sit alongside them.":
"いいえ。AI生成の回答は検索エンジン結果ページを置き換えるものではなく、それらと並んで存在します。",
"GEO is an additional channel, not a replacement. The clients who benefit most from GEO are the ones who already have a solid SEO foundation.":
"GEOは追加チャネルであり、置き換えではありません。GEOから最も恩恵を受けるクライアントは、すでに強固なSEO基盤を持っているクライアントです。",
"Cutting SEO to fund GEO would likely hurt your overall visibility in the long run.":
"SEOを削ってGEOに資金を回すと、長期的には全体的な可視性を損なう可能性があります。",
"They serve different parts of the funnel and complement each other well.":
"両者はファネルの異なる部分を担当し、互いに補完し合います。",
"Baidu SEM reaches users who are actively searching right now — high commercial intent, immediate conversion potential.":
"Baidu SEMは今まさに能動的に検索しているユーザーにリーチ — 高い商業意図、即時のコンバージョン可能性。",
"Think of SEM as paying for a spot at the front of the line. GEO is trying to become the name the waiter recommends.":
"SEMは列の先頭の場所にお金を払うこと。GEOはウェイターが推薦する名前になること。",
"Some clients also use GEO to research which topics and queries their AI-visibility competitors are winning.":
"一部のクライアントは、競合がAI可視性で勝っているトピックとクエリを調査するためにもGEOを利用。",
"Based on what AI systems tend to reference:":
"AIシステムが参照する傾向があるものに基づく：",
"FAQ pages — direct Q&amp;A format maps naturally to how users ask AI questions. High priority.":
"FAQページ — 直接的なQ&A形式はユーザーがAIに質問する方法に自然にマッピング。優先度：高。",
"Data points and statistics — specific numbers, benchmarks, and research findings get cited frequently.":
"データポイントと統計 — 具体的な数字、ベンチマーク、調査結果は頻繁に引用される。",
"Clear definitions and explanations — the AI equivalent of a dictionary entry":
"明確な定義と説明 — 辞書エントリのAI版",
"Case studies and real examples — concrete stories outperform abstract claims":
"ケーススタディと実例 — 具体的なストーリーは抽象的な主張より効果的",
"Properly structured articles — clear headings (H1/H2/H3), opening paragraphs that answer the main question directly.":
"適切に構造化された記事 — 明確な見出し（H1/H2/H3）、メインの質問に直接答える冒頭段落。",

# === Bing FAQ ===
"Bing China's user base represents a premium audience: highly educated, urban, and with above-average income levels.":
"Bing Chinaのユーザーベースはプレミアムオーディエンス：高学歴、都市部、平均以上の所得層。",
"More than 75% hold college degrees, compared to 57% national average":
"75%以上が大学学位保有（全国平均57%に対して）",
"27.5% overrepresentation in personal monthly income over ¥8,000 (TGI 127.5)":
"月収8,000元以上の割合が27.5%超過（TGI 127.5）",
"This makes Bing China users ideal for brands targeting educated professionals, urban consumers, and high-value segments.":
"これによりBing Chinaユーザーは、教育を受けたプロフェッショナル、都市部消費者、高価値セグメントをターゲットとするブランドに最適。",
"How do Bing China users differ from Baidu users?":
"Bing ChinaユーザーはBaiduユーザーとどう違う？",
"Bing China attracts a younger, more educated, and higher-income demographic compared to Baidu's broader, more diversified user base.":
"Bing ChinaはBaiduのより広く多様化されたユーザーベースと比較して、より若く、高学歴で、高所得の層を引き付けています。",
"More representative of general population":
"一般的な人口により近い",
"For international advertisers, this means Bing China offers a more premium audience, while Baidu provides maximum reach.":
"国際的な広告主にとって、Bing Chinaはよりプレミアムなオーディエンスを提供し、Baiduは最大のリーチを提供します。",
"What are Bing China users interested in buying?":
"Bing Chinaユーザーは何を買いたいと思っていますか？",
"Bing China users show strong purchasing intent across several categories, with average planned spending of ¥3,040.1 per month.":
"Bing Chinaユーザーは複数のカテゴリで強い購買意欲を示し、平均計画月間支出は3,040.1元。",
"Additionally, 68% express interest in AI technology, making them early adopters for tech products and services.":
"さらに68%がAIテクノロジーに関心を示し、テクノロジー製品とサービスのアーリーアダプター。",
"What advertising formats work best on Bing China?":
"Bing Chinaで最も効果的な広告フォーマットは？",
"Based on user behavior data, the following ad formats perform well:":
"ユーザー行動データに基づき、以下の広告フォーマットが効果的：",
"59% of users research products before purchase, making search ads effective for capturing intent":
"59%のユーザーが購入前に製品をリサーチ、検索広告が意図の捕捉に効果的",
"With 68% interest in AI, technology-focused display ads see higher engagement":
"AI関心度68%により、テクノロジー重視のディスプレイ広告が高いエンゲージメント",
"Education and professional service promotions:":
"教育および専門サービスのプロモーション：",
"Over 75% college educated, with planned education spending averaging ¥3,040.1":
"75%以上が大学教育を受け、計画的教育支出は平均3,040.1元",
"Higher income levels support premium product advertising":
"高所得レベルがプレミアム製品広告をサポート",
"Additionally, 62% of users show greater willingness to engage with ads compared to average users.":
"さらに62%のユーザーが平均的なユーザーよりも広告と関わる意欲を示します。",
"Which industries are best suited for Bing China advertising?":
"Bing広告に最も適した業種は？",
"68% interest in AI, high education level":
"AI関心度68%、高学歴",
">75% college educated, 72.4% plan education spending for children":
"75%超が大学教育、72.4%が子どもの教育費を計画",
"High disposable income (¥4,334.5 monthly personal consumption)":
"高い可処分所得（月間個人消費4,334.5元）",
"Professional user base with decision-making authority":
"意思決定権を持つプロフェッショナルユーザーベース",
"These categories align with the demographic and behavioral characteristics of Bing China users.":
"これらのカテゴリはBing Chinaユーザーの人口統計的・行動的特性と一致。",
"Some restricted categories can advertise with special qualification approval.":
"一部の制限カテゴリは特別資格承認により広告可能。",

# === Other common text ===
"Baidu's official rule is a minimum top-up of CNY 2,400. However, to save on transaction fees and reduce transfer time, we recommend a single top-up of at least CNY 10,000.":
"Baiduの公式ルールでは最低チャージ額は2,400元です。ただし、振込手数料を節約し入金時間を短縮するため、最低10,000元の一括チャージをお勧めします。",
"The most common rejection reasons are: (1) Expired qualifications or licenses; (2) Content contains prohibited words; (3) Website is unreachable or offline; (4) Mismatch between ad content and landing page; (5) Missing or incorrect industry qualification documents.":
"最も一般的な否認理由：(1) 期限切れの資格またはライセンス；(2) 禁止用語を含むコンテンツ；(3) ウェブサイトにアクセスできない、またはオフライン；(4) 広告内容とランディングページの不一致；(5) 業界資格証明書の欠落または誤り。",
"Yes. Regulated industries such as healthcare and finance must provide industry-specific licenses, avoid efficacy claims in all ad copy and landing pages, and comply with strict review standards.":
"はい。医療や金融などの規制業界は、業界固有のライセンスを提出し、全広告文とランディングページで効能主張を避け、厳格な審査基準に準拠する必要があります。",
"Yes, but the process is not as straightforward as Baidu. Xiaohongshu requires a Chinese business license for direct account registration. Foreign companies typically advertise through TMG as a certified agency partner.":
"はい、ただしBaiduほど簡単ではありません。小紅書は直接アカウント登録に中国の営業許可証が必要です。外国企業は通常、TMGの認定代理店パートナーを通じて広告出稿します。",
"Companies registered in Hong Kong, Japan, South Korea, or Taiwan can apply with additional documentation. For all other countries, eligibility is assessed case by case through the agency.":
"香港、日本、韓国、台湾に登録されている企業は追加書類で申請可能。その他の国は代理店を通じてケースバイケースで審査。",
"At minimum, you need a Chinese business license (if registering directly) or a partnership agreement with a certified agency. Depending on your industry and ad content, you may also need:":
"最低限、中国の営業許可証（直接登録の場合）または認定代理店とのパートナーシップ契約。業界や広告内容によっては以下も必要：",
"Foreign entities need to provide a BR or CR certificate (Hong Kong) or a declaration letter (Japan, South Korea, Taiwan).":
"外国企業はBR/CR証明書（香港）または宣誓書（日本、韓国、台湾）を提出。",
"The review process on Xiaohongshu's professional account takes up to 30 days. The platform charges a one-time review fee of CNY 600 per application — non-refundable.":
"小紅書プロフェッショナルアカウントの審査には最大30日。プラットフォームは申請ごとに600元の一回限りの審査料（返金不可）を請求。",
"The account name must relate to your registered business name, trademark, or website/app name. It cannot be vague, impersonate real people, or mimic Xiaohongshu official branding.":
"アカウント名は登録事業者名、商標、ウェブサイト/アプリ名に関連が必要。曖昧、実在人物の模倣、小紅書公式ブランディングの模倣は不可。",
"Two options: CPC (cost per click) and CPM (cost per thousand impressions). You pick the model that fits your goal. CPC makes sense when you want actual traffic; CPM works best for brand visibility.":
"2つのオプション：CPC（クリック課金）とCPM（インプレッション課金）。目標に合わせて選択。実際のトラフィックを求めるならCPC、ブランド認知にはCPMが最適。",
"There is no hard minimum published by the platform, but in practice you need at least a few thousand CNY to test and gather meaningful data. Once your account is approved, you can start with a modest budget and scale up.":
"プラットフォーム公表の最低額はありませんが、実務上は数千元のテスト予算が必要。アカウント承認後は少額から開始し、スケールアップ可能。",
"Yes. The professional account review fee is CNY 600 (one-time, non-refundable). If you work through an agency, there is typically a service fee on top of the ad spend.":
"はい。プロフェッショナルアカウント審査料600元（一回限り、返金不可）。代理店を通じて運用する場合、広告費に加えてサービス料が発生。",
"It varies a lot by industry and targeting. Low-competition niches might see CPCs of a few yuan. Competitive categories like beauty, fashion, or mother-and-baby can see CPCs of 10–30+ CNY.":
"業界やターゲティングによって大きく異なります。競合の少ないニッチでは数元、美容、ファッション、マタニティなどの競争の激しいカテゴリでは10〜30元以上。",
"Three things to check: your bid might be too low (raise it), your targeting might be too narrow (loosen it), or your creative might have failed review (check your account notifications).":
"3つの確認ポイント：入札額が低すぎる（上げる）、ターゲティングが狭すぎる（広げる）、クリエイティブが審査に落ちている（アカウント通知を確認）。",
"Impressions without conversions usually point to an audience mismatch or a landing page problem.":
"インプレッションのみでコンバージョンがない場合、オーディエンスのミスマッチかランディングページの問題。",
"The big ones: using someone's face in your avatar (not allowed), mentioning prohibited industries (finance, gambling, tobacco, medical/health, dietary supplements), unlicensed trademark usage, and missing ICP filings.":
"主な理由：アバターに他人の顔を使用（禁止）、禁止業種への言及（金融、ギャンブル、タバコ、医療/健康、サプリメント）、無許可の商標使用、ICP登録の欠落。",
"Yes. Financial services (securities, private equity, cryptocurrency, P2P lending), gambling, tobacco, and certain health/medical categories are either fully restricted or heavily regulated.":
"はい。金融サービス（証券、PE、暗号通貨、P2Pレンディング）、ギャンブル、タバコ、特定の健康/医療カテゴリは全面的に制限されるか、厳しく規制されています。",
"If the account name references a trademark, you need to prove you own it or have authorization.":
"アカウント名が商標を参照する場合、所有権または使用許可の証明が必要。",
"Yes. If your account name or ad content references a website, Xiaohongshu requires a screenshot of the ICP filing (MIIT) from China's MIIT.":
"はい。アカウント名や広告コンテンツがウェブサイトを参照する場合、小紅書は中国MIITのICP登録のスクリーンショットを要求。",
"The avatar cannot be a real person's face or a photo showing someone's face. It must be relevant to your brand, product, or company.":
"アバターは実際の人物の顔や顔写真を使用できません。ブランド、製品、会社に関連するものでなければなりません。",
"Xiaohongshu isn't just another social media platform—it's where 350 million Chinese consumers go to research products before buying.":
"小紅書は単なるソーシャルメディアプラットフォームではありません — 3億5千万人の中国消費者が購入前に製品をリサーチする場所です。",
"Unlike platforms where ads interrupt, XHS thrives on authentic user-generated content (种草, \"seeding\")—everyday consumers sharing real experiences.":
"広告が割り込むプラットフォームとは異なり、XHSは本物のUGC（种草＝シーディング）で成長 — 一般消費者が実際の体験を共有。",
"Over 4.5 million brand employees now act as trusted product experts, generating 29,000+ monthly leads.":
"450万人以上のブランド従業員が信頼される製品エキスパートとして活動し、月間29,000件以上のリードを生成。",
"The most common rejection reasons are: (1) Expired qualifications or licenses; (2) Content contains prohibited words; (3":
"最も一般的な否認理由：(1) 期限切れの資格またはライセンス；(2) 禁止用語を含むコンテンツ；(3",
"Yes, but the process is not as straightforward as Baidu. Xiaohongshu requires a Chinese business license for direct acco":
"はい、ただしBaiduほど簡単ではありません。小紅書は直接アカウント登録に中国の営業許可証が必要です。外国企業は通常",
"Yes. Regulated industries such as healthcare and finance must provide industry-specific licenses, avoid efficacy claims ":
"はい。医療や金融などの規制業界は、業界固有のライセンスを提出し、効能主張を避け",
}

def translate_faq():
    filepath = os.path.join(BASE, 'ja/faqs/index.html')
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    replacements = 0
    for eng, jp in sorted(D.items(), key=lambda x: -len(x[0])):
        if eng in content:
            content = content.replace(eng, jp)
            replacements += 1
    
    if replacements > 0:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
    
    print(f'FAQ: {replacements} replacements')
    return replacements

if __name__ == '__main__':
    total = translate_faq()
    print(f'Done: {total} total')
