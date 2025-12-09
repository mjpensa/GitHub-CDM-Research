# Collateral and Liquidity Efficiency in the Derivatives Market

*Converted from: Collateral-and-Liquidity-Efficiency-in-the-Derivatives-Market.pdf*

---

## Page 1

Collateral and 
Liquidity Efficiency in 
the Derivatives Market:
Navigating Risk in a 
Fragile Ecosystem
MAY 2025

## Page 2

02
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
CONTENTS
Executive Summary.................................................................... 03
1. Introduction............................................................................. 05
1.1 From Risk Mitigation to Systemic Vulnerability ............................. 05
1.2 A Structural Trilemma: Market, Credit and Liquidity Risks............... 06
1.3 A Fragmented Infrastructure in an Interconnected World............. 07
1.4 Strengthening the Foundations of Financial Stability................... 08
2. Collateral Optimization: From Pain Points to Solutions.......... 09
2.1 Cost of Collateral ................................................................... 09
2.2 Optimizing Collateral Selection and Allocation .......................... 10
2.3 Repo and Financing Markets................................................... 12
2.4 Considerations for Cleared Activity and Cross-product Margining ..14
2.5 Collateral Efficiencies and Data Management........................... 15
2.6 Conclusion............................................................................ 17
3. Expanding the Collateral Liquidity Pool................................. 18
3.1 Collateral Eligibility in the Derivatives Market.............................. 18
3.2 Stress Events .......................................................................... 24
3.3 Conclusion............................................................................ 27
4. Using Technology to Support Optimization and Resilience....28
4.1 Building a New Collateral Management Architecture ................. 28
4.2 Tokenization: Expanding and Mobilizing the Collateral Pool ......... 29
4.3 Agentic AI: Autonomous Optimization of Collateral Processes ...... 30
4.4 Short-term Efficiency Fixes While DLT Matures.............................. 31
4.5 Conclusions .......................................................................... 32
5. Conclusion.............................................................................. 33
6. Appendix: List of Contributors ................................................ 36

## Page 3

03
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
EXECUTIVE SUMMARY 
Central clearing and margining of non-cleared derivatives have contributed to a significant reduction 
in counterparty credit risk. However, delays and inefficiencies in sourcing and posting collateral can 
quickly lead to increased liquidity risk, particularly during periods of stress. Persistent inefficiencies 
risk cascading liquidity crises, undermining the post-crisis reforms that were designed to curb 
systemic risk. Current market conditions, including quantitative tightening, geopolitical tensions 
and the continued implementation of non-cleared margin rules, demand urgent action.
Recent stress events – including the 2020 dash for cash, energy market volatility and the 2022 
UK gilt market crisis – have exposed critical weaknesses in collateral frameworks, threatening 
financial stability. The market faces three main challenges: the need for cost reduction, liquidity 
improvement and efficient operations. The ‘risk triangle’ – market risk, counterparty credit risk 
and liquidity risk – frames all these challenges. Each of these elements must be considered in the 
context of the fragmented market, with diverse players seeking different solutions.
This whitepaper, developed by the 2024/2025 cohort of the ISDA Future Leaders in Derivatives 
(IFLD) program, examines the growing challenges of collateral efficiency and liquidity resilience in 
the global derivatives market. The paper addresses issues driven by regulatory complexity, market 
fragmentation and systemic vulnerabilities. It outlines practical strategies to address these issues, 
balancing the costs of collateral, risk management, regulatory compliance and technological innovation.
• Optimizing Use of Collateral 
Market participants should consider their collateral optimization strategies to maximize the 
use of available assets while reducing margin inefficiencies, improving funding flexibility 
and managing costs. This includes active portfolio rebalancing, leveraging repurchase and 
other financing markets to free up liquidity, expansion of cross-product margining at central 
counterparties (CCPs), consolidation of collateral governance functions and expanded adoption 
of technology across both product and CCP margining frameworks.
• Expanding and Diversifying the Eligible Collateral Pool
To address systemic liquidity risk, the financial industry must broaden the universe of eligible 
collateral beyond traditional high-quality liquid assets (HQLA). Other forms of collateral 
should be considered, such as money market funds (MMFs), guarantees, commercial paper 
(CP) and emissions certificates, alongside the development of robust valuation, legal and 
operational frameworks to support their inclusion. 
• Modernizing Infrastructure through Technology
Technology will play a pivotal role in enhancing collateral transparency, mobility and efficiency. 
Distributed ledger technology (DLT) can enable near real-time settlement. The Common 
Domain Model (CDM) provides consistent data standards across systems. Additionally, agentic 
artificial intelligence (AI) has the potential to automate dispute resolution, stress testing and 
predictive liquidity management. Cross-chain interoperability and tokenized asset networks offer 
new avenues for collateral portability, provided legal and operational risks are carefully managed.
This whitepaper also introduces a contingency framework for market-wide stress events, 
recommending mechanisms such as a ‘stress event protocol’ for automatic expansion of eligible 
collateral schedules during systemic liquidity crunches. The protocol would allow pre-elected 
collateral types to become exchangeable between consenting parties during periods of market-wide 
dislocation, reducing the need for emergency policy intervention and mitigating procyclicality in 
margin frameworks.

## Page 4

04
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
By optimizing existing collateral processes through cross-sector collaboration, exploring new 
potential sources of eligible collateral and investing in new and improved technologies like 
DLT and the CDM, market participants can reduce funding costs, mitigate operational risks 
and enhance financial stability. These measures seek to address current pain points and lay the 
foundations for a more adaptive and harmonized derivatives market, which can withstand future 
shocks while maintaining its global integrity.

## Page 5

05
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
1. INTRODUCTION
1.1 From Risk Mitigation to Systemic Vulnerability
The global over-the-counter (OTC) derivatives market, including cleared and non-cleared contracts, is 
a central pillar of the modern financial system, facilitating risk transfer, price formation and liquidity 
provision across virtually all asset classes and economic sectors. With a notional value of $729.8 trillion 
as of June 30, 20241
, OTC derivatives are instrumental in supporting the functioning of bond markets, 
commodity supply chains, corporate risk management and institutional asset allocation. 
Collateral and liquidity frameworks underpin the functioning of this key market. Counterparties 
post collateral to mitigate credit exposure in derivatives contracts. Collateral typically takes two 
forms: initial margin (IM) and variation margin (VM). Parties post IM at the outset of a trade to 
cover potential future exposure over a predefined liquidation period, and this IM is generally held in 
segregated accounts to prevent re-use. Parties exchange VM on a daily or intraday basis to reflect the 
current mark-to-market value of open positions and protect against losses that have already occurred. 
Cleared VM is always posted in cash and non-cleared VM is predominantly posted in cash and 
subject to strict same-day settlement requirements. Cleared IM frameworks allow for a broader set 
of eligible assets and non-cleared IM tends to be non-cash due to segregation requirements, but 
with greater regulatory, operational and funding complexity.
The burden of meeting these collateral requirements varies significantly across market participants 
and the increasing scale, frequency and procyclicality of margin calls has placed additional strain 
on individual institutions and the broader market infrastructure. Once a peripheral operational 
afterthought, collateral management has become a process of strategic and systemic significance.
Regulatory reforms introduced after the financial crisis have profoundly reshaped the risk 
management framework. These include requirements driven by the Group-of-20 nations for central 
clearing, higher capital charges and the phased implementation of non-cleared margin requirements. 
These changes were designed to mitigate counterparty credit risk and promote financial stability. In 
doing so, they have elevated the role of collateral, particularly HQLA, to the extent it now impacts 
institutional solvency and market functioning. In parallel, secular trends such as global monetary 
tightening, the growth of non-bank financial intermediation (NBFI) and increased geopolitical 
fragmentation, have compounded liquidity pressures across the financial system.
Recent market shocks, including the 2020 dash for cash, the energy market volatility following 
Russia’s invasion of Ukraine and the 2022 UK gilt market crisis, have underscored a stark 
reality. Inefficiencies in collateral frameworks can amplify risks, destabilize institutions and 
lead to systemic contagion.
The UK gilt market crisis revealed liquidity fragilities in NBFI portfolios under stress. The dash 
for cash exposed systemic interdependence between margin calls and funding markets. The 
energy crisis showed that collateral demands while liquidity is constrained reduce market depth, 
highlighting the need to broaden eligible collateral during price shocks. 
In each case, deficiencies in collateral availability, eligibility or mobilization – rather than outright 
credit defaults – amplified systemic instability. These episodes underscore a critical shift. What 
1 OTC derivatives statistics at end-June 2024, Bank for International Settlements, November 21, 2024, www.bis.org/publ/otc_hy2411.pdf

## Page 6

06
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
began with reforms to reduce counterparty credit risk has led to new forms of liquidity risk, 
operational complexity and systemic risk exposure.
As collateral becomes increasingly essential yet scarce, inefficiencies in eligibility criteria, settlement 
systems and collateral reuse are no longer tolerable frictions. They have become systemic 
vulnerabilities. This whitepaper addresses those vulnerabilities, proposing a holistic framework to 
improve collateral efficiency, expand liquidity capacity and ultimately strengthen the resilience of 
the derivatives ecosystem.
1.2 A Structural Trilemma: Market, Credit and Liquidity Risks
At the heart of well-functioning, liquid, open and efficient derivatives markets there is a structural 
interdependence between three key risks:
• Market Risk: The potential for losses due to price fluctuations in derivatives positions. This 
includes exposure to shifts in interest rates, equity indices, FX rates and commodity prices. 
Hedging via derivatives aims to mitigate market risk2
. 
• Counterparty Credit Risk: The potential for losses where a counterparty defaults on its 
obligations before the final settlement of the transaction’s cashflows. This risk is managed 
primarily through collateralization and central clearing, which transforms it into liquidity risk 
but does not eliminate it.
• Liquidity Risk: The inability to meet margin calls due to insufficient liquid assets. Even solvent firms 
may face funding shortfalls if collateral is trapped in illiquid instruments or fragmented systems.
These tightly interlinked risks comprise the risk triangle. During periods of market turbulence, 
margin requirements rise, forcing market participants to post additional collateral, which creates 
a strain on liquidity. This is a clear example of how market shocks, transmitted through credit 
channels, can trigger collateral demands that expose liquidity shortfalls, which intensify credit 
concerns. The risk triangle is not static, but rather a feedback-prone structure.
Figure 1: The Risk Triangle
Source: Energy Trader Europe
2 The Value of OTC Derivatives: Empowering Organizations to Manage Risks, Enhance Returns and Optimize Liquidity, ISDA, March 17, 2025, www.isda.
org/2025/03/17/the-value-of-otc-derivatives-empowering-organizations-to-manage-risks-enhance-returns-and-optimize-liquidity
Risk of financial losses from unhedged
positions following price and volitility
movements on the market
Risk of counterparty default
related to a market transaction
Risk of available cash for
disposal required to secure
the market transactions
in a very short time period Mutual risk dependency
Mutual risk dependency
Mutual risk dependen
Risk
cy
triangle
Market
risk
Cash
liquidity
risk
Credit
risk

## Page 7

