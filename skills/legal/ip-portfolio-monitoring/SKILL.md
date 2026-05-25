name: ip-portfolio-monitoring
language: en
description: Monitors an IP portfolio across marketplaces and the open web for infringements — trademark abuse, counterfeit listings, unauthorized use of copyrighted images, and design patent violations. Generates prioritized enforcement reports with evidence packs ready for action.
tags:
  - research
  - analysis
  - regulatory
---

# IP Portfolio Monitoring & Infringement Detection

Systematically monitors a brand's intellectual property across ecommerce marketplaces, social platforms, and the open web for unauthorized use, counterfeiting, and infringement.

## Prerequisites

Before executing, collect:

1. **IP register** — all trademarks, registered copyrights, design patents with registration numbers
2. **Authorized product images** — high-res product photos linked to SKUs/catalog items
3. **Authorized sellers list** — which distributors/resellers have permission
4. **Target marketplaces** — Amazon, Shopify, eBay, Etsy, TikTok Shop, Temu, Shein, etc.

## Workflow

1. **Catalog ingestion** — import product images, descriptions, and IP register
2. **Computer vision scan** — deploy visual search against target marketplaces using product imagery
3. **Trademark keyword search** — scan listings for unauthorized use of registered marks
4. **Result correlation** — match findings against authorized sellers to flag unauthorized use
5. **Evidence packaging** — compile screenshot evidence, URLs, timestamps, and IP matching results
6. **Prioritization** — rank by severity (direct counterfeiting > unauthorized reselling > image theft)
7. **Enforcement handoff** — output structured report ready for takedown or legal action

## Pitfalls

- Computer vision false positives from similar but legitimate products
- Listing text evasion (blurred images, altered trademarks, keyword stuffing)
- Platform detection gaps — some marketplaces lack robust enforcement APIs
- Local marketplace variants (e.g., regional .cn domains) may escape detection
- Results noise requires human review before enforcement action
