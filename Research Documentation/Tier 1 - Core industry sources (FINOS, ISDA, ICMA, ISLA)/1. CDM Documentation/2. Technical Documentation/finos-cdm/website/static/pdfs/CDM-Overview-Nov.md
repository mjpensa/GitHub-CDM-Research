# CDM Overview Nov

*Converted from: CDM-Overview-Nov.pdf*

---

## Page 1

Common Domain Model- An Overview
Sep 2024

## Page 2

Catalyst for Change- Current Market Structure Challenges
All parties store trade data in different formats & make lifecycle 
changes to these records inconsistently Differences in booking models lead to real 
world events in those models producing 
different outcomes:
• Reconciliation breaks
• Valuation differences
• Collateral disputes
• Reporting mismatches
• Operational inefficiency
• Settlement failures
• Barriers to automation
What is the true “truth” at any point in time?

## Page 3

What is the CDM?
The Common Domain Model (CDM) is a standardised, machine-readable and 
machine-executable blueprint for how financial products are traded and 
managed across the transaction lifecycle.
Dimensions of the CDM:
The CDM is NOT an application in and of itself, but can be implemented within one
Composability allows for re-use of components for efficiency
Product
Event
Legal Agreement
Process
Reference Data
Mapping
Definitions of tradeable products qualified by their economic terms
Data structures to represent the lifecycle events of financial transactions
Digital representation of the legal agreements that govern transactions
Translates the technical standards that support those industry processes into a standardised
machine-readable and machine-executable format
Reference data components that are specifically needed to model the other dimensions
Mapped to a set of alternative data representations including FIX, FpML, ISO20022

## Page 4

CDM vs. FpML
While both CDM & FpML are standards, they can and will co-exist
• CDM is not a data format for messaging or storage, it is a logical model describing relationships between 
pieces of data
• CDM can be expressed in various forms including XML, JSON and other standard formats such as FpML, 
FIX & ISO20022 for exchange and storage of information
• FpML does not define standards for event and workflow processing, CDM prescribes the validation logic 
to express these more specifically

## Page 5

Benefits- Consistency of representation

## Page 6

Core Benefits
q A mutualised free open-source standardised digital blueprint on how to represent financial transactions, performance and business events.
q Extensible to compose financial instruments by assembling reusable components. Already covers robustly derivative and securities financial
transactions.
q Scalable as event-driven model that encapsulates primitive components that will de facto make the fabric of complex business and operational 
processes.
q Operational and functional to codify the contract mechanics and business logic of legal agreements.
q Unambiguous in digitising functionally complex business and regulatory logic into code.
q Directly approachable as published in both human readable and machine executable languages.
q Implementable across several strategic uses cases in capital markets for better automation and greater consistency e.g. Trade management 
systems, clearing, digital documentation, collateral managements, regulatory reporting.
Enhance interoperability, reduce 
reconciliations and promote straight￾through processing
Efficiency
Promote transparency and alignment 
between regulators and market 
participants
Transparency
Create an environment for
innovation in financial markets
Accelerated Innovation

## Page 7

History of the CDM
Jun 2018
Version 1.0 released
Conceptual pilot
Mar 2019
CDM 2.0 released
Interest Rate and Credit 
Derivatives
Initial Margin CSA
Opened access to market
Nov 2021
MoU- ISDA, ICMA, ISLA
Enshrine Collaboration 
on CDM
2017
ISDA Publishes
CDM Design Paper
RFQ for Technology 
Partner
2020
Addition of all IM
& VM CSAs
FX and Equity derivatives
2017 2018 2019 2020 2021 2022 2023
Jun 2021
First non-derivatives 
product class contributed 
by ISLA:
Securities Lending MVP
Nov/Dec 2022
First production use:
DRR for CFTC reporting
CDM 3.0
Further product, event and 
workflow coverage
Feb 2023
CDM migrated to FINOS
Open-source community
Jul 2023
CDM 4.0
ICMA contributes Repos
2016
Sep 2016
ISDA publishes white 
paper on Future of 
Derivatives Processing
Q4 2023
CDM 5.0
ETD & Commodity
Derivatives
ISLA GMSLA Clause 
Library
Further Repo & Bond 
enhancements
Increasing momentum through industry contributions

