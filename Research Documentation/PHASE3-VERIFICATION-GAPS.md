# Phase 3 Final Verification Gaps and Additional Findings

**Generated:** December 9, 2025
**Phase:** 3 - Additional Evidence Search & Gap Analysis

---

## Executive Summary

Phase 3 searched for additional supporting evidence across the repository. Key findings:

| Category | Result |
|----------|--------|
| **Additional Sources Found** | 5 claims updated |
| **Jurisdiction Data Corrected** | Claim 122 - 8 regimes, not 12 |
| **Bank Governance Clarified** | ISDA DRR governance structure documented |
| **External Gaps Confirmed** | 28 claims still require external verification |

---

## Part A: Additional Evidence Found (Phase 3)

### 1. ISDA DRR Governance Structure

**Source:** `Tier 4/.../digital-regulatory-reporting-2023-update.md` (Lines 1441-1504)

This document clarifies how banks participate in CDM governance through ISDA DRR working groups:

| Working Group | Description | Membership |
|---------------|-------------|------------|
| DRR Steering Committee | Sets DRR roadmap | Firms providing resources or using DRR |
| DRR Technical Execution WG | Develops code | Technologists from participating firms |
| ISDA Data & Reporting EMEA WG | Regulatory interpretations | Any ISDA member |
| CFTC-EMIR DRR Peer Review Group | Reviews contributed code | Members interested in DRR |

**Impact on Claims 1, 5, 101:**
- Banks can participate in CDM governance through ISDA working groups (not just FINOS)
- "30 contributing firms" mentioned for DRR initiative
- Specific bank names still not listed in repo documents

**Recommendation:** Update claims to reference "ISDA DRR Working Groups" as governance mechanism, but specific bank names require external verification.

---

### 2. Jurisdiction Coverage Correction (Claim 122)

**Original Claim:** "ISDA is extending CDM to 12 regulatory regimes across 9 jurisdictions"

**Actual Evidence from ISDA/Capgemini Report (p.5):**

| Regulation | Jurisdiction | Status |
|------------|--------------|--------|
| CFTC | United States | ✓ Delivered |
| CFTC 3.2 | United States | ✓ Delivered |
| JFSA Phase 1 | Japan | ✓ Delivered |
| JFSA Phase 2 | Japan | ✓ Delivered (Apr 2025) |
| ESMA EMIR | EU | ✓ Delivered |
| FCA EMIR | UK | ✓ Delivered |
| ASIC | Australia | ✓ Delivered |
| MAS | Singapore | ✓ Delivered |
| CSA | Canada | ✓ Delivered (Jul 2025) |
| HKMA | Hong Kong | ✓ Delivered (Sep 2025) |

**Corrected Count:**
- **8 regulatory regimes** (not 12)
- **8 jurisdictions** (US, Japan, EU, UK, Australia, Singapore, Canada, Hong Kong)

**Recommendation:** Update Claim 122 to cite [ISDA/Capgemini Nov 2025, p.5] with corrected numbers.

---

### 3. FpML Coexistence Evidence

**Source:** `CDM-Overview-Nov-*.md` (Lines 53-60)

Key quotes supporting claim 119 context:
- "While both CDM & FpML are standards, they can and will co-exist"
- "CDM is not a data format for messaging or storage, it is a logical model"
- "CDM can be expressed in various forms including...FpML"
- "FpML does not define standards for event and workflow processing"

**Impact on Claims 73, 119, 121:**
- Confirms FpML and CDM coexistence is by design
- Supports author's analysis that "multiple approaches coexist"
- JPMorgan's FpML bypass (claim 73) is consistent with CDM design philosophy

**Recommendation:** Add supporting context citation [FINOS CDM Overview] to claim 121.

---

### 4. 30 Contributing Firms Evidence

**Source:** `Digital-Regulatory-Reporting-Market-and-Regulatory-Initiatives.md` (Line 79)

Quote: "ISDA and over 30 contributing firms are currently prioritizing digitization of the CFTC requirements"

**Impact:**
- Supports claim that "major banks participate" but doesn't name specific firms
- Confirms broad industry engagement beyond the 4 production + 15 POC firms

---

## Part B: Bank Governance Evidence Summary

### Evidence Found

| Bank | FINOS Evidence | ISDA DRR Evidence | Total Confidence |
|------|----------------|-------------------|------------------|
| **JPMorgan** | OrgRep Maintainer (Nicholas Moger) | Production firm | **HIGH** |
| **Goldman Sachs** | Legend Pilot contributor | POC firm | **MEDIUM** |
| **Bank of America** | None | "30 contributing firms" (unspecified) | **LOW** |
| **Citigroup** | None | "30 contributing firms" (unspecified) | **LOW** |
| **Morgan Stanley** | Panel moderator mention | "30 contributing firms" (unspecified) | **LOW** |
| **Wells Fargo** | None | None | **NONE** |

### Recommendation for Claims 1, 5

**Current Claim 1:** "Every major US bank participates in the governance of the ISDA Common Domain Model"

**Suggested Revision:**
- Change to: "Major US banks participate in CDM governance through ISDA DRR working groups and FINOS contributions"
- Add citation: [ISDA/Capgemini Nov 2025; FINOS CDM README]
- Note: Specific participation of BofA, Citi, MS, Wells Fargo not documented in repo

---

## Part C: Confirmed External Verification Required

### Tier 1: Critical Claims (Impact Paper's Core Arguments)

| Claim # | Claim | Required Source | Priority |
|---------|-------|-----------------|----------|
| 38-53 | Bank revenue percentages | SEC 10-K filings | HIGH |
| 60 | $500M-$1B transformation estimate | Industry analyst reports | HIGH |
| 65-76 | JPMorgan webinar quotes | ISDA November 2024 webinar | HIGH |
| 116-117 | Platform investments = billions | Industry estimates | MEDIUM |

### Tier 2: Supporting Claims (Enhance Credibility)

| Claim # | Claim | Required Source | Priority |
|---------|-------|-----------------|----------|
| 91 | Citigroup 90+ countries | Citi investor materials | MEDIUM |
| 106 | M&A technology stacks | Industry reporting | MEDIUM |
| 108 | BofA 15 years integration | Timeline verification | LOW |
| 110 | Quartz is Python-based | BofA technical docs | LOW |
| 119 | FpML adoption cycle decades | FpML history | LOW |

### Tier 3: Regulatory Claims (Already Cited but External)

| Claim # | Claim | Required Source | Notes |
|---------|-------|-----------------|-------|
| 126-127 | CFTC penalties FY2024 | CFTC Press Release 9011-24 | Citation exists, verify |
| 129-131 | Specific fine amounts | Regnosys Industry News | Citation exists, verify |
| 132 | Ian McGinley quote | CFTC official statement | Citation exists, verify |

---

## Part D: Claims Upgraded in Phase 3

| Claim # | Original | Updated | Evidence Added |
|---------|----------|---------|----------------|
| 93 | UNATTRIBUTED | [ISDA/Capgemini Nov 2025, p.5] | Table 1: Jurisdiction list |
| 121 | AUTHOR ANALYSIS | [FINOS CDM Overview] | FpML coexistence design |
| 122 | [ISDA DRR InfoHub] | [ISDA/Capgemini Nov 2025, p.5] | 8 regimes, not 12 - CORRECTED |

---

## Part E: Final Categorization (All 202 Claims)

| Category | Count | Percentage |
|----------|-------|------------|
| **REPO VERIFIED** (with page refs) | 25 | 12.4% |
| **INFERENCE** (analytical conclusions) | 62 | 30.7% |
| **AUTHOR ANALYSIS** (framework claims) | 42 | 20.8% |
| **EXTERNAL REQUIRED** | 28 | 13.9% |
| **PARTIAL - VERIFY** (some evidence) | 5 | 2.5% |
| **ALREADY CITED** (external sources) | 40 | 19.8% |
| **TOTAL** | **202** | **100%** |

---

## Part F: Recommendations

### Immediate Actions

1. **Update Claim 122** with corrected regime count (8 not 12)
2. **Add ISDA DRR governance context** to claims about bank participation
3. **Soften Claims 1, 5** to acknowledge some banks not specifically evidenced

### Documentation Actions

1. **Create external verification checklist** for SEC 10-K data extraction
2. **Document ISDA webinar sourcing** process if recording is available
3. **Note the "30 contributing firms"** as supporting context for broad participation

### Claims to Consider Removing or Revising

| Claim # | Issue | Recommendation |
|---------|-------|----------------|
| 1 | "Every major US bank" not evidenced | Revise to "Major US banks" |
| 5 | Specific banks not all evidenced | Add caveat or soften |
| 122 | Numbers incorrect | Correct to 8 regimes |

---

## Phase 3 Complete

The repository contains strong evidence for CDM/DRR metrics (ISDA/Capgemini report) and technical architecture, but bank-specific claims and financial data require external verification.

**Next Steps for User:**
1. Review claims_inventory_table_v2.md for all updated attributions
2. Prioritize external verification for Tier 1 critical claims
3. Consider revising claims 1, 5, 122 based on actual evidence

---

*Phase 3 Analysis Complete*
