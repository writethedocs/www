.. post:: Oct 30, 2019
   :tags: governance, wep, weps

Introducing Write the Docs Enhancement Proposals
================================================

Write the Docs began seven years ago with a single conference.  
It has now grown to multiple conferences worldwide,
over 50 international meetups,
and `many other projects`_.

We have often followed the open source philosophy in our community practices,
keeping a loose governance model and mostly letting the work speak for itself.
However,
we've been experiencing a number of growing pains with this approach.
A loosely defined process makes it much harder for new people to understand and join the community in leadership positions,
since they don't understand how the community actually works.
Even folks doing a lot of work in the community are often lost or confused when it comes to projects they aren't directly involved with.

All organizations have power structures,
some are just not documented. [#]_
Instead of trying to reinvent the wheel,
we've once again taken an idea from the open source ecosystem:
Write the Docs Enhancement Proposals,
or WEPs.

What is a Write the Docs Enhancement Proposal (WEP)
---------------------------------------------------

The WEP system is a formalized process for making major policy changes in the community.
Previously, our governance was usually defined with some kind of fuzzy consensus on a Slack channel or a meeting at a conference.
Going forward, we want to establish a written record that people have time to review and comment on.
Importantly, 
there will also be records of the conversation that lead to a change.

We hope that WEPs will make the process of making major changes inside the community more explicit and collaborative.
Any contributors can propose WEPs with a well-defined process,
and the whole community can follow the process of proposing and implementing WEPs.
WEPs are the first major step towards having a more open and defined model for governance,
but certainly not the last.
All further governance changes are planned to go through the WEP process,
so it is truly foundational for future improvements to our community management processes.

What is the WEP process?
------------------------

The WEP process is defined in `WEP0`_,
the first ever WEP.
WEP0 itself is currently ready for review,
following the draft WEP process.
This might appear circular at first glance,
but we hope that it will showcase how the process works as we adopt it.

The high-level overview of the WEP process is as follows,
from the perspective of someone proposing a WEP:

#. Talk to people about your idea, and get feedback from other community members
#. Draft and submit a Pull Request on the WEP GitHub Repository, which submits the WEP as a **draft**
#. The **WEP team** then reviews the Draft WEP to make sure it falls within the WEP guidelines:
    * Is the WEP well-formed? Does it have all the required sections?
    * Is the WEP specific enough that the outcome of approving it is clear?
    * Is the proposed change within the scope of the WEP process?
#. After the WEP team accepts the draft, it is now **ready-for-discussion**.
#. The WEP team then sets a deadline for discussion, currently 30 days, for community feedback and review
#. Once the WEP is **ready-for-discussion** and has a deadline, the Core Ops team announce the WEP in a few defined channels, where interested community members can subscribe
    * The ``WEP-announcements`` Slack channel 
    * The ``WEP-announcements`` Email list
#. During this month-long period, the WEP is updated based on incoming feedback, and the community works towards a consensus on the proposed change
#. At the deadline, the Core Ops team determines if consensus has been reached
    * If there is consensus, the WEP is **Accepted**, it will be implemented as specified
    * If there is no consensus, the WEP is either **Rejected** or **Extended** for another month. Extension is available when it seems further activity could lead to consensus.
#. Once the WEP decision is made, another announcement is sent to the defined announcement channels

Get involved
------------

If you want to understand the full policy,
we invite you to review and comment on `WEP0`_.
We also welcome feedback privately via email at support@writethedocs.org if that is more comfortable for you.
This is a new process,
but we hope it will start to address questions of how change happens in the community. 

We hope that you'll take the time to read our proposal and understand how we're changing the process of making changes in the community.
The more engaged folks are with the process,
the better the community will be for everyone.

.. [#] A great read if you haven't already: https://www.jofreeman.com/joreen/tyranny.htm
 
.. _many other projects: https://www.writethedocs.org/#join-the-community
.. _WEP0: https://github.com/writethedocs/weps/pull/1
