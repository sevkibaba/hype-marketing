# GitHub Marketing Automation Agents Araştırması

Bu dosya, GitHub'daki açık kaynak marketing automation agent repolarının bir derlemesidir.

---

## 1. crewAI-examples (5,752 ⭐)

**Repo:** [crewAIInc/crewAI-examples](https://github.com/crewAIInc/crewAI-examples)

**Açıklama:** CrewAI framework'ünü kullanarak workflow'ları otomatikleştiren örnek uygulamalar koleksiyonu. Multi-agent işbirliği ile gerçek dünya uygulamaları gösteriyor.

**Özellikler:**
- Multi-crew orchestration (Content Creator Flow, Email Auto Responder, Lead Score Flow)
- Marketing Strategy crew - kampanya geliştirme
- Instagram Post - sosyal medya içerik üretimi
- Landing Page Generator
- Stock Analysis - finansal analiz
- Trip Planner

**Kullanım:**
```bash
git clone https://github.com/crewAIInc/crewAI-examples.git
cd crewAI-examples
uv sync
```

**Dil:** Jupyter Notebook (%82.4), Python (%10.1)

---

## 2. gtm-agents (123 ⭐)

**Repo:** [gtmagents/gtm-agents](https://github.com/gtmagents/gtm-agents)

**Açıklama:** Sales, marketing, customer success ve revenue operations workflow'ları için production-ready GTM (Go-To-Market) agentları ve specialized skills koleksiyonu. Claude Code için optimize edilmiş.

**Özellikler:**
- 67 plugin, 92 AI agent, 52 business skill
- Sales: Prospecting, pipeline management, account management
- Marketing: Content, email, social media, SEO, paid media
- Growth: Experiments, analytics, A/B testing, churn prediction
- Customer Success: Onboarding, health scoring, retention
- Workflow orchestrators: Campaign, ABM, lead nurture

**Kurulum:**
```bash
/plugin marketplace add gtmagents/gtm-agents
/plugin install sales-prospecting
/plugin install content-marketing
```

**Dil:** Python (%99.2)

---

## 3. Marketing-Swarm-Template (23 ⭐)

**Repo:** [The-Swarm-Corporation/Marketing-Swarm-Template](https://github.com/The-Swarm-Corporation/Marketing-Swarm-Template)

**Açıklama:** Swarms framework üzerine inşa edilmiş, multi-platform marketing content oluşturan AI agentları için şablon. Alex Hormozi'nin high-ticket offer framework'lerini kullanıyor.

**Özellikler:**
- 10+ specialized marketing agent (Instagram, LinkedIn, Twitter, Email, TikTok)
- Hormozi-style high-ticket offer frameworks
- Platform-specific content strategies
- Automated content generation
- Value-first marketing approach

**Kullanım:**
```bash
pip install -U swarms
git clone https://github.com/The-Swarm-Corporation/Marketing-Swarm-Template
cd Marketing-Swarm-Template
python3 main.py
```

**Dil:** Python

---

## 4. Agents4Marketing (9 ⭐)

**Repo:** [TheCMOAI/Agents4Marketing](https://github.com/TheCMOAI/Agents4Marketing)

**Açıklama:** Production-grade AI marketing agents for Claude Code. 10 farklı marketing agent, paylaşılan knowledge base, 15 industry vertical ve situational playbooks içeriyor.

**Özellikler:**
- **10 Marketing Agents:** Google Ads, Meta Ads, SEO Auditor, GBP Manager, Blog Writer, Website Builder, Landing Page, Copywriter, WordPress, Shopify
- **Knowledge Base:** Unit economics, frameworks (Schwartz, Hormozi), ad strategy, CRO
- **15 Industry Verticals:** Pressure washing, plumbing, HVAC, landscaping, roofing, etc.
- **Situational Playbooks:** CPA optimization, creative fatigue, ranking drops
- **MCP Servers:** Google Ads, Meta, GBP, Search Console, Analytics, WordPress, Shopify API entegrasyonları

**Kullanım:**
```bash
git clone https://github.com/TheCMOAI/Agents4Marketing.git
cd Agents4Marketing
claude
```

**Dil:** Python (%99.3)

---

## 5. opensoul (8 ⭐)

**Repo:** [iamevandrake/opensoul](https://github.com/iamevandrake/opensoul)

**Açıklama:** Açık kaynak agentic marketing stack. Paperclip üzerine inşa edilmiş, gerçek bir marketing ajansı gibi organize edilmiş AI agent ekibi. Director, Strategist, Producer, Creative, Growth Marketer, Analyst rolleri ile tam org yapısı.

**Özellikler:**
- **6 Marketing Roles:** Director, Strategist, Producer, Creative, Growth Marketer, Analyst
- Goal-driven campaigns - her görev marketing objective'larına geri döner
- Autonomous execution - agentlar scheduled heartbeats ile çalışır
- Budget control - agent başına aylık bütçe takibi
- Campaign governance - kullanıcı onayı gerekli
- Full audit trail - her karar, her draft kayıtlı

**Kullanım:**
```bash
git clone https://github.com/iamevandrake/opensoul.git
cd opensoul
pnpm install
pnpm dev
```

**Dil:** TypeScript (%96)

---

## 6. openclaudia-skills (261 ⭐)

**Repo:** [OpenClaudia/openclaudia-skills](https://github.com/openclaudia/openclaudia-skills)

**Açıklama:** Claude Code için 34 açık kaynak marketing skills. SEO, content, email, ads, analytics ve growth konularında uzmanlaşmış skill'ler.

**Özellikler:**
- SEO skills
- Content creation
- Email marketing
- Ads management
- Analytics
- Growth strategies

**Dil:** JavaScript

---

## Karşılaştırma Özeti

| Repo | Stars | Dil | Odak Alanı |
|------|-------|-----|-------------|
| crewAI-examples | 5,752 | Python/Jupyter | Multi-agent workflows, various use cases |
| gtm-agents | 123 | Python | GTM (sales + marketing + growth) |
| Marketing-Swarm-Template | 23 | Python | Multi-platform content, Hormozi frameworks |
| Agents4Marketing | 9 | Python | 10 specialized marketing agents, API integrations |
| opensoul | 8 | TypeScript | Full marketing org structure, autonomous execution |
| openclaudia-skills | 261 | JavaScript | Marketing skills for Claude Code |

---

## Öneriler

1. **Hızlı başlangıç için:** `crewAI-examples` - En popüler ve bol örnek içeren
2. **Kapsamlı GTM için:** `gtm-agents` - Sales + Marketing + Growth tam kapsama
3. **Production-grade marketing için:** `Agents4Marketing` - Gerçek müşteri deneyimi ile test edilmiş
4. **Tam org yapısı için:** `opensoul` - Gerçek ajans gibi çalışan agentlar
5. **Content-focused için:** `Marketing-Swarm-Template` - Social media, email, content