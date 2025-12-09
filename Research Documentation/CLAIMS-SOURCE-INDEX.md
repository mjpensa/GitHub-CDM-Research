# Claims Source Index for Attribution Matching

**Generated:** December 9, 2025
**Purpose:** Phase 1 index for matching unattributed claims to repo sources
**Target:** 170 claims (108 unattributed + 62 inferred)

---

## Part A: Source Document Inventory

### Priority 1 Sources (Highest Authority)

#### ISDA/Capgemini Industry Perspectives Report
**Path:** `Tier 1/.../isda/cdm-specific/Industry-Perspectives-on-the-ISDA-DRR-Unlocking-Efficiency-Accuracy-and-Strategic-Value.md`
**Date:** November 2025
**Key Data Points:**
- 4 firms in production (JPMorgan, BNP Paribas, JSCC, Banque Pictet)
- 15 firms running POCs (including DBS, DTCC, Goldman Sachs, Strate Ltd)
- 100% ACK rate under MAS rules
- 98.2% ACK rate for ESMA EMIR Refit
- Up to 50% cost reduction post-implementation
- 85% code reuse across jurisdictions (one firm)
- 92% code reuse for CSA implementation
- 12-21 month implementation timeline
- Under 3 months to add jurisdictions after initial build
- 3 integration strategies documented

**Supports Claims:** 4, 94, 134-139, 141

---

#### CDM Market Infrastructure Implementations
**Path:** `Tier 6/.../CDM-Market-Infrastructure-Implementations.md`
**Key Data Points:**
- Production implementations: JSCC, JPX, BNP Paribas, JPMorgan
- JPMorgan announcement: October 2024
- BNP Paribas go-live: November 2022
- Infrastructure partners: DTCC, SWIFT
- Regulatory jurisdictions with DRR support

**Supports Claims:** 4, 5, 138

---

#### FINOS CDM Participants List
**Path:** `Tier 1/.../finos-cdm/Participants.md`
**Key Data Points:**
- Enrolled participants with dates
- Organizations: ISDA, ICMA, ISLA, REGnosys, TradeHeader, Fragmos Chain, etc.
- Note: Does NOT list major banks as code maintainers

**Supports Claims:** 1, 5, 101

---

### Priority 2 Sources (Official Reports)

#### FINOS CDM Working Groups Documentation
**Path:** `Tier 1/.../finos-cdm/docs/CDM-*-WG.md`
**Covers:** Steering, Technology Architecture, Contribution Review, Derivatives, Collateral, Tokenized Assets

**Supports Claims:** 1, 5 (governance participation)

---

#### ISDA CDM Factsheet
**Path:** `Tier 1/.../isda/cdm-specific/ISDA-CDM-Factsheet.md`
**Key Topics:** CDM overview, benefits, use cases

---

#### Digital Regulatory Reporting Fact Sheet
**Path:** `Tier 1/.../isda/cdm-specific/Digital-Regulatory-Reporting-DRR-Fact-Sheet_042823.md`
**Key Topics:** DRR overview, regulatory coverage

---

#### CDM for Collateral Initiatives
**Path:** `Tier 1/.../isda/cdm-specific/CDM-for-Collateral-Initiatives-factsheet-2024.md`
**Key Topics:** Collateral management use cases

---

### Priority 3 Sources (Technical Documentation)

#### FINOS CDM Repository Documentation
**Path:** `Tier 1/.../finos-cdm/docs/`
- `cdm-overview.md` - Core CDM concepts
- `design-principles.md` - Architecture principles
- `event-model.md` - Business event model
- `product-model.md` - Product representation
- `process-model.md` - Lifecycle processes
- `use-cases.md` - Implementation use cases

---

#### FINOS CDM Roadmap
**Path:** `Tier 1/.../finos-cdm/ROADMAP.md`
**Key Topics:** 2025 roadmap, regulatory extensions

**Supports Claims:** 122 (jurisdictional expansion)

---

### Priority 4 Sources (Regulatory Context)

#### CFTC Documentation
**Path:** `Tier 4/.../cftc/`
- `cftc-swap-reporting-part43-2020.md`
- `cftc-swap-reporting-part45-2020.md`
- `cftc-technical-specification-v3.2-mar-2023.md`

**Supports Claims:** 126-133 (regulatory penalties context)

---

