# Industry Perspectives on the ISDA DRR Unlocking Efficiency Accuracy and Strategic Value

*Converted from: Industry-Perspectives-on-the-ISDA-DRR-Unlocking-Efficiency-Accuracy-and-Strategic-Value.pdf*

---

## Page 1

November 2025
Industry Perspectives on 
the ISDA DRR: Unlocking 
Efficiency, Accuracy and 
Strategic Value
In collaboration with:

## Page 2

Industry Perspectives on the ISDA DRR: Unlocking Efficiency, Accuracy and Strategic Value
02
CONTENTS
Executive Summary................................................................................................................................................03
Introduction to the ISDA DRR....................................................................................................................04
ISDA DRR Implementation Journey....................................................................................................06
Benefits of ISDA DRR Adoption..............................................................................................................14
What’s Next for the ISDA DRR?...............................................................................................................16
Beyond Reporting: the CDM in Post-trade Processes................................................17
Conclusion.........................................................................................................................................................................18

## Page 3

Industry Perspectives on the ISDA DRR: Unlocking Efficiency, Accuracy and Strategic Value
03
EXECUTIVE SUMMARY
This report examines how financial institutions are adopting the ISDA Digital Regulatory 
Reporting (DRR) solution, a standardized and open-access initiative built on the Fintech Open 
Source Foundation (FINOS) Common Domain Model (CDM). Drawing on insights from 
structured interviews with industry stakeholders, it highlights how firms are implementing the 
ISDA DRR to enhance regulatory reporting processes. The ISDA 
DRR is gaining traction as a transformative approach to regulatory 
compliance, offering automation, consistency and scalability. 
Institutions are adopting the ISDA DRR through varied strategies – 
either by embedding the CDM within upstream systems, integrating 
it at the post-trade layer or by converting data at the reporting stage. 
Each approach reflects different operational priorities and levels of 
investment.
Interviewees reported significant benefits from ISDA DRR adoption, 
including improved data quality and high trade repository 
acknowledgement (ACK) rates1
, with reported figures of 100% 
under Monetary Authority of Singapore (MAS) rules and 98.2% for the European Securities and 
Markets Authority’s (ESMA) European Market Infrastructure Regulation (EMIR) Refit. 
Additionally, streamlined operations and reduced ongoing costs of up to 50% were 
highlighted. The collaborative, open-access nature of the ISDA DRR was frequently cited as a 
key enabler of code reusability and faster adaptation to regulatory changes. This agility has 
positioned ISDA DRR adopters to meet evolving compliance demands more efficiently and at 
scale. As regulatory obligations continue to evolve, the ISDA DRR, powered by the CDM, is 
emerging not just as a technical upgrade, but as a strategic foundation for resilient and future￾proof regulatory reporting.
The ISDA DRR is 
gaining traction as a 
transformative approach 
to regulatory compliance, 
offering automation, 
consistency and scalability
1 The percentage of regulatory submissions successfully acknowledged by the repository/regulator

## Page 4

Industry Perspectives on the ISDA DRR: Unlocking Efficiency, Accuracy and Strategic Value
04
INTRODUCTION TO THE ISDA DRR 
Since regulatory reporting was first introduced, firms have met the requirements through bespoke 
and largely manual processes. Each institution interprets regulations independently and develops 
custom reporting logic, frequently within siloed systems. This fragmented approach often results 
in duplicated efforts, high maintenance costs and expensive change-management programs 
whenever new regulations or rewrites arise.
The ISDA DRR addresses these challenges by embedding regulatory reporting rules, logic and data 
validations directly into standardized, free, open-access code. This enables firms to automate the 
generation of regulatory-compliant reports. The CDM – the foundation of the ISDA DRR – is an 
open-source framework developed collaboratively by FINOS of the 
Linux Foundation, ISDA, the International Capital Market Association 
and the International Securities Lending Association to standardize the 
digital representation of financial instruments, transactions and lifecycle 
events. The ISDA DRR utilizes the CDM to convert the transaction 
data inputs into compliant reportable submission outputs.
The reusability of the ISDA DRR code and its reporting logic offer 
users significant long-term efficiency gains by enabling consistent 
implementation of regulatory reporting requirements across 
multiple jurisdictions and systems, reducing duplication of effort 
and maintenance costs. ISDA’s ongoing commitment to updating 
and expanding the DRR in line with new and evolving reporting 
regimes ensures sustained compliance and future proofing of firms’ 
infrastructure. Furthermore, the alignment of the DRR with the 
CDM provides a foundation for broader operational efficiency, 
supporting automation and standardization across the full trade 
lifecycle beyond regulatory reporting. 
More than 20 leading institutions, including global banks, asset managers and trade repositories, 
actively contribute to the DRR initiative under ISDA’s governance. Through collaborative industry 
working groups, regulatory requirements are jointly interpreted for each regulation and translated 
into open-source, human-readable and machine-executable code. The ISDA DRR serves as a 
golden source for mutualized regulatory interpretations. Built-in reporting validations within the 
code promote consistent reporting best practices across the industry. 
Firms have adopted the ISDA DRR to align their reporting with industry peers and benchmark 
their own interpretations to ensure optimal compliance. Four firms are currently using the 
solution: JP Morgan, BNP Paribas, Japan Securities Clearing Corporation and Banque Pictet. 
Additionally, 15 firms are running proof-of-concept (POC) initiatives for DRR adoption, 
including DBS, Depository Trust & Clearing Corporation (DTCC), Goldman Sachs and Strate 
Ltd. Technology companies and service providers, such as Fragmos Chain, Tokenovate and 
Novatus Global, are also developing post-trade infrastructure using the CDM and ISDA DRR.
The initial version of the ISDA DRR was introduced in November 2022, ahead of the first 
phase of reporting rule amendments implemented by the Commodity Futures Trading 
Commission (CFTC). Since then, its scope has expanded to cover additional regulatory rewrites 
by the Australian Securities and Investments Commission (ASIC), the Canadian Securities 
Administrators (CSA), ESMA for EU EMIR, the Financial Conduct Authority (FCA) for UK 
EMIR, the Hong Kong Monetary Authority (HKMA), the Japanese Financial Services Agency 
(JFSA) and MAS, as well as a further update to the CFTC rules (version 3.2). 
The reusability of the ISDA 
DRR code and its reporting 
logic offers users significant 
long-term efficiency gains 
by enabling consistent 
implementation of 
regulatory reporting 
requirements across 
multiple jurisdictions 
and systems, reducing 
duplication of effort and 
maintenance costs

