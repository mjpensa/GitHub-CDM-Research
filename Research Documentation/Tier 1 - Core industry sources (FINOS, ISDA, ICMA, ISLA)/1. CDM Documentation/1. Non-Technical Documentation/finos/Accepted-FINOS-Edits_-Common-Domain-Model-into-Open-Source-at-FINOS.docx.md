# Accepted FINOS Edits  Common Domain Model into Open Source at FINOS.docx

*Converted from: Accepted-FINOS-Edits_-Common-Domain-Model-into-Open-Source-at-FINOS.docx.pdf*

---

## Page 1

Common Domain Model
becoming
Open Source @ FINOS
Contents
CDM Then and Now 3
CDM Becomes Open Source 3
Migration 4
Contribution Opportunities 4
Governance 4
Meetings 5
Tools & Platforms 5
Rosetta 5
Legend 5
Other Tools 5
Contribution Guidelines & Best Practices 5
Contribution 5
Licensing 6
CDM Implementation 6
Frequently Asked Questions 6
Do I have to be a member of the TAs to contribute to the CDM? 6
Do I have to be a member of FINOS to contribute to the CDM? 6
Do I have to be a member of the TAs to attend a CDM WG? 6
Do I have to be a member of FINOS to attend a CDM WG? 6
What is the CDM Steering Working Group? 6
What is the CDM Contribution Review Working Group? 7
Who is on the CDM Steering Working Group/ CDM Contribution Review Working Group? 7
How will other subject specific working groups be managed at FINOS? 7

## Page 2

How do I/does my firm become a member of the CDM Steering Working Group, CDM
Contribution Review Working Group or other CDM working groups? 7
Who are the Maintainers of the CDM? 8
What other roles are there for participants in CDM? 8
How are the Maintainers appointed? 8
How can I view or download the model? 8
How can I contribute to the CDM? 8
Other key notes and links: 9
DRAFT MEMO: To CDM Working Groups & Committees re: Community License Agreement (CLA) 10

## Page 3

CDM Then and Now
ISDA began the "ISDA CDM" project in 2017 with initial research, cost benefit analysis, surveying of
members and publishing a paper which laid out the possibilities for a common domain model for
derivatives markets. In June 2018 version 1.0 was released to ISDA members and in March 2019
version 2.0 was released and made available to all market participants. In 2021, ISDA, ISLA and ICMA
signed a memorandum of understanding to work together on the development of the CDM which
was the culmination of initial work by those associations to develop initial models for their respective
markets. In 2022, the associations sought a third party home for CDM, and this search was successful
in appointing FINOS as the new open source home of the CDM.
CDM Becomes Open Source
The CDM (Common Domain Model) is in its physical form a collection of source code (Rosetta files,
JSON files, etc.) that has until recently been version-controlled (and strictly isolated) in a
REGnosys-maintained git repository connected to the Rosetta platform. In becoming open source,
the CDM source code has transitioned to a new home in GitHub and become open for contribution
in a publicly accessible git repository, maintained by FINOS, the “Fintech Open-Source Foundation”.
Contribution is possible independent of platform using standard best practices, editing within git,
using the Rosetta platform (and Legend when version is upgraded) or a tool of your choice.

## Page 4

Migration
Transfer has taken place on February 14th and its full completion (expected 2-3 weeks later) will be
made known to the community via FINOS, ICMA, ISLA and ISDA channels. However, the source code
is now open source at this address: https://github.com/finos/common-domain-model
Please log in to GitHub (creating an account if you don’t already have one) and follow the link above,
“Star” the project as a favourite and you can also choose to “Watch” the project repository so that
you are updated on any changes, issues, pull requests or releases.
Contribution Opportunities
Participants to the CDM will in future be able to propose changes to the source code in the
FINOS-maintained CDM Repo. This contribution functionality has been sought-after by the technical
community using CDM and will now be possible using standard code contribution practices with the
open-source repo, as part of the repo transition to FINOS.
Governance
As previously discussed, and presented to the CDM Architecture and Review Committee, the
governance structure will change to accommodate and cater for the expanding community of
contributors and maintainers and the wider adoption of the Common Domain Model as a whole. A
greater involvement from the existing community will be possible and is greatly encouraged.

