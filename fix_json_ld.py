#!/usr/bin/env python3
"""
修复所有 HTML 文件的 JSON-LD 结构化数据
问题：URL 被截断，JSON 语法错误（缺少逗号、引号位置错误）
修复：完全重写三个 JSON-LD 块
"""
import os
import json
import re

BASE = "."

def get_correct_json_ld(lang='en'):
    """根据语言返回正确的 JSON-LD 块（minified）"""
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
    }, separators=(',', ':'))
    
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
    }, separators=(',', ':'))
    
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
    }, separators=(',', ':'))
    
    return org, website, agency

def fix_json_ld(content, lang='en'):
    """修复内容中的 JSON-LD 块"""
    org, website, agency = get_correct_json_ld(lang)
    
    # 替换 Organization JSON-LD
    pattern1 = r'<script type="application/ld\+json">\{.*?"Organization".*?\}</script>'
    repl1 = f'<script type="application/ld+json">{org}</script>'
    content = re.sub(pattern1, repl1, content, flags=re.DOTALL)
    
    # 替换 WebSite JSON-LD
    pattern2 = r'<script type="application/ld\+json">\{.*?"WebSite".*?\}</script>'
    repl2 = f'<script type="application/ld+json">{website}</script>'
    content = re.sub(pattern2, repl2, content, flags=re.DOTALL)
    
    # 替换 AdvertisingAgency JSON-LD
    pattern3 = r'<script type="application/ld\+json">\{.*?"AdvertisingAgency".*?\}</script>'
    repl3 = f'<script type="application/ld+json">{agency}</script>'
    content = re.sub(pattern3, repl3, content, flags=re.DOTALL)
    
    return content

def detect_lang(filepath):
    """根据文件路径检测语言"""
    if '/ja/' in filepath or '\\ja\\' in filepath:
        return 'ja'
    elif '/ko/' in filepath or '\\ko\\' in filepath:
        return 'ko'
    else:
        return 'en'

def fix_file(filepath):
    """修复单个文件"""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    lang = detect_lang(filepath)
    content = fix_json_ld(content, lang)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
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
