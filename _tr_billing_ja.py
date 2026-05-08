# -*- coding: utf-8 -*-
"""JA translation: ad-billing-models-explained.html"""
import os, re

BASE = os.path.dirname(os.path.abspath(__file__))
fp = os.path.join(BASE, 'ja', 'blog', 'ad-billing-models-explained.html')

with open(fp, 'r', encoding='utf-8') as f:
    content = f.read()

# Meta tags
content = content.replace(
    '<title>Ad Billing Models Explained: CPM, CPC, CPA, oCPM and When to Use Each | Tuyue Media Gateway (TMG)</title>',
    '<title>広告課金モデル解説：CPM、CPC、CPA、oCPMとそれぞれの使い分け | Tuyue Media Gateway (TMG)</title>')
content = content.replace(
    '<meta name="description" content="A practical guide to ad billing models in paid media: CPM, CPC, CPA, oCPM and more. Learn which pricing model fits your campaign goals and how to avoid burning budget on the wrong one.">',
    '<meta name="description" content="有料メディアの広告課金モデル実践ガイド：CPM、CPC、CPA、oCPMなど。キャンペーン目標に合った課金モデルの選び方と、間違った選択で予算を浪費しない方法を解説します。">')

# Replace article body (using positional replacement)
start_marker = '  <article class="article-body">\n    \n'
end_marker = '\n  </article>\n  \n  <!-- Related Posts -->'

idx_s = content.find(start_marker)
idx_e = content.find(end_marker, idx_s)

if idx_s < 0 or idx_e < 0:
    print('ERROR: boundaries not found', idx_s, idx_e)
    exit(1)

