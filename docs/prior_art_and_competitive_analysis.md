# Consensus Engine: Prior Art & Competitive Intelligence Analysis

## Executive Summary
This document provides a comprehensive market, academic, and open-source audit to determine whether the **AI Consensus Engine** (or its constituent sub-modules) has been built by others—either as standalone products, open-source frameworks, or features embedded inside Big Tech platforms.

---

## 1. Sub-Module Breakdown: What Has Already Been Built?

The Consensus Engine is composed of five distinct technical primitives. Each primitive has existing prior art in different stages of maturity:

```
┌────────────────────────────────────────────────────────────────────────────────────────┐
│                               THE CONSENSUS ENGINE PRIMITIVES                          │
├────────────────────────┬─────────────────────────┬───────────────────┬────────────────┤
│ Primitive Module       │ Market Maturity         │ Primary Builders  │ Dominant Tech  │
├────────────────────────┼─────────────────────────┼───────────────────┼────────────────┤
│ 1. Academic RAG        │ High (Commercial SaaS)  │ Consensus.app     │ PubMed Embeds  │
│    (Scientific Truth)  │                         │ Scite.ai, Elicit  │ LLM Synthesis  │
├────────────────────────┼─────────────────────────┼───────────────────┼────────────────┤
│ 2. Claim Verification  │ Moderate (Research/OSS) │ MultiVerS (Allen) │ FEVER dataset  │
│    from Media          │                         │ Bullshit-Detector │ Multimodal LLM │
├────────────────────────┼─────────────────────────┼───────────────────┼────────────────┤
│ 3. Author Credibility  │ High (Finance & Trust)  │ TipRanks          │ Graph Networks │
│    & Trust Graphs      │                         │ X Community Notes │ Matrix Factor. │
├────────────────────────┼─────────────────────────┼───────────────────┼────────────────┤
│ 4. Computer Vision     │ High (Fitness Apps)     │ Tonal, Tempo      │ MediaPipe      │
│    Pose Form Check     │                         │ FormFix.AI        │ Joint Angles   │
├────────────────────────┼─────────────────────────┼───────────────────┼────────────────┤
│ 5. Closed-Loop         │ Non-Existent / Rare     │ UNBUILT           │ Proprietary    │
│    Proprioceptive Loop │ (Greenfield Moat)       │ (WikiGem Space)   │ Feedback Loop  │
└────────────────────────┴─────────────────────────┴───────────────────┴────────────────┘
```

---

## 2. Detailed Landscape Audit by Primitive

