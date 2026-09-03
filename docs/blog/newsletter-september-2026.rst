:og:image: https://www.writethedocs.org/_static/logo-opengraph.png

.. post:: September 01, 2026
  :tags: newsletter

##########################################
Write the Docs Newsletter – September 2026
##########################################

Hello and hello, fellow documentarians! Aaron and the rest of the newsletter team are back after our short break (summer for some, winter for another) and ready to fill your inbox with insight from the community.

Speaking of the community, the `Berlin conference is coming starting on Sunday </conf/berlin/2026/>`__, so you still have a little time to get a ticket, whether in-person or virtual. Hope to see you there! Later in the year, the `Australia conference is coming back </conf/australia/2026/>`__, so check that out if the time suits you. If you have ideas to share, the `call for proposals </conf/australia/2026/cfp/>`__ is open until next Friday, so get them in soon. And keep up to date with how the community is running with the `community board's latest quarterly update </blog/2026-Q3-community-board/>`__.

The job market is tough right now, and real-world, accurate salary data is needed more than ever. You can help by filling out the `WTD Documentation Salary Survey for 2026 <https://salary-survey.writethedocs.org/>`__. It's open to anyone working in documentation anywhere in the world - employed, freelance, contract, full-time or part-time, at any level of experience, and even if you're currently between jobs. Everything is anonymous, nothing is shared with any third party, and results are published free for everyone. 

This month marks 10 years since `our first newsletter </blog/newsletter-september-2016/>`__. It's amazing that we've keep going so long. Thanks especially to my predecesssors in the editor role, Kelly O'Brien and Beth Aitman, but also everyone else who has contributed over the years, including Hillary Fraley, Jennifer Rondeau, Claire Lundeby, Royce Cook, Heather Zoppetti, Elle Jones, Kyla del Rosario, Alia Michaels, Felicity Brand, Andrew Williams, and Ane Tröger. It takes a team effort to keep this going, but we have no plans to stop yet!

That's more than enough for an intro, so let's jump into the insights from the community for this month.

--------------------------
How to sustain an OSS tool
--------------------------

Funding open-source software (OSS) is not a new problem. Plenty of projects are key dependencies, widely used and well loved, without any of that translating into money to support their maintainers. AI is exacerbating this problem because building something new is easier than ever. The culture of giving back depends on knowing whose work you're using, but vibe coding is a black box, so you're less likely to be aware of a person behind the code you're building on.

This is a topic that was raised in Slack recently by Joseph Kato, the author and maintainer of `Vale <https://vale.sh/>`__, a popular prose linting tool used by many documentarians. Remove the "Vale" part, and Joseph could be any OSS maintainer speaking about their project. Close to a decade of development and support, with widespread adoption among users but little interest in funding its future from the organizations that depend on it. Meanwhile, startups build commercial products on the work and contribute nothing back. It’s hard to justify investing more effort into the project when the value keeps being captured elsewhere. Joseph told the group he was seriously considering moving to a closed-source model.

Alongside shout-outs about how Vale has changed how documentarians work, community members offered no shortage of ideas. A business source license, dual licensing, relicensing to AGPL, trademarking the name, customer-funded feature development. All valid options, but none a real and complete solution.

Sponsorship is the usual answer. But sponsorship is easier said than done, and for many OSS maintainers the issue goes beyond money. It's about where your time is best spent and whether you own a fair share of what you built. As Joseph said, "There are projects 10x as big that can’t solve this problem."

If you use or rely on OSS, how do you support the maintainers who make it possible? In a postscript to this conversation, Joseph noted he had shipped two releases, launched a new offering (`Vale CMS <https://cms.vale.sh/>`__), and found three sponsors. So there is some hope, but perhaps not yet a completely sustainable model.

See more Write the Docs resources about `documentation testing and quality </topics/#culture-and-community>`__.

---------------------------
Doing unpaid work for a job
---------------------------

A recent discussion in `#career-advice <https://writethedocs.slack.com/archives/C6ADX1YVA>`__ focused on a ongoing problem: Is a writing assignment from a job interview appropriate or not? Not all documentarians rejected writing tests but some did have concerns about the distinction between reasonable skill assessments and free production work. For related concerns, see `a previous newsletter article about extreme take-home tests </blog/newsletter-june-2023/#extreme-take-home-tests>`__.

This particular case involved writing a 1,000+ word article about an actual product launch. Because of the "actual product" focus and the length of the assignment, many cautioned against complying with the assignment and considered this "free work". (This could indicate an employer taking advantage of job candidates in a difficult labor market.)

