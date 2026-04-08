<div align="center">

# roast.skill

> *"AI read all your messages and decided to tell the truth"*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![nexu](https://img.shields.io/badge/nexu-Skill-blueviolet)](https://github.com/nexu-io/nexu)
[![Claude Code](https://img.shields.io/badge/Claude%20Code-Skill-blueviolet)](https://claude.ai/code)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

<br>

Your boss posts motivational quotes at 2 AM and calls it "leadership"?<br>
Your PM writes 500-word Feishu messages that could be one sentence?<br>
Your tech lead's code reviews are just "LGTM" on everything?<br>
Your CEO changes direction every Monday and calls it "agile"?<br>

**Let AI read their data and say what everyone's thinking.**

<br>

Give your AI agent a Twitter/X link, Feishu chat logs, or any public data<br>
Get back a **savage, data-driven roast** — 8 dimensions, 6 rhetoric weapons, zero mercy<br>
Plus a cyberpunk landing page that's begging to be shared

[How It Works](#how-it-works) · [Install](#install) · [Usage](#usage) · [Examples](#examples) · [中文](README.md)

</div>

---

> 🔥 **roast.skill** is part of the [nexu](https://github.com/nexu-io/nexu) ecosystem — an Agent-Native platform where AI stands next to you, not instead of you. Sometimes it stands next to you and roasts you.

---

## What You Get

| Output | Description |
|--------|-------------|
| 🏷️ **Profile Tags** | 8-12 tags across 5 types: company / role / level / MBTI / vibe |
| 🐂 **Niú Mǎ Index** | 0-100 "work-horse" intensity score |
| 🦅 **Species ID** | Absurd animal metaphor ("Bald eagle plugged into a nuclear reactor") |
| 📊 **Ability Bars** | 4 custom metrics with meme-worthy names (e.g. "Delivery: 43%", "Caps Lock: 100%") |
| 🔥 **Main Roast** | 150-250 word savage takedown, second-person, no filter |
| 🔬 **8-Dimension Deep Roast** | Roast / Strengths / Weaknesses / Money / Spirit Animal / Others' View / Famous Person / Life Suggestion |
| 💬 **AI Chat Demo** | 2-round conversation simulating the person's actual voice |
| 🌐 **Landing Page** | Deployable HTML — glassmorphism dark theme, shareable, cyberpunk aesthetic |

---

## How It Works

```
Input Data → Behavior Analysis → Pattern Extraction → Rhetoric Selection → Roast Generation
                                                            ↓
                                                    6 Weapons × 8 Dimensions
                                                            ↓
                                                    Landing Page → Share 🚀
```

### The 6 Rhetoric Weapons

Every roast combines multiple techniques for maximum impact:

| # | Weapon | What it does | Example |
|---|--------|-------------|---------|
| 1 | **Praise-as-Roast** | Compliment on the surface, knife underneath | "Your execution is truly *unmatched* — 5 projects started per day, 0 completed" |
| 2 | **Absurd Analogy** | Ridiculous comparisons that hit close to home | "Your logic is more tangled than my cat's yarn ball" |
| 3 | **Rhetorical Questions** | Questions that answer themselves | "You call this 'pure sharing'? Or growth-hacking disguised as zen?" |
| 4 | **Object-as-Person** | Map objects/animals to behaviors | "Your tweets are like airport self-help books — shocking titles, random content" |
| 5 | **Habit Amplification** | Take a real habit, crank it to 11 | "Your line-break habit has evolved from formatting style to personality trait" |
| 6 | **Classical Quotes** | Wrap poison in proverbs | "Buddha says all beings are equal — but after reading your tweets, Buddha might reconsider" |

**Combo moves > single hits.** Every paragraph uses at least 2 weapons:

> **Praise + Analogy**: "Your diligence is touching — posting 6 inspirational quotes a day with the dedication of the incense vendor outside a temple"

---

## Examples

### 🔗 [Live Demo: Tom's Cyber Avatar](https://distill-campaign.vercel.app/)

### [Elon Musk](examples/elon/)

> "You got 24 million likes with a one-word 'Yes' — not because you said it well, but because you **bought the platform**"

- 🐂🐴 Score: 99/100 · 🦅 Species: Bald eagle plugged into a nuclear reactor
- Tags: `Rocket-recycling entrepreneur` · `Meme cannon` · `100K tweets club` · `DOGE Secretary`
- Delivery: 43% · Meme Power: 97% · Sleep: 6%

### [Donald Trump](examples/trump/)

> "You're not governing — you're running **an emotion panel with only two buttons: GREAT and TERRIBLE**"

- 🐂🐴 Score: 85/100 · 🦅 Species: Bald eagle in a suit
- Tags: `MAGA perpetual motion` · `ALL CAPS diplomat` · `Tariff King` · `Surrender: 0%`
- Slogan Power: 99% · Caps Lock: 100% · Diplomacy: 3%

### [Tom — CEO, nexu](examples/tom/)

> "You're not a CEO — you're a **group chat bot that got admin privileges**"

- 🐂🐴 Score: 94/100 · 🦉 Species: Midnight Perpetual Motion Machine
- Tags: `Midnight CEO` · `Human RSS feed` · `[smirk] addict` · `DDoS communicator`

---

## Install

### nexu / OpenClaw (Recommended)

Just send the GitHub link to your nexu agent:

```
Install this skill: https://github.com/nexu-io/roast-skill
```

Or via CLI:

```bash
openclaw skill install https://github.com/nexu-io/roast-skill
```

### Claude Code

```bash
mkdir -p .claude/skills
git clone https://github.com/nexu-io/roast-skill .claude/skills/roast-skill
```

### Manual

```bash
git clone https://github.com/nexu-io/roast-skill <your agent skills directory>
```

No dependencies — pure prompt skill, works immediately after install.

---

## Usage

### Quick Roast (from Twitter)

Tell your agent:

```
Roast this person: https://x.com/elonmusk
```

The agent will:
1. Fetch profile + recent tweets
2. Analyze behavior patterns, language style, posting habits
3. Generate full roast report with 8 dimensions
4. Create a shareable landing page (optional)

### Full Roast (with Feishu/Slack data)

```
Use roast-skill to roast [name]
Data: Feishu messages [N] + Twitter @[username]
```

### Generate Landing Page

```
Generate a landing page for the roast, use the cyber avatar template
```

→ The agent will create an HTML file using the `assets/template.html` template and handle deployment automatically.

---

## Supported Data Sources

| Source | Auto-Collect | Manual Input |
|--------|:------------:|:------------:|
| Twitter/X | ✅ twitter-cli | ✅ Paste tweets |
| Feishu | ✅ API | ✅ Paste messages |
| Slack | ✅ API | ✅ Paste messages |
| Articles/URLs | ✅ Fetch | ✅ Paste text |
| GitHub | ✅ gh CLI | ✅ Paste README |
| Podcasts | — | ✅ Paste transcript |

---

## Notes

- **Data quality = Roast quality**: Real chat logs + tweets >> manual description
- Prioritize: **decision-making messages** > **long-form writing by them** > casual chat
- Public figures work best (more data, more patterns)
- The roast is meant to be sharp but not malicious — **funny > mean**
- Best results with bilingual agents (Chinese roast culture hits different)

---

## Project Structure

```
roast-skill/
├── SKILL.md              # Agent skill entry point
├── README.md             # English docs
├── README_ZH.md          # 中文文档
├── LICENSE               # MIT License
├── assets/
│   └── template.html     # Landing page template (glassmorphism dark theme)
└── examples/
    ├── elon/             # Elon Musk roast
    │   └── roast.md
    ├── trump/            # Donald Trump roast
    │   └── roast.md
    └── tom/              # Tom (nexu CEO) roast
        └── roast.md
```

---

## Star History

<a href="https://www.star-history.com/?repos=nexu-io%2Froast-skill&type=date&legend=top-left">
 <picture>
   <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/image?repos=nexu-io/roast-skill&type=date&theme=dark&legend=top-left" />
   <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/image?repos=nexu-io/roast-skill&type=date&legend=top-left" />
   <img alt="Star History Chart" src="https://api.star-history.com/image?repos=nexu-io/roast-skill&type=date&legend=top-left" />
 </picture>
</a>

---

## Contributing

PRs welcome! You can contribute:
- 🔥 New example roasts in `examples/`
- 🌐 Translations
- 🎨 Landing page theme variants in `assets/`
- ⚔️ New rhetoric weapon patterns

---

<div align="center">

MIT License © [nexu](https://github.com/nexu-io)

Made with 🔥 by [nexu](https://github.com/nexu-io/nexu)

**AI that stands next to you — and occasionally roasts you**

⭐ [Star this repo](https://github.com/nexu-io/roast-skill) · ⭐ [Star nexu](https://github.com/nexu-io/nexu)

</div>
