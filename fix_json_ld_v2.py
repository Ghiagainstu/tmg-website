#!/usr/bin/env python3
"""
修复所有 HTML 文件的 JSON-LD 结构化数据（正确版本）
"""
import os
import json
import re

BASE = "."

def get_correct_json_ld(lang='en'):
    """根据语言返回正确的 JSON-LD 块（minified，非 ASCII 不转义）"""
    if lang == 'ja':
        site_name = "Tuyue Media Gateway"
        description = "国際代理店向け中国デジタル広告の統合インターフェース。1つの接続で全プラットフォーム対応。"
        agency_description = "国際ブランドの中国市場進出を支援するデジタル広告代理店"
    elif lang == 'ko':
        site_name = "Tuyue Media Gateway"
        description = "국제 에이전시를 위한 중국 디지털 광고 통합 인터페이스. 하나의 연결로 모든 플랫폼 대응."
        agency_description = "국제 브랜드의 중국 시장 진출을 돕는 디지털 광고 대행사"
    else:  # en
        site_name = "Tuyue Media Gateway"
        description = "The unified media interface for international agencies entering China's digital advertising market. One connection, all platforms."
        agency_description = "Digital advertising agency helping international brands enter China's market"
    
    # Organization
    org = json.dumps({
        "@context": "https://schema.org",
        "@type": "Organization",
        "name": site_name,
        "alternateName": "TMG",
        "url": "https://www.tuyuesouxin.cn/",
        "description": description,
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
    
    # WebSite
    website = json.dumps({
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": site_name,
        "url": "https://www.tuyuesouxin.cn/",
        "potentialAction": {
            "@type": "SearchAction",
            "target": "https://www.tuyuesouxin.cn/search?q={search_term_string}",
            "query-input": "required name=search_term_string"
        }
    }, separators=(',', ':'), ensure_ascii=False)
    
    # AdvertisingAgency
    agency = json.dumps({
        "@context": "https://schema.org",
        "@type": "AdvertisingAgency",
        "name": site_name,
        "alternateName": "TMG",
        "url": "https://www.tuyuesouxin.cn/",
        "description": agency_description,
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
    }, separators=(',', ':'), ensure_ascii=False)
    
    return org, website, agency

def fix_file(filepath):
    """修复单个文件"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    
    # 检测语言
    if '/ja/' in filepath or '\\ja\\' in filepath:
        lang = 'ja'
    elif '/ko/' in filepath or '\\ko\\' in filepath:
        lang = 'ko'
    else:
        lang = 'en'
    
    org, website, agency = get_correct_json_ld(lang)
    
    # 用简单的字符串替换（不用 regex）
    # 找到 <script type="application/ld+json"> 和 </script> 之间的内容
    
    # Organization
    start_tag = '<script type="application/ld+json">'
    end_tag = '</script>'
    
    # 分割内容，找到所有 JSON-LD 块
    parts = content.split(start_tag)
    new_parts = [parts[0]]  # 第一个部分（head 之前的内容）
    
    org_done = False
    website_done = False
    agency_done = False
    
    for part in parts[1:]:
        if '</script>' not in part:
            new_parts.append(part)
            continue
        
        script_content, rest = part.split('</script>', 1)
        
        # 判断是哪个类型的 JSON-LD
        if '"Organization"' in script_content and not org_done:
            new_parts.append(start_tag + org + end_tag + rest)
            org_done = True
        elif '"WebSite"' in script_content and not website_done:
            new_parts.append(start_tag + website + end_tag + rest)
            website_done = True
        elif '"AdvertisingAgency"' in script_content and not agency_done:
            new_parts.append(start_tag + agency + end_tag + rest)
            agency_done = True
        else:
            # 不是这三个之一，保持原样
            new_parts.append(start_tag + script_content + end_tag + rest)
    
    new_content = ''.join(new_parts)
    
    if new_content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
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
