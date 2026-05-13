"""
Translate blog content from English to Japanese (JA) and Korean (KO).
Uses exact dictionary-based string replacement — NO BeautifulSoup.
Safe for HTML files.
"""

import re, os

def translate_file(filepath, translations):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    modified = False
    for en_text, tr_text in translations.items():
        if en_text in content:
            content = content.replace(en_text, tr_text)
            modified = True
        else:
            print(f"  ⚠ NOT FOUND: {en_text[:60]}...")
    
    if modified:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False

# ─── Japanese Translations ───

ja_translations = {
    # Hero
    '<span>Doubao</span> Added Ads — Is <span>GEO</span> Still Worth It?':
        '<span>Doubao</span>に広告が登場 — <span>GEO</span>はまだ必要？',
    '<p class="article-hero__intro">Doubao (ByteDance AI) has started running ads. Many are asking: is GEO still worth it? The short answer: yes — and more than ever. Here\'s why paid and natural AI traffic work together.</p>':
        '<p class="article-hero__intro">Doubao（ByteDance AI）が広告配信を開始しました。「GEOはまだ意味があるのか？」と多くの方が疑問に思っています。答えはシンプルです。**はい、そしてこれまで以上に重要です**。有料トラフィックと自然AIトラフィックがどのように連携するのか、その理由をご説明します。</p>',

    # Article body - Section 1
    '<h2>Every Medium Has Two Types of Traffic</h2>':
        '<h2>あらゆるメディアに2種類のトラフィックが存在する</h2>',
    "<p>Let's go back to basics:</p>":
        '<p>基本に戻りましょう：</p>',
    '<p>In every media era, there are two kinds of traffic — <strong>organic</strong> and <strong>paid</strong>.</p>':
        '<p>あらゆるメディア時代において、トラフィックには<strong>オーガニック</strong>と<strong>有料</strong>の2種類があります。</p>',
    '<li><strong>Search era:</strong> SEO was organic, SEM was paid.</li>':
        '<li><strong>検索時代：</strong>SEOがオーガニック、SEMが有料でした。</li>',
    '<li><strong>WeChat era:</strong> Content growth was organic, ad spend was paid.</li>':
        '<li><strong>WeChat時代：</strong>コンテンツ成長がオーガニック、広告費が有料でした。</li>',
    '<li><strong>Douyin era:</strong> Video recommendations were organic, DOU+ and feed ads were paid.</li>':
        '<li><strong>Douyin時代：</strong>動画レコメンドがオーガニック、DOU+やフィード広告が有料でした。</li>',
    '<li><strong>AI Search era:</strong> <strong>GEO is organic, AI ads are paid.</strong></li>':
        '<li><strong>AI検索時代：</strong><strong>GEOがオーガニック、AI広告が有料です。</strong></li>',
    '<p>The logic has never changed.</p>':
        '<p>この構図は決して変わりません。</p>',
    '<p>When Baidu launched SEM ads, did companies stop doing SEO? No. They ran SEM for immediate traffic while building SEO as a long-term asset.</p>':
        '<p>BaiduがSEM広告を開始したとき、企業はSEOをやめましたか？いいえ。彼らはSEMで即時のトラフィックを得ながら、SEOを長期的な資産として構築しました。</p>',
    '<h4>Key Principle</h4>':
        '<h4>重要な原則</h4>',
    '<p><strong>Paid traffic is rented — stop paying, it vanishes. Organic traffic is an asset — nobody can take it away.</strong></p>':
        '<p><strong>有料トラフィックは賃貸 — 支払いを止めれば消えます。オーガニックトラフィックは資産 — 誰も奪えません。</strong></p>',
    '<p>The same logic applies to AI search. You will be able to buy Doubao ads for instant exposure, but the trust assets you build through GEO will keep generating free AI recommendations day after day.</p>':
        '<p>同じロジックがAI検索にも当てはまります。Doubao広告を購入して即座に露出を得ることはできますが、GEOを通じて構築した信頼資産は、日々無料のAIレコメンドを生み出し続けます。</p>',
    '<p><strong>You need both legs to walk.</strong></p>':
        '<p><strong>歩くには両足が必要です。</strong></p>',

    # Section 2
    '<h2>Paid Traffic Scales Results — Organic Traffic Cuts Costs</h2>':
        '<h2>有料トラフィックは成果を拡大し、オーガニックトラフィックはコストを削減する</h2>',
    '<p>Paid traffic and organic traffic serve completely different roles.</p>':
        '<p>有料トラフィックとオーガニックトラフィックはまったく異なる役割を果たします。</p>',
    '<div class="stat-card__label">ChatGPT ad CPC</div>':
        '<div class="stat-card__label">ChatGPT広告CPC</div>',
    '<div class="stat-card__label">ChatGPT CPM (3x more than Meta)</div>':
        '<div class="stat-card__label">ChatGPT CPM（Metaの3倍）</div>',
    '<div class="stat-card__label">Months for GEO trust assets to build</div>':
        '<div class="stat-card__label">GEO信頼資産構築にかかる月数</div>',
    '<h3>Paid traffic: short-term scaling</h3>':
        '<h3>有料トラフィック：短期的な拡大</h3>',
    "<p>You spend ad dollars today, you see traffic tomorrow. ChatGPT's CPC is $3-5, and Doubao's ad pricing won't be cheap either. But paid traffic lets you:</p>":
        '<p>今日広告費を投じれば、明日にはトラフィックが得られます。ChatGPTのCPCは3〜5ドルで、Doubaoの広告料金も安くはないでしょう。しかし有料トラフィックには以下のメリットがあります：</p>',
    '<li>Test markets quickly</li>':
        '<li>市場を迅速にテストできる</li>',
    '<li>Acquire leads fast</li>':
        '<li>リードを素早く獲得できる</li>',
    '<li>Validate products immediately</li>':
        '<li>製品をすぐに検証できる</li>',
    "<p>For companies with budget, AI advertising will become a critical acquisition channel — a new traffic gateway, a new growth curve. <strong>Whoever figures it out first wins.</strong></p>":
        '<p>予算のある企業にとって、AI広告は重要な獲得チャネルになります — 新しいトラフィックの玄関口、新しい成長曲線です。<strong>最初に活用した者が勝ちます。</strong></p>',
    '<h4>The Hidden Cost of Paid Traffic</h4>':
        '<h4>有料トラフィックの隠れたコスト</h4>',
    "<p>Bidding ads have a fundamental flaw: <strong>the more participants, the higher the price.</strong> Early Baidu SEM cost pennies per click. Today? Some industries pay $10-50 per click. The same will happen with AI ads. Doubao ad prices will only go up over time.</p>":
        '<p>入札型広告には根本的な欠点があります：<strong>参加者が増えるほど、価格が上がる。</strong>初期のBaidu SEMは1クリック数セントでした。今では？業界によっては1クリック10〜50ドルです。AI広告も同じ運命をたどります。Doubaoの広告料金は時間とともに上昇する一方です。</p>',
    "<p><strong>If you rely only on paid traffic, your customer acquisition costs will keep rising and your margins will shrink.</strong></p>":
        '<p><strong>有料トラフィックだけに頼ると、顧客獲得コストは上昇し続け、利益率は縮小します。</strong></p>',
    '<h3>Organic traffic (GEO): long-term cost reduction</h3>':
        '<h3>オーガニックトラフィック（GEO）：長期的なコスト削減</h3>',
    "<p>GEO-generated organic traffic has a fixed cost — you invest upfront in content strategy, then earn AI recommendations ongoing. No recurring payment needed.</p>":
        '<p>GEOが生み出すオーガニックトラフィックには固定費用がかかります — コンテンツ戦略に先行投資すれば、その後は継続的にAIレコメンドを得られます。継続的な支払いは不要です。</p>',
    "<p><strong>Paid traffic gets you started. Organic traffic keeps costs under control. Remove either leg, and you won't go far.</strong></p>":
        '<p><strong>有料トラフィックでスタートし、オーガニックトラフィックでコストを抑える。どちらかの足を欠けば、遠くまで進めません。</strong></p>',

    # Section 3
    '<h2>The Earlier You Start, the Bigger the Advantage</h2>':
        '<h2>早く始めるほど、優位性は大きくなる</h2>',
    "<p>Here's a message every brand should hear:</p>":
        '<p>すべてのブランドが聞くべきメッセージ：</p>',
    "<p><strong>GEO's window of opportunity won't stay open forever.</strong></p>":
        '<p><strong>GEOのチャンスの窓は永遠に開いたままではありません。</strong></p>',
    '<p>Right now, AI search has no ads. All brand exposure comes from natural recommendations. If you do GEO, AI recommends you. The better your GEO, the deeper the recommendation.</p>':
        '<p>現時点では、AI検索に広告はありません。すべてのブランド露出は自然なレコメンドから来ています。GEOを実施すれば、AIがあなたを推奨します。GEOが優れているほど、レコメンドは深まります。</p>',
    "<p>At this stage, your acquisition cost is at its lowest.</p>":
        '<p>この段階では、獲得コストは最低水準です。</p>',
    '<h4>Three Windows Opening Now</h4>':
        '<h4>今まさに開いている3つの窓</h4>',
    '<li><strong>AI search habits are forming.</strong> More users are turning to Doubao, Qwen, and DeepSeek for research and decisions. But most brands are invisible in AI search — zero trust assets. <strong>Start now and you have almost no competition.</strong></li>':
        '<li><strong>AI検索習慣が形成されています。</strong>多くのユーザーが調査や意思決定にDoubao、Qwen、DeepSeekを利用し始めています。しかしほとんどのブランドはAI検索で見えていません — 信頼資産はゼロです。<strong>今始めれば、競合はほぼいません。</strong></li>',
    "<li><strong>AI ad systems haven't launched yet.</strong> All natural recommendation traffic is free today. Once ads launch, organic share will be squeezed. <strong>Doing GEO now is like \"free-riding\" AI recommendations before ads arrive.</strong></li>":
        '<li><strong>AI広告システムはまだ開始されていません。</strong>現在の自然レコメンドトラフィックはすべて無料です。広告が開始されれば、オーガニックのシェアは圧迫されます。<strong>今GEOを始めることは、広告が来る前にAIレコメンドに「ただ乗り」するようなものです。</strong></li>',
    '<li><strong>AI search rules are still being written.</strong> Google just defined GEO\'s core rule last month: information value is key, AI-generated fluff will be filtered. Early movers have disproportionate influence in shaping the rules.</li>':
        '<li><strong>AI検索のルールはまだ策定中です。</strong>Googleは先月、GEOのコアルールを定義しました：情報価値が鍵であり、AI生成の薄っぺらなコンテンツは除外されます。先発者はルール形成において不均衡な影響力を持ちます。</li>',
    "<p>By the time AI ads launch and competitors flood in, costs will have multiplied. But if you start today?</p>":
        '<p>AI広告が開始され、競合が殺到する頃には、コストは何倍にもなっているでしょう。しかし今始めたらどうでしょうか？</p>',
    '<p>Your trust assets are already built. AI is already recommending you. Competitors will spend big on ads to compete for position, while you earn free recommendations through GEO.</p>':
        '<p>あなたの信頼資産はすでに構築されています。AIはすでにあなたを推奨しています。競合が広告に巨額を投じてポジションを争う一方、あなたはGEOを通じて無料のレコメンドを得られます。</p>',
    "<p><strong>That's the value of \"early.\" Not cheap — early.</strong></p>":
        '<p><strong>それが「早さ」の価値です。「安い」ではなく「早い」のです。</strong></p>',
    '<p>The last time three windows opened simultaneously was 2015 (WeChat official accounts) and 2010 (SEO). <strong>Each new traffic system\'s golden period only belongs to those who run in first.</strong></p>':
        '<p>3つの窓が同時に開いた前回は2015年（WeChat公式アカウント）と2010年（SEO）でした。<strong>新しいトラフィックシステムの黄金期は、最初に駆け込んだ者だけのものです。</strong></p>',

    # Section 4
    '<h2>Walk on Two Legs: Paid + Organic</h2>':
        '<h2>二本足で歩く：有料＋オーガニック</h2>',
    "<h3>1. Start GEO now — don't wait for ads to launch</h3>":
        '<h3>1. 今すぐGEOを始める — 広告開始を待たない</h3>',
    "<p>By the time you see competitors being recommended in AI search, it's already too late. Trust assets take 3-6 months to accumulate. Start today, and you'll see results by the end of the year.</p>":
        '<p>競合がAI検索でレコメンドされているのを見た時には、すでに手遅れです。信頼資産の蓄積には3〜6ヶ月かかります。今日始めれば、年末までに結果が見えます。</p>',
    '<h3>2. When AI ads launch, invest in both channels</h3>':
        '<h3>2. AI広告が開始されたら、両方のチャネルに投資する</h3>',
    "<p>AI ads are a powerful rapid acquisition tool, especially for high-intent scenarios where conversion rates far exceed traditional feeds. But don't put all your budget on ads — reserve some for GEO to keep long-term costs low.</p>":
        '<p>AI広告は強力な迅速獲得ツールです。特にコンバージョン率が従来のフィードをはるかに超える高意図シナリオで効果的です。しかし予算をすべて広告に投じないでください — 長期的なコストを低く抑えるために、一部をGEOに確保しましょう。</p>',
    "<h3>3. Use GEO data to guide ad targeting</h3>":
        '<h3>3. GEOデータを活用して広告ターゲティングを最適化する</h3>',
    "<p>The scenarios and keywords where GEO performs well are your most precise ad targets. <strong>Organic traffic tells you where users are and what they're asking. Paid traffic helps you scale those scenarios fast.</strong></p>":
        '<p>GEOが効果を発揮するシナリオやキーワードこそ、最も精密な広告ターゲットです。<strong>オーガニックトラフィックはユーザーの居場所と質問を教えてくれます。有料トラフィックはそれらのシナリオを迅速に拡大します。</strong></p>',
    "<p><strong>First, use GEO to map the battlefield. Then, deploy ads for precision strikes.</strong></p>":
        '<p><strong>まずGEOで戦場を把握し、その後広告で精密攻撃を仕掛けましょう。</strong></p>',

    # Section 5 - Bottom Line
    '<h2>The Bottom Line</h2>':
        '<h2>結論</h2>',
    "<p><strong>Doubao launching ads isn't the end of GEO — it's GEO's accelerator.</strong></p>":
        '<p><strong>Doubaoの広告開始はGEOの終わりではなく、GEOの加速装置です。</strong></p>',
    "<p>When ads launch, AI search traffic will explode — more people using it, using it more deeply, relying on it for decisions. <strong>The more people use AI, the more valuable brands recommended by AI become.</strong></p>":
        '<p>広告が開始されれば、AI検索トラフィックは爆発的に増加します — より多くの人が利用し、より深く使い、意思決定に頼るようになります。<strong>AIを使う人が増えれば増えるほど、AIに推奨されるブランドの価値は高まります。</strong></p>',
    '<p>And AI recommends you not through ad spend, but through <strong>trust assets</strong>.</p>':
        '<p>そして、AIがあなたを推奨するのは広告費によるものではなく、<strong>信頼資産</strong>によるものです。</p>',
    '<p>Paid traffic helps you scale. Organic traffic keeps costs under control. <strong>Walk on two legs to run far in the AI marketing era.</strong></p>':
        '<p>有料トラフィックは拡大を助け、オーガニックトラフィックはコストを抑制します。<strong>AIマーケティング時代を遠くまで走るには、二本足で歩きましょう。</strong></p>',
    '<h3>Ready to build your AI trust assets?</h3>':
        '<h3>AI信頼資産の構築を始めませんか？</h3>',
    "<p>At TMG, we help international brands establish GEO presence in China's AI search ecosystem. From content strategy to implementation, we'll make sure you're visible where it matters.</p>":
        '<p>TMGでは、国際ブランドが中国のAI検索エコシステムでGEOプレゼンスを確立するのを支援しています。コンテンツ戦略から実装まで、重要な場所で可視化されるよう確実にお手伝いします。</p>',
    '<p><a href="/ja/contact/" class="btn btn--primary">Get in touch →</a></p>':
        '<p><a href="/ja/contact/" class="btn btn--primary">お問い合わせ →</a></p>',

    # Sidebar TOC
    '<div class="toc__title">In This Article</div>':
        '<div class="toc__title">目次</div>',
    '<li><a class="toc__link" href="#every-medium-two-traffic-types">Two Types of Traffic</a></li>':
        '<li><a class="toc__link" href="#every-medium-two-traffic-types">2種類のトラフィック</a></li>',
    '<li><a class="toc__link" href="#paid-scales-organic-saves">Paid vs Organic</a></li>':
        '<li><a class="toc__link" href="#paid-scales-organic-saves">有料 vs オーガニック</a></li>',
    '<li><a class="toc__link" href="#early-mover-advantage">First Mover Advantage</a></li>':
        '<li><a class="toc__link" href="#early-mover-advantage">先発者の優位性</a></li>',
    '<li><a class="toc__link" href="#walk-on-two-legs">Two-Leg Strategy</a></li>':
        '<li><a class="toc__link" href="#walk-on-two-legs">二本足戦略</a></li>',
    '<li><a class="toc__link" href="#bottom-line">Bottom Line</a></li>':
        '<li><a class="toc__link" href="#bottom-line">結論</a></li>',

    # Sidebar CTA
    '<p>Doubao\'s 140M+ DAU just signaled that AI discovery is a permanent channel. Is your brand ready?</p>':
        '<p>Doubaoの1.4億+ DAUは、AIディスカバリーが恒久的なチャネルであることを示しています。あなたのブランドは準備できていますか？</p>',
    '<a href="https://www.tuyuesouxin.cn/geo/" class="btn btn--primary">Explore TMG GEO</a>':
        '<a href="https://www.tuyuesouxin.cn/ja/geo/" class="btn btn--primary">TMG GEOを詳しく見る</a>',

    # Related Posts
    '<div class="related__title">More from the Blog</div>':
        '<div class="related__title">関連記事</div>',
    '<div class="related-card__cat">GEO / Channel Strategy</div>':
        '<div class="related-card__cat">GEO / チャネル戦略</div>',
    '<div class="related-card__title">GEO Channel Weight 2026: Which Platforms Get the Most AI Traffic?</div>':
        '<div class="related-card__title">GEOチャネルウェイト2026：どのプラットフォームが最もAIトラフィックを得ているか？</div>',
    '<div class="related-card__cat">GEO / AI Search</div>':
        '<div class="related-card__cat">GEO / AI検索</div>',
    '<div class="related-card__title">Doubao Paid — What It Means for GEO Marketing</div>':
        '<div class="related-card__title">Doubao有料化 — GEOマーケティングへの影響</div>',
    '<div class="related-card__cat">Paid Media / Strategy</div>':
        '<div class="related-card__cat">有料メディア / 戦略</div>',
    '<div class="related-card__title">CPM Is Rising — Is That Really a Bad Thing?</div>':
        '<div class="related-card__title">CPM上昇 — 本当に悪いことなのか？</div>',

    # Footer text
    '<h4 class="footer__title">About TMG</h4>':
        '<h4 class="footer__title">TMGについて</h4>',
    '<p class="footer__description">\n            Your single point of access to China\'s $100B digital advertising market. We help international agencies navigate Chinese platforms with ease.\n          </p>':
        '<p class="footer__description">\n            中国の1000億ドル規模のデジタル広告市場への単一アクセスポイント。国際的なエージェンシーが中国のプラットフォームを簡単にナビゲートできるよう支援します。\n          </p>',
    '<h4 class="footer__title">Quick Links</h4>':
        '<h4 class="footer__title">クイックリンク</h4>',
    '<li><a href="https://www.tuyuesouxin.cn/ja/services/" class="footer__link">Services</a></li>':
        '<li><a href="https://www.tuyuesouxin.cn/ja/services/" class="footer__link">サービス</a></li>',
    '<li><a href="https://www.tuyuesouxin.cn/ja/pricing/" class="footer__link">Pricing</a></li>':
        '<li><a href="https://www.tuyuesouxin.cn/ja/pricing/" class="footer__link">料金</a></li>',
    '<li><a href="https://www.tuyuesouxin.cn/ja/about/" class="footer__link">About Us</a></li>':
        '<li><a href="https://www.tuyuesouxin.cn/ja/about/" class="footer__link">会社概要</a></li>',
    '<li><a href="https://www.tuyuesouxin.cn/ja/client-stories" class="footer__link">Client Stories</a></li>':
        '<li><a href="https://www.tuyuesouxin.cn/ja/client-stories" class="footer__link">導入事例</a></li>',
    '<li><a href="https://www.tuyuesouxin.cn/ja/faqs" class="footer__link">FAQ</a></li>':
        '<li><a href="https://www.tuyuesouxin.cn/ja/faqs" class="footer__link">FAQ</a></li>',
    '<h4 class="footer__title">Contact</h4>':
        '<h4 class="footer__title">お問い合わせ</h4>',
    '<h4 class="footer__title">Legal</h4>':
        '<h4 class="footer__title">法的情報</h4>',
    '<p class="footer__copyright">© 2026 Tuyue Media Gateway. All rights reserved.</p>':
        '<p class="footer__copyright">© 2026 Tuyue Media Gateway. All rights reserved.</p>',
}

