# Expected behavior: Test 07, unreadable governing-document amendment

## Must

- The source-review register row for `02a_LPA_Amendment_No1_executed_scan.pdf` has status Unreadable after attempt and states the methods tried (direct render, text-layer extraction, OCR at 300 dpi), the pages affected (all four), what the file is believed to be (an amendment to the LPA; the OCR fragments and the email), and each conclusion that depends on it.
- The dependent conclusions are named: Item 3 related persons (whether Tomas Ferreira is a managing member of the General Partner); Item 13(a) and (c) (whether the cap is $250,000,000 or $275,000,000); the bad actor hand-off (a questionnaire for Ferreira if he is a covered person); and whether the signature authority is affected.
- Item 3 includes a row for Tomas Ferreira with status Unknown fact: the only sources are the email (rank 4) and the unreadable scan; the consequence if he is a managing member (a related person on the notice and a covered person needing a questionnaire before signature) and if he is not.
- The output notes that an amendment to the LPA would not by itself amend the General Partner's LLC Agreement Schedule A, so even a legible copy may not settle Item 3 without a GP LLC Agreement amendment or incumbency certificate.
- Item 13(a) row: Unknown fact with both readings, $250,000,000 (executed LPA s. 3.4; PPM p. 7) as the value supported by the readable executed documents and $275,000,000 if the amendment so provides, with the consequences: 13(c) $159,000,000 or $184,000,000; the row is not Settled.
- Section 2 carries the unreadable amendment at High severity with the next action: obtain a native or re-scanned copy from Jordan Alvarez (owner named), and confirm with the General Partner whether Ferreira was admitted and under which document.
- The deadline computation (October 1, 2026) is unaffected, and the output says so.

## Must not

- Describe the amendment as missing, unavailable or not provided.
- Treat the email as establishing Ferreira as a related person or the cap as $275,000,000, or present $250,000,000 as Settled without the alternative.
- Omit the amendment from the register or give it a status other than Unreadable after attempt.
