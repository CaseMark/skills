---
name: stock-purchase-agreement
description: Drafts comprehensive Stock Purchase Agreements for 100% stock acquisitions in middle-market M&A transactions. Extracts deal terms from uploaded documents, structures purchase price with working capital adjustments and earnouts, builds seller representations and warranties with disclosure schedules, and includes indemnification, escrow, restrictive covenants, and closing mechanics. Use when drafting SPAs, stock acquisition agreements, definitive purchase agreements, or M&A closing documents.
tags:
  - agreement
  - corporate
  - drafting
  - transactional
---

# Stock Purchase Agreement (M&A)

Drafts a definitive Stock Purchase Agreement for acquiring 100% of a target company's outstanding capital stock in a middle-market transaction.

## Prerequisites

1. **Deal documents** — LOI, term sheet, or preliminary agreement with negotiated business terms
2. **Target company organizational docs** — articles of incorporation, bylaws, shareholder agreements
3. **Capitalization details** — authorized shares, outstanding shares, each seller's ownership
4. **Financial statements** — audited/reviewed for 2+ fiscal years, most recent interim period
5. **Due diligence materials** — material contracts, employment agreements, IP schedules, litigation history
6. **Negotiated economics** — purchase price, working capital target, escrow percentage, earnout terms

## Document Intelligence

Extract from uploaded materials before drafting:

| Data Point | Source Priority |
|---|---|
| Party names, entity types, jurisdictions | LOI → Org docs → Correspondence |
| Cap table (shares, classes, ownership %) | Stock ledger → Org docs → LOI |
| Purchase price & adjustments | Term sheet → LOI |
| Working capital target | Financial statements → Term sheet |
| Escrow/earnout terms | LOI → Term sheet |
| Material contracts requiring consent | Due diligence schedule |
| Disclosed liabilities/contingencies | Financial statements → Disclosure schedules |
| Related party transactions | Financial statements → Due diligence |
| Key employees & compensation | Employment agreements → HR records |
| Balance sheet date (MAE baseline) | Most recent financial statements |

Cite specific source documents when incorporating extracted terms. Flag gaps requiring user input.

## Output Structure

### Article I: Purchase and Sale of Shares

- Sale of 100% of outstanding capital stock, free and clear of all liens
- Seller-by-seller allocation on **Exhibit A** (name, shares, %, price allocation)
- Confirmation no other equity securities, options, warrants, or commitments exist
- Transfer mechanics: endorsed certificates or blank stock powers
- Post-closing: buyer owns 100% equity, elects all directors

### Article II: Purchase Price and Payment

**Fixed vs. Adjusted Price:**
- State aggregate price in USD
- If adjusted: define Net Working Capital (current assets − current liabilities per GAAP consistent with historical statements)

**Working Capital Adjustment Procedure:**

| Step | Timeline | Action |
|---|---|---|
| Closing statement delivery | Closing + 60 days | Buyer delivers NWC calculation |
| Review period | 30 days after delivery | Sellers review with access to books |
| Dispute notice | End of review period | Sellers object or statement becomes final |
| Good faith negotiation | 30 days after objection | Parties attempt resolution |
| Independent accountant | After negotiation fails | Binding determination; fees split proportionally |
| True-up payment | 5 business days after final determination | Dollar-for-dollar adjustment paid by owing party |

**Payment Mechanics:**
- Wire transfer of immediately available funds to seller-designated accounts (designated 2+ business days pre-closing)
- Allocate per Exhibit A ownership percentages
- Buyer has no obligation to resolve inter-seller allocation disputes

**Escrow:**
- Typical range: 10-20% of aggregate purchase price
- Deposit with escrow agent at closing per escrow agreement (attach as exhibit)
- Release schedule: e.g., 50% at 1st anniversary, remainder at 2nd anniversary (subject to pending claims)

**Tax Withholding:**
- Buyer entitled to withhold per federal/state/local/foreign law
- Withheld amounts treated as paid to applicable seller
- Reasonable advance notice + opportunity to provide exemption documentation

### Article III: Closing

**Timing & Location:**
- Fixed date or within specified business days after condition satisfaction/waiver
- In person or remote via electronic exchange + wire transfer
- Effective as of 12:01 a.m. local time on closing date

**Seller Closing Deliveries:**
- [ ] Stock certificates endorsed in blank / with executed stock powers + transfer tax stamps
- [ ] Director and officer resignations (effective at closing) + general releases (except accrued compensation, indemnification)
- [ ] Good standing certificate (within 10 business days of closing)
- [ ] Seller compliance certificate (reps true, covenants performed)
- [ ] Third-party consents per disclosure schedules
- [ ] Lender payoff letters + UCC-3 termination statements + lien releases
- [ ] Key employee employment/non-compete agreements (if applicable)
- [ ] FIRPTA certificates (TIN + non-foreign person certification per Treasury Regs)

