import subprocess
import os

html_content = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>The AI Consensus Engine: A Guide to Building Truth & Trust in the AI Era</title>
<style>
  @page {
    size: letter;
    margin: 12mm 13mm 12mm 13mm;
    @bottom-right {
      content: "Page " counter(page);
      font-size: 8pt;
      color: #718096;
    }
  }

  * {
    box-sizing: border-box;
  }

  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: #1a202c;
    line-height: 1.45;
    font-size: 9pt;
    margin: 0;
    padding: 0;
    background-color: #ffffff;
  }

  .header {
    border-bottom: 2px solid #2b6cb0;
    padding-bottom: 8px;
    margin-bottom: 10px;
  }

  .badge {
    display: inline-block;
    background: #ebf8ff;
    color: #2b6cb0;
    font-weight: 700;
    font-size: 7.5pt;
    text-transform: uppercase;
    letter-spacing: 0.06em;
    padding: 2px 6px;
    border-radius: 4px;
    margin-bottom: 4px;
    border: 1px solid #bee3f8;
  }

  h1 {
    font-size: 18pt;
    color: #1a365d;
    margin: 2px 0 4px 0;
    line-height: 1.2;
    font-weight: 800;
  }

  .subtitle {
    font-size: 9.5pt;
    color: #4a5568;
    margin: 0;
    font-weight: 400;
  }

  .meta-bar {
    margin-top: 6px;
    font-size: 8pt;
    color: #718096;
    display: flex;
    gap: 14px;
    flex-wrap: wrap;
  }

  h2 {
    font-size: 12pt;
    color: #2b6cb0;
    margin-top: 12px;
    margin-bottom: 5px;
    border-bottom: 1px solid #e2e8f0;
    padding-bottom: 3px;
    page-break-after: avoid;
    font-weight: 700;
  }

  h3 {
    font-size: 9.5pt;
    color: #2d3748;
    margin-top: 8px;
    margin-bottom: 3px;
    page-break-after: avoid;
    font-weight: 600;
  }

  p {
    margin-top: 0;
    margin-bottom: 5px;
  }

  ul, ol {
    margin-top: 0;
    margin-bottom: 5px;
    padding-left: 16px;
  }

  li {
    margin-bottom: 2px;
  }

  .card {
    background: #f7fafc;
    border: 1px solid #e2e8f0;
    border-left: 3.5px solid #3182ce;
    border-radius: 5px;
    padding: 7px 10px;
    margin-bottom: 8px;
    page-break-inside: avoid;
  }

  .card.warning {
    border-left-color: #dd6b20;
    background: #fffaf0;
  }

  .card.success {
    border-left-color: #38a169;
    background: #f0fff4;
  }

  .card.purple {
    border-left-color: #805ad5;
    background: #faf5ff;
  }

  .card-title {
    font-weight: 700;
    font-size: 9pt;
    margin-bottom: 2px;
    color: #2d3748;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 6px;
    margin-bottom: 8px;
    font-size: 8pt;
    page-break-inside: avoid;
  }

  th, td {
    padding: 5px 7px;
    text-align: left;
    border: 1px solid #e2e8f0;
    vertical-align: top;
  }

  th {
    background-color: #edf2f7;
    color: #2d3748;
    font-weight: 700;
  }

  tr:nth-child(even) {
    background-color: #f7fafc;
  }

  .diagram-flow {
    background: #f8fafc;
    border: 1px solid #cbd5e0;
    border-radius: 5px;
    padding: 8px;
    margin: 8px 0;
    text-align: center;
    page-break-inside: avoid;
    display: flex;
    justify-content: space-around;
    align-items: center;
    flex-wrap: wrap;
    gap: 4px;
  }

  .step-box {
    padding: 4px 7px;
    background: #ffffff;
    border: 1.5px solid #3182ce;
    border-radius: 4px;
    font-size: 7.5pt;
    font-weight: 700;
    color: #2b6cb0;
  }

  .arrow {
    color: #718096;
    font-weight: bold;
    font-size: 8pt;
  }

  .grid-2 {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    margin-bottom: 8px;
    page-break-inside: avoid;
  }

  .grid-item {
    background: #f7fafc;
    border: 1px solid #e2e8f0;
    border-radius: 5px;
    padding: 6px 8px;
  }

  .grid-item h4 {
    margin: 0 0 2px 0;
    font-size: 8.5pt;
    color: #2b6cb0;
  }

  .grid-item p {
    font-size: 7.5pt;
    margin: 0;
    color: #4a5568;
    line-height: 1.3;
  }

  .industry-card {
    background: #ffffff;
    border: 1px solid #e2e8f0;
    border-radius: 5px;
    padding: 6px 9px;
    margin-bottom: 6px;
    page-break-inside: avoid;
  }

  .industry-title {
    font-weight: 700;
    font-size: 8.5pt;
    color: #1a365d;
    margin-bottom: 2px;
    display: flex;
    justify-content: space-between;
  }

  .industry-tag {
    font-size: 7pt;
    padding: 1px 5px;
    background: #edf2f7;
    border-radius: 3px;
    color: #4a5568;
    font-weight: 600;
  }

  .section-block {
    page-break-inside: avoid;
    margin-bottom: 6px;
  }
