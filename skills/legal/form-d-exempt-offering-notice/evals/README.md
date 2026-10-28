# Regression tests for form-d-exempt-offering-notice

Synthetic fact patterns that exercise the failure modes the skill is built to prevent. Every name, identifier, date and amount is fictional. The suite is two things: a structural check of the skill package, and ten behavioral tests run by giving an agent the skill and a fixture and grading its output against a written expectation.

## Layout

- `evals.json`: the test index in the repository's eval format (prompt, files, expected output), plus the path of each test's expected-behavior file.
- `fixtures/base-matter.md`: the shared synthetic matter (Larkspur Growth Partners III). Each test file names which base documents are in its inventory, which are replaced and which are added.
- `fixtures/NN-*.md`: one file per test with the inventory, the varied documents and the request.
- `expected/_common.md`: expectations that apply to every test.
- `expected/NN-*.md`: Must and Must not lines for each test.
- `check-package.py`: the structural check.

## What each test targets

| # | Fixture | Failure mode |
|---|---|---|
| 1 | overlooked-questionnaire | A document in the inventory (an oddly named scan) is called missing because the client's email says so |
| 2 | subscription-vs-ledger | A ledger figure is carried into Items 13 and 15 over the executed amendment |
| 3 | common-program-cap | Program totals pushed into issuer fields; feeder double counted; per-vehicle deadlines lost |
| 4 | waived-minimum | Item 11 answered categorically (0 or the stated minimum) instead of through the framework |
| 5 | investor-qualification-conflict | A ledger flag treated as controlling over an executed non-qualified-purchaser response; no recommendation |
| 6 | bad-actor-yes | A "Yes" listed in the hand-off without the event being reviewed and characterized under Rule 506(d) |
| 7 | unreadable-document | An unreadable scan described as missing, or filled from the client's recollection |
| 8 | edgar-affirmative-no-match | A 404 on EDGAR softened to "unverified"; a real entity substituted for a fictional one |
| 9 | edgar-lookup-failed | A blocked lookup reported as "not found" |
| 10 | offshore-feeder-reg-s | Regulation S investors double counted or shown in one variant only; a client instruction to use a ledger total followed; the placement agent cross-check eyeballed instead of run over every investor |

## Running the behavioral tests

1. Give a fresh agent the skill directory (SKILL.md and `references/`) and only the fixture files listed for the test in `evals.json`. Do not give it the `expected/` files.
2. Use the test's `prompt` verbatim. Tests 1 to 8 and 10 may use the network for identifier lookups (the fixtures use CIK 0009876543 and the issuer name "Larkspur Growth Partners", both of which returned affirmative no-matches on EDGAR when the suite was written). Test 9 must run with outbound network disabled so the transcript in the fixture is the only lookup evidence.
3. Save the output, then grade it against `expected/_common.md` and the test's expected file: one pass or fail per line, with the evidence quoted. The test passes only when every Must line passes and no Must not line is breached.
4. Record results with the skill version (commit hash), the model, and the date.

A grader should read the whole output. Several expectations are about absence (no "MISSING", no file called missing, no program total in an issuer field), which a keyword search can miss in either direction.

## Running the structural check

```bash
python3 -I skills/legal/form-d-exempt-offering-notice/evals/check-package.py
```

It verifies that the root skill stays under the repository's line limit, that every reference the root skill names exists, that the operative rules live where the root skill says they do (the gate statuses, the worksheet statuses, the five lookup outcomes, the Item 11 framework, the issuer-specific reconciliation, the hand-off tables, the quality-control gate), that reference files do not link to each other with markdown links, and that every test in `evals.json` has its fixture and expected files.