body_ja = '''    <p class="emoji-lead">💰</p>
    <p>
      キャンペーン設定画面を見つめながら、「CPMで入札すべきか、CPCがいいのか、それともoCPMというものなのか」と悩んだことがある方も多いはずです。Baidu、Douyin、WeChat、小紅書、Bilibili、Bing Chinaで7桁規模の有料メディア予算を運用してきたTMGの経験から言えることは、間違った課金モデルが静かに予算を消耗させることも、正しいモデルが結果を劇的に変えることもあるということです。
    </p>
    
    <p>
      具体的なモデルに入る前に、まず押さえておくべき2つの概念があります。第一に、<strong>広告課金モデルと広告タイプは同じではありません</strong>が、課金モデルによって利用可能な広告タイプが決まります。第二に、<strong>選択する課金モデルによって、広告プラットフォームのアルゴリズムが広告をどのように優先するかが決まります</strong>。間違った選択をすると、間違った成果に対して支払うことになります。
    </p>
    
    <div class="callout callout--info">
      <div class="callout__title">📊 2つの大きなカテゴリ</div>
      <div class="callout__text">
        有料メディアでは、一般的にキャンペーンを<strong>ブランド広告</strong>（認知度重視）と<strong>パフォーマンス広告</strong>（コンバージョン重視）に分けます。選ぶ課金モデルはカテゴリに合わせるべきで、その逆ではありません。
      </div>
    </div>
    
    <h2>🎯 ブランド広告：注目に対して支払う</h2>
    
    <p>
      ブランド広告とは<strong>見られること</strong>が目的です。今日のクリックや購入が目標ではなく、ブランドの想起、好意度、「最初に思い浮かべてもらう」ポジショニングが重要です。消費者がいずれあなたの商品を必要としたときに、最初にあなたのことを思い出してもらうためです。
    </p>
    
    <p>
      <strong>購入しているもの：</strong>インプレッション、視聴、人の目の前にいる時間。
    </p>
    
    <p>
      <strong>測定方法：</strong>インプレッション数、視聴完了率、エンゲージメント率、ブランド検索リフト、ブランド認知度調査。
    </p>
    
    <p>
      <strong>代表的なシナリオ：</strong>新製品ローンチ、ブランド再ポジショニング、祝祭日キャンペーン、カテゴリ所有権の確立。
    </p>
    
    <p>
      <strong>一言で：</strong>ブランド広告 = <em>人々に自分の存在を知ってもらうためにお金を払う</em>。
    </p>
    
    <h3>実際に出会うブランド課金モデル</h3>
    
    <h4>1. CPM（Cost Per Mille）— 1,000インプレッションあたりの支払い</h4>
    
    <p>
      これはクラシックなブランド広告課金モデルです。クリックの有無に関わらず、広告が1,000回表示されるごとに支払います。CPMはほとんどのディスプレイ、動画、SNS認知度キャンペーンのデフォルトです。
    </p>
    
    <div class="highlights-grid">
      <div class="highlight-card">
        <span class="highlight-card__icon">📈</span>
        <div class="highlight-card__title">仕組み</div>
        <div class="highlight-card__text">1,000インプレッションあたり固定レートで支払います。CPMが30円で100CPM（＝10万インプレッション）を購入した場合、コストは3,000円です。</div>
      </div>
      <div class="highlight-card">
        <span class="highlight-card__icon">⏱️</span>
        <div class="highlight-card__title">配信パターン</div>
        <div class="highlight-card__text">注文が確定すると、プラットフォームがインプレッション量をロックします。100CPMすべてが1時間で配信されることもあれば、1日かけて配信されることもあります — 在庫状況に基づいてプラットフォームが判断します。</div>
      </div>
      <div class="highlight-card">
        <span class="highlight-card__icon">✅</span>
        <div class="highlight-card__title">最適な用途</div>
        <div class="highlight-card__text">幅広い認知度向上、新市場参入、「見られること」が即時の反応よりも重要な製品のローンチ。</div>
      </div>
      <div class="highlight-card">
        <span class="highlight-card__icon">⚠️</span>
        <div class="highlight-card__title">注意点</div>
        <div class="highlight-card__text">CPMはインプレッションを保証しますが、注目を保証しません。広告がファーストビューの下やスクロールされやすい位置に表示されることもあります。可能であればCPMとビューアビリティ指標を組み合わせてください。</div>
      </div>
    </div>
    
    <h4>2. CPD（Cost Per Day）— 固定広告枠の日額支払い</h4>
    
    <p>
      CPDはシンプルです：デジタルハイウェイ上の看板を借りるようなものです。広告の表示回数や閲覧人数に関係なく、特定の広告枠に対して固定の日額を支払います。
    </p>
    
    <p>
      <strong>代表的な用途：</strong>スプラッシュ広告（アプリ起動時に表示される広告）、ホームページバナー、その他「配置保証型」の購入。
    </p>
    
    <p>
      <strong>トレードオフ：</strong>広告が<em>どこに</em>表示されるかは確実ですが、<em>何人に</em>見られるかは保証されません。「量ベース」ではなく「時間ベース」の購入です。
    </p>
    
    <h4>3. CPT（Cost Per Time）— 特定の時間枠に対する支払い</h4>
    
    <p>
      CPTはCPDのより細かいバージョンです。1日全体を購入するのではなく、特定の時間枠（例：金曜日の20時から22時）を購入します。デジタル動画プラットフォーム上のテレビ風広告で一般的です。
    </p>
    
    <p>
      <strong>重要ポイント：</strong>プライムタイム枠はコストが高いですが、より多くの人にリーチします。オーディエンスが予測可能な場合（例：全員が同じライブ配信を視聴する）、CPTを使えば一度に全員を捉えることができます。
    </p>
    
    <h4>4. CPV（Cost Per View）— 有効な動画視聴に対する支払い</h4>
    
    <p>
      CPVは、ユーザーが一定時間以上動画広告を視聴した場合にのみ課金されます。「有効な視聴」の定義はプラットフォームによって異なります：
    </p>
    
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>プラットフォーム</th>
            <th>有効視聴の定義</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>YouTube</td>
            <td>30秒以上（30秒未満の動画は全編）</td>
          </tr>
          <tr>
            <td>Douyin / Kuaishou / Bilibili</td>
            <td>3〜5秒以上</td>
          </tr>
          <tr>
            <td>長尺動画（iQiyi、Tencent Video等）</td>
            <td>プレロール広告の完了</td>
          </tr>
        </tbody>
      </table>
    </div>
    
    <p>
      CPVはCPMより高価です。なぜなら、0.3秒でスキップされたかもしれない単なるインプレッションではなく、<em>質の高い</em>注目に対して支払っているからです。
    </p>
    
    <h4>5. CPCV（Cost Per Completed View）— 全編視聴時のみ支払い</h4>
    
    <p>
      CPCVはCPVのより厳格な兄弟と考えてください。ユーザーが動画広告を<strong>最後まで</strong>視聴した場合にのみ支払います。スキップなし、部分的なクレジットなしです。
    </p>
    
    <p>
      <strong>使うべきタイミング：</strong>完全なメッセージが重要な高関与製品 — 自動車の発表、金融サービスの説明、プレミアムスキンケアライン。広告が15秒なら、15秒すべて見てもらいたいのです。
    </p>
    
    <div class="callout callout--tip">
      <div class="callout__title">💡 TMGチームからのプロのヒント</div>
      <div class="callout__text">
        ブランドキャンペーンでは、CPM（リーチ用）とCPVまたはCPCV（主要なローンチタイミング用）を組み合わせることがよくあります。ブランド予算を1つの課金モデルだけに集中させず、クリエイティブ形式とキャンペーンフェーズに合わせてモデルを使い分けてください。
      </div>
    </div>
    
    <h2>🚀 パフォーマンス広告：アクションに対して支払う</h2>
    
    <p>
      パフォーマンス広告はロジックを逆転させます。目玉に対して支払うのではなく、<strong>成果</strong>に対して支払います。クリック、ダウンロード、フォーム送信、購入。ユーザーがアクションを取らなければ、支払いは発生しません（または大幅に少なくなります）。
    </p>
    
    <p>
      <strong>購入しているもの：</strong>クリック、コンバージョン、売上、リード。
    </p>
    
    <p>
      <strong>測定方法：</strong>クリック率（CTR）、コンバージョン率（CVR）、顧客獲得単価（CPA）、広告費用対効果（ROAS）。
    </p>
    
    <p>
      <strong>代表的なシナリオ：</strong>ECプロモーション、アプリユーザー獲得、リードジェネレーション、ダイレクトレスポンスキャンペーン。
    </p>
    
    <p>
      <strong>一言で：</strong>パフォーマンス広告 = <em>人々が何かをするためにお金を払う</em>。
    </p>
    
    <h3>実際に効果を発揮するパフォーマンス課金モデル</h3>
    
    <h4>1. CPC（Cost Per Click）— クリックごとの支払い</h4>
    
    <p>
      CPCはその名の通り：誰かが広告をクリックしたときだけ支払います。インプレッションは無料で、クリックがコストを発生させます。
    </p>
    
    <p>
      <strong>計算：</strong>広告が10,000インプレッションを獲得し、CTR 2% = 200クリック。1クリック2円の場合、総コストは400円です。
    </p>
    
    <div class="callout callout--warning">
      <div class="callout__title">⚠️ CPCの罠</div>
      <div class="callout__text">
        CPCは驚くほど簡単にスケールできます — つまり、予算を簡単に燃やしてしまうということです。CPCキャンペーンは<em>クリックの可能性</em>に対して最適化し、<em>コンバージョンの可能性</em>に対しては最適化しません。好奇心でクリックした2,000人が何もせず去っていくなか、本当の顧客（より慎重な判断をする人たち）があなたの広告を見ることはありません。
        <br><br>
        業界では「不適切に管理されたCPCキャンペーンは30分で家1軒分を燃やせる」というジョークがあります — 私たちもそれを目の当たりにしてきました。
      </div>
    </div>
    
    <p>
      <strong>CPCが最も効果的な場面：</strong>検索広告。誰かが「ランニングシューズ 通販」と検索するとき、その検索<em>自体</em>が意図です。そのキーワードへのCPC入札は、検索クエリによってクリックが既に絞り込まれているため理にかなっています。
    </p>
    
    <h4>2. oCPC（Optimized Cost Per Click）— 頭脳を持ったCPC</h4>
    
    <p>
      oCPCはCPCの課金構造（クリックごとに支払う）を維持しながら、プラットフォームのアルゴリズムが<em>コンバージョン</em>の可能性が高いユーザーに広告を積極的に誘導します。
    </p>
    
    <p>
      <strong>違い：</strong>CPCでは、システムは「誰がクリックしそうか」に対して最適化します。oCPCでは、重視するコンバージョン（購入、フォーム入力、アプリインストール）をシステムに伝え、そのアクションを完了する可能性に基づいてユーザーごとに異なる入札を行います。
    </p>
    
    <p>
      <strong>結果：</strong>クリック単価は高くなるかもしれませんが、<em>コンバージョン</em>単価は通常低くなります。
    </p>
    
    <h4>3. CPA（Cost Per Action）— コンバージョン時のみ支払い</h4>
    
    <p>
      CPAは多くの広告主にとって聖杯です：事前に定義した特定のアクション（アプリインストール、フォーム送信、アカウント登録、購入）をユーザーが完了した場合にのみ支払います。
    </p>
    
    <div class="callout callout--tip">
      <div class="callout__title">✅ 広告主がCPAを好む理由</div>
      <div class="callout__text">
        「成果なければ支払いなし」— 少なくとも理論上は。広告費を直接ビジネス成果に結びつけられます。デジタル広告における成果報酬型課金に最も近い形態です。
      </div>
    </div>
    
    <p>
      <strong>落とし穴：</strong>CPAキャンペーンはスケールが非常に難しいことで知られています。プラットフォームが効果的に最適化するには十分なコンバージョンデータが必要です。過去データがゼロの新規広告主の場合、CPA入札は予算を使い切ることすら難しいかもしれません。
    </p>
    
    <p>
      <strong>TMGの経験則：</strong>プラットフォームに週20〜30件以上のコンバージョンが既に流れていない限り、CPAで始めないでください。そうでなければ、アルゴリズムに十分なシグナルがありません。
    </p>
    
    <h4>4. CPS（Cost Per Sale）— 実際の売上に対するコミッション支払い</h4>
    
    <p>
      CPSはCPAをさらに一歩進めます：<em>販売</em>が発生した場合にのみ支払い、支払額は通常、固定額ではなく収益の一定割合（コミッション）です。
    </p>
    
    <p>
      <strong>CPSが輝く場面：</strong>アフィリエイトマーケティングとインフルエンサー主導の販売。淘宝客、京東アフィリエイト、拼多多の多多進宝、Douyin精选連盟、小紅書クリエイターマーケットプレイスなどのプラットフォームはすべてCPS類似モデルで運営されています。
    </p>
    
    <p>
      <strong>計算：</strong>商品が1,000円で販売され、CPSコミッション率が10%の場合、1販売あたり100円を支払います。アフィリエイトが100販売を生み出した場合、総広告コストは10,000円 — そして実際に販売が発生したからこそ支払うのです。
    </p>
    
    <h4>5. oCPM（Optimized Cost Per Mille）— 業界の主力</h4>
    
    <p>
      oCPMは現在、主要広告プラットフォームで<strong>最も広く使われているパフォーマンス課金モデル</strong>です。CPMの課金構造（1,000インプレッションごとに支払う）と、コンバージョンの可能性が最も高いユーザーをターゲットにするアルゴリズム最適化を組み合わせています。
    </p>
    
    <div class="callout callout--info">
      <div class="callout__title">🧠 oCPMの実際の仕組み</div>
      <div class="callout__text">
        <strong>ステップ1：</strong>目標コンバージョンをプラットフォームに伝えます（例：「アプリインストールが欲しい」）。<br>
        <strong>ステップ2：</strong>アルゴリズムが様々なユーザーに広告を表示し、誰がコンバージョンするかを追跡します。<br>
        <strong>ステップ3：</strong>時間とともに、どのユーザープロファイルがコンバージョンするかを学習し、類似ユーザーに広告を表示するためにより積極的に入札します。<br>
        <strong>ステップ4：</strong>インプレッション単位（CPM）で支払いますが、購入するインプレッションは徐々に「スマート」なものになっていきます。
      </div>
    </div>
    
    <p>
      <strong>なぜ主流なのか：</strong>oCPMはプラットフォームに最適化の最大の柔軟性を与えます。予算、入札、在庫のバランスを取りながら、可能な限り多くのコンバージョンを提供できます。広告主としては、トラッキングが正しく設定されていれば、ボリューム<em>と</em>効率の両方を得られます。
    </p>
    
    <h2>📊 どのモデルを使うべきか？</h2>
    
    <p>
      TMGがクライアントと共に使用している判断フレームワークです：
    </p>
    
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>主な目標</th>
            <th>推奨課金モデル</th>
            <th>理由</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td>新市場でのブランド認知度構築</td>
            <td>CPM</td>
            <td>ボリュームとリーチが必要。効率は後からでよい。</td>
          </tr>
          <tr>
            <td>ヒーロー動画による新製品ローンチ</td>
            <td>CPVまたはCPCV</td>
            <td>インプレッションだけでなく、確実な注目が欲しい。</td>
          </tr>
          <tr>
            <td>高意図の検索トラフィック獲得</td>
            <td>CPC</td>
            <td>検索クエリ自体がクリックを絞り込んでいる。</td>
          </tr>
          <tr>
            <td>大規模なEC販売促進</td>
            <td>oCPM</td>
            <td>ボリュームとコンバージョン効率の最適なバランス。</td>
          </tr>
          <tr>
            <td>リード獲得（フォーム入力、相談）</td>
            <td>oCPCまたはCPA</td>
            <td>クリックではなく、アクションに対して支払う。</td>
          </tr>
          <tr>
            <td>インフルエンサー/アフィリエイトでのスケール</td>
            <td>CPS</td>
            <td>収益が発生したときのみ支払う。</td>
          </tr>
        </tbody>
      </table>
    </div>
    
    <h2>🎯 TMGの見解：モデルだけの話ではない</h2>
    
    <p>
      私たちはBaidu、Douyin、WeChat、小紅書、Bilibili、Bing Chinaの主要な全中国プラットフォームで7桁の広告予算を管理してきました。そして学んだことは次の通りです：
    </p>
    
    <p>
      <strong>課金モデルはトラッキング設定の良し悪しに左右されます。</strong>oCPMやCPAは理論上素晴らしいですが、コンバージョントラッキングが壊れていると、アルゴリズムはゴミに対して最適化します。「コンバージョン」の40%が重複イベントやボットトラフィックだったキャンペーンも見てきました。まずトラッキングを修正し、それから課金モデルを選んでください。
    </p>
    
    <p>
      <strong>ブランド課金とパフォーマンス課金を同じキャンペーンで混ぜないでください。</strong>この間違いを常に見かけます。「ブランド認知度」キャンペーンを作成しながら、「より効率的だから」とoCPM（パフォーマンス課金モデル）を選んでしまう。すると、アルゴリズムはコンバージョンに対して最適化し、ブランドインプレッションの目標は台無しになります。ブランドキャンペーンはCPM/CPVに。パフォーマンスキャンペーンはoCPM/CPA/CPCに。混ぜないでください。
    </p>
    
    <p>
      <strong>シンプルに始めて、徐々に複雑に。</strong>プラットフォームに不慣れな場合は、CPCまたはoCPMから始めてください — 最も理解しやすく、トラブルシューティングもしやすいです。コンバージョンデータが流れ始めたら、CPAやCPSをテストしてください。過去データがゼロの状態で初日からCPAを実行するのは、ハンドル操作を学ぶ前に車を運転しようとするようなものです。
    </p>
    
    <div class="callout callout--tip">
      <div class="callout__title">💡 もう一つ</div>
      <div class="callout__text">
        プラットフォームは「スマート入札」（oCPM、oCPC）を推奨したがります。アルゴリズムが良く見えるからです。しかし、適切なコンバージョンイベントの設定、適切な入札上限の設定、データの解釈には、あなたのビジネスを理解している人間が依然として必要です。自動化は強力ですが、それだけで戦略にはなりません。
      </div>
    </div>
    
    <h2>広告予算をより効果的に活用する準備はできましたか？</h2>
    
    <p>
      <strong>Tuyue Media Gateway</strong>では、中国市場に参入する国際代理店やブランド向けに、Baidu、Douyin、WeChat、小紅書、Bilibili、Bing Chinaで有料メディアを運用しています。単に「キャンペーンを設定する」のではなく、ビジネス目標に実際に合致する課金モデル、トラッキング設定、クリエイティブ戦略を設計します。
    </p>
    
    <p>
      中国でブランドを初めて立ち上げる場合でも、既存のパフォーマンスプログラムを拡大する場合でも、適切な課金モデルの選択、万全なトラッキングの設定、ビジネスにとって本当に重要な指標への最適化をお手伝いします。
    </p>
    
    <p>
      <strong>キャンペーン設定についてご相談されたいですか？</strong> <a href="https://www.tuyuesouxin.cn/contact/" style="color:var(--color-accent);">お問い合わせはこちら</a> — 現在の設定をレビューし、目標と予算に合った課金モデル戦略を提案いたします。
    </p>
    '''