07
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
Any attempt to mitigate one of these risks – whether through increased margining, stricter 
collateral eligibility or central clearing – can reduce market depth and accessibility, or shift stress to 
one or both of the other risk dimensions. 
For example, overcollateralization policies may reduce credit exposure but introduce liquidity 
strain during periods of volatility. Liberalizing collateral schedules may ease liquidity pressure 
but raise concerns about asset creditworthiness or valuation under stress. Central clearing lowers 
bilateral counterparty risk but often concentrates liquidity needs at CCPs, which only accept the 
narrowest forms of HQLA for VM.
This ‘trilemma’ is not theoretical. It manifests acutely during stress events, where the procyclical 
nature of margin frameworks, coupled with a scarcity of eligible collateral, can trigger pathways 
that undermine market functioning and depth. Achieving a balance so that margin rules are risk 
appropriate has become an increasingly complex challenge, particularly as collateral demands grow 
faster than market capacity to supply and mobilize suitable assets.
1.3 A Fragmented Infrastructure in an Interconnected World
Compounding these pressures is a fragmented infrastructure landscape that inhibits efficient 
collateral mobilization. Many institutions continue to operate within siloed architectures across 
trading, treasury and risk departments, as well as across jurisdictions. Cross-border differences 
in margin rules, inconsistent collateral eligibility criteria across CCPs and divergent accounting 
treatments for collateral assets further restrict the fluidity of global collateral pools. Even where 
institutions seek to optimize collateral deployment, operational constraints – such as settlement 
delays, manual instructions and data inconsistency – limit their ability to respond in real-time to 
fast-moving market conditions.
This operational friction is particularly acute for NBFIs and corporates, which often face 
constraints on cash access and balance sheet flexibility and don’t have direct access to central bank 
liquidity. The use of non-cash collateral, while sometimes permitted by regulators, is operationally 
intensive and legally complex. These constraints not only impair the ability of such entities to 
meet margin calls during periods of stress but also reduce their capacity to efficiently recycle or re￾use collateral. This increases dependence on cash and exacerbates market-wide liquidity shortages.
The net effect of these forces is an environment in which the cost of collateral is rising, the 
pool of eligible assets is narrowing and the ability to mobilize collateral across markets is 
increasingly constrained. This creates the potential for market-wide consequences, particularly 
under conditions of stress. At the same time, regulators face difficult trade-offs as they work 
to determine how to calibrate margin and liquidity requirements to prevent risk transmission, 
without inadvertently triggering fire sales, constraining hedging activity or disincentivizing market 
participation.
In parallel, the rise of novel financial instruments and decentralized technologies brings both 
opportunity and risk. DLT, tokenization and the CDM hold the promise of real-time settlement, 
greater standardization and improved collateral transparency. Yet adoption remains uneven, legal 
frameworks are still evolving and interoperability with legacy systems is limited. If successfully 
integrated, these technologies could revolutionize collateral mobility and resilience.

## Page 8

08
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
1.4 Strengthening the Foundations of Financial Stability
As the market structure continues to evolve and as global monetary, geopolitical and climate￾related risks continue to intensify, the ability to efficiently source, deploy and manage collateral 
will be a key determinant of market resilience. The derivatives market cannot afford to treat 
collateral merely as an operational necessity. Instead, it must be understood as a strategic resource: 
one that underpins the pricing, funding and risk capacity of institutions and markets alike.
Persisting with outdated collateral frameworks risks past crises being repeated with greater severity. 
Conversely, embracing process improvements, technological innovation and asset diversification 
can transform the management of collateral from a vulnerability into a pillar of resilience. Success 
hinges on collaboration. Regulators must balance prudence with flexibility; institutions must 
prioritize harmonization and interoperability; and technologists must bridge the gap between 
legacy systems and cutting-edge tools.

## Page 9

09
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
2. COLLATERAL OPTIMIZATION: FROM PAIN POINTS TO 
SOLUTIONS
This section addresses the high costs of collateral and outlines key strategies to enhance collateral 
efficiency. It examines techniques such as multilateral IM rebalancing to reduce margin 
requirements and explains how participants can leverage repo and other financing markets to 
meet collateral demands without straining liquidity. It also explores issues relating to centrally 
cleared positions, including leveraging cross-product margining opportunities that can further 
reduce overall collateral needs. Finally, it highlights the essential operational enablers – centralized 
collateral governance, data-driven automation and strong data management – that underpin 
successful collateral optimization. 
2.1 Cost of Collateral
Effective collateral optimization allows an institution to efficiently manage its asset portfolio, 
satisfying its collateral obligations while reducing costs and maintaining sufficient liquidity in an 
operationally scalable manner. However, maintaining adequate collateral buffers is costly, as it 
forces firms to hold highly liquid assets (cash or HQLA) for use as margin. 
The main cost drivers include:
• Funding costs: The opportunity cost of using a particular asset as collateral instead of deploying 
it elsewhere. For example, posting a high-yielding asset as collateral means giving up its 
potential return. Institutions manage this trade-off by maintaining internal funding curves 
across different tenors and collateral types to help determine the cheapest-to-post asset at any 
given time.
• Liquidity and capital costs: Tapping financial markets to obtain eligible collateral (for instance, 
lending cash to borrow securities via repo) can erode an institution’s immediate liquidity and 
introduce counterparty credit exposure. This not only reduces the liquidity premium of holding 
cash but can also increase regulatory capital charges or incur additional collateral requirements 
to cover the new risks. 
• Custodian costs: Handling collateral across multiple settlement venues incurs a patchwork of 
fees. Depositories and custodians have different fee structures for different asset classes, so using 
a wide range of collateral types can lead to higher aggregate custodian fees and operational 
complexity. 
• Legal costs: Broadening the types of acceptable collateral necessitates robust legal arrangements 
to ensure enforceability. Drafting and maintaining these arrangements (eg, updating credit 
support annexes (CSAs) to accept non-traditional assets) incurs legal and administrative 
expense and effort.

## Page 10

10
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
While the post-crisis reforms have reduced counterparty credit risk, they have further elevated 
margin and capital requirements and the cost of funding derivatives positions. Managing collateral 
costs has become an increasing concern for a diverse range of market participants, including banks 
and NBFIs. Although the phased implementation of non-cleared margin requirements helped to 
ease the initial transition for smaller firms, as more of the derivatives market becomes subject to 
the requirements and threshold limits are reached, firms will face significantly higher IM demands. 
Institutions should be prepared to fund these requirements and mitigate the impact on their 
balance sheets. 
Further, differences in regulatory treatment between banks and NBFIs result in divergent funding 
capacities, with stricter regimes often leading to higher collateral costs for those subject to the 
stricter requirements. Banks typically require sophisticated strategies to align the use of collateral 
with strict funding and liquidity standards, while non-banks and corporates often leverage 
innovative financing solutions to maintain liquidity and meet collateral demands. 
Institutions should look carefully at collateral selection and allocation as a way of managing the 
costs of collateral. 
2.2 Optimizing Collateral Selection and Allocation
Multilateral IM Rebalancing
Effective management of IM is key to achieving collateral efficiency across both bilateral and 
CCP-cleared derivatives. IM requirements – applicable to both bilateral and cleared trades – often 
consume a large portion of an institution’s collateral. 
Bilateral IM is generally calculated using the ISDA Standard Initial Margin Model (ISDA SIMM) 
based on risk sensitivities, whereas each CCP employs its own internal margin models for cleared 
portfolios. As IM requirements have increased and as clearing mandates extend to more products, 
firms are increasingly looking for ways to optimize the amount of margin they need to post. 
One promising technique is multilateral IM rebalancing, which aims to redistribute risk across a 
network of trading participants so that each participant’s margin requirement is optimized and 
reduced. In this process, an independent service provider analyzes the risk sensitivities of each 
portfolio in the network and identifies offsetting trades that participants can execute with each 
other to mutually reduce their IM exposures. 
Unlike bilateral margin optimization, which only considers two counterparties at a time, this 
multilateral approach spreads risk offsets across many participants, yielding a greater aggregate 
reduction in IM. Crucially, the rebalancing is designed to keep overall market risk unchanged 
for each firm; the new trades simply offset existing exposures. This process helps to avoid over￾margining and under-margining and seeks to achieve significant IM savings by lowering the cost 
of funding, captured by the margin valuation adjustment. This multilateral rebalancing exercise 
can be run for both bilateral portfolios and CCP-cleared portfolios. 
The following example highlights how multilateral IM rebalancing analyzes counterparty risk 
sensitivities and identifies offsetting trades to minimize counterparty credit risk while keeping 
market risk constant.

## Page 11

11
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
Figure 2: Example of delta risk transfers
This is an illustrative example of some delta risk transfers for a simplified portfolio, with a hypothetical 
network of four participants – A, B, C and D – resulting in an overall systemic risk reduction of 47%. 
triBalance has been used for the multilateral IM rebalancing and triCalculate to compute the ISDA SIMM 
sensitivities and IM. Initial portfolio included FX non-deliverable forwards and FX options.
While multilateral rebalancing effectively reduces overall collateral requirements, focusing solely 
on minimizing IM costs could adversely impact other risk objectives, such as regulatory capital 
usage3
. For this reason, some vendors offer optimization frameworks that jointly reduce both IM 
and regulatory capital costs (reflected in the Capital Valuation Adjustment, or KVA). 
This holistic approach ensures that lowering liquidity risk (via reduced IM) does not inadvertently 
raise credit or solvency risk elsewhere. It also seeks to balance the risks identified in the risk 
triangle by lowering liquidity risk, keeping market risk constant and managing counterparty credit 
risk by reducing exposure and regulatory capital requirements.
While counterparty risk optimization techniques may be particularly beneficial for larger firms 
that have exceeded applicable non-cleared IM thresholds, effective margin management is also 
crucial for smaller market participants. Even without engaging in network-wide optimization, 
these institutions can improve margin efficiency through IM analysis tools. 
Monitoring the main drivers of daily IM movements and using scenario analysis can help 
institutions assess portfolio performance under market stress and the impact of adding or 
unwinding trades. Additionally, unilateral IM optimization can identify trades that reduce 
overall IM requirements for an institution, which may be particularly useful for counterparty 
arrangements nearing the applicable non-cleared IM thresholds, where proactive management can 
prevent unanticipated breaches of the thresholds and optimize collateral usage.
3 Counterparty Risk Optimisation, OSTTRA, osttra.com/services/optimisation/counterparty-risk-optimisation
Systemic Risk
Reduction
501 527 ---> 267 108
= 47%
Source: OSTTRA * All numbers are shown in US dollars
After A B C D Net Sum 
Abs
Risk 
Reduction
A -3 910 -61 107 -11 812 -76 829 76 829 47%
B 3 910 491 0 4 401 4 401 67%
C 61 107 - 491 -56 234 4 382 117 832 43%
D 11 812 0 56 234 68 046 68 046 50%
267 108 47%
B
D
A
C
3 910
Exposure after
IM rebalancing
56 234
61 107
491
11 812
Before A B C D Net Sum 
Abs
A -8 783 -101 882 33 836 -76 829 144 500
B 8 783 -4 382 0 4 401 13 165
C 101 882 4 382 -101 882 4 382 208 145
D -33 836 0 101 882 68 046 135 717
501 527
B
D
A
C
8 783
Exposure before
IM rebalancing
Market risk Counterparty risk
101 882
101 882
4 382
33 836
Diff A B C D Net
A 4 873 40 775 -45 648 0
B -4 873 0 4 873 0 0
C -40 775 -4 873 0 45 648 0
D 45 648 0 -45 648 0 0
B
D
A
C
4 873
No market
risk impact
Add triBalance 
hedge trades
45 647
40 774
4 873
45 647

## Page 12

