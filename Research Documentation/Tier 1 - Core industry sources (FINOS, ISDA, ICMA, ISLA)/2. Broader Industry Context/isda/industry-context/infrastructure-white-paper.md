# infrastructure white paper

*Converted from: infrastructure-white-paper.pdf*

---

## Page 1

1
September 2016
ISDA Whitepaper
The Future of Derivatives 
Processing and Market 
Infrastructure

## Page 2

ISDA Whitepaper: The Future of Derivatives Processing and Market Infrastructure
2
CONTENTS
Executive Summary ......................................................................3
Introduction .................................................................................5
Infrastructure Challenges Facing the Derivatives Industry .................6
• Pre-trade..................................................................................................... 6
• Trade Execution........................................................................................... 8
• Post-trade ................................................................................................... 9
• Collateral Management .............................................................................. 12
• Reporting.................................................................................................. 12
The Need for Change ..................................................................13
The Future – Opportunities for Technology and Standardization.......15
• Standardization ......................................................................................... 15
• Data ......................................................................................................... 16
• Documentation .......................................................................................... 17
• Process..................................................................................................... 18
• Collaboration............................................................................................. 20
• Technology ................................................................................................ 21
Conclusion.................................................................................25
Next Steps .................................................................................26

## Page 3

ISDA Whitepaper: The Future of Derivatives Processing and Market Infrastructure
3
EXECUTIVE SUMMARY
Derivatives markets today are very different to the derivatives markets before the crisis. In response 
to regulatory changes instigated by the Group-of-20 (G-20) nations in 2009, most derivatives trades 
are now reported to a repository, clearing is more common, and electronic execution is gaining 
momentum. These changes have had an impact on virtually all areas of the transaction process, 
from pre-trade execution through to lifecycle management and reporting.
Market participants have worked hard and have been successful in meeting the various deadlines for 
compliance set by regulators. But in focusing on meeting the tight timelines, less attention has been 
given to achieving operational and technological efficiencies.
The complexity inherent in the new derivatives ecosystem is now putting derivatives participants 
under considerable strain. Given the lack of opportunity to redesign the embedded processes 
in order to meet regulatory time frames, industry participants find themselves struggling with 
a complex set of workflows that create challenges for continued compliance, efficiency and 
operational risk management. There is also growing concern about the capacity across the industry 
to support the needs of all market participants in all areas.
This now needs to be addressed.
This paper provides an insight into the challenges facing market participants across all parts of the 
derivatives process, and proposes a path forward for developing a standardized, efficient, robust and 
compliant ecosystem that supports the needs of an array of market users. The principles focus on 
three key areas: 
• Data: Agreement on formats and identifiers would significantly benefit market participants and 
regulators. In particular, a robust, granular, multi-use product identifier with strong governance 
based on an open-source infrastructure would remove many systemic inefficiencies and further 
promote transparency.
• Documentation: Despite a plethora of standard documents published for industry use, many 
documents are still customized between transacting parties. The benefits of this customization are 
now being questioned. There are opportunities for further standardization and digitization across 
the suite of existing ISDA documentation, from Master Agreements to definitions booklets and 
confirmation templates, which will drive more efficient processing and adoption of technology, 
both within firms and across the market.
• Process: The complexity and multiplicity of business processes required to support the same 
functions within or across asset classes is significant. In some cases, this has been caused by a 
divergence of requirements, driven by global regulations. However, there is an opportunity for 
the industry, working collaboratively with global regulators, to reassess and promote improved 
standards in this space. Standard processing models can provide a solid base for further 
evolution of the derivatives processing environment in order to remove cost and inefficiency. 
Additionally, the industry would benefit significantly from a holistic review and redesign of 
collateral management processes to aid compliance with new rules on margining for non-cleared 
derivatives.

## Page 4

ISDA Whitepaper: The Future of Derivatives Processing and Market Infrastructure
4
To deliver these objectives, the industry needs to collaborate effectively across all sectors – market 
participants and their representatives, infrastructures and regulators. Where standards are required, 
it is imperative they are suitable for addressing the needs of all stakeholders. While market 
participants have collaborated on initiatives in the past, many firms continue to individually build 
and maintain the same functional solutions, particularly in post-trade activities. In many cases, 
there is no competitive advantage in continuing to do this, and it only serves to increase the overall 
cost of supporting the derivatives market. 
In addition, the industry needs to further explore the role of existing and new technologies in the 
development of the future-state derivatives ecosystem. Technology has evolved considerably over 
recent years and continues to do so. While many market participants and infrastructures have 
embraced technology as part of the evolution of the current ecosystem, adoption has not always 
been complete. This may continue to be the case, but the current need to find efficiencies provides 
a platform from which the industry can collaborate on the analysis, design and implementation of 
a system that leverages advancements in technology. Cloud services and distributed ledger are two 
examples where industry focus on how they can be deployed to address the challenges faced by 
market participants would be extremely worthwhile. 
All of this requires time and commitment on the part of industry participants, as well as thought 
leadership, direction and oversight. If the industry is able to collaboratively explore the opportunity 
to redesign the processing model and leverage advances in technology, ISDA believes it will benefit 
from greater operating efficiency, more consistent regulatory compliance and increased quality and 
transparency of data.
As a first step, there is an urgent need to agree on common objectives, be they short-term solutions 
to current infrastructure challenges or longer-term objectives associated with process redesign. 
ISDA, with its broad membership, has always provided an environment for this to happen, and 
will continue to encourage and facilitate discussion among traditional and new operators in the 
derivatives market, as well as other industry associations and regulators. If market participants 
embrace this opportunity and pursue the proposals outlined in this paper, we believe there is a real 
opportunity to improve operating efficiency, reduce operating costs and risk, and increase both 
quality and transparency of data.

## Page 5

ISDA Whitepaper: The Future of Derivatives Processing and Market Infrastructure
5
INTRODUCTION
The derivatives industry has changed significantly since the first interest rate swap was executed in 
1981. A steady growth in products, trade volumes and outstanding notional has seen it become a 
multi-trillion dollar market with outstanding notional of $492.9 trillion combined across all asset 
classes by the end of December 2015. 
During this time, the post-trade processing and market infrastructure landscape has changed 
considerably. The process for trade confirmations serves as a good illustration. The reliance on long￾form paper confirmations has largely been replaced by industry solutions that leverage industry￾standard ISDA documentation to facilitate the electronic exchange and matching of trade details. 
In some cases, short-form confirmations have been developed to reduce the number of fields that 
firms need to exchange and match. This has had a dramatic effect on the timeliness of confirmation 
processing and represents a key risk mitigant within the industry. Further industry collaboration 
has facilitated improved processes for settlement and lifecycle event management and a gradual 
move towards clearing for vanilla products. Other initiatives, such as compression and portfolio 
reconciliation, have improved risk management.
Many of these initiatives were driven by market participants and their desire to improve the safety 
and efficiency of the derivatives market, with ISDA being at the epicenter of these activities. However, 
following the 2008 financial crisis and the commitments made by the G-20 in Pittsburgh, a raft 
of new regulation across the globe has required the implementation of new techniques for risk 
management and process efficiency. Key among these are the increased use of clearing, the execution 
of transactions on electronic trading venues, greater use of reporting to assist regulators to monitor 
systemic risk, and the development of margin requirements for non-cleared transactions. These 
changes have introduced new infrastructures to the market and created new ways of executing and 
processing derivatives trades. In the case of margin requirements for non-cleared derivatives – which 
were implemented in some jurisdictions from September 2016 – an industry focus on collateral 
management processing efficiency and optimization presents a real challenge and opportunity.
These changes have placed a considerable burden on derivatives market participants. The increased 
cost of supporting traditional post-trade activities and complying with new regulatory obligations, 
alongside reduced profit margins in many areas of the derivatives business, is not sustainable. 
Industry participants need to find new ways of operating. However, uncertainty over how the 
various derivatives markets will grow over the next few years, as well as uncertainty over the final 
outcome of some domestic and international regulations (eg, the revised Markets in Financial 
Instruments Directive, or MIFID II) makes it increasingly difficult for firms to make plans 
and invest for the future. The complicated interaction between systems and processes, whether 
internal or external, takes time and financial commitment to evaluate and replace, and needs to be 
approached in a collaborative manner across the market. 
ISDA has written this paper to help develop a common vision on what the industry requires in 
order to reduce operational complexity and associated costs. A common approach is preferable to 
each firm trying to address the shared challenges on its own and arriving at sub-optimal, duplicative 
and more expensive solutions. 
Furthermore, these challenges arise in the midst of huge technological change, which could 
potentially help to re-draw the landscape. With all of this in mind, the derivatives industry needs to 
take stock and develop a collective approach to securing safe and efficient processing of transactions 
as it moves beyond the initial wave of global regulation. 
By stepping back, taking the time to understand these changes and the potential opportunities for 
process redesign and embracing new technology, the industry will deliver safe and efficient markets.
A raft of new 
regulation 
across the globe 
has required the 
implementation 
of new 
techniques 
for risk 
management 
and process 
efficiency

