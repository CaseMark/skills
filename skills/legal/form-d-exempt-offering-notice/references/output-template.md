# Output Template

Produce the six sections in this order. Keep sentences plain; put detail in tables. Every date shows its weekday.

## Header

- Matter or offering name, issuer(s), date prepared, preparer note: "Draft for attorney review."
- Today's date used for deadline comparison.
- A short document inventory (document, type, date, rank in the source hierarchy) and one paragraph classifying the structure (issuers, vehicles, exemption and exclusion, existing or new offering).

Put the EDGAR access plan (CIK status for each issuer, Form ID needs, delegation to the firm) in Section 1 beside the Form ID rows.

## 1. Filing determination

A table with one row per required filing.

| Filing | Issuer | Trigger | Date of first sale (basis) | Due date | Status |
|---|---|---|---|---|---|
| New notice / Amendment / Form ID | name | what requires it | date and the contract clause relied on | date | on time / due in N days / past due |

Under the table, for each new notice, the fixed computation:

```
Date of first sale: <date> (<weekday>)
Raw day 15:         <date> (<weekday>)
Due date:           <date> (<weekday>)   [rolled because <reason> | not rolled]
```

For each amendment, state which trigger applies (error, change, annual), the figures and percentages behind any 10 percent test, the annual anniversary date, and the reset date if a change-driven amendment is filed first. State which issuers need a Form ID.

## 2. Blocking issues and client questions

Ranked by severity, most severe first. A table:

| # | Severity | Issue | Why it blocks | Source citation | Who can resolve |
|---|---|---|---|---|---|

Severity levels: Critical (deadline, CIK, exemption or exclusion in doubt, qualification conflict); High (value conflict that changes a filing outcome); Medium (value conflict with a clear controlling source); Low (clean-up). A missing CIK for any issuer is Critical.

## 3. Item-by-item draft

One table per filing, using the form's item numbers and field labels.

| Item | Value | Source | Confidence | Flag or clarification text |
|---|---|---|---|---|
| 1. Issuer's Identity: Name of Issuer | | document, section | High / Medium / Low | |

Use one row per field or per repeating entry (each related person, each compensation recipient). Show clarification text only where the form has a clarification field (Items 3, 10, 13, 15, 16), and show its character count. Mark missing values MISSING and say what is needed. Include the signature block row with the signer, capacity and authority.

## 4. Judgment calls

For each: the question, the options, the recommended choice and the reason. Include every judgment call on an item that has no clarification field. Typical entries: date of first sale where the contract is ambiguous; one filing or separate filings; Regulation S reporting; Item 13 cap presentation; Item 15 placement fees; Item 11 waiver; entity type for a non-U.S. vehicle; related persons beyond the form's examples.

## 5. Hand-offs

- `blue-sky-filings`: state notice filings needed, each state and the investors there, and any placement agent state registration gap with the specific state and investor.
- `bad-actor-disqualification-review`: each new covered person, each "Yes" answer, each missing or unsigned questionnaire, each stale or expired agent certification, with the document and date.

## 6. Assumptions, open items and `[VERIFY]` list

- Assumptions made and what changes if each is wrong.
- Documents still needed.
- Each `[VERIFY]` statement with what would settle it.

Close with: "Draft for attorney review. This is not a filing-ready submission."
