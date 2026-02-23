---
name: closing-disclosure-timing-reference
description: Reference guide for TRID Closing Disclosure timing compliance under 12 CFR § 1026.19(f). Covers the three-business-day receipt rule, dual business-day definitions, federal holiday list, delivery method deemed-receipt rules, re-disclosure triggers requiring new waiting periods, waiver procedures for bona fide emergencies, seller CD timing, and post-consummation correction deadlines. Use when calculating CD delivery deadlines, determining earliest permitted closing dates, evaluating re-disclosure triggers, or advising on emergency waiver procedures.
tags:
  - analysis
  - policy
  - regulatory
  - transactional
---

# Closing Disclosure Timing Reference (TRID)

TRID timing compliance reference for CD delivery deadlines, re-disclosure triggers, and waiver procedures under 12 CFR § 1026.19(f).

## Prerequisites

1. Scheduled closing (consummation) date
2. Intended delivery method (hand, mail, electronic)
3. Identification of any post-CD changes to APR, loan product, or prepayment penalty

## Core Rules

### Three-Business-Day Receipt Rule — 12 CFR § 1026.19(f)(1)(ii)

- Borrower must **receive** CD ≥ 3 business days before consummation (not sending date — receipt)
- "Consummation" = date borrower becomes contractually obligated (typically signing)
- All borrowers on the loan must receive the CD
- Creditor bears compliance responsibility

### Business Day Definitions

TRID uses **two definitions**:

| Definition | Used For | Excludes |
|---|---|---|
| **General** (Def. 1) | CD 3-day waiting period | Sundays + federal public holidays |
| **Specific** (Def. 2) | 7-day LE waiting period | Days creditor's offices are closed |

> The CD 3-day rule uses **Definition 1 (General)**.

**Federal Legal Public Holidays:**

| Holiday | Date |
|---|---|
| New Year's Day | Jan 1 |
| MLK Jr. Day | 3rd Mon in January |
| Presidents Day | 3rd Mon in February |
| Memorial Day | Last Mon in May |
| Independence Day | Jul 4 |
| Labor Day | 1st Mon in September |
| Columbus Day | 2nd Mon in October |
| Veterans Day | Nov 11 |
| Thanksgiving | 4th Thu in November |
| Christmas Day | Dec 25 |

*Saturday holiday → observed Friday; Sunday holiday → observed Monday.*

## Delivery & Deemed Receipt

| Method | Deemed Receipt | Notes |
|---|---|---|
| Hand delivery | Same day | Best for tight timelines |
| Mail (USPS or overnight) | +3 business days after mailing | Effective 6 business days before closing |
| Electronic | +3 business days after sending | Unless earlier actual receipt is documented |
| Actual receipt | Date received | Creditor may prove earlier receipt with evidence |

**E-SIGN requirements for electronic delivery:** obtain consent, disclose hardware/software requirements, retain delivery evidence.

## Calculating Deadlines

**Count back from closing date (exclude closing day itself):**

```
Closing: Wednesday Mar 19
  Day 1 ← Tuesday Mar 18
  Day 2 ← Monday Mar 17
  Day 3 ← Friday Mar 14  (skip Sunday)
Latest receipt: Friday Mar 14
If mailing: mail by Tuesday Mar 11 (add 3 more business days back)
```

**With holiday:**
```
Closing: Tuesday Jan 21  (MLK Day = Mon Jan 20 — excluded)
  Day 1 ← Friday Jan 17
  Day 2 ← Thursday Jan 16
  Day 3 ← Wednesday Jan 15
Latest receipt: Wednesday Jan 15
```

**Key deadline summary:**

| Scenario | Days Before Closing |
|---|---|
| Hand deliver CD | 3 business days |
| Mail or e-deliver CD | 6 business days |
| LE delivery before consummation | 7 business days (Def. 2) |

## Re-Disclosure Triggers (New 3-Day Waiting Period)

Only **three changes** require a corrected CD with a new 3-day wait — 12 CFR § 1026.19(f)(2)(ii):

| Trigger | Detail |
|---|---|
| **APR becomes inaccurate** | Fixed/regular: >0.125% increase; ARM/irregular: >0.25% increase. APR decrease (overstatement cure) does NOT trigger. |
| **Loan product changes** | Fixed↔ARM, index change (e.g., SOFR→Treasury), initial fixed period change (e.g., 5/1→7/1) |
| **Prepayment penalty added** | Previously undisclosed penalty added. Removal/reduction does NOT trigger. |

### Changes That Do NOT Require New Waiting Period

Corrected CD may be provided at or before consummation without restarting the clock:
- Settlement charge increases (including tolerance violations)
- Seller credit changes
- Loan amount changes (unless product type changes)
- Interest rate decreases
- Escrow changes, cash-to-close changes, clerical corrections

| Correction Type | Timing |
|---|---|
| APR, product, or prepayment penalty change | New 3-day waiting period |
| All other changes | At or before consummation |
| Post-consummation corrections | Within 30 calendar days |
| Tolerance cure refunds | Within 60 calendar days |

## Waiver of Waiting Period — 12 CFR § 1026.19(f)(1)(iv)

**Requirements (all must be met):**
1. Bona fide personal financial emergency exists
2. Consumer provides a **dated written statement** in their own words describing the emergency and specifically waiving the right
3. **All** consumers primarily liable must sign
4. Statement **must not be on a pre-printed form**

**Valid emergencies:** imminent foreclosure on current home, closing deadline tied to medical crisis, impending job relocation, natural disaster affecting residence, COVID-19-related emergencies (per CFPB guidance).

**Invalid "emergencies":** vacation plans, moving convenience, avoiding rate lock extension fees, seller pressure to close quickly.

## Seller CD Timing

| Party | Timing Requirement | Responsible Party |
|---|---|---|
| Borrower | ≥3 business days before consummation | Creditor |
| Seller | No later than day of consummation | Settlement agent |

Seller may receive full 5-page CD or modified CD showing only seller's transaction summary (page 3).

## Post-Consummation

| Deadline | Requirement |
|---|---|
| 30 calendar days | Deliver corrected CD for discovered errors |
| 60 calendar days | Cure tolerance violations with refund to borrower |
| 5 years | Retain all CDs (original and corrected) |

## Common Errors

| Error | Correct Approach |
|---|---|
| Counting closing day as business day | Start count day before closing |
| Forgetting to skip Sundays | Sundays always excluded |
| Missing observed holiday dates | Check Saturday/Sunday shift rules |
| Treating electronic delivery as instant | Still carries 3-day deemed receipt |
| Using pre-printed waiver form | Consumer must write in own words |
| Accepting convenience as emergency | Only bona fide emergencies qualify |

## Regulatory Citations

- 12 CFR § 1026.19(f)(1)(ii) — Three-business-day receipt rule
- 12 CFR § 1026.19(f)(1)(iii) — Deemed receipt rules
- 12 CFR § 1026.19(f)(1)(iv) — Waiver of waiting period
- 12 CFR § 1026.19(f)(2)(ii) — Re-disclosure triggers
- 12 CFR § 1026.2(a)(6) — Business day definitions
- CFPB Official Interpretation, Comments 19(f)(1)(ii)-1 through -4
- CFPB Official Interpretation, Comments 19(f)(1)(iv)-1 through -3
- CFPB Interpretive Rule on COVID-19 Flexibilities (April 2020)