## Page 5

Meetings
Per above governance structure there will be new working groups replacing the existing ones which
ISDA has facilitated. The responsibilities of the ARC will migrate to the Contribution Review
Committee and Technology Architecture working group.
For more information see the FAQs (click below)
What is the CDM Steering Working Group?
What is the CDM Contribution Review Working Group?
Tools & Platforms
As mentioned, in becoming open source, contributions to the CDM can follow several channels
including existing ones.
Rosetta
The Rosetta platform currently provides contribution functionality that links to git version control
behind the scenes. In future, the platform will continue to provide within its UI this initial layer of
abstraction to git with the user reviewing and contributing changes made in Rosetta from within the
platform, then submitting a Pull Request to the FINOS ‘CDM Repo” from within GitHub, using their
GitHub credentials, with guidance and support from maintainers.
Legend
Previously certain aspects of the CDM have been developed using the Legend platform which is an
open source project at FINOS too. It is expected that the version of CDM on Legend will be upgraded
soon so that developers interested in contributing to CDM via the Legend platform will be able to do
so.
Other Tools
The migration to open source opens up the CDM ecosystem to new possibilities for participants in
using their own tools and platforms as well as building new ones. Opening the CDM GitHub
repository and Maven Central published binaries being available also will make this a reality.
Contribution Guidelines & Best Practices
Contribution
Previous code contributors to CDM via Rosetta can continue to contribute in the same manner that
they have before. There will be an additional step for where the participant will be asked to create
the Pull Request in GitHub to ensure that they are recognised for their efforts. All instructions will be
made clear and contributors will be guided through the process.
For further detail on general standard contribution practices directly please see link:
https://community.finos.org/docs/finos-contributors-cheatsheet

## Page 6

Licensing
It is important to note that participants in the CDM project (via Rosetta, directly or other channels)
will need to have signed a Contribution Licence Agreement (CLA) or be covered by one for their
organisation – details on CLA and EasyCLA the management system that FINOS/Linux Foundation
provides can be found below.
More details and instructions will be provided separately on how to set yourself up or you can reach
out to FINOS or Trade Association CDM Team contacts who will be happy to help.
https://docs.linuxfoundation.org/lfx/easycla
CDM Implementation
With regard to implementers of CDM, the main use case for CDM implementors is via the Java
distribution, which is compiled from the Rosetta files to create software that is then distributed to
users via binary mechanisms. Currently, it is being distributed through a product called Artifactory (a
REGnosys account), but in the future it will be available through Maven Central. To use the CDM,
users will download the pre-built Java artifacts from Maven Central. This is another new
development which CDM implementers have been requesting that we can deliver with the CDM at
FINOS.
Frequently Asked Questions
“TAs” = ISDA, ISLA and ICMA, the key sponsoring trade association of CDM to date.
Do I have to be a member of the TAs to contribute to the CDM?
No, as with any open source project contributions can come from anyone. However, realistically key
investment in time and resources to develop designs and make contributions should persist to be
from trade associations, their technology partners and firms implementing CDM who have
contributed to date.
Do I have to be a member of FINOS to contribute to the CDM?
No. FINOS membership is required to set the course and have input to the development of FINOS as
an organisation.
Do I have to be a member of the TAs to attend a CDM WG?
No. The working groups will be open forums for anyone interested in the topic the working group is
discussing to participate.
Do I have to be a member of FINOS to attend a CDM WG?
No.
What is the CDM Steering Working Group?
This group will take the place, roles and responsibilities of the current CDM Executive Committee and
parts of the current CDM Architecture and Review Committee. It will meet quarterly at a minimum.
Setting the roadmap and agenda for CDM development - it will carry out function of