# ─── Korean Translations ───

ko_translations = {
    # Hero
    '<span>Doubao</span> Added Ads — Is <span>GEO</span> Still Worth It?':
        '<span>Doubao</span>에 광고 등장 — <span>GEO</span>는 여전히 필요할까?',
    '<p class="article-hero__intro">Doubao (ByteDance AI) has started running ads. Many are asking: is GEO still worth it? The short answer: yes — and more than ever. Here\'s why paid and natural AI traffic work together.</p>':
        '<p class="article-hero__intro">Doubao(ByteDance AI)가 광고 게재를 시작했습니다. 많은 분들이 "GEO가 여전히 의미가 있을까?"라고 묻고 있습니다. 답은 간단합니다. **네, 그리고 그 어느 때보다 중요합니다**. 유료 트래픽과 자연 AI 트래픽이 어떻게 함께 작동하는지 그 이유를 설명드립니다.</p>',

    # Article body - Section 1
    '<h2>Every Medium Has Two Types of Traffic</h2>':
        '<h2>모든 미디어에는 두 가지 유형의 트래픽이 있다</h2>',
    "<p>Let's go back to basics:</p>":
        '<p>기본으로 돌아가 봅시다:</p>',
    '<p>In every media era, there are two kinds of traffic — <strong>organic</strong> and <strong>paid</strong>.</p>':
        '<p>모든 미디어 시대에는 <strong>오가닉</strong>과 <strong>유료</strong>라는 두 가지 유형의 트래픽이 있습니다.</p>',
    '<li><strong>Search era:</strong> SEO was organic, SEM was paid.</li>':
        '<li><strong>검색 시대:</strong> SEO가 오가닉, SEM이 유료였습니다.</li>',
    '<li><strong>WeChat era:</strong> Content growth was organic, ad spend was paid.</li>':
        '<li><strong>WeChat 시대:</strong> 콘텐츠 성장이 오가닉, 광고비가 유료였습니다.</li>',
    '<li><strong>Douyin era:</strong> Video recommendations were organic, DOU+ and feed ads were paid.</li>':
        '<li><strong>Douyin 시대:</strong> 동영상 추천이 오가닉, DOU+와 피드 광고가 유료였습니다.</li>',
    '<li><strong>AI Search era:</strong> <strong>GEO is organic, AI ads are paid.</strong></li>':
        '<li><strong>AI 검색 시대:</strong> <strong>GEO가 오가닉, AI 광고가 유료입니다.</strong></li>',
    '<p>The logic has never changed.</p>':
        '<p>이 구조는 결코 변하지 않았습니다.</p>',
    '<p>When Baidu launched SEM ads, did companies stop doing SEO? No. They ran SEM for immediate traffic while building SEO as a long-term asset.</p>':
        '<p>Baidu가 SEM 광고를 시작했을 때, 기업들은 SEO를 중단했을까요? 아닙니다. 그들은 SEM으로 즉각적인 트래픽을 확보하면서 SEO를 장기 자산으로 구축했습니다.</p>',
    '<h4>Key Principle</h4>':
        '<h4>핵심 원칙</h4>',
    '<p><strong>Paid traffic is rented — stop paying, it vanishes. Organic traffic is an asset — nobody can take it away.</strong></p>':
        '<p><strong>유료 트래픽은 임대입니다 — 지불을 중단하면 사라집니다. 오가닉 트래픽은 자산입니다 — 아무도 빼앗을 수 없습니다.</strong></p>',
    '<p>The same logic applies to AI search. You will be able to buy Doubao ads for instant exposure, but the trust assets you build through GEO will keep generating free AI recommendations day after day.</p>':
        '<p>동일한 논리가 AI 검색에도 적용됩니다. Doubao 광고를 구매하여 즉각적인 노출을 얻을 수 있지만, GEO를 통해 구축한 신뢰 자산은 매일 무료 AI 추천을 계속 생성합니다.</p>',
    '<p><strong>You need both legs to walk.</strong></p>':
        '<p><strong>걷기 위해서는 두 다리가 필요합니다.</strong></p>',

    # Section 2
    '<h2>Paid Traffic Scales Results — Organic Traffic Cuts Costs</h2>':
        '<h2>유료 트래픽은 결과를 확대하고, 오가닉 트래픽은 비용을 절감한다</h2>',
    '<p>Paid traffic and organic traffic serve completely different roles.</p>':
        '<p>유료 트래픽과 오가닉 트래픽은 완전히 다른 역할을 수행합니다.</p>',
    '<div class="stat-card__label">ChatGPT ad CPC</div>':
        '<div class="stat-card__label">ChatGPT 광고 CPC</div>',
    '<div class="stat-card__label">ChatGPT CPM (3x more than Meta)</div>':
        '<div class="stat-card__label">ChatGPT CPM(Meta의 3배)</div>',
    '<div class="stat-card__label">Months for GEO trust assets to build</div>':
        '<div class="stat-card__label">GEO 신뢰 자산 구축 기간(개월)</div>',
    '<h3>Paid traffic: short-term scaling</h3>':
        '<h3>유료 트래픽: 단기적 확장</h3>',
    "<p>You spend ad dollars today, you see traffic tomorrow. ChatGPT's CPC is $3-5, and Doubao's ad pricing won't be cheap either. But paid traffic lets you:</p>":
        '<p>오늘 광고비를 투자하면 내일 트래픽을 볼 수 있습니다. ChatGPT의 CPC는 3~5달러이며, Doubao의 광고 요금도 저렴하지 않을 것입니다. 하지만 유료 트래픽은 다음과 같은 이점을 제공합니다:</p>',
    '<li>Test markets quickly</li>':
        '<li>시장을 빠르게 테스트</li>',
    '<li>Acquire leads fast</li>':
        '<li>리드를 신속하게 확보</li>',
    '<li>Validate products immediately</li>':
        '<li>제품을 즉시 검증</li>',
    "<p>For companies with budget, AI advertising will become a critical acquisition channel — a new traffic gateway, a new growth curve. <strong>Whoever figures it out first wins.</strong></p>":
        '<p>예산이 있는 기업에게 AI 광고는 중요한 획득 채널이 될 것입니다 — 새로운 트래픽 관문, 새로운 성장 곡선입니다.<strong>가장 먼저 활용하는 자가 승리합니다.</strong></p>',
    '<h4>The Hidden Cost of Paid Traffic</h4>':
        '<h4>유료 트래픽의 숨은 비용</h4>',
    "<p>Bidding ads have a fundamental flaw: <strong>the more participants, the higher the price.</strong> Early Baidu SEM cost pennies per click. Today? Some industries pay $10-50 per click. The same will happen with AI ads. Doubao ad prices will only go up over time.</p>":
        '<p>입찰형 광고에는 근본적인 결함이 있습니다: <strong>참여자가 많을수록 가격이 올라갑니다.</strong> 초기 Baidu SEM은 클릭당 몇 센트였습니다. 지금은요? 일부 업종은 클릭당 10~50달러를 지불합니다. AI 광고도 같은 운명을 겪을 것입니다. Doubao의 광고 요금은 시간이 지날수록 상승할 것입니다.</p>',
    "<p><strong>If you rely only on paid traffic, your customer acquisition costs will keep rising and your margins will shrink.</strong></p>":
        '<p><strong>유료 트래픽에만 의존하면 고객 획득 비용은 계속 상승하고 마진은 줄어들 것입니다.</strong></p>',
    '<h3>Organic traffic (GEO): long-term cost reduction</h3>':
        '<h3>오가닉 트래픽(GEO): 장기적 비용 절감</h3>',
    "<p>GEO-generated organic traffic has a fixed cost — you invest upfront in content strategy, then earn AI recommendations ongoing. No recurring payment needed.</p>":
        '<p>GEO가 생성하는 오가닉 트래픽에는 고정 비용이 있습니다 — 콘텐츠 전략에 선행 투자하면 지속적으로 AI 추천을 얻을 수 있습니다. 반복 지불은 필요 없습니다.</p>',
    "<p><strong>Paid traffic gets you started. Organic traffic keeps costs under control. Remove either leg, and you won't go far.</strong></p>":
        '<p><strong>유료 트래픽으로 시작하고, 오가닉 트래픽으로 비용을 통제하세요. 한쪽 다리를 빼면 멀리 갈 수 없습니다.</strong></p>',

    # Section 3
    '<h2>The Earlier You Start, the Bigger the Advantage</h2>':
        '<h2>일찍 시작할수록, 이점은 커진다</h2>',
    "<p>Here's a message every brand should hear:</p>":
        '<p>모든 브랜드가 들어야 할 메시지:</p>',
    "<p><strong>GEO's window of opportunity won't stay open forever.</strong></p>":
        '<p><strong>GEO의 기회의 창은 영원히 열려 있지 않습니다.</strong></p>',
    '<p>Right now, AI search has no ads. All brand exposure comes from natural recommendations. If you do GEO, AI recommends you. The better your GEO, the deeper the recommendation.</p>':
        '<p>현재 AI 검색에는 광고가 없습니다. 모든 브랜드 노출은 자연 추천에서 비롯됩니다. GEO를 실시하면 AI가 당신을 추천합니다. GEO가 좋을수록 추천은 더 깊어집니다.</p>',
    "<p>At this stage, your acquisition cost is at its lowest.</p>":
        '<p>이 단계에서는 획득 비용이 최저 수준입니다.</p>',
    '<h4>Three Windows Opening Now</h4>':
        '<h4>지금 열리고 있는 세 개의 창</h4>',
    '<li><strong>AI search habits are forming.</strong> More users are turning to Doubao, Qwen, and DeepSeek for research and decisions. But most brands are invisible in AI search — zero trust assets. <strong>Start now and you have almost no competition.</strong></li>':
        '<li><strong>AI 검색 습관이 형성되고 있습니다.</strong>越来越多的用户正在转向 Doubao、Qwen 和 DeepSeek 进行研究和决策。하지만 대부분의 브랜드는 AI 검색에서 보이지 않습니다 — 신뢰 자산이 제로입니다.<strong>지금 시작하면 경쟁자가 거의 없습니다.</strong></li>',
    "<li><strong>AI ad systems haven't launched yet.</strong> All natural recommendation traffic is free today. Once ads launch, organic share will be squeezed. <strong>Doing GEO now is like \"free-riding\" AI recommendations before ads arrive.</strong></li>":
        '<li><strong>AI 광고 시스템은 아직 시작되지 않았습니다.</strong>현재의 자연 추천 트래픽은 모두 무료입니다. 광고가 시작되면 오가닉 점유율은 압박을 받을 것입니다.<strong>지금 GEO를 하는 것은 광고가 도착하기 전에 AI 추천에 "무임승차"하는 것과 같습니다.</strong></li>',
    '<li><strong>AI search rules are still being written.</strong> Google just defined GEO\'s core rule last month: information value is key, AI-generated fluff will be filtered. Early movers have disproportionate influence in shaping the rules.</li>':
        '<li><strong>AI 검색 규칙은 아직 작성 중입니다.</strong>Google은 지난달 GEO의 핵심 규칙을 정의했습니다: 정보 가치가 핵심이며, AI 생성 얇은 콘텐츠는 필터링됩니다. 선발 주자는 규칙 형성에 불균형적인 영향력을 행사합니다.</li>',
    "<p>By the time AI ads launch and competitors flood in, costs will have multiplied. But if you start today?</p>":
        '<p>AI 광고가 시작되고 경쟁자들이 몰려들 때쯤이면 비용은 몇 배로 늘어날 것입니다. 하지만 지금 시작한다면?</p>',
    '<p>Your trust assets are already built. AI is already recommending you. Competitors will spend big on ads to compete for position, while you earn free recommendations through GEO.</p>':
        '<p>당신의 신뢰 자산은 이미 구축되어 있습니다. AI는 이미 당신을 추천하고 있습니다. 경쟁자들은 위치 선점을 위해 광고에 막대한 비용을 쏟아부을 것이지만, 당신은 GEO를 통해 무료 추천을 얻습니다.</p>',
    "<p><strong>That's the value of \"early.\" Not cheap — early.</strong></p>":
        '<p><strong>それが「早さ」の価値です。「安い」ではなく「早い」のです。</strong></p>',
    '<p>The last time three windows opened simultaneously was 2015 (WeChat official accounts) and 2010 (SEO). <strong>Each new traffic system\'s golden period only belongs to those who run in first.</strong></p>':
        '<p>세 개의 창이 동시에 열린 마지막 때는 2015년(WeChat 공식 계정)과 2010년(SEO)이었습니다.<strong>새로운 트래픽 시스템의 황금기는 먼저 뛰어든 자의 몫입니다.</strong></p>',

    # Section 4
    '<h2>Walk on Two Legs: Paid + Organic</h2>':
        '<h2>두 다리로 걷기: 유료 + 오가닉</h2>',
    "<h3>1. Start GEO now — don't wait for ads to launch</h3>":
        '<h3>1. 지금 GEO를 시작하세요 — 광고 시작을 기다리지 마세요</h3>',
    "<p>By the time you see competitors being recommended in AI search, it's already too late. Trust assets take 3-6 months to accumulate. Start today, and you'll see results by the end of the year.</p>":
        '<p>경쟁자가 AI 검색에서 추천되는 것을 보는 때는 이미 늦었습니다. 신뢰 자산이 축적되는 데는 3~6개월이 걸립니다. 오늘 시작하면 연말까지 결과를 볼 수 있습니다.</p>',
    '<h3>2. When AI ads launch, invest in both channels</h3>':
        '<h3>2. AI 광고가 시작되면 두 채널에 모두 투자하세요</h3>',
    "<p>AI ads are a powerful rapid acquisition tool, especially for high-intent scenarios where conversion rates far exceed traditional feeds. But don't put all your budget on ads — reserve some for GEO to keep long-term costs low.</p>":
        '<p>AI 광고는 강력한 신속 획득 도구입니다. 특히 전환율이 기존 피드를 크게 웃도는 고의도 시나리오에서 효과적입니다. 하지만 예산을 모두 광고에 투입하지 마세요 — 장기 비용을 낮게 유지하기 위해 일부를 GEO에 할당하세요.</p>',
    "<h3>3. Use GEO data to guide ad targeting</h3>":
        '<h3>3. GEO 데이터를 활용하여 광고 타겟팅 최적화</h3>',
    "<p>The scenarios and keywords where GEO performs well are your most precise ad targets. <strong>Organic traffic tells you where users are and what they're asking. Paid traffic helps you scale those scenarios fast.</strong></p>":
        '<p>GEO가 효과를 발휘하는 시나리오와 키워드야말로 가장 정밀한 광고 타겟입니다.<strong>오가닉 트래픽은 사용자의 위치와 질문을 알려줍니다. 유료 트래픽은 이러한 시나리오를 빠르게 확장합니다.</strong></p>',
    "<p><strong>First, use GEO to map the battlefield. Then, deploy ads for precision strikes.</strong></p>":
        '<p><strong>먼저 GEO로 전장을 파악하고, 그다음 광고로 정밀 타격을 가하세요.</strong></p>',

    # Section 5 - Bottom Line
    '<h2>The Bottom Line</h2>':
        '<h2>결론</h2>',
    "<p><strong>Doubao launching ads isn't the end of GEO — it's GEO's accelerator.</strong></p>":
        '<p><strong>Doubao의 광고 출시는 GEO의 종말이 아니라 GEO의 가속 장치입니다.</strong></p>',
    "<p>When ads launch, AI search traffic will explode — more people using it, using it more deeply, relying on it for decisions. <strong>The more people use AI, the more valuable brands recommended by AI become.</strong></p>":
        '<p>광고가 시작되면 AI 검색 트래픽은 폭발적으로 증가합니다 — 더 많은 사람들이 사용하고, 더 깊이 활용하며, 의사 결정에 의존하게 됩니다.<strong>AI를 사용하는 사람이 많을수록 AI가 추천하는 브랜드의 가치는 높아집니다.</strong></p>',
    '<p>And AI recommends you not through ad spend, but through <strong>trust assets</strong>.</p>':
        '<p>그리고 AI가 당신을 추천하는 것은 광고비 때문이 아니라 <strong>신뢰 자산</strong> 때문입니다.</p>',
    '<p>Paid traffic helps you scale. Organic traffic keeps costs under control. <strong>Walk on two legs to run far in the AI marketing era.</strong></p>':
        '<p>유료 트래픽은 확장을 돕고, 오가닉 트래픽은 비용을 통제합니다.<strong>AI 마케팅 시대를 멀리 달리려면 두 다리로 걸으세요.</strong></p>',
    '<h3>Ready to build your AI trust assets?</h3>':
        '<h3>AI 신뢰 자산 구축을 준비하셨나요?</h3>',
    "<p>At TMG, we help international brands establish GEO presence in China's AI search ecosystem. From content strategy to implementation, we'll make sure you're visible where it matters.</p>":
        '<p>TMG는 국제 브랜드가 중국의 AI 검색 생태계에서 GEO 입지를 구축하도록 지원합니다. 콘텐츠 전략부터 구현까지, 중요한 곳에서 가시성을 확보할 수 있도록 도와드립니다.</p>',
    '<p><a href="/ko/contact/" class="btn btn--primary">Get in touch →</a></p>':
        '<p><a href="/ko/contact/" class="btn btn--primary">문의하기 →</a></p>',

    # Sidebar TOC
    '<div class="toc__title">In This Article</div>':
        '<div class="toc__title">목차</div>',
    '<li><a class="toc__link" href="#every-medium-two-traffic-types">Two Types of Traffic</a></li>':
        '<li><a class="toc__link" href="#every-medium-two-traffic-types">두 가지 트래픽 유형</a></li>',
    '<li><a class="toc__link" href="#paid-scales-organic-saves">Paid vs Organic</a></li>':
        '<li><a class="toc__link" href="#paid-scales-organic-saves">유료 vs 오가닉</a></li>',
    '<li><a class="toc__link" href="#early-mover-advantage">First Mover Advantage</a></li>':
        '<li><a class="toc__link" href="#early-mover-advantage">선발주자 이점</a></li>',
    '<li><a class="toc__link" href="#walk-on-two-legs">Two-Leg Strategy</a></li>':
        '<li><a class="toc__link" href="#walk-on-two-legs">두 다리 전략</a></li>',
    '<li><a class="toc__link" href="#bottom-line">Bottom Line</a></li>':
        '<li><a class="toc__link" href="#bottom-line">결론</a></li>',

    # Sidebar CTA
    "<p>Doubao's 140M+ DAU just signaled that AI discovery is a permanent channel. Is your brand ready?</p>":
        '<p>Doubao의 1.4억+ DAU는 AI 디스커버리가 영구적인 채널임을 알리고 있습니다. 귀하의 브랜드는 준비되었나요?</p>',
    '<a href="https://www.tuyuesouxin.cn/geo/" class="btn btn--primary">Explore TMG GEO</a>':
        '<a href="https://www.tuyuesouxin.cn/ko/geo/" class="btn btn--primary">TMG GEO 살펴보기</a>',

    # Related Posts
    '<div class="related__title">More from the Blog</div>':
        '<div class="related__title">관련 글</div>',
    '<div class="related-card__cat">GEO / Channel Strategy</div>':
        '<div class="related-card__cat">GEO / 채널 전략</div>',
    '<div class="related-card__title">GEO Channel Weight 2026: Which Platforms Get the Most AI Traffic?</div>':
        '<div class="related-card__title">GEO 채널 가중치 2026: 어떤 플랫폼이 가장 많은 AI 트래픽을 얻을까?</div>',
    '<div class="related-card__cat">GEO / AI Search</div>':
        '<div class="related-card__cat">GEO / AI 검색</div>',
    '<div class="related-card__title">Doubao Paid — What It Means for GEO Marketing</div>':
        '<div class="related-card__title">Doubao 유료화 — GEO 마케팅에 미치는 영향</div>',
    '<div class="related-card__cat">Paid Media / Strategy</div>':
        '<div class="related-card__cat">유료 미디어 / 전략</div>',
    '<div class="related-card__title">CPM Is Rising — Is That Really a Bad Thing?</div>':
        '<div class="related-card__title">CPM 상승 — 정말 나쁜 일일까?</div>',

    # Footer text
    '<h4 class="footer__title">About TMG</h4>':
        '<h4 class="footer__title">TMG 소개</h4>',
    '<p class="footer__description">\n            Your single point of access to China\'s $100B digital advertising market. We help international agencies navigate Chinese platforms with ease.\n          </p>':
        '<p class="footer__description">\n            중국 1000억 달러 디지털 광고 시장으로의 단일 액세스 포인트. 국제 에이전시가 중국 플랫폼을 쉽게 탐색할 수 있도록 지원합니다.\n          </p>',
    '<h4 class="footer__title">Quick Links</h4>':
        '<h4 class="footer__title">빠른 링크</h4>',
    '<li><a href="https://www.tuyuesouxin.cn/ko/services/" class="footer__link">Services</a></li>':
        '<li><a href="https://www.tuyuesouxin.cn/ko/services/" class="footer__link">서비스</a></li>',
    '<li><a href="https://www.tuyuesouxin.cn/ko/pricing/" class="footer__link">Pricing</a></li>':
        '<li><a href="https://www.tuyuesouxin.cn/ko/pricing/" class="footer__link">요금제</a></li>',
    '<li><a href="https://www.tuyuesouxin.cn/ko/about/" class="footer__link">About Us</a></li>':
        '<li><a href="https://www.tuyuesouxin.cn/ko/about/" class="footer__link">회사 소개</a></li>',
    '<li><a href="https://www.tuyuesouxin.cn/ko/client-stories" class="footer__link">Client Stories</a></li>':
        '<li><a href="https://www.tuyuesouxin.cn/ko/client-stories" class="footer__link">고객 사례</a></li>',
    '<li><a href="https://www.tuyuesouxin.cn/ko/faqs" class="footer__link">FAQ</a></li>':
        '<li><a href="https://www.tuyuesouxin.cn/ko/faqs" class="footer__link">FAQ</a></li>',
    '<h4 class="footer__title">Contact</h4>':
        '<h4 class="footer__title">연락처</h4>',
    '<h4 class="footer__title">Legal</h4>':
        '<h4 class="footer__title">법적 정보</h4>',
    '<p class="footer__copyright">© 2026 Tuyue Media Gateway. All rights reserved.</p>':
        '<p class="footer__copyright">© 2026 Tuyue Media Gateway. All rights reserved.</p>',
}

# ─── Execute ───
base = os.path.dirname(os.path.abspath(__file__))

ja_file = os.path.join(base, 'ja', 'blog', 'doubao-ads-geo-still-worth-it.html')
ko_file = os.path.join(base, 'ko', 'blog', 'doubao-ads-geo-still-worth-it.html')

print("=== Translating JA ===")
result_ja = translate_file(ja_file, ja_translations)
print(f"JA modified: {result_ja}")

print("\n=== Translating KO ===")
result_ko = translate_file(ko_file, ko_translations)
print(f"KO modified: {result_ko}")

print("\nDone!")
