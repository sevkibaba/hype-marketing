# Market Analysis & App Store Keyword Strategy
*Targeting the Largest Addressable Audience for Word Hype*

## 1. Persona Market Size Analysis
To build a successful App Store Optimization (ASO) and Apple Search Ads (ASA) strategy, we must focus our keywords on the persona that represents the largest, highest-intent search volume on the iOS App Store.

*   **Persona 3: The "Edge-AI / Tech Enthusiast":** *Smallest.* While a great hook for Twitter and Product Hunt, "local LLM" or "neural network game" has virtually zero organic search volume on the App Store.
*   **Persona 2: The "Continuous Improvement" Professional:** *Medium.* These users search for terms like "brain training", "vocabulary builder", or "improve communication". They have a high Lifetime Value (LTV) and willingness to subscribe, but they are fewer in number compared to massive global student markets.
*   **Persona 4: The "Subway Commuter":** *Giant, but hard to convert.* "Offline games" or "no wifi games" has massive search volume. However, the intent is purely entertainment. You are competing against hyper-casual giants (Candy Crush, Subway Surfers). Getting them to download an *educational* English game is an uphill battle. 
*   **Persona 1: The "Active Language Learner" (ESL/ELL):** **THE WINNER.** The language learning market is a multi-billion dollar industry. Furthermore, millions of users globally search specifically for "learn English" or "IELTS vocabulary" every single day. This audience has both **massive scale** and **exact intent** matching Word Hype's core feature (contextual learning).

**Conclusion:** Our keyword architecture must dedicate 80% of its real estate (Title, Subtitle, Keyword Field, ASA Bids) to targeting **Persona 1: The Active Language Learner**.

---

## 2. Keyword Strategy for "The Active Language Learner"
This strategy relies on capturing high-intent users who are actively trying to pass exams or improve their English fluency, rather than just playing a game.

### A. Primary Head Terms (High Volume / High Competition)
These are for our master keyword list and exact match Apple Search Ads.
*   english vocabulary
*   vocabulary builder
*   english words
*   learn english
*   english dictionary

### B. Long-Tail "Double Intent" Keywords (High Conversion / Low Competition)
Because Word Hype solves the "flashcard" problem, we want to target users looking for advanced or specific learning methods.
*   *IELTS vocabulary offline*
*   *TOEFL word practice*
*   *learn english in context*
*   *offline english dictionary*
*   *ESL word game*

### C. Apple Search Ads (ASA) Competitor Conquesting
We will bid on the brand names of our competitors. When a user searches for a boring flashcard app, we show them Word Hype.
*   `anki`
*   `quizlet`
*   `duolingo`
*   `memrise`
*   `babbel`

---

## 3. Metadata Implementation Example (US / UK Store)
*How this looks in practice on the App Store page:*

*   **App Title (30 Chars):** Word Hype: English Vocabulary
*   **Subtitle (30 Chars):** Learn offline, IELTS & TOEFL
*   **Hidden Keyword String (100 Chars limit):** `learn,english,ESL,IELTS,TOEFL,dictionary,flashcard,anki,offline,study,context,quizlet,builder,words`

---

## 4. Apple Search Ads (ASA) Campaign Strategy
Based on the keyword strategy above, we will deploy an advanced 4-Campaign ASA architecture to maximize ROI targeting the "Active Language Learner". For detailed tactical setup instructions, see: [03_apple_search_ads_structure.md](03_apple_search_ads_structure.md).

### The 4-Campaign Framework
*   **1. Brand Campaign (Exact Match):** Defend our brand keywords (`word hype`, `wordhype`). Very low CPA expected.
*   **2. Generic/Category Campaign (Exact Match):** Target our high-intent, primary head terms and double-intent keywords (`learn english`, `vocabulary builder`, `IELTS offline`).
*   **3. Competitor Campaign (Exact Match):** Conquest well-known brands (`anki`, `quizlet`, `duolingo`) to capture their specific audience.
*   **4. Discovery Campaign (Search Match ON & Broad Match):** Uncover new keywords using Apple's auto-matching. **Crucial:** All exact match keywords from campaigns 1-3 must be added here as Negative Keywords to prevent self-cannibalization and ensure we only pay for *new* discovery.

### Advanced Improvements & Optimization
*   **Custom Product Pages (CPPs):** Direct specific ad groups to tailored App Store pages (e.g., showing a TOEFL-specific storefront to users searching for "TOEFL practice" or an anki-superiority page to users searching "anki").
*   **Geo-Targeting & LTV Adjustments:** Clone successful US/UK campaigns for Tier 2/3 markets but adjust bids downward based on the region's expected Lifetime Value (LTV).
*   **Dayparting:** Adjust bids dynamically during peak learning and commuting hours.
*   **LAT (Limit Ad Tracking) Segmentation:** Separate ad groups for users who opted out of App Tracking Transparency to manage their bids independently, as their post-install conversions are harder to track.
*   **Automatic Search Term Funneling:** Establish a routine (or automation) to continuously harvest profitable terms from the Discovery campaign, moving them to Exact Match, and adding them as negatives to Discovery.
