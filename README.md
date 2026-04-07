<div align="center">

# 锐评.skill

> *"AI 读完了你所有消息，决定说实话了"*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![nexu](https://img.shields.io/badge/nexu-Skill-blueviolet)](https://github.com/nexu-io/nexu)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

<br>

Give your AI agent a Twitter/X profile link or Feishu chat history<br>
Get back a **savage, data-driven roast** with 8-dimension deep analysis<br>
Plus a shareable landing page that looks like a cyberpunk business card

[Features](#features) · [Install](#install) · [Usage](#usage) · [Demo](#demo) · [中文](README_ZH.md)

</div>

---

## What It Does

Feed your AI agent someone's public data (tweets, Feishu messages, articles), and it generates:

| Output | Description |
|--------|-------------|
| **Profile Tags** | 8-12 tags across 5 types (company/role/level/MBTI/vibe) |
| **Niú Mǎ Index** | 0-100 "work-horse" intensity score |
| **Species ID** | Absurd animal metaphor (e.g. "Midnight Perpetual Motion Machine") |
| **Ability Bars** | 4 custom metrics with meme-worthy labels |
| **Main Roast** | 150-250 word savage takedown, second-person |
| **8-Dimension Deep Roast** | Roast / Strengths / Weaknesses / Money / Spirit Animal / Others' Perspective / Famous Person / Life Suggestion |
| **AI Chat Demo** | 2-round simulated conversation in the person's style |
| **Landing Page** | Deployable HTML with glassmorphism dark theme |

### The 6 Rhetoric Weapons

Every roast combines multiple techniques:

1. **Praise-as-Roast** — Compliment on the surface, knife underneath
2. **Absurd Analogy** — Ridiculous comparisons that hit close to home
3. **Rhetorical Questions** — Questions that answer themselves
4. **Object-as-Person** — Map objects/animals to behaviors
5. **Habit Amplification** — Take a real habit, crank it to 11
6. **Classical Quotes** — Wrap poison in proverbs

Best results come from **combo moves**: Praise + Analogy, Question + Habit, Quote + Object.

---

## Demo

🔗 **[Live Demo: Tom's Cyber Avatar](https://distill-campaign.vercel.app/)**

<img src="assets/demo-screenshot.png" width="360" alt="Demo screenshot">

---

## Install

### nexu (OpenClaw)

```bash
git clone https://github.com/nexu-io/roast-skill ~/.nexu/skills/roast-skill
```

### Claude Code

```bash
mkdir -p .claude/skills
git clone https://github.com/nexu-io/roast-skill .claude/skills/roast-skill
```

---

## Usage

### Quick Roast (from Twitter)

Tell your agent:

```
锐评一下这个人：https://x.com/lifesinger
```

The agent will:
1. Fetch the user's profile + recent tweets
2. Analyze behavior patterns, language style, posting habits
3. Generate the full roast report
4. Optionally create a shareable landing page

### Full Roast (with Feishu data)

```
用 roast-skill 锐评一下 [名字]
数据来源：飞书消息 [N] 条 + 推特 @[username]
```

### Generate Landing Page

```
把锐评结果生成一个落地页，用赛博分身模板
```

The agent will create an HTML file using the `assets/template.html` glass-morphism template and can deploy to Vercel.

---

## Supported Data Sources

| Source | Auto-Collect | Manual Input |
|--------|:------------:|:------------:|
| Twitter/X | ✅ (via twitter-cli) | ✅ Paste tweets |
| Feishu | ✅ (via API) | ✅ Paste messages |
| Articles | ✅ (via URL fetch) | ✅ Paste text |
| GitHub | ✅ (via gh CLI) | ✅ Paste README |
| Podcasts | — | ✅ Paste transcript |

---

## Examples

### [Tom (CEO, nexu)](examples/tom/)

> "你不是 CEO，你是一个获得了管理权限的群聊机器人"

- 🐂🐴 牛马指数: 94/100
- 🦉 物种: 午夜永动机
- Tags: 午夜CEO · 人形RSS · [坏笑]成瘾 · DDoS沟通

### [玉伯 (Founder, YouMind)](examples/yubo/)

> "你的推特不是社交媒体，是一本没有页码的禅宗语录"

- 🐂🐴 牛马指数: 72/100
- 🧘 物种: 赛博禅师
- Tags: 推特诗人 · 自黑大师 · 鸡汤酿造师 · 同行点火员

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
    ├── tom/              # Tom (nexu CEO) roast example
    │   └── roast.md
    └── yubo/             # 玉伯 (YouMind Founder) roast example
        └── roast.md
```

---

## How It Works

```
Input Data → Behavior Analysis → Pattern Extraction → Rhetoric Selection → Roast Generation
                                                            ↓
                                                    6 Weapons × 8 Dimensions
                                                            ↓
                                                    Landing Page (optional)
```

The skill instructs the AI agent to:
1. Extract behavioral patterns from data (posting frequency, active hours, word habits, emoji usage)
2. Select the most distinctive 3-4 traits
3. Apply rhetoric weapons in combinations (combos > singles)
4. Generate each dimension with data-backed specifics
5. Ensure tone: sharp but not malicious, memeable but grounded in truth

---

## Contributing

PRs welcome! You can contribute:
- New example roasts in `examples/`
- Translations
- Landing page theme variants in `assets/`
- New rhetoric weapon patterns

---

## License

MIT License — roast responsibly.

---

<div align="center">

Made with 🔥 by [nexu](https://github.com/nexu-io/nexu)

**AI that stands next to you — and occasionally roasts you**

⭐ Star this repo · ⭐ [Star nexu](https://github.com/nexu-io/nexu)

</div>