## Page 6

ISDA Whitepaper: The Future of Derivatives Processing and Market Infrastructure
6
INFRASTRUCTURE CHALLENGES FACING THE 
DERIVATIVES INDUSTRY
To fully appreciate the range of challenges that exist today, we should start by considering the 
evolution of the derivatives process flow. Figure 1 represents the core functions that support a trade 
from inception through its lifecycle. 
Figure 1: Generic Process Flow
Considered in isolation, this process flow is relatively simple, but the reality is very different. 
Despite common agreement on the high-level process flow and the steps required to support 
derivatives transactions, the rate of change and nuances of individual asset classes have resulted in 
each evolving its own multi-dimensional ecosystem of market infrastructures and processes across 
the entire front-to-back lifecycle. This fragments the trading ecosystem, and increases cost and 
complexity. 
Global regulatory reform has contributed to this rapid and unstructured evolution. Regulatory 
changes have caused firms to implement new or amended processes across the front-to-back lifecycle 
in order to be compliant. However, the speed at which these modifications have needed to be 
made means they have not always occurred in the most efficient manner. As a result, the costs of 
supporting derivatives transactions have also increased when compared to alternative products, such 
as futures or other exchange-traded derivatives. 
 
Pre-trade
Knowing who is permitted to trade and therefore which regulations are applicable, as well as pricing 
any resulting additional post-trade considerations into the execution process, represents a significant 
challenge – particularly when new rules in some jurisdictions require firms to track and demonstrate 
best execution. It is essential that market participants look at mechanisms to automate the checking 
and validating process and build or integrate appropriate rules engines into their infrastructure.
Regulatory 
changes have 
caused firms to 
implement new 
or amended 
processes 
across the 
front-to-back 
lifecycle in 
order to be 
compliant

## Page 7

ISDA Whitepaper: The Future of Derivatives Processing and Market Infrastructure
7
Firms also need to consider the downstream consequences of failing to comply with a particular 
regulation. Trade rectification activities or trade nullification carry the associated risk that markets 
move during the intervening period. They could also result in regulatory penalties and/or a 
damaged reputation. Trade nullification has been addressed, to an extent, by the introduction of 
pre-trade credit checking for trades executed under rules set out by the US Commodity Futures 
Trading Commission (CFTC), and equivalent process steps are needed for similar rules under the 
revised Markets in Financial Instruments Directive and its associated regulation (MIFID II/MIFIR) 
in Europe.
Execution of relationship documents such as Master Agreements and Credit Support Annexes 
(CSAs) are another critical aspect of the pre-trade landscape. ISDA has worked with members to 
develop and publish standard forms of these documents to assist industry participants, but many 
are still heavily negotiated as part of the execution process. A degree of tailoring is undoubtedly 
required to reflect the variety of market participants and ensure appropriate protection for all. 
However, this variation creates a layer of complexity and introduces operational and technology 
challenges to accurately storing and recalling these nuances for business purposes. 
Solutions can be developed to assist firms with scraping existing documents and recording 
the information electronically, but this only creates a point-in-time representation that may 
need continual reconciliation. It is therefore unlikely to guarantee 100% accuracy. Greater 
standardization and the utilization of technology to facilitate electronic creation and digital 
representation of these documents could provide significant benefit to industry participants, 
allowing recall and re-use of the data for additional purposes. 
Furthermore, there is a significant challenge in Europe regarding transparency requirements, 
which are a key element of MIFID II/MIFIR. The first test to resolving whether a trade should 
be subject to transparency requirements is to determine if it is traded on a trading venue (ToTV). 
While this may seem straightforward, the requirement is also designed to capture over-the-counter 
(OTC) trading in instruments that are traded on venues. While secondary measurements related to 
liquidity and size-specific-to-the-instrument (SSTI) thresholds have received significant attention 
from the industry and regulators, there has been little attention on the true scope of ToTV until 
recently. This lack of clarity creates challenges for firms that need to build systems and processes to 
ensure they are compliant. 
While MIFID II will not come into effect until January 2018, experience suggests that the 
investment in design, building and implementation of systems and processes can take significant 
time. ISDA continues to support members to define the principles of what instruments are ToTV, 
and to develop mechanisms for practical implementation of those principles. 
The industry faces a number of challenges and issues that need to be carefully considered in order to 
ensure market participants can develop their processes accordingly. These include: the development 
of product identifiers at an appropriate level of granularity for the ToTV determination; the 
development of a suitable infrastructure to ensure there is clarity over which products are in scope 
and which are not; and issues such as frequency of change, lead time from the notification of such 
change and market adoption. 
Finally, there are a variety of representations and agreements that need to be made in order to 
execute a transaction. Having the means to make these representations and store the necessary 
output in digital form for re-use, either at the point of trade or further in the post-trade process, is 
critical for improved efficiency. To date, there are mechanisms to facilitate some of this, but more 
work needs to be done in this area.
It is essential 
that market 
participants 
look at 
mechanisms 
to automate 
the checking 
and validating 
process 
and build 
or integrate 
appropriate 
rules engines 
into their 
infrastructure

## Page 8