## Page 5

Industry Perspectives on the ISDA DRR: Unlocking Efficiency, Accuracy and Strategic Value
05
Table 1: Regulations and Go-live Dates
Regulation Implementation Date ISDA DRR Status
CFTC
December 5, 2022
✓Delivered
CFTC 3.2: March 2023
JFSA
Phase 1: April 1, 2024
✓Delivered
Phase 2: April 7, 2025
ESMA EMIR April 29, 2024 ✓Delivered
FCA EMIR September 30, 2024 ✓Delivered
ASIC October 21, 2024 ✓Delivered
MAS October 21, 2024 ✓Delivered
CSA July 25, 2025 ✓Delivered
HKMA September 29, 2025 ✓Delivered

## Page 6

Industry Perspectives on the ISDA DRR: Unlocking Efficiency, Accuracy and Strategic Value
06
ISDA DRR IMPLEMENTATION JOURNEY
ISDA DRR Implementation Strategies
Interview feedback identified that determining the optimal point for CDM integration was a key 
challenge in implementing the ISDA DRR. Firms had to decide to integrate the CDM either 
natively upstream within their booking systems or embedded within a data lake at the post-trade 
processing layer, or to apply it just ahead of the reporting layer, where the CDM functions as the 
reporting engine input data.
When considering how to incorporate the CDM into their infrastructure, interviewed firms have 
adopted one of three primary integration strategies. Firms selected their architecture based on cost 
considerations and assessments of complexity.
• Native CDM Integration via Upstream Data Models: Build the CDM directly into upstream 
systems for seamless data generation.
• Post-trade CDM Conversion: Integrate the CDM within a post-trade data lake or data 
warehouse, or by translating an internal model to the CDM.
• CDM Conversion at the Reporting Layer: Transform existing Financial Products Markup 
Language (FpML) or an internal data model into CDM format just before reporting. 
Figure 1: CDM Integration Points
External Booking Platforms
A B C
Internal Booking Platforms
End-user Layer
Reference Data
Information 
(Entity Reference
Data/Product
Reference Data) 
1. Native CDM
Integration via
Upstream Data
Models
2. Post-trade
CDM Conversion
3. CDM Conversion
at the Reporting
Layer
The CDM can be
implemented at various
levels in the data stack
Risk Systems/Databases/Golden-source
and Data Lakes/Data Warehouse
1
Regulatory
Reporting 
Collateral
Management 
Regulatory Reporting Data Layer
TR/ARM
ISDA DRR
Settlement
Management 
2 3
Typical Data Flow

## Page 7