Several suggested clarifying copyright, publishing, and portfolio rights before submitting the assignment (possibly as a password-protected PDF file with printing and copying disabled). Also of concern was any required non-disclosure agreement (NDA), which might be legally binding.

Because of the current job market, some people made suggestions about "working around" the assignment:

- **Submit existing writing samples**: Ask why they aren't sufficient for an evaluation.
- **Write a portion of the requested article**: Explain the proposed approach on how to finish the assignment.
- **Ask to be paid an agreed upon amount**: The assignment is effectively commissioned work.
- **Secure the right to use the work in a portfolio**: If you decide to complete the assignment for free, let the company know that this is a portfolio piece for gaining employment. (In an interview, there’s no guarantee of employment.)
- **Treat the assignment as a first paid assignment**: If this is for a contract position, a candidate could propose a reduced rate for this first, trial assignment.

In general, lengthy take-home assignments are problematic when they go from evaluating writing ability to producing content the employer can use. Candidates may decide the risk is worthwhile depending on how valuable the opportunity is to them. Don’t refuse every assignment, but establish boundaries (such as compensation, copyright, and portfolio use) before doing substantial work.

See more Write the Docs resources about `getting hired </topics/#getting-hired>`__.

-------------------------------------
AI skills as a documentation practice
-------------------------------------

Over the summer, documentarians reported on new projects they were building: collections of AI skills, reusable instruction sets that extend what a model can do. Participants noted that the discipline required to build them well looks a lot like the discipline that makes good documentation: Scope carefully. Write for your audience. Offer clear examples. Maintain ruthlessly.

People reported that comprehensive skills performed worse than more focused ones. The instinct to be thorough, so natural for documentarians, may not always serve skills well. People said that a skill tended to work better when it does one thing well and clearly signals when it applies. Deciding what not to write can be as important as deciding what to include.

Soft instructions may not be enough to act as guardrails. For example, some found telling Claude "don't use this skill for Product B" worked when the context was clear, but failed when the context was ambiguous. Some teams found a more reliable approach in the structure around the skill itself: storing skills in project directories so they only load in the right context, using path scoping to restrict availability and explicit permissions to enforce harder boundaries.

As with some docs, examples may be more helpful than instructions. Participants found that a corpus of strong examples can outperform even well-crafted rules. When a skill produces output you're genuinely happy with, capturing that output can be useful. Over time, consider growing your example library, rather than continually expanding their instruction prose.

Maintenance is the practice nobody talks about enough. Skills can compound, much like documentation. Participants talked about experimenting with regular deletion passes, revisiting skills as the underlying model improved, and tracking whether a skill is actually reducing the amount of correction required during review.

The practitioners reporting the most success were often applying the same instincts that make them good documentarians. The tools are new. The discipline isn't.

See more Write the Docs resources about `AI and LLMs </topics/#ai-and-llms>`__.

------------------------
Write the Docs resources
------------------------

Write the Docs offers lots of valuable resources related to documentation. See all of the Write the Docs `learning resources </about/learning-resources/>`__. To discuss any of these ideas or others related to documentation, join the conversation in the `Write the Docs Slack community </slack/>`__ in one of the many `channels </slack/#channel-guide>`__.

----------------
Events coming up
----------------

- 4 Sep, 08:30 EDT (US East Coast Virtual): `Social Hour for Documentarians <https://www.meetup.com/write-the-docs-east-coast/events/313625244/>`__
- 8 Sep, 17:30 MDT (Calgary, Canada): `Write the Docs Calgary Coffee Night <https://www.meetup.com/wtd-calgary/events/312192275/>`__
- 17 Sep, 18:00 BST (London, United Kingdom): `School of Docs: Graduating in Technical Writing <https://www.meetup.com/write-the-docs-london/events/313761551/>`__
- 17 Sep, 17:00 MST (Phoenix, USA): `WTD PHX September Happy Hour <https://www.meetup.com/write-the-docs-phoenix/events/316287440/>`__
- 18 Sep, 08:30 EDT (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/311760896/>`__
- 26 Sep, 11:00 IST (Bangalore, India): `Documentation & Technical Writing Devroom | (Registration via IndiaFOSS) <https://www.meetup.com/write-the-docs-india/events/315066535/>`__
- 30 Sep, 18:30 PDT (San Francisco, USA): `The AI-Native Technical Writer <https://www.meetup.com/write-the-docs-bay-area/events/316203268/>`__
- 2 Oct, 08:30 EDT (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/313625245/>`__
- 6 Oct, 18:30 PDT (San Francisco, USA): `Practical AI for Documentation <https://www.meetup.com/write-the-docs-bay-area/events/316163978/>`__
