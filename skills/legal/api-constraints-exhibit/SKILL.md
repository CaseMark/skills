---
name: api-constraints-exhibit
description: >-
  Extracts technical API constraints from OpenAPI/Swagger and developer docs
  into a contract-ready API Access & Constraints Schedule with traceability,
  risk flags, and change-control language. Use when preparing legal exhibits
  or schedules for API access, rate limits, authentication, data fields, and
  deprecation terms. Trigger keywords: OpenAPI, Swagger, API constraints, rate
  limits, authentication, API access exhibit, contract schedule, MSA/SOW,
  technical exhibit, API schedule, endpoint scope.
tags:
  - summarization
---

# API Access & Constraints Schedule

## Why This Skill Exists

API contracts routinely incorporate technical constraints by reference to "Documentation" — but documentation is controlled by engineering, changes without legal review, and often describes aspirational rather than committed behavior. When a dispute arises over rate limits, authentication requirements, or deprecated endpoints, the question becomes: what was actually committed, and where is the evidence? A contract exhibit that hard-codes numbers from a marketing page creates over-commitment risk; one that simply says "per Documentation" provides no baseline for enforcement. This skill bridges the gap by extracting constraints from authoritative technical sources, mapping each statement to a source with version and retrieval timestamp, and producing contract-ready language with appropriate commitment levels and change-control mechanics.

---

## Checkpoint A: Pre-Draft Intake (Mandatory)

Ask every time unless the user says "use defaults" or "just draft." Gather:

1. **Agreement context** — exhibit name/placement, provider vs. client posture, commitment level
2. **Authoritative sources** — OpenAPI/Swagger files, auth docs, rate limit/quotas page, error docs, changelog/deprecation policy
3. **Scope boundaries** — API product, versions, environments, regions, in-scope endpoints, webhooks
4. **Data classification rules** — Personal Data, Sensitive Data, PHI, PCI, secrets
5. **SLA/support references** — if any uptime or support statements are to be referenced

**If the user doesn't respond**, apply and clearly label these defaults:

| Parameter | Default | Alternatives |
|---|---|---|
| Exhibit type | API Access & Constraints Schedule | DPA Annex, Security Exhibit, Order Form attachment |
| API scope | Single API, current GA version | Multiple APIs, beta endpoints, webhooks |
| Contract posture | Provider (outbound) | Client (inbound), mutual |
| Commitment level | Descriptive/as-is | Binding commitments, hybrid |
| Constraint categories | Auth, rate limits, data fields | Add environments, IP allowlisting, logging, errors, deprecation |
| Output mode | Full Package | Quick Reference, Checklist Only, Risk Matrix |

Record deviations and unresolved items in the Risk/Gap Log.

---

## Step 1: Source Register and Normalization

Build a register of all authoritative sources:

| ID | Source Type | URL/File | Version/Commit | Retrieved (UTC) | Owner | Notes |
|---|---|---|---|---|---|---|
| S-1 | OpenAPI spec | | | | Eng | Primary |
| S-2 | Auth docs | | | | Eng | |
| S-3 | Rate limits | | | | Eng/Support | Plan-dependent? |
| S-4 | Changelog/deprecation | | | | PM | |
| S-5 | Error codes | | | | Eng | |

**Checklist:**
- [ ] Lock version and retrieval timestamp for each source
- [ ] Capture `servers[].url` and environment labels
- [ ] Identify `components.securitySchemes` and operation-level security

---

## Step 2: Technical-to-Legal Crosswalk

Map technical spec elements to their legal significance:

| Field / Doc Section | Example | Legal Significance | Clause Reference |
|---|---|---|---|
| `info.version` | v2.1.0 | Versioning & sunset | Change management |
| `servers[].url` | https://api.example.com | Data residency | Privacy/compliance |
| `paths.{path}.{method}` | GET /v1/widgets | Scope of license | Grant of access |
| `components.securitySchemes` | OAuth2 client credentials | Security standard | Security obligations |
| Rate limit docs | 1000/min | Usage caps | Fees/SLA |

---

## Step 3: Extraction Tables

### API Constraint Extraction Table

| Tag | Method | Path | Summary | Auth Required | Auth Type/Scopes | Rate Limit | Key Required Fields | Key Response Fields | Pagination/Max | Errors | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|

### Data Field Inventory

| Schema | Field | Type | Required | Example | Classification | Notes |
|---|---|---|---|---|---|---|

### Auth & Access Profile

| Category | Details |
|---|---|
| Methods | API key, OAuth2, mTLS, JWT |
| Credential placement | Header, query, cookie |
| Scopes/roles | List scopes/roles |
| Token lifecycle | Expiry, refresh, rotation |