Industry Perspectives on the ISDA DRR: Unlocking Efficiency, Accuracy and Strategic Value
07
Option 1: Native CDM Integration via Upstream Data Model
This option involves adopting the CDM as the native data model across the full trade lifecycle, 
from trade capture through to post-trade processing and regulatory reporting. Implementing the 
CDM at this level typically requires rearchitecting upstream systems to ingest, store and process 
CDM JSON objects.
Integration through the upstream data model allows firms to unlock broader CDM use cases 
beyond regulatory reporting. The CDM’s standardized structure supports a wide range of post￾trade processes, including settlements, collateral management and legal documentation.
The CDM can be used for a wide range of financial processes, serving as a unified standard to 
streamline operations. It standardizes settlement logic for faster, automated and interoperable 
clearing and settlement, enhances collateral management by improving asset mobility, liquidity 
and risk controls, and embeds legal terms into trade data, enabling automated, enforceable 
contracts. This versatility makes the CDM a powerful foundation for modernizing and 
harmonizing key workflows. Additional insights into the CDM’s broader capabilities are detailed 
in the Beyond Reporting: CDM in Post-trade Processes section.
Advantages:
• Full lifecycle standardization and straight-through processing (STP);
• Enhanced data quality from upstream, thanks to integrated data validation mechanisms;
• Enables machine-executable regulatory reporting via the ISDA DRR;
• Enables harmonization across legacy booking systems to reduce run-the-bank engineering costs, 
cutting the number of separate systems that require maintaining; 
• Facilitates automation, analytics and smart contract execution (eg, via distributed ledger 
technology); and 
• Enables wider CDM adoption in other post-trade processes. 
Limitations:
• Higher upfront investment in system redesign and training;
• Requires robust governance and architectural decision frameworks; and
• Longer implementation timelines (typically six to eight months after POC).
Best Suited For: 
• Firms aiming for long-term scalability, cross-jurisdictional compliance and operational efficiency;
• Firms seeking to standardize legacy booking systems’ data models; and
• Firms looking to replace their booking systems.
Option 2: CDM Consumptions at the Post-trade Processing Layer
Firms selecting this method commonly implement the CDM within their data lake or data 
warehouse. In this model, data is transformed into CDM objects, enabling a centralized repository 
that supports multiple post-trade processes.
This approach has proven effective for integrating the CDM. Prior to implementation, one firm 
operated complex legacy systems characterized by intricate reporting flows involving extensive 
data translation and transformation. By integrating the CDM into the data lake associated with 
one of its primary asset classes, the firm is now able to generate CDM-compliant output with 
minimal data translation. The CDM output then feeds into its regulatory reporting layer, enabling

## Page 8

Industry Perspectives on the ISDA DRR: Unlocking Efficiency, Accuracy and Strategic Value
08
ISDA DRR enrichment and timely submissions to the regulator. The firm also identified wider 
operational benefits. The CDM’s role as a unified data model across banking processes allows 
multiple teams to access and scrutinize trade data, creating consistent feedback that improves data 
integrity and governance.
Like the upstream ingestion approach, firms can leverage a broader CDM adoption to enhance 
post-trade operations processes. One ISDA DRR adopter found that integrating the CDM within 
a cloud-based data lake enabled other post-trade operations – such as the settlements team – to 
easily access CDM objects. This centralized architecture positions the data lake as the CDM 
producer for downstream stakeholders, fostering utilization across additional functions, such as 
settlements and collateral management.
Advantages:
• Integrated data validation mechanisms in a data lake enhance data quality;
• Facilitates automation of post-trade processes; and 
• Minimal changes to existing trade capture systems.
Limitations:
• Higher upfront investment in system architecture design compared to conversion at the 
reporting layer; and 
• Requires robust governance and architectural decision frameworks.
Best Suited For: 
• Firms seeking to utilize the CDM across the post-trade process with minimal upstream changes 
and efficient implementation; and 
• Firms interested in adopting standardized data representation.
Option 3: CDM Conversion at the Reporting Layer
This approach involves converting existing internal data formats (often proprietary or legacy) into 
CDM-compliant structures at the point of regulatory reporting. It is particularly suited for firms 
that want to minimize disruption to upstream and data lake systems. 
One participant utilized a customized data model and implemented the CDM at the reporting 
layer during the development of a new regulatory reporting platform aligned with the ISDA DRR. 
The primary objective was to optimize regulatory reporting data flows, addressing the challenges 
posed by the previous framework, which was characterized by complexity and fragmented logic. 
To facilitate this transition, the organization developed tools to convert its internal data model 
into the CDM. This undertaking involved thorough mapping of regulatory reporting data 
elements and the establishment of CDM workflow steps necessary for generating ISDA DRR 
reports for submission to the regulator. 
Firms using this method have a shorter time to deployment and can integrate quickly with limited 
disruption to upstream data applications. Vendor solutions can speed up this process, with various 
mapping tools available on the market. When integrating at the reporting layer, the use of the 
CDM is restricted to the ISDA DRR. Integrating the CDM into other operational processes 
would require an additional build further up the data stack.

## Page 9

