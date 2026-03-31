#!/usr/bin/env python3
"""
generate_index.py
Scans writeups/ directories and auto-generates index data.
Run by CI/CD pipeline before build.
"""

import os
import re
import json
from pathlib import Path
from datetime import datetime


def extract_meta(filepath):
    """Extract metadata from an HTML writeup file."""
    meta = {
        "title": "Unknown",
        "category": "unknown",
        "difficulty": "unknown",
        "os": "unknown",
        "date": "",
        "tags": [],
        "path": str(filepath),
        "url": str(filepath).replace("\\", "/"),
    }

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        # Extract title from <title> tag
        title_match = re.search(r"<title>([^<]+)</title>", content)
        if title_match:
            meta["title"] = title_match.group(1).replace(" — ruiz00 Writeup", "").strip()

        # Extract difficulty
        for diff in ["easy", "medium", "hard", "insane"]:
            if f'card-diff {diff}' in content:
                meta["difficulty"] = diff
                break

        # Extract OS
        if "🐧" in content or "linux" in content.lower():
            meta["os"] = "Linux"
        elif "🪟" in content or "windows" in content.lower():
            meta["os"] = "Windows"

        # Extract tags
        tag_matches = re.findall(r'<span class="tag">([^<]+)</span>', content)
        meta["tags"] = tag_matches[:5]

        # Extract date
        date_match = re.search(r"Published:\s*([\d-]+)", content)
        if date_match:
            meta["date"] = date_match.group(1)

    except Exception as e:
        print(f"  Warning: Could not parse {filepath}: {e}")

    return meta


def generate_index():
    root = Path(__file__).parent.parent

    writeups = []
    stats = {"htb": 0, "ctf": 0, "total": 0}

    for category in ["htb", "ctf"]:
        cat_dir = root / "writeups" / category
        if not cat_dir.exists():
            print(f"  Creating directory: {cat_dir}")
            cat_dir.mkdir(parents=True, exist_ok=True)
            continue

        for html_file in sorted(cat_dir.glob("*.html")):
            if html_file.name == "template.html":
                continue

            print(f"  Found: {html_file.name}")
            meta = extract_meta(html_file)
            meta["category"] = category
            meta["url"] = f"writeups/{category}/{html_file.name}"
            writeups.append(meta)
            stats[category] += 1

    stats["total"] = stats["htb"] + stats["ctf"]

    # Sort by date (newest first)
    writeups.sort(key=lambda x: x["date"], reverse=True)

    # Write JSON data file for dynamic loading
    data_dir = root / "assets" / "data"
    data_dir.mkdir(parents=True, exist_ok=True)

    output = {
        "generated": datetime.now().isoformat(),
        "stats": stats,
        "writeups": writeups,
    }

    output_path = data_dir / "writeups.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)

    print(f"\n✅ Generated index with {stats['total']} writeups")
    print(f"   HTB: {stats['htb']} | CTF: {stats['ctf']}")
    print(f"   Output: {output_path}")

    return output


if __name__ == "__main__":
    generate_index()
