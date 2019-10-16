Introducing Write the Docs Enhancement Proposals
================================================

Write the Docs has been growing each year for the past 7,
and the scope of the community has expanded dramatically.
We started with a single conference,
and now we have multiple conferences,
over 50 meetups around the world,
multiple online spaces,
and many other ongoing projects.

We have often followed open source in our approach to things,
keeping a loose governance model and mostly letting the work speak for itself.
However,
we've been noticing a number of growing pains with this approach.
It makes it much harder for new people to understand and join the community in leadership positions,
since they don't understand how the community actually works.
Even folks doing a lot of work in the community are often lost or confused when it comes to other ongoing projects.

All organizations have power structures,
some are just not documented. [#]_
Instead of trying to reinvent the wheel,
we've once again taken an idea from the open source ecosystem:
Write the Docs Enhancement Proposals,
or WEP's.

What is a Write the Docs Enhancement Proposal (WEP)
---------------------------------------------------

WEP's are a formalized process for making major policy changes in the community.
Previously there was fuzzy consensus on a Slack channel or at a conference that defined our governance.
Going forward, there will be a written record that people have had time to review and comment on.
Importantly, 
there will also be records of the conversation that lead to a change.

We hope that WEP's will make it explicit how major changes are made inside the community.
New contributors can propose them with a well-defined process,
but can also see WEP's proposed by existing contributors.
WEP's are the first step towards having a more open and defined model for governance,
but certainly not the last.
All further governance changes are planned to go through the WEP process,
so it is truly foundational for ongoing work on how the community is managed.

What is the WEP process?
------------------------

The WEP process is defined in `WEP0`_,
the first ever WEP.
The process is currently undergoing review,
following the draft WEP process.
This is a bit circular,
but we hope that it will showcase how the process works as we adopt it.

The high-level overview of the WEP process is as follows,
from the perspective of someone proposing a WEP:

* Talk to people about your idea, and get feedback from other community members
* Draft and submit a Pull Request on the WEP GitHub Repository, it is now a **draft**
* The **WEP team** then reviews the Draft WEP to make sure it passes a few tests:
    * Is the WEP well-formed? Does it have all the required sections?
    * Is the WEP specific enough that the outcome of approving it is clear?
    * Is the WEP on-topic for the community?
* After the WEP team accepts the draft, it is now **ready-for-discussion**.
* The WEP team then sets a deadline for discussion, currently 30 days, for community feedback and review
* Once the WEP is **ready-for-discussion** and has a deadline, the Core Ops team announce the WEP in a few defined channels, where interested community members can subscribe
    * The ``WEP-announcements`` Slack channel 
    * The ``WEP-announcements`` Email list
* During this month-long period, as there is feedback, the WEP is updated with any changes, and the community works towards a consensus on a path forward
* At the deadline, the Core Ops team determines if consensus has been reached
    * If there is consensus, the WEP is **Accepted**, it will be implemented as specified
    * If there is no consensus, the WEP is either **Rejected** or **Extended** for another month. Extension is available when it seems further activitiy could lead to consensus.
* Once the WEP decision is made, another announcement is sent to the defined announcement channels

If you want to understand the full policy,
we invite you to review and comment on `WEP0`_.
This is a new process,
but we hope it will start to address questions of how change happens in the community. 
 

.. [#]: A great read if you haven't already: https://www.jofreeman.com/joreen/tyranny.htm

