---
name: lease-summary
description: Summarizes U.S. commercial lease agreements into a transactional lease abstract for diligence, negotiation, and administration. Use for requests such as commercial lease summary, lease abstract, key lease terms, rent schedule review, default/termination analysis, or lease handoff. Captures party allocations, economics, operational restrictions, risk flags, and critical date obligations.
tags:
  - summarization
  - summary
  - transactional
---

# Commercial Lease Summary

Produces a concise, party-responsible breakdown of a commercial lease for deal execution and ongoing lease management.

## Prerequisites

1. Complete lease document including all attachments, exhibits, exhibits by reference, and definition sections.
2. All amendments, riders, side letters, extensions, renewals, and modification agreements.
3. Statement of governing law and intended jurisdiction (if not in the lease, infer from internal evidence and mark as inference).
4. Business context: landlord vs. tenant roles and whether a lender, guarantor, master tenant, or affiliate is materially involved.
5. Any missing-text assumptions flagged separately for counsel review before final reliance.

## Output Structure / Process

1. Extract party identity, lease identity, jurisdiction, and governing law.
2. Capture baseline business terms before moving to risk-heavy clauses.
3. Normalize definitions relevant to obligations (Premises, CAM, Base Rent, Additional Rent, Term, etc.).
4. Build financial mechanics in formulaic form (not prose-only).
5. Map rights/obligations to party and triggering conditions.
6. Flag ambiguity, missing provisions, and provisions outside typical U.S. commercial leasing patterns.
7. Compile deadline calendar and actionability checklist.

| Output Block | Required Elements | Mandatory Format |
| --- | --- | --- |
| Deal Snapshot | Parties, premises, lease type, governing law, date, form status | 1-3 lines each |
| Term & Premises | Commencement, expiration, renewal/extension, holdover, grace periods | `date / term option / condition / election window` |
| Financial Terms | Base rent, rent start, CAM, taxes, insurance pass-throughs, percentage rent, escalation, deposits | Formula table |
| Use & Operations | Permitted use, prohibited use, assignment/underwriting, signage, hours, access | Party / condition / remedy |
| Maintenance & Repairs | Structural, systems, common areas, HVAC, elevators, roof, windows, tenant improvements | Responsibility matrix |
| Insurance & Liability | Required coverages, limits, additional insureds, waivers, indemnity scope | Policy type / limit / party / trigger |
| Default, Cure & Remedies | Events of default, cure, notices, self-help limits, damages, remedies | Event / notice requirement / cure window / remedy |
| Special Provisions | SNDA/attornment, co-tenancy, kick-out, radius/exclusivity, right of first refusal, options | Provision / risk level / practical impact |
| Missing/Unusual Terms | Missing clauses, drafting conflicts, ambiguity, interpretation risk | `risk / reason / impact / recommended action` |
| Critical Dates | Rent commencements, notice/deadline windows, option windows, renewals, inspections | `date / action / responsible party / status` |

```text
Commercial Lease Summary Output Template

1) Executive Snapshot
- Deal profile: ...
- Risk profile: ...
- Immediate attention items: ...

2) Terms Matrix
| Category | Clause | Text anchor | Party burden | Condition | Trigger | Notes |

3) Financial Obligation Matrix
| Obligation | Base amount / formula | Frequency | Due date rule | Escalation | Cap / floor | Responsible party |

4) Obligation Heat Map
- High-risk:
- Moderate-risk:
- Low-risk:

5) Calendar of Obligations
- ...
6) Counsel Action Items
- ...
```

Checklist before final output:
1. Every obligation includes named responsible party.
2. Every amount has amount or calculation method.
3. Every trigger has date/time condition or event condition.
4. Every special clause has practical consequence for business operation.
5. Missing data explicitly labeled `UNAVAILABLE` instead of inferred, unless clearly stated.

## Guidelines

- Do not summarize in purely narrative form; always return structured output with party-to-obligation mapping.
- Preserve exact contractual terms for numbers, percentages, percentages-of-sales formulas, and escalation indices.
- Use neutral language and avoid legal conclusions unless text supports them.
- If governing law is not explicitly stated, label as `ASSUMED: [jurisdiction from context]` and apply cautious confidence.
- Prioritize operational impact over interpretive advocacy.
- Do not treat template language as custom intent; cite whether a clause is boilerplate by context.
- When clauses are internally conflicting, quote both sections and flag inconsistency as `RECONCILIATION NEEDED`.
- Distinguish between absolute rights and conditional rights (e.g., termination rights that depend on lender notices or approvals).
- Missing provisions requiring counsel review: casualty allocation, environmental indemnity carve-outs, non-disturbance and landlord lien treatment, and unconscionability or assignment exceptions.
- If legal references exist and are uncertain, append `[VERIFY]` to citation or statute references.
