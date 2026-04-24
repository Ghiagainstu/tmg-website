#!/usr/bin/env python3
"""Sync header CSS + JS from homepage to all blog detail pages."""
import re

# Files to fix
FILES = [
    'blog/ocean-engine-local-reach.html',
    'blog/ocean-engine-overview.html',
    'blog/douyin-enterprise-account.html',
    'blog/pangle-ads.html',
]

def extract_homepage_header_css(html):
    """Extract the complete header CSS block from homepage."""
    # Find .header__logo-text span { ... } section up to .header__toggle
    start = html.index('.header__logo-text span {')
    end = html.index('.header__toggle {', start)
    # Find the whole rule block (back up to .header { or wherever it starts)
    # Actually find the block from .header (the header rule)
    m = re.search(r'(\n    /\* ── Header ── \*/.*?\n    \.header__toggle \{)', html, re.DOTALL)
    if not m:
        # Try alternative approach - from .header through .header__toggle
        m = re.search(r'(\n    \.header \{.*?\n    \.header__toggle \{)', html, re.DOTALL)
    if not m:
        # Last resort: find .header__logo-text through .header__toggle
        m = re.search(r'(\n    \.header__logo-text span.*?\n    \.header__toggle \{)', html, re.DOTALL)
    return m.group(1) + '\n    }' if m else None

def find_and_replace_header_css(html, new_css):
    """Replace the header CSS block in a blog page with homepage CSS."""
    # Pattern: from /* ── Header ── */ comment or .header { through .header__toggle { ... }
    # We need to find the section that covers header styles and replace it

    # Look for .header { ... .header__toggle { in the blog page
    # This covers everything from .header through the mobile media query that includes .header__toggle

    # Find the start: either /* ── Header ── */ comment or .header {
    pattern = r'(\n    /\* ── Header ── \*/\s*\n    \.header \{.*?\n    @media \(max-width: 900px\) \{.*?\.header__toggle.*?\n    \})'
    m = re.search(pattern, html, re.DOTALL)

    if not m:
        # Try to find .header { ... } and .header__toggle together
        pattern2 = r'(\n    \.header \{.*?\.header__toggle \{.*?\n    \})'
        m = re.search(pattern2, html, re.DOTALL)

    if not m:
        # Try finding just the .header rule up to next major section
        pattern3 = r'(\n    \.header \{.*?\n    \.header__toggle \{.*?)(?=\n    \.header__cta|\n    /\* ── )'
        m = re.search(pattern3, html, re.DOTALL)

    if m:
        old_block = m.group(1)
        print(f"  Found header block at char {m.start()}-{m.end()}, len={len(old_block)}")
        return html.replace(old_block, new_css), True
    else:
        print("  WARNING: Could not find header CSS block to replace!")
        # Print around .header
        idx = html.find('.header { ')
        if idx > 0:
            print(f"  Found .header at {idx}: {html[idx:idx+200]}")
        return html, False

def fix_header_js(html):
    """Fix the header toggle JS in blog pages to match homepage."""
    # Blog pages have old .nav__dropdown-trigger JS, replace with homepage JS
    old_js = """  // Mobile nav toggle
  var toggle = document.querySelector('.header__toggle');
  var nav = document.querySelector('.header__nav');
  if (toggle && nav) {
    toggle.addEventListener('click', function() {
      nav.classList.toggle('active');
      this.classList.toggle('active');
    });
  }

  // Dropdown close on outside click
  document.addEventListener('click', function(e) {
    if (!e.target.closest('.header__dropdown')) {
      document.querySelectorAll('.header__dropdown').forEach(function(d) { d.classList.remove('open'); });
    }
  });

  // Mobile dropdown toggle
  document.querySelectorAll('.header__dropdown > .header__nav-link').forEach(function(trigger) {
    trigger.addEventListener('click', function(e) {
      e.preventDefault();
      var dropdown = this.parentElement;
      dropdown.classList.toggle('open');
    });
  });"""

    # Homepage has different JS - find it
    # The homepage has a more complex script that we need to use
    return html  # Keep existing JS for now, just fix CSS

def main():
    with open('index.html', 'r', encoding='utf-8') as f:
        homepage = f.read()

    # Extract header CSS from homepage
    # Find from /* ── Header ── */ to .header__toggle { ... } (including media query)
    pattern = r'(\n    /\* ── Header ── \*/.*?\.header__toggle \{[^}]+\})'
    m = re.search(pattern, homepage, re.DOTALL)
    if not m:
        print("ERROR: Could not find header CSS in homepage")
        return

    header_css = m.group(1)
    print(f"Extracted homepage header CSS, len={len(header_css)}")
    print(f"Preview: {header_css[:100]}...")

    for filepath in FILES:
        print(f"\nProcessing {filepath}...")
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        new_content, ok = find_and_replace_header_css(content, header_css)
        if ok:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  ✓ Fixed {filepath}")
        else:
            print(f"  ✗ Could not fix {filepath}")

if __name__ == '__main__':
    main()