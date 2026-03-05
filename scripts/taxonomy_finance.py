"""
Finance (agentskills.finance) taxonomy: 20 subgroups, 20-40 skills each.

Each subgroup is analogous to a legal practice area (e.g., "intellectual property",
"court motions"). Skills within encode semi-structured agentic workflows for
moving and processing/synthesizing information in consumer finance, corporate
finance, tax, insurance, accounting, and financial services operations.

Naming: gerund form, lowercase-hyphenated, max 64 chars.
"""

FINANCE_TAXONOMY = {
    # ─── 1. EQUITY RESEARCH ──────────────────────────────────────────
    "Equity Research": {
        "description": "Public equity analysis workflows from screening through initiation and coverage",
        "practice_areas": ["Equity Research", "Investment Management"],
        "skills": [
            (
                "summarizing-earnings-calls",
                "Transforms earnings call transcripts into structured summaries with financial guidance, KPI changes, management sentiment, and analyst Q&A highlights. Use when processing quarterly earnings calls, preparing investment research, or tracking company performance narratives.",
            ),
            (
                "analyzing-financial-ratios",
                "Computes and interprets liquidity, profitability, leverage, and efficiency ratios with peer benchmarking. Use when analyzing financial statements, building comparable analyses, or evaluating company health metrics.",
            ),
            (
                "building-equity-valuation-models",
                "Constructs DCF, comparable company, and precedent transaction valuation models with sensitivity analysis. Use when valuing public companies, building financial models, or estimating fair value ranges.",
            ),
            (
                "writing-equity-research-notes",
                "Creates structured equity research notes with thesis, valuation, risks, and rating justification. Use when initiating coverage, updating research opinions, or writing investment notes.",
            ),
            (
                "screening-equity-opportunities",
                "Applies quantitative and qualitative screens to filter investable equity universe by financial and strategic criteria. Use when screening stocks, filtering investment candidates, or building watchlists.",
            ),
            (
                "analyzing-management-commentary",
                "Extracts forward-looking signals from management commentary with sentiment analysis and guidance tracking. Use when analyzing earnings transcripts, tracking guidance changes, or assessing management credibility.",
            ),
            (
                "tracking-consensus-estimates",
                "Monitors sell-side consensus estimates with revision tracking and surprise analysis. Use when tracking estimate revisions, analyzing consensus changes, or monitoring analyst expectations.",
            ),
            (
                "analyzing-industry-supply-chains",
                "Maps industry supply chain dynamics with upstream/downstream exposure and competitive positioning. Use when analyzing supply chains, assessing industry structure, or evaluating competitive moats.",
            ),
            (
                "modeling-revenue-forecasts",
                "Builds bottom-up revenue models from segment-level drivers with assumption documentation. Use when forecasting revenue, modeling growth drivers, or building segment-level projections.",
            ),
            (
                "analyzing-shareholder-activism",
                "Tracks activist investor campaigns with thesis analysis and outcome assessment. Use when monitoring activist situations, analyzing proxy fights, or evaluating activist theses.",
            ),
            (
                "analyzing-insider-transactions",
                "Structures insider trading analysis with pattern identification and significance assessment. Use when tracking insider activity, analyzing Form 4 filings, or evaluating insider buying/selling patterns.",
            ),
            (
                "analyzing-short-interest",
                "Monitors short interest dynamics with days-to-cover calculations and squeeze risk assessment. Use when tracking short interest, analyzing borrowing costs, or assessing short squeeze risk.",
            ),
            (
                "conducting-channel-checks",
                "Structures industry channel check findings with data normalization and trend identification. Use when synthesizing channel check data, analyzing industry indicators, or documenting field research.",
            ),
            (
                "analyzing-competitive-dynamics",
                "Maps competitive landscapes with market share tracking and Porter's Five Forces analysis. Use when analyzing competition, assessing market structure, or evaluating competitive threats.",
            ),
            (
                "modeling-margin-analysis",
                "Deconstructs gross, operating, and net margin trends with driver attribution and normalization. Use when analyzing profitability, attributing margin changes, or benchmarking margins.",
            ),
            (
                "analyzing-capital-allocation",
                "Evaluates management capital allocation decisions across M&A, buybacks, dividends, and reinvestment. Use when assessing capital allocation, analyzing ROIC, or evaluating shareholder return strategies.",
            ),
            (
                "tracking-sector-rotation",
                "Monitors sector performance rotation with factor exposure and macro sensitivity analysis. Use when tracking sector rotation, analyzing factor exposures, or identifying sector trends.",
            ),
            (
                "writing-investment-theses",
                "Formulates structured bull/bear investment theses with variant perception and key risk identification. Use when developing investment theses, articulating variant views, or structuring bull/bear arguments.",
            ),
            (
                "analyzing-earnings-quality",
                "Assesses earnings quality through accruals analysis, cash conversion, and accounting red flag identification. Use when evaluating earnings quality, detecting accounting anomalies, or analyzing accruals.",
            ),
            (
                "modeling-sum-of-parts-valuations",
                "Builds SOTP valuations for conglomerates and multi-segment companies with segment-appropriate methodologies. Use when valuing diversified companies, calculating conglomerate discounts, or modeling segment breakups.",
            ),
        ],
    },
    # ─── 2. FIXED INCOME / CREDIT ────────────────────────────────────
    "Fixed Income": {
        "description": "Bond analysis, credit assessment, and fixed income portfolio workflows",
        "practice_areas": ["Fixed Income", "Credit Research", "Bond Trading"],
        "skills": [
            (
                "analyzing-bond-structures",
                "Deconstructs bond indenture terms including covenants, call provisions, and credit support features. Use when analyzing bond structures, reviewing indentures, or evaluating bond terms.",
            ),
            (
                "assessing-credit-risk",
                "Evaluates borrower creditworthiness using financial analysis, industry assessment, and qualitative factors with structured credit opinions. Use when assessing credit risk, writing credit opinions, or evaluating borrower quality.",
            ),
            (
                "analyzing-yield-curves",
                "Interprets yield curve shapes with term structure analysis and relative value identification. Use when analyzing yield curves, identifying curve trades, or interpreting interest rate expectations.",
            ),
            (
                "modeling-bond-valuations",
                "Calculates bond pricing with duration, convexity, OAS, and Z-spread analysis. Use when pricing bonds, calculating risk metrics, or evaluating relative value.",
            ),
            (
                "analyzing-credit-ratings",
                "Interprets and anticipates credit rating actions with methodology analysis and surveillance monitoring. Use when analyzing credit ratings, predicting rating changes, or understanding rating methodology.",
            ),
            (
                "managing-duration-exposure",
                "Structures portfolio duration management with hedging strategies and benchmark tracking. Use when managing interest rate risk, hedging duration, or optimizing portfolio duration.",
            ),
            (
                "analyzing-municipal-bonds",
                "Evaluates municipal credit with revenue source analysis, tax considerations, and state/local economic assessment. Use when analyzing municipal bonds, evaluating GO vs revenue bonds, or assessing muni credit.",
            ),
            (
                "analyzing-high-yield-credit",
                "Structures high-yield credit analysis with recovery rate estimation and distressed debt evaluation. Use when analyzing high-yield bonds, estimating recovery rates, or evaluating distressed credits.",
            ),
            (
                "analyzing-structured-products",
                "Evaluates ABS, MBS, CLO, and CDO structures with cash flow waterfall and subordination analysis. Use when analyzing structured products, modeling cash flow waterfalls, or evaluating tranche risk.",
            ),
            (
                "analyzing-convertible-bonds",
                "Evaluates convertible bond structures with equity sensitivity, credit floor, and Greeks calculation. Use when analyzing convertibles, calculating conversion premiums, or evaluating hybrid instruments.",
            ),
            (
                "managing-credit-portfolio-risk",
                "Structures credit portfolio analysis with concentration metrics, correlation assessment, and stress testing. Use when managing credit portfolios, measuring concentration risk, or stress testing credit exposure.",
            ),
            (
                "analyzing-sovereign-debt",
                "Evaluates sovereign credit with fiscal analysis, external vulnerability, and political risk assessment. Use when analyzing sovereign bonds, assessing country risk, or evaluating government creditworthiness.",
            ),
            (
                "analyzing-leveraged-loans",
                "Structures leveraged loan analysis with covenant assessment, amendment tracking, and repricing risk. Use when analyzing leveraged loans, reviewing loan covenants, or evaluating loan market dynamics.",
            ),
            (
                "analyzing-credit-default-swaps",
                "Interprets CDS markets with basis analysis, curve dynamics, and credit event monitoring. Use when analyzing CDS spreads, monitoring credit events, or evaluating CDS basis.",
            ),
            (
                "managing-fixed-income-attribution",
                "Structures fixed income performance attribution across duration, credit, and sector allocation effects. Use when attributing fixed income returns, analyzing portfolio performance, or decomposing return drivers.",
            ),
            (
                "analyzing-inflation-linked-bonds",
                "Evaluates TIPS and inflation-linked securities with breakeven analysis and real yield assessment. Use when analyzing inflation bonds, calculating breakeven inflation, or evaluating real return.",
            ),
            (
                "managing-repo-and-funding",
                "Structures repo market analysis with collateral valuation, haircut assessment, and funding cost optimization. Use when managing repo positions, evaluating collateral, or optimizing funding costs.",
            ),
            (
                "analyzing-agency-mortgage-bonds",
                "Evaluates agency MBS with prepayment modeling, OAS analysis, and convexity assessment. Use when analyzing agency MBS, modeling prepayments, or evaluating mortgage bond convexity.",
            ),
            (
                "drafting-credit-memos",
                "Creates structured credit memos with borrower analysis, risk assessment, and recommendation justification. Use when writing credit memos, documenting credit decisions, or presenting credit recommendations.",
            ),
            (
                "analyzing-covenant-compliance",
                "Reviews financial covenant compliance calculations with cure provisions and default trigger analysis. Use when checking covenant compliance, calculating coverage ratios, or evaluating covenant headroom.",
            ),
        ],
    },
    # ─── 3. INVESTMENT BANKING / M&A ─────────────────────────────────
    "Investment Banking": {
        "description": "M&A advisory, capital markets, and transaction execution workflows",
        "practice_areas": [
            "Investment Banking",
            "Mergers and Acquisitions",
            "Corporate Finance",
        ],
        "skills": [
            (
                "drafting-investment-memos",
                "Creates structured investment memoranda with business description, financial analysis, valuation, and risk assessment for deal review. Use when writing investment memos, preparing deal summaries, or documenting investment recommendations.",
            ),
            (
                "creating-pitch-books",
                "Builds client pitch materials with market overview, strategic rationale, valuation analysis, and transaction positioning. Use when creating pitch books, preparing client presentations, or building deal marketing materials.",
            ),
            (
                "analyzing-comparable-transactions",
                "Structures precedent transaction analysis with deal multiples, premium calculation, and transaction characteristic comparison. Use when analyzing M&A precedents, calculating transaction multiples, or benchmarking deal terms.",
            ),
            (
                "building-merger-models",
                "Constructs merger consequence analysis with accretion/dilution, pro forma financials, and synergy assumptions. Use when modeling mergers, calculating accretion/dilution, or analyzing deal structures.",
            ),
            (
                "building-lbo-models",
                "Constructs leveraged buyout models with debt capacity, returns analysis, and exit scenarios. Use when modeling LBOs, calculating sponsor returns, or analyzing leveraged transactions.",
            ),
            (
                "drafting-offering-memoranda",
                "Creates confidential information memoranda (CIM) for sell-side M&A with business description and financial presentation. Use when preparing CIMs, writing sell-side materials, or creating offering documents.",
            ),
            (
                "managing-due-diligence-processes",
                "Structures buy-side and sell-side due diligence with workstream coordination and findings documentation. Use when managing due diligence, coordinating DD workstreams, or documenting diligence findings.",
            ),
            (
                "analyzing-fairness-opinions",
                "Evaluates fairness opinion analyses with valuation methodology review and conclusion assessment. Use when reviewing fairness opinions, analyzing board-level valuations, or evaluating transaction fairness.",
            ),
            (
                "preparing-board-materials",
                "Creates board presentation materials with strategic analysis, financial performance, and transaction recommendations. Use when preparing board decks, creating governance presentations, or summarizing strategic options.",
            ),
            (
                "managing-deal-processes",
                "Structures M&A process management with timeline tracking, bid analysis, and negotiation documentation. Use when managing sell-side auctions, tracking bid processes, or coordinating deal timelines.",
            ),
            (
                "analyzing-synergy-cases",
                "Structures revenue and cost synergy analysis with build-up methodology and realization timing. Use when estimating synergies, modeling cost savings, or analyzing revenue enhancement opportunities.",
            ),
            (
                "structuring-debt-financing",
                "Designs acquisition financing structures with leverage analysis, covenant negotiation, and capital structure optimization. Use when structuring deal financing, analyzing debt capacity, or negotiating loan terms.",
            ),
            (
                "analyzing-corporate-restructuring",
                "Evaluates restructuring alternatives with debt-for-equity analysis, 363 sale considerations, and recovery analysis. Use when analyzing restructurings, evaluating Chapter 11 options, or modeling recovery scenarios.",
            ),
            (
                "managing-ipo-processes",
                "Structures IPO execution with prospectus preparation, pricing analysis, and allocation methodology. Use when managing IPO processes, preparing S-1 filings, or analyzing IPO pricing.",
            ),
            (
                "analyzing-spin-off-transactions",
                "Evaluates corporate spin-off and separation transactions with standalone valuation and Remainco impact. Use when analyzing spin-offs, modeling separations, or evaluating corporate breakup value.",
            ),
            (
                "drafting-transaction-opinions",
                "Structures transaction opinion analysis with solvency, capital adequacy, and reasonably equivalent value assessment. Use when preparing transaction opinions, evaluating solvency, or assessing transaction fairness.",
            ),
            (
                "analyzing-cross-border-transactions",
                "Evaluates cross-border M&A considerations including currency, tax, regulatory, and cultural factors. Use when analyzing international deals, assessing cross-border risks, or structuring multinational transactions.",
            ),
            (
                "managing-data-room-operations",
                "Structures virtual data room organization with document indexing, access management, and Q&A tracking. Use when managing VDR operations, organizing deal documents, or tracking buyer questions.",
            ),
            (
                "analyzing-deal-financing-alternatives",
                "Compares financing alternatives including debt, equity, convertibles, and hybrid instruments for transactions. Use when evaluating financing options, comparing capital structure alternatives, or optimizing deal funding.",
            ),
            (
                "writing-engagement-letters",
                "Structures investment banking engagement terms with scope, fees, indemnification, and tail provisions. Use when drafting engagement letters, negotiating fee structures, or documenting advisory mandates.",
            ),
        ],
    },
    # ─── 4. PRIVATE EQUITY / VENTURE CAPITAL ─────────────────────────
    "Private Equity": {
        "description": "PE/VC investment evaluation, portfolio management, and fund operations workflows",
        "practice_areas": ["Private Equity", "Venture Capital", "Growth Equity"],
        "skills": [
            (
                "evaluating-investment-opportunities",
                "Structures PE/VC investment evaluation with business model assessment, market analysis, and return potential. Use when evaluating deals, screening investment opportunities, or assessing company fit.",
            ),
            (
                "conducting-commercial-due-diligence",
                "Structures commercial diligence with market sizing, competitive dynamics, and customer reference analysis. Use when conducting CDD, analyzing target markets, or validating commercial assumptions.",
            ),
            (
                "modeling-portfolio-company-returns",
                "Builds PE return models with entry/exit multiples, leverage analysis, and value creation attribution. Use when modeling PE returns, calculating IRR/MOIC, or attributing value creation drivers.",
            ),
            (
                "writing-investment-committee-memos",
                "Creates IC presentation materials with deal thesis, risk analysis, and recommendation structure. Use when preparing IC memos, presenting deal opportunities, or documenting investment decisions.",
            ),
            (
                "managing-portfolio-company-reporting",
                "Structures portfolio company monitoring with KPI tracking, budget variance, and management assessment. Use when monitoring portfolio companies, tracking financial performance, or preparing portfolio reviews.",
            ),
            (
                "analyzing-venture-deal-terms",
                "Evaluates VC term sheet provisions with economic and control analysis and cap table impact. Use when analyzing term sheets, negotiating deal terms, or modeling cap table outcomes.",
            ),
            (
                "managing-fund-reporting",
                "Structures LP fund reporting with NAV calculation, performance attribution, and portfolio updates. Use when preparing LP reports, calculating fund performance, or creating quarterly updates.",
            ),
            (
                "conducting-operational-due-diligence",
                "Structures operational diligence with management assessment, systems evaluation, and integration planning. Use when evaluating target operations, assessing management capabilities, or planning post-close integration.",
            ),
            (
                "modeling-cap-table-scenarios",
                "Builds cap table models with round-by-round dilution, option pool, and exit waterfall analysis. Use when modeling cap tables, calculating ownership dilution, or projecting exit proceeds.",
            ),
            (
                "managing-value-creation-plans",
                "Structures 100-day and long-term value creation plans with initiative tracking and KPI targets. Use when building value creation plans, tracking improvement initiatives, or managing post-acquisition integration.",
            ),
            (
                "analyzing-add-on-acquisitions",
                "Evaluates platform add-on opportunities with strategic fit, synergy potential, and return contribution. Use when analyzing add-on M&A, evaluating bolt-on targets, or building platform acquisition strategies.",
            ),
            (
                "managing-fundraising-processes",
                "Structures PE/VC fundraising with LP outreach, DDQ completion, and closing documentation. Use when managing fund raises, completing due diligence questionnaires, or preparing fundraising materials.",
            ),
            (
                "analyzing-exit-strategies",
                "Evaluates exit alternatives (IPO, strategic sale, secondary, recapitalization) with timing and return analysis. Use when planning exits, evaluating exit routes, or modeling exit scenarios.",
            ),
            (
                "conducting-management-assessments",
                "Structures executive evaluation with leadership capabilities, organizational gaps, and bench strength analysis. Use when assessing management teams, evaluating CEO/CFO capabilities, or identifying talent gaps.",
            ),
            (
                "managing-co-investment-processes",
                "Structures co-investment offerings with allocation, terms, and LP communication documentation. Use when managing co-investments, structuring co-invest terms, or documenting LP allocations.",
            ),
            (
                "analyzing-sector-theses",
                "Develops investment sector theses with market mapping, trend analysis, and opportunity identification. Use when building sector strategies, mapping target markets, or identifying investment themes.",
            ),
            (
                "managing-esg-in-private-equity",
                "Structures ESG integration in PE investment process with screening, monitoring, and reporting frameworks. Use when implementing PE ESG, screening investments for ESG, or reporting ESG metrics.",
            ),
            (
                "analyzing-secondary-transactions",
                "Evaluates secondary market transactions with NAV assessment, discount/premium analysis, and portfolio evaluation. Use when analyzing secondary deals, pricing LP interests, or evaluating GP-led secondaries.",
            ),
            (
                "managing-portfolio-company-governance",
                "Structures board governance for portfolio companies with reporting cadence and strategic oversight documentation. Use when managing portfolio boards, structuring governance frameworks, or documenting board practices.",
            ),
            (
                "analyzing-continuation-vehicles",
                "Evaluates GP-led continuation fund structures with existing LP options and new investor terms. Use when analyzing continuation vehicles, structuring GP-led transactions, or evaluating tender offers.",
            ),
        ],
    },
    # ─── 5. ASSET MANAGEMENT / PORTFOLIO MANAGEMENT ──────────────────
    "Asset Management": {
        "description": "Portfolio construction, risk management, and investment operations workflows",
        "practice_areas": [
            "Portfolio Management",
            "Asset Management",
            "Wealth Management",
        ],
        "skills": [
            (
                "constructing-portfolio-allocations",
                "Builds strategic and tactical asset allocation models with risk-return optimization and constraint management. Use when constructing portfolios, optimizing asset allocation, or building model portfolios.",
            ),
            (
                "benchmarking-portfolio-performance",
                "Conducts portfolio performance measurement with benchmark comparison, attribution, and risk-adjusted metrics. Use when measuring portfolio performance, calculating Sharpe/Sortino ratios, or conducting performance attribution.",
            ),
            (
                "managing-portfolio-rebalancing",
                "Structures rebalancing processes with drift monitoring, tax-aware trading, and transaction cost optimization. Use when rebalancing portfolios, managing allocation drift, or optimizing trading costs.",
            ),
            (
                "analyzing-factor-exposures",
                "Decomposes portfolio factor exposures (value, growth, momentum, quality, size) with benchmark relative analysis. Use when analyzing factor tilts, decomposing returns, or managing style exposure.",
            ),
            (
                "managing-investment-policy-statements",
                "Creates and maintains IPS documents with objectives, constraints, and governance requirements. Use when writing investment policy statements, documenting investment guidelines, or updating policy parameters.",
            ),
            (
                "analyzing-alternative-investments",
                "Evaluates alternative investment strategies (hedge funds, real assets, private markets) with risk-return and liquidity analysis. Use when analyzing alternatives, evaluating fund strategies, or assessing illiquidity premiums.",
            ),
            (
                "managing-tax-loss-harvesting",
                "Identifies and executes tax-loss harvesting opportunities with wash sale compliance and tracking. Use when harvesting tax losses, managing wash sale rules, or optimizing after-tax returns.",
            ),
            (
                "generating-client-portfolio-reports",
                "Creates client-facing portfolio reports with performance, allocation, commentary, and outlook. Use when producing client reports, preparing quarterly reviews, or creating portfolio summaries.",
            ),
            (
                "managing-cash-flow-modeling",
                "Models portfolio cash flows for liability-driven and income-oriented investment strategies. Use when modeling portfolio cash flows, planning income distributions, or managing liability matching.",
            ),
            (
                "analyzing-currency-exposure",
                "Evaluates and manages portfolio currency risk with hedging strategy analysis and cost assessment. Use when analyzing FX exposure, planning currency hedges, or assessing hedging costs.",
            ),
            (
                "managing-concentrated-positions",
                "Structures diversification strategies for concentrated single-stock positions with tax and risk considerations. Use when managing concentrated holdings, planning diversification, or evaluating exchange funds.",
            ),
            (
                "analyzing-esg-integration",
                "Integrates ESG factors into investment analysis with scoring methodology and impact measurement. Use when implementing ESG integration, scoring ESG factors, or measuring sustainability impact.",
            ),
            (
                "managing-model-portfolio-governance",
                "Structures investment committee processes with model approval, modification, and compliance documentation. Use when managing model portfolios, documenting investment decisions, or tracking portfolio changes.",
            ),
            (
                "analyzing-private-market-allocations",
                "Structures private market allocation strategy with commitment pacing, J-curve modeling, and liquidity planning. Use when allocating to private markets, modeling commitment pacing, or planning illiquid allocations.",
            ),
            (
                "managing-portfolio-risk-budgeting",
                "Allocates portfolio risk across asset classes and strategies with tracking error and VaR budgeting. Use when budgeting portfolio risk, managing tracking error, or allocating risk capital.",
            ),
            (
                "analyzing-manager-selection",
                "Evaluates and selects investment managers with quantitative screening and qualitative assessment. Use when selecting fund managers, conducting manager due diligence, or evaluating strategy fit.",
            ),
            (
                "managing-portfolio-transitions",
                "Structures portfolio transitions with legacy position analysis, rebalancing path, and transition cost management. Use when transitioning portfolios, managing manager changes, or planning portfolio restructuring.",
            ),
            (
                "analyzing-multi-asset-strategies",
                "Evaluates multi-asset investment strategies with regime analysis and dynamic allocation models. Use when analyzing multi-asset funds, evaluating tactical allocation, or assessing regime-based strategies.",
            ),
            (
                "managing-separately-managed-accounts",
                "Structures SMA operations with customization, compliance overlay, and performance composites. Use when managing SMAs, implementing custom portfolios, or maintaining performance composites.",
            ),
            (
                "analyzing-liquidity-risk",
                "Assesses portfolio liquidity with redemption stress testing and market impact estimation. Use when analyzing liquidity risk, stress testing redemptions, or evaluating market impact.",
            ),
        ],
    },
    # ─── 6. RISK MANAGEMENT ──────────────────────────────────────────
    "Risk Management": {
        "description": "Enterprise, market, credit, and operational risk management workflows",
        "practice_areas": ["Risk Management", "Enterprise Risk", "Market Risk"],
        "skills": [
            (
                "calculating-value-at-risk",
                "Computes VaR using parametric, historical simulation, and Monte Carlo methods with backtesting validation. Use when calculating VaR, comparing risk methodologies, or backtesting risk models.",
            ),
            (
                "conducting-stress-testing",
                "Designs and executes portfolio and enterprise stress tests with scenario specification and result analysis. Use when stress testing portfolios, designing stress scenarios, or analyzing stress test results.",
            ),
            (
                "managing-counterparty-risk",
                "Structures counterparty credit risk assessment with exposure calculation and mitigation monitoring. Use when assessing counterparty risk, calculating potential future exposure, or managing collateral.",
            ),
            (
                "managing-operational-risk",
                "Structures operational risk assessment with loss event classification, RCSA, and KRI monitoring. Use when managing operational risk, conducting risk assessments, or tracking key risk indicators.",
            ),
            (
                "managing-model-risk",
                "Structures model validation with independent testing, limitation documentation, and ongoing monitoring. Use when validating risk models, documenting model limitations, or managing model governance.",
            ),
            (
                "managing-liquidity-risk",
                "Structures liquidity risk management with cash flow projections, stress testing, and contingency planning. Use when managing liquidity risk, projecting cash needs, or developing liquidity contingency plans.",
            ),
            (
                "conducting-risk-appetite-frameworks",
                "Develops risk appetite statements with quantitative limits and qualitative boundaries documentation. Use when defining risk appetite, setting risk limits, or calibrating risk tolerances.",
            ),
            (
                "managing-concentration-risk",
                "Identifies and monitors portfolio concentration across counterparties, sectors, geographies, and instruments. Use when analyzing concentration risk, setting exposure limits, or monitoring concentration breaches.",
            ),
            (
                "analyzing-scenario-analysis",
                "Structures forward-looking scenario analysis with macroeconomic assumptions and portfolio impact assessment. Use when conducting scenario analysis, modeling macro scenarios, or assessing portfolio vulnerability.",
            ),
            (
                "managing-risk-reporting",
                "Structures risk reporting dashboards with limit utilization, risk metric trends, and exception documentation. Use when creating risk reports, designing risk dashboards, or documenting risk positions.",
            ),
            (
                "managing-credit-risk-models",
                "Evaluates and monitors credit risk models (PD, LGD, EAD) with calibration and discrimination metrics. Use when validating credit models, assessing model performance, or calibrating default models.",
            ),
            (
                "managing-market-risk-limits",
                "Structures market risk limit frameworks with VaR, sensitivity, and notional-based limits and escalation protocols. Use when setting market risk limits, managing limit breaches, or calibrating risk parameters.",
            ),
            (
                "analyzing-tail-risk",
                "Evaluates portfolio tail risk with extreme value theory, expected shortfall, and tail hedge strategies. Use when analyzing tail risk, estimating expected shortfall, or evaluating tail protection.",
            ),
            (
                "managing-climate-risk",
                "Structures climate risk assessment with physical and transition risk analysis and scenario modeling. Use when assessing climate risk, modeling transition scenarios, or evaluating environmental exposure.",
            ),
            (
                "managing-cyber-risk-financial",
                "Structures financial sector cyber risk assessment with scenario quantification and insurance evaluation. Use when assessing cyber risk, quantifying cyber exposure, or evaluating cyber insurance.",
            ),
            (
                "managing-third-party-risk",
                "Structures vendor and third-party risk assessment with due diligence, monitoring, and concentration analysis. Use when assessing vendor risk, conducting third-party due diligence, or monitoring outsourcing risk.",
            ),
            (
                "managing-reputational-risk",
                "Structures reputational risk identification with scenario planning and mitigation strategy documentation. Use when assessing reputational risk, planning crisis scenarios, or documenting reputation management.",
            ),
            (
                "conducting-risk-control-self-assessments",
                "Designs and facilitates RCSA processes with risk identification, control evaluation, and action planning. Use when conducting RCSAs, evaluating internal controls, or identifying emerging risks.",
            ),
            (
                "managing-emerging-risk-identification",
                "Structures emerging risk scanning with horizon analysis and early warning indicator development. Use when identifying emerging risks, scanning for new threats, or developing early warning systems.",
            ),
            (
                "managing-risk-governance",
                "Structures risk governance frameworks with committee charters, escalation protocols, and reporting cadences. Use when designing risk governance, structuring risk committees, or documenting governance frameworks.",
            ),
        ],
    },
    # ─── 7. COMPLIANCE & REGULATION ──────────────────────────────────
    "Financial Compliance": {
        "description": "Regulatory compliance, examination preparation, and regulatory change management",
        "practice_areas": [
            "Regulatory Compliance",
            "Financial Regulation",
            "Compliance",
        ],
        "skills": [
            (
                "auditing-aml-transactions",
                "Screens transaction data for suspicious patterns using red flag typologies and structures SAR narrative elements. Use when reviewing transactions for AML, identifying suspicious activity, or drafting SAR narratives.",
            ),
            (
                "reviewing-kyc-documentation",
                "Evaluates customer identification and verification documentation against CIP/CDD/EDD requirements. Use when reviewing KYC files, validating customer identification, or assessing customer risk.",
            ),
            (
                "managing-regulatory-examinations",
                "Structures regulatory exam preparation with document production, findings response, and remediation tracking. Use when preparing for regulatory exams, responding to examination findings, or managing exam timelines.",
            ),
            (
                "tracking-regulatory-changes",
                "Monitors regulatory developments with impact assessment, gap analysis, and implementation timeline planning. Use when tracking regulatory changes, assessing compliance gaps, or planning implementation.",
            ),
            (
                "managing-compliance-testing",
                "Designs and executes compliance testing programs with sampling methodology and findings documentation. Use when conducting compliance testing, designing test procedures, or documenting testing results.",
            ),
            (
                "managing-sanctions-screening",
                "Structures OFAC and global sanctions screening with match investigation and escalation protocols. Use when screening for sanctions, investigating potential matches, or managing sanctions compliance.",
            ),
            (
                "managing-trade-surveillance",
                "Monitors trading activity for market manipulation, insider trading, and best execution compliance. Use when conducting trade surveillance, investigating suspicious trading, or monitoring execution quality.",
            ),
            (
                "managing-advertising-compliance",
                "Reviews marketing materials against SEC, FINRA, and state regulatory requirements. Use when reviewing investment advertising, ensuring compliance of marketing materials, or managing ad review.",
            ),
            (
                "managing-fiduciary-compliance",
                "Evaluates advisory practices against fiduciary standards with conflict identification and disclosure requirements. Use when assessing fiduciary duties, managing conflicts of interest, or documenting fiduciary compliance.",
            ),
            (
                "managing-privacy-compliance-financial",
                "Evaluates data privacy practices against GLBA, CCPA, and state privacy requirements. Use when assessing financial privacy compliance, managing opt-out requirements, or documenting data practices.",
            ),
            (
                "managing-broker-dealer-compliance",
                "Structures BD compliance monitoring with supervision, registration, and reporting requirements. Use when managing BD compliance, reviewing supervisory procedures, or monitoring registration requirements.",
            ),
            (
                "managing-investment-adviser-compliance",
                "Structures IA compliance with Form ADV, custody rule, and Code of Ethics requirements. Use when managing IA compliance, updating Form ADV, or reviewing Code of Ethics.",
            ),
            (
                "conducting-compliance-risk-assessments",
                "Structures compliance risk assessment with regulatory inventory and inherent/residual risk evaluation. Use when assessing compliance risk, inventorying regulatory obligations, or prioritizing compliance resources.",
            ),
            (
                "managing-whistleblower-programs",
                "Structures whistleblower program operations with intake, investigation, and anti-retaliation documentation. Use when managing whistleblower reports, investigating complaints, or documenting anti-retaliation measures.",
            ),
            (
                "managing-code-of-ethics-compliance",
                "Monitors personal trading, outside activities, and gift/entertainment compliance with documentation. Use when reviewing personal trading, monitoring outside activities, or managing ethics compliance.",
            ),
            (
                "managing-vendor-due-diligence-compliance",
                "Structures regulatory vendor due diligence with risk assessment and ongoing monitoring requirements. Use when conducting vendor DD, assessing outsourcing risk, or managing third-party compliance.",
            ),
            (
                "managing-senior-investor-protection",
                "Structures senior and vulnerable investor protection programs with exploitation identification and hold protocols. Use when protecting senior investors, identifying financial exploitation, or implementing hold procedures.",
            ),
            (
                "managing-cybersecurity-compliance",
                "Evaluates cybersecurity programs against SEC, FINRA, and state regulatory requirements. Use when assessing cybersecurity compliance, implementing security frameworks, or responding to cyber requirements.",
            ),
            (
                "managing-regulation-best-interest",
                "Evaluates compliance with Regulation Best Interest including disclosure, care, and conflict obligations. Use when implementing Reg BI, reviewing recommendation practices, or documenting BI compliance.",
            ),
            (
                "managing-cross-border-compliance",
                "Structures cross-border compliance with multi-jurisdictional regulatory requirements and conflict resolution. Use when managing international compliance, navigating multi-jurisdictional rules, or resolving regulatory conflicts.",
            ),
        ],
    },
    # ─── 8. CORPORATE FINANCE / TREASURY ─────────────────────────────
    "Corporate Finance": {
        "description": "Corporate financial planning, treasury management, and capital structure workflows",
        "practice_areas": ["Corporate Finance", "Treasury", "Financial Planning"],
        "skills": [
            (
                "building-financial-projections",
                "Constructs integrated three-statement financial models with scenario analysis and assumption documentation. Use when building financial models, projecting financial statements, or creating forecast scenarios.",
            ),
            (
                "managing-capital-structure",
                "Analyzes optimal capital structure with WACC minimization, rating implications, and financing alternatives. Use when optimizing capital structure, analyzing debt capacity, or evaluating leverage targets.",
            ),
            (
                "managing-cash-flow-forecasting",
                "Structures short and long-term cash flow forecasting with variance analysis and liquidity planning. Use when forecasting cash flows, planning liquidity, or analyzing cash flow variances.",
            ),
            (
                "managing-dividend-policy",
                "Evaluates dividend policy options with payout ratio analysis, sustainability assessment, and shareholder return comparison. Use when setting dividend policy, analyzing payout sustainability, or comparing return alternatives.",
            ),
            (
                "managing-share-repurchase-programs",
                "Structures buyback program analysis with timing, accretion impact, and regulatory compliance documentation. Use when analyzing buybacks, modeling EPS accretion, or documenting repurchase programs.",
            ),
            (
                "conducting-cost-of-capital-analysis",
                "Calculates WACC components with equity risk premium, beta estimation, and debt cost measurement. Use when calculating cost of capital, estimating WACC, or analyzing discount rates.",
            ),
            (
                "managing-working-capital",
                "Optimizes working capital with DSO, DPO, and DIO analysis and improvement initiative tracking. Use when managing working capital, analyzing cash conversion cycle, or improving collection/payment terms.",
            ),
            (
                "managing-foreign-exchange-hedging",
                "Structures FX hedging programs with exposure identification, instrument selection, and hedge effectiveness testing. Use when managing FX risk, designing hedge programs, or testing hedge effectiveness.",
            ),
            (
                "managing-interest-rate-hedging",
                "Structures interest rate hedging with swap, cap, and collar analysis and hedge accounting documentation. Use when hedging interest rate risk, selecting hedging instruments, or documenting hedge relationships.",
            ),
            (
                "managing-credit-facility-administration",
                "Tracks revolving credit facility compliance with borrowing base, covenant calculations, and amendment documentation. Use when managing credit facilities, calculating borrowing availability, or tracking covenants.",
            ),
            (
                "managing-pension-fund-obligations",
                "Structures pension analysis with funded status, actuarial assumptions, and contribution planning. Use when analyzing pension obligations, reviewing actuarial reports, or planning pension contributions.",
            ),
            (
                "managing-lease-accounting",
                "Structures ASC 842 lease analysis with classification, measurement, and disclosure requirements. Use when managing lease accounting, classifying leases, or calculating right-of-use assets.",
            ),
            (
                "managing-intercompany-transactions",
                "Structures intercompany pricing with transfer pricing documentation and arm's-length analysis. Use when managing transfer pricing, documenting intercompany transactions, or ensuring arm's-length compliance.",
            ),
            (
                "managing-insurance-programs",
                "Structures corporate insurance program analysis with coverage adequacy and renewal documentation. Use when managing insurance programs, analyzing coverage, or documenting insurance renewals.",
            ),
            (
                "managing-corporate-budgeting",
                "Structures annual budget processes with bottom-up development, consolidation, and variance tracking. Use when managing budgeting processes, consolidating budget submissions, or tracking budget variances.",
            ),
            (
                "conducting-working-capital-due-diligence",
                "Analyzes target company working capital for M&A with normalization, peg calculation, and adjustment mechanics. Use when analyzing WC for transactions, calculating WC pegs, or structuring WC adjustment mechanisms.",
            ),
            (
                "managing-debt-covenant-compliance",
                "Tracks financial covenant compliance with calculation methodology and certification requirements. Use when monitoring covenants, calculating compliance metrics, or preparing compliance certificates.",
            ),
            (
                "managing-corporate-credit-ratings",
                "Structures credit rating agency relationship management with rating methodology analysis and presentation preparation. Use when managing rating relationships, preparing rating presentations, or analyzing rating criteria.",
            ),
            (
                "managing-subsidiary-financing",
                "Structures subsidiary-level financing with upstream guarantee analysis and structural subordination considerations. Use when financing subsidiaries, analyzing guarantee structures, or evaluating structural subordination.",
            ),
            (
                "managing-capital-expenditure-planning",
                "Structures capex evaluation with ROI analysis, approval workflows, and project tracking. Use when evaluating capital projects, analyzing investment returns, or managing capex budgets.",
            ),
        ],
    },
    # ─── 9. ACCOUNTING / FINANCIAL REPORTING ─────────────────────────
    "Accounting": {
        "description": "Financial reporting, audit, and accounting standards workflows",
        "practice_areas": ["Financial Reporting", "Audit", "Accounting"],
        "skills": [
            (
                "synthesizing-financial-statements",
                "Analyzes 10-K/10-Q filings to extract key metrics, identify trends, and create structured YoY comparisons. Use when analyzing SEC filings, comparing financial statements, or tracking company financial trends.",
            ),
            (
                "executing-month-end-close",
                "Structures month-end close procedures with journal entry preparation, reconciliation, and variance analysis. Use when performing month-end close, preparing close checklists, or analyzing period variances.",
            ),
            (
                "reconciling-accounts",
                "Compares multiple data sources to produce reconciliation reports with break identification and aging analysis. Use when reconciling accounts, identifying breaks, or performing bank reconciliations.",
            ),
            (
                "managing-revenue-recognition",
                "Applies ASC 606 five-step model with contract analysis, performance obligation identification, and allocation documentation. Use when analyzing revenue contracts, applying ASC 606, or documenting revenue recognition.",
            ),
            (
                "managing-lease-accounting-asc842",
                "Structures ASC 842 compliance with lease identification, classification, measurement, and transition documentation. Use when implementing ASC 842, classifying leases, or calculating lease liabilities.",
            ),
            (
                "managing-impairment-testing",
                "Structures goodwill and long-lived asset impairment testing with fair value estimation and documentation. Use when testing for impairment, estimating fair values, or documenting impairment analysis.",
            ),
            (
                "managing-equity-compensation-accounting",
                "Structures stock-based compensation accounting with fair value measurement and expense recognition. Use when accounting for equity comp, calculating Black-Scholes values, or documenting share-based payments.",
            ),
            (
                "managing-income-tax-provisions",
                "Structures income tax provision calculation with current/deferred components and rate reconciliation. Use when calculating tax provisions, analyzing deferred taxes, or preparing rate reconciliations.",
            ),
            (
                "managing-consolidation-accounting",
                "Structures consolidation procedures with intercompany elimination, minority interest, and foreign currency translation. Use when performing consolidations, eliminating intercompany transactions, or translating foreign subsidiaries.",
            ),
            (
                "managing-audit-preparation",
                "Structures external audit preparation with PBC list management, supporting documentation, and inquiry responses. Use when preparing for external audit, organizing PBC items, or responding to audit inquiries.",
            ),
            (
                "managing-internal-audit",
                "Structures internal audit planning and execution with risk assessment, testing, and findings documentation. Use when planning internal audits, conducting audit testing, or documenting audit findings.",
            ),
            (
                "managing-sox-compliance",
                "Structures SOX compliance with control documentation, testing, and deficiency evaluation. Use when managing SOX compliance, testing internal controls, or evaluating control deficiencies.",
            ),
            (
                "managing-business-combinations",
                "Structures acquisition accounting with purchase price allocation, fair value measurement, and goodwill calculation. Use when accounting for acquisitions, allocating purchase price, or measuring fair values.",
            ),
            (
                "managing-segment-reporting",
                "Structures segment reporting with operating segment identification, measurement, and disclosure requirements. Use when preparing segment disclosures, identifying operating segments, or allocating intersegment items.",
            ),
            (
                "managing-fair-value-measurement",
                "Applies ASC 820 fair value framework with hierarchy classification and valuation technique documentation. Use when measuring fair values, classifying in the fair value hierarchy, or documenting valuation approaches.",
            ),
            (
                "managing-sec-reporting",
                "Structures SEC filing preparation with 10-K, 10-Q, 8-K content requirements and XBRL tagging. Use when preparing SEC filings, reviewing filing content, or managing XBRL tagging.",
            ),
            (
                "managing-earnings-releases",
                "Structures earnings release preparation with GAAP/non-GAAP reconciliation and forward guidance documentation. Use when preparing earnings releases, reconciling non-GAAP measures, or drafting press releases.",
            ),
            (
                "managing-accounting-policy-changes",
                "Evaluates new accounting standard impacts with transition planning and disclosure preparation. Use when implementing new standards, assessing ASU impacts, or planning accounting transitions.",
            ),
            (
                "managing-foreign-currency-accounting",
                "Structures foreign currency transaction and translation accounting with hedge documentation. Use when accounting for FX transactions, translating foreign operations, or documenting FX hedges.",
            ),
            (
                "managing-debt-and-equity-issuance",
                "Structures accounting for debt and equity issuances with classification, measurement, and issuance cost treatment. Use when accounting for debt issuance, recording equity offerings, or classifying hybrid instruments.",
            ),
        ],
    },
    # ─── 10. REAL ESTATE ─────────────────────────────────────────────
    "Real Estate Finance": {
        "description": "Real estate investment analysis, property finance, and REIT workflows",
        "practice_areas": [
            "Real Estate Finance",
            "REIT Analysis",
            "Property Investment",
        ],
        "skills": [
            (
                "analyzing-property-valuations",
                "Structures real estate valuation with income, comparable sales, and cost approaches. Use when valuing properties, performing appraisal analysis, or comparing valuation methodologies.",
            ),
            (
                "building-real-estate-pro-formas",
                "Constructs property pro forma models with rent roll analysis, expense projections, and cash flow forecasting. Use when building real estate models, projecting property cash flows, or analyzing investment returns.",
            ),
            (
                "analyzing-reit-financials",
                "Evaluates REIT financial performance with FFO, AFFO, NAV, and leverage metrics. Use when analyzing REITs, calculating FFO/AFFO, or comparing REIT valuations.",
            ),
            (
                "managing-loan-underwriting-real-estate",
                "Structures commercial real estate loan underwriting with DSCR, LTV, and debt yield analysis. Use when underwriting CRE loans, calculating coverage ratios, or evaluating loan terms.",
            ),
            (
                "analyzing-lease-structures",
                "Evaluates commercial lease terms with net effective rent, concession analysis, and tenant credit assessment. Use when analyzing leases, calculating effective rents, or comparing lease structures.",
            ),
            (
                "managing-construction-lending",
                "Structures construction loan analysis with draw schedules, budget tracking, and completion risk assessment. Use when managing construction loans, tracking draw requests, or monitoring construction progress.",
            ),
            (
                "analyzing-cap-rates",
                "Structures capitalization rate analysis with market comparison, risk premium decomposition, and trend assessment. Use when analyzing cap rates, comparing market yields, or assessing pricing trends.",
            ),
            (
                "managing-property-due-diligence",
                "Structures real estate due diligence with physical inspection, environmental review, and title analysis coordination. Use when conducting property DD, reviewing environmental reports, or coordinating due diligence workstreams.",
            ),
            (
                "analyzing-real-estate-markets",
                "Structures real estate market analysis with supply/demand dynamics, absorption rates, and rent growth projections. Use when analyzing real estate markets, forecasting market conditions, or evaluating market fundamentals.",
            ),
            (
                "managing-reit-portfolio-analysis",
                "Structures REIT portfolio evaluation with property-level analysis, geographic diversification, and tenant concentration. Use when analyzing REIT portfolios, evaluating property mix, or assessing concentration risk.",
            ),
            (
                "managing-real-estate-fund-reporting",
                "Structures real estate fund reporting with property-level performance, valuation updates, and distribution analysis. Use when preparing real estate fund reports, calculating fund returns, or documenting property performance.",
            ),
            (
                "analyzing-development-feasibility",
                "Evaluates real estate development projects with cost analysis, return projections, and risk assessment. Use when analyzing development deals, projecting development returns, or assessing feasibility.",
            ),
            (
                "managing-property-disposition",
                "Structures property sale processes with broker opinion of value, marketing strategy, and bid analysis. Use when managing property sales, evaluating offers, or coordinating disposition processes.",
            ),
            (
                "analyzing-multifamily-investments",
                "Structures multifamily property analysis with rent comps, expense benchmarking, and value-add assessment. Use when analyzing apartment investments, comparing rent levels, or evaluating value-add opportunities.",
            ),
            (
                "managing-cmbs-analysis",
                "Evaluates CMBS structures with loan-level analysis, subordination assessment, and special servicing monitoring. Use when analyzing CMBS deals, reviewing loan pools, or monitoring CMBS performance.",
            ),
            (
                "analyzing-industrial-properties",
                "Structures industrial real estate analysis with logistics market assessment and tenant credit evaluation. Use when analyzing industrial properties, evaluating warehouse investments, or assessing logistics demand.",
            ),
            (
                "managing-real-estate-tax-considerations",
                "Structures real estate tax planning with 1031 exchange, depreciation, and opportunity zone analysis. Use when planning real estate taxes, structuring 1031 exchanges, or analyzing tax implications.",
            ),
            (
                "analyzing-hospitality-investments",
                "Structures hotel and hospitality investment analysis with RevPAR, ADR, and operational benchmarking. Use when analyzing hotel investments, benchmarking hospitality metrics, or evaluating hotel performance.",
            ),
            (
                "managing-real-estate-debt-funds",
                "Structures real estate debt fund analysis with loan origination, portfolio management, and credit metrics. Use when analyzing RE debt funds, evaluating loan portfolios, or managing debt fund performance.",
            ),
            (
                "analyzing-retail-properties",
                "Structures retail property analysis with tenant sales productivity, co-tenancy evaluation, and redevelopment potential. Use when analyzing retail properties, evaluating tenant performance, or assessing redevelopment.",
            ),
        ],
    },
    # ─── 11. INSURANCE ───────────────────────────────────────────────
    "Insurance": {
        "description": "Insurance analysis, underwriting, and actuarial workflows",
        "practice_areas": ["Insurance", "Actuarial Science", "Reinsurance"],
        "skills": [
            (
                "analyzing-insurance-financials",
                "Structures insurance company financial analysis with combined ratio, reserve adequacy, and capital metrics. Use when analyzing insurance financials, evaluating combined ratios, or assessing reserve strength.",
            ),
            (
                "managing-underwriting-analysis",
                "Structures underwriting evaluation with risk assessment, pricing analysis, and terms documentation. Use when evaluating underwriting risk, analyzing pricing adequacy, or documenting underwriting decisions.",
            ),
            (
                "analyzing-loss-reserves",
                "Evaluates loss reserve adequacy with development triangle analysis and actuarial methods. Use when analyzing reserves, interpreting loss triangles, or assessing reserve adequacy.",
            ),
            (
                "managing-reinsurance-programs",
                "Structures reinsurance program analysis with cession optimization, pricing, and counterparty evaluation. Use when analyzing reinsurance, optimizing cession structures, or evaluating reinsurer credit.",
            ),
            (
                "analyzing-catastrophe-risk",
                "Structures catastrophe risk assessment with model output interpretation and accumulation monitoring. Use when analyzing cat risk, interpreting cat model results, or managing cat exposure.",
            ),
            (
                "managing-insurance-regulatory-filings",
                "Structures statutory filing preparation with SAP differences, risk-based capital, and annual statement schedules. Use when preparing statutory filings, calculating RBC, or managing regulatory submissions.",
            ),
            (
                "analyzing-premium-pricing",
                "Structures actuarial pricing analysis with loss cost estimation, expense loading, and rate adequacy testing. Use when analyzing premium rates, calculating rate indications, or assessing pricing adequacy.",
            ),
            (
                "managing-claims-analysis",
                "Structures claims data analysis with severity/frequency trending, case reserve monitoring, and litigation management. Use when analyzing claims data, trending claim frequency, or monitoring claim severity.",
            ),
            (
                "analyzing-insurance-investments",
                "Evaluates insurance company investment portfolios with ALM considerations and regulatory constraints. Use when analyzing insurer investments, managing ALM, or evaluating portfolio compliance.",
            ),
            (
                "managing-surplus-lines-compliance",
                "Structures surplus lines compliance with eligibility verification, tax filing, and reporting requirements. Use when managing surplus lines, verifying eligibility, or documenting E&S compliance.",
            ),
            (
                "analyzing-life-insurance-products",
                "Evaluates life insurance product structures with cash value analysis, cost comparisons, and suitability assessment. Use when analyzing life products, comparing insurance costs, or assessing product suitability.",
            ),
            (
                "managing-insurance-fraud-detection",
                "Structures insurance fraud detection with red flag identification, investigation protocols, and SIU referral documentation. Use when detecting insurance fraud, investigating suspicious claims, or documenting fraud indicators.",
            ),
            (
                "analyzing-health-insurance-plans",
                "Evaluates health insurance plan structures with actuarial value, network analysis, and cost projection. Use when analyzing health plans, comparing coverage, or projecting healthcare costs.",
            ),
            (
                "managing-insurtech-evaluations",
                "Evaluates insurance technology solutions with business case analysis and implementation assessment. Use when evaluating insurtech, assessing technology solutions, or analyzing digital insurance platforms.",
            ),
            (
                "analyzing-cyber-insurance",
                "Structures cyber insurance evaluation with coverage assessment, limit adequacy, and claims scenario analysis. Use when evaluating cyber coverage, analyzing policy terms, or assessing cyber insurance adequacy.",
            ),
            (
                "managing-insurance-capital-modeling",
                "Structures insurance capital model analysis with economic capital, regulatory capital, and rating agency capital comparison. Use when modeling insurance capital, comparing capital frameworks, or assessing capital adequacy.",
            ),
            (
                "analyzing-property-casualty-lines",
                "Evaluates P&C insurance lines with market cycle analysis, loss cost trending, and competitive assessment. Use when analyzing P&C markets, tracking insurance cycles, or evaluating line profitability.",
            ),
            (
                "managing-insurance-distribution",
                "Structures insurance distribution analysis with channel economics, producer management, and compensation modeling. Use when analyzing distribution, evaluating producer performance, or modeling commission structures.",
            ),
            (
                "analyzing-annuity-products",
                "Evaluates annuity structures with guaranteed benefit analysis, fee comparison, and surrender value modeling. Use when analyzing annuities, comparing guaranteed benefits, or evaluating annuity products.",
            ),
            (
                "managing-risk-transfer-analysis",
                "Structures risk transfer evaluation with economic efficiency, capacity optimization, and alternative risk transfer assessment. Use when evaluating risk transfer, optimizing risk financing, or assessing captive/ART structures.",
            ),
        ],
    },
    # ─── 12. DERIVATIVES / QUANTITATIVE FINANCE ─────────────────────
    "Quantitative Finance": {
        "description": "Derivatives pricing, quantitative modeling, and structured product workflows",
        "practice_areas": [
            "Derivatives",
            "Quantitative Analysis",
            "Structured Products",
        ],
        "skills": [
            (
                "pricing-equity-options",
                "Structures equity option pricing with Black-Scholes, binomial models, and implied volatility analysis. Use when pricing options, calculating Greeks, or analyzing implied volatility.",
            ),
            (
                "pricing-interest-rate-derivatives",
                "Structures interest rate swap, cap, floor, and swaption pricing with curve construction and valuation. Use when pricing IR derivatives, building yield curves, or valuing swap portfolios.",
            ),
            (
                "managing-derivatives-portfolio-risk",
                "Structures derivatives portfolio risk with Greek sensitivities, scenario analysis, and hedging strategies. Use when managing derivatives risk, analyzing Greek exposures, or designing hedge strategies.",
            ),
            (
                "analyzing-volatility-surfaces",
                "Constructs and interprets implied volatility surfaces with skew analysis and term structure assessment. Use when analyzing vol surfaces, interpreting skew, or modeling volatility dynamics.",
            ),
            (
                "managing-collateral-and-margining",
                "Structures CSA terms analysis with initial/variation margin calculation and collateral optimization. Use when managing collateral, calculating margin requirements, or optimizing posting strategies.",
            ),
            (
                "pricing-credit-derivatives",
                "Structures credit derivative pricing with hazard rate calibration and default probability estimation. Use when pricing CDS, calculating credit spreads, or modeling default risk.",
            ),
            (
                "analyzing-exotic-options",
                "Structures exotic option analysis with barrier, Asian, lookback, and digital option pricing methodologies. Use when pricing exotic options, modeling path-dependent payoffs, or analyzing exotic structures.",
            ),
            (
                "managing-xva-calculations",
                "Structures CVA, DVA, FVA, and KVA calculation with methodology selection and counterparty exposure modeling. Use when calculating XVA, pricing counterparty credit risk, or analyzing funding valuation adjustments.",
            ),
            (
                "building-quantitative-trading-models",
                "Structures systematic trading strategy development with signal generation, backtesting, and validation. Use when building quant models, backtesting strategies, or validating trading signals.",
            ),
            (
                "managing-structured-note-analysis",
                "Structures structured note evaluation with payoff analysis, embedded option decomposition, and fair value assessment. Use when analyzing structured notes, decomposing embedded options, or evaluating note pricing.",
            ),
            (
                "analyzing-commodity-derivatives",
                "Structures commodity derivative pricing with forward curve construction and convenience yield estimation. Use when pricing commodity derivatives, analyzing forward curves, or modeling commodity markets.",
            ),
            (
                "managing-hedge-accounting",
                "Structures hedge accounting documentation with effectiveness testing and ASC 815/IFRS 9 compliance. Use when documenting hedge relationships, testing effectiveness, or managing hedge accounting compliance.",
            ),
            (
                "analyzing-fx-derivatives",
                "Structures FX option and forward pricing with cross-currency basis analysis and volatility assessment. Use when pricing FX derivatives, analyzing currency options, or evaluating cross-currency basis.",
            ),
            (
                "managing-clearing-and-settlement",
                "Structures central clearing analysis with CCP margin methodology and default waterfall assessment. Use when managing clearing relationships, analyzing CCP margins, or evaluating default waterfalls.",
            ),
            (
                "building-monte-carlo-simulations",
                "Constructs Monte Carlo simulation frameworks with variance reduction and convergence analysis. Use when building MC simulations, implementing variance reduction, or assessing simulation accuracy.",
            ),
            (
                "analyzing-correlation-trading",
                "Structures correlation analysis with index vs. tranche pricing and correlation skew assessment. Use when analyzing correlation products, pricing tranches, or evaluating dispersion trades.",
            ),
            (
                "managing-algorithmic-trading-risk",
                "Structures algo trading risk management with execution quality, market impact, and circuit breaker monitoring. Use when managing algo risk, evaluating execution quality, or monitoring trading algorithms.",
            ),
            (
                "analyzing-variance-swaps",
                "Structures variance and volatility swap pricing with realized/implied vol analysis and hedging. Use when pricing variance swaps, analyzing vol risk premium, or hedging volatility exposure.",
            ),
            (
                "managing-dodd-frank-reporting",
                "Structures Dodd-Frank derivatives reporting with trade reporting, position limits, and SEF compliance. Use when managing DFA reporting, submitting trade reports, or ensuring SEF compliance.",
            ),
            (
                "analyzing-total-return-swaps",
                "Structures TRS analysis with funding benefit, counterparty exposure, and economic equivalence assessment. Use when analyzing TRS, evaluating synthetic exposure, or comparing TRS to cash positions.",
            ),
        ],
    },
    # ─── 13. FINTECH / PAYMENTS ──────────────────────────────────────
    "Financial Technology": {
        "description": "Digital finance, payments, and financial innovation workflows",
        "practice_areas": ["Fintech", "Payments", "Digital Banking"],
        "skills": [
            (
                "analyzing-payment-flows",
                "Structures payment system analysis with transaction flow mapping, interchange economics, and settlement timing. Use when analyzing payment systems, mapping transaction flows, or understanding interchange.",
            ),
            (
                "evaluating-fintech-business-models",
                "Structures fintech company analysis with unit economics, customer acquisition, and regulatory moat assessment. Use when evaluating fintech companies, analyzing unit economics, or assessing fintech business models.",
            ),
            (
                "managing-payment-compliance",
                "Structures payment regulatory compliance with PCI-DSS, money transmitter licensing, and BSA requirements. Use when managing payment compliance, assessing PCI requirements, or navigating MTL licensing.",
            ),
            (
                "analyzing-digital-lending-platforms",
                "Evaluates digital lending models with credit model assessment, funding structure, and regulatory analysis. Use when analyzing online lenders, evaluating credit models, or assessing lending platform risk.",
            ),
            (
                "managing-open-banking-integration",
                "Structures open banking API integration with data sharing, consent management, and security requirements. Use when implementing open banking, managing API integrations, or evaluating data sharing frameworks.",
            ),
            (
                "analyzing-blockchain-applications",
                "Evaluates blockchain use cases in financial services with DLT assessment and implementation feasibility. Use when analyzing blockchain applications, evaluating DLT solutions, or assessing crypto infrastructure.",
            ),
            (
                "managing-digital-wallet-operations",
                "Structures digital wallet analysis with stored value, regulatory classification, and risk assessment. Use when analyzing digital wallets, evaluating stored value products, or managing wallet compliance.",
            ),
            (
                "analyzing-embedded-finance",
                "Evaluates embedded finance opportunities with distribution economics and regulatory framework analysis. Use when analyzing embedded finance, evaluating BaaS models, or assessing embedded lending/insurance.",
            ),
            (
                "managing-regtech-evaluations",
                "Evaluates regulatory technology solutions with compliance efficiency and implementation cost-benefit analysis. Use when evaluating regtech, analyzing compliance automation, or assessing regulatory technology.",
            ),
            (
                "analyzing-neobank-models",
                "Structures neobank business analysis with customer economics, funding structure, and growth sustainability. Use when analyzing neobanks, evaluating digital bank models, or assessing challenger bank viability.",
            ),
            (
                "managing-api-banking-analysis",
                "Structures banking API evaluation with functionality assessment, security review, and integration planning. Use when evaluating banking APIs, planning API integration, or assessing API security.",
            ),
            (
                "analyzing-insurtech-models",
                "Evaluates insurtech business models with distribution innovation, underwriting technology, and claims automation. Use when analyzing insurtech, evaluating digital insurance, or assessing insurance technology.",
            ),
            (
                "managing-crypto-asset-analysis",
                "Structures cryptocurrency and digital asset analysis with protocol evaluation and market assessment. Use when analyzing crypto assets, evaluating blockchain protocols, or assessing digital asset markets.",
            ),
            (
                "analyzing-wealthtech-platforms",
                "Evaluates wealth management technology with robo-advisory models, digital planning, and fee analysis. Use when analyzing wealthtech, evaluating robo-advisors, or assessing digital wealth platforms.",
            ),
            (
                "managing-cross-border-payment-analysis",
                "Structures cross-border payment evaluation with corridor analysis, pricing, and regulatory requirements. Use when analyzing cross-border payments, evaluating remittance services, or assessing international payment solutions.",
            ),
            (
                "analyzing-buy-now-pay-later",
                "Evaluates BNPL business models with credit performance, merchant economics, and regulatory treatment. Use when analyzing BNPL, evaluating installment products, or assessing consumer lending innovation.",
            ),
            (
                "managing-stablecoin-analysis",
                "Structures stablecoin evaluation with reserve backing, redemption mechanics, and regulatory classification. Use when analyzing stablecoins, evaluating reserve adequacy, or assessing stablecoin risk.",
            ),
            (
                "analyzing-tokenization-applications",
                "Evaluates real-world asset tokenization with legal structure, market infrastructure, and liquidity analysis. Use when analyzing tokenization, evaluating security tokens, or assessing asset digitization.",
            ),
            (
                "managing-financial-data-aggregation",
                "Structures data aggregation analysis with connectivity, accuracy assessment, and consumer consent frameworks. Use when evaluating data aggregation, analyzing financial data APIs, or assessing account linking.",
            ),
            (
                "analyzing-ai-in-financial-services",
                "Evaluates AI/ML applications in financial services with model governance, bias assessment, and regulatory considerations. Use when analyzing AI in finance, evaluating ML models, or assessing AI governance.",
            ),
        ],
    },
    # ─── 14. TAX ─────────────────────────────────────────────────────
    "Tax": {
        "description": "Tax planning, compliance, and advisory workflows for financial transactions",
        "practice_areas": ["Tax Planning", "Tax Compliance", "International Tax"],
        "skills": [
            (
                "analyzing-corporate-tax-structures",
                "Structures corporate tax analysis with entity selection, state nexus, and effective tax rate optimization. Use when analyzing tax structures, selecting entity types, or optimizing corporate tax positions.",
            ),
            (
                "managing-transfer-pricing-compliance",
                "Structures transfer pricing documentation with comparable analysis, method selection, and intercompany agreement review. Use when managing transfer pricing, documenting arm's-length pricing, or preparing TP reports.",
            ),
            (
                "analyzing-international-tax-planning",
                "Evaluates international tax structures with BEPS considerations, treaty analysis, and repatriation planning. Use when planning international tax, analyzing tax treaties, or structuring cross-border operations.",
            ),
            (
                "managing-sales-tax-compliance",
                "Structures sales tax analysis with nexus determination, taxability classification, and exemption management. Use when managing sales tax, determining nexus, or analyzing taxability.",
            ),
            (
                "analyzing-m-and-a-tax-implications",
                "Evaluates tax implications of acquisition structures with 338(h)(10), 368 reorganization, and step-up analysis. Use when analyzing deal tax, structuring tax-efficient acquisitions, or evaluating tax-free reorganizations.",
            ),
            (
                "managing-tax-provision-preparation",
                "Structures income tax provision calculations with ASC 740 requirements and rate reconciliation. Use when preparing tax provisions, calculating deferred taxes, or analyzing ETR components.",
            ),
            (
                "analyzing-partnership-tax-structures",
                "Evaluates partnership tax arrangements with allocation waterfall, basis tracking, and carried interest treatment. Use when analyzing partnership tax, modeling distribution waterfalls, or tracking outside basis.",
            ),
            (
                "managing-tax-controversy",
                "Structures tax controversy management with audit defense, protest, and appeals documentation. Use when managing tax audits, preparing protest letters, or documenting audit defense positions.",
            ),
            (
                "analyzing-real-estate-tax-planning",
                "Evaluates real estate tax strategies including 1031 exchanges, opportunity zones, and cost segregation. Use when planning real estate tax, structuring 1031 exchanges, or analyzing cost segregation studies.",
            ),
            (
                "managing-estimated-tax-planning",
                "Structures quarterly estimated tax planning with safe harbor calculations and penalty avoidance strategies. Use when planning estimated taxes, calculating safe harbor payments, or avoiding underpayment penalties.",
            ),
            (
                "analyzing-state-income-tax",
                "Evaluates multi-state income tax positions with apportionment, nexus, and combined reporting analysis. Use when analyzing state tax, calculating apportionment, or managing multi-state filing.",
            ),
            (
                "managing-tax-credit-analysis",
                "Identifies and structures tax credit opportunities including R&D, energy, and employment credits. Use when analyzing tax credits, quantifying R&D credits, or evaluating credit eligibility.",
            ),
            (
                "analyzing-cryptocurrency-tax",
                "Structures cryptocurrency tax analysis with cost basis tracking, gain classification, and reporting requirements. Use when analyzing crypto tax, tracking digital asset basis, or classifying crypto transactions.",
            ),
            (
                "managing-estate-and-gift-tax",
                "Structures estate and gift tax planning with valuation, exemption utilization, and generation-skipping analysis. Use when planning estate tax, analyzing gift tax, or structuring generational transfers.",
            ),
            (
                "analyzing-compensation-tax",
                "Evaluates executive compensation tax with Section 409A, 280G golden parachute, and equity comp treatment. Use when analyzing compensation tax, evaluating 409A compliance, or structuring equity compensation.",
            ),
            (
                "managing-indirect-tax-analysis",
                "Structures value-added tax and customs duty analysis with cross-border transaction considerations. Use when managing VAT, analyzing customs duties, or evaluating indirect tax positions.",
            ),
            (
                "analyzing-tax-reform-impacts",
                "Evaluates legislative tax changes with modeling, transition planning, and compliance requirement analysis. Use when assessing tax reform, modeling legislative changes, or planning compliance transitions.",
            ),
            (
                "managing-tax-information-reporting",
                "Structures Form 1099, W-2, and other information reporting with classification and filing requirements. Use when managing tax reporting, classifying payments, or ensuring filing compliance.",
            ),
            (
                "analyzing-nonprofit-tax-compliance",
                "Evaluates tax-exempt organization compliance with Form 990, UBIT, and private foundation requirements. Use when managing nonprofit tax, reviewing Form 990, or analyzing UBIT exposure.",
            ),
            (
                "managing-international-withholding-tax",
                "Structures withholding tax analysis with treaty benefit claims and QI/QDD compliance. Use when managing withholding tax, claiming treaty benefits, or ensuring QI compliance.",
            ),
        ],
    },
    # ─── 15. WEALTH MANAGEMENT / PRIVATE BANKING ─────────────────────
    "Wealth Management": {
        "description": "High-net-worth advisory, financial planning, and family office workflows",
        "practice_areas": [
            "Wealth Management",
            "Private Banking",
            "Financial Planning",
        ],
        "skills": [
            (
                "creating-financial-plans",
                "Structures comprehensive financial plans with cash flow projection, goal analysis, and strategy integration. Use when building financial plans, projecting retirement needs, or creating comprehensive wealth strategies.",
            ),
            (
                "managing-estate-planning",
                "Structures estate plan analysis with trust review, tax efficiency, and legacy documentation. Use when analyzing estate plans, reviewing trust structures, or planning wealth transfer.",
            ),
            (
                "managing-retirement-planning",
                "Structures retirement income analysis with Social Security optimization, distribution sequencing, and longevity modeling. Use when planning retirement income, optimizing Social Security, or modeling retirement spending.",
            ),
            (
                "managing-insurance-planning",
                "Evaluates insurance needs with gap analysis, product comparison, and coverage adequacy assessment. Use when analyzing insurance needs, comparing insurance products, or identifying coverage gaps.",
            ),
            (
                "generating-client-reports-wealth",
                "Creates wealth management client reports with performance, net worth, and planning progress documentation. Use when preparing client reviews, creating wealth reports, or documenting planning progress.",
            ),
            (
                "managing-education-funding",
                "Structures education savings analysis with 529 plans, financial aid impact, and funding strategy comparison. Use when planning education funding, analyzing 529 options, or projecting college costs.",
            ),
            (
                "managing-charitable-giving-strategies",
                "Structures charitable planning with vehicle selection, tax benefit optimization, and legacy impact analysis. Use when planning charitable giving, evaluating donor-advised funds, or structuring foundation contributions.",
            ),
            (
                "managing-concentrated-stock-positions",
                "Evaluates strategies for concentrated equity positions with tax-efficient diversification and hedging analysis. Use when managing concentrated positions, planning diversification, or evaluating hedging strategies.",
            ),
            (
                "managing-trust-administration",
                "Structures trust administration with distribution analysis, tax reporting, and beneficiary communication. Use when managing trusts, analyzing distribution decisions, or documenting trust administration.",
            ),
            (
                "managing-family-governance",
                "Structures family governance frameworks with meeting protocols, decision-making, and succession planning. Use when establishing family governance, planning family meetings, or documenting succession.",
            ),
            (
                "managing-alternative-investments-wealth",
                "Evaluates alternative investment suitability for wealthy clients with liquidity analysis and portfolio fit assessment. Use when recommending alternatives, assessing suitability, or evaluating illiquid investments.",
            ),
            (
                "conducting-wealth-transfer-analysis",
                "Structures intergenerational wealth transfer with gifting strategies, trust design, and tax impact modeling. Use when planning wealth transfer, modeling gift strategies, or designing transfer structures.",
            ),
            (
                "managing-business-succession-planning",
                "Structures business exit and succession planning with valuation, buyer identification, and tax strategy. Use when planning business succession, valuing private businesses, or structuring ownership transitions.",
            ),
            (
                "managing-private-banking-reviews",
                "Structures private banking relationship reviews with service assessment, fee analysis, and strategy evaluation. Use when reviewing banking relationships, analyzing fees, or evaluating service quality.",
            ),
            (
                "managing-philanthropy-strategy",
                "Structures philanthropic strategy with impact measurement, vehicle selection, and giving policy documentation. Use when developing philanthropy strategy, measuring charitable impact, or creating giving policies.",
            ),
            (
                "managing-lifestyle-advisory",
                "Structures lifestyle advisory services with cash flow management, major purchase planning, and concierge coordination. Use when managing lifestyle expenses, planning major purchases, or coordinating advisory services.",
            ),
            (
                "managing-credit-and-lending-wealth",
                "Structures wealth-based lending analysis with securities-backed, real estate, and art lending evaluation. Use when evaluating wealth lending, analyzing pledge portfolios, or structuring high-net-worth credit.",
            ),
            (
                "managing-next-generation-planning",
                "Structures next-generation wealth education and involvement with financial literacy and responsibility programs. Use when preparing next generation, designing wealth education, or managing family learning programs.",
            ),
            (
                "managing-divorce-financial-planning",
                "Structures divorce financial analysis with asset division, support calculations, and post-divorce financial planning. Use when analyzing divorce finances, projecting settlement impacts, or planning post-divorce finances.",
            ),
            (
                "managing-expatriate-financial-planning",
                "Structures cross-border financial planning for expatriates with tax treaty, retirement, and estate considerations. Use when planning for expatriates, managing cross-border taxes, or coordinating international retirement planning.",
            ),
        ],
    },
    # ─── 16. FUND ADMINISTRATION / OPERATIONS ────────────────────────
    "Fund Operations": {
        "description": "Fund accounting, administration, and investment operations workflows",
        "practice_areas": [
            "Fund Administration",
            "Investment Operations",
            "Fund Accounting",
        ],
        "skills": [
            (
                "calculating-net-asset-value",
                "Structures NAV calculation with security pricing, accruals, expense allocation, and reconciliation. Use when calculating fund NAV, pricing portfolios, or reconciling NAV components.",
            ),
            (
                "managing-fund-accounting",
                "Structures fund accounting processes with trade recording, income allocation, and financial statement preparation. Use when managing fund books, recording investment transactions, or preparing fund financials.",
            ),
            (
                "managing-investor-reporting",
                "Structures investor communications with performance reporting, capital account statements, and distribution notices. Use when creating investor reports, preparing capital statements, or distributing fund communications.",
            ),
            (
                "managing-trade-operations",
                "Structures trade lifecycle management with confirmation, settlement, and exception processing. Use when managing trade operations, processing confirmations, or resolving settlement exceptions.",
            ),
            (
                "managing-corporate-actions",
                "Processes corporate action events with election management, entitlement calculation, and position adjustment. Use when managing corporate actions, processing dividends, or handling stock splits.",
            ),
            (
                "managing-fund-compliance-monitoring",
                "Structures investment compliance testing with guideline monitoring and breach reporting. Use when monitoring investment guidelines, testing compliance, or reporting breaches.",
            ),
            (
                "managing-performance-calculation",
                "Structures portfolio performance calculation with GIPS compliance, composite management, and attribution. Use when calculating returns, managing GIPS composites, or performing attribution analysis.",
            ),
            (
                "managing-investor-onboarding",
                "Structures investor onboarding with subscription documentation, AML/KYC, and suitability verification. Use when onboarding investors, processing subscriptions, or managing investor documentation.",
            ),
            (
                "managing-fund-distributions",
                "Structures fund distribution processes with allocation methodology, tax lot selection, and distribution notice preparation. Use when processing distributions, allocating fund income, or preparing distribution notices.",
            ),
            (
                "managing-proxy-voting",
                "Structures proxy voting processes with policy application, vote execution, and disclosure requirements. Use when managing proxy votes, applying voting policies, or documenting vote rationale.",
            ),
            (
                "managing-fund-expense-allocation",
                "Structures fund expense allocation with methodology documentation, compliance, and investor disclosure. Use when allocating fund expenses, documenting allocation methods, or managing expense ratios.",
            ),
            (
                "managing-redemption-processing",
                "Structures redemption processing with NAV calculation, gate provisions, and liquidity management. Use when processing redemptions, managing liquidity, or applying gate provisions.",
            ),
            (
                "managing-fund-audit-preparation",
                "Structures fund audit preparation with financial statement drafting, confirmation management, and workpaper organization. Use when preparing for fund audits, drafting fund financials, or managing audit confirmations.",
            ),
            (
                "managing-fund-tax-reporting",
                "Structures fund tax reporting with K-1 preparation, PFIC reporting, and investor tax package coordination. Use when preparing K-1s, managing fund tax reporting, or coordinating investor tax packages.",
            ),
            (
                "managing-middle-office-operations",
                "Structures middle office functions with trade matching, position reconciliation, and P&L verification. Use when managing middle office, reconciling positions, or verifying P&L calculations.",
            ),
            (
                "managing-securities-lending",
                "Structures securities lending operations with borrower management, collateral monitoring, and revenue optimization. Use when managing sec lending, monitoring loan collateral, or optimizing lending revenue.",
            ),
            (
                "managing-fund-formation-documents",
                "Reviews fund offering documents with LPA terms, side letter analysis, and compliance requirement extraction. Use when reviewing fund documents, analyzing LPA terms, or managing side letter provisions.",
            ),
            (
                "managing-alternative-fund-operations",
                "Structures operational processes for hedge fund, PE, and real estate fund specific workflows. Use when managing alternative fund ops, processing capital calls, or handling commitment tracking.",
            ),
            (
                "managing-transfer-agency",
                "Structures transfer agency operations with shareholder servicing, registration, and distribution management. Use when managing transfer agency, processing shareholder transactions, or maintaining shareholder records.",
            ),
            (
                "managing-fund-board-reporting",
                "Structures fund board reporting with compliance summaries, performance review, and governance documentation. Use when preparing board reports, summarizing fund compliance, or documenting governance items.",
            ),
        ],
    },
    # ─── 17. FINANCIAL PLANNING & ANALYSIS (FP&A) ────────────────────
    "Financial Planning and Analysis": {
        "description": "Corporate FP&A, budgeting, and management reporting workflows",
        "practice_areas": ["FP&A", "Management Accounting", "Business Intelligence"],
        "skills": [
            (
                "building-annual-operating-plans",
                "Structures annual operating plan development with revenue, expense, and capital budget integration. Use when building annual budgets, creating operating plans, or developing financial targets.",
            ),
            (
                "conducting-variance-analysis",
                "Structures budget vs. actual variance analysis with driver decomposition and management narrative. Use when analyzing variances, explaining budget deviations, or preparing variance reports.",
            ),
            (
                "building-rolling-forecasts",
                "Structures rolling forecast process with driver-based projections and continuous planning methodology. Use when creating rolling forecasts, updating financial projections, or managing continuous planning.",
            ),
            (
                "creating-management-dashboards",
                "Designs management reporting dashboards with KPI selection, visualization, and drill-down structure. Use when building financial dashboards, selecting KPIs, or designing management reports.",
            ),
            (
                "conducting-profitability-analysis",
                "Structures product, customer, and segment profitability analysis with cost allocation methodology. Use when analyzing profitability, allocating costs, or evaluating segment performance.",
            ),
            (
                "managing-headcount-planning",
                "Structures workforce planning with headcount budgeting, compensation modeling, and organizational analysis. Use when planning headcount, budgeting compensation, or modeling workforce scenarios.",
            ),
            (
                "conducting-scenario-planning",
                "Structures financial scenario analysis with assumption modeling, sensitivity testing, and decision frameworks. Use when modeling scenarios, testing assumptions, or evaluating strategic options.",
            ),
            (
                "managing-capital-allocation-fpna",
                "Structures capital allocation analysis with project prioritization, ROI evaluation, and portfolio optimization. Use when prioritizing investments, evaluating capital projects, or managing capital budgets.",
            ),
            (
                "building-driver-based-models",
                "Constructs driver-based financial models with operational metric linkage and sensitivity analysis. Use when building driver-based forecasts, linking operational and financial metrics, or modeling business drivers.",
            ),
            (
                "managing-board-financial-reporting",
                "Structures board-level financial packages with executive summary, strategic metrics, and forward outlook. Use when preparing board packages, creating executive financial summaries, or presenting financial results.",
            ),
            (
                "analyzing-revenue-trends",
                "Structures revenue analysis with growth decomposition, cohort analysis, and leading indicator tracking. Use when analyzing revenue, decomposing growth drivers, or tracking revenue leading indicators.",
            ),
            (
                "managing-cost-optimization",
                "Structures cost reduction analysis with opportunity identification, implementation tracking, and savings verification. Use when identifying cost savings, tracking reduction initiatives, or verifying cost optimization.",
            ),
            (
                "conducting-benchmarking-analysis",
                "Structures financial and operational benchmarking against industry peers with gap identification. Use when benchmarking performance, comparing to industry metrics, or identifying improvement opportunities.",
            ),
            (
                "managing-long-range-planning",
                "Structures long-range financial planning (3-5 year) with strategic initiative integration and investment phasing. Use when building long-range plans, modeling strategic scenarios, or projecting multi-year financials.",
            ),
            (
                "analyzing-unit-economics",
                "Structures unit economic analysis with CAC, LTV, payback period, and cohort-based measurement. Use when analyzing unit economics, calculating LTV/CAC, or evaluating customer economics.",
            ),
            (
                "managing-pricing-analysis",
                "Structures pricing analysis with margin impact, competitive positioning, and elasticity assessment. Use when analyzing pricing, evaluating margin impact, or assessing pricing strategies.",
            ),
            (
                "managing-business-case-development",
                "Structures business case documentation with financial impact, risk assessment, and decision criteria. Use when building business cases, justifying investments, or documenting project proposals.",
            ),
            (
                "managing-management-commentary",
                "Structures MD&A-style management commentary with narrative quality and metric alignment. Use when writing management commentary, preparing earnings narratives, or documenting financial performance.",
            ),
            (
                "managing-consolidation-reporting",
                "Structures multi-entity consolidation reporting with elimination entries and intercompany reconciliation. Use when consolidating financial results, managing eliminations, or preparing consolidated reports.",
            ),
            (
                "analyzing-operating-leverage",
                "Structures operating leverage analysis with fixed/variable cost decomposition and breakeven modeling. Use when analyzing operating leverage, modeling breakeven, or assessing cost structure.",
            ),
        ],
    },
    # ─── 18. TRADE FINANCE / COMMERCIAL BANKING ──────────────────────
    "Commercial Banking": {
        "description": "Commercial lending, trade finance, and banking operations workflows",
        "practice_areas": ["Commercial Banking", "Trade Finance", "Lending"],
        "skills": [
            (
                "managing-commercial-loan-underwriting",
                "Structures commercial loan underwriting with financial spreading, cash flow analysis, and risk rating. Use when underwriting commercial loans, analyzing borrower financials, or assigning risk ratings.",
            ),
            (
                "managing-credit-approval-packages",
                "Creates credit approval memoranda with borrower analysis, deal structure, and risk mitigation documentation. Use when preparing credit packages, documenting loan recommendations, or presenting to credit committee.",
            ),
            (
                "managing-loan-portfolio-monitoring",
                "Structures loan portfolio review with credit quality trends, watch list management, and concentration analysis. Use when monitoring loan portfolios, tracking credit quality, or managing watch lists.",
            ),
            (
                "managing-trade-finance-instruments",
                "Structures letter of credit, bankers acceptance, and documentary collection processing and analysis. Use when managing LCs, processing trade documents, or evaluating trade finance instruments.",
            ),
            (
                "managing-syndicated-loan-operations",
                "Structures syndicated loan participation with allocation, settlement, and agent bank coordination. Use when managing syndicated loans, processing loan allocations, or coordinating agent bank functions.",
            ),
            (
                "managing-loan-documentation-review",
                "Reviews loan agreements with covenant extraction, terms analysis, and compliance requirement identification. Use when reviewing loan documents, extracting covenants, or analyzing credit agreement terms.",
            ),
            (
                "managing-agricultural-lending",
                "Structures agricultural loan analysis with crop budget evaluation, collateral assessment, and seasonal patterns. Use when underwriting agricultural loans, evaluating farm financials, or analyzing crop budgets.",
            ),
            (
                "managing-sba-lending",
                "Structures SBA loan origination with eligibility verification, packaging requirements, and guarantee documentation. Use when processing SBA loans, verifying eligibility, or preparing SBA packages.",
            ),
            (
                "managing-commercial-real-estate-lending",
                "Structures CRE loan underwriting with property valuation, cash flow analysis, and environmental review. Use when underwriting CRE loans, analyzing property cash flows, or evaluating loan collateral.",
            ),
            (
                "managing-construction-loan-administration",
                "Structures construction loan management with draw processing, inspection tracking, and budget monitoring. Use when administering construction loans, processing draw requests, or monitoring construction budgets.",
            ),
            (
                "managing-equipment-financing",
                "Structures equipment finance analysis with asset valuation, residual estimation, and lease vs. buy comparison. Use when analyzing equipment financing, estimating residuals, or comparing financing alternatives.",
            ),
            (
                "managing-treasury-management-services",
                "Structures treasury management product analysis with cash management, payment solutions, and fee optimization. Use when evaluating treasury services, analyzing cash management needs, or optimizing banking relationships.",
            ),
            (
                "managing-deposit-operations",
                "Structures deposit product analysis with pricing, retention analytics, and regulatory compliance. Use when analyzing deposits, evaluating pricing strategies, or managing deposit compliance.",
            ),
            (
                "managing-correspondent-banking",
                "Structures correspondent banking analysis with relationship assessment, risk evaluation, and regulatory requirements. Use when managing correspondent relationships, evaluating partner banks, or assessing correspondent risk.",
            ),
            (
                "managing-bank-regulatory-reporting",
                "Structures regulatory report preparation including Call Reports, FR Y-9C, and other required filings. Use when preparing bank regulatory reports, filing Call Reports, or managing regulatory submissions.",
            ),
            (
                "managing-community-reinvestment",
                "Structures CRA compliance monitoring with lending, investment, and service test analysis. Use when managing CRA compliance, analyzing lending patterns, or documenting community investment.",
            ),
            (
                "managing-loan-loss-provisioning",
                "Structures CECL/ACL estimation with model methodology, qualitative factors, and forecast integration. Use when calculating loan loss provisions, implementing CECL, or estimating credit losses.",
            ),
            (
                "managing-interest-rate-risk-banking",
                "Structures bank interest rate risk analysis with EVE, NII sensitivity, and gap analysis. Use when managing bank IRR, modeling NII sensitivity, or analyzing repricing gaps.",
            ),
            (
                "managing-wire-transfer-operations",
                "Structures wire transfer processing with verification, OFAC screening, and exception handling. Use when processing wires, managing wire operations, or handling wire exceptions.",
            ),
            (
                "managing-fraud-operations-banking",
                "Structures banking fraud detection with transaction monitoring, investigation, and recovery documentation. Use when detecting banking fraud, investigating suspicious activity, or managing fraud cases.",
            ),
        ],
    },
    # ─── 19. ESG / SUSTAINABLE FINANCE ───────────────────────────────
    "Sustainable Finance": {
        "description": "ESG analysis, impact investing, and sustainable finance workflows",
        "practice_areas": ["ESG", "Impact Investing", "Sustainable Finance"],
        "skills": [
            (
                "scoring-esg-factors",
                "Structures ESG scoring methodology with environmental, social, and governance pillar assessment. Use when scoring ESG, evaluating sustainability, or building ESG frameworks.",
            ),
            (
                "analyzing-carbon-footprints",
                "Structures carbon footprint analysis with Scope 1/2/3 measurement and intensity benchmarking. Use when measuring carbon emissions, analyzing Scope 3, or benchmarking carbon intensity.",
            ),
            (
                "evaluating-green-bonds",
                "Structures green bond analysis with use-of-proceeds verification, impact reporting, and ICMA alignment. Use when evaluating green bonds, verifying green credentials, or analyzing sustainable debt.",
            ),
            (
                "managing-esg-reporting-standards",
                "Structures ESG disclosure with TCFD, SASB, GRI, and ISSB framework alignment and gap analysis. Use when preparing ESG disclosures, aligning to reporting frameworks, or analyzing ESG reporting gaps.",
            ),
            (
                "analyzing-social-impact",
                "Structures social impact measurement with theory of change, outcome metrics, and stakeholder analysis. Use when measuring social impact, designing impact metrics, or evaluating social outcomes.",
            ),
            (
                "managing-climate-scenario-analysis",
                "Structures TCFD-aligned climate scenario analysis with transition and physical risk modeling. Use when conducting climate scenarios, modeling transition risk, or analyzing physical climate exposure.",
            ),
            (
                "evaluating-sustainability-linked-loans",
                "Structures SLL analysis with KPI assessment, margin ratchet evaluation, and ambition verification. Use when evaluating sustainability-linked loans, assessing SLL KPIs, or analyzing margin ratchets.",
            ),
            (
                "managing-stewardship-and-engagement",
                "Structures shareholder engagement programs with escalation frameworks and outcome documentation. Use when managing stewardship, planning engagement, or documenting shareholder activism outcomes.",
            ),
            (
                "analyzing-biodiversity-risk",
                "Structures biodiversity risk assessment with nature-related dependency mapping and TNFD alignment. Use when analyzing biodiversity risk, mapping nature dependencies, or implementing TNFD disclosure.",
            ),
            (
                "managing-impact-fund-reporting",
                "Structures impact fund reporting with IRIS+ metrics, theory of change alignment, and additionality assessment. Use when reporting impact metrics, using IRIS+ indicators, or measuring fund impact.",
            ),
            (
                "analyzing-just-transition",
                "Evaluates just transition implications of decarbonization with workforce impact and community assessment. Use when analyzing just transition, assessing workforce impacts, or evaluating community effects.",
            ),
            (
                "managing-esg-data-quality",
                "Structures ESG data quality assessment with source comparison, estimation methodology, and disclosure gaps. Use when evaluating ESG data, comparing data providers, or assessing data quality.",
            ),
            (
                "analyzing-sustainable-supply-chains",
                "Structures supply chain sustainability assessment with Scope 3 attribution and risk identification. Use when analyzing supply chain ESG, mapping supplier risk, or assessing supply chain sustainability.",
            ),
            (
                "evaluating-social-bonds",
                "Structures social bond analysis with eligible population targeting, impact metrics, and SBP alignment. Use when evaluating social bonds, assessing social bond frameworks, or measuring social outcomes.",
            ),
            (
                "managing-proxy-voting-esg",
                "Structures ESG-informed proxy voting with resolution analysis, voting rationale, and disclosure. Use when making ESG proxy decisions, analyzing shareholder resolutions, or documenting vote rationale.",
            ),
            (
                "analyzing-stranded-asset-risk",
                "Evaluates stranded asset exposure for fossil fuel and carbon-intensive investments with transition modeling. Use when analyzing stranded assets, evaluating fossil fuel exposure, or modeling transition risk.",
            ),
            (
                "managing-dei-metrics",
                "Structures diversity, equity, and inclusion data collection with benchmarking and disclosure requirements. Use when analyzing DEI metrics, benchmarking diversity, or preparing DEI disclosures.",
            ),
            (
                "evaluating-transition-bonds",
                "Structures transition bond analysis with credibility assessment and transition plan evaluation. Use when evaluating transition bonds, assessing issuer transition plans, or analyzing climate transition financing.",
            ),
            (
                "managing-eu-taxonomy-compliance",
                "Structures EU Taxonomy alignment assessment with technical screening criteria and DNSH evaluation. Use when assessing Taxonomy alignment, applying technical criteria, or evaluating substantial contribution.",
            ),
            (
                "analyzing-water-risk",
                "Structures water risk assessment with water stress mapping, usage analysis, and regulatory exposure evaluation. Use when analyzing water risk, mapping water stress, or evaluating water-related financial exposure.",
            ),
        ],
    },
    # ─── 20. ECONOMIC ANALYSIS / MACRO ───────────────────────────────
    "Economic Analysis": {
        "description": "Macroeconomic analysis, monetary policy, and economic research workflows",
        "practice_areas": ["Economic Research", "Macroeconomics", "Policy Analysis"],
        "skills": [
            (
                "analyzing-economic-indicators",
                "Structures economic indicator analysis with leading, coincident, and lagging indicator interpretation. Use when analyzing economic data, interpreting economic releases, or tracking macro indicators.",
            ),
            (
                "analyzing-monetary-policy",
                "Structures central bank policy analysis with rate decision assessment, forward guidance interpretation, and market impact. Use when analyzing Fed policy, interpreting FOMC statements, or assessing monetary policy impact.",
            ),
            (
                "analyzing-fiscal-policy",
                "Evaluates government fiscal policy with budget impact, multiplier effects, and deficit/debt trajectory analysis. Use when analyzing fiscal policy, evaluating budget proposals, or assessing government spending impact.",
            ),
            (
                "forecasting-economic-growth",
                "Structures GDP growth forecasting with component analysis, nowcasting techniques, and revision tracking. Use when forecasting GDP, analyzing growth components, or building economic projections.",
            ),
            (
                "analyzing-inflation-dynamics",
                "Structures inflation analysis with component decomposition, expectations tracking, and Phillips curve assessment. Use when analyzing inflation, decomposing CPI/PCE, or tracking inflation expectations.",
            ),
            (
                "analyzing-labor-markets",
                "Structures employment data analysis with payroll, wage, and participation rate interpretation. Use when analyzing employment, interpreting jobs data, or assessing labor market conditions.",
            ),
            (
                "analyzing-housing-markets",
                "Structures housing market analysis with price trends, inventory dynamics, and affordability metrics. Use when analyzing housing data, tracking home prices, or assessing affordability.",
            ),
            (
                "analyzing-trade-and-currency",
                "Structures trade balance analysis with currency dynamics, competitiveness assessment, and tariff impact modeling. Use when analyzing trade data, evaluating currency trends, or assessing trade policy impact.",
            ),
            (
                "analyzing-emerging-markets",
                "Structures EM economic analysis with growth, inflation, external vulnerability, and political risk assessment. Use when analyzing emerging markets, assessing EM risk, or evaluating developing economy outlook.",
            ),
            (
                "conducting-country-risk-analysis",
                "Structures sovereign and country risk assessment with economic, political, and financial system evaluation. Use when assessing country risk, evaluating sovereign creditworthiness, or analyzing political risk.",
            ),
            (
                "analyzing-commodity-markets",
                "Structures commodity market analysis with supply/demand balances, inventory dynamics, and price driver attribution. Use when analyzing commodities, evaluating supply/demand, or forecasting commodity prices.",
            ),
            (
                "analyzing-financial-conditions",
                "Structures financial conditions index analysis with credit, equity, funding, and volatility component tracking. Use when analyzing financial conditions, tracking financial stress, or assessing market tightness.",
            ),
            (
                "analyzing-business-cycle-positioning",
                "Structures business cycle analysis with phase identification, leading indicator tracking, and sector implications. Use when identifying cycle phase, tracking business cycles, or assessing cyclical positioning.",
            ),
            (
                "analyzing-productivity-trends",
                "Structures productivity analysis with labor productivity, TFP estimation, and growth accounting decomposition. Use when analyzing productivity, estimating TFP, or decomposing growth drivers.",
            ),
            (
                "analyzing-global-capital-flows",
                "Structures capital flow analysis with BOP interpretation, hot money tracking, and flow dynamics assessment. Use when analyzing capital flows, interpreting BOP data, or tracking cross-border investment.",
            ),
            (
                "analyzing-banking-system-health",
                "Structures banking system assessment with capital adequacy, asset quality, and systemic risk evaluation. Use when analyzing banking systems, assessing financial stability, or evaluating systemic risk.",
            ),
            (
                "managing-economic-scenario-development",
                "Structures macroeconomic scenario design with consistent variable paths and probability assessment. Use when building economic scenarios, designing stress test scenarios, or creating macro forecasts.",
            ),
            (
                "analyzing-central-bank-balance-sheets",
                "Structures central bank balance sheet analysis with QE/QT impact assessment and reserve management. Use when analyzing central bank operations, evaluating QE effects, or tracking reserve management.",
            ),
            (
                "analyzing-demographic-trends",
                "Structures demographic analysis with population projections, dependency ratios, and economic impact assessment. Use when analyzing demographics, projecting population trends, or assessing demographic economic impact.",
            ),
            (
                "analyzing-geopolitical-risk",
                "Structures geopolitical risk assessment with scenario planning, market impact analysis, and portfolio implications. Use when analyzing geopolitical events, assessing political risk, or evaluating conflict scenarios.",
            ),
        ],
    },
}
