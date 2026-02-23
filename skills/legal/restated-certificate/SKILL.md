---
name: restated-certificate
description: Drafts an Amended and Restated Certificate of Incorporation for Delaware corporations in preferred stock financing rounds. Implements authorized capital structure, preferred stock rights (dividends, liquidation preferences, conversion, anti-dilution), protective provisions, and DGCL compliance from term sheets and cap tables. Use when drafting charter documents, restated certificates, venture financing corporate documents, or Delaware certificate amendments.
tags:
  - agreement
  - corporate
  - drafting
---

# Amended and Restated Certificate of Incorporation

Drafts a filing-ready Amended and Restated Certificate of Incorporation for a Delaware corporation, typically in connection with a preferred stock financing round.

## Prerequisites

1. **Term sheet** — pricing, liquidation preference multiple, anti-dilution method, protective provisions, board composition
2. **Prior Certificate of Incorporation** — current authorized capital, existing preferred series, any unusual provisions
3. **Capitalization table** — shares outstanding, option pool, warrants, convertible notes
4. **Transaction documents** — SPA, IRA, voting agreement, ROFR/co-sale (for cross-reference)
5. **Registered agent info** — name, physical Delaware street address, county

## Pre-Draft Verification

Before drafting, extract and cross-check:

| Data Point | Source | Verify Against |
|---|---|---|
| Pre/post-money valuation | Term sheet | Cap table |
| Price per share | Term sheet | SPA, cap table math |
| Shares issued this round | Term sheet | SPA |
| Total authorized Common | Cap table | Outstanding + option pool + all conversions + cushion |
| Total authorized Preferred (per series) | Term sheet | Shares issued + warrant/note conversions + anti-dilution cushion |
| Option pool size | Term sheet | Board resolutions, cap table |
| Liquidation preference multiple | Term sheet | SPA |
| Dividend rate & type | Term sheet | — |
| Anti-dilution method | Term sheet | — |
| Board composition | Term sheet | Voting agreement |

Flag any discrepancies before proceeding.

## Output Structure

### Document Skeleton

```
AMENDED AND RESTATED CERTIFICATE OF INCORPORATION
OF [EXACT LEGAL NAME]

[Corporation] hereby certifies:

1. Original Certificate filed with the Delaware Secretary of State on [DATE].
2. This Amended and Restated Certificate has been duly adopted pursuant to
   Sections 242 and 245 of the DGCL [by board consent under §245 / by board
   and stockholder approval under §242].
3. The text of the Certificate is hereby amended and restated in its entirety
   as follows:

ARTICLE I — NAME
ARTICLE II — REGISTERED OFFICE AND AGENT
ARTICLE III — PURPOSE
ARTICLE IV — AUTHORIZED CAPITAL
ARTICLE V — PREFERRED STOCK RIGHTS
ARTICLE VI — DIRECTOR EXCULPATION
ARTICLE VII — [Additional governance as needed]

IN WITNESS WHEREOF...
[Signature block: name, title, date]
```

### Article-by-Article Drafting Guide

**Article I — Name**
- Must include corporate designator (Corp., Inc., Incorporated, etc.) per DGCL §102(a)(1)
- Must match name across all transaction documents exactly

**Article II — Registered Office**
- Physical street address in Delaware (no P.O. boxes), include county
- Named registered agent who has consented to serve

**Article III — Purpose**
- Standard broad clause: "any lawful act or activity for which corporations may be organized under the DGCL"
- Narrow only if regulatory/tax reasons require it

**Article IV — Authorized Capital**

```
Total authorized: [X] shares
  Common Stock: [X] shares, $[0.0001] par value
  Preferred Stock: [X] shares, $[0.0001] par value
    Series Seed: [X] shares
    Series A: [X] shares
    [Additional series as needed]
    Undesignated: [X] shares (blank check authority)
```

Verify Common Stock covers: outstanding + option pool + all preferred as-converted + warrants/notes + cushion.

**Article V — Preferred Stock Rights**

Draft each section in this order:

| Section | Key Decisions |
|---|---|
| **Dividends** | Cumulative vs. non-cumulative; rate (% of OIP/annum); when-as-if-declared vs. auto-accruing; priority among series; treatment on conversion |
| **Liquidation Preference** | Define "Liquidation Event" broadly (dissolution + deemed liquidation: M&A, asset sale); preference amount (OIP × multiple + accrued dividends); series priority (pari passu vs. senior); participating vs. non-participating; participation cap if applicable |
| **Optional Conversion** | Conversion ratio = OIP ÷ Conversion Price; initial CP = OIP; mechanics (certificate surrender, no fractional shares — round or cash out) |
| **Mandatory Conversion** | Triggers: qualified IPO (min gross proceeds + min per-share price as multiple of OIP); vote/consent of [majority/⅔] of Preferred voting as-converted as single class |
| **Anti-Dilution** | Broad-based weighted average formula (see below); define "fully diluted" broadly (outstanding + as-converted preferred + options + warrants + pool); enumerate carve-outs |
| **Voting Rights** | As-converted voting with Common as single class; separate class vote for protective provisions |
| **Protective Provisions** | Require [majority/⅔] Preferred consent for enumerated actions (see checklist below) |
| **Board Designation** | Seats allocated to Common holders, each Preferred series, independent/mutual (if in certificate rather than voting agreement) |

**Anti-Dilution Formula (Broad-Based Weighted Average):**

```
Adjusted CP = CP × (A + B) / (A + C)

Where:
  CP  = Conversion Price in effect immediately prior to new issuance
  A   = Shares of Common outstanding on fully-diluted, as-converted basis
  B   = Aggregate consideration received ÷ CP (shares purchasable at old price)
  C   = Number of shares actually issued in new issuance
```

**Standard Anti-Dilution Carve-Outs:**
- [ ] Employee/consultant equity under board-approved plans
- [ ] Bank/equipment lender securities
- [ ] Strategic partner/vendor/customer securities (board-approved)
- [ ] Sponsored research/collaboration securities (board-approved)
- [ ] Acquisition consideration (board-approved)
- [ ] Conversion/exercise of existing convertible securities
- [ ] Stock splits, stock dividends, recapitalizations
- [ ] Securities approved by requisite Preferred holders

**Protective Provisions Checklist:**
- [ ] Amend certificate or bylaws adversely affecting Preferred
- [ ] Authorize/create senior or pari passu stock
- [ ] Increase/decrease authorized Preferred or Common
- [ ] Declare dividends or distributions on Common
- [ ] Redeem/repurchase Common or Preferred (except terminated-employee repurchases at cost)
- [ ] Liquidate, dissolve, or wind up
- [ ] Consummate deemed liquidation event (M&A, asset sale)
- [ ] Amend transaction documents adversely to Preferred
- [ ] Change board size
- [ ] Incur debt above board-approved thresholds
- [ ] Exclusively license or dispose of material IP

Determine whether series vote together or have separate series votes for specific matters.

**Liquidation Waterfall — Non-Participating:**
1. Pay Preferred liquidation preference (OIP × multiple + accrued dividends)
2. Remaining proceeds to Common only
3. Each Preferred holder may elect to convert and take Common pro rata instead

**Liquidation Waterfall — Participating (with cap):**
1. Pay Preferred liquidation preference
2. Remaining proceeds shared pro rata among Preferred (as-converted) and Common
3. Preferred participation ceases at cap (e.g., 3× OIP); further proceeds to Common only

**Article VI — Director Exculpation**
- DGCL §102(b)(7) maximum exculpation
- Carve-outs required by statute: duty of loyalty breach, bad faith/intentional misconduct, §174 liability, improper personal benefit
- Include future-amendment auto-update clause

**Article VII+ — Optional Additional Provisions**
- Indemnification to fullest extent of Delaware law + mandatory advancement
- D&O insurance authority
- Corporate opportunity waiver (if applicable for investor-affiliated directors)
- Forum selection clause (Court of Chancery for internal affairs)
- Written consent / special meeting provisions

## Guidelines

1. **Defined terms** — define once, use consistently; cross-check against SPA/IRA/voting agreement definitions
2. **Mathematical verification** — test liquidation waterfall at multiple exit values; verify anti-dilution formula produces correct adjusted CP for a sample down-round
3. **Cross-reference accuracy** — verify all internal section references and subsection numbering
4. **DGCL compliance** — cite §§242, 245 in recitals; §102(a)(1) for naming; §102(b)(7) for exculpation; §151 for stock rights; §174 for exculpation carve-out
5. **Blank check preferred** — if authorized, ensure protective provisions give Preferred consent rights over future series designation
6. **Par value consistency** — match across Common and Preferred unless specific reason to differ
7. **Filing readiness** — document must be executable and fileable with Delaware Secretary of State as-is
8. **Edge case testing** — verify conversion mechanics for partial conversion, mandatory triggers, and acquisition scenarios
9. **Do not** guess at share numbers, valuations, or pricing — flag gaps and request clarification
10. **Jurisdiction** — this skill is Delaware-specific; do not apply to other states without modification
