# hkma otc derivatives consultation mar 2024

*Converted from: hkma-otc-derivatives-consultation-mar-2024.pdf*

---

## Page 1

Joint further consultation on enhancements to the OTC 
derivatives reporting regime for Hong Kong to mandate – 
(1) the use of Unique Transaction Identifier, (2) the use of
Unique Product Identifier and (3) the reporting of Critical
Data Elements
and 
Joint consultation conclusions on revising the list of 
designated jurisdictions for the masking relief
March 2024

## Page 2

2
TABLE OF CONTENTS 
Foreword...................................................................................................................................... i
Personal Information Collection Statement ............................................................................iii
Executive summary.................................................................................................................... 1
Mandating the use of UTI ....................................................................................................... 1
Mandating the use of UPI ....................................................................................................... 1
Mandating the reporting of CDE ............................................................................................ 2
Mandating the adoption of ISO 20022 Standard................................................................... 2
Conclusions on revising the list of designated jurisdictions for the masking relief ......... 2
Timeline for submitting comments........................................................................................ 2
Conclusions and further consultation on mandating the use of UTI...................................... 4
Proposed implementation timeline and interim measure .................................................... 4
Proposed requirements for reporting UTI............................................................................. 5
Proposed responsibility for generating UTI.......................................................................... 6
Proposed approaches to UTI ................................................................................................. 9
Proposed structure and format of UTI................................................................................... 9
Responsibility to provide or obtain UTI in a timely manner ................................................ 9
Consultation on mandating the use of UPI.............................................................................11
Proposed structure and format of UPI ................................................................................11
Proposed approaches to the implementation of UPI .........................................................12
Consultation on mandating the reporting of CDE..................................................................13
Proposed approaches to CDE .............................................................................................13
Proposed implementation timeline......................................................................................16
Proposed treatment of live legacy transactions and other transitional issues................17
Consultation on adoption of the ISO 20022 Standard ...........................................................19
Conclusions on revising the list of designated jurisdictions for the masking relief...........20
The way forward.......................................................................................................................22
Appendix A – List of respondents...........................................................................................23
Appendix B – List of proposed data elements for reporting.................................................24
Appendix C – Jurisdictions in the SFC designated list gazetted on 7 July 2015.................25

## Page 3

i
Foreword
In line with the Group of 20 (G20) commitment to reform over-the-counter (OTC) derivatives
markets, the Hong Kong Monetary Authority (HKMA) and the Securities and Futures 
Commission (SFC) have been working with the Government of the Hong Kong Special 
Administrative Region and relevant stakeholders on implementing a regulatory regime for the 
OTC derivatives market in Hong Kong.
OTC derivatives reporting is an important component of the OTC derivatives regulatory regime.
We have implemented two phases of mandatory reporting, covering OTC derivatives
transactions in five key asset classes — interest rates, foreign exchange, credit, commodities 
and equities. The use of Legal Entity Identifier (LEI) has also been mandated and is applicable to 
all entities on the reporting entity’s side of a transaction.
To facilitate the aggregation of OTC derivatives data through standardisation and harmonisation 
of data elements, the Committee on Payments and Market Infrastructures and the International 
Organization of Securities Commissions (CPMI-IOSCO) published a technical guidance (UTI 
Technical Guidance) on the harmonisation of the unique transaction identifier (UTI) in February 
2017, a technical guidance (UPI Technical Guidance) on the harmonisation of the unique 
product identifier (UPI) in September 2017, and three versions of technical guidance (CDE
Technical Guidance) on the harmonisation of critical OTC derivatives data elements (other than 
the unique transaction identifier and unique product identifier) (CDE) in April 2018, September 
2021 and September 2023. These technical guidances set out the approaches, definitions and 
characteristics of key reportable data elements (ie, the UTI, UPI and CDE) for authorities to 
consider in implementing their respective OTC derivatives reporting regimes.
To align with global developments, the HKMA and the SFC issued a joint consultation paper in 
April 2019 (2019 Consultation Paper) on mandating the use of UTI in Hong Kong and other 
proposals. We received a total of 15 submissions with mixed and divergent views. A list of 
respondents is set out in Appendix A. This prompted discussions on how UTI should be 
implemented in Hong Kong and globally. Nevertheless, there was insufficient consensus 
internationally and among market participants at that time. 
Over the past four years, we have seen active international discussions promoted by the 
Committee on Derivatives Identifiers and Data Elements (CDIDE) 1, and controversial issues 
being resolved with the joint efforts of regulators and market participants worldwide. Major 
jurisdictions have been making progress, including launching and concluding related 
consultations as well as implementing UTI, UPI and CDE. We believe the time is ripe for us to 
conclude and further consult on the UTI framework in this paper.
In addition, we set out in this paper our proposal on mandating the use of UPI, the reporting of 
CDE and the adoption of the International Organization for Standardization (ISO) 20022 standard 
for the reporting obligation in Hong Kong. Furthermore, this paper provides conclusions to our
consultation on revising the list of designated jurisdictions for the masking relief set out in the 
2019 Consultation Paper. This paper should be read together with the 2019 Consultation Paper 
and all comments received, which can be viewed on the websites of the HKMA and the SFC.
1 CDIDE is a standing working group under the Regulatory Oversight Committee of the Global Legal Entity Identifier 
Foundation for matters relating to the implementation and adoption of UTI, UPI and CDE.

## Page 4

ii
We take this opportunity to thank everyone who took the time and effort to submit comments to 
the 2019 Consultation Paper. Your feedback has been most useful in helping us finalise various 
aspects of our regime.
For the further consultation in this paper, we invite interested parties to submit written comments 
on the proposals to either the HKMA or the SFC on or before 17 May 2024. Comments may be 
submitted by any of the following methods –
By online submission at: http://www.sfc.hk/edistributionWeb/gateway/EN/consultation/
By email to: fss@hkma.gov.hk or otcconsult@sfc.hk
By fax to: (852) 2878 7297 or (852) 2521 7917 
By post to one of the following:
Financial Stability Surveillance Division 
Hong Kong Monetary Authority 
55/F Two International Finance Centre 
8 Finance Street, Central 
Hong Kong 
Supervision of Markets Division 
Securities and Futures Commission 
54/F, One Island East
18 Westlands Road
Quarry Bay, Hong Kong
Persons submitting comments on behalf of an organisation should provide details of the 
organisation whose views they represent.
Please note that the names of respondents and the contents of their submissions may be 
published by the HKMA and the SFC on their respective websites and in other documents 
to be published by them. In this connection, please read the Personal Information 
Collection Statement attached to this consultation paper.
If you do not wish your name or submission to be published by the HKMA and the SFC, 
please state that you wish your name, your submission or both to be withheld from 
publication when you make your submission.
22 March 2024

## Page 5

iii
Personal Information Collection Statement 
1. This Personal Information Collection Statement (PICS) is made in accordance with the 
guidelines issued by the Privacy Commissioner for Personal Data. The PICS sets out the 
purposes for which your Personal Data2 will be used following collection, what you are 
agreeing to with respect to the HKMA’s and the SFC’s use of your Personal Data and 
your rights under the Personal Data (Privacy) Ordinance (Cap. 486) (PDPO). 
Purpose of collection
2. The personal data provided in your submission in response to this consultation paper 
may be used by the HKMA or the SFC for one or more of the following purposes –
(a) to administer –
(i) the provisions of the Banking Ordinance (Cap. 155) and guidelines 
published pursuant to the powers vested in the HKMA; and
(ii) the relevant provisions3 and codes and guidelines published pursuant to 
the powers vested in the SFC; 
(b) to perform statutory functions under the provisions of the Banking Ordinance (Cap. 
155), the Securities and Futures Ordinance (Cap. 571) and relevant provisions;
(c) for research and statistical purposes; or 
(d) for other purposes permitted by law. 
Transfer of personal data
3. Personal data may be disclosed by the HKMA or the SFC to members of the public in 
Hong Kong and elsewhere as part of this public consultation. The names of persons who 
submit comments on this consultation paper, together with the whole or any part of their 
submissions, may be disclosed to members of the public. This will be done by publishing 
this information on the HKMA and the SFC websites and in documents to be published by 
the HKMA and the SFC during the consultation period or at its conclusion. 
Access to data 
4. You have the right to request access to and correction of your personal data in 
accordance with the provisions of the PDPO. Your right of access includes the right to 
obtain a copy of your personal data provided in your submission on this consultation 
2 Personal data means personal information as defined in the Personal Data (Privacy) Ordinance (Cap. 486). 3 The term “relevant provisions” is defined in section 1 of Part 1 of Schedule 1 to the Securities and Futures Ordinance 
(Cap. 571) and refers to the provisions of that Ordinance together with certain provisions in the Companies (Winding 
Up and Miscellaneous Provisions) Ordinance (Cap. 32), the Companies Ordinance (Cap. 622) and the Anti-Money 
Laundering and Counter-Terrorist Financing (Financial Institutions) Ordinance (Cap. 615).

## Page 6

iv
paper. The HKMA and the SFC have the right to charge a reasonable fee for processing 
any data access request. 
Retention
5. Personal data provided to the HKMA and the SFC in response to this consultation paper 
will be retained for such period as may be necessary for the proper discharge of their
functions. 
Enquiries
6. Any enquiries regarding the personal data provided in your submission on this 
consultation paper, requests for access to personal data or correction of personal data 
should be addressed in writing to –
HKMA 
Personal Data Privacy Officer 
Hong Kong Monetary Authority 
55/F Two International Finance Centre 
8 Finance Street 
Central, Hong Kong
SFC 
Data Privacy Officer 
Securities and Futures Commission 
54/F One Island East
18 Westlands Road
Hong Kong
7. A copy of the Privacy Policy Statement adopted by the HKMA and the SFC is available 
upon request.

## Page 7

1
Executive summary
1. To keep up with international developments and ensure our OTC derivatives
reporting regime stays relevant and appropriate as the markets evolve, we wish to 
consult the market on the following four proposals for the OTC derivatives reporting 
obligation (items (a) to (d)) and provide conclusions to our proposal on the masking 
relief (item (e)): 
(a) Mandating the use of UTI;
(b) Mandating the use of UPI;
(c) Mandating the reporting of CDE;
(d) Mandating the adoption of the ISO 20022 standard; and
(e) Maintaining the current list of designated jurisdictions for the masking relief.
Mandating the use of UTI
2. Based on the industry’s feedback received from the 2019 Consultation Paper, the 
HKMA and the SFC have been monitoring international developments on UTI and 
maintaining a close dialogue with the industry to refine the proposal on UTI 
implementation in Hong Kong. This paper sets out our conclusions and further 
consultation on UTI implementation. Considering the feedback on the 2019 
Consultation Paper and the latest international developments of UTI implementation, 
we propose to implement the mandatory use of UTI in Hong Kong on 29 September 
2025 (implementation date). To support reporting entities in transitioning to UTI, 
they may continue to report the existing trade identifiers of Unique Swap Identifier 
(USI) and Unique Trade ID (TID) as per the current reporting requirements, or report 
the UTI voluntarily, until the implementation date.
3. In the meantime, we conclude that the use of UTI will be mandated for the reporting 
of new trades (including their subsequent life-cycle events and valuation) that take 
place on or after the implementation date, and that we will fully adopt the UTI 
Technical Guidance in the approaches to as well as the format, structure and 
generation logic of UTI. The proposed steps to generate UTI are based on the 
waterfall of factors as set out in the UTI Technical Guidance (TG Waterfall) and 
paragraph 25 of this paper. In addition, we propose to accept the use of interim-UTI 
to the extent as set out in paragraphs 29-32 of this paper where a reporting entity 
does not receive a UTI from the UTI generating entity in sufficient time for reporting.
We also propose that live legacy transactions with remaining maturity of more than 
one year as at the implementation date will need to be re-reported in the Hong Kong 
Trade Repository (HKTR) in a new data format.
Mandating the use of UPI
4. We propose that reporting entities should provide the UPI for the underlying 
derivatives of each submitted reportable transaction to the HKTR on a mandatory

## Page 8

2
basis from 29 September 2025. We also propose to fully adopt the UPI Technical 
Guidance and the ISO 4914 standard for the structure and format of UPI. 
Mandating the reporting of CDE 
5. The HKMA and the SFC propose to adopt the CDE Technical Guidance as far as 
practicable. Our approach to implementing it is to adopt a scope that serves our 
regulatory purposes while maximising the data elements common to other 
jurisdictions and minimising the data elements unique to Hong Kong. Where certain 
data fields are not covered by the CDE Technical Guidance but are also required to 
be reported in other jurisdictions, we intend to align the definitions with those used by 
other jurisdictions as closely as practicable to facilitate global data aggregation and 
reporting. Our proposed data elements are set out in Appendix B. We propose that 
they replace the current set of data fields upon the implementation of CDE in Hong 
Kong from 29 September 2025.
Mandating the adoption of ISO 20022 Standard
6. The HKMA and the SFC recognise the need and benefits of a single global standard 
for OTC derivatives reporting, and have been collaborating with international peer 
regulators on the harmonisation of reporting requirements in relation to UTI, UPI and 
CDE. Adopting the ISO 20022 XML message standard will be a critical step for the 
harmonisation work. The HKMA and the SFC propose to adopt the ISO 20022 XML 
message format (i) for OTC derivatives reporting to the HKTR and (ii) at the same 
time when we implement the UTI, UPI and CDE in a “big bang” approach on the 
implementation date.
Conclusions on revising the list of designated jurisdictions for the masking 
relief 
7. Under Rules 26(1) of the Securities and Futures (OTC Derivative Transactions –
Reporting and Record Keeping Obligations) Rules (Reporting Rules), the masking 
relief enables reporting entities to mask the counterparty information when they 
report a transaction to the HKTR if they encounter reporting barriers in a jurisdiction 
that is designated by the SFC (Designated List). In 2019, we consulted the industry 
on revising the Designated List in view of the publication of the Follow-up Report on 
Trade Reporting Legal Barriers issued by the Financial Stability Board (FSB). As
there is still uncertainty on whether reporting barriers remain for certain jurisdictions, 
especially non-FSB jurisdictions, this paper sets out our conclusion that no change 
will be made to the current Designated List for the masking relief. This will not cause 
any detrimental effect on our effort to minimise masked trades as our masking relief 
was cast in a way which prevents abuse when actual legal or regulatory reporting 
barriers no longer exist.
Timeline for submitting comments
8. Our proposals to enhance the existing reporting regime are largely in line with those 
requirements imposed in other major jurisdictions. Therefore, we believe market 
participants will have anticipated the substance of our proposals.

## Page 9

3
9. In view of the above, we propose to allow eight weeks for the submission of 
comments on the proposals. Comments should be submitted to the HKMA or the 
SFC in writing no later than 17 May 2024.

## Page 10

4
Conclusions and further consultation on mandating the use of UTI
10. To improve the transparency of OTC derivatives markets, the existing reporting 
requirements set out in the Supplementary Reporting Instructions for OTC Derivative 
Transactions (SRI) published by the HKMA specify that, if available, the USI
reportable under the US mandatory reporting requirements and the TID reportable 
under the European Union (EU) mandatory reporting requirements must be reported 
as the identifying references for a transaction submitted to the HKTR. 
11. We proposed to adopt UTI as an international standard in the 2019 Consultation 
Paper. We further proposed an implementation timeline of April 2020 for transactions 
that have neither a USI nor TID, and an interim measure to continue to accept USI 
and TID as trade identifiers until six months after both the US and the EU have 
adopted an international standard for UTI. At that time, we proposed to adopt a full 
implementation of UTI in Hong Kong. The proposals aimed to address the issue that 
transactions that did not involve the EU and US counterparties so far did not have a 
unique trade identifier.
12. Subsequent to our 2019 consultation on mandating the use of UTI for reporting 
obligation, the US Commodity Futures Trading Commission (CFTC) and the 
European Securities and Markets Authority (ESMA) proposed adopting the UTI in 
December 2022 and April 2024 respectively. As many OTC derivatives transactions 
are cross-border in nature, involving reporting requirements in multiple jurisdictions, 
the HKMA and the SFC have been working closely with the Monetary Authority of 
Singapore, Australian Securities & Investments Commission and the Japan Financial 
Services Agency on a coordinated implementation plan for UTI in the Asia-Pacific 
(APAC) region to ensure a smooth UTI adoption in Hong Kong.
Proposed implementation timeline and interim measure
13. We received many useful feedback and opinions on the proposed implementation 
timeline and interim measure in the 2019 Consultation Paper. Market participants 
strongly supported aligning Hong Kong’s reporting requirements with international 
standards. Interim usage of USI and TID was also well supported so that market 
participants could continue to observe the UTI implementation proposals in the US 
and the EU. Upon our subsequent engagements with the industry, market 
participants also expressed concerns on implementing UTI before the ISO 20022 
standard is finalised, and they wished to focus their resources on the US and the EU 
implementation first, and then implement UTI in the APAC region. 
14. Given that the US and the EU did not have clear implementation timelines for UTI 
adoption at that time and that market participants did not wish that the APAC 
jurisdictions front-run the US and the EU on UTI implementation, we have been 
monitoring international developments and maintaining a close dialogue with the 
industry to refine the proposal for UTI implementation in Hong Kong. 
15. Now with the CFTC and ESMA UTI implementation timelines announced in 
December 2022 and April 2024, we propose that reporting entities should provide the

## Page 11

5
UTI for each submitted reportable transaction to the HKTR on a mandatory basis 
from 29 September 2025. The proposed implementation timeline has taken into 
account that major jurisdictions will implement UTI this year 4 , and that an 
international industry association has requested a staggered implementation of at 
least six months for Hong Kong after Australia and Singapore’s joint implementation. 
16. In addition, the implementation of UTI, together with UPI, CDE and the ISO 20022 
standard, will constitute a major revamp of the OTC derivatives reporting
requirements in Hong Kong. This will involve an extensive system change for both 
the HKTR and market participants. The proposed timeline should provide sufficient 
time for relevant parties to allocate adequate resources for the necessary system 
change. In the meantime, the HKMA and the SFC will continue to utilise the OTC 
derivatives data currently submitted to the HKTR for regulatory purposes until the
implementation date. 
Question 1
The HKMA and the SFC are seeking views on the proposal to mandate the use of 
UTI in submitting transactions to the HKTR from 29 September 2025. If you foresee 
any operational difficulties in meeting the implementation timeline, please provide 
specific details.
17. Considering our currently proposed timeline, an interim measure or grace period to 
allow for the interim use of USI and TID upon the UTI implementation in Hong Kong 
is no longer needed5
. On the other hand, to support reporting entities in transitioning 
to the UTI, they may continue to report the existing trade identifiers of USI and TID as 
per the current reporting requirements, or report UTI voluntarily6
, from now until the
implementation date.
Proposed requirements for reporting UTI
18. Because of the cross-border nature of OTC derivatives transactions, pursuant to 
other jurisdictions’ reporting requirements, reporting entities may generate and 
submit UTI to the HKTR even before their mandatory use is implemented in Hong 
Kong. Reporting entities may do so as voluntary reporting. Starting from 29 
September 2025, each transaction submitted to the HKTR must be identified by a 
single UTI based on the international standard. 
19. In the 2019 Consultation Paper, we proposed that reporting entities can use the UTI 
generated in accordance with relevant overseas requirements, which are also 
4
 In 2024, Japan will implement UTI on 1 April, the EU on 29 April, the UK on 30 September, and both Australia 