ISDA Whitepaper: The Future of Derivatives Processing and Market Infrastructure
8
Trade Execution
A key objective of new regulation is to make the execution process fair and more efficient. However, 
it will take the industry more time to complete the transition. For some market participants, the 
process of execution appears complicated and confusing, with new infrastructures in the form of 
trade execution venues having been introduced in several jurisdictions. This confusion is amplified 
by inconsistent rules for these venues across jurisdictions. 
Swap execution facilities (SEFs) are now firmly established in the US under CFTC rules. These 
rules dictate whether a firm is required to trade on or off venue, and for which products. They 
also specify the obligations of the venues with regard to execution protocol and aspects of post￾trade processing. However, as the post-trade processing rules have been implemented, a range of 
approaches to supporting post-trade functions have developed. 
Similarly, trade execution rules came into effect in Japan in September 2015, but the requirements 
to trade on electronic trading platforms are not wholly consistent with other jurisdictions. 
In Europe, the trading obligation is due to come into force as part of MIFID II, which introduces 
multilateral trading facilities (MTFs) and organized trading facilities (OTFs) to the derivatives 
landscape alongside organized exchanges. The exact details of the rules and requirements for these 
execution venues remain vague, but, in addition to the challenges associated with supporting ToTV, 
we anticipate similar challenges in the evolution of multiple additional process flows as venues are 
established and have to interface with post-trade activities. 
European market participants are also waiting for details on the products that will be subject to the 
trading obligation. The European Securities and Markets Authority (ESMA) still needs to conduct 
consultations on the procedure for determining products that are in scope, as well as the specific 
products for the initial go-live of MIFID II. As noted previously, MIFID II does not come into 
effect until January 2018, but it will take market participants time to develop the infrastructure and 
processes to support these requirements. The sooner there is visibility on the scope of the rules, the 
sooner this work can commence. 
Elsewhere, market participants have raised concerns about the risks associated with a market rapidly 
migrating to new forms of execution. For example, where trading mandates are already in operation, 
trades are increasingly executed in electronic form, with prices streamed to execution venues by 
liquidity providers. Market participants are exposed to the risk that breaks in this process at the 
trading-venue level could cause prices to become stale but executable and ultimately cleared unless 
robust controls are in place to monitor the streamed prices. 
Mechanisms such as kill switches and heartbeats are already used in some parts of the infrastructure 
and allow a firm to suspend its operations should an issue be identified. Opportunities to extend 
these tools to other operations should be explored. It is incumbent on all participants in the process 
– whether they are execution venues or executing parties – to ensure they have sufficiently robust 
processes to identify and address these types of incidents. In addition, SEFs have a challenge because 
they are required to monitor position limits and manipulation within the swaps market. This is 
extremely difficult given that swaps are fungible across SEFs, but individual SEFs do not have 
visibility regarding trades executed on other venues.
For some 
market 
participants, 
the process 
of execution 
appears 
complicated 
and confusing

## Page 9

ISDA Whitepaper: The Future of Derivatives Processing and Market Infrastructure
9
The above commentary focuses on the challenges associated with a market moving to execution on 
organized venues. Additionally, market participants in Europe will need to adjust to a regime that 
permits trading of derivatives by a systematic internaliser (SI), albeit subject to certain restrictions 
and obligations. At this stage, it is not clear exactly how this arrangement will operate and how it 
will impact the global ecosystem, existing process models or the traditional model of market makers. 
But with MIFID II on the horizon, industry participants need to start considering these questions.
Post-trade
Regulatory reform has accelerated the bifurcation of the derivatives market into two distinct 
forms: cleared and bilateral. In some cases, post-trade processes are common and can be leveraged. 
However, there are instances where infrastructure or processes may be more relevant to one or 
the other environment. All of this adds to the complexity of the post-trade environment. In the 
following sections, we highlight some of the specific post-trade challenges.
1. Validation and Trade Routing
Trade execution venues represent points of entry of a derivatives transaction into the post-trade 
environment, and inconsistencies in approaches adopted by venues inevitably causes disruption 
to a relatively widely established post-trade processing environment. Factors influencing different 
approaches include whether a trade is executed electronically or by voice, through a request-for￾quote (RFQ) or central-limit-order-book (CLOB), and, to a lesser extent, the requirement for 
a transaction to be cleared, along with competition between venues. This, in turn, influences a 
market participant’s decision on whether or not to leverage existing infrastructure and can lead to 
a fragmentation of market practice, which reduces efficiency and creates challenges for regulatory 
compliance. As a consequence, where there is no competitive advantage, the industry needs to 
collaborate on changing current practices, review process design and identify opportunities to 
deploy new technologies in order to build a robust and efficient future state.
For example, direct entry from an execution venue into a clearing house is different from the 
historic process flow that many market participants have adopted and integrated with their internal 
infrastructure and operational processes. There are instances where firms may wish to retain a 
validation process to ensure that a trade intended for clearing actually clears in an accurate state. 
An erroneously cleared trade could have a significant financial or reputational impact on the parties 
involved, absent the necessary tools to correct this at the central counterparty (CCP) level. The 
challenge for the industry is to develop solutions that enable the validation and, if necessary, correction 
to take place in as short a time as possible. CFTC straight-through-processing (STP) rules require this 
to be done as quickly after execution as would be technologically practicable if fully automated systems 
were used. Proposed rules under MIFID II require transactions executed on venue to be sent to a 
central clearing house within 10 seconds if electronically executed, and otherwise within 10 minutes. 
The current industry infrastructure and processing models make these time frames extremely difficult 
to comply with. Infrastructures and market participants need to review existing practices and explore 
opportunities for process redesign and adoption of new technologies in order to meet these new 
requirements without introducing operational risk. Moreover, if all participants wish to access all 
venues through multiple and inconsistent processing models, there will inevitably be a cost. 
Notwithstanding further complication created by regional inconsistencies, we can already start to 
see in Figure 2 how the number of potential process flows starts to multiply.
Inconsistencies 
in approaches 
adopted 
by venues 
inevitably cause 
disruption to a 
relatively widely 
established 
post-trade 
processing 
environment

## Page 10

ISDA Whitepaper: The Future of Derivatives Processing and Market Infrastructure
10
Figure 2. Core Process Flow Decision Tree

## Page 11

ISDA Whitepaper: The Future of Derivatives Processing and Market Infrastructure
11
2. Trade Maintenance
The existence of multiple competing infrastructures at each functional step creates myriad 
different processing flows, each with its own vagaries and nuances. On a positive note, this creates 
competition that is important for a healthy and efficient market. However, there are instances 
where there is little competitive advantage and where multiple approaches create challenges for 
market efficiency, introducing operational risk and cost to market participants. Figure 3 is a visual 
representation of how this complexity builds out.
Figure 3. The extended workflow.
Beyond the issue of workflows to support a trade through to a cleared or bilateral state, new 
regulations have also been implemented to address trade maintenance in the post-trade space. Rules 
now exist that require firms to reconcile portfolios and consider compression opportunities where 
trade portfolios are above a certain size. 
Many of these activities have a business benefit and were performed between larger market participants 
during the pre-regulatory era. Other market participants that meet the qualifying regulatory criteria 
are now faced with having to adopt industry solutions that were developed for a different user base. 
Some of these solutions may not be accessible beyond the original users due to a combination of 
cost or eligibility. In order to comply with regulatory obligations, these market participants therefore 
require their counterparties to support alternative mechanisms, which adds to the complexity and 
overheads in the post-trade space. Therefore, existing infrastructures need to consider how they can 
adjust their models to make their solutions more accessible to the broader community.

## Page 12

