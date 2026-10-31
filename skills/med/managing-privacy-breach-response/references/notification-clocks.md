# Notification Clocks, Thresholds and State Overlays

Every notice is its own clock with its own trigger. Compute each date with a script from the trigger date, show the arithmetic, and say which deadlines are outer limits that "without unreasonable delay" can shorten. Checked October 30, 2026; sources in `references/primary-sources.md`.

## Contents

1. Federal clocks table
2. Business associates, agents and BAA terms
3. Law enforcement delay
4. Counting affected individuals
5. State overlays checked for this skill
6. Notice content checklist
7. Date arithmetic

## 1. Federal clocks table

| # | Notice | Who gives it | Trigger event | Deadline | Threshold | Authority |
|---|---|---|---|---|---|---|
| F1 | Individuals | Covered entity (may delegate to the BA) | Discovery by the covered entity (164.404(a)(2)) | Without unreasonable delay; outer limit 60 calendar days after discovery | Any number | 45 C.F.R. 164.404(b) |
| F2 | Media (prominent outlets serving the State or jurisdiction) | Covered entity | Discovery by the covered entity | Without unreasonable delay; outer limit 60 calendar days after discovery | More than 500 residents of one State or jurisdiction | 164.406 |
| F3 | HHS, 500 or more | Covered entity | The date individual notice is given (contemporaneous), and in any event the discovery date | Contemporaneously with F1; HHS's page also states no later than 60 calendar days from discovery | 500 or more individuals in total | 164.408(b) |
| F4 | HHS, fewer than 500 | Covered entity | End of the calendar year in which the breach was discovered | Not later than 60 days after that year end (for 2026 discoveries: 2027-03-01); may be filed earlier | Fewer than 500 | 164.408(c) |
| F5 | Covered entity, by the business associate | Business associate (and subcontractor to BA) | Discovery by the business associate (164.410(a)(2)) | Without unreasonable delay; outer limit 60 calendar days; a shorter BAA term is a separate contractual clock with its own trigger | Any number | 164.410(b) |
| F6 | Part 2 patients, HHS, media | Part 2 program | Discovery by the program | Same as F1 to F4, applied "in the same manner" | Same | 42 C.F.R. 2.16(b) |
| F7 | FTC HBNR individuals and media | PHR vendor or PHR related entity | Discovery (318.3(c)) | Without unreasonable delay; outer limit 60 calendar days | Media: 500 or more residents of a State or jurisdiction | 16 C.F.R. 318.4(a), 318.5(b) |
| F8 | FTC, 500 or more / fewer than 500 | PHR vendor or PHR related entity | Individual notice date / end of calendar year | Contemporaneous with individual notice / 60 calendar days after year end | 500 or more / fewer | 318.4(b) |
| F9 | Vendor, by third party service provider | Third party service provider | Discovery by the service provider | Without unreasonable delay; outer limit 60 calendar days; obtain acknowledgment | Any number | 318.3(b), 318.4(a) |

Notes:

- Subpart D and 16 C.F.R. Part 318 count calendar days and contain no weekend or holiday extension: a 60th day on a Saturday is the deadline (no roll). Every computed date states its weekday and whether it rolls. Whether a state deadline that falls on a weekend rolls depends on that state's general construction law `[VERIFY]`; until confirmed, do not roll it.
- 60 days is an outer limit. Waiting to day 60 when the information was ready earlier can be unreasonable delay (74 FR 42740, 42750).
- Individual notice may go out in more than one mailing as information becomes available (164.404(d)(1)). Substitute notice: fewer than 10 with bad contact data, any reasonable alternative; 10 or more, a 90-day website posting or major media notice plus a toll-free number active 90 days (164.404(d)(2)).
- HHS accepts an estimate when the count is uncertain and an addendum later (HHS breach reporting page).

## 2. Business associates, agents and BAA terms

- Compute the business associate's own deadline (F5) from its discovery date.
- Read the BAA for every notice term: event that triggers it (security incident, suspected breach, confirmed breach), the period (business or calendar days, hours), the recipient, and required content. A shorter BAA term does not change the regulatory outer limit but is a separate clock; a late contractual notice is a contract issue and evidence on "unreasonable delay".
- Covered entity clock: if the business associate is an agent, F1 runs from the business associate's discovery; if not, from the business associate's notice. When agency is unclear, show both and use the earlier as the working deadline.
- Proposed Security Rule changes (90 FR 898, Jan. 6, 2025) would require a BAA term for reporting contingency plan activation within 24 hours; the rule is not final (Unified Agenda: long-term action, final action projected July 2027) and would not change breach reporting. Do not apply it as law.

## 3. Law enforcement delay

- Written statement that notice would impede a criminal investigation or damage national security, specifying a period: delay for that period (164.412(a)).
- Oral statement: document it and the official's identity; delay no longer than 30 days from the oral statement unless a written statement arrives in that time (164.412(b)).
- HHS reads 164.412 as tolling the notice periods (78 FR 5566, 5658). How the remaining days are counted after the delay ends is `[VERIFY]`; show the computation used.
- The delay applies to each notice (individual, media, HHS, BA). State statutes have their own law enforcement provisions; apply each separately.

## 4. Counting affected individuals

- Count unique individuals whose unsecured PHI was, or is reasonably believed to have been, accessed, acquired, used or disclosed. Deduplicate across systems and record types.
- HHS threshold: 500 or more in total. Media threshold: more than 500 residents of one State or jurisdiction (a county, city or town). 600 people split 200/200/200 across three jurisdictions requires HHS notice but no media notice; 600 in Maryland and 600 in the District of Columbia requires media notice in both (74 FR 42740, 42753; 78 FR 5566, 5654).
- FTC media threshold is 500 or more residents, not more than 500.
- Residence is the individual's state of residence, not the facility's state or the state where care was given. Use last known address; list unknown residence as its own row.
- Count deceased individuals; notice goes to next of kin or personal representative where the address is known (164.404(d)(1)(ii)).
- State attorney general thresholds count residents of that state only.

