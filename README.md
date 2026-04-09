<div align="center">

# 牛马锐评 Skill

> *"AI 蒸馏了你的所有数据，决定说实话了"*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![nexu](https://img.shields.io/badge/nexu-Skill-blueviolet)](https://github.com/nexu-io/nexu)

<br>

每天在飞书里回复 200 条消息，你管这叫「高效协作」？<br>
凌晨两点还在群里分享行业文章，你管这叫「学习型人才」？<br>
周末加班写方案改了八版，你管这叫「追求极致」？<br>
年终总结写了三千字，其实干的活一句话能说完？<br>

**让 AI 蒸馏你自己的数据，生成一份毒舌但精准的牛马画像。**<br>
也可以顺便蒸馏一下你的同事 😏

<br>

给 AI agent 你的推特链接、飞书消息记录、或任何公开数据<br>
它会先蒸馏你的工作人格，再生成一份**8 维度锐评报告** — 6 种修辞武器、不留情面<br>
还能一键生成赛博朋克风格的分享落地页

<br>


> 复制链接发给你的 nexu agent：`https://github.com/nexu-io/roast-skill`

[工作原理](#工作原理) · [安装](#安装) · [使用](#使用) · [示例](#示例) · [English](README_EN.md)

</div>

---

> 🔥 **牛马锐评** 是 [nexu](https://github.com/nexu-io/nexu) 生态的一部分 — Agent-Native 平台，AI 站在你旁边而不是替代你。偶尔也会站在你旁边锐评你一下。

---

## 你会得到什么

| 输出 | 说明 |
|------|------|
| 🏷️ **Profile 标签** | 8-12 个标签，5 种类型：公司 / 岗位 / 职级 / MBTI / 性格 |
| 🐂 **牛马指数** | 0-100 工作强度评分 |
| 🦅 **物种鉴定** | 荒诞动物比喻（"接入核电站的秃鹰""午夜永动机"） |
| 📊 **能力条** | 4 项自定义指标，命名要有梗（如"交付力: 43%""大写锁定力: 100%"） |
| 🔥 **主 Roast** | 150-250 字毒舌吐槽，第二人称直接开怼，不留余地 |
| 🔬 **8 维度深度扒皮** | Roast / 优势 / 弱点 / 金钱观 / 灵魂动物 / 同事视角 / 名人对标 / 人生建议 |
| 💬 **AI 对话示例** | 2 轮模拟对话，还原本人说话风格 |
| 🌐 **落地页** | 可部署的 HTML — 深色毛玻璃赛博风，分享即传播 |

---

## 工作原理

```
输入数据 → 行为分析 → 特征提取 → 修辞选择 → 锐评生成
                                        ↓
                                 6 种武器 × 8 个维度
                                        ↓
                                 落地页 → 分享 🚀
```

### 🎯 6 大阴阳怪气修辞武器

每段吐槽混合使用多种技巧，**组合连招比单招更毒**：

| # | 武器 | 原理 | 示例 |
|---|------|------|------|
| 1 | **以夸代讽** | 表面夸赞，暗藏刀子 | "你的执行力真是'无与伦比'，一天能启动五个项目——完成数是零" |
| 2 | **类比讽刺** | 荒诞比喻暗示不足 | "你这逻辑，比我家猫玩的毛线团还乱" |
| 3 | **反问质疑** | 反问即答案 | "你确定这叫'纯粹分享'？还是用佛系话术做增长？" |
| 4 | **借物喻人** | 用物品映射行为 | "你的推特就像机场鸡汤书——标题震撼，内容随缘" |
| 5 | **调侃习惯** | 真实习惯放大到荒诞 | "你的换行习惯已从排版风格进化成了人格特征" |
| 6 | **引典用俗** | 典故包装毒舌 | "佛曰众生平等，但看了你的推特，佛可能会改口" |

**组合连招示例**：

> **夸讽 + 类比**："你的勤奋真让人感动——每天发六条鸡汤的勤奋程度，堪比寺庙门口卖香火的大妈"
>
> **反问 + 调侃**："你说'X是脆弱人类互相抚慰的地方'——请问一天发六条的你，是在抚慰别人还是抚慰自己？"
>
> **借物 + 引典**："你的推特就像道德经——谁都说好，没人看完。老子说'大音希声'，你做到了'大量稀声'"

---

## 示例

### 🔗 [在线 Demo: Tom 的赛博分身](https://distill-campaign.vercel.app/)

### [Elon Musk](examples/elon/)

> "你用一个字'Yes'获得 2400 万赞——不是因为你说得好，是因为你**买了这个平台**"

- 🐂🐴 牛马指数: 99 · 🦅 物种: 接入核电站的秃鹰
- 标签: `火箭回收型创业家` · `Meme投放机` · `10万条推文俱乐部` · `DOGE部长`
- 交付力: 43% · Meme力: 97% · 睡眠力: 6%

### [Donald Trump](examples/trump/)

> "你不是在治国，你是在经营一个**只有两个按钮的情绪面板：伟大和灾难**"

- 🐂🐴 牛马指数: 85 · 🦅 物种: 穿西装的美国秃鹰
- 标签: `MAGA永动机` · `全大写外交官` · `关税之王` · `认输力0%`
- 口号力: 99% · 大写锁定力: 100% · 外交委婉力: 3%

### [Tom — CEO, nexu](examples/tom/)

> "你不是 CEO，你是一个**获得了管理权限的群聊机器人**"

- 🐂🐴 牛马指数: 94 · 🦉 物种: 午夜永动机
- 标签: `午夜CEO` · `人形RSS` · `[坏笑]成瘾` · `DDoS沟通` · `疑似 cron job`

---

## 安装

### nexu（推荐）

直接把 GitHub 链接发给你的 nexu agent：

```
帮我安装这个 skill：https://github.com/nexu-io/roast-skill
```

### 手动安装

```bash
git clone https://github.com/nexu-io/roast-skill <你的 agent skills 目录>
```

无需安装依赖 — 纯 prompt skill，装完即用。

### ⚠️ 平台兼容性说明

| 功能 | nexu | 其他 Agent 平台 |
|------|:----:|:--------------:|
| 锐评生成 | ✅ | ✅ |
| 飞书消息自动采集 | ✅ | ✅（需配飞书凭证） |
| **落地页一键部署** | ✅ 自动部署到 `.nexu.space` | ❌ 需手动打开本地 HTML |

> **落地页部署**依赖 nexu 内置的 `deploy-skill`，会自动将锐评结果渲染为赛博朋克风格网页并部署到 `nexu.space`。
>
> 在其他 Agent 平台上使用时，锐评内容仍然会生成，但**落地页需要手动处理**：
> 1. Agent 会将渲染好的 HTML 文件保存到本地（`~/.nexu/deploy-skill-generated/`）
> 2. 你可以直接用浏览器打开这个 HTML 文件查看效果
> 3. 或者自行部署到 Vercel / Netlify / GitHub Pages 等静态托管平台

---

## 使用

### 锐评自己（核心玩法）

对你的 agent 说：

```
锐评 我自己
```

Agent 会自动：
1. 读取你在所有飞书群聊中的消息
2. 蒸馏你的工作人格和行为模式
3. 生成完整锐评报告（牛马指数 + 8 维度深度扒皮）
4. 可选：生成可分享的赛博朋克落地页

### 锐评同事

```
锐评 张三
```

Agent 会自动采集飞书共同群中 TA 的消息来分析。也可以补充推特链接让结果更精准：

```
锐评 张三，推特是 https://x.com/zhangsan
```

### 生成落地页

```
把锐评结果生成一个落地页
```

→ Agent 会用 `assets/template.html` 模板生成 HTML 落地页，自动处理部署。

---

## 支持的数据来源

| 来源 | 自动采集 | 手动输入 |
|------|:-------:|:-------:|
| Twitter/X | ✅ twitter-cli | ✅ 粘贴推文 |
| 飞书 | ✅ API | ✅ 粘贴消息 |
| Slack | ✅ API | ✅ 粘贴消息 |
| 文章/URL | ✅ 抓取 | ✅ 粘贴文本 |
| GitHub | ✅ gh CLI | ✅ 粘贴 README |
| 播客 | — | ✅ 粘贴文字稿 |

---

## 注意事项

- **原材料质量 = 锐评质量**：真实聊天记录 + 推文 >> 纯手动描述
- 建议优先收集：**决策类回复** > **他主动写的长文** > 日常水群
- 公共人物效果最好（数据多、模式明显）
- 锐评的目标是**又气又笑** — funny > mean，阴阳怪气 > 直接骂
- 中文锐评文化 + 双语 agent 效果最佳

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
    ├── elon/             # Elon Musk 锐评
    │   └── roast.md
    ├── trump/            # Donald Trump 锐评
    │   └── roast.md
    └── tom/              # Tom (nexu CEO) 锐评
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

## 贡献

欢迎 PR！你可以贡献：
- 🔥 新的锐评示例（`examples/`）
- 🌐 翻译
- 🎨 落地页主题变体（`assets/`）
- ⚔️ 新的修辞武器模板

---

<div align="center">

MIT License © [nexu](https://github.com/nexu-io)

Made with 🔥 by [nexu](https://github.com/nexu-io/nexu)

**站在你旁边的 AI — 偶尔也会锐评你一下**

⭐ [Star 这个 repo](https://github.com/nexu-io/roast-skill) · ⭐ [Star nexu](https://github.com/nexu-io/nexu)

</div>
