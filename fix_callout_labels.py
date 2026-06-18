import re
from pathlib import Path

WEBSITE = Path(r"C:\Users\fireh\WorkBuddy\20260326144402\tmg-website")

# English -> Japanese translations for callout labels
LABEL_TRANSLATIONS = {
    'Key Insight': '重要な洞察',
    'Why This Matters': 'なぜ重要か',
    'Pro Tip': 'プロのヒント',
    'Common Pitfall': '一般的な落とし穴',
    'Important Note': '重要な注意',
    'Key Takeaway': '重要な要点',
    'Summary': 'まとめ',
    'Conclusion': '結論',
    'Warning': '警告',
    'Note': '注意',
    'Tip': 'ヒント',
    'Example': '例',
    'Source': '出典',
    'Sources': '出典',
    'Reference': '参考',
    'References': '参考',
    'Further Reading': '进一步阅读',
    'Related Articles': '関連記事',
    'See Also': '参照',
    'Learn More': '详细',
    'Get Started': '始めましょう',
    'Next Steps': '次のステップ',
    'Action Items': 'アクションアイテム',
    'Key Points': '重要なポイント',
    'Main Takeaways': '主な要点',
    'What You Need to Know': '知っておくべきこと',
    'The Bottom Line': '結論',
    'Final Thoughts': '最終考察',
    'Recommendations': '推奨事項',
    'Best Practices': 'ベストプラクティス',
    'Common Mistakes': '一般的なミス',
    'FAQ': 'よくある質問',
    'Q&A': 'Q&A',
}

def fix_callout_labels(html_path, lang):
    """Fix English callout labels in JA/KO articles."""
    content = html_path.read_text(encoding='utf-8')
    changed = False
    
    for en_label, ja_label in LABEL_TRANSLATIONS.items():
        # Pattern: callout__label">{en_label}
        old_pattern = f'callout__label">{en_label}'
        new_pattern = f'callout__label">{ja_label}'
        
        if old_pattern in content:
            content = content.replace(old_pattern, new_pattern)
            changed = True
    
    # Also fix emoji-prefixed labels like "🎯 Key Insight"
    emoji_pattern = re.compile(r'callout__label">[🎯💡🏆⚠️📝🔑✅❌📊📈🔍💡🎯🏆📌📋🔗✨🚀💥🎉🎊🎈🎁🎀🏆🥇🥈🥉💎👑🎯📌📍🔔⏰📅📆🗓️⏰🔑🔐🔒🔓🔑🗝️🔨🔧⚙️🛠️🔩🔑🗝️🔐🔒🔓🔑🗝️🔨🔧⚙️🛠️🔩🔑🗝️]+ ([A-Za-z\s]+)')
    
    def replace_emoji_label(m):
        en_label = m.group(1).strip()
        ja_label = LABEL_TRANSLATIONS.get(en_label, en_label)
        return f'callout__label">{ja_label}'
    
    content = emoji_pattern.sub(replace_emoji_label, content)
    
    if changed:
        html_path.write_text(content, encoding='utf-8')
        return True
    return False

# Process batch articles
batch_prefixes = ['baidu-', 'bilibili-', 'bing-china-', 'douyin-', 'wechat-', 'xiaohongshu-']

fixed = 0
for lang, lang_dir in [('ja', 'ja/blog'), ('ko', 'ko/blog')]:
    for prefix in batch_prefixes:
        for html in (WEBSITE / lang_dir).glob(f'{prefix}*.html'):
            if fix_callout_labels(html, lang):
                fixed += 1

print(f"Fixed {fixed} articles")
