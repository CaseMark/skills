---
name: screening-deal-flow-pipeline
language: en
description: Filters inbound deal flow against fund thesis, stage, sector, and return requirements with structured pass/advance decisions. Use when triaging deal flow, evaluating inbound pitches, or managing sourcing pipelines.
tags:
  - screening
  - venture-capital
metadata:
  author: casemark
  practice_areas:
    - Venture Capital
    - Seed/Series Investing
    - Startup Ecosystems
  document_types:
    - Screening Report
  skill_modes:
    - Screening
    - Filtering
---
# Screening Deal Flow Pipeline

Filters inbound deal flow against fund thesis, stage, sector, and return requirements with structured pass/advance decisions.

## When To Use

- Triaging a batch of inbound pitch decks, intros, or cold outreach against fund mandate
- Running weekly/monthly pipeline reviews to move deals from sourcing to first meeting
- Evaluating whether a specific opportunity clears hard filters before spending partner time
- Building a ranked shortlist from an accelerator demo day, conference, or sourcing sprint
- Auditing pipeline consistency to ensure screening criteria are applied uniformly across the team

## Inputs To Gather

- **Fund thesis parameters**: target sectors, stage (pre-seed / seed / Series A / growth), geography, check size range, ownership targets
- **Return requirements**: target fund multiple (e.g., 3x net), implied deal-level return bar (e.g., 10x+ potential for seed), follow-on reserve assumptions
- **Deal batch**: list of companies with available data — deck, memo, CRM record, or intro email
- **Per-deal data points** (as available):
  - Company name, one-line description, sector/vertical
  - Stage and current raise (amount, valuation/cap, instrument)
  - Revenue or traction metrics (ARR, MRR, GMV, users, growth rate)
  - Founder background (domain expertise, prior exits, technical depth)
  - Existing investors and cap table highlights
  - Competitive landscape notes
- **Pass/advance history** (optional): prior screening decisions for pattern calibration

## Workflow

1. **Establish hard filters** — Set binary pass/fail gates derived from fund mandate:
   - Stage match (e.g., only pre-seed and seed)
   - Sector match (e.g., B2B SaaS, fintech, climate — per thesis)
   - Geography match [VERIFY fund LP restrictions or regulatory limits on geography]
   - Check size fit (requested raise allows fund to deploy within check range)
   - Instrument compatibility (SAFE, priced equity, convertible note — per fund policy)
   - Flag any deal that fails a hard filter as **PASS (out of scope)** with the specific reason

2. **Apply soft scoring criteria** — For deals surviving hard filters, evaluate on a 1–5 scale across:
   - **Market**: TAM credibility, timing, tailwinds, regulatory clarity [VERIFY sector-specific regulatory status]
   - **Team**: founder-market fit, relevant experience, technical capability, coachability signals
   - **Traction**: revenue trajectory, engagement metrics, or credible pre-revenue milestones relative to stage
   - **Product**: differentiation, defensibility (IP, network effects, data moats), demo or prototype quality
   - **Deal terms**: valuation reasonableness for stage, pro-rata rights, investor-friendly governance
   - **Return potential**: plausible path to fund-returning outcome at entry valuation

3. **Classify each deal** — Assign a disposition:
   - **Advance to partner review**: scores ≥ 4 average or exceptional strength in 2+ dimensions with no dimension below 3
   - **Hold / request more info**: borderline scores (3–3.5 average) or missing critical data points — specify what is needed
   - **Pass**: scores < 3 average or fatal flaw in any single dimension (e.g., tiny market, no differentiation)
   - **Flag for co-invest / refer out**: strong company but outside fund scope — note which fund in network might fit

4. **Rank the advance list** — Order advanced deals by composite score, breaking ties by:
   - Urgency (round closing timeline, competitive dynamics)
   - Strategic fit to portfolio gaps
   - Likelihood of winning allocation

5. **Document rationale** — For every deal, record:
   - Disposition and one-sentence rationale
   - Key data points that drove the decision
   - Any [VERIFY] flags for data that was estimated or unavailable
   - Recommended next action and owner (for advances and holds)

## Output

Produce a **Screening Report** containing:

- **Summary statistics**: total deals reviewed, breakdown by disposition (advance / hold / pass / refer), sector distribution
- **Advance list** (ranked): company name, one-liner, stage, raise details, composite score, top strengths, key risks, recommended next step
- **Hold list**: company name, missing info or open question, deadline to resolve
- **Pass log**: company name, one-sentence pass reason (maintains institutional memory and avoids re-screening)
- **Refer-out list**: company name, suggested fund/contact, brief rationale
- **Screening criteria applied**: explicit statement of hard filters and soft scoring rubric used for this batch (supports auditability)

## Quality Checks

- Every deal in the batch has a recorded disposition — no deal is left unclassified
- Hard filter pass reasons cite the specific criterion failed, not a vague "not a fit"
- Soft scores are grounded in stated evidence, not gut feel — each score references a data point
- Valuations and metrics are stage-benchmarked (e.g., a $30M cap at pre-seed is flagged differently than at Series A) [VERIFY current market benchmarks for target stage/sector]
- No deal is advanced solely on founder pedigree without evaluating market and product dimensions
- Round timing and competitive urgency are noted so the advance list can be actioned in priority order
- [VERIFY] flags appear wherever a data point was inferred, estimated, or sourced from a single unverified channel
- Report is structured for quick partner consumption — a GP should be able to review the advance list in under 5 minutes