Industry Perspectives on the ISDA DRR: Unlocking Efficiency, Accuracy and Strategic Value
09
Advantages: 
• Minimal changes to existing trade capture and processing systems;
• Faster time-to-market for ISDA DRR compliance; and
• Easier to pilot via POCs with limited scope (eg, interest rate products).
Limitations: 
• Limited scalability across asset classes and jurisdictions; 
• Potential duplication of logic and mappings across systems; and
• Less opportunity to benefit from the CDM’s full lifecycle standardization.
Best Suited For: 
• Firms with a mature reporting infrastructure but fragmented upstream data models that are 
seeking faster implementation.
Proof of Concept
Most interviewees initiated their ISDA DRR implementation process with a POC. This 
preliminary stage proved valuable in assessing the effectiveness and applicability of the ISDA 
DRR within their reporting practices. During this period, they evaluated the optimal placement 
of the CDM within their data stack. The POC phase typically ran for three months and involved 
mapping internal data to the CDM and integrating the ISDA DRR into the reporting framework 
to generate outbound reporting messages. Firms also used this phase to conduct a parallel run, to 
identify and resolve data anomalies and validate data integrity. 
The interviewees concentrated on a single product or asset class and jurisdiction, using the output 
to assess broader implementation strategies. Firms often prioritized jurisdictions and asset classes by 
volume and complexity, beginning with vanilla products and progressing towards more complex 
instruments. The products most often selected for POCs were FX forwards, equity derivatives, credit 
default swaps or interest rate swaps, primarily due to their straightforward reporting requirements. 
Figure 2: ISDA DRR POC Implementation Timelines
Month 1
Week 1 Week 2 Week 3 Week 4 Week 5 Week 6 Week 7 Week 8 Week 9 Week 10 Week 12 Week 12
Month 2 Month 3
Planning
Training
Identify Derivative
Product
Identify Jurisdiction
Mapping
Option 1 Native CDM Integration via Upstream Data Models*
Option 2 Post-Trade CDM Conversion
Option 3 CDM Conversion at the
Reporting Layer
Integration
Inetgrate DRR into Reporting
Framework
Note: Option 1 (integrating the CDM via an upstream data model) may require more time than the eight-week period outlined in Figure 
3. Actual timelines will vary depending on a firm’s product scope, system architecture and connectivity. The use of vendors and additional 
experienced resources can significantly reduce implementation time

## Page 10

Industry Perspectives on the ISDA DRR: Unlocking Efficiency, Accuracy and Strategic Value
10
To support their POCs, firms performed activities set out in Table 2.
Table 2: POC Activities
What Internal Teams are Needed to Implement the ISDA DRR?
During the interviews, certain roles were identified as crucial to a successful DRR implementation 
and CDM integration, outlined in Table 3.
Table 3: ISDA DRR Implementation Roles and Responsibilities
Full ISDA DRR Implementation
Interview feedback indicates that the average implementation period ranges from 12 months to 21 
months, depending on the chosen implementation strategy. Adding a new jurisdiction after production 
implementation has typically taken less than three months, with most of the focus on testing. The 
project phases and activities are like those outlined in the POC section. These timelines are typical of the 
pioneering firms interviewed. New joiners will benefit from established processes, further guidance and 
additional resources, such as the ISDA DRR Starter Kit2
 and FpML to CDM translation materials3
. These 
tools can accelerate implementation timelines, particularly when the program is adequately resourced. 
Phase Activities and Outcomes
Planning •Training technology teams
•Review CDM implementation options - upstream CDM integration vs CDM integration at post trade 
vs CDM at regulatory reporting layer 
•Identify the optimal CDM implementation location within the technology data flow
•Scoping exercise to determine product/asset class and jurisdiction
•Define the POC implementation roadmap
Mapping •Map internal trade data to the CDM specification using selected implemented methodology
Integration •Integrate the ISDA DRR Java library into the regulatory reporting platform
•Integrate ISDA DRR code with reference data, both internal and external
•Review regulatory reporting output in required format - eg, ISO 20022 format
•Submit test trades to the regulator and review accuracy
Role Roles and Responsibilities 
Regtech 
Developers
Involved in coding, server set-up and tool development for the CDM and ISDA DRR. Facilitate discussions on 
optimal implementation location and support integration of the ISDA DRR into internal regulatory frameworks.
Regulatory 
Operations
Work alongside technical staff to understand ISDA DRR field interpretations and support 
implementation of the regulatory framework. Validate if there is sufficient coverage of rules and 
whether regulatory output is compliant and ACK rates are in line with the expected outcome. 
Business 
Analysts
Responsible for data model review and data model mapping to the CDM. Support testing for trade 
repository (TR) submissions and ensure compliance with various reporting regimes. Firms benefit from 
business analysts with strong product and front-office system knowledge.
Legal Implicitly involved via the open-source program office, which handles license issues related to open￾source tools. Provide sign-off on ISDA DRR interpretations. 
Compliance Addressed through internal risk mitigation processes and ensuring regulatory compliance, especially 
when using open-source code. Conduct a review of industry interpretations and identify any 
divergence with the firm's perspective.
IT Specialists Work through technical challenges like server set-up, system connectivity and infrastructure development. 
Firms need specialists with expertise in Java, data modelling and an understanding of firm’s data strategy.
Product 
Specialists 
Product experts can provide in-depth knowledge of the products being implemented. Their insights 
are vital for accurate data mapping and reporting. 
2 The ISDA DRR starter kit refers to the resources that market participants can use to begin implementing the ISDA DRR framework. The starter kit 
primarily consists of open-source components built on the Common Domain Model. It can be requested by emailing CDMDRR@isda.org
3 https://github.com/finos/common-domain-model/issues/3364

