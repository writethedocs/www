:og:image: https://www.writethedocs.org/_static/logo-opengraph.png

.. post:: June 02, 2026
  :tags: newsletter

#####################################
Write the Docs Newsletter – June 2026
#####################################

Salutations, documentarians. I'm writing to you from a trip up to Estonia, where the days are longer than I've experienced in a while. The way the light stretches on makes it seem possible to accomplish more in a single day. It brings a sense of optimism that maybe we can solve more problems, whether they are big, global ones or just finally fixing those outdated articles I've been meaning to get to. I hope you can manage to find time to fix some problems too.

The year will also stretch on for a while more, so we have three larger events coming up. First is `Write the Docs Kenya <https://www.meetup.com/wtd-kenya/events/314376384/>`__ on 8 August, then `Write the Docs Berlin </conf/berlin/2026/>`__ on 6--8 September, and then Write the Docs Melbourne on 3--4 December. I hope you can make it to at least one.

This month we have articles on dealing with people sharing unofficial docs, whether to flag content that had an assist from an LLM, some thoughts about whether docs can ever be too comprehensive, and some ideas on how AI search can be done well. Enjoy!

------------------------
Dealing with shadow docs
------------------------

A recent `#ai channel <https://writethedocs.slack.com/archives/C1NEAD7D4>`__ discussion focussed on a growing problem of "shadow documentation": where non-documentation teams -- such as Support, Sales, or Customer Success -- use AI tools to generate PDF files and guides for customers from official documentation. (This has been done in the past without AI involvement.) Participants agreed that the issue is becoming more common as AI tools make it easy to generate customized onboarding, deployment, or troubleshooting materials. 

Documentarians are primarily concerned with the accuracy, version, supportability, and `governance <https://en.wikipedia.org/wiki/Governance>`__ of these docs. AI-generated documents may become outdated quickly because of a lack of oversight and may contain invalid, hallucinated, or unsupported functionality based on the AI prompts used.

Shadow docs (whether AI-generated or not) often circulate without the documentation team’s knowledge. This can be a governance issue. Also, non-docs teams may create unofficial content when official documentation is incomplete, difficult to use, or insufficiently tailored to specific customer workflows. Some non-docs teams create unofficial docs because they face customer pressure and operational realities. But even with robust official documentation, if someone receives shadow docs, they're unknowingly using something that may be out of date instead of accessing the up-to-date official documentation.

The discussion suggested different strategies for handling the problem of shadow docs.

* **A governance-focused approach:** Clarifies ownership and accountability for unofficial content. The documentation team should know about any shadow docs to vet them properly and make sure to redirect the shadow docs to the maintained content. Alternatively, encourage teams to share URLs to maintained content rather than distributing AI-generated docs.
* **A partnership model:** Incorporates field-generated knowledge back into the official documentation set. AI-generated content can provide value when used internally for improving official documentation if the output is reviewed and validated. The documentation team may need to put into place procedures for making verified "rogue" content accessible to other teams.
* **Doc customization:** Adds customized content into the official documentation -- such as curated collections of official topics.

Shadow documentation can be an organizational challenge that requires balancing governance, usability, customer needs, and evolving AI-generated content.

See more Write the Docs resources about `working across roles </topics/#working-across-roles>`__.

------------------------------------
Flagging AI content in documentation
------------------------------------

Should you flag AI-generated content in internal or external docs? It’s tempting to reach for a label, but is such a label actually useful? Members of the WTD community discussed the different angles in Slack this month.

AI has given every department the ability to generate 50 pages of content overnight and drop it in the company intranet. Management of internal documentation often lands on the docs team, officially or not. Tools such as Confluence and SharePoint make labeling easy, so it’s tempting to identify AI-generated content to give a heads-up to the reader. The writer’s impulse is understandable: this content hasn’t been reviewed by a human yet, read with caution.

But an "AI-generated" label might not convey the meaning you intend. Technical readers may already expect AI authorship. And if management has encouraged AI use across the organization, they may read the label as a positive marker of adoption. To differentiate human-reviewed content from AI noise, it may be better to add a "needs review" label or, better still, tighten the publishing workflow itself to require sign-off before content goes live.

With user-facing documentation, the impulse to label human-reviewed AI content is about trust. Writers want to be transparent and disclosure feels like the honest thing to do. Here too, the label may not land as intended.

Many readers are skeptical of AI, so labelling human-reviewed AI content may undermine confidence rather than build it. For others, that same label might do the reverse -- one contributor speculated that AI-generated code samples might actually inspire more trust than human-written ones. On the legal side, the question of whether we’re obliged to disclose was raised, though the general view was that human-written content can be just as wrong as AI-generated content. Ultimately, people come to your documentation to solve a problem. The main concern for users is not "How was this created?", but "Is it useful?".

