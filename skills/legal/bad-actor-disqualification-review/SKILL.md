---
name: bad-actor-disqualification-review
description: Produces a Rule 506(d) bad actor disqualification review for private securities offerings, including a covered persons register, tailored questionnaires mapping to each disqualifying event category, a documented reasonable-care diligence record, and classification analysis of flagged events with remediation or disclosure recommendations. Use when conducting Rule 506(d) diligence, identifying covered persons for a Regulation D offering, drafting bad actor questionnaires, or analyzing potential disqualifying events involving criminal convictions, SEC orders, SRO sanctions, or state regulatory actions.
tags:
  - analysis
  - checklist
  - corporate
  - drafting
  - memo
  - regulatory
---

# Bad Actor Disqualification Review (Rule 506(d))

Executes a defensible Rule 506(d) reasonable-care review — identifying covered persons, administering questionnaires, verifying independently, classifying disqualifying events, and recommending remediation or disclosure pathways.

## Prerequisites

1. **Offering perimeter** — Rule 506(b) vs. 506(c), expected sale date(s), staged closing schedule
2. **Cap table** — full beneficial ownership chains, voting agreements, convertible instruments, super-voting stock; sufficient to calculate voting power, not just equity %
3. **Organizational documents** — charter/bylaws or operating agreement, board consents
4. **Officer/director list** — full legal names, roles, and description of each person's involvement in investor-facing activities
5. **Promoter arrangements** — any person who founded/organized the issuer or receives compensation in connection with founding (Rule 405 definition)
6. **Solicitation arrangements** — placement agent, finder, broker-dealer, and portal agreements including compensation terms; identify the specific individuals soliciting, not just the firm entity
7. **Prior Form D filings** and known enforcement history
8. **Per-person identifiers** — full legal name, aliases, DOB, current/prior addresses, FINRA/SEC registrations (for screening)

If screening identifiers are unavailable for any covered person, propose a risk-based path (remove from covered role, restructure, delay) before proceeding.

## Output Structure

### Phase 1 — Covered Persons Register

Build a version-controlled register mapping each person/entity to their Rule 506(d)(1) category. Update at every material deal change.

| Category | Rule Ref | Persons/Entities | Basis for Inclusion |
|---|---|---|---|
| Issuer + affiliated/predecessor issuers | 506(d)(1)(i) | | |
| Directors and executive officers | 506(d)(1)(ii) | | Rule 405 "executive officer" definition |
| Other officers **participating in the offering** | 506(d)(1)(ii) | | Participation = road shows, investor comms, preparing materials; err toward inclusion |
| General partners / managing members of issuer | 506(d)(1)(iii) | | Read operating agreement; title alone is insufficient in DE LLCs |
| **20%+ voting equity** holders | 506(d)(1)(iv) | | Voting power, not equity %; aggregate holdings under common control |
| Promoters | 506(d)(1)(v) | | Rule 405 definition |
| Compensated solicitors | 506(d)(1)(vi) | | Direct or indirect remuneration for solicitation |
| GPs/directors/EOs/MMs of compensated solicitors | 506(d)(1)(vii) | | Check specific individuals at each broker-dealer, not just the firm |

**Voting power traps**: Aggregate related-entity holdings under common control; account for voting agreements, preferred stock as-converted, and super-vote share classes. A fund at 15% through one entity + 6% through an affiliate under common control = 21% covered person.

### Phase 2 — Questionnaire Drafting

Draft a signed questionnaire for each covered person. Questions must mirror the disqualifying event categories in 17 C.F.R. § 230.506(d)(1). **[VERIFY all lookback periods against current rule text before finalizing — do not rely on cached values.]**

| Category | Lookback | Key Drafting Notes |
|---|---|---|
| Criminal convictions — securities purchase/sale, false SEC filings, securities-business conduct | 10 years | Include guilty pleas and nolo contendere |
| Court injunctions/restraining orders — same subject areas | 5 years [VERIFY] | Final orders only |
| Final orders — state securities/banking/insurance regulators, federal banking regulators, NCUA | 10 years | Bars from association, or based on fraud/manipulation/deception; confirm "finality" by reviewing the actual document — do not rely on state terminology |
| SEC disciplinary orders — broker, dealer, MSRB dealer, IA, funding portal | [VERIFY] | Suspension, revocation, or limitation of activities |
| SEC cease-and-desist orders — scienter-based anti-fraud (§17(a)(1), §10(b)/10b-5, §15(c)(1)) or §5 | 5 years [VERIFY] | §17(a) trigger requires scienter; all §5 orders qualify |
| SRO suspension/expulsion — FINRA, etc. | 10 years [VERIFY] | Confirm respondent was "associated with a member" at time of sanction |
| U.S. Postal Service false representation orders | 5 years [VERIFY] | |

**Questionnaire requirements**:
- Define key terms in plain English tied to rule text to prevent under-disclosure
- Require supporting documents (orders, judgments, AWC papers) for every "yes" response
- Signature block: (i) certification of completeness, (ii) agreement to update through final sale, (iii) reliance acknowledgment
- Require refresh if closing is delayed or staged

