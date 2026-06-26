# TMG Blog Template Architecture — EN / JA / KO

## 概述

TMG 三语博客统一模板规范。每个 blog 文章都有 EN、JA、KO 三个语言版本，共用相同 HTML 骨架，仅 8 个部分需要语言化。

---

## 一、模板组成（8 个语言化模块）

| # | 模块 | 作用域 | EN | JA | KO |
|---|------|--------|-----|-----|-----|
| 1 | `html lang` | `<html>` 标签 | `en` | `ja` | `ko` |
| 2 | hreflang | `<head>` 内 4 个 `<link>` | 同下 | 同下 | 同下 |
| 3 | Title + Meta | `<head>` 内 title/og/twitter/description | 英语 | 日语 | 韩语 |
| 4 | 导航菜单 Nav | `<header>` 内 | 见 Nav 对照表 | 见 Nav 对照表 | 见 Nav 对照表 |
| 5 | 语言切换器 | `<header>` 内 `lang-item` | 见切换器对照表 | 见切换器对照表 | 见切换器对照表 |
| 6 | 作者 Author | Hero 区 `article-hero__author-role` | Paid Media Team · Shanghai | ペイドメディアチーム · 上海 | 유료 미디어 팀 · 상하이 |
| 7 | 日期 Date | Hero 区 `article-date` | `June 25, 2026` | `2026年6月25日` | `2026년 6월 25일` |
| 8 | Footer | `<footer>` 内文案 + 链接前缀 | `/services/` | `/ja/services/` | `/ko/services/` |

---

## 二、每个模块的详细规格

### 1. `html lang`

```html
EN:  <html lang="en">
JA:  <html lang="ja">
KO:  <html lang="ko">
```

### 2. hreflang

**EN 版本：**
```html
<link rel="alternate" hreflang="en" href="https://www.tuyuesouxin.cn/blog/{slug}/">
<link rel="alternate" hreflang="ja" href="https://www.tuyuesouxin.cn/ja/blog/{slug}/">
<link rel="alternate" hreflang="ko" href="https://www.tuyuesouxin.cn/ko/blog/{slug}/">
<link rel="alternate" hreflang="x-default" href="https://www.tuyuesouxin.cn/blog/{slug}/">
```

**JA 版本：**
```html
<link rel="alternate" hreflang="en" href="https://www.tuyuesouxin.cn/blog/{slug}/">
<link rel="alternate" hreflang="ja" href="https://www.tuyuesouxin.cn/ja/blog/{slug}/">
<link rel="alternate" hreflang="ko" href="https://www.tuyuesouxin.cn/ko/blog/{slug}/">
<link rel="alternate" hreflang="x-default" href="https://www.tuyuesouxin.cn/blog/{slug}/">
```

**KO 版本：**
```html
<link rel="alternate" hreflang="en" href="https://www.tuyuesouxin.cn/blog/{slug}/">
<link rel="alternate" hreflang="ja" href="https://www.tuyuesouxin.cn/ja/blog/{slug}/">
<link rel="alternate" hreflang="ko" href="https://www.tuyuesouxin.cn/ko/blog/{slug}/">
<link rel="alternate" hreflang="x-default" href="https://www.tuyuesouxin.cn/blog/{slug}/">
```

**规则：hreflang 的 `href` 跟 `hreflang` 属性走，不跟文件位置走。**
- hreflang="en" → 永远指向 `/blog/`
- hreflang="ja" → 永远指向 `/ja/blog/`
- hreflang="ko" → 永远指向 `/ko/blog/`
- hreflang="x-default" → 永远指向 `/blog/`

### 3. Title + Meta

| 字段 | EN | JA | KO |
|------|-----|-----|-----|
| `<title>` | English Title \| TMG | 日本語タイトル \| TMG | 한국어 제목 \| TMG |
| `og:title` | 同 title | 同 title | 同 title |
| `twitter:title` | 同 title | 同 title | 同 title |
| `description` | English excerpt | 日本語抜粋 | 한국어 요약 |
| `og:description` | 同 description | 同 description | 同 description |
| `twitter:description` | 同 description | 同 description | 同 description |
| `canonical` | `/blog/{slug}/` | `/ja/blog/{slug}/` | `/ko/blog/{slug}/` |
| `og:url` | 同 canonical | 同 canonical | 同 canonical |

