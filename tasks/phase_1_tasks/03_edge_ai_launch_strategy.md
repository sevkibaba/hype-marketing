# Launch Strategy: "Edge-AI / Tech Enthusiast" Persona
*Bootstrapping Initial Users by Showcasing Technical Innovation*

While the long-term App Store strategy targets English Language Learners, our immediate, high-impact launch strategy targets the **Edge-AI / Tech Enthusiast**. This persona is highly active, vocal, and willing to try new apps simply for the novelty of the technology.

**The Hook:** A mobile app powered by a 1.1B (TinyLlama) or 3B (Phi-2) parameter LLM running *100% locally* on iOS/Android via React Native, offline, with zero latency.

---

## 1. Product Hunt Launch
Product Hunt is the epicenter for early adopters in the tech community.

*   **Tagline:** Word Hype: The Offline AI Word Game (Powered by Local LLMs).
*   **The Maker's Comment:** This is your chance to shine as the developer.
    *   *Highlight:* Introduce yourself as a Data/AI Engineer. Explain *why* you built it (the technical challenge).
    *   *Technical Details:* Mention `llama.rn`, React Native, and the specific models (TinyLlama Q4/Q8, Phi-2) used for inference. Discuss the challenges of managing memory and mobile deployment.
    *   *Call to Action:* Ask the community to test the inference speed on their specific device models (e.g., "Let me know how fast TinyLlama runs on your iPhone 13 vs 15!"). This drives engagement and comments.
*   **Visuals:** Include a short GIF or video showing the app generating a definition *while in airplane mode* to prove it runs locally.

## 2. Reddit "Show & Tell" Campaigns
The developer and AI communities on Reddit love deep technical breakdowns of side projects.

*   **r/LocalLLaMA:**
    *   *Post Type:* Technical Showcase.
    *   *Title Example:* "I managed to get Phi-2 running locally on iOS for a vocab game. Here's how inference speeds look across devices."
    *   *Content:* Share the open-source libraries (`llama.rn`), model quantization details (Q4 vs Q8), and battery impact. Frame the app as a real-world use case for local LLMs.
*   **r/reactnative / r/iOSProgramming:**
    *   *Post Type:* "I Built This" Developer Post.
    *   *Title Example:* "Built a fully offline AI app using React Native + local LLMs. Bypassing cloud costs entirely."
    *   *Content:* Focus on the architecture, state management, and the unique challenges of packaging large binary model files (500MB+) inside an Expo/React Native app.
*   **r/SideProject / r/macapps:**
    *   *Post Type:* General Launch. Focus on the final polished game rather than just the tech stack.

## 3. The Hacker News (Y Combinator) Post
HN is notoriously tough, but a highly technical, transparent post can go viral.

*   **Show HN Format:** "Show HN: Word Hype – An offline vocabulary game using local, on-device LLMs"
*   **The Content:** Keep it brief, humble, and strictly focused on the engineering. Explain that it's a "toy" game built to solve the "flashcard lack of context" problem using edge computing instead of expensive API calls. Answer architectural questions rapidly in the comments.

## 4. X (Twitter) "Build in Public" Thread
A thread aimed at AI researchers and iOS developers.

*   **The Thread Structure:**
    *   *Tweet 1:* The Hook. A video of airplane mode inference with a bold statement ("Cloud AI is expensive. So I put a 3B parameter model on my phone instead. Here is Word Hype...").
    *   *Tweet 2:* The Problem. Why flashcards suck and why context is needed.
    *   *Tweet 3:* The Tech Stack (React Native + llama.rn).
    *   *Tweet 4:* The UX Challenge (Downloading a 1GB model file gracefully on first launch without the OS killing the app).
    *   *Tweet 5:* The Link. "Try it for free here and tell me your tokens-per-second speed."

---

## Objective of this Launch:
*   **Free, high-quality backlinks** to your App Store page for SEO.
*   **A sudden spike in downloads** (1,000 - 5,000+ D1 installs) which trains the App Store algorithm that the app is popular, pushing it up in organic search rankings *before* you start spending money on Apple Search Ads.
*   **Valuable technical feedback** and bug reports from power users regarding model inference across different mobile hardware.
