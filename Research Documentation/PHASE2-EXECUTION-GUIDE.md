# Phase 2 Execution Guide: Automated Source Matching

**Generated:** December 9, 2025
**Prerequisite:** Phase 1 Index Complete
**Executor:** Opus 4.5 in Claude Code

---

## Execution Overview

### Constraints
- **Search Path:** `/home/user/GitHub-CDM-Research/Research Documentation/`
- **Tools Allowed:** Read, Grep, Glob only
- **NO web searches or WebFetch**
- **Report "NO REPO SOURCE" rather than inferring**

### Output Format
For each claim processed:
```
| Claim # | Original Status | New Status | Source File | Evidence Quote | Confidence |
```

Confidence Levels:
- **HIGH**: Exact match with direct quote
- **MEDIUM**: Supports claim with contextual evidence
- **LOW**: Partial support only
- **NONE**: No repo source found

---

## Session 2: High-Confidence Matches (Claims with Direct Repo Evidence)

### Batch 2A: ISDA/Capgemini Report Claims

**Source File:** `Tier 1/.../isda/cdm-specific/Industry-Perspectives-on-the-ISDA-DRR-Unlocking-Efficiency-Accuracy-and-Strategic-Value.md`

| Claim # | Claim Text | Search Term | Expected Match |
|---------|------------|-------------|----------------|
| 94 | CDM/DRR has 85–92% code reuse | "85%" OR "92%" OR "reuse" | Page 14: "85% reuse rate" / "92% of its existing ISDA DRR code" |
| 134 | 98–100% trade repository ACK rates | "100%" AND "ACK" | Page 3: "100% under MAS rules and 98.2% for ESMA" |
| 135 | Up to 50% reduction in maintenance costs | "50%" AND "cost" | Page 3: "reduced ongoing costs of up to 50%" |
| 136 | 85–92% code reuse across jurisdictions | "reuse" AND "jurisdiction" | Page 14: "85% reuse rate across jurisdictions" |
| 137 | Under 3 months to add jurisdictions | "three months" OR "3 months" | Page 10: "less than three months" |
| 138 | Four firms in production | "four firms" OR "JP Morgan, BNP" | Page 4: "Four firms are currently using" |
| 139 | 15 firms running POCs | "15 firms" OR "proof-of-concept" | Page 4: "15 firms are running proof-of-concept" |

**Execution Commands:**
```bash
# Search for ACK rate data
grep -n "100%\|98\|ACK" "/path/to/Industry-Perspectives*.md"

# Search for cost reduction
grep -n "50%\|cost\|savings" "/path/to/Industry-Perspectives*.md"

# Search for code reuse
grep -n "85%\|92%\|reuse" "/path/to/Industry-Perspectives*.md"

# Search for production firms
grep -n "four firms\|production\|JP Morgan\|BNP Paribas" "/path/to/Industry-Perspectives*.md"
```

---

### Batch 2B: CDM Market Infrastructure Claims

**Source File:** `Tier 6/.../CDM-Market-Infrastructure-Implementations.md`

| Claim # | Claim Text | Search Term | Expected Match |
|---------|------------|-------------|----------------|
| 4 | JPMorgan went live Oct 21, 2024 for ASIC/MAS | "JPMorgan" AND "October" | "Announcement: October 2024" |

**Execution Commands:**
```bash
grep -n "JPMorgan\|October 2024" "/path/to/CDM-Market-Infrastructure*.md"
```

---

### Batch 2C: FINOS Governance Claims

**Source Files:**
- `Tier 1/.../finos-cdm/Participants.md`
- `Tier 1/.../finos-cdm/docs/working-groups.md`
- `Tier 1/.../finos/WORKING-GROUP-ACCESS-MATRIX.md`

| Claim # | Claim Text | Search Term | Expected Match |
|---------|------------|-------------|----------------|
| 1 | Every major US bank participates in CDM governance | "Bank of America" OR "JPMorgan" OR "Goldman" | Check Participants list |
| 5 | BofA, Citi, Goldman, MS, Wells active in governance | "Bank of America" etc. | Check working group lists |
| 101 | BofA participates but isn't code maintainer | "Bank of America" NOT "maintainer" | Check Participants list |

**Execution Commands:**
```bash
grep -n -i "bank of america\|bofa\|jpmorgan\|goldman\|citigroup\|morgan stanley\|wells fargo" "/path/to/Participants.md"
grep -n -i "bank of america\|bofa\|jpmorgan\|goldman\|citigroup\|morgan stanley\|wells fargo" "/path/to/working-groups.md"
```

---

## Session 3: Partial Evidence Claims (Architecture & Regulatory)

### Batch 3A: Integration Architecture Claims

**Source File:** `Tier 1/.../isda/cdm-specific/Industry-Perspectives-on-the-ISDA-DRR-*.md`

| Claim # | Claim Text | Search Term | Notes |
|---------|------------|-------------|-------|
| 8 | Four distinct integration strategies emerged | "integration" AND "strategies" | Report documents 3, not 4 |
| 13-35 | Archetype characteristics | "native" OR "integration layer" | May provide partial support |

**Note:** The ISDA/Capgemini report documents 3 integration strategies:
1. Native CDM Integration via Upstream Data Models
2. Post-trade CDM Conversion
3. CDM Conversion at Reporting Layer