content = content[:idx_s + len(start_marker)] + body_ja + content[idx_e:]

# Translate hero section
content = content.replace(
    '<span class="article-hero__cat">Paid Media Strategy</span>',
    '<span class="article-hero__cat">有料メディア戦略</span>')
content = content.replace(
    '<span class="article-hero__read-time">9 min read</span>',
    '<span class="article-hero__read-time">読了時間 約9分</span>')
content = content.replace(
    '<h1 class="article-hero__title">Ad Billing Models Explained: CPM, CPC, CPA, oCPM and When to Use Each</h1>',
    '<h1 class="article-hero__title">広告課金モデル解説：CPM、CPC、CPA、oCPMとそれぞれの使い分け</h1>')
content = content.replace(
    'Behind every ad campaign is a billing model that determines how you pay — and whether you get the result you paid for. We break down the main billing models, explain how they actually work, and help you pick the right one for your campaign goals.',
    'すべての広告キャンペーンの背後には、支払い方法を決定する課金モデルがあり、支払った分の成果が得られるかどうかも決まります。主要な課金モデルを分解し、実際の仕組みを説明し、キャンペーン目標に合った適切なモデル選びをお手伝いします。')
content = content.replace(
    '<div class="article-hero__author-role">Paid Media Team \u00b7 Shanghai</div>',
    '<div class="article-hero__author-role">有料メディアチーム \u00b7 上海</div>')

# Translate related posts
content = content.replace(
    '<h2 class="related__title">Related Articles</h2>',
    '<h2 class="related__title">関連記事</h2>')

with open(fp, 'w', encoding='utf-8') as f:
    f.write(content)

print('OK: ad-billing-models-explained.html translated to Japanese')