12
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
Given margin reduction benefits increase as more participants join the network, the IFLD 
encourages broader participation in multilateral IM optimization networks. The more 
counterparties that can offset each other’s risks, the greater the cumulative IM savings can be for 
the system without an increase in systemic risk. Additionally, firms that remain below the non￾cleared IM thresholds should adopt a proactive margin management approach. 
Regular IM monitoring, targeted risk offset trades and scenario-based stress testing of portfolios can 
significantly improve margin efficiency and prevent unanticipated liquidity strains from margin calls. 
By combining market-wide cooperation with diligent, enhanced in-house risk management, the 
industry can substantially reduce redundant collateral and improve overall liquidity preparedness.
2.3 Repo and Financing Markets
Beyond reducing the amount of collateral required through portfolio optimization, market 
participants also focus on mobilizing liquidity when collateral requirements increase. Non￾centrally cleared derivatives markets can provide alternative sources of collateral, enabling parties 
to negotiate bilateral arrangements that reflect specific trade and counterparty risks. 
Strong repo and securities financing markets play a crucial role in this context, enabling firms to 
swiftly convert collateral into cash to meet VM or other cash collateral calls without incurring 
sudden losses. In non-cleared derivatives markets, counterparties have the flexibility to negotiate 
bespoke collateral arrangements and many NBFIs rely on these financing markets as an alternative 
source of liquidity. Since the introduction of mandatory clearing of standardized OTC derivatives, 
repo markets have become increasingly important for NBFIs that need to quickly convert 
collateral into cash to fulfil margin requirements set by CCPs. 
Strategies for raising cash via securities financing include: 
(1) Repo transactions: Under a repo, a firm sells securities to a counterparty and agrees to buy 
them back later at a set price. These transactions are often governed by standard agreements such 
as the Global Master Repurchase Agreement or the Master Repurchase Agreement. Economically, 
repos allow an institution to borrow cash against high-quality securities for a short period, 
providing immediate liquidity in exchange for a modest financing cost. 
(2) Total return swap: Derivatives can also be used to replicate the economic effect of a repo. One structure 
involves the parties entering into a total return swap, which is margined under an ISDA CSA. One leg of 
the swap is collateralized with cash and the other with securities. In practice, the NBFI pledges bonds to a 
dealer, earning the total return on those bonds via the swap, and the dealer provides cash collateral on the 
other leg. This arrangement can yield the same economic result as a repo (securities for cash funding), but 
is effected within the ISDA derivatives documentation framework, which can be useful for counterparties 
that prefer or require collateral exchanges to occur under their ISDA agreements.
In addition to trading strategies employed by firms, there are broader industry initiatives to integrate 
securities financing and derivatives markets for greater collateral efficiency. From a regulatory 
perspective, repos and derivatives are increasingly viewed through a similar lens in bank capital rules 
such as the EU’s Capital Requirements Regulation and the equivalent US regulatory capital framework. 
In February 2022, ISDA published the 2022 ISDA Securities Financing Transactions Definitions 
and related documents, enabling repos, stock loans and derivatives to be documented as a single 
close-out netting arrangement under an ISDA Master Agreement4
. 
4 Collaboration and Standardization Opportunities in Derivatives and SFT Markets, ISDA, October 5, 2020, www.isda.org/2020/10/05/collaboration-and￾standardization-opportunities-in-derivatives-and-sft-markets

## Page 13

13
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
This development paves the way for cross-product netting and potentially unified collateral 
agreements covering multiple product types. In a scenario in which a repo and an OTC swap 
with the same counterparty are subject to a single master netting agreement and single collateral 
agreement, only a single net margin amount would need be exchanged, instead of each transaction 
having separate collateral requirements. Cross-product netting could free up significant collateral 
resources, ease operational burdens and reduce settlement risk, particularly during times of stress. 
Realizing this vision will require further work on both the regulatory and operational fronts to 
permit and operationalize cross-product margining, but this represents a promising avenue for 
future collateral optimization.
Looking ahead, market participants should monitor regulatory changes that could impact NBFIs’ 
access to the repo and financing markets. In the US, the Securities and Exchange Commission 
(SEC) will require that secondary market trading of in-scope US Treasury securities must be 
centrally cleared by the end of 2026, with mandatory clearing of Treasury repo transactions to 
follow by mid-20275
. The derivatives market will see significant change as pressure mounts to 
address current impediments in the existing regulatory and capital framework, but it is not yet 
clear the effect such changes will have for market liquidity, spreads or investors. 
In its response to the Financial Stability Board’s (FSB) consultation on NBFI leverage6
, which was 
submitted on February 28, ISDA highlighted that the implementation of repo clearing in the US 
Treasury market is highly complex and the market will need to consider whether access models can 
be developed to enable repo clearing at an affordable cost for all clients7
. In addition, key features 
of repo markets differ across jurisdictions and the approach followed in the US might not be 
appropriate elsewhere. Although other jurisdictions appear to be exploring whether to implement 
repo clearing mandates, legislative proposals have not yet been published. 
The upcoming regulatory changes highlight the importance of bilateral repo markets as a stable 
and accessible source of liquidity for NBFIs. They also reinforce the need for market participants 
to consider alternative sources of collateral, such as broadening the range of assets that can be used 
as margin or for establishing committed credit lines for margin liquidity. Collateral diversification 
strategies are explored in Section 3 of this paper. Even as clearing and other reforms emerge, 
maintaining flexible funding options through repo and related markets will remain a key element 
of collateral optimization and liquidity risk management.
CASE STUDY: A major European bank recently consolidated all collateral activities onto a 
single platform, replacing siloed systems across its securities finance and derivatives units. 
This has improved the firm’s agility during market swings and enhanced the quality of 
data available to risk managers and regulators. By managing its entire collateral inventory 
in one place, the bank can respond faster to margin calls and optimize allocations in 
line with balance sheet and funding needs, demonstrating how integration drives both 
efficiency and resilience.
5 Extension of Compliance Dates for Standards for Covered Cleared Agencies for U.S. Treasury Securities and Application of Broker-Dealer Customer 
Protection Rule With Respect to U.S. Treasury Securities, Federal Register, www.sec.gov/files/rules/final/2025/34-102487.pdf
6 Leverage in Non-Bank Financial Intermediation: Consultation report, Financial Stability Board, December 18, 2024, www.fsb.org/2024/12/leverage-in￾non-bank-financial-intermediation-consultation-report
7 ISDA Responds to FSB Consultation on Leverage in NBFI, ISDA, March 4, 2025, www.isda.org/2025/03/04/isda-responds-to-fsb-consultation-on-leverage￾in-nbfi

## Page 14

14
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
2.4 Considerations for Cleared Activity and Cross-product Margining
Optimizing margin costs involves not only bilateral agreements and collateral selection, but 
also the efficient transfer of exchange-traded positions across clearing members and exchanges. 
This strategy leverages netting advantages within CCPs by reallocating trades to minimize IM 
requirements. Balancing bilateral and cleared positions through strategic reallocation ensures 
optimal IM levels across both cleared and non-cleared derivatives, highlighting the importance 
of a holistic optimization framework that considers collateral composition and trade placement 
across various venues.
The clearing landscape is evolving quickly and new regulations are applying clearing mandates to 
more asset classes. CCPs will need to adapt swiftly to these regulatory changes, as well as to related 
market shifts and a potential surge in collateral inflows. 
Cross-product margining (CPM) enables margin requirements to be offset across markets within 
the same asset class, recognizing correlations between positions to reduce IM requirements. For 
example, Eurex Clearing offers cross-margining between exchange-traded and OTC products and 
has indicated it will add cleared repos soon8
. Another form of CPM allows offsets across CCPs, 
which necessitates some level of interoperability between involved CCPs. These initiatives often 
require multiple CCP memberships for users (or affiliates). 
A cross-margining initiative led by CME/DTCC is one notable solution in this area9
. Both 
forms of CPM have significant potential to reduce IM requirements, and therefore funding 
cost requirements, but the inconsistent adoption of CPM, particularly in client clearing, 
indicates that maximizing margin efficiencies is not the only concern. The use of CPM can bring 
implementation costs and introduce varying degrees of operational challenges for CCP members, 
including reconciliation of the new margin calculations and passing those on to their client users. 
Each institution should weigh these implementation cost considerations against potential IM 
reductions and funding cost savings to decide whether to opt for CPM when clearing transactions 
at CCPs. Institutions with directional portfolios may find it less attractive than those with 
balanced portfolios. The IFLD encourages CCPs to continue innovating and investing in CPM 
initiatives to give institutions the option to optimize their collateral requirements. 
Case Study: Analysis by a clearing venue showed that reallocating trades across portfolios 
can dramatically cut collateral needs. In one case, a firm rearranged swap positions 
between two CCPs to maximize offsetting exposures, reducing total margin requirements by 
nearly 40%. This translated into significant daily funding cost savings of tens of thousands 
of dollars. The example illustrates a key collateral optimization technique – holistic portfolio 
margining. By viewing collateral obligations at an enterprise level, rather than at the desk 
or counterparty level, institutions identified substantial cost reduction opportunities through 
multilateral netting and the use of ‘cheapest-to-deliver’ assets for margin.
8 Deep liquidity: High margin efficiencies, www.eurex.com/ec-en/services/margining/cross-margining
9 CME Group and DTCC to Increase Cross-Margining Opportunities for the Treasury Markets, July 17, 2023, www.cmegroup.com/media-room/press￾releases/2023/7/18/cme_group_and_dtcctoincreasecross-marginingopportunitiesforthetr.html

## Page 15

15
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
2.5 Collateral Efficiencies and Data Management
Effective governance structures are vital for managing collateral, funding, liquidity and hedging 
risks in both cleared and non-cleared markets, whether through central steering or active 
management of collateral within an institution. Institutions must also consider whether their 
collateral optimization strategies are operationally scalable and consume an appropriate number 
of resources that an institution is willing to devote to this exercise. This is where new technologies 
can be deployed to improve automation and data management. 
Technological innovation will likely result in an initial upfront spend as institutions work 
to upgrade systems or map to industry data standards to support these changes. However, 
implementation of technology solutions across the industry to automate collateral management 
processes by sending margin calls, moving assets between different custodial locations or 
optimizing collateral on a pre- and post-trade basis, will enable firms to be more nimble across 
their collateral strategies and keep up with the pace of market changes.
Central Governance 
Every institution in the derivatives market faces unique challenges that require tailored governance 
structures. Factors such as institutions’ geographic footprints and business models necessitate 
different organizational setups, ensuring governance structures are proportional to each 
organization’s scale and complexity.
A uniform governance framework is not appropriate for the wide range of participants in the 
derivatives market, particularly among NBFIs and corporates, which operate under wide-ranging 
regulatory environments, risk appetites and internal capabilities. As such, governance structures 
must be tailored to reflect these differences, ensuring that oversight and decision-making processes 
are appropriately aligned with each participant’s regulatory obligations and market role.
This point was highlighted in ISDA’s response to the FSB’s consultation on liquidity preparedness 
for margin and collateral calls last year, in the importance of integrating margin and collateral 
management into liquidity risk governance10. “NBFIs should integrate the management of margin 
and collateral calls into their liquidity risk management systems, processes, and governance 
frameworks… Many NBFIs are already required to do this under existing regulation,” ISDA wrote.
This underscores the need for governance models that are both proportionate and sector-specific, 
enabling effective margin call preparedness without imposing inappropriate structures on diverse 
institutions.
For some organizations, effective governance can include central steering, with a dedicated desk to 
streamline and optimize collateralized positions – this is often done by way of an XVA desk. 
In modern risk and pricing practices, many collateral-related costs are quantified through XVA, 
which measures the credit, capital and funding risks embedded in a trade. While the credit 
valuation adjustment (CVA) and the debit valuation Adjustment (DVA) – which capture 
counterparty and own credit risk – have historically been more prominent, the widespread use of 
collateral has significantly reduced counterparty credit exposure and, with it, the size of CVA and 
DVA. As a result, regulatory and economic attention has increasingly shifted toward funding and 
capital costs, captured in the following XVAs:
10 ISDA Responds to FSB Consultation on Liquidity Preparedness for Margin and Collateral Calls, ISDA, June 19, 2024, www.isda.org/2024/06/19/isda￾responds-to-fsb-consultation-on-liquidity-preparedness-for-margin-and-collateral-calls