The paper's "four archetypes" may be author interpretation. Mark as INFERENCE if no direct 4-archetype source found.

---

### Batch 3B: Jurisdictional Expansion Claims

**Source Files:**
- `Tier 1/.../finos-cdm/ROADMAP.md`
- `Tier 1/.../isda/cdm-specific/Digital-Regulatory-Reporting-Market-*.md`

| Claim # | Claim Text | Search Term | Expected Match |
|---------|------------|-------------|----------------|
| 122 | ISDA extending CDM to 12 regimes, 9 jurisdictions | "jurisdiction" OR "regime" | Check roadmap |
| 93 | EMIR, CFTC, MAS, ASIC, JFSA impose requirements | "EMIR" OR "CFTC" OR "MAS" | Regulatory docs |

**Execution Commands:**
```bash
grep -n -i "jurisdiction\|regime\|regulatory" "/path/to/ROADMAP.md"
grep -n -i "CFTC\|EMIR\|MAS\|ASIC\|JFSA" "/path/to/Digital-Regulatory-Reporting-Market*.md"
```

---

## Session 4: Inference Validation

### Claims to Review for Upgrade Potential

These claims are marked [INFERENCE] but may have supporting evidence:

| Claim # | Claim Text | Validation Approach |
|---------|------------|---------------------|
| 11 | Archetype selection is capital allocation decision | Look for investment/cost discussion |
| 61-64 | JPMorgan integrated client model creates value | Look for JPMorgan strategy discussion |
| 74 | FpML bypass reflects Athena investment | Search for "FpML" context |
| 81-90 | Goldman/MS strategy interpretations | Search for Goldman Sachs, Legend |

**Search Commands:**
```bash
grep -n -i "capital\|investment\|cost" "/path/to/Research Documentation/" -r
grep -n -i "jpmorgan\|athena\|fpml" "/path/to/Research Documentation/" -r
grep -n -i "goldman\|legend\|secdb" "/path/to/Research Documentation/" -r
```

---

## Session 5-8: External Verification Needed

### Claims Requiring External Sources (Document Gaps)

**These claims cannot be sourced from the repo:**

| Claim # | Data Needed | External Source | Action |
|---------|------------|-----------------|--------|
| 38-53 | Bank revenue percentages | SEC 10-K filings | Mark "EXTERNAL VERIFICATION" |
| 60 | $500M-$1B transformation estimate | Industry analyst | Mark "EXTERNAL VERIFICATION" |
| 65-76 | JPMorgan webinar quotes | ISDA webinar recording | Mark "EXTERNAL: ISDA JPM Webinar" |
| 79-80 | Goldman Legend/FX pilot | Google Cloud press | Mark "EXTERNAL: Google Cloud/GS" |
| 91 | Citigroup 90+ countries | Citi investor materials | Mark "EXTERNAL VERIFICATION" |
| 106, 108 | BofA M&A history | Financial news | Mark "EXTERNAL VERIFICATION" |
| 110 | Quartz Python platform | BofA tech docs | Mark "EXTERNAL VERIFICATION" |
| 116-117 | Platform investment estimates | Industry estimates | Mark "EXTERNAL VERIFICATION" |
| 126-127 | CFTC FY2024 penalties | CFTC Press Release | Mark "EXTERNAL: CFTC 9011-24" |
| 129-131 | Specific fine amounts | Regnosys Industry News | Mark "EXTERNAL: Regnosys" |
| 132 | Ian McGinley quote | CFTC official statement | Mark "EXTERNAL: CFTC" |
| 141 | Translation tax analysis | Broadridge Analysis | Mark "EXTERNAL: Broadridge" |

---

## Session 9: Final Output Generation

### Deliverables to Generate

1. **claims_inventory_table_v2.md** - Updated with new attributions
2. **source_mapping_report.md** - Full evidence trail for sourced claims
3. **verification_gaps.md** - Claims requiring external sources
4. **inference_justification.md** - Rationale for retained INFERENCE claims

### Template for Updated Claims Table

```markdown
| # | Section | Claim | Source Status | Evidence |
|---|---------|-------|---------------|----------|
| 94 | Citigroup | CDM/DRR has 85–92% code reuse | [ISDA/Capgemini Nov 2025] | "85% reuse rate...92% of existing ISDA DRR code" |
| 134 | Economics | 98–100% ACK rates | [ISDA/Capgemini Nov 2025] | "100% under MAS...98.2% for ESMA EMIR Refit" |
```

---

## Quality Assurance Checklist

For each sourced claim:
- [ ] Source file exists in repo
- [ ] Quote accurately represents source content
- [ ] Citation format is consistent
- [ ] Confidence rating is justified
- [ ] No web searches were used

---

## Summary Statistics Target

| Category | Starting Count | Target After Phase 2 |
|----------|---------------|---------------------|
| UNATTRIBUTED | 108 | ~70-80 (external needed) |
| INFERENCE | 62 | ~50-55 (some upgraded) |
| Cited Source | 32 | ~75-82 (newly sourced) |

**Expected Outcome:**
- ~25-30 claims upgraded from UNATTRIBUTED to sourced
- ~7-12 claims upgraded from INFERENCE to sourced
- ~70-80 claims flagged as requiring external verification

---

*Execution guide for Phase 2 automated source matching*
