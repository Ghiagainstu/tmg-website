#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Stats-grid integrity checker and fixer for TMG blog articles.

Usage:
  python verify_stats_grid.py <file_or_directory>  --check    (report issues only)
  python verify_stats_grid.py <file_or_directory>  --fix      (fix issues)
  python verify_stats_grid.py <file_or_directory>  --verify   (check + fix)

Patterns detected:
  1. Nested stat-card (missing label + missing </div>)
  2. Premature grid close (cards outside grid)
  3. Orphan labels (stat-card__label outside any stat-card)
"""

import os, re, sys, argparse
from pathlib import Path


# ── Card extraction ──

CARD_RE = re.compile(
    rb'<div class="stat-card__num">([^<]+)</div>\s*<div class="stat-card__label">(.*?)</div>',
    re.DOTALL,
)


def find_html_stats_grids(c: bytes):
    """Yield (start, end) positions of all HTML (non-CSS) stats-grid divs."""
    idx = 0
    while True:
        idx = c.find(b'<div class="stats-grid">', idx)
        if idx < 0:
            break
        # Skip CSS occurrences
        if b'{' in c[idx:idx + 80] or idx < 800:
            idx += 1
            continue
        # Find matching close via depth counting
        depth = 0
        pos = idx
        while pos < len(c):
            if c[pos:pos + 5] == b'<div ' or c[pos:pos + 5] == b'<div>':
                depth += 1
            elif c[pos:pos + 6] == b'</div>':
                depth -= 1
                if depth == 0:
                    break
            pos += 1
        else:
            idx += 1
            continue
        yield idx, pos + 6
        idx += 1


def extract_cards_from_area(c: bytes, start: int, end: int):
    """Extract (num, label) pairs as (str, str) from a byte range."""
    area = c[start:end]
    cards = []
    for m in CARD_RE.finditer(area):
        num = m[1].decode('utf-8', errors='replace').strip()
        label = re.sub(r'\s+', ' ', m[2].decode('utf-8', errors='replace').strip())
        cards.append((num, label))
    return cards


def check_file(filepath: str) -> list[str]:
    """Return list of issue descriptions. Empty = clean."""
    with open(filepath, 'rb') as f:
        c = f.read()

    issues = []
    for grid_start, grid_close in find_html_stats_grids(c):
        # Issue 1: cards after grid close (premature close)
        next_h2 = c.find(b'<h2', grid_close)
        if next_h2 < 0 or next_h2 > grid_close + 3000:
            next_h2 = grid_close + 1000
        after_area = c[grid_close:next_h2]
        if b'<div class="stat-card">' in after_area:
            cards_after = after_area.count(b'<div class="stat-card__num">')
            issues.append(f'  ⚠️  {cards_after} card(s) outside grid (premature close)')

        # Issue 2: nested cards in grid
        grid_text = c[grid_start:grid_close].decode('utf-8', errors='replace')
        if re.search(r'stat-card__num">[^<\n]{1,80}<div class="stat-card"', grid_text):
            issues.append(f'  ⚠️  Nested stat-card detected (missing </div>)')

        # Issue 3: orphan labels
        nums = CARD_RE.findall(c[grid_start:grid_close])
        label_count = c[grid_start:grid_close].count(b'<div class="stat-card__label">')
        if label_count > len(nums):
            issues.append(f'  ⚠️  {label_count - len(nums)} orphan label(s)')

    return issues


def fix_file(filepath: str) -> bool:
    """Fix stats-grid issues. Returns True if modified."""
    with open(filepath, 'rb') as f:
        c = f.read()

    modified = False

    for grid_start, grid_close in find_html_stats_grids(c):
        # Find end of ALL cards (including orphaned ones after grid close)
        next_h2 = c.find(b'\r\n<h2', grid_start)
        if next_h2 < 0 or next_h2 > grid_start + 3000:
            next_h2 = c.find(b'\n<h2', grid_start)
        if next_h2 < 0 or next_h2 > grid_start + 3000:
            next_h2 = grid_start + 1500

        area = c[grid_start:next_h2]
        cards = extract_cards_from_area(c, grid_start, next_h2)

        if len(cards) < 2:
            continue

        new_grid = b'\r\n<div class="stats-grid">\r\n'
        for num, label in cards:
            new_grid += b'<div class="stat-card">\r\n'
            new_grid += b'<div class="stat-card__num">' + num.encode('utf-8') + b'</div>\r\n'
            new_grid += b'<div class="stat-card__label">' + label.encode('utf-8') + b'</div>\r\n'
            new_grid += b'</div>\r\n'
        new_grid += b'</div>\r\n\r\n'

        c = c[:grid_start] + new_grid + c[next_h2:]
        modified = True

    if modified:
        with open(filepath, 'wb') as f:
            f.write(c)

    return modified


# ── CLI ──

if __name__ == '__main__':
    ap = argparse.ArgumentParser(description='TMG stats-grid checker/fixer')
    ap.add_argument('path', help='File or directory to check')
    ap.add_argument('--check', action='store_true', help='Report issues only')
    ap.add_argument('--fix', action='store_true', help='Fix issues')
    ap.add_argument('--verify', action='store_true', help='Check and fix')
    args = ap.parse_args()

    if not any([args.check, args.fix, args.verify]):
        args.check = True  # default

    def get_files(root):
        p = Path(root)
        if p.is_file():
            return [str(p)]
        return sorted(str(f) for f in p.rglob('*.html') if f.name != 'index.html')

    files = get_files(args.path)
    total_issues = 0
    total_fixed = 0

    for fp in files:
        issues = check_file(fp)
        if issues:
            total_issues += len(issues)
            status = 'FIXED' if (args.fix or args.verify) and fix_file(fp) else 'NEEDS_FIX'
            icon = '✅' if status == 'FIXED' else '⚠️'
            print(f'{icon} {fp}')
            for iss in issues:
                print(iss)
            if status == 'FIXED':
                total_fixed += 1

    print(f'\nFiles with issues: {total_issues} issues in {total_fixed} files')
