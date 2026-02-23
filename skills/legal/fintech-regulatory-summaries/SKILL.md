---
name: fintech-regulatory-summaries
description: Generates concise, actionable regulatory summaries covering recent developments impacting fintech sectors including mobile banking, cryptocurrency, digital assets, electronic payments, money transmission, and peer-to-peer lending. Covers federal and state-level changes from CFPB, SEC, CFTC, FinCEN, OCC, Federal Reserve, and state regulators. Prioritizes developments from the past 90 days with urgency triage and compliance deadlines. Use when compliance officers or legal teams need to navigate recent financial regulation changes, monitor agency guidance, or produce regulatory status reports.
tags:
  - analysis
  - regulatory
  - research
  - summarization
  - summary
---

# Fintech Regulatory Summary

Produces a structured regulatory update enabling fintech compliance officers and legal counsel to quickly identify critical developments, compliance deadlines, and required actions.

## Prerequisites

1. **Scope parameters** — sectors of interest (crypto, payments, lending, mobile banking, regtech) and any specific agencies or topics to prioritize
2. **Time window** — default is past 90 days; adjust if narrower/broader coverage needed
3. **Jurisdictions** — federal only, specific states, or full multi-jurisdictional sweep
4. **Business context** (optional) — company's regulated activities to tailor materiality assessments

## Output Structure

### 1. Executive Overview
3–5 bullet items, each covering:
- **What changed** (rule/guidance/enforcement action + agency)
- **Who it affects** (specific fintech activity or model)
- **Urgency** (`Immediate` / `Near-Term` / `Monitor`)
- **Deadline** (effective date or comment period close)

### 2. Detailed Analysis by Topic/Agency

For each significant development, provide:

| Field | Content |
|---|---|
| **Source** | Agency, document title, FR citation or docket no. [VERIFY] |
| **Effective/Comment Date** | Specific date or "Proposed — Comment by [date]" |
| **Sectors Affected** | Crypto exchanges / Payment processors / Lenders / MSBs / etc. |
| **Key Requirements** | Numbered compliance obligations extracted from regulatory text |
| **Ambiguities** | Areas of interpretive uncertainty or pending agency guidance |
| **Recommended Action** | Specific next steps (update policies, file comments, conduct gap analysis) |

### 3. Regulatory Interaction Map
Note where multiple frameworks overlap on a single development (e.g., a crypto custody rule implicating SEC + OCC + FinCEN simultaneously). Flag conflict or gap between federal and state approaches.

### 4. State Spotlight (if applicable)
Highlight notable state-level divergence in:
- Money transmitter licensing (MTL) requirements
- State crypto or digital asset frameworks
- State consumer lending rate caps or disclosure rules

### 5. International Context (crypto/cross-border payments only)
Note alignment or divergence with EU MiCA, FATF guidance, or major foreign regulator actions when material to U.S.-based multinationals.

## Agency Coverage Checklist

- [ ] CFPB — consumer protection, BNPL, open banking (1033 rulemaking)
- [ ] SEC — digital asset securities, investment adviser rules, broker-dealer
- [ ] CFTC — crypto derivatives, commodity token classification
- [ ] FinCEN/Treasury — AML/BSA, beneficial ownership, travel rule
- [ ] OCC — bank charter, crypto custody, fintech partnerships
- [ ] Federal Reserve — payments, FedNow, Reg E/Z amendments
- [ ] State regulators — MTL, lending, state-chartered bank rules

## Guidelines

- Cite only primary sources (Federal Register, agency press releases, official guidance); use `[VERIFY]` on any citation not confirmed against the source
- Distinguish **final rules**, **proposed rules**, **guidance/no-action letters**, and **enforcement actions** — compliance obligations differ materially
- Do not conflate "guidance" with binding regulation; flag where agency position lacks formal rulemaking
- For proposed rules, include comment period deadlines and note whether industry has raised significant objections
- Urgency tiers: **Immediate** = effective or past due; **Near-Term** = effective within 90 days; **Monitor** = proposed or 90+ days out
- Acknowledge interpretive ambiguity rather than asserting false certainty on unsettled regulatory questions
