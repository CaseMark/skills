---
name: due-diligence-summary
description: Produces structured U.S. transactional due diligence summaries for M&A, investments, and partnerships, covering corporate structure, financials, contracts, IP, litigation, regulatory, employment, real estate, tax, and environmental matters with risk ratings, document citations, and follow-up actions. Use when drafting a due diligence summary, diligence report, red-flag memo, or data room analysis for a transaction or acquisition review.
tags:
  - analysis
  - corporate
  - summarization
  - summary
  - transactional
---

# Due Diligence Summary

Deliver a decision-ready diligence summary with risk ratings, evidence citations, and next-step actions.

## Prerequisites

1. Transaction snapshot (type, buyer/seller/investor, structure, timeline, target entity list)
2. Scope definition (categories in-scope/out-of-scope, materiality threshold, industries, jurisdictions)
3. Data room index or document list with stable identifiers and dates
4. Corporate governance docs and ownership materials (organizational chart, cap table, equity awards)
5. Financial statements, debt schedules, and contingent liabilities
6. Material contracts list and contract repository
7. IP schedules and IP-related agreements
8. Litigation, claims, and regulatory correspondence (including investigations)
9. HR/benefits, real estate/asset schedules, tax and environmental records as applicable
10. Privilege/confidentiality designation and allowed audience

## Output Structure / Process

1. Map scope to document inventory; mark coverage status per category.
2. Extract facts, obligations, restrictions, and change-of-control/consent triggers.
3. Classify each finding as Fact, Representation, or Open Issue.
4. Assign Risk and Materiality; quantify exposure when possible.
5. Note conflicts across sources with authority/date rationale.
6. Produce the summary using the template below and cite every material finding.

Risk scale:

| Rating | Meaning | Action |
| --- | --- | --- |
| High | Likely deal impact or material exposure | Escalate and require resolution/mitigation |
| Medium | Manageable but needs diligence or contractual protection | Track and address in docs/price |
| Low | Informational or minor exposure | Note; monitor if cumulative |

Coverage checklist (fill Status as Complete, Partial, Missing):

| Category | Expected Core Docs | Status | Notes |
| --- | --- | --- | --- |
| Corporate/Governance | Charter, bylaws, consents, cap table, subsidiary org |  |  |
| Financials/Debt | Audited/unaudited FS, debt docs, guarantees, liens |  |  |
| Contracts | Top customer/vendor, assignment/consent, exclusivity |  |  |
| IP/Tech | IP schedule, licenses, OSS use, assignments |  |  |
| Litigation/Reg | Docket list, claims history, agency letters |  |  |
| HR/Benefits | Payroll, key employee agreements, benefits plans |  |  |
| Real Estate/Assets | Leases, deeds, asset schedules |  |  |
| Tax | Returns, audits, NOLs, nexus |  |  |
| Environmental | Phase I/II, permits, compliance |  |  |

Citation format: `[Doc ID or Title, date, page/section]`

Deliverable template:

```markdown
# Executive Summary
- Deal snapshot (type, parties, target, valuation if known)
- Top 5 red flags with risk rating and cited evidence
- Missing critical items

# Scope & Coverage
- In-scope categories and jurisdictions
- Coverage checklist with gaps and rationale

# Key Findings by Category
## Corporate/Governance
| Issue | Evidence | Risk | Materiality | Follow-up |
| --- | --- | --- | --- | --- |

## Financials/Debt
| Issue | Evidence | Risk | Materiality | Follow-up |
| --- | --- | --- | --- | --- |

## Contracts
| Issue | Evidence | Risk | Materiality | Follow-up |
| --- | --- | --- | --- | --- |

## IP/Tech
| Issue | Evidence | Risk | Materiality | Follow-up |
| --- | --- | --- | --- | --- |

## Litigation/Regulatory
| Issue | Evidence | Risk | Materiality | Follow-up |
| --- | --- | --- | --- | --- |

## HR/Benefits
| Issue | Evidence | Risk | Materiality | Follow-up |
| --- | --- | --- | --- | --- |

## Real Estate/Assets
| Issue | Evidence | Risk | Materiality | Follow-up |
| --- | --- | --- | --- | --- |

## Tax
| Issue | Evidence | Risk | Materiality | Follow-up |
| --- | --- | --- | --- | --- |

## Environmental
| Issue | Evidence | Risk | Materiality | Follow-up |
| --- | --- | --- | --- | --- |

# Conflicts & Discrepancies
| Topic | Conflicting Sources | Assessment | Action |
| --- | --- | --- | --- |

# Open Items / Follow-Up Requests
| Item | Rationale | Requested From | Priority |
| --- | --- | --- | --- |

# Recommended Actions
- Contractual protections (rep, warranty, indemnity, covenants)
- Price or structure adjustments
- Pre-closing conditions or consents
```

## Guidelines

- Separate confirmed facts from representations and open issues.
- Flag missing expected documents as findings with risk and impact.
- Use exact dates, parties, dollar amounts, and governing law when available.
- Treat unsigned drafts as non-authoritative; label clearly.
- If regulated industry is involved, add a compliance subsection (e.g., HIPAA, FDA, FINRA/SEC, OFAC, FCPA, state licensing) and mark statutes [VERIFY] if uncertain.
- Do not advocate for or against the deal; stay neutral and evidence-driven.
- Preserve privilege and confidentiality; limit distribution as instructed.
