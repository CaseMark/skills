---
name: real-estate-transaction-summary
description: Generates structured summaries of real estate transactions from purchase agreements, addenda, disclosures, and closing documents. Extracts property details, financial terms, parties, key dates, contingencies, obligations, title matters, and risk allocation into a scannable format. Use when summarizing a real estate deal, creating transaction overviews, onboarding to a new matter, or preparing closing checklists for buyers, sellers, attorneys, or brokers.
tags:
  - summarization
  - summary
  - transactional
---

# Real Estate Transaction Summary

Distills real estate transaction documents into a structured, scannable overview covering all material terms and obligations.

## Prerequisites

1. **Purchase and sale agreement** — fully executed, with all amendments
2. **Addenda and side agreements** — inspection, financing, rent-back, 1031 exchange, etc.
3. **Title commitment and survey** (if available)
4. **Disclosure documents** — seller disclosures, lead paint, HOA docs
5. **Financing documents** (if applicable)

## Output Structure

Begin with an **Executive Summary** block, then produce each section below. Use exact dates, dollar amounts, and legal descriptions throughout.

### Executive Summary

| Field | Detail |
|-------|--------|
| Property | Legal description, address, parcel ID |
| Parties | Buyer / Seller (legal names, entity types) |
| Purchase Price | $amount |
| Closing Date | MM/DD/YYYY |
| Key Contingencies | List critical ones |
| High-Risk Items | Flag unusual or time-sensitive provisions |

### Section Outline

Produce the following sections in order:

1. **Property Information**
   - Legal description, address, parcel ID, type/use, size
   - Zoning, easements, encumbrances, restrictions
   - Included fixtures and personal property

2. **Financial Terms**
   - Price breakdown: earnest money, down payment, loan amount/type, seller financing
   - Price allocations (land/improvements/personalty) for tax purposes
   - Credits, adjustments, prorations

3. **Parties and Roles**
   - Buyer, seller, counsel, brokers (with commission structure), title/escrow agent, lender
   - Guarantors, assignees, special relationships

4. **Key Dates and Deadlines** — present as a chronological table:

   | Date | Deadline | Consequence of Missing |
   |------|----------|----------------------|
   | MM/DD/YYYY | Description | Remedy/default |

   Flag all time-is-of-the-essence provisions.

5. **Contingencies and Conditions Precedent** — for each:
   - Condition description
   - Responsible party
   - Deadline
   - Remedy if unsatisfied

   Cover: financing, inspection, appraisal, title, sale of buyer's property, zoning approvals, tenant estoppels.

6. **Buyer Obligations**
   - Earnest money deposit, financing commitment, inspections, title/survey review
   - Insurance, final walk-through, closing funds
   - Post-closing: lease assumptions, rent-back duties

7. **Seller Obligations**
   - Property maintenance until closing, disclosures, title cure
   - Repairs, contract termination/assignment, possession delivery
   - Representations and warranties surviving closing

8. **Closing Conditions and Procedures**
   - Method (in-person/escrow/remote), location
   - Cost allocation by line item
   - Prorations: taxes, HOA, rents, utilities
   - Required deliverables per party, recording requirements

9. **Title and Survey Matters**
   - Exceptions to coverage, curative requirements
   - Easements, encroachments, boundary issues
   - Policy types and amounts (owner/lender)

10. **Risk Allocation and Remedies**
    - Risk of loss before closing
    - Default remedies: specific performance, liquidated damages
    - Earnest money disposition by scenario
    - Dispute resolution (mediation/arbitration), attorney's fees, liability caps

11. **Special Provisions**
    - Rent-back / early occupancy terms
    - Assignment rights, 1031 exchange accommodations
    - Environmental indemnities, non-competes, confidentiality

12. **Legal and Regulatory Compliance**
    - Required disclosures (federal/state/local)
    - Lead-based paint (pre-1978 properties)
    - HOA approval requirements, transfer taxes
    - FIRPTA withholding (foreign sellers)
    - Fair housing considerations

13. **Matters Requiring Attention**
    - Missing material terms
    - Document conflicts or ambiguities
    - Identified risks needing resolution before closing

## Guidelines

- Use specific dates (MM/DD/YYYY), not relative timeframes ("30 days after execution")
- Use exact dollar amounts, not approximations
- Flag ambiguities explicitly — note where source documents conflict or are silent
- Write for both attorneys and lay parties — precise but minimal jargon
- The summary must be self-contained: reader should not need to consult underlying documents for material terms
- Keep the Matters Requiring Attention section even if empty (state "None identified")
- Do not editorialize on deal quality — report terms neutrally