#### Other Regulatory Bodies
**Path:** `Tier 4/.../`
- ESMA EMIR documentation
- FCA UK EMIR documentation
- MAS Singapore guidelines
- ASIC Australia RG251
- JFSA Japan guidelines
- HKMA Hong Kong guidelines

**Supports Claims:** 93 (multi-jurisdiction reporting)

---

### Priority 5 Sources (Consulting/Industry Analysis)

#### Deloitte CDM Analysis
**Path:** `Tier 5/.../deloitte/2024-deloitte-cdm-drr-financial-services.md`

#### REGnosys Overview
**Path:** `Tier 5/.../specialists/regnosys/regnosys-regulatory-reporting-overview.md`

#### TradeHeader DRR FAQ
**Path:** `Tier 5/.../specialists/tradeheader/2024-tradeheader-drr-faq.md`

---

## Part B: Claims Categorization by Verification Type

### Group A: Quantitative Claims (Need Numerical Verification)

| Claim # | Claim Summary | Likely Source |
|---------|--------------|---------------|
| 38-53 | Bank revenue percentages (JPM, MS, Citi, BofA) | **EXTERNAL: 10-K filings required** |
| 60 | $500M-$1B transformation investment | **EXTERNAL: CFO statements required** |
| 94 | 85-92% code reuse | ISDA/Capgemini Report |
| 126-127 | CFTC $17.1B/$2.6B penalties FY2024 | **EXTERNAL: CFTC Press Release 9011-24** |
| 129-131 | BNY $5M, Barclays $4M, Goldman/BofA/JPM $50M fines | **EXTERNAL: Regnosys Industry News** |
| 134-137 | 98-100% ACK, 50% cost reduction, 85-92% reuse, <3 months | ISDA/Capgemini Report |
| 138 | 4 firms in production | ISDA/Capgemini Report |
| 139 | 15 firms running POCs | ISDA/Capgemini Report |

---

### Group B: Factual Claims (Need Source Confirmation)

| Claim # | Claim Summary | Likely Source |
|---------|--------------|---------------|
| 4 | JPMorgan go-live Oct 21, 2024 for ASIC/MAS | CDM Market Infrastructure + ISDA/Capgemini |
| 5 | BofA, Citi, Goldman, MS, Wells in governance | FINOS Working Groups / Participants |
| 65 | JPMorgan calls approach "semi-native" | **EXTERNAL: ISDA JPM Webinar** |
| 66 | Nick Mosher is JPMorgan's Product Director | **EXTERNAL: ISDA JPM Webinar** |
| 67-76 | JPMorgan webinar quotes (timestamps) | **EXTERNAL: ISDA JPM Webinar** |
| 79-80 | Goldman contributed Legend, piloted FX options | **EXTERNAL: Google Cloud/Goldman announcement** |
| 91 | Citigroup operates in 90+ countries | **EXTERNAL: Citi investor materials** |
| 101 | BofA participates in working groups, not maintainer | FINOS Participants list |
| 106 | Merrill, Countrywide, FleetBoston, MBNA acquisitions | **EXTERNAL: Industry reporting** |
| 108 | BofA spent 15 years integrating acquisitions | **EXTERNAL: Timeline verification** |
| 110 | Quartz is BofA's Python-based platform | **EXTERNAL: Technical documentation** |
| 116-117 | Quartz, SecDB, Athena = "billions" in investment | **EXTERNAL: Estimates required** |
| 122 | ISDA extending CDM to 12 regimes, 9 jurisdictions | ISDA DRR InfoHub / FINOS Roadmap |

---

### Group C: Analytical/Inference Claims (May Support with Evidence)

| Claim # | Claim Summary | Verification Approach |
|---------|--------------|----------------------|
| 8 | Four integration strategies emerged | ISDA/Capgemini (documents 3 strategies) |
| 11 | Archetype selection is capital allocation decision | Analytical inference - may remain INFERENCE |
| 36-37 | Revenue composition correlates with CDM investment | Analytical inference - may remain INFERENCE |
| 61-64 | JPMorgan integrated client model creates value | Analytical inference |
| 74-75 | FpML bypass reflects Athena investment | Analytical inference |
| 81-90 | Goldman/MS strategy interpretations | Analytical inference |
| 92-100 | Citigroup strategy interpretations | Analytical inference |
| 104-113 | BofA strategy interpretations | Analytical inference |
| 147-173 | Risk assessments, network effects, projections | Analytical inference |

