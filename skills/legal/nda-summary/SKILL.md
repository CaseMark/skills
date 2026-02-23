---
name: nda-summary
description: Generates structured summaries of Non-Disclosure Agreements, extracting parties, confidential information definitions, permitted disclosures, exclusions, standard of care, term/survival provisions, breach remedies, and risk flags into a scannable reference format. Use when summarizing NDAs, reviewing confidentiality agreements, distilling NDA obligations, or onboarding stakeholders to NDA terms in corporate or transactional contexts.
tags:
  - corporate
  - summarization
  - summary
  - transactional
---

# NDA Summary

Distills a Non-Disclosure Agreement into a structured, scannable reference covering all material terms, obligations, and risk areas.

## Prerequisites

1. **Complete NDA document** — fully executed or near-final draft
2. **Any amendments or side letters** modifying the original NDA terms

## Output Structure

### 1. Overview

| Field | Extract |
|-------|---------|
| Parties | Full legal names, roles (Disclosing / Receiving / Mutual) |
| Effective Date | — |
| Purpose / Context | Transaction type, employment, vendor, etc. |
| Agreement Type | Unilateral or Mutual |
| Governing Law | Jurisdiction, venue, choice of law |

### 2. Confidential Information

| Element | Details |
|---------|---------|
| **Definition** | Quoted or paraphrased definition with scope |
| **Categories / Examples** | Listed categories from agreement |
| **Exclusions** | Publicly available, independently developed, prior knowledge, authorized disclosure |
| **Standard of Care** | Same as own confidential info / reasonable care / heightened standard |
| **Marking Requirements** | Whether written marking or oral designation follow-up required |

### 3. Disclosure Parameters

| Topic | Details |
|-------|---------|
| **Permitted Recipients** | Employees, contractors, advisors, affiliates — note any need-to-know or binding requirements |
| **Permitted Uses** | Evaluation, due diligence, specific project scope |
| **Prohibited Uses** | Reverse engineering, competitive use, etc. |
| **Compelled Disclosure** | Legal process / regulatory — note advance notice requirement and right to seek protective order |

### 4. Term and Survival

| Element | Details |
|---------|---------|
| **Term** | Duration of agreement |
| **Survival Period** | How long obligations continue post-termination |
| **Return / Destruction** | Requirements for materials upon termination, certification obligations |

### 5. Breach Consequences and Remedies

| Remedy | Present? | Details |
|--------|----------|---------|
| Injunctive Relief | Y/N | Bond waiver? |
| Liquidated Damages | Y/N | Amount / formula |
| Indemnification | Y/N | Scope, legal fees included? |
| Liability Cap | Y/N | Amount or exclusions (consequential, punitive) |
| Dispute Resolution | Y/N | Arbitration, mediation, forum |

### 6. Additional Material Terms

Extract if present:

- Non-solicitation or non-compete restrictions
- IP ownership or licensing terms for exchanged information
- Representations and warranties re: authority to disclose
- Assignment restrictions
- Third-party beneficiary provisions

### 7. Risk Flags

Identify and flag:

- [ ] **Unusual terms** — provisions deviating from market-standard NDAs
- [ ] **Onerous obligations** — asymmetric burdens, broad definitions, long survival
- [ ] **Ambiguities** — vague definitions, internally inconsistent provisions
- [ ] **Gaps** — missing standard of care, no survival period, no return/destruction clause, no compelled-disclosure carve-out
- [ ] **Enforceability concerns** — overbroad scope, unreasonable duration

## Guidelines

- Cite section numbers or page references for every extracted term
- Use exact contract language in quotes for definitions and key obligations; paraphrase elsewhere for brevity
- Flag silent topics as **[NOT ADDRESSED]** — especially standard of care, survival period, and return/destruction
- Mark any uncertain legal citations with **[VERIFY]**
- Keep tone neutral and precise; accessible to non-lawyers but legally accurate
- Target 1–3 pages depending on NDA complexity
- Do not provide legal advice or enforceability opinions — flag issues for attorney review
