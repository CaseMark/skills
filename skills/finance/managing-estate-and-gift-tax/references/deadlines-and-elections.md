# Deadlines and Elections

Every timed element has its own trigger event. Compute each date by script from that trigger, state its weekday, and say whether IRC 7503 moves it. Checked on October 30, 2026 against the sources in `primary-sources.md`.

## Contents

1. Clock table
2. Computing a date
3. Weekends and legal holidays (IRC 7503)
4. Checking windows on the as-of date
5. Election traps

## 1. Clock table

| # | Element | Trigger event | Length or test | Citation |
|---|---|---|---|---|
| C1 | Form 706 due | Date of death | Same numbered day of the ninth month after death; if none, last day of that month | IRC 6075(a); Treas. Reg. 20.6075-1 |
| C2 | Automatic six-month filing extension | Form 4768 filed on or before C1 | Extended due date six months after the C1 date | Treas. Reg. 20.6081-1(b) |
| C3 | Estate tax payment due | Date of death (time fixed for filing, without extension) | Same date as unextended C1; C2 does not move it | IRC 6151(a); Treas. Reg. 20.6081-1(e) |
| C4 | Extension of time to pay | Request made before C3 | Up to 12 months (6161(a)(1)); up to 10 years for reasonable cause (6161(a)(2)) | IRC 6161 |
| C5 | Portability election | Date of death | On a timely Form 706 (C1, or C2 if extended) | IRC 2010(c)(5)(A); Treas. Reg. 20.2010-2(a)(1) |
| C6 | Late portability election | Date of death | On or before the fifth anniversary of death; only for an estate not required to file by value that did not file timely | Rev. Proc. 2022-32 secs. 3.01, 4.01 |
| C7 | Alternate valuation date | Date of death; or an earlier distribution, sale or disposition | Six months after death, or the disposition date | IRC 2032(a) |
| C8 | Alternate valuation election | Form 706 due date including extensions (C1 or C2 as prescribed) | Return filed no more than one year after that date | IRC 2032(d)(2) |
| C9 | 6166 installment election | Form 706 due date including extensions | Made on a timely filed return | IRC 6166(d); Treas. Reg. 20.6166-1(b) |
| C10 | First 6166 installment | Payment due date (C3) | Date selected, not more than five years after C3; then yearly | IRC 6166(a)(3) |
| C11 | Basis statements (Form 8971) | Earlier of the Form 706 due date (including extensions) and the date the Form 706 is filed | 30 days after that date | IRC 6035(a)(3) |
| C12 | Form 709 due | Close of the calendar year of the gift | April 15 of the following year | IRC 6075(b)(1) |
| C13 | Form 709 extension | Income tax extension for the year, or Form 8892 filed by C12 | Six months (October 15); no extension to pay | IRC 6075(b)(2); Treas. Reg. 25.6081-1 |
| C14 | Form 709 for the year of the donor's death | Donor's date of death | No later than the Form 706 due date including extensions | IRC 6075(b)(3) |
| C15 | Gift-splitting consent | Close of the calendar year of the gift | Not after April 15 of the following year unless no return was filed by then; never after a notice of deficiency | IRC 2513(b)(2) |
| C16 | Timely GST allocation; election out; election to treat as a GST trust | Calendar year of the transfer | On a Form 709 filed by C12, or C13 if an extension was actually granted | IRC 2632(b)(3), (c)(5)(B); 2642(b)(1); Treas. Reg. 26.2632-1(b)(2), (b)(4) |
| C17 | Gift tax assessment period | Date the Form 709 is filed (an early return is treated as filed on C12) | Three years; no limit for a gift not adequately disclosed | IRC 6501(a), (b)(1), (c)(9); Treas. Reg. 301.6501(c)-1(f) |
| C18 | Three-year lookback | Each transfer of an interest or release of a power | Within three years before death | IRC 2035(a); 2038(a)(1) |
| C19 | Proposed anti-clawback lookback | Each release of an interest or power that would have caused inclusion | Within 18 months before death | Proposed Treas. Reg. 20.2010-1(c)(3)(i)(D) (not final) |
| C20 | Annual exclusion year | Calendar year | Gifts completed by December 31 | IRC 2503(b) |
| C21 | Crummey withdrawal window | Each contribution, or notice, as the instrument provides | Period stated in the trust instrument | Trust instrument; notice practice [VERIFY] |
| C22 | Estate tax assessment period | Date the Form 706 is filed | Three years | IRC 6501(a), (b)(1) |
| C23 | Gift tax payment | Close of the calendar year of the gift | April 15 of the following year; a C13 extension does not extend payment | IRC 6151(a); Treas. Reg. 25.6081-1(c) |

