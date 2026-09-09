# Secret detection and prevention control

Owner: Security Engineering  
Control: CI secret detection, with native GitHub push protection tracked separately  
Review cadence: at least annually and after a material repository or scanner change

## Required control

The `Secret detection` workflow scans the complete reachable Git history on every push and pull request and once each week. A finding fails the workflow, so a change cannot satisfy a branch rule that requires this check until the finding is treated. The scanner binary, download checksum, and checkout action are pinned.

This workflow is a **detective CI control**, not native GitHub push protection. Repository administrators must separately record whether GitHub secret scanning and push protection are enabled. CI coverage must never be reported as native push prevention.

## Historical findings

After this workflow reaches the repository's protected base branch, run it manually once and retain the run URL, repository SHA, UTC time, and result. Triage every finding without copying a secret value into logs, issues, or evidence:

1. Confirm whether it is a real credential, a synthetic test value, or a false positive.
2. For a real credential, follow the incident-response process and obtain authorization before revocation, rotation, or history rewriting.
3. Link the treatment record to the scanner run and record owner, disposition, and completion time.
4. Re-run the full-history scan and retain the passing result. A history rewrite is destructive and requires separate explicit approval.

An initial failing historical scan proves detection is operating; it does not establish remediation or compliance.

## Exceptions

Exceptions must be narrow, time-bounded, and approved by both the repository owner and Security Engineering. The linked tracking record must contain the detector/fingerprint, justification, compensating control, owner, approval, and an expiry no later than 90 days. Add only the approved fingerprint to `.gitleaksignore`. Broad path, regex, detector, or repository-wide allowlists are prohibited unless the same approval record explicitly authorizes them. Remove an exception when it expires and re-run the workflow.

## Safe validation

Use an invalid synthetic credential in a temporary branch; never use a live credential. Verify that the workflow fails and redacts the value, remove the fixture, and verify that the same workflow passes. Retain both run URLs and the tested SHA. Native push-protection validation is a separate GitHub-administrator test and must identify itself as such.
