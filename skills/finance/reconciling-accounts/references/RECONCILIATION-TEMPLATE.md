# Reconciliation Template — Standardized Format

Use this template for all account reconciliation outputs. Adapt sections as needed by reconciliation type, but maintain the structure and required fields.

---

## 1. Reconciliation Header

```
═══════════════════════════════════════════════════════════════
ACCOUNT RECONCILIATION
═══════════════════════════════════════════════════════════════
Account Number:     _______________
Account Name:       _______________
Entity / Co. Code:  _______________
Period End Date:    _______________
Currency:           _______________
Recon Type:         [ ] Bank  [ ] Intercompany  [ ] Sub-ledger to GL  [ ] Balance Sheet
Prepared by:        _______________    Date: _______________
Reviewed by:        _______________    Date: _______________
═══════════════════════════════════════════════════════════════
```

---

## 2. Balance Comparison

```
                                          Source A (GL)    Source B (Support)
                                          ─────────────    ──────────────────
Ending Balance per Source                 $____________    $____________
```

---

## 3. Reconciling Items Table

### Items in Supporting Source, Not in GL (add to GL to reconcile)

| # | Date | Reference | Description | Category | Amount | Days Out | Aging Bucket | Action / Resolution | Owner | Due Date |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | YYYY-MM-DD | ref# | description | TIMING / ERR-B / MISSING | $X,XXX.XX | NN | Current / Aged / Stale | action | name | YYYY-MM-DD |
| 2 | | | | | | | | | | |
| | | | **Subtotal** | | **$X,XXX.XX** | | | | | |

### Items in GL, Not in Supporting Source (add to supporting source to reconcile)

| # | Date | Reference | Description | Category | Amount | Days Out | Aging Bucket | Action / Resolution | Owner | Due Date |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | YYYY-MM-DD | ref# | description | TIMING / ERR-A / CUTOFF | $X,XXX.XX | NN | Current / Aged / Stale | action | name | YYYY-MM-DD |
| 2 | | | | | | | | | | |
| | | | **Subtotal** | | **$X,XXX.XX** | | | | | |

### Category Codes

| Code | Meaning |
|---|---|
| `TIMING` | Timing difference — expected to clear in subsequent period |
| `ERR-A` | Error in Source A (GL) — requires correcting journal entry |
| `ERR-B` | Error in Source B (supporting source) — requires correction at source |
| `MISSING` | Entry exists in one source with no corresponding entry in the other |
| `CUTOFF` | Transaction recorded in the wrong period |
| `FX` | Foreign exchange translation difference |
| `WOFF` | Immaterial difference — approved for write-off per materiality threshold |

### Aging Buckets

| Bucket | Days Outstanding | Required Action |
|---|---|---|
| Current | 0–30 | Monitor; expected to clear |
| Aged | 31–90 | Investigate and document reason |
| Stale | >90 | Mandatory investigation; escalate to controller |

---

## 4. Reconciliation Proof

```
GL Balance (per books)                                    $____________

  Add: Items in supporting source, not yet in GL
    [list items or reference table above]
    Subtotal                                              $____________

  Less: Items in GL, not yet in supporting source
    [list items or reference table above]
    Subtotal                                             ($____________)
                                                          ────────────
Adjusted GL Balance                                       $____________


Supporting Source Balance                                 $____________

  Add: Items in GL, not yet in supporting source
    [list items or reference table above]
    Subtotal                                              $____________

  Less: Items in supporting source, not yet in GL
    [list items or reference table above]
    Subtotal                                             ($____________)
                                                          ────────────
Adjusted Supporting Source Balance                         $____________


DIFFERENCE                                                $       0.00
                                                          ════════════
```

If the difference is not $0.00, the reconciliation is **incomplete**. Do not submit.

---

## 5. Summary Metrics

| Metric | Value |
|---|---|
| GL Balance | $ |
| Supporting Source Balance | $ |
| Gross Reconciling Items (absolute sum) | $ |
| Net Reconciling Difference (must be $0.00) | $ |
| Total Count of Reconciling Items | |
| — Current (0–30 days) | |
| — Aged (31–90 days) | |
| — Stale (>90 days) | |
| Largest Single Reconciling Item | $ |
| Materiality Threshold Applied | $ |
| Items Exceeding Materiality | |
| Correcting JEs Required | |
| JEs Posted (ref #s) | |
| JEs Pending | |

---

## 6. Prior Period Carryforward Tracker

Track items that carried over from the prior reconciliation. Every item from last period must appear here as either cleared or still open (re-aged).

| # | Original Date | Reference | Description | Category | Amount | Prior Aging | Current Status | Resolution |
|---|---|---|---|---|---|---|---|---|
| 1 | YYYY-MM-DD | ref# | description | code | $X,XXX.XX | Aged | Cleared / Still Open | how resolved or current action |
| 2 | | | | | | | | |

---

## 7. Sign-Off

```
Preparer Certification:
I confirm that this reconciliation is complete, all reconciling items are
identified and categorized, and proposed resolutions are documented.

Preparer: _______________    Signature: _______________    Date: ___________


Reviewer Certification:
I have reviewed this reconciliation for completeness, accuracy, and
appropriateness of reconciling item categorization and resolution.

Reviewer: _______________    Signature: _______________    Date: ___________
```

---

## Notes

- All amounts should use consistent sign convention: positive = debit / asset increase; negative = credit / asset decrease.
- Reference numbers should match the source document (check #, wire ref, invoice #, JE #).
- For bank reconciliations: attach or reference the bank statement. For IC: attach counterparty confirmation.
- This template satisfies SOX evidence requirements for key reconciliation controls when fully completed and signed.
