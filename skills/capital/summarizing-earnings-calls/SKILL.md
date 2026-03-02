---
name: summarizing-earnings-calls
description: Transforms earnings call transcripts into structured summaries with financial guidance, KPI changes, management sentiment, and analyst Q&A highlights. Use when processing quarterly earnings calls, preparing investment research, or tracking company performance narratives.
tags:
  - summarization
  - equity-research
  - investment
  - research
metadata:
  author: casemark
  practice_areas:
    - Equity Research
    - Investment Management
  document_types:
    - Summary Report
  skill_modes:
    - Summarization
---

# Summarizing Earnings Calls

## Why This Skill Exists

Earnings calls are the single most information-dense event in the public-equity calendar. Every quarter, management teams deliver prepared remarks and field analyst questions — compressing capital-allocation decisions, operating trends, and forward guidance into 45–90 minutes. Buy-side analysts covering 30–60 names cannot attend every call live. They need structured, comparable summaries that surface what moved and what matters, delivered within hours of the call ending.

This skill converts a raw earnings-call transcript into a multi-section research summary that tracks beats/misses, guidance changes, KPI trajectories, management tone, and analyst Q&A signal — in a format that plugs directly into an investment workflow.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Before touching the transcript, collect the following from the user. Do not proceed until every required field is answered.

| Field | Required | Why It Matters |
|---|---|---|
| **Ticker / Company name** | Yes | Determines industry KPI set and peer context |
| **Quarter & fiscal year** | Yes | Anchors YoY and QoQ comparisons |
| **Consensus estimates** (Revenue, EPS at minimum) | Yes | Enables beat/miss framing — the single most actionable data point |
| **Prior-quarter guidance** (if any) | Yes | Needed to quantify guidance revisions |
| **User's coverage context** | Recommended | "I cover SaaS infrastructure" vs. "I'm a generalist" changes emphasis |
| **Specific focus areas** | Recommended | e.g., "margin trajectory", "China exposure", "AI capex" |
| **Prior-quarter summary** (if available) | Optional | Enables language-delta and KPI-trend analysis |
| **Industry vertical** | Auto-infer | Drives the KPI extraction set (see §Industry KPI Matrix) |

If the user cannot supply consensus estimates, flag this limitation prominently and note that beat/miss language will be omitted.

---

## Workflow

### Step 1 — Structural Parse

Segment the transcript into its canonical sections:

1. **Operator / Safe Harbor** — note the safe-harbor disclaimer; do not summarize it, but confirm it exists.
2. **CEO Prepared Remarks** — strategic narrative, high-level results, thematic emphasis.
3. **CFO Prepared Remarks** — financial details: revenue, margins, EPS, cash flow, balance sheet, guidance.
4. **Other Executive Remarks** (if any) — segment heads, CTO on product, etc.
5. **Analyst Q&A** — each question/answer pair is a discrete unit.

If the transcript is missing section headers, infer boundaries from speaker changes and content transitions. Flag inferred boundaries with `[INFERRED SECTION BREAK]`.

### Step 2 — Headline Numbers Extraction

Build the **Financial Snapshot Table**:

| Metric | Reported | Consensus | Beat / Miss | YoY Δ | QoQ Δ |
|---|---|---|---|---|---|
| Revenue | $X.XXB | $X.XXB | Beat +X% | +X% | +X% |
| Adj. EPS | $X.XX | $X.XX | Miss −$0.XX | +X% | −X% |
| Gross Margin | XX.X% | — | — | +XXbps | −XXbps |
| Operating Margin | XX.X% | — | — | +XXbps | +XXbps |
| FCF | $X.XXB | — | — | +X% | +X% |

Rules:
- **GAAP vs Non-GAAP**: Always state which basis is used. If management leads with Non-GAAP (common), include both. Flag large adjustments (SBC > 10% of revenue, restructuring charges, one-time items).
- Use basis points (bps) for margin deltas, percentages for revenue/EPS deltas.
- If a metric is not disclosed or not applicable, write "Not disclosed" — never infer.

### Step 3 — Guidance Analysis

Build the **Guidance Table**:

| Metric | New Guidance | Prior Guidance | Δ | Consensus | vs. Street |
|---|---|---|---|---|---|
| FY Revenue | $XX.X–XX.XB | $XX.X–XX.XB | Raised +$XXM at midpoint | $XX.XB | Above / In-line / Below |
| Q+1 Revenue | $X.XX–X.XXB | — | New | $X.XXB | Above / Below |
| FY Adj. EPS | $X.XX–X.XX | $X.XX–X.XX | Narrowed, midpoint +$0.XX | $X.XX | Above |

Classify each guidance metric: **Raised / Maintained / Lowered / Narrowed / Initiated / Withdrawn**.

Quantify the magnitude: "$150M raise at midpoint, or +2.1% vs prior guide" is far more useful than "guidance was raised."

### Step 4 — Segment & KPI Deep Dive

Extract every segment-level disclosure and map to industry-relevant KPIs.

#### Industry KPI Matrix (select the applicable set)

| Vertical | Key KPIs to Extract |
|---|---|
| **SaaS / Cloud** | ARR, NRR/NDR, RPO/cRPO, CAC payback, gross retention, logo adds, DBE |
| **Retail / Consumer** | Same-store sales (SSS), comp growth, inventory turns, store count Δ, e-commerce mix |
| **Banks / Financials** | NIM, provision for credit losses, CET1 ratio, loan growth, deposit costs, NCO rate |
| **Industrials** | Book-to-bill, backlog, organic growth, price vs volume, input cost trends |
| **Pharma / Biotech** | Pipeline milestones, Rx volume, pricing/reimbursement, patent cliffs, R&D as % of revenue |
| **Semiconductors** | Design wins, wafer utilization, ASP trends, inventory days, lead times |
| **Media / Streaming** | Subscriber adds/churn, ARPU, content spend, ad revenue mix |

For each segment reported, produce a mini-table:

| Segment | Revenue | YoY Δ | Margin | Commentary |
|---|---|---|---|---|
| Cloud | $X.XB | +XX% | XX% | "Reacceleration driven by AI workloads" |
| Enterprise | $X.XB | +X% | XX% | "Large deal closures pushed to Q+1" |

### Step 5 — Management Sentiment & Tone Analysis

Score management tone on a 5-point scale and support with direct quotes.

| Dimension | Rating (1–5) | Key Evidence |
|---|---|---|
| **Overall confidence** | X | Direct quote |
| **Demand environment** | X | Direct quote |
| **Margin outlook** | X | Direct quote |
| **Competitive positioning** | X | Direct quote |

**Hedging language flags**: Track frequency and context of soft qualifiers — "we believe," "we expect," "we anticipate," "we're cautiously optimistic." Compare to prior quarter if a previous summary is available.

**Tone shifts**: If the user provides a prior-quarter summary, explicitly call out any change in language strength (e.g., "Management shifted from 'confident' to 'cautiously optimistic' on enterprise demand").

**Forward-looking statements**: Note material forward-looking claims but flag them as subject to safe-harbor provisions. Do not treat forward-looking language as commitments.

### Step 6 — Analyst Q&A Extraction

The Q&A section often contains the most investable information. Structure each exchange:

| # | Analyst (Firm) | Topic | Key Takeaway | New Info? | Evasion Flag |
|---|---|---|---|---|---|
| 1 | Jane Doe (GS) | AI monetization | Mgmt expects AI revenue to be "material" in FY+1 | Yes | No |
| 2 | John Smith (MS) | Gross margin headwinds | Deflected — "multiple puts and takes" | No | **Yes** |
| 3 | … | … | … | … | … |

Rules:
- **New Information**: Flag any disclosure in Q&A that was not in prepared remarks. This is where alpha lives.
- **Evasion Detection**: If management redirects, gives a non-answer, or uses vague language to avoid a direct question, flag it. Evasion on a topic is itself a signal.
- **Follow-up patterns**: Note if multiple analysts pressed on the same topic — this indicates Street-level concern.
- Capture the analyst's name and firm when identifiable (most transcripts include this).

### Step 7 — Capital Allocation & Balance Sheet

