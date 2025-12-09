# Smart Derivatives Contracts From Concept to Construction Oct 2018

*Converted from: Smart-Derivatives-Contracts-From-Concept-to-Construction-Oct-2018.pdf*

---

## Page 1

1
October 2018
Whitepaper
Smart Derivatives Contracts: 
From Concept to Construction

## Page 2

Whitepaper: Smart Derivatives Contracts: From Concept to Construction
2
CONTENTS
Executive Summary ......................................................................3
Introduction .................................................................................4
Concept: Smart Derivatives Contracts .............................................5
Compatibility With Standards.........................................................6
ISDA Common Domain Model........................................................9
Complexity in the Contract...........................................................11
Complexity Outside the Contract ..................................................16
Constructing a Smart Derivatives Contract.....................................19
Conclusion.................................................................................27

## Page 3

Whitepaper: Smart Derivatives Contracts: From Concept to Construction
3
EXECUTIVE SUMMARY
Smart contracts could help revolutionize the derivatives market by creating much-needed 
efficiencies that would benefit the entire industry. But transforming smart contracts from an 
exciting concept to practical use will present a number of challenges. 
From a legal perspective, a number of issues need to be considered. What contractual terms should 
be automated? How should these terms be expressed? How can lawyers validate the legal effect of 
any automated contractual terms that are not expressed in natural language? 
This paper considers some of these issues, and proposes a practical framework for constructing 
smart derivatives contracts (see Figure 1). This includes:
• Selecting parts of a derivatives contract for which automation would be effective and efficient;
• Changing the expression of the legal terms of those parts of the derivatives contract into a more 
formalized form;
• Breaking the formalized expression into component parts for representation as functions;
• Combining the functions into templates for use with particular derivatives products; and
• Validating the templates as having the same legal effect as the legal terms of a derivatives contract.
In developing this framework, the ISDA Common Domain Model (ISDA CDM™) could play an 
important role in ensuring that a shared, standardized representation of events and actions that 
occur through the derivatives lifecycle is applied across the industry. 
For smart derivatives contracts to fulfill their potential, it is important they are developed in a 
way that is compatible and consistent with the technological, commercial, regulatory and legal 
standards applicable to both derivatives contracts and smart contracts. This will require knowledge 
and experience from different disciplines and domains. Expertise in the technology used, the 
commercial context of its use, the regulation that applies to it and the law that supports its 
effectiveness, are all critical.
These suggestions, and the issues discussed in this paper, are intended to stimulate further 
collaborative work between ISDA and its members in developing a set of principles that can be used 
to construct smart contracts for derivatives that are not only technologically efficient, but are legally 
effective and consistent with ISDA’s mission to promote safe and efficient markets.
Figure 1
Select the 
parts of a 
derivatives 
contract 
for which 
automation 
would be both 
effective and 
efficient
Change the 
expression of 
the legal terms 
of a derivatives 
contract 
into a more 
formalized 
form
Break the 
formalized 
expression into 
component 
parts for 
representation 
as functions
Combine the 
functions into 
templates
for use with 
particular 
derivatives 
products
Validate the 
templates as 
having the 
same legal 
effect as 
legal terms 
of derivatives 
contracts

## Page 4

Whitepaper: Smart Derivatives Contracts: From Concept to Construction
4
INTRODUCTION
Smart contracts could radically improve the efficiency of the derivatives market by automating the 
performance of certain events and obligations. Significant work has been conducted to explore the 
use of smart contracts, and to consider the implications from a technological, legal and operations 
perspective. 
As part of this work, ISDA has published a series of papers looking at both legal and technological 
aspects of smart contracts. These include:
The Future of Derivatives Processing and Market Infrastructure (September 2016)1
: This paper 
summarizes the need to develop new and efficient processes for the global derivatives market, and 
identifies three key contributors to the improvements required: standardization, collaboration 
and technology. The paper highlights the importance of distributed ledger technology and smart 
contracts.
Smart Contracts and Distributed Ledger – A Legal Perspective (August 2017)2
: Jointly prepared 
by ISDA and Linklaters, this paper sets out a framework for smart contracts in the context of 
ISDA’s documents. It describes what smart contracts are and makes an important distinction 
between smart contract code and smart legal contracts. It also gives a preliminary and high-level 
description of the application of smart contracts within the ISDA documentation framework.
ISDA Common Domain Model Version 1.0 Design Definition Document (October 2017)3
: This 
publication describes some of the fundamental elements of the ISDA CDM. The ISDA CDM 
seeks to create a standard blueprint for events and actions that occur throughout the lifecycle of a 
derivatives trade. 
CDM 1.0 (June 2018)4
: This initial snapshot of a digital version of the CDM provides a human￾readable standard digital representation of the model, addressing a limited product scope of simple 
interest and credit derivatives products and an agreed sample of business events.
This paper contributes to this work by examining, from a legal viewpoint, what is required in order 
to apply smart legal contracts to ISDA documentary standards, within the context of the ISDA 
CDM where relevant. 
Smart contracts 
could create 
significant 
efficiencies 
in derivatives 
markets, 
but further 
industry effort 
is required 
to address 
the legal, 
technological 
and operational 
challenges
1 International Swaps and Derivatives Association, Inc. (ISDA), The Future of Derivatives Processing and Market Infrastructure (September 2016), https://
www.isda.org/a/UEKDE/infrastructure-white-paper.pdf
2 ISDA and Linklaters LLP, Smart Contracts and Distributed Ledger – A Legal Perspective (August 2017), https://www.isda.org/a/6EKDE/smart-contracts￾and-distributed-ledger-a-legal-perspective.pdf
3 ISDA, ISDA Common Domain Model Version 1.0 Design Definition Document (October 2017), https://www.isda.org/a/gVKDE/CDM-FINAL.pdf 
4 The ISDA CDM 1.0 (June 2018), https://www.isda.org/2018/06/04/the-isda-cdm-1-0/

## Page 5

Whitepaper: Smart Derivatives Contracts: From Concept to Construction
5
CONCEPT: SMART DERIVATIVES CONTRACTS
The term ‘smart contracts’ can be defined in multiple ways, but the following description is 
commonly used in work on smart contracts with derivatives transactions. 
“A smart contract is an automatable and enforceable agreement. Automatable by computer, although 
some parts may require human input and control. Enforceable either by legal enforcement of rights 
and obligations or via tamper-proof execution of computer code.” 5
Usefully, this definition combines the elements of both legal and technological effectiveness. 
However, a smart contract does not have to be a legal contract. There is a distinction between smart 
contract code (a piece of code designed to execute certain tasks if pre-defined conditions are met) 
and smart legal contracts (legal contracts, or elements of legal contracts, represented by software)6
. 
The ISDA/Linklaters Smart Contracts and Distributed Ledger – A Legal Perspective paper also 
distinguishes between two different models of smart legal contracts: the external model and the 
internal model. In the external model, the coded provisions remain external to the legal contract, 
and represent only a mechanism for automatic performance of the contract. In the internal model, 
the provisions that can be performed automatically are included in the legal contract, but are 
rewritten in a more formal representation than the current natural language form. A computer 
could then take this more formal representation and automate performance. 
This paper focuses on smart legal contracts using the internal model. This is where the most 
complexity in legal issues arises, because changes to the legal contract would be necessary 7
. But it 
also provides the greatest efficiency and risk management benefits, because the same representation 
could be used both for legal effect and to implement automation. This would minimize the 
possibility of divergence between the legal meaning and operational performance of the contract. 
To avoid repetition and confusion, this paper refers to these smart contracts as smart derivatives 
contracts. Smart derivatives contracts are smart because they are derivatives contracts with some 
terms that can be automatically performed. Those terms are expressed in a form that enables their 
efficient automation. Other terms that are not automatically performed are expressed in natural 
language. As such, they are derivatives contracts and smart contracts (and smart legal contracts), as 
shown in Figure 2.
Figure 2
5 Clack, C., Bakshi, V., and Braine, L., Smart Contract Templates: foundations, design landscape and research directions (August 4, 2016, revised March 
15, 2017) 
6 Stark, J., Making sense of blockchain smart contracts (June 4, 2016, updated June 7, 2016), https://www.coindesk.com/making-sense-smart-contracts/
7 However, issues of legal validation discussed later in this paper can arise whether the internal model or external model is used
Smart 
derivatives 
contracts 
include 
terms within 
the contract 
that can be 
performed 
automatically
Derivative
contracts
Smart
derivative
contracts
Smart
legal
contracts
Smart
contracts