## Page 11

Industry Perspectives on the ISDA DRR: Unlocking Efficiency, Accuracy and Strategic Value
11
Table 4: Full ISDA DRR Implementation
Vendors were often engaged due to the availability of tools for CDM data mapping and ISDA 
DRR integration. One vendor platform helps firms to model ISDA DRR reporting logic, test 
outputs and integrate ISDA DRR libraries.
Implementation Cost Considerations
All participants implemented the ISDA DRR and CDM within their existing regulatory change 
budgets. No additional investment was assigned to the ISDA DRR change program. The primary 
expenses were related to training and upskilling staff to understand the CDM objects, mapping 
internal models to the CDM, integrating the ISDA DRR code base and developing new reporting 
architecture. Firms invested significant time participating in ISDA DRR and FINOS CDM 
working groups to deepen their understanding. These calls played an important role during the 
development phase, particularly in addressing issues with the code base. All interviewed firms that 
encountered code base issues used these calls to successfully resolve them.
One firm quoted an initial estimated cost equivalent to 30% of its change budget for EMIR Refit. 
This investment was allocated for infrastructure enhancements, including the implementation of 
a new reporting platform and adoption of the ISDA DRR. The firm had two resources engaged in 
ISDA sessions once or twice a week. This upfront expenditure proved valuable in the long term, as 
future implementations were quicker due to code reusability.
Phase Key Actions Responsible Teams Typical Timeline
1. Initial 
Assessment and 
Planning
•Engage stakeholders
•Map current processes and data flows
•Define objectives and scope
Project lead, operations, 
IT and compliance
Four to six weeks
2. CDM 
Integration 
Strategy 
Selection
•Evaluate integration options (native, 
post-trade or reporting layer)
•Conduct cost-benefit analysis 
•Decide on vendor support
Project team, IT and 
business analysts
Two to four weeks
3. POC •Select product/jurisdiction for POC
•Map data to the CDM
•Integrate the ISDA DRR library
•Parallel run of TR submissions with the 
ISDA DRR and legacy system
•Address eligibility, cybersecurity and 
open-source concerns
IT, regtech developers, 
operations, analysts and 
vendors (if applicable)
Three months
4. Full 
Implementation
•Develop project plan
•Provide training to the delivery team 
on the CDM/ ISDA DRR 
•Attend relevant working groups
•Map the CDM to internal data and 
integrate the ISDA DRR libraries 
•Address eligibility, cybersecurity and 
open-source concerns
IT, operations, compliance 
and vendors (if 
applicable)
Eight to 13 months (varies 
by strategy)
5. Testing and 
Go-live
•System integration testing
•End-to-end regression testing
•User acceptance testing (UAT) with 
operations
•Deployment
IT, operations, regulatory 
reporting and vendors (if 
applicable)
Two to three months
6. Optimisation 
& Expansion
•Develop key performance indicator 
metrics for the ISDA DRR
•Collect feedback on ACK rates and 
business as usual
•Assess if there is a desire to expand 
to more products/jurisdictions
Project team, operations 
and IT
Ongoing

## Page 12

Industry Perspectives on the ISDA DRR: Unlocking Efficiency, Accuracy and Strategic Value
12
Another firm noted that a significant cost factor was the learning curve associated with the ISDA 
DRR and CDM. The team dedicated substantial time and effort to understanding new systems 
and processes and were heavily involved with the ISDA DRR calls, which contributed to the 
initial expenses. Implementing new architecture, such as Amazon Web Services (AWS) and an 
open-source database system for the CDM, represented another 
notable cost. Nonetheless, the team efficiently allocated resources 
within the existing budget to cover these implementation costs.
While initial ISDA DRR implementation efforts have been delivered 
within existing regulatory change budgets, firms aiming to implement 
the ISDA DRR outside of a non-discretionary change program must 
consider the cost implications of the architectural uplift. In this 
context, a clear and measurable return on investment (ROI) is essential 
to build a compelling business case and justify further funding. 
Interview feedback indicates that some firms have already achieved cost savings up to 50% since 
implementation. This is a promising indicator that other firms could achieve comparable results with 
a well-defined strategy. These savings have largely been attributed to enhanced code reusability, lower 
maintenance overheads and more efficient change-management processes. 
Other Implementation Considerations
Training and Development
Training and development emerged as a critical success factor in implementing the ISDA DRR 
and CDM across all interviewed firms. The transition to the ISDA DRR required significant 
upskilling of technology, operations and compliance teams to understand the CDM and ISDA 
DRR code base, as well as new architectural components. The interviewees had to dedicate 
substantial time and resources to structured training sessions and often leveraged vendor solutions 
and participated in industry working groups, such as those led by ISDA and FINOS. The main 
working groups that contributed towards implementation success are: 
• ISDA DRR Peer Review Working Group
• ISDA DRR Steering Committee
• ISDA DRR Technical Execution Working Group4
• FINOS CDM Derivative Product and Business Events Working Group5
These working groups contributed to a deeper understanding of CDM products, business events, 
rule interpretation, validation, escalations and solutions for technical queries. They also provided 
members with information about upcoming changes in the CDM and the roadmap for future 
modifications. A buy-side firm that participated in the interviews noted that involvement in the 
working groups helped establish best practices tailored to the specific requirements of buy-side firms.
Regulatory Reporting Architecture
Firms adopting the ISDA DRR will still need regulatory reporting architecture to send 
submissions and receive responses from their TR. The ISDA DRR supports the process up to the 
generation and pre-validation of regulatory reporting messages. All interviewed firms still had 
Interview feedback 
indicates that some firms 
have already achieved 
cost savings up to 50% 
since implementation
4 The three ISDA working groups – the ISDA DRR Peer Review Working Group, the ISDA DRR Steering Committee and the ISDA DRR Technical 
Execution Working Group – can be found at www.isda.org/committees/
5 https://lists.finos.org/g/cdm-derivatives-wg

