# Program Rules by Institution Type

## Contents

1. Institution type decides the rule set
2. Program components common to every rule
3. Risk assessment as the design input
4. Governance: approval body and the BSA/AML officer
5. Independent testing
6. Customer due diligence and beneficial ownership
7. Rule status as of 2026-10-30

All citations are to 31 C.F.R. Chapter X unless stated. Each rule was read on 2026-10-30; see `references/primary-sources.md` for the URL and method. Re-read the current eCFR text before a program goes to the board.

## 1. Institution type decides the rule set

Identify the institution type from its charter, license, FinCEN registration or SEC/CFTC registration before writing anything. An entity can hold more than one status (a bank holding company with a broker-dealer affiliate; a fintech that is an MSB and a bank's program manager). Each regulated entity needs a program under its own rule.

| Institution type | Program rule | Who approves the program | Independent testing standard | SAR rule and dollar threshold | 60-day "no suspect" extension? | Beneficial ownership rule (1010.230) applies? |
|---|---|---|---|---|---|---|
| Bank, savings association, credit union with a federal functional regulator | 1020.210(a); plus the regulator's rule: OCC 12 C.F.R. 21.21, FDIC 326.8, Federal Reserve 208.63, NCUA 748.2 (each: written, board-approved, noted in the minutes) | Board of directors (21.21(c)(1); 326.8(b)(1); 208.63(b)(1); 748.2(b)(1)) | Bank personnel or an outside party (1020.210(a)(2)(ii); 21.21(d)(2)); FFIEC manual: no regulatory frequency | 1020.320: $5,000 | Yes, 30 more days, never more than 60 from initial detection | Yes (covered financial institution, 1010.605(e)(1)) |
| Bank without a federal functional regulator (private bank, non-federally insured credit union, certain trust companies) | 1020.210(b) | Board or equivalent governing body (1020.210(b)(3)) | Bank personnel or an outside party | 1020.320: $5,000 | Yes | Yes |
| Money services business | 1022.210 | No approval body named in the rule; program must be written | "Independent review" by anyone except the person designated under (d)(2); scope and frequency commensurate with risk (1022.210(d)(4)) | 1022.320: $2,000; $5,000 only where an issuer of money orders or traveler's checks finds the transaction through clearance records (1022.320(a)(3)) | No. 30 calendar days from initial detection (1022.320(b)(3)) | No. MSBs are not "covered financial institutions"; collecting beneficial ownership is a policy election |
| Broker-dealer in securities | 1023.210; FINRA Rule 3310 | Senior management (1023.210; FINRA 3310 in writing) | Personnel or a qualified outside party; FINRA 3310(c) annual on a calendar-year basis (every two years for firms with no customer accounts); 3310.01(c) bars the person performing the functions tested, the AML compliance person, and anyone reporting to either | 1023.320: $5,000 | Yes | Yes |
| Futures commission merchant, introducing broker in commodities | 1026.210; SRO rule | Senior management | Personnel or a qualified outside party | 1026.320: $5,000 | Yes | Yes |
| Mutual fund | 1024.210 | Board of directors or trustees, in writing | Personnel or a qualified outside party | 1024.320: $5,000 | Yes | Yes |
| Insurance company (covered products) | 1025.210: program based on its assessment of risks of covered products; integrates agents and brokers | Senior management | Third party or any officer or employee other than the designated compliance officer; includes testing agents and brokers (1025.210(b)(4)) | 1025.320: $5,000 | Yes | No |
| Loan or finance company (including residential mortgage lenders and originators) | 1029.210: based on its risk assessment; integrates agents and brokers | Senior management | Third party or any officer or employee other than the designated compliance officer (1029.210(b)(4)) | 1029.320: $5,000 | Yes | No |
| Registered investment adviser and exempt reporting adviser | 1032.210 (published 89 FR 72156) | Board or trustees, or sole proprietor, general partner or similar (1032.210(a)(2)) | Per 1032.210(b) | 1032.320: $5,000; 30 days, 60 if no suspect | Yes | Not under current text |
| Casinos, card clubs, dealers in precious metals, credit card system operators, housing GSEs | 1021.210, 1027.210, 1028.210, 1030.210 | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | `[VERIFY]` | No |

Investment advisers: the rule's effective date is January 1, 2028, after FinCEN's final rule of December 31, 2025 (91 FR 36, Jan. 2, 2026). Before that date an adviser has no BSA program obligation under Part 1032; a program drafted now is a readiness program and says so. FinCEN said it intends to revisit the rule's substance, so mark any Part 1032 provision relied on as subject to change.

MSBs also register with FinCEN and keep an agent list under 1022.380; the registration, renewal, agent-list and re-registration clocks are in `references/sar-ctr-and-sanctions-rules.md`, section 1. Rules not in the table (state MSB licensing law, state BSA examination statutes, payment stablecoin issuer rules proposed April 2026) are `[VERIFY]` and are named as open items when the institution may be subject to them.

## 2. Program components common to every rule

31 U.S.C. 5318(h)(1) requires, at a minimum: internal policies, procedures and controls; a designated compliance officer; an ongoing employee training program; and an independent audit function to test the program. 5318(h)(2)(B)(iv) states programs should be reasonably designed and risk-based, directing more attention and resources to higher-risk customers and activities. 5318(h)(5) requires that the duty to establish, maintain and enforce the program be performed by persons in the United States accessible to Treasury and the functional regulator.

Banks, broker-dealers and FCMs add a fifth element: risk-based procedures for ongoing customer due diligence, covering the nature and purpose of customer relationships (customer risk profile) and ongoing monitoring to report suspicious transactions and, on a risk basis, maintain and update customer information, including beneficial ownership (1020.210(a)(2)(v); 1023.210(b)(5); 1026.210(b)(5)).

Banks, broker-dealers and FCMs must also comply with 1010.610 (correspondent accounts for foreign financial institutions) and 1010.620 (private banking accounts). If the institution offers neither, the program says so and requires a program update and approval before any such account is opened.

## 3. Risk assessment as the design input

No current program rule for banks uses the words "risk assessment," but the rules for insurance companies (1025.210(b)(1)) and loan or finance companies (1029.210(b)(1)) base controls on the company's own risk assessment, the MSB rule requires a program commensurate with location, size, and nature and volume of services (1022.210(b)), and the FFIEC manual has examiners check that internal controls incorporate the bank's BSA/AML risk assessment. The April 2026 proposed rule would make a documented risk assessment process an express element (see section 7).

Design test for every program section:

| Program section | Risk assessment row it answers | Inherent rating | Control strength chosen | Residual rating | Why this control fits |
|---|---|---|---|---|---|

- A section that answers no risk row is either a legal minimum (state the rule) or template residue (remove it or mark it "not applicable to this institution," with the basis).
- A high inherent row with no section is a Critical gap.
- Review cycles, monitoring thresholds and EDD triggers vary by risk tier; a single cycle for every customer is a gap unless the risk assessment supports it.
- Review the AML/CFT National Priorities (June 30, 2021: corruption; cybercrime; terrorist financing; fraud; transnational criminal organizations; drug trafficking organizations; human trafficking and smuggling; proliferation financing) against the institution's products and record the result. No update had issued as of the August 2026 secondary report read; re-check before relying on the 2021 list.
- If the risk assessment is missing or predates a new product, channel or acquisition, route the update to bsa-risk-assessment and list it as a Critical item.

## 4. Governance: approval body and the BSA/AML officer

Approval body depends on type (table in section 1). Use the body the rule names. For federally regulated banks and credit unions the four regulator rules name the board of directors and require the approval to be noted in the minutes; whether a board committee may approve on the board's behalf is `[VERIFY]` for the regulator.

The BSA/AML officer: the rules require designation of an individual responsible for coordinating and monitoring day-to-day compliance (1020.210(a)(2)(iii); 1022.210(d)(2); 1023.210(b)(3)). For banks, the FFIEC manual says appointment alone does not meet the requirement; the board must ensure the officer has appropriate authority, independence and access to resources, and the officer reports regularly to the board, including SAR filing notifications. Indicators the manual lists:

| Test | Evidence to request | Gap if |
|---|---|---|
| Authority | Charter or board resolution; input sought on new products and system changes | Officer has no say on new products or monitoring changes |
| Independence | Reporting line to the board or a committee; compensation not tied to business-line production | Reports to a revenue line head; business line can override SAR decisions |
| Resources | Staffing model, budget line, systems | Part-time with no staff and no budget against a high-risk profile |
| Competence | Knowledge of BSA and of the institution's risk profile | No BSA experience and no training plan |
| Location | U.S.-based (5318(h)(5)) | Officer located outside the U.S. with no U.S. person performing the duty |

For broker-dealers, FINRA 3310(d) also requires the AML compliance person to be an associated person and identified to FINRA, with prompt notice of changes.

## 5. Independent testing

| Institution | Who may test | Who may not test | Frequency |
|---|---|---|---|
| Bank (OCC, Fed, FDIC, NCUA) | Internal audit, outside auditors, consultants, or qualified staff not involved in the function tested (FFIEC manual) | Persons involved in the function tested; outside parties also doing BSA training or writing policies for the bank (FFIEC manual) | No regulatory frequency; risk-based (FFIEC cites 12 to 18 months as an example) |
| MSB | Any officer or employee, or an outside party | The person designated under 1022.210(d)(2) | Commensurate with risk |
| Insurance company; loan or finance company | Third party or any officer or employee | The designated compliance officer (1025.210(b)(4); 1029.210(b)(4)) | Commensurate with risk of products |
| Broker-dealer | Personnel or qualified outside party with BSA working knowledge | Person performing the functions tested; the AML compliance person; anyone reporting to either (FINRA 3310.01(c)) | Annual, calendar-year basis (two years if no customer accounts) |

Testers report to the board or a committee composed primarily of outside directors (FFIEC manual for banks). The April 2026 proposal would treat the AML/CFT officer and anyone reporting directly to the officer as generally not independent; that is proposed, not current, for banks, but it is the current rule for broker-dealers under FINRA 3310.01(c).

## 6. Customer due diligence and beneficial ownership

**Who is covered.** 1010.230 applies to covered financial institutions as defined in 1010.605(e)(1): banks, registered broker-dealers, FCMs and introducing brokers, and mutual funds. It does not apply to MSBs, insurance companies or loan or finance companies.

**Who is a beneficial owner (1010.230(d)).**
- Ownership prong: each individual, if any, who directly or indirectly owns 25 percent or more of the equity interests. "25 percent or more" includes exactly 25 percent. Look through entity owners; an individual owning a holding company outright owns indirectly what the holding company owns. Up to four individuals.
- Control prong: one individual with significant responsibility to control, manage or direct the entity (executive officer or senior manager, or one who regularly performs similar functions). Always required, even when ownership-prong owners are identified; it may be the same person.
- Trust owning 25 percent or more: the trustee is the beneficial owner for the ownership prong (1010.230(d)(3)).
- Excluded legal entity customers (1010.230(e)(2)) and control-prong-only customers (pooled vehicles advised by non-excluded institutions; nonprofits) (1010.230(e)(3)).

**Timing.** Identify at account opening by certification (Appendix A form) or equivalent; verify by risk-based procedures including at least the CIP elements for individuals. Since FinCEN's exceptive relief order FIN-2026-R001 (February 13, 2026), identification and verification are required only (1) when a legal entity customer first opens an account with the institution, (2) when the institution knows facts that would reasonably call into question the reliability of beneficial ownership information previously obtained, and (3) as the institution's risk-based ongoing CDD procedures require. Repeating it at every new account is now a policy election. Where the institution holds facts that conflict with the certification on file (a new operating agreement, a public filing, an ownership change), relief does not apply and the owners are re-identified and verified.

**Corporate Transparency Act changes.** The March 26, 2025 interim final rule exempted U.S.-formed entities from beneficial ownership information (BOI) reporting to FinCEN, and the final rule effective August 14, 2026 (91 FR 52508) made the exemptions permanent and extended them to U.S. person company applicants. Neither changed 1010.230. In the August 2026 final rule FinCEN states that the reporting rule and the CDD rule serve different purposes under different authorities, that CDD compliance remains important, and that FinCEN remains legally required to revise the CDD rule and intends to address it. A program that drops beneficial ownership collection for domestic entities because they no longer report to FinCEN is wrong. Do not build verification around the FinCEN BOI database.

**Records (1010.230(i)).** Identification records (including the certification): five years after the account is closed. Verification records (documents relied on, non-documentary methods, discrepancy resolution): five years after the record is made.

## 7. Rule status as of 2026-10-30

| Item | Status | Effect on a program drafted today |
|---|---|---|
| FinCEN AML/CFT program NPRM, July 3, 2024 (89 FR 55428) | Withdrawn and superseded by the April 2026 proposal | Do not cite as pending |
| FinCEN AML/CFT program NPRM, April 10, 2026 (91 FR 18704, RIN 1506-AB72) | Proposed; comments closed June 9, 2026; the Federal Register's 2026 FinCEN index as of October 30, 2026 lists it only as a proposed rule; eCFR 1020.210 still shows the 2020 text; proposed effective date 12 months after issuance of a final rule | Not in effect. Its elements (risk assessment processes that incorporate the National Priorities and are updated on significant change; U.S.-located officer; establishment versus implementation framework) may be adopted as design choices and labeled "proposed" |
| OCC, FDIC and NCUA joint proposal (April 10, 2026, concurrent with FinCEN's) and Federal Reserve proposal (published July 9, 2026, comments to September 8, 2026) | Proposed | Same |
| Investment adviser rule (Part 1032) | Final; effective January 1, 2028 | Readiness only before that date |
| FinCEN exceptive relief FIN-2026-R001 (CDD timing) | In force since February 13, 2026 | Optional relief from per-account re-identification |
| CTA BOI reporting final rule (91 FR 52508) | Effective August 14, 2026 | No change to CDD rule |
| Interagency SAR FAQs, October 9, 2025 | Guidance in force | See `references/sar-ctr-and-sanctions-rules.md`, sections 1 to 3 |

Before the program goes to the board, check the eCFR and the FinCEN news page for any final program rule, CDD rule revision, or change to the IA rule; record what was checked and the date.