## Page 8

Trade Association Collaboration
Associations are collaborating towards the same future goal, to benefit the whole industry
• An open-source model mutualises cost of development between TAs and contributing firms while retaining best practice governance
• MoU in 2021 enshrined collaboration publicly
• Working groups were opened to each others’ members
• TAs appointed FINOS to provide a repository with a view to fostering the growth of an open-source community for the CDM, with 
migration completed early 2023
Align Functional Roadmaps
• Best-practice led 
Governance
• Open-Source Community 
of Members
Joint steering forum
Combined governance policy
Open-Source Repository

## Page 9

Product Coverage
The use of common elements allow for representation of multiple types of products and events in the trade workflow with minimal incremental work. Thus, this coverage list does 
not represent an exhaustive list of all possible combinations of elements or events
The scope of contractual products in the current model are summarized below:
• Interest rate derivatives:
• Interest Rate Swaps (incl. cross-currency swaps, non-deliverable swaps, basis swaps, swaps with non-regular periods, ...)
• Swaptions
• Caps/floors
• FRAs
• OTC Options on Bonds
• Credit derivatives:
• Credit Default Swaps (incl. baskets, tranche, swaps with mortgage and loans underliers, ...)
• Options on Credit Default Swaps
• Equity derivatives:
• Equity Swaps (TRS, PRS, single name/index/basket, VarSwap, VolSwap, Dispersion, Correlation, Dividend Swap)
• Options & Forwards
• Foreign Exchange derivatives:
• FX Swap, Forward, NDF, Options
• Commodity derivatives:
• Swaps, options, swaptions
• Exchange Traded derivatives

## Page 10

Product & Event Coverage
The use of common elements allow for representation of multiple types of products and events in the trade workflow with minimal incremental work. Thus, this coverage list does 
not represent an exhaustive list of all possible combinations of elements or events
The scope of contractual products and events in the current model are summarized below:
• Securities Lending:
• Single underlier, cash collateralised, open/term security loan
• Repurchase Agreements:
• Open Term, Fixed Term, Fixed Rate, Floating Rate
• Events:
• Allocation, Re-allocation
• Cash, Security transfers, DVP settlement
• Clearing events
• Compression
• Increase and decreases/returns
• Novations- full, partial
• Terminations- full, partial
• Renegotiation
• Reset
• Execution
• Stock Split
• Index Transition
• Determination of corporate action and credit events

## Page 11

Legal Document Coverage
ISDA Documentation ISDA Documentation
ISLA have also contributed their Clause Library and 
Taxonomy for the GMSLA 2000/2010
CDM ISDACreate
ISDACreate/ 
CDM 
Compatible 
INITIAL MARGIN 
2016 ISDA IM CSD (English Law) x
2016 ISDA IM CSA (NY Law)
2016 ISDA IM CSA (Japanese Law) x
2018 ISDA IM CSA (NY Law)
2018 ISDA IM CSD (Eng Law)
2019 ISDA Bank Custodian CTA
2019 ISDA Bank Custodian SA (NY Law)
2019 ISDA Bank Custodian SA (Eng Law)
2019 ISDA Bank Custodian SA Luxembourg Law x
2020 ISDA Bank Custodian SA Belgium Law x
2016 Euroclear SA (Bel Law) x
2017 Euroclear CTA (NY Law) x
2017 Euroclear CTA (Eng Law) x
2018 Euroclear CTA (Eng Law) x
2018 Euroclear CTA (NY Law) x
2018 Euroclear SA (Bel Law) x
2019 Euroclear CTA
2019 Euroclear SA (Bel Law) x
2016 Clearstream CTA (Eng Law) x
2016 Clearstream CTA (NY Law) x
2017 Clearstream SA (Lux Law) x
2016 Clearstream SA (Lux Law) x
2019 Clearstream CTA
2019 Clearstream SA (Security-provider) (Lux Law)
2019 Clearstream SA (Security-taker) (Lux Law)
CDM ISDACreate
ISDACreate/ 
CDM 
Compatible 
VARIATION MARGIN 
2016 ISDA CSA (VM) (Loan - Japanese Law) x x
2016 ISDA CSA (VM) (Security Interest - New York Law) x
2016 ISDA CSA (VM) (Title Transfer - English Law) x
2016 ISDA CSA (VM) (Title Transfer - French law) x x
2016 ISDA CSA (VM) (Title Transfer - Irish law) x x
1994 ISDA Credit Support Annex VM (Security Interest - New York Law) In Development x
1995 ISDA Credit Support Annex VM (Title Transfer - English Law) In Development x
1995 ISDA Credit Support Annex (Security Interest - Japanese Law) x x x
1995 ISDA Credit Support Deed (Security Interest - English Law) In Development x
ISDA MASTER AGREEMENT 
1992 ISDA Master Agreement See below x
2002 ISDA Master Agreement See below CP details only 
Automatic Early Termination ("AET") x
Address for Notices x
Dated as of Date x
Credit Support Provider x
Credit Support Document x
Governing Law x
Specified Entity x
Termination Currency x

