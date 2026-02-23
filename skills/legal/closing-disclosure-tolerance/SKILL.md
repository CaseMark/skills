---
name: closing-disclosure-tolerance
description: Applies U.S. TRID tolerance rules to a residential mortgage Closing Disclosure (CD) against the controlling Loan Estimate (LE), classifies fees by tolerance category, identifies valid changed-circumstance reset triggers, and calculates required tolerances, violations, and cure amounts. Use when keywords include Closing Disclosure tolerance, LE-CD variance, 10% tolerance, revised LE, changed circumstances, or tolerance cure; especially during pre-closing/compliance QA and closing file reviews.
tags:
  - analysis
  - policy
  - regulatory
  - transactional
---

# Closing Disclosure Tolerance Reference

Provides a structured TRID tolerance review workflow for U.S. residential mortgage Loan Estimates and Closing Disclosures, including cure mechanics and changed-circumstance gating.

## Prerequisites

1. Most recent valid Loan Estimate (LE) used as baseline, plus any prior revised LE versions with issue dates.
2. Final Closing Disclosure (CD) with borrower-paid fees by line item and payor category.
3. Charge taxonomy tags for each fee: creditor, broker, affiliate, third party, and whether borrower-selected from lender list.
4. Loan timeline evidence: rate lock date, lock-expiration date, consummation date, LE delivery dates.
5. Documentation for any post-LE events (appraisal updates, title defects, borrower requests, delays, lock changes, etc.).
6. Jurisdictional scope confirmed as U.S. federal TRID (12 CFR Part 1026) and any overlay state overlay rules.

## Output Structure / Process

1. Normalize the baseline
- Use the most recent valid LE as of CD generation.
- Ignore invalid prior LEs unless a valid revised LE was triggered.

2. Classify each CD fee
| Fee Class | Example Items | Tolerance Bucket |
|---|---|---|
| Creditor/Broker Fees | origination, application, processing, underwriting, points, broker administration/origination | Zero tolerance |
| Affiliate Fees | affiliate title/appraisal/other affiliate compensation | Zero tolerance |
| Transfer Taxes | state/local transfer and documentary taxes, mansion taxes | Zero tolerance |
| Cannot-Shop Services | appraisal when lender-required, credit report, flood determination, required provider services | Zero tolerance |
| 10% Cumulative | recording, lender-list shopped title/settlement/inspection/legal settlement items | 10% cumulative |
| Unlimited | prepaid interest, insurance premiums, homeowner-association costs, initial escrow deposits, optional services | Unlimited |

3. Zero-tolerance worksheet
```text
ZERO TOLERANCE WORKSHEET
Item | LE Amount | CD Amount | Variance (CD-LE) | Pass/Fail (<=0)
- Creditor/Broker fees (itemized)
- Affiliate fees (itemized)
- Transfer taxes (itemized)
- Cannot-shop services (itemized)
Zero Tolerance Total Variance = Σ(variances) <= 0
Pass if every required zero-tolerance item has non-positive variance.
```

4. 10% cumulative worksheet
```text
10% CUMULATIVE WORKSHEET
Item | LE Amount | CD Amount
- Recording fees
- Shopped services from lender list (as disclosed)
10% LE Total = Σ(LE)
10% CD Total = Σ(CD)
Limit = 10% LE Total × 1.10
Pass if CD Total <= Limit
Variance ratio = (CD Total - LE Total) / LE Total
```

5. Unlimited-tolerance review
- Verify items are truly unlimited by category and not mis-tagged as zero/10% items.
- Do not auto-pass if disclosures are missing or miscategorized.

6. Changed circumstance gate
| Trigger | Validity Check | Does it allow revised LE? |
|---|---|---|
| Extraordinary event | External events affecting valuation/timing/possessions | Yes, if documented |
| New information unavailable at LE | New material facts later discovered | Yes, if substantiated |
| Borrower-requested change | Product/borrower/property change | Yes, if evidenced |
| Rate lock event | New lock term or lock confirmation | Yes |
| LE expires before consummation window | Delay beyond LE validity period | Yes |
| Inaccurate prior estimate | Good-faith correction only, not correction-only updates | No |

7. Revised LE impact rules
- If changed circumstance is valid, only affected fees may be revised.
- Revised LE must be issued promptly and within required timing windows; include evidence.
- Recompute tolerance against the revised LE for affected categories only.
- Flag potential pretext where “revised LE” appears to repair errors only. [VERIFY]

8. Cure requirement engine
| Requirement | Rule |
|---|---|
| 12 CFR 1026.19(f)(2)(v) credit/refund trigger | Must cure tolerance excess from CD |
| Cure deadline | Within 60 calendar days after consummation |
| Cure document | Corrected CD or itemized cure disclosure in file |
| Cure amount formula | Cure = max(0, zero variance excess) + max(0, CD10 - LE10×1.10) |

```text
CURE CALCULATION
Zero excess = max(0, CD Zero Total - LE Zero Total) [must be reduced to 0 via credit/refund]
10% excess = max(0, CD 10% Total - (LE 10% Total × 1.10))
Total cure required = Zero excess + 10% excess
```

9. Final output format (deliverable)
- Summary conclusion: Pass/Fail by category.
- Variance table with all values and date references.
- Changed-circumstance decision table (each asserted change + evidence + fee impact).
- Cure memo with totals, method (refund/escrow/principal/other), and target cure date.

## Guidelines

| Do | Don’t |
|---|---|
| Compare CD to the controlling LE snapshot in effect at closing. | Aggregate 10% items individually; it is a category total test. |
| Compute zero-tolerance at fee-line level for strict categories. | Shift fees between categories to dodge tolerance failures. |
| Separate lender-list and non-lender-list shopper-selected services correctly. | Treat non-lender-list selected services as 10% if not disclosed on lender list. |
| Document file evidence for every changed circumstance claim. | Revise LE for goodwill corrections of prior mistakes. |
| Track cure deadlines and filing artifacts in the compliance packet. | Treat cure as satisfied without borrower-facing correction/record evidence. |
| Apply federal TRID baseline first, then layer state-specific overlays if any. | Assume all jurisdictions share identical timing or definition nuances. |

## Special Situations

| Situation | Rule |
|---|---|
| Construction loans | Apply CD tolerance logic by phase where required by structure |
| Subordinate financing | Test each loan stream independently; no cross-loan fee shifting |
| Seller credits | Do not net credits for fee-line tolerance math; compare gross charges |
| Lender credits | Item-specific reductions may affect that fee only if specifically tied |

## Common Errors to Flag

| Error | Correction |
|---|---|
| Misclassifying affiliate items as 10% | Recategorize to zero tolerance |
| Missing lender-list evidence for shopped items | Demand file proof before final pass |
| Issuing revised LE after required window | Treat as invalid unless corrected by later valid circumstance |
| Using 4/4.1/4.5% shortcuts | Apply exact TRID formula and categories |
| Forgetting to recalc after valid revised LE | Re-run both zero and 10% tests on revised baseline |

## Cross-References

- @draft-closing-disclosure-cd-residential-real-estate
- @closing-disclosure-timing-reference
- @loan-estimate-residential
- @trid-changed-circumstances

## References

- 12 CFR 1026.19(e)(3) — Good faith determination and tolerance [VERIFY]
- 12 CFR 1026.19(e)(3)(iv) — Changed circumstances [VERIFY]
- 12 CFR 1026.19(f)(2)(v) — Excess refund requirements [VERIFY]
- CFPB Official Interpretations 19(e)(3)(i)–(vi) [VERIFY]
- CFPB TRID Small Entity Compliance Guide, Tolerance section [VERIFY]