### Rate Limit Profile

| Dimension | Limit | Burst | Headers | Enforcement | Tiering |
|---|---|---|---|---|---|
| Per API key | | | X-RateLimit-* | 429 | By plan |

---

## Step 4: Draft Exhibit

```text
EXHIBIT [___]: API ACCESS & CONSTRAINTS SCHEDULE

Section 1. API Identification
API Name: [ ]
API Version(s): [ ]
Base URLs: Production [ ], Sandbox [ ]
Documentation: Source Register IDs [ ] as of [date] ("Documentation")

Section 2. Authentication and Access Controls
Methods: [ ]
Credential placement: [ ]
Scopes/Roles: [ ]
Tenant isolation: [ ]
Client obligations: credential security and rotation

Section 3. Rate Limits / Quotas / Throttling
Published limits: [ ]
Limit dimensions: [ ]
Burst tolerance: [ ]
Throttle response: 429 and backoff
SLA treatment of throttling: [ ]

Section 4. Endpoint Scope and Core Operations
In-scope endpoints: [table or attach OpenAPI]
Beta/experimental endpoints excluded unless expressly included

Section 5. Data Fields and Data Handling Notes
Primary objects: [ ]
Required fields: [ ]
Sensitive data permitted or prohibited: [ ]
Webhooks: event schema and retry behavior per Documentation

Section 6. Change Management / Versioning / Deprecation
Versioning scheme: [ ]
Breaking Change definition: [ ]
Notice period and channel: [ ]

Section 7. Error Handling
Error format: [ ]
Retriable errors: [ ]
Non-retriable errors: [ ]

Section 8. Support & Incident Notes
Support/SLA governed by [SLA/Support Exhibit]

Section 9. Order of Precedence
Option A: Schedule controls only for express commitments
Option B: Schedule controls in full
```

---

## Step 5: Traceability Matrix

| Exhibit Section | Statement | Source ID | Spec Path/Anchor | Confidence | Notes |
|---|---|---|---|---|---|
| 3 | "60 requests/min per API key" | S-3 | Rate limits page | M | Plan-dependent |

Every numeric limit, authentication requirement, and scope boundary in the exhibit must have a corresponding row in this matrix.

---

## Step 6: Risk/Gap Log

| ID | Issue | Impact | Proposed Fix | Owner | Status |
|---|---|---|---|---|---|
| G-1 | Rate limits only on marketing page | Over-commitment risk | Reference docs, avoid hard numbers | Legal/Eng | Open |

---

## Checkpoint B: Post-Draft Alignment (Mandatory)

After delivering the initial exhibit, ask:

1. Does the endpoint scope match the commercial agreement's intended API access?
2. Should any constraints be elevated from descriptive/as-is to binding commitments?
3. Are there rate-limit tiers or authentication methods not captured in the sources provided?
4. Does the order of precedence (Section 9) align with the master agreement's precedence clause?

---

## Quality Audit

- Every numeric limit has a source ID and tier qualifier in the traceability matrix
- Auth methods match operation-level security from OpenAPI spec
- Beta/experimental endpoints excluded or explicitly labeled
- "Documentation" definition locks version and retrieval date
- No unintended warranties (descriptive/as-is vs. binding commitments clearly distinguished)
- Error-code treatment aligns with SLA exhibit
- Sensitive data fields flagged and mapped to DPA requirements
- Rate limits reference documentation — no hard-coded numbers without source
- Risk/gap log captures all unresolved items
- Order of precedence consistent with master agreement
- Source register complete with version, timestamp, and owner for each source
- All `[BRACKETED]` placeholders clearly marked

---

## Guidelines

- Avoid over-warranting undocumented behavior; prefer "as of [date]" with change-control
- Do not include numeric limits without a source and tier qualifier
- Treat 429 throttling explicitly in relation to SLA calculations
- Exclude beta/preview endpoints unless expressly agreed
- Flag regulated data categories and require appropriate addenda
- If jurisdiction or practice area is unknown, use neutral language and flag for review
- Any citation or technical claim uncertainty should be marked `[VERIFY]`
- Output requires legal and engineering review before incorporation into agreements

**Required disclaimer on every output:**

> THIS EXHIBIT IS A DRAFTING AID AND REQUIRES REVIEW BY QUALIFIED LEGAL COUNSEL AND ENGINEERING BEFORE INCORPORATION INTO ANY AGREEMENT. IT DOES NOT CONSTITUTE LEGAL ADVICE.