ISDA Whitepaper: The Future of Derivatives Processing and Market Infrastructure
12
When it comes to reconciliation, the current process model creates a continuous and duplicative 
activity that absorbs a significant amount of operational capacity within firms. Despite the fact 
that most transactions are validated through a confirmation or affirmation process shortly after 
execution, internal process and infrastructure may cause the accuracy to degenerate over time. As 
a result, downstream processes such as collateral management, reporting and settlement continue 
to experience processing breaks and mismatches of trade information. Many firms incorporate 
additional reconciliations to address these breaks, but there must be a better model. 
Collateral Management
The significant increase in the number of firms that will be in scope for delivering collateral 
to satisfy initial and variation margin requirements under new rules will place the existing 
infrastructure under considerable strain. Infrastructures are emerging with solutions to address this 
challenge, but existing solutions to some of the basic challenges facing the industry have not been 
fully adopted in some cases. 
For example, some firms and infrastructures still rely on fax for some of their business 
communication and instruction. It is concerning that electronic messaging has not yet become the 
de facto standard for business communication in some areas of the derivatives market, particularly 
given the timing requirements for certain processes under new margining regulations. There remains 
a real need for the industry to consider how the market functions and to develop principles to guide 
the development of an efficient collateral management infrastructure. This is an area where the 
ability to understand the costs of downstream processing will be particularly important at the point 
of trade, as it may influence the execution price. Simplification and standardization in this area will 
create business benefits, as well as operational efficiency.
Reporting
A further challenge relates to reporting and monitoring. Reporting was a key objective of the 
G-20’s Pittsburgh summit as a way to assist regulators in monitoring the build-up of systemic risk. 
Despite an avalanche of new requirements, it is clear that reporting objectives have not been met. 
Regulatory requirements have been inconsistently developed in different jurisdictions, making it 
impossible to get a truly global picture of this market. In fact, it is questionable whether an accurate 
picture even exists at a jurisdictional level. Reporting requirements are disconnected from the way 
many firms currently represent transactions in their systems, making it a key area that continues to 
need further collaboration between the industry and regulators.
ISDA has been leading initiatives to solve many of the reporting challenges facing market 
participants. In the past 14 months, ISDA has published key principles for improving regulatory 
transparency of global derivatives markets, co-authored a letter to regulators on key principles to 
improve global trade reporting and data harmonization and written a paper recommending global 
adoption of entity based reporting. Copies of these documents can be found on the ISDA website1
.
1 http://www2.isda.org/functional-areas/technology-infrastructure/data-and-reporting/reporting/
Some firms and 
infrastructures 
still rely on fax 
for some of 
their business 
communication 
and instruction

## Page 13

ISDA Whitepaper: The Future of Derivatives Processing and Market Infrastructure
13
THE NEED FOR CHANGE
It is evident from the previous sections that standardization, collaboration and technology are key 
drivers to building an efficient future state operating environment for derivatives.
We are aware that many market participants are assessing their roles and involvement in the 
derivatives markets, and some firms have already stepped away from less profitable areas. For 
example, some investment banks have reduced their footprint in certain asset classes, while several 
have stopped providing clearing member services for their customers in some jurisdictions. This 
is not necessarily just the result of higher operating costs, but it does play a part. As a result, it is 
unclear whether there will be enough capacity in the system to support all industry participants that 
are mandated to clear, let alone those that elect to clear for cost and efficiency reasons. Additionally, 
there may be too much risk concentrated in too few venues or critical functions, increasing concerns 
about ‘too big to fail’. 
In order for some of these firms to continue to provide the services desired by their client base and 
to remain profitable, there is a need to adopt a strategy to standardize, digitize and automate front￾to-back processes. As a further benefit, such a strategy will deliver cost and other efficiencies, as well 
as assisting firms to manage compliance and operational risk through easily retrievable audit trails. 
Industry collaboration is essential to developing this strategy, although there is unlikely to be a one￾size-fits-all approach, and this needs to be factored into any design. 
Furthermore, an appropriately designed market infrastructure and processing model can consider 
how market participants from different sectors interact with infrastructures, and promote solutions 
that accommodate their needs. For example, in the new environment of mandated clearing, market 
participants need the ability to efficiently and quickly port positions between clearing members at a 
CCP.
In recent years, the strategy for many firms has been to increase outsourcing and offshoring. This 
allowed traditional processes to be performed at lower cost, but did little to remove dependency 
on human capacity. As profit margins continue to contract, pressure to find further cost savings is 
increasing. A complete rethink of the process is needed to develop appropriate industry standards 
and facilitate adoption of advances in technology.
Firms recognize the need to review and retire redundant and duplicative internal systems, but this 
is easier said than done. As firms have made business acquisitions to increase market share over the 
years, integration of these systems has become more complicated and interdependent, and equally 
complex processing models have developed. As a result, it is not uncommon for multiple different 
platforms within a firm to support essentially similar functions across asset classes or across desks. 
Many firms continue to strive for the synchronization and integration of internal infrastructure 
and look for ways to centralize internal functions across asset classes. However, the current rapid 
change in the derivatives ecosystem is making this increasingly difficult. While it may be possible to 
leverage advances in technology and implement new systems, the reality is that many firms find it 
very difficult to decommission legacy architecture while remaining compliant with regulations. This 
is not helped by the lack of industry standards in many areas and an inconsistent or changing set 
of requirements from different global regulators, which adds to the challenge of forward planning. 
Greater collaboration between market participants, infrastructures and regulators could help solve 
this challenge and provide greater benefit to the industry as a whole. 
In order 
for some of 
these firms 
to continue 
to provide 
the services 
desired by their 
client base 
and to remain 
profitable, there 
is a need to 
adopt a strategy 
to standardize, 
digitize and 
automate 
front-to-back 
processes

## Page 14

ISDA Whitepaper: The Future of Derivatives Processing and Market Infrastructure
14
Furthermore, the sheer pace of regulatory implementation and a limited capacity, both human and 
financial, to take stock, re-engineer and implement changes have caused many market participants 
to build tactical solutions to their immediate problems. This is not sustainable and, in addition to 
being costly, there is a nervousness that the resulting ecosystem is not sufficiently robust to support 
the industry in times of stress. Indeed, there appears to be insufficient understanding of the risks of 
contagion from the failure of a single market infrastructure within the new operating environment. 
The current state has become a complex set of interdependent systems (internal and external) that 
require a significant amount of hybrid domain and technical expertise in order to be maintained. 
Furthermore, integrating these systems with one another as the market evolves poses a considerable 
challenge. 
Strategic investments and large-scale in-house initiatives to overhaul infrastructure are difficult to 
justify while the future remains so unpredictable. Some market participants have proven to be more 
nimble and better at adjusting than others – possibly a function of less legacy and interconnected 
infrastructure. However, there is a growing desire from industry participants for a coordinated 
approach to solving these problems to ensure that focus and investment is appropriately defined and 
targeted and delivers cross-industry benefits without disrupting business as usual.
In addition to market participants being faced with rising costs in an environment where profit 
margins are on the wane, existing infrastructures are being presented with similar challenges. There 
is currently an erosion of volume flow through these infrastructures as a result of the emergence 
of alternative processes. Infrastructures are re-evaluating, taking into account market structure 
changes, and determining how they fit into the new environment. New infrastructures and solution 
providers are appearing, while new and disruptive technologies are getting significant airtime.
The answer is not just about speed and the replacement of existing processes with faster solutions. It 
is about reviewing and possibly re-engineering the whole post-trade process. This need, combined 
with the emergence of new and potentially disruptive technologies, presents an opportunity to 
reshape the future state of the derivatives processing environment. This needs to be a collaborative 
effort on the part of both market participants and regulators. It is not simply a case of ‘out with the 
old and in with the new’. The market, in the meantime, still needs to function effectively and the 
change needs to be coordinated. 
Individual market participants may have differing priorities – for instance, whether to collaborate 
on certain activities or retain processes in-house. Existing external activities may be riper for 
collaboration, whereas firms may be more sensitive about collaborating on initiatives that are 
currently performed internally, as they may believe they have a competitive advantage. As a 
result, implementation may be gradual, with different market participants adopting the changes 
at their own pace and perhaps, in some cases, not at all. Therefore, any new ecosystem needs to 
support interoperability between old and new systems and processes. A common view on how the 
ecosystem should operate will assist firms to make an informed decision and implement accordingly. 
Furthermore, it is imperative that, as the environment changes, there is sufficient capacity to 
support a safe and efficient market while new technologies and processes are being introduced.
The current 
state has 
become a 
complex set of 
interdependent 
systems