</style>
</head>
<body>

<div class="header">
  <span class="badge">Executive Whitepaper & Strategy Guide</span>
  <h1>The AI Consensus Engine</h1>
  <div class="subtitle">How to Build a "Truth & Trust" Machine for Noisy Human Knowledge Across Any Industry</div>
  <div class="meta-bar">
    <span><strong>Target Audience:</strong> Founders, Product Leaders & Builders</span>
    <span><strong>Core Focus:</strong> Verifiable AI, Closed-Loop Grounding & Cross-Industry Blueprint</span>
  </div>
</div>

<h2>1. The Problem: The Internet's "Popularity Trap"</h2>
<p>
  Today, anyone with a smartphone can broadcast advice to millions. On Instagram, TikTok, LinkedIn, YouTube, and Reddit, algorithms optimize for <strong>engagement, sensationalism, and outrage</strong>—not truth.
</p>
<p>
  When generative AI tools (ChatGPT, Perplexity, Gemini) browse the web to answer questions, they inevitably fall into the <strong>Popularity Trap</strong>: if 50,000 creators repeat a flawed finance hack, a dangerous gym exercise, or bad legal advice, the AI assumes it is consensus and serves it as fact.
</p>

<div class="card warning">
  <div class="card-title">The Fundamental Flaw of Standard AI</div>
  <p>
    Standard AI calculates truth by measuring <em>how often words co-occur on the internet</em>. But in the real world, <strong>viral popularity ≠ factual truth</strong>. An AI that merely summarizes the crowd acts as a megaphone for collective misinformation.
  </p>
</div>

<h2>2. What is an AI Consensus Engine?</h2>
<p>
  An <strong>AI Consensus Engine</strong> is an automated "truth & credibility verification system." Instead of believing what an influencer says or generating advice from raw statistics, it functions as:
</p>
<ul>
  <li><strong>The Librarian:</strong> It never invents advice. It catalogs verified claims from real human experts with exact receipts (citations).</li>
  <li><strong>The Peer Reviewer:</strong> It evaluates whether reputable domain authorities agree with the claim, ignoring bot comments and hype.</li>
  <li><strong>The Real-World Sensor:</strong> It measures actual outcomes (did this tip work, fail, or cause harm when applied in real life?).</li>
</ul>

<div class="card purple">
  <div class="card-title">The 3 Legs of the Truth Stool</div>
  <p>An idea is only accepted as "True Consensus" if it is supported by three independent pillars:</p>
  <div class="grid-2" style="margin-top: 4px;">
    <div class="grid-item">
      <h4>1. Who Said It? (Credibility)</h4>
      <p>Is the author backed by peer respect and qualified credentials, or selling snake oil?</p>
    </div>
    <div class="grid-item">
      <h4>2. What Does Science Say? (Cross-Check)</h4>
      <p>Do formal research papers or official standards back this up, and do peers echo it?</p>
    </div>
  </div>
  <div style="text-align: center; margin-top: 3px; font-weight: 600; font-size: 8pt; color: #805ad5;">
    + Leg 3: What Happened in Reality? (Empirical Real-World Outcome Telemetry)
  </div>