### 4. 导航菜单 Nav 对照表

**文字对照：**

| EN | JA | KO |
|-----|-----|-----|
| Pricing | 料金 | 가격 |
| Client Stories | 導入事例 | 고객 사례 |
| GEO | GEO | GEO |
| Blog | ブログ | 블로그 |
| FAQ | FAQ | FAQ |
| About Us | 会社概要 | 회사 소개 |
| Services | サービス | 서비스 |

**HTML 结构（所有语言共用，仅文字不同）：**
```html
<nav class="header__nav">
  <a href="/services/" class="header__nav-link header__dropdown-trigger">{Services Text}</a>
  <a href="/pricing/" class="header__nav-link">{Pricing Text}</a>
  <a href="/client-stories/" class="header__nav-link">{Client Stories Text}</a>
  <a href="/geo/" class="header__nav-link">GEO</a>
  <a href="/blog/" class="header__nav-link header__nav-link--active">{Blog Text}</a>
  <a href="/faqs/" class="header__nav-link">FAQ</a>
  <a href="/about/" class="header__nav-link header__dropdown-trigger">{About Us Text}</a>
</nav>
```

### 5. 语言切换器 Language Switcher

**EN 版本（显示 JA 和 KO 链接）：**
```html
<div class="header__lang">
  <button class="header__lang-btn">🇺🇸 English</button>
  <div class="header__lang-dropdown">
    <a href="/ja/blog/{slug}/" class="header__lang-item">🇯🇵 日本語</a>
    <a href="/ko/blog/{slug}/" class="header__lang-item">🇰🇷 한국어</a>
  </div>
</div>
```

**JA 版本（显示 EN 和 KO 链接）：**
```html
<div class="header__lang">
  <button class="header__lang-btn">🇯🇵 日本語</button>
  <div class="header__lang-dropdown">
    <a href="/blog/{slug}/" class="header__lang-item">🇺🇸 English</a>
    <a href="/ko/blog/{slug}/" class="header__lang-item">🇰🇷 한국어</a>
  </div>
</div>
```

**KO 版本（显示 EN 和 JA 链接）：**
```html
<div class="header__lang">
  <button class="header__lang-btn">🇰🇷 한국어</button>
  <div class="header__lang-dropdown">
    <a href="/blog/{slug}/" class="header__lang-item">🇺🇸 English</a>
    <a href="/ja/blog/{slug}/" class="header__lang-item">🇯🇵 日本語</a>
  </div>
</div>
```

### 6. 作者 Author

```html
<span class="article-hero__author-role">{Author Text}</span>
```

| EN | JA | KO |
|-----|-----|-----|
| Paid Media Team · Shanghai | ペイドメディアチーム · 上海 | 유료 미디어 팀 · 상하이 |

### 7. 日期 Date

```html
<span class="article-date">{Date Text}</span>
```

| EN | JA | KO |
|-----|-----|-----|
| `June 25, 2026` | `2026年6月25日` | `2026년 6월 25일` |
| 格式: `Month DD, YYYY` | 格式: `YYYY年M月D日` | 格式: `YYYY년 M월 D일` |

### 8. Footer

**规则：** JA 和 KO 版本的 footer 链接必须带语言前缀 `/ja/` 或 `/ko/`。

| EN URL | JA URL | KO URL |
|--------|--------|--------|
| `/services/` | `/ja/services/` | `/ko/services/` |
| `/pricing/` | `/ja/pricing/` | `/ko/pricing/` |
| `/about/` | `/ja/about/` | `/ko/about/` |
| `/client-stories/` | `/ja/client-stories/` | `/ko/client-stories/` |
| `/faqs/` | `/ja/faqs/` | `/ko/faqs/` |
| `/contact/` | `/ja/contact/` | `/ko/contact/` |