## Page 12

Roadmap 2024
Title/Topic Chair Q1 Q2 Q3 Q4
Steering WG David Shone, ISDA - Complete governance updates - Annual Review of governance- end June
- Establish release schedule and process
Technical Architecture WG Chris Rayner, ISLA - Release build process moves to Github 
Actions
- Release build process moves to Github 
Actions
-- Redesign Testing Process
- Vision Statement
- Prioritise initiatives
'- Serialisation Phase 1 begins
- Ref data list management phase 
1/2- TBC
- Serialisation Phase 1 complete
- Ref data list management 
phase 3 TBC
Contribution Review WG Rotating- trade associations - Establish Release management 
process/bed in resources: Release Manager 
& Engineer
- Release approval & review
- Release approval & review - Release approval & review - Release approval & review
-->Cross-product Modelling N/A - Product model changes:
-- Asset & Observable refactoring [supports 
structured products and strategic fix for sec 
finance qualifications]
-- Define product with contractdetails
-- Redesign Product Qualification to separate 
economic qualification from product 
qualification
- Product model changes:
-- Asset & Observable refactoring [supports 
structured products and strategic fix for sec 
finance qualifications]
'- Product model changes:
-- Harmonise date/timestamp
Collateral WG Vernon Alden-Smith, ISDA - Extend ECS model
- Repo collateral extension
Securities Lending WG Chris Rayner, ISLA
Derivatives Product and Business Event 
WG
David Shone, ISDA - Migrate to FINOS governance umbrella
- Option payout refactoring (ETD/OTC)
- Product enhancements driven by DRR
- Member modelling proposals: Equity Swaps
- Member modelling proposals - Member modelling proposals - Member modelling proposals
Structured Products WG Jean-Baptiste Ziade, Fragmos 
Chain
ICMA Repo/Bonds WG Gabriel Callsen, ICMA
Securities Finance Reg Reporting? TBC
ISDA Legal Agreement WG Vernon Alden-Smith, ISDA
Ciaran McGonagle, ISDA
- Analyse and develop framework for 
remaining 20 clauses of legacy CSA 
agreements
- Model 10 clauses of legacy CSAs analysed 
in 2023
Analyse and develop framework for remaining 
20 clauses of legacy CSA agreements
Complete legacy CSAs in CDM and 
create test data
Complete legacy CSAs in CDM 
and create test data
ISDA DRR Eleanor Hsu, ISDA
Tabish Ahmed, ISDA
- DRR 4.0 Release: Complete coverage EMIR 
and JFSA
- FCA dev complete target 30th March
- EMIR /JFSA Compliance Dates [1st/29th 
April]
- ASIC & MAS dev complete target
- FCA compliance date- 30th Sept - ASIC/MAS Compliance date￾21st October
Working Groups
Ongoing adoption support & WG prioritised items
Ongoing adoption support & WG prioritised items
Ongoing structured product enhancements & WG prioritised items
Ongoing adoption support and WG prioritised items

## Page 13

