name: ecommerce-infringement-analysis
language: en
description: Analyzes suspected ecommerce infringements to classify severity — distinguishes direct counterfeiting, unauthorized reselling, image copyright theft, and trademark confusion. Produces actionable enforcement recommendations with platform-specific next steps and estimated removal success probability.
tags:
  - analysis
  - agreement
  - regulatory
---

# Ecommerce Infringement Classification & Analysis

Classifies and prioritizes ecommerce IP infringements by type and severity, then recommends platform-appropriate enforcement actions with success probability estimates.

## Prerequisites

Before executing, collect:

1. **Infringing listing(s)** — URL(s) to suspected infringing product pages
2. **Owner's IP rights** — trademark registrations, copyright certificates, design patents
3. **Product reference data** — authorized product images, descriptions, MSRP
4. **Authorization proof** — brand registry status, letter of authorization status

## Workflow

1. **Listing analysis** — scrape infringing page: images, text, price, seller info, marketplace
2. **IP match scoring** — compare against registered marks/images using text and visual matching
3. **Infringement classification** — categorize as: direct counterfeiting, unauthorized resale, image theft, trademark confusion, or design patent violation
4. **Severity assessment** — rank by volume of infringement, price undercutting, brand damage risk, and seller history
5. **Enforcement recommendation** — select optimal action: DMCA notice, LLP/Brand Registry report, VeRO report, or cease-and-desist
6. **Success probability** — estimate removal likelihood based on marketplace, IP strength, and seller type
7. **Evidence package** — compile screenshots, IP matches, timestamps for enforcement submission

## Pitfalls

- Counterfeiters blur/mutate images to evade detection — require human verification
- Unauthorized resellers may have legitimate sourcing — distinguish from counterfeiting
- Platform-specific reporting forms have different evidentiary standards
- Some marketplaces (Temu, Shein, TikTok Shop) have inconsistent enforcement responsiveness