</div>

<h2>3. How It Works (Without the Code Jargon)</h2>
<p>The Consensus Engine evaluates incoming advice across two main questions:</p>

<h3>Axis A: Can We Trust the Author? (The "Trust Score", 0–100)</h3>
<ul>
  <li><strong>The Respect Network:</strong> Instead of counting followers (which can be bought), the engine maps who follows whom. A creator followed by 50 board-certified specialists gets high authority even with modest followers.</li>
  <li><strong>Qualified Comment Filtering:</strong> The engine throws out 99% of comments ("Awesome video!", emojis, memes). It only listens to feedback from people with demonstrated domain credentials or precise technical vocabulary.</li>
  <li><strong>"Hidden Gem" Discovery:</strong> When small, unknown creators share unique insights that match established science, the engine automatically surfaces them.</li>
</ul>

<h3>Axis B: Does the Specific Advice Hold Water? (The "Congruence Score", 0–100)</h3>
<ul>
  <li><strong>The Echo Test:</strong> Do multiple unrelated experts independently recommend the exact same technique? When experts converge without copying each other, it is likely foundational truth.</li>
  <li><strong>The Literature Cross-Check:</strong> The advice is checked against formal research libraries (academic papers, regulatory guidelines, official specifications).</li>
  <li><strong>The Real-World Reality Check:</strong> If real users apply the advice and experience negative outcomes, the advice is penalized and downgraded.</li>
</ul>

<div class="card">
  <div class="card-title">The "Critic" Guardrail (Strict Receipts)</div>
  <p>
    The AI is <strong>strictly forbidden from answering on its own</strong>. Every single recommendation must be tied to a verified source receipt. If the engine cannot prove a claim with evidence, it is hard-programmed to admit: <em>"There is not enough verifiable consensus on this topic."</em>
  </p>
</div>

<h2>4. Cross-Industry Applications: How Other Domains Use It</h2>
<p>While WikiGem applied this to fitness and physical therapy, the exact same architecture solves multi-billion dollar problems across major industries:</p>

<div class="industry-card">
  <div class="industry-title">
    <span>1. Finance & Wealth Management</span>
    <span class="industry-tag">Fintech & Retail Investing</span>
  </div>
  <p><strong>The Problem:</strong> "Finfluencers" on TikTok and YouTube hype volatile stocks, crypto tokens, or risky tax avoidance schemes.</p>
  <p><strong>How the Consensus Engine Solves It:</strong></p>
  <ul>
    <li><em>Credibility Filter:</em> Filters comments for chartered analysts (CFAs, CPAs) and discards hype bots.</li>
    <li><em>Cross-Check:</em> Compares pitches against audited SEC 10-K filings, Bloomberg consensus, and macroeconomic data.</li>
    <li><em>Outcome Feedback:</em> Tracks real-world portfolio performance over 6–24 months. Creators whose tips consistently lose money have their trust scores degraded.</li>
  </ul>
</div>

<div class="industry-card">
  <div class="industry-title">
    <span>2. Healthcare & Nutrition</span>
    <span class="industry-tag">Digital Health & Longevity</span>
  </div>
  <p><strong>The Problem:</strong> Contradictory diet fads, miracle supplements, and dubious medical hacks spread unchecked on social feeds.</p>
  <p><strong>How the Consensus Engine Solves It:</strong></p>
  <ul>
    <li><em>Credibility Filter:</em> Prioritizes authors endorsed by academic medical centers and accredited clinicians.</li>
    <li><em>Cross-Check:</em> Compares claims against double-blind, placebo-controlled trials on PubMed and FDA safety alerts.</li>
    <li><em>Outcome Feedback:</em> Integrates with health wearables (biomarkers, continuous glucose monitors, blood panels) to verify whether the diet actually improved metabolic markers.</li>
  </ul>