## Page 16

16
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
Incorporating these adjustments into pricing may support better decision-making around 
collateral, promote financial transparency and can contribute to the overall financial health and 
resilience of an institution11.
While XVA desks have played a crucial role in pricing and risk managing various valuation 
adjustments, they are often also responsible for carrying out optimization exercises of various 
types12. This further increases the value of XVA desks by making their organizations more cost 
efficient. However, due to the complexity and computational cost, smaller institutions may 
outsource these types of optimization activities.
For firms that lack internal resources or infrastructure to calculate XVAs or perform cost-based collateral 
optimization, leveraging external providers can ensure accurate, efficient and scalable computation of XVA 
metrics and optimization strategies, helping institutions remain competitive while managing complexity. 
Ultimately, integrating XVA into governance and pricing processes improves collateral decision-making, 
increases financial transparency and strengthens the institution’s overall financial resilience.
By consolidating collateral optimization under a centralized desk, whether internal or via 
outsourcing, institutions can enhance liquidity efficiency and optimize collateral requirements. 
Overall collateral levels can be aligned internally within an institution, enabling active management 
and rebalancing of collateral across markets, counterparties and clearing venues. Collateral 
management processes and optimization strategies should be periodically reviewed to identify areas 
for improvement, particularly given the continuously evolving regulatory landscape and technology. 
Automation and Data Management 
As a result of differing non-cleared margin requirements for banks and NBFIs, there have been 
different risk appetites in determining eligible collateral. This has resulted in eligible collateral 
schedules either being too narrow or too complex, as schedules need to be codified from multiple 
formats into risk systems. Institutions require certainty in collateral eligibility. One way to address 
this issue is by requiring clear, machine-readable eligible collateral schedules (ie, eligible collateral 
schedules with consistent legal terminology and formatting).
The CDM can be used to ease the burden on collateral management systems across products, 
as further explored in Section 4 of this paper. The model should be developed in line with 
data formats and standards used for the underlying debt instruments, including golden source 
concepts, to ensure ISDA aligns with the recommendations of the International Capital Market 
Association (ICMA) and bond data models, as an example13. The ISDA Legal Agreement 
Taxonomy and ISDA Clause Library promotes the use of common terminology in negotiated 
terms (including regulatory CSAs and non-regulatory VM CSAs) and assists with the 
categorization and management of legal agreement data within those contractual terms14. 
Funding Valuation Adjustment The cost of funding uncollateralized exposure
Margin Valuation Adjustment The cost of funding segregated IM collateral
Collateral Valuation Adjustment The cost of funding unsegregated collateral
Capital Valuation Adjustment The cost of holding regulatory capital
11 The xVA Challenge: Counterparty Credit Risk, Funding, Collateral and Capital, Jon Gregory, Wiley, 2020
12 XVA at the Forefront: Addressing Key Financial Challenges, OSTTRA, September 20, 2023, osttra.com/articles/xva-at-the-forefront-addressing-key￾financial-challenges
13 Bond Data Taxonomy Working Group, ICMA, www.icmagroup.org/fintech-and-digitalisation/fintech-advisory-committee-and-related-groups/bond￾data-taxonomy#
14 What is the ISDA Clause Library?, ISDA, www.isda.org/a/u6TgE/ISDA-Clause-Library-factsheet-2021.pdf

## Page 17

17
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
2.6 Conclusion
At its core, collateral optimization is about balancing cost efficiency with robust risk management. 
By adopting practical optimization techniques – such as smarter collateral sourcing, improved 
market access, better margin management and stronger governance – along with standardized 
documentation and scalable infrastructure, institutions can proactively enhance collateral 
efficiency, reduce operational and funding burdens and build greater resilience in a fragmented 
and margin-intensive environment. 
Effective collateral optimization has the potential to transform collateral from a passive compliance 
requirement into a strategic resource. Institutions that successfully deploy innovative techniques 
and frameworks like those set out in this paper may be better poised to not only lower their own 
costs and risks, but also to contribute to a more liquid and stable derivatives market.

## Page 18

18
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
3. EXPANDING THE COLLATERAL LIQUIDITY POOL
To improve liquidity resilience, the pool of acceptable collateral for derivatives margin can 
be expanded beyond conventional HQLA. This section examines the strategic rationale for 
considering a broadening of the range of eligible collateral to include MMFs, bank guarantees, 
CP and even carbon emissions certificates. It considers the safeguards needed to integrate these 
non-traditional assets in a safe way and the idea of a European ‘common safe asset’ to provide 
a uniformly reliable form of collateral across EU markets, thereby deepening repo liquidity and 
reducing fragmentation. Finally, a stress event protocol is proposed to dynamically widen collateral 
eligibility during severe market dislocations, temporarily alleviating cash shortages and mitigating 
contagion pathways. 
3.1 Collateral Eligibility in the Derivatives Market
The eligibility of collateral in the derivatives market is crucial for managing counterparty credit 
risk and maintaining adequate liquidity levels while keeping the derivatives markets deep and 
open. Regulators impose strict eligibility criteria to ensure posted assets are liquid, stable and 
readily enforceable, balancing market stability with operational feasibility. Expanding the universe 
of eligible collateral could free up immobilized capital and ease the strain on scarce cash and 
government bonds, making the market safer, more liquid and more accessible. 
This change would not be without complications, including potential additional valuation 
complexity, operational friction and consequences for capital or leverage ratios. Any broadening of 
collateral schedules must therefore be approached cautiously, with a focus on addressing the issues 
that arise during market stress events.
Two primary hurdles hinder the expansion of the eligible collateral pool: first, legal and 
contractual constraints; and second, technological or operational limitations. Amending collateral 
agreements or industry rules to accept new asset types often requires protracted legal negotiations 
and legacy systems may struggle to handle non-traditional assets. Expanding the universe of 
eligible collateral could help to create deeper markets and increase liquidity preparedness. 
However, not all participants may accept guarantees, commercial paper or emission credits, as 
each entity faces its own reuse, liquidity or regulatory concerns. The following sections explore 
possible assets that could be used to expand the collateral pool and considers whether these could 
be applied as new forms of eligible collateral. 
CASE STUDY: CCPs have also moved to broaden the mix of assets that members can post 
as margin. For example, one leading CCP recently announced plans to accept offshore 
government bonds from an emerging market as eligible collateral, aiming to reduce 
members’ over-reliance on cash and improve margin flexibility in that region. Likewise, 
regulators are weighing the acceptance of MMF shares for margin to unlock cash tied up 
in funds. These developments highlight a clear trend: by expanding collateral eligibility 
to non-traditional assets, market participants can tap into a deeper liquidity pool. Such 
diversification, supported by robust haircuts and governance, increases the overall buffer of 
assets available to meet obligations in stressed market conditions.

## Page 19

19
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
Money Market Funds
Although government-only/Treasury-only MMFs are permitted as eligible collateral in the non￾cleared margin rules of various jurisdictions, the IFLD recommends that regulators should engage 
in efforts to harmonize eligibility criteria. They should also take steps to mitigate concentration 
risk and the susceptibility of MMFs to run-like behavior by establishing eligibility criteria that 
expand the scope of eligible MMFs.15
An MMF is a pooled investment fund that invests in high quality, short term debt instruments, 
including Treasury bills, agency securities, commercial paper, certificates of deposit and repos. MMFs 
are widely considered safe investments due to their low concentration risk and broad diversification, 
making them a popular alternative to bank deposits16. They are a potentially liquid source of 
collateral for posting as IM and benefit from relatively low haircuts, typically 2% of pledged value. 
Compared to other asset classes, MMFs have no, or very low, net asset value volatility. MMFs that 
use repo can accommodate late-day and large purchases, offering greater flexibility for investors 
using these funds as margin collateral. EU regulations allow and even promote the use of repos 
and securities lending by MMFs to support liquidity management, while the US Commodity 
Futures Trading Commission (CFTC) and US prudential regulators’ rules prohibit such asset 
transfers, limiting eligible MMFs to static holdings.
ISDA’s suggested operational practices for cash and MMFs outline standardized procedures for 
posting cash as IM and reinvesting it into MMFs within segregated accounts17. These practices aim 
to enhance collateral mobility, reduce transaction costs and mitigate settlement risks. 
In the EU, MMFs are permitted to engage in repos and securities lending as part of their liquidity 
management strategies. These activities are recognized under EU margin rules, allowing MMFs to be 
used as eligible collateral for IM purposes. Conversely, US regulations from the CFTC and prudential 
regulators impose restrictions that disqualify MMFs engaging in repos or securities lending from being 
used as eligible collateral. This limitation has led to calls from industry associations to align US rules 
more closely with EU standards and to consider substituted compliance with EU margin rules.
The IFLD recommends further evaluating the recommendation published by the Technical Issues 
Subcommittee of the CFTC’s Global Markets Advisory Committee on November 6, 202318, to 
expand the scope of eligible MMFs by:
• Removing criteria that disqualify an MMF as eligible collateral if it transfers assets through 
securities lending, securities borrowing, repo or reverse-repos. Nearly all US MMFs engage in 
the foregoing transactions or are authorized to do so19; 
15 ISDA Letter to EU Policy Makers on Money Market Funds as Initial Margin, ISDA, October 2, 2019, www.isda.org/2019/10/02/isda-letter-to-eu-policy￾makers-on-money-market-funds-as-initial-margin; Joint Letter on Posting Cash and Money Market Funds for Initial Margin, www.sifma.org/resources/
submissions/letters/joint-letter-on-posting-cash-and-money-market-funds-for-initial-margin
16 Money Market Mutual Funds: Policy Concerns and Reform Options, Eva Su, Congressional Research Service, R47309, November 17, 2022, crsreports.
congress.gov/product/pdf/R/R47309
17 Posting Cash as IM to be Reinvested into a MMF, ISDA Suggested Operational Practices, www.isda.org/collateral-management-sop
18 GMAC Technical Issues Subcommittee Recommendation: Money Market Funds as Eligible Collateral, November 6, 2023, www.cftc.gov/media/9721/
gmac_TechnicalSubcommitteeRecommendationsMMF110623/download 
19 Recommendations to Improve Scoping and Implementation of Initial Margin Requirements for Non-Cleared Swaps, Report to the CFTC’s Global 
Markets Advisory Committee by the Subcommittee on Margin Requirements for Non-Cleared Swaps, May 2020, page 24, www.cftc.gov/media/3886/
GMAC_051920MarginSubcommitteeReport/download (providing that (i) research from a leading custodial bank concluded that only four US money market 
funds (MMFs) would qualify as eligible collateral due to the inclusion of these eligibility criteria; and (ii) the industry is not aware of a single MMF that would 
qualify as eligible initial margin under the Commodity Futures Trading Commission rules, US prudential regulators rules and EU non-cleared margin rules)