## Page 7

o reviewing and approving roadmaps for CDM (initially each of the TAs will have areas
of development they expect to work on),
o approving formation of new working groups to develop CDM, and
o approving major version (“stable”) releases of CDM.
What is the CDM Contribution Review Working Group?
This group will take the place, roles and responsibilities of the current CDM Architecture and Review
Committee. It will meet every two weeks.
Reviewing contributions from other CDM working groups or otherwise and approving them - it will
carry out function of
o reviewing and approving roadmaps Pull Requests which are contributed from
working group development or otherwise,
o ensuring contributions adhere to CDM design principles and are compatible with
other parts of CDM, and
o suggesting milestones for major version (“stable”) releases of CDM to the CDM
Steering Working Group.
Who is on the CDM Steering Working Group/ CDM Contribution Review
Working Group?
It should be noted that meetings at FINOS are not closed and anyone may attend. Transparency is a
key principle in the future governance of CDM at FINOS.
Initially, the participants in the CDM Steering Working Group are expected to be a selection of senior
TA staff meeting to coordinate roadmaps and share plans for CDM development, and carry out stated
functions of the working group.
Initially, the participants in the CDM Contribution Review Working Group are expected to be a
selection of TA staff, technology partners, and present active members of CDM working groups and
committees. This working group will be the forum where CDM maintainers discuss and approve
changes to CDM.
How will other subject specific working groups be managed at FINOS?
Working groups which develop CDM components such as the Structured Products Working Group
and CDM Collateral working groups will continue or be migrated to FINOS. These and any other new
working groups approved by the CDM Steering Working Group will be the primary place for
development and discussion of CDM design and output of these working groups will be the pull
requests to merge proposed changes to CDM into the model, subject to approval by maintainers at
the CDM Contribution Review Working Group.
How do I/does my firm become a member of the CDM Steering Working
Group, CDM Contribution Review Working Group or other CDM working
groups?
A memo (or series of memos) will be sent to all CDM working groups with information presented
today plus information on how to join the new groups and get necessary calendar invitations to
ensure you can continue to be an active participant in the development of CDM.

## Page 8

