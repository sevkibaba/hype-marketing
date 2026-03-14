# Task: Apple Search Ads (ASA) Account Structure Setup

*Objective: Establish a scalable and efficient Apple Search Ads (ASA) Advanced account architecture for Word Hype to capture high-intent users, defend the brand, and discover new profitable keywords without cannibalizing exact match bids.*

## 1. Core Campaign Structure (The "4-Campaign" Framework)

To effectively manage bids and isolate performance, we will implement the industry-standard isolation strategy, separating our keywords into four distinct campaigns.

### A. Brand Campaign
*   **Purpose:** Protect our own brand terms from competitors conquesting our name. This usually has the highest conversion rate and lowest CPA.
*   **Match Type:** Exact Match
*   **Ad Groups:** `Brand - Exact`
*   **Keywords:** `word hype`, `wordhype`, `word hype game`, `word hype english`

### B. Generic / Category Campaign
*   **Purpose:** Capture high-intent "Active Language Learner" (Persona 1) users searching for specific functionalities.
*   **Match Type:** Exact Match
*   **Ad Groups:** 
    *   `Vocab - Exact` (e.g., `[vocabulary builder]`, `[learn english words]`)
    *   `Exams - Exact` (e.g., `[TOEFL vocabulary]`, `[IELTS practice]`)
    *   `Features - Exact` (e.g., `[offline english dictionary]`, `[flashcards app]`)
*   **Keywords:** Pulled from our primary head terms and long-tail double intent lists.

### C. Competitor Campaign
*   **Purpose:** Steal market share by showing our app when users search for similar or established, but potentially "boring" apps.
*   **Match Type:** Exact Match
*   **Ad Groups:** `Competitors - Exact`
*   **Keywords:** `[anki]`, `[quizlet]`, `[duolingo]`, `[memrise]`, `[babbel]`

### D. Discovery Campaign
*   **Purpose:** Mine the App Store for new, unexpected search terms that users are actually using to find apps like ours.
*   **Match Types & Setup:**
    *   **Ad Group 1: Search Match.** (Search Match = ON, No keywords). Apple's algorithm automatically matches your app to relevant searches based on your App Store metadata.
    *   **Ad Group 2: Broad Match.** Bidding on broad terms like `english vocabulary` or `word game` to see what long-tail variants stem from them.
*   **CRITICAL NEGATIVE KEYWORD ROUTING:** To ensure the Discovery campaign only finds *new* keywords, you MUST add every Exact Match keyword from the Brand, Generic, and Competitor campaigns as **Exact Match Negative Keywords** to the Discovery campaign. If you discover a winning term in Discovery, you move it to the Generic Exact campaign and add it as a negative to Discovery.

---

## 2. Execution Steps

1.  **Fund ASA Account:** Set up billing and daily budgets.
2.  **Campaign Creation:** Create the 4 campaigns outlined above for the primary storefront (e.g., US/UK).
3.  **Negative Keyword Implementation:** Cross-pollinate negative keywords immediately (all exacts into the discovery campaign as negatives).
4.  **Initial Bidding Strategy:** 
    *   Set exact match bids higher (willing to pay more for proven intent).
    *   Set discovery bids lower (paying for exploration, expecting lower CVR).
    *   Set CPT (Cost Per Tap) bids based on expected CPA to maintain profitability.
5.  **Tracking Setup:** Ensure the Apple Search Ads Attribution API is integrated with the mobile app (via MMP like AppsFlyer/Adjust or custom implementation) to track post-install events (e.g., trial started, subscription purchased).

---

## 3. Advanced Improvements & Next Steps

Once the baseline account structure is running and gathering data, we can implement the following improvements to boost ROAS (Return on Ad Spend):

*   **Custom Product Pages (CPPs) & Ad Variations:**
    *   Create a specific App Store product page tailored for the "Competitor Campaign" highlighting why Word Hype is better than flashcards (targeting Anki/Quizlet switchers).
    *   Create a CPP specifically for "Exam Prep" (TOEFL/IELTS) for the Generic campaign. Match the ASA ad to the specific CPP.
*   **Granular Geo-Targeting & Localization:**
    *   Clone the successful US/UK structure into Tier 2 and Tier 3 English-learning markets (e.g., India, Brazil, Southeast Asia). 
    *   Adjust bids downward for regions with lower LTV (Lifetime Value).
*   **Dayparting (Ad Scheduling):**
    *   Analyze when users are most likely to convert (e.g., evenings for students doing homework, or morning commutes). Use the ASA API or third-party tools to increase bids during high-conversion hours.
*   **LAT On vs. LAT Off Separation:**
    *   Limit Ad Tracking (LAT) users (now ATT - App Tracking Transparency opted-out users). Create separate ad groups targeting LAT-On vs LAT-Off to manage bids separately, as LAT-on users might convert differently and are harder to track.
*   **Search-Term to Keyword Funneling (Weekly Routine):**
    *   Review Discovery campaign search terms weekly.
    *   Promote terms with high ROAS to Exact Match campaigns.
    *   Add terms with high spend and 0 conversions as *Negative Keywords* across all campaigns to stop wasting money.