### A. Academic Literature & Scientific Grounding
*   **What exists:**
    *   **[Consensus.app](https://consensus.app):** Commercial AI search engine querying 200M+ peer-reviewed papers. It extracts a "Consensus Meter" showing what percentage of research agrees with a medical/health query.
    *   **[Scite.ai](https://scite.ai):** Indexes over 1.2B citation statements, classifying citations as *supporting*, *contrasting*, or *mentioning*.
    *   **[Elicit.org](https://elicit.org):** Automates research workflows and systematically extracts findings from clinical trials.
    *   **[MultiVerS](https://github.com/dwadden/multivers) (Allen Institute for AI):** Open-source model specifically trained to verify scientific claims against biomedical abstracts.
*   **Assessment:** *Commodity.* You do not need to build academic RAG from scratch; existing tools and vector indexes (PubMed, Semantic Scholar API) already provide the foundation.

### B. Claim Verification from Social Media
*   **What exists:**
    *   **[SerhiiKorniienko/bullshit-detector](https://github.com/SerhiiKorniienko/bullshit-detector):** Open-source agent that breaks YouTube videos and social posts into atomic claims and cross-verifies them against sources to output a 0–10 BS score.
    *   **[konoeph/AgentClaimGuard](https://github.com/konoeph/AgentClaimGuard):** Open-source evidence gate verifying LLM agent claims against policies and retrieved tool outputs.
    *   **[ClaimBuster / FEVER Benchmark](https://github.com/ASoleimaniB/BERT_FEVER):** Natural Language Processing pipeline that extracts factual claims and tests them against Wikipedia / reference corpora.
*   **Assessment:** *Established in academic NLP.* Extracting claims and matching them against a text database is a solved pattern.

### C. Creator Credibility & Trust Networks
*   **What exists:**
    *   **[TipRanks](https://tipranks.com):** The gold standard in finance. Scores financial bloggers, analysts, and Twitter accounts based on actual historical success rates of their stock calls.
    *   **[X / Twitter Community Notes (Birdwatch)](https://github.com/twitter/communitynotes):** Open-source consensus algorithm. Uses matrix factorization to find consensus across users who typically hold opposing viewpoints, preventing partisan vote-brigading.
    *   **[Google E-E-A-T & YouTube Health Shelves](https://support.google.com/youtube/answer/12209736):** Algorithmic verification that boosts licensed doctors/PTs and flags videos from unaccredited sources.
    *   **[Anti-AI Bot Spam (AABS)](https://github.com/steve-rodrigue/aabs):** Open-source project evaluating social comment networks to score account authenticity and suppress bot spam.
*   **Assessment:** *Established in Finance and Social Platforms.* However, **deterministic clinical comment gatekeeping** (filtering comments exclusively for users with certified medical credentials or rigorous anatomical terminology) is virtually untouched in consumer health apps.

### D. Computer Vision Pose Estimation & Form Checks
*   **What exists:**
    *   **Hardware Gyms (Tonal, Tempo):** Proprietary 3D sensors that track joint positions and count reps.
    *   **Mobile / Open-Source (FormFix.AI, RepDetect, MediaPipe Pose):** Open-source libraries that calculate joint angles (e.g. knee-over-toe angle, hip hinge depth) using consumer phone webcams and compare them to ideal reference ranges.
*   **Assessment:** *Widely built in isolation.* Hundreds of projects can tell a user *"Your knees collapsed inward during that squat."*

---

## 3. What Has NOT Been Built: The "Novelty Gap" & Moat

While each sub-module exists in isolation, **nobody has connected them into a closed-loop truth machine**. Here is the exact white space WikiGem occupies:

### 1. Disconnection of Advice from Physical Validation
*   Existing claim verification tools (Consensus.app, ClaimBuster) verify **text against text**. They check whether words in a video match words in a paper.
*   Existing form checkers (Tonal, MediaPipe apps) verify **angles against hardcoded standards**. They assume the exercise being performed is already correct.
*   **The Novelty Gap:** No system tests whether the *creator's advice itself* succeeds or fails when executed with verified form in the real world.

### 2. The Proprioception Feedback Loop (Activation vs. Pain)
*   Standard apps ask: *"Did you finish the workout? Rate 1 to 5 stars."*
*   WikiGem asks: *"MediaPose confirmed your knees were aligned. Where on this 3D body map did you feel tension? Did your glute fire, or did your lower back ache?"*
*   By conditioning tip penalization on **(Form Verified + Activation Exercises Done + Pain Still Reported)**, WikiGem isolates whether the advice itself is biomechanically flawed versus just executed poorly.

### 3. The Diagnostic Decoding Engine (Hypothesizing "Cures")
*   No consumer fitness app correlates failure rates with anatomical geometry (e.g. *"82% of people with long femurs fail standard squats"*).
*   No consumer fitness app automatically crawls its vector database to find another creator's cue that solves that exact anatomical constraint (e.g. *"Elevate heels on wedges"*) and runs an automated A/B test across affected users to see if the failure rate drops.

---

## 4. Competitive Intelligence Summary Matrix

| Capability | Consensus.app | TipRanks | Tonal / MediaPipe Apps | X Community Notes | **WikiGem Consensus Engine** |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Claim Extraction from Video** | ❌ | ❌ | ❌ | ❌ | ✅ |
| **Scientific RAG Literature** | ✅ | ❌ | ❌ | ❌ | ✅ |
| **Creator Credibility Scoring** | ❌ | ✅ | ❌ | ✅ | ✅ |
| **Clinical Comment Filtering** | ❌ | ❌ | ❌ | ❌ | ✅ |
| **Real-Time CV Form Check** | ❌ | ❌ | ✅ | ❌ | ✅ |
| **Proprioceptive Body Mapping** | ❌ | ❌ | ❌ | ❌ | ✅ |
| **Demographic Failure Trend Analysis** | ❌ | ❌ | ❌ | ❌ | ✅ |
| **Automated "Cure" A/B Testing** | ❌ | ❌ | ❌ | ❌ | ✅ |
| **Anti-Hallucination Strict Provenance** | ✅ | ❌ | ❌ | ❌ | ✅ |

---

## 5. Strategic Recommendations for Builders

1. **Do NOT Reinvent the Commodity Pieces:**
   * Use **MediaPipe Pose** directly for webcam tracking rather than training custom vision models.
   * Use **Semantic Scholar / PubMed APIs** or **ChromaDB embeddings** for academic literature RAG.
   * Use **Apify + Whisper + Gemini Flash** for video multimodal extraction.
2. **Focus 100% of Proprietary Effort on the Moat:**
   * Build the **Proprioception 3D Body Map & Conditional Penalty Math**.
   * Build the **Diagnostic Decoding Engine** (Failure trends correlated to body geometry).
   * Build the **Clinical Comment Filter** (Throwing out 99% of spam comments and ranking creators by PT peer endorsements).
