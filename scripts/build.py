#!/usr/bin/env python3
"""
ruiz00.io Build Script
----------------------
Converts Markdown writeups to HTML pages and regenerates writeups-data.js
Run: python scripts/build.py
"""

import os
import json
import yaml
import re
import markdown
from pathlib import Path
from jinja2 import Template
from datetime import datetime

ROOT = Path(__file__).parent.parent
WRITEUPS_DIR = ROOT / "writeups"
ASSETS_DIR = ROOT / "assets"
DATA_OUT = ASSETS_DIR / "js" / "writeups-data.js"

# ─── HTML TEMPLATE FOR WRITEUP PAGES ─────────────────────────────────────────
WRITEUP_TEMPLATE = Template("""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{{ title }} — {{ type_label }} // ruiz00</title>
  <meta name="description" content="{{ summary }}" />
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@400;700;900&family=Rajdhani:wght@300;400;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="{{ depth }}assets/css/style.css" />
</head>
<body>
  <div class="scanlines"></div>
  <div style="position:relative;z-index:1;">
    <nav class="nav-bar">
      <div class="nav-brand">
        <span class="bracket">[</span>
        <span class="brand-text"><a href="{{ depth }}index.html" style="color:inherit;text-decoration:none;">ruiz00</a></span>
        <span class="bracket">]</span>
      </div>
      <div class="nav-links">
        <a href="{{ depth }}index.html#writeups" class="nav-link">writeups</a>
        <a href="{{ depth }}index.html#about" class="nav-link">whoami</a>
        <a href="https://app.hackthebox.com" target="_blank" class="nav-link nav-htb">HTB ↗</a>
      </div>
    </nav>
    <div class="writeup-page">
      <a href="{{ depth }}index.html#writeups" class="back-btn">← back to writeups</a>
      <div style="display:flex;gap:1rem;align-items:center;margin-bottom:1rem;">
        <span class="card-type type-{{ type }}">{{ type_label }}</span>
        <span class="card-diff diff-{{ difficulty }}">{{ difficulty | upper }}</span>
        {% if os %}<span style="font-size:11px;color:var(--text-dim);">{{ os }}</span>{% endif %}
        {% if event %}<span style="font-size:11px;color:var(--text-dim);">{{ event }}</span>{% endif %}
      </div>
      <h1>{{ title }}</h1>
      <div class="meta">
        <span>Date: {{ date }}</span>
        {% if points %}<span>Points: {{ points }}</span>{% endif %}
        {% if tags %}<span>Tags: {{ tags | join(' · ') }}</span>{% endif %}
      </div>
      <div class="content">
        {{ content }}
      </div>
    </div>
  </div>
</body>
</html>""")

def parse_frontmatter(text):
    """Extract YAML frontmatter from markdown file."""
    match = re.match(r'^---\s*\n(.*?)\n---\s*\n', text, re.DOTALL)
    if match:
        meta = yaml.safe_load(match.group(1))
        body = text[match.end():]
        return meta, body
    return {}, text

def slug_from_path(path):
    return path.stem

def process_writeup(md_path):
    """Convert a .md writeup to HTML and return metadata dict."""
    text = md_path.read_text(encoding='utf-8')
    meta, body = parse_frontmatter(text)
    
    if not meta.get('title'):
        return None
    
    # Calculate relative depth
    rel = md_path.relative_to(WRITEUPS_DIR)
    depth = '../../'  # writeups/type/file.md → back to root
    
    # Convert markdown to HTML
    html_content = markdown.markdown(
        body,
        extensions=['fenced_code', 'codehilite', 'tables', 'toc']
    )
    
    wtype = meta.get('type', 'htb')
    type_label = 'HackTheBox' if wtype == 'htb' else 'CTF'
    slug = slug_from_path(md_path)
    
    # Render HTML page
    html = WRITEUP_TEMPLATE.render(
        title=meta.get('title', slug),
        type=wtype,
        type_label=type_label,
        difficulty=meta.get('difficulty', 'easy'),
        os=meta.get('os', ''),
        event=meta.get('event', ''),
        date=str(meta.get('date', '')),
        points=meta.get('points', 0),
        tags=meta.get('tags', []),
        summary=meta.get('summary', ''),
        content=html_content,
        depth=depth
    )
    
    # Write HTML file
    out_path = md_path.parent / (slug + '.html')
    out_path.write_text(html, encoding='utf-8')
    print(f"  ✓ {out_path.relative_to(ROOT)}")
    
    # Return metadata for writeups-data.js
    return {
        'id': slug,
        'title': meta.get('title', slug),
        'type': wtype,
        'category': meta.get('category', [wtype]),
        'difficulty': meta.get('difficulty', 'easy'),
        'date': str(meta.get('date', '')),
        'os': meta.get('os', ''),
        'event': meta.get('event', ''),
        'points': meta.get('points', 0),
        'summary': meta.get('summary', ''),
        'tags': meta.get('tags', []),
        'url': f"writeups/{wtype}/{slug}.html",
        'retired': meta.get('retired', False)
    }

def build():
    print("🔨 Building ruiz00.io...\n")
    
    all_writeups = []
    
    for folder in ['htb', 'ctf']:
        folder_path = WRITEUPS_DIR / folder
        if not folder_path.exists():
            folder_path.mkdir(parents=True)
            continue
        
        print(f"📁 Processing writeups/{folder}/")
        for md_file in sorted(folder_path.glob('*.md')):
            if md_file.stem.startswith('_'):
                continue  # skip templates
            meta = process_writeup(md_file)
            if meta:
                all_writeups.append(meta)
    
    # Sort by date descending
    all_writeups.sort(key=lambda x: x.get('date', ''), reverse=True)
    
    # Write writeups-data.js
    js_content = "// AUTO-GENERATED by scripts/build.py — DO NOT EDIT MANUALLY\n"
    js_content += "// Run: python scripts/build.py\n\n"
    js_content += "window.WRITEUPS = "
    js_content += json.dumps(all_writeups, indent=2, ensure_ascii=False)
    js_content += ";\n"
    
    DATA_OUT.write_text(js_content, encoding='utf-8')
    print(f"\n✅ Generated {DATA_OUT.relative_to(ROOT)} ({len(all_writeups)} writeups)")
    print("✅ Build complete!\n")

if __name__ == '__main__':
    build()
