---
name: biotech-patent-summaries
description: >-
  Summarizes biotechnology patent families and related disputes into
  litigation-ready intelligence for litigation planning, transactions, and
  business strategy. Captures bibliographic facts, claim scope,
  validity/infringement posture, procedural status, and commercial
  consequences for FTO decisions, licensing, pre-filing, discovery, pre-trial,
  and settlement workflows. Use when handling patent applications, issued
  patents, PTAB filings, litigation documents, licensing materials, or
  prosecution histories in biotech domains. Trigger keywords: patent family,
  independent claim, genus claim, enablement, written description, IPR,
  reexamination, §101, infringement contentions, claim construction, validity,
  FTO, licensing.
tags:
  - analysis
  - litigation
  - summarization
  - summary
  - transactional
---

# Biotechnology Patent Summaries

Produces a concise, source-grounded intelligence brief on biotech patents and disputes for executive, litigation, and portfolio decisions.

## Prerequisites

1. Patent corpus: applications, patents, continuations, divisionals, PTAB/FTO or reexamination records.
2. Dispute materials: complaint/counterclaims, answer, motions, claim charts, briefs, hearing notices, docket entries, settlement communications.
3. Parties and products map: owners, assignees, licensees, defendants, accused products/methods, development stage.
4. Jurisdiction scope: at minimum U.S., plus foreign offices where filings/disputes are active (EP, JPO, CNIPA, etc.).
5. Time-stamp and source authority list for fact verification (patent numbers, filing IDs, publication dates, docket event dates).
6. Clear objective: litigation exposure, licensing negotiation, design-around, or freedom-to-operate review.
7. Reviewer style preference: technical audience, executive summary only, or mixed audience.

## Output Structure / Process

1. Ingest and normalize
2. Extract and map claims
3. Analyze validity/infringement risks
4. Translate to procedural/business impact
5. Deliver standardized summary with uncertainty tags

## Input Capture Table

| Bucket | Required fields | Notes |
|---|---|---|
| Patent identity | Patent/application no., title, family ID, filing/priority/publication/grant dates, inventors, assignee, representative | Normalize dates to ISO format |
| Technical scope | Field/domain, mechanism, target indication/platform, key molecules/materials/processes | Define terms on first use |
| Claim set | Independent and dependent claims, claim type, explicit limitations, fallback embodiments | Quote critical claim language verbatim |
| Status | Pending/granted/abandoned, opposition/reexamination/IPR posture, next filing/event deadlines | Include deadline drivers |
| Dispute metadata | Court/tribunal, case type, forum, parties, products at issue, allegations | Federal, PTAB, ITC, foreign proceedings |
| Procedural calendar | Key hearings, motions, disclosures, discovery, expert, claim construction, trial | Include date certainty rating |
| Strategic posture | Commercial significance, exclusivity interactions, competitor landscape, remedies sought | Link to revenue/exclusivity exposure |

## Analysis Checklist

1. Confirm factual integrity before interpretation.
2. Separate factual findings, party arguments, and analytical assessments.
3. Identify claim scope at the independent-claim level before mapping to accused products.
4. Test enforceability and validity vectors early:
   - 101 eligibility concerns for methods/diagnostics/natural products.
   - 102/103 novelty/obviousness posture.
   - 112 enablement/written description vulnerabilities for biotech variability, especially claims to families of biological matter.
5. Quantify litigation risk and execution risk (timeline, motion posture, potential injunction exposure, claim construction volatility).
6. Flag cross-jurisdiction differences for corresponding foreign filings.

## Required Output Template

```text
# [Document / Matter Title]

Date range current through: [DATE]

## 1) Executive Summary (3 short paragraphs)
- Material patent landscape
- Key legal issues
- Bottom-line action recommendation(s)

## 2) Patent/Dispute Snapshot
| Field | Value |
|---|---|
| Identifier | |
| Jurisdiction(s) | |
| Governing parties | |
| Status | |
| Urgency | |

## 3) Claim and Scope Analysis
| Claim # | Text excerpt | Claim breadth | FTO relevance | Risk flags |
|---|---|---|---|---|

## 4) Validity and Prior-Art Assessment
| Ground | Basis | Record support | Counterargument strength | Preliminary probability |
|---|---|---|---|---|

## 5) Infringement Analysis
| Accused product/method | Claim-mapped feature match | Non-infringement/invalidity argument space | Exposure level |
|---|---|---|---|

## 6) Dispute Timeline
| Date | Event | Court/tribunal | Strategic effect |
|---|---|---|---|

## 7) Strategic Recommendations
- [ ] Litigation strategy implications
- [ ] Licensing / settlement options
- [ ] Design-around or alternative pathway
- [ ] Portfolio filing or challenge opportunities
- [ ] Regulatory and exclusivity coordination

## 8) Uncertainty Register
- Confirmed facts
- Documented allegations
- Analytical assumptions
- Open intelligence gaps
```

## Deliverable Rules

| Rule | Requirement |
|---|---|
| Citation discipline | Use party docs, filing records, patent numbers, paragraph/claim/docket references; no uncited assertions |
| Scope discipline | Distinguish facts vs arguments vs analysis |
| Technical clarity | Keep scientific language precise; avoid oversimplification that changes meaning |
| Jurisdiction tags | Label each legal standard by jurisdiction and confidence level |
| Currency | Include explicit "current through" date and stop-line assumptions |

## Guidelines

- No legal advice; provide neutral counsel-grade analysis.
- Treat all claims as jurisdiction-specific; default to US unless clearly labeled otherwise.
- Do not overstate claim scope where specification support is thin.
- Inability-to-prove or missing records must be flagged as “needs confirmation,” not inferred.
- In eligibility/invalidation context, verify current case law and statutory text before finalizing, especially for biotech diagnostic and sequence-related patentability frameworks [VERIFY].
- For US patents, cross-check AIA/first-inventor-to-file effects, PGR/IPR timing, and applicable equitable doctrines [VERIFY].
- For biologics, explicitly evaluate regulatory exclusivities (e.g., orphan, pediatric, biologics data exclusivity) alongside patent rights.