Roadmap 2024
Title/Topic Chair Q1 Q2 Q3 Q4
- Onboard shared documentation resource
-Model Documentation: Securities Lending 
Use Cases
- Model documentation: Pre-trade securities 
lending user guide
- Model documentation: GMSLA 
user guide
- All agreed governance updated on FINOS 
website
- Addition of recorded demos - Consistency and accuracy 
exercise- website/github
- Consistently branded overviews - Collateral getting started guide 
- Training course development
- Tiered overviews
- Business case templates
- Reference implementations
-Expand getting started guides to 
other use cases
- Develop certification/award 
system?
- CDM Showcase London Feb 28
- Informa Trade & Transaction reporting Conf￾5th March
- London OSFF - June 26
- ISDA AGM Tokyo 16-18th April
- ISLA Annual Conf Geneva 18-20 June
- New York OSFF - Sept 30, Oct 1 - ISLA Post-Trade- Oct TBC
Events
Adoption Support Framework
Documentation
Website
Support material

## Page 14

ISDA Extensions to CDM
base - common elements: date & time, static data etc.
observable - asset & event (e.g. credit event) – basic building blocks to construct products
product – the product model
Legal Agreement/documentation – including market 
master agreements, definitions, contract, etc.
event – including workflow & position
Reporting – including models for derivatives reg reporting
ISDA Licences
CDM under open 
source license at 
FINOS
ISDA has created 
two extensions to 
the core CDM: DRR 
and ISDA 
Foundations
ISDA Foundations Digital Regulatory Reporting

## Page 15

Use Cases

## Page 16

Collateral - Today’s Challenge
Broker/ 
Dealers
Buy Side
Vendors
§ Lack of industry standards - Every 
industry participant left to 
implement their own version
§ Loss of inter-operability between 
solutions
§ Pervasive reconciliation issues 
and other operational 
inefficiencies
Guidelines outlined under BCBS/IOSCO and Basel III were translated by each regulatory regime spearheading collateral management as a
key function in capital markets for both bilateral and cleared OTC. Compliance has increased processing volumes significantly and will continue
to do so, the need for automation in collateral management processing. The industry is faced with many challenges which has led to
fragmented implementations and operational inefficiencies.
INDUSTRY PARTICIPANTS
CalculationDependencies 
Margin Monitoring 
Margin Allocation 
Documentation
Collateral Segregation 
Establishing CustodyAccounts 
Eligibility Schedules
Risk Control 
Optimisation 
Regulatory Compliance 
Reconciliation
DisputeManagement 
Efficient Settlement
Custodians

## Page 17

Collateral- Documentation Model Representation 2020/2021

## Page 18

Collateral- Benefits of CDM Standard Documentation

## Page 19

Collateral- ECS Challenges – No Standard Data Format

## Page 20

Collateral- Eligible Collateral Schedules
CDM Digital structure KEY datapoints:
Eligible 
Collateral
IssuerCriteria AssetType Concentration 
Limits/Wrong 
Way Risk
Maturity 
Type/Range
Asset/Product 
Identifier
Valuation 
Percentage 
Haircut
AgencyRating
• Country ofOrigin
• Sovereign/CentralBank
• Quasi Government
• Corporate
• Regional Government
• Funds
• Special PurposeVehicles
• Denominated Currency
• Security
• Cash
• Commodity
• Other
• Source ID-
(ISIN/ CUSIP)
• Taxonomy
(ICAD /ISO-CFI)
Options to apply 
Concentration Limitsby
• Issuer
• Product
• Country ofOrigin
• Currency
• AgencyRatings
By Percentage orValue
• Original Maturity
• RemainingMaturity
• From Issuance
• Period Range 
(Lower & Upper)
Rating is flexible 
to be providedfor
• Asset/ Product
• ISSUER
• SOVEREIGN
• Reference Agency
• MultipleAgency
• Rating
•MismatchSpecify 
(Lowest/Highest/ 
Agency override)
• RegulatoryHaircut
• FX Haircut
• Margin Percentage
• Additional H/C
• Debt
• Equity
• Fund
• Warrant
• Certificate
• Letter of Credit
• Other