This is a moment in time. The labeling question may look very different in a few years. If you do use labels, think carefully about what job you want them to do and how they will land with your audience and your organization. In both cases, a human in the loop remains a standard worth sticking to.

See more Write the Docs resources about `AI and LLMs </topics/#ai-and-llms>`__.

------------------------------
Can docs be too comprehensive?
------------------------------

A recent discussion of the question of whether docs can ever be too comprehensive was sparked by feedback to a documentarian that a particular guide was too comprehensive for most users, since the full document was only necessary for a small percentage of use cases. The central question was how to address this -- whether through a separate "light" version of the guide or some other approach.

Several structural solutions emerged as the most practical responses. One such solution was breaking content into smaller, meaningful chunks, including separate pages when practical. Others mentioned using progressive disclosure, where readers are shown the content in a simple version and enabled to drill into detail as needed. Separating content by user role or task (or persona) was also suggested, particularly for audiences with distinct needs, such as admins versus end users.

There was a brief debate about whether documentation can ever truly be "too comprehensive". Some held that gaps are always worse than over-documentation and that the real problem lies in how the content is presented rather than how much there is. Others countered that overloading users prevents them from finding a clear path from where they are to where they want to be –- if they see all the content and feel overwhelmed, they may never get the information they were seeking.

The core challenge may be delivering the right content to the right persona at the right time. This may mean creating a quick-start guide for most users while preserving the full details for those who need it. Think carefully about how to structure and filter your content to best match your audience's needs.

See more Write the Docs resources about `writing doc sets </topics/#writing-doc-sets>`__.

----------------
From our sponsor
----------------

This month’s newsletter is sponsored by `Document360 <https://document360.com/request-demo/?utm_medium=writethedocs&utm_source=nlsponsorship>`__.

.. image:: /_static/img/sponsors/document360.png
  :align: center
  :width: 50%
  :target: https://document360.com/request-demo/?utm_medium=writethedocs&utm_source=nlsponsorship
  :alt: Document360 logo

Most days, the writing isn't the hard part. It's everything around it like the outdated articles, the missing context from engineering, the same reader questions arriving in different shapes. The craft gets squeezed into the gaps.

Document360's AI is built to fill those gaps. A writing agent that turns a prompt or a video into a structured draft. A search that knows what a reader actually means. A chatbot that handles repeated questions. A connection to the LLMs your team uses, so your docs are cited, not guessed at.

It's an assistant. Not a replacement. The voice stays yours. `Talk to our specialists <https://document360.com/request-demo/?utm_medium=writethedocs&utm_source=nlsponsorship>`__.

*Interested in sponsoring the newsletter? Take a look at our* `sponsorship prospectus </sponsorship/newsletter/>`__.


------------------
Featured job posts
------------------

`Technical Writer, AI Lead <https://jobs.ashbyhq.com/Pear-VC/2f350d00-ecac-4764-98ae-4533b1c398a8>`__, Paxos Health - *NYC or Toronto (Hybrid)*
Note: The interview process is moving forward soon, so apply as soon as practical.

*Interested in promoting your open position? See our* `job posting sponsorship </sponsorship/jobs/>`__ *for more details.*

------------------------
Write the Docs resources
------------------------

Write the Docs offers lots of valuable resources related to documentation. See all of the Write the Docs `learning resources </about/learning-resources/>`__. To discuss any of these ideas or others related to documentation, join the conversation in the `Write the Docs Slack community </slack/>`__ in one of the many `channels </slack/#channel-guide>`__.

----------------
Events coming up
----------------

- 10 Jun, 18:30 CEST (Munich, Germany): `WTD Munich: Rethinking Technical Writing in the Age of AI <https://www.meetup.com/write-the-docs-munich/events/314541165/>`__
- 12 Jun, 08:30 EDT (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/311760891/>`__
- 16 Jun, 19:00 MDT (Calgary, Canada): `Breaking Down Silos with The 4X Method™ <https://www.meetup.com/wtd-calgary/events/312192098/>`__
- 18 Jun, 18:30 CEST (Barcelona, Spain): `Collaborating with OSS projects: OpenTelemetry Docs <https://www.meetup.com/write-the-docs-barcelona/events/314193667/>`__
- 18 Jun, 18:30 BST (London, United Kingdom): `Rock the Docs: Applying music theory and band dynamics to technical writing <https://www.meetup.com/write-the-docs-london/events/313761436/>`__
- 25 Jun, 18:30 EDT (Pittsburgh, USA): `Navigating the Job Market as a Tech Writer in 2026 <https://www.meetup.com/write-the-docs-pittsburgh/events/314865661/>`__
- 25 Jun, 17:00 PDT (San Francisco, USA): `The Modern Technical Writer’s Guide to Docs-as-Code <https://www.meetup.com/write-the-docs-bay-area/events/314892684/>`__
- 26 Jun, 08:30 EDT (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/313233193/>`__
- 10 Jul, 08:30 EDT (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/313625241/>`__