### Phase 3 — Independent Verification

Search all covered persons independently. Document date, scope, and results for every search.

| Database | Scope |
|---|---|
| SEC EDGAR (litigation releases, admin proceedings) | All covered persons |
| FINRA BrokerCheck | Registered broker-dealer personnel |
| SEC IAPD | Investment advisers |
| PACER | Federal criminal and civil matters |
| State securities regulator databases (NASAA member sites) | State-licensed persons |
| GSA SAM (debarment) | All covered persons |

Calibrate depth to risk: deeper investigation for promoters, compensated solicitors, persons with regulatory friction, penny-stock backgrounds, or complex ownership chains. Refresh all searches shortly before sale if offering extends beyond initial diligence. Flag FCRA applicability if consumer reports are obtained.

### Phase 4 — Disqualifying Event Analysis

For each flagged item, write a memo section covering:

1. **What happened** — nature, issuing authority, date of order/conviction
2. **Lookback math** — date of event to date of intended sale; within the applicable period?
3. **Category match** — quote the order/judgment text and map it to a specific Rule 506(d)(1) category; do not paraphrase
4. **"Final order" analysis** — for state regulatory actions, confirm finality from the document itself
5. **SRO analysis** — confirm "associated with a member" status and that the sanction qualifies
6. **Pre-September 23, 2013 events** — no disqualification, but **mandatory Rule 506(e) disclosure** to investors; this is a frequent trap
7. **Conclusion** — disqualifying / not disqualifying / requires attorney verification, with rationale

### Phase 5 — Exceptions, Remediation & Disclosure

| Scenario | Path |
|---|---|
| Pre-Sept. 23, 2013 event | No disqualification; draft Rule 506(e) investor disclosure |
| Event discovered, no prior knowledge | Document reasonable-care record supporting Rule 506(d)(2)(iv) exception |
| SEC waiver | Available but rare and slow; flag for attorney to evaluate feasibility |
| Remove person from covered category | End solicitation role; resign officer role before sale; restructure ownership below 20% voting threshold — flag any arrangement that could constitute a sham |
| Replace placement agent | Engage FINRA-member broker-dealer with clean record; obtain that firm's own 506(d) certifications covering its specific soliciting individuals |
| Change exemption strategy | Evaluate Section 4(a)(2); analyze Blue Sky implications of losing §18(b)(4)(E) preemption |

**Rule 506(e) disclosure**: Must be accurate, complete, and not misleading; review against §17(a) and Rule 10b-5 anti-fraud standards before delivery to investors.

**Post-closing caution**: Remediation after sales have occurred may not cure past noncompliance. Evaluate rescission exposure and supplemental disclosure obligation.

### Phase 6 — Final Work Product Package

Deliver:
1. **Executive conclusion** — one of: (a) no disqualifying events identified; (b) potential event requiring remediation; (c) disqualifying event — do not rely on Rule 506 absent waiver or restructure
2. **Covered persons register** with basis for each inclusion/exclusion
3. **Diligence log** — dates, databases searched, attached logs or vendor reports
4. **Per-item analysis** for each flagged event
5. **Open items list** — pending questionnaires, outstanding searches, unresolved classifications; state whether closing should be conditioned on completion
6. **Next steps** with responsible owners (legal vs. company)

Cross-check any transaction document representations about 506(d) status against the diligence record. Do not permit a blanket "no bad actors" representation when diligence is incomplete or items are pending; carve out or disclose known issues.

## Guidelines

- **Verify rule text first**: Search 17 C.F.R. § 230.506(d) before finalizing — do not rely on cached lookback periods or category lists
- **No invented citations**: Any CDI, no-action letter, or case law reference must include a verified URL or be marked `[VERIFY]`
- **Voting power ≠ equity**: Always calculate the 20% threshold on voting power; aggregate related-entity holdings under common control
- **Participation is broad**: Any officer with investor contact is likely a covered person; err toward inclusion
- **Questionnaires are evidence**: A plaintiff will use a poorly drafted questionnaire against the issuer; signed certifications with document production requirements are non-negotiable
- **Diligence currency**: Searches must be current as of the sale date; refresh if closing is delayed
- **Blue Sky exposure**: Loss of Rule 506 means loss of §18(b)(4)(E) preemption; California (§25102(f) [VERIFY]), New York, and Texas have aggressive state registration regimes
- **Privilege**: The analysis memo can be privileged; questionnaires and certifications may be discoverable — draft and distribute accordingly
- **Conflicts**: Monitor for conflicts where the firm represents both the issuer and a covered person who discloses personal wrongdoing (ABA Model Rules 1.7, 1.13); separate counsel may be required
- **Attorney review required** before any output is used in an offering, shared with investors, or relied upon for filings (ABA Model Rules 1.1, 1.3, 5.3)
