# Official ISDA Documents Related to CDM on GitHub

This document catalogs all official ISDA (International Swaps and Derivatives Association) documents related to the CDM (Common Domain Model) available on GitHub.

---

# COMPREHENSIVE DOCUMENT COUNT SUMMARY

## Total Count: ~2,100+ Documents/Resources

| Category | Count |
|----------|-------|
| **FINOS CDM Repository Files** | ~1,200+ |
| **FINOS CDM Releases** | ~653 |
| **FINOS CDM GitHub Issues** | 694 |
| **FINOS CDM Discussions** | 50+ |
| **Other GitHub CDM Repositories** | 11 repositories (~70+ files) |
| **ISDA.org CDM Documents** | 35+ |
| **ISDA-tagged GitHub Repositories** | 9 |

---

# DETAILED BREAKDOWN

## 1. FINOS Common Domain Model Repository (Primary)

**Repository**: https://github.com/finos/common-domain-model

### File Count by Directory (~1,200+ files total)

| Directory | Files | Description |
|-----------|-------|-------------|
| `rosetta-source/src/main/rosetta/` | 141 | Rosetta DSL model definitions |
| `docs/` | 46 | Markdown documentation files |
| `examples/` | 5+ | Usage examples |
| `.github/` | 40+ | GitHub configuration, workflows |
| Root level | 15+ | README, LICENSE, GOVERNANCE, etc. |
| Java source files | 400+ | Generated Java code |
| JSON/XML/YAML configs | 90+ | Configuration and sample data |
| Other (tests, website, etc.) | 460+ | Additional resources |

### GitHub Releases: ~653 Total

| Version Track | Count | Date Range |
|---------------|-------|------------|
| v7.0.0-dev.x | 62+ | 2025 |
| v6.x.x | 12+ | 2024-2025 |
| v5.x.x | 30+ | 2024-2025 |
| v4.x.x | Various | 2023-2024 |
| v3.x.x | Various | 2022-2023 |
| v2.x.x (legacy) | 100+ | 2019-2022 |

*66 pages of releases, ~10 releases per page*

### GitHub Issues: 694 Total
- Working Group meeting notes
- Feature requests
- Bug reports
- Design discussions

### GitHub Discussions: 50+
- CDM Design Principles
- Working Group updates
- Community Q&A

### Key Root Documents (9)

