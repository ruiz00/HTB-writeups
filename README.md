Here is a **refactored and improved README.md** derived from your `index.html`, aligning documentation with the actual UI/UX, sections, and functionality of your site:

---

# ruiz00.io — Security Research Writeups 

> HTB writeups · Penetration testing · Security research

**Live site:** [https://ruiz00.github.io](https://ruiz00.github.io)

---

## 🧠 Overview

This project is a **personal security research portfolio** showcasing:

* HackTheBox (HTB) writeups
* Exploit development notes
* Offensive security skills progression
* Public research and methodology

The site is designed with a **terminal / cyberpunk aesthetic**, featuring dynamic UI elements like:

* Matrix-style animated background
* Glitch effects
* Interactive filtering system
* Live stats and skill tracking

---

## ⚙️ Features

### 🔹 Hero Section

* Terminal-style intro (`root@ruiz00:~$`)
* Identity: *Security Researcher / Pentester*
* Quick access to writeups and HTB profile

### 🔹 About

* Terminal-styled profile (`whoami.sh`)
* Focus areas:

  * Web Exploitation
  * Reverse Engineering
  * Active Directory
  * Privilege Escalation
  * OSINT, Crypto, Forensics

### 🔹 Writeups System

* Dynamic card-based layout
* Filters:

  * Difficulty (Easy → Insane)
  * Search functionality
* Metadata per writeup:

  * OS (Linux/Windows)
  * Tags (CVE, RCE, PrivEsc, etc.)
  * Date
* Example:

  * *Kobold* → API RCE + Docker socket privilege escalation 

### 🔹 Stats Dashboard

Tracks progression:

* Boxes Pwned
* User / Root flags
* HTB Points

Includes:

* Skill level bars
* Rank progression system (e.g., Script Kiddie → …)

### 🔹 Contact Section

* GitHub
* Twitter / X
* HackTheBox profile
* Optional PGP key block

---

## 🧩 Tech Stack

### Frontend

* HTML5 (single-page structure)
* CSS3 (custom cyberpunk UI)
* Vanilla JavaScript

### Assets

```
assets/
├── css/main.css
├── js/
│   ├── main.js
│   └── matrix.js
```

### Features Implemented in JS

* Typing animation
* Matrix canvas rendering
* Writeup filtering & search
* Animated counters (stats)

---

## 📁 Project Structure

```
ruiz00.github.io/
├── index.html              # Main UI (SPA layout)
├── assets/
│   ├── css/
│   │   └── main.css
│   └── js/
│       ├── main.js
│       └── matrix.js
├── writeups/
│   ├── htb/
│   └── ctf/
├── scripts/
│   └── build.py            # Markdown → HTML generator
├── .github/
│   └── workflows/
│       ├── deploy.yml
│       └── new-writeup.yml
```

---

## ✍️ Writeups Workflow

### Manual

```bash
cp writeups/htb/_template.md writeups/htb/<machine>.md
python scripts/build.py
git commit -m "add writeup"
git push
```

### Automated (GitHub Actions)

* Go to **Actions → New Writeup Helper**
* Fill the form
* File is scaffolded and deployed automatically

---

## 🔎 Writeup Format

Each writeup includes:

* Title
* Difficulty
* OS
* Tags (CVE, techniques)
* Summary
* Exploitation steps
* Privilege escalation path

---

## 📊 Design Philosophy

This project emphasizes:

* **Clarity of exploitation steps**
* **Minimal dependencies (no frameworks)**
* **Performance-first frontend**
* **Readable + searchable knowledge base**

---

## 🔒 Policy Reminder (HTB)

Only publish writeups for:

✔ Retired machines
❌ Active machines (violates HTB ToS)

---

## 🚀 Deployment

* Hosted via **GitHub Pages**
* Auto-deploy on push to `main` via GitHub Actions

---

## 📬 Contact

* GitHub: [https://github.com/ruiz00](https://github.com/ruiz00)
* HTB: [https://app.hackthebox.com/profile/](https://app.hackthebox.com/profile/)
* Twitter/X: [https://twitter.com/ruiz00](https://twitter.com/ruiz00)


## 💡 Quote

> “The quieter you become, the more you can hear.”


