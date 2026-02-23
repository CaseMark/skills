---
name: patent-infringement-summary
description: Generates structured summaries of patent infringement cases covering parties, patents-at-issue, infringement theories, procedural history, claim construction, damages, and outcomes. Produces standalone reference documents for IP enforcement tracking by legal teams and corporate IP departments. Use when summarizing patent disputes, creating case digests for IP portfolios, or onboarding to patent litigation matters.
tags:
  - litigation
  - research
  - summarization
  - summary
---

# Patent Infringement Case Summary

Produces a structured, standalone summary of a patent infringement case for IP enforcement tracking and litigation reference.

## Prerequisites

1. **Case filings** — complaint, answer, counterclaims, key motions
2. **Patent documents** — patents-at-issue with claims, prosecution history if available
3. **Court orders** — claim construction (Markman) rulings, dispositive motions, final judgment
4. **Outcome documents** — verdict, settlement terms (if public), damages reports, injunction orders

## Output Structure

### 1. Case Caption

| Field | Content |
|-------|---------|
| **Case Name** | Full party names (Plaintiff v. Defendant) |
| **Court** | Court, district, division |
| **Case No.** | Docket number |
| **Filed** | Filing date |
| **Judge** | Assigned judge |

### 2. Executive Overview

Two to three sentences capturing: the core technology dispute, principal relief sought, and current status or outcome.

### 3. Patents-at-Issue

For each patent, provide:

| Field | Content |
|-------|---------|
| **Patent No.** | U.S. Patent No. X,XXX,XXX |
| **Title** | Patent title |
| **Filed / Issued** | Dates |
| **Owner** | Patent holder / assignee |
| **Technology** | Plain-language description of the claimed invention |
| **Key Claims** | Claim numbers central to the dispute with brief element descriptions |
| **Commercial Significance** | Products, standards, or market relevance |

### 4. Alleged Infringement

- **Accused instrumentalities** — products, services, or processes
- **Infringement type** — direct, indirect (induced/contributory), willful, literal, DOE
- **Claim mapping** — how accused instrumentalities allegedly meet asserted claim elements
- **Multiple defendants** — note any joint/several theories or customer-suit issues

### 5. Procedural History

Chronological table of key events:

| Date | Event | Significance |
|------|-------|--------------|
| | Complaint filed | |
| | Answer / counterclaims | |
| | Markman hearing | |
| | Key discovery rulings | |
| | Summary judgment | |
| | Trial | |
| | Post-trial motions | |
| | Appeal | |

Flag critical rulings that shaped case trajectory.

### 6. Legal Arguments

**Plaintiff's theories:**
- Infringement theories and claim construction positions
- Damages model (lost profits / reasonable royalty / both)
- Injunctive relief basis

**Defendant's defenses:**
- Invalidity (anticipation, obviousness, § 101, indefiniteness)
- Non-infringement / claim construction positions
- Inequitable conduct, laches, exhaustion, licensing defenses
- Counterclaims (DJ of invalidity/non-infringement, antitrust, FRAND)

### 7. Claim Construction

| Claim Term | Plaintiff's Construction | Defendant's Construction | Court's Construction |
|------------|--------------------------|--------------------------|----------------------|
| | | | |

Note governing methodology (Phillips v. AWH Corp.) and any Federal Circuit guidance applied.

### 8. Outcome

| Field | Content |
|-------|---------|
| **Disposition** | Verdict / settlement / dismissal / SJ |
| **Infringement finding** | Per claim, per accused product |
| **Validity finding** | Per claim, per defense |
| **Damages** | Amount, methodology, royalty rate or lost-profits basis |
| **Enhanced damages** | Willfulness finding, multiplier |
| **Injunction** | Granted/denied, scope, eBay factor analysis |
| **Attorney's fees** | § 285 exceptional case finding |
| **Appeal status** | Pending / affirmed / reversed / remanded |

For ongoing cases: state current procedural posture and next scheduled events.

### 9. Strategic Implications

- Precedential value (claim construction, damages methodology, validity)
- Impact on licensing/enforcement in the technology sector
- SEP/FRAND considerations if applicable
- Portfolio-level takeaways for IP strategy

## Guidelines

- Cite all sources: court documents by docket number and date, patents by number
- Use `[VERIFY]` for any citation not confirmed against source documents
- Keep technical descriptions accessible to non-technical readers while preserving precision
- If settlement terms are confidential, note "Terms confidential" — do not speculate
- Treat each patent separately when multiple patents are asserted
- Note any inter partes review (IPR) or other PTAB proceedings running parallel
- For FRAND-encumbered patents, flag commitment terms and any licensing history
- Jurisdiction is presumed U.S. federal (district courts / Federal Circuit) unless stated otherwise