and Singapore on 21 October. 5 By the time of Hong Kong’s implementation, major jurisdictions should have already implemented the 
mandatory use of UTI, and therefore USI and TID will no longer be in use, except in legacy trades. 6 The HKTR has revised its reporting templates from 19 December 2022 to include, among others, the “Global 
UTI” data field to cater to market participants’ needs to include the UTI information in a transaction to be 
submitted to the HKTR during the transition towards UTI mandatory reporting.

## Page 12

6
consistent with the structure and format set out in the UTI Technical Guidance, to 
meet the proposed Hong Kong UTI requirements. We have received no objection to 
this proposal. UTI may be generated in Hong Kong, pursuant to Hong Kong’s
reporting requirements, or elsewhere, pursuant to the reporting requirements of other 
jurisdictions. In both scenarios, UTI based on the international standard will be 
equally accepted in Hong Kong.
20. To reduce the compliance burden for reporting entities, we proposed in the 2019 
Consultation Paper to mandate the use of UTI only for the reporting of new trades 
(including their subsequent life-cycle events and valuation) that take place on or after 
the mandatory use of UTI is implemented on 29 September 2025. Thus, reporting 
entities are not required to use a UTI when reporting life-cycle events and valuation 
for trades that were submitted prior to the implementation date (or legacy 
transactions), even if the events take place on or after that date7
. The exception is 
when the life-cycle event requires a new UTI to be used as set out in the UTI 
Technical Guidance. We have received no objection to this proposal and will proceed 
to require UTI only for reporting new trades (including their subsequent life-cycle 
events and valuation).
21. To support the mandatory use of UTI, we proposed in the 2019 Consultation Paper to 
adopt two data fields for the reporting of the UTI and Prior UTI, namely the “Global 
UTI” and “Prior global UTI”. The data field “Global UTI” is for reporting the value of a 
UTI in a structure and format consistent with the UTI Technical Guidance, while the 
data field “Prior global UTI” is for reporting the UTI of a prior related transaction under
a central clearing scenario. We received no objection to this proposal. The two data 
fields have been developed and included in the HKTR reporting templates for 
voluntary reporting since December 2022.
22. As mentioned in the 2019 Consultation Paper, to prepare for the implementation of 
the mandatory use of UTI, relevant requirements in the SRI and, where appropriate, 
the Frequently Asked Questions, technical specifications for reporting and the 
gazetted data fields for mandatory reporting will be updated after the consultation 
conclusions on the use of UPI, CDE and the ISO 20022 standard and further 
consultation conclusions on UTI are published.
Proposed responsibility for generating UTI
23. To avoid the risk of multiple UTIs being generated for the same reportable OTC 
derivatives transaction, only one entity should be responsible for generating the UTI. 
In this regard, the UTI Technical Guidance sets out the TG Waterfall for authorities to 
consider in allocating the responsibility for UTI generation while acknowledging that 
not all factors would be relevant for all jurisdictions. 
24. In the 2019 Consultation Paper, we proposed introducing some flexibility to the TG 
Waterfall in that counterparties may bilaterally agree on whom would generate the 
UTI; and if a bilateral agreement could not be reached, the TG Waterfall be followed. 
7 In some cases, re-reporting of a legacy trade may be needed even though a UTI is not required. For details, 
please refer to the CDE proposals in this paper.

## Page 13

7
Although there is general support for the adoption of the TG Waterfall, there were
mixed views on whether the flexibility of a bilateral agreement should be put in place
before the TG Waterfall. Some respondents considered this would create 
unnecessary uncertainty, complexity and potential fragmentation in the UTI 
generation logic, and would pose operational difficulties for reporting entities with a 
large counterparty base. In contrast, another respondent agreed that the bilateral 
agreement mechanism would allow for flexible approaches at financial institutions’ 
discretion. 
25. We have considered the industry’s feedback and had subsequent discussions with 
market participants. Taking into account the latest UTI developments (eg, a bilateral 
agreement before the TG Waterfall is not implemented by other major jurisdictions),
we now do not propose to provide the flexibility for bilateral agreements. We would 
like to further consult the market and propose that reporting entities shall adopt the 
steps (a)–(e) below to determine the entity responsible for generating the UTI. These
steps are based on the TG Waterfall and are largely equivalent to those adopted by 
other major jurisdictions, eg, the final EU REFIT rules published by ESMA. We 
recognise a harmonised UTI generation logic is crucial to ensure seamless pairing 
and sharing of UTI and reduce complexity for reporting entities with multiple reporting 
obligations. The proposed steps are:
(a) for cleared OTC derivatives transactions other than OTC derivatives
transactions between two central counterparties (CCPs), the UTI shall be 
generated at the point of clearing by the CCP for clearing members. A 
different UTI shall be generated by a clearing member for its counterparty for 
a trade in which the CCP is not a counterparty;
(b) for OTC derivatives transactions which are centrally executed but not 
centrally cleared, the UTI shall be generated by the venue of execution for its 
member;
(c) for OTC derivatives transactions other than those referred to in points (a) and 
(b), where either counterparty is subject to the reporting requirements in a
jurisdiction outside Hong Kong8
, the UTI shall be generated pursuant to the 
rules of the jurisdiction of the counterparty that must first comply with those 
reporting requirements.
Where the counterparty subject to reporting must first comply with Hong 
Kong’s reporting requirements, the following entities shall be responsible for 
generating the UTI: 
(i) for OTC derivatives transactions that were centrally confirmed by 
electronic means, the trade confirmation platform at the point of 
confirmation;
8 In determining whether a counterparty is subject to the reporting requirements in a jurisdiction outside Hong 
Kong in the UTI generation logic, the nexus element of a “conducted in Hong Kong” transaction as set out in 
Rule 4 of the Reporting Rules should be disregarded, ie, only the counterparty’s reporting requirements should 
be considered.

## Page 14

8
(ii) for all other OTC derivatives transactions, the counterparties shall 
agree on the entity responsible for generating the UTI. Where the 
counterparties fail to agree, the counterparty whose LEI9 is first based 
on sorting the identifiers of the counterparties with the characters of 
the identifier reversed shall be responsible for the generation10.
Where the applicable laws of the relevant jurisdiction outside Hong Kong 
provide for the same reporting deadline as the one applicable to the 
counterparty subject to Hong Kong’s reporting requirements, the 
counterparties shall agree on the entity responsible for generating the UTI.
Where the counterparties fail to agree, and the OTC derivatives transaction 
was centrally confirmed by electronic means, the UTI shall be generated by 
the trade confirmation platform at the point of confirmation.
If the UTI cannot be generated by the trade confirmation platform at the point 
of confirmation, and the details of the OTC derivatives transaction have to be 
reported to a single trade repository, that trade repository shall be responsible 
for generating the UTI.
If the UTI cannot be generated by the trade repository to which the details of 
the OTC derivatives transaction have been reported, the counterparty whose 
LEI 11 is first based on sorting the identifiers of the counterparties with the 
characters reversed shall be responsible for UTI generation;
(d) for OTC derivatives transactions other than those referred to in points (a), (b) 
and (c), that were centrally confirmed by electronic means, the UTI shall be 
generated by the trade confirmation platform at the point of confirmation;
(e) for all OTC derivatives transactions other than those referred to in points (a) 
to (d), the following shall apply:
(i) where reporting counterparties 12 conclude an OTC derivatives
transaction with non-reporting counterparties, the reporting 
counterparties shall generate the UTI;
(ii) for all OTC derivatives transactions other than those referred to in 
point (i), the counterparties shall agree on the entity responsible for 
generating the UTI. Where the counterparties fail to agree, the 
counterparty whose LEI13 is first based on sorting the identifiers of the 
9 If Trade Party 2 does not have an LEI, Trade Party 1 should generate the UTI. 10 To avoid any prefix of an LEI determining which entity to generate the UTI, a direct comparison of the 
characters of the counterparties’ LEI is not adopted. Instead, a more random way of comparison by comparing 
the reverse order of such characters is adopted. 11 If Trade Party 2 does not have an LEI, Trade Party 1 should generate the UTI. 12 In determining whether a counterparty is a reporting counterparty in the UTI generation logic, the nexus 
element of a “conducted in Hong Kong” transaction as set out in Rule 4 of the Reporting Rules should be 
disregarded, ie, only the counterparty’s reporting obligation should be considered. 13 If Trade Party 2 does not have an LEI, Trade Party 1 should generate the UTI.

## Page 15