**Footer 文案：**

| 区块 | EN | JA | KO |
|------|-----|-----|-----|
| About TMG desc | Your single point of access... | 中国デジタル広告市場への... | 중국 디지털 광고 시장으로의... |
| Quick Links | Quick Links | クイックリンク | 빠른 링크 |
| Contact | Contact | お問い合わせ | 문의하기 |
| Legal | Legal | 法的情報 | 법적 정보 |
| Copyright | © 2026 Tuyue Media Gateway. All rights reserved. | © 2026 Tuyue Media Gateway. All rights reserved. | © 2026 Tuyue Media Gateway. All rights reserved. |

---

## 三、不变的固定部分（所有语言相同）

以下部分在所有三个语言版本中完全相同，不需修改：
- GA4 代码（`G-P5RQGYPTGP`）
- CSS 样式块
- JS 脚本块（IntersectionObserver、导航交互、表单）
- Favicon
- OG Image / Twitter Card 图片链接
- JSON-LD Schema 中的 Organization/WebSite 部分
- SVG logo 定义
- Headers` `header__lang-flag 样式
- 结构类名（`.footer__section`、`.footer__title` 等）
- Logo SVG（viewBox 48x48，渐变月牙，TMG 文字）

---

## 四、创建新文章时 OLD SLUG → NEW SLUG 替换清单

从模板复制时，必须替换以下所有出现**旧模板 slug** 的地方：

| # | 位置 | 示例 | 替换目标 |
|---|------|------|----------|
| 1 | `<link rel="canonical"` | `/blog/{old-slug}/` | `/blog/{new-slug}/` |
| 2 | `<link rel="alternate" hreflang="en"` | `/blog/{old-slug}/` | `/blog/{new-slug}/` |
| 3 | `<link rel="alternate" hreflang="ja"` | `/ja/blog/{old-slug}/` | `/ja/blog/{new-slug}/` |
| 4 | `<link rel="alternate" hreflang="ko"` | `/ko/blog/{old-slug}/` | `/ko/blog/{new-slug}/` |
| 5 | `<link rel="alternate" hreflang="x-default"` | `/blog/{old-slug}/` | `/blog/{new-slug}/` |
| 6 | `<meta property="og:url"` | `/blog/{old-slug}/` | `/blog/{new-slug}/` |
| 7 | 语言切换器 EN `<a href="/blog/{old-slug}/"` | `/blog/{old-slug}/` | `/blog/{new-slug}/` |
| 8 | 语言切换器 JA `<a href="/ja/blog/{old-slug}/"` | `/ja/blog/{old-slug}/` | `/ja/blog/{new-slug}/` |
| 9 | 语言切换器 KO `<a href="/ko/blog/{old-slug}/"` | `/ko/blog/{old-slug}/` | `/ko/blog/{new-slug}/` |

**替换方法（Python 代码级）：**
```python
html = html.replace(f'/blog/{OLD_SLUG}/', f'/blog/{NEW_SLUG}/')
html = html.replace(f'/ja/blog/{OLD_SLUG}/', f'/ja/blog/{NEW_SLUG}/')
html = html.replace(f'/ko/blog/{OLD_SLUG}/', f'/ko/blog/{NEW_SLUG}/')
```

这是最安全的方式，比 regex 更可靠。

---

## 五、模板文件

当前参考模板：
- EN: `blog/wechat-ai-agent-coming-for-advertisers.html`
- JA: `ja/blog/wechat-mini-program-search-ads.html`
- KO: `ko/blog/wechat-mini-program-search-ads.html`

建议后续将这三个模板文件标准化，确保：
1. JA 和 KO 的 hreflang 已修复（当前存在 JA 的 hreflang="en" 指向 `/ja/blog/` 的问题）
2. 语言切换器 URL 使用 `{slug}` 占位符方便替换
3. 作者和日期占位符可识别
