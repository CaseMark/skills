---
name: deed-of-trust
description: Drafts dual-purpose Deed of Trust and Security Agreement instruments creating real property and UCC personal property security interests. Handles party identification, jurisdictional trust deed requirements, granting language, collateral descriptions, covenants, default/remedies, and execution formalities. Use when drafting trust deeds, security agreements, commercial real estate financing documents, or combined real/personal property security instruments.
tags:
  - agreement
  - drafting
  - transactional
---

# Deed of Trust and Security Agreement

Drafts a combined Deed of Trust and Security Agreement that creates enforceable security interests in both real property and personal property (UCC Article 9) for commercial real estate financing transactions.

## Prerequisites

1. **Loan documents** — promissory note, loan agreement, any related transaction documents
2. **Party information** — full legal names, addresses, entity status for Grantor (borrower/debtor), Trustee, and Beneficiary (lender/secured party)
3. **Real property description** — legal description from chain of title, street address, APN, title report with encumbrances/exceptions
4. **Personal property inventory** — specific items, serial numbers, equipment lists, account descriptions
5. **Jurisdiction** — state where property is located (determines theory, foreclosure process, execution requirements)

## Process

### Phase 1: Information Extraction

Extract from uploaded documents:

| Data Point | Source |
|---|---|
| Parties (names, addresses, entity type) | Loan agreement, formation docs |
| Loan terms (amount, rate, maturity, payment schedule) | Promissory note |
| Legal description + APN | Title report, prior deed |
| Encumbrances / title exceptions | Title commitment |
| Personal property collateral | Equipment lists, inventory schedules |
| Notice clause addresses | Loan agreement |
| Insurance requirements | Loan agreement |

### Phase 2: Jurisdictional Research

Determine before drafting:

- **Property theory**: title theory, lien theory, or intermediate theory → affects conveyance language
- **Foreclosure type**: non-judicial (trustee's sale) vs. judicial; deficiency judgment availability
- **Statutory requirements**: notice periods, cure periods, publication rules, right of redemption
- **Execution formalities**: notarization, witnesses, spousal/homestead consent or joinder
- **Recording requirements**: format, margin, font size, indexing standards
- **Community property / homestead**: whether spousal joinder required

### Phase 3: Document Structure

Draft in this order:

```
1.  PARTIES
2.  RECITALS
3.  PROPERTY DESCRIPTION (real + personal)
4.  GRANT OF DEED OF TRUST
5.  SECURITY AGREEMENT (UCC Article 9)
6.  REPRESENTATIONS AND WARRANTIES
7.  AFFIRMATIVE COVENANTS
8.  NEGATIVE COVENANTS
9.  EVENTS OF DEFAULT
10. REMEDIES
11. ENVIRONMENTAL INDEMNIFICATION
12. SUBORDINATION / ATTORNMENT (if leased property)
13. MISCELLANEOUS
14. EXECUTION / ACKNOWLEDGMENT
```

### Key Drafting Requirements by Section

**Parties** — Verify entity good standing and authority to grant. Include organizational status (corporation, LLC, etc.).

**Property Description:**
- Real property: full legal description from chain of title + street address + APN
- Fixtures, improvements, appurtenances, easements
- Personal property: must satisfy UCC § 9-108 sufficiency — include specific items, inventory, equipment, accounts, general intangibles, and **proceeds**

**Grant of Deed of Trust:**
- Use jurisdiction-standard granting language
- Absolute in form, defeasible on satisfaction
- Define trustee powers: sale authority, substitution procedure, liability limitations

**Security Agreement (UCC Article 9):**
- Satisfy attachment requirements: authenticated agreement + value + debtor's rights in collateral
- Include Grantor's authorization for UCC-1 financing statement filing
- Address after-acquired property and proceeds

**Representations & Warranties:**

| Category | Key Items |
|---|---|
| Title | Fee simple ownership, no conflicting liens |
| Authority | Power to grant, entity in good standing |
| Property condition | Compliance with laws, environmental status |
| Personal property | Ownership, location, no prior security interests |

**Covenants:**

| Affirmative | Negative |
|---|---|
| Timely payment of obligation | No waste |
| Maintain insurance (Beneficiary as loss payee) | No unauthorized transfers or junior liens |
| Pay taxes and assessments | No material alterations without consent |
| Maintain and repair property | No disposal of personal property collateral |
| Comply with laws | No relocation of collateral without consent |

**Events of Default:**
- Non-payment (specify grace period for monetary defaults)
- Covenant/representation breach (reasonable cure period for non-monetary)
- Cross-default to related agreements
- Bankruptcy / insolvency
- Material adverse change in financial condition or collateral value

**Remedies — dual track:**

| Real Property | Personal Property (UCC Art. 9) |
|---|---|
| Trustee's sale per state statute | Right to take possession |
| Judicial foreclosure (if available) | Public or private disposition |
| Receiver appointment | Retention in satisfaction of debt |
| Notice → publication → sale → proceeds distribution | Commercially reasonable disposition required |
| Research deficiency judgment availability | Notice to debtor and other secured parties |

**Governing Law:**
- Real property provisions → law of situs state
- UCC provisions → check UCC choice-of-law rules (§ 9-301 et seq.)
- Include conflict-of-law analysis if split governance

**Execution:**
- Notarized acknowledgment (use jurisdiction-specific form)
- Check witness requirements
- Corporate/LLC authority recitals + authorized officer signature blocks
- Spousal consent block if community property or homestead jurisdiction

## Guidelines

- **Jurisdiction controls**: Never assume uniform rules — foreclosure procedures, cure periods, redemption rights, and execution formalities vary significantly by state
- **Homestead/community property**: Always verify whether spousal joinder or waiver is required and whether such waiver is enforceable
- **UCC-1 filing**: Flag for attorney whether financing statement filing is needed for perfection; include authorization language in the agreement regardless
- **Environmental**: Include indemnification provisions for commercial property; flag if Phase I/II assessments are in uploaded documents
- **Waiver enforceability**: Verify that any waiver of redemption rights, homestead exemptions, or jury trial is enforceable in the jurisdiction before including
- **Internal consistency**: Cross-check that defined terms, cross-references, and collateral descriptions are consistent between the trust deed and security agreement sections
- **Mark all statutory citations** with `[VERIFY]` unless confirmed from uploaded jurisdiction-specific materials