</div>

<div class="industry-card">
  <div class="industry-title">
    <span>3. Software Engineering & Cloud Infrastructure</span>
    <span class="industry-tag">Developer Tools & Cybersecurity</span>
  </div>
  <p><strong>The Problem:</strong> Blogs and social threads promote outdated architectural patterns, insecure code snippets, or trendy libraries that fail under scale.</p>
  <p><strong>How the Consensus Engine Solves It:</strong></p>
  <ul>
    <li><em>Credibility Filter:</em> Measures how many Principal/Staff engineers and core maintainers endorse the pattern.</li>
    <li><em>Cross-Check:</em> Checks recommendations against official RFCs, security vulnerability databases (CVEs), and cloud architecture benchmarks.</li>
    <li><em>Outcome Feedback:</em> Collects telemetry from staging/production deployments (latency, memory leaks, crash rates). Advice that causes outages is blacklisted.</li>
  </ul>
</div>

<div class="industry-card">
  <div class="industry-title">
    <span>4. Legal, Tax & Regulatory Compliance</span>
    <span class="industry-tag">LegalTech & Corporate Governance</span>
  </div>
  <p><strong>The Problem:</strong> Small business owners follow viral "tax loop" or contract advice that exposes them to catastrophic audits or lawsuits.</p>
  <p><strong>How the Consensus Engine Solves It:</strong></p>
  <ul>
    <li><em>Credibility Filter:</em> Verifies active state bar standing, court appearances, and peer citations among legal scholars.</li>
    <li><em>Cross-Check:</em> Cross-references claims against statutory tax codes, court precedent, and IRS revenue rulings.</li>
    <li><em>Outcome Feedback:</em> Gathers outcomes from legal filings and audit results, alerting users to emerging regulatory crackdowns.</li>
  </ul>
</div>

<div class="industry-card">
  <div class="industry-title">
    <span>5. Fitness & Biomechanics (The WikiGem Example)</span>
    <span class="industry-tag">Sports Tech & Physical Therapy</span>
  </div>
  <p><strong>The Problem:</strong> Flashy gym influencers teach high-risk workout cues that cause joint damage to lifters with different body proportions.</p>
  <p><strong>How the Consensus Engine Solves It:</strong></p>
  <ul>
    <li><em>Credibility Filter:</em> Tracks physical therapy credentials and filters comments for clinical terminology.</li>
    <li><em>Cross-Check:</em> Compares cues against sports science papers and semantic agreement across top therapists.</li>
    <li><em>Outcome Feedback:</em> Uses phone cameras (MediaPose) to verify exercise form, coupled with a 3D body map where users log muscle activation vs. joint pain.</li>
  </ul>
</div>

<h2>5. The "Diagnostic Cure" Engine: Beyond Pass/Fail</h2>
<p>Most AI systems treat failure as a binary error. A Consensus Engine treats failure as <strong>diagnostic data</strong>:</p>

<div class="diagram-flow">
  <div class="step-box">1. User Applies Advice</div>
  <span class="arrow">▶</span>
  <div class="step-box">2. Outcome Fails</div>
  <span class="arrow">▶</span>
  <div class="step-box">3. Profile Context Analyzed</div>
  <span class="arrow">▶</span>
  <div class="step-box">4. Automatic Cure Suggested</div>
</div>

<ul>
  <li><strong>In Fitness:</strong> If 80% of users with long femurs get lower-back pain from back squats, the engine doesn't just say "squats are bad." It diagnoses the body geometry and tests solutions (e.g. <em>"Elevate heels 1 inch"</em> or <em>"Do front squats instead"</em>).</li>
  <li><strong>In Finance:</strong> If an investing strategy fails for freelance workers with irregular income, the engine isolates the variable and recommends higher cash buffers before investing.</li>
  <li><strong>In Software:</strong> If microservice advice causes downtime for 5-person engineering teams, the engine learns the team-size threshold and prescribes a modular monolith instead.</li>
</ul>

<h2>6. Why You Can't Just Use Off-the-Shelf AI</h2>

