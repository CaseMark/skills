---
name: contract-portfolio-analytics
description: >-
  Analyzes a portfolio of contracts to surface aggregate insights: risk
  concentrations, expiration clusters, non-standard term prevalence, and
  counterparty exposure. Produces dashboards and executive summaries for
  legal operations reporting. Use when auditing contract portfolios or
  reporting to leadership on legal risk posture.
tags:
  - corporate
  - analysis
  - summary
---

# Contract Portfolio Analytics

Extracts structured data from a contract portfolio and generates aggregate insights for legal operations and executive reporting.

## Prerequisites

- Access to contract repository (structured metadata or raw documents)
- Minimum 20+ contracts for meaningful aggregate analysis
- Organization's risk categories and reporting requirements

## Workflow

### 1. Extract Metadata

For each contract, extract: contract type, counterparty, effective date, expiration date, total value, governing law, key clause variants (indemnification type, liability caps, termination provisions), and current status.

### 2. Analyze Risk Concentrations

Identify patterns: counterparties with highest aggregate exposure, contract types with most non-standard terms, jurisdictions with highest regulatory complexity, and time periods with clustered expirations or renewals.

### 3. Flag Outliers and Anomalies

Detect contracts with: uncapped liability, missing standard protections, expired but still active, auto-renewal approaching without review, unusual governing law selections, or terms inconsistent with current organizational policy.

### 4. Generate Trend Analysis

Compare current portfolio against prior periods: new contracts added, average negotiation time, template vs. counterparty paper ratio, most negotiated clauses, and compliance improvement or regression.

### 5. Produce Executive Summary

Deliver a one-page dashboard with: total portfolio value, active contract count, top risks, upcoming expirations, and recommended actions prioritized by business impact.

## Pitfalls

- Drawing conclusions from incomplete repository data (missing contracts skew analysis)
- Treating all non-standard terms as equal risk regardless of business context
- Reporting raw counts without normalizing for contract value or counterparty significance