## Page 6

Whitepaper: Smart Derivatives Contracts: From Concept to Construction
6
COMPATIBILITY WITH STANDARDS
“Standardization takes many forms, covering product definitions, process descriptions, legal 
documentation, messaging and terminology. ISDA has long been at the forefront of publishing 
and promoting legal documentation standards, from the ISDA Master Agreement and CSAs to 
definitional booklets and confirmation templates. … Standards in all forms help to create a platform 
for technology to evolve within an ecosystem.” 8
There are many different standards applicable in the derivatives markets and for regulating conduct 
and decision-making. All have a similar overall goal – to enable reliable, consistent and safe 
outcomes. This should also be the goal in developing smart derivatives contracts and is consistent 
with ISDA’s role in facilitating safe and efficient markets.
At least four different types of standards need to be considered for smart derivatives contracts: 
regulatory, legal, commercial and technological. 
Regulatory Standards
Regulatory standards would include those applicable to derivatives markets and participants, such 
as requirements on clearing, data reporting, trading, capital and margin9
. These standards are often 
conceived at an international level in an effort to provide a consistent cross-border regulatory 
framework for derivatives market participants10. Despite the existence of international standards, 
a lack of harmonization in the implementation of regulations at a national level can create 
jurisdictional complexity that should be considered. 
In the context of smart derivatives contracts, regulatory standards would also include regulations 
directly applicable to smart contracts, but these are less well developed. 
The Financial Stability Board and Committee on Payments and Market Infrastructures have both 
highlighted issues related to automated contracting11, including transparency, appropriateness of 
the code and data feed concerns12. However, there are currently no comprehensive international 
standards on regulatory policy issues relating to smart contracts. Such standards could emerge in the 
future, and smart contract work with derivatives will need to be compatible with them.
8 ISDA, Future of Derivatives Processing and Market Infrastructure, page 15
9 Derivatives documentation needs to comply with these regulations. For example, ISDA is in the process of drafting of next-generation initial margin 
(IM) documentation for phases four and five of the IM regulation phase-in, scheduled for September 2019 and September 2020, respectively
10 For example, through bodies such as the International Organization of Securities Commissions (IOSCO), Financial Stability Board (FSB) and the 
Committee on Payments and Market Infrastructure (CPMI)
11 For example, FSB, Financial Stability Implications from FinTech: Supervisory and Regulatory Issues that Merit Authorities’ Attention (June 27, 2017), 
http://www.fsb.org/2017/06/financial-stability-implications-from-fintech/ 
12 “Automation of contract terms could improve efficiency by eliminating the need for human intervention in executing a transaction and thus reduce 
the probability of human error. The addition of automated contract tools, among other value-added features, could significantly simplify back office 
processes and records management. At the same time, self-executing applications may create new challenges and risks for the financial ecosystem”: 
CPMI, Distributed ledger technology in payment, clearing and settlement - an analytical framework (February 2017), https://www.bis.org/cpmi/publ/
d157.htm, pages 13–14
Smart 
derivatives 
contracts would 
need to comply 
with regulatory, 
legal, 
commercial and 
technological 
standards

## Page 7

Whitepaper: Smart Derivatives Contracts: From Concept to Construction
7
Legal Standards
Legal standards exist to provide certainty that arrangements entered into between parties will be 
enforceable as a matter of law13. The laws on which legal standards are based are developed at a 
national level. Like regulatory standards, this can create complexity where these arrangements are 
entered into on a cross-border basis between counterparties that may be subject to different legal 
systems.
However, international standards do exist for laws in important areas, such as the model laws of 
the United Nations Commission on International Trade Law (UNCITRAL), the work of the 
International Institute for the Unification of Private Law (UNIDROIT) and the Hague Conference 
on Private International Law. This assists the development of cross-border trade by providing for 
consistency of laws across the different jurisdictions that adopt them.
Nonetheless, the bodies responsible for international legal standards have been mostly silent on legal 
standards for smart contracts. 
An example of where such standards may develop is in relation to the cross-border recognition 
of smart contracts, including in relation to choices of law. If smart contract legal standards are 
developed, then the derivatives smart contract work will need to be compatible with them.
Commercial Standards
Commercial standards set out the market practice for how commercial arrangements are reached 
and performed. They are usually developed by participants in the relevant industry and facilitate 
cross-border activity by creating consistency across the different markets that adopt them14. 
This gives market participants confidence that their transactions will be conducted on the same 
basis, regardless of counterparty. This is critical for proper identification and assessment of risk. 
Ensuring that smart derivatives contracts reflect and are compatible with these commercial 
standards is important work for ISDA and its members.
Technological Standards
Technology standards set a common framework for development, and provide for consistency 
between results. A smart contract framework should therefore be built on a technological 
framework because consistency is critical for adoption. 
Various technological standards (such as those applicable to messaging) can be applied to the 
operational aspects of derivatives contracts. Some international standards bodies, such as the 
International Organization for Standardization, are also working on technical standards for smart 
contracts, although the focus is on a wide range of smart contract applications and not derivatives 
contracts15.
13 The legal standards applicable to derivatives contracts are reflected in ISDA’s standard legal documentation. For example, ISDA’s work in 
commissioning netting opinions in relation to that documentation provides certainty to derivatives markets participants that they are entering into 
legally enforceable netting arrangements
14 The development of commercial standards in the derivatives market has been reflected through the development of ISDA’s documentation framework, 
including its credit support documentation and its transaction-specific definition booklets
15 ISO Technical Committee, ISO/TC 307 Blockchain and distributed ledger technologies, includes Working Group WG3, Smart Contracts and their 
applications

## Page 8

Whitepaper: Smart Derivatives Contracts: From Concept to Construction
8
Compatibility with Standards
Smart derivatives contracts need to be compatible and consistent with the technological, 
commercial, regulatory and legal standards applicable to both derivatives and smart contracts. This 
is necessary in order for them to achieve their potential to improve efficiency in the derivatives 
market. 
For example, if smart derivatives contracts are developed only with technological standards in mind, 
they may not be legally enforceable, they may conflict with regulatory requirements, and they may 
be inconsistent with the way that derivatives contracts are actually transacted between parties16. This 
would obstruct their use, even if they represent a significant technological improvement. 
Alternatively, if they are developed only with legal standards in mind, they may not be 
technologically operable. Consequently, it is important that smart derivatives contracts are 
compatible with the multiple sources of standards described above, and work to develop them is a 
co-operative effort between lawyers, computer scientists and banking technology practitioners.
Fortunately, ISDA’s documentation framework provides an excellent foundation for the 
development of smart derivatives contracts17. These documents reflect and are consistent with legal, 
regulatory and commercial standards for derivatives. Importantly, use of ISDA documents would 
allow the technological framework ultimately used to be consistent with the commercial standards 
for derivatives contracts. 
In order to achieve compatibility with the various standards, the sharing of terms and concepts 
across different knowledge disciplines will be important. The ISDA CDM will play a fundamental 
role in this regard. The CDM builds a foundation for common data and process standards, 
providing a platform for the development of a framework that may ultimately be applicable to 
smart derivatives contracts. 
16 An example of this could be a technological process that automates the close-out amount calculation process. If such a process was constructed 
without regard to regulatory, legal and commercial standards, it might be unlawful in the insolvency of one of the parties and deprive the other party of 
the flexibility needed to manage the market risks arising because of the transactions’ termination
17 For example, ISDA recently assisted Axoni in its development of peer-to-peer blockchain infrastructure for equity swaps processing by helping to 
create a standardised equity swap confirmation and trade template based on a 2011 ISDA Equity Derivatives Definitions framework designed to 
facilitate electronic processing of equity derivatives

