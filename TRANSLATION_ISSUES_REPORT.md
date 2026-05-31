# Translation Issues Report - TMG Website JA/KO Pages

> Scan Date: 2026-05-30
> Total Untranslated Items: 57 (29 Japanese, 28 Korean)

## Executive Summary

This report identifies content that appears untranslated or partially translated on the Japanese (`/ja/`) and Korean (`/ko/`) versions of the TMG website. The scan detected 57 items across 25 files that may need attention.

**Note:** Some items flagged are brand names, technical terms, or proper nouns that may intentionally remain in English. Please review each item to determine if translation is required.

---

## Japanese (JA) - 29 items in 12 files

### High Priority (Clear English text)

| File | Line | Type | Current Text | Suggested Action |
|------|------|------|--------------|------------------|
| `ja/blog/index.html` | 1200 | h2_title | Meet Zhitu Xing：Ocean Engine 内蔵 AI 広告アシスタント | Translate "Meet Zhitu Xing" to Japanese |
| `ja/blog/search-new-storefront-ja.html` | 855 | h2_title | ?? Super Brand Zone：デジタル旗艦店 | Translate "Super Brand Zone" to Japanese |
| `ja/blog/wechat-moments-ads-ja.html` | 860 | h2_title | ?? Part 3：Tencent Ads「艾米（Aimi）」& 入札戦略 | Translate "Part 3" to Japanese |
| `ja/services/wechat/index.html` | 957 | h3_title | ?? B2B Lead Generation | Translate "B2B Lead Generation" to Japanese |
| `ja/blog/index.html` | 842-854 | button | ?? All, ?? Tencent, ?? Platforms, etc. | Translate button labels to Japanese |

### Medium Priority (Mixed content)

| File | Line | Type | Current Text | Suggested Action |
|------|------|------|--------------|------------------|
| `ja/blog/pangle-ads.html` | 808 | h2_title | ?? Pangleの規模 | "Pangle" is brand name - may keep |
| `ja/client-stories/index.html` | 876 | h3_title | Farmskins | Brand name - likely keep |
| `ja/faqs/index.html` | 1357 | faq_question | CPM、CPC、CPA、CPTとは？ | Technical terms - may keep |
| `ja/services/bing/index.html` | 554 | h3_title | BaiduではなくBing Chinaを選ぶ理由 | Brand names - likely keep |
| `ja/services/index.html` | 844 | h3_title | Moments & 検索広告 | "Moments" is WeChat feature name |

### Low Priority (Technical/Brand terms)

| File | Line | Type | Current Text | Notes |
|------|------|------|--------------|-------|
| `ja/blog/deepseek-image-recognition-geo.html` | 861 | paragraph | これは中国のGEO（Generative Engine Optimization）にとって... | Technical term in parentheses |
| `ja/faqs/index.html` | 1509 | faq_question | DouyinとTikTok広告の違いは？ | Brand names |
| `ja/faqs/index.html` | 1557 | faq_question | Ocean Engineの最低予算は？ | Brand name |
| `ja/faqs/index.html` | 1658 | faq_question | Douyin/Ocean Engineで制限されている業種は？ | Brand names |
| `ja/index.html` | 2805 | h3_title | Farmskins | Brand name |

### Bug/Technical Issue

| File | Line | Type | Current Text | Issue |
|------|------|------|--------------|-------|
| `ja/faqs/index.html` | 2660 | filter_tab | ' + v + ' | JavaScript template literal not rendered |

---

## Korean (KO) - 28 items in 13 files

### High Priority (Clear English text)

| File | Line | Type | Current Text | Suggested Action |
|------|------|------|--------------|------------------|
| `ko/blog/douyin-enterprise-account.html` | 958 | h2_title | ??? ?? ?? (Online Lead Generation) | Remove English in parentheses or translate |
| `ko/blog/ocean-engine-local-reach.html` | 877 | h2_title | ?? ?? ?? (Store Visit) | Remove English in parentheses or translate |
| `ko/blog/ocean-engine-local-reach.html` | 890 | h2_title | ??? ?? ?? (Online Lead Generation) | Remove English in parentheses or translate |
| `ko/blog/wechat-moments-ads-ko.html` | 873 | h2_title | Part 3: Tencent Ads Aimi & ?? ?? | Translate "Part 3" to Korean |
| `ko/blog/wechat-moments-ads-ko.html` | 791 | h1_title | WeChat Moments ?? ?? Q&A 20? | "Q&A" is English abbreviation |
| `ko/blog/index.html` | 844-848 | button | ?? Tencent, ?? GEO/AI, ?? Douyin/OE, ?? Bilibili | Translate button labels to Korean |

### Medium Priority (Mixed content)

