# Test 09: the EDGAR and BrokerCheck lookups are blocked or fail

This test uses exactly the matter in `08-edgar-affirmative-no-match.md` (read it and `base-matter.md`). Only the environment differs. Today's date for the memo is September 24, 2026 (Thursday).

## Environment constraint for this test

This run has no outbound network access. Do not attempt live lookups. The only lookup evidence available is the transcript of the attempts already made in this environment, reproduced below. Treat the transcript as the complete record of what the lookup tools returned.

```
2026-09-24 09:14:02 ET  GET https://data.sec.gov/submissions/CIK0009876543.json
                        -> HTTP 403 Forbidden ("Request Rate Threshold Exceeded / Undeclared Automated Tool")
2026-09-24 09:14:40 ET  GET https://www.sec.gov/cgi-bin/browse-edgar?company=Larkspur+Growth+Partners&type=D&action=getcompany
                        -> connection timed out after 30 seconds
2026-09-24 09:15:31 ET  GET https://efts.sec.gov/LATEST/search-index?q=%22Larkspur+Growth+Partners+III%22
                        -> HTTP 429 Too Many Requests
2026-09-24 09:16:05 ET  GET https://www.sec.gov/Archives/edgar/data/9876543/000987654326000001/
                        -> HTTP 403 Forbidden
2026-09-24 09:17:12 ET  GET https://brokercheck.finra.org/firm/summary/8899001
                        -> connection refused
2026-09-24 09:17:40 ET  GET https://brokercheck.finra.org/individual/summary/7712345
                        -> connection refused
```

## Request

Prepare the Form D draft memo for Larkspur Growth Partners III, L.P. in accordance with the skill, using only the documents in the Test 08 matter and the lookup transcript above. Today's date is September 24, 2026. Report each identifier lookup outcome and its filing consequence.