Who are the Maintainers of the CDM?
The maintainers of the CDM project code repository are a group of TA staff and their technology
partners who have been involved in management and maintenance of CDM to date.
https://github.com/orgs/finos/teams/cdm-maintainers/members
What other roles are there for participants in CDM?
(The content below can be found at this link:
https://community.finos.org/docs/finos-maintainers-cheatsheet )
Each FINOS project and SIG has a community of participants, also referred to as "editors",
and maintainers.
Participants are those that have made Contributions to the Working Group subject to the Community
Specification License.
A maintainer is a contributor who, by virtue of their contribution history, has been given write
access to project repositories and may approve and merge contributions to the project.
FINOS Standards projects can also have editors.
How are the Maintainers appointed?
By agreement of the current set of maintainers. A logical evolution of the CDM governance in the
open source would be for a broader set of maintainers be appointed in time.
How can I view or download the model?
Current access points to CDM will persist (e.g. Rosetta and CDM Portal) additionally the CDM GitHub
repository is now open publicly. LEGEND is expected to have the CDM version upgraded in the near
future so that will also be available as a modelling platform too.
How can I contribute to the CDM?
Contributions to the CDM are and will be continually sought in the form of contributions to design
discussion and subject matter expertise and provision of test data samples and examples which can
illustrate and validate use cases and designed solutions. The working groups will welcome your
continued participation in those discussions.
With regard to the contribution of code changes to CDM by individuals (who may be contributing
code on behalf or as a result of a working group design), FINOS has extensive information which can
be found here: https://community.finos.org/docs/finos-contributors-cheatsheet/
One important point of note is that a participant will need to have signed a Community License
Agreement – this may be centrally managed by your firm and to continue contributing to the CDM
code you will need to be added to a corporate CLA participant list – detailed information will be
provided in forthcoming memo(s).
https://docs.linuxfoundation.org/lfx/easycla
Other key notes and links:
o FINOS meetings will take place on Tuesdays at a similar time to the present Architecture and
Review Committee – the specific working group that will meet will be alternating

## Page 9

o Tuesday March 14th 2023 will be the first CDM working group at FINOS: A joint session of
the CDM Steering & CDM Contribution Review Working Groups – to
instantiate governance structure working groups and affirm the roadmap of development
expected by the TAs (previously presented to ARC by ISLA, ICMA and ISDA)
o The FINOS Financial Objects Special Interests Group is another notable forum for wider
discussion of data topics which may eventually result in development in CDM or CDM
integration with other standards – and members are invited to consider this forum for
discussion of topics they would like to discuss.
o You can join any FINOS working group by clicking on a meeting in the FINOS Community
Calendar https://www.finos.org/finos-community-calendar
o To subscribe to the CDM mailing lists you can email cdm+subscribe@lists.finos.org
o Reminder for ISDA members: as well as ISDA Digital Regulatory Reporting (DRR) models,
certain legal documentation and other ISDA specific model content has not been made open
source in this CDM transition project - when changes or projects are underway to further
enhance this content ISDA members will be alerted separately.

## Page 10

DRAFT MEMO: To CDM Working Groups & Committees re:
Contributor License Agreement (CLA)
Dear CDM Community,
As you may be aware we have completed the code transfer of CDM to FINOS. It is important to
understand the role of the FINOS Contributor License Agreement (CLA), what it is used for and what
is expected from each CDM participant in order to continue their contribution work.
To be clear, this pertains to those who intend to become participants in the CDM project and create
pull requests against the CDM repository at FINOS – we encourage all of the CDM community to
review this process and check your corporate status internally and start the process of becoming a
FINOS CLA covered participant.
The FINOS CLA defines the terms under which intellectual property has been contributed. Every
individual who wants to make a contribution to participate in a FINOS hosted standards project must
formally enroll as a participant using the Community Specification License (CSL) , which is available
for firms (Corporate CLA) and individuals (Individual CLA). By enforcing participants to be covered
by a CLA, we protect consumers from having legal disputes around intellectual property.
The Linux Foundation provides a framework called EasyCLA, which a) flags contributions that are
submitted by participants not covered by CLA and b) simplifies the onboarding and signature of
CLAs as firms or individuals.
Many organisations who are members of ICMA, ISDA and ISLA are already setup with Corporate
CLA on EasyCLA and a CDM contributor may just need to be added to the list under their
organisation.
Organisations who want to onboard their employees on EasyCLA can follow these simple steps:
1. Access https://organization.lfx.linuxfoundation.org and add or manage your organization;
you'll need to have an LF ID, the page will guide you through the profile creation, if needed.
2. As soon as you are in front of your Organisation landing page in EasyCLA, you can search
for the FINOS (The Fintech Open Source foundation) project (in the left sidebar) and define
one or more CLA Managers, individuals within the organization who have the authority to
add or remove employees from the list of approved contributors.
Any employee who submits a Pull Request via GitHub on the CDM repository will either be
identified by the EasyCLA bot (and the PR will be green-flagged accordingly) or flagged as "Not
Covered", reporting instructions on how to a) define her/his affiliation and b) notify the CLA Manager
of the employer to add the contributor to the approved list.
FINOS have directed us to an interesting video on Youtube that can help understand how the process
works, which can hopefully provide a clearer overview of the tool. Alternatively, please click on the
following link to find out more
https://docs.linuxfoundation.org/lfx/easycla and/or
https://github.com/finos/standards-project-blueprint/blob/master/governance-documents/Getting%20S
tarted.md#best-practices
If you have any questions regarding the onboarding process or any other query relating to the code
transfer of CDM to FINOS please email cdminfo@isda.org.
Many thanks,

## Page 11

CDM Team