---

### Group D: Technical/Architectural Claims

| Claim # | Claim Summary | Likely Source |
|---------|--------------|---------------|
| 13-35 | Archetype definitions and characteristics | ISDA/Capgemini (partial) + CDM docs |
| 119 | FpML adoption cycle proved translation works | **EXTERNAL: FpML history** |
| 141-146 | Translation tax, field mapping issues | Broadridge Analysis (if available) |

---

## Part C: Source-to-Claim Mapping

### ISDA/Capgemini Report Supports:

**Direct Evidence:**
- Claim 4: JPMorgan production (partial - date/jurisdictions)
- Claim 94: 85-92% code reuse
- Claim 134: 98-100% ACK rates
- Claim 135: Up to 50% cost reduction
- Claim 136: 85-92% code reuse across jurisdictions
- Claim 137: Under 3 months to add jurisdictions
- Claim 138: 4 firms in production
- Claim 139: 15 firms running POCs

**Partial Evidence (supports context):**
- Claims 13-35: Integration architectures (3 documented vs 4 claimed)
- Claim 8: Integration strategies (3 vs 4 archetypes)

---

### CDM Market Infrastructure Document Supports:

**Direct Evidence:**
- Claim 4: JPMorgan October 2024 announcement
- Claim 138: Production implementations list

---

### FINOS Documentation Supports:

**Direct Evidence:**
- Claim 1: Bank participation in governance (via working groups)
- Claim 5: Active governance participation
- Claim 101: BofA working group participation (if evidenced)
- Claim 122: Jurisdictional expansion roadmap

---

## Part D: Gap Analysis - External Sources Required

### High Priority Gaps (No Repo Source)

| Claim # | Data Needed | External Source Required |
|---------|------------|--------------------------|
| 38-53 | Bank revenue breakdowns | SEC 10-K filings |
| 60 | $500M-$1B estimate | Industry analyst reports |
| 65-76 | JPMorgan webinar quotes | ISDA November 2024 webinar recording |
| 79-80 | Goldman Legend/FX pilot | Google Cloud press release |
| 91 | Citi 90+ countries | Citi investor relations |
| 106, 108 | BofA M&A history/timeline | Financial news archives |
| 110 | Quartz technical details | BofA technology documentation |
| 116-117 | Platform investment estimates | Industry estimates |
| 126-127 | CFTC FY2024 penalties | CFTC Press Release 9011-24 |
| 129-131 | Specific fine amounts | Regnosys Industry News |
| 132 | Ian McGinley quote | CFTC official statement |

---

## Part E: Recommended Processing Order

### Session 2: High-Confidence Matches
Process claims with direct repo evidence:
- Claims 4, 94, 134-139 (ISDA/Capgemini)
- Claims 1, 5, 101, 122 (FINOS documentation)

### Session 3: Partial Evidence Claims
Process claims with supporting context:
- Claims 8, 13-35 (architecture documentation)
- Claims 93 (regulatory jurisdiction context)

### Session 4: Inference Validation
Review inference claims for upgrade potential:
- Claims 11, 36-37, 61-64 (analytical claims)

### Session 5-8: External Verification Needed
Document gaps requiring external sourcing:
- Bank revenue data (38-53)
- JPMorgan webinar content (65-76)
- Goldman/BofA specific claims
- Regulatory penalty data

---

## Part F: Search Keywords by Topic

### JPMorgan Implementation
- "JPMorgan", "JP Morgan", "JPM"
- "October 2024", "go-live", "production"
- "ASIC", "MAS", "semi-native"
- "Nick Mosher", "regulatory technology"

### Bank Governance
- "working group", "participant", "maintainer"
- "Bank of America", "BofA", "Goldman Sachs", "Citigroup", "Morgan Stanley"
- "governance", "contributor"

### Cost/ROI Metrics
- "cost reduction", "savings", "50%"
- "code reuse", "85%", "92%"
- "ACK rate", "acknowledgment", "98%", "100%"

### Regulatory
- "CFTC", "EMIR", "ASIC", "MAS", "JFSA"
- "jurisdiction", "regime", "reporting"
- "penalty", "fine", "enforcement"

### Technical Architecture
- "native", "integration", "translation"
- "FpML", "upstream", "downstream"
- "canonical", "data model"

---

*Index generated for Phase 2 automated source matching*
