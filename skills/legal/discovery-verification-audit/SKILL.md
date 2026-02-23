---
name: discovery-verification-audit
description: Produces an attorney-grade audit memorandum assessing whether written discovery responses (interrogatories, RFPs, RFAs) are legally binding and timely. Verifies signature authority, party verification formalities including under-penalty-of-perjury compliance, proof of service sufficiency, and deadline computation with mailbox-rule extensions across federal and state forums. Embeds adversarial risk analysis, defect categorization (fatal vs. technical), and cure strategy. Use when auditing outgoing discovery responses pre-service, analyzing opponent responses for defects, preparing meet-and-confer letters, or assessing waiver risk and motion-to-compel deadlines.
tags:
  - analysis
  - drafting
  - litigation
  - memo
---

# Discovery Verification and Proof of Service Audit

Produces a structured audit memorandum confirming whether written discovery responses are properly verified, served, and timely under applicable federal or state procedural rules.

## Prerequisites

1. **Discovery set and responses** — propounding requests and full response package as served, including all signature/verification pages and attachments
2. **Proof(s) of service** — for both the requests and the responses; ECF notices, certified mail receipts, courier confirmations, or email headers if e-service is authorized
3. **Forum identification** — jurisdiction (state + county or federal district), governing procedural rules (FRCP, CCP, etc.), and any applicable local rules or standing orders
4. **Deadline modifiers** — stipulations, court orders, or extensions modifying response deadlines
5. **Party identity** — responding party type (individual, corporation, LLC, government entity), signer's name and title, and basis of authority
6. **Master service list** — all parties and counsel of record to verify service completeness

> If the verification page(s), proof of service, or any deadline-modifying order is missing, request those documents before reaching conclusions.

## Output Structure

### Audit Memorandum Sections

**1. Scope and Posture**
- Discovery instruments audited (interrogatories / RFPs / RFAs / supplemental / amended responses)
- Audit posture: outgoing (pre-service QA) or incoming (opponent defect analysis)
- Governing rule set confirmed; any inferences flagged for attorney confirmation

---

**2. Verification Sufficiency**

| Element | Required | Present | Notes |
|---|---|---|---|
| Affirmation responses are true and correct | ✓ | | |
| "Under penalty of perjury" language | ✓ | | |
| Correct jurisdictional reference in perjury clause | ✓ | | |
| Signed by party (not counsel, unless permitted) | ✓ | | |
| Date of signing | ✓ | | |
| Verification references specific discovery set | ✓ | | |
| Verification date ≤ proof-of-service date | ✓ | | |

**Perjury clause standards:**
- **Federal (28 U.S.C. § 1746):** "I declare under penalty of perjury under the laws of the United States of America that the foregoing is true and correct."
- **California (CCP § 2015.5):** Must state "under the laws of the State of California"; must include city and state of signing; if signed outside California, must specify CA law or be notarized.
- **Other forums:** Web-verify perjury statute language; flag `[VERIFY]` if unconfirmed.

---

**3. Signature Authority and Capacity**

| Party Type | Required Signer | Attorney Verification Permitted? |
|---|---|---|
| Individual | The individual party | Generally no |
| Corporation / LLC | Officer, managing agent, or authorized representative with knowledge | No (CA: only if party absent from county — but triggers privilege risk) |
| Partnership | General partner or authorized agent | No |
| Government entity | Authorized official | Forum-specific — confirm |

> Attorney verification where party verification is required = **fatal defect**. In many forums, this is treated identically to no verification. If an attorney verifies where a party must, flag privilege waiver risk as to sources.

---

**4. Proof of Service Sufficiency**

Required elements:
- [ ] Date of service stated
- [ ] Method of service identified (must be an authorized method under applicable rules)
- [ ] Name and address / e-service address of each recipient
- [ ] Server's identity and signature (with perjury declaration where required)
- [ ] All parties on master service list included

**Service method authorization check:**
- Email/electronic service requires written consent, ECF registration, stipulation, or court order — flag "served via email" without documented authorization as potentially invalid service
- Discrepancy between stated address and current service list = flag
- Responses served but verification mailed separately = flag; determine operative service date

---

**5. Deadline Computation**

Show each step explicitly:

```
Trigger date (day of service, excluded):  [Date]
Baseline response period:                 [30 days — FRCP 33/34/36; state-specific]
End of baseline period:                   [Date]
Weekend/holiday rollover:                 [Next business day if Sat/Sun/holiday]
Service method extension:                 [See table]
Final deadline:                           [Date]
```

