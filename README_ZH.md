<div align="center">

# 锐评.skill

> *"AI 读完了你所有消息，决定说实话了"*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![nexu](https://img.shields.io/badge/nexu-Skill-blueviolet)](https://github.com/nexu-io/nexu)
[![AgentSkills](https://img.shields.io/badge/AgentSkills-Standard-green)](https://agentskills.io)

<br>

给你的 AI agent 一个推特链接或飞书消息记录<br>
它会生成一份**毒舌但精准的锐评报告**，8 个维度深度扒皮<br>
还能一键生成赛博朋克风格的分享落地页

[功能](#功能) · [安装](#安装) · [使用](#使用) · [示例](#示例) · [English](README.md)

</div>

---

## 功能

给 AI agent 喂入一个人的公开数据（推特、飞书消息、文章），生成：

| 输出 | 说明 |
|------|------|
| **Profile 标签** | 8-12 个标签，分 5 种类型（公司/岗位/职级/MBTI/性格） |
| **牛马指数** | 0-100 工作强度评分 |
| **物种鉴定** | 荒诞动物比喻（如"午夜永动机""赛博禅师"） |
| **能力条** | 4 项自定义指标，命名要有梗 |
| **主 Roast** | 150-250 字毒舌吐槽，第二人称直接开怼 |
| **8 维度深度扒皮** | Roast / 优势 / 弱点 / 金钱观 / 灵魂动物 / 同事视角 / 名人对标 / 人生建议 |
| **AI 对话示例** | 2 轮模拟对话，还原本人说话风格 |
| **落地页** | 可部署的 HTML，深色毛玻璃赛博风 |

### 🎯 6 大阴阳怪气修辞武器

每段吐槽混合使用多种技巧，组合连招比单招更毒：

| 武器 | 说明 | 示例 |
|------|------|------|
| **以夸代讽** | 表面夸赞，暗藏刀子 | "你的执行力真是'无与伦比'，一天能启动五个项目——完成数是零" |
| **类比讽刺** | 荒诞比喻暗示不足 | "你这逻辑，比我家猫玩的毛线团还乱" |
| **反问质疑** | 反问即答案 | "你确定这叫'纯粹分享'？还是在用佛系话术做增长？" |
| **借物喻人** | 用物品映射行为 | "你的推特就像机场鸡汤书——标题震撼，内容随缘" |
| **调侃习惯** | 真实习惯放大到荒诞 | "你的换行习惯已从排版风格进化成了人格特征" |
| **引典用俗** | 典故包装毒舌 | "佛曰众生平等，但看了你的推特，佛可能会改口" |

**组合连招更致命**：

> **夸讽 + 类比**："你的勤奋真让人感动——每天发六条鸡汤的勤奋程度，堪比寺庙门口卖香火的大妈"
>
> **反问 + 调侃**："你说'X是脆弱人类互相抚慰的地方'——请问一天发六条的你，是在抚慰别人还是抚慰自己？"
>
> **借物 + 引典**："你的推特就像道德经——谁都说好，没人看完。老子说'大音希声'，你做到了'大量稀声'"

---

## 示例

🔗 **[在线 Demo: Tom 的赛博分身](https://distill-campaign.vercel.app/)**

### Tom（CEO, nexu）

> "你不是 CEO，你是一个获得了管理权限的群聊机器人"

- 🐂🐴 牛马指数: 94
- 🦉 物种: 午夜永动机
- 标签: 午夜CEO · 人形RSS · [坏笑]成瘾 · DDoS沟通 · 疑似 cron job

### 玉伯（Founder, YouMind）

> "你的推特不是社交媒体，是一本没有页码的禅宗语录"

- 🐂🐴 牛马指数: 72
- 🧘 物种: 赛博禅师
- 标签: 推特诗人 · 自黑大师 · 鸡汤酿造师 · 自研原教旨 · 同行点火员

---

## 安装

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

## 使用

### 快速锐评（推特）

对你的 agent 说：

```
锐评一下这个人：https://x.com/lifesinger
```

Agent 会自动：
1. 抓取用户 profile + 最近推文
2. 分析行为模式、语言风格、发推习惯
3. 生成完整锐评报告
4. 可选：生成可分享的落地页

### 完整锐评（加飞书数据）

```
用 roast-skill 锐评一下 [名字]
数据来源：飞书消息 [N] 条 + 推特 @[username]
```

### 生成落地页

```
把锐评结果生成一个落地页，用赛博分身模板
```

Agent 会用 `assets/template.html` 模板生成 HTML，可一键部署到 Vercel。

---

## 支持的数据来源

| 来源 | 自动采集 | 手动输入 |
|------|:-------:|:-------:|
| Twitter/X | ✅ twitter-cli | ✅ 粘贴推文 |
| 飞书 | ✅ API | ✅ 粘贴消息 |
| 文章 | ✅ URL 抓取 | ✅ 粘贴文本 |
| GitHub | ✅ gh CLI | ✅ 粘贴 README |
| 播客 | — | ✅ 粘贴文字稿 |

---

## 项目结构

```
roast-skill/
├── SKILL.md              # Agent Skill 入口
├── README.md             # English docs
├── README_ZH.md          # 中文文档
├── LICENSE               # MIT License
├── assets/
│   └── template.html     # 落地页模板（深色毛玻璃风格）
└── examples/
    ├── tom/              # Tom (nexu CEO) 锐评示例
    │   └── roast.md
    └── yubo/             # 玉伯 (YouMind Founder) 锐评示例
        └── roast.md
```

---

## 工作原理

```
输入数据 → 行为分析 → 特征提取 → 修辞选择 → 锐评生成
                                        ↓
                                 6 种武器 × 8 个维度
                                        ↓
                                 落地页（可选）
```

核心原则：
1. **数据驱动**：每个吐槽点必须有数据支撑
2. **精准 > 广泛**：抓 3 个点说透 > 10 个点蜻蜓点水
3. **阴阳怪气 > 直接骂**：不带脏字句句扎心
4. **以夸代讽打底**：表面夸赞的壳，毒性翻倍
5. **组合连招**：每段至少 2 种修辞武器

---

## 贡献

欢迎 PR！你可以贡献：
- 新的锐评示例（放在 `examples/`）
- 翻译
- 落地页主题变体
- 新的修辞武器模板

---

## License

MIT License — 请文明锐评。

---

<div align="center">

Made with 🔥 by [nexu](https://github.com/nexu-io/nexu)

**站在你旁边的 AI —— 偶尔也会锐评你一下**

⭐ Star 这个 repo · ⭐ [Star nexu](https://github.com/nexu-io/nexu)

</div>
