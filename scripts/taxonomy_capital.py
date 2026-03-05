"""
Capital (agentskills.capital) taxonomy: 20 subgroups, 20 skills each.

Capital focuses on institutional capital deployment, deal-making, and capital
markets — M&A, venture capital, private equity, fund formation, structured
finance, capital allocation, and institutional investing. This is distinct from
the finance vertical (agentskills.finance) which covers consumer/corporate
finance operations like tax, budgets, accounting, insurance, and banking.

Each subgroup is analogous to a legal practice area. Skills within encode
semi-structured agentic workflows for moving and processing/synthesizing
information in capital deployment and capital markets contexts.

Naming: gerund form, lowercase-hyphenated, max 64 chars.
"""

CAPITAL_TAXONOMY = {
    # ─── 1. MERGERS & ACQUISITIONS ────────────────────────────────────
    "Mergers and Acquisitions": {
        "description": "Deal origination, due diligence, transaction execution, and post-merger integration",
        "practice_areas": [
            "M&A Advisory",
            "Corporate Development",
            "Investment Banking",
        ],
        "skills": [
            (
                "screening-acquisition-targets",
                "Filters potential acquisition targets against strategic criteria including size, geography, capability gaps, and synergy potential. Use when building target lists, screening M&A pipelines, or identifying bolt-on candidates.",
            ),
            (
                "building-merger-consequence-models",
                "Constructs accretion/dilution analysis with pro forma financials, synergy phasing, and purchase price allocation. Use when modeling merger outcomes, calculating EPS accretion, or analyzing deal structures.",
            ),
            (
                "conducting-buy-side-due-diligence",
                "Structures comprehensive buy-side diligence across financial, legal, commercial, and operational workstreams. Use when coordinating DD processes, building diligence checklists, or synthesizing DD findings.",
            ),
            (
                "drafting-confidential-information-memoranda",
                "Creates sell-side CIMs with business description, financial overview, growth drivers, and investment highlights. Use when preparing sell-side marketing materials, writing CIMs, or positioning companies for sale.",
            ),
            (
                "analyzing-synergy-potential",
                "Quantifies revenue and cost synergies with build-up methodology, realization timelines, and integration cost offsets. Use when estimating deal synergies, modeling cost savings, or building synergy cases for IC.",
            ),
            (
                "structuring-deal-consideration",
                "Evaluates cash vs stock vs mixed consideration structures with tax, accounting, and shareholder impact analysis. Use when structuring deal terms, comparing consideration alternatives, or analyzing tax-efficient structures.",
            ),
            (
                "managing-sell-side-auction-processes",
                "Coordinates competitive auction workflows from teaser distribution through definitive agreement execution. Use when running sell-side processes, managing bid rounds, or tracking buyer engagement.",
            ),
            (
                "analyzing-fairness-opinion-valuations",
                "Evaluates fairness opinion methodologies across DCF, trading comps, and precedent transactions for board-level decisions. Use when reviewing fairness opinions, preparing board materials, or analyzing transaction fairness.",
            ),
            (
                "modeling-purchase-price-allocation",
                "Structures PPA analysis with tangible/intangible asset identification, useful life estimation, and goodwill calculation. Use when modeling purchase accounting, allocating deal price, or estimating amortization impact.",
            ),
            (
                "managing-deal-data-rooms",
                "Organizes virtual data room structure with document indexing, access permissions, activity tracking, and Q&A management. Use when setting up VDRs, managing document production, or tracking buyer diligence activity.",
            ),
            (
                "drafting-transaction-term-sheets",
                "Structures preliminary transaction terms including price, consideration, conditions, reps/warranties, and indemnification. Use when drafting LOIs, preparing term sheets, or summarizing negotiated deal points.",
            ),
            (
                "analyzing-anti-trust-risk",
                "Evaluates competition law exposure with market definition, HHI analysis, and remedy estimation for proposed transactions. Use when assessing merger clearance risk, analyzing market concentration, or preparing HSR filings.",
            ),
            (
                "conducting-quality-of-earnings-analysis",
                "Adjusts reported earnings for non-recurring items, accounting policy choices, and run-rate normalizations. Use when performing QofE analysis, adjusting EBITDA, or validating seller financial presentations.",
            ),
            (
                "planning-post-merger-integration",
                "Structures Day 1 readiness, 100-day plans, and long-term integration workstreams with synergy realization tracking. Use when planning PMI, building integration timelines, or tracking workstream execution.",
            ),
            (
                "analyzing-break-up-fees-and-protections",
                "Evaluates deal protection mechanisms including break-up fees, no-shop clauses, matching rights, and force-the-vote provisions. Use when analyzing deal protections, negotiating break fees, or assessing termination provisions.",
            ),
            (
                "modeling-contingent-consideration",
                "Structures earnout and contingent payment mechanisms with milestone definitions, measurement periods, and payout scenarios. Use when modeling earnouts, designing milestone-based payments, or valuing contingent consideration.",
            ),
            (
                "analyzing-material-adverse-change-clauses",
                "Evaluates MAC clause scope, carve-outs, and enforceability standards in acquisition agreements. Use when reviewing MAC provisions, assessing deal certainty, or analyzing interim covenant protections.",
            ),
            (
                "conducting-management-presentations",
                "Structures management presentation materials for buyer meetings with business overview, strategy, and financial deep-dives. Use when preparing management presentations, coaching management teams, or organizing buyer meetings.",
            ),
            (
                "analyzing-cross-border-deal-structures",
                "Evaluates cross-border transaction complexities including tax treaties, currency, regulatory approvals, and cultural factors. Use when structuring international deals, assessing cross-border risk, or navigating multi-jurisdiction closings.",
            ),
            (
                "modeling-transaction-financing-structures",
                "Constructs acquisition financing models with debt capacity, leverage analysis, coverage ratios, and capital structure optimization. Use when modeling deal financing, analyzing leverage capacity, or structuring acquisition debt.",
            ),
        ],
    },
    # ─── 2. VENTURE CAPITAL ───────────────────────────────────────────
    "Venture Capital": {
        "description": "Early-stage deal flow, evaluation, term negotiation, and portfolio support",
        "practice_areas": [
            "Venture Capital",
            "Seed/Series Investing",
            "Startup Ecosystems",
        ],
        "skills": [
            (
                "screening-deal-flow-pipeline",
                "Filters inbound deal flow against fund thesis, stage, sector, and return requirements with structured pass/advance decisions. Use when triaging deal flow, evaluating inbound pitches, or managing sourcing pipelines.",
            ),
            (
                "evaluating-startup-business-models",
                "Assesses startup viability through business model canvas analysis, unit economics validation, and market timing evaluation. Use when evaluating startup pitches, analyzing business model sustainability, or assessing product-market fit.",
            ),
            (
                "analyzing-term-sheet-economics",
                "Deconstructs VC term sheets with liquidation preference waterfalls, anti-dilution mechanics, and option pool impact analysis. Use when analyzing term sheets, comparing investor terms, or modeling founder dilution.",
            ),
            (
                "modeling-venture-cap-tables",
                "Builds cap table models with round-by-round dilution, ESOP expansion, convertible note conversion, and exit waterfall analysis. Use when modeling cap tables, projecting ownership dilution, or calculating exit proceeds distribution.",
            ),
            (
                "conducting-technical-due-diligence",
                "Structures technology diligence with architecture review, code quality assessment, scalability analysis, and technical debt evaluation. Use when evaluating startup technology, assessing engineering teams, or reviewing technical infrastructure.",
            ),
            (
                "drafting-investment-committee-memos",
                "Creates VC IC presentation materials with deal thesis, market analysis, team assessment, competitive landscape, and return scenarios. Use when preparing IC memos, presenting investment opportunities, or documenting investment decisions.",
            ),
            (
                "building-venture-return-models",
                "Constructs venture return models with entry valuation, follow-on reserve, multiple scenario exits, and portfolio-level fund math. Use when modeling VC returns, calculating fund economics, or projecting portfolio outcomes.",
            ),
            (
                "managing-portfolio-company-support",
                "Structures portfolio company engagement with board preparation, hiring support, business development, and follow-on strategy. Use when supporting portfolio companies, preparing board meetings, or coordinating investor resources.",
            ),
            (
                "evaluating-founder-team-dynamics",
                "Assesses founding team composition, complementarity, equity split rationale, and execution capability. Use when evaluating founding teams, assessing management risk, or conducting reference checks.",
            ),
            (
                "analyzing-market-size-and-timing",
                "Structures TAM/SAM/SOM analysis with bottom-up and top-down methodology and market timing assessment. Use when sizing markets, validating market opportunity, or assessing timing risk.",
            ),
            (
                "managing-syndication-and-co-investment",
                "Coordinates multi-investor rounds with allocation, lead/follow dynamics, and information rights structuring. Use when syndicating rounds, managing co-investor relationships, or structuring investor groups.",
            ),
            (
                "analyzing-convertible-instrument-terms",
                "Evaluates SAFE, convertible note, and KISS structures with conversion mechanics, caps, discounts, and MFN provisions. Use when analyzing convertible instruments, comparing SAFE vs note terms, or modeling conversion scenarios.",
            ),
            (
                "tracking-portfolio-company-metrics",
                "Monitors portfolio company KPIs including burn rate, runway, MRR growth, CAC/LTV, and cohort performance. Use when tracking portfolio metrics, assessing company health, or preparing portfolio reviews.",
            ),
            (
                "managing-bridge-financing-decisions",
                "Evaluates bridge round scenarios with insider dynamics, signal risk, and term structuring for existing portfolio companies. Use when considering bridge financing, structuring insider rounds, or analyzing pay-to-play provisions.",
            ),
            (
                "analyzing-competitive-landscapes",
                "Maps competitive dynamics with market positioning, feature comparison, funding histories, and differentiation assessment. Use when analyzing startup competition, mapping market landscapes, or identifying competitive threats.",
            ),
            (
                "conducting-customer-reference-checks",
                "Structures customer diligence with interview guides, NPS analysis, switching cost assessment, and usage pattern evaluation. Use when conducting customer references, validating product-market fit, or assessing customer satisfaction.",
            ),
            (
                "managing-follow-on-investment-decisions",
                "Evaluates pro-rata and follow-on investment decisions with portfolio construction, signaling effects, and reserve management. Use when making follow-on decisions, managing reserves, or evaluating pro-rata rights.",
            ),
            (
                "analyzing-startup-unit-economics",
                "Deconstructs unit economics with CAC, LTV, payback period, gross margin, and contribution margin analysis. Use when analyzing unit economics, validating SaaS metrics, or assessing business model efficiency.",
            ),
            (
                "modeling-venture-fund-economics",
                "Builds LP-level fund models with management fees, carried interest, clawback provisions, and waterfall distributions. Use when modeling fund economics, projecting LP returns, or analyzing fund terms.",
            ),
            (
                "preparing-venture-exit-analyses",
                "Evaluates exit scenarios including IPO, M&A, secondary sale, and recapitalization with timing and return analysis. Use when planning exits, comparing exit routes, or modeling exit outcomes for portfolio companies.",
            ),
        ],
    },
    # ─── 3. PRIVATE EQUITY ────────────────────────────────────────────
    "Private Equity": {
        "description": "Buyout evaluation, LBO modeling, value creation, and fund-level operations",
        "practice_areas": ["Private Equity", "Leveraged Buyouts", "Growth Equity"],
        "skills": [
            (
                "building-leveraged-buyout-models",
                "Constructs LBO models with sources/uses, debt schedules, operating projections, and returns analysis across entry/exit scenarios. Use when modeling leveraged buyouts, calculating sponsor returns, or analyzing leverage capacity.",
            ),
            (
                "evaluating-platform-acquisition-targets",
                "Assesses platform investment opportunities with industry positioning, management quality, organic growth potential, and add-on runway. Use when evaluating platform deals, screening PE investments, or analyzing industry leaders.",
            ),
            (
                "analyzing-add-on-acquisition-candidates",
                "Evaluates bolt-on acquisitions for existing platforms with strategic fit, synergy quantification, and return contribution analysis. Use when screening add-on targets, building platform acquisition strategies, or modeling tuck-in economics.",
            ),
            (
                "structuring-management-equity-programs",
                "Designs management incentive structures with rollover equity, option pools, ratchets, and vesting schedules aligned to value creation. Use when structuring management incentives, designing co-invest programs, or aligning management economics.",
            ),
            (
                "conducting-buyout-operational-diligence",
                "Evaluates target company operations with management assessment, systems review, process maturity, and improvement opportunity identification. Use when conducting ops DD, assessing operational risk, or identifying value creation levers.",
            ),
            (
                "building-value-creation-plans",
                "Structures 100-day and long-term value creation plans with revenue growth, margin improvement, and capital efficiency initiatives. Use when building value creation plans, tracking improvement initiatives, or preparing operating partner reviews.",
            ),
            (
                "managing-sponsor-portfolio-reporting",
                "Structures portfolio company monitoring with monthly financial packages, KPI dashboards, and management assessment frameworks. Use when monitoring portfolio companies, building reporting templates, or tracking financial performance.",
            ),
            (
                "analyzing-debt-capacity-and-structure",
                "Evaluates target leverage capacity with cash flow coverage, stress testing, and optimal debt structure across term loans, revolver, and mezzanine. Use when analyzing debt capacity, structuring acquisition financing, or stress testing leverage.",
            ),
            (
                "modeling-dividend-recapitalizations",
                "Structures dividend recap analysis with leverage impact, credit agreement compliance, and return enhancement calculation. Use when modeling dividend recaps, evaluating interim distributions, or analyzing recapitalization options.",
            ),
            (
                "planning-exit-timing-and-strategy",
                "Evaluates exit alternatives (strategic sale, IPO, secondary, continuation) with market conditions, buyer universe, and return optimization. Use when planning exits, evaluating exit timing, or comparing exit routes.",
            ),
            (
                "conducting-buyout-commercial-diligence",
                "Structures CDD with market sizing, customer concentration, competitive dynamics, and growth sustainability analysis. Use when conducting commercial DD, validating market assumptions, or assessing revenue durability.",
            ),
            (
                "modeling-management-case-scenarios",
                "Builds base, upside, and downside operating scenarios with key assumption sensitivity and return distribution analysis. Use when building operating cases, stress testing projections, or presenting scenario analysis.",
            ),
            (
                "analyzing-sector-investment-theses",
                "Develops PE sector theses with industry mapping, secular trends, fragmentation opportunity, and target universe identification. Use when building sector strategies, mapping investment themes, or identifying subsector opportunities.",
            ),
            (
                "managing-deal-process-execution",
                "Coordinates buy-side deal execution from LOI through closing with workstream tracking, timeline management, and closing conditions. Use when managing deal processes, tracking closing conditions, or coordinating deal teams.",
            ),
            (
                "structuring-co-investment-allocations",
                "Designs co-invest offerings with allocation methodology, LP terms, and fee/carry structure for direct investment opportunities. Use when structuring co-investments, allocating deal capacity, or managing LP co-invest programs.",
            ),
            (
                "analyzing-public-to-private-transactions",
                "Evaluates take-private feasibility with premium analysis, financing capacity, governance considerations, and regulatory requirements. Use when analyzing take-private opportunities, modeling go-private premiums, or assessing delisting mechanics.",
            ),
            (
                "tracking-value-creation-attribution",
                "Decomposes PE returns into revenue growth, margin expansion, multiple expansion, leverage paydown, and multiple contraction components. Use when attributing value creation, analyzing return drivers, or preparing exit case studies.",
            ),
            (
                "managing-operating-partner-engagement",
                "Structures operating partner involvement with portfolio company assignment, initiative tracking, and impact measurement. Use when coordinating operating partners, tracking operational initiatives, or measuring portfolio support impact.",
            ),
            (
                "analyzing-continuation-fund-structures",
                "Evaluates GP-led continuation vehicle structures with existing LP options, pricing methodology, and new investor terms. Use when analyzing continuation vehicles, structuring GP-led transactions, or evaluating tender offers.",
            ),
            (
                "building-pe-fund-performance-reports",
                "Constructs fund-level performance reporting with IRR, MOIC, DPI, RVPI, PME, and vintage year benchmarking. Use when building fund reports, calculating performance metrics, or preparing LP reporting packages.",
            ),
        ],
    },
    # ─── 4. GROWTH EQUITY ─────────────────────────────────────────────
    "Growth Equity": {
        "description": "Late-stage minority and majority investments in scaling companies",
        "practice_areas": [
            "Growth Equity",
            "Expansion Capital",
            "Late-Stage Investing",
        ],
        "skills": [
            (
                "evaluating-growth-stage-companies",
                "Assesses scaling companies with product-market fit validation, unit economics maturity, and growth trajectory sustainability analysis. Use when evaluating growth-stage investments, analyzing scaling businesses, or assessing expansion readiness.",
            ),
            (
                "analyzing-saas-business-metrics",
                "Deconstructs SaaS operating metrics including ARR, NRR, gross retention, magic number, rule of 40, and cohort economics. Use when analyzing SaaS businesses, benchmarking software metrics, or evaluating subscription model health.",
            ),
            (
                "modeling-growth-equity-returns",
                "Builds growth equity return models with minority/majority economics, participation rights, and preference stack analysis. Use when modeling growth equity returns, projecting minority investment outcomes, or analyzing preference structures.",
            ),
            (
                "structuring-minority-protection-rights",
                "Designs minority investor protections including board seats, information rights, consent provisions, and anti-dilution mechanisms. Use when negotiating minority terms, structuring protective provisions, or analyzing governance rights.",
            ),
            (
                "analyzing-go-to-market-efficiency",
                "Evaluates sales efficiency with CAC payback, sales cycle analysis, channel economics, and pipeline conversion metrics. Use when assessing GTM efficiency, analyzing sales productivity, or evaluating distribution strategy.",
            ),
            (
                "conducting-pre-ipo-readiness-assessments",
                "Evaluates IPO preparedness across financial reporting, governance, compliance, and operational maturity dimensions. Use when assessing IPO readiness, identifying pre-IPO gaps, or planning public market transitions.",
            ),
            (
                "modeling-secondary-share-purchases",
                "Structures secondary direct transactions with pricing methodology, transfer restriction analysis, and ROFR navigation. Use when modeling secondary purchases, pricing founder/employee shares, or structuring tender offers.",
            ),
            (
                "analyzing-product-led-growth-metrics",
                "Evaluates PLG dynamics with viral coefficients, freemium conversion, product-qualified leads, and expansion revenue mechanics. Use when analyzing PLG companies, assessing virality, or evaluating product-driven acquisition.",
            ),
            (
                "tracking-net-revenue-retention-dynamics",
                "Monitors NRR components with expansion, contraction, and churn decomposition across customer segments and cohorts. Use when analyzing revenue retention, decomposing NRR drivers, or assessing expansion revenue quality.",
            ),
            (
                "evaluating-marketplace-business-models",
                "Assesses marketplace dynamics with take rate analysis, liquidity metrics, supply/demand balance, and network effect strength. Use when evaluating marketplaces, analyzing take rates, or assessing network effect moats.",
            ),
            (
                "analyzing-burn-multiple-efficiency",
                "Evaluates capital efficiency with burn multiple, net new ARR per dollar burned, and path to profitability analysis. Use when analyzing burn efficiency, assessing capital needs, or modeling runway scenarios.",
            ),
            (
                "structuring-structured-equity-instruments",
                "Designs structured equity with participating preferred, PIK dividends, conversion mechanics, and downside protection features. Use when structuring growth equity instruments, designing preference terms, or modeling structured returns.",
            ),
            (
                "conducting-growth-due-diligence",
                "Structures growth-focused DD with revenue quality, customer concentration, technology scalability, and organizational readiness. Use when conducting growth DD, validating revenue sustainability, or assessing scale capability.",
            ),
            (
                "analyzing-international-expansion-plans",
                "Evaluates geographic expansion strategies with market entry sequencing, localization requirements, and international unit economics. Use when analyzing expansion plans, assessing international readiness, or modeling geo-expansion costs.",
            ),
            (
                "modeling-scenario-based-valuations",
                "Builds probability-weighted valuation models with multiple exit scenarios, timing assumptions, and risk-adjusted returns. Use when building growth equity valuations, modeling scenario-weighted outcomes, or analyzing risk-adjusted returns.",
            ),
            (
                "evaluating-management-team-scalability",
                "Assesses leadership team capacity to scale with organizational design review, key person risk, and executive bench analysis. Use when evaluating management scalability, identifying talent gaps, or assessing organizational readiness.",
            ),
            (
                "analyzing-competitive-moat-durability",
                "Evaluates competitive advantage sustainability with switching costs, network effects, data assets, and brand strength analysis. Use when assessing competitive moats, analyzing defensibility, or evaluating long-term positioning.",
            ),
            (
                "managing-growth-equity-board-governance",
                "Structures board engagement for growth equity investments with meeting cadence, committee design, and information rights. Use when establishing board governance, preparing board materials, or managing investor board relationships.",
            ),
            (
                "analyzing-customer-cohort-economics",
                "Deconstructs customer cohort behavior with retention curves, LTV progression, and vintage-over-vintage comparison analysis. Use when analyzing cohort data, assessing customer quality, or modeling lifetime value trajectories.",
            ),
            (
                "preparing-growth-equity-exit-materials",
                "Structures exit preparation with financial audit readiness, management presentation preparation, and buyer/IPO positioning. Use when preparing for exit, building exit marketing materials, or positioning companies for sale or IPO.",
            ),
        ],
    },
    # ─── 5. EQUITY CAPITAL MARKETS ────────────────────────────────────
    "Equity Capital Markets": {
        "description": "IPO execution, follow-on offerings, and equity-linked issuance",
        "practice_areas": ["ECM", "IPO Advisory", "Equity Origination"],
        "skills": [
            (
                "managing-ipo-execution-processes",
                "Structures IPO execution from organizational meeting through pricing with workstream coordination and timeline management. Use when managing IPOs, coordinating offering processes, or tracking ECM execution milestones.",
            ),
            (
                "analyzing-ipo-valuation-and-pricing",
                "Evaluates IPO pricing with comparable company analysis, IPO discount estimation, and investor demand assessment. Use when pricing IPOs, determining offering ranges, or analyzing IPO valuation methodologies.",
            ),
            (
                "drafting-equity-offering-prospectuses",
                "Structures S-1/F-1 prospectus content with business description, risk factors, MD&A, and financial presentation requirements. Use when preparing IPO prospectuses, drafting SEC filings, or structuring offering documents.",
            ),
            (
                "managing-investor-roadshow-logistics",
                "Coordinates roadshow scheduling with institutional investor targeting, presentation materials, and feedback tracking. Use when managing roadshows, organizing investor meetings, or tracking investor engagement.",
            ),
            (
                "analyzing-follow-on-offering-structures",
                "Evaluates secondary offering types including overnight blocks, marketed deals, ATMs, and bought deals with dilution analysis. Use when analyzing follow-on options, structuring secondary offerings, or evaluating dilution impact.",
            ),
            (
                "modeling-book-building-dynamics",
                "Structures book-building analysis with demand tiers, allocation methodology, and price sensitivity assessment. Use when managing book-building, analyzing investor demand, or optimizing allocation strategies.",
            ),
            (
                "analyzing-equity-linked-instruments",
                "Evaluates convertible bond and mandatory convertible structures with equity sensitivity, credit floor, and Greeks analysis. Use when analyzing convertible offerings, pricing equity-linked instruments, or modeling conversion economics.",
            ),
            (
                "managing-stabilization-and-greenshoe",
                "Structures post-offering stabilization with overallotment option exercise, market support, and penalty bid mechanisms. Use when managing stabilization, exercising greenshoe options, or analyzing aftermarket support.",
            ),
            (
                "analyzing-lock-up-period-dynamics",
                "Evaluates lock-up expiration impact with float analysis, insider selling patterns, and supply overhang assessment. Use when analyzing lock-up expirations, modeling supply dynamics, or assessing post-IPO trading patterns.",
            ),
            (
                "structuring-rights-offerings",
                "Designs rights issue structures with subscription ratios, pricing discounts, and standby underwriting arrangements. Use when structuring rights offerings, analyzing dilution protection, or evaluating capital raise alternatives.",
            ),
            (
                "managing-direct-listing-processes",
                "Structures direct listing execution with opening auction mechanics, reference price methodology, and market maker coordination. Use when executing direct listings, analyzing DL mechanics, or comparing DL vs IPO economics.",
            ),
            (
                "analyzing-spac-transaction-structures",
                "Evaluates SPAC de-SPAC transaction economics with sponsor dilution, redemption risk, PIPE analysis, and warrant impact. Use when analyzing SPAC deals, evaluating sponsor economics, or modeling de-SPAC outcomes.",
            ),
            (
                "managing-at-the-market-programs",
                "Structures ATM offering programs with sales agent selection, volume limitations, and disclosure requirements. Use when establishing ATM programs, managing ongoing equity issuance, or optimizing capital raising timing.",
            ),
            (
                "analyzing-cornerstone-investor-structures",
                "Evaluates cornerstone investment commitments with allocation guarantees, lock-up terms, and signaling value assessment. Use when structuring cornerstone tranches, analyzing anchor investors, or evaluating demand signals.",
            ),
            (
                "conducting-equity-market-windows-analysis",
                "Assesses market receptivity for equity issuance with sector sentiment, volatility, and comparable recent offering performance. Use when timing equity offerings, analyzing market windows, or evaluating issuance conditions.",
            ),
            (
                "modeling-dilution-impact-analysis",
                "Calculates dilutive impact of equity issuance on existing shareholders with EPS, ownership, and NAV per share analysis. Use when modeling dilution, communicating shareholder impact, or comparing capital raise alternatives.",
            ),
            (
                "managing-sec-registration-processes",
                "Coordinates SEC filing workflows with S-1/S-3 preparation, comment letter responses, and effectiveness timing. Use when managing SEC registration, responding to SEC comments, or tracking filing status.",
            ),
            (
                "analyzing-institutional-investor-demand",
                "Maps institutional investor targeting with AUM analysis, sector allocation preferences, and historical participation patterns. Use when targeting investors, analyzing demand profiles, or building investor marketing lists.",
            ),
            (
                "structuring-employee-stock-offerings",
                "Designs ESPP and directed share programs with eligibility, pricing mechanics, and regulatory compliance requirements. Use when structuring employee offerings, designing share purchase plans, or managing directed share allocations.",
            ),
            (
                "preparing-equity-capital-markets-updates",
                "Synthesizes ECM market conditions with recent pricing, sector performance, and pipeline activity for client communication. Use when preparing market updates, summarizing ECM activity, or advising on market timing.",
            ),
        ],
    },
    # ─── 6. DEBT CAPITAL MARKETS ──────────────────────────────────────
    "Debt Capital Markets": {
        "description": "Bond issuance, loan syndication, and debt origination across investment grade and high yield",
        "practice_areas": ["DCM", "Leveraged Finance", "Debt Origination"],
        "skills": [
            (
                "structuring-bond-offerings",
                "Designs bond offering structures with tenor, coupon, call provisions, covenant packages, and pricing methodology. Use when structuring bond deals, selecting debt parameters, or comparing issuance alternatives.",
            ),
            (
                "managing-loan-syndication-processes",
                "Coordinates leveraged loan syndication from mandate through closing with lender marketing, commitment tracking, and flex analysis. Use when syndicating loans, managing lender groups, or tracking commitment levels.",
            ),
            (
                "drafting-offering-memoranda-debt",
                "Creates debt offering memoranda with credit overview, financial analysis, industry section, and risk factors for investor marketing. Use when preparing debt OMs, writing credit marketing materials, or structuring lender presentations.",
            ),
            (
                "analyzing-covenant-packages",
                "Evaluates financial and incurrence covenant packages with headroom analysis, definition review, and covenant-lite comparison. Use when analyzing loan covenants, negotiating covenant levels, or assessing borrower flexibility.",
            ),
            (
                "modeling-debt-capacity-analysis",
                "Calculates borrower debt capacity with cash flow coverage, leverage multiples, and stress-tested servicing ability. Use when sizing debt facilities, analyzing leverage capacity, or determining optimal capital structure.",
            ),
            (
                "analyzing-high-yield-bond-structures",
                "Evaluates high-yield issuance with call schedules, change of control puts, and restricted payment baskets. Use when analyzing HY bonds, comparing HY vs leveraged loan terms, or assessing issuer flexibility.",
            ),
            (
                "structuring-revolving-credit-facilities",
                "Designs revolver structures with commitment amounts, borrowing base mechanics, letter of credit sub-facilities, and pricing grids. Use when structuring revolvers, designing borrowing bases, or analyzing liquidity facilities.",
            ),
            (
                "analyzing-investment-grade-issuance",
                "Evaluates IG bond market conditions with spread analysis, maturity curve optimization, and investor demand assessment. Use when advising IG issuers, analyzing credit spreads, or timing IG bond offerings.",
            ),
            (
                "managing-bridge-loan-commitments",
                "Structures bridge financing with commitment terms, flex provisions, and permanent takeout analysis for acquisition financing. Use when arranging bridge facilities, analyzing flex economics, or managing bridge-to-bond transitions.",
            ),
            (
                "analyzing-mezzanine-and-subordinated-debt",
                "Evaluates mezzanine structures with PIK toggle, equity kickers, and intercreditor subordination mechanics. Use when analyzing mezzanine financing, comparing subordinated debt terms, or modeling layered capital structures.",
            ),
            (
                "structuring-term-loan-b-facilities",
                "Designs institutional term loan structures with amortization schedules, repricing protection, and soft call provisions. Use when structuring TLBs, analyzing institutional loan terms, or comparing bank vs institutional debt.",
            ),
            (
                "analyzing-credit-facility-amendments",
                "Evaluates amendment and waiver requests with consent requirements, fee structures, and modified term impact analysis. Use when analyzing amendments, structuring consent solicitations, or evaluating covenant relief requests.",
            ),
            (
                "modeling-debt-maturity-profiles",
                "Structures debt maturity analysis with refinancing risk, market access assumptions, and liability management opportunities. Use when analyzing maturity walls, planning refinancing, or optimizing debt tenor.",
            ),
            (
                "analyzing-unitranche-financing",
                "Evaluates unitranche structures with first-out/last-out splits, blended pricing, and agreement among lenders provisions. Use when analyzing unitranche options, comparing unitranche vs traditional structures, or modeling blended costs.",
            ),
            (
                "managing-debt-private-placements",
                "Coordinates private placement execution with investor targeting, NAIC designation analysis, and shelf registration requirements. Use when managing PP offerings, targeting insurance company investors, or structuring private notes.",
            ),
            (
                "analyzing-sustainable-debt-structures",
                "Evaluates green bonds, sustainability-linked bonds, and social bonds with KPI selection, step-up mechanics, and framework assessment. Use when structuring ESG-linked debt, analyzing sustainability frameworks, or evaluating green bond eligibility.",
            ),
            (
                "structuring-asset-based-lending",
                "Designs ABL facilities with borrowing base calculations, collateral eligibility criteria, and field exam requirements. Use when structuring ABL facilities, calculating borrowing availability, or analyzing collateral pools.",
            ),
            (
                "analyzing-credit-rating-advisory",
                "Prepares credit rating agency presentations with methodology alignment, peer positioning, and target rating analysis. Use when advising on credit ratings, preparing rating agency meetings, or analyzing rating methodology impact.",
            ),
            (
                "conducting-debt-market-conditions-analysis",
                "Synthesizes DCM market activity with new issue spreads, fund flows, and market technical analysis for issuance timing. Use when analyzing debt market windows, timing bond issuance, or assessing market receptivity.",
            ),
            (
                "modeling-interest-rate-hedging-strategies",
                "Structures interest rate hedging programs with swap analysis, cap/floor evaluation, and hedge accounting documentation. Use when designing rate hedges, comparing hedging instruments, or analyzing hedge effectiveness.",
            ),
        ],
    },
    # ─── 7. STRUCTURED FINANCE ────────────────────────────────────────
    "Structured Finance": {
        "description": "Securitization, ABS/MBS/CLO structuring, and cash flow waterfall analysis",
        "practice_areas": ["Structured Finance", "Securitization", "ABS/MBS/CLO"],
        "skills": [
            (
                "structuring-abs-transactions",
                "Designs asset-backed securitization structures with tranche hierarchy, credit enhancement, and cash flow allocation mechanics. Use when structuring ABS deals, designing tranche waterfall, or analyzing credit enhancement levels.",
            ),
            (
                "modeling-clo-cash-flow-waterfalls",
                "Builds CLO waterfall models with coverage tests, reinvestment criteria, and distribution allocation across tranches. Use when modeling CLO structures, analyzing OC/IC tests, or projecting tranche returns.",
            ),
            (
                "analyzing-mortgage-backed-securities",
                "Evaluates MBS structures with prepayment modeling (CPR/CDR), collateral analysis, and tranche-level credit risk assessment. Use when analyzing MBS, modeling prepayment scenarios, or evaluating residential mortgage pools.",
            ),
            (
                "conducting-collateral-pool-analysis",
                "Assesses underlying asset pools with stratification, concentration analysis, historical performance, and credit quality distribution. Use when analyzing collateral pools, stratifying asset characteristics, or evaluating pool quality.",
            ),
            (
                "modeling-credit-enhancement-requirements",
                "Calculates required credit enhancement levels with loss modeling, attachment/detachment points, and rating agency methodology. Use when sizing credit enhancement, modeling loss scenarios, or determining tranche subordination.",
            ),
            (
                "structuring-commercial-mortgage-securitization",
                "Designs CMBS structures with property-level underwriting, DSCR analysis, and loan-level credit assessment. Use when structuring CMBS deals, underwriting commercial mortgage pools, or analyzing property cash flows.",
            ),
            (
                "analyzing-servicer-performance",
                "Evaluates master and special servicer performance with delinquency management, modification outcomes, and loss mitigation effectiveness. Use when assessing servicer quality, monitoring servicing metrics, or evaluating servicer transfers.",
            ),
            (
                "modeling-prepayment-and-default-scenarios",
                "Builds CPR/CDR/severity vectors with scenario analysis across interest rate and economic environments. Use when modeling prepayment behavior, projecting default scenarios, or stress testing pool performance.",
            ),
            (
                "structuring-whole-business-securitizations",
                "Designs whole business securitization with IP collateral, franchise cash flows, and operating covenant structures. Use when structuring WBS transactions, analyzing franchise securitizations, or evaluating non-traditional collateral.",
            ),
            (
                "analyzing-structured-product-ratings",
                "Evaluates rating agency methodology application with loss model inputs, correlation assumptions, and tranche-level credit assessment. Use when analyzing structured product ratings, comparing agency methodologies, or assessing rating sensitivity.",
            ),
            (
                "modeling-revolving-period-structures",
                "Builds revolving securitization models with replenishment criteria, early amortization triggers, and portfolio composition limits. Use when modeling revolving structures, analyzing credit card ABS, or evaluating asset purchase criteria.",
            ),
            (
                "structuring-clo-reinvestment-periods",
                "Designs CLO reinvestment criteria with portfolio quality tests, trading guidelines, and concentration limits. Use when structuring CLO reinvestment, setting portfolio constraints, or analyzing manager flexibility.",
            ),
            (
                "analyzing-tranche-relative-value",
                "Evaluates structured product tranche pricing with spread analysis, yield attribution, and comparable structure benchmarking. Use when assessing tranche value, comparing structured product pricing, or analyzing spread components.",
            ),
            (
                "conducting-reg-ab-compliance",
                "Structures Regulation AB II compliance with asset-level data requirements, servicer reporting, and shelf registration eligibility. Use when ensuring Reg AB compliance, preparing ABS reporting, or structuring shelf eligibility.",
            ),
            (
                "modeling-interest-rate-and-basis-risk",
                "Analyzes structural interest rate exposure with fixed/floating mismatch, basis risk, and cap/floor adequacy assessment. Use when modeling structural rate risk, analyzing basis risk, or evaluating interest rate hedging needs.",
            ),
            (
                "structuring-risk-retention-compliance",
                "Designs risk retention structures meeting US and EU requirements with vertical, horizontal, and L-shaped retention options. Use when structuring risk retention, analyzing sponsor retention alternatives, or ensuring regulatory compliance.",
            ),
            (
                "analyzing-esoteric-abs-collateral",
                "Evaluates non-traditional securitization collateral including solar, data centers, digital infrastructure, and IP royalties. Use when analyzing esoteric ABS, evaluating non-standard collateral, or structuring novel asset classes.",
            ),
            (
                "managing-securitization-warehouse-facilities",
                "Structures warehouse lending for securitization programs with advance rates, eligibility criteria, and ramp-up analysis. Use when managing warehouse lines, structuring ramp facilities, or analyzing warehouse economics.",
            ),
            (
                "analyzing-synthetic-securitization-structures",
                "Evaluates synthetic CDO and CRT structures with credit default swap mechanics and funded/unfunded tranche analysis. Use when analyzing synthetic structures, evaluating credit risk transfer, or modeling CDS-based securitizations.",
            ),
            (
                "conducting-structured-finance-surveillance",
                "Monitors structured product performance with collateral deterioration triggers, coverage test tracking, and credit migration analysis. Use when conducting ABS surveillance, monitoring CLO performance, or tracking structured product credit.",
            ),
        ],
    },
    # ─── 8. DISTRESSED DEBT & RESTRUCTURING ───────────────────────────
    "Distressed and Restructuring": {
        "description": "Distressed investing, Chapter 11 processes, and corporate restructuring",
        "practice_areas": ["Restructuring", "Distressed Investing", "Turnaround"],
        "skills": [
            (
                "analyzing-distressed-credit-situations",
                "Evaluates distressed debt opportunities with recovery analysis, liquidity assessment, and potential restructuring outcomes. Use when screening distressed situations, analyzing stressed credits, or evaluating workout scenarios.",
            ),
            (
                "modeling-chapter-11-recovery-waterfalls",
                "Builds recovery waterfall models with absolute priority, secured vs unsecured claims, and plan of reorganization distribution analysis. Use when modeling bankruptcy recoveries, analyzing claim priorities, or estimating creditor distributions.",
            ),
            (
                "conducting-liquidity-and-viability-analysis",
                "Assesses going-concern viability with 13-week cash flow models, liquidity runway, and critical vendor analysis. Use when evaluating liquidity crises, building 13-week models, or assessing near-term solvency.",
            ),
            (
                "structuring-debtor-in-possession-financing",
                "Designs DIP financing structures with priming liens, adequate protection, and budget milestones for Chapter 11 proceedings. Use when structuring DIP facilities, analyzing superpriority claims, or evaluating DIP terms.",
            ),
            (
                "analyzing-section-363-asset-sales",
                "Evaluates 363 sale processes with stalking horse protections, bid procedures, and credit bidding mechanics. Use when analyzing 363 sales, structuring stalking horse bids, or evaluating asset sale alternatives.",
            ),
            (
                "building-restructuring-plan-models",
                "Constructs plan of reorganization models with debt-for-equity conversion, new money injection, and emergence capital structure. Use when modeling restructuring plans, designing emergence capital structures, or analyzing plan feasibility.",
            ),
            (
                "analyzing-claims-trading-dynamics",
                "Evaluates claims trading market with trading levels, holder identification, and blocking position analysis. Use when analyzing claims markets, tracking distressed debt trading, or evaluating ad hoc group dynamics.",
            ),
            (
                "conducting-fulcrum-security-analysis",
                "Identifies fulcrum securities in distressed capital structures with enterprise value allocation and recovery sensitivity analysis. Use when analyzing fulcrum securities, estimating recovery ranges, or determining value breaks.",
            ),
            (
                "managing-out-of-court-workout-processes",
                "Structures exchange offers, consent solicitations, and amend-and-extend transactions as Chapter 11 alternatives. Use when managing out-of-court workouts, designing exchange offers, or structuring pre-negotiated deals.",
            ),
            (
                "analyzing-executory-contract-decisions",
                "Evaluates assumption, rejection, and assignment decisions for executory contracts and unexpired leases in bankruptcy. Use when analyzing contract decisions, evaluating lease rejections, or modeling cure cost exposure.",
            ),
            (
                "modeling-fresh-start-accounting",
                "Structures fresh-start accounting analysis with reorganization value allocation, new basis determination, and emergence balance sheet. Use when modeling fresh-start accounting, preparing emergence financials, or allocating reorganization value.",
            ),
            (
                "analyzing-fraudulent-transfer-exposure",
                "Evaluates fraudulent conveyance risk for leveraged transactions with solvency analysis and reasonably equivalent value assessment. Use when analyzing fraudulent transfer risk, conducting solvency tests, or evaluating historical transactions.",
            ),
            (
                "structuring-exit-financing-packages",
                "Designs emergence financing structures with exit term loans, ABL facilities, and capital structure optimization for reorganized entities. Use when structuring exit financing, analyzing emergence capital needs, or comparing financing alternatives.",
            ),
            (
                "analyzing-make-whole-and-redemption-claims",
                "Evaluates make-whole premium claims in bankruptcy with contract interpretation, present value disputes, and secured status analysis. Use when analyzing make-whole claims, evaluating redemption disputes, or assessing premium recovery.",
            ),
            (
                "managing-creditor-committee-activities",
                "Structures official committee operations with financial advisor engagement, investigation scope, and plan negotiation strategy. Use when supporting creditor committees, coordinating committee advisors, or analyzing committee positions.",
            ),
            (
                "analyzing-liability-management-transactions",
                "Evaluates uptier exchanges, drop-down transactions, and covenant-stripping maneuvers as aggressive liability management tools. Use when analyzing LMTs, evaluating creditor-on-creditor violence, or assessing cooperation agreement strategies.",
            ),
            (
                "conducting-operational-turnaround-analysis",
                "Assesses operational improvement opportunities with cost rationalization, revenue stabilization, and management changes for distressed businesses. Use when evaluating turnaround plans, identifying operational improvements, or assessing management capability.",
            ),
            (
                "analyzing-cross-border-insolvency",
                "Evaluates multi-jurisdictional restructuring with Chapter 15 recognition, COMI analysis, and parallel proceeding coordination. Use when analyzing cross-border insolvency, assessing jurisdiction selection, or coordinating multi-country restructurings.",
            ),
            (
                "modeling-tax-attribute-preservation",
                "Analyzes NOL and tax attribute preservation strategies under Section 382 limitations in ownership change scenarios. Use when modeling tax attribute preservation, analyzing 382 limitations, or structuring ownership change thresholds.",
            ),
            (
                "preparing-disclosure-statement-analysis",
                "Evaluates Chapter 11 disclosure statements with plan description adequacy, feasibility projections, and liquidation analysis comparison. Use when reviewing disclosure statements, analyzing plan feasibility, or preparing objections.",
            ),
        ],
    },
    # ─── 9. SECONDARY MARKETS & GP-LED TRANSACTIONS ───────────────────
    "Secondaries and GP-Led": {
        "description": "LP interest transactions, continuation vehicles, and secondary market dynamics",
        "practice_areas": [
            "Secondaries",
            "GP-Led Transactions",
            "LP Portfolio Management",
        ],
        "skills": [
            (
                "pricing-lp-interest-portfolios",
                "Evaluates LP interest portfolios with fund-by-fund NAV assessment, J-curve positioning, and portfolio-level pricing methodology. Use when pricing secondary portfolios, evaluating LP interest bids, or analyzing fund vintages.",
            ),
            (
                "structuring-gp-led-continuation-vehicles",
                "Designs GP-led continuation fund structures with rollover mechanics, new money terms, and existing LP election options. Use when structuring continuation vehicles, designing rollover terms, or analyzing GP-led economics.",
            ),
            (
                "analyzing-secondary-market-pricing",
                "Monitors secondary market pricing trends with discount/premium analysis, bid-ask spreads, and market-clearing dynamics. Use when analyzing secondary pricing, tracking market trends, or benchmarking transaction levels.",
            ),
            (
                "modeling-strip-and-tail-transactions",
                "Builds strip and tail-end fund models with remaining portfolio analysis, unfunded obligation treatment, and duration-adjusted pricing. Use when modeling strip deals, evaluating tail-end portfolios, or analyzing remaining value.",
            ),
            (
                "conducting-secondary-due-diligence",
                "Structures buy-side DD for secondary transactions with underlying fund analysis, manager assessment, and portfolio-level risk evaluation. Use when conducting secondary DD, evaluating fund managers, or analyzing underlying portfolios.",
            ),
            (
                "managing-tender-offer-processes",
                "Coordinates tender offer execution with offer terms, election mechanics, proration, and transfer documentation for LP interests. Use when managing tender offers, structuring LP elections, or coordinating interest transfers.",
            ),
            (
                "analyzing-unfunded-commitment-exposure",
                "Evaluates unfunded commitment obligations with call probability, pacing models, and portfolio-level exposure management. Use when analyzing unfunded exposure, managing commitment pacing, or stress testing capital calls.",
            ),
            (
                "structuring-preferred-equity-solutions",
                "Designs NAV-based and structured preferred equity facilities with overcollateralization, coverage tests, and waterfall mechanics. Use when structuring preferred equity, analyzing NAV lending, or evaluating fund-level leverage.",
            ),
            (
                "modeling-fund-of-funds-secondaries",
                "Evaluates fund-of-funds secondary transactions with layer-on-layer fee analysis, double-carry impact, and net return adjustment. Use when pricing FoF secondaries, analyzing fee drag, or modeling net LP economics.",
            ),
            (
                "analyzing-stapled-transaction-structures",
                "Evaluates stapled secondary structures combining primary commitment with secondary purchase in coordinated transactions. Use when analyzing stapled deals, structuring combined primary/secondary, or evaluating staple economics.",
            ),
            (
                "managing-transfer-restriction-navigation",
                "Navigates LP transfer requirements including GP consent, ROFR compliance, and partnership agreement transfer provisions. Use when managing LP transfers, obtaining GP consent, or navigating transfer restrictions.",
            ),
            (
                "analyzing-single-asset-continuation-vehicles",
                "Evaluates single-asset GP-led transactions with stand-alone asset valuation, financing structure, and rolling LP vs cashing out analysis. Use when analyzing single-asset CVs, evaluating trophy asset transactions, or structuring single-asset rolls.",
            ),
            (
                "conducting-manager-track-record-analysis",
                "Assesses GP track records for secondary pricing with fund-level attribution, unrealized portfolio assessment, and consistency analysis. Use when evaluating GP track records, analyzing fund performance consistency, or assessing manager quality.",
            ),
            (
                "modeling-j-curve-adjusted-pricing",
                "Builds pricing models incorporating J-curve positioning with blind pool risk, early-vintage assessment, and age-weighted adjustments. Use when pricing early-vintage funds, analyzing J-curve risk, or adjusting for fund maturity.",
            ),
            (
                "structuring-deferred-payment-mechanisms",
                "Designs deferred and contingent payment structures for secondary transactions with earnout mechanics and escrow arrangements. Use when structuring deferred payments, designing earnout mechanisms, or managing payment timing.",
            ),
            (
                "analyzing-secondary-credit-facilities",
                "Evaluates secondary-focused credit facilities with leverage terms, borrowing base mechanics, and portfolio pledging requirements. Use when analyzing secondary lending, structuring portfolio leverage, or evaluating fund finance options.",
            ),
            (
                "managing-portfolio-construction-secondaries",
                "Structures secondary portfolio construction with vintage diversification, strategy mix, and geographic allocation optimization. Use when building secondary portfolios, managing allocation targets, or optimizing portfolio composition.",
            ),
            (
                "analyzing-real-estate-secondaries",
                "Evaluates real estate fund secondary transactions with NAV validation, property-level assessment, and sector/vintage analysis. Use when pricing RE secondaries, analyzing property portfolios, or evaluating REIT fund interests.",
            ),
            (
                "conducting-infrastructure-secondary-analysis",
                "Assesses infrastructure fund secondaries with asset-level cash flow analysis, concession period evaluation, and regulatory risk assessment. Use when analyzing infra secondaries, evaluating infrastructure assets, or pricing infra fund interests.",
            ),
            (
                "preparing-secondary-market-reports",
                "Synthesizes secondary market activity with volume trends, pricing benchmarks, and deal type composition for market participants. Use when preparing market reports, analyzing secondary volumes, or tracking market evolution.",
            ),
        ],
    },
    # ─── 10. FUND FORMATION & STRUCTURING ─────────────────────────────
    "Fund Formation and Structuring": {
        "description": "Fund vehicle design, LP/GP economics, and partnership documentation",
        "practice_areas": ["Fund Formation", "Fund Structuring", "Partnership Law"],
        "skills": [
            (
                "structuring-fund-vehicle-architecture",
                "Designs fund legal structures with master-feeder, parallel fund, and blocker entity configurations for tax-efficient investor access. Use when designing fund structures, selecting vehicle types, or optimizing multi-jurisdictional access.",
            ),
            (
                "modeling-carried-interest-mechanics",
                "Builds carry waterfall models with preferred return hurdles, catch-up provisions, and clawback mechanics across deal-by-deal and whole-fund structures. Use when modeling carry economics, comparing waterfall structures, or analyzing GP incentive alignment.",
            ),
            (
                "drafting-limited-partnership-agreements",
                "Structures LPA terms with investment period, harvesting period, key person provisions, and investor governance rights. Use when preparing LPA terms, negotiating fund documents, or summarizing partnership provisions.",
            ),
            (
                "analyzing-management-fee-structures",
                "Evaluates management fee designs with commitment-period vs invested-capital bases, step-downs, and offset provisions. Use when analyzing fee structures, comparing fee levels, or modeling fee revenue for GPs.",
            ),
            (
                "structuring-side-letter-provisions",
                "Designs side letter accommodations with MFN rights, capacity reservations, co-invest rights, and reporting enhancements. Use when negotiating side letters, analyzing MFN obligations, or structuring LP-specific terms.",
            ),
            (
                "managing-fund-formation-processes",
                "Coordinates fundraising execution with PPM preparation, DDQ completion, legal documentation, and closing mechanics. Use when managing fund launches, coordinating formation processes, or tracking fundraising milestones.",
            ),
            (
                "analyzing-gp-commitment-structures",
                "Evaluates GP capital commitment levels with co-invest obligations, management company funding, and alignment assessment. Use when analyzing GP commitment, assessing alignment, or structuring GP capital contributions.",
            ),
            (
                "structuring-fund-of-funds-vehicles",
                "Designs fund-of-funds structures with layer-on-layer economics, allocation methodology, and portfolio construction guidelines. Use when structuring FoF vehicles, analyzing layered fee impact, or designing multi-manager programs.",
            ),
            (
                "modeling-fund-economics-sensitivity",
                "Builds fund economic models with sensitivity across deployment pace, exit multiples, and fee/carry structures for LP and GP returns. Use when modeling fund economics, projecting LP net returns, or analyzing fee-adjusted performance.",
            ),
            (
                "analyzing-key-person-event-provisions",
                "Evaluates key person clause triggers, consequences, and cure mechanics in partnership documentation. Use when analyzing key person provisions, assessing management stability risk, or structuring departure protections.",
            ),
            (
                "structuring-co-investment-vehicles",
                "Designs co-investment fund structures with deal-specific and programmatic formats, fee terms, and allocation methodology. Use when structuring co-invest programs, designing deal-specific vehicles, or analyzing co-invest economics.",
            ),
            (
                "analyzing-investor-advisory-committees",
                "Structures IAC/LPAC design with composition, authority scope, conflict review protocols, and valuation oversight. Use when designing advisory committees, defining LPAC authority, or structuring conflict resolution processes.",
            ),
            (
                "managing-regulatory-fund-compliance",
                "Coordinates fund regulatory requirements across SEC, AIFMD, and local jurisdiction registration, reporting, and compliance obligations. Use when managing fund compliance, navigating regulatory registration, or ensuring cross-border compliance.",
            ),
            (
                "structuring-fund-level-credit-facilities",
                "Designs subscription credit facilities with LP commitment-based lending, borrowing base mechanics, and advance rate analysis. Use when structuring fund lines, analyzing subscription facilities, or evaluating fund-level leverage.",
            ),
            (
                "analyzing-seed-and-anchor-investor-terms",
                "Evaluates seed/anchor investor economics with revenue sharing, fee discounts, capacity reservations, and governance rights. Use when analyzing seed terms, structuring anchor economics, or evaluating founding investor arrangements.",
            ),
            (
                "structuring-permanent-capital-vehicles",
                "Designs permanent capital structures including listed vehicles, evergreen funds, and non-traded REITs with perpetual-life governance. Use when structuring permanent capital, analyzing evergreen mechanics, or designing listed fund vehicles.",
            ),
            (
                "modeling-waterfall-distribution-mechanics",
                "Builds distribution waterfall models with European vs American style carry, preferred return accrual, and GP clawback calculation. Use when modeling distribution waterfalls, comparing carry structures, or calculating LP distributions.",
            ),
            (
                "analyzing-erisa-and-benefit-plan-compliance",
                "Evaluates ERISA plan asset rules with 25% test, VCOC/REOC exemptions, and benefit plan investor tracking. Use when analyzing ERISA compliance, structuring plan asset exemptions, or managing benefit plan investor thresholds.",
            ),
            (
                "structuring-opportunity-zone-funds",
                "Designs Qualified Opportunity Zone fund structures with investment timeline requirements, substantial improvement tests, and tax benefit mechanics. Use when structuring OZ funds, analyzing QOF requirements, or evaluating OZ tax benefits.",
            ),
            (
                "preparing-private-placement-memoranda",
                "Creates fund PPM documentation with investment strategy, risk factors, fee disclosure, and regulatory compliance for fund marketing. Use when preparing PPMs, drafting fund marketing materials, or structuring offering documentation.",
            ),
        ],
    },
    # ─── 11. INVESTOR RELATIONS & LP REPORTING ────────────────────────
    "Investor Relations and LP Reporting": {
        "description": "Capital call/distribution management, performance reporting, and LP communications",
        "practice_areas": ["Investor Relations", "LP Reporting", "Fund Administration"],
        "skills": [
            (
                "managing-capital-call-processes",
                "Structures capital call execution with notice preparation, pro-rata allocation, default remedy provisions, and wire coordination. Use when processing capital calls, calculating LP contributions, or managing call logistics.",
            ),
            (
                "calculating-fund-performance-metrics",
                "Computes fund performance with gross/net IRR, MOIC, DPI, RVPI, TVPI, PME, and direct alpha methodologies. Use when calculating fund performance, reconciling return metrics, or benchmarking against peer groups.",
            ),
            (
                "preparing-quarterly-lp-reports",
                "Creates comprehensive quarterly LP reporting packages with fund performance, portfolio updates, and market commentary. Use when preparing quarterly reports, building LP update packages, or structuring fund communications.",
            ),
            (
                "managing-distribution-waterfall-calculations",
                "Executes distribution calculations through partnership waterfall with preferred return, GP catch-up, and carried interest allocation. Use when calculating distributions, processing waterfall mechanics, or determining carry payments.",
            ),
            (
                "structuring-annual-meeting-materials",
                "Prepares annual meeting presentations with fund performance review, market outlook, pipeline discussion, and LP Q&A preparation. Use when preparing AGM materials, structuring LP presentations, or coordinating annual meetings.",
            ),
            (
                "managing-investor-due-diligence-responses",
                "Coordinates DDQ completion with standardized responses, data room preparation, and reference call management for prospective LPs. Use when responding to LP DD, completing DDQs, or managing investor onboarding processes.",
            ),
            (
                "preparing-fund-valuation-reports",
                "Structures fund NAV reporting with investment-level valuations, methodology disclosure, and fair value hierarchy classification. Use when preparing NAV reports, documenting valuation methodology, or presenting fair value analysis.",
            ),
            (
                "managing-investor-portal-content",
                "Structures investor portal organization with document hierarchy, access permissions, and communication archive management. Use when managing investor portals, organizing LP documentation, or maintaining investor communication records.",
            ),
            (
                "analyzing-commitment-pacing-models",
                "Builds LP commitment pacing with deployment curves, distribution assumptions, and NAV projection for portfolio planning. Use when modeling commitment pacing, projecting LP cash flows, or planning new fund allocations.",
            ),
            (
                "preparing-k1-and-tax-reporting-packages",
                "Coordinates partner tax reporting with Schedule K-1 preparation, PFIC reporting, and state filing requirements. Use when preparing K-1 packages, coordinating tax reporting, or managing partner tax communication.",
            ),
            (
                "structuring-investor-segmentation",
                "Designs LP segmentation with tiered communication, access differentiation, and relationship management frameworks. Use when segmenting investor base, designing communication strategies, or managing LP relationships.",
            ),
            (
                "managing-secondary-transfer-requests",
                "Processes LP interest transfer requests with GP consent evaluation, ROFR administration, and transfer documentation requirements. Use when managing LP transfers, evaluating transfer requests, or coordinating interest assignments.",
            ),
            (
                "preparing-esg-and-impact-reporting",
                "Structures ESG and impact reporting for fund investors with metric collection, framework alignment, and progress communication. Use when preparing ESG reports, collecting impact data, or aligning with reporting frameworks.",
            ),
            (
                "managing-investor-compliance-requests",
                "Coordinates regulatory and compliance information requests from institutional LPs including FOIA, regulatory filings, and audit support. Use when responding to compliance requests, managing FOIA inquiries, or supporting LP audit processes.",
            ),
            (
                "analyzing-investor-concentration-risk",
                "Monitors LP base composition with concentration analysis, redemption risk, and re-up probability assessment. Use when analyzing investor concentration, assessing re-up risk, or managing LP base diversification.",
            ),
            (
                "preparing-deal-attribution-analysis",
                "Structures investment-level performance attribution with return decomposition, timing analysis, and value driver identification. Use when preparing deal attribution, analyzing investment returns, or building exit case studies.",
            ),
            (
                "managing-co-investment-reporting",
                "Structures co-investment reporting with deal-level performance, fee/carry calculations, and co-invest program aggregate analysis. Use when reporting co-invest performance, tracking deal-level returns, or preparing co-invest summaries.",
            ),
            (
                "conducting-peer-benchmarking-analysis",
                "Evaluates fund performance against peer universes with vintage year comparison, quartile ranking, and strategy-specific benchmarking. Use when benchmarking fund performance, analyzing vintage comparisons, or assessing relative positioning.",
            ),
            (
                "managing-denominator-effect-analysis",
                "Evaluates LP portfolio rebalancing pressure from denominator effects with over-allocation analysis and pace adjustment recommendations. Use when analyzing denominator effects, assessing LP allocation constraints, or modeling portfolio rebalancing.",
            ),
            (
                "preparing-fundraising-pipeline-reports",
                "Tracks fundraising progress with prospect pipeline, commitment tracking, and closing projection for fund formation processes. Use when monitoring fundraising, tracking LP commitments, or projecting fund closing timelines.",
            ),
        ],
    },
    # ─── 12. INFRASTRUCTURE & PROJECT FINANCE ─────────────────────────
    "Infrastructure and Project Finance": {
        "description": "Project development, concession analysis, and infrastructure investment evaluation",
        "practice_areas": ["Project Finance", "Infrastructure Investment", "PPP"],
        "skills": [
            (
                "modeling-project-finance-structures",
                "Builds project finance models with construction period draws, operational cash flows, DSCR covenants, and sculpted debt repayment. Use when modeling project finance, calculating debt service coverage, or structuring project lending.",
            ),
            (
                "evaluating-concession-agreements",
                "Analyzes concession terms with revenue sharing, performance requirements, hand-back conditions, and termination provisions. Use when evaluating concessions, analyzing PPP contracts, or assessing concession economics.",
            ),
            (
                "analyzing-infrastructure-asset-valuations",
                "Values infrastructure assets with DCF, regulated asset base, and comparable transaction methodologies adjusted for regulatory and contractual frameworks. Use when valuing infrastructure assets, analyzing regulated utilities, or benchmarking infra transactions.",
            ),
            (
                "conducting-traffic-and-demand-studies",
                "Evaluates demand forecasts for toll roads, airports, and ports with independent engineer review and scenario sensitivity analysis. Use when analyzing traffic studies, validating demand forecasts, or stress testing revenue projections.",
            ),
            (
                "structuring-public-private-partnerships",
                "Designs PPP structures with risk allocation, availability payment mechanisms, and value-for-money analysis for public sponsors. Use when structuring PPPs, analyzing risk allocation, or evaluating VfM for public sector clients.",
            ),
            (
                "analyzing-renewable-energy-project-finance",
                "Evaluates renewable energy project economics with PPA structures, merchant tail risk, and production profile analysis. Use when analyzing wind/solar projects, evaluating PPA terms, or modeling renewable energy cash flows.",
            ),
            (
                "modeling-construction-period-risk",
                "Analyzes construction risk with EPC contract review, delay and cost overrun scenarios, and completion guarantee structures. Use when modeling construction risk, evaluating EPC terms, or stress testing project timelines.",
            ),
            (
                "analyzing-regulatory-rate-structures",
                "Evaluates regulated utility rate-setting with RAB methodology, allowed return analysis, and regulatory reset risk assessment. Use when analyzing regulatory frameworks, modeling rate cases, or evaluating allowed return mechanics.",
            ),
            (
                "structuring-infrastructure-debt-facilities",
                "Designs infrastructure lending with mini-perm structures, cash sweep mechanics, and maintenance/distribution covenants. Use when structuring project debt, designing covenant packages, or analyzing infrastructure lending terms.",
            ),
            (
                "conducting-infrastructure-due-diligence",
                "Structures infrastructure DD with technical assessment, regulatory review, environmental analysis, and community impact evaluation. Use when conducting infra DD, evaluating asset condition, or assessing regulatory risk.",
            ),
            (
                "analyzing-transportation-infrastructure",
                "Evaluates transportation assets with ridership analysis, fare structure assessment, and operating efficiency benchmarking. Use when analyzing transportation projects, evaluating mass transit, or assessing toll road economics.",
            ),
            (
                "modeling-energy-transition-infrastructure",
                "Assesses energy transition investments with battery storage, grid modernization, EV charging, and hydrogen infrastructure analysis. Use when modeling energy transition assets, evaluating storage economics, or analyzing grid infrastructure.",
            ),
            (
                "analyzing-digital-infrastructure-assets",
                "Evaluates data centers, fiber networks, and tower assets with capacity analysis, tenant credit, and technology obsolescence risk. Use when analyzing digital infrastructure, evaluating tower portfolios, or assessing data center investments.",
            ),
            (
                "structuring-infrastructure-fund-terms",
                "Designs infrastructure fund structures with longer fund lives, NAV-based distributions, and co-investment programs for illiquid assets. Use when structuring infra funds, designing open-ended vehicles, or analyzing infrastructure fund terms.",
            ),
            (
                "analyzing-water-and-waste-infrastructure",
                "Evaluates water treatment, waste management, and environmental services assets with regulatory compliance and growth drivers. Use when analyzing water infrastructure, evaluating waste assets, or assessing utility investments.",
            ),
            (
                "modeling-inflation-linkage-in-infrastructure",
                "Analyzes inflation protection mechanisms in infrastructure with CPI-linked revenues, index-based contracts, and real return modeling. Use when modeling inflation linkage, analyzing CPI adjustment, or evaluating real return profiles.",
            ),
            (
                "conducting-environmental-impact-assessments",
                "Evaluates environmental compliance requirements with permitting risk, mitigation obligations, and ESG assessment for infrastructure investments. Use when assessing environmental risk, evaluating permitting timelines, or analyzing environmental compliance.",
            ),
            (
                "analyzing-social-infrastructure-investments",
                "Evaluates social infrastructure including healthcare, education, and government facilities with availability-based revenue structures. Use when analyzing social infrastructure, evaluating availability payments, or assessing government-backed projects.",
            ),
            (
                "managing-infrastructure-asset-lifecycle",
                "Tracks infrastructure asset performance with maintenance planning, capital expenditure optimization, and end-of-life valuation. Use when managing infrastructure portfolios, planning capex, or evaluating asset condition.",
            ),
            (
                "preparing-infrastructure-investment-cases",
                "Structures infrastructure investment recommendations with regulatory analysis, cash flow modeling, and risk assessment for IC presentation. Use when preparing infra investment cases, building IC materials, or documenting infrastructure opportunities.",
            ),
        ],
    },
    # ─── 13. REAL ASSETS & NATURAL RESOURCES ──────────────────────────
    "Real Assets and Natural Resources": {
        "description": "Commodity-linked capital, mining, energy, and real asset investment evaluation",
        "practice_areas": [
            "Natural Resources",
            "Energy Capital",
            "Commodity Investment",
        ],
        "skills": [
            (
                "evaluating-upstream-energy-assets",
                "Assesses upstream oil and gas assets with reserve estimation, production decline curves, and net asset value modeling. Use when evaluating E&P assets, analyzing reserve reports, or modeling upstream economics.",
            ),
            (
                "modeling-mining-project-economics",
                "Builds mining project financial models with resource estimation, mine plan integration, and commodity price sensitivity analysis. Use when modeling mining investments, analyzing feasibility studies, or evaluating mineral assets.",
            ),
            (
                "analyzing-commodity-price-risk",
                "Evaluates commodity price exposure with forward curve analysis, hedging strategies, and break-even price sensitivity. Use when analyzing commodity risk, designing hedging programs, or stress testing price assumptions.",
            ),
            (
                "structuring-royalty-and-streaming-deals",
                "Designs royalty and streaming agreements with volume projections, delivery schedules, and implied return analysis. Use when structuring royalty deals, analyzing stream economics, or evaluating passive resource exposure.",
            ),
            (
                "conducting-reserve-and-resource-analysis",
                "Evaluates mineral and hydrocarbon reserves with classification methodology, resource conversion rates, and valuation per unit analysis. Use when analyzing reserve reports, validating resource estimates, or assessing depletion profiles.",
            ),
            (
                "analyzing-midstream-infrastructure-assets",
                "Evaluates midstream assets with throughput analysis, fee-based vs commodity-exposed revenue, and contract structure assessment. Use when analyzing midstream investments, evaluating pipeline assets, or assessing gathering systems.",
            ),
            (
                "modeling-renewable-resource-yields",
                "Builds renewable energy yield models with resource assessment, capacity factor analysis, and P50/P90 production estimates. Use when modeling wind/solar yields, analyzing resource data, or evaluating production uncertainty.",
            ),
            (
                "evaluating-timber-and-agriculture-assets",
                "Assesses timberland and agricultural investments with biological growth rates, harvest economics, and land value appreciation. Use when evaluating timber investments, analyzing farmland, or assessing biological asset returns.",
            ),
            (
                "analyzing-power-market-structures",
                "Evaluates electricity market design with capacity payments, energy margins, ancillary services, and renewable intermittency management. Use when analyzing power markets, evaluating merchant exposure, or assessing capacity market dynamics.",
            ),
            (
                "structuring-energy-offtake-agreements",
                "Designs power purchase agreements and energy offtake structures with price mechanics, volume commitments, and curtailment provisions. Use when structuring PPAs, analyzing offtake terms, or evaluating energy contract risk.",
            ),
            (
                "conducting-environmental-remediation-analysis",
                "Evaluates environmental liability exposure with remediation cost estimation, regulatory compliance requirements, and insurance coverage assessment. Use when analyzing environmental liabilities, estimating cleanup costs, or assessing environmental risk.",
            ),
            (
                "analyzing-water-rights-and-allocation",
                "Evaluates water rights valuation with seniority analysis, regulatory framework assessment, and allocation risk for resource investments. Use when analyzing water rights, evaluating water allocation, or assessing water risk.",
            ),
            (
                "modeling-carbon-credit-economics",
                "Builds carbon credit models with offset generation analysis, verification costs, and market pricing dynamics for carbon-linked investments. Use when modeling carbon credits, analyzing offset economics, or evaluating carbon market exposure.",
            ),
            (
                "evaluating-critical-minerals-supply-chains",
                "Assesses critical mineral investments with supply chain mapping, geopolitical risk, and processing infrastructure analysis. Use when evaluating critical minerals, analyzing lithium/cobalt supply, or assessing rare earth investments.",
            ),
            (
                "analyzing-oilfield-services-economics",
                "Evaluates OFS sector investments with rig count sensitivity, day rate analysis, and technology adoption curves. Use when analyzing oilfield services, evaluating service company economics, or assessing technology uptake.",
            ),
            (
                "structuring-real-asset-fund-vehicles",
                "Designs fund structures for real asset strategies with long-dated commitments, NAV-based mechanics, and co-investment programs. Use when structuring resource funds, designing natural resource vehicles, or analyzing real asset fund terms.",
            ),
            (
                "analyzing-decommissioning-obligations",
                "Evaluates asset retirement and decommissioning liabilities with cost estimation, timing analysis, and funding adequacy assessment. Use when analyzing decommissioning costs, evaluating ARO exposure, or assessing abandonment liability.",
            ),
            (
                "conducting-resource-asset-due-diligence",
                "Structures technical and commercial DD for resource assets with geological review, operational assessment, and regulatory evaluation. Use when conducting resource DD, evaluating technical reports, or assessing operational risk.",
            ),
            (
                "modeling-resource-depletion-economics",
                "Builds depletion models with production decline, reserve replacement economics, and terminal value analysis for finite-life assets. Use when modeling depletion, analyzing resource longevity, or evaluating reserve life economics.",
            ),
            (
                "preparing-real-asset-investment-cases",
                "Structures real asset investment recommendations with commodity thesis, asset-level analysis, and risk assessment for IC presentation. Use when preparing resource investment cases, building IC materials, or documenting real asset opportunities.",
            ),
        ],
    },
    # ─── 14. CREDIT & INSTITUTIONAL LENDING ───────────────────────────
    "Credit and Institutional Lending": {
        "description": "Institutional credit analysis, syndicated lending, and credit fund operations",
        "practice_areas": ["Credit Markets", "Leveraged Lending", "Direct Lending"],
        "skills": [
            (
                "conducting-institutional-credit-analysis",
                "Structures credit underwriting with financial ratio analysis, cash flow quality assessment, and downside scenario modeling. Use when underwriting credit, analyzing borrower quality, or writing credit opinions.",
            ),
            (
                "analyzing-leveraged-loan-markets",
                "Monitors leveraged loan market conditions with new issue activity, technical dynamics, and CLO demand analysis. Use when analyzing loan markets, tracking CLO activity, or assessing market technical conditions.",
            ),
            (
                "modeling-credit-fund-portfolios",
                "Builds credit fund portfolio models with yield attribution, default/recovery scenarios, and portfolio-level return analysis. Use when modeling credit funds, projecting portfolio returns, or analyzing yield components.",
            ),
            (
                "structuring-direct-lending-facilities",
                "Designs direct lending structures with pricing, covenant packages, and documentation tailored for middle-market borrowers. Use when structuring direct loans, designing covenant packages, or analyzing direct lending terms.",
            ),
            (
                "analyzing-credit-agreement-terms",
                "Evaluates credit agreement provisions with borrower flexibility, lender protections, and documentation comparison analysis. Use when reviewing credit agreements, analyzing doc terms, or comparing loan documentation.",
            ),
            (
                "conducting-credit-committee-presentations",
                "Structures credit committee packages with borrower analysis, risk assessment, structuring proposal, and recommendation documentation. Use when preparing credit committee materials, presenting loan opportunities, or documenting credit decisions.",
            ),
            (
                "modeling-default-and-recovery-analysis",
                "Builds default probability and recovery rate models with industry data, structural analysis, and loss-given-default estimation. Use when modeling credit losses, estimating recovery values, or analyzing default scenarios.",
            ),
            (
                "analyzing-middle-market-lending-dynamics",
                "Evaluates middle-market lending environment with competition analysis, spread trends, and deal structure evolution. Use when analyzing middle-market lending, tracking competitive dynamics, or assessing market conditions.",
            ),
            (
                "structuring-delayed-draw-facilities",
                "Designs delayed-draw term loan structures with commitment fees, draw conditions, and availability period mechanics. Use when structuring DDTL facilities, designing draw-down mechanisms, or analyzing delayed-draw economics.",
            ),
            (
                "managing-credit-portfolio-surveillance",
                "Monitors credit portfolio health with rating migration tracking, watchlist management, and early warning indicator analysis. Use when conducting portfolio surveillance, managing credit watchlists, or tracking credit migration.",
            ),
            (
                "analyzing-sponsor-backed-credit",
                "Evaluates PE sponsor-backed credit with sponsor track record, equity contribution, and governance assessment. Use when analyzing sponsor-backed loans, assessing sponsor quality, or evaluating sponsor support dynamics.",
            ),
            (
                "modeling-payment-in-kind-structures",
                "Builds PIK and PIK toggle models with compound interest analysis, cash vs PIK election scenarios, and leverage impact assessment. Use when modeling PIK instruments, analyzing toggle mechanics, or evaluating accrued interest impact.",
            ),
            (
                "structuring-revolving-credit-commitments",
                "Designs revolver structures with commitment sizing, utilization analysis, and availability management for credit fund portfolios. Use when structuring revolvers, sizing commitments, or managing availability exposure.",
            ),
            (
                "conducting-industry-credit-analysis",
                "Structures industry-level credit assessment with cyclicality analysis, regulatory risk, and sector-specific credit metrics. Use when analyzing industry credit conditions, evaluating sector risk, or building industry-level views.",
            ),
            (
                "analyzing-intercreditor-agreements",
                "Evaluates intercreditor and subordination provisions with lien priority, payment waterfall, and enforcement rights analysis. Use when analyzing intercreditor terms, evaluating subordination structures, or assessing lender priority.",
            ),
            (
                "managing-loan-trading-and-settlement",
                "Coordinates loan trading with LSTA standard documentation, delayed settlement compensation, and trade settlement mechanics. Use when managing loan trades, processing LSTA documentation, or coordinating trade settlement.",
            ),
            (
                "analyzing-credit-fund-performance",
                "Evaluates credit fund returns with yield attribution, mark-to-market dynamics, and performance comparison across credit strategies. Use when analyzing credit fund performance, decomposing returns, or benchmarking credit strategies.",
            ),
            (
                "structuring-first-lien-last-out-facilities",
                "Designs FILO structures with tranche-level pricing, distribution waterfalls, and intercreditor provisions within unitranche financing. Use when structuring FILO tranches, analyzing split economics, or designing blended pricing.",
            ),
            (
                "analyzing-private-credit-market-dynamics",
                "Monitors private credit market evolution with AUM growth, competitive dynamics, and spread convergence with broadly syndicated markets. Use when analyzing private credit trends, tracking market evolution, or assessing competitive positioning.",
            ),
            (
                "preparing-credit-investment-memoranda",
                "Creates credit investment memos with borrower analysis, structural assessment, risk evaluation, and relative value positioning. Use when writing credit memos, documenting loan decisions, or presenting credit opportunities.",
            ),
        ],
    },
    # ─── 15. PUBLIC MARKETS & TRADING ─────────────────────────────────
    "Public Markets and Trading": {
        "description": "Market microstructure, execution strategies, and institutional trading workflows",
        "practice_areas": ["Trading", "Market Making", "Execution"],
        "skills": [
            (
                "analyzing-market-microstructure",
                "Evaluates market structure dynamics with order book analysis, spread decomposition, and information asymmetry assessment. Use when analyzing market structure, evaluating trading venues, or assessing execution quality.",
            ),
            (
                "modeling-transaction-cost-analysis",
                "Builds TCA frameworks with implementation shortfall, VWAP comparison, and market impact estimation across asset classes. Use when conducting TCA, measuring execution quality, or analyzing trading costs.",
            ),
            (
                "structuring-algorithmic-execution-strategies",
                "Designs algo trading strategies with TWAP, VWAP, and implementation shortfall approaches tailored to order characteristics. Use when selecting execution algos, designing trading strategies, or optimizing order routing.",
            ),
            (
                "analyzing-market-regime-indicators",
                "Monitors market regime signals with volatility clustering, correlation dynamics, and liquidity condition assessment. Use when analyzing market regimes, detecting regime shifts, or adjusting strategy for market conditions.",
            ),
            (
                "managing-block-trade-execution",
                "Coordinates large block execution with market impact minimization, counterparty selection, and crossing network utilization. Use when executing block trades, managing large orders, or minimizing market footprint.",
            ),
            (
                "analyzing-equity-market-breadth",
                "Evaluates market breadth with advance-decline analysis, new high/low tracking, and sector participation assessment. Use when analyzing market breadth, assessing rally quality, or identifying divergences.",
            ),
            (
                "modeling-securities-lending-dynamics",
                "Analyzes securities lending market with borrow cost, short interest dynamics, and fail-to-deliver monitoring. Use when analyzing lending markets, tracking borrow costs, or evaluating short selling dynamics.",
            ),
            (
                "structuring-portfolio-trading-strategies",
                "Designs portfolio transition strategies with trade list optimization, crossing opportunities, and execution timeline planning. Use when planning portfolio transitions, managing rebalancing trades, or optimizing transition costs.",
            ),
            (
                "analyzing-etf-creation-redemption-dynamics",
                "Evaluates ETF market mechanics with premium/discount analysis, authorized participant activity, and creation unit arbitrage. Use when analyzing ETF trading, evaluating NAV premiums, or understanding creation/redemption flows.",
            ),
            (
                "managing-best-execution-compliance",
                "Structures best execution monitoring with venue analysis, systematic internalization assessment, and regulatory compliance documentation. Use when managing best execution, documenting execution decisions, or conducting venue analysis.",
            ),
            (
                "analyzing-dark-pool-and-alternative-venues",
                "Evaluates alternative trading systems with fill rate analysis, information leakage assessment, and venue toxicity measurement. Use when analyzing dark pools, evaluating ATS venues, or assessing execution venue quality.",
            ),
            (
                "modeling-intraday-volatility-patterns",
                "Analyzes intraday volatility dynamics with open/close effects, lunch-time patterns, and event-driven volatility estimation. Use when modeling intraday volatility, timing order execution, or analyzing time-of-day effects.",
            ),
            (
                "analyzing-cross-asset-correlation-dynamics",
                "Monitors cross-asset correlation patterns with regime-dependent analysis and diversification effectiveness assessment. Use when analyzing correlations, assessing diversification, or evaluating cross-asset relationships.",
            ),
            (
                "structuring-pairs-trading-strategies",
                "Designs statistical arbitrage pairs with cointegration analysis, spread dynamics, and entry/exit signal calibration. Use when building pairs trades, analyzing cointegration, or designing mean-reversion strategies.",
            ),
            (
                "managing-margin-and-collateral-requirements",
                "Tracks margin requirements with initial/variation margin, portfolio margin optimization, and collateral eligibility analysis. Use when managing margin, optimizing collateral, or analyzing portfolio margin impact.",
            ),
            (
                "analyzing-market-flow-dynamics",
                "Evaluates institutional flow patterns with fund flow analysis, positioning data, and sentiment indicator synthesis. Use when analyzing market flows, tracking institutional positioning, or assessing market sentiment.",
            ),
            (
                "conducting-pre-trade-compliance-checks",
                "Structures pre-trade compliance with restricted list screening, position limits, and regulatory constraint verification. Use when running pre-trade compliance, screening restricted securities, or verifying trading limits.",
            ),
            (
                "analyzing-fixed-income-market-liquidity",
                "Evaluates bond market liquidity with bid-ask spread analysis, dealer inventory assessment, and electronic trading penetration. Use when analyzing bond liquidity, assessing execution conditions, or evaluating venue selection.",
            ),
            (
                "modeling-event-driven-trading-analysis",
                "Analyzes event-driven opportunities with catalyst identification, pricing efficiency assessment, and risk/reward evaluation. Use when analyzing event-driven situations, evaluating catalysts, or assessing event timing.",
            ),
            (
                "preparing-trading-desk-risk-reports",
                "Structures trading desk risk reporting with P&L attribution, position summaries, and limit utilization tracking. Use when preparing desk risk reports, attributing trading P&L, or monitoring position limits.",
            ),
        ],
    },
    # ─── 16. DERIVATIVES & STRUCTURED PRODUCTS ────────────────────────
    "Derivatives and Structured Products": {
        "description": "Options, swaps, exotic structures, and hedging program design",
        "practice_areas": ["Derivatives", "Structured Products", "Hedging"],
        "skills": [
            (
                "pricing-vanilla-equity-options",
                "Calculates option values with Black-Scholes, binomial, and Monte Carlo methods including Greeks sensitivity analysis. Use when pricing equity options, calculating Greeks, or evaluating option strategies.",
            ),
            (
                "structuring-interest-rate-swaps",
                "Designs IRS structures with fixed/float mechanics, day count conventions, and mark-to-market valuation analysis. Use when structuring rate swaps, analyzing swap economics, or evaluating hedging alternatives.",
            ),
            (
                "modeling-exotic-option-payoffs",
                "Builds pricing models for barrier, Asian, lookback, and other path-dependent options with Monte Carlo simulation. Use when pricing exotic options, modeling complex payoffs, or evaluating structured product components.",
            ),
            (
                "analyzing-credit-derivative-structures",
                "Evaluates CDS, CDX, and bespoke credit derivative structures with spread analysis and credit event mechanics. Use when analyzing credit derivatives, pricing CDS, or evaluating index tranche products.",
            ),
            (
                "structuring-corporate-hedging-programs",
                "Designs enterprise hedging strategies for commodity, FX, and interest rate exposures with hedge accounting qualification. Use when designing hedge programs, selecting hedging instruments, or structuring hedge documentation.",
            ),
            (
                "modeling-counterparty-credit-exposure",
                "Calculates potential future exposure and CVA with simulation-based approaches and netting agreement analysis. Use when modeling counterparty exposure, calculating CVA/DVA, or assessing counterparty risk.",
            ),
            (
                "analyzing-volatility-surface-dynamics",
                "Evaluates implied volatility surfaces with skew analysis, term structure dynamics, and surface fitting methodologies. Use when analyzing vol surfaces, assessing skew dynamics, or calibrating volatility models.",
            ),
            (
                "structuring-total-return-swaps",
                "Designs TRS structures with reference asset selection, financing rate mechanics, and collateral arrangements. Use when structuring TRS, analyzing synthetic exposure, or evaluating unfunded exposure alternatives.",
            ),
            (
                "modeling-variance-and-volatility-swaps",
                "Prices variance and volatility swaps with replication methodology, convexity adjustment, and discrete monitoring analysis. Use when pricing vol products, modeling variance swaps, or evaluating volatility strategies.",
            ),
            (
                "analyzing-structured-note-payoffs",
                "Deconstructs structured note payoffs with embedded option identification, issuer credit risk, and all-in cost analysis. Use when analyzing structured notes, evaluating embedded options, or assessing structured product costs.",
            ),
            (
                "structuring-collar-and-prepaid-forward",
                "Designs equity monetization structures with zero-cost collars, prepaid variable forwards, and exchange fund alternatives. Use when structuring equity monetization, designing collars, or evaluating concentrated stock solutions.",
            ),
            (
                "modeling-fx-derivative-pricing",
                "Prices FX options and exotic structures with Garman-Kohlhagen, local volatility, and stochastic volatility models. Use when pricing FX derivatives, evaluating FX options, or modeling cross-currency products.",
            ),
            (
                "analyzing-isda-documentation-terms",
                "Evaluates ISDA Master Agreement provisions with close-out netting, termination events, and credit support annexes. Use when reviewing ISDA terms, analyzing CSA provisions, or assessing documentation risk.",
            ),
            (
                "structuring-inflation-derivatives",
                "Designs inflation swap and option structures with zero-coupon and year-on-year mechanics and seasonal adjustment analysis. Use when structuring inflation derivatives, pricing inflation swaps, or evaluating inflation hedging.",
            ),
            (
                "modeling-xva-adjustments",
                "Calculates comprehensive XVA including CVA, DVA, FVA, KVA, and MVA with portfolio-level analysis and hedging strategies. Use when computing XVA, modeling valuation adjustments, or analyzing funding costs.",
            ),
            (
                "analyzing-commodity-derivative-structures",
                "Evaluates commodity swaps, options, and exotic structures with seasonality, convenience yield, and storage cost analysis. Use when pricing commodity derivatives, analyzing energy structures, or evaluating commodity hedging.",
            ),
            (
                "structuring-equity-derivative-strategies",
                "Designs equity derivative strategies with call spreads, put spreads, straddles, and ratio combinations for investment and hedging. Use when structuring equity strategies, designing option combinations, or evaluating strategy payoffs.",
            ),
            (
                "managing-central-clearing-obligations",
                "Coordinates central clearing requirements with CCP selection, margin optimization, and clearing threshold monitoring. Use when managing clearing obligations, optimizing CCP selection, or analyzing clearing economics.",
            ),
            (
                "analyzing-counterparty-netting-efficiency",
                "Evaluates netting benefits across derivative portfolios with bilateral vs cleared netting, portfolio compression, and capital savings. Use when analyzing netting efficiency, evaluating compression opportunities, or optimizing counterparty exposure.",
            ),
            (
                "preparing-derivative-risk-reports",
                "Structures derivative portfolio risk reporting with Greeks aggregation, scenario analysis, and limit monitoring. Use when preparing derivative risk reports, aggregating portfolio Greeks, or monitoring risk limits.",
            ),
        ],
    },
    # ─── 17. CROSS-BORDER CAPITAL ─────────────────────────────────────
    "Cross-Border Capital": {
        "description": "International deal structuring, FX management, and sovereign risk assessment",
        "practice_areas": [
            "International Finance",
            "Cross-Border Transactions",
            "Emerging Markets",
        ],
        "skills": [
            (
                "analyzing-sovereign-credit-risk",
                "Evaluates sovereign creditworthiness with fiscal analysis, external vulnerability, political risk, and institutional quality assessment. Use when analyzing sovereign risk, assessing country credit, or evaluating government bond exposure.",
            ),
            (
                "structuring-cross-border-investments",
                "Designs international investment structures with holding company selection, treaty benefits, and repatriation pathway optimization. Use when structuring cross-border deals, optimizing holding structures, or planning repatriation strategies.",
            ),
            (
                "analyzing-emerging-market-capital-flows",
                "Monitors EM capital flow dynamics with FDI, portfolio flows, reserve changes, and balance of payments analysis. Use when analyzing EM flows, tracking capital movement, or assessing EM investment conditions.",
            ),
            (
                "managing-foreign-currency-exposure",
                "Structures FX hedging strategies for international portfolios with natural hedge identification, instrument selection, and cost analysis. Use when managing currency risk, designing FX hedges, or analyzing translation exposure.",
            ),
            (
                "evaluating-country-risk-factors",
                "Assesses country-level investment risk with political stability, rule of law, corruption indices, and expropriation history analysis. Use when evaluating country risk, assessing political exposure, or scoring sovereign investment environments.",
            ),
            (
                "analyzing-cross-border-tax-structuring",
                "Evaluates international tax structures with treaty networks, withholding rates, and permanent establishment risk analysis. Use when structuring cross-border tax, analyzing treaty benefits, or evaluating tax-efficient structuring.",
            ),
            (
                "structuring-global-fund-distribution",
                "Designs international fund distribution with UCITS/AIFMD compliance, passporting, and local registration requirements. Use when planning international distribution, structuring cross-border fund access, or navigating regulatory requirements.",
            ),
            (
                "analyzing-frontier-market-investments",
                "Evaluates frontier market opportunities with liquidity constraints, custody risk, settlement infrastructure, and governance assessment. Use when analyzing frontier markets, assessing operational risk, or evaluating frontier market access.",
            ),
            (
                "modeling-currency-hedging-programs",
                "Builds currency hedging models with rolling forward programs, option-based strategies, and cross-hedge analysis for international portfolios. Use when designing hedge programs, analyzing hedge ratios, or evaluating FX protection costs.",
            ),
            (
                "analyzing-capital-control-environments",
                "Evaluates capital control regimes with repatriation restrictions, investment caps, and regulatory approval requirements. Use when assessing capital controls, evaluating repatriation risk, or analyzing investment restrictions.",
            ),
            (
                "structuring-offshore-and-onshore-access",
                "Designs market access structures including QFII, Stock Connect, and GDR programs for restricted market entry. Use when structuring market access, evaluating access programs, or analyzing quota-based investment systems.",
            ),
            (
                "analyzing-geopolitical-risk-exposure",
                "Evaluates geopolitical risk impact on investment portfolios with sanctions exposure, conflict risk, and supply chain disruption analysis. Use when analyzing geopolitical risk, assessing sanctions impact, or evaluating political event exposure.",
            ),
            (
                "conducting-cross-border-due-diligence",
                "Structures international DD with multi-jurisdictional legal review, regulatory assessment, and cultural integration analysis. Use when conducting international DD, managing multi-country processes, or evaluating cross-border operational risk.",
            ),
            (
                "analyzing-local-currency-debt-markets",
                "Evaluates local currency government and corporate bond markets with yield analysis, inflation dynamics, and FX carry assessment. Use when analyzing local currency debt, evaluating EM bond opportunities, or assessing carry strategies.",
            ),
            (
                "structuring-development-finance-instruments",
                "Designs blended finance structures with DFI participation, concessional capital, and catalytic funding for emerging market investments. Use when structuring DFI co-investments, designing blended finance, or analyzing concessional terms.",
            ),
            (
                "managing-cross-border-settlement-risk",
                "Evaluates settlement risk in cross-border transactions with time zone analysis, CLS participation, and Herstatt risk mitigation. Use when managing settlement risk, analyzing CLS eligibility, or evaluating cross-currency settlement.",
            ),
            (
                "analyzing-international-regulatory-arbitrage",
                "Evaluates regulatory differences across jurisdictions with comparative framework analysis and optimal domicile selection. Use when analyzing regulatory environments, comparing jurisdiction frameworks, or selecting fund domiciles.",
            ),
            (
                "structuring-joint-venture-investments",
                "Designs cross-border JV structures with governance frameworks, exit mechanisms, and dispute resolution for international partnerships. Use when structuring international JVs, designing governance frameworks, or planning exit mechanics.",
            ),
            (
                "analyzing-trade-finance-instruments",
                "Evaluates trade finance structures with letters of credit, supply chain financing, and receivables factoring for cross-border commerce. Use when analyzing trade finance, evaluating LC structures, or assessing supply chain financing.",
            ),
            (
                "preparing-cross-border-investment-cases",
                "Structures international investment recommendations with country risk overlay, currency analysis, and structural considerations for IC presentation. Use when preparing cross-border cases, building international IC materials, or documenting cross-border opportunities.",
            ),
        ],
    },
    # ─── 18. CAPITAL ALLOCATION & CORPORATE STRATEGY ──────────────────
    "Capital Allocation and Corporate Strategy": {
        "description": "ROIC frameworks, capital budgeting, strategic alternatives, and shareholder value optimization",
        "practice_areas": [
            "Corporate Strategy",
            "Capital Allocation",
            "Shareholder Value",
        ],
        "skills": [
            (
                "building-roic-analysis-frameworks",
                "Constructs ROIC decomposition with invested capital measurement, operating return analysis, and value creation vs destruction assessment. Use when analyzing ROIC, building capital return frameworks, or assessing value creation.",
            ),
            (
                "evaluating-strategic-alternatives",
                "Structures strategic alternatives analysis with status quo, sale, merger, spin-off, and recapitalization scenario comparison. Use when evaluating strategic options, preparing board-level alternatives, or analyzing corporate transformations.",
            ),
            (
                "modeling-capital-budgeting-decisions",
                "Builds NPV, IRR, and payback models for capital investment decisions with hurdle rate calibration and risk adjustment. Use when evaluating capital investments, comparing project returns, or building capital allocation frameworks.",
            ),
            (
                "analyzing-conglomerate-discount-dynamics",
                "Evaluates conglomerate discount with SOTP analysis, segment-level valuation, and separation benefit quantification. Use when analyzing conglomerate value, building SOTP models, or evaluating break-up scenarios.",
            ),
            (
                "structuring-spin-off-transactions",
                "Designs corporate spin-off execution with Remainco/SpinCo capitalization, Form 10 preparation, and tax-free qualification analysis. Use when structuring spin-offs, analyzing separation mechanics, or evaluating Remainco impact.",
            ),
            (
                "modeling-share-repurchase-optimization",
                "Analyzes buyback program design with timing optimization, price sensitivity, and EPS accretion impact modeling. Use when optimizing buybacks, modeling repurchase economics, or comparing return-of-capital alternatives.",
            ),
            (
                "analyzing-dividend-policy-optimization",
                "Evaluates dividend policy with payout sustainability, peer comparison, and investor preference analysis across growth and value contexts. Use when analyzing dividend policy, evaluating payout ratios, or designing dividend programs.",
            ),
            (
                "conducting-portfolio-rationalization",
                "Structures portfolio review with strategic fit assessment, divestiture candidate identification, and proceeds redeployment analysis. Use when reviewing corporate portfolios, identifying divestiture candidates, or planning asset dispositions.",
            ),
            (
                "modeling-organic-vs-inorganic-growth",
                "Compares build vs buy alternatives with risk-adjusted returns, time-to-value, and execution probability assessment. Use when evaluating growth strategies, comparing M&A vs organic investment, or analyzing make-vs-buy decisions.",
            ),
            (
                "analyzing-activist-investor-vulnerabilities",
                "Evaluates corporate vulnerability to shareholder activism with governance assessment, valuation gaps, and operational improvement opportunities. Use when assessing activist risk, identifying vulnerabilities, or preparing defensive analyses.",
            ),
            (
                "structuring-tracking-stock-arrangements",
                "Designs tracking stock structures with attributed business economics, intergroup arrangements, and value realization mechanics. Use when evaluating tracking stocks, analyzing attributed value structures, or assessing partial separation alternatives.",
            ),
            (
                "modeling-economic-profit-analysis",
                "Builds economic profit (EVA) models with capital charge calculation, value spread analysis, and long-term value creation measurement. Use when calculating economic profit, analyzing EVA trends, or measuring value creation.",
            ),
            (
                "analyzing-capital-structure-optimization",
                "Evaluates optimal leverage with WACC minimization, rating impact, and financial flexibility assessment across market conditions. Use when optimizing capital structure, analyzing target leverage, or evaluating rating implications.",
            ),
            (
                "conducting-investor-day-preparation",
                "Structures investor day content with long-term strategy presentation, financial targets, and capital allocation framework communication. Use when preparing investor days, designing strategy presentations, or building financial target frameworks.",
            ),
            (
                "analyzing-corporate-governance-effectiveness",
                "Evaluates board composition, compensation alignment, and governance practices with proxy advisory and institutional investor standards. Use when analyzing governance, evaluating board effectiveness, or assessing shareholder alignment.",
            ),
            (
                "modeling-scenario-planning-frameworks",
                "Builds corporate scenario planning models with macro assumption sets, strategic response options, and contingency plan development. Use when building scenario frameworks, planning strategic responses, or developing contingency strategies.",
            ),
            (
                "analyzing-vertical-integration-economics",
                "Evaluates vertical integration decisions with make-vs-buy analysis, supply chain control benefits, and margin capture opportunity assessment. Use when analyzing vertical integration, evaluating supply chain strategy, or assessing integration economics.",
            ),
            (
                "structuring-joint-venture-governance",
                "Designs JV governance frameworks with decision-making rights, deadlock resolution, and exit mechanisms for corporate partnerships. Use when structuring JV governance, designing partnership agreements, or planning JV operations.",
            ),
            (
                "analyzing-esg-strategy-and-value-creation",
                "Evaluates ESG strategy with materiality assessment, stakeholder analysis, and value creation linkage for corporate decision-making. Use when analyzing ESG strategy, assessing material ESG factors, or linking sustainability to value.",
            ),
            (
                "preparing-strategic-alternatives-board-materials",
                "Creates board presentation materials with strategic options analysis, financial impact, and recommendation framework for corporate transformation decisions. Use when preparing board strategy materials, presenting alternatives, or documenting strategic recommendations.",
            ),
        ],
    },
    # ─── 19. ACTIVIST & EVENT-DRIVEN INVESTING ────────────────────────
    "Activist and Event-Driven Investing": {
        "description": "Activist campaigns, special situations, and event-driven strategy analysis",
        "practice_areas": [
            "Activist Investing",
            "Event-Driven Strategy",
            "Special Situations",
        ],
        "skills": [
            (
                "analyzing-activist-campaign-strategies",
                "Evaluates activist investor campaigns with thesis assessment, proposed changes, and likely outcome analysis. Use when analyzing activist situations, evaluating campaign theses, or assessing activist track records.",
            ),
            (
                "modeling-merger-arbitrage-spreads",
                "Calculates merger arb risk/reward with annualized spread, deal break probability, and downside scenario analysis. Use when analyzing merger arb, calculating spread returns, or evaluating deal completion probability.",
            ),
            (
                "analyzing-proxy-contest-dynamics",
                "Evaluates proxy fight mechanics with shareholder base analysis, ISS/Glass Lewis recommendations, and vote probability modeling. Use when analyzing proxy contests, assessing vote outcomes, or evaluating director nomination campaigns.",
            ),
            (
                "evaluating-spin-off-investment-opportunities",
                "Assesses spin-off equity with forced selling dynamics, orphaned security identification, and standalone valuation analysis. Use when evaluating spin-off investments, identifying forced-sell situations, or analyzing newly public entities.",
            ),
            (
                "analyzing-tender-offer-economics",
                "Evaluates tender offer structures with premium analysis, proration risk, and conditional tender strategies. Use when analyzing tender offers, calculating tender economics, or evaluating proration scenarios.",
            ),
            (
                "modeling-rights-offering-arbitrage",
                "Analyzes rights offering dynamics with theoretical ex-rights price, subscription premium, and nil-paid value calculation. Use when evaluating rights offerings, modeling TERP, or analyzing subscription arbitrage.",
            ),
            (
                "evaluating-post-reorganization-equity",
                "Assesses post-emergence equity with clean balance sheet analysis, improved capital structure, and re-rating potential. Use when evaluating post-reorg equity, analyzing emergence opportunities, or assessing restructured company value.",
            ),
            (
                "analyzing-dutch-auction-tender-strategies",
                "Evaluates Dutch auction mechanics with optimal pricing strategy, odd-lot proration, and shareholder base analysis. Use when analyzing Dutch auctions, modeling tender strategies, or evaluating self-tender economics.",
            ),
            (
                "tracking-13d-and-13g-filing-patterns",
                "Monitors beneficial ownership filings with accumulation pattern analysis, intent assessment, and historical activist progression. Use when tracking 13D filings, analyzing accumulation patterns, or identifying potential activist situations.",
            ),
            (
                "analyzing-going-private-transactions",
                "Evaluates management buyouts and take-private proposals with fairness assessment, minority squeeze-out mechanics, and appraisal rights analysis. Use when analyzing going-private deals, evaluating MBO fairness, or assessing minority shareholder protections.",
            ),
            (
                "modeling-stub-value-analysis",
                "Calculates stub equity value with subsidiary attribution, holding company discount, and sum-of-parts residual analysis. Use when analyzing stub values, evaluating holding company discounts, or identifying negative stub situations.",
            ),
            (
                "analyzing-corporate-governance-catalysts",
                "Identifies governance-related catalysts with board refreshment, compensation reform, and shareholder proposal analysis. Use when analyzing governance catalysts, evaluating shareholder proposals, or assessing governance improvement potential.",
            ),
            (
                "evaluating-litigation-driven-catalysts",
                "Assesses litigation outcome impact with settlement probability, damage range estimation, and stock price sensitivity analysis. Use when evaluating litigation catalysts, modeling legal outcomes, or analyzing litigation-driven opportunities.",
            ),
            (
                "analyzing-regulatory-event-impacts",
                "Evaluates regulatory decision impact with approval probability, timeline analysis, and outcome scenario modeling for event-driven positions. Use when analyzing regulatory events, evaluating FDA/FCC/DOJ decisions, or modeling regulatory outcomes.",
            ),
            (
                "structuring-activist-engagement-strategies",
                "Designs constructive engagement approaches with value creation proposals, governance improvements, and strategic change recommendations. Use when planning activist engagement, designing value creation proposals, or structuring board discussions.",
            ),
            (
                "analyzing-share-class-arbitrage",
                "Evaluates dual-class share structures with discount analysis, unification catalysts, and governance reform probability assessment. Use when analyzing share class spreads, evaluating unification likelihood, or assessing dual-class dynamics.",
            ),
            (
                "modeling-special-dividend-scenarios",
                "Analyzes special dividend catalysts with balance sheet capacity, tax efficiency, and shareholder return comparison analysis. Use when modeling special dividends, evaluating capital return catalysts, or assessing dividend capacity.",
            ),
            (
                "evaluating-sum-of-parts-activism",
                "Assesses conglomerate break-up activism with segment valuation, separation feasibility, and tax-free qualification analysis. Use when evaluating SOTP activism, analyzing break-up proposals, or modeling separation value.",
            ),
            (
                "analyzing-insider-buying-signals",
                "Evaluates insider purchase patterns with cluster buying identification, historical signal analysis, and conviction scoring. Use when analyzing insider buying, assessing management confidence signals, or tracking insider activity patterns.",
            ),
            (
                "preparing-event-driven-investment-cases",
                "Structures event-driven investment recommendations with catalyst identification, timeline analysis, and risk/reward framework for portfolio allocation. Use when preparing event-driven cases, documenting catalyst theses, or presenting special situation opportunities.",
            ),
        ],
    },
    # ─── 20. QUANTITATIVE CAPITAL STRATEGIES ──────────────────────────
    "Quantitative Capital Strategies": {
        "description": "Systematic investing, factor modeling, and quantitative portfolio construction for capital markets",
        "practice_areas": [
            "Quantitative Investing",
            "Systematic Strategies",
            "Factor Investing",
        ],
        "skills": [
            (
                "building-multi-factor-equity-models",
                "Constructs multi-factor models with value, momentum, quality, size, and volatility factor definitions and portfolio construction rules. Use when building factor models, designing systematic strategies, or constructing factor portfolios.",
            ),
            (
                "modeling-portfolio-risk-decomposition",
                "Decomposes portfolio risk with factor attribution, idiosyncratic risk, and marginal contribution to risk analysis. Use when decomposing portfolio risk, attributing risk sources, or analyzing factor risk contribution.",
            ),
            (
                "analyzing-factor-timing-signals",
                "Evaluates factor timing strategies with macro regime indicators, valuation spreads, and momentum signals for factor rotation. Use when analyzing factor timing, evaluating rotation signals, or designing tactical factor allocation.",
            ),
            (
                "building-statistical-arbitrage-models",
                "Constructs stat arb strategies with pair selection, signal generation, and portfolio optimization under market neutrality constraints. Use when building stat arb models, designing market-neutral strategies, or optimizing pair portfolios.",
            ),
            (
                "modeling-portfolio-optimization",
                "Builds mean-variance, Black-Litterman, and risk parity optimization models with constraint management and rebalancing rules. Use when optimizing portfolios, implementing risk parity, or applying Black-Litterman views.",
            ),
            (
                "analyzing-alpha-signal-decay",
                "Evaluates signal half-life, turnover implications, and capacity constraints for systematic alpha factors. Use when analyzing signal persistence, evaluating factor decay, or estimating strategy capacity.",
            ),
            (
                "conducting-backtest-validation",
                "Structures backtesting methodology with out-of-sample testing, cross-validation, and overfitting detection techniques. Use when validating backtests, detecting overfitting, or ensuring backtest robustness.",
            ),
            (
                "modeling-transaction-cost-optimization",
                "Builds transaction cost models with market impact estimation, optimal trade scheduling, and turnover-adjusted returns. Use when modeling trading costs, optimizing turnover, or evaluating net-of-cost alpha.",
            ),
            (
                "analyzing-alternative-data-signals",
                "Evaluates alternative data sources including satellite, NLP sentiment, web scraping, and geolocation for alpha signal generation. Use when analyzing alt data, evaluating new data sources, or integrating non-traditional signals.",
            ),
            (
                "building-risk-parity-portfolios",
                "Constructs risk parity allocation with equal risk contribution, leverage optimization, and asset class volatility targeting. Use when building risk parity, equalizing risk contribution, or designing leveraged balanced portfolios.",
            ),
            (
                "modeling-regime-switching-strategies",
                "Builds regime detection models with hidden Markov, threshold, and Bayesian change-point methodologies for strategy adaptation. Use when modeling regime changes, detecting market shifts, or adapting strategies to market conditions.",
            ),
            (
                "analyzing-crowding-and-factor-valuations",
                "Evaluates factor crowding with positioning analysis, valuation spread monitoring, and unwind risk assessment. Use when analyzing factor crowding, assessing unwind risk, or monitoring factor valuation extremes.",
            ),
            (
                "structuring-smart-beta-product-design",
                "Designs systematic investment products with transparent methodology, rebalancing rules, and index construction specifications. Use when designing smart beta products, creating index methodologies, or structuring systematic funds.",
            ),
            (
                "modeling-volatility-targeting-strategies",
                "Builds volatility targeting models with realized vol estimation, leverage adjustment, and drawdown management mechanics. Use when implementing vol targeting, adjusting portfolio leverage, or managing drawdown limits.",
            ),
            (
                "conducting-monte-carlo-portfolio-analysis",
                "Runs Monte Carlo simulations for portfolio analysis with return distribution, tail risk, and path-dependent scenario evaluation. Use when running portfolio simulations, estimating tail risk, or analyzing return distributions.",
            ),
            (
                "analyzing-machine-learning-in-investing",
                "Evaluates ML applications in investment with feature engineering, model selection, and implementation considerations for alpha generation. Use when evaluating ML for investing, designing ML pipelines, or assessing ML strategy feasibility.",
            ),
            (
                "building-custom-factor-definitions",
                "Constructs proprietary factor definitions with signal specification, universe application, and orthogonalization methodology. Use when defining custom factors, creating proprietary signals, or building factor libraries.",
            ),
            (
                "modeling-portfolio-rebalancing-rules",
                "Designs rebalancing triggers with calendar-based, threshold-based, and hybrid approaches with tax and cost optimization. Use when designing rebalancing rules, optimizing rebalancing frequency, or modeling turnover impact.",
            ),
            (
                "analyzing-execution-implementation-shortfall",
                "Measures implementation shortfall with paper portfolio comparison, delay cost attribution, and execution quality assessment. Use when measuring implementation shortfall, analyzing execution quality, or attributing trading costs.",
            ),
            (
                "preparing-quantitative-strategy-reports",
                "Structures systematic strategy performance reporting with factor exposure, attribution, and risk analytics for investor communication. Use when preparing quant reports, documenting strategy performance, or presenting systematic strategy results.",
            ),
        ],
    },
}
