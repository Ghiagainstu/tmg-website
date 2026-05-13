#!/usr/bin/env python3
"""
修复 KO pangle-ads.html 中的剩余问题：
1. 第750行空段落
2. h2 id="getting-start-ed" 空标题
3. h3 标题不准确
"""
filepath = 'ko/blog/pangle-ads.html'

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 修复第750行的空段落 + 空h2 + 错误的h3
old_section = '''<p>서비스</p>
<h2 id="getting-start-ed"></h2>
<h3>국제 앱 개발자를 위한 권장 전략</h3>'''

new_section = '''<p>Pangle을 시작하는 방법은 다음과 같습니다.</p>
<h2 id="getting-start-ed">Pangle 시작하기</h2>
<h3>앱 개발자용 (공급 사이드)</h3>'''

content = content.replace(old_section, new_section)
print(f"✓ Fixed getting-started section")

# 2. 修复第二个h3（应该是"For Advertisers"）
content = content.replace('<h3>요약</h3>', '<h3>광고주용 (수요 사이드)</h3>')
print(f"✓ Fixed h3 for advertisers")

# 写入文件
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"\n✅ Fixed remaining issues in {filepath}")