## Page 9

Whitepaper: Smart Derivatives Contracts: From Concept to Construction
9
ISDA COMMON DOMAIN MODEL
“The ISDA CDM aims to deliver a standardized model for the post-execution trade lifecycle, focusing 
on the non-differentiating aspects of that trade lifecycle that are candidates for mutualization by the 
industry.” 18
ISDA published the first draft of the ISDA CDM in October 2017. This initial conceptual version 
of the model served as a basis for discussion with ISDA’s membership and the broader industry on 
its feasibility as the basis for common process and data standards. 
ISDA subsequently published ISDA CDM 1.0 in June 2018. This provides a standard digital 
representation of events and actions that occur during the life of a derivatives trade, expressed in a 
machine-readable format that is agnostic of any programing language or software technology.
The ISDA CDM framework is more in line with ISDA’s work in developing operational standards19
than its work on legal documentation. It can therefore initially be difficult to understand from a 
legal perspective. However, understanding the way in which the CDM can connect the different 
representations of derivatives transactions is important to constructing smart derivatives contracts 
that operate efficiently in the derivatives market 20. 
Events
The ISDA CDM focuses on ‘events’ that occur during the life of a derivatives transaction. These 
include ‘independent events’ that are independent from the economics of a derivatives transaction, 
such as the creation, termination, amendment and cancellation of a transaction. It also includes 
‘dependent events’ that are contingent on the economics of a derivatives transaction, such as 
updating the floating rate for a payment, making a payment, valuing a transaction and exercising an 
option. From a legal perspective, independent events can be thought of as actions that change the 
contract, while many dependent events are actions that happen under the contract 21.
For smart derivatives contracts, an initial step for lawyers may be to focus on dependent events, as 
they can represent operations that occur under the terms of a contract. For example, the calculation 
of a floating rate interest amount starts with an observation of the rate, followed by a function for 
its calculation, which results in a derived observation of the floating amount. The ISDA CDM has 
described this ‘function’ as highly automatable in a smart contract.
The ISDA CDM looks at derivatives products not by reference to the labels given to them, 
but by reference to the functions performed under them. Derivatives products are expressed as 
combinations of these functions and the observations they use, rather than being expressed as a 
prescribed form for a particular type of product into which product specific inputs are made. 
18 ISDA, Design Definition Document, page 4
19 For example, ISDA’s work in developing FpML® (Financial products Markup Language) has certain similarities to the approach taken to developing the 
ISDA CDM, as it is open sourced and establishes the industry protocol for sharing information on, and dealing in, financial derivatives and structured 
products. The standard is developed under the auspices of ISDA, using the ISDA derivatives documentation as the basis. While the ISDA CDM is 
based on FpML product representations, it goes further by providing a digital representation of all the events during the lifecycle of a derivatives 
transaction
20 An analogy that may help is to consider the legal, risk, pricing and collateral perspectives of a derivatives transaction to be different, partial maps of 
the same landscape. The ISDA CDM is the common system of reference points that can be used to ensure that that each of these maps is of the same 
landscape so that when they are used together, they cover all aspects of the derivatives transaction
21 However, some dependent events, such as valuation of a transaction, are not required to take place by the terms of the contract, even though they are 
based on the contract’s economic terms 
The ISDA CDM 
provides a 
standard digital 
representation 
of events and 
actions that 
occur during 
the life of a 
derivatives 
trade

## Page 10

Whitepaper: Smart Derivatives Contracts: From Concept to Construction
10
Functions and Templates
From a legal perspective, this approach is a significant change. The focus on functions applied to 
observed information changes the role of the operative legal terms of a derivatives contract (many 
of which are contained in ISDA’s product definitions). Rather than being the fundamental rulebook 
for the transaction’s lifecycle, terms can be seen as inputs into the current representation of the state 
of the transaction. 
These inputs can be broken down into their simplest representation – for example, an interest rate 
swap as a combination of two coupon payments. Those simple functions can then be combined 
into templates that follow the functionality of the ISDA definitions, producing observations when 
they are run together with the economic terms (the derived observations). This combination of 
functions into templates is an important aspect of what makes a smart derivatives contract ‘smart’ 
and effective for implementation with derivatives transactions.
This means there could be a single ‘library’ of functions that can be used to build the templates of 
smart contracts used for different products, rather than having separate definitional booklets for 
each product. 
Figure 3 shows how the features of the economic terms, calculations and performance in the ISDA 
CDM have analogies in the ISDA transaction-specific documentation.
The ISDA CDM proposes a hierarchical product definition to allow a product to be built from 
predefined functions, which are in turn built from predefined elements (such as dates and numbers). 
This produces a template for the product that that can be used repeatedly for transactions. This 
structure is important in enabling a framework for constructing smart derivatives contracts. 
However, before applying this framework, it is necessary to consider the legal complexities that need 
to be managed within it. These are considered in the next two sections of this paper.
Figure 3
Certain 
operational 
clauses within 
legal contracts 
are more suitable 
to automation 
and self￾execution than 
non-operational 
clauses
Confirmation Observations Economic terms
Terms in product 
definition booklet
Transaction 
performance 
Functions combined into 
product template Calculations
Derived 
observations Performance
ISDA transaction documentation ISDA Common Domain Model

## Page 11

Whitepaper: Smart Derivatives Contracts: From Concept to Construction
11
COMPLEXITY IN THE CONTRACT
“Defining contractual performance in software requires prudence and forethought. Hundreds of years 
of case law, legal tests such as ‘the reasonable person’ test, and the chaotic nature of real-world events 
and human frailties presents an environment that is impossible to entirely emulate in code. This 
software is not a contract in reality, and ideally should exist wrapped within a legal framework that 
links the code with a contract.” 22
Laws have often evolved over centuries to adapt to many circumstances and possibilities. Although 
laws can comprise rules and regulations, the application of law often involves flexibility and 
judgment. In derivatives contracts, examples include flexibility in the calculation of ‘close-out 
amount’ within the ISDA Master Agreement 23, and flexibility over the determination of a ‘potential 
adjustment event’ within the ISDA equity derivatives definitions 24. Prescribing rules in advance to 
automate these parts of contracts present considerable challenges. 
Automating Parts of a Derivatives Contract
Not all of the terms of a smart derivatives contract need to be automated. Automated terms can 
form a single contract with those that are not automated, in the same way that an ISDA Master 
Agreement forms a single agreement with the confirmations of the transactions entered into under 
it 25. It is therefore critical to identify what parts of a derivatives contract should be represented in 
automatable form. There are two parts to this: 
• Determining which parts of a contract it is possible to automate (the parts for which automation 
could be described as being effective); and
• Determining which of those parts there is sufficient benefit in automating (the parts for which 
automation could be described as being efficient).
Figure 4
22 Hanson, R., Reeson, A., and Staples, M., Distributed Ledgers: Scenarios for the Australian economy over the coming decades, page 16 (May 2017, Data61), 
https://publications.csiro.au/rpr/pub?pid=csiro:EP175257, Data61 is part of Australia’s Commonwealth Scientific and Industrial Research Organisation (CSIRO)
23 The definition of close-out amount in Section 14 of the 2002 ISDA Master Agreement continues for more than a page of its printed form, providing 
the determining party with a range of bases on which it can be calculated. This flexibility proved very valuable in calculating these amounts in the 
aftermath of the global financial crisis due to the significant disruption in markets that took place 
24 A potential adjustment event in Section 11.2(e) of the 2002 ISDA Equity Derivatives Definitions is defined to include a number of generally described 
events, such as subdivisions, consolidations and reclassification of the relevant shares, certain distributions, issues or dividends to holders and other 
events. It also includes “any other event that may have a diluting or concentrative effect on the theoretical value of the relevant Shares”
25 The possibility of representing only a part of legal contracts in smart contract code has been noted by Clack and ISDA/Linklaters. In a conceptual 
sense, it is similar to different parts of the one legal contract being expressed in different natural languages, on the basis that the parts to be performed 
in different countries are expressed in the language most easily understood in the relevant country of performance
Some parts of 
a legal contract 
are complex 
or involve 
subjective 
judgement 
and will be 
challenging to 
automate
Derivative
contract 
terms
Terms that
could be
automated
Terms that
should be
automated