## Page 21

Collateral- Structure to define Asset Types and Identify Issuers
ISDA CDM will offer the flexibility to identify collateral asset types, with particular focus on securities, as most 
common form found in collateralschedules. However,this can be extended to cover many otherassets.
AssetType
Cash Security Commodity
Debt 
Security
Fund 
Unit
Equity and Equity-linked 
Security
Other
Other
Regional Governments, Local 
Authorities, Municipals
With recourseto 
Sovereign
Without 
recourseto
Sovereign
Either
List ofEligible 
Sovereigns
List ofEligible 
Issuers
Other issuer typesinclude:
• Sovereign Central Banks
• Corporate
• Supranational Debt
• SPV and Funds
With the functional flexibility to 
capture detail of its identity 
including specific issuer name and 
use of common identifiers

## Page 22

Collateral- CDM Eligibility Schedules Representation
CDM offers standard data references points required for many industry forms of ECS. The structure enables consistent
expression of data with the ability to apply various include/exclude rules and complex concentration limits. ISDA has
demonstrated translation of several ECS provided by members into digital output

## Page 23

Collateral- Eligible Collateral Schedules
An Eligible Collateral Schedule is represented in the CDM through the specification of criteria that can be used to 
“filter” whether a piece of collateral is eligible or not.
Asset Type – is used to specify criteria related to the nature of the asset, such as its type (cash, equity, debt, etc), 
country of origin or denominated currency
Issuer Type – is used to specify criteria related to the issuer of the asset, such the type of issuer (government, 
corporate, etc), specific issuer name, or agency rating
Treatment – is used to specify the valuation percentage, any concentration limits and whether the criteria specify 
inclusion or exclusion conditions
The combination of these terms allows a wide variety of eligible collateral types to be represented and can be 
applied across industry use cases for OTC, Securities Lending, Repo, Cleared and ETD. s
Solving problems for Global Banks, Custodians, Data Providers, Vendors and connecting solutions. 
Standard data for Eligible Collateral information facilitates DLT, Smart Contract and technology to be built to add 
further efficiencies to processes

## Page 24

Collateral- CDM Object Builder
Vendors
Counterparties
DataProviders
Administrators
Negotiation 
Platforms
Custodians
REGnosys on behalf of ISDA have developed a user interface (UI) this allows you to create CDM Eligible Collateral schedule information using 
drop down functions. The user can create, import, share or inspect in CDM JSON and view in a tabular format. The Object Builder will be 
contributed to FINOS in 2023
The UI can be used for predefined common eligibility profiles to import and edit and producing industry compatible consumable data output. 
The current UI gives the user the ability to also validate and construct many version of eligible collateral as CDM data and has the scope to be 
development further and built into services for use cases beyond collateral

## Page 25

2021/22 – TechnicalIntegration work 
with ISDA Create completed, and CDM
standard format IM documentation
available via CreateAPI
2021/22 – Workshops to assess 
compatibility, first-stage mapping 
and analysis for IM CSA
H2 2023 – Development in COBRA for
CDM IM CSA ingestion to COLLINE 
Q1 2024 – CDM connector (IM CSA) 
released to production in COLLINE 
ready for client use
Q2 2024 - Ongoing discussions with 
clients to deploy connector into 
production.
For Calypso Solution: 
2022 – Mapping to CDM IM CSA 
representationcompleted 
and validated using test data
2023 – Testing import/export using 
data uploader tool; version 1 
competed 
2024 – Extend document coverage to 
Legacy VM
2023 - Representation mapping 
and analysis for supporting 
selected CSA types feed in CDM 
format completed. Focus shifted 
to ECS for H1 2024 
H2 2024 – Continue analysis and 
mapping to prepare for ingestion 
status. Potential to connect to
service providers able to support 
CDM
Focus – CDM for representing IM, VM, 
Legacy CSA and Master Agreement data
2022/23 – Investigation into ability to 
round trip CDM data between Lyncs and
ISDA Create for IM CSA
2024 – Ensure compatibility of CDM with 
internal model for Legacy VM CSA inc
complex clauses. Production status/ 
timeline dependent on clients interested in 
using CDM
2023 – Mapping for CDM IM CSA 
coverage completed to deliver 
integration into Murex (CDM vs MX.3) 
First version of CDM agreement import 
available (without eligibility schedule 
and legacy fields) 
2024 – Extend upon IM CSA CDM 
availability with mapping for Legacy 
CSAs once delivered to CDM
For more questions on CDM and Collateral related initiatives, please reach out to: valdensmith@isda.org.
2019- 2023 – Continued support and input on 
CDM Collateral related representations 
Focus – VM & IM CSA, CSD and IM CTA, ISDA 
Master. Support CDM build for Legacy VM 
CSA 
Q3 2024 – Analysis phase 
Copyright © 2024 by International Swaps and Derivatives Association,Inc.
12
Commitment to CDM Integration: Digital Documentation SLIDE 1 
Focus –Exporting data models of CSA, 
ISDA master agreements, GMSLAs and 
GMRAs to the CDM
2024 – VM CSA finalised and in 
production, IM and legacy CSA in pipeline.
2025 – Continue working with WG to 
ensure representations capture relevant 
data, begin work on other agreements

