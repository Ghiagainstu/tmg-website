# TMG Blog 全站质量修复 — 完整 Prompt

仓库路径：C:\Users\fireh\WorkBuddy\20260326144402\tmg-website

## 背景
全站扫描发现 144 个文件仍有问题。需要逐篇修复。
以下是 4 类问题的处理方式。

---

## 第一类：EN 页面 Get Started → Contact Us（108篇）

所有英文 blog 详情页的 CTA 按钮仍是 "Get Started"。
批量替换：在 blog/*.html 中，把 `Get Started` 替换为 `Contact Us`。

注意：只替换 CTA 按钮文本，不要替换正文中的 "Get Started"（如果有）。
推荐用 Python 操作，保持 UTF-8 编码。

---

## 第二类：EN 旧模板 Insight → 主题相关内容（64篇）

以下英文文件的 TMG Insight 是通用模板：
```
Based on our experience managing campaigns for 60+ international brands in China, this represents a significant opportunity...
```
需要逐篇根据文章主题重写 Insight，要求：
- 与文章主题强相关
- 2-3 句话，专业简洁
- 不用 "Based on our experience" 开头

以下英文文件也需要检查（同一模板的变体）：
```
this platform represents a significant opportunity. The key is combining platform-specific best practices with data-driven optimization for maximum ROI.
```

### 操作步骤
1. 先批量替换 CTA（第一类）
2. 再逐篇重写 Insight（第二类）
3. 每篇修完验证 UTF-8 编码正确

---

## 第三类：JA/KO 旧模板 Insight（11篇）

### JA 文件（5篇）
这些文件的 TMG Insight 含英文残留（significantな機会を represent / our経験 based on）：

- ja/blog/bing-china-demographics-who-are-these-users.html
- ja/blog/byte-jump-vs-alibaba-content-agent-war.html
- ja/blog/china-big-tech-ai-monetization-2026.html
- ja/blog/cpm-is-rising-bad.html
- ja/blog/geo-channel-weight-2026.html

需要根据每篇文章主题用自然日语重写 Insight。
用 Python（open with encoding='utf-8'）操作，不要用 PowerShell Write-Content。

### KO 文件（6篇）
这些文件的 TMG Insight 是通用韩文模板：

- ko/blog/baidu-demographics-who-are-these-735m-users.html
- ko/blog/byte-jump-vs-alibaba-content-agent-war.html
- ko/blog/china-big-tech-ai-monetization-2026.html
- ko/blog/cpm-is-rising-bad.html
- ko/blog/geo-channel-weight-2026.html
- ko/blog/kuaishou-demographics-who-are-these-400m-users.html

需要根据每篇文章主题用自然韩语重写 Insight。

---

## 第四类：缺失 Insight（3篇）

以下文件缺少 TMG Insight callout 组件，需要添加：

- ko/blog/bing-china-performance-max-2026.html

格式：
```html
<div class="callout"><div class="callout__label">TMG Insight</div><p>（与文章主题相关的Insight内容）</p></div>
```

注意：ja/blog/index.html 和 ko/blog/index.html 是列表页，不需要 Insight。

---

## 第五类：正文 ? 乱码（31篇，可选）

以下文件正文有较多 ? 字符（可能是 em-dash — 或特殊引号损坏）：

EN 页面（qmarks 11-49）：
blog/ad-billing-models-explained.html (49)
blog/baidu-advertising-complete-guide-2026.html (48)
blog/618-2026-ai-takedown-shopping-festival.html (46)
blog/618-data-review-2026.html (44)
blog/china-geo-2026-ai-search-ad-visibility.html (43)
blog/xiaohongshu-demographics-who-are-these-350m-users.html (43)
blog/618-ai-native-era-2026-first-round-report.html (40)
blog/alipay-abao-ai-launch-2026.html (39)
blog/618-2026-final-push-ai-everywhere.html (38)
blog/618-2026-geo-goes-mainstream.html (37)
blog/wechat-mini-program-search-private-domain-closed-loop.html (38)
blog/xiaohongshu-search-koc-local-discovery.html (38)
blog/wechat-moments-ads.html (26)
blog/attribution-models-guide.html (16)

JA 页面：
ja/blog/xiaohongshu-search-koc-local-discovery.html (12)
ja/blog/baidu-ai-search-brand-zone-sem-high-intent-leads.html (11)

KO 页面：
ko/blog/wechat-moments-ads-ko.html (18)
ko/blog/doubao-ads-geo-still-worth-it.html (16)
ko/blog/bing-china-premium-audience-guide.html (13)
ko/blog/chinese-influencer-marketing-ko.html (13)
ko/blog/xiaohongshu-demographics-who-are-these-350m-users.html (12)
ko/blog/attribution-models-guide.html (11)
ko/blog/douyin-sem-vs-search-feed-2026.html (11)
ko/blog/index.html (20)

这类问题需要检查原文是否用了 em-dash（—）或特殊引号（"" ''），然后用 git 历史恢复或手动替换。
如果不确定，先用 git show <commit>:<file> 对比确认是编码损坏还是原文就有 ?。

---

## 执行顺序

1. **第一类**：批量替换 EN CTA（最快，1次操作）
2. **第三类**：修复 JA/KO 旧模板 Insight（11篇，逐篇）
3. **第四类**：添加缺失 Insight（1篇）
4. **第二类**：重写 EN 旧模板 Insight（64篇，逐篇，最耗时）
5. **第五类**：检查正文乱码（可选，需要对比 git 历史）

## 编码要求
- 所有文件操作用 Python（encoding='utf-8'）
- 不要用 PowerShell 的 Set-Content / Write-Content（会破坏 UTF-8）
- 每个文件操作后回读验证

## 完成后
- git add -A
- git commit -m "fix: full-site blog quality pass - CTA localization + TMG Insight rewrite"
- git push
- 给我 commit 号