## Page 15

ISDA Whitepaper: The Future of Derivatives Processing and Market Infrastructure
15
THE FUTURE – OPPORTUNITIES FOR TECHNOLOGY 
AND STANDARDIZATION
The derivatives industry is complex, with many variations of product and market participant. Many 
of the challenges described in the previous sections could be alleviated by the existence of greater 
standardization on data and processing, but reaching common standards can be a slow and arduous 
process. The lack of a coordinated approach with clearly defined, unbiased objectives is at the heart 
of these challenges, as the industry’s limited resources are not always focused on developing and 
delivering common solutions. The result is that unnecessary complexity is introduced, and this is 
exacerbated by the inconsistent application of regulation. 
Technology, utilities and managed services can revolutionize this industry and the financial services 
sector as a whole. ISDA believes it is time for market participants to take stock and consider the 
opportunities to create a safer and more efficient market infrastructure, given i) the technical build 
required to meet upcoming regulations, such as MIFID II and margining requirements for non￾cleared derivatives; ii) the challenges resulting from recent regulatory implementation, such as the 
Dodd-Frank Act and European Market Infrastructure Regulation (EMIR); and iii) the urgent need 
to improve efficiency, and reduce cost and operational risk within the derivatives industry. It is vital 
that the industry as a whole recognizes this, and commits to a concerted and coordinated effort to 
develop and implement more efficient processes
As part of this process, ISDA’s members have identified three key contributors to evolving and 
improving the derivatives ecosystem – standardization, collaboration and technology. 
Standardization
Standardization takes many forms, covering product definitions, process descriptions, legal 
documentation, messaging and terminology. ISDA has long been at the forefront of publishing and 
promoting legal documentation standards, from the ISDA Master Agreement and CSAs to definitional 
booklets and confirmation templates. Digitizing this suite of documentation can facilitate industry 
evolution into a more electronically interconnected and efficient environment. On the process side, 
market practice statements and principles papers based on broad consensus have helped keep the industry 
coordinated. Standards in all forms help to create a platform for technology to evolve within an ecosystem.
One area where greater standardization is particularly needed is collateral management. The 
margining of non-cleared derivatives transactions will pose significant challenges to the industry, 
and there are numerous opportunities for standardization. ISDA’s various collateral committees 
have long championed improvements in this area and, as the first wave of margining rules come 
into effect, market participants in these committees are already identifying opportunities for further 
work. Among these are opportunities to develop standard account control agreements (ACAs), 
publication of eligible collateral matrices, netting of swap obligations with collateral cash flows 
and segregation account standards for bilateral margin. All of these need further exploration to 
determine feasibility, but they indicate just some of the opportunities. As part of a bigger exercise, 
it would be valuable for industry stakeholders from all backgrounds to focus on an initiative to 
propose an optimum future state processing model for this activity. 
Looking ahead, there are clear opportunities for further standardization that will help to address 
some of the challenges highlighted in this paper, and these can be categorized in three key areas: 
data, documentation and process.
The lack of a 
coordinated 
approach with 
clearly defined, 
unbiased 
objectives is 
at the heart 
of these 
challenges

## Page 16

ISDA Whitepaper: The Future of Derivatives Processing and Market Infrastructure
16
1. Data
Data standards are a fundamental element of developing an efficient future state model where 
multiple participants interact with one another. They facilitate easier integration of solutions and 
promote interoperability. Data representation, naming conventions and formats are all critical in 
this regard, and it is vital that these are developed in a globally consistent manner for derivatives 
markets. In addition, product identifiers and trade identifiers are key elements of regulatory 
requirements, and the industry needs them to be globally consistent. Combined, these two 
identifiers provide an opportunity to revolutionize the way markets operate today. 
Product Identifiers
A consistent global product identifier, if designed and implemented correctly, can drive significant 
efficiency across the entire trade lifecycle by creating a common reference for a product that can be 
leveraged by various market participants, infrastructures and processes. The product identifier would 
be a major step on the path to regulatory reporting and harmonization, and facilitate supervisory 
aggregation of derivatives trade data across borders. There are many other use cases to which an 
appropriately designed product identifier can be applied – for example, product categorization to 
aid compliance with various regulatory obligations (eg, ToTV), and various post-trade activities, 
including trade confirmation, reconciliation and compression, by removing the number of data 
fields that need to match for these processes to be successful. The challenge for the industry, 
working in collaboration with global regulators, is to identify or design a product identifier that 
meets the criteria necessary for each of these use cases.
It should not just be a case of designing a product identifier for multi-purposes. Serious 
consideration needs to be given to how such a product identifier is generated and published in order 
to be effective and useful. It is critical that it is freely open and accessible to all, as this will promote 
further innovation and process improvement.
ISDA is at the forefront of efforts to design a suitable product identifier for derivatives products. In 
2011, ISDA commenced work on defining product taxonomies for derivatives products, publishing 
a first iteration of taxonomies for cross-jurisdictional reporting in credit, interest rates, equity, 
commodities and FX on March 1, 2011. While these taxonomies have helped solve a number of 
reporting issues, the industry still strives for a globally consistent product identifier that is supported 
by regulators. 
While the initiative to find a suitable product identifier continues, ISDA has published a document 
that sets out four key principles that should form the basis of any global product identifier 
construct2
. These principles cover: i) appropriate granularity; ii) open governance; iii) open source 
data and competitive market infrastructure; and iv) business usage and post-trade adaptability. 
In addition, there is a desire for the development of standard naming conventions and associated 
definitions for package transactions. Implementation of new regulations, particularly with regards to 
the application of trading obligations and STP, have caused many challenges for market participants. 
A clear definition and means of identifying packages could address this challenge and also perhaps 
introduce efficiencies for other post-trade activities, such as confirmation and reporting. 
2 See Principles on the Development of Derivative Product Identifiers, ISDA, May 23, 2016: at http://www2.isda.org/functional-areas/technology￾infrastructure/data-and-reporting/identifiers/upi-and-taxonomies/
A consistent 
global product 
identifier, if 
designed and 
implemented 
correctly, can 
drive significant 
efficiency 
across the 
entire trade 
lifecycle

## Page 17