## Page 12

Whitepaper: Smart Derivatives Contracts: From Concept to Construction
12
Selection for Effective Automation
Considerable thought has already been applied to how to determine the parts of a legal contract that 
could be automated. 
One approach, outlined in the ISDA/Linklaters Smart Contracts and Distributed Ledger – A 
Legal Perspective paper, divides a legal contract into ‘operational’ and ‘non-operational’ clauses. 
Operational clauses are described as those that embed some form of conditional logic – that 
upon the occurrence of a specified event, or at a specified time, a deterministic action is required. 
Conversely, the non-operational clauses of a contract are those that relate to the wider legal 
relationship between the parties26. 
The intent of this distinction is that operational clauses are more appropriate for automation. 
However, the Legal Perspectives paper recognizes that this distinction can be difficult to draw in 
some cases, and this difficulty has also been noted from a computer science perspective27. 
Another approach considered is to rewrite contracts in a more formal expression based on a 
logical framework that can easily be converted into a programming language 28. However, there are 
limitations to this approach in terms of feasibility. It would be a massive task to rewrite the entirety 
of derivatives contracts in a new semantic form. Furthermore, unless all contracts are changed at the 
same time, those expressed in the old form would need to have the same meaning as those expressed 
in the new form, otherwise basis risk could develop between them. This would be problematic 
if they are intended to be matching transactions. Given these practical limitations, it is perhaps 
unlikely that the parties would be comfortable with this approach.
Nonetheless, there could be another method that combines each of these two approaches with the 
perspective of the parties to the contract whose performance is to be automated.
Need for Legal Validation
Before agreeing to use a new form of derivatives contract that includes automated terms, the parties 
are likely to require confirmation that the new form has the same legal effect as the form they would 
otherwise have used. One reason for this is that the parties will need to know what they are agreeing 
to. As mentioned above, another reason is because derivatives contracts are often used in connection 
with each other.
26 The operational / non-operational distinction is also made in other works, such as that of Clack et al. who describe the ‘operational aspects’ as:
“the parts of the contract that we wish to automate, which typically derive from consideration of the precise actions to be taken by the parties and 
therefore are concerned with performing the contract.”
And the non-operational aspects as: 
“the parts of the contract that we do not wish to (or cannot) automate”
27 “Development of smart contract code for large, high-value legal agreements is a complex matter – it is not simply a matter of ‘lifting’ operational 
phrases out of the legal text and turning them into code, because operational and non-operational aspects of the agreement are intertwined”. Clack, 
C., Smart Contract Templates: Legal semantics and code validation (2018), Journal of Digital Banking
28 “In the far future, we may see an increasing use of a formally structured style of expression embedded in legal prose; if all business logic in legal prose
could be replaced with arithmetical or logical expressions, such as the higher-order parameters discussed in the previous paragraph, this should 
lead to reduced ambiguity in legal prose and fewer errors. The adoption of formal logic into legal prose would require such formal constructs to gain 
acceptance in the courts and to be admissible as evidence of the intentions of the parties”. Clack et al, page 9

## Page 13

Whitepaper: Smart Derivatives Contracts: From Concept to Construction
13
For example, the risks under one interest rate swap might be hedged with another, provided the 
effect of their terms is the same. Ensuring they have the same effect is normally based on ensuring 
they have the same form – that the two interest rate swaps look the same – and they are governed by 
the same law (or different laws that will interpret the contracts in the same way). If the form of one 
of those interest rate swaps is different, then it is critical it retains the same legal effect, otherwise it 
won’t be an effective hedge for the other and basis risk could develop. 
If parties need confirmation that a smart derivatives contract produces the same legal effect as an 
equivalent traditional derivatives contract, then this can guide what parts of a derivatives contract 
are selected for translation into automatable form. Only those parts of the derivatives contract that 
a lawyer can confirm will not change their legal effect when automated should be selected. In other 
words, selection for effective automation should be based on an ability to conduct legal validation of 
the automated terms 29. 
Selection for Legal Validation
Automating the performance of a derivatives contract involves the translation of contractual terms 
from legal drafting in a natural language that can be understood by humans into a form of a 
program in a programming language that can be converted for use by a machine. Legal validation of 
the contract will be challenging if lawyers are required to understand the programming languages or 
programmers to understand legal drafting. 
However, this translation could occur in two steps. The legal drafting could be translated by a 
lawyer into a form that could be used by a programmer to convert into a program that a machine 
can use for automation. From a legal perspective, this intermediate form could be described as a 
more strict and procedural expression of the drafting. From a programming perspective, it could be 
described as the use of a domain-specific language 30. 
Using such a shared, formal representation takes the benefit of the expertise of the lawyer and the 
programmer: the lawyer can confirm that the formalized representation is consistent with the legal 
drafting, while the programmer can confirm that the program is consistent with the formalized 
representation31. The ISDA CDM is an example of how shared, formal representations can 
assist efficiency in the market, and ISDA could have an important role in developing this formal 
representation for smart derivatives contracts. 
An example of how legal drafting could be translated into such a shared, formal representation is 
set out in the Constructing a Smart Derivatives Contract section of this paper. Such a representation 
needs to use defined variables, functions, precise language and control structures such as sequencing, 
selection and repetition of processes. From a lawyer’s perspective, these are logical processes. Under 
the legal validation approach, only those parts of a contract that a lawyer believes can be reliably 
expressed in such a way should be selected for automation.
29 Of course, technological expertise is essential to determine what form an automated expression could take. A combination of both of legal and 
technological expertise should be needed
30 Such a domain-specific language would be an informal description of the operating principles of an algorithm or piece of computer code. It uses some
of the structured conventions of a computer programming language but is intended to be read and understood by humans, rather than a computer. 
There is no standard form of such a language, but it takes some of the style and syntax from programming languages, and it can be designed in 
whatever way the parties involved desire, provided each understands the constructs and precise rules involved
31 In concept, this is similar to the manner of calculating the exchange rates between two currencies on a cross-exchange basis, through their respective
exchange rates with the US dollar

## Page 14

Whitepaper: Smart Derivatives Contracts: From Concept to Construction
14
Many parts of a derivatives contract cannot be expressed in such a manner and will need to be 
expressed in natural language. A lawyer is unlikely to be able to confirm that the legal drafting 
in a contract that requires the exercise of reason or conscience (for example, that something is to 
be determined by a person in good faith and a commercially reasonable manner) has the same 
meaning when it is represented in a form that is based on logical processes. Even if this were 
possible technologically, a lawyer is unlikely to be able to validate that its outcome is the same as the 
application of legal reasoning to the traditional contract, because the determination of these matters 
from a legal perspective is not simply the result of following clear, precise and logical steps 32. 
For this reason, it is likely that an iterative process between lawyers and programmers will be 
needed to work out what parts of the ISDA documentation framework would be legally effective if 
converted to an automatable form33. ISDA is well positioned to facilitate this work. 
Figure 5
Selection for Efficient Automation
Not all of the provisions of the ISDA documentation framework that could be effectively 
represented in an automatable form should be. For some, the level of effort required will not 
produce a sufficient benefit and will not be efficient. 
One example is events of default (as defined in the ISDA Master Agreement). Assuming the non￾defaulting party is rational, it may be possible to conceive a logical progression of steps that it will take in 
order to determine whether it will call an event of default and terminate the outstanding transactions. 
Under the current form of the event of default mechanism, the determination will be based on a 
range of factors beyond the scope of the contract itself, potentially including the relationship with 
the defaulting party – for instance, the impact on other contracts or relationships or information on 
the circumstances of other, unrelated entities. 
Theoretically, it is possible to comprehensively catalogue all these influences. However, it would be 
an immense task to even identify all the potential factors, let alone determine the way they influence 
the decision. This would involve such an extensive data set and heavy use of code to contemplate 
the range of possibilities that its use would be inefficient, even if theoretically possible.
32 It is possible for smart contract code to be programmed to pause for human input. However, this does not mean the code takes the place of the 
exercise of reason or conscience. It simply allows for it to occur before restarting
33 This iterative process will not only need to bridge differences in meaning between the written expressions used by lawyers and programmers, but 
also the unwritten differences in meaning in the use of expressions by lawyers and programmers. There is an analogy here to working out if the same 
contract terms have the same legal meaning when governed by two different laws
Automated performance of terms that can be legally validated
Rights and obligations for other terms of the contract
Smart 
derivatives 
contract
Formal representation governs
Natural language governs

