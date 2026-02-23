---
name: api-constraints-exhibit
description: >-
  Extracts technical API constraints from OpenAPI/Swagger and developer docs
  into a contract-ready API Access & Constraints Schedule with traceability,
  risk flags, and change-control language. Use when preparing legal exhibits
  or schedules for API access, rate limits, authentication, data fields, and
  deprecation terms. Trigger keywords: OpenAPI, Swagger, API constraints, rate
  limits, authentication, API access exhibit, contract schedule, MSA/SOW.
tags:
  - summarization
---

# API Access & Constraints Schedule

Produces a traceable exhibit that translates API technical limits into contract-ready language.

## Prerequisites

1. Agreement context: exhibit name/placement, provider vs. client posture, commitment level.
2. Authoritative sources: OpenAPI/Swagger files, auth docs, rate limit/quotas page, error docs, changelog/deprecation policy.
3. Scope boundaries: API product, versions, environments, regions, in-scope endpoints, webhooks.
4. Data classification rules: Personal Data, Sensitive Data, PHI, PCI, secrets.
5. SLA/support references if any uptime or support statements are to be referenced.

## Output Structure / Process

### Step 1: Intake Snapshot

| Parameter | Default | Alternatives |
|---|---|---|
| Exhibit type | API Access & Constraints Schedule | DPA Annex, Security Exhibit, Order Form attachment |
| API scope | Single API, current GA version | Multiple APIs, beta endpoints, webhooks |
| Contract posture | Provider (outbound) | Client (inbound), mutual |
| Commitment level | Descriptive/as-is | Binding commitments, hybrid |
| Constraint categories | Auth, rate limits, data fields | Add environments, IP allowlisting, logging, errors, deprecation |
| Output mode | Full Package | Quick Reference, Checklist Only, Risk Matrix |

Record deviations and unresolved items in the Risk/Gap Log.

### Step 2: Source Register and Normalization

| ID | Source Type | URL/File | Version/Commit | Retrieved (UTC) | Owner | Notes |
|---|---|---|---|---|---|---|
| S-1 | OpenAPI spec | | | | Eng | Primary |
| S-2 | Auth docs | | | | Eng | |
| S-3 | Rate limits | | | | Eng/Support | Plan-dependent? |
| S-4 | Changelog/deprecation | | | | PM | |
| S-5 | Error codes | | | | Eng | |

Checklist:
- [ ] Lock version and retrieval timestamp for each source.
- [ ] Capture `servers[].url` and environment labels.
- [ ] Identify `components.securitySchemes` and operation-level security.

### Step 3: Technical-to-Legal Crosswalk

| Field / Doc Section | Example | Legal Significance | Clause Reference |
|---|---|---|---|
| `info.version` | v2.1.0 | Versioning & sunset | Change management |
| `servers[].url` | https://api.example.com | Data residency | Privacy/compliance |
| `paths.{path}.{method}` | GET /v1/widgets | Scope of license | Grant of access |
| `components.securitySchemes` | OAuth2 client credentials | Security standard | Security obligations |
| Rate limit docs | 1000/min | Usage caps | Fees/SLA |

### Step 4: Extraction Tables

API Constraint Extraction Table:

| Tag | Method | Path | Summary | Auth Required | Auth Type/Scopes | Rate Limit | Key Required Fields | Key Response Fields | Pagination/Max | Errors | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| | GET | /v1/widgets | List widgets | Yes | OAuth2: widgets:read | 60 rpm | tenant_id | items[].id | limit<=100 | 401/403/429 | |

Data Field Inventory:

| Schema | Field | Type | Required | Example | Classification | Notes |
|---|---|---|---|---|---|---|
| User | email | string | Yes | a@b.com | Personal Data | |
| Payment | card_last4 | string | No | 1234 | PCI-related | |

Auth & Access Profile:

| Category | Details |
|---|---|
| Methods | API key, OAuth2, mTLS, JWT |
| Credential placement | Header, query, cookie |
| Scopes/roles | List scopes/roles |
| Token lifecycle | Expiry, refresh, rotation |

Rate Limit Profile:

| Dimension | Limit | Burst | Headers | Enforcement | Tiering |
|---|---|---|---|---|---|
| Per API key | | | X-RateLimit-* | 429 | By plan |

### Step 5: Exhibit Draft (Template)

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

### Step 6: Traceability Matrix

| Exhibit Section | Statement | Source ID | Spec Path/Anchor | Confidence | Notes |
|---|---|---|---|---|---|
| 3 | "60 requests/min per API key" | S-3 | Rate limits page | M | Plan-dependent |

### Step 7: Risk/Gap Log

| ID | Issue | Impact | Proposed Fix | Owner | Status |
|---|---|---|---|---|---|
| G-1 | Rate limits only on marketing page | Over-commitment risk | Reference docs, avoid hard numbers | Legal/Eng | Open |

### Step 8: QC Checklist

- [ ] Every numeric limit has a source and tier qualifier.
- [ ] Auth methods match operation-level security.
- [ ] Beta/experimental endpoints excluded or labeled.
- [ ] "Documentation" definition locks version and retrieval date.
- [ ] No unintended warranties.
- [ ] Error-code treatment aligns with SLA exhibit.
- [ ] Sensitive fields flagged and mapped to DPA.

### Output Modes

| Mode | Contents |
|---|---|
| Full Package | All tables, exhibit, traceability, risk/gap log |
| Quick Reference | One-page checklist summary |
| Checklist Only | Consolidated checklists |
| Risk Matrix | Client request vs. API reality |

## Guidelines

- Avoid over-warranting undocumented behavior; prefer "as of [date]" with change-control.
- Do not include numeric limits without a source and tier qualifier.
- Treat 429 throttling explicitly in relation to SLA calculations.
- Exclude beta/preview endpoints unless expressly agreed.
- Flag regulated data categories and require appropriate addenda.
- If jurisdiction or practice area is unknown, use neutral language and flag for review.
- Any citation uncertainty should be marked `[VERIFY]`.
