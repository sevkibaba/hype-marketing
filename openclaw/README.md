# 🦞 OpenClaw: The Marketing Master Framework

OpenClaw is an open-source, autonomous AI agent framework designed to automate complex, multi-step workflows. This repository uses OpenClaw to transform static marketing strategies into a living "Marketing Master" instance that handles content creation, community engagement, LLM optimization, and competitor tracking across the digital landscape.

---

## 🚀 What OpenClaw Can Do For Your App

OpenClaw bridges the gap between a developer's vision and actual marketing execution — especially important when you have no time, budget, or marketing team.

| Channel | Skill | What it Automates |
|---|---|---|
| **Twitter / X** | `twitter_content_master` | "Build in Public" threads, Word of the Day posts, hooks |
| **ProductHunt** | `producthunt_launch_master` | Taglines, Maker's comment, launch day monitoring |
| **Medium / Blog** | `medium_article_generator` | Article repurposing from technical docs |
| **Blog (Full)** | `blog_post_writer` | Long-form SEO + GEO-optimized posts with comparison tables |
| **Reddit** | `reddit_engagement_expert` | "Help First" community replies, subreddit suggestion |
| **LLM Search (GEO)** | `llm_seo_optimizer` | AI directory submissions, schema markup, consensus loops |
| **Email / Newsletter** | `email_newsletter_master` | Weekly newsletters, drip sequences, lead magnet drafts |
| **Competitor Intel** | `competitor_watcher` | ASO scraping, keyword gap analysis, quarterly roadmap |

---

## 📂 What's In This Directory

```
openclaw/
├── README.md                   ← You are here
├── SOUL.md                     ← Agent identity, tone, and personality
├── AGENTS.md                   ← Operational rules, data handling, security
├── research_summary.md         ← Deep research on OpenClaw capabilities (from Reddit, GitHub, etc.)
└── skills/
    ├── twitter_content_master.md       ← X threads & daily posts
    ├── producthunt_launch_master.md    ← PH launch lifecycle
    ├── medium_article_generator.md     ← Doc-to-article conversion (GEO focus)
    ├── blog_post_writer.md             ← Long-form SEO & GEO blog posts ← NEW
    ├── llm_seo_optimizer.md            ← Generative Engine Optimization (LLMO) ← NEW
    ├── email_newsletter_master.md      ← Email list & newsletter automation ← NEW
    ├── reddit_engagement_expert.md     ← Community-first Reddit engagement
    └── competitor_watcher.md           ← App Store intelligence
```

---

## 🛠 How to Initialize Your Marketing Master

### Prerequisites
- Node.js v22+ (`node -v` to check)
- An API key for your preferred LLM (Gemini, Claude, or GPT-4)

### Install OpenClaw CLI
```bash
# Recommended: Installer script (handles Node.js automatically)
curl -fsSL https://openclaw.ai/install.sh | bash

# OR: via npm
npm install -g @openclaw/cli
```

### Link This Repository
```bash
cd /path/to/your/hype-marketing
openclaw init --soul openclaw/SOUL.md --agents openclaw/AGENTS.md
```

### Run a Specific Skill
```bash
# Generate a Twitter thread about the latest update
openclaw run openclaw/skills/twitter_content_master.md \
  --goal "Announce the new 3B local LLM model for Word Hype"

# Write a full blog post
openclaw run openclaw/skills/blog_post_writer.md \
  --goal "Write about how to learn TOEFL vocabulary offline" \
  --keyword "offline vocabulary app"

# Run the GEO optimizer for this week
openclaw run openclaw/skills/llm_seo_optimizer.md \
  --goal "Submit to 2 new AI directories and check LLMO audit checklist"

# Generate this week's newsletter
openclaw run openclaw/skills/email_newsletter_master.md \
  --goal "Write Issue #4 of The Weekly Hype"
```

---

## 📅 The Weekly Marketing Loop (Phase 2 Automation)

Once Phase 1 strategy is complete, OpenClaw can run a **weekly 4-hour marketing sprint** autonomously:

| Day | Skill | Output |
|---|---|---|
| Monday | `competitor_watcher` | Weekly Intel Report |
| Tuesday | `blog_post_writer` | Full blog post draft |
| Wednesday | `twitter_content_master` + `reddit_engagement_expert` | Social media drafts |
| Thursday | `llm_seo_optimizer` | GEO maintenance + directory submissions |
| Friday | `email_newsletter_master` | Newsletter issue draft |

**Human effort required per week:** ~30 minutes to review and approve the "Review Table" before posting.

---

## 🔄 Making This Work for ANY Company

This system is **app-agnostic by design**. To use it for a new company or product:

1. **Update `SOUL.md`** — Change the brand name, app name, and core value proposition.
2. **Replace the persona file** — Swap `results/phase_1_results/persona_word_hype.md` with a new persona document for your app's audience.
3. **Re-run the Phase 1 agent** — `agent_files/marketing_phase_1_agent.md` will generate new keyword strategies, ASO metadata, and roadmaps.
4. **Skills are plug-and-play** — Each skill file accepts `App Name`, `Target Persona`, and `Unique Value Proposition` as inputs. No skill needs to be rewritten.

> **Example:** A developer building a meditation app can use this entire system by entering "30-year-old burnt-out professional" as their persona and "Headspace, Calm" as competitors. The blog post writer will generate articles about "best offline meditation app", the GEO optimizer will list the app on AI directories under "Wellness AI", and the Twitter skill will write threads about building the app in public.

---

## 📚 Related Files
- **Phase 1 & Phase 2 Agent:** [`agent_files/marketing_phase_1_agent.md`](../agent_files/marketing_phase_1_agent.md)
- **Research Foundation:** [`openclaw/research_summary.md`](research_summary.md)
- **GEO Deep-Dive Strategy:** [`tasks/phase_1_tasks/03_llm_search_optimization_strategy.md`](../tasks/phase_1_tasks/03_llm_search_optimization_strategy.md)
- **Marketing Roadmap:** [`results/phase_1_results/roadmap_marketing_automation.md`](../results/phase_1_results/roadmap_marketing_automation.md)

---

*OpenClaw Marketing Master — v2.0 | Built for indie developers by indie developers.*