9
counterparties with the characters of the identifier reversed shall be 
responsible for UTI generation.
Question 2
Do you have any comments or concerns about the proposed steps for
counterparties to determine the entity responsible for UTI generation? If you 
foresee any operational difficulties in implementing the proposals, please provide 
specific details.
Proposed approaches to UTI
26. In the 2019 Consultation Paper, we proposed to fully adopt the characteristics and 
approaches to UTI as set out in the UTI Technical Guidance, including situations 
where the same UTI should be kept or a different UTI should be generated. We 
received support from market participants on aligning our approaches to UTI with that 
in the UTI Technical Guidance. We will therefore adopt the approaches to UTI as 
proposed.
Proposed structure and format of UTI
27. In the 2019 Consultation Paper, we proposed to fully adopt the structure and format 
of UTI as set out in the UTI Technical Guidance, including how UTI should be 
constructed and the maximum number of characters forming UTI. We received 
support from market participants on aligning the structure and format of UTI with 
those in the UTI Technical Guidance. We will therefore adopt the structure and format 
of UTI as proposed. 
28. In August 2020, the ISO published the data standard for UTI, and the structure and 
format of UTI are specified in ISO 2389714. We have accommodated the ISO 23897 
standard for the UTI format in implementing UTI.
Responsibility to provide or obtain UTI in a timely manner
29. The UTI Technical Guidance sets out that UTI must be generated, shared and 
paired 15 (to the extent necessary) with other entities in time for all applicable 
reporting obligations. The HKMA and the SFC generally expect UTI to be generated 
in a timely manner for all relevant entities to comply with their reporting deadlines, 
pursuant to the reporting requirements of Hong Kong or other jurisdictions. To 
facilitate the timely identification of the entity generating the UTI, we encourage the 
entity responsible for generating the UTI (which may or may not be a reporting entity) 
14 ISO 23897:2020 Financial services — Unique transaction identifier (UTI) 
(https://www.iso.org/standard/77308.html). 15 The shared and paired UTI would help facilitate the linking and matching arrangements in the upcoming UTI 
implementation.

## Page 16

10
to inform its counterparties or clients whether it will generate a UTI or delegate 
another party to generate a UTI. 
30. Where a reporting entity is responsible for generating the UTI, it should make 
reasonable efforts to provide the UTI in a timely manner to any entity who requests 
for the UTI to comply with relevant reporting requirements. 
31. If a reporting entity is not the entity responsible for generating the UTI, it should make 
reasonable efforts to obtain the UTI in a timely manner, whether from the UTI
generating entity or a counterparty to the OTC derivatives transaction, in order to 
comply with the reporting requirements. We expect reporting entities to establish 
internal policies and arrangements to obtain UTI in a timely manner.
32. In the event that the reporting entity does not receive a UTI from the UTI generating 
entity in sufficient time for reporting, we propose that the reporting entity should 
generate its own UTI16 (in a format based on the UTI Technical Guidance) as an 
interim-UTI for reporting purposes and continue to make reasonable efforts to obtain 
the UTI from the UTI generating entity. Where the reporting entity subsequently 
obtains the UTI, it should report the UTI no later than two business days after 
obtaining the UTI. 
Question 3
Do you have any comments or concerns about the proposals to require reporting 
entities to:
(a) make reasonable efforts to provide or obtain a UTI in a timely manner;
(b) report an interim-UTI where it is unable to obtain the UTI despite having made 
reasonable efforts; and
(c) subsequently report the UTI within two business days after obtaining the UTI? 
If you foresee any operational difficulties in implementing the proposals or have 
other comments, please provide specific details.
16 If it is not technically feasible for a reporting entity to generate the UTI, it may report an internally generated 
code as an interim-UTI.

## Page 17

11
Consultation on mandating the use of UPI
33. The UPI is one of the international harmonised standards for reporting financial 
transaction data, for which the CPMI-IOSCO has developed the UPI Technical 
Guidance. The UPI aims to denote a specific OTC derivatives product reported to a 
trade repository to facilitate global data aggregation in the OTC derivatives market. 
34. The UPI is a 12-character reference code to uniquely identify an OTC derivatives
product reported to trade repositories. Each UPI code is mapped to a set of reference 
data elements with specific values that together describe the product. The 
combination of the UPI code, UPI reference data and the process of a UPI service 
provider assigning a UPI code to a particular set of reference data represents the UPI 
System. 
35. UPI service provider(s) provide for the timely issuance of UPI codes and maintain the
associated reference data in the UPI Reference Data Library, which is accessible to 
authorities and market participants. Authorities and market participants may locate 
the UPI code in the reference data library with the UPI reference data elements and 
values that pertain to a particular product for reporting to trade repositories.
36. Examples of reference data stored in the UPI Reference Data Library include each 
OTC derivatives product’s asset class, currency pair, delivery type, instrument type, 
option style, option type, underlying asset type and underlier ID.
37. In May 2019, the FSB designated the Derivatives Service Bureau (DSB) 17 as the 
service provider for the UPI System18. As the sole issuer of UPI codes, the DSB is 
also the operator of the UPI Reference Data Library. In the fourth quarter of 2023, the 
DSB launched the UPI Service for OTC derivatives products to facilitate the reporting 
and aggregation of data on OTC derivatives transactions globally.
Proposed structure and format of UPI
38. The key characteristics of the UPI as set out in the UPI Technical Guidance satisfy
the various principles that are necessary for a unique identifier that identifies an OTC 
derivatives product, including its uniqueness, consistency, clarity, jurisdiction 
neutrality, ease of assignment / retrieval / query and adaptability. To harmonise with 
the international standard, we propose to fully adopt the UPI Technical Guidance for 
the structure and format of UPI. 
17 DSB is a subsidiary of the Association of National Numbering Agencies, which is a global numbering agency 
for OTC derivatives serving the needs of market participants through the allocation of globally recognised and 
adopted ISO standards, such as International Securities Identification Number (ISIN), the Classification of 
Financial Instruments (CFI) and Financial Instrument Short Name (FISN), for identifying, classifying and 
describing financial instruments. 18 FSB designated DSB as the Unique Product Identifier (UPI) Service Provider: 
(https://www.fsb.org/2019/05/fsb-designates-dsb-as-unique-product-identifier-upi-service-provider/).

## Page 18

12
39. In November 2021, the ISO published the data standard for UPI, and the structure 
and format of UPI are specified in ISO 491419. We also propose to fully adopt the 
ISO 4914 standard for the UPI format in the HKTR reporting templates.
Proposed approaches to the implementation of UPI
40. We propose that reporting entities should provide the UPI for the derivatives of each 
submitted reportable transaction to the HKTR on a mandatory basis from 29 
September 2025. However, as the UPI service is a new set-up, we will keep in view 
the developments of the UPI System and align our practice with other regulators’ by 
maintaining certain product-related data fields in the reporting requirements. We will 
consider removing those product-related data fields at a later stage if the information 
is also available in the UPI system.
Question 4
The HKMA and the SFC are seeking views on the proposed approaches to the 
UPIs:
(a) the proposal to fully adopt the UPI Technical Guidance and the ISO 4914 
standard for the structure and format of UPI to be implemented in Hong Kong;
and
(b) the proposal to mandate the use of the UPI for the underlying derivatives of 
each submitted reportable transaction to the HKTR from 29 September 2025. 
If you foresee any operational difficulties in meeting the implementation timeline or 
have other comments, please provide specific details.
19 ISO 4914:2021 Financial services — Unique product identifier (UPI) (https://www.iso.org/standard/80506.html).

## Page 19

13
Consultation on mandating the reporting of CDE
41. The CDE is a set of derivatives transaction data elements (other than UTI and UPI) 
and formats and, where relevant, allowable values. It is intended to be the universe 
of data elements for regulators to draw from to form their individual data sets. For 
each data element, the CDE Technical Guidance sets out a definition, an existing 
industry standard (if applicable), a format and the allowable values. Standardisation 
allows market participants to gain a better understanding of data requirements, and 
the adoption of CDE promotes transparency in OTC derivatives transactions and 
facilitates data aggregation across data sets.
42. Adopting data elements from the CDE Technical Guidance for reporting will be 
beneficial to regulators and reporting entities in:
(a) expanding the data set for important data elements not under the current 
reporting requirements;
(b) transforming data elements which are unique to Hong Kong’s existing 
reporting requirements into the internationally-aligned standard;
(c) simplifying the process for entities that report under Hong Kong’s
requirements as well as other jurisdictions’ as the content in the transaction 
reports may not be significantly different across jurisdictions; and
(d) standardising the definitions of data elements, formats and allowable values 
to reduce ambiguity and complexity for reporting entities as well as improve 
the conformance and consistency in data values reported.
Proposed approaches to CDE
43. The HKMA and the SFC propose to adopt the CDE Technical Guidance as far as 
practicable. Our approach to implementing this technical guidance is to adopt a 
scope that serves our regulatory purposes while maximising the data elements that 
are common to other jurisdictions and minimising the data elements that are unique 
to Hong Kong.
44. The HKMA and the SFC propose to revamp the existing data fields to align with the 
definitions of and reporting requirements for data elements specified in the CDE 
Technical Guidance as closely as possible. Where there are data fields not covered 
by the CDE Technical Guidance but are also required to be reported in other 
jurisdictions, we intend to align the definitions with those used by other jurisdictions 
as closely as practicable to facilitate global data aggregation and reporting. 
45. The data elements we propose for Hong Kong’s reporting requirements are set out in 
Appendix B. They will replace the current set of data fields upon the implementation 
of CDE in Hong Kong. Appendix B contains data elements which are:
(a) sourced from the CDE Technical Guidance;

## Page 20

14
(b) sourced from other jurisdictions’ requirements; and
(c) administrative data fields which facilitate the HKTR’s operation and are 
currently required for reporting.
46. For each CDE, the CDE Technical Guidance sets out a definition, existing industry 
standard (if applicable), format and the allowable values for the data element. For 
data elements sourced from other jurisdictions that are not CDEs, those sources also 
set out the definitions, formats and allowable values. For the data elements that are 
existing administrative data fields, we propose using the definitions, formats and 
allowable values under existing reporting requirements. 
47. The proposed major changes to the existing data elements include:
(a) Adoption of data elements related to collateral and margins specified in the 
CDE Technical Guidance;
(b) Adoption of data elements related to lifecycle events specified by the CDE
Technical Guidance;
(c) Substitution of asset class- or product-specific data elements with more 
generic, cross-asset class elements along with the implementation of UPI; 
and
(d) Removal of a number of Party Type- and Party Name-related sub-fields to 
align with the CDE Technical Guidance and requirements proposed in other 
jurisdictions20.
Question 5
The HKMA and the SFC are seeking comments on the proposed data elements
and their definitions, formats and allowable values as set out in Appendix B. If there 
are data elements that you consider should be excluded or modified, or that you 
foresee any operational difficulties in implementing the proposal, please provide 
specific details and elaborate on the rationale. 
Question 6
Do you consider there are other data elements that the HKMA and the SFC should 
include in Appendix B? If so, please suggest the data elements together with the 
purposes, definitions, formats and allowable values of the suggested data 
elements.
20 LEI is proposed as the entity identifier to identify all entities involved in OTC derivatives transactions in the
CDE Technical Guidance.

## Page 21

15
Data elements related to the direction of the transaction (corresponding to data fields 
no.9 to 11 of Appendix B)
48. The CDE Technical Guidance has identified two ways to report information related to 
the direction (ie, buyer, seller, payer or receiver) of the trade: (1) to report the 
direction of the trade from the reporting entity’s perspective21, or (2) to report the 
identifier of the counterparty for each direction. The HKMA and the SFC propose to 
adopt the former by reporting the direction of the trade from the reporting entity’s 
perspective, which is the common approach adopted by ESMA and some APAC 
jurisdictions22.
Data elements related to collateral & margin (corresponding to data fields no.37 to 55, 
156 to 158 and no. 192 of Appendix B)
49. In addition to the proposed data element “Collateral portfolio code” (data field no. 38
of Appendix B), which is specified in the CDE Technical Guidance, we propose to 
adopt two additional collateral portfolio codes “Initial margin collateral portfolio code” 
and “Variation margin collateral portfolio code” (data fields no. 156 and 158 of 
Appendix B), which are required by the CFTC and also proposed by some APAC 
jurisdictions 23 . We learnt from the industry’s consultation feedback from other 
jurisdictions that each OTC derivatives transaction may be treated differently for the 
purposes of margining in accordance with a collateral agreement between the 
parties, and also the separation of initial margin and variation margin would make 
reporting easier as the amounts may be recorded separately in the reporting entities’ 
systems. As such, we intend to mandate the “Initial margin collateral portfolio code” 
and “Variation margin collateral portfolio code”, if applicable, for the identification of 
collateral portfolios. The HKMA and the SFC will update relevant requirements in the 
SRI to give further guidance on how to report collateral when there is no collateral 
portfolio or only a single collateral portfolio.
Data elements related to lifecycle events (corresponding to data fields no.136 to 139
of Appendix B)
50. The set of data elements related to lifecycle events includes “Action Type”, “Event 
type”, “Event timestamp” and “Event identifier”, and are included in the Revised CDE 
Technical Guidance – version 3 released by the Regulatory Oversight Committee in 
September 2023. It provides a harmonised approach for reporting entities to report 
lifecycle events and allows regulators to track the history of material lifecycle events 
and amendments made to reported transactions for better transparency in the OTC 
derivatives market. While the reporting methodologies related to lifecycle events exist 
in various forms across different jurisdictions at present, a lack of uniformity limits the 
value for aggregation of data. 
51. The HKMA and the SFC propose to adopt the CDE data elements related to the 
lifecycle events as set out in the Revised CDE Technical Guidance – version 3 for 
Hong Kong’s reporting requirements. These data elements enhance a better 
21 In the case of a reporting entity acting as an agent in relation to the OTC derivatives transaction, this refers to 
the perspective of the counterparty to the transaction that the reporting entity is acting for. 22 Australia, Japan and Singapore also adopt the first approach. 23 Australia and Japan also require two collateral portfolio codes.

## Page 22

16
understanding of the lifecycle of an OTC derivatives transaction, including what 
action is applied (Action type), what event is causing such action (Event type) and 
when a given lifecycle event takes place (Event timestamp). In the case of many-to￾many relations, such as a compression or credit event, an Event identifier allows
regulators to link multiple OTC derivatives transactions pertaining to the same event, 
when they cannot be linked by other transaction identifiers, such as the “Prior UTI”. 
Data elements related to barrier strike values and secondary transaction identifier
(corresponding to data fields no.201 to 203 of Appendix B)
52. We are aware that proposals are being made by some authorities to the CDIDE for 
including in the ISO message standard 3 additional data fields, namely “Lower or 
only barrier”, “Upper barrier” and “Secondary transaction identifier”. The purposes are
to facilitate the reporting of strike values for barrier options and accommodate market 
participants’ request to have a data field for the internal client code. We understand 
that the CDIDE process related to these three additional data fields will be completed
soon, we consider that these data fields suit our regulatory needs and propose to 
adopt them in the format to be set out in the ISO message standard. 
Question 7
The HKMA and the SFC are seeking comments on the proposals regarding the 
above data elements for Hong Kong’s reporting requirements. If you foresee any 
operational difficulties in implementing the proposal or have other comments, 
please provide specific details.
Proposed implementation timeline
53. Regulators across jurisdictions are making changes to their OTC derivatives
reporting regimes to implement the UTI, UPI and CDE technical guidances. It could 
be resource-intensive for reporting entities with global operations to simultaneously 
implement changes to their systems and processes across different jurisdictions. To 
allow reporting entities sufficient time to prepare for implementation, and to maintain 
a simple “big bang” approach to roll out UTI, UPI and CDE in one go, the HKMA and 
the SFC intend to implement the reporting requirements as set out in Appendix B on 
29 September 2025. 
54. Having considered the implementation dates in major jurisdictions such as the US, 
EU, UK, Japan, Australia and Singapore, and having considered the time needed for 
system upgrades, the proposed implementation date for Hong Kong will mitigate 
conflicts with the preparation and implementation of similar data harmonisation 
exercises put forward by these jurisdictions. This gives market participants more than 
18 months from the issuance of this paper (and we expect more than 12 months from 
the issuance of the conclusions to this paper) to prepare for implementation in Hong 
Kong.

## Page 23

17
Question 8
Do you foresee any difficulties in implementing the list of proposed data elements 
specified in Appendix B for OTC derivatives trade reporting on the implementation 
date? If so, please specify the data field(s) and provide specific details and 
reasons. 
Proposed treatment of live legacy transactions and other transitional issues
55. For live legacy transactions, ie, transactions entered into prior to the implementation 
date of the proposed reporting requirements but have not yet matured, been 
terminated, quitted or withdrawn, the HKMA and the SFC propose to require the re￾reporting of live legacy transactions (other than UTIs and UPIs) and adopt the 
proposed reporting requirements (ie, in the new reporting format) only if the 
transaction has remaining maturity of more than one year as at the implementation 
date. We propose that reporting entities be provided six months from the 
implementation date to report those live legacy transactions as they may need time 
to gather the information required under the proposed reporting requirements. This 
approach strikes a balance between the regulators’ surveillance needs for the new 
data set in respect of long-dated transactions and market participants’ compliance 
burden in re-reporting legacy transactions. Our proposal is in line with that adopted 
by other major APAC jurisdictions. The HKMA and the SFC will update relevant 
requirements in the SRI to provide further guidance to the industry.
56. Once the live legacy transaction is re-reported (whether on the last day of the six￾month transition period or before that), any amendments to the transaction will need 
to be reported in the new reporting format within two business days. 
57. For live legacy transactions with maturity of more than one year from the 
implementation date (ie, live legacy transactions required to be re-reported), before 
the transaction is re-reported, where there is an update of content24 to any of the 
existing required data fields in the six-month transition period, reporting entities are 
required to continue to report such updates using the pre-implementation reporting 
templates (ie, the existing reporting templates for submitting trades to the HKTR
before the implementation of UTI, UPI and CDE) within two business days.
58. For live legacy transactions maturing within one year from the implementation date 
(ie, live legacy transactions not required to be re-reported), where there is an update 
of content to any of the existing required data fields after the implementation date, 
reporting entities are required to continue to report such updates in the pre￾implementation reporting templates until the transactions mature, are terminated, 
quitted or withdrawn.
24 Irrespective of whether such an update is a lifecycle event, error amendment or a backload of a transaction.

## Page 24

18
59. For completeness, “dead” legacy transactions (ie, transactions entered into prior to 
the implementation date but have matured, been terminated, quitted or withdrawn
before that date) are not required to be re-reported to the HKTR in the new reporting 
format. 
Question 9
Do you have any comments or concerns on the below?
(a) The proposed approach of requiring re-reporting of live legacy transactions with 
maturity of more than one year as at the implementation date, and providing a 
six-month transition period for these reportable legacy transactions to be re￾reported; and 
(b) Are there any particular data fields that a reporting entity may find challenging in 
re-reporting a legacy transaction? If so, please specify the data field(s) and 
provide specific details.

## Page 25

19
Consultation on adoption of the ISO 20022 Standard
60. ISO 20022 is an agreed framework and methodology used by the global financial 
industry to create consistent message standards across business processes. It can 
assist in standardising the reporting of OTC derivatives transactions internationally. 
For reporting entities with multi-jurisdictional reporting requirements and trade 
repositories and providers of reporting services operating in multiple jurisdictions, we 
see significant benefits in forming, transmitting and receiving OTC derivatives
transaction information based on a common form of message.
61. As set out in the CPMI-IOSCO Governance Arrangements for Critical OTC 
Derivatives Data Elements (Other Than UTI and UPI) published in October 2019, 
CDE data elements will be included in the ISO 20022 data dictionary and an ISO 
20022 XML message format has been developed for OTC derivatives reporting25. 
The standard was required by the US and EU authorities for OTC derivatives
reporting and was proposed to be adopted by some APAC authorities. 
62. The HKMA and the SFC have been collaborating with a number of international peer 
regulators and are seeking to harmonise, to the extent practicable, with other 
jurisdictions in relation to the UTI, UPI and CDE requirements for OTC derivatives
reporting. Adopting the ISO 20022 XML message standard would be another 
harmonising step.
63. The HKMA and the SFC recognise the need and benefits of a single global standard 
for OTC derivatives reporting in the long run and propose to adopt the ISO 20022 
XML message format (i) for OTC derivatives reporting to the HKTR and (ii) at the 
same time as we implement UTI, UPI and CDE in a “big bang” approach on 29
September 2025. The proposed implementation date will provide sufficient time for 
market participants to make necessary system changes to enable the adoption and 
usage of the ISO 20022 message standard26.
Question 10
The HKMA and the SFC are seeking comments on the adoption of the ISO 20022 
XML message standard for OTC derivatives reporting to the HKTR and on 
implementing ISO 20022 XML message standard at the same time when we 
implement the UTI, UPI and CDE. If you foresee any operational difficulties in 
implementing the proposals, please provide specific details.
25 Governance Arrangements for Critical OTC Derivatives Data Elements (Other Than UTI and UPI): 
https://www.bis.org/cpmi/publ/d186.pdf. 26 In order to accommodate the corresponding revamp, certain functions in respect of the HKTR system reports 
and user interface will be rolled out at a later date under the ISO implementation.

## Page 26

20
Conclusions on revising the list of designated jurisdictions for the 
masking relief
64. When the first phase of OTC derivatives reporting took effect in July 2015, we 
introduced a masking relief to deal with situations where a reporting entity is 
prevented from reporting certain information identifying the counterparty 
(Counterparty Information) to the HKMA via the HKTR due to a conflicting 
confidentiality obligation (or other requirements) under the laws of another jurisdiction. 
The current masking relief under Rule 26(1) of the Reporting Rules enables reporting 
entities to mask the Counterparty Information when they report a transaction to the 
HKMA via the HKTR if both of the following preconditions are fulfilled:
(a) The submission of Counterparty Information is prohibited under the laws of, or 
by an authority or regulatory organisation in, a jurisdiction; and
(b) This jurisdiction is designated by the SFC (on the Designated List).
65. The purpose of the masking relief is to give some degree of flexibility to reporting 
entities who face an actual legal or regulatory prohibition of reporting Counterparty 
Information. It was cast in a way that when a jurisdiction in the Designated List 
removes its prohibition (ie, the first precondition in paragraph 64(a) is no longer 
satisfied), the reporting entities can no longer rely on the masking relief in respect of 
that jurisdiction. The current Designated List was gazetted on 7 July 2015 and 
consists of 18 jurisdictions (Appendix C). 
66. Over the past few years, many regulators across the globe have worked towards 
removing legal prohibitions that may prevent the reporting of Counterparty 
Information to trade repositories. The FSB issued a report27 in 2018 to review the 
related progress and re-categorise a number of jurisdictions as having either 
reporting barriers which are curable by standing consent or no such barriers. In view 
of the FSB report and as a housekeeping exercise, we proposed in the 2019 
Consultation Paper to review the Designated List by removing some jurisdictions 
from the list. 
67. We received mixed feedback on this matter in the 2019 Consultation Paper. Out of 
the 15 responses to this consultation, two respondents expressly supported the 
proposal. However, one respondent asserted that one of the non-FSB jurisdictions 
that we proposed to remove from the Designated List had only removed reporting 
barriers in respect of reporting to trade repositories in a certain region, but reporting 
barrier still existed when reporting was made to trade repositories outside of that 
region, such as the HKTR.
68. An international industry association expressed concerns on behalf of its members 
about the lack of official and formal clarity from specific APAC jurisdictions on 
whether any legal or regulatory prohibition to reporting remains. 
27 See the FSB’s Trade reporting legal barriers: Follow-up of 2015 peer review recommendations issued in 
November 2018: https://www.fsb.org/wp-content/uploads/P191118-4.pdf.

## Page 27

21
69. We recognise that there is still uncertainty on whether reporting barriers remain for 
certain jurisdictions, especially non-FSB jurisdictions, which were not covered 
extensively in the FSB’s 2018 report. As stated before, our masking relief was cast in 
a way that would prevent abuse when actual legal or regulatory prohibition no longer 
exists, even when the relevant jurisdiction remains on the Designated List. In other 
words, maintaining the status quo in the Designated List would not cause any 
detrimental effect on our effort to minimise masked trades. In fact, the volume of 
trades submitted to the HKTR with masked Counterparty Information is currently 
insignificant.
70. In the meantime, we fully acknowledge the amount of work and resources market 
participants will need for the UTI, UPI, CDE and the ISO 20022 standard to be 
implemented globally in the upcoming harmonisation exercise. In view of all these 
factors, we will not make any changes to the Designated List at this time. 
71. That said, we wish to remind reporting entities that the Designated List is not 
intended to enable them to automatically mask Counterparty Information when 
transacting with counterparties from any of those jurisdictions. Rather, they should 
carry out reasonable due diligence to ensure that the first precondition for the
masking relief (ie, actual legal or regulatory prohibition) is still valid.

## Page 28

22
The way forward
72. The HKMA and the SFC continue to ensure that our OTC derivatives reporting 
regime remains relevant and up-to-date. The proposals in this paper have been 
developed in response to the global call for OTC derivatives data harmonisation and 
similar reform efforts in other major markets. We believe our proposals strike the right 
balance between the need for transparency in the OTC derivatives market and 
addressing market concerns. As always, we welcome market views on the proposals. 
Interested parties are invited to submit written comments on our proposals to either 
the HKMA or the SFC on or before 17 May 2024. Please refer to the Foreword for the 
methods of submission.

## Page 29

23
Appendix A – List of respondents
(In alphabetical order)
Respondent has no objection to publication of name and content of submission
1. CME Group
2. Depository Trust and Clearing Corporation 
3. Global Financial Markets Association 
4. Global Legal Entity Identifier Foundation
5. Hong Kong Bar Association 
6. IHS Markit (merged with S&P Global)
7. International Swaps and Derivatives Association 
8. Japanese Bankers Association 
9. Private Wealth Management Association
10. The DTC Association 
11. The Hong Kong Association of Banks
12. The Law Society of Hong Kong
Respondent requested submission to be published on a “no-name” basis
One submission
Respondent requested that both name and submission to be withheld from 
publication
Two submissions

## Page 30

24
Appendix B – List of proposed data elements for reporting

## Page 31

Row no. Data Element Name Definition of Data Element Format and allowable values IR FX EQ CD CM
1 Effective date Unadjusted date at which obligations under the OTC derivative transaction come into effect, as included in the 
confirmation, if applicable.
If the effective date is not specified as part of the terms of the contract, the counterparties shall report in this field the date 
of execution of the derivative.
ISO 8601
YYYY-MM-DD, based on UTC.
    
2 Expiration date Unadjusted date at which obligations under the OTC derivative transaction stop being effective, as included in the 
confirmation, if applicable. Early termination does not affect this data element.
ISO 8601
YYYY-MM-DD, based on UTC.
    
3 Early termination date Effective date of the early termination (expiry) of the reported transaction, if applicable.
This data element is applicable if the termination of the transaction occurs prior to its maturity due to an ex-interim decision 
of a counterparty (or counterparties). Examples of early terminations (expiry) are: negotiated early termination; early 
termination under an optional early termination provision (“mutual put”); novation; offsetting (netting) transaction; option 
exercise; compression; early termination clause specified in the original contract which is a callable swap (bought 
embedded option); mutual credit break.
ISO 8601
YYYY-MM-DD, based on UTC.
    
4 Reporting timestamp Date and time of the submission of the report as reported to the trade repository. ISO 8601
YYYY-MM-DDThh:mm:ssZ, based on UTC. 
    
5 Execution timestamp Date and time a transaction was originally executed, resulting in the generation of a new UTI. This data element remains 
unchanged throughout the life of the UTI.
ISO 8601
YYYY-MM-DDThh:mm:ssZ, based on UTC. 
    
6 Counterparty 1 Identifier of the counterparty to an OTC derivative transaction. ISO 17442 Legal Entity Identifier (LEI) 
Char(20)
LEI code that is included in the LEI data as published by the Global LEI Foundation (GLEIF, www.gleif.org/).
    
7 Counterparty 2 Identifier of the second counterparty to an OTC derivative transaction. ISO 17442 Legal Entity Identifier (LEI) 
Char(20) for an LEI code
Varchar(72) natural persons who are acting as private individuals (not eligible for an LEI per the ROC Statement - Individuals Acting in a Business Capacity).
LEI code that is included in the LEI data as published by the Global LEI Foundation (GLEIF, www.gleif.org/).
For natural persons who are acting as private individuals (not eligible for an LEI per the ROC Statement - Individuals Acting in a Business Capacity): LEI of the reporting counterparty followed by a unique 
identifier assigned and maintained consistently by the reporting counterparty for that natural person(s) for regulatory reporting purpose.
    
8 Counterparty 2 identifier type indicator Indicator of whether LEI was used to identify the Counterparty 2. Boolean:
true, for Legal entities
false, for natural persons who are acting as private individuals (not eligible for an LEI per the ROC Statement - Individuals Acting in a Business Capacity)
    
9 Direction 1 Indicator of whether the counterparty 1 is the buyer or the seller as determined at the time of the transaction, if applicable. Char(4)
Allowable values:
BYER = buyer
SLLR = seller
    
10 Direction 2 - Leg 1 Indicator of whether the counterparty 1 is the payer or the receiver of leg 1 as determined at the time of the conclusion of 
the derivative, if applicable.
Char(4)
Allowable values:
MAKE = payer
TAKE = receiver
    
11 Direction 2 - Leg 2 Indicator of whether the counterparty 1 is the payer or the receiver of leg 2 as determined at the time of the conclusion of 
the derivative, if applicable.
Char(4)
Allowable values:
MAKE = payer
TAKE = receiver
    
12 Cleared Indicator of whether the transaction has been cleared, or is intended to be cleared, by a central counterparty. Char(1)
Allowable values:
Y= yes, centrally cleared, for beta and gamma transactions.
N= no, not centrally cleared.
I= intent to clear, for alpha transactions that are planned to be submitted to clearing.
    
13 Central counterparty Identifier of the central counterparty that cleared the transaction, if applicable.
This data element is not applicable if the value of the data element “Cleared” is “N” (“No, not centrally cleared”) or “I” 
(“Intent to clear”).
ISO 17442 Legal Entity Identifier (LEI) 
Char(20)
LEI code that is included in the LEI data as published by the Global LEI Foundation (GLEIF, www.gleif.org/).
    
14 Clearing member Identifier of the clearing member through which a derivative transaction was cleared at a central counterparty, if applicable.
This data element is applicable to cleared transactions under both the agency clearing model and the principal clearing 
model.
• In the case of the principal clearing model, the clearing member is identified as clearing member and also as a 
counterparty in both transactions resulting from clearing: (i) in the transaction between the central counterparty and the 
clearing member; and (ii) in the transaction between the clearing member and the counterparty to the original alpha 
transaction.
• In the case of the agency clearing model, the clearing member is identified as clearing member but not as the 
counterparty to transactions resulting from clearing. Under this model, the counterparties are the central counterparty and 
the client.
This data element is not applicable if the value of the data element “Cleared” is “N” (“No, not centrally cleared”) or “I” 
(“Intent to clear”).
ISO 17442 Legal Entity Identifier (LEI) 
Char(20)
LEI code that is included in the LEI data as published by the Global LEI Foundation (GLEIF, www.gleif.org/).
    
Appendix B to the Consultation Paper - List of Proposed Data Elements Data element applicable to asset class
24-1

## Page 32

Row no. Data Element Name Definition of Data Element Format and allowable values IR FX EQ CD CM
Appendix B to the Consultation Paper - List of Proposed Data Elements Data element applicable to asset class
15 Platform identifier Identifier of the trading facility (eg exchange, multilateral trading facility, swap execution facility) on which the transaction 
was executed, if applicable.
ISO 10383 Segment Market Identifier Code (MIC)
Char(4)
Allowable values:
ISO 10383 segment MIC code.
If no trading facility was involved in the transaction:
XOFF, for transactions in listed instruments
XXXX, for transactions in instruments that are not listed in any venue
BILT, if the reporting counterparty cannot determine whether the instrument is listed or not, as per jurisdictional requirements.
    
16 Confirmed For new reportable transactions (as defined by the CPMI-IOSCO Technical Guidance: Harmonisation of the Unique 
Transaction Identifier), whether the Legally binding terms of an OTC derivatives contract were documented and agreed 
upon (confirmed) or not (unconfirmed). If documented and agreed, whether such confirmation was done:
• via a shared confirmation facility or platform, or a private/bilateral electronic system (electronic);
• via a human-readable written document, such as fax, paper or manually processed e-mails (non- electronic).
ISO 20022: SecuritiesTradeStatus/TradeConfirmationStatus
Char(4) 
NCNF = unconfirmed
ECNF = electronic
YCNF = non-electronic
    
17 Final contractual settlement date Unadjusted date as per the contract, by which all transfer of cash or assets should take place and the counterparties 
should no longer have any outstanding obligations to each other under that contract, if applicable.
For products that may not have a final contractual settlement date (eg American options), this data element reflects the 
date by which the transfer of cash or asset would take place if termination were to occur on the expiration date.
ISO 8601
YYYY-MM-DD, based on UTC.
    
18 Settlement currency - Leg 1 Currency for the cash settlement of the transaction when applicable.
For multicurrency products that do not net, the settlement currency of the leg 1.
This data element is not applicable for physically settled products (eg physically settled swaptions).
ISO 4217
Char(3)
Allowable values:
Currencies included in ISO 4217
    
19 Settlement currency - Leg 2 Currency for the cash settlement of the transaction when applicable.
For multicurrency products that do not net, the settlement currency of the leg 2.
This data element is not applicable for physically settled products (eg physically settled swaptions).
ISO 4217
Char(3)
Allowable values:
Currencies included in ISO 4217
    
20 Settlement location Place of settlement of the transaction as stipulated in the contract, if applicable. This data element is only applicable for 
transactions that involve an offshore currency (i.e. a currency which is not included in the ISO 4217 currency list, for 
example CNH).
ISO 3166
Char(2)
ISO country code
    
21 Fixed rate day count convention - Leg 1 Where applicable: day count convention of leg 1 (often also referred to as day count fraction or day count basis or day 
count method) that determines how interest payments are calculated. It is used to compute the year fraction of the 
calculation period, and indicates the number of days in the calculation period divided by the number of days in the year.
ISO 20022: Interest Calculation/Day Count Basis
Char(4)
Allowable values:
A001 = IC30360ISDAor30360AmericanBasicRule 
A002 = IC30365
A003 = IC30Actual 
A004 = Actual360 
A005 = Actual365Fixed
A006 = ActualActualICMA
A007 = IC30E360orEuroBondBasismodel1 
A008 = ActualActualISDA
A009 = Actual365LorActuActubasisRule 
A010 = ActualActualAFB
A011 = IC30360ICMAor30360basicrule 
A012 = IC30E2360orEurobondbasismodel2 
A013 = IC30E3360orEurobondbasismodel3 
A014 = Actual365NL
A015 = ActualActualUltimo 
A016 = IC30EPlus360
A017 = Actual364 
A018 = Business252 
A019 = Actual360NL 
A020 = 1/1
NARR = Narrative
    
22 Floating rate day count convention - Leg 1 Where applicable: day count convention (often also referred to as day count fraction or day count basis or day count 
method) that determines how interest payments for the floating rate of leg 1 are calculated. It is used to compute the year 
fraction of the calculation period, and indicates the number of days in the calculation period divided by the number of days 
in the year.
ISO 20022: Interest Calculation/Day Count Basis
Char(4)
Allowable values:
A001 = IC30360ISDAor30360AmericanBasicRule 
A002 = IC30365
A003 = IC30Actual 
A004 = Actual360 
A005 = Actual365Fixed
A006 = ActualActualICMA
A007 = IC30E360orEuroBondBasismodel1 
A008 = ActualActualISDA
A009 = Actual365LorActuActubasisRule 
A010 = ActualActualAFB
A011 = IC30360ICMAor30360basicrule 
A012 = IC30E2360orEurobondbasismodel2 
A013 = IC30E3360orEurobondbasismodel3 
A014 = Actual365NL
A015 = ActualActualUltimo 
A016 = IC30EPlus360
A017 = Actual364 
A018 = Business252 
A019 = Actual360NL 
A020 = 1/1
NARR = Narrative
    
24-2

## Page 33

Row no. Data Element Name Definition of Data Element Format and allowable values IR FX EQ CD CM
Appendix B to the Consultation Paper - List of Proposed Data Elements Data element applicable to asset class
23 Fixed rate day count convention - Leg 2 Where applicable: day count convention of leg 2 (often also referred to as day count fraction or day count basis or day 
count method) that determines how interest payments are calculated. It is used to compute the year fraction of the 
calculation period, and indicates the number of days in the calculation
period divided by the number of days in the year.
ISO 20022: Interest Calculation/Day Count Basis
Char(4)
Allowable values:
A001 = IC30360ISDAor30360AmericanBasicRule 
A002 = IC30365
A003 = IC30Actual 
A004 = Actual360 
A005 = Actual365Fixed
A006 = ActualActualICMA
A007 = IC30E360orEuroBondBasismodel1 
A008 = ActualActualISDA
A009 = Actual365LorActuActubasisRule 
A010 = ActualActualAFB
A011 = IC30360ICMAor30360basicrule 
A012 = IC30E2360orEurobondbasismodel2 
A013 = IC30E3360orEurobondbasismodel3 
A014 = Actual365NL
A015 = ActualActualUltimo 
A016 = IC30EPlus360
A017 = Actual364 
A018 = Business252 
A019 = Actual360NL 
A020 = 1/1
NARR = Narrative
    
24 Floating rate day count convention - Leg 2 Where applicable: day count convention (often also referred to as day count fraction or day count basis or day count 
method) that determines how interest payments for the floating rate of leg 2 are calculated. It is used to compute the year 
fraction of the calculation period, and indicates the number of days in the calculation period divided by the number of days 
in the year.
ISO 20022: Interest Calculation/Day Count Basis
Char(4)
Allowable values:
A001 = IC30360ISDAor30360AmericanBasicRule 
A002 = IC30365
A003 = IC30Actual 
A004 = Actual360 
A005 = Actual365Fixed
A006 = ActualActualICMA
A007 = IC30E360orEuroBondBasismodel1 
A008 = ActualActualISDA
A009 = Actual365LorActuActubasisRule 
A010 = ActualActualAFB
A011 = IC30360ICMAor30360basicrule 
A012 = IC30E2360orEurobondbasismodel2 
A013 = IC30E3360orEurobondbasismodel3 
A014 = Actual365NL
A015 = ActualActualUltimo 
A016 = IC30EPlus360
A017 = Actual364 
A018 = Business252 
A019 = Actual360NL 
A020 = 1/1
NARR = Narrative
    
25 Fixed rate payment frequency period - Leg 1 Where applicable: time unit associated with the frequency of payments, eg day, week, month, year or term of the stream for 
the fixed rate of leg 1.
ISO 20022: InterestCalculation/PaymentFrequency
Char(4)
Allowable values:
DAIL = daily
WEEK = weekly
MNTH = monthly
YEAR = yearly
ADHO = ad hoc which applies when payments are irregular
EXPI = payment at term
    
26 Floating rate payment frequency period - Leg 1 Where applicable: time unit associated with the frequency of payments, eg day, week, month, year or term of the stream for 
the floating rate of leg 1.
ISO 20022: InterestCalculation/PaymentFrequency
Char(4)
Allowable values:
DAIL = daily
WEEK = weekly
MNTH = monthly
YEAR = yearly
ADHO = ad hoc which applies when payments are irregular
EXPI = payment at term
    
27 Fixed rate payment frequency period - Leg 1 Where applicable: time unit associated with the frequency of payments, eg day, week, month, year or term of the stream for 
the fixed rate of leg 2.
ISO 20022: InterestCalculation/PaymentFrequency
Char(4)
Allowable values:
DAIL = daily
WEEK = weekly
MNTH = monthly
YEAR = yearly
ADHO = ad hoc which applies when payments are irregular
EXPI = payment at term
    
28 Floating rate payment frequency period - Leg 2 Where applicable: time unit associated with the frequency of payments, eg day, week, month, year or term of the stream for 
the floating rate of leg 2.
ISO 20022: InterestCalculation/PaymentFrequency
Char(4)
Allowable values:
DAIL = daily
WEEK = weekly
MNTH = monthly
YEAR = yearly
ADHO = ad hoc which applies when payments are irregular
EXPI = payment at term
    
24-3

## Page 34

Row no. Data Element Name Definition of Data Element Format and allowable values IR FX EQ CD CM
Appendix B to the Consultation Paper - List of Proposed Data Elements Data element applicable to asset class
29 Fixed rate payment frequency period multiplier - Leg 1 Where applicable: number of time units (as expressed by the payment frequency period) that determines the frequency at 
which periodic payment dates occur for the fixed rate of leg 1.
For example, a transaction with payments occurring every two months is represented with a payment frequency period of 
“MNTH” (monthly) and a payment frequency period multiplier of 2.
This data element is not applicable if the payment
frequency period is “ADHO”. If payment frequency period is "EXPI", then the payment frequency period multiplier is 1. If the 
payment frequency is intraday, then the payment frequency period is “DAIL” and the payment frequency multiplier is 0.
Num(3,0)
Any value greater than or equal to zero.
    
30 Floating rate payment frequency period multiplier - Leg 
1
Where applicable: number of time units (as expressed by the payment frequency period) that determines the frequency at 
which periodic payment dates occur for the floating rate of leg 1. For example, a transaction with payments occurring every 
two months is represented with a payment frequency period of “MNTH” (monthly) and a payment frequency period 
multiplier of 2.
This data element is not applicable if the payment frequency period is “ADHO”. If payment frequency period is "EXPI", then 
the payment frequency period multiplier is 1. If the payment frequency is intraday, then the payment frequency period is 
“DAIL” and the payment frequency multiplier is 0.
Num(3,0)
Any value greater than or equal to zero.
    
31 Fixed rate payment frequency period multiplier - Leg 2 Where applicable: number of time units (as expressed by the payment frequency period) that determines the frequency at 
which periodic payment dates occur for the fixed rate of leg 2. For example, a transaction with payments occurring every 
two months is represented with a payment frequency period of “MNTH” (monthly) and a payment frequency period 
multiplier of 2.
This data element is not applicable if the payment frequency period is “ADHO”. If payment frequency period is "EXPI", then 
the payment frequency period multiplier is 1. If the payment frequency is intraday, then the payment frequency period is 
“DAIL” and the payment frequency multiplier is 0.
Num(3,0)
Any value greater than or equal to zero.
    
32 Floating rate payment frequency period multiplier - Leg 
2
Where applicable: number of time units (as expressed by the payment frequency period) that determines the frequency at 
which periodic payment dates occur for the floating rate of leg 2. For example, a transaction
with payments occurring every two months is represented with a payment frequency period of “MNTH” (monthly) and a 
payment frequency period multiplier of 2.
This data element is not applicable if the payment frequency period is “ADHO”. If payment frequency period is "EXPI", then 
the payment frequency period multiplier is 1. If the payment frequency is intraday, then the payment frequency period is 
“DAIL” and the payment frequency multiplier is 0.
Num(3,0)
Any value greater than or equal to zero.
    
33 Valuation amount Current value of the outstanding contract. without applying any valuation adjustments (i.e. any XVA adjustment such as 
CVA, DVA, etc).
Valuation amount is expressed as the exit cost of the contract or components of the contract, i.e. the price that would be 
received to sell the contract (in the market in an orderly transaction at the valuation date).
Num(25,5)
Any value. 
    
34 Valuation currency Currency in which the valuation amount is denominated. ISO 4217
Char(3)
Allowable values:
Currencies included in ISO 4217
    
35 Valuation timestamp Date and time of the last valuation marked to market, provided by the central counterparty or calculated using the current or 
last available market price of the inputs. If for example a currency exchange rate is the basis for a transaction’s valuation, 
then the valuation timestamp reflects the moment in time that exchange rate was current.
ISO 8601
YYYY-MM-DDThh:mm:ssZ, based on UTC. 
    
36 Valuation method Source and method used for the valuation of the transaction by the reporting counterparty.
If at least one valuation input is used that is classified as mark-to-model in the below table, then the whole valuation is 
classified as mark-to-model.
If only inputs are used that are classified as mark-to-market in the table below, then the whole valuation is classified as 
mark-to-market.
Char(4)
Allowable values:
MTMA = mark-to-market
MTMO = mark-to-model
CCPV = central counterparty’s valuation
    
37 Collateral portfolio indicator Indicator of whether the collateralisation was performed on a portfolio basis, if applicable. By “on a portfolio basis”, it is 
meant a set of transactions that are margined together (either on a net or a gross basis) contrary to the scenario where the 
margin is calculated and posted for each individual transaction separately.
Boolean
Allowable values:
true, if collateralised on a portfolio basis
false, if not part of a portfolio
    
38 Collateral portfolio code If collateral is reported on a portfolio basis, unique code assigned by the reporting counterparty to the portfolio, if applicable. 
This data element is not applicable if the collateralisation was performed on a transaction level basis, or if there is no 
collateral agreement or if no collateral is posted or received.
ISO 20022 Portfolio/Identification
Varchar(52)
Up to 52 alphanumerical characters.
    
39 Initial margin posted by the counterparty 1 (pre￾haircut)
Monetary value of initial margin that has been posted by the reporting counterparty, including any margin that is in transit 
and pending settlement unless inclusion of such margin is not allowed under the jurisdictional requirements, if applicable.
If the collateralisation is performed at portfolio level, the initial margin posted relates to the whole portfolio; if the 
collateralisation is performed for single transactions, the initial margin posted relates to such single transaction.
This refers to the total current value of the initial margin, rather than to its daily change. The data element refers both to 
uncleared and centrally cleared transactions.
For centrally cleared transactions, the data element does not include default fund contributions, nor collateral posted 
against liquidity provisions to the central counterparty, i.e. committed credit lines.
If the initial margin posted is denominated in more than one currency, those amounts are converted into a single currency 
chosen by the reporting counterparty and reported as one
total value.
ISO 20022: MarginCall/InitialMargin
Num(25,5)
Any value greater than or equal to zero.
    
24-4

## Page 35

Row no. Data Element Name Definition of Data Element Format and allowable values IR FX EQ CD CM
Appendix B to the Consultation Paper - List of Proposed Data Elements Data element applicable to asset class
40 Initial margin posted by the counterparty 1 (post￾haircut)
Monetary value of initial margin that has been posted by the reporting counterparty, including any margin that is in transit 
and pending settlement unless inclusion of such margin is not allowed under the jurisdictional requirements, if applicable.
If the collateralisation is performed at portfolio level, the initial margin posted relates to the whole portfolio; if the 
collateralisation is performed for single transactions, the initial margin posted relates to such single transaction.
This refers to the total current value of the initial margin after application of the haircut (if applicable), rather than to its daily 
change.
The data element refers both to uncleared and centrally cleared transactions. For centrally cleared transactions, the data 
element does not include default fund contributions, nor collateral posted against liquidity provisions to the central 
counterparty, i.e. committed credit lines.
If the initial margin posted is denominated in more than one currency, those amounts are converted into a single currency 
chosen by the reporting counterparty and reported as one total value.
ISO 20022: MarginCall/InitialMargin
Num(25,5)
Any value greater than or equal to zero.
    
41 Currency of initial margin posted Currency in which the initial margin posted is denominated, if applicable.
If the initial margin posted is denominated in more than one currency, this data element reflects one of those currencies into 
which the reporting counterparty has chosen to convert all the values of posted initial margins.
ISO 4217
Char(3)
Allowable values:
Currencies included in ISO 4217
    
42 Initial margin collected by the counterparty 1 (pre￾haircut)
Monetary value of initial margin that has been collected by the reporting counterparty, including any margin that is in transit 
and pending settlement unless inclusion of such margin is not allowed under the jurisdictional requirements, if applicable.
If the collateralisation is performed at portfolio level, the initial margin collected relates to the whole portfolio; if the 
collateralisation is performed for single transactions, the initial margin collected relates to such single transaction.
This refers to the total current value of the initial margin, rather than to its daily change. The data element refers both to 
uncleared and centrally cleared transactions. For centrally cleared transactions, the data element does not include 
collateral collected by the central counterparty as part of its investment activity.
If the initial margin collected is denominated in more than one currency, those amounts are converted into a single currency 
chosen by the reporting counterparty and reported as one total value.
ISO 20022: MarginCall/InitialMargin
Num(25,5)
Any value greater than or equal to zero.
    
43 Initial margin collected by the counterparty 1 (post￾haircut)
Monetary value of initial margin that has been collected by the reporting counterparty, including any margin that is in transit 
and pending settlement unless inclusion of such margin is not allowed under the jurisdictional requirements.
If the collateralisation is performed at portfolio level, the initial margin collected relates to the whole portfolio; if the 
collateralisation is performed for single transactions, the initial margin collected relates to such single transaction.
This refers to the total current value of the initial margin after application of the haircut (if applicable), rather than to its daily 
change.
The data element refers both to uncleared and centrally cleared transactions. For centrally cleared transactions, the data 
element does not include collateral collected by the central counterparty as part of its investment activity.
If the initial margin collected is denominated in more than one currency, those amounts are converted into a single currency 
chosen by the reporting counterparty and reported as one total value.
ISO 20022: MarginCall/InitialMargin
Num(25,5)
Any value greater than or equal to zero.
    
44 Currency of initial margin collected Currency in which the initial margin collected is denominated, if applicable.
If the initial margin collected is denominated in more than one currency, this data element reflects one of those currencies 
into which the reporting counterparty has chosen to convert all the values of collected initial margins.
ISO 4217
Char(3)
Allowable values:
Currencies included in ISO 4217
    
45 Variation margin posted by the counterparty 1 (pre￾haircut)
Monetary value of the variation margin posted by the reporting counterparty (including the cash-settled one), and including 
any margin that is in transit and pending settlement unless inclusion of such margin is not allowed under the jurisdictional 
requirements, if applicable.
Contingent variation margin is not included.
If the collateralisation is performed at portfolio level, the variation margin posted relates to the whole portfolio; if the 
collateralisation is performed for single transactions, the variation margin posted relates to such single transaction.
This data element refers to the total current value of the variation margin, cumulated since the first reporting of variation 
margins posted for the portfolio/transaction.
If the variation margin posted is denominated in more than one currency, those amounts are converted into a single 
currency chosen by the reporting counterparty and reported as one total value.
ISO 20022: MarginCall/VariationMargin
Num(25,5)
Any value greater than or equal to zero.
    
46 Variation margin posted by the counterparty 1 (post￾haircut)
Monetary value of the variation margin posted by the reporting counterparty (including the cash-settled one), and including 
any margin that is in transit and pending settlement unless inclusion of such margin is not allowed under the jurisdictional 
requirements, if applicable.
Contingent variation margin is not included.
If the collateralisation is performed at portfolio level, the variation margin posted relates to the whole portfolio; if the 
collateralisation is performed for single transactions, the variation margin posted relates to such single transaction.
This data element refers to the total current value of the variation margin after application of the haircut (if applicable), 
cumulated since the first reporting of posted variation margins for the portfolio/transaction.
If the variation margin posted is denominated in more than one currency, those amounts are converted into a single 
currency chosen by the reporting counterparty and reported as one total value.
ISO 20022: MarginCall/VariationMargin
Num(25,5)
Any value greater than or equal to zero.
    
24-5

## Page 36

Row no. Data Element Name Definition of Data Element Format and allowable values IR FX EQ CD CM
Appendix B to the Consultation Paper - List of Proposed Data Elements Data element applicable to asset class
47 Currency of variation margin posted Currency in which the variation margin posted is denominated, if applicable.
If the variation margin posted is denominated in more than one currency, this data element reflects one of those currencies 
into which the reporting counterparty has chosen to convert all the values of posted variation margins.
ISO 4217
Char(3)
Allowable values:
Currencies included in ISO 4217
    
48 Variation margin collected by the counterparty 1 (pre￾haircut)
Monetary value of the variation margin collected by the reporting counterparty (including the cash- settled one), and 
including any margin that is in transit and pending settlement unless inclusion of such margin is not allowed under the 
jurisdictional requirements, if applicable.
Contingent variation margin is not included.
If the collateralisation is performed at portfolio level, the variation margin collected relates to the whole portfolio; if the 
collateralisation is performed for single transactions, the variation margin collected relates to such single transaction.
This refers to the total current value of the variation margin, cumulated since the first reporting of collected variation 
margins for the portfolio/transaction.
If the variation margin collected is denominated in more than one currency, those amounts are converted into a single 
currency chosen by the reporting counterparty and reported as one total value.
ISO 20022: MarginCall/VariationMargin
Num(25,5)
Any value greater than or equal to zero.
    
49 Variation margin collected by the counterparty 1 (post￾haircut)
Monetary value of the variation margin collected by the reporting counterparty (including the cash- settled one), and 
including any margin that is in transit and pending settlement unless inclusion of such margin is not allowed under the 
jurisdictional requirements, if applicable.
Contingent variation margin is not included.
If the collateralisation is performed at portfolio level, the variation margin collected relates to the whole portfolio; if the 
collateralisation is performed for single transactions, the variation margin collected relates to such single transaction.
This refers to the total current value of the variation margin collected after application of the haircut (if applicable), 
cumulated since the first reporting of collected variation margins for the portfolio/transaction.
If the variation margin collected is denominated in more than one currency, those amounts are converted into a single 
currency chosen by the reporting counterparty and reported as one total value.
ISO 20022: MarginCall/VariationMargin
Num(25,5)
Any value greater than or equal to zero.
    
50 Currency of variation margin collected Currency in which the variation margin collected is denominated, if applicable.
If the variation margin collected is denominated in more than one currency, this data element reflects one of those 
currencies into which the reporting counterparty has chosen to convert all the values of collected variation margins.
ISO 4217
Char(3)
Allowable values:
Currencies included in ISO 4217
    
51 Excess collateral posted by the counterparty 1 Monetary value of any additional collateral posted by the reporting counterparty separate and independent from initial and 
variation margin. This refers to the total current value of the excess collateral before application of the haircut (if 
applicable), rather than to its daily change.
Any initial or variation margin amount posted that exceeds the required initial margin or required variation margin, is 
reported as part of the initial margin posted or variation margin posted respectively rather than included as excess 
collateral posted.
For centrally cleared transactions, excess collateral is reported only to the extent it can be assigned to a specific portfolio 
or transaction.
Num(25,5)
Any value greater than or equal to zero.
    
52 Currency of excess collateral posted Currency in which the excess collateral posted is denominated, if applicable.
If the excess collateral posted is denominated in more than one currency, this data element reflects one of those currencies 
into which the reporting counterparty has chosen to convert all the values of posted excess collateral.
ISO 4217
Char(3)
Allowable values:
Currencies included in ISO 4217
    
53 Excess collateral collected by the counterparty 1 Monetary value of any additional collateral collected by the reporting counterparty separate and independent from initial and 
variation margin. This data element refers to the total current value of the excess collateral before application of the haircut 
(if applicable), rather than to its daily change.
Any initial or variation margin amount collected that exceeds the required initial margin or required variation margin, is 
reported as part of the initial margin collected or variation margin collected respectively, rather than included as excess 
collateral collected.
For centrally cleared transactions excess collateral is reported only to the extent it can be assigned to a specific portfolio or 
transaction.
Num(25,5)
Any value greater than or equal to zero.
    
54 Currency of excess collateral collected Currency in which the excess collateral collected is denominated, if applicable.
If the excess collateral is denominated in more than one currency, this data element reflects one of those currencies into 
which the reporting counterparty has chosen to convert all the values of collected excess collateral.
ISO 4217
Char(3)
Allowable values:
Currencies included in ISO 4217
    
24-6

## Page 37

Row no. Data Element Name Definition of Data Element Format and allowable values IR FX EQ CD CM
Appendix B to the Consultation Paper - List of Proposed Data Elements Data element applicable to asset class
55 Collateralisation category Indicator of whether a collateral agreement (or collateral agreements) between the counterparties exists 
(uncollateralised/partially collateralised/one-way collateralised/fully collateralised), if applicable. This data element is 
provided for each transaction or each portfolio, depending on whether the collateralisation is performed at the transaction 
or portfolio level, and is applicable to both cleared and uncleared transactions.
Char(4)
Allowable values:
UNCL = Uncollateralised
There is no collateral agreement between the counterparties or the collateral agreement(s) between the counterparties stipulates that no collateral (neither initial margin nor variation margin) has to be posted 
with respect to the derivative transaction.
PRC1 = Partially collateralised: Counterparty 1 only
The collateral agreement(s) between the counterparties stipulates that the reporting counterparty regularly posts only variation margin and that the other counterparty does not post any margin with respect to 
the derivative transaction.
PRC2 = Partially collateralised: Counterparty 2 only
The collateral agreement(s) between the counterparties stipulates that the other counterparty regularly posts only variation margin and that the reporting counterparty does not post any margin with respect to 
the derivative transaction.
PRCL = Partially collateralised
The collateral agreement(s) between the counterparties stipulates that both counterparties regularly post only variation margin with respect to the derivative transaction.
OWC1 = One-way collateralised: Counterparty 1 only
The collateral agreement(s) between the counterparties stipulates that the reporting counterparty posts the initial margin and regularly posts variation margin and that the other counterparty does not post any 
margin with respect to the derivative transaction.
OWC2 = One-way collateralised: Counterparty 2 only
The collateral agreement(s) between the counterparties stipulates that the other counterparty posts the initial margin and regularly posts variation margin and that the reporting counterparty does not post any 
margin with respect to the derivative transaction.
    
OWP1 = One-way/partially collateralised: Counterparty 1
The collateral agreement(s) between the counterparties stipulates that the reporting counterparty posts the initial margin and regularly posts variation margin and that the other counterparty regularly posts only 
variation margin.
OWP2 = One- way/partially collateralised: Counterparty 2
The collateral agreement(s) between the counterparties stipulates that the other counterparty posts the initial margin and regularly posts variation margin and that the reporting counterparty regularly posts only 
variation margin.
FLCL = Fully collateralised
The collateral agreement(s) between the counterparties stipulates that both counterparties post initial margin and regularly post variation margin with respect to the derivative transaction.
56 Price Price specified in the OTC derivative transaction, if applicable. It does not include fees, taxes or commissions, if applicable.
For commodity fixed/float swaps and similar products with periodic payments, this data element refers to the fixed price of the fixed 
Leg(s).
For commodity and equity forwards and similar products, this data element refers to the forward price of the underlying or reference 
asset.
For equity swaps, portfolios swaps, and similar products, this data element refers to the initial price of the underlying or reference asset.
For contracts for difference and similar products, this data element refers to the initial price of the underlier. 
This data element is not applicable to:
• Interest rate swaps and forward rate agreements, as it is understood that the information included in the data elements Fixed rate and 
Spread may be interpreted as the price of the transaction.
• Interest rate options and interest rate swaptions, as it is understood that the information included in the data elements Strike price and 
Option premium may be interpreted as the price of the transaction.
• Commodity basis swaps, as it is understood that the information included in the data element Spread may be interpreted as the price of
the transaction.
• Foreign exchange swaps, forwards and options, as it is understood that the information included in the data elements Exchange rate,
Strike price, and Option premium may be interpreted as the price of the transaction.
• Equity options, as it is understood that the information included in the data elements Strike price and Option premium may be 
interpreted as the price of the transaction.
• Credit default swaps and credit total return swaps, as it is understood that the information included in the data elements Fixed rate,
Spread and Upfront payment (Other payment type: Upfront payment) may be interpreted as the price of the transaction.
• Commodity options, as it is understood that the information included in the data elements Strike price and Option premium may be 
interpreted as the price of the transaction.
Where the price is not known when a new transaction is reported, the price is updated as it becomes available.
For transactions that are part of a package, this data element contains the price of the component transaction where applicable.
ISO 20022: Price/Amount
Num(18,13), if Price notation = 1
Num(11,10), if Price notation = 3
Any value, if Price notation = 1
Any value expressed as decimal (eg 0.0257 instead of 2.57%), if Price notation = 3
    
57 Price currency Currency in which the price is denominated, if applicable.
Price currency is only applicable if Price notation = 1.
ISO 4217
Char(3)
Allowable values:
Currencies included in ISO 4217
    
58 Price notation Manner in which the price is expressed, if applicable. Char(1)
Allowable values:
1 = monetary amount
3 = decimal
    
59 Price unit of measure Unit of measure in which the price is expressed, if applicable. ISO 20022: Price/UnitOfMeasure
Char(4) 
Allowable values:
ISO 20022: approved external UnitOfMeasureCode codeset
    
60 Price schedule - Unadjusted effective date of the price Where applicable: for OTC derivative transactions with prices varying throughout the life of the transaction: Unadjusted 
effective date of the price.
Price schedule is only applicable if the price varies per schedule.
ISO 8601
YYYY-MM-DD, based on UTC, repeatable for each date.
    
61 Price schedule - Unadjusted end date of the price Where applicable: for OTC derivative transactions with prices varying throughout the life of the transaction: Unadjusted end 
date of the price.
(not applicable if the unadjusted end date of a given schedule’s period is back-to-back with the unadjusted effective date of 
the subsequent period).
Price schedule is only applicable if the price varies per schedule.
ISO 8601
YYYY-MM-DD, based on UTC, repeatable for each date.
    
24-7

## Page 38

Row no. Data Element Name Definition of Data Element Format and allowable values IR FX EQ CD CM
Appendix B to the Consultation Paper - List of Proposed Data Elements Data element applicable to asset class
62 Price schedule - Price in effect between the 
unadjusted effective date and unadjusted end date 
inclusive
Where applicable: for OTC derivative transactions with prices varying throughout the life of the transaction: Price in effect 
between the unadjusted effective date and unadjusted end date inclusive.
Price schedule is only applicable if the price varies per schedule.
2.54.3: ISO 20022: Price/Amount
Num(18,13), if Price notation = 1
Num(11,10), if Price notation = 3
Any value greater than zero, if Price notation = 1
Any value expressed as decimal (eg 0.0257 instead of 2.57%), if Price notation = 3
Repeatable for each price.
    
63 Fixed rate - Leg 1 Where applicable: for OTC derivative transactions with periodic payments, per annum rate of the fixed rate of leg 1. ISO 20022: Interest/Rate
Num(11,10), if Fixed rate notation = 2
Positive and negative values expressed as decimal (eg 0.0257 instead of 2.57%), if Fixed rate notation = 2
    
64 Fixed rate - Leg 2 Where applicable: for OTC derivative transactions with periodic payments, per annum rate of the fixed rate of leg 2. ISO 20022: Interest/Rate
Num(11,10), if Fixed rate notation = 2
Positive and negative values expressed as decimal (eg 0.0257 instead of 2.57%), if Fixed rate notation = 2
    
65 Fixed rate notation - Leg 1 Where applicable: manner in which the fixed rate is expressed for leg 1 Char(1)
Allowable values:
2 = decimal
    
66 Fixed rate notation - Leg 2 Where applicable: manner in which the fixed rate is expressed for leg 2 Char(1)
Allowable values:
2 = decimal
    
67 Spread - Leg 1 An indication of the spread of leg 1, Where applicable: for OTC derivative transactions with periodic payments (eg interest 
rate fixed/float swaps, interest rate basis swaps, commodity swaps),
• spread on the individual floating leg(s) index reference price, in the case where there is a spread on a floating leg(s).
• difference between the reference prices of the two floating leg indexes.
ISO 20022: Spread/SpreadRate or ISO 20022: Spread/PriceOffset or ISO 20022: Spread/BasisPointSpread
Num(18,13), if Spread notation = 1
Num(11,10), if Spread notation = 3
Num(5), if Spread notation = 4
Any value, if Spread notation = 1
Any value expressed as decimal (eg 0.0257 instead of 2.57%), if Spread notation = 3
Any integer value expressed in basis points (eg 257 instead of 2.57%), if Spread notation = 4
    
68 Spread - Leg 2 An indication of the spread of leg 2, Where applicable: for OTC derivative transactions with periodic payments (e.g. interest 
rate fixed/float swaps, interest rate basis swaps, commodity swaps),
• spread on the individual floating leg(s) index reference price, in the case where there is a
spread on a floating leg(s).
• difference between the reference prices of the two floating leg indexes.
ISO 20022: Spread/SpreadRate or ISO 20022: Spread/PriceOffset or ISO 20022: Spread/BasisPointSpread
Num(18,13), if Spread notation = 1
Num(11,10), if Spread notation = 3
Num(5), if Spread notation = 4
Any value, if Spread notation = 1
Any value expressed as decimal (eg 0.0257 instead of 2.57%), if Spread notation = 3
Any integer value expressed in basis points (eg 257 instead of 2.57%), if Spread notation = 4
    
69 Spread currency - Leg 1 Where applicable: currency in which the spread of leg 1 is denominated.
This data element is only applicable if Spread notation = 1.
ISO 4217
Char(3)
Allowable values:
Currencies included in ISO 4217
    
70 Spread currency - Leg 2 Where applicable: currency in which the spread of leg 2 is denominated.
This data element is only applicable if Spread notation = 1.
ISO 4217
Char(3)
Allowable values:
Currencies included in ISO 4217
    
71 Spread notation - Leg 1 Where applicable: manner in which the spread is expressed for leg 1. Char(1)
Allowable values:
1 = monetary amount
3 = decimal
4 = basis points
    
72 Spread notation - Leg 2 Where applicable: manner in which the spread is expressed for leg 2. Char(1)
Allowable values:
1 = monetary amount
3 = decimal
4 = basis points
    
73 Strike price Where applicable:
• For options other than FX options, swaptions and similar products, price at which the owner of an option can buy or sell 
the underlying asset of the option.
• For foreign exchange options, exchange rate at which the option can be exercised, expressed as the rate of exchange 
from converting the unit currency into the quoted currency. In the example 0.9426 USD/EUR, USD is the unit currency and 
EUR is the quoted currency; USD 1 = EUR 0.9426.Where the strike price is not known when a new transaction is reported, 
the strike price is updated as it becomes available.
• For volatility and variance swaps and similar products the volatility strike price is reported in this data element.
ISO 20022: Option/Strike Price
Num(18,13), if Strike price notation = 1
Num(11,10), if Strike price notation = 3
Any value (eg USD 6.39) expressed as 6.39, for equity options, commodity options, foreign exchange options and similar products, if Strike price notation = 1.
Any value expressed as decimals (eg 0.021 instead of 2.1%), for interest rate options, interest rate and credit swaptions quoted in spread, and similar products, if Strike price notation = 3.
    
24-8

## Page 39

Row no. Data Element Name Definition of Data Element Format and allowable values IR FX EQ CD CM
Appendix B to the Consultation Paper - List of Proposed Data Elements Data element applicable to asset class
74 Strike price currency/currency pair Where applicable:
For equity options, commodity options, and similar products, currency in which the strike price is denominated.
For foreign exchange options: Currency pair and order in which the strike price is expressed. It is expressed as unit 
currency/quoted currency. 
Strike price currency/currency pair is only applicable if Strike price notation = 1.
ISO 4217
Char(3)
For foreign exchange options: Char(3)/Char(3); [Unit currency/Quoted currency] without restricting the currency pair ordering
Allowable values:
Currencies included in ISO 4217
    
75 Strike price notation Manner in which the Strike price is expressed, if applicable. Char(1)
Allowable values:
1 = monetary amount
3 = decimal
    
76 Strike price schedule - Unadjusted effective date of 
the strike price
Where applicable: for options, swaptions and similar products with strike prices varying throughout the life of the 
transaction: Unadjusted effective date of the strike price.
Strike price schedule is only applicable if the strike price varies per schedule.
ISO 8601
YYYY-MM-DD, based on UTC, repeatable for each date.
    
77 Strike price schedule - Unadjusted end date of the 
strike price
Where applicable: for options, swaptions and similar products with strike prices varying throughout the life of the 
transaction: Unadjusted end date of the strike price.
(not applicable if the unadjusted end date of a given schedule’s period is back-to-back with the unadjusted effective date of 
the subsequent period).
Strike price schedule is only applicable if the strike price varies per schedule.
ISO 8601
YYYY-MM-DD, based on UTC, repeatable for each date.
    
78 Strike price schedule - Strike price in effect between 
the unadjusted effective date and unadjusted end date 
inclusive
Where applicable: for options, swaptions and similar products with strike prices varying throughout the life of the 
transaction: Strike price in effect between the unadjusted effective date and unadjusted end date inclusive.
Strike price schedule is only applicable if the strike price varies per schedule.
ISO 20022 Option/Strike Price
Num(18,13), if Strike price notation = 1
Num(11,10), if Strike price notation = 3
Any value greater than zero:
- Any value (eg USD 6.39) expressed as 6.39, for equity options, commodity options, foreign exchange options and similar products if Strike price notation = 1.
- Any value expressed as decimal (eg 0.021 instead of 2.1%), for interest rate options, interest rate and credit swaptions quoted in spread, and similar products, if Strike price notation = 3.
Repeatable for each strike price.
    
79 Option premium amount For options and swaptions of all asset classes, monetary amount paid by the option buyer. This data element is not 
applicable if the instrument is not an option or does not embed any optionality, if applicable.
Num(25,5)
Any value greater than or equal to zero.
    
80 Option premium currency For options and swaptions of all asset classes, currency in which the option premium amount is denominated. This data 
element is not applicable if the instrument is not an option or does not embed any optionality, if applicable.
ISO 4217
Char(3)
Allowable values:
Currencies included in ISO 4217
    
81 Option premium payment date Unadjusted date on which the option premium is paid, if applicable. ISO 8601
YYYY-MM-DD, based on UTC.
    
82 First exercise date First unadjusted date during the exercise period in which an option can be exercised, if applicable.
For European-style options, this date is same as the Expiration date. 
For American-style options, the first possible exercise date is the unadjusted date included in the execution timestamp.
For knock-in options, where the first exercise date is not known when a new transaction is reported, the first exercise date 
is updated as it becomes available.
This data element is not applicable if the instrument is not an option or does not embed any optionality.
ISO 8601
YYYY-MM-DD, based on UTC.
    
83 Exchange rate Exchange rate between the two different currencies specified in the OTC derivative transaction agreed by the 
counterparties at the inception of the transaction, expressed as the rate of exchange from converting the unit currency into 
the quoted currency, if applicable.
ISO 20022 CurrencyExchange/ExchangeRate
Num(18,13)
Any value greater than zero. 
    
84 Exchange rate basis Currency pair and order in which the exchange rate is denominated, expressed as unit currency/quoted currency, if 
applicable.
In the example 0.9426 USD/EUR, USD is the unit currency and EUR is the quoted currency, USD 1 = EUR 0.9426.
Char(3)/Char(3); [Unit currency/Quoted currency], without restricting the currency pair ordering (i.e. the exchange rate basis may be USD/EUR or EUR/USD).
Any pair of currencies included in ISO 4217.
    
85 Notional amount - Leg 1 Where applicable: Notional amount of leg 1.
- for OTC derivative transactions negotiated in monetary amounts, amount specified in the contract.
- for OTC derivative transactions negotiated in non-monetary amounts:
(1) Equity options and similar products: Product of the strike price and the number of shares or index units
(2) Equity forwards and similar products: Product of the forward price and the number of shares or index units
(3) Equity dividend swaps and similar products: Product of the period fixed strike and the number of shares or index units.
(4) Equity swaps, portfolio swaps and similar products: Product of the initial price and the number of shares or index units.
(5) Equity variance swaps and similar products: Variance amount.
(6) Equity volatility swaps and similar products: Vega notional amount
(7) Equity CFDs and similar products: Product of the initial price and the number of shares or index units
(8) Commodity options and similar products: Product of the strike price and the total notional quantity
(9) Commodity forwards and similar products: Product of the forward price and the total notional quantity
(10) Commodity fixed/float swaps and similar products: Product of the fixed price and the total notional quantity
(11) Commodity basis swaps and similar products: Product of the last available spot price at the time of the transaction of 
the underlying asset of the leg with no spread and the total notional quantity of the leg with no spread
(12) Commodity swaptions and similar products: Notional amount of the underlying contract
(13) Commodity CFDs and similar products: Product of the initial price and the total notional quantity
ISO 20022: Derivative/NotionalCurrencyAndAmount
Num(25,5)
Any value (Negative values are only allowed for commodity derivatives when applies).
    
24-9

## Page 40

Row no. Data Element Name Definition of Data Element Format and allowable values IR FX EQ CD CM
Appendix B to the Consultation Paper - List of Proposed Data Elements Data element applicable to asset class
Notes to the conversion table for OTC derivative transactions negotiated in non-monetary amounts:
Note 1: for transactions where the quantity unit of measure differs from the price unit of measure, the price or total quantity 
is converted to a unified unit of measure.
Note 2: if applicable to the transaction, the notional amount reflects any multipliers and option entitlements.
Note 3: for basket-type contracts, the notional amount of the transaction is the sum of the notional amounts of each 
constituent of the basket.
In addition:
For OTC derivative transactions with a notional amount schedule, the initial notional amount, agreed by the counterparties 
at the inception of the transaction, is reported in this data element.
For OTC foreign exchange options, in addition to this data element, the amounts are reported using the data elements Call 
amount and Put amount. For amendments or lifecycle events, the resulting outstanding notional amount is reported; (steps 
in notional amount schedules are not considered to be amendments or lifecycle events);
Where the notional amount is not known when a new transaction is reported, the notional amount is updated as it becomes 
available.
86 Notional amount - Leg 2 Where applicable: Notional amount of leg 2.
- for OTC derivative transactions negotiated in monetary amounts, amount specified in the contract.
- for OTC derivative transactions negotiated in non-monetary amounts:
(1) Equity options and similar products: Product of the strike price and the number of shares or index units
(2) Equity forwards and similar products: Product of the forward price and the number of shares or index units
(3) Equity dividend swaps and similar products: Product of the period fixed strike and the number of shares or index units.
(4) Equity swaps, portfolio swaps and similar products: Product of the initial price and the number of shares or index units.
(5) Equity variance swaps and similar products: Variance amount.
(6) Equity volatility swaps and similar products: Vega notional amount
(7) Equity CFDs and similar products: Product of the initial price and the number of shares or index units
(8) Commodity options and similar products: Product of the strike price and the total notional quantity
(9) Commodity forwards and similar products: Product of the forward price and the total notional quantity
(10) Commodity fixed/float swaps and similar products: Product of the fixed price and the total notional quantity
(11) Commodity basis swaps and similar products: Product of the last available spot price at the time of the transaction of 
the underlying asset of the leg with no spread and the total notional quantity of the leg with no spread
(12) Commodity swaptions and similar products: Notional amount of the underlying contract
(13) Commodity CFDs and similar products: Product of the initial price and the total notional quantity
ISO 20022: Derivative/NotionalCurrencyAndAmount
Num(25,5)
Any value (Negative values are only allowed for commodity derivatives when applies).
    
Notes to the conversion table for OTC derivative transactions negotiated in non-monetary amounts:
Note 1: for transactions where the quantity unit of measure differs from the price unit of measure, the price or total quantity 
is converted to a unified unit of measure.
Note 2: if applicable to the transaction, the notional amount reflects any multipliers and option entitlements.
Note 3: for basket-type contracts, the notional amount of the transaction is the sum of the notional amounts of each 
constituent of the basket.
In addition:
For OTC derivative transactions with a notional amount schedule, the initial notional amount, agreed by the counterparties 
at the inception of the transaction, is reported in this data element.
For OTC foreign exchange options, in addition to this data element, the amounts are reported using the data elements Call 
amount and Put amount. For amendments or lifecycle events, the resulting outstanding notional amount is reported; (steps 
in notional amount schedules are not considered to be amendments or lifecycle events);
Where the notional amount is not known when a new transaction is reported, the notional amount is updated as it becomes 
available.
87 Delta The ratio of the change in the price of an OTC derivative transaction to the change in the price of the underlier if applicable. Num(25,5)
Any value
    
88 Call amount For foreign exchange options, the monetary amount that the option gives the right to buy, if applicable. ISO 20022: CurrencyOption/CallAmount
Num(25,5)
Any value greater than zero. 
    
89 Put amount For foreign exchange options, the monetary amount that the option gives the right to sell, if applicable. ISO 20022: CurrencyOption/PutAmount
Num(25,5)
Any value greater than zero. 
    
90 Notional currency - Leg 1 Where applicable: the currency in which the notional amount of leg 1 is denominated. ISO 4217
Char(3)
Allowable values:
Currencies included in ISO 4217
    
91 Notional currency - Leg 2 Where applicable: the currency in which the notional amount of leg 2 is denominated. ISO 4217
Char(3)
Allowable values:
Currencies included in ISO 4217
    
92 Call currency For foreign exchange options, the currency in which the Call amount is denominated, if applicable. ISO 4217
Char(3)
Allowable values:
Currencies included in ISO 4217
    
93 Put currency For foreign exchange options, the currency in which the Put amount is denominated, if applicable. ISO 4217
Char(3)
Allowable values:
Currencies included in ISO 4217
    
94 Quantity unit of measure - Leg 1 Where applicable: unit of measure in which the Total notional quantity and the Notional quantity schedules are expressed 
of leg 1.
ISO 20022: ProductQuantity/UnitOfMeasure
Char(4) 
Allowable values:
ISO 20022: approved external UnitOfMeasureCode codeset
    
24-10

## Page 41

Row no. Data Element Name Definition of Data Element Format and allowable values IR FX EQ CD CM
Appendix B to the Consultation Paper - List of Proposed Data Elements Data element applicable to asset class
95 Quantity unit of measure - Leg 2 Where applicable: unit of measure in which the Total notional quantity and the Notional quantity schedules are expressed 
of leg 2.
ISO 20022: ProductQuantity/UnitOfMeasure
Char(4) 
Allowable values:
ISO 20022: approved external UnitOfMeasureCode codeset
    
96 Notional amount schedule - Unadjusted date on which 
the associated notional amount becomes effective - 
Leg 1
Where applicable: for OTC derivative transactions negotiated in monetary amounts with a notional amount schedule: 
Unadjusted date on which the associated notional amount becomes effective of leg 1.
The initial notional amount and associated unadjusted effective and end date are reported as the first values of the 
schedule.
This data element is not applicable to OTC derivative transactions with notional amounts that are condition- or event￾dependent.
ISO 8601
YYYY-MM-DD, based on UTC, repeatable for each date.
    
97 Notional amount schedule - Unadjusted date on which 
the associated notional amount becomes effective - 
Leg 2
Where applicable: for OTC derivative transactions negotiated in monetary amounts with a notional amount schedule: 
Unadjusted date on which the associated notional amount becomes effective of leg 2.
The initial notional amount and associated unadjusted effective and end date are reported as the first values of the 
schedule.
This data element is not applicable to OTC derivative transactions with notional amounts that are condition- or event￾dependent.
ISO 8601
YYYY-MM-DD, based on UTC, repeatable for each date.
    
98 Notional amount schedule - Unadjusted end date of 
the notional amount - Leg 1
Where applicable: for OTC derivative transactions negotiated in monetary amounts with a notional amount schedule: 
Unadjusted end date of the notional amount of leg 1
(not applicable if the unadjusted end date of a given schedule’s period is back-to-back with the unadjusted effective date of 
the subsequent period)
The initial notional amount and associated unadjusted effective and end date are reported as the first values of the 
schedule.
This data element is not applicable to OTC derivative transactions with notional amounts that are condition- or event￾dependent.
ISO 8601
YYYY-MM-DD, based on UTC, repeatable for each date.
    
99 Notional amount schedule - Unadjusted end date of 
the notional amount - Leg 2
Where applicable: for OTC derivative transactions negotiated in monetary amounts with a notional amount schedule: 
Unadjusted end date of the notional amount of leg 2
(not applicable if the unadjusted end date of a given schedule’s period is back-to-back with the unadjusted effective date of 
the subsequent period)
The initial notional amount and associated unadjusted effective and end date are reported as the first values of the 
schedule.
This data element is not applicable to OTC derivative transactions with notional amounts that are condition- or event￾dependent.
ISO 8601
YYYY-MM-DD, based on UTC, repeatable for each date.
    
100 Notional amount schedule - Notional amount which 
becomes effective on the associated unadjusted 
effective date - Leg 1
Where applicable: for OTC derivative transactions negotiated in monetary amounts with a notional amount schedule: 
Notional amount which becomes effective on the associated unadjusted effective date of leg 1.
The initial notional amount and associated unadjusted effective and end date are reported as the first values of the 
schedule.
This data element is not applicable to OTC derivative transactions with notional amounts that are condition- or event￾dependent. The currency of the varying notional amounts in the schedule is reported in Notional currency.
ISO 20022: Derivative/NotionalCurrencyAndAmount
Num(25,5)
Any value
Repeatable for each notional amount.
    
101 Notional amount schedule - Notional amount which 
becomes effective on the associated unadjusted 
effective date - Leg 2
Where applicable: for OTC derivative transactions negotiated in monetary amounts with a notional amount schedule: 
Notional amount which becomes effective on the associated unadjusted effective date of leg 2.
The initial notional amount and associated unadjusted effective and end date are reported as the first values of the 
schedule.
This data element is not applicable to OTC derivative transactions with notional amounts that are condition- or event￾dependent. The currency of the varying notional amounts in the schedule is reported in Notional currency.
ISO 20022: Derivative/NotionalCurrencyAndAmount
Num(25,5)
Any value 
Repeatable for each notional amount.
    
102 Total notional quantity - Leg 1 Where applicable: aggregate Notional quantity of the underlying asset for the term of the transaction of leg 1, if applicable.
Where the Total notional quantity is not known when a new transaction is reported, the Total notional quantity is updated as 
it becomes available.
Num(25,5)
Any value greater than or equal to zero.
    
103 Total notional quantity - Leg 2 Where applicable: aggregate Notional quantity of the underlying asset for the term of the transaction of leg 2, if applicable.
Where the Total notional quantity is not known when a new transaction is reported, the Total notional quantity is updated as 
it becomes available.
Num(25,5)
Any value greater than or equal to zero.
    
104 Notional quantity schedule - Unadjusted date on which 
the associated notional quantity becomes effective - 
Leg 1
Where applicable: for OTC derivative transactions negotiated in non-monetary amounts with a Notional quantity schedule: 
Unadjusted date on which the associated notional quantity becomes effective of leg 1.
The initial notional quantity and associated unadjusted effective and end date are be reported as the first values of the 
schedule.
This data element is not applicable to OTC derivative transactions with notional quantities that are condition- or event￾dependent.
ISO 8601
YYYY-MM-DD, based on UTC, repeatable for each date.
    
105 Notional quantity schedule - Unadjusted date on which 
the associated notional quantity becomes effective - 
Leg 2
Where applicable: for OTC derivative transactions negotiated in non-monetary amounts with a Notional quantity schedule: 
Unadjusted date on which the associated notional quantity becomes effective of leg 2.
The initial notional quantity and associated unadjusted effective and end date are be reported as the first values of the 
schedule.
This data element is not applicable to OTC derivative transactions with notional quantities that are condition- or event￾dependent.
ISO 8601
YYYY-MM-DD, based on UTC, repeatable for each date.
    
106 Notional quantity schedule - Unadjusted end date of 
the notional quantity - Leg 1
Where applicable: for OTC derivative transactions negotiated in non-monetary amounts with a Notional quantity schedule: 
Unadjusted end date of the notional quantity of leg 1.
(not applicable if the unadjusted end date of a given schedule’s period is back-to-back with the unadjusted effective date of 
the subsequent period)
The initial notional quantity and associated unadjusted effective and end date are be reported as the first values of the 
schedule.
This data element is not applicable to OTC derivative transactions with notional quantities that are condition- or event￾dependent.
ISO 8601
YYYY-MM-DD, based on UTC, repeatable for each date.
    
24-11

## Page 42

Row no. Data Element Name Definition of Data Element Format and allowable values IR FX EQ CD CM
Appendix B to the Consultation Paper - List of Proposed Data Elements Data element applicable to asset class
107 Notional quantity schedule - Unadjusted end date of 
the notional quantity - Leg 2
Where applicable: for OTC derivative transactions negotiated in non-monetary amounts with a Notional quantity schedule: 
Unadjusted end date of the notional quantity of leg 2.
(not applicable if the unadjusted end date of a given schedule’s period is back-to-back with the unadjusted effective date of 
the subsequent period)
The initial notional quantity and associated unadjusted effective and end date are be reported as the first values of the 
schedule.
This data element is not applicable to OTC derivative transactions with notional quantities that are condition- or event￾dependent.
ISO 8601
YYYY-MM-DD, based on UTC, repeatable for each date.
    
108 Notional quantity schedule - Notional quantity which 
becomes effective on the associated unadjusted 
effective date - Leg 1
Where applicable: for OTC derivative transactions negotiated in non-monetary amounts with a Notional quantity schedule: 
Notional quantity which becomes effective on the associated unadjusted effective date of leg 1.
The initial notional quantity and associated unadjusted effective and end date are be reported as the first values of the 
schedule.
This data element is not applicable to OTC derivative transactions with notional quantities that are condition- or event￾dependent.
Num(25,5)
Any value greater than or equal to zero.
Repeatable for each notional quantity.
    
109 Notional quantity schedule - Notional quantity which 
becomes effective on the associated unadjusted 
effective date - Leg 2
Where applicable: for OTC derivative transactions negotiated in non-monetary amounts with a Notional quantity schedule: 
Notional quantity which becomes effective on the associated unadjusted effective date of leg 2.
The initial notional quantity and associated unadjusted effective and end date are be reported as the first values of the 
schedule.
This data element is not applicable to OTC derivative transactions with notional quantities that are condition- or event￾dependent.
Num(25,5)
Any value greater than or equal to zero.
Repeatable for each notional quantity.
    
110 CDS index attachment point Defined lower point at which the level of losses in the underlying portfolio reduces the notional of a tranche. For example, 
the notional in a tranche with an attachment point of 3% will be reduced after 3% of losses in the portfolio have occurred. 
This data element is not applicable if the transaction is not a CDS tranche transaction (index or custom basket).
ISO 20022: Tranche/AttachmentPoint
Num(11,10)
Any value between 0 and 1 (including 0 and 1), expressed as decimal (e.g. 0.05 instead of 5%).
    
111 CDS index detachment point Defined point beyond which losses in the underlying portfolio no longer reduce the notional of a tranche. For example, the 
notional in a tranche with an attachment point of 3% and a detachment point of 6% will be reduced after there have been 
3% of losses in the portfolio. 6% losses in the portfolio deplete the notional of the tranche. This data element is not 
applicable if the transaction is not a CDS tranche transaction (index or custom basket).
ISO 20022: Tranche/AttachmentPoint
Num(11,10)
Any value between 0 and 1 (including 0 and 1), expressed as decimal (e.g. 0.05 instead of 5%).
    
112 Other payment amount Payment amounts with corresponding payment types to accommodate requirements of transaction descriptions from 
different asset classes, if applicable.
Num(25,5)
Any value greater than or equal to zero.
Repeatable in the case of multiple payments
    
113 Other payment type Type of Other payment amount, if applicable.
Option premium payment is not included as a payment type as premiums for option are reported using the option premium 
dedicated data element.
Char(4)
Repeatable in the case of multiple payments
Allowable values:
UFRO = Upfront Payment, i.e. the initial payment made by one of the counterparties either to bring a transaction to fair value or for any other reason that may be the cause of an off-market transaction
UWIN = Unwind or Full termination, i.e. the final settlement payment made when a transaction is unwound prior to its end date; Payments that may result due to full termination of derivative transaction(s)
PEXH = Principal Exchange, i.e. Exchange of notional values for cross- currency swaps
    
114 Other payment currency Currency in which Other payment amount is denominated, if applicable. ISO 4217
Char(3)
Repeatable in the case of multiple payments
Allowable values:
Currencies included in ISO 4217
    
115 Other payment date Unadjusted date on which the other payment amount is paid, if applicable. ISO 8601
YYYY-MM-DD, based on UTC.
Repeatable in the case of multiple payments
    
116 Other payment payer Identifier of the payer of Other payment amount, if applicable. ISO 17442 Legal Entity Identifier (LEI)
Char(20), for an LEI code
Varchar(72), for natural persons who are acting as private individuals (not eligible for an LEI per the ROC Statement - Individuals Acting in a Business Capacity).
Repeatable in the case of multiple payments
Allowable values:
LEI code that is included in the LEI data as published by the Global LEI Foundation (GLEIF, www.gleif.org/).
For natural persons who are acting as private individuals (not eligible for an LEI per the ROC Statement - Individuals Acting in a Business Capacity): LEI of the reporting counterparty followed by a unique 
identifier assigned and maintained consistently by the reporting counterparty for that natural person(s) for regulatory reporting purpose.
    
117 Other payment receiver Identifier of the receiver of Other payment amount, if applicable. ISO 17442 Legal Entity Identifier (LEI)
Char(20), for an LEI code
Varchar(72), for natural persons who are acting as private individuals (not eligible for an LEI per the ROC Statement - Individuals Acting in a Business Capacity).
Repeatable in the case of multiple payments
Allowable values:
LEI code that is included in the LEI data as published by the Global LEI Foundation (GLEIF, www.gleif.org/).
For natural persons who are acting as private individuals (not eligible for an LEI per the ROC Statement - Individuals Acting in a Business Capacity): LEI of the reporting counterparty followed by a unique 
identifier assigned and maintained consistently by the reporting counterparty for that natural person(s) for regulatory reporting purpose.
    
24-12

## Page 43

Row no. Data Element Name Definition of Data Element Format and allowable values IR FX EQ CD CM
Appendix B to the Consultation Paper - List of Proposed Data Elements Data element applicable to asset class
118 Package identifier Where applicable: identifier (determined by the Reporting Party) in order to connect
- two or more transactions that are reported separately by the reporting counterparty, but that are negotiated together as
the product of a single economic agreement.
- two or more reports pertaining to the same transaction whenever jurisdictional reporting requirement does not allow the 
transaction to be reported with a single report to TRs.
A package may include reportable and non-reportable transactions. 
This data element is not applicable
- if no package is involved, or
- to allocations
Where the package identifier is not known when a new transaction is reported, the package identifier is updated as it 
becomes available.
Varchar(35)
Up to 35 alphanumerical characters.
    
119 Package transaction price Where applicable: traded price of the entire package in which the reported derivative transaction is a component. This data 
element is not applicable if
- no package is involved, or
- package transaction spread is used
Prices and related data elements of the transactions (Price currency, Price notation, Price unit of measure) that represent 
individual components of the package are reported when available.
The package transaction price may not be known when a new transaction is reported but may be updated later.
ISO 20022: Price/Amount
Num(18,13), if Package transaction price notation = 1
Num(11,10), if Package transaction price notation = 3
Any value, if Package transaction price notation = 1
Any value expressed as decimal (eg 0.0257 instead of 2.57%), if Package transaction price notation = 3
    
120 Package transaction price currency Where applicable: currency in which the Package transaction price is denominated. 
This data element is not applicable if
- no package is involved, or
- Package transaction spread is used, or
- Package transaction price notation = 3
ISO 4217
Char(3)
Allowable values:
Currencies included in ISO 4217
    
121 Package transaction price notation Where applicable: manner in which the Package transaction price is expressed. 
This data element is not applicable if
- no package is involved, or
- Package transaction spread is used
Char(1)
Allowable values:
1 = monetary amount
3 = decimal
    
122 Package transaction spread Where applicable: traded price of the entire package in which the reported derivative transaction is a component of a 
package transaction.
Package transaction price when the price of the package is expressed as a spread, difference between two reference 
prices.
This data element is not applicable if
- no package is involved, or
- Package transaction price is used
Spread and related data elements of the transactions (spread currency, Spread notation) that represent individual 
components of the package are reported when available.
Package transaction spread may not be known when a new transaction is reported but may be updated later.
ISO 20022: Spread/SpreadRate or ISO 20022: Spread/PriceOffset or ISO 20022: Spread: BasisPointSpread
Num(18,13), if Package transaction spread notation = 1
Num(11,10), if Package transaction spread notation = 3
Num(5), if Package transaction spread notation = 4
Any value, if Package transaction spread notation = 1
Any value expressed as decimal (eg 0.0257 instead of 2.57%), Package spread price notation = 3
Any integer value expressed in basis points (eg 257 instead of 2.57%), if Package transaction spread notation = 4
    
123 Package transaction spread currency Where applicable: currency in which the Package transaction spread is denominated. 
This data element is not applicable if
- no package is involved, or
- Package transaction price is used, or
- Package transaction spread notation = 3 or = 4
ISO 4217
Char(3)
Allowable values:
Currencies included in ISO 4217
    
124 Package transaction spread notation Where applicable: manner in which the Package transaction spread is expressed. 
This data element is not applicable if
• no package is involved, or
• Package transaction price is used
Char(1)
Allowable values:
1 = monetary amount
3 = decimal
4 = basis points
    
125 Prior UTI (for one-to-one and one-to-many relations 
between transactions)
Where applicable: UTI assigned to the predecessor transaction that has given rise to the reported transaction due to a 
lifecycle event, in a one-to-one relation between transactions (eg in the case of a novation, when a transaction is 
terminated, and a new transaction is generated) or in a one- to-many relation between transactions (eg in clearing or if a 
transaction is split into several different transactions).
This data element is not applicable when reporting many-to-one and many-to-many relations between transactions (eg in 
the case of a compression).
ISO 23897 Unique transaction identifier
Varchar(52)
Up to 52 alphanumeric characters
    
126 Custom basket code Where applicable: if the OTC derivative transaction is based on a custom basket, unique code assigned by the structurer of 
the custom basket to link its constituents. This data element is not applicable if no custom basket is involved or no unique 
code has been assigned to it.
Varchar(72)
ISO 17442 Legal Entity Identifier (LEI) code of the basket structurer followed by a unique identifier up to 52 alphanumeric characters.
    
127 Basket constituent identifier An identifier that represents a constituent of an underlying custom basket,in line with the Underlier ID within the ISO 4914 
UPI reference data elements, as maintained by the UPI Service Provider or in line with an identifier that would be reported 
as an Underlier ID (Other) where the UPI Underlier ID is ‘OTHER’. This data element is not applicable if no custom basket 
is involved.
Varchar(350)
An identifier that can be used to determine an asset, index or benchmark included in a basket
Up to 350 alphanumeric characters.
Repeatable in the case of multiple basket constituents
    
128 Basket constituent unit of measure Where applicable: unit of measure in which the number of units of a particular custom basket constituent is expressed. This 
data element is not applicable if no custom basket is involved.
ISO 20022: ProductQuantity/Unit Of Measure Code
Char(4)
ISO 20022: approved external UnitOfMeasureCode codeset
Repeatable in the case of multiple basket constituents
    
129 Basket constituent number of units Where applicable: the number of units of a particular constituent in a custom basket. This data element is not applicable if 
no custom basket is involved.
Num(18,13)
Any value greater than zero.
Repeatable in the case of multiple basket constituents
    
24-13

## Page 44

Row no. Data Element Name Definition of Data Element Format and allowable values IR FX EQ CD CM
Appendix B to the Consultation Paper - List of Proposed Data Elements Data element applicable to asset class
130 Basket constituent identifier source Where applicable: the origin, or publisher, of the associated Basket constituent identifier, in line with the Underlier ID source 
within the ISO 4914 UPI reference data elements as maintained by the UPI Service Provider or in line with the allowable 
value that would be reported as an Underlier ID (Other) source where the UPI Underlier ID is ‘OTHER’. This data element 
is not applicable if no custom basket is involved.
Varchar(350)
The origin, or publisher, of the associated basket constituent identifier.
Up to 350 alphanumeric characters.
Repeatable in the case of multiple basket constituents
    
131 Underlier ID (OTHER) Where applicable: the asset(s), index (indices) or benchmark underlying a contract or, in the case of a foreign exchange 
derivative, identification of index.
This data element is applicable when the value of Underlier ID is submitted as ‘OTHER’ to the UPI service provider.
Varchar(350)
An identifier that can be used to determine the asset(s), index (indices) or benchmark underlying a contract.
Up to 350 alphanumeric characters.
    
132 Underlier ID (OTHER) source Where applicable: the origin, or publisher, of the associated Underlier ID (Other).
This data element is applicable when the value of Underlier ID source is submitted as ‘OTHER’ to the UPI service provider.
Varchar(350)
The origin, or publisher, of the associated Underlier ID.
Up to 350 alphanumeric characters.
    
133 Underlying asset trading platform identifier Where applicable: for a platform (e.g. exchange) traded underlying asset, the platform on which the asset is traded. 
This data element is not applicable to OTC derivative transactions with custom basket constituents.
ISO 10383 Segment Market Identifier Code (MIC)
Char(4)
ISO 10383 Segment Market identifier codes.
    
134 Underlying asset price source Where applicable: for an underlying asset or benchmark not traded on a platform, the source of the price used to determine 
the value or level of the asset or benchmark.
This data element is not applicable to OTC derivative transactions with custom basket constituents.
Varchar(50)
Up to 50 alphanumeric characters.
    
135 Crypto asset underlying indicator Where applicable: indicator of whether the underlying of the derivative is crypto asset. This element should be reported as 
‘true’ if any of the underlyings is a crypto asset (immediate or ultimate underlying as well as where the derivative is based 
on a mix of crypto assets and other underlyings).
Boolean
Allowable values:
true, if underlying is crypto asset
false, if underlying is not crypto asset
    
136 Action type Type of action taken on the transaction or type of end-of-day reporting. Char(4)
Allowable values:
NEWT = New
The creation of the first transaction resulting in the generation of a new UTI.
MODI = Modify
A modification of the terms of a previously reported transaction due to a newly negotiated modification (amendment) or a filling in of not available missing information (e.g., post price transaction). It does not include correction of a 
previously reported transaction.
CORR = Correct
A correction of erroneous data of a previously reported transaction.
EROR = Error
A cancellation of a wrongly submitted entire transaction in case it never came into existence or was not subject to the reporting requirements under the applicable law of a given jurisdiction, or a cancellation of a duplicate report.
TERM = Terminate
A termination of a previously reported transaction.
REVI = Revive
An action that reinstates a reported transaction that was reported with action type “Error” or terminated by mistake or expired due to an incorrectly reported Expiration date.
PRTO = Transfer out
A transfer of a transaction from one reporting agent to another reporting agent (change of reporting agent).
VALU = Valuation
An update of a valuation of a transaction. There will be no corresponding Event type.
MARU = Collateral/Margin update
An update to collateral margin data. There will be no corresponding Event type.
    
137 Event type Explanation or reason for the action being taken on the transaction. Char(4)
Allowable values:
TRAD = Trade
Creation or modification of a transaction.
NOVA = Novation/Step-in
A novation or step-in legally moves part or all of the financial risks of a transaction from a transferor to a transferee and has the effect of terminating/modifying the original transaction so that it is either 
terminated or its notional is modified.
COMP = Post trade risk reduction exercise
Compressions and other post trade risk reduction exercises generally have the effect either of terminating or modifying (i.e., reducing the notional value) a set of existing transactions and/or of creating a set of 
new transaction(s). These processes result in largely the same exposure of market risk that existed prior to the event for the counterparty.
ETRM = Early termination
Termination of an existing transaction prior to expiration date.
CLRG = Clearing
Central clearing is a process where a central counterparty (CCP) interposes itself between counterparties to transactions, becoming the buyer to every seller and the seller to every buyer and thereby ensuring 
the performance of open transactions. It has the effect of terminating an existing transaction between the buyer and the seller.
EXER = Exercise
The full or partial exercise of an option or swaption by one counterparty of the transaction.
ALOC = Allocation
The process by which portions of a single transaction (or multiple transactions) are allocated to one or multiple different counterparties and reported as new transactions.
    
24-14

## Page 45

Row no. Data Element Name Definition of Data Element Format and allowable values IR FX EQ CD CM
Appendix B to the Consultation Paper - List of Proposed Data Elements Data element applicable to asset class
CLAL = Clearing & Allocation
A simultaneous clearing and allocation event in a central counterparty (CCP).
CREV = Credit event
An event that results in a modification or a termination of a previously submitted credit transaction. Applies only to credit derivatives.
PTNG = Transfer
The process by which a transaction is transferred to another reporting agent that has the effect of the closing of the transaction reported by one reporting agent and opening of the same transaction using the 
same UTI by a different agent.
CORP = Corporate event
The process by which a corporate action is taken on equity underlying that impacts the transactions on that equity.
UPDT = Update
Update of an outstanding transaction performed in order to ensure its conformity with the amended reporting requirements.
138 Event timestamp Date and time of occurrence of the event.
In the case of a modification agreed for a future date, this data element should reflect the date, the modification occurs 
(becomes effective) and not when it was negotiated.
In the case of a correction, this data element should reflect the date and time as of when the correction is applicable.
In the case of a clearing event, this data element should reflect the recorded date and time when the alpha transaction is 
accepted by the central counterparty (CCP) for clearing.
In the case of collateral update, the date and time for which the information contained in the report is provided.
ISO 8601
YYYY-MM-DDThh:mm:ssZ, based on UTC. 
    
139 Event identifier Where applicable: Unique identifier to link transactions entering into and resulting from an event, which may be, but is not 
limited to, compression or other post trade risk reduction exercises, credit event, etc. The unique identifier may be assigned 
by the reporting counterparty or a service provider or CCP providing the service.
Varchar(52)
ISO 17442 Legal Entity Identifier (LEI) code of the entity assigning the event identifier followed by a unique identifier up to 32 characters.
    
140 Unique Transaction Identifier (UTI) The unique transaction identifier as described in the Technical Guidance on the Harmonization of the Unique Transaction 
Identifier published by the Committee on Payments and Market Infrastructures and Board of International Organization of 
Securities Commissions in February 2017. 
ISO 23897 - Unique transaction identifier
Varchar(52)
Up to 52 alphanumeric characters, only the he upper-case alphabetic characters A–Z and the digits 0–9 are allowed
    
141 Unique Product Identifier (UPI) A unique set of characters that represents a particular OTC derivative. ISO 4914 - Unique product identifier
UPI code in accordance with the ISO standard implemented pursuant to the FSB governance arrangements for the UPI
    
142 Notional quantity - Leg 1 Where applicable, Notional quantity of leg 1. 
For swap transactions negotiated in non-monetary amounts with fixed notional quantity for each schedule period (i.e., 50 
barrels per month).
The frequency is reported in Quantity frequency and the unit of measure is reported in Quantity unit of measure.
Num(25,5)
Any value greater than or equal to zero.
    
143 Notional quantity - Leg 2 Where applicable, Notional quantity of leg 2.
For swap transactions negotiated in non-monetary amounts with fixed notional quantity for each schedule period (i.e., 50 
barrels per month).
The frequency is reported in Quantity frequency and the unit of measure is reported in Quantity unit of measure.
Num(25,5)
Any value greater than or equal to zero.
    
144 Quantity frequency - Leg 1 The rate at which the quantity is quoted on the leg 1 of the swap transaction. e.g., hourly, daily, weekly, monthly, if 
applicable.
Char(4)
Allowable values:
HOUL = Hourly 
DAIL = Daily 
WEEK = Weekly 
MNTH = Monthly 
ONDE = OnDemand
YEAR = Yearly 
EXPI = End of term
ADHO = Ad hoc which applies when payments are irregular
    
145 Quantity frequency - Leg 2 The rate at which the quantity is quoted on the leg 2 of the swap transaction. e.g., hourly, daily, weekly, monthly, if 
applicable.
Char(4)
Allowable values:
HOUL = Hourly 
DAIL = Daily 
WEEK = Weekly 
MNTH = Monthly 
ONDE = OnDemand
YEAR = Yearly 
EXPI = End of term
ADHO = Ad hoc which applies when payments are irregular
    
146 Quantity frequency multiplier - Leg 1 The number of time units for the Quantity frequency of leg 1, if applicable. Num(3,0)
Any value greater than or equal to zero.
    
147 Quantity frequency multiplier - Leg 2 The number of time units for the Quantity frequency of leg 2, if applicable. Num(3,0)
Any value greater than or equal to zero.
    
148 Fixing date - Leg 1 Describes the specific date when a non-deliverable forward as well as various types of FX OTC options such as cash￾settled options that will "fix" against a particular exchange rate, which will be used to compute the ultimate cash settlement 
of leg 1, if applicable.
ISO 8601
YYYY-MM-DD, based on UTC.
    
149 Fixing date - Leg 2 Describes the specific date when a non-deliverable forward as well as various types of FX OTC options such as cash￾settled options that will "fix" against a particular exchange rate, which will be used to compute the ultimate cash settlement 
of leg 2, if applicable.
ISO 8601
YYYY-MM-DD, based on UTC.
    
24-15

## Page 46

Row no. Data Element Name Definition of Data Element Format and allowable values IR FX EQ CD CM
Appendix B to the Consultation Paper - List of Proposed Data Elements Data element applicable to asset class
150 Floating rate reset frequency period - Leg 1 Where applicable: time unit associated with the frequency of payments resets, e.g. day, week, month, year or term of the 
stream for the floating rate of leg 1.
Char(4)
Allowable values:
DAIL = Daily
WEEK = Weekly
MNTH = Monthly
YEAR = Yearly
ADHO = Ad hoc which applies when payments are irregular
EXPI = Payment at term
    
151 Floating rate reset frequency period - Leg 2 Where applicable: time unit associated with the frequency of payments resets, e.g. day, week, month, year or term of the 
stream for the floating rate of leg 2.
Char(4)
Allowable values:
DAIL = Daily
WEEK = Weekly
MNTH = Monthly
YEAR = Yearly
ADHO = Ad hoc which applies when payments are irregular
EXPI = Payment at term
    
152 Floating rate reset frequency multiplier - Leg 1 Where applicable: number of time units (as expressed by the payment frequency period) that determines the frequency at 
which periodic payment resets dates occur for the floating rate of leg 1. For example, a transaction with payments occurring 
every two months is represented with a payment frequency period of “MNTH” (monthly) and a payment frequency period 
multiplier of 2.
This data element is not applicable if the payment frequency period is “ADHO”. If payment frequency period is “TERM”, 
then the payment frequency period multiplier is 1. If the payment frequency is intraday, then the payment frequency period 
is “DAIL” and the payment frequency multiplier is 0.
Num(3,0)
Any value greater than or equal to zero.
    
153 Floating rate reset frequency multiplier - Leg 2 Where applicable: number of time units (as expressed by the payment frequency period) that determines the frequency at 
which periodic payment resets dates occur for the floating rate of leg 2. For example, a transaction with payments occurring 
every two months is represented with a payment frequency period of “MNTH” (monthly) and a payment frequency period 
multiplier of 2.
This data element is not applicable if the payment frequency period is “ADHO”. If payment frequency period is “TERM”, 
then the payment frequency period multiplier is 1. If the payment frequency is intraday, then the payment frequency period 
is “DAIL” and the payment frequency multiplier is 0.
Num(3,0)
Any value greater than or equal to zero.
    
154 Index factor The index version factor or percent, expressed as a decimal value, that multiplied by the Notional amount yields the 
notional amount covered by the seller of protection for credit default swap, if applicable.
Num(11,10)
Any value between 0 and 1 (including 0 and 1), expressed as decimal (e.g.0.05 instead of 5%).
    
155 Embedded option type Type of option or optional provision embedded in a contract, if applicable. Char(4)
Allowable values:
MDET = Mandatory early termination
OPET = Optional early termination
CANC = Cancellable
EXTD = Extendible
OTHR = Other
    
156 Initial margin collateral portfolio code If collateral is reported on a portfolio basis, a unique code assigned by the reporting counterparty to the portfolio that tracks 
the aggregate initial margin of a set of open swap transactions, if applicable.
This data element is not applicable if the collateralisation was performed on a transaction level basis, or if there is no 
collateral agreement, or if no collateral is posted or received or if only one collateral portfolio of amounts of margin that 
does not distinguish between margin that is initial margin and margin that is variation margin.
Varchar(52)
Up to 52 alphanumeric characters.
    
157 Portfolio containing non-reportable component 
indicator
If collateral is reported on a portfolio basis, indicator of whether the collateral portfolio includes swap transactions exempt 
from reporting., if applicable.
Boolean
Allowable values:
true: for collateral portfolio contains one or more nonreported transactions; or
false: for collateral portfolio does not contain one or more non-reported transactions
    
158 Variation margin collateral portfolio code If collateral is reported on a portfolio basis, a unique code assigned by the reporting counterparty to the portfolio that tracks 
the aggregate variation margin related to a set of open swap transactions, if applicable.
This data element is not applicable if the collateralisation was performed on a transaction level basis, or if there is no 
collateral agreement, or if no collateral is posted or received or if only one collateral portfolio of amounts of margin that 
does not distinguish between margin that is initial margin and margin that is variation margin.
Varchar(52)
Up to 52 alphanumeric characters.
    
159 Submitting Party In the case where the entity responsible for reporting has delegated the submission of the report to a third party or to the 
other counterparty, this entity has to be identified in this field by a unique code. Otherwise the entity responsible for 
reporting should be identified in this field.
ISO 17442 Legal Entity Identifier (LEI) 
Char(20)
LEI code that is included in the LEI data as published by the Global LEI Foundation (GLEIF, www.gleif.org/).
    
160 Entity responsible for reporting Identification code of the Reporting Party who has the obligation to report the transaction. ISO 17442 Legal Entity Identifier (LEI) 
Char(20)
    
161 Country of the counterparty 2 The code of country where the registered office of the other counterparty is located or country of residence in case that the 
other counterparty is a natural person.
ISO 3166 - 2 character country code     
162 Broker ID If a broker acted as intermediary for the Reporting Entity in relation to the Reportable Transaction, without becoming a 
counterparty to the OTC Derivative the subject of the Reportable Transaction, the current LEI of the broker.
ISO 17442 Legal Entity Identifier (LEI) 
Char(20)
LEI code that is included in the LEI data as published by the Global LEI Foundation (GLEIF, www.gleif.org/).
    
24-16

## Page 47

Row no. Data Element Name Definition of Data Element Format and allowable values IR FX EQ CD CM
Appendix B to the Consultation Paper - List of Proposed Data Elements Data element applicable to asset class
163 Contract type Each reported contract shall be classified according to its type, if applicable. Char(4) 
Allowable values:
CFDS = Financial contracts for difference
FRAS = Forward rate agreements
FUTR = Futures 
FORW = Forwards 
OPTN = Option 
SPDB = Spreadbet 
SWAP = Swap 
SWPT = Swaption 
OTHR = Other
    
164 Asset Class Each reported contract shall be classified according to the asset class it is based on, if applicable. Char(4) 
Allowable values:
CRDT - Credit
CURR - Currency 
EQUI - Equity
INTR - Interest Rate 
COMM - Commodity
    
165 Underlying identification type The type of relevant underlying identifier, if applicable. Char(1)
Allowable values:
I = ISIN
B = Basket
X = Index
    
166 Underlying identification The direct underlying shall be identified by using a unique identification for this underlying based on its type. For Credit 
Default Swaps, the ISIN of the reference obligation should be provided, if applicable.
For underlying identification type I: ISO 6166 ISIN 12 character alphanumeric code 
For underlying identification type X: ISO 6166 ISIN if available
    
167 Name of the underlying index The full name of the underlying index as assigned by the index provider, if applicable. Varchar(50)
Up to 50 alphanumeric characters. Special characters are allowed if they form part of the full name of the index.
    
168 Clearing timestamp Time and date when clearing took place, if applicable. ISO 8601
YYYY-MM-DDThh:mm:ssZ, based on UTC. 
    
169 Delivery type Indicates whether the contract is settled physically or in cash, if applicable. Char(4)
Allowable values:
CASH = Cash
PHYS = Physical 
OPTL = Optional for counterparty or when determined by a third party
    
170 Identifier of the floating rate - Leg 1 Where applicable: an identifier of the interest rates used which are reset at predetermined intervals by reference to a 
market reference rate of leg 1.
If the floating rate has an ISIN, the ISIN code for that rate.     
171 Indicator of the floating rate - Leg 1 An indication of the interest rate of leg 1, where available. Char(4)
The indication of the floating rate index.
ESTR = €STR 
SONA = SONIA 
SOFR = SOFR 
EONA = EONIA
EONS = EONIA SWAP 
EURI = EURIBOR 
EUUS = EURODOLLAR
EUCH = EuroSwiss 
GCFR = GCF REPO 
ISDA = ISDAFIX 
LIBI = LIBID
LIBO = LIBOR 
MAAA = Muni AAA
PFAN = Pfandbriefe 
TIBO = TIBOR 
STBO = STIBOR 
BBSW = BBSW 
JIBA = JIBAR 
BUBO = BUBOR 
CDOR = CDOR 
CIBO = CIBOR 
MOSP = MOSPRIM 
NIBO = NIBOR 
PRBO = PRIBOR 
TLBO = TELBOR 
WIBO = WIBOR
TREA = Treasury 
SWAP = SWAP
FUSW = Future SWAP
EFFR = Effective Federal Funds Rate 
OBFR = Overnight Bank Funding Rate
CZNA = CZEONIA
    
172 Name of the floating rate - Leg 1 The full name of the interest rate as assigned by the index provider of leg 1, if applicable. Varchar(50)
Up to 50 alphanumeric characters. Special characters are allowed if they form part of the full name of the index.
    
173 Floating rate reference period - Leg 1 – time period Time period describing the reference period for the floating rate of leg 1, if applicable. Char(4)
Allowable values:
DAIL = daily
WEEK = weekly 
MNTH = monthly 
YEAR = yearly
ADHO = ad hoc which applies when payments are irregular
EXPI = payment at term
    
174 Floating rate reference period - Leg 1 – multiplier Multiplier of the time period describing the reference period for the floating rate of leg 1, if applicable. Num(3,0)
Any integer value greater than or equal to zero up to 3 numeric characters.
    
24-17

## Page 48

Row no. Data Element Name Definition of Data Element Format and allowable values IR FX EQ CD CM
Appendix B to the Consultation Paper - List of Proposed Data Elements Data element applicable to asset class
175 Identifier of the floating rate - Leg 2 Where applicable: an identifier of the interest rates used which are reset at predetermined intervals by reference to a 
market reference rate of leg 2.
If the floating rate has an ISIN, the ISIN code for that rate.     
176 Indicator of the floating rate - Leg 2 An indication of the interest rate of leg 2, where available. Char(4)
The indication of the floating rate index.
ESTR = €STR 
SONA = SONIA 
SOFR = SOFR 
EONA = EONIA
EONS = EONIA SWAP 
EURI = EURIBOR 
EUUS = EURODOLLAR
EUCH = EuroSwiss 
GCFR = GCF REPO 
ISDA = ISDAFIX 
LIBI = LIBID
LIBO = LIBOR 
MAAA = Muni AAA
PFAN = Pfandbriefe 
TIBO = TIBOR 
STBO = STIBOR 
BBSW = BBSW 
JIBA = JIBAR 
BUBO = BUBOR 
CDOR = CDOR 
CIBO = CIBOR 
MOSP = MOSPRIM 
NIBO = NIBOR 
PRBO = PRIBOR 
TLBO = TELBOR 
WIBO = WIBOR
TREA = Treasury 
SWAP = SWAP
FUSW = Future SWAP
EFFR = Effective Federal Funds Rate 
OBFR = Overnight Bank Funding Rate
CZNA = CZEONIA
    
177 Name of the floating rate - Leg 2 The full name of the interest rate as assigned by the index provider of leg 2, if applicable. Varchar(50)
Up to 50 alphanumeric characters. Special characters are allowed if they form part of the full name of the index.
    
178 Floating rate reference period - Leg 2 – time period Time period describing the reference period for the floating rate of leg 2, if applicable. Char(4)
Allowable values:
DAIL = daily
WEEK = weekly 
MNTH = monthly 
YEAR = yearly
ADHO = ad hoc which applies when payments are irregular
EXPI = payment at term
    
179 Floating rate reference period - Leg 2 – multiplier Multiplier of the time period describing the reference period for the floating rate of leg 2, if applicable. Num(3,0)
Any integer value greater than or equal to zero up to 3 numeric characters.
    
180 Forward exchange rate Forward exchange rate as agreed between the counterparties in the contractual agreement It shall be expressed as a price 
of base currency in the quoted currency, if applicable.
Num(18,13)
Any value greater than zero up to 18 numeric digits including up to 13 decimal places. The decimal mark is not counted as a numeric character. If populated, it shall be represented by a dot.
    
181 Base product Base product as specified in the classification of commodities in Table 4 of the Annex to Implementing Regulation (EU) 
2022/1860.
Only values in the ‘Base product’ column of the classification of commodities derivatives table are allowed.     
182 Sub-product Sub-product as specified in the classification of commodities in Table 4 of the Annex to Implementing Regulation (EU) 
2022/1860.
This field requires a specific base product in field.
Only values in the ‘Sub — product’ column of the classification of commodities
derivatives table are allowed.
    
183 Further sub-product Further sub product as specified in the classification of commodities in Table 4 of the Annex to Implementing Regulation 
(EU) 2022/1860.
This field requires a specific sub product in field.
Only values in the ‘Further sub — product’ of the classification of commodities
derivatives table are allowed.
    
184 Option type Indication as to whether the derivative contract is a call (right to purchase a specific underlying asset) or a put (right to sell 
a specific underlying asset) or whether it cannot be determined whether it is a call or a put at the time of execution of the 
derivative contract, if applicable.
In case of swaptions it shall be:
- “Put”, in case of receiver swaption, in which the buyer has the right to enter into a swap as a fixed-rate receiver.
-“Call”, in case of payer swaption, in which the buyer has the right to enter into a swap as a fixed-rate payer. In case of 
Caps and Floors it shall be:
-“Put”, in case of a Floor.
-“Call”, in case of a Cap.
Char(4)
Allowable values:
PUTO = Put
CALL = Call
OTHR = where it cannot be determined whether it is a call or a put
    
185 Option style Indicates whether the option may be exercised only at a fixed date (European), a series of pre-specified dates (Bermudan) 
or at any time during the life of the contract (American), if applicable.
Char(4)
Allowable values:
AMER = American 
BERM = Bermudan 
EURO = European
    
186 Maturity date of the underlying In case of swaptions, maturity date of the underlying swap, if applicable. ISO 8601
YYYY-MM-DD, based on UTC.
    
187 Seniority Indicates the seniority of the debt security, or debt basket or index underlying a derivative, if applicable. Char(4)
Allowable values:
SNDB = Senior, such as Senior Unsecured Debt (Corporate/Financial), Foreign Currency Sovereign Debt (Government)
SBOD = Subordinated, such as Subordinated or Lower Tier 2 Debt (Banks), Junior Subordinated or Upper Tier 2 Debt (Banks),
OTHR = Other, such as Preference Shares or Tier 1 Capital (Banks) or other credit derivatives
    
24-18

## Page 49

Row no. Data Element Name Definition of Data Element Format and allowable values IR FX EQ CD CM
Appendix B to the Consultation Paper - List of Proposed Data Elements Data element applicable to asset class
188 Reference entity Identification of the underlying reference entity, if applicable. ISO 3166: 2 character country code,
or
ISO 3166-2: 2 character country code followed by dash "-" and up to 3 alphanumeric character country subdivision code,
or
ISO 17442 Legal Entity Identifier (LEI) 20 alphanumeric character code
    
189 Series The series number of the composition of the index if applicable. Num(5,0)
Any integer value greater than or equal to zero up to 5 numeric characters.
    
190 Series Version A new version of a series is issued if one of the constituents defaults and the index has to be reweighted to account for the 
new number of total constituents within the index, if applicable.
Num(5,0)
Any integer value greater than or equal to zero up to 5 numeric characters.
    
191 Indicator of the underlying index An indication of the underlying index, where available. Char(4)
The indication of the floating rate index. 
ESTR = €STR 
SONA = SONIA 
SOFR = SOFR 
EONA = EONIA
EONS = EONIA SWAP 
EURI = EURIBOR 
EUUS = EURODOLLAR
EUCH = EuroSwiss 
GCFR = GCF REPO 
ISDA = ISDAFIX 
LIBI = LIBID
LIBO = LIBOR 
MAAA = Muni AAA
PFAN = Pfandbriefe 
TIBO = TIBOR 
STBO = STIBOR 
BBSW = BBSW 
JIBA = JIBAR 
BUBO = BUBOR 
CDOR = CDOR 
CIBO = CIBOR 
MOSP = MOSPRIM 
NIBO = NIBOR 
PRBO = PRIBOR 
TLBO = TELBOR 
WIBO = WIBOR
TREA = Treasury 
SWAP = SWAP
FUSW = Future SWAP
EFFR = Effective Federal Funds Rate 
OBFR = Overnight Bank Funding Rate 
CZNA = CZEONIA
    
192 Collateral timestamp Date and time as of which the values of the margins are reported, if applicable. ISO 8601
YYYY-MM-DDThh:mm:ssZ, based on UTC. 
    
193 Trading capacity Identifies the trading capacity of the seller. Allowable values:
AGEN = Agent (Trading as Agent on behalf of a customer)
PRIN = Principal (Trading as Principal)
    
194 Swap Link ID A linking element used to link the Near Leg and Far Leg of an FX Swap, if applicable. Varchar(100)     
195 Trader location Location of the trading desk or trader responsible for the decision of entering into or execution of the transaction. ISO 3166 - 2 character country code     
196 Booking location Location of the trade party or the branch/office of the trade party to which the transaction is booked. ISO 3166 - 2 character country code     
197 Intragroup Indicates whether the contract was entered into as an intragroup transaction.
Usage: When absent, default value is false.
Boolean
Allowable values:
true : contract entered into as an intragroup transaction
false : contract not entered into as an intragroup transaction
    
198 Nature of the counterparty 1 Indicate if the counterparty 1 is a CCP, a financial, non-financial counterparty or other type of counterparty. F = Financial Counterparty
N = Non-Financial Counterparty 
C = Central Counterparty
O = Other
    
199 Nature of the counterparty 2 Indicate if the counterparty 2 is a CCP, a financial, non-financial counterparty or other type of counterparty. F = Financial Counterparty
N = Non-Financial Counterparty 
C = Central Counterparty
O = Other
    
200 Non-standardized term indicator indicates whether the derivative transaction has one or more additional terms or provisions that materially affect the price of 
the transaction.
Boolean
Allowable values:
true
false
    
201 Secondary transaction identifier For internal client code, if applicable. Subject to ISO message standard     
202 Lower or only barrier To facilitate the reporting of strike values for barrier options, if applicable. Subject to ISO message standard     
203 Upper barrier To facilitate the reporting of strike values for barrier options, if applicable. Subject to ISO message standard     
204 Business message identifier An unique user file reference assigned by the Submitting Party on request file Varchar(35)     
24-19

## Page 50

Row no. Data Element Name Definition of Data Element Format and allowable values IR FX EQ CD CM
Appendix B to the Consultation Paper - List of Proposed Data Elements Data element applicable to asset class
205 Message definition identifier The Message Definition Identifier of the Business Message instance with which this Business Application Header instance 
is associated.
Varchar(35)
Allowable values are:
auth.108.001.01_HKMAUG_DATMDA_1.0.0
auth.030.001.03_HKMAUG_DATTAR_1.0.0
    
206 Business service To indicate whether the request is used for Reporting service. Varchar(35)
Allowable values are:
Trade
Valuation 
    
207 Creation date Date and time when this Business Message (header) was created. ISO 8601
YYYY-MM-DDThh:mm:ssZ, based on UTC.
    
208 Number records Indicates the number of trade action in the request file. Num(4,0)
Any value greater than zero.
    
209 Technical record identification Unique identifier of a trade action used as part of error management and status advice message. Varchar(140)     
24-20

## Page 51

25
Appendix C – Jurisdictions in the SFC designated list gazetted on 7 
July 2015
FSB member jurisdictions Non-FSB member jurisdictions
1. Argentina 1. Algeria
2. France 2. Austria
3. India 3. Bahrain
4. Indonesia 4. Belgium
5. People’s Republic of China 5. Hungary
6. Singapore 6. Israel
7. South Korea 7. Luxembourg
8. Switzerland 8. Pakistan
9. Samoa
10. Taiwan, China