<table>
  <thead>
    <tr>
      <th style="width: 25%;">Off-The-Shelf Tool</th>
      <th style="width: 35%;">How People Try to Use It</th>
      <th style="width: 40%;">Why It Fails Without a Consensus Engine</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>ChatGPT / Gemini / Claude</strong></td>
      <td>Prompting the AI to "act like an expert" or browse the web.</td>
      <td><strong>Hallucination & Popularity Bias:</strong> They generate answers based on word frequency, not real-world validity. They cannot tell an expert from a marketer.</td>
    </tr>
    <tr>
      <td><strong>Perplexity / AI Search</strong></td>
      <td>Searching live web pages and summarizing articles.</td>
      <td><strong>SEO Exploitation:</strong> Search engines rank content based on keyword optimization and backlinks, not verified efficacy or safety.</td>
    </tr>
    <tr>
      <td><strong>Standard RAG (Document Search)</strong></td>
      <td>Searching a company's internal PDF or document database.</td>
      <td><strong>Blind Matching:</strong> Matches text keywords without verifying author authority, peer consensus, or whether the advice actually worked.</td>
    </tr>
  </tbody>
</table>

<div style="page-break-before: always;"></div>
<h2>7. How to Build a Consensus Engine: A 4-Step Blueprint</h2>

<div class="section-block">
  <h3>Step 1: Ingest & Atomize</h3>
  <p>Collect messy human content (videos, posts, blogs, podcasts) and break them into <strong>single, atomic claims</strong> (e.g., <em>"Claim: Keep knees behind toes during squats"</em> or <em>"Claim: Dollar-cost averaging beats lump-sum investing in bull markets"</em>).</p>
</div>

<div class="section-block">
  <h3>Step 2: Build the Trust & Cross-Referencing Graph</h3>
  <p>Rate the author using peer endorsements and professional audience feedback. Then, map the claim into a vector database to see if other trusted authors agree and whether academic/regulatory literature backs it up.</p>
</div>

<div class="section-block">
  <h3>Step 3: Hook Up Real-World Outcome Telemetry</h3>
  <p>This is the secret sauce. Build a mechanism to track what happens when someone actually applies the advice. (Did form look right? Did the portfolio make money? Did the code break? Did the diet lower inflammation?). Use this telemetry to adjust scores.</p>
</div>

<div class="section-block">
  <h3>Step 4: Deploy the "Critic" Anti-Hallucination Shield</h3>
  <p>Ensure your AI interface is incapable of guessing. If an output lacks direct citations to trusted sources and confirmed outcomes, the system gracefully declines to answer.</p>
</div>

<h2>8. Executive Checklist for Builders & Leaders</h2>
<div class="grid-2">
  <div class="grid-item">
    <h4>1. What is your Source of Truth?</h4>
    <p>Do you have a grounded anchor (scientific papers, SEC filings, RFC specs) to counterbalance public opinion?</p>
  </div>
  <div class="grid-item">
    <h4>2. How will you collect Outcomes?</h4>
    <p>How will your product know if an advice succeeded or failed? (Cameras, telemetry, portfolios, symptom tracking).</p>
  </div>
  <div class="grid-item">
    <h4>3. How do you stop Sybil/Bot Gaming?</h4>
    <p>Are you gating audience feedback by credentials or clinical vocabulary, or can anyone game the score?</p>
  </div>
  <div class="grid-item">
    <h4>4. Is Liability Transferred?</h4>
    <p>Does your user interface display exact source receipts so your product remains a trusted curator, not a liable advisor?</p>
  </div>
</div>

<div class="card success" style="margin-top: 6px;">
  <div class="card-title">Key Takeaway</div>
  <p>
    The future of AI is not larger models with more parameters—it is <strong>verifiable truth architectures</strong>. A Consensus Engine bridges the gap between chaotic human opinions and reliable, ground-truth intelligence across any knowledge-intensive domain.
  </p>
</div>

</body>
</html>
"""

with open("/tmp/consensus_guide.html", "w") as f:
    f.write(html_content)

print("HTML generated successfully at /tmp/consensus_guide.html")
