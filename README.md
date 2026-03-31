# ruiz00.io — Security Research Blog

> HTB writeups · Exploit development

**Live site:** https://ruiz00.github.io

---

## 🚀 Quick Start

### Setup
```bash
git clone https://github.com/ruiz00/ruiz00.github.io
cd ruiz00.github.io
```

### Add a writeup (manual)
1. Copy the template:
```bash
cp writeups/htb/_template.md writeups/htb/machine-name.md
# or
cp writeups/ctf/_template.md writeups/ctf/challenge-name.md
```
2. Edit the file with your writeup
3. Run the build script locally:
```bash
pip install markdown pyyaml jinja2
python scripts/build.py
```
4. Commit & push → CI/CD deploys automatically

### Add a writeup (via GitHub Actions)
Go to **Actions → New Writeup Helper → Run workflow**
Fill in the form → scaffold file is created and committed automatically.

---

## 📁 Project Structure

```
ruiz00.github.io/
├── index.html                    # Main site
├── assets/
│   ├── css/style.css             # All styles
│   └── js/
│       ├── main.js               # Site logic
│       └── writeups-data.js      # Auto-generated writeup index
├── writeups/
│   ├── htb/
│   │   ├── _template.md          # HTB writeup template
│   │   └── *.md / *.html         # Your writeups (md=source, html=generated)
├── scripts/
│   └── build.py                  # Markdown → HTML converter + data generator
└── .github/
    └── workflows/
        ├── deploy.yml            # Auto-deploy on push to main
        └── new-writeup.yml       # Scaffold new writeup via UI
```

---

## 📝 Writeup Frontmatter Reference

### HTB
```yaml
---
title: "Machine Name"
type: htb
difficulty: easy        # easy | medium | hard | insane
os: Linux               # Linux | Windows | FreeBSD
date: 2024-01-01
points: 20
tags: [samba, metasploit, CVE-2007-2447]
summary: "One-line summary for the card view."
retired: true           # true = machine is retired (safe to publish)
---

---

## ⚙️ GitHub Pages Setup

1. Go to **Settings → Pages**
2. Source: **GitHub Actions**
3. Push to `main` — the site deploys automatically

---

## 🔒 HTB Policy Reminder

Only publish writeups for **retired machines**. Active machine writeups violate HTB ToS.

---

*Built with ♦ and `nmap`*