## Page 15

Whitepaper: Smart Derivatives Contracts: From Concept to Construction
15
A number of factors are likely to influence the choice of what is efficient to represent in automatable form:
• Standardization: The provisions selected for automation should be standardized, so they are 
used in common form by many parties in many contracts. For example, although it would 
be possible to automate a provision agreed by two parties in the schedule of the ISDA Master 
Agreement, this would not be efficient if the provision is not commonly used by others.
• Complexity: The provisions selected for automation should not be overly complex. If 
the selected provisions require the operation of a large number of interconnected or 
interdependent rules at each stage of execution, then this could mean that the process is 
difficult to establish, operate and maintain.
• Externalities: If the provisions selected for automation are triggered by factors that are 
external to the contract, then the ability to import that trigger into the automated form needs 
to be considered. For example, if the trigger is an observable market-based event, then it may 
not cause any concern. If it is the exercise of some discretion, including by someone not party 
to the contract, then the ability to have the result of this event incorporated into the contract 
needs to be carefully considered. If it is not a simple matter, then the automation of this 
provision may not be efficient.
• Commonality: Smart derivatives contracts that are to serve as functions in the ISDA CDM 
would be more useful if they are used with more than one derivatives product. That’s because 
the ISDA CDM seeks to avoid making functions product-specific where possible. Commonality 
of the functions performed by the automation provisions is therefore important.
Further Work in Developing Selection Principles
The selection of the provisions within the ISDA documentation framework that could be chosen 
for automation in smart derivatives contracts is important further work for ISDA and its members. 
It should be based on what is effective (meaning what can be automated without changing legal 
effect), as well as what is efficient (meaning the work required to standardize its automated form 
will be used enough to make it worthwhile). 
A simple example of this would be the calculation of an amount based on a formula, such as a fixed-rate 
payer amount calculation in an interest rate swap. An illustrative example of how this could be done is set 
out in the Constructing a Smart Derivatives Contract section of this paper. This selection of effective and 
efficient provisions for automation is the first step in the framework suggested in this paper (see Figure 6). 
However, before demonstrating how the next steps could be taken, it is necessary to consider 
another stream of legal complexities – those caused by laws operating beyond the contract.
Figure 6
Select the 
parts of a 
derivatives 
contract 
for which 
automation 
would be both 
effective and 
efficient
Change the 
expression of 
the legal terms 
of a derivatives 
contract 
into a more 
formalized 
form
Break the 
formalized 
expression into 
component 
parts for 
representation 
as functions
Combine the 
functions into 
templates
for use with 
particular 
derivatives 
products
Validate the 
templates as 
having the 
same legal 
effect as 
legal terms 
of derivatives 
contracts

## Page 16

Whitepaper: Smart Derivatives Contracts: From Concept to Construction
16
COMPLEXITY OUTSIDE THE CONTRACT
“Tamper-proof code might not be suitable for high-value, long-duration, highly-regulated financial 
contracts. Discretion is a key issue with many such contracts, and there must be support for the smart 
contract code to request human input. Furthermore, a change in applicable law might require smart 
contract code to be stopped and perhaps modified before continuing.” 34
The impact of laws on the performance of contracts is not limited to the meaning of their terms. 
Binding parties to perform the terms they have agreed is only one aspect of the law’s influence 
on contracts. In some circumstances, laws will change or prohibit performance of a contract. 
Furthermore, agreement to a contract’s terms does not mean that laws will always cause it to be 
performed. It is important to take these laws into account when constructing smart derivatives 
contracts. 
Laws Affecting Contractual Performance
Laws can interrupt the performance of contracts or cause the reversal of performance of contracts. 
These laws express the public policy that interrupting or reversing a contract is more important than 
compelling the parties to fulfill their obligations in accordance with contractual terms. 
Examples include laws that render obligations under a contract void or voidable. This can happen 
if a contract is found to be unauthorized, improper or fraudulent, if the purpose of the contract or 
the conduct of parties is unlawful or upon the bankruptcy or insolvency of one of the parties. In the 
case of derivatives, this includes insolvency laws that would render the close-out netting provisions 
of an ISDA Master Agreement unenforceable or open to challenge if not for the safe harbors and 
special legislative protection offered to them in many jurisdictions.
Laws can also change the terms of a contract expressly agreed between parties. Terms can be implied 
by law (such as under consumer protection legislation), they can be found void and removed, and 
they can be changed by rectification if a court finds they do not reflect the true agreement between 
the parties.
The complexity created by these laws cannot be avoided by the terms of a contract, as these laws 
override contractual terms. In the context of smart derivatives contracts, the focus should be on 
managing the impact of these laws on the automatic operation, so the contract is not performed 
when it no longer represents the legal obligations of the parties, or when it is unlawful. 
Laws Relevant to Non-performance
From a legal perspective, parties agreeing to perform obligations under a legal contract does not 
ensure that performance will actually happen. A party may not be able to perform because of a 
range of possible practical or legal constraints, such as impossibility or bankruptcy. The contract sets 
out what the parties agree they will do for each other. Of course, the parties could do more for each 
other than what they specify in the contract, but the contract sets out the minimum requirements 
of the parties’ performance and it serves as a benchmark to determine the consequences if they do 
not.
34 Clack, C., Smart Contract Templates: Legal semantics and code validation (2018), Journal of Digital Banking
A legal contract 
can be affected 
by a number of 
external events, 
which must 
be considered 
when 
developing 
smart contracts

## Page 17

Whitepaper: Smart Derivatives Contracts: From Concept to Construction
17
If a party defaults on its obligations, then the consequences of the non-performance can be varied, 
even when non-performance is contemplated by the terms of the contract. For example, the ISDA 
Master Agreement contemplates a termination process that can be initiated in the case of a party’s 
default. However, the other party has a range of possible choices of what it can do next, beyond 
calling an event of default and initiating that termination process. It could choose to suspend its 
own performance under Section 2(a)(iii), or it could choose to ignore the default and continue to 
perform. It could also choose to take separate legal action to recover amounts that have not been 
paid to it, or seek to set them off against its own obligations or enforce against collateral. There are 
many interdependencies involved in making these choices, and the approach taken is not possible to 
predict with certainty.
A further complication related to non-performance arises because parties to a contract can choose 
not to perform by willingly breaching the contract. If it is a legally enforceable contract, then there 
are consequences if this happens, such as an obligation to compensate the other party, usually 
through the payment of damages. 
Nevertheless, it is a choice that parties to a contract can make, and in certain circumstances (such as 
pending insolvency), it is an option that can be important and valuable. 
These create complications for smart derivatives contracts, as they mean that automation of 
performance of the agreed terms of a contract so they are executed in a tamper-proof way is not 
always going to be consistent with the legal outcome of the contract. 
Managing Complexity Outside of the Contract
There are at least three approaches that could be taken in constructing smart derivatives contracts to 
manage complexities that are introduced by laws beyond the contract. 
One approach is to attempt to set out all the possible circumstances and the consequences. Due 
to the huge amount of possibilities and complexity, this would not be feasible and would seem 
impossible. Any approximation would change the legal substance of the relationship between the 
parties, which would no longer represent the agreement they otherwise would have had with each 
other. 
Another approach is to let the smart derivatives contract continue to perform automatically in 
ignorance of these laws and for the parties to deal with the consequences outside of its operation. 
Legally speaking, this can be risky. The consequences of continuing to perform obligations 
originally required by a contract but that have become contrary to law are not limited to significant 
economic loss (for example, amounts paid may not be recoverable in insolvency), but also include 
potential legal action and penalties (such as for breach of anti-money laundering laws). This too 
would therefore appear to be a sub-optimal outcome.
Suspending Automatic Performance
A further approach is to build in a right for either party to suspend the automatic performance 
of a smart derivatives contract. This is not suspending the contract between the parties – just its 
automatic performance. The parties’ rights and obligations continue to exist. For example, if there is 
a default under a smart derivatives contract, the non-defaulting party could suspend the automatic 
performance of the obligations under the transactions and exercise its rights to close-out those 
transactions. Using the approach suggested in the previous section of this paper, the performance of 
the contract ceases to be governed by the parts expressed in formal representation. Instead, they are 
governed by the parts expressed in natural language.

