---
name: contract-obligation-tracker
description: >-
  Extracts and tracks post-signature contractual obligations, deadlines, and
  renewal dates from executed agreements. Generates a structured obligation
  register with alerts for upcoming milestones. Use when managing active
  contract portfolios or preparing for renewals and terminations.
tags:
  - corporate
  - checklist
  - analysis
---

# Contract Obligation Tracker

Builds and maintains a structured register of obligations, deadlines, and key dates extracted from executed contracts.

## Prerequisites

- Executed contract(s) in searchable format
- Access to organization's contract repository or file system
- Calendar or task system for deadline alerts

## Workflow

### 1. Extract Key Dates and Deadlines

Parse each executed contract for: effective date, expiration date, renewal date, notice periods, payment schedules, delivery milestones, audit rights windows, and termination notice deadlines.

### 2. Identify Affirmative Obligations

Catalog every obligation each party must perform: reporting requirements, insurance maintenance, compliance certifications, consent requirements, non-compete periods, and post-termination duties.

### 3. Build Obligation Register

Create a structured table with columns: obligation description, responsible party, due date, recurrence (one-time/monthly/annual), days until due, and consequence of breach.

### 4. Set Alert Thresholds

For each obligation, calculate alert windows: 90 days for renewals and terminations, 30 days for reporting deadlines, 14 days for payment obligations. Flag any obligation due within its alert window.

### 5. Generate Portfolio Dashboard

Summarize across all contracts: total active obligations, upcoming deadlines this month/quarter, obligations at risk, and contracts approaching renewal or expiration.

## Pitfalls

- Missing obligations buried in exhibits, schedules, or amendment riders
- Failing to account for business days vs. calendar days in deadline calculations
- Overlooking automatic renewal clauses that require affirmative opt-out