## 2. Computing a date

Compute with a script, never by hand. A minimal version:

```python
from datetime import date, timedelta
from calendar import monthrange

def add_months(d, months):
    y, m = divmod(d.month - 1 + months, 12)
    y, m = d.year + y, m + 1
    return date(y, m, min(d.day, monthrange(y, m)[1]))  # no matching day -> last day of month

def roll(d, holidays):
    while d.weekday() >= 5 or d in holidays:  # Saturday, Sunday, DC legal holiday
        d += timedelta(days=1)
    return d

death = date(2026, 4, 10)
c1 = add_months(death, 9)              # 2027-01-10, a Sunday
c1_rolled = roll(c1, holidays=set())   # 2027-01-11, a Monday
print(c1, c1.strftime("%A"), c1_rolled, c1_rolled.strftime("%A"))
```

Rules for the output:
- Show the prescribed date, its weekday, and the rolled date if IRC 7503 moves it.
- A period measured from another deadline (C8, C11) is measured from the prescribed date, not the rolled date. Where the reading is unclear, use the earlier date and say so.
- Treat a filing extension and a payment extension as different rows. An extension is counted only if it was actually requested or granted; otherwise show the extended date as "available if requested by" the unextended date.
- A deadline that depends on whether a return was filed (C11, C15, C17) shows each branch.

## 3. Weekends and legal holidays (IRC 7503)

- IRC 7503: when the last day for an act falls on a Saturday, Sunday or legal holiday, the act is timely on the next day that is none of these. Extensions are included in finding the last day. It applies to acts by taxpayers (returns, payments, petitions, claims) and by the IRS (notices, assessment, collection) (Treas. Reg. 301.7503-1(a)).
- Legal holidays are those of the District of Columbia under D.C. Code 28-2701 (Treas. Reg. 301.7503-1(b)): New Year's Day; Martin Luther King, Jr.'s Birthday (third Monday in January); Washington's Birthday (third Monday in February); District of Columbia Emancipation Day (April 16); Memorial Day (last Monday in May); Juneteenth (June 19); Independence Day (July 4); Labor Day (first Monday in September); Indigenous Peoples' Day (second Monday in October); Veterans Day (November 11); Thanksgiving (fourth Thursday in November); Christmas (December 25); Inauguration Day every fourth year. A holiday on a Saturday is observed the preceding Friday; on a Sunday, the following Monday.
- A statewide legal holiday in the state where the IRS office is located also counts for a filing at that office (301.7503-1(b)). Which state applies to a given filing is [VERIFY].
- Example: an assessment period ending Sunday, April 15, 2029 moves past Monday, April 16, 2029 (DC Emancipation Day) to Tuesday, April 17, 2029.

## 4. Checking windows on the as-of date

State the as-of date. For every row of the clock table that the matter triggers, give the status:
- **Open**: the prescribed date is on or after the as-of date.
- **Open (rolled by IRC 7503)**: the prescribed date is before the as-of date but the rolled date is on or after it.
- **Passed**: the rolled date is before the as-of date.
- **Not triggered**: the trigger event has not happened (for example no death, no gift in the year).
- **Not determinable**: the trigger date is unknown or disputed; name what would settle it.

List every Open window, its action, and who must act (donor, consenting spouse, executor, trustee). A window that is Open but would not help the client (for example a late portability election for a spouse who is no longer the last deceased spouse) is still listed, with the reason it does not help.

## 5. Election traps

- Portability is lost by not filing; the 9100 route is closed to an estate that was required to file by value (Treas. Reg. 20.2010-2(a)(1)).
- The 6166 and 2032 elections need a timely return; a late return loses 6166 and, after one year, 2032.
- Filing for an extension (Form 4768, Form 8892 or an income tax extension) does not extend payment.
- Gift splitting covers all of both spouses' gifts to third parties for the year; it cannot be chosen gift by gift.
- An election out of automatic GST allocation, or an affirmative allocation to a trust that is not a GST trust, is made only on a timely Form 709; after that, allocation is late and uses current value.
- Backdating a document or a signature to meet any of these dates is never an option (Ground Rule 8 in SKILL.md).
