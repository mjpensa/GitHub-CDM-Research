# Guidelines for Smart Contracts CDS

*Converted from: Guidelines-for-Smart-Contracts-CDS.pdf*

---

## Page 1

ISDA Legal Guidelines for Smart Derivatives Contracts: 
Credit Derivatives

## Page 2

2
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
Contents 
Disclaimer ................................................................................................................................ 3 
Introduction .............................................................................................................................. 4 
Building the foundation for Smart Derivatives Contracts ......................................................... 5 
Constructing Smart Derivatives Contracts ............................................................................... 7 
The Credit Derivatives Market .................................................................................................9 
Understanding Credit Derivatives .......................................................................................... 12 
Cash flows and key events under a typical credit derivative ...................................... 12 
Other Intervening Events ........................................................................................... 13 
Understanding key market documentation ................................................................. 13 
Credit Derivatives lifecycle events ......................................................................................... 15 
Premium ..................................................................................................................... 15 
Triggering ................................................................................................................... 15 
Settlement .................................................................................................................. 19 
Index CDS .............................................................................................................................. 22 
Considerations for technology developers ............................................................................. 25 
Clearing .................................................................................................................................. 28 
CCP Rules ................................................................................................................. 28 
Client clearing arrangements ..................................................................................... 29 
CCP discretion in respect of cleared products ........................................................... 31 
Reporting ............................................................................................................................... 33 
Conclusion ............................................................................................................................. 35 
Acknowledgement .................................................................................................................. 36

## Page 3

3
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
Disclaimer 
The purpose of these guidelines is to provide an introduction to credit derivatives for readers 
who are designing and implementing technological solutions for them. The intention of this 
paper is not to specify or recommend any particular technological application or project. 
Rather, these guidelines intend to provide an overview of the legal and documentary 
framework used for credit derivatives transactions and to highlight certain issues that 
developers may wish to consider. This paper is intended to help developers tailor appropriate 
technology solutions for the credit derivatives market. 
These guidelines discuss a number of legal issues. These discussions are intended to provide 
general guidance, not legal advice, and to promote a better understanding of the basic 
principles that underpin documentation produced by the International Swaps and Derivatives 
Association ("ISDA"). In practice, the law relating to derivatives transactions and the legal 
documentation that governs them is complex, it may change over time due to evolving case 
law and new regulations and it may vary substantially from jurisdiction to jurisdiction. 
In presenting this material, an assumption is made that certain terms in ISDA documentation 
relevant to credit derivatives are capable of being (and may currently be) represented in 
computer code or performed by or on a technology platform. For example, payment-related 
provisions that require one party to pay another an amount that is calculated on the occurrence 
of a certain event may be suited to codification or automated processing. This paper also 
assumes that some provisions within such ISDA documentation may not be as well suited or 
efficient to code and will remain as written in the contract. 
These guidelines do not represent an explanation of all relevant issues or considerations in a 
particular transaction, technology application or contractual relationship. These guidelines do 
not constitute legal advice. Parties should therefore consult with their legal advisors and any 
other advisor they deem appropriate prior to using any standard ISDA documentation. ISDA 
assumes no responsibility for any use to which any of its documentation or any definition or 
provision contained therein may be put. 
Unless otherwise defined or the context otherwise requires, capitalized terms used in these 
guidelines have the meanings given to them in the relevant ISDA document.

## Page 4

4
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
Introduction 
Since its foundation in 1985, ISDA has consistently sought to promote efficiencies and cost￾savings through improvements to processes for the settlement and management of lifecycle 
events related to a variety of derivatives products. Today, as new technologies are developed 
and implemented across the financial markets, the derivatives industry is increasingly seeking 
to achieve even greater efficiencies and cost-savings through the deployment of such 
technologies. 
In response, ISDA has published a series of Legal Guidelines for Smart Derivatives Contracts. 
The purpose of these guidelines is to support technology developers and other key 
stakeholders in the development of smart derivatives contracts by explaining the core 
principles of ISDA documentation, and raising awareness of the important legal and regulatory 
issues that developers and other relevant stakeholders should consider when developing and 
deploying such solutions within the derivatives market. 
This paper focusses on the application of such technology solutions to the credit derivatives 
market. These guidelines will: 
 provide high-level background on the credit derivatives market; 
 identify opportunities for the potential application of smart contract technology 
to credit derivatives; and 
 highlight important issues for technology developers to consider when 
designing technology-enabled solutions for trading and processing credit 
derivatives and associated processes. 
A number of technology-based initiatives working towards greater standardization and 
automation of the derivatives market have already been developed and implemented. There 
are opportunities to build on this further by harnessing new technologies, such as smart 
contracts and distributed ledger technology ("DLT"), in order to provide scalable, cost-efficient 
and more accurate technology solutions within the credit derivatives market. 
While the intention of this paper is not to specify or recommend any particular approach or to 
address any particular technological application or project, these guidelines do identify areas 
where existing legal and regulatory standards are likely to influence system design and 
implementation. These guidelines also highlight areas where further industry collaboration will 
be required to identify existing areas of legal and regulatory uncertainty and to develop 
solutions.

## Page 5

5
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
Building the foundation for Smart Derivatives Contracts 
On 28th July 2020, ISDA and several other trade associations sent a letter to the Financial 
Stability Board, IOSCO and the Bank for International Settlements asserting our joint 
commitment to defining and promoting the development of a digital future for financial 
markets.1 The benefits of digitization for market participants are clear. Increased and more 
widespread implementation of automated, straight-through processing of financial 
transactions will increase efficiency and reduce costs for market participants. Digitization will 
promote the consistent creation, processing and aggregation of global financial data, 
bolstering regulatory oversight and compliance. Through the removal of redundancy and 
unnecessary complexity, increased digitization and automation will strengthen the operational 
resilience of market participants and financial markets infrastructure, reducing systemic risk 
and creating a safer and more robust global financial system. 
None of this is possible without industry-led development of essential data standards and the 
distribution of these standards in digital formats to allow direct deployment within enhanced, 
automated and intelligent processes, systems and technology. 
The letter sets out a series of principles and objectives aimed at promoting the development, 
distribution and adoption of digital standards within the financial markets, creating the 
foundation for transformational change in our industry. These principles and objectives 
address three key areas: Standardization, Digitization, and Distribution. 
ISDA’s Digitization Initiatives
ISDA is currently working on a number of initiatives to deliver enhanced standardization and 
digitization of industry-standard derivatives documentation.2 In the interest rate market, for 
example, ISDA will develop and publish a new definitional booklet in digital format and make 
it available through an online platform. 
ISDA has also developed the ISDA Common Domain Model (CDM), which establishes a 
common, digital representation of derivatives life-cycle events described within ISDA 
documentation. The CDM creates a common set of process and data standards that will 
1 https://www.isda.org/a/MGmTE/Digital-Future-for-Financial-Markets-Letter.pdf 2 See, for example, the ISDA Clause Library: https://www.isda.org/2020/06/23/isda-launches-clause-library/

## Page 6

6
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
increase automation and efficiency in the derivatives market. The CDM currently contains full 
representations for credit derivatives, in addition to other products and derivatives processes.3
Refinement and expansion of these models will facilitate greater connectivity between 
contractual terms and the processes designed to implement important business and 
operational functions deriving from contracts, including netting and collateral enforceability, 
liquidity, and counterparty credit-risk. All of this will help move the industry towards more 
efficient, cost-effective and scalable payment, settlement, collateral management and 
regulatory processes, providing a robust foundation for straight through processing of financial 
transactions. 
These enhanced standards will also enable the development and implementation of 
innovative, automated and intelligent technology solutions. Common, shared representations 
of data are required in order for distributed ledger technology to operate effectively. It is upon 
these distributed platforms and data structures that executable and autonomous code within 
smart contracts can be developed and deployed effectively and efficiently across the financial 
markets. The aggregation of large, structured data sets will also accelerate the use of AI￾based technology solutions, with potential applications across numerous business, risk 
management and regulatory compliance functions. 
Using these enhanced standards as a foundation, technology developers can then deploy 
automated business logic in a way that draws upon the CDM to facilitate specific functionality. 
For example, market participants could use the CDM to implement a common underlying 
digital representation for the calculation of settlement amounts under a credit derivative and 
to design and run a process that automatically carries out a calculation (possibly taking 
necessary data from external sources, such as the relevant Determinations Committee) and 
makes the relevant payment. 
3 https://www.isda.org/2019/03/20/isda-publishes-cdm-2-0-for-deployment-and-opens-access-to-entire-market/