## Page 13

Industry Perspectives on the ISDA DRR: Unlocking Efficiency, Accuracy and Strategic Value
13
a regulatory reporting engine that submitted their messages to the TR using an ISO 20022 or 
harmonized XML message generated by the ISDA DRR. One firm noted that its implementation 
uses a mix of message formats, depending on the jurisdiction and trade repository – ISO 20022 
messages for one jurisdiction and .csv messages for others. The ability of the ISDA DRR to 
generate both .csv and ISO 20022 messages was seen as a significant advantage, as it allowed the 
firm to maintain its existing reporting pipelines across different TRs without requiring format￾specific changes.
One of the significant challenges is managing eligibility when transitioning to the ISDA DRR. 
All participants had to implement logic within their reporting engines to manage eligibility rules, 
covering entity and product eligibility and jurisdictional scoping. Eligibility is usually addressed as 
a separate part of the DRR change project. 
Open Source, Cloud Readiness and Cybersecurity
Firms implementing the ISDA DRR should ensure they have appropriate tools to address 
cybersecurity risks and evaluate the open-access ISDA DRR code and open-source CDM model 
effectively. Hosting solutions are required to integrate the open-source code, which can be done 
on cloud or on premises. Cloud-ready solutions like AWS are being used by adopters to host 
the CDM. One firm had a license to integrate open-source code via an on-premises solution. 
To address cybersecurity concerns, it implemented an internal tool to evaluate open-source 
components and established mitigation measures within its architecture. Another firm also used 
an on-premises solution and utilized code scanners to check the code prior to deployment. This is 
part of the firm’s internal build process. 
Vendor Support 
Vendor support is optional and can help streamline ISDA DRR and CDM adoption by providing 
specialized tools, integration accelerators and training resources. Interviewed firms that used 
vendor support found it particularly valuable for testing CDM objects and ISDA DRR code 
as vendors offered platforms and expertise to validate outputs and accelerate implementation. 
While these solutions can simplify technical integration and automate workflows, organizations 
should carefully consider costs, licensing and the need for ongoing technical expertise. Effective 
integration and maintenance are achievable with or without vendor involvement, depending on 
internal capabilities and project requirements.

## Page 14

Industry Perspectives on the ISDA DRR: Unlocking Efficiency, Accuracy and Strategic Value
14
BENEFITS OF ISDA DRR ADOPTION
Figure 3: Benefits of ISDA DRR Adoption Framework Comparison
Standardization Across Jurisdictions
Firms are leveraging the CDM and ISDA DRR to harmonize reporting across multiple 
jurisdictions. One firm described its implementation journey, noting that it is fully implemented 
for various regimes, including EMIR in the EU and UK, Singapore under MAS rules, Canada 
under CSA requirements and Hong Kong under HKMA regulations. Another firm stated that 
it has implemented the ISDA DRR for its equities business under 
ASIC, MAS and CSA reporting rules. Both highlighted a reduction 
in fragmentation and regulatory interpretation risk.
Streamlined Change Management Process
The ISDA DRR enables reusability of code and logic, which 
accelerates the change-management process. Faster turnaround times 
for regulatory changes have been achieved, improving responsiveness 
to evolving requirements. One participant noted an 85% reuse rate 
across jurisdictions during rewrites, attributed to the introduction of 
critical data elements and ISDA DRR code.
This helped achieve the firm’s cross-market strategy for 
regulatory reporting, which aimed to standardize reporting 
processes and ensure consistency across different jurisdictions 
and lines of business. During its recent implementation of the 
CSA rules, the firm was able to utilize 92% of its existing ISDA DRR code. As a result, it 
could focus more on testing and enhancing operational processes. Another firm reported a 
30% cost reduction by reusing code and minimizing time spent on interpretation. These 
efficiencies freed up budget for enhancing data controls and developing more advanced 
graphical user interfaces for the regulatory operations team. 
The ISDA DRR enables 
reusability of code 
and logic, which 
accelerates the change￾management process. 
Faster turnaround times 
for regulatory changes 
have been achieved, 
improving responsiveness 
to evolving requirements
Standardisation
BAU Complexity
DRR Reporting Framework Legacy Reporting Framework
Maintenance Costs Code Reusability
Remediation Efforts Accuracy