## Page 18

Whitepaper: Smart Derivatives Contracts: From Concept to Construction
18
This right to suspend does not have to be limited to when a party defaults. It would be useful in 
other circumstances, such as when errors have been identified that need to be corrected. The ability 
to suspend automatic performance would be particularly important where the technology on which 
the automatically performed parts of the smart contract operate is, from a technology perspective, 
immutable. This could be the case for smart contracts held on a blockchain or other distributed 
ledger technology 35. This approach has the advantage that the automatic performance does not 
complicate the resolution of the legal complexity.
Figure 7
Further Work
Including a right to suspend the automatic performance of the smart derivatives contract’s terms 
need not be considered to nullify its utility. The automatically performed terms would apply 
where they still accurately reflect the parties’ legal relationship and then cease apply where they 
do not. Automatic performance of the smart derivatives contract could be recommenced after the 
suspension with a new state or modified parameters (or both). 
Taking such an approach removes some of the challenges that arise in trying to automate the 
nuances and complexities of financial market contracts. Where flexibility is required that is beyond 
what is possible to express in a formal representation of the terms, then it can be left to the natural 
language provisions, on the basis that either of the parties could choose to suspend the application 
of the automated provisions. 
Assessing how such a suspension right can be constructed, and if there should be any conditions to 
its use, is an important area of further work for ISDA and its members.
35 The immutability of a blockchain arises from its ‘append only’ nature. This means that new information can be added, but the existing information 
cannot be altered 
Automated performance of 
contractual terms
No other rights and 
obligations exercised or 
performed
Ordinary contractual 
lifecycle events
No automated performance
Post-default rights and 
obligations exercised and 
performed
Post-default 
contractual events Default
Smart 
derivatives 
contract
Formal representation governs
Natural language governs

## Page 19

Whitepaper: Smart Derivatives Contracts: From Concept to Construction
19
CONSTRUCTING A SMART DERIVATIVES CONTRACT
“We now have at our disposal a rich language for describing financial contracts. This is already useful 
for communicating between people – the industry lacks any such precise notation. But in addition, a 
precise notation lends itself to automatic processing of various sorts.” 36
There are similarities between legal drafting and programming languages because each uses rules and 
constructs. The commonality between them is important to constructing smart derivatives contracts 
that can be validated legally, because it allows a shared representation of contractual provisions 
between them.
This section of the paper seeks to identify key areas where the similarities exist and shows how they 
might be used to construct a smart derivatives contract through the formalization of legal terms. To 
do so, it uses provisions from a sample interest rate swap transaction to illustrate the issues and steps 
formalization could take. 
Variables and Functions
Legal drafting uses defined terms as names to refer to objects. For example, an interest rate swap 
confirmation could include the following:
Party A: ABC Bank Ltd
Party B: DEF Corporation Plc 37
Programming languages also use names to refer to objects, often referred to as variables. For 
example, Party A is a variable given the value is ABC Bank Ltd and Party B is a variable given the 
value of DEF Corporation Plc. 
Legal drafting also uses operative clauses to carry out procedures using defined terms. An example of 
this is Section 5.1 of the 2006 ISDA Definitions, which sets out how to determine the fixed amount 
payable by the fixed rate payer (a defined term itself). Programming languages can use functions to 
carry out procedures using variables, or the results of other functions. 
Using this commonality, the calculation of the fixed amount under Section 5.1 of the 2006 ISDA 
Definitions could be described as a function using variables such as the payment dates, the fixed 
rate and the fixed rate day count fraction. The values of these variables are set out in the relevant 
confirmation and the function is the procedure set out in Section 5.1. The result of following 
these steps with these variables is a value being given to ‘fixed amount’ for a payment date. This 
connection between operative clauses and functions is also shown by the ISDA CDM.
36 Peyton Jones, S.L., Eber, J.M., and Seward, J., Composing contracts: an adventure in financial engineering, ACM SIGPLAN International Conference 
on Financial Programming (KFP’00), Montreal, September 1, 2000
37 Defined terms in a contract can be much more complex than this example, consisting of lists of objects, a number of other defined terms or even a 
procedure that is applied to a number of defined terms having a particular result (which can be akin to a function in a programming language)
An important 
step to 
developing 
smart contracts 
is to construct a 
shared, formal 
representation 
of legal terms

## Page 20

Whitepaper: Smart Derivatives Contracts: From Concept to Construction
20
Drafting Precision
Although legal drafting and programming languages share similarities in use of variables and 
functions, there is a difference between them in the precision required in the use of language. 
This is because of the difference in the user of the language. Legal drafting is used by humans and 
programming languages are used by machines 38. Although both humans and machines can learn 
the rules of a language, humans are more able to work out the meaning of statements that are not 
expressed in accordance with those rules. This means legal drafting can use different words, or a 
different word order, to mean the same thing.
For example, it would not be unusual for an additional payment to be specified in a derivatives 
confirmation in the following manner:
Party A Payment Amount: $1,000,000
Party A Payment Date: August 1, 2018
Although this expression is not strictly in compliance with the framework stipulated in the 2006 ISDA 
Definitions 39, it would be understood to mean that Party A must pay $1 million on August 1, 2018.
Programming languages are used to state things precisely. If a word is used incorrectly, or is not 
defined, then it either cannot operate or cannot operate in the manner intended. This means that a 
greater level of precision is required in preparing legal language for adoption for automation40. 
In the case of derivatives, such precision is not just a question of following the relevant ISDA 
definitions more strictly. In some cases there is insufficient precision within the ISDA definitions 
themselves. An example of this within the 2006 ISDA Definitions are the terms ‘relevant’ or 
‘applicable’ when used in conjunction with a defined term that contains more than one date or 
period of time, or the terms ‘in relation to’ or ‘in respect of’ particular terms, dates or things. 
Understanding the meaning of these provisions and whether they intend to have the same meaning 
requires a level of flexibility that is beyond that of rule-based machines used in automation. 
Control Structures
Structural rules are often applied in legal drafting, from grammatical rules to drafting rules written 
into a contract. These are important in carrying out functions in the right manner. 
Examples of these in the 2006 ISDA Definitions include:
• The requirement for a sequence of steps to be followed in the process for the exercise of an option 
transaction in Section 13.2;
• The requirement for a selection to be made using logical conditions in determining the correct 
floating rate in Section 6.2; and
38 This is a necessary over-simplification. Programming languages are used by human programmers. Machines use the machine code that the 
programming language is turned into
39 The 2006 ISDA Definitions provide for floating amounts, fixed amounts, initial exchange amounts, interim exchange amounts and final exchange 
amounts
40 This is another necessary over-simplification. A good programming language can also permit the programmer to model alternative inputs and apply 
methods to understand human inputs

## Page 21