## Page 7

7
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
Constructing Smart Derivatives Contracts 
In October 2018, ISDA and King & Wood Mallesons jointly published a white paper entitled 
"Smart Derivatives Contracts: From Concept to Construction."4
This paper proposed a practical framework for the construction of smart derivatives contracts. 
As part of this framework, the paper suggests that the first step toward the construction of a 
smart derivatives contract is the selection of those parts of a derivatives contract for which 
automation would be: 
 effective, which involves determining the parts of a contract for which automation is 
possible; and 
 efficient, which involves determining those parts of a contract for which automation 
delivers sufficient benefit. 
Effective Automation 
In 2017, ISDA and Linklaters jointly published a white paper entitled "Smart Contracts and 
Distributed Ledger – A Legal Perspective."5
This paper notes that derivatives are fertile territory for the application of smart contracts and 
DLT because their main payments and deliveries are typically operational in nature, and thus 
heavily dependent on conditional logic. As a result, they are highly suitable to being machine￾automated or analysed in some way. The paper illustrates how one might express these 
operational provisions in a more formalized form and break them down into components for 
representation as functions within the ISDA CDM. Developers can then combine these 
functions with other functions to create templates for use with particular derivatives products, 
including credit derivatives. 
Efficient Automation 
There are a number of opportunities for delivering considerable efficiency benefits through 
greater automation of the credit derivatives market. 
First, as mentioned above, the operational processes involved in calculating and settling 
payment and delivery obligations are likely to lend themselves well to automation and to 
deliver real efficiencies and cost-savings as compared with existing payment infrastructures. 
Additionally, the impact of regulatory change on the credit derivatives market (particularly 
mandatory clearing and transaction reporting) has caused firms to implement new or amended 
processes across the front-to-back transaction lifecycle in order to ensure ongoing regulatory 
compliance. Increased automation can delivery greater efficiency and cost-savings in these 
areas. 
4 See ISDA's Whitepaper on "Smart Derivatives Contracts: From Concept to Construction" available at: 
https://www.isda.org/a/cHvEE/Smart-Derivatives-Contracts-From-Concept-to-Construction-Oct-2018.pdf. 5 See ISDA, Smart Contracts and Distributed Ledger: A Legal Perspective" available at: 
https://www.isda.org/a/6EKDE/smart-contracts-and-distributed-ledger-a-legal-perspective.pdf.

## Page 8

8
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
These guidelines will explore each of these areas, identifying opportunities for greater 
automation and highlighting key considerations for technology developers who are creating 
technology solutions in response.

## Page 9

