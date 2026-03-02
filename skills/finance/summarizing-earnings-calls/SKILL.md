---
name: summarizing-earnings-calls
description: Transforms earnings call transcripts into structured summaries with financial guidance, KPI changes, management sentiment, and analyst Q&A highlights. Use when processing quarterly earnings calls, preparing investment research, or tracking company performance narratives.
tags:
  - summarization
  - equity-research
  - corporate
metadata:
  author: casemark
  practice_areas:
    - Equity Research
    - Investment Management
  document_types:
    - Earnings Call Transcript
  skill_modes:
    - Summarization
---

# Summarizing Earnings Calls

Converts verbose earnings call transcripts into actionable intelligence.

## Workflow

1. **Extract** prepared remarks — CEO/CFO key messages, guidance changes
2. **Capture** financial metrics — revenue, EPS, margins, guidance (compare to prior quarter/consensus)
3. **Analyze** Q&A section — key analyst concerns, management deflections, new disclosures
4. **Assess** tone — confidence level, hedging language, forward-looking optimism/caution
5. **Flag** surprises — guidance changes, one-time items, strategic shifts, management changes

## Output Template

```markdown
## Earnings Call Summary: [Company] — [Quarter/Year]

### Key Numbers
| Metric | Reported | Consensus | Prior Quarter | YoY Change |
|--------|----------|-----------|--------------|------------|
| Revenue | | | | |
| EPS | | | | |
| Gross Margin | | | | |
| Operating Margin | | | | |

### Guidance Update
| Metric | New Guidance | Prior Guidance | Change |
|--------|-------------|---------------|--------|

### Management Key Messages
1. [Top message/theme from prepared remarks]
2. [Second key message]
3. [Third key message]

### Analyst Q&A Highlights
| Analyst / Firm | Question Topic | Management Response | Notable? |
|---------------|---------------|-------------------|----------|

### Tone Assessment
- **Overall**: [Confident / Cautious / Defensive / Neutral]
- **Notable Language**: [Specific hedging or bullish phrases]

### Surprises / Action Items
- [Anything unexpected or requiring follow-up]
```

## Key Rules

- Always compare to consensus AND prior quarter — beats/misses matter
- Distinguish GAAP from non-GAAP metrics — note which is being discussed
- Track guidance changes precisely — range widened, narrowed, raised, lowered
- Management tone matters: "confident" vs. "cautiously optimistic" vs. hedging language
- Note what management did NOT address that analysts asked about
- One-time items / non-recurring charges must be called out separately

For earnings call structure patterns, see [references/EARNINGS-TEMPLATE.md](references/EARNINGS-TEMPLATE.md).