**Buyer Closing Deliveries:**
- [ ] Purchase price payment (adjusted, less escrow/holdbacks) via wire
- [ ] Buyer compliance certificate
- [ ] Executed ancillary agreements (employment, escrow, etc.)
- [ ] Escrow deposit with escrow agent

### Article IV: Sellers' Representations and Warranties

Structure as joint and several (or several only per deal terms). All subject to disclosure schedules.

**Fundamental Representations** (extended survival):
- Organization, valid existence, good standing; qualification in required jurisdictions
- Authority, due execution, enforceability (subject to bankruptcy/equity exceptions)
- Capitalization: authorized/outstanding shares, duly authorized, validly issued, fully paid, non-assessable; no outstanding options/warrants/convertibles
- Title to shares: record and beneficial ownership, free and clear of all liens

**Business Representations** (standard survival):

| Category | Key Elements |
|---|---|
| Financial statements | Fair presentation per GAAP, consistent application, adequate internal controls |
| No undisclosed liabilities | None beyond balance sheet + ordinary course since balance sheet date |
| Absence of MAE | Ordinary course since balance sheet date; no specified prohibited actions taken |
| Compliance with laws | Material compliance; all permits in force; no violation notices |
| Litigation | No pending/threatened actions; no outstanding orders/injunctions |
| Taxes | Timely filed/paid; no audits pending; withholding compliance; no lien for taxes; no waived SOL |
| Material contracts | Complete list on schedules; valid/binding; no breach/default by any party |
| Intellectual property | Complete list; ownership/valid rights; no infringement claims (inbound or outbound) |
| Real & personal property | Good title/valid leasehold; free of liens (except permitted); good operating condition |
| Employees & benefits | Complete roster; labor law compliance; no CBA/union activity; ERISA/IRC compliance; funded obligations |
| Environmental | Compliance with environmental laws/permits; no violations/releases; no hazardous materials issues |
| Insurance | Complete policy list; all in force; premiums current; no cancellation notices |
| Related party transactions | Disclosed on schedules; arm's-length terms |
| Full disclosure | No untrue statement of material fact; no omission rendering statements misleading |

### Article V: Buyer's Representations and Warranties

- Organization, valid existence, good standing
- Authority, due execution, enforceability
- No conflicts with organizational docs, law, or existing agreements
- Financial capacity: sufficient funds available at closing (address financing commitment if applicable)
- Investment representations (if unregistered): investment intent, accredited investor status, access to information

### Article VI: Covenants

**Pre-Closing Covenants:**
- Operate in ordinary course consistent with past practice
- Preserve business organization, relationships, assets