Whitepaper: Smart Derivatives Contracts: From Concept to Construction
21
• The requirement for repetition of steps multiple times until an answer is worked out in 
determining the fallbacks that apply if a particular rate is not displayed on the relevant screen at 
the relevant time in Section 7.1. 
Programming languages also use similar structures. However, there is a need for more precision 
in preparing these structures for the same reason as applies for precision in meaning of words – a 
human user has more flexibility to work out the right method to follow to understand legal drafting 
than a machine has to understand the right method in programming languages. This is perhaps 
most evident from the principle that the ultimate user of legal drafting (a court) will try to give 
some meaning to it, rather than to conclude there is no meaning at all. 
Example of Formalization
Using these principles, it is possible to attempt the formalization of selected parts of legal drafting in 
derivatives contracts. It is not necessary to learn a programming language to do this – the intent is 
to bridge the gap between legal drafting and programming languages in a manner that lawyers and 
programmers can both use and understand. This is the second step in the framework suggested in 
this paper.
Figure 8
Here is an example using the ‘fixed amount’ definition in the 2006 ISDA Definitions. Section 5.1 
reads as follows:
Section 5.1. Calculation of a Fixed Amount. The Fixed Amount payable by a party on a Payment Date 
will be:
(a) If an amount is specified for the Swap Transaction as the Fixed Amount payable by that party for 
that Payment Date or for the related Calculation Period, that amount; or
(b) If an amount is not specified for the Swap Transaction as the Fixed Amount payable by that party 
for that Payment Date or for the related Calculation Period, an amount calculated on a formula 
basis for that Payment Date or for the related Calculation Period as follows:
Fixed Amount = Calculation Amount x Fixed Rate x Fixed Rate Day Count Fraction.
Select the 
parts of a 
derivatives 
contract 
for which 
automation 
would be both 
effective and 
efficient
Change the 
expression of 
the legal terms 
of a derivatives 
contract 
into a more 
formalized 
form
Break the 
formalized 
expression into 
component 
parts for 
representation 
as functions
Combine the 
functions into 
templates
for use with 
particular 
derivatives 
products
Validate the 
templates as 
having the 
same legal 
effect as 
legal terms 
of derivatives 
contracts

## Page 22

Whitepaper: Smart Derivatives Contracts: From Concept to Construction
22
A first step could be to turn the natural language text into a series of instructions, with one function 
(where possible) per line:
The Fixed Amount
payable by a party on
a Payment Date will be:
If an amount is specified for the Swap Transaction as the Fixed Amount payable by that party for 
that Payment Date or for the related Calculation Period,
That amount; or
If an amount is not specified for the Swap Transaction as the Fixed Amount payable by that 
party for that Payment Date or for the related Calculation Period,
an amount calculated on a formula basis for that Payment Date or for the related Calculation 
Period as follows: Fixed Amount = Calculation Amount x Fixed Rate x Fixed Rate Day 
Count Fraction.
A further step is to further formalize the wording using some of the principles set out earlier in 
this section:
Fixed Amount (PARTY):
FOR Payment Date(n):
IF
EITHER
amount is specified as Fixed Amount(PARTY) for Payment Date(n) 
OR
amount is specified as Fixed Amount(PARTY) for Calculation Period(n) THEN
EQUALS amount specified
ELSE
EQUALS Calculation Amount × Fixed Rate × Fixed Rate Day Count Fraction
This formalized version differs in its drafting from the original natural language drafting as it uses 
‘IF’, ‘THEN’, ‘ELSE’ as control flow statements, ‘OR’ as an operator, ‘EQUALS’, ‘FOR’ and 
‘EITHER’ as logic statements, ‘x’ as a mathematical symbol and () to apply a term to a particular 
party or date. The result is a more structured and formal version of the original legal drafting 
without losing the optionality and meaning within the clause. There also remain some natural 
language elements to assist understanding of the text 41.
41 For example, attempts to formalize what ‘specified’ means have not been attempted at this stage, on the basis that the parties understand that it is 
the amount specified in the relevant confirmation of the transaction, however that may end up being recorded in a smart contract format. If this is 
determined to be a particular repository or piece of code, reference could be made to it if desired. In addition, things that are ‘specified’ might also be 
specified dynamically by a party during performance of a contract

## Page 23

Whitepaper: Smart Derivatives Contracts: From Concept to Construction
23
This is only a sample to show what could be meant by a shared, formal representation of the 
provisions selected for automation. Much more work would need to be conducted to make 
this useable. Furthermore, this uses one of the simplest examples that can be taken from ISDA 
documentation. Increasing complexity produces more complicated results, especially if it is to run 
multiple times.
However, even this simple example shows that it is important the parties agree the precise notation 
to be used, so they can trust that the formalized version reflects the legal drafting version and the 
parties’ intentions. That notation would be an important standard for use in smart derivatives 
contracts, and this represents another stream of potential further work for ISDA and its members, 
perhaps through the ISDA CDM and/or as part of ISDA’s proposed update to the 2006 ISDA 
Definitions42.
To illustrate this point, the ISDA CDM 1.0 describes the calculation of the fixed amount using a 
further formalized version. This is expressed as:
fixedAmount number: calculationAmount * rate * dayCountFraction
currencyAmount CurrencyEnum: currencyAmount
Each of the elements set out in the calculation are expressed as a set of arguments (sign 
posts) to locate their inputs (or point to further calculations to calculate their values). The 
calculationAmount, rate or dayCountFraction arguments used for an ‘InterestRatePayout’, are 
expressed in the ISDA CDM 1.0 as follows43:
calculationAmount: is InterestRatePayout -> quantity -> notionalSchedule -> notionalStepSchedule -> 
initialValue
currencyAmount: is InterestRatePayout -> quantity -> notionalSchedule -> notionalStepSchedule -> 
currency
rate: is InterestRatePayout -> interestRate -> fixedRate -> initialValue
dayCountFraction: is InterestRatePayout -> dayCountFraction
Breaking Down into Component Functions
The expression of a legal term in a formalized form that can be understood clearly by both lawyers 
and programmers should be an important step in its conversion into a programmatic form. 
However, use in the ISDA CDM would also require that the term be broken down into component 
functions. As noted above, the ISDA CDM contemplates that functions should not be product￾specific, and can be combined to form templates relevant to particular products. The ability to 
develop component functions that can be used with multiple products is an important factor in 
selecting which parts of a derivatives contract should be initially selected for representation in smart 
contract form44. This forms the third step in framework suggested in this paper.
42 ISDA has recently commenced a survey of its membership to obtain feedback on a proposed update to the 2006 ISDA Definitions. The update aims to
refresh the definitions, consolidate existing supplements into a single version and include results of work across each of the various global benchmark 
reform initiatives. As part of the survey, ISDA is consulting with members as to whether they would like ISDA to consider redrafting the definitions in a 
more formal or machine-readable way as a means of supporting industry adoption of new technology, such as smart contracts
43 For more detailed explanation of the ISDA CDM 1.0, see the ISDA Common Domain Model (ISDA CDM) Supporting Material
44 Using operative provisions from different types of products in the one derivatives transaction is not new. It is common for equity derivatives to have 
payment obligations described by both the 2002 Equity Derivative Definitions as well as the 2006 ISDA Definitions

## Page 24