| Item | Current Quarter | Prior Quarter | Commentary |
|---|---|---|---|
| Share repurchases | $X.XB | $X.XB | New $XB authorization announced |
| Dividends | $X.XX/share | $X.XX/share | +X% YoY increase |
| Net debt / EBITDA | X.Xx | X.Xx | Deleveraging on track |
| M&A commentary | — | — | "Evaluating bolt-on opportunities in [segment]" |
| CapEx | $X.XB | $X.XB | +XX% YoY — driven by AI infrastructure |

### Step 8 — Risks & Watchlist Items

Compile a forward-looking watchlist:

- **Risks disclosed by management**: Macro, regulatory, supply chain, FX, competitive.
- **Risks implied by Q&A pressure**: Topics where multiple analysts pushed.
- **Risks inferred from data**: Decelerating growth, margin compression, rising DSO.

Format as a numbered list with severity tags: `[HIGH]` `[MEDIUM]` `[LOW]`.

---

## Output Structure

Assemble the final summary in this order:

1. **Header**: Ticker, Company, Quarter, Date, Call Duration
2. **TL;DR** (3–5 bullets): The most investable takeaways — what changed, what surprised
3. **Financial Snapshot Table** (Step 2)
4. **Guidance Table** (Step 3)
5. **Segment & KPI Detail** (Step 4)
6. **Management Tone** (Step 5)
7. **Analyst Q&A Highlights** (Step 6)
8. **Capital Allocation** (Step 7)
9. **Risks & Watchlist** (Step 8)
10. **Appendix**: GAAP/Non-GAAP reconciliation notes, definitions of non-standard KPIs

See `references/EARNINGS-SUMMARY-TEMPLATE.md` for a complete output template.

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

Present the draft to the user and explicitly ask:

1. **Completeness**: "Are there specific metrics or topics I missed that matter for your thesis?"
2. **Emphasis**: "Should I elevate or de-emphasize any section? (e.g., more detail on Q&A, less on balance sheet)"
3. **Accuracy**: "Please verify the consensus estimates and guidance figures I used — these are the highest-risk fields for error."
4. **Tone calibration**: "Does the sentiment scoring align with your read of the call?"
5. **Formatting**: "Any changes to structure for your internal template or distribution list?"

Iterate once based on feedback. If the user requests a second revision, proceed but note that the quality ceiling is limited by transcript fidelity.

---

## Quality Audit

Before finalizing, verify against this checklist:

| # | Check | Pass? |
|---|---|---|
| 1 | Every reported metric cites GAAP or Non-GAAP basis | |
| 2 | Beat/miss framing uses user-provided consensus — not hallucinated estimates | |
| 3 | Guidance deltas are quantified at the midpoint, not just directional | |
| 4 | No forward-looking statement is presented as a commitment or fact | |
| 5 | Analyst names and firms are attributed where identifiable | |
| 6 | Evasion flags are supported by specific non-answer quotes | |
| 7 | YoY and QoQ deltas use consistent basis (same quarter, same metric definition) | |
| 8 | Industry-specific KPIs match the company's actual vertical | |
| 9 | Risks section includes at least one item from each source (disclosed, Q&A-implied, data-inferred) | |
| 10 | `[VERIFY]` tags are attached to any data point sourced from inference rather than explicit transcript text | |
| 11 | No material information from Q&A is omitted from the summary | |
| 12 | Compliance disclaimer is present if output will be distributed externally | |

---

## Key Rules

- **Never fabricate consensus estimates.** If not provided, omit beat/miss language entirely.
- **Always distinguish GAAP from Non-GAAP.** When management presents Non-GAAP as the headline, include the GAAP figure in a footnote or reconciliation note.
- **Mark uncertain data with `[VERIFY]`.** This includes unclear speaker attribution, ambiguous numbers, and inferred section breaks.
- **Do not editorialize.** "Management sounded defensive" is acceptable only if supported by quoted evidence. "This was a bad quarter" is never acceptable.
- **Safe harbor awareness.** Acknowledge forward-looking statements but do not amplify or discount them without basis.
- **Escalate to human review** when the transcript is partial, audio-to-text artifacts are present, or the company uses unusual reporting frameworks.