**Prohibited Pre-Closing Actions** (without buyer's written consent):
- Amend organizational documents
- Issue/grant equity securities or options
- Declare dividends/distributions or redeem equity
- Acquire/dispose assets above threshold (except ordinary course)
- Incur indebtedness above threshold
- CapEx above threshold
- Enter/modify/terminate material contracts outside ordinary course
- Increase compensation/benefits or adopt/amend benefit plans
- Hire/terminate employees above compensation threshold
- Settle litigation above threshold
- Related party transactions
- Actions causing rep breach or condition failure

**Access:** Buyer gets reasonable access during business hours to properties, books, records, contracts, personnel (no interference with operations; does not diminish seller obligations).

**Restrictive Covenants (Post-Closing):**

| Covenant | Scope | Duration | Exceptions |
|---|---|---|---|
| Non-compete | Specific business activities; defined geography | 1-5 years (per jurisdiction) | Passive ownership ≤5% of public company |
| Employee non-solicit | Company employees (or those with material contact) | Same or longer than non-compete | General advertisements not directed at employees |
| Customer non-solicit | Customers during 12-24 months pre-closing | Same or longer than non-compete | — |
| Supplier non-solicit | Company suppliers | Same as customer non-solicit | — |
| Confidentiality | All proprietary/confidential information | Indefinite (or extended period) | Publicly available info; legally compelled disclosure |

Include judicial reformation language and severability for all restrictive covenants.

**Additional Covenants:**
- Reasonable best efforts to satisfy conditions and close
- Public announcements only with mutual consent (except legally required)
- Expenses: each party bears own; specify treatment of company transaction expenses
- Tax cooperation: joint preparation/filing, pre/post-closing allocation (interim closing of books or pro rata), straddle period treatment, Section 1060 allocation + consistent Forms 8594
- Further assurances and post-closing cooperation (transition assistance, litigation support)

### Article VII: Indemnification

**Sellers' Indemnification:** Losses from:
- Breach of seller reps/warranties
- Breach of seller covenants
- Undisclosed company liabilities
- Unpaid company transaction expenses
- Pre-closing taxes

**Buyer's Indemnification:** Losses from:
- Breach of buyer reps/warranties
- Breach of buyer covenants
- Post-closing company liabilities

**Survival Periods:**

| Representation Category | Survival |
|---|---|
| Fundamental (org, authority, cap, title) | 3-5 years or indefinite |
| Tax | SOL + 60 days (including extensions) |
| All other reps | 12-24 months post-closing |
| Post-closing covenants | Until fully performed |

**Limitations on Seller Liability:**

| Limitation | Typical Range |
|---|---|
| Basket/deductible | 0.5%-2% of purchase price |
| Basket type | True deductible or tipping (specify) |
| Cap | 20-50% of purchase price |
| Cap exclusions | Fundamental reps, covenants, fraud/intentional misrepresentation |

**Third-Party Claim Procedures:**
1. Indemnified party gives prompt written notice (failure doesn't relieve obligation unless actual prejudice)
2. Indemnifying party may assume defense within 20-30 days with reasonably acceptable counsel
3. Indemnified party may participate at own expense
4. No settlement without indemnified party consent if: admits liability, imposes injunctive relief, or lacks unconditional release
5. If defense not assumed, indemnified party defends at indemnifying party's expense

**Loss Calculation:**
- Net of insurance proceeds and third-party recoveries actually received
- Net of tax benefits actually realized
- Commercially reasonable mitigation required
- Exclude consequential/punitive damages (except if awarded in third-party claim)

**Escrow as Recovery Source:**
- During escrow period: escrowed funds are sole recovery source (no personal seller liability until exhausted, if negotiated)
- Claim procedure: written notice to escrow agent + sellers → 30-day objection period → release or hold pending resolution

**Exclusive remedy** for rep/warranty/covenant breaches (except fraud and equitable relief).

### Article VIII: Termination

**Termination Rights:**

| Trigger | Who May Terminate |
|---|---|
| Mutual written consent | Either party |
| Outside date passed (3-6 months) | Non-breaching party |
| Final non-appealable governmental prohibition | Either party |
| Material uncured breach by sellers (30-day cure) | Buyer |
| Material uncured breach by buyer (30-day cure) | Sellers |
| Material adverse effect (if negotiated) | Buyer |

**Effects:** All obligations terminate except confidentiality, expense obligations, and liability for willful pre-termination breach. Consider termination fee / reverse termination fee provisions.

### Article IX: General Provisions

- **Governing law:** [State — typically Delaware, NY, or state of incorporation] without conflict-of-law principles
- **Jurisdiction/venue:** Exclusive in specified state/federal courts; waive inconvenient forum
- **Alternative:** Binding arbitration (AAA Commercial Rules; specify seat, arbitrator count, discovery scope)
- **Attorneys' fees:** Each party bears own (or prevailing party provision)
- **Entire agreement:** This agreement + exhibits/schedules supersedes all prior agreements/negotiations
- **Amendments/waivers:** Written instrument signed by all parties; no oral modifications
- **Notices:** Written; effective on personal delivery, overnight courier with confirmation, or email with confirmation; to specified addresses with counsel copies
- **Assignment:** No assignment without consent; buyer may assign to affiliates or successors
- **Severability:** Invalid provisions reformed to closest enforceable scope; remaining provisions unaffected
- **Counterparts:** Multiple counterparts; electronic/PDF signatures have original force
- **Construction:** Headings for convenience; "including" means "without limitation"; jointly drafted (no authorship presumption)
- **No third-party beneficiaries**
- **Time is of the essence**

### Exhibits and Schedules

**Exhibit A:** Seller schedule (name, address, TIN, shares, class, ownership %, price allocation) — must total 100%

**Disclosure Schedules:** Numbered to correspond to each representation. Prepare shells for all material rep categories. Review for completeness and internal consistency.

## Guidelines

- Extract and cite specific terms from uploaded deal documents; flag gaps requiring user input
- Balance buyer-protective structure with reasonable seller limitations (baskets, caps, survival)
- Use defined terms consistently; capitalize when used as defined terms
- Verify all cross-references, section numbers, and exhibit references for internal consistency
- Address Section 1060 allocation and Forms 8594 for tax compliance
- Include FIRPTA certification requirements for seller closing deliveries
- Restrictive covenant scope must be reasonable and enforceable in governing jurisdiction — flag if jurisdiction disfavors non-competes
- Mark any uncertain statutory citations with [VERIFY]
- Final document typically 30-60 pages depending on complexity and schedule extent
