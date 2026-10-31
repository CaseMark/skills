# Testing Methods and Typologies

## Contents

1. Alert and case review tests
2. Threshold tuning and below-the-line testing
3. Monitoring system validation after the April 2026 model risk guidance
4. Lookbacks: scope and population reconciliation
5. Sampling: size, confidence and what a sample can support
6. Reviewer and tester independence
7. SAR narrative drafting and SAR quality-assurance sampling
8. Red flag typologies
9. Red flag severity

Rules on thresholds, clocks, CTRs, structuring, 314(a) and confidentiality are in `references/aml-reporting-rules.md`. Sources are in `references/primary-sources.md`.

## 1. Alert and case review tests

For each alert or case in the sample, record and test:

| Test | Pass condition | Common failure |
|---|---|---|
| Activity reviewed | The whole alerted period and the customer's other accounts and channels were looked at | Only the alerted transaction reviewed |
| KYC basis current | The customer profile relied on was current under the institution's refresh cycle for that risk tier, or refreshed during the review | Closure says "consistent with expected activity" against a profile years old, or against a stated occupation the activity contradicts |
| Linked parties | Joint owners, signers, beneficial owners, related accounts and repeat counterparties checked | Funnel or pass-through activity missed because each account looks small |
| Rationale matches evidence | The closing reason is supported by documents in the file | "Business explained" with no invoice, contract or customer contact |
| Decision maker | The person or committee with SAR authority made the decision; preparer and decision maker separated where the procedure requires | Analyst both prepared and decided; business line overrode |
| Timeliness | Alert review completed within the institution's standard; SAR filed within 30 days of determination | See `references/aml-reporting-rules.md`, sections 2 and 3 |
| Confidentiality | No SAR reference outside permitted channels | RM note or exit letter mentions the SAR |

Decision labels (defined in `references/output-template.md`): Decision supported, Decision not supported, Insufficient record.

## 2. Threshold tuning and below-the-line testing

The FFIEC manual expects management to document and explain filtering criteria and thresholds and how they fit the institution's risks, to periodically review and test them, to control changes (approval by the BSA officer or senior management), and to have the system's programming methodology and effectiveness independently validated. New York DFS-regulated institutions also have express end-to-end, pre- and post-implementation testing duties (3 NYCRR 504.3); apply that rule only to an institution the DFS regulates.

A tuning conclusion needs evidence on both sides of the line:

| Evidence | What it shows | What it cannot show |
|---|---|---|
| Above-the-line productivity (SARs per alert at the new setting) | Alerts that remain are more productive | Anything about activity no longer alerted |
| Back-test of the old setting over a past period | How many past SARs came from the band the new setting drops | Whether unalerted activity in the band was suspicious but never reviewed |
| Below-the-line sample (activity just under the new threshold, reviewed as if alerted) | Rate of reportable activity the new setting would miss | Rates far below the sample's detectable rate (see section 5) |

Tests for a threshold change:

1. State the old and new parameters, the effective date, the approver and the documented reason.
2. Compute alerts and SARs at both settings over the same period, the SARs in the dropped band, and the percent of past SARs lost.
3. Draw a below-the-line sample from the dropped band (and, for a new scenario, just below its threshold), sized under section 5, reviewed by analysts who do not know it is a test where practicable.
4. Check that the population feeding the scenario is complete (all products, channels and customer types the scenario is meant to cover, including CTR-exempt customers).
5. Label the threshold Supported, Not supported or Untested under the template test.

A threshold raised because alert volume or staffing is high is a legitimate aim only when the evidence shows reportable activity is not lost. A change made so that a customer, segment or pattern cannot alert, or to reduce SAR filings as such, is a hard stop.

## 3. Monitoring system validation after the April 2026 model risk guidance

- On April 17, 2026 the Federal Reserve, OCC and FDIC issued Revised Guidance on Model Risk Management (SR 26-2). It supersedes SR 11-7 (2011) and SR 21-8, the 2021 interagency statement on model risk management for BSA/AML systems. The OCC rescinded OCC Bulletins 2011-12 and 2021-19 and the Model Risk Management booklet; the FDIC rescinded FIL-22-2017 and FIL-27-2021.
- The revised guidance is not an enforceable standard; non-compliance with it will not result in supervisory criticism, though unsafe practices and violations still can. It is expected to be most relevant to banking organizations with over $30 billion in total assets. Its "model" excludes simple arithmetic and deterministic rule-based processes with no statistical, economic or financial theory underpinning them, and excludes generative and agentic AI.
- Consequences for testing: a deterministic threshold rule is not a "model" under the 2026 guidance, but the FFIEC manual's expectations for documenting, testing and independently validating monitoring criteria still apply. A statistical or machine-learning scoring layer is a model; its validation goes to managing-model-risk. Never cite SR 11-7, SR 21-8, OCC 2011-12 or OCC 2021-19 as current. OCC Bulletin 2025-26 (Oct. 6, 2025) told community banks that annual validation is not required.

## 4. Lookbacks: scope and population reconciliation

A lookback re-reviews past activity to find reportable activity that was missed. Its scope comes from the document that requires it (consent order, written agreement, MRA response, board direction or engagement letter); no regulation sets a standard scope.

Reconcile before any testing:

| Dimension | Test | Typical gap |
|---|---|---|
| Customers | Population count from the risk-rating history equals the extract count; closed, charged-off and migrated accounts included | Extract built from active accounts on the run date drops accounts closed during the period |
| Period | Every day from the start to the end date covered, across system migrations | Legacy-core months excluded because data was "unavailable" |
| Products and channels | Every product and channel named in the scope document present | Remote deposit capture, ACH, cards, prepaid, crypto or trade activity left out as "low risk" |
| Entities | Affiliates, branches and agents named in scope included | Subsidiary or foreign branch activity omitted |
| Data completeness | Extract totals tie to the core or general ledger for the period | Record counts not tied; filters silently drop transaction codes |

Each excluded segment is a "Scope gap" unless the scope document or the regulator excludes it in writing. A conclusion about the population covers only the population actually tested.

## 5. Sampling: size, confidence and what a sample can support

For an attribute test with zero expected exceptions (binomial), the sample size for confidence C and tolerable exception rate p is n = ln(1 - C) / ln(1 - p), rounded up. With zero exceptions found in n items, the upper bound on the population exception rate at confidence C is 1 - (1 - C)^(1/n). Computed on 2026-10-30:

| Confidence | Tolerable rate | Sample size (zero exceptions) |
|---|---|---|
| 95% | 10% | 29 |
| 95% | 5% | 59 |
| 95% | 3% | 99 |
| 95% | 2% | 149 |
| 90% | 5% | 45 |

| Items tested, zero exceptions | Upper bound at 95% confidence |
|---|---|
| 25 | 11.3% |
| 30 | 9.5% |
| 45 | 6.4% |
| 59 | 4.95% |
| 100 | 3.0% |

- A sample never supports "no exceptions in the population"; it supports "the exception rate is below X percent at Y percent confidence".
- Use the institution's or the order's stated confidence and tolerable rate; if none is stated, record the parameters chosen as a policy election.
- A judgmental or targeted sample is not projected to the population; label its conclusion accordingly. Stratify by risk, product and period when they differ; size each stratum that a conclusion is drawn about.
- If exceptions are found, report the count and recompute the bound (Clopper-Pearson), and expand testing or the lookback as the plan requires. Finite population corrections reduce the size slightly for small populations; state when used.

## 6. Reviewer and tester independence

- QA reviewers do not review their own alerts or those of analysts who report to them, and are not paid on alert closure volume.
- FFIEC manual (independent testing): testing by internal audit, outside auditors, consultants or qualified staff not involved in the function tested; outside parties should not be involved in other BSA functions that create a conflict (training, policy writing); the tester reports to the board or a committee of mostly outside directors. Frequency is not set by regulation.
- A vendor that designed, tuned or operates the scenarios under test is not independent of that work. Where an order requires an independent third party, the conflict is disclosed and assessed against the order's terms.
- Labels: Independent, Independence impaired, Not determinable (template).

## 7. SAR narrative drafting and SAR quality-assurance sampling

- The narrative is factual and chronological: who (subjects and roles), what (instruments, amounts, totals), when (date range), where (branches, accounts, jurisdictions), why it is unusual against the customer's profile, and how the activity was conducted. It states what happened and why it was unusual; it never states that a crime was committed.
- Include totals and counts recomputed from the data, account numbers, and the detection method; list supporting documents kept with the SAR.
- SAR QA sample tests: threshold and SAR definition met; subject data complete; narrative answers the six questions; amounts tie to the data; timely from determination; confidentiality kept; continuing SARs (if elected) cover the 90-day period after the prior filing.

## 8. Red flag typologies

Moved from the former AML-RED-FLAGS.md reference. Screen each applicable category; cite typology names as written.

| Category | Indicators |
|---|---|
| Structuring | Cash deposits just under $10,000 across days; same-day deposits at different branches; splitting across own or related accounts; declining amounts; multiple people depositing to one account; ATM deposits under the threshold; monetary instruments bought just under recordkeeping amounts |
| Rapid movement | Deposit and wire-out within one to two days; pass-through balances; funnel accounts with deposits from many locations; layering across accounts or institutions; repeated deposit and same-day cash withdrawal |
| Cash-intensive activity | Cash inconsistent with the stated business or occupation; large small-to-large denomination exchanges; business cash used for personal spending |
| Geographic | Jurisdictions on FATF lists or subject to OFAC programs (check current lists on the date of review); cross-border wires with no stated international business; nested correspondent activity |
| Shell and layering | Nominee or opaque ownership; no physical operations; activity unrelated to stated purpose; rapid entity formation; round-tripping; circular intercompany transfers |
| Wire transfers | Round-dollar wires unlike invoicing; frequent beneficiary or intermediary changes; unrelated third parties; many low-value wires to one destination; business wires through personal accounts |
| Trade-based | Over- or under-invoicing; phantom or multiple invoicing; goods misdescribed; illogical trade partners; third-party payments for goods |
| Behavioral | Reluctance to give KYC or source-of-funds information; questions about reporting thresholds; frequent contact changes; multiple identifiers; dormant account suddenly active; burst of activity then closure; power-of-attorney misuse |
| Insider | Repeated overrides of alerts for one customer; staff coaching customers on thresholds; undisclosed relationships; exception processing; access outside job function |
| Emerging | Fiat-crypto on- and off-ramps and unhosted wallets; human trafficking payment patterns; benefit or relief fraud diversion; ransomware payments; professional money laundering through gatekeepers; all-cash real estate through LLCs |

## 9. Red flag severity

| Severity | Criteria |
|---|---|
| High | Several typologies together; no explanation fits the profile; sanctions, structuring or insider indicators; material amounts |
| Medium | One typology with corroboration; partial explanation |
| Low | Isolated indicator with a plausible explanation and small amounts |

A cluster of Low indicators can warrant escalation; assess the activity as a whole. Red flag severity informs the review; it is not the finding severity scale in the template.