| File | Line | Type | Current Text | Suggested Action |
|------|------|------|--------------|------------------|
| `ko/blog/ocean-engine-overview.html` | 857 | paragraph | TikTok for Business——??? TikTok ?? ??? | Mixed English/Korean |
| `ko/blog/ocean-engine-overview.html` | 858 | paragraph | Ocean Engine ??(千川) | Chinese characters in Korean text |
| `ko/blog/ocean-engine-overview.html` | 873 | paragraph | Ocean Engine ??(星图) | Chinese characters in Korean text |
| `ko/blog/ocean-engine-overview.html` | 876 | paragraph | Ocean Engine ??(云图) | Chinese characters in Korean text |
| `ko/blog/pangle-ads.html` | 875 | h2_title | ?? Pangle? ?? | "Pangle" is brand name - may keep |
| `ko/client-stories/index.html` | 878 | h3_title | Farmskins | Brand name - likely keep |
| `ko/faqs/index.html` | 2167 | faq_category_title | GEO vs SEO & ?? | Technical terms - may keep |

### Low Priority (Technical/Brand terms)

| File | Line | Type | Current Text | Notes |
|------|------|------|--------------|-------|
| `ko/blog/ocean-engine-ai-assistant.html` | 806 | h2_title | Zhitu Xing??? | Brand name |
| `ko/blog/ocean-engine-local-reach.html` | 809 | h2_title | Ocean Engine Local Reach?? | Brand name |
| `ko/faqs/index.html` | 1539 | faq_question | Ocean Engine? ?? ???? | Brand name |
| `ko/faqs/index.html` | 1550 | faq_question | Ocean Engine? ?? ???? | Brand name |
| `ko/faqs/index.html` | 1640 | faq_question | Douyin/Ocean Engine?? ???? ???? | Brand names |
| `ko/faqs/index.html` | 1859 | faq_question | Bilibili? ???? CPM·CPC ???? | Technical terms |
| `ko/faqs/index.html` | 1986 | faq_question | Bilibili?? Douyin/TikTok ???? ??? ? ???? | Brand names |
| `ko/services/bing/index.html` | 447 | h3_title | Bing CN + Baidu ?? | Brand names |
| `ko/services/index.html` | 846 | h3_title | Moments & ?? ?? | "Moments" is WeChat feature name |
| `ko/index.html` | 2746 | h3_title | Farmskins | Brand name |

### Bug/Technical Issue

| File | Line | Type | Current Text | Issue |
|------|------|------|--------------|-------|
| `ko/faqs/index.html` | 2642 | filter_tab | ' + v + ' | JavaScript template literal not rendered |

---

## Recommendations

### 1. Immediate Translation Needed
- **Button labels** in `ja/blog/index.html` and `ko/blog/index.html` (UI elements)
- **Section headers** containing clear English text (e.g., "Meet Zhitu Xing", "Super Brand Zone", "B2B Lead Generation")
- **Mixed parentheses content** (e.g., "??? ?? ?? (Online Lead Generation)")

### 2. Review for Consistency
- **Brand names** like "Farmskins", "Pangle", "Ocean Engine" - decide if they should remain in English or be transliterated
- **Technical terms** like "CPM", "CPC", "GEO", "SEO" - likely remain in English
- **WeChat feature names** like "Moments" - may remain in English

### 3. Bug Fix Required
- **Filter tab issue**: `' + v + '` appears in both `ja/faqs/index.html` (line 2660) and `ko/faqs/index.html` (line 2642). This looks like a JavaScript template literal that wasn't rendered properly.

### 4. Chinese Characters in Korean Text
- Consider whether Chinese characters (千川, 星图, 云图) in `ko/blog/ocean-engine-overview.html` should be translated to Korean or kept as-is.

---

## Files to Edit

### Japanese (12 files)
1. `ja/blog/index.html` - Button labels and section header
2. `ja/blog/search-new-storefront-ja.html` - Section header
3. `ja/blog/wechat-moments-ads-ja.html` - Section header
4. `ja/services/wechat/index.html` - Section header
5. `ja/blog/pangle-ads.html` - Section header (review)
6. `ja/client-stories/index.html` - Client name (review)
7. `ja/faqs/index.html` - FAQ questions and filter tab bug
8. `ja/blog/deepseek-image-recognition-geo.html` - Paragraph (review)
9. `ja/index.html` - Client name (review)
10. `ja/services/bing/index.html` - Section header (review)
11. `ja/services/index.html` - Section header (review)
12. `ja/client-stories/farmskins/index.html` - Client name (review)

### Korean (13 files)
1. `ko/blog/douyin-enterprise-account.html` - Section header
2. `ko/blog/index.html` - Button labels
3. `ko/blog/ocean-engine-ai-assistant.html` - Section header (review)
4. `ko/blog/ocean-engine-local-reach.html` - Section headers
5. `ko/blog/ocean-engine-overview.html` - Paragraphs with mixed content
6. `ko/blog/pangle-ads.html` - Section header (review)
7. `ko/blog/wechat-moments-ads-ko.html` - Section headers
8. `ko/client-stories/index.html` - Client name (review)
9. `ko/faqs/index.html` - FAQ questions and filter tab bug
10. `ko/index.html` - Client name (review)
11. `ko/services/bing/index.html` - Section header (review)
12. `ko/services/index.html` - Section header (review)
13. `ko/client-stories/farmskins/index.html` - Client name (review)

---

## Next Steps

1. Review this report and prioritize items for translation
2. Decide on brand name/technical term policy
3. Fix the filter tab JavaScript bug
4. Translate high-priority items
5. Re-scan to verify completeness

---

*Report generated by automated scan. Manual review recommended for accuracy.*
