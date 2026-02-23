---
name: prospectus-draft
description: Drafts SEC-compliant prospectuses for corporate securities offerings, integrating company documents, financial data, risk factors, and offering terms into a structured disclosure document. Conducts research on SEC guidelines and comparable filings to ensure regulatory adherence and full investor disclosure. Use when preparing prospectuses, S-1 registration statements, offering memoranda, or primary disclosure documents for public or private securities issuances.
tags:
  - analysis
  - corporate
  - drafting
  - memo
  - regulatory
  - research
---

# SEC Prospectus Draft

Drafts a comprehensive securities offering prospectus that satisfies SEC disclosure requirements while balancing promotional objectives with investor protection.

## Prerequisites

1. **Corporate documents** — articles of incorporation, bylaws, governance docs, capitalization table
2. **Financial statements** — audited financials, interim results, projections (GAAP-compliant)
3. **Offering terms** — term sheet, underwriting agreement, or preliminary offering parameters
4. **Management bios** — officer/director backgrounds, compensation arrangements, ownership percentages
5. **Risk inventory** — known litigation, regulatory matters, operational vulnerabilities
6. **Business plan** — revenue model, competitive landscape, growth strategy, IP portfolio

## Output Structure

### 1. Cover Page

| Element | Requirement |
|---------|-------------|
| Issuer name | Full legal name |
| Securities offered | Type, amount, price/range |
| Prospectus date | Date of issuance |
| SEC legends | "Neither the SEC nor any state securities commission has approved..." |
| Preliminary notice | If applicable, red herring language per Rule 430 [VERIFY] |
| Risk warning | Statement directing investors to read full prospectus |

### 2. Executive Summary

- Company value proposition and competitive positioning
- Offering type and high-level use of proceeds
- Investment thesis — substantiate every claim with later disclosures
- Avoid promotional language that could be deemed misleading under Section 10(b)

### 3. Risk Factors

Organize in this order:

1. **Offering-specific risks** — dilution, liquidity, pricing
2. **Company-specific risks** — operational, financial, key-person dependency
3. **Industry risks** — regulatory, competitive, cyclical
4. **Market/economic risks** — macro conditions, interest rates, geopolitical

Requirements:
- Each risk must be specific and company-tailored — no generic boilerplate
- Describe potential impact with sufficient particularity
- Cross-reference SEC comment letter trends for the relevant industry
- Check Regulation S-K Item 105 for current disclosure standards [VERIFY]

### 4. Use of Proceeds

```
Category                    Amount ($)    % of Proceeds    Timeline
─────────────────────────────────────────────────────────────────────
Working capital             ___           ___              ___
Capital expenditures        ___           ___              ___
Debt repayment              ___           ___              ___
R&D                         ___           ___              ___
Acquisitions                ___           ___              ___
General corporate purposes  ___           ___              ___
```

- Disclose material assumptions underlying allocations
- State whether management retains reallocation discretion
- If amounts are approximate, specify parameters

### 5. Business Description

Cover each in sufficient detail for an unfamiliar sophisticated investor:

- [ ] Company history, formation, and key milestones
- [ ] Revenue model and unit economics
- [ ] Products/services and target markets
- [ ] Customer base and concentration
- [ ] Distribution channels
- [ ] Competitive landscape and positioning
- [ ] Intellectual property portfolio
- [ ] Regulatory environment and compliance status
- [ ] Supply chain dependencies
- [ ] Seasonal/cyclical factors

Reference: Regulation S-K Items 101-103 [VERIFY]

### 6. Management & Governance

For each executive officer and director:

| Field | Detail |
|-------|--------|
| Name, title, age | Required |
| Professional background | Relevant experience, 5-year history |
| Education | Degrees, relevant certifications |
| Board committee roles | Audit, compensation, nominating |
| Independence status | Per exchange listing standards |

Also disclose:
- Compensation arrangements (summary compensation table if applicable)
- Ownership structure and major shareholders (>5%)
- Related party transactions
- Family relationships among officers/directors

### 7. Financial Information

Required statements (GAAP-compliant):
- Balance sheet
- Income statement
- Cash flow statement
- Statement of stockholders' equity
- Notes to financial statements

Checklist:
- [ ] Audited financials for required periods per Regulation S-X [VERIFY]
- [ ] Unaudited interim results with comparative periods
- [ ] Non-GAAP measures reconciled to GAAP equivalents with justification
- [ ] Forward-looking statements include PSLRA safe harbor language
- [ ] MD&A section covering trends, liquidity, capital resources

### 8. Legal Proceedings & Regulatory Matters

For each material proceeding:

| Element | Description |
|---------|-------------|
| Parties | Named parties and relationship to company |
| Nature | Type of claims/investigation |
| Forum | Court, agency, arbitral body |
| Status | Current procedural posture |
| Exposure | Management's assessment of potential liability |

- Apply Regulation S-K Item 103 materiality threshold [VERIFY]
- Balance transparency with privilege preservation
- Include regulatory compliance overview for industry-specific requirements

### 9. Terms of the Offering

- [ ] Security type (common, preferred, debt, warrants, units)
- [ ] Number of securities and price/pricing mechanism
- [ ] Underwriting arrangements and discounts/commissions
- [ ] Plan of distribution
- [ ] Conditions to closing
- [ ] Dilution analysis (pre/post-offering ownership table)
- [ ] Lock-up agreements — parties, duration, exceptions
- [ ] Registration rights
- [ ] Preferences, rights, and limitations of the securities
- [ ] Transfer restrictions, if any

### 10. Signature Pages & Certifications

- Signatures required from CEO, CFO, principal accounting officer, and majority of directors
- SOX certifications if applicable (Sections 302, 906) [VERIFY]
- Verify signing authority against bylaws and board resolutions

## Guidelines

- **Tone**: Balanced, factual disclosure — never promotional. Every claim must be substantiated elsewhere in the document.
- **Materiality standard**: Disclose anything a reasonable investor would consider important in making an investment decision (TSC Industries v. Northway, 426 U.S. 438 (1976) [VERIFY]).
- **Cross-references**: Use internal cross-references between related sections for navigability.
- **Consistency**: Maintain uniform terminology throughout; define key terms at first use.
- **FLS safe harbor**: All forward-looking statements must include meaningful cautionary language identifying specific risk factors that could cause actual results to differ.
- **Jurisdiction**: Default U.S. federal securities law (Securities Act of 1933, Securities Exchange Act of 1934). Flag state blue sky requirements as needing separate analysis.
- **EDGAR formatting**: Note any EDGAR-specific formatting requirements if filing electronically.
- **Privilege**: Do not include attorney-client privileged analysis in the prospectus text; flag items requiring legal review with `[LEGAL REVIEW]`.
- **Gaps**: If source materials are insufficient for a required section, flag with `[INFORMATION NEEDED: description]` rather than fabricating details.