## Page 20

20
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
• Allowing for the exchange of third-country MMFs (ie, MMFs that are issued in a different 
jurisdiction) by: 
i. Adopting uniform standards for determining whether an MMF qualifies as an eligible 
third-country MMF (including, without limitation, the asset classes that such third-country 
MMFs are permitted to invest in, any financial or asset test that a third-country MMF 
must satisfy, and the supervisory and regulatory standards applicable to such third-country 
MMFs);
ii. Maintaining a publicly accessible list of third-country MMFs that a regulator has determined 
qualify as eligible collateral, removing the need for market participants to undertake a time￾consuming and costly analysis in this respect.
Guarantees
There has been widespread discussion of the use of guarantees as eligible collateral, and whether a 
proposal to allow corporates and trading firms to use a broader spectrum of guarantees and forms 
of credit support, such as letters of credit and surety bonds, would be acceptable to regulators and 
market participants. 
These instruments could secure both cleared IM and non-cleared bilateral VM, improving 
collateral management and addressing liquidity challenges. However, in both the EU and the US, 
guarantees are not generally used to cover VM in centrally cleared trades, as VM is exchanged 
in cash through a robust ‘cash-through’ process. The bilateral OTC market allows for more 
discretionary collateralization and some institutions use guarantees or other forms of credit 
support to cover VM exposures in certain cases. In cleared markets, IM is typically not passed 
through, which could support an argument for using guarantees to cover IM.
Despite their potential benefits, guarantees are not generally permissible for covering cleared VM in 
either the EU or the US, due to concerns over liquidity and enforceability. Their reuse is inherently 
limited because guarantees are considered bespoke instruments: they lack an attached market value, 
cannot be easily transformed into other forms of collateral and often require legal amendments 
in order to be transferable. Institutions must also contend with potential enforcement delays, due 
diligence complexities and ongoing monitoring of the guarantor’s credit quality. For guarantees to 
function effectively as collateral, they must be issued by eligible high credit quality guarantors – 
typically highly-rated financial institutions such as banks or insurance companies – under stringent, 
risk-weighted acceptance criteria and concentration limits (often around 20% per guarantor). 
During the energy crisis in 2022, when energy prices spiked and liquidity was strained, regulators, 
led by the European Securities and Markets Authority (ESMA), temporarily broadened the pool 
of eligible CCP collateral to include uncollateralized bank guarantees and similar instruments20. 
This flexibility was critical in ensuring that non-financial counterparties active in volatile gas and 
electricity derivatives markets could meet margin calls in spite of limited cash availability. 
Building on these lessons, the European Market Infrastructure Regulation (EMIR 3.0) has 
permanently integrated the use of bank and public guarantees, under certain conditions, as 
collateral. By codifying eligibility for a range of guarantees, including standby letters of credit, 
bank guarantees and surety bonds, this has given market participants a more diversified and liquid 
asset pool to meet their margin obligations.
20 ESMA extends temporary CCP collateral management measures by six months, European Securities and Markets Authority, October 13, 2023, 
www.esma.europa.eu/press-news/esma-news/esma-extends-temporary-ccp-collateral-emergency-measures-six-months

## Page 21

21
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
One of the challenges with using guarantees as collateral is the variety of forms that such 
guarantees can take. This further hinders the use of guarantees as collateral because there is time 
and cost involved in reviewing differing terms. While advances in natural language processing and 
large language models promise efficiencies in processing dense legal texts, the challenge remains 
with integrating these innovations into legacy systems to allow for a quick and efficient review of 
guarantee terms. Given the variety of guarantee forms and levels of investor protection, achieving a 
single standardized format would ease the burden of review. The IFLD recommends a coordinated 
industry initiative, which could be led by ISDA, to standardize guarantee documentation and 
streamline legal review processes.
CASE STUDY: In a recent commodities market crisis, authorities in Germany set up an 
emergency liquidity scheme using government guarantees as collateral support. The 
program offered 100% state-backed bank guarantees to extend credit to energy firms 
facing massive margin calls. By effectively accepting sovereign credit assurances in lieu of 
cash, this measure enabled distressed but viable firms to meet their VM requirements. The 
case highlights an innovative expansion of the collateral pool – using public guarantees to 
backstop private collateral needs – to prevent a cascade of defaults during extreme volatility.
Corporate Commercial Paper
Although there are conceptual similarities with guarantees, CP is a direct debt instrument and is 
tradeable on a secondary market, although this is limited by buy-and-hold investor behavior. CP 
provides high-credit-quality entities with access to short-term funding for working capital and 
collateral requirements. While operational, legal and liquidity challenges exist, the risk profile 
of CP resembles corporate debt, making it suitable if these challenges are addressed. From a 
regulatory perspective, in its current state, CP may only be eligible for IM, not for VM. For the 
latter, CP is not permitted because it does not meet the requirements of operational immediacy of 
settlement and ease of valuation and liquidation21.
The liquidity of CP is less than certain other types of eligible collateral, such as sovereign 
and corporate bonds. To further enhance market liquidity and depth, the IFLD encourages 
consideration of the following:
• Developing CP Baskets and Indices: Creating CP baskets, which are part of indices and index 
products, could improve transparency and attract broader investor participation;
• Expanding Investor Access: Allowing retail participation in CP instruments could strengthen 
monetary transmission mechanisms and create deeper markets;
• Establishing Private CP Repo Markets: Enhancing repo market structures would improve CP 
liquidity and financial stability.
Developing a functional and liquid secondary market is crucial for CP to be recognized as HQLA. 
While HQLA is the most prudent and narrow form of collateral, it is not a strict requirement 
for collateral to be classified as HQLA. ICMA has proposed several initiatives on the European 
markets for CP and certificates of deposit that are worth considering in more detail.
21 EMIR – Delegated Regulation (EU) 2016/2251 – Article 4 and Article 5(1) + RTS Guidelines; CFTC 17 CFR § 23.156

## Page 22

22
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
The need for greater standardization and harmonization is mostly needed in the European CP 
market, as discussed in publications by ICMA and the FSB22. The European CP and negotiable 
European CP market are the two largest, followed by various domestic markets, each with their 
own legal and regulatory frameworks. 
The Short-term European Paper (STEP) label was introduced in 2006 to integrate the European 
short-term paper market, and its adoption has steadily increased. However, as of August 2023, 
STEP-labelled paper accounts for only 25-30% of the euro-denominated short-term market. 
With its January 2025 update, the STEP statistics available through the European Central Bank 
(ECB) data portal have greatly improved market transparency and more granular coverage. Greater 
standardization and digitization of the issuance process, while enabling the continued bespoke 
nature of CP, would improve market accessibility for both issuers and investors. 
A fragmented market also presents challenges for market data transparency. There is currently no 
consolidated public source for pre- and post-trade data, issuance statistics and market structure 
insights. Establishing a centralized, publicly available and accurate market data source would 
enhance transparency and boost confidence among market participants. Industry engagement will 
be essential in refining and implementing robust systems and durable solutions.
Emission Certificates
The carbon derivatives market plays a crucial role in combating climate change by enabling the 
trading of greenhouse gas emission allowances and related instruments23. Emission certificates 
represent allowances to emit a specified amount of greenhouse gases and are actively traded on 
exchanges such as ICE, EEX and other global trading platforms, as well as OTC markets. 
The market for emission certificates has matured significantly, with increasing liquidity and 
growing participation from institutional investors. Emission certificates offer a potentially viable 
alternative to cash collateral. However, price volatility (driven by regulatory changes, energy 
market dynamics, macroeconomic conditions and geopolitical factors), varied depth of liquidity 
(depending on jurisdiction, market structure and how established and sizable the program is) and 
the risk of regulatory change are factors that raise potential concerns in this respect.
The acceptance of emission certificates as collateral in centrally cleared derivatives markets has 
been expanding, with several CCPs permitting their use under defined conditions such as where:
• Haircuts are applied to cushion against volatility; 
• Collateral limits cap the share of overall collateral that certificates may represent; and
• Eligibility criteria restrict acceptance to liquid, exchange-traded allowances.
Despite increasing acceptance by CCPs, the regulatory frameworks governing emissions trading and 
financial collateral varies across jurisdictions, creating challenges in harmonizing risk management 
and capital treatment. Such uneven regulatory treatment across jurisdictions and high capital 
charges under Basel III and the Fundamental Review of the Trading Book (FRTB) can restrict their 
attractiveness, leading to market fragmentation. ISDA has recommended that the risk weight for 
carbon certificates should be reduced and the tenor correlation parameter should be recalibrated24.
22 Enhancing the Functioning and Resilience of Commercial Paper and Negotiable Certificates of Deposit Markets, Financial Stability Board, May 22, 
2024, www.fsb.org/2024/05/enhancing-the-functioning-and-resilience-of-commercial-paper-and-negotiable-certificates-of-deposit-markets
23 Role of Derivatives in Carbon Markets, ISDA, September 30, 2021, www.isda.org/2021/09/30/role-of-derivatives-in-carbon-markets
24 Implications of the FRTB for Carbon Certificates, ISDA, July 23, 2021, www.isda.org/2021/07/23/implications-of-the-frtb-for-carbon-certificates; 
Implications of the FRTB for Carbon Certificates: A Global Perspective, ISDA, April 21, 2022, www.isda.org/2022/04/21/implications-of-the-frtb-for-carbon￾certificates-a-global-perspective

## Page 23

23
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
While most discussion focuses on compliance grade allowances, broadening the lens to other 
certificates whose different origins and market structures could carry distinct collateral opportunities:
• Certified Emissions Reductions: Clean Development Mechanism–issued offsets, traded OTC 
via the UN registry;
• Voluntary Emissions Reductions: private sector or non-governmental organization led credits 
with varying standards, terms and liquidity;
• Renewable Energy Certificates and Guarantees of Origin: renewable energy certificates that 
tag electricity attributes.
Each instrument’s underlying rights, tradability and liquidity must be assessed or developed on its 
own terms before considering it as collateral.
Engaging with global regulators to standardize the prudential treatment of emission certificates 
as collateral could enhance their viability in financial markets. The European Commission has 
taken steps to address this regulatory fragmentation by consulting on potential amendments to 
the Financial Collateral Directive to explicitly include emission allowances as eligible collateral – a 
move supported by ISDA and other entities25. Advocacy for clearer and more harmonized rules 
can enhance market efficiency, the transition to a net-zero economy and collateral diversification. 
A Common Safe Asset
To improve the preparedness of NBFIs for margin calls, ISDA has suggested that the EU should 
enhance the resilience of its repo markets to serve as a reliable backstop source of liquidity and 
collateral during market stress26. 
One proposed solution is the introduction of a European common safe asset to lead to a deep and 
liquid repo market suitable for both cleared and non-cleared transactions. In his 2024 report on 
EU competitiveness, former Italian prime minister and ECB president Mario Draghi described this 
common safe asset as a type of collateral usable across all EU member states and market segments, 
including CCPs and interbank liquidity exchanges . The ECB emphasizes that such an asset is 
essential for fostering macroeconomic and financial stability in the EU by mitigating country-specific 
shocks and reducing negative feedback loops between sovereigns and their domestic banking sectors.
One proposed solution is the introduction of a European common safe asset to lead to a deep and 
liquid repo market suitable for both cleared and non-cleared transactions. In his 2024 report on 
EU competitiveness, former Italian prime minister and ECB president Mario Draghi described 
this common safe asset as a type of collateral usable across all EU member states and market 
segments, including CCPs and interbank liquidity exchanges27. The ECB emphasizes that such 
an asset is essential for fostering macroeconomic and financial stability in the EU by mitigating 
country-specific shocks and reducing negative feedback loops between sovereigns and their 
domestic banking sectors.
25 Summary report of the targeted consultation on the review of the Directive on financial collateral arrangements, European Commission, February 12, 
2021 – May 7, 2021, finance.ec.europa.eu/system/files/2023-06/2021-financial-collateral-review-summary-of-responses_en_0.pdf 
26 ISDA Response to EC Consultation on Macroprudential Policies for NBFIs, ISDA, November 25, 2024, www.isda.org/2024/11/25/isda-response-to-ec￾consultation-on-macroprudential-policies-for-nbfis 
27 The future of European competitiveness, Report by Mario Draghi, European Commission, commission.europa.eu/topics/eu-competitiveness/draghi￾report_en

