---
name: insider-trading-policy
description: >-
  Drafts a U.S. financial-services insider trading policy memo with MNPI
  definitions, possession standard, tipping bans, restricted and watch lists,
  preclearance, blackout windows, 10b5-1 plan governance, reporting, training,
  and enforcement. Use when creating or updating insider trading policies for
  broker-dealers, investment advisers, investment companies, or other
  financial firms. Trigger keywords: insider trading policy, 10b5-1 plan,
  preclearance, restricted list, watch list, blackout period, Reg FD, MNPI.
tags:
  - drafting
  - memo
  - regulatory
  - research
---

# Insider Trading Policy (Financial Services)

Produce a firm-ready insider trading policy that is enforceable, auditable, and practical for employees.

## Prerequisites

1. Firm name, legal entity structure, and regulatory status (broker-dealer, investment adviser, investment company, bank affiliate, or other).
2. Business lines and access points to MNPI (IB, research, trading, portfolio mgmt, corporate access, lending, etc.).
3. Whether the firm or parent is a public issuer and earnings release cadence.
4. Existing employee trading systems and preclearance workflows.
5. Current restricted and watch list practices and list owners.
6. Personal trading exceptions the firm will allow.
7. Outside business activity and board service approval process.
8. Compliance contacts, reporting hotline, and non-retaliation policy text.

## Output Structure / Process

1. Populate the variables and confirm regulatory add-ons that apply.
2. Verify legal authorities and insert accurate citations.
3. Draft the policy in the section order below, using defined terms consistently.
4. Tailor controls to the firm's systems and risk profile.
5. Add appendices for quick reference and forms.

**Variables**
```
firm_name:
effective_date:
version:
policy_owner_title:
policy_owner_contact:
public_cooldown_days: 2
blackout_start_days_before_q_end: 14
blackout_end_days_after_earnings: 2
preclearance_lead_time_days: 1
holding_period_days: 60
cooling_off_days_officer_director: [VERIFY]
cooling_off_days_other: [VERIFY]
```

**Authorities To Validate**
| Authority | Applies to | Notes |
| --- | --- | --- |
| Exchange Act Section 10(b) and Rule 10b-5 [VERIFY] | All | Core anti-fraud and insider trading prohibition. |
| Rule 10b5-1 [VERIFY] | All | Affirmative defense and plan requirements. |
| Regulation FD [VERIFY] | Issuers | Selective disclosure restrictions. |
| Advisers Act Rule 204A-1 [VERIFY] | Investment advisers | Code of ethics and personal trading controls. |
| Investment Company Act Rule 17j-1 [VERIFY] | Investment companies | Code of ethics and reporting. |
| FINRA rules on OBA, private securities transactions, and outside accounts [VERIFY] | Broker-dealers | Align with supervisory procedures. |

**Policy Sections**
| Section | Required content |
| --- | --- |
| 1. Purpose and Scope | Covered persons; covered securities; possession standard; extraterritorial application; personal, joint, trust, and managed accounts. |
| 2. Definitions | MNPI, Material, Nonpublic, Public dissemination, Tipping, Beneficial ownership, Covered person, Trading, Recommendation. |
| 3. Core Prohibitions | No trading while in possession of MNPI; no tipping; no recommending or inducing; no circumvention via third parties. |
| 4. Information Barriers | Physical and system controls; access logs; prohibited cross-wall communications; monitoring and audits. |
| 5. Wall Crossing | Pre-approval; written notice; acknowledgment; duration; trading freeze; documentation. |
| 6. Restricted List | Criteria; trading bans; research restrictions; additions and removals; distribution method. |
| 7. Watch List | Monitoring scope; escalation triggers; no safe harbor. |
| 8. Preclearance | Who must preclear; request data; approval window; denial grounds; execution confirmation. |
| 9. Blackout Periods | If issuer: who is subject; timing; exceptions; earnings releases. |
| 10. 10b5-1 Plans | Eligibility; approval; cooling-off; modifications; overlapping plans; certifications; monitoring. |
| 11. Personal Trading Limits | Short sales, derivatives, margin limits, holding periods, speculative trading bans. |
| 12. Reporting | Initial holdings, quarterly transactions, annual certifications, duplicate statements. |
| 13. Outside Activities | Board service approval; conflicts; reporting MNPI received externally. |
| 14. Training | Annual training; role-based frequency; case studies. |
| 15. Enforcement | Discipline range; zero-tolerance for intentional misconduct; regulator cooperation. |
| 16. Reporting and Non-Retaliation | Hotline; escalation; confidentiality; non-retaliation. |
| 17. Administration | Policy owner, amendments, annual review, version control. |

**Definitions Table**
| Term | Standard to use |
| --- | --- |
| Material | Reasonable investor would consider it important or it would likely affect price. |
| Nonpublic | Not broadly disseminated; requires market absorption period of `public_cooldown_days`. |
| MNPI | Material and nonpublic information from any source. |
| Possession standard | Trading while aware of MNPI is prohibited regardless of use. |
| Public dissemination | SEC filings, major newswires, broad press release, or public conference with open access. |
| Tipping | Disclosing MNPI to anyone outside authorized channels. |
| Covered securities | Equity, debt, options, swaps, derivatives, ADRs, and instruments linked to the issuer. |
| Covered persons | Employees, officers, directors, interns, contractors, consultants, and temporary staff. |

**Core Prohibitions Checklist**
- No trading in covered securities while in possession of MNPI.
- No tipping MNPI to any person outside authorized channels.
- No recommendations or inducement to trade while in possession of MNPI.
- No trading via third-party accounts or through managed accounts to evade restrictions.

**Controls Checklist**
- Information barriers with documented access controls and audits.
- Wall crossing protocol with compliance approval and written acknowledgments.
- Restricted list and watch list governance with documented criteria.
- Mandatory preclearance with same-day execution limits.
- Blackout periods for issuer securities, if applicable.
- 10b5-1 plan governance and monitoring.
- Personal trading limits: short sales, derivatives, margin, and holding periods.
- Reporting: initial, quarterly, and annual plus duplicate confirmations.
- Training, certification, and enforcement.

**Template Blocks**
```text
Policy Header
Title: Insider Trading Policy
Effective Date: {effective_date}
Version: {version}
Owner: {policy_owner_title}
Contact: {policy_owner_contact}
```

```text
Preclearance Request (minimum fields)
Employee name and role:
Security name and ticker/CUSIP:
Transaction type and quantity:
Account and broker:
Proposed trade date:
Reason for trade:
```

```text
Wall Crossing Notice
Recipient:
Project or issuer:
MNPI categories disclosed:
Restriction start date:
Restriction end condition:
Acknowledgment:
```

```text
Annual Certification
I have read and will comply with the Insider Trading Policy. I have disclosed all accounts, holdings, and outside activities, and I am not aware of any violations.
```

## Guidelines

- Use defined terms consistently and capitalize them.
- Do not claim a legal requirement for the `public_cooldown_days` value; treat it as firm policy.
- If the firm is not a public issuer, remove Reg FD and blackout sections.
- Insert only verified citations; mark unverified ones with `[VERIFY]`.
- Align with adviser or investment company code-of-ethics rules if applicable.
- Include jurisdiction-specific addenda for non-US personnel and non-US markets.
- Route policy questions and exceptions to the Compliance Department and document approvals.
