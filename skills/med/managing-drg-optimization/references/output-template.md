# Output Template

Produce the header and sections below in order. Every code carries its source locator; every rule carries its authority and version. Put detail in tables and keep the narrative short.

## Contents

1. Header
2. Section 1. Determination summary
3. Section 2. Source register and code ledger
4. Section 3. Principal diagnosis analysis
5. Section 4. Secondary diagnoses, severity and POA
6. Section 5. Grouping result
7. Section 6. Query candidates and clinical validation
8. Section 7. Reconciliation table
9. Section 8. Declined requests
10. Section 9. Hand-offs
11. Section 10. Open items and `[VERIFY]` list

## Header

- Case identifier (de-identified), admission date, inpatient order date and time, discharge date, discharge disposition.
- Payer and payment basis as stated (Medicare FFS on MS-DRG; Medicare Advantage or commercial per contract, `[VERIFY]` unless the contract was read).
- Versions applied: "ICD-10 MS-DRG Grouper V44 (discharges on or after 10/01/2026)"; "ICD-10-CM Official Guidelines FY 2027"; "ACDIS/AHIMA query practice brief, 2026 update".
- Review type: pre-bill, retrospective, CDI second-level, or record review for counsel.
- Preparer note: "Draft for coder, CDI and compliance review."

## 1. Determination summary

| Item | Submitted or draft | Validated | Basis in one line | Blocking open items |
|---|---|---|---|---|
| Principal diagnosis | | | | |
| MS-DRG | | Provisional pending <facts> if any query is open | | |
| Direction of change | Up / Down / None | | | |

## 2. Source register and code ledger

| Source | Type | Date range | Status | Note |
|---|---|---|---|---|
| | H&P, progress note, consult, discharge summary, operative report, ED note, nursing, dietitian, social work, lab, imaging, MAR, coder worksheet, grouper output | | Reviewed / Not relevant / Unreadable after attempt / Still needed | |

Code ledger, one row per code on the claim or proposed:

| Code | Description | Role (PDX / SDX) | Provider statement and locator | Section III basis | POA | Severity in V44 (MCC / CC / NonCC) | Excluded with PDX? | Outcome |
|---|---|---|---|---|---|---|---|---|

Outcome labels, verbatim: Supported; Not supported, remove; Query candidate; Excluded as CC/MCC (still coded); Declined request.

## 3. Principal diagnosis analysis

| Candidate | Reason for admission evidence | Established after study? | Guideline applied (II.A-II.K) | Selected? |
|---|---|---|---|---|

State why each rejected candidate fails. Never cite relative weight.

## 4. Secondary diagnoses, severity and POA

For each CC or MCC: the provider statement, the Section III basis, the V44 severity, the Appendix C PDX collection checked and the result, the POA indicator and source, and whether a HAC category applies.

## 5. Grouping result

```
Grouper version:            V44 (discharge <date>)
MDC / family:               <MDC> / <family name>, split <MCC-CC-none | MCC only | MV, then MCC>
Principal diagnosis:        <code> (<locator>)
Severity drivers counted:   <code: MCC or CC, not excluded>
Severity codes not counted: <code: excluded with PDX collection nnnn | HAC with POA N or U | unsupported>
MS-DRG:                     <number and title>
Draft claim MS-DRG:         <number>   change: <up | down | none>
Relative weight:            <from corrected Table 5, or [VERIFY]>
Transfer status:            <full DRG | acute transfer | post-acute transfer per diem [VERIFY] | n/a>
```

## 6. Query candidates and clinical validation

| # | Issue | Indicators with source | Format | Options | To whom | Possible effect (preparer only, not in query) |
|---|---|---|---|---|---|---|

Each query text follows the template in `references/query-compliance.md`, Section 5. List clinical validation candidates, which may lower the DRG, beside capture candidates.

## 7. Reconciliation table

| # | Fact or rule | Source A says | Source B says | Controlling source and why | Effect on DRG |
|---|---|---|---|---|---|

Typical rows: worksheet CC list against V44; coder's POA against the ED note; consultant against attending; payer letter against the Official Guidelines.

## 8. Declined requests

| Request | Declined part | Reason and authority | Compliant alternative offered |
|---|---|---|---|

## 9. Hand-offs

| To skill | Why | What is passed | What this review did not do |
|---|---|---|---|
| managing-cdi-programs | Query issuance and tracking | Query candidates | Did not send queries |
| managing-coding-denials | Payer denial or clinical validation dispute | Validated coding and indicators | Did not draft an appeal |
| conducting-false-claims-analysis | Pattern of unsupported codes or one-way query policy | Findings and policy text | Did not assess FCA exposure |
| managing-observation-stays | Inpatient status question | Order times and status notes | Did not decide status |

## 10. Open items and `[VERIFY]` list

| # | Open item | Gap class (unknown fact / source conflict / unverified external lookup / policy election) | Owner | Next action | Changes the DRG? |
|---|---|---|---|---|---|

Then each `[VERIFY]` relied on, with what would settle it.

Close with: "Draft for coder, CDI and compliance review. Not a final code set and not a query sent to a provider."