## Page 24

24
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
A robust European common safe asset could encourage banks to diversify their sovereign 
portfolios, reducing reliance on any single sovereign and lessening the impact of potential 
sovereign debt crises. Denominated in euros, it would also mitigate cross-currency risks for 
European banks compared to non-EU sovereign bonds. Additionally, this common safe asset 
would promote financial development in the EU by introducing a new financial instrument with 
a different risk-return profile, supporting the creation of a unified securities market. Its attractive 
features could generate substantial domestic and international demand, enhancing the global role 
of the euro. This common safe asset could be structured in such a way that ensures it can serve as 
eligible collateral for margining purposes, similarly to government-issued debt. 
Despite several attempts to introduce such an asset, political and structural challenges have 
hindered the progress on further implementation. Examples include the conflicting views on fiscal 
risk sharing and concerns over moral hazards, as well as the risk of jurisdictions taking on excessive 
debt without consequences. However, one example stands out as a potential model for how such 
an asset could be successfully operationalized. During the pandemic, the EU issued €750 billion 
in common debt under the ‘Next Generation EU’ recovery fund, partially financed by EU bonds. 
While this fund was a temporary issuance with limited liquidity, it could be investigated as a 
successful model for mutualizing EU debt.
3.2 Stress Events
While margin requirements have been central to the post-financial crisis regulatory reforms, 
mitigating counterparty credit risk and promoting market resilience, market stress events can still 
trigger severe liquidity problems for certain market participants. When volatility spikes, margin 
calls can rise sharply and quickly increase the demand for cash, which is the preferred form of 
margin for banks and clearing houses. 
In a crisis scenario, a dash for cash often forces participants to liquidate assets, such as stocks and 
bonds, to meet margin calls, which can lead to price falls and instability across markets. The initial 
shocks can quickly spread, amplifying volatility and eroding liquidity in a procyclical feedback 
loop. One way to ease the demand for cash during these episodes is to temporarily expand the 
scope of eligible collateral that can be used to meet margin calls. For this approach to work, 
however, the industry needs a clear framework to identify when a stress event is occurring and to 
govern the temporary relaxation of collateral rules.
Determining the Occurrence of a Stress Event
The IFLD recommends gathering feedback from market participants on the various options to 
determine the occurrence of a stress event, including but not limited to those listed below. 
Even if a mechanism is chosen, the eventual stress event protocol could allow any bilateral 
counterparties to mutually agree on a different trigger mechanism between themselves, 
provided both have opted in to that approach. This flexibility would enable firms to tailor their 
arrangements if needed, without undermining the overall goal of a coordinated response.
Defining a stress event precisely and objectively is challenging, as crises vary in nature, scope and 
impact. The IFLD recommends ISDA should gather feedback on the possibility of both objective 
and subjective criteria relevant to this determination.

## Page 25

25
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
(i) Objective criteria: The IFLD proposes existing regulatory mechanisms should be leveraged 
as objective triggers for industry-wide relief. For example, under Article 6a (1) of EMIR, 
ESMA may ask the European Commission to suspend the clearing obligation in certain 
exceptional situations, such as the risk of disorderly functioning of financial markets. If 
such a suspension were to occur, it would signal that collateral-induced liquidity risk has 
grown so acute that even normal clearing requirements must be temporarily loosened. An 
official announcement by a regulator or authority invoking such emergency powers provides 
a clear, objective indication of severe financial stress and could serve as a logical trigger for 
temporarily expanding collateral eligibility.
(ii) Subjective criteria: Developing a commonly accepted subjective trigger is even more 
challenging, but certain market indicators can strongly suggest that a period of stress is 
present or underway. Such a subjective trigger could be met prior to any objective trigger 
– for example, because of a potential lag between the event occurring and regulators 
responding. These market indicators include: 
i. a sharp increase in market volatility across multiple asset classes;
ii. a significant tightening of liquidity conditions or other signs of a dash for cash among 
investors; 
iii. a rapid widening of credit spreads, reflecting increased risk aversion; 
iv. a substantial decline in asset prices signaling collapsing market confidence; or 
v. clear contagion effects, where stress in one market or sector is spilling over into others. 
However, assessing such subjective criteria in times of stress could cause confusion and increase 
the risk of litigation, so it is unlikely that subjective criteria can realistically be relied upon to 
determine whether a stress event has occurred.
The next question that arises is on the need to designate a determining party. Various options are 
considered below.
(i) Public Authority: Any subjective determination of a stress event would likely need to 
be made by public authorities, given their market oversight and the need for consistency. 
In this respect, the IFLD recommends empowering a supervisor that operates across 
jurisdictions or asset classes (eg, ESMA or the SEC), or an appropriate regulator or 
central bank (with jurisdiction over the relevant market) to declare when a stress event is 
occurring and for how long it continues. This would ensure uniform criteria and consistent 
application across markets, enhancing transparency and reducing potential disputes about 
whether extraordinary measures should be invoked. 
(ii) Calculation Agent: Individual counterparties could rely on the calculation agent in their 
contracts to make a subjective determination of whether a relevant stress event exists for 
that transaction, and if so for how long. This approach would enable parties to respond 
quickly in bilateral cases to deteriorating market conditions, but it would lack market-wide 
harmonization and could lead to inconsistent actions and the risk of disputes.

## Page 26

26
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
(iii) Industry Panel: though challenging to administer, especially in times where prompt 
action is warranted, an industry-wide stress event panel comprised of buy- and sell-side 
representatives (modeled on the ISDA Credit Derivatives Determinations Committees) 
could make collective judgments. A panel could respond faster and more uniformly than 
dispersed calculation agents, but it introduces governance complexity and would still 
require broad market acceptance of its authority. 
Expanding Collateral Eligibility and Backstop Facilities during a Stress Event
The IFLD recommends that after an announcement that a stress event has been triggered, there 
is an automatic expansion of the schedule of eligible collateral between market participants for 
the duration of the stress event (the ‘Springing Stress Event Collateral’). In practice, this means 
temporarily allowing a much broader set of assets to be posted as margin, subject to appropriate 
haircuts and conditions. 
This Springing Stress Event Collateral would be available to market participants for the duration 
of the relevant stress event. In the event of a severe stress scenario, market participants may 
temporarily accept forms of emergency collateral that would typically be ineligible or less 
favorable, by prioritizing liquidity risk management over standard collateral requirements. The 
expanded collateral menu would prioritize shoring up liquidity over the usual strict quality 
requirements – for example, accepting assets that are less liquid or carry higher credit risk than 
would be allowed in normal times – to stave off a systemic cash crunch. These extraordinary 
collateral measures would remain in force only while the stress event persists, reverting to standard 
eligibility once conditions stabilize. 
In parallel, authorities should be prepared to activate emergency liquidity facilities to support the 
market. A central bank or supervisor’s declaration of a stress event could unlock or broaden access 
to lender-of-last-resort programs specifically tailored for NBFIs and margin financing needs. For 
example, the Bank of England’s recently introduced Contingent NBFI Repo Facility is designed to 
provide repo funding against gilts for NBFIs facing liquidity strains. Such facilities, combined with 
private measures like expanded collateral eligibility, form a powerful toolkit to prevent disorderly 
market dynamics. Notably, temporary collateral expansions during crises can sometimes pave the 
way to considering the adoption of permanent changes once their efficacy is proven. For example, 
ESMA’s emergency decision to accept bank guarantees as collateral for non-financial energy firms 
in late 2022 provided relief during the energy crisis and this practice was later formalized under 
EMIR 3.0 for CCP clearing. In this way, what begins as a contingency measure can evolve into an 
accepted market norm, further diversifying the collateral pool in the long run. 
CASE STUDY: During a severe liquidity crunch at the time of the financial crisis in 2008, the 
European Central Bank temporarily expanded its eligible collateral list to support funding 
markets. In an unprecedented move, policymakers began accepting a much wider range 
of assets – including lower-rated securities – at the central bank’s lending window to inject 
liquidity. This emergency expansion of collateral eligibility dramatically increased banks’ 
access to cash, peaking at more than €700 billion in loans, and stabilized interbank lending. 
This episode underscores how broadening acceptable collateral in crisis times can unlock 
vital liquidity, albeit with careful risk management to eventually unwind those measures. 
Many central banks took similar actions in response to the market volatility at the start of the 
pandemic in March 2020.

## Page 27

27
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
Stress Event Protocol
To facilitate adoption of these recommendations, the IFLD proposes that ISDA should develop a 
voluntary industry agreement that firms can adhere to in advance of any stress event. This would 
be known as a ‘stress event protocol’. 
The protocol would serve as the operational guidance for implementing collateral expansions 
during a stress event. Adhering parties would commit to the framework and gain the option 
to exchange Springing Stress Event Collateral with other adherents if a stress event is declared. 
Critically, the protocol should allow each firm to pre-select which types of collateral it is willing to 
both post and accept under stress conditions. 
The effective eligible collateral exchanged between counterparties would then be the intersection 
of their selections – ie, only those asset types that both parties have opted into via the protocol. 
This ensures that, even in a broad stress scenario, no firm is forced to take a form of collateral it 
cannot prudently manage or does not wish to handle. Participation would be elective: only those 
institutions confident in their risk management and operational capacity for expanded collateral 
would adhere, while others could choose to rely on conventional measures.
3.3 Conclusion
These proposals for expanding eligible collateral and establishing contingency measures during 
severe market stress are intended to spark dialogue and further analysis among market participants, 
regulators and industry groups. These tools could significantly bolster the resilience of the 
derivatives market by alleviating liquidity squeezes and preventing fire-sale dynamics. However, 
they must be carefully standardized and governed to avoid unintended consequences. 
Any dynamic expansion of collateral should be viewed as a strict temporary safety valve – used 
only in well-defined crisis conditions – and not as a replacement for maintaining high-quality 
collateral in normal market conditions. With prudent implementation, expanding the collateral 
liquidity pool both in business-as-usual times and under stress can transform collateral from a 
point of vulnerability into a cornerstone of systemic resilience.

## Page 28

