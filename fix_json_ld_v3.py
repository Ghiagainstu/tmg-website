#!/usr/bin/env python3
"""修复所有 HTML 文件的 JSON-LD（正确版本 v3）"""
import json
import re
import os

BASE = "."

def get_json_ld_blocks(lang='en', is_homepage=False):
    """返回正确的 JSON-LD 块列表"""
    blocks = []
    
    # Organization（所有页面）
    org_desc = "Digital advertising agency" if lang != 'ja' else "デジタル広告代理店"
    org = json.dumps({
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": "Tuyue Media Gateway",
        "alternateName": "TMG",
        "url": "https://www.tuyuesouxin.cn/",
        "description": org_desc,
        "email": "tmg@tuyuesouxin.cn",
        "address": {
            "@type": "PostalAddress",
            "streetAddress": "599-2F202 Wanzhen Road",
            "addressLocality": "Shanghai",
            "addressRegion": "Shanghai",
            "postalCode": "201824",
            "addressCountry": "CN"
        },
        "sameAs": []
    }, separators=(',', ':'), ensure_ascii=False)
    blocks.append(('Organization', org))
    
    # WebSite（所有页面）
    website = json.dumps({
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": "Tuyue Media Gateway",
        "url": "https://www.tuyuesouxin.cn/"
    }, separators=(',', ':'), ensure_ascii=False)
    blocks.append(('WebSite', website))
    
    # AdvertisingAgency（仅 homepage）
    if is_homepage:
        agency_desc = "Digital advertising agency helping international brands enter China's market"
        agency = json.dumps({
            "@context": "https://schema.org",
            "@type": "AdvertisingAgency",
            "name": "Tuyue Media Gateway",
            "alternateName": "TMG",
            "url": "https://www.tuyuesouxin.cn/",
            "description": agency_desc,
            "email": "tmg@tuyuesouxin.cn",
            "address": {
                "@type": "PostalAddress",
                "streetAddress": "599-2F202 Wanzhen Road",
                "addressLocality": "Shanghai",
                "addressRegion": "Shanghai",
                "postalCode": "201824",
                "addressCountry": "CN"
            },
            "geo": {
                "@type": "GeoCoordinates",
                "latitude": "31.25099883847901",
                "longitude": "121.37682772821607"
            },
            "openingHoursSpecification": {
                "@type": "OpeningHoursSpecification",
                "dayOfWeek": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"],
                "opens": "09:00",
                "closes": "18:00"
            },
            "priceRange": "$100-$10000"
        }, separators=(',': ''), ensure_ascii=False)
        blocks.append(('AdvertisingAgency', agency))
    
    return blocks

def fix_file(filepath):
    """修复单个文件"""
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # 检测语言
    if '/ja/' in filepath or '\\ja\\' in filepath:
        lang = 'ja'
    elif '/ko/' in filepath or '\\ko\\' in filepath:
        lang = 'ko'
    else:
        lang = 'en'
    
    # 检测是否是 homepage
    is_homepage = filepath.endswith('index.html')
    
    # 删除旧的 JSON-LD 块
    new_lines = []
    in_json_ld = False
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        if '<script type="application/ld+json">' in line:
            in_json_ld = True
            # 找到 </script> 的行
            for j in range(i, len(lines)):
                if '</script>' in lines[j]:
                    i = j + 1
                    break
            continue
        
        if not in_json_ld:
            new_lines.append(line)
        i += 1
    
    # 找到插入位置
    insert_pos = -1
    for i, line in enumerate(new_lines):
        if 'JSON-LD' in line or '<style>' in line:
            insert_pos = i
            break
    
    if insert_pos == -1:
        # 找不到，插入在 </head> 之前
        for i, line in enumerate(new_lines):
            if '</head>' in line:
                insert_pos = i
                break
    
    if insert_pos != -1:
        # 插入正确的 JSON-LD 块
        blocks = get_json_ld_blocks(lang, is_homepage)
        insert_lines = []
        for block_type, block_json in blocks:
            insert_lines.append(f'  <script type="application/ld+json">{block_json}</script>\n')
        insert_lines.append('\n')
        
        for line in reversed(insert_lines):
            new_lines.insert(insert_pos, line)
        
        # 写回
        with open(filepath, 'w', encoding='utf-8') as f:
            f.writelines(new_lines)
        return True
    
    return False

# 收集所有 HTML 文件
html_files = []
for root, dirs, files in os.walk(BASE):
    for file in files:
        if file.endswith('.html'):
            html_files.append(os.path.join(root, file))

print(f"找到 {len(html_files)} 个 HTML 文件")

# 修复所有文件
fixed = 0
for filepath in sorted(html_files):
    try:
        if fix_file(filepath):
            rel_path = os.path.relpath(filepath, BASE)
            print(f"✅ {rel_path}")
            fixed += 1
    except Exception as e:
        print(f"❌ {filepath}: {e}")

print(f"\n总共修复 {fixed} 个文件")