Whitepaper: Smart Derivatives Contracts: From Concept to Construction
24
Figure 9
An initial step to identifying operative legal drafting that can be broken down into functions is to 
identify the same calculation being used for different reasons. For example, both the calculation 
of the fixed amount and floating amount within the 2006 ISDA Definitions use a very similar 
mathematical calculation. Both multiply the calculation amount by a particular rate and a particular 
day count fraction. The difference between the fixed leg and the floating leg of the transaction is 
the result of the values of the variables applied to them, not the function that calculates them. This 
makes it possible to develop one function for the determination of an amount by reference to an 
interest rate (either fixed or floating), as long as the correct elements are input into that function to 
produce the correct derived observation.
Using the same formalization principles used above, the way the ISDA CDM 1.0 has grouped 
features together 45 and the use of ‘(leg)’ to refer to the relevant fixed or floating elements 46
(expressed in the ISDA CDM 1.0 as different ‘payouts’, each comprising a leg of the trade), this 
function could be written as:
InterestRatePayout(leg):
FOR PaymentDate(n):
EQUALS calculationAmount × interestRate(leg) × dayCountFraction(leg)
The relevant interestRate and dayCountFraction applicable to the leg would be need to be specified 
(being the observations as described in the ISDA CDM). For example, taking an Australian dollar 
fixed/floating interest rate swap where the fixed rate is 3.00% and the floating rate references the 
Australian dollar bank bill swap rate plus a spread of 1.50%, this could be expressed as:
leg(fixed):
interestRate(fixed) -> fixedRate: 
EQUALS 3.00 per cent. per annum
dayCountFraction(fixed): 
EQUALS Act/365 (Fixed)
45 In particular, see Figure 6 of the ISDA Common Domain Model (ISDA CDM) Supporting Material, page 16
46 The term ‘(leg)’ is used in this manner in ISDA’s 2011 Equity Derivative Definitions
Select the 
parts of a 
derivatives 
contract 
for which 
automation 
would be both 
effective and 
efficient
Change the 
expression of 
the legal terms 
of a derivatives 
contract 
into a more 
formalized 
form
Break the 
formalized 
expression into 
component 
parts for 
representation 
as functions
Combine the 
functions into 
templates
for use with 
particular 
derivatives 
products
Validate the 
templates as 
having the 
same legal 
effect as 
legal terms 
of derivatives 
contracts

## Page 25

Whitepaper: Smart Derivatives Contracts: From Concept to Construction
25
leg(floating):
interestRate(floating) -> floatingRate: 
EQUALS AUD-BBR-BBSW-Bloomberg + 1.50 per cent. per annum
dayCountFraction(floating): 
EQUALS Act/365 (Fixed)
Of course, each of the dayCountFraction elements and interestRate(floating) element are themselves 
calculations that could be described as functions and should be further defined and formalized47.
Combination of Functions into Product Templates
The interest rate amount function described above could be utilized in any product where there 
is an amount payable calculated by reference to an interest rate, or even some other rate. Similar 
functions are used in credit derivatives, equity derivatives and commodity derivatives, for example. 
Other functions could be built that set out other operations used commonly in derivatives. The 
ISDA CDM 1.0 utilizes this concept by inferring the product through the economic terms and 
payout classes used, and by identifying features of the components of the transaction. For example, 
a credit default swap would have a ‘CreditDefaultPayout’ leg and an ‘InterestRatePayout’ leg. These 
functions could also be used in combination with each other to create more complex bespoke 
derivatives transactions, just as lawyers and market participants use elements of different definition 
booklets in highly structured transactions today.
This combination of functions into templates for particular products is the fourth step in the 
framework suggested in this paper. It is also an opportunity for important collaborative work 
between ISDA and its members, as is currently being progressed through the ISDA CDM 1.0. 
As noted previously, this step offers the greatest opportunity to make smart derivatives contracts 
‘smart’, and will require a significant amount of cross-disciplinary attention and effort to make them 
truly effective.
Figure 10
47 Within the ISDA CDM, these are described as basic elements to highlight the different levels in the hierarchical lineage (see pages 35 and 37). Within 
the ISDA CDM 1.0, these have been formalized further by including specific day count fraction calculations and arguments, as well as an argument for 
determining the spread for the particular trade. See common domain model documentation file ‘model_cdm_calculations.rosetta’
Select the 
parts of a 
derivatives 
contract 
for which 
automation 
would be both 
effective and 
efficient
Change the 
expression of 
the legal terms 
of a derivatives 
contract 
into a more 
formalized 
form
Break the 
formalized 
expression into 
component 
parts for 
representation 
as functions
Combine the 
functions into 
templates
for use with 
particular 
derivatives 
products
Validate the 
templates as 
having the 
same legal 
effect as 
legal terms 
of derivatives 
contracts

## Page 26

Whitepaper: Smart Derivatives Contracts: From Concept to Construction
26
Validating the Legal Effect of the Product Templates
The final step in the framework suggested in this paper is the validation of the legal effect of the 
templates of the formalized terms of the selected contractual provisions prepared in the previous 
four steps. The importance of this was described earlier in this paper in the Complexity in the 
Contract section. 
There is no doubt that this will be a challenging task, but perhaps no more challenging than the 
tasks coordinated by ISDA in the context of its existing documentation framework, which provides 
legally valid templates to complex financial transactions. A key part to managing this challenge 
is to involve lawyers in the previous four steps of the framework, rather than waiting until the 
end of the process. That way, validation becomes the logical end of a discursive process between 
lawyers, programmers and market participants. There are many ways in which this process could be 
conducted, and ISDA has many examples from the development of its documentation that it could 
draw upon to facilitate this.
Figure 11
Select the 
parts of a 
derivatives 
contract 
for which 
automation 
would be both 
effective and 
efficient
Change the 
expression of 
the legal terms 
of a derivatives 
contract 
into a more 
formalized 
form
Break the 
formalized 
expression into 
component 
parts for 
representation 
as functions
Combine the 
functions into 
templates
for use with 
particular 
derivatives 
products
Validate the 
templates as 
having the 
same legal 
effect as 
legal terms 
of derivatives 
contracts

## Page 27

Whitepaper: Smart Derivatives Contracts: From Concept to Construction
27
CONCLUSION
Taking smart derivatives contracts from a promising concept to practical construction in a 
complicated market-place is a complex task. Not only is it necessary to maintain compliance with 
technological, commercial, regulatory and legal standards, but it is also necessary for there to be 
confidence that the legal effect of the derivatives contract is the same whether or not its performance 
is to be automated. The areas of legal complexity described in this paper mean that this requires 
coordination of expertise in technology, market practice and law. 
ISDA has a proven track record in coordinating expertise to solve complicated problems in 
the derivatives markets, and the ISDA CDM provides guidance on the way forward for smart 
derivatives contracts. It could create a representation ‘standard’ for derivatives contracts and their 
lifecycle that can be shared across multiple uses – including the construction of smart derivatives 
contracts.
This paper suggests a practical approach (from a legal perspective) that could be taken to developing 
smart derivatives contracts, and suggests a number of areas where further work could be beneficial. 
This includes work in determining principles for selecting which parts of the ISDA documentation 
framework lend themselves to automation, the framework that should be used for their more formal 
representation, the distillation of functions from them, and the creation of templates from those 
functions. It could also include principles for the suspension of automatic performance. 
Each of these requires the collaboration of the users of smart derivatives contracts – the participants 
in the international derivatives market – and each of these would benefit from the involvement of 
ISDA. This work is important in facilitating safe, efficient markets for derivatives, in whatever form 
or representation they take in the future.
Collaboration 
between 
lawyers, 
technologists 
and market 
participants 
is vital in 
the creation 
of smart 
derivatives 
contracts

## Page 28

Whitepaper: Smart Derivatives Contracts: From Concept to Construction
28
ABOUT KING & WOOD MALLESONS
Recognised as one of the world’s most 
innovative law firms, King & Wood 
Mallesons offers a different perspective 
to commercial thinking and the client 
experience. As a leading international law firm 
headquartered in Asia, KWM helps clients to 
open doors and unlock opportunities as they 
look to Asian markets to unleash their full 
potential. Combining an unrivalled depth of 
expertise and breadth of relationships in our 
core markets, we are connecting Asia to the 
world, and the world to Asia.
ABOUT ISDA
Since 1985, ISDA has worked to make the 
global derivatives markets safer and more 
efficient. Today, ISDA has over 900 member 
institutions from 68 countries. These members 
comprise a broad range of derivatives market 
participants, including corporations, investment 
managers, government and supranational 
entities, insurance companies, energy and 
commodities firms, and international and 
regional banks. In addition to market 
participants, members also include key 
components of the derivatives market 
infrastructure, such as exchanges, intermediaries, 
clearing houses and repositories, as well as 
law firms, accounting firms and other service 
providers. Information about ISDA and its 
activities is available on the Association’s website: 
www.isda.org. Follow us on Twitter @ISDA.