28
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
4. USING TECHNOLOGY TO SUPPORT OPTIMIZATION 
AND RESILIENCE
Emerging technologies provide a way to significantly improve the transparency of collateral 
positions, the mobility of assets and the automation of collateral management. By leveraging these 
innovations, market participants can reduce liquidity constraints, streamline collateral workflows 
and build more robust buffers against systemic shocks. This can support enhanced collateral 
mobility and streamlined regulatory compliance, contributing to a more transparent and resilient 
financial system. 
This section explores key technologies driving this transformation – DLT, the CDM, cross-chain 
interoperability solutions, agentic AI, and asset tokenization – and emphasizes the need to pursue 
long-term innovation while implementing short-term solutions to bridge legacy infrastructure. 
Key components of this transformation include:
1) Next-generation collateral architecture: A new collateral management architecture built 
on the CDM and DLT, allowing assets to move seamlessly across different platforms and 
blockchain networks;
2) Asset tokenization: Converting traditional securities and non-traditional assets into digital 
tokens, thereby expanding the universe of eligible collateral; 
3) Agentic AI automation: Deploying autonomous AI agents to optimize collateral decisions, 
dispute resolution and process automation in real time. 
4.1 Building a New Collateral Management Architecture
A modern collateral infrastructure is emerging, with common data standards and distributed 
ledgers at its core. At the center sits the CDM, which provides a standardized, machine-readable 
representation of trades, lifecycle events, documentation and collateral assets/eligibility terms 
representation, which leads to efficiency for processes (eg, margin calls, portfolio reconciliation). 
By ensuring all participants speak the same data language, the CDM eliminates ambiguity and 
enables interoperability between systems. 
On this foundation, DLT replaces fragmented, intermediary-driven processes. Instead of 
waiting for end-of-day or T+1 settlements, collateral transfers can occur almost instantaneously, 
dramatically improving liquidity utilization. Embedding compliance checks into DLT smart 
contracts can further ensure that only eligible collateral is transferred, reducing operational errors 
and the risk of regulatory breaches. 
Finally, cross-chain interoperability acts as the connective tissue linking various blockchain 
networks. With effective interoperability protocols, collateral tokenized on one network can be 
recognized and mobilized on another without manual reconciliation or duplicative capital buffers. 
Secure cross-chain bridges or similar solutions preserve the integrity of transfers between ledgers, 
preventing fragmentation as different platforms adopt DLT.

## Page 29

29
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
Industry pilots already demonstrate these benefits. For example, ISDA has launched a pilot to 
implement the CDM for the clearing of interest rate derivatives on the blockchain using DAML, 
an open-source smart contract language enhancing standardization, transparency and efficiency28, 
achieving streamlined, transparent workflows. As firms continue to invest in common standards 
and ledger integration, collateral will be able to flow more freely across a harmonized, resilient 
ecosystem.
CASE STUDY: Innovative projects are tackling the challenge of interoperability between 
different blockchain networks. In one 2022 proof of concept, a group of major banks and 
financial technology firms executed a cross-chain repo transaction that atomically swapped 
digital cash on one ledger for digitized securities on another. The pilot linked two separate 
DLT platforms – one for a tokenized payment asset and another for a digital collateral 
registry – and successfully achieved deliver-versus-payment settlement across chains. This 
marked the first instance of an intraday repurchase agreement being settled simultaneously 
on interoperable blockchains, hinting at a future where collateral and liquidity can flow 
seamlessly through interconnected networks. If adopted at scale, the ability to bridge 
systems in this way could increase collateral portability across markets and timezones.
4.2 Tokenization: Expanding and Mobilizing the Collateral Pool
Tokenization refers to creating digital representations of real-world assets on a blockchain. In a 
tokenized system, traditional assets such as government bonds, equities or even alternative assets 
are converted into digital tokens that carry the same value and rights as the underlying asset. This 
approach can greatly enhance transparency, as each token’s ownership and transaction history are 
recorded on a shared ledger, and improve operational efficiency by enabling faster, automated 
transactions. By unlocking fractional ownership, tokenization can also create new markets 
(for example, by allowing a large asset to be divided among many holders), thereby improving 
liquidity29. 
The derivatives market has started to lay the legal and operational groundwork for tokenized 
collateral. In 2023, ISDA published the Tokenized Collateral Model Provisions to help parties 
include tokenized securities or stablecoins as eligible collateral under standard derivatives collateral 
agreements (eg, the ISDA credit support annex)30. Recognizing that novel issues arise with on￾chain assets – such as how to establish legal finality of a blockchain transfer – ISDA followed 
up with a 2024 Guidance Note on Tokenized Collateral31. This guidance note provides a basic 
taxonomy of tokenization structures and outlines key legal considerations across jurisdictions for 
using tokenized assets as collateral. These efforts aim to ensure that as markets adopt tokenization, 
the contractual and legal frameworks keep pace.
28 ISDA and Digital Asset Launch CDM Clearing Pilot Using DAML, ISDA, October 6, 2020, www.isda.org/2020/10/06/isda-and-digital-asset-launch-cdm￾clearing-pilot-using-daml
29 Recommendations to Expand Use of Non-cash Collateral Through Use of Distributed Ledger Technology, CFTC Global Markets Advisory Committee, 
November 21, 2024, www.cftc.gov/media/11581/GMAC_DAM_UseofDLTasDerivativesCollateral_112124/download
30 Tokenized Collateral Model Provisions for Inclusion in ISDA 2016 Credit Support Annexes for Variation Margin (VM), ISDA, www.isda.org/book/tokenized￾collateral-model-provisions-for-vm-csa 
31 ISDA Tokenized Collateral Guidance Note, ISDA, May 21 2024, www.isda.org/2024/05/21/isda-tokenized-collateral-guidance-note

## Page 30

30
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
Early implementations of tokenized collateral are already demonstrating improved mobility 
and speed. For example, in late 2023, a major trading platform enabled shares of an MMF 
to be tokenized and pledged as collateral for derivatives margin calls32. This pilot showed that 
delivering collateral as digital tokens can significantly cut down settlement times of margin calls. 
Meanwhile, several large banks in Europe have used a permissioned DLT platform to tokenize 
and swap bond positions held at custodians in real time. By exchanging tokenized entitlement 
instead of physically moving securities, they effectively eliminated the normal two-day settlement 
lag associated with reallocating HQLA. Additionally, post-trade infrastructure providers have 
partnered to achieve cross-platform atomic settlement. One pilot successfully executed a repo 
transaction across two different DLT networks using central bank digital currency, ensuring 
instant delivery-versus-payment for tokenized collateral. 
Beyond these examples, tokenization has broad transformational potential to diversify and enlarge 
the pool of assets available for collateral. In repurchase agreements and securities lending, for 
instance, HQLA such as government bonds and blue-chip stocks can be converted into tokens 
and traded for cash almost instantly, avoiding the frictions of current settlement. Tokenized MMF 
shares offer another use case: rather than redeeming shares for cash to meet a margin call, a fund 
investor could pledge tokenized shares directly, allowing the posting party to retain its investment 
and yield.
Even traditionally illiquid assets, such as real estate, infrastructure investment, commodities and 
fine art, could become acceptable collateral if tokenized and made subject to transparent valuation 
and legal safeguards. For example, a portfolio of commercial real estate loans could be tokenized 
and pledged in a financing transaction, with smart contracts automatically monitoring valuations 
and enforcing security interests. By reducing the time required for due diligence and improving 
traceability, this kind of innovation might enable banks to lend against asset classes that were 
previously difficult to leverage. However, incorporating such novel assets will require robust risk 
management tools to handle their unique risks. 
CASE STUDY: A consortium of financial institutions recently demonstrated near-instant 
collateral transfers using blockchain technology. In mid-2023, an industry pilot created digital 
tokens representing government bonds and used them to satisfy margin calls in real time 
on a privacy-enabled distributed ledger. The exercise proved that a ‘digital twin’ of a high￾quality asset could be pledged then rapidly recalled, with clear ownership tracked on-chain 
even in a default scenario. This real-world trial of DLT showcased the potential for atomic 
settlement of collateral – where posting and returning margin can occur within seconds, 
vastly improving collateral mobility and reducing settlement risk.
4.3 Agentic AI: Autonomous Optimization of Collateral Processes
While today’s generative AI tools focus on producing outputs from learned data patterns, agentic 
AI represents the next step – AI agents capable of making autonomous decisions to achieve 
specified goals. In the context of collateral management, agentic AI systems can dynamically 
manage collateral workflows end-to-end with minimal human intervention. These AI agents could 
continuously monitor market conditions, predict needs and execute tasks to ensure collateral 
moves optimally through the system, thereby enhancing speed and resilience in times of stress.
32 JP Morgan’s tokenised collateral platform sees first live settlement through BlackRock and Barclays, The Trade, October 11, 2023, www.thetradenews.
com/jp-morgans-tokenised-collateral-platform-sees-first-live-settlement-through-blackrock-and-barclays/

## Page 31

31
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
Agentic AI has the potential to augment each stage of the collateral lifecycle. At the pre-trade 
and allocation stage, an AI agent could analyze a firm’s available assets, prevailing market prices 
and counterparty credit exposures in real time to recommend the ideal collateral to post for a 
given trade. It could factor in constraints like eligibility, haircuts and concentration limits much 
faster than a human, improving both efficiency and risk mitigation. During the agreement and 
dispute resolution stage, agentic AI could automatically reconcile discrepancies between parties 
by referencing agreed-upon valuation models and legal frameworks, such as the terms of ISDA 
agreements. For example, if there was a valuation dispute on a collateral call, the AI agent could 
identify the divergence and propose a resolution or adjustment immediately, without waiting for a 
lengthy human negotiation.
In the margin calculation and collateral selection stage, agentic AI systems could interface with 
smart contracts to transfer collateral instantly once conditions are met, ensuring settlements occur 
seamlessly and in compliance with regulatory requirements. They would track the status of each 
collateral movement, adapting to any sudden changes in market conditions or liquidity needs – for 
example, rerouting or substituting collateral if a particular asset becomes scarce or volatile. Finally, 
in the post-trade stage, these AI agents could continuously stress test and rebalance collateral 
portfolios. 
By simulating market shocks and forecasting future margin calls, an AI agent can preemptively 
suggest topping up collateral or reallocating assets, thereby reducing the likelihood of last￾minute scrambles or fire sales during a crisis. Notably, agentic AI could also work in tandem with 
tokenization initiatives: as firms start pledging tokenized assets, AI-driven algorithms will be 
essential to assess real-time fair value, monitor on-chain metrics and manage the unique risks of 
digital tokens. In short, agentic AI has the potential to act as an intelligent control tower that not 
only automates routine decisions but also learns and adapts, ultimately reinforcing the stability of 
the collateral system.
CASE STUDY: Firms are also exploring AI to enhance collateral processes. For example, 
several large dealers are piloting AI-driven tools to automate margin call handling and 
dispute resolution, replacing the traditionally email-heavy workflow of margin calls with 
intelligent systems that interpret and respond to calls instantly. Early efforts in this area aim 
to not only speed up margin agreements and reduce operational friction, but also to predict 
funding stresses before they occur. By analyzing historical patterns, machine learning models 
can forecast when and where collateral pressures might arise, allowing treasury teams to 
proactively position assets. While still in their nascent stages, these technologies – along with 
cloud-based data standards like the CDM – promise a future of smarter, more transparent 
collateral management. One bank’s experience already shows progress. It deployed AI 
bots to perform routine collateral data entries and reconciliations, achieving a notable 
drop in manual errors and processing time. Such technology-driven innovation is gradually 
transforming collateral from a manual, reactive task into an optimized, predictive discipline.
4.4 Short-term Efficiency Fixes While DLT Matures
While these emerging technologies offer a compelling long-term vision, full-scale adoption across 
the industry will take time, and many institutions continue to operate on legacy infrastructures. 
To bridge this gap, firms could pursue a range of short-term efficiency fixes using existing 
technology, bringing immediate benefits in collateral management without waiting for full-scale 
digital transformation:

