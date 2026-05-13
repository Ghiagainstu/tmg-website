#!/usr/bin/env python3
"""
修复英语站所有页面的 canonical 和 og:url：
1. 添加 trailing slash（与 sitemap 一致）
2. 确保 canonical 和 og:url 完全匹配
3. 修复 homepage（index.html 在根目录）
"""
import os
import re

BASE = "."

def get_url_path(filepath):
    """根据文件路径生成 URL 路径（带 trailing slash）"""
    # 相对路径
    rel_path = os.path.relpath(filepath, BASE).replace('\\', '/')
    
    # 如果是 index.html，取目录名
    if rel_path.endswith('index.html'):
        # about/index.html → /about/
        url_path = '/' + rel_path.replace('index.html', '') + '/'
    else:
        # blog/post.html → /blog/post/
        url_path = '/' + rel_path.replace('.html', '') + '/'
    
    return url_path

def fix_file(filepath):
    """修复单个文件的 canonical 和 og:url"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 获取正确的 URL 路径
    url_path = get_url_path(filepath)
    full_url = f"https://www.tuyuesouxin.cn{url_path}"
    
    # 修复 canonical
    # 格式: <link rel="canonical" href="...">
    canonical_pattern = r'<link rel="canonical" href="[^"]*">'
    canonical_replacement = f'<link rel="canonical" href="{full_url}">'
    content = re.sub(canonical_pattern, canonical_replacement, content)
    
    # 修复 og:url
    # 格式: <meta property="og:url" content="...">
    og_pattern = r'<meta property="og:url" content="[^"]*">'
    og_replacement = f'<meta property="og:url" content="{full_url}">'
    content = re.sub(og_pattern, og_replacement, content)
    
    # 写回
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return full_url

# 收集所有英语站 HTML 文件（排除 ja/ 和 ko/）
html_files = []
for root, dirs, files in os.walk(BASE):
    # 跳过 ja/ 和 ko/ 目录
    if '/ja/' in root or '\\ja\\' in root or '/ko/' in root or '\\ko\\' in root:
        continue
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

print(f"找到 {len(html_files)} 个英语站 HTML 文件")

# 修复所有文件
fixed = 0
for filepath in sorted(html_files):
    try:
        url = fix_file(filepath)
        rel_path = os.path.relpath(filepath, BASE)
        print(f"✅ {rel_path} → {url}")
        fixed += 1
    except Exception as e:
        print(f"❌ {filepath}: {e}")

print(f"\n总共修复 {fixed} 个文件")
