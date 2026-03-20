# Email Newsletter Strategy: "The Weekly Hype"

**Goal:** Build a direct, owned communication channel for Word Hype and Test Maker users that is immune to algorithm changes, platform bans, and social media noise. Email lists are the indie developer's most durable marketing asset.

---

## 1. Platform Recommendation

| Platform | Cost | Best For | Our Recommendation |
|---|---|---|---|
| **Substack** | Free (up to 50k subscribers) | "Build In Public" audience, discovery via Substack network | ✅ **Start here** |
| **Beehiiv** | Free up to 2,500 subs | Growth-focused newsletters with referral programs | ✅ **Switch to when > 1k subscribers** |
| **Ghost** | $9/mo (or self-host free) | Technical control, blog integration | 🔵 Long-term landing page + blog combo |
| **Mailchimp** | Free up to 500 contacts | Mass marketing — AVOID for authentic indie newsletters | ❌ Not recommended |

**Immediate Action:** Set up Substack at `substack.com/[appname]`. Pick a newsletter name:
- Suggestions: **"The Weekly Hype"**, **"The Local AI Letter"**, **"Word Drop"**

---

## 2. Two Newsletter Tracks

### Track A: "The Weekly Hype" (For App Users / Language Learners)
**Audience:** People who downloaded Word Hype or Test Maker. ESL students, IELTS/TOEFL preppers.
**Frequency:** Every Tuesday
**Format:** Short (400-600 words), educational, engaging.

**Recurring Sections:**
1. **📌 Word of the Week** — A high-level vocabulary word with a context-aware AI definition, example, and memory hook.
2. **💡 Study Tip of the Week** — 1 actionable strategy for better retention, comprehension, or exam prep.
3. **📰 App Update** — 2-3 sentences: what shipped this week.
4. **📲 CTA** — App download link + "Share with a study buddy."

### Track B: "The Dev Log" (For Build-In-Public / Indie Dev Audience)
**Audience:** Fellow indie developers, AI enthusiasts, ProductHunt community.
**Frequency:** Every other Friday (biweekly)
**Format:** Personal, raw, data-driven. (600-900 words)

**Recurring Sections:**
1. **👋 What I Shipped** — Honest development recap.
2. **📊 The Numbers** — Downloads, active users, top review feedback.
3. **🧠 What I Learned** — 1 genuine business/marketing/AI insight.
4. **🔗 3 Links Worth Your Time** — Curated reading relevant to indie dev / AI / EdTech.

---

## 3. Lead Magnets (List Growth Strategy)

Offer free, high-value content to incentivize email sign-ups. Promote each lead magnet on Reddit, Twitter, and the app's landing page.

| Lead Magnet | Format | Promoted On | Estimated Conversion |
|---|---|---|---|
| **"500 Must-Know IELTS Words (Free PDF)"** | PDF / Notion doc | Reddit r/IELTS, r/EnglishLearning | High |
| **"The Spaced Repetition Formula (No App Required)"** | 1-page PDF | Reddit r/productivity, Twitter | Medium |
| **"How I Built a Local LLM App in 90 Days"** | Technical PDF | HN, r/LocalLLaMA, Twitter | Low (but high-quality leads) |
| **"The Indie App Launch Checklist (40 Steps)"** | Google Sheet | Indie Hackers, r/SideProject | Medium |

**Landing Page Implementation:**
- Add an email capture form to the app's landing page (above the App Store download button).
- Copy: *"Get the free IELTS 500 Word PDF + weekly vocabulary tips. No spam."*

---

## 4. 5-Email Welcome Drip Sequence

When someone subscribes (via any lead magnet), trigger this automated sequence:

```
Email 1 — Day 0: Welcome + Lead Magnet Delivery
Subject: "Your [Lead Magnet Name] is here 🎉"
Body:
- Deliver the lead magnet (PDF link / Notion link).
- 1-paragraph personal intro from the developer.
- CTA: "Download Word Hype for free while you're at it."

---

Email 2 — Day 2: Feature Deep Dive
Subject: "One feature in Word Hype that most people miss..."
Body:
- Focus entirely on the "My Words" save feature.
- Show how it replaces Anki flashcards with a smarter, context-aware system.
- CTA: "Try it yourself — tap any word during a game."

---

Email 3 — Day 5: The Problem / The Mission
Subject: "Why I'm building a language app powered by AI that costs $0 to run"
Body:
- Honest story about the cost and privacy problems with cloud AI apps.
- Explain the edge AI / local LLM approach.
- Make the reader feel like an insider ("You get it, most people don't").
- CTA: "Share with a friend who uses Duolingo but wants something smarter."

---

Email 4 — Day 9: Social Proof
Subject: "Users share how they used Word Hype to pass IELTS Band 7"
Body:
- 2-3 curated testimonials or App Store reviews (with permission).
- Frame each as a before/after story.
- CTA: "Leave a rating if Word Hype helped you." (App Store review ask)

---

Email 5 — Day 14: Feedback Request
Subject: "Quick question for you..."
Body:
- A single, simple question: "What's the one thing you'd change about Word Hype?"
- Reply-to-email setup: responses go directly to the developer's inbox.
- This drives replies (which improves email deliverability) and provides invaluable product feedback.
- CTA: "Hit reply. I read every response."
```

---

## 5. Subject Line Best Practices

Good subject lines feel personal, specific, and slightly unfinished:
- ✅ "The word you've been mispronouncing since middle school 🤐"
- ✅ "I shipped a feature at 2 AM. Here's what happened."
- ✅ "5 IELTS words that always trip people up (one fix each)"
- ❌ "Our Weekly Newsletter — Issue #4"
- ❌ "Check out our latest update!"
- ❌ "You won't believe this vocabulary tip"

**Always generate 3 variants and A/B test the first 3 issues.**

---

## 6. Analytics & KPI Tracking

Track these metrics monthly:

| KPI | Industry Avg | Our Target |
|---|---|---|
| Open Rate | 20-30% | >35% (personal tone) |
| Click-Through Rate | 2-5% | >4% |
| Unsubscribe Rate | <0.5% | <0.3% |
| Reply Rate | <1% | >2% (key for deliverability) |
| Subscriber Growth | — | +50/month (organic), +200/month (with lead magnets) |

---

## 7. Technical Setup Checklist

- [ ] Create Substack account at `substack.com/[name]`
- [ ] Set up custom domain or vanity URL (e.g., `theweeklyhype.substack.com`)
- [ ] Add email capture pop-up to landing page (use ConvertKit embed or native Substack form)
- [ ] Configure the 5-email welcome drip sequence (via Beehiiv or ConvertKit when switching)
- [ ] Create the first lead magnet (IELTS 500 Word PDF)
- [ ] Add "Subscribe for weekly vocabulary tips" CTA to all blog posts and Reddit profiles
- [ ] Set up SPF/DKIM authentication for custom sender domain (reduces spam filtering)

---

## 🔗 Skill to Use
Run via: `openclaw run openclaw/skills/email_newsletter_master.md --goal "Write Issue #1 of The Weekly Hype"`

---
*Task created: 2026-03-20 | Start: Immediately*