## Page 32

32
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
1) Real-Time Data Feeds for Improved Collateral Visibility: Integrate live data feeds to gain 
a better view of collateral holdings across custodians, CCPs and trading desks. Having a 
consolidated, real-time inventory reduces the chance of excess collateralization and enables 
more proactive liquidity management.
2) API-driven System Integration: Use Application Programming Interfaces (APIs) to connect 
siloed trading, risk and collateral management systems. Seamless data sharing between trade 
execution platforms, risk analytics and collateral optimization tools can eliminate lag time 
in margin calls and allocations. The CDM will make such integration easier by ensuring all 
systems interpret the data consistently.
3) Automated Margin Calls to Reduce Manual Processing: Implement automation for 
routine collateral processes such as margin calls and interest payments. For instance, margin 
calls can be automatically triggered and fulfilled based on real-time portfolio valuations 
without waiting for human intervention, minimizing operational delays and errors. In 
practice, vendors offer tools that already facilitate these automated margin workflows.
4.5 Conclusion
Modernizing collateral management is not just a theoretical exercise but an essential step to adapt 
to an increasingly complex and digitized financial landscape. Embracing technologies like DLT, 
CDM, cross-chain interoperability, agentic AI and tokenization can fundamentally improve how 
collateral is mobilized and managed, while bolstering liquidity efficiency and reducing systemic 
risk in the long run. 
Full-scale adoption of the new collateral ecosystems will take time and funds, but financial 
institutions can achieve immediate efficiency gains in the interim. Measures such as real-time data 
integration, centralized collateral inventory tracking and API-enabled connectivity streamline 
collateral operations and help lay the groundwork for a fully digital, automated future framework.

## Page 33

33
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
5. IFLD RECOMMENDATIONDS
The derivatives market must grapple with a structural risk triangle of three interlinked risks 
– market risk, counterparty credit risk and liquidity risk. Efforts to mitigate any one of these 
dimensions in isolation could unintentionally increase pressure on the others. This delicate 
balance is further strained by market fragmentation – a patchwork of siloed systems and divergent 
regulations that hinders efficient collateral flows. In such a fragile environment, maintaining 
stability requires a holistic approach.
Collateral optimization has emerged as a key strategy to strengthen liquidity efficiency. This 
whitepaper posits that firms should recalibrate how they post and manage collateral to reduce 
margin inefficiencies and funding costs without eroding risk safeguards. This means actively 
rebalancing portfolios and making greater use of bilateral and multilateral optimization, 
consolidating collateral management functions and extending cross-product, cross-CCP margining 
frameworks. 
At its core, optimizing collateral is about balancing cost efficiency with robust risk management 
– requiring smarter collateral sourcing, improved market access, better margin management and 
stronger governance practices. By instituting these practices, market participants can lower the 
drag of collateral demands while bolstering overall resilience in a margin-intensive environment.
In parallel, collateral diversification is essential to address systemic liquidity risk. This whitepaper 
considers broadening the pool of acceptable collateral beyond traditional HQLA, incorporating 
non-traditional forms such as MMFs, guarantees, tokenized assets and even emissions credits. 
Expanding eligibility in this way can unlock additional liquidity buffers, though it demands robust 
valuation, legal and operational frameworks to ensure these new assets can be reliably valued and 
swiftly mobilized. This diversification, if carefully managed, could ease the strain on scarce cash 
and government bonds during crises, enhancing the shock-absorbing capacity of the market’s 
collateral architecture and increasing the depth of derivatives markets.
At the same time, technological modernization of market infrastructure is highlighted as a pivotal 
enabler of both optimization and diversification. Advanced technology can streamline collateral 
mobility and transparency across the fragmented ecosystem. For example, DLT promises near 
real-time settlement of margin calls, the CDM standardizes data across platforms and agentic AI 
can automate tasks like dispute resolution, stress testing and predictive liquidity management. 
Similarly, cross-chain interoperability and tokenized asset networks offer new avenues for moving 
collateral seamlessly across systems. By upgrading legacy systems with these innovations, the 
industry can reduce operational bottlenecks and build an adaptive infrastructure that responds 
fluidly to stress.
Ultimately, safeguarding the derivatives market’s stability will require coordination and 
commitment among stakeholders. Success hinges on collaboration: regulators must balance 
prudence with flexibility, institutions must prioritize harmonization and interoperability, and 
technologists must bridge the gap between legacy systems and cutting-edge tools. Through such 
coordinated action – involving policymakers, market participants, and infrastructure providers – 
the industry can transform collateral from a point of vulnerability into a cornerstone of systemic 
strength. These collective efforts lay the groundwork for a more adaptive, harmonized market that 
can withstand future shocks while preserving market integrity.

## Page 34

34
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
In line with this analysis, the IFLD makes the following recommendations to help navigate risks 
in this fragile environment and enhance collateral and liquidity efficiency.
• Increase participation in collateral optimization programs: Encourage broader use of both 
multilateral and bilateral optimization services to reduce duplicate margin and improve overall 
efficiency in collateral usage.
• Leverage financing markets for collateral needs: Use repo and other securities financing 
transactions to mobilize collateral more flexibly, easing the process of meeting margin calls 
under stress.
• Support cross-margining innovations: Encourage CCPs to invest in cross-product margining 
initiatives (and explore cross-CCP margining) that expand netting opportunities and reduce 
aggregate collateral requirements across cleared portfolios.
• Continuously refine collateral management practices: Periodically review and update internal 
collateral management processes and optimization strategies to adapt to evolving market 
conditions, technologies, regulations and best practices.
• Expand eligible collateral through partnerships: Engage in bilateral negotiations and industry 
agreements to expand collateral eligibility schedules between firms, broadening the range of 
assets accepted as margin by counterparties.
• Broaden acceptance of MMFs: Advocate for regulatory and policy changes that allow highly 
liquid instruments like MMFs to be included as eligible collateral, thereby diversifying available 
liquidity sources.
• Deliberate expansion of guarantee eligibility as collateral: Standardizing documentation and 
facilitating resolutions via industry coordination, enhancing flexibility and legal clarity.
• Consider CP eligibility: Support standardization, secondary market liquidity and centralized 
data to enhance the suitability of CP as collateral.
• Explore the broader use of emission certificates: Standardize global regulatory frameworks, 
harmonize collateral rules for emission certificates, develop consistent accounting standards for 
carbon credits and reduce capital charges to support the broader use of emission certificates in 
financial markets.
• Promote deeper non-bank liquidity pools: Push for the development of deeper and more liquid 
markets in assets such as high-grade corporate debt, so that these instruments can reliably serve 
as collateral without disrupting market stability.
• Recognize digital sovereign debt as collateral: Work with regulators to clarify that tokenized 
sovereign debt (native digital asset bond issuances) is permissible collateral, aligning the 
treatment of these assets with traditional government securities and unlocking new liquidity 
channels.
• Advocate for the digitization of the issuance process of corporate debt (eg, golden source data 
and automated end-to-end processing): Faster digital issuance or re-opening of issued debt 
instruments will improve overall liquidity and transparency, thereby improving their usability as 
collateral.

## Page 35

35
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
• Consider a standardized stress event protocol and emergency collateral framework: Explore the 
development of an industry-standard stress event protocol that enables the temporary expansion 
of eligible collateral schedules during periods of systemic stress. This protocol should define 
clear, objective triggers for activation and allow consenting parties to exchange broader forms of 
collateral, including guarantees and non-traditional instruments, under pre-agreed conditions. 
The protocol should be complemented by central bank contingency facilities where appropriate, 
ensuring a coordinated and proportionate response to market-wide liquidity dislocations.
• Integrate advanced AI in the collateral lifecycle: Consider generative and agentic AI solutions to 
automate collateral processes (eg, eligibility checks, valuations, dispute resolution), which can 
reduce operational costs and errors while speeding up response times.
• Implement cross-chain settlement solutions: Use cross-chain interoperability technologies to 
connect disparate DLT platforms, accelerating the adoption of blockchain-based collateral 
settlement and reducing settlement delays.
• Adopt common data standards with AI support: Accelerate industry-wide adoption of standard 
data models like the CDM, leveraging AI tools to streamline implementation and maintenance 
– a step that enhances transparency and interoperability while lowering long-term costs.
Only through coordinated innovation – optimizing collateral practices, diversifying assets and 
modernizing infrastructure – can the derivatives market navigate the triad of risks and emerge as a 
more liquid, efficient and resilient market.

## Page 36

36
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
6. APPENDIX 
List of Contributors
Firm Name
AllianceBernstein Amanda Streeter
APG Asset Management Koen Ottenheijm
AXA Investment Managers Charles-Edouard Rakotoarison
Bank of America Cairistiona Simmonds
Barclays Celina Bulk
BlackRock Jojo Yan
BNP Paribas Ann-Marie Myhill
Citi Maddie Parmar
Citi Namrata Praveen
Crédit Agricole CIB Andrea Cavone
D. E. Shaw & Co., L.P. James Goodall
DBS Bank Mariana Lesmana
Deutsche Bank Piuli Roy-Chowdhury
Eurex Michael Hildebrand
Goldman Sachs Shamira Sendegala
HSBC Jakir Alam
Intercontinental Exchange Helen Fermor
King & Wood Mallesons Claire Warren
Landesbank Baden-Württemberg Christian Hering
LSEG Post Trade Solutions Sean Funke
MetLife Insurance Investments Will Hua
Mizuho International Plc Maksym Volkov
Morgan Stanley Simon Lafrance
NatWest Markets Jon Anderson
OSTTRA Greta Graziani
Royal Bank of Canada David Young
RWE Sebastian Kiris
Standard Chartered Xiaobo Liu
UBS Joakim Sorensen
Wilmer Cutler Pickering Hale and Dorr LLP Megan O’Flynn
XP Inc. Georgia Cazarré

## Page 37

37
FUTURE LEADERS IN DERIVATIVES
Collateral and Liquidity Efficiency in the Derivatives Market: Navigating Risk in a Fragile Ecosystem
ABOUT THE IFLD
The ISDA Future Leaders in Derivatives (IFLD) program aims to make a positive impact on the 
future of the derivatives industry by identifying a diverse group of emerging leaders across the 
industry. The program has four core objectives: to create an active forum for networking and 
discussion of industry topics and future industry trends; to increase the demographic, cultural and 
professional diversity of senior leaders within the financial services sector; to support emerging 
leaders in developing soft skills and technical expertise; and to develop and produce content on 
issues of strategic importance to ISDA and its members. For more information on the IFLD 
program, please contact IFLD@isda.org.
ABOUT ISDA
Since 1985, ISDA has worked to make the global derivatives markets safer and more efficient. 
Today, ISDA has over 1,000 member institutions from 76 countries. These members comprise 
a broad range of derivatives market participants, including corporations, investment managers, 
government and supranational entities, insurance companies, energy and commodities firms, 
and international and regional banks. In addition to market participants, members also include 
key components of the derivatives market infrastructure, such as exchanges, intermediaries, 
clearing houses and repositories, as well as law firms, accounting firms and other service providers. 
Information about ISDA and its activities is available on the Association’s website: www.isda.org. 
Follow us on LinkedIn and YouTube.