## Page 15

Industry Perspectives on the ISDA DRR: Unlocking Efficiency, Accuracy and Strategic Value
15
Improved Accuracy and Reduced Complexity 
The CDM and ISDA DRR have led to higher accuracy in regulatory reporting by digitizing rules 
and automating mapping. The built-in validations ensure output is generated in a regulatory￾compliant format. Firms highlighted that ISDA DRR and CDM implementation has resulted 
in higher accuracy in regulatory reporting. One bank observed a 100% ACK rate for reporting 
under the MAS rules during the go-live period, while another achieved a 98.2% ACK rate 
following implementation of the EU’s EMIR Refit reporting requirements. The ACK rates were 
notably higher than those observed during previous implementations and compare favorably with 
established business-as-usual (BAU) ACK rates. The organizations have been able to maintain high 
ACK rates after go-live, which they attribute to the standardization and automation of reporting 
processes through the ISDA DRR.
Enhanced BAU Operations 
Issue management can be performed more efficiently with the ISDA DRR. The reduced 
complexity in workflows and fewer manual interventions enable teams to identify the sources 
of errors more quickly. According to one firm, BAU teams would previously have had to review 
multiple systems for root-cause analysis. The ISDA DRR has allowed for quicker and simpler 
investigation. Another firm noted that issue management has become externalized, with ISDA 
now overseeing the DRR industry working groups and BAU issue management, which has freed 
up the regulatory operations team’s capacity.
Quicker Remediation Process 
The implementation of the ISDA DRR has reduced the UAT window. Developers can perform 
comprehensive end-to-end validations independently, as there is minimal interference from other 
systems. Furthermore, the operations teams in certain firms have assumed the role of UAT testers. 
As the BAU workload reduces, operations teams can dedicate greater attention to testing and 
validation activities.
Cost Savings and Budget Optimization
Implementations have often been completed within existing change budgets, with future 
reductions in regulatory spending expected due to lower maintenance and shorter change 
windows. During interviews, one firm emphasized that the cost of the ISDA DRR is 
significantly lower than its previous in-house solution. All firms interviewed anticipate a 
reduction in ongoing regulatory maintenance costs for processes that are live with the ISDA DRR.

## Page 16

Industry Perspectives on the ISDA DRR: Unlocking Efficiency, Accuracy and Strategic Value
16
WHAT’S NEXT FOR THE ISDA DRR? 
The ISDA DRR was originally developed to address challenges in derivatives trade and transaction 
reporting. Over time, its applications have expanded beyond derivatives reporting. Some of these 
emerging use cases are detailed in this section.
Cross-check and Quality Assurance of Regulatory Logic
The ISDA DRR uses shared logic as a benchmark, enabling firms to run legacy reports in parallel 
and quickly spot discrepancies. Any divergence in output signals potential misinterpretations or 
errors in existing processes. Some early adopters have used the ISDA DRR in parallel to validate 
that their in-house systems are producing the right results or to debug reporting breaks by 
comparing against the industry standard code. This logic comparison use case helps firms gain 
confidence and catch errors before fully switching over to ISDA-DRR-based reporting. Some 
firms have gone live with implementing the ISDA DRR for quality assurance purposes and 
have found it to be advantageous.
Expansion to New Products and Jurisdictions
The ISDA DRR already covers all vanilla derivatives and common exotic products. Individual 
firms can also enhance the model to cover bespoke complex products. ISDA also plans to 
extend the DRR to Securities and Exchange Commission rules, requirements under the Markets 
in Financial Instruments Regulation (MIFIR) in the EU and UK and obligations under the 
Securities Financing Transaction Regulation (SFTR), showing an intent to cover post-trade 
transparency and transaction reporting in securities markets as well. In practice, this means a firm 
already using the ISDA DRR can utilize the DRR libraries to accelerate its SEC, MIFIR and/or 
SFTR implementation. This highlights the value of the ISDA DRR as a scalable platform. Once 
onboard, adding a new regulation is much simpler.
Shared Industry Utilities and Services
An increasingly collaborative use case is emerging in which market infrastructure providers and 
vendors are incorporating the ISDA DRR framework. For example, the DTCC intends to embed 
ISDA DRR logic within its Global Trade Repository services, allowing its client trade submissions 
to be validated via the ISDA DRR. While firms may not directly implement the code in this 
type of arrangement, they benefit from the consistency provided by utilities leveraging the ISDA 
DRR. This scenario reflects a significant industry shift towards widespread adoption, with both 
individual firms and market utilities aligning on a unified digital rulebook.

