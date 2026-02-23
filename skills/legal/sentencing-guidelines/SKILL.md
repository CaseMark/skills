---
name: sentencing-guidelines
description: Analyzes federal and state sentencing guidelines for criminal defense matters. Calculates base offense levels, specific offense characteristics, adjustments, criminal history categories, and advisory guideline ranges with precise USSG citations. Evaluates departures, variances, and § 3553(a) factors. Use when calculating sentencing ranges, preparing sentencing memoranda, analyzing PSRs, or developing sentencing advocacy strategy.
tags:
  - analysis
  - litigation
---

# Sentencing Guideline Analysis

Produces a complete sentencing guideline calculation and strategic analysis for federal or state criminal matters.

## Prerequisites

1. **Charging documents** — indictment, information, or superseding instruments with specific counts and statutes
2. **Presentence Investigation Report (PSR)** — if available; note any objections
3. **Criminal history records** — prior convictions, sentences imposed, dates of offense/release
4. **Plea agreement** — if applicable, including any stipulated guidelines or § 5K1.1 provisions
5. **Offense conduct summary** — factual basis, relevant conduct under USSG § 1B1.3
6. **Jurisdiction** — federal (specify district/circuit) or state (specify sentencing scheme)

## Output Structure

### 1. Executive Summary

| Field | Content |
|---|---|
| Defendant | Name, case number |
| Counts | List with statute citations |
| Total Offense Level | Final calculated TOL |
| Criminal History Category | I–VI |
| Advisory Range | X–Y months |
| Statutory Range | Mandatory mins/maxes per count |
| Recommended Position | Below/within/above range with rationale |

### 2. Base Offense Level Calculation

For each count, produce:

| Step | USSG Section | Description | Level |
|---|---|---|---|
| Base Offense Level | § 2X#.# | Offense guideline | +## |
| SOC 1 | § 2X#.#(b)(#) | Specific offense characteristic | +/- ## |
| SOC 2 | § 2X#.#(b)(#) | Specific offense characteristic | +/- ## |
| Cross-reference | § 2X#.#(c)(#) | If applicable | +/- ## |
| **Adjusted BOL** | | | **##** |

### 3. Chapter 3 Adjustments

| Adjustment | USSG Section | Application | Level |
|---|---|---|---|
| Victim-related | §§ 3A1.1–3A1.4 | Vulnerable victim, hate crime, etc. | +/- ## |
| Role | §§ 3B1.1–3B1.4 | Leader/manager/minimal/minor participant | +/- ## |
| Obstruction | § 3C1.1 | If applicable | +2 |
| Acceptance | § 3E1.1 | 2-level + 1-level if timely (gov't motion) | -2/-3 |
| **Adjusted Offense Level** | | | **##** |

### 4. Multiple Count Analysis (if applicable)

Apply USSG §§ 3D1.1–3D1.5 grouping rules:

- Identify count groups under § 3D1.2(a)–(d)
- Determine highest adjusted offense level per group
- Apply multiple count units table (§ 3D1.4)
- Calculate combined adjusted offense level

### 5. Criminal History Category

| Prior Conviction | Sentence | Points | USSG Section | Notes |
|---|---|---|---|---|
| [Offense] | [Term] | # | § 4A1.1(a)/(b)/(c) | Recency, revocations |

**Total CH Points:** ##
**Criminal History Category:** #

Flag if applicable:
- [ ] Career Offender — § 4B1.1 (prior felony crime of violence or controlled substance offense)
- [ ] Armed Career Criminal — 18 U.S.C. § 924(e) / § 4B1.4
- [ ] Criminal Livelihood — § 4B1.3
- [ ] Excluded sentences — § 4A1.2(c) (petty offenses, expired convictions)

### 6. Sentencing Table Application

- **Final Offense Level:** ##
- **Criminal History Category:** #
- **Advisory Range:** ##–## months (USSG Ch. 5, Pt. A)
- **Zone:** A / B / C / D (determines probation eligibility per §§ 5B1.1, 5C1.1)

### 7. Statutory Constraints

| Count | Statute | Mandatory Minimum | Statutory Maximum | Effect on Range |
|---|---|---|---|---|
| # | [cite] | ## months | ## months | Overrides/constrains |

Note § 5G1.1 interaction: if guideline range falls below mandatory minimum, the minimum becomes the guideline floor.

### 8. Departures & Variances

#### Downward Departures (Chapter 5K)

| Ground | USSG Section | Strength | Supporting Facts |
|---|---|---|---|
| Substantial assistance | § 5K1.1 | Strong/Moderate/Weak | Gov't motion required |
| Diminished capacity | § 5K2.13 | | Mental health evidence |
| Aberrant behavior | § 5K2.20 | | Single act, no planning |
| Family ties | § 5H1.6 | | Dependent care obligations |
| Over-representation of CH | § 4A1.3(b) | | Stale or minor priors |

#### § 3553(a) Variance Arguments

For each factor, identify specific facts:

1. **Nature and circumstances of offense** — § 3553(a)(1)
2. **History and characteristics of defendant** — § 3553(a)(1)
3. **Seriousness / just punishment** — § 3553(a)(2)(A)
4. **Deterrence** — § 3553(a)(2)(B)
5. **Public protection** — § 3553(a)(2)(C)
6. **Rehabilitation / treatment** — § 3553(a)(2)(D)
7. **Guidelines range** — § 3553(a)(4)
8. **Avoid unwarranted disparities** — § 3553(a)(6)

Cite circuit-specific case law supporting each variance argument.

### 9. Strategic Recommendations

- Recommended sentencing position with range
- Key arguments ranked by persuasiveness
- Weaknesses to address preemptively
- Restitution, forfeiture, supervised release considerations (§§ 5D1.1–5D1.3, 5E1.1)

## Guidelines

- Cite specific USSG sections for every calculation step — never state a level without a provision
- When PSR is available, identify all objections with specificity
- For state cases, substitute the applicable state sentencing grid/scheme and cite state provisions
- Flag any relevant conduct disputes under § 1B1.3 — preponderance standard applies
- Note circuit splits or recent amendments that affect the analysis
- If career offender or ACCA applies, calculate both the enhanced and non-enhanced range
- Mark any case citations as `[VERIFY]` unless sourced from provided documents
- Identify missing information explicitly — incomplete criminal history or unresolved relevant conduct can shift the range significantly
- Always note whether *Booker* advisory framework or any mandatory scheme applies
- For drug cases, address safety valve eligibility under 18 U.S.C. § 3553(f) / USSG § 5C1.2
