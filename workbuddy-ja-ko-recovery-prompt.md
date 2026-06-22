仓库路径：C:\Users\fireh\WorkBuddy\20260326144402\tmg-website

# 任务：恢复损坏文件 + 重写 TMG Insight

## 第一步：从 git 恢复 6 个损坏文件

以下文件在当前本地版本中正文已编码损坏（出现大量 ? 乱码）。
从 commit 62e2af1 恢复这些文件的完好版本：

```
git checkout 62e2af1 -- ja/blog/618-2026-ai-takedown-shopping-festival.html
git checkout 62e2af1 -- ja/blog/618-2026-final-push-ai-everywhere.html
git checkout 62e2af1 -- ja/blog/618-2026-geo-goes-mainstream.html
git checkout 62e2af1 -- ja/blog/baidu-advertising-complete-guide-2026.html
git checkout 62e2af1 -- ja/blog/alipay-abao-ai-launch-2026.html
git checkout 62e2af1 -- ko/blog/618-2026-ai-takedown-shopping-festival.html
```

恢复后验证每个文件正文可读（不应有大量 ? 字符）。

## 第二步：为恢复后的文件重写 TMG Insight

恢复后这些文件的 TMG Insight 会是旧模板（含英文残留如 significantな機会を represent）。
需要用与文章主题相关的自然日语/韩语重写。

### 2a. JA 618-2026-ai-takedown-shopping-festival.html
找到：
```
<div class="callout"><div class="callout__label">TMG Insight</div><p>中国で60以上の internationalブランドの campaignを管理した our経験 based on、これは significantな機会を representしています。プラットフォーム固有の best practicesとデータ駆動型 optimizationを組み合わせることが keyです。</p></div>
```
替换为：
```
<div class="callout"><div class="callout__label">TMG Insight</div><p>2026年の618は、割引競争からAI主導の商品発見へと重心が移りました。TMGの運用知見では、商品フィード・LP構造・検索意図をAI推薦前提に最適化したブランドが、CPAを抑えながらコンバージョンを伸ばしています。</p></div>
```

### 2b. JA 618-2026-final-push-ai-everywhere.html
找到同样的旧模板，替换为：
```
<div class="callout"><div class="callout__label">TMG Insight</div><p>2026年の618で重要なのは、AIを実験的な打ち手ではなく業務インフラとして組み込むことでした。AI配信者、推薦対応カタログ、価格自動化を前提に運用を再設計したブランドが、CPA抑制とROAS改善の両面で優位に立っています。</p></div>
```

### 2c. JA 618-2026-geo-goes-mainstream.html
找到同样的旧模板，替换为：
```
<div class="callout"><div class="callout__label">TMG Insight</div><p>618 2026でGEOは仮説から予算執行のフェーズに移行しました。2025年からAI発見性シグナルのテストを先行したブランドは、競争が激化する前に低コストで可視性を確保できており、検索やフィードと並ぶ独立テスト予算として整理すべき局面です。</p></div>
```

### 2d. JA baidu-advertising-complete-guide-2026.html
找到旧模板，替换为：
```
<div class="callout"><div class="callout__label">TMG Insight</div><p>Baiduは明示的な検索意図がある案件で最も力を発揮します。成果が安定している広告主は、ブランド検索の防衛、競合ワードへの攻め、AI時代のクリエイティブテストを組み合わせており、単一キャンペーンタイプへの依存を避けています。</p></div>
```

### 2e. JA alipay-abao-ai-launch-2026.html
找到旧模板（注意这个文件的 Insight 可能混入了韩文），替换为：
```
<div class="callout"><div class="callout__label">TMG Insight</div><p>AlipayのアバオAIアシスタントは、決済フロー内の新しいAIネイティブ広告面です。アプリ内AIタッチポイントの早期テストに取り組んだ広告主は、ユーザーがすでに購買モードにあるため、エンゲージメントが35%向上しています。</p></div>
```

### 2f. KO 618-2026-ai-takedown-shopping-festival.html
找到旧模板，替换为：
```
<div class="callout"><div class="callout__label">TMG Insight</div><p>2026년 618은 할인 중심 프로모션에서 AI 중심 상품 발견으로 무게추가 옮겨졌습니다. TMG 운영 경험상 상품 피드, LP 구조, 검색 의도를 AI 추천 기준에 맞게 최적화한 브랜드가 CPA를 낮추면서 전환 성과를 더 잘 만들고 있습니다.</p></div>
```

## 第三步：验证

恢复+重写后，对每个文件执行验证：
1. 正文可读（不应有大量 ? 乱码）
2. TMG Insight 内容为目标语言（JA文件=日语，KO文件=韩语），不含英文残留
3. CTA 按钮不是 "Get Started"（如果是，JA改为"お問い合わせ"，KO改为"문의하기"）

## 注意事项
- 用 UTF-8 编码读写文件，不要用 PowerShell 默认的 Write-Content（会破坏编码）
- 推荐用 Python 或 git checkout + sed 的方式操作
- 每个文件操作完后用 UTF-8 回读验证内容是否正确

## 完成后
git add + commit + push，给我 commit 号。