| Document | Description |
|----------|-------------|
| [README.md](https://github.com/finos/common-domain-model/blob/master/README.md) | Main project overview |
| [CONTRIBUTING.md](https://github.com/finos/common-domain-model/blob/master/CONTRIBUTING.md) | Contribution guidelines |
| [GOVERNANCE.md](https://github.com/finos/common-domain-model/blob/master/GOVERNANCE.md) | Roles and decision-making |
| [LICENSE.md](https://github.com/finos/common-domain-model/blob/master/LICENSE.md) | Community Specification License 1.0 |
| [NOTICE.md](https://github.com/finos/common-domain-model/blob/master/NOTICE.md) | Copyright and ISDA licensing history |
| [Participants.md](https://github.com/finos/common-domain-model/blob/master/Participants.md) | Project participants |
| [ROADMAP.md](https://github.com/finos/common-domain-model/blob/master/ROADMAP.md) | ICMA, ISDA, ISLA roadmap |
| [RELEASE.md](https://github.com/finos/common-domain-model/blob/master/RELEASE.md) | Release management |
| [SCOPE.md](https://github.com/finos/common-domain-model/blob/master/SCOPE.md) | Project scope |

### Documentation Files (46 in /docs)

1. CDM-Collateral-WG.md
2. CDM-Contribution-Review-WG.md
3. CDM-Derivatives-WG.md
4. CDM-Physical-Risk-WG.md
5. CDM-Steering-WG.md
6. CDM-Technology-Architecture-WG.md
7. CDM-Tokenized-Assets-WG.md
8. cdm-demos.md
9. cdm-java-distribution.md
10. cdm-materials.md
11. cdm-org-structure.md
12. cdm-overview.md
13. change-control-guidelines.md
14. common-domain-model.md
15. design-principles.md
16. dev-guidelines.md
17. development-approach.md
18. documentation-style-guide.md
19. download.md
20. editing.md
21. eligible-collateral-representation.md
22. event-model.md
23. get-involved.md
24. governance.md
25. home.mdx
26. legal-agreements.md
27. links-template.md
28. maintainers.md
29. maintenance-and-release.md
30. major-release-scheduling-guidelines.md
31. mapping.md
32. namespace.md
33. pre-trade-processing.md
34. process-model.md
35. product-model.md
36. reference-data-model.md
37. repurchase-agreement-representation.md
38. roadmap.mdx
39. securities-lending.md
40. standardized-functions.md
41. team.mdx
42. training.md
43. use-cases.md
44. versioning.md
45. working-groups.md
46. code-snippets/ (directory)

---

## 2. Other CDM-Related GitHub Repositories

### 2.1 freight-trust/cdm (4 items)
**Repository**: https://github.com/freight-trust/cdm

| Item | Type |
|------|------|
| ISDA_CDMTM_License_Version_2.0 | License file |
| cdm/ | Directory |
| docs/ | Directory |
| finance/ | Directory |

**Key Document**: Official ISDA CDM License Version 2.0 (Feb 26, 2019)

---

### 2.2 manifoldfinance/isda (2 files)
**Repository**: https://github.com/manifoldfinance/isda

| File | Description |
|------|-------------|
| LICENSE.spdx | License file |
| README.mediawiki | ISDA definitions, functions, data types |

---

### 2.3 digital-asset-archive/lib-cdm-event-specification-module (9 items)
**Repository**: https://github.com/digital-asset/lib-cdm-event-specification-module

| Item | Type |
|------|------|
| .circleci/ | Directory |
| daml/ | Directory |
| docs/ | Directory |
| haskell/ | Directory |
| .gitignore | File |
| LICENSE | Apache-2.0 |
| NOTICES | File |
| Readme.md | Documentation |
| VERSION | File |

*Archived January 16, 2025*

---

### 2.4 digital-asset-archive/ex-cdm-swaps (18 items)
**Repository**: https://github.com/digital-asset-archive/ex-cdm-swaps

| Item | Type |
|------|------|
| .circleci/ | Directory |
| app/ | Directory |
| daml/ | Directory (contains Org/Isda/Cdm/Classes.daml) |
| docs/ | Directory |
| examples/ | Directory |
| .gitattributes | File |
| .gitignore | File |
| Dockerfile-bots | File |
| Dockerfile-daml | File |
| Dockerfile-repl | File |
| LICENSE | Apache-2.0 |
| Makefile | File |
| NOTICES | File |
| README.md | Documentation |
| daml.yaml | Configuration |
| docker-compose.yml | File |
| frontend-config.js | File |
| ui-backend.conf | File |

*Archived January 13, 2025*

---

### 2.5 rosetta-models/g20-tech-sprint (10 items)
**Repository**: https://github.com/rosetta-models/g20-tech-sprint

| Item | Type |
|------|------|
| api-demo/ | Directory |
| lib/ | Directory |
| rosetta-source/ | Directory |
| .gitignore | File |
| LICENSE | Apache-2.0 |
| README.md | Documentation |
| codefresh.yml | CI/CD config |
| config.json | Configuration |
| demo.sh | Demo script |
| pom.xml | Maven config |

*Archived March 5, 2024 - G20 Regulatory Reporting Demo*

---

### 2.6 REGnosys/rosetta-dsl (24+ items)
**Repository**: https://github.com/REGnosys/rosetta-dsl

The Rune DSL foundation for CDM.

| Directories (13) | Files (11) |
|------------------|------------|
| .github | .antlr-generator-3.2.0-patch.jar |
| .junie | .gitignore |
| docs | .project |
| rosetta-backport | CODE_OF_CONDUCT.md |
| rune-ide | CONTRIBUTING.md |
| rune-integration-tests | CVE-suppressions.xml |
| rune-lang | LICENSE |
| rune-maven-plugin | NOTICE |
| rune-profiling | README.md |
| rune-runtime | checkstyle.xml |
| rune-testing | pom.xml |
| rune-tools | |
| rune-xcore-plugin-dependencies | |

*1,148 commits, actively maintained*

---

### 2.7 mvanmeerbeck/ts-cdm (3+ files)
**Repository**: https://github.com/mvanmeerbeck/ts-cdm

TypeScript implementation of ISDA CDM.

| Item | Type |
|------|------|
| src/ | Directory |
| README.md | Documentation |
| package.json | Configuration |

---

### 2.8 Additional ISDA-Tagged Repositories (9 total)

**GitHub Topic**: https://github.com/topics/isda

| Repository | Language | Description |
|------------|----------|-------------|
| sambacha/compendium | Jupyter Notebook | Finance and crypto collection |
| Anexen/pyxirr | Rust | Financial functions |
| meenmo/ISDA_SIMM | Python | ISDA SIMM v2.3~2.6 |
| digital-asset-archive/lib-cdm-event-specification-module | Haskell | CDM event specification |
| kmedian/yearfrac | Python | Date fractions |
| suhasghorp/isda_model | Python | CDS modeling |
| freight-trust/cdm | TypeScript | ISDA CDM |
| sambacha/finanical-instrument-events | - | ISDA events |
| jimzucker/iCDS | C | CDS calculator |

---

## 3. ISDA.org Official Documents (35+ documents)

### CDM Hub Resources (16)
**URL**: https://www.isda.org/isda-solutions-infohub/cdm/

#### Educational Modules (7)
1. Module A: Introduction to the CDM
2. Module B: Accessing the CDM
3. Module C: How the CDM works
4. Module D: How the CDM is used
5. Module E: Collateral Use Cases
6. Module F: Advanced Features
7. Module G: Getting Started with CDM for DRR

#### Fact Sheets & Presentations (4)
1. Common Domain Model – An Overview (October 2023, PowerPoint)
2. CDM Collateral Initiatives Fact Sheet (April 2023)
3. ISDA Digital Regulatory Reporting (DRR) Fact Sheet (January 2023)
4. ISDA Digital Regulatory Reporting (DRR) License (September 2023)

#### Policy Documents (2)
1. ISDA Letter on Vision for UK as Global Finance Center (October 2023)
2. Mitigating Eligible Collateral Risks (September 2023)

#### Videos (3)
1. Automation and Standardization of Collateral Processes (May 2023)
2. Introduction to ISDA's Digital Regulatory Reporting Initiative (May 2022)
3. What is the ISDA CDM? (November 2017)

---

### PDF Documents (19+)

| Document | URL |
|----------|-----|
| CDM Launch Press Release | https://www.isda.org/a/IPKDE/CDM-Launch-Press-Release-FINAL.pdf |
| CDM for Collateral Initiatives Factsheet 2024 | https://www.isda.org/a/NAlgE/CDM-for-Collateral-Initiatives-factsheet-2024.pdf |
| ISDA CDM Factsheet | https://www.isda.org/a/z8AEE/ISDA-CDM-Factsheet.pdf |
| Smart Derivatives Contracts Whitepaper (Oct 2018) | https://www.isda.org/a/cHvEE/Smart-Derivatives-Contracts-From-Concept-to-Construction-Oct-2018.pdf |
| ISDA & KWM Smart Contracts Whitepaper | https://www.isda.org/a/yHvEE/ISDA-and-KWM-Publish-Smart-Contracts-Whitepaper-03102018.pdf |
| VERMEG CDM Integration Press Release | https://www.isda.org/a/5R1gE/Vermeg-Integrates-CDM-into-Colline-Collateral-Management-System.pdf |
| ISDA Clause Library Factsheet 2021 | https://www.isda.org/a/u6TgE/ISDA-Clause-Library-factsheet-2021.pdf |
| Industry Perspectives on ISDA DRR (Nov 2025) | https://www.isda.org/a/LhRgE/Industry-Perspectives-on-the-ISDA-DRR-Unlocking-Efficiency-Accuracy-and-Strategic-Value.pdf |
| Digital Asset & ISDA CDM Adoption | https://www.isda.org/a/HTSME/Digital-Asset-ISDA-CDM-Adoption-Press-Release.pdf |
| Demystifying Collateral Optimization (Nov 2021) | https://www.isda.org/a/G1UgE/Demystifying-Collateral-Optimization.pdf |
| ISDA Quarterly - January 2025 | https://www.isda.org/a/nNHgE/Marking-a-Milestone-IQ-January-2025.pdf |
| Milestone Update for CDM | https://www.isda.org/a/EGqgE/Milestone-Update-for-the-Common-Domain-Model.pdf |
| The Future of Derivatives (Sept 2016) | https://www.isda.org/a/B9EDE/infrastructure-white-paper.pdf |
| GenAI in Derivatives Market (April 2024) | https://www.isda.org/a/PbwgE/GenAI-in-the-Derivatives-Market-A-Future-Perspective.pdf |
| Legal Guidelines Smart Contracts CDS | https://www.isda.org/a/ur4TE/Guidelines-for-Smart-Contracts-CDS.pdf |
| Digital Regulatory Reporting (March 2022) | https://www.isda.org/a/33PgE/Digital-Regulatory-Reporting-Market-and-Regulatory-Initiatives.pdf |
| Collateral and Liquidity Efficiency (2025) | https://www.isda.org/a/TbfgE/Collateral-and-Liquidity-Efficiency-in-the-Derivatives-Market.pdf |
| Benchmarking GenAI for CSA Clause Extraction | (Available on isda.org) |
| CDM 5.0 Milestone Update (Dec 2023) | (Available on isda.org) |

---

## 4. Working Groups & Governance on GitHub

| Working Group | GitHub Link |
|---------------|-------------|
| CDM Derivatives Products and Business Events WG | https://github.com/finos/common-domain-model/issues/3122 |
| CDM Collateral Working Group | https://github.com/finos/common-domain-model/issues/3121 |
| CDM Tokenized Assets Working Group | https://github.com/finos/common-domain-model/discussions/4011 |
| CDM Design Principles Discussion | https://github.com/finos/common-domain-model/discussions/2422 |
| CDM Workshop 2025: Workflows and Business Events | https://github.com/finos/common-domain-model/discussions/3921 |

---

## 5. Licensing History

| Period | License | Location |
|--------|---------|----------|
| Pre-4.0.0 (before Feb 2023) | ISDA CDM License Version 2.0 | https://portal.cdm.rosetta-technology.io/#/ |
| 4.0.0+ (Feb 2023 onwards) | Community Specification License 1.0 | https://github.com/finos/common-domain-model |

---

## 6. Official External Resources

| Resource | URL |
|----------|-----|
| CDM Official Documentation | https://cdm.finos.org/ |
| ISDA CDM Page | https://www.isda.org/cdm/ |
| ISDA CDM Solutions Hub | https://www.isda.org/isda-solutions-infohub/cdm/ |
| CDM Downloads | https://cdm.finos.org/docs/download/ |
| Legacy CDM Portal (pre-4.0.0) | https://portal.cdm.rosetta-technology.io/#/ |
| GitHub Topics - CDM | https://github.com/topics/common-domain-model |
| GitHub Topics - ISDA | https://github.com/topics/isda |

---

## 7. Key GitHub Topics for Discovery

- https://github.com/topics/common-domain-model (1 repository)
- https://github.com/topics/isda (9 repositories)

---

# FINAL COMPREHENSIVE COUNT

## By Category

| Category | Count |
|----------|-------|
| FINOS CDM Repository - Total Files | ~1,200 |
| FINOS CDM Repository - Rosetta DSL Files | 141 |
| FINOS CDM Repository - Documentation Files | 46 |
| FINOS CDM Repository - Root Documents | 9 |
| FINOS CDM Repository - Releases | ~653 |
| FINOS CDM Repository - Issues | 694 |
| FINOS CDM Repository - Discussions | 50+ |
| Other GitHub Repositories | 11 |
| Other GitHub Repository Files | ~70 |
| ISDA.org Hub Resources | 16 |
| ISDA.org PDF Documents | 19+ |
| ISDA-tagged GitHub Repos | 9 |

## Grand Total

| Type | Total |
|------|-------|
| **GitHub Files (all repositories)** | ~1,270 |
| **GitHub Releases** | ~653 |
| **GitHub Issues** | 694 |
| **GitHub Discussions** | 50+ |
| **ISDA.org Documents** | 35+ |
| **Total GitHub Repositories** | 11 (CDM-specific) + 9 (ISDA-tagged) = 20 |

### **GRAND TOTAL: ~2,700+ documents/resources**

---

*Document generated: December 7, 2025*
*Source: GitHub repositories, GitHub API, and ISDA/FINOS official resources*
*Research methodology: Comprehensive web scraping, API queries, and manual verification*
