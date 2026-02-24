---
name: certificate-of-service
description: Drafts certificates of service and proofs of service for court filings. Generates properly formatted service certificates that comply with FRCP Rule 5 and state equivalents, supporting electronic service (ECF/e-service), U.S. mail, hand delivery, and overnight courier methods. Covers both federal and state court requirements.
tags:
  - litigation
  - pleading
  - drafting
---

# Certificate of Service

Draft a certificate of service (also called "proof of service") to accompany any court filing. The certificate attests that copies of the filing were served on all parties or their counsel.

## When to Use

- Accompanying any motion, brief, response, or notice filed with a court
- Serving initial pleadings (complaint, summons) on defendants
- Serving discovery requests or responses on opposing counsel
- Filing any document that requires proof of delivery to other parties

## Output Structure

```
CERTIFICATE OF SERVICE

I hereby certify that on [DATE], I served a true and correct copy of the
foregoing [DOCUMENT TITLE] on the following by [SERVICE METHOD]:

[PARTY/COUNSEL LIST with addresses]

Dated: [DATE]

____________________________
[ATTORNEY NAME]
[BAR NUMBER]
[FIRM NAME]
[ADDRESS]
[PHONE]
[EMAIL]
```

## Service Methods

Select the appropriate method based on court rules and party agreement:

| Method | Language | When to Use |
|--------|----------|-------------|
| **ECF/E-filing** | "via the Court's CM/ECF system, which will send notification to all registered counsel of record" | Federal courts and most state e-filing systems |
| **Email** | "via electronic mail to the email address(es) listed below" | When parties have consented to email service per FRCP 5(b)(2)(E) |
| **U.S. Mail** | "by placing a true and correct copy in the United States mail, first-class postage prepaid, addressed to" | Default fallback; adds 3 days to response deadlines under FRCP 6(d) |
| **Hand Delivery** | "by hand delivery to the office of" | Same-day service required or local practice |
| **Overnight Courier** | "via overnight courier service (e.g., FedEx, UPS) to" | Time-sensitive filings where mail is too slow |

## Key Rules

- **FRCP 5(b)**: Governs service methods in federal court. Electronic service via CM/ECF is complete upon transmission.
- **FRCP 6(d)**: Adds 3 calendar days to response deadlines when service is by mail, leaving with clerk, or other means consented to under Rule 5(b)(2)(F).
- **State variations**: Many states mirror FRCP 5 but check local rules. California uses CCP 1013 (mail) and CCP 1010.6 (electronic). New York uses CPLR 2103.
- **Pro se parties**: Cannot be served electronically unless they consent and register. Always serve by mail or hand delivery.
- **Multiple methods**: If serving different parties by different methods, list each party under the applicable method heading.

## Instructions

1. Ask the user for:
   - The document being served (title of the filing)
   - The court and case caption
   - The service method (or determine from court type)
   - Names and addresses of all parties/counsel to be served
   - The attorney signing the certificate

2. For **federal court filings** where all counsel are registered on CM/ECF, use the short-form ECF certificate — no individual addresses needed.

3. For **mixed service** (some ECF, some mail), separate the certificate into sections by method.

4. Include the attorney's bar number, firm name, and contact information in the signature block.

5. Match the date of service to the date of filing unless the user specifies otherwise.

## Examples

### Federal Court — ECF Only

```
CERTIFICATE OF SERVICE

I hereby certify that on February 20, 2025, I electronically filed the
foregoing DEFENDANT'S MOTION TO DISMISS with the Clerk of Court using the
CM/ECF system, which will send notification of such filing to all counsel
of record registered in this case.

Dated: February 20, 2025

/s/ Jane Smith
Jane Smith (Bar No. 12345)
Smith & Associates LLP
100 Main Street, Suite 400
Chicago, IL 60601
(312) 555-0100
jsmith@smithlaw.com
```

### State Court — Multiple Methods

```
CERTIFICATE OF SERVICE

I hereby certify that on February 20, 2025, I served a true and correct
copy of the foregoing PLAINTIFF'S RESPONSE TO INTERROGATORIES on the
following:

Via U.S. Mail, First-Class Postage Prepaid:
  John Doe, Esq.
  Doe Law Group
  200 Oak Avenue
  Los Angeles, CA 90001

Via Electronic Mail:
  Sarah Lee, Esq. (slee@leefirm.com)
  Lee & Partners
  300 Pine Street
  San Francisco, CA 94102

Dated: February 20, 2025

____________________________
Robert Johnson (SBN 67890)
Johnson Legal PC
500 Elm Boulevard
Sacramento, CA 95814
(916) 555-0200
rjohnson@johnsonlegal.com
```

## Troubleshooting

| Issue | Resolution |
|-------|------------|
| Unsure if opposing counsel is on ECF | Check the court's CM/ECF system or PACER for the case docket. If no appearance filed electronically, serve by mail. |
| Pro se party without address | Check the court docket for the party's address of record. If none, note "last known address" in the certificate. |
| Service on a government entity | Federal agencies may require service on the U.S. Attorney under FRCP 4(i). Check local rules. |
| Multiple documents served together | List all documents in a single certificate: "the foregoing MOTION TO COMPEL and MEMORANDUM IN SUPPORT." |