**Mailbox Rule Extensions by Forum and Method:**

| Forum | Mail | Overnight | Electronic / ECF | Personal |
|---|---|---|---|---|
| Federal (FRCP 6(d)) | +3 calendar days | +3 calendar days [VERIFY] | **None** (eliminated by 2016 amendment) | None |
| California (CCP § 1013) | +5 cal. days (in-state) / +10 cal. days (out-of-state) | +2 cal. days | +2 **court** days (CCP § 1010.6) | None |
| New York [VERIFY] | +5 cal. days | — | — | None |
| Other jurisdictions | Web-verify statute; flag `[VERIFY]` if unconfirmed | | | |

> **CA critical distinction:** Electronic service adds 2 **court days** (not calendar days) — a long weekend shifts the deadline further. Confusing court days and calendar days is a frequent computation error.

---

**6. Defect Inventory and Risk Assessment**

| Defect | Severity | Consequence | Cure |
|---|---|---|---|
| No verification where party verification required | **Fatal** | Response = legal nullity; objections may be waived | Serve corrected party verification immediately |
| Attorney verification where party required | **Fatal** | Treated as unverified; privilege waiver risk | Party must re-execute |
| Missing "penalty of perjury" language | **Fatal** | Declaration ineffective | New verification |
| Wrong jurisdictional reference in perjury clause | **Fatal** | Declaration ineffective | New verification |
| Verification dated after proof-of-service date | **High** | Suggests responses served before verified | Investigate; may require re-service |
| "Floating" verification not identifying discovery set | **High** | Opponent may argue it doesn't cover served responses | Amended verification with specific reference |
| Unauthorized service method (e.g., email without consent) | **High** | Operative service date may be disputed or void | Confirm authorization; re-serve if needed |
| Not all parties served | **High** | Absent party not bound; motion deadlines may not run | Re-serve; reconcile against master service list |
| Wrong address on proof of service | **Technical** | Arguable invalid service | Corrected proof; confirm actual receipt |
| Missing date on verification | **Technical** | Curable | Serve corrected verification |

---

**7. Adversarial Risk and Strategic Notes**
- Identify whether defects favor the auditing party (opponent's responses) or expose the client (client's responses)
- **CA motion-to-compel clock: CCP § 2030.300 — 45-day deadline is jurisdictional.** Filing on day 46 permanently forfeits the right to compel that discovery. Connect all computed dates to this risk explicitly.
- Unverified interrogatory responses in CA = no response at all for purposes of the motion-to-compel clock (*Appleton v. Superior Court* (1988) 206 Cal.App.3d 632)
- FRCP 26(g) counsel signature certification is separate from FRCP 33(b)(3) party verification — both layers must be present for federal interrogatory compliance
- Document all service evidence now: ECF notices, email headers, postmarks — this record determines timeliness disputes later

---

**8. Recommended Next Steps (attorney decision)**
- [ ] Serve corrected/amended verification page (outgoing defect)
- [ ] Send meet-and-confer letter demanding cure by [date] — required before filing FRCP 37(a)(1) / CCP § 2030.300 motion
- [ ] Obtain stipulation confirming operative service date / extending deadline
- [ ] Calendar motion-to-compel deadline based on corrected service date
- [ ] Preserve proof-of-service evidence in case file

## Guidelines

- **No hallucinated citations:** Every jurisdiction-specific extension day count must be web-verified against the current statutory text or flagged `[VERIFY]`
- **Document every factual assertion:** Tie each conclusion to a specific exhibit, Bates number, or PDF page — do not assume what "must have happened"
- **Distinguish defect severity:** Fatal (response = nullity) vs. technical (curable) — never declare waiver or sanctions automatic without confirming the forum's standard
- **Attorney verification trap:** Flag any instance where counsel signed an instrument requiring party execution — the single most frequent fatal defect in practice
- **Do not recommend filing motions or threatening sanctions as a definitive step** — present as options for attorney evaluation
- **Mandatory attorney review before use:** Supervising attorney must personally verify signatures and the final computed deadline before calendaring, client communications, or court filings
- **Privilege and confidentiality:** Minimize quoting substantive discovery content; reference by paragraph/page number; flag if responses contain HIPAA-protected, PII, or protective-order-designated material
- **International service:** If any party is outside the U.S., flag Hague Service Convention applicability and require separate attorney review — this audit is not sufficient for cross-border service analysis