## Page 17

Industry Perspectives on the ISDA DRR: Unlocking Efficiency, Accuracy and Strategic Value
17
BEYOND REPORTING: CDM IN POST-TRADE PROCESSES
Accelerated Settlement and Clearing Systems
As financial markets move toward shorter settlement cycles, such as T+1, the CDM is 
increasingly being adopted to support near real-time settlement. The CDM provides a unified 
framework that standardizes settlement logic, enabling automation and interoperability across 
platforms and smart contracts. This makes it a foundational layer for clearing systems, especially 
when integrated with DLT. Firms leveraging the CDM in this space benefit from reduced latency, 
improved reconciliation and enhanced transparency across asset classes.
Collateral Management
Collateral management is a critical function in trading and post-trade operations, but its 
representation varies widely across firms. The CDM addresses this fragmentation by standardizing 
workflows, definitions and data formats. This enhances asset mobility, supports reuse and 
tokenization, and streamlines processes such as haircuts and margining. Vendor tools have 
already been integrated into the CDM to support initial margin (IM) and credit support 
annex (CSA) consumption, demonstrating its practical utility in improving liquidity and 
reducing operational risk.
Legal Documentation
The CDM is being used to digitize and automate legal documentation processes. By embedding 
legal terms directly into trade data, the CDM enables machine-executable contracts that 
enhance enforceability and reduce ambiguity. This supports efficient negotiation, maintenance 
and compliance of legal agreements. Mapping exercises between the CDM and standard 
agreements (eg, the ISDA Master Agreements, IM/variation margin CSAs) allow for dynamic data 
flows and integration with smart contracts, particularly in tokenized environments.

## Page 18

Industry Perspectives on the ISDA DRR: Unlocking Efficiency, Accuracy and Strategic Value
18
CONCLUSION
Interviews with industry stakeholders confirm that adopting the ISDA DRR powered by the 
CDM is delivering real benefits for financial institutions across multiple areas of the regulatory 
reporting process.
Key outcomes reported by participants include:
• Improved data quality and greater accuracy in reporting;
• Operational efficiencies through automation and streamlined processes;
• Code reusability, enabling faster development cycles;
• Accelerated adaptation to evolving regulatory requirements; and
• Cost efficiencies from lower maintenance and shorter change windows.
Integration strategies have differed among firms, reflecting the various options available for 
implementing the ISDA DRR. Most implementations were completed within existing budgets, 
highlighting the cost-effectiveness of the approach. Success was strongly linked to effective training 
and cross-functional collaboration, which helped teams navigate the transition smoothly. 
Overall, stakeholders agreed that the ISDA DRR and CDM are helping firms to:
• Harmonize reporting across jurisdictions and systems;
• Reduce regulatory risk through standardization; and
• Future-proof compliance in an increasingly complex and dynamic environment.
As regulatory demands continue to evolve, the collective experience of these institutions 
demonstrates that embracing the ISDA DRR and CDM is not just a technical upgrade, but a 
strategic move towards more resilient, scalable and agile regulatory reporting.

## Page 19

Industry Perspectives on the ISDA DRR: Unlocking Efficiency, Accuracy and Strategic Value
ISDA® is a registered trademark of the International Swaps and Derivatives Association, Inc. 19
ABOUT ISDA
Since 1985, ISDA has worked to make the global derivatives 
markets safer and more efficient. Today, ISDA has over 1,000 
member institutions from 78 countries. These members 
comprise a broad range of derivatives market participants, 
including corporations, investment managers, government 
and supranational entities, insurance companies, energy and 
commodities firms, and international and regional banks. In 
addition to market participants, members also include key 
components of the derivatives market infrastructure, such as 
exchanges, intermediaries, clearing houses and repositories, 
as well as law firms, accounting firms and other service 
providers. Information about ISDA and its activities is 
available on the Association’s website: www.isda.org. 
Follow us on LinkedIn and YouTube.
ABOUT CAPGEMINI
Capgemini is an AI-powered global business and technology 
transformation partner, delivering tangible business value. We 
imagine the future of organizations and make it real with AI, 
technology and people. With our strong heritage of nearly 60 
years, we are a responsible and diverse group of 420,000 team 
members in more than 50 countries. We deliver end-to-end 
services and solutions with our deep industry expertise and 
strong partner ecosystem, leveraging our capabilities across 
strategy, technology, design, engineering and business operations. 
The Group reported 2024 global revenues of €22.1 billion.
Make it real | www.capgemini.com