ISDA Whitepaper: The Future of Derivatives Processing and Market Infrastructure
17
Trade Identifiers
Trade identifiers that are globally unique to a specific transaction are an essential tool for identifying 
a trade between counterparties and across different jurisdictions throughout the trade lifecycle. 
Although required for transaction reporting, unique trade identifiers (UTIs) are a valuable reference 
tool for other regulatory requirements, such as portfolio reconciliation, as well as for non-regulatory 
internal and bilateral post-trade reconciliation, communication and processes. The availability of a 
UTI in all cases facilitates communication regarding the relevant transaction and resolution of any 
related issues (eg, confirmation discrepancies) by allowing the parties to refer to a single, mutually 
understood transaction identifier, rather than having to exchange transaction details or their 
respective internal trade identifiers.
ISDA was an early advocate of the value that would be derived from consistent use and application 
of a trade identifier, initially working with industry participants to develop practices pertaining 
to use of the CFTC’s unique swap identifiers. ISDA anticipated the necessity of a global trade 
identifier (rather than jurisdictional ones), and encouraged regulators to adopt an approach to 
creating a UTI value that would be globally extensible. In the absence of a UTI standard endorsed 
by global regulators, ISDA worked with its members and the broader OTC derivatives industry 
to develop an approach to the generation, communication and matching of UTIs . ISDA’s UTI 
standard has been widely implemented and used by market participants to meet their regulatory 
reporting requirements and has been accepted by various regulators globally. 
Through the Committee on Payments and Market Infrastructures (CPMI) and the International 
Organization of Securities Commissions (IOSCO), global regulators are working to establish 
recommendations for UTIs. ISDA supports this work, and has led industry feedback on the relevant 
consultations. A global approach for UTIs and their universal adoption is not only essential to 
meaningful global data aggregation and analysis, but also has the potential to improve the efficiency 
and accuracy of front-to-back trade processing and reconciliation.
2. Documentation
Further opportunities for standardization exist in the area of pre-trade, particularly with regards to 
the negotiation of CSAs. As noted earlier, many firms are struggling to manage the complexity of 
processing relationships due to the historical negotiation of bespoke documentation. While many 
of these legacy clauses may have been appropriate when they were negotiated, they may no longer 
deliver the perceived benefits due to the changing regulatory environment and the significant 
burden of managing these bespoke elements. 
Market participants should seriously consider the benefits of their bespoke forms of documentation 
versus further standardization, particularly given the need for review and in some case replacement 
of these documents as a result of new regulations on margin for non-cleared derivatives. ISDA 
can assist the industry in reaching agreement on more appropriate levels of standardization and 
incorporate these into new versions of relationship documentation. Even agreeing to restrict 
negotiation of these documents to certain standard elections could represent a big step forward. 
Solutions can be developed to help market participants electronically agree and store this 
information upfront in an easily accessible form. 
Although 
required for 
transaction 
reporting, 
unique trade 
identifiers 
(UTIs) are 
a valuable 
reference 
tool for other 
regulatory 
requirements

## Page 18

ISDA Whitepaper: The Future of Derivatives Processing and Market Infrastructure
18
3. Process
ISDA believes there is a need for industry agreement on the process, behaviors and data 
elements of the derivatives market. The current derivatives ecosystem consists of a complex set 
of interdependent, duplicative systems and processes with inconsistent operating rules. This 
has evolved as a rapid and often tactical response to the demands of new regulation. There is a 
significant opportunity for simplification of these processes, including a potential re-ordering of the 
workflow that would facilitate a safer and more efficient market. However, the industry needs to be 
mindful not to create new single points of failure or, at a minimum, to recognize critical functions 
and build in fallback or safety mechanisms as part of the overall design. 
It is important that the industry collectively pursues this objective, agrees on and collaborates 
to define the most efficient market operating models. Once agreed, these processes should be 
technically encoded as common domain models (or CDMs) that systematically reflect how the 
market operates, from pre-trade to books and records, by describing the necessary data, functions 
and participants of the derivatives market and how each interacts with each other to deliver the 
desired outcomes for various stakeholders. 
Views on these CDMs can then be leveraged for regulatory reporting, eligibility, interfaces and any 
other data-driven use cases within the market, such as where data is passed between organizations. 
In ISDA’s view, CDMs can only be successful if they are used to drive trade execution within the 
market, not just for reporting purposes. This helps to ensure they are kept in line with current 
market practices and can facilitate common agreement on how changes to the ecosystem will impact 
market participants (eg, the introduction of SIs under MIFID II). 
It is therefore important that CDMs are interoperable with some of the existing standards (eg, 
Financial products Markup Language, or FpML) and, to the extent possible, are consistent across 
asset classes. This would require appropriate levels of continuing governance and direction from 
the various stakeholders, and it would also necessitate a sponsor to publish and maintain a library 
of CDMs. To realize these benefits, as well as unambiguously describe data, a CDM should be a 
technical artefact – in other words, machine readable and containing semantics that are able to be 
enforced using validation. Furthermore, regulators and the industry as a whole would benefit if 
future rules and technical standards referenced current CDMs.
The broader benefits of CDMs with integrated data standards will be to allow the industry to evolve 
further. These concepts facilitate increased interoperability, which in turn could create opportunities 
for market-wide utilities to emerge, either as new standalone entities or from an aggregation of 
existing infrastructures. One example of this could be in the area of settlements. Currently, firms 
invest significant effort in reconciling cash flows, agreeing settlement instructions, making payments 
and addressing settlement breaks. These processes are currently all managed independently, 
although potentially by the same functional area within a firm. Developing a utility to connect all of 
these activities could provide the industry with significant efficiency and cost reduction and could 
reduce settlement risk. Alternatively, the industry could consider adopting outsourced services that 
perform all lifecycle events directly onto transactions. This could include cash flow generation and 
settlement, rate setting, market disruption and credit-event adjustments.
Interoperability will assist the industry to unpick the complicated maze of work flows that exist 
today. For example, the STP rules are proving to be particularly challenging to implement. Some 
firms want trades to be sent directly to clearing by the execution venue, whereas others prefer to 
leverage existing middleware for this purpose in order to benefit from the additional services that 
middleware may provide. These two approaches are proving to be incompatible and are therefore 
preventing firms from independently selecting the process flow that best suits their needs. 
ISDA believes 
there is a need 
for industry 
agreement on 
the process, 
behaviors 
and data 
elements of 
the derivatives 
market

## Page 19

ISDA Whitepaper: The Future of Derivatives Processing and Market Infrastructure
19
The lack of a coordinated approach is making resolution of this issue particularly slow and 
painful. Firms had to build specific tactical solutions to comply with CFTC requirements to send 
transactions to a clearing house within 10 minutes from August 1, 2016. However, MIFID II 
sets an even more aggressive time frame for electronically executed transactions, which is unlikely 
to be achievable using these tactical solutions. If the industry is able to agree certain process and 
messaging standards, then this challenge could be addressed more effectively. This could also provide 
market participants with the choice of process based on their own requirements, rather than those 
of their counterparties or venues, reducing the need for firms to support multiple process flows.
The initiative to develop pre-trade credit checking principles is a good example of where industry 
associations have previously facilitated discussion among market participants to establish a processing 
standard for a critical function. A similar coordinated approach would be helpful to solving the STP 
challenges, but it does require all relevant participants to agree on and embrace the objective. 
An added benefit of process standardization should be to provide infrastructures with the 
opportunity to enter and exit the market without causing undue disruption to existing participants, 
allowing new infrastructures to bring ideas and efficiencies to the ecosystem. 
Figure 4 illustrates this interoperability, where infrastructures building to a CDM and utilizing 
standard messaging formats can interact with each other. These infrastructures are still able to 
differentiate themselves on their core business, and market participants remain free to select the 
infrastructure(s) that best meet their needs, but this will no longer have to support multiple nuances 
of essentially the same workflow. As illustrated in the bottom right corner, infrastructures within a 
function may gather into a market utility to further enhance their offering.
Figure 4. Opportunities for Interoperability

## Page 20