## 5. State overlays checked for this skill

Read from the official statute pages on October 30, 2026. Each row has its own trigger. Any state not listed is `[VERIFY]`: many states set deadlines shorter than 60 days and require attorney general notice, and their definitions differ (computerized data only, name plus element, risk-of-harm exceptions, HIPAA deemed-compliance clauses).

| State and statute | Notice | Trigger | Deadline | Threshold or condition | HIPAA interaction |
|---|---|---|---|---|---|
| California, Civ. Code 1798.82 (as amended by SB 446, effective Jan. 1, 2026) | Residents | Discovery or notification of the breach | Within 30 calendar days; delay allowed for law enforcement or to determine scope and restore integrity | Computerized personal information, including medical and health insurance information with name | (e) deems a covered entity compliant with the content rules of (d) if it complied with HITECH 13402(f); no other exemption. Applying (a)(2) timing to a covered entity rests on that text `[VERIFY]` |
| California, Civ. Code 1798.82(f) | Attorney General (sample copy) | Date consumers were notified | Within 15 calendar days | More than 500 California residents | Same |
| California, Health & Safety Code 1280.15 | CDPH and the patient | Detection of the unlawful or unauthorized access, use or disclosure | No later than 15 business days | Licensed clinic, health facility, home health agency, hospice; paper and electronic; internal misdirection within the same facility or system while coordinating care is not unauthorized | Separate from HIPAA; own law enforcement delay rule |
| New York, Gen. Bus. Law 899-aa(2) | Residents | Discovery | Within 30 days | Computerized private information (includes medical and health insurance information) | If notice is given under HIPAA rules, no additional resident notice (899-aa(2)(b)). Whenever any NY residents are notified, notice also goes to the AG, Department of State and State Police, and to the Department of Financial Services only if the entity is a covered entity under 23 NYCRR 500.1 (filed under 23 NYCRR 500.17), with a template copy (8)(a); whether a HIPAA notice sent after day 30 satisfies the 30-day rule is `[VERIFY]` |
| New York, 899-aa(9) | Attorney General | The date the covered entity notified HHS | Within 5 business days of notifying HHS | Any breach a covered entity reports to HHS, even if not "private information" | Applies to covered entities |
| New York, 899-aa(2)(a) | Written determination to AG | Date of the no-notice determination | Within 10 days | Inadvertent disclosure by authorized persons, determined unlikely to cause misuse or harm; affects over 500 NY residents; keep 5 years | State-law exception, separate from HIPAA's |
| Texas, Bus. & Com. Code 521.053(b) | Residents | Date the entity determines that the breach occurred | Without unreasonable delay; not later than the 60th day, "except as provided by Subsection (d) or as necessary to determine the scope of the breach and restore the reasonable integrity of the data system" | Computerized sensitive personal information, including health information that identifies the individual | No covered-entity exemption found |
| Texas, 521.053(i) | Attorney General (online form) | Date the entity determines that the breach occurred | As soon as practicable; not later than the 30th day | At least 250 Texas residents | Same |
| Washington, RCW 19.255.010(8) | Residents | Discovery | Within 30 calendar days, unless the delay is at law enforcement's request or "due to any measures necessary to determine the scope of the breach and restore the reasonable integrity of the data system" | Personal information (includes medical and health insurance information); not required if not reasonably likely to subject consumers to a risk of harm | A covered entity that complied with HITECH 13402 is deemed compliant (RCW 19.255.030) |
| Washington, RCW 19.255.010(7) | Attorney General | Discovery | Within 30 days; for a covered entity, on HITECH timing (RCW 19.255.030) | More than 500 Washington residents | Covered entities still notify the AG |

The Texas and Washington scope-and-integrity wording (and California 1798.82(a)(2)(B)) reads as permitting delay past the stated day while those measures are necessary; how far it reaches has no agency guidance read `[VERIFY]`. Treat it as narrow: document each measure and its dates, and never use it to cover a stalled investigation.

"Determines" (Texas) and "detected" (California) are different triggers from HIPAA "discovery". Record each date from the record; do not assume they coincide, and do not postpone a determination to delay a clock.

## 6. Notice content checklist

HIPAA individual and media notice (164.404(c)), in plain language, to the extent possible: (A) what happened, with the date of the breach and the date of discovery; (B) the types of unsecured PHI involved; (C) steps individuals should take to protect themselves; (D) what the entity is doing to investigate, mitigate harm and protect against further breaches; (E) contact procedures including a toll-free number, email address, website or postal address. FTC notices add third-party identity and two or more contact methods (318.6). State statutes add elements (for example California's headings and New York's agency contact list); check each state row. Drafting the letters is routed to data-breach-consumer-notice.

## 7. Date arithmetic

Compute dates with a script, never by hand, and paste the inputs and outputs into the clocks table. Example in Python:

```python
from datetime import date, timedelta
def plus_days(d, n): return d + timedelta(days=n)
def plus_business_days(d, n, holidays=()):
    x, k = d, 0
    while k < n:
        x += timedelta(days=1)
        if x.weekday() < 5 and x not in holidays: k += 1
    return x
discovery = date(2026, 9, 3)
print(plus_days(discovery, 60))                       # outer limit, calendar days
print(plus_days(date(2026, 12, 31), 60))              # HHS log for 2026 discoveries
```

Business-day clocks depend on the state's holiday calendar; list the holidays used and mark them `[VERIFY]` unless confirmed.