9
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
The Credit Derivatives Market 
The key characteristic of credit derivatives is that parties make payments thereunder by 
reference to the creditworthiness of a particular "Reference Entity," "Reference Obligation" or 
group thereof. One of the parties to the transaction will be a purchaser of credit protection and 
the other will be a seller of credit protection. The credit derivative therefore transfers credit risk 
on the relevant Reference Entity from protection buyer (“Buyer”) to protection seller (“Seller). 
Market participants often use credit derivatives to hedge exposure to a particular piece of debt 
or economic sector. They may also use credit derivatives to take short or long positions as 
part of a broader investment strategy. 
While the market encompasses a range of products, some of which are highly bespoke, by far 
the most popular and important product is the credit default swap (“CDS”). Due to a series of 
industry initiatives, a highly standardised market exists for CDS on commonly traded 
Reference Entities6. As such, the CDS market represents perhaps the most standardized of 
all derivatives asset classes, and any technological solution addressing market standard 
contracts is likely to benefit from a high level of scalability. 
However, while the CDS market is highly standardized, the determinations required even for 
market standard contracts can be relatively complex. These determinations are discussed in 
more detail below. A number of key determinations for market standard contracts are made 
by the relevant Credit Derivatives Determinations Committee (the "Determinations 
Committee" or "DC"), a group of market participants tasked with such responsibility. 
Determinations made by the DC apply to standard CDS on a market-wide basis. The 
Determinations Committee is subject to a set of published rules (the "DC Rules").7. Their input 
is a key feature of market standard credit derivatives. This means that, uniquely amongst 
OTC derivatives products, there is no need for a calculation agent, or the parties themselves, 
to make calculations or determinations under the contract (subject to a very limited number of 
exceptions, which are discussed below). 
Although, in theory, the Determinations Committees can make a determination in relation to 
any CDS contract which uses the ISDA documentation architecture, in practice determinations 
are only made in relation to commonly traded Reference Entities and market standard terms. 
In terms of developing any technological solutions for the CDS market, it is questionable 
whether it would be worth building functionality for scenarios where the DC does not make a 
determination (although it would be beneficial for any technology solutions to facilitate manual 
processing as a fallback in such circumstances). The DC will almost certainly act in cases 
where a Reference Entity is traded in large volumes. Technology developers may therefore 
wish to focus on solutions and applications in this area. 
6 There are some regional variations, and variations based on the type of Reference Entity, but for any particular 
Reference Entity the CDS contract is highly standardised. 7 Available at https://www.cdsdeterminationscommittees.org/dc-rules/.

## Page 10

10
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
Key market infrastructure 
The CDS market already has significant amounts of centralized infrastructure that provides 
functions such as (i) confirmation matching through MarkitSERV; and (ii) the Trade Information 
Warehouse maintained by DTCC. 
DTCC maintain and operate the Trade Information Warehouse.8 The Trade Information 
Warehouse facilitates the processing of lifecycle events including the splitting of CDS 
transactions due to Successor events, changes to the names of Reference Entities and 
triggering for "soft" Credit Events, where the parties can elect whether or not to trigger following 
a Credit Event (e.g. for certain Transaction Types and Restructuring Credit Events). 
The Trade Information Warehouse also facilitates the calculation of payments and central 
settlement of the cash flows through a partnership with CLS Bank International. Further 
information on the Trade Information Warehouse is available from DTCC.9 
Despite the existence of this infrastructure, there remain opportunities for greater automation 
and more efficient straight-through processing in the CDS market. For example, each firm still 
reconciles their data separately. 
Cleared versus uncleared credit derivatives 
A high proportion of credit derivatives are centrally cleared through central clearing 
counterparties ("CCPs") following market reforms in response to the global financial crisis. The 
share of CDS outstanding with CCPs was approximately 55.9% in the second half of 2019 
and totalled $4.2 trillion.10 The rules of the relevant CCP, which to an extent incorporate the 
same ISDA definitions as used for non-cleared derivatives, will govern the legal framework 
and operations related to the cleared credit derivatives. However, CCPs generally retain broad 
discretion regarding how they manage cleared products, for example in the context of default 
management. This is likely to result in additional challenges when developing technological 
solutions for cleared CDS. The impact and relevance of this for implementation of new 
technology in the cleared credit derivatives market is discussed below. 
Exchange-traded versus OTC credit derivatives 
Market participants can also trade credit derivatives on specific exchanges ("exchange-traded 
derivatives" or "ETDs"), rather than bilaterally between counterparties.11 Discussion of ETDs 
is beyond the scope of these guidelines. 
8
 The Trade Information Warehouse is described by DTCC as “a centralized, electronic database holding the 
most current details on the official, or “gold,” record for virtually all cleared and bilateral credit default swap 
(CDS) contracts outstanding in the global marketplace.” 9 See DTCC TIW Website: https://www.dtcc.com/repository-and-derivatives-services/derivatives-services/trade￾information-warehouse 10 https://www.isda.org/a/BAQTE/Key-Trends-in-Size-and-Composition-of-OTC-Derivatives-Markets-in-2H￾2019.pdf 11 ETDs should not be confused with OTC derivatives that are traded on specific trading venues, but remain 
bilateral contracts directly between trading counterparties without the interposition of an exchange or clearing 
house (and so are commonly referred to as bilateral OTC derivatives).

## Page 11

11
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
Market Evolution 
Due to the very high level of standardization in the OTC credit derivatives market, the market 
benefits from continuous innovation. Markets and market practices evolve continuously in 
response to a range of inputs, from market participants’ changing needs to changing 
regulatory requirements. New products are developed and old products occasionally fall out 
of mainstream use. 
ISDA publishes standard definitional booklets that allow users to add market standard 
provisions into their trade confirmations. From time to time, ISDA updates these definitional 
booklets. For example, in 2014 ISDA published the 2014 ISDA Credit Derivatives Definitions 
(the “2014 Definitions”) which have become the market standard for credit derivatives, in place 
of the 2003 ISDA Credit Derivatives Definitions as supplemented (the “Updated 2003 
Definitions”). With respect to the replacement of a set of definitions, there is often a very 
significant period in which some market participants continue to trade under the old definitional 
booklet for some of their trading relationships while using the newer booklets for others, and 
there remains a (dwindling) number of market standard legacy contracts that incorporate the 
Updated 2003 Definitions. In order to enhance the efficiency of the credit derivatives market 
and to ensure that the digitization process continues to facilitate innovation, developers will 
have to accommodate the evolution of this market and avoid building products that may only 
work for the market as it exists today. 
Furthermore, the credit derivatives market has been in the past an enthusiastic user of the 
“Protocol” approach to documentation updates. This means that when ISDA publishes a new 
set of definitions, or an amendment to an existing set of definitions it also typically publishes 
a Protocol. A Protocol is a multilateral mechanism under which adherents agree to amend 
their existing credit derivative trades to adopt the new definitions or an amendment. Adherents 
to the Protocol then conduct their trades on contractual terms consistent with the market 
standard going forward. Developers will need to build products that are capable of updating 
existing terms from time to time through Protocol adherence. 
The credit derivatives market is expansive and cross-jurisdictional in nature. There are a 
number of participants involved in the process, including counterparties, external data 
providers, benchmark administrators, CCPs and other financial market infrastructure and 
payment service providers. Developers should consider the challenges in ensuring 
interoperability among systems and data formats used by these different participants and 
across different jurisdictions.

## Page 12

12
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
Understanding Credit Derivatives 
This section sets out how a typical credit derivative transaction works, with a focus on typical 
calculation/valuation processes and payments/deliveries. 
Cash flows and key events under a typical credit derivative 
The simplest form of market standard credit derivative is a single name CDS. Its cash flows 
and key events are summarized below. 
Credit derivatives can become significantly more complex. For example: 
 they can reference a group (or "index") of Reference Entities, 
 they can trigger only once a certain number of Reference Entities have experienced 
a Credit Event ("nth to default products"), and/or 
 losses can be allocated on a tranched basis i.e. risk is shared overall between the 
contracting parties, but allocated between them on a sequential basis as losses 
occur. 
For certain types of Reference Entity (e.g. financial institutions), market standard CDS can 
reference debt at different levels of seniority, which means a Credit Event can occur and be 
settled by reference to debt obligations of the Reference Entity that have different levels of 
contractual/legal subordination. However, the below is broadly indicative of the main features 
of credit derivatives in general, and highlights the key issues that a developer will need to 
consider. 
The lifecycle of a single name CDS can be broken down into three stages, each of which is 
described in more detail below: 
Premium 
The premium is a payment by Buyer to Seller of a fixed periodic amount, typically in addition 
to an upfront amount paid by Buyer to Seller or by Seller to Buyer. These periodic amounts 
represent the fee for the credit protection provided by the Seller. These payments stop if 
settlement of the contract occurs. The upfront payment is determined at the time of trade. 
Buyer makes this payment shortly after the trade date, regardless of whether settlement of the 
contract occurs. 
Triggering 
If the Reference Entity experiences a Credit Event, the contract may be “triggered.” At this 
point, payment of premium ceases and the contract moves to the settlement phase. The 
relevant Determinations Committee determines the occurrence of a Credit Event.12 
12 For contracts incorporating the 2014 Definitions or the Updated 2003 Definitions.

## Page 13

13
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
Settlement 
CDS can settle in multiple ways: 
 Physical settlement: Historically, CDS settled by physical settlement. In this scenario, 
Buyer delivers to Seller a debt obligation of the Reference Entity in exchange for 
payment by Seller to Buyer of its par value. 
 Cash settlement: CDS typically includes the option (generally as a fallback) of cash 
settlement – Seller pays Buyer the difference between the market value of a 
"Reference Obligation" and its par value. 
 Auction settlement: The standard and most common form of settlement for market 
standard CDS on liquid names. This is essentially a form of cash settlement. However, 
the cash settlement amount is calculated by reference to an auction of participating 
dealers.13 
Other Intervening Events 
A number of other intervening events could also occur. Successor events are particularly 
noteworthy. If certain corporate events occur in relation to a Reference Entity (for example it 
merges with another entity or it demerges) the DC may determine that the CDS trade should 
be adjusted to reflect the relevant event. So for example, if Reference Entity X merges with 
Company Y to produce a new entity Z, the DC may make a determination that the CDS trade 
should now refer to Z as its Reference Entity. If Reference Entity X demerged into Y and Z 
and each took on half of X’s debt obligations, then the CDS trade may split into two CDS 
trades half the size – one with Y as the Reference Entity and one with Z as the Reference 
Entity. Therefore, a smart contract would need to have the functionality to accommodate these 
types of input from the DC and to update the transaction(s) accordingly. 
Understanding key market documentation 
Before considering these three stages further, it is important to understand the key market 
documentation employed by market standard credit derivatives contracts. This documentation 
has been designed to achieve greater standardization across contracts, with the aim of 
enhancing trade fungibility and liquidity. 
The 2014 Definitions and the Updated 2003 Definitions 
Credit derivatives typically incorporate the 2014 Definitions. It is less common for new trades 
to incorporate the Updated 2003 Definitions. Market standard contracts incorporate these 
definitions virtually wholesale, so that the only terms that parties need to agree for a specific 
transaction are the key economic terms such as Reference Entity, Reference Obligation, price, 
size and tenor of the trade. The 2014 Definitions have largely superseded the Updated 2003 
Definitions, though some longer-dated trades written on the Updated 2003 Definitions remain 
outstanding, and there remains market interest in determinations thereunder. Any technology 
solution that is deployed within the CDS market will therefore need to have regard for the fact 
13 The auction also provides an opportunity for parties to CDS trades to buy or sell debt obligations of the 
Reference Entity at the same price as is used to cash settle their CDS trade, thereby eliminating basis risk.

## Page 14

14
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
that there is a not a single or uniform set of definitions that apply to all CDS transactions, and 
that some trades still operate under the Updated 2003 Definitions. 
Contracts that incorporate the 2014 Definitions or the Updated 2003 Definitions include the 
concept of a "Transaction Type." This contractual term effectively imports a pre-identified set 
of elections from the Credit Derivatives Physical Settlement Matrix.14 For example, by 
specifying that a trade references the "Standard North American Corporate" Transaction Type, 
the parties thereby specify the particular Business Days, Credit Events and other key terms 
that apply. The Credit Derivatives Physical Settlement Matrix can evolve over time as the 
relevant definitional booklets are amended and supplemented. Once entered into, trades will 
not typically incorporate subsequent amendments to the Credit Derivatives Physical 
Settlement Matrix. 
The definitional booklets can also change over time. As noted above, when this happens, 
parties may amend existing trades by adhering to a Protocol. 
The Determinations Committees 
The Determinations Committees make binding determinations in relation to contracts that 
incorporate the 2014 Definitions or the Updated 2003 Definitions, including whether or not a 
Credit Event has occurred with respect to a particular Reference Entity. These common 
determinations promote standardization, as they ensure that two otherwise identical contracts 
do not result in, for example, different determinations as to whether a Credit Event has 
occurred. As such, each DC effectively represents an external source whose determinations 
have a direct bearing on the payouts and cash flows under market standard credit derivatives. 
Each DC consists of up to ten sell-side and five buy-side voting firms, alongside observers 
representing central counterparties. Each DC may also include up to two consultative non￾voting sell-side firms. A DC currently exists for the Americas, Asia (excluding Japan), 
Australia-New Zealand, EMEA (Europe), and Japan, each with responsibility for their local 
transaction types. The DC rules govern determinations made by the DCs, which include 
provisions designed to ensure the independence of the authorized representatives of each 
participating institution. DC Administration Services, Inc. currently acts as a secretary to each 
DC, and does not have a vote. 
14 Available at https://www.isda.org/2011/01/20/credit-derivatives-physical-settlement-matrix-3/.

## Page 15

15
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
Credit Derivatives lifecycle events 
Premium 
A key trade process in the context of credit derivatives is the calculation of the premium 
payable by Buyer to Seller. As a starting point, this will be calculated as a fixed periodic amount 
for market standard contracts, payable quarterly on the standard dates (referred to below), 
which ceases following the occurrence of a Credit Event (see further below). This may be (and 
in the CDS market typically is) augmented by an upfront payment payable by either Buyer or 
Seller (the "Initial Payment"). 
Market participants trade and price CDS based on changes in the credit risk of the underlying 
Reference Entity. But to aid standardization and fungibility among contracts, the established 
convention for market standard CDS trades is for the premium to be agreed at one of a small 
number of conventional fixed percentage rates for a given Reference Entity (e.g. 1% or 5% 
per annum), which are then paid on standard quarterly dates across all contracts, regardless 
of when traded. 
The parties agree the Initial Payment at the time of trade, based on two components. The first 
component reflects the correction necessary to arrive at the overall premium rate agreed 
between Buyer and Seller at the time of trading. For example, where the chosen conventional 
fixed rate is 1% per annum but the parties agree a price of 0.90% per annum, Seller will pay 
to Buyer an Initial Payment equal to the present value of 0.10% percent per annum. The 
second component is for premium that accrued from the previous quarterly payment date to 
the trade date, which the Seller pays to Buyer. The Initial Payment is the net of these two 
amounts. ISDA publishes a market standard calculation for the conversion of market rates to 
Initial Payments, including the code necessary to automate the calculations. 
Note that credit derivatives do not typically reference floating rates of interest, as the premium 
element of the trade comprises a fixed amount. However, some more bespoke products may 
reference floating interest rates, for instance where one of the cash flows represents the 
provision of funding. To the extent a developer wishes to build a solution capable of handling 
such payments, we refer to the discussion on floating reference rates and the ongoing global 
reform thereof in ISDA's "Legal Guidelines for Smart Derivatives Contracts – Interest Rate 
Derivatives" paper.15
Triggering 
Broadly speaking, the occurrence of a Credit Event reflects a decline in the creditworthiness 
of the relevant Reference Entity. The occurrence of a Credit Event is what triggers the payment 
of a credit protection amount from Seller to Buyer. 
15 See ISDA Legal Guidelines for Smart Derivatives Contracts – Interest Rate Derivatives available at 
https://www.isda.org/2020/02/11/legal-guidelines-for-smart-derivatives-contracts-ird/.

## Page 16

16
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
The 2014 Definitions contain the following seven different Credit Events: 
Credit Event Description 
Bankruptcy The commencement of liquidation proceedings in relation to the 
Reference Entity or other insolvency related events. 
Failure to Pay The failure of the Reference Entity to make a payment under 
any of its relevant obligations once the relevant grace period has 
expired. 
Obligation Acceleration A situation, excluding a failure to pay, where a relevant 
obligation of the Reference Entity becomes immediately due 
and payable prior to its termination date. 
Obligation Default A situation, excluding a failure to pay, where a relevant 
obligation of the Reference Entity becomes capable of being 
declared due and payable prior to its termination date. 
Repudiation/Moratorium An authorised officer of the Reference Entity or a governmental 
authority repudiates, or declares a moratorium in respect of any 
of, the Reference Entity’s obligations and the repudiation or 
moratorium is followed by a non-payment or a restructuring 
within a specified time frame. 
Unlike a Failure to Pay or Restructuring, the non-payment does 
not need to exceed a certain amount and the amount of the 
restructured obligation does not need to exceed a specified 
threshold. 
Restructuring A change in terms of a debt obligation of the Reference Entity, 
causing it to become less favourable to the holders of that 
obligation. 
Governmental 
Intervention 
Actions or announcements by a governmental authority 
resulting in, amongst other events, the reduction in the rate or 
amount of interest or amount of principal payable by a 
Reference Entity, an expropriation or other event which 
mandatorily changes the beneficial holder of the obligation or a 
mandatory cancellation, conversion or exchange of the 
Reference Entity’s obligations. 
Different Credit Events apply to different Transaction Types, some Credit Events are only 
relevant to certain types of Reference Entity, and bespoke transactions may apply non￾standard combinations or even entirely new events.16 These events may occur at an entity 
16 It is worth noting that thresholds or other more detailed criteria may also apply.

## Page 17

17
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
level (e.g. Bankruptcy) or an obligation level (e.g. Failure to Pay). For the obligation level 
events, market standard contracts will define the universe of debt obligations on which a Credit 
Event may be observed, which may include direct obligations of the Reference Entity or 
obligations under certain guarantees. The DC will determine which obligations are eligible for 
these purposes. The parties will typically specify a Reference Obligation, which (amongst 
other functions) is always capable of being an obligation in respect of which an obligation level 
Credit Event may occur. 
The occurrence of some Credit Events and potential Credit Events will cause other terms of 
the contract to behave differently. For instance, where applicable, the occurrence of a potential 
Failure to Pay Credit Event or Repudiation/Moratorium Credit Event close to maturity of the 
contract can cause its expiry date effectively to extend. The purpose of this extension is to see 
whether the potential Credit Event crystallizes into an actual Credit Event. 
There is also a difference between "hard" credit events, where the contract triggers 
automatically upon determination thereof (e.g. Bankruptcy and Failure to Pay), and "soft" 
credit events, where the parties can elect whether to trigger (e.g. for certain Transaction Types 
where “Mod (Mod) R” Restructuring is applicable). 
Some Credit Events can also settle on a more complex basis e.g. "Mod (Mod) R" Restructuring 
Credit Events settle differently depending on the tenor of the contract and any relevant debt 
obligations of the Reference Entity. 
An important difference between CDS and Interest Rate Swaps is that the underlying 
Reference Entity or Reference Obligation of a CDS contract can change during its life. This 
may be because the Reference Entity changes due to one or more Successors being identified 
or the Reference Obligation is replaced following the occurrence of one of a defined set of 
events in respect of the agreed Reference Obligation. 
As the occurrence of a Credit Event will depend on an event occurring in respect of the 
Reference Entity or the Reference Obligation during the life of the contract, it is important that 
these changes are capable of being monitored and recorded. This will ensure that users can 
properly map an event in respect of an entity or obligation to any contract currently referencing 
that entity as the Reference Entity or that obligation as the Reference Obligation. 
DC determinations 
As mentioned above, the default position for a market-standard CDS is that the Determinations 
Committee responsible for the relevant Transaction Type determines the occurrence of a 
Credit Event. Eligible Market Participants17 are able to submit a question to the relevant DC, 
along with supporting publicly available information from particular source(s). The DC will then 
deliberate the issue and determine whether the event described constitutes a Credit Event. 
This will sometimes be clear-cut, such as when a court filing demonstrates that a Reference 
Entity is in insolvent liquidation. Other times it will require potentially extensive legal 
17 Eligible Market Participants are parties to actual credit derivatives contracts, as opposed to interested 
bystanders.

## Page 18

18
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
interpretation, and may even go to "External Review" – an arbitration process that can be 
utilised where the DC is not able to reach the necessary majority.18 
This determination effectively represents an external input. A smart contract will need to be 
capable of accommodating the impact of this input. 
Bilateral triggering 
A determination by a DC that a Credit Event has occurred will typically result in the automatic 
triggering and settlement of the CDS trade. 
However, there is one situation in which this is not the case, namely where the CDS is 
triggered following a Mod (Mod) R Restructuring. In this case, separate triggering is required 
as the parties’ settlement obligations differ depending on whether the CDS was triggered at 
the election of the Buyer or Seller. 
In addition, there is always a possibility that the DC declines to make a determination, most 
likely because the relevant Reference Entity is not widely traded. 
In either of these circumstances, it is open to the parties to trigger their contract bilaterally. To 
do so, there is a formal timeline and notification requirements that the "Notifying Party" must 
observe. In particular, the Notifying Party must deliver a Credit Event Notice, setting out the 
Credit Event in reasonable detail. Unless the bilateral triggering is for the purpose of triggering 
CDS following the DC determining that a Mod (Mod) R Restructuring has occurred, the 
Notifying Party must also deliver accompanying publicly available information from a particular 
source(s). 
Generally, accounting for the consequences of DC determinations would likely lend itself well 
to automation within a smart derivatives contract. However, it will be more challenging to 
reflect the limited circumstances in which bilateral triggering may become available and the 
related timelines and notices. In particular, if the DC does not act and the two parties have 
differing views on the outcome under the contract of external events, there is no rules-based 
fallback for determining which party’s view is correct. One potential solution could be to 
develop an affirmation system for bilateral triggers that are not subject to DC action, which 
allows parties to proceed to settlement or the next phase of the smart contract once the 
bilateral process has reached consensus. 
Having regard for these complexities will be important when evaluating opportunities for 
automating aspects of this process and in determining where human intervention may 
continue to be required. 
18 For Credit Events, an 80% majority is required.

## Page 19

19
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
Settlement 
Once it has been determined that the contract will settle, the settlement amount must be 
determined. Credit Derivatives can physically settle, cash settle, or settle by reference to an 
auction convened by the DC. Market standard contracts typically auction settle, with a fallback 
to physical settlement. 
There is a lot of detail and complexity that goes into determining the settlement value of a CDS 
trade. For a commonly traded Reference Entity on market standard terms, the DC undertakes 
this process. This results in a simple numerical input to determine a settlement payment that 
can serve as a straightforward input to an automated calculation process.19 
However, it may be that the DC decides not to hold an auction or the auction does not apply 
to a particular trade. While this is only likely for trades on non-commonly traded Reference 
Entities or bespoke trades, developers may need to consider this possibility. Developers will 
also need to consider how any automated technology solution should operate upon the 
occurrence of a fallback to physical or cash settlement. 
These issues are considered in more detail below. 
Physical Settlement 
Historically, most market standard credit derivatives physically settled. Understanding physical 
settlement remains important for auction settlement. When auction settlement was introduced, 
the DC Rules provided that Buyer and Seller should not be prejudiced by the holding of an 
auction when compared to the position they would have experienced had physical settlement 
applied. 
Physical Settlement is fundamentally simple. Buyer delivers to Seller any eligible obligation in 
exchange for a cash payment in the currency of the notional amount of the contract equal to 
the obligation’s par amount. Buyer can deliver eligible obligations with an aggregate par 
amount up to the notional amount of the CDS contract. If the eligible obligation is denominated 
in a different currency from the notional amount of the contract, the contract sets out rules for 
calculating the FX rate to be applied to make these calculations. 
The debt obligations of the Reference Entity that are eligible for physical settlement are called 
"Deliverable Obligations", these being the obligations that Buyer may deliver to Seller. This 
always includes the Reference Obligation. The parties will use a set of Deliverable Obligations 
Characteristics to determine which other debt obligations may be eligible for delivery. These 
characteristics broadly reflect the parameters that market participants expect to see in 
relatively standard types of debt obligation for the relevant Reference Entity type. The DC will 
typically determine what constitutes a Deliverable Obligation, and will invite submissions from 
market participants as to what should be admitted. 
19 The results of each auction are published on www.creditfixings.com.

## Page 20

20
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
Physical Settlement
The provisions of the relevant Credit Derivatives Definitions and the DC rules may adjust an 
obligation’s “par” amount for these purposes. This is to reflect, for example, the fact that a 
bond that was originally issued at a significant discount to its face value will not necessarily 
entitle the holder to a claim for its full face value upon the insolvency of its issuer. Under the 
2014 Definitions, the amount a Seller pays is also reduced to reflect any contingency on the 
obligation delivered to it. This could include, for example, a credit-linked note whose 
redemption amount may be eliminated by the occurrence of an uncertain event that will make 
that obligation entirely contingent, and so reduce its deliverable amount to zero (i.e. it is not 
eligible to settle the contract). Similarly, a guaranteed bond whose guarantee is capped at a 
given amount will only be deliverable up to such cap amount. 
Once the list of Deliverable Obligations is established, Buyer may deliver anything on that list 
to Seller. Rationally, any Buyer will deliver the obligation with the lowest market value in order 
to maximize its CDS pay-out (such obligation is referred to as the "cheapest to deliver" 
obligation). This principle informs how auction settlement works. 
Auction Settlement 
Auction settlement is typically used to settle CDS transactions on commonly traded Reference 
Entities. 
The auction is designed to replicate the outcomes of physical settlement, but results in cash 
settlement of market standard contracts. Auction participants20 effectively bid on the "cheapest 
to deliver" Deliverable Obligation on the "Final List" provided by the DC, expressed as a 
percentage of its due and payable amount. This process ultimately sets the Auction Final 
Price, which is a single value expressed as a percentage. Auction-settled CDS contracts will 
then pay out such that the Buyer receives an amount equal to the greater of 100% minus the 
Auction Final Price and zero, multiplied by the notional amount of its trade. 
20 Generally the dealer firms represented on the relevant DC and certain other dealers that are active in CDS 
markets.

## Page 21

21
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
Auction Settlement
Markit Group Limited and either Creditex Securities Corporation or Creditex Brokerage LLP 
administer the auction. The rules for each auction are set out in the particular "Auction 
Settlement Terms" for that auction. The mechanics of the auction are well established, but are 
generally beyond the scope of this paper.2122 
Cash Settlement 
In common with auction settlement, cash settlement results in a one-way payment from Seller 
to Buyer. The Cash Settlement Amount is typically determined by reference to the Reference 
Obligation, as opposed to the cheapest to deliver amongst all Deliverable Obligations. The 
Buyer receives 100% minus the Reference Obligation's "Final Price," multiplied by the notional 
amount of the trade. The valuation process for determining the Final Price is set out in detail 
in the applicable definitions booklet and the Credit Derivatives Physical Settlement Matrix. 
Cash Settlement
While cash settlement will generally not apply, it remains a contractual possibility under most 
market standard contracts. Cash settlement will generally only occur in circumstances where 
(i) the DC decided not to hold an auction and (ii) physical settlement cannot be completed due 
to an impossibility or illegality, or where the contracting parties cannot trade in the relevant 
obligations being delivered due to constitutional restrictions. Forms of cash settlement also 
apply where one party fails to deliver an obligation when required to do so. These fallbacks 
apply quite rarely and their terms can be reasonably complex. 
21 It is worth noting that the auction permits CDS users to place orders to buy or sell Deliverable Obligations at 
the Auction Final Price, subject to certain conditions. These orders will then be physically settled, by delivery 
and payment between the relevant dealer and its customer. The auction also generates actual trades between 
participating dealers, which will result in similar transfers. 22 For more detailed information on this, Markit and Creditex published a "Credit Event Auction Primer" available 
at http://www.creditfixings.com/CreditEventAuctions/fixings.jsp (last updated February 2010).

## Page 22

22
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
Index CDS 
So far this paper has focussed primarily on single name CDS. As mentioned above, a number 
of more complex CDS product types are widely traded. In fact, the largest part of the CDS 
market by volume is Index CDS. 
The term “Index” in this context is something of a misnomer - CDS indices are essentially 
defined baskets of Reference Entities. The Reference Entities included in CDS indices are 
typically updated on a semi-annual basis in March and September. Whether or not single 
name CDS trading on a Reference Entity is liquid is often an important factor in determining 
whether or not a Reference Entity is included in one of the CDS indices. There are different 
indices for different geographical regions and market segments (e.g. investment grade versus 
non-investment grade). 
Organizations such as IHS Markit support Index CDS products through the publication of both 
the indices themselves and standard documentation for Index CDS. IHS Markit is responsible 
for the iTraxx and CDX indices. The standard documentation typically consists of standard 
terms supplements and standardised forms of confirmations. These documents are designed 
to supplement the 2014 Definitions or the Updated 2003 Definitions (as applicable) to enable 
the trading of Index CDS. 
In keeping with other market initiatives, Index CDS documentation is designed to ensure 
maximum standardization. The parties will only need to agree limited trade parameters such 
as size and tenor when entering into a trade. Accordingly, though the cash flows and structural 
features of Index CDS products are more complex than single name CDS, these products 
often benefit from a similar degree of standardization. 
As noted above, CDS indices are rebalanced on a semi-annual basis. In addition to the 
scheduled semi-annual updates, CDS indices are also “re-versioned” following the occurrence 
of a Credit Event in respect of a Reference Entity in the index which results in the weighting 
of that Reference Entity being reduced to zero. The most recent version of any particular index 
is known as the “on-the-run index”. 
Market participants often use Index CDS (both untranched and tranched) as part of an 
investment strategy or for other purposes, such as hedging credit risk on a portfolio of 
derivatives counterparties. 
Untranched Index CDS 
Index CDS trades are essentially basket trades. A simple Untranched Index CDS is analogous 
to a defined basket of single name CDS trades. For example, if the relevant CDS index 
included 100 Reference Entities, then by entering into an Untranched Index CDS, the parties 
have in effect entered into 100 separate single name CDS trades. Credit Events or Successors 
in respect of any of the Reference Entities will be handled in broadly the same manner as 
described elsewhere in this paper. 
In respect of Untranched Index CDS using certain Transaction Types, Mod Mod R 
Restructuring will apply which is a “soft” Credit Event. This means parties can elect whether 
or not to trigger. In order to maintain fungibility between Index CDS transactions on the same

## Page 23

23
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
index version, the affected Reference Entity is “spun-off” from the Untranched Index CDS 
transaction and turned into a separate single name CDS on that Reference Entity. The 
separate single name CDS can be then either bilaterally triggered and settled or not triggered 
and remain between the parties as a single name CDS until expiry or a subsequent Credit 
Event. This process can be operationally burdensome and could be further streamlined using 
technology. 
Tranched Index CDS 
Tranched Index CDS is more complex than Untranched Index CDS. Whilst Untranched Index 
CDS provides exposure to each of the Reference Entities in the relevant index, Tranched 
Index CDS allows market participants to take exposure to a particular tranche of risk 
associated with the defined basket of Referenced Entities. 
For example, the relevant CDS index could consist of 100 Reference Entities and be divided 
into four tranches: 
 Most senior tranche: 35-100% 
 Second most senior tranche: 25-35% 
 Third most senior tranche: 15-25% 
 Most junior tranche: 0-15% 
Each tranche consists of a starting point and an end point. Market participants specify a 
tranche in their trade by specifying an “Attachment Point” and a “Detachment Point”. 
By way of example, if a market participant desired protection on the most junior tranche, the 
relevant market participant would buy a Tranched Index CDS referencing the 0% - 15% 
tranche – i.e. the Attachment Point would be 0% and the Detachment Point would be 15%. 
Upon the occurrence of the first Credit Event in respect of a Reference Entity in the Index, the 
DC would be responsible for the DC process as normal, including organising the Auction. 
Following the occurrence of the Auction, since the Attachment Point is 0%, the Seller would 
be required to make a payment to the Buyer. 
As with single name CDS, the recovery is typically based on a percentage equal to 100% 
minus the Auction Final Price. The amount payable by the Seller depends on the notional 
amount of the trade, the size of the tranche and the weighting of the relevant Reference Entity 
in the overall portfolio. 
The remaining portion of the tranche is reduced in size to reflect that a Credit Event has 
occurred. This process is repeated in respect of any subsequent Credit Events until the 
Detachment Point is reached. 
Once the Detachment Point is reached, no further payments are made by the Seller to the 
Buyer (regardless of how many additional Credit Events occur). This is because the tranche 
in respect of which protection was bought is exhausted.

## Page 24

24
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
Whilst Index CDS, and particularly Tranched Index CDS, is a more complex product than 
single name CDS, it may be an area particularly suited to technological innovation that assists 
with the processing of Credit Events and Successor Events in respect of Reference Entities 
in the relevant index and the operational processes involved in the rebalancing and 
reversioning of the indices. Developers and technology providers should also consider 
whether licences or permissions are needed for any proposed solutions and contact the 
organization that produces the relevant CDS index.

## Page 25

25
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
Considerations for technology developers 
CDS transactions would likely benefit from the implementation of new technology solutions to 
further facilitate efficient post-trade processing. As described above, many of these functions 
are already automated and performed by existing market infrastructure (e.g. TIW). It seems 
likely therefore that any new technology solution would need to be integrated within existing 
market infrastructure and perhaps provide for existing services to be delivered in a more 
efficient manner e.g. by aiding reconciliation or the more complex processing required in index 
CDS. 
There may also be opportunities for derivatives market participants to use new automated and 
intelligent technology solutions to automate settlement of amounts or deliveries that are 
determined to be due and payable under derivatives transactions. 
For example, it may be possible to use DLT or similar technology to allow for quicker and more 
efficient settlement. In considering the use of DLT in this context, it is useful to recall the 
distinction made in the ISDA Guidelines for Smart Derivative Contracts: Introduction23 between 
different types of potential DLT implementation that are capable of supporting smart 
derivatives contracts. 
In the context of credit derivatives, a 'light chain' system would allow market participants to 
exchange information in relation to credit derivatives in an automated, digitized way, and then 
carry out certain trade processes (for example, calculation of fixed amounts) through 
technological means. This could involve, for example, an automated feed or API that transmits 
a relevant determination made by the DC.24 
In a light chain scenario, the ledger recorded by way of DLT would in effect serve as a 
messaging system among participants. The parties would continue to use the existing banking 
system to make payments and deliveries. The ledger would record the parties' payment 
obligations, but actual payments would take place off-chain. The parties would need to, for 
example, use an existing payment system to initiate the relevant transfers of cash or non-cash 
assets. This scenario also assumes that the parties are using the same DLT platform or ledger, 
or that there is a sufficient degree of interoperability between their platforms. 
Light chain settlement 
23 See ISDA, Legal Guidelines for Smart Derivatives Contracts: Introduction available at: 
https://www.isda.org/a/MhgME/Legal-Guidelines-for-Smart-Derivatives-Contracts-Introduction.pdf. 24 Note that there is currently no standardized data feed provided by the DC website.

## Page 26

26
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
A 'heavy chain' system would be a settlement system in itself. Payments and deliveries would 
take place directly on the ledger or platform. In this scenario, certain forms of digital asset (e.g. 
tokenised securities) would be constituted on the ledger itself, either in native form or as 
representations of real-world assets. The ledger would also facilitate and record the transfer 
of these digital assets among the parties to meet their payment or delivery obligations. Both 
the obligations of the parties and the transfers of value (including of collateral, where 
applicable) would be recorded or occur (as applicable) on the ledger, without the need for 
external payment or settlement systems.25 
However, there are inherent limitations to a heavy-chain system in the context of CDS. For 
example, if there is a physical settlement of a deliverable obligation, that asset will need to be 
tokenised such that it is capable of being hosted and transferred on the platform. The 
deliverable obligation is an asset of the Reference Entity and it is likely that it will be outside 
the control of the parties to a CDS to arrange for tokenisation of any of the Reference Entity’s 
assets. Although more detailed discussion around tokenisation is beyond the scope of this 
paper, these issues should be taken into account when developing automated settlement 
platforms for use in the CDS market.26 It should however be noted that because of the 
prevalence of auction settlement it would be rare to have physical settlement for a commonly 
traded CDS Reference Entity. 
Heavy chain settlement 
As described in earlier ISDA Guidelines, the approach taken will have an impact on the issues 
that technology developers should keep in mind. Where parties use external systems to make 
payments, the need to accurately identify payment flows and address the interoperability of 
systems will be significant. Parties will need to address any divergences that arise between 
outcomes on- and off-ledger. For example, where a payment is recorded as having been made 
on the ledger but settlement off-ledger has not been executed, the parties will need to ensure 
that there is a robust reconciliation mechanism capable of addressing such scenarios. 
Ultimately, a robust, clear and enforceable legal solution will be key to achieving legal certainty 
in such situations. 
25 For further discussion of these issues, see the Bank for International Settlements' Committee on Payments and 
Market Infrastructures paper on wholesale digital tokens (December 2019) available at: 
mailto:https://www.bis.org/cpmi/publ/d190.pdf. 26 These issues include settlement finality, netting and legal certainty around the characterization of certain types 
of collateral arrangement. The appropriate response to these issues will likely depend on the specific legal or 
regulatory framework in the relevant jurisdiction.

## Page 27

27
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
Where a DLT platform is designed to house a settlement system as described above, using 
digital or dematerialized assets to meet payment or collateral obligations, the system or 
platform design may have an impact on the laws governing operations involving the asset 
itself.27
27 See Private International Law Aspects of Smart Derivatives Contracts Utilizing Distributed Ledger Technology 
(https://www.isda.org/a/4RJTE/Private-International-Law-Aspects-of-Smart-Derivatives-Contracts-Utilizing￾DLT.pdf)

## Page 28

28
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
Clearing 
A large proportion of the credit derivatives market is centrally cleared. Technology developers 
should be aware of the broader considerations that apply to the cleared derivatives market. 
Cleared credit derivatives will include the following legal relationships: 
(i) Relationship between the CCP and the clearing member: The CCP rules govern this 
relationship. 
(ii) Relationship between the clearing member and underlying client: This will not be 
relevant to all cleared credit derivatives but will be relevant to arrangements where a 
clearing member of a CCP clears a credit derivative on behalf of an underlying client 
(whether directly or indirectly). Parties generally enter into cleared transactions using 
some form of clearing agreement. The clearing agreement typically takes the form of 
an addendum or module to the ISDA Master Agreement between the clearing member 
and its client.28 The illustration below represents a stylized example of a typical clearing 
model.29
Typical clearing model 
CCP Rules 
The rules of the relevant CCP primarily govern the mechanics of cleared credit derivatives, 
and the legal principles that apply to them. These rules typically give CCPs significant 
discretion (as discussed further below) and broad powers to make amendments to the rules. 
For example, CCPs have developed internal systems and models to calculate (i) margin 
required from clearing members; (ii) contributions from clearing members to the default fund 
28 ISDA has published the ISDA-FIA Client Cleared OTC Derivatives Addendum for these purposes. 
29 It is important to note that different clearing models exist in different jurisdictions, and the above example may 
not accurately represent the documentation structure or content that might be used in all scenarios.

## Page 29

29
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
based on possible losses the CCP may suffer; and (iii) transaction valuations leading to 
settlement of payments flows under credit derivatives. The CCP generally makes calculations 
and amounts are paid to or by the clearing members on prescribed deadlines or as requested 
by the CCP. The economic terms of the cleared credit derivative will incorporate the 2014 
Definitions or the Updated 2003 Definitions and cleared contracts will be in a market standard 
form. 
New automated technology solutions have the potential to create more streamlined and 
integrated processes for clearing and settlement of derivatives. Presently, these processes 
are somewhat fragmented, with manual input and intervention required at various stages of 
the trading and post-trading clearing and settlement cycle for cleared derivatives. There is 
scope for further automating the flow of information between participants involved in this 
process, particularly given the high level of standardization that is already present in cleared 
credit derivatives transactions. 
Developers of technology solutions will need to consider interoperability among different 
technology applications and infrastructure. CCPs, as with other market participants in this 
space, have specific systems, platforms and processes that they use. 
CCPs and other market infrastructure providers (such as Central Securities Depositories or 
“CSDs”) are also considering opportunities to migrate, upgrade and automate their existing 
systems, using DLT and other automated and intelligent technology solutions. These system 
enhancements will simplify processes and achieve efficiencies by reducing the amount of 
manual intervention required. New requirements under the Central Securities Depository 
Regulation (CSDR30) that aim to improve the efficiency of securities settlement within the EU 
are likely to accelerate these plans. However, it is likely that the wholesale implementation of 
such technologies by regulated financial market infrastructures will be an incremental process. 
Client clearing arrangements 
Parties use a number of industry standard contracts to document the legal relationship 
between a clearing member and its client. The mechanics of the documents and the legal 
architecture will depend in part on the client clearing model being used: 
(i) Principal model (typical for Europe): Under this model, there will be a separate back￾to-back credit derivative between the clearing member and the client. The legal 
documentation will typically ensure that this credit derivative mirrors the trade between 
the clearing member and the CCP, particularly in terms of close-out triggers and 
payment flows. The intention is for the clearing member to act as a riskless principal. 
(ii) "Agency" model (typical for the US): Under this model, the clearing member typically 
acts as an "agent-trust" of the client but is liable as principal for the client's obligations 
under the credit derivative vis-a-vis the CCP. 
There are certain elements of this relationship where further automation and digitization would 
be beneficial. For example, where the principal model is used automated technology could 
30 Regulation (EU) No 909/2014 of the European Parliament and of the Council of 23 July 2014 on improving 
securities settlement in the European Union and on central securities depositories and amending Directives 
98/26/EC and 2014/65/EU and Regulation (EU) No 236/2012

## Page 30

30
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
ensure alignment between the entry into and modification of client transactions and the 
associated transaction between the clearing member and CCP. 
Pass-through of margin from the client to the CCP could also be automated and streamlined. 
However, it should be noted that there might not necessarily be a direct correlation between 
(i) payments (including of margin) between a clearing member and a CCP and (ii) payments 
(including of margin) between a clearing member and its clients. This is because payment 
flows between a CCP and the clearing member may be netted across the transactions of many 
different clients of the clearing member. In addition, clearing members may call clients for a 
broader range of margin and may retain margin where margining at the CCP is on a net 
omnibus basis. 
Technology developers should also bear in mind the wider legal framework. For example, the 
application of smart contract technology to the termination of the cleared credit derivative will 
need to take account of the process that exists at the CCP level for terminating the transaction 
between the CCP and Clearing Member. It will also need to consider the means by which this 
process is then reflected in the corresponding transaction entered into between the Clearing 
Member and client (if applicable). This level of contingency may present some challenges for 
automation when a transaction is modified or terminated. Similarly, many of the standard ISDA 
Master Agreement provisions (to the extent still relevant to the particular trading relationship) 
are often adjusted. For example, clearing documentation might disapply provisions allowing 
the client to suspend payment and deliveries upon the occurrence of an event of default or 
potential event of default. This creates a complicated legal structure through the interaction of 
the CCP rules, underlying trading documentation (such as the ISDA Master Agreement), client 
clearing documentation and specific trade details. 
Porting is another area where there is considerable potential for further digitization and the 
adoption of smart contracts. There are, however, practical obstacles that will need to be 
considered and overcome, particularly in relation to partial porting, whether or not collateral is 
to be ported and where there is net omnibus margining. 
Porting is the process by which a client is entitled to transfer transactions they are clearing 
through one clearing member to another member (who has agreed to accept the transactions) 
with the same CCP. Such transfers may take place in the context of a clearing member's 
default, where positions held by its clients would have to be transferred to a different clearing 
member, but client clearing agreements generally also permit porting in a business-as-usual 
scenario (provided certain conditions are satisfied). When porting of transactions takes place, 
a CCP will transfer affected transactions with the existing clearing member to the transferee 
clearing member31, accompanied by a transfer of the associated collateral balances (although 
the exact way in which this will occur varies slightly at different CCPs). At the same time, the 
client's clearing agreement with the transferor clearing member may be terminated and a 
separate arrangement with the transferee clearing member will be established. Once triggered 
by a client, the execution of the porting process itself can be largely mechanical in nature 
(although the complexity of the client's cleared portfolio and the collateral holding 
arrangements at the CCP may present certain challenges, particularly where only some of the 
transactions rather than the entire portfolio is being transferred). The process would therefore 
31 The precise legal mechanism involved in the transfer may vary.

## Page 31

31
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
lend itself to automation, although it would require CCP involvement in the digitization process 
as porting effectively occurs at the level of the CCP. 
CCP discretion in respect of cleared products 
As noted, a key consideration in the cleared credit derivatives market will be the level of 
discretion afforded to CCPs. CCPs will have significant discretion to make determinations, 
make unilateral demands and/or take unilateral action both in a business-as-usual scenario 
and in the context of a clearing member default. This could include, amongst other actions, 
demands for additional margin or contributions to the CCP default fund (calculated by the CCP 
on the basis of certain parameters but with room for discretion or adjustment as to how the 
CCP makes those calculations) and managing the default process. 
Technological solutions are most easily applied to processes that involve limited discretion, 
for example a calculation based on objective inputs, or to make a payment if a certain objective 
criterion is met at a specified time on a specified date. Discretion fits less easily within these 
applications and technology developers should therefore consider how their technological 
solution should account for the exercise of CCP discretion. Likewise, clearing members 
reserve similarly broad discretions and powers when passing clearing risk onto their client. 
One cannot assume that an outcome at the CCP/clearing member level will necessarily be 
replicated at the clearing member/client level. 
This may not prove to be a major obstacle. Developers will need to ensure that their technology 
is capable of identifying situations where CCPs exercise their discretion to make changes to 
their processes or requirements. This will require effective interoperability and the 
establishment of automated communication channels between the CCP and any external 
platforms used for this purpose. Such platforms will also need to be flexible enough to 
accommodate any consequent changes to trade terms, including with respect to collateral 
arrangements. 
A key example of CCP discretion arises upon the default of a clearing member. A CCP will 
typically have discretion to exercise a broad range of powers with respect to the contracts and 
margin of the defaulted clearing member.32 
Such powers may include: 
(i) Hedging – To reduce the market risk associated with a defaulted portfolio, the CCP 
may consider hedging its exposure by entering into offsetting transactions with other 
clearing members. The CCP will have discretion to determine whether to take this 
action and the exact terms on which it does so. 
(ii) Auction – The CCP may go through a detailed process to auction the defaulted portfolio 
to other clearing members. The CCP may have discretion in terms of splitting up the 
defaulted portfolio into separate portfolios for auction purposes. CCPs will have 
32 This is in contrast to the comparatively straightforward contractual mechanism that parties follow in the event 
of a counterparty default under an uncleared transaction. For further information, see ISDA Legal Guidelines 
for Smart Derivatives Contracts – The ISDA Master Agreement (https://www.isda.org/a/23iME/Legal￾Guidelines-for-Smart-Derivatives-Contracts-ISDA-Master-Agreement.pdf)

## Page 32

32
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
different processes for running these auctions and different requirements imposed on 
non-defaulted clearing members around bidding for these portfolios. 
(iii) Loss attribution – The CCP may also attribute any remaining losses it has suffered due 
to the default through a pre-defined order of priority (‘or waterfall’), using default fund 
contributions made by clearing members and other sums. The exact waterfall will differ 
between different CCPs. 
These processes and powers of CCPs are broad and may vary among different CCPs. They 
are designed to give the CCP room to manoeuvre in what may be a significant period of stress 
in the financial markets. This discretion is therefore an important feature of the cleared credit 
derivatives market, and one that technology developers will need to contemplate when 
considering the possible application of smart contract technology.

## Page 33

33
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
Reporting 
A number of jurisdictions require the reporting of credit derivatives transactions to certain 
authorized bodies, as part of initiatives to allow regulators to better understand and regulate 
the derivatives market as a whole. 
Requirements regarding regulatory reporting of credit derivatives are detailed and precise. To 
take the requirements under EMIR33 in the EU as an example, the details of each credit 
derivative entered into, modified or terminated and which has (in most circumstances) at least 
one EU counterparty will need to be reported to an EMIR-registered or recognized trade 
repository. The content and format of these reports are prescribed by regulation, with the aim 
of harmonizing standards and reducing the need for reconciliation of data between trade 
repositories in a specific jurisdiction. This includes the use of specific identifiers (e.g. LEIs with 
respect to relevant parties such as the counterparty or CCP, or unique product identifiers to 
identify the derivative type), as well as detailed information around the terms of the relevant 
contract. 
Depending on the counterparties to the transaction, multiple regulatory reporting regimes may 
be relevant, each of which will have different detailed requirements. However, while significant 
differences still exist between different regulatory regimes (e.g. in the collection of data under 
EMIR and Dodd-Frank), regulators are working towards a goal of harmonizing the data and 
audit trail to reduce redundancies and inefficiencies.34
Given the short timeframes for compliance with regulatory reporting requirements,35 the ability 
to automate and streamline this process would be highly beneficial. Technology developers 
and providers in this space will need to ensure that they are familiar with the detailed 
requirements around format and content of these reports. Specifically, developers should 
consider carefully how to attribute liability for the failure to make a report (or errors in the 
report) among the parties, as the market participant will typically retain regulatory responsibility 
for compliance. 
Developers should also consider any requirements to protect data and information collected 
and may need to build separate silos to protect parties' confidential information from 
unauthorized disclosures. Only information that is permitted to be disclosed to each participant 
in the system (e.g. CCPs, regulators, brokers, counterparties) should be made available to 
them, even where data is collected centrally. Technology developers should consider 
designing and integrating appropriate information barriers or other data security measures into 
the relevant platform to address this concern. 
Regulators are already considering how to apply technology to regulatory reporting 
requirements. For example, ISDA is working with the UK Financial Conduct Authority, the 
33 Regulation (EU) No 648/2012 of the European Parliament and of the Council of 4 July 2012 on OTC derivatives, 
central counterparties and trade repositories Text with EEA relevance. 34 See OICU-IOSCO Report, "Market Fragmentation & Cross-border Regulation" available at: 
https://www.iosco.org/library/pubdocs/pdf/IOSCOPD629.pdf. 35 For example, under EMIR parties must submit reports no later than the next working day.

## Page 34

34
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
Bank of England and participating financial institutions to explore how the ISDA CDM can 
support the digital regulatory reporting pilot for derivatives.36
Any technology solution in this area would benefit from being interoperable across multiple 
regulatory reporting regimes. This would remove the need to build multiple systems to comply 
with these requirements. This includes the multiple jurisdictional reporting regimes which may 
apply to derivatives, but also reporting regimes which apply to other similar products (such as 
securities financing transactions under SFTR).37 
36 A report on the deployment of ISDA CDM to deliver a UK digital regulatory reporting pilot is available at: 
https://www.isda.org/2019/05/21/isda-cdm-deployed-to-help-deliver-uk-digital-regulatory-reporting-pilot/. 37 Regulation (EU) 2015/2365 of the European Parliament and of the Council of 25 November 2015 on 
transparency of securities financing transactions and of reuse and amending Regulation (EU) No 648/2012.

## Page 35

35
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
Conclusion 
These guidelines provide an overview of the existing legal framework and processes for OTC 
and cleared credit derivatives. They highlight areas in which there is significant scope for 
further digitization and adoption of new technologies that can lead to increased efficiencies. 
Credit derivatives, in particular, present fertile ground for such initiatives as they are highly 
standardized derivative products, although even market standard contracts can contain 
complex features. It is therefore important to give careful consideration to the development of 
smart derivatives contracts in the context of credit derivatives, given the size of the market 
and their widespread use by many different types of market participants. 
This paper discusses aspects of credit derivatives to which technology developers should 
have regard, particularly in the context of the settlement/lifecycle event process, where the 
greatest potential for increased automation and application of new technologies may exist. 
ISDA encourages members to contribute to this work to ensure industry views are taken into 
account and that each of these various projects and initiatives benefit from broad-based 
market feedback and expert insight. 
Members can participate in ISDA's work by joining the following working groups: 
 ISDA Legal Technology Working Group: Established to promote greater 
standardization and digitization of ISDA documentation through the ISDA Clause 
Library Project. 
 ISDA Fintech Legal Working Group: Established to raise and discuss areas of legal 
and regulatory uncertainty in the application of new technology (such as smart 
contracts, DLT, digital assets and AI) to derivatives trading. 
 ISDA CDM Architecture and Review Committee: Established to define a standard 
representation of derivatives trade events that are asset class and product agnostic, 
and to develop a common domain model across transaction and legal agreement 
data required for processing of such events. 
Members can join these Working Groups through the My Committee Dashboard on the ISDA 
website: http://www.isda.org/committees. 
If you have any questions on any of the issues raised in this paper, please contact 
ISDALegal@ISDA.org

## Page 36

36
Copyright © 2020 by the International Swaps and Derivatives Association, Inc. 
Acknowledgement 
ISDA greatly appreciates the efforts of everyone who contributed to the preparation of these 
ISDA Legal Guidelines for Smart Derivatives Contracts. Special thanks goes to Allen & Overy 
LLP and, in particular, David Benton, Paul Allan and Robert Simmons, who each undertook to 
author various sections of these guidelines. 
ISDA would like to offer special thanks to the following individuals who contributed 
substantively to these guidelines at various stages of the process: 
Keith Blizzard (Factor) 
Yvette Valdez (Latham & Watkins LLP) 
John Ho (Standard Chartered Bank) 
Judith Lawless (McCann FitzGerald) 
Gregory Chartier (Clifford Chance LLP)
Since both the individual participants and their employers contributed towards the preparation 
of these guidelines, participants are identified by reference to the organization with which they 
were associated during the preparation process.