ISDA Whitepaper: The Future of Derivatives Processing and Market Infrastructure
20
Collaboration
In response to new regulations, many firms individually build and maintain the same functional 
solutions, particularly in post-trade activities. Through mutualizing the build of common 
requirements, technology can drive operating efficiency. This allows firms to focus on their core 
market facilitation and risk management roles. 
Furthermore, leveraging cloud technology could deliver immediate cost benefits when it comes 
to maintaining hardware associated with certain activities. Where market participants are able to 
interact externally on a process hosted by an external infrastructure, they can potentially reduce 
server requirements within their respective organizations. There may be challenges with franchise 
and data security, and concerns about balancing the outsource versus intellectual property, but it 
should be possible to address these when weighed against the ongoing costs of each firm supporting 
and warehousing expensive hardware. 
A similar opportunity may exist in the reporting arena, where multiple repositories currently store 
the same information on local databases. This is proving to be extremely costly, and this cost is 
inevitably transferred to market participants. There could be opportunities for these repositories to 
collaborate and store information on a single database that is secure but mutually accessible.
While collaboration on infrastructure is important and can deliver significant cost benefits, 
there may be some limitations. Firms will need to consider the balance between developing and 
maintaining their own solutions versus buying or subscribing to an external solution. Individual 
market participants may have particular preferences, but if the solutions can be developed according 
to commonly agreed models and processing standards, then there should be an opportunity for each 
firm to choose and adopt a tailored front-to-back solution that does not restrict or create additional 
cost layers for other market participants.
As the industry ecosystem evolves and solutions to problems are developed, it is extremely 
important to consider the applicability of these solutions to all market participants. Solutions 
developed in specific segments of the market are not always well-adopted by smaller or less 
sophisticated market participants. Engaging with these market participants at an early stage, either 
directly or through their representatives, would enable solutions to be developed that are capable of 
being extended to the broader community.
It is imperative that collaboration occurs across the market and with regulators to ensure that 
models are consistent with business and regulatory expectations. Collaboration within business is 
not a new concept and has provided real benefit to market participants over recent years through 
initiatives such as the Trade Information Warehouse (TIW), as well as the development of standard 
forms of documentation published by ISDA. Parallels can be drawn with other industries, such 
as manufacturing, where collaboration throughout the supply chain has boosted production and 
increased the rate of product development – and ultimately increased the profitability of the 
collaborating firms. The key is to have agreement on the objectives of the collaboration from the 
outset. It should focus on areas of mutual benefit where there is no competitive advantage. Firms 
should take responsibility to ensure they understand the benefits and the risks.
Firms will need 
to consider 
the balance 
between 
developing and 
maintaining 
their own 
solutions 
versus buying 
or subscribing 
to an external 
solution

## Page 21

ISDA Whitepaper: The Future of Derivatives Processing and Market Infrastructure
21
ISDA’s working groups will continue to provide a platform from which broad market collaboration 
can occur. These forums will explore opportunities to standardize and streamline operational 
processes and improve critical infrastructures for the benefit of all market participants. Helping 
the market to implement the MIFID II STP requirements by leveraging the experience of market 
participants implementing the similar requirement under CFTC rules is a good example of how 
ISDA’s senior infrastructure committee can help focus the collective industry resource. 
Technology
1. Regulatory Technology (RegTech)
ISDA believes there is an opportunity for the regulatory and industry communities to develop a 
collective RegTech strategy. 
In our view, the term ‘RegTech’ is meant to encompass common technical artefacts that provide 
mutual benefit to both regulators and market participants in complying with regulations. These 
artefacts can be split into two parts: software and standards. Standards were covered in the 
preceding section, but initiatives such as the adoption of legal entity identifiers (LEIs) are another 
good targeted example. The software delivered as part of RegTech can be run as traditional utilities 
or managed services (software as a service) using cloud technology. 
This section highlights some further examples of RegTech opportunities. 
Most regulatory compliance begins with an eligibility calculation of some type. Eligibility decisions 
have an acute dependency on the input data. To achieve uniform compliance, the eligibility models, 
reference data and transaction data inputs should, in theory, share a common understanding. 
At present, many firms source and scrub the same reference data – for example, data regarding 
representations on clearing categories under EMIR – duplicating effort and potentially leading to 
inconsistencies. This reference data is used heavily in regulatory eligibility decisions and reporting. 
There are already examples of utilities helping firms with product and client reference data 
scrubbing. Ideally, this concept could be advanced further with CDMs enforcing a consistent 
interpretation of data used for these calculations. Common regulatory eligibility models that 
effectively encode a consistent interpretation of rule eligibility could also provide significant 
additional benefits – this reference data, if digitized, centrally stored and accessible, could be used 
by other infrastructures (eg, trading platforms), subject to appropriate permission, to assist routing 
of transactions through the process.
MIFID II is a good use case. The main technology challenge with the reporting requirements 
contained within MIFID II relates to interpretation of data. There are product and organizational 
nuances with derivatives contracts that make common understanding of data challenging. When 
analyzing public data on interest rate swaps, it is important to have agreement on a number of non￾core product attributes, such as business day conventions, to be able to compare prices accurately. 
By referencing common models within a regulatory text, regulators can then have a greater degree of 
confidence about common interpretation and compliance with rules. This would particularly help 
in the case of MIFID II, as transparency can only be effective if there is a mutual understanding of 
the data being made transparent. 
Most regulatory 
compliance 
begins with 
an eligibility 
calculation of 
some type

## Page 22

ISDA Whitepaper: The Future of Derivatives Processing and Market Infrastructure
22
A further challenge may result from the fact that the derivatives market is global. So, for this 
initiative to be truly successful, it will need the buy-in of the global regulatory community to 
develop consistent regulatory nomenclature. This could be achieved through CPMI-IOSCO. 
Software providers will have various roles to play in the RegTech space. As well as providing utility 
solutions to aid compliance (eg, reference data scrubbing), providers can also help both regulators 
and market participants understand the quantum of data that will be produced as a result of 
regulation. In order to accelerate innovation in this space, software providers can extend and 
leverage CDMs as per their use cases. Having CDMs underlying data interfaces between software 
producers and consumers can encourage competition within the RegTech space, resulting in a 
healthy utility market.
All this should coalesce to reduce the time it takes firms to fully comply with rules once they are 
finalized. It is important to distinguish between the two types of technical standards often referred 
to: regulatory technical standards published by regulators; and the technical specifications (usually 
for data) used for technical compliance. The use of a CDM should provide a mechanism for the 
latter, meaning regulators could make adjustments directly to the model in order to achieve the 
desired outcome, without having to make changes to the regulation.
Finally, it is important to note that leveraging RegTech for parts of regulatory compliance carries 
some risks. Unlike software or standards, accountability for complying with regulations cannot be 
transferred to a third party. Therefore, non-functional requirements on governance, testing and 
stability are key to any solutions in this space.
2. Financial Technology and Distributed Ledger Technology 
Beyond RegTech, there are opportunities for the broader financial technology (FinTech) community 
to drive efficiencies and cost reduction. Many FinTech companies are emerging across capital 
markets. Unfortunately, these companies do not necessarily succeed or fail based on the quality of 
their product, but on their ability to penetrate their target audience. 
With so many companies vying for attention, obtaining quality airtime can be difficult. But, many 
of the building blocks for RegTech described in the previous section apply equally to FinTech and 
can be helpful in this regard. Standardization is a core facilitator to both RegTech and FinTech, and 
reaching industry agreement on CDMs will provide all of these technologies with a centrally agreed 
place from which to develop their solutions. This is particularly important given the likelihood that 
market participants will require these technologies to interoperate in a global ecosystem in order to 
avoid a new disconnected global infrastructure that replicates the core issue of today. 
Of particular interest in the FinTech space may be the opportunities for blockchain or distributed 
ledger technology (DLT). DLT is currently gaining a significant amount of attention, and many 
traditional market participants are collaborating and gathering around this technology, either 
through involvement in consortiums and/or exploring their own initiatives internally. Regulators 
around the globe are taking an interest – although, in many cases, they are appropriately limiting 
their involvement to monitoring developments rather than regulating activity. If DLT does take a 
more prominent role in the derivatives ecosystem, or in capital markets more broadly, there may be 
a requirement for regulators to reconsider some of their existing regulation. Therefore, collaboration 
between regulators and industry participants will be an important element of any deployment in 
this field. 
Standardization 
is a core 
facilitator to 
both RegTech 
and FinTech