## Page 26

Focus – using CDM standards to link the 
library of composable contracts into an 
asset class agnostic automated lifecycle 
platform. 
2023/24 - for Interest Rate Swaps and 
Verified Carbon Credits.
2025 - creating a golden record of high￾fidelity trade data to reduce operational 
pain points on reconciliation and 
streamline back-office processes.
For more questions on CDM and Collateral related initiatives, please reach out to: valdensmith@isda.org. Copyright © 2024 by International Swaps and Derivatives Association,Inc.
12
Commitment to CDM Integration: Digital Documentation SLIDE 2
Focus – CDM mappings for an adapter for 
collateral agreement data.
2024 – Review and update current mappings 
for IM, VM and Legacy CSA agreements

## Page 27

Focus – Build CDM translator for Eligible Collateral 
terms for 2- way client transfer via API
2021/2 – Phase1 ECS
representation mapping analysis
completed
2022/23 – Stage 2 technical mapping into 
application import/export functionality
2023/24 – Functionality release pending 
launch; dependent on connecting firms to 
support CDM
2022/2 3 – Continued support, input to 
workshops and contribution to CDM 
Eligible Collateral terms/conditions
2024 – Analysis for integration and 
model mapping of collateral eligibility
terms, and pilot test with connecting 
client for POC. 
For Calypso Solution: 
Focus – Redesign eligibility 
framework to extend clients options 
to include a CDM compliant version 
2024 - Analysis for CDM Eligible 
Collateral model started 
Focus – Delivery of an ingestion 
mechanism for all Eligibility terms in CDM 
format
H2 2023 / 2024 – Integration analysis 
completed in 2023, including workshops 
held with CDM. ECS mapping exercise in 
progress, to enable complex eligibility 
terms ingestion into CloudMargin in CDM 
format 
2024 – Extension for Eligible Collateral in 
2024, internal effort to re-build eligibility 
model leveraging CDM foundational 
structure 
For more questions on CDM and Collateral related initiatives, please reach out to: valdensmith@isda.org.
2024 – Focus on Collateral Eligibility 
Schedules and continued support 
through CDM working groups with 
model development
2024 – As part of the full 
representation of legal agreement, 
the CDM Eligible Collateral 
schedule use case would be in 
scope for clients wishing to 
connect using CDM. Logical 
Construct will continue to support 
through CDM working groups
2019- 2023 – Continued support and input on 
CDM Collateral related representations 
Focus – Eligible Collateral and concentration 
attributes (in legacy/regulatory CSA/CTA 
docs and Triparty ECS. Ability to compare 
and reconcile eligible collateral and 
concentration representations from any CMS 
or Collateral service providers
Q3 2024 – Analysis phase 
Copyright © 2024 by International Swaps and Derivatives Association,Inc.
13
Commitment to CDM Integration: Eligible Collateral Representation SLIDE 1

## Page 28

For more questions on CDM and Collateral related initiatives, please reach out to: valdensmith@isda.org. Copyright © 2024 by International Swaps and Derivatives Association,Inc.
13
Commitment to CDM Integration: Eligible Collateral Representation SLIDE 2 
Focus –Export collateral representation 
data from Ark51 to the CDM, continue 
with WG to ensure data is captured 
correctly.
2025 – Expand AI capacity of our 
application to extract collateral information 
automatically for exporting to CDM
Focus – Established linkage between CDM 
collateral model and FIA Tech’s Eligible 
Collateral schema, allowing interoperability 
for end users to evaluate eligible collateral 
assets on a range of global CCPs supported 
within FIA Tech’s ETD focused data set.
Continued interest in further building out 
mappings for a production feed for end user 
consumption but seeking support and 
feedback from subscribers to prioritize 
resource for the build out.
Focus – combining CDM standards, to build 
composable contracts, with tokenisation of 
real-world assets enabling near real time 
eligible collateral mobility within an 
automated lifecycle platform. 
2023/24 - for Interest Rate Swaps and 
Verified Carbon Credits.
2025 - expand scope to cover derivatives in 
other asset classes including repo trades and 
using CDM to deliver a golden record of 
high-fidelity trade data to reduce 
operational pain points on reconciliation
Focus –CDM collateral eligibility and 
concentration mappings. 
2024 – - Analysis of current structure and 
mappings ongoing.

## Page 29

Collateral- CDM Margin Call / Positions / Balances and Exposure
Data to support the Collateral Margin Call process and its related components for Collateral Balance , Collateral Positions and 
Exposure are now represented in the CDM.
A foundationalstructure to support the data required for the margin call process including:
o Standard margin call action labels
o Base details for margin call data types and attributesto support unique featuresfor issuance and response
o Collateral positions and ability to list collateral assets for responding to margin demands and for information purposes
o Collateral balance data requirements and aggregate values for margin call data and reporting

## Page 30

Collateral- Margin Call connection to other CDM components

## Page 31

Collateral- Processing Standards in CDM- What next?
2023/2024 - CDM Collateral Initiatives
Objectives:
Documentation Extensions: 
1995 VM CSA
ISDA Master Agreement 
AmendmentAgreements
Support Adoption of CDM 
Documentation and ECSinto 
Production Environments of 
External Platforms
Validate CDM DataStructure 
for Margin Call Issuance and 
Response Standards
Engage with Membersfor 
Support and Adoption
Collaboration with other 
Trade Associations to extend 
CDM
Repo and Securities 
Lending CollateralProcess

## Page 32

Digital Regulatory Reporting
Trade Reporting Rule Implementation Today

## Page 33

Digital Regulatory Reporting
Trade Reporting Rule Implementation Using the DRR

## Page 34

Digital Regulatory Reporting
Trade Reporting Rule Implementation Using the DRR
• Rule interpretations and compliance effort is spread across the industry
Mutualize regulatory reporting compliance effort
• Reflects rules, guidance and industry best practices in an unambiguous way within the DRR 
model
Gives you an unambiguous rule interpretation
• The DRR will be accessible to regulators and market participants
DRR is open-access and increases transparency
• Thereafter, only incremental efforts are required to extend the DRR model to other 
jurisdictions and future changes to reporting rules
• And such updates will be delivered through centralized DRR model changes
Defines core regulatory reporting ruleset only once
• Through the mutualized effort, firms leveraging DRR using the CDM will reap significant 
compliance, reporting and implementation project savings
Significant resource and cost savings

## Page 35

35

## Page 36

Integrating CDM and Legal Agreements
36
Securities loan
• Quantity
• Security
• Collateral Type
• Duration
• Legal Agreement
• ………
Legal Agmt
• Version
• Auto Early Term 
variant 1 business 
outcome
• Aggregation variant 5 
business outcome
• Corp Action variant 3
• …….
Legal Agmt
• Auto Early Term 
variant 1 wording
• Aggregation 
variant 5 wording
• Corp Action 
variant 3 wording
• …….
Legal 
Agmt
• Auto Early 
Term wording
• Aggregation 
wording
• Corp Action 
wording
• ……
Hard Copy or
Unstructured Soft Copy
Clause Library & 
Taxonomy
Structured Digital Document
2-way translation
UI <-> database
CDM Legal Agreement CDM Product/Transaction
Encode 
Machine
Read/Create
Legal 
agreement
is linked
to loan
Mandatory
Corp Action
• Input transaction
• Input ref data
• Input legal agreement
• Transformation function
• ………
CDM Event Function Current document 
software capability
Future document 
software capability 
Human user-based 
world
Digital computer-based 
world
Component in legal agreement informs 
functional behaviour
Future Development Work

## Page 37

Further Use Cases: Ecosystem
CDM presents opportunities to interact with entire 
eco system of other applications and standards 
provided by trade bodies

## Page 38

Further Use Cases: Smart contract technology support

## Page 39

Further Use Cases
Integration with CRIF 
standard for FRTB, SIMM, 
and SA-CVA reporting
Transcribe legally prescribed 
functional clauses from ISDA Def 
into machine readable and human 
readable codified functions
Facilitate more efficient re-use 
of data e.g. data template for 
large volume of increases of 
an Equity portfolio swap
Set a standard for the 
efficient digitalisation of 
collateral related margin 
process
Assert and mutualise the 
standardised encoding and capacity 
for implementation of legal clauses 
supporting the life cycle events of 
derivative transactions.
Express the CCP clearing handbook 
book that regulates the registration 
and clearing of a transaction into a 
machine readable and executable code 
that can be automatically generated.
Support more consistent implementation 
of market infrastructures processes such 
as clearing in tally with upcoming new 
innovative technologies (DLT, Cloud, Smart 
Contract, etc)
Match and store consistent trade 
representations that feed in “real 
time” FO trading systems using DLT 
and detect inconsistencies if any.
Aid the standardized 
representation of SSIs

## Page 40

Get Involved

## Page 41

How to get involved- Community Structure
Steering WG 
(SWG)
Contribution 
Review Working 
Group
(CRWG)
Technology 
Architecture WG 
(TAWG)
• Defines and monitors overall roadmap, setting annual priorities
• Decides support for resourcing initiatives proposed by TAWG, CRWG or DWGs
• Approves new FINOS WGs
• Decides matters of Governance & Operating Model for FINOS CDM WGs
• Final release approval
• Monthly
• Modelling, design and execution of work items within their domain scope
• Contributions compliant with guidelines and consistency across CDM
• Updates on/feeds domain based work items and plans into overall 
roadmap set by steering 
• Meets around every 2 weeks as needed
• Assembles releases
• Initial release proposal approval
• Arbitrates disputes arising from DWG contributions
• Guardians and enforcers of design principles and 
guidelines
• Triages and facilitates long-dated PRs and Issues
• Fortnightly, with sub-groups as required
Domain WGs (DWGs)
List of DWGs & their Scope as at Mar 24:
• Collateral- Collateral schedules & processes
• Repo & Bonds- Repo & bond products
• Securities Lending- Securities Lending
• Derivatives Products and Business Events (DBPE)- Derivatives products of a non-structured/exotic 
nature
• Structured Products- Structured & Exotic Derivatives
• DRR Peer Review- Digital Regulatory Reporting (Derivatives regimes)
• ISDA Legal Agreements- ISDA Legal Agreement modelling
• Defines and works on items related to technical aspects 
and architecture e.g. language distributions, packaging, 
libraries, serialization, reference data architecture, 
integration with other data standards
• Interacts with CRWG like a DWG
• Monthly, with sub-groups as required
Initiative Proposals, Updates, 
Escalation of Critical Issues
Approvals, 
Direction
Approvals, 
Direction
Technical Issue 
guidance 
requests
Guidance, 
Solutions
Dispute Escalation, 
Design guidance 
requests
Guidance, Feedback, 
Re-work requests
FINOS groups
ISDA WGs
ISLA WGs
ICMA WGs

## Page 42

How to get involved
Info hub for FINOS including user documentation downloadable distributions: Homepage | Common Domain Model (finos.org)

## Page 43

The Common Domain Model is brought to you by:
