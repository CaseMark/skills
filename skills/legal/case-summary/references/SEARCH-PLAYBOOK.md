# Search Playbook — Vault Queries per Case Dimension

Runnable query patterns for each dimension listed in `SKILL.md`'s MAP phase. Use them as starting points, not a script. Adjust wording to the case (practice area, venue, specific parties).

Every query assumes `casedev search vault "<query>" --vault <vault-id>`; see `RUNBOOK.md` for the full command and method variants.

## Parties & posture

- `"caption parties plaintiff defendant"`
- `"case number docket venue jurisdiction"`
- `"attorney of record appearance"`
- `"insurance carrier policy number"`

Use `--method entity` when you want canonical mentions of a specific person or org.

## Timeline / incident facts

- `"date of incident accident loss occurrence"`
- `"location of incident address intersection premises"`
- `"police report officer narrative"`
- `"witness statement observation"`
- `"mechanism of injury how it happened"`

Then, once you have the date, narrow with `--query "<incident-date> ..."`.

## Injuries / harm

- `"diagnosis ICD injury body part"`
- `"chief complaint presenting symptoms"`
- `"initial emergency room triage"`
- `"imaging MRI CT X-ray findings"`
- `"pre-existing condition history"`

## Treatment

- `"treatment plan provider specialist referral"`
- `"surgery operative report procedure"`
- `"physical therapy rehabilitation"`
- `"medication prescription"`
- `"maximum medical improvement MMI discharge"`
- `"treatment gap no appointment noncompliance"`

## Damages

**Specials:**
- `"medical bill billed amount statement"`
- `"paid amount adjustment write-off balance"`
- `"CPT code procedure charge"`

**Wage loss:**
- `"employer wage loss time missed work"`
- `"return to work restrictions"`
- `"earnings capacity vocational"`

**Future care:**
- `"life care plan future treatment cost"`
- `"future medical surgery projected"`

**Non-economic:**
- `"pain suffering impact activities daily living"`
- `"loss of consortium enjoyment"`

## Liability

- `"negligence duty breach causation"`
- `"admission statement against interest"`
- `"violation of statute regulation ordinance"`
- `"prior similar incident notice"`
- `"training policy procedure violation"`
- `"deposition admission acknowledged conceded"`

Run against specific depositions with `--object <depo-obj-id>` after inventory.

## Defenses

- `"affirmative defense comparative fault"`
- `"contributory negligence failure to mitigate"`
- `"statute of limitations"`
- `"release waiver assumption of risk"`
- `"denial liability answer"`

## Liens and offsets

- `"Medicare conditional payment MSP"`
- `"Medicaid recovery notice"`
- `"ERISA plan reimbursement"`
- `"workers compensation subrogation"`
- `"hospital lien statutory"`
- `"health insurance subrogation right"`

## Key testimony

- `"deposition page line question answer"`
- `"trial testimony direct examination"`
- `"expert opinion causation"`
- `"30(b)(6) corporate representative"`

## Red flags

- `"social media post photograph"`
- `"surveillance video investigation"`
- `"inconsistent statement prior"`
- `"spoliation missing evidence"`
- `"gap in treatment unexplained"`

## Meta-query tips

- If a query returns nothing relevant, try `--method vector` for paraphrase-tolerance.
- If the corpus is huge and searches return irrelevant hits, narrow with `--object` after inventory.
- Use `--method entity` once you know a name or exhibit number — it's far more precise than hybrid.
- `--method global` is useful for one-shot "what is this case about?" framing before going deep.
