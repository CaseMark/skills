---
name: structuring-global-fund-distribution
language: en
description: Designs international fund distribution with UCITS/AIFMD compliance, passporting, and local registration requirements. Use when planning international distribution, structuring cross-border fund access, or navigating regulatory requirements.
tags:
  - cross-border-capital
  - compliance
  - regulatory
metadata:
  author: casemark
  practice_areas:
    - International Finance
    - Cross-Border Transactions
    - Emerging Markets
  document_types:
    - Report
  skill_modes:
    - Analysis
---
# Structuring Global Fund Distribution

Designs international fund distribution strategies for investment funds seeking cross-border access, addressing UCITS/AIFMD regulatory frameworks, passporting mechanics, and local registration or private placement requirements in target jurisdictions.

## When To Use

- Planning distribution of a UCITS or AIF into new jurisdictions beyond the fund's home member state
- Evaluating whether to use EU passporting, national private placement regimes (NPPRs), or reverse solicitation
- Structuring fund wrappers or feeder vehicles for non-EU market access (Asia-Pacific, Latin America, Middle East)
- Assessing regulatory feasibility and timeline for multi-jurisdiction distribution rollouts
- Advising on post-Brexit distribution between UK and EU/EEA markets

## Inputs To Gather

- **Fund structure details**: domicile, legal form (SICAV, FCP, unit trust, LP), umbrella vs. standalone, sub-fund count
- **Regulatory classification**: UCITS, EU AIF, non-EU AIF, or unregulated fund; AIFM location and authorization status
- **Target jurisdictions**: ranked list of distribution countries with priority tiers
- **Investor universe**: institutional only, professional investors, retail-eligible, or mixed
- **Distribution model**: direct offering by the manager, third-party distribution agreements, platform placement, or sub-advisory arrangement
- **Existing registrations**: current passported or locally registered markets, pending filings
- **Timeline and budget constraints**: launch dates, regulatory fee tolerance, appetite for local substance requirements

## Workflow

1. **Classify the fund and manager regime**
   - Confirm whether the fund qualifies as UCITS (Directive 2009/65/EC) or falls under AIFMD (Directive 2011/61/EU) [VERIFY current directive amendments]
   - Determine AIFM authorization status — full-scope authorized, sub-threshold, or non-EU AIFM
   - For non-EU funds, assess availability of NPPRs in each target country

2. **Map passporting eligibility per jurisdiction**
   - UCITS passport: verify management company passport vs. fund passport distinction; confirm KIID/KID availability in required languages [VERIFY PRIIPs KID requirements by jurisdiction]
   - AIFMD passport: confirm whether marketing is to professional investors only; check if host-state requires additional local filings beyond the AIFMD notification
   - Identify jurisdictions where passporting is unavailable (non-EU/EEA) and alternative access routes are needed

3. **Evaluate local registration and private placement options**
   - For each non-passportable jurisdiction, determine the available regime:
     - **Reverse solicitation**: document strict conditions and compliance risks; note regulatory trend toward narrowing this exception [VERIFY local regulator guidance]
     - **Local private placement**: identify filing requirements, eligible investor definitions, and ongoing reporting obligations
     - **Local fund wrapper or feeder**: assess whether a locally domiciled feeder (e.g., Singapore VCC, Hong Kong OFC, Cayman feeder) is commercially justified
   - Flag jurisdictions with pre-approval requirements vs. notification-only regimes

4. **Design the distribution architecture**
   - Select optimal structure: single passport notification, parallel local registrations, hub-and-spoke feeder model, or platform-based distribution
   - Address facility agent / local paying agent / representative requirements per jurisdiction [VERIFY country-specific requirements, e.g., Swiss representative and paying agent under FinSA]
   - Plan marketing material localization: language translations, local risk disclosures, regulatory legends
   - Map distributor agreements: assess whether local distribution partners require sub-distribution agreements, MiFID II inducement-compliant fee structures, or local licensing

5. **Build regulatory filing timeline and cost model**
   - Sequence filings by priority tier and interdependencies (e.g., home-state notification must precede host-state marketing)
   - Estimate per-jurisdiction costs: regulatory filing fees, legal counsel, translation, local agent appointments, ongoing annual maintenance
   - Identify jurisdictions with extended review periods or substantive review risk (e.g., certain LATAM regulators, ADGM/DIFC registration processes)

6. **Address ongoing compliance obligations**
   - UCITS: host-state investor notification facilities, NAV publication, local reporting to host NCAs [VERIFY specific host-state requirements]
   - AIFMD: Annex IV reporting to home NCA, AIFMD transparency requirements to investors, leverage reporting
   - Non-EU markets: periodic filings, local tax registrations (e.g., German Investmentsteuergesetz reporting, UK HMRC reporting fund status), withholding tax considerations
   - De-registration procedures for jurisdictions where distribution is discontinued

## Output

Produce a **Global Fund Distribution Report** containing:

- **Executive summary**: recommended distribution structure with rationale
- **Jurisdiction matrix**: table listing each target country with columns for access route (passport / NPPR / local registration / feeder), investor eligibility, filing type, estimated timeline, estimated cost, and local agent requirements
- **Regulatory risk assessment**: flagged jurisdictions with heightened compliance complexity, pending regulatory changes, or enforcement trends
- **Filing sequence plan**: Gantt-style timeline showing filing dependencies and critical path to first distribution in each market
- **Ongoing obligations summary**: annual reporting, filing renewals, and regulatory monitoring commitments per jurisdiction
- **Open items and [VERIFY] flags**: list of jurisdiction-specific points requiring local counsel confirmation

## Quality Checks

- Every jurisdiction entry includes the specific legal basis for the chosen access route (directive article, local statute, or regulator guidance reference)
- Investor eligibility definitions are stated precisely — do not conflate "professional investor" (MiFID II) with "qualified purchaser" (US) or "accredited investor" (Singapore MAS)
- Cost estimates distinguish between one-time setup fees and recurring annual maintenance
- Any reliance on reverse solicitation is flagged with explicit risk warnings and documentation requirements
- Post-Brexit UK/EU distribution is addressed separately with current regulatory status [VERIFY FCA Temporary Marketing Permissions Regime or successor]
- All [VERIFY] markers identify the specific local law, regulation, or regulator guidance that must be confirmed with jurisdiction counsel