## Page 23

ISDA Whitepaper: The Future of Derivatives Processing and Market Infrastructure
23
Either way, there have recently been announcements from a number of DLT providers that have 
developed and successfully completed test use cases for derivatives transactions. These would 
appear to be very small scale at this time, but it nevertheless indicates there is an opportunity for 
this technology to be deployed in the derivatives market. There are likely to be multiple ledgers 
in existence across the financial markets, and potentially within the derivatives market alone. 
It is therefore critical that the industry learns from experience and ensures that this technology 
is delivered in an interoperable form. It may be that related parts of a derivatives process exist 
on different ledgers – for example, collateral management may exist on one ledger and trade 
performance on another. To be unable to connect these ledgers seamlessly would be a significant 
missed opportunity.
The development of smart contracts is a potential further application of this technology within the 
derivatives market. As a publisher of industry agreed standards for derivatives products, ISDA can 
play a key role in the development and publication of these contracts in a standard form that can 
potentially be used across multiple ledgers. Indeed, much of the work already undertaken by ISDA 
to develop standard forms of documentation, including definitional booklets and confirmation 
templates, coupled with FpML, has the potential to form the basis of these smart contracts. 
Furthermore, it enables the industry to leverage a robust legal architecture with which industry 
participants are familiar and helps to reduce development time and investment costs. The existing 
FpML templates can be extended to include business logic that creates a self-executing transaction. 
Such transactions would need little in the way of manual input after execution, provided the 
industry could agree on the required process model and identify the sources of any inputs. However, 
considerably more work is required in this area to determine the feasibility of this approach.
In the absence of smart contracts, or perhaps as a precursor, the industry could benefit significantly 
from developing a processing model that operates on the basis of a single representation of a 
transaction, or ‘Golden Record’. If structured correctly, this Golden Record may remove the 
need for many of the duplicative reconciliation processes that exist today, such as reconciliation 
for settlement, compression and margining purposes. More importantly, it will assist market 
participants and regulators to access an accurate and up-to-date instance of a transaction at any 
time, potentially removing or reducing some of the current burdens of regulatory reporting. 
In order for this Golden Record to have maximum impact, it is imperative that the industry 
establishes a mechanism to designate the record as ‘gold’ as early in the trade lifecycle as possible 
to allow as many post-trade activities as possible to leverage this record and rely on it as definitive. 
This record could aggregate with other data elements extracted from other data digitization activities 
(eg, electronically created relationship documentation) to form a central data store that provides 
sufficient information to allow additional post-trade activities (eg, collateral management) to be 
performed by solution providers and infrastructures. Figure 5 builds on Figure 4 to demonstrate 
how this could look.
The industry 
could benefit 
significantly 
from developing 
a processing 
model that 
operates on the 
basis of a single 
representation 
of a transaction
3 A smart contract is an agreement whose execution is both automatable and enforceable. Automatable by computer, although some parts may require 
human input and control. Enforceable by either legal enforcement of rights and obligations or tamper-proof execution.” Smart Contract Templates: 
foundations, design landscape and research directions, http://arxiv.org/abs/1608.00771

## Page 24

ISDA Whitepaper: The Future of Derivatives Processing and Market Infrastructure
24
Figure 5. The Golden Record

## Page 25

ISDA Whitepaper: The Future of Derivatives Processing and Market Infrastructure
25
CONCLUSION
This report describes some of the challenges that the industry faces, and touches on a number of 
core building blocks that will help the derivatives market migrate to a safer and more efficient 
operating environment while complying with regulatory obligations. 
As implementation of global regulation continues, the challenges for the industry are numerous. 
New technologies are available to help provide solutions, and market participants should take the 
opportunity to consider and embrace these technologies where appropriate. These should draw on 
the experience of market participants and how the market does or should operate, without stifling 
innovation. 
Furthermore, we should take the opportunity to identify and develop further standards that 
facilitate greater efficiency throughout the ecosystem. There is an opportunity for regulators and 
the industry to collaborate to commit, plan and execute on the core building blocks identified in 
this report. The benefit of having an open-source repository for financial services to assist with this 
collaboration is clear. As well as housing CDMs, this repository could also contain artefacts such 
as eligibility models or core software that is tailored more towards financial services than general 
technical uses. 
However, this requires thought leadership, direction and oversight. ISDA’s Market Infrastructure 
and Technology Oversight Committee (MITOC) will provide a forum for this to happen, and will 
collaborate with other interested parties as necessary. We believe that a strong coordinated effort 
should enable the global derivatives industry to realize the following benefits:
• Greater operating efficiency for all market participants through mutualizing common technical 
builds, increased standardization and process simplification; 
• More consistent compliance through a common understanding of data and decision models 
between regulators and market participants;
• Increased quality of data for regulatory and non-regulatory purposes by using models containing 
semantics that restrict use of certain data fields based on inherent criteria;
• More effective transparency of data, helping to achieve some of the core aims of regulations such 
as MIFID II;
• An environment that encourages innovation and competition and promotes the use of 
technology, lowering barriers to entry for FinTech and RegTech;
• A potential for a shorter time to market between rule finalization and technical compliance;
• Removal and consolidation of redundant and duplicative processes. 
There is an 
opportunity for 
regulators and 
the industry to 
collaborate

## Page 26

ISDA Whitepaper: The Future of Derivatives Processing and Market Infrastructure
26
NEXT STEPS
Identify and track solutions to current post-trade inefficiencies
By the end of 2016, ISDA will work with the industry to perform an assessment of current post￾trade infrastructure and processes to expose inefficiencies and develop a mechanism to assist 
members in identifying, prioritizing and developing near-term solutions. ISDA will leverage its 
existing working group structure, under the direction of MITOC, to facilitate this exercise which 
will enable market participants to allocate resources more efficiently and to prioritize key issues.
Develop common domain models
ISDA will also coordinate the development of a plan for the creation of common domain models 
for the derivatives market by the end of 2016. The plan should identify and prioritize the necessary 
models required to deliver safe and efficient derivatives markets. ISDA’s MITOC will oversee 
this initiative and liaise with regulators to identify the earliest possible use cases of these models 
from both a regulatory and commercial standpoint, as well as how they may be used to support 
publication of future rules and technical standards.
Promote open source
MITOC will work with industry stakeholders to identify a venue that can be tasked with creating 
an open-source repository (or repositories) for required artefacts, as described earlier in this paper. 
The roadmap for these repositories, roles and responsibilities and basic principles should be 
agreed and circulated by the end 2016. Specific discussion should also take place on what role the 
regulators and the industry should play with regards to the repositories, as they should all benefit 
from some of the artefacts housed within them (eg, common domain models).
Facilitate industry collaboration and communication
ISDA will collaborate with other trade associations to coordinate and promote the above initiatives 
and, in particular, explore opportunities to leverage advances in technology. This should provide a 
coordinated mechanism for solution providers to discuss and identify opportunities (and gaps) with 
market participants. In addition, this should facilitate synchronized broadcast of events that may 
have an impact on market participants and infrastructures, and enable the industry to coordinate 
efficient responses to these events. This collaborative arrangement should also be used to ensure that 
respective organizations are focused on their specific areas of expertise and reduce the burden on 
market participants to contribute to multiple similar discussions.
