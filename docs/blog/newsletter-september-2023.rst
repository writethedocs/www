.. post:: September 05, 2023
   :tags: newsletter

##########################################
Write the Docs Newsletter – September 2023
##########################################

Hey, documentarians, the newsletter is back!

In conference news, we have the `2023 Atlantic conference </conf/atlantic/2023/>`__ running Sunday through Tuesday. If you don't have a ticket yet, grab one while you can (through 7 September). Looking forward to seeing you there. And after you get inspired, the Australia conference still has its `call for proposals </conf/australia/2023/cfp/>`__, but it closes 15 September, so get your ideas in soon.

Elsewhere, the Write the Docs Salary Survey for 2023 is opening next week. We encourage everyone working in areas related to documentation to participate - working or currently unemployed, contract or permanent, employee or freelance. Your contribution will help the whole community better understand what an appropriate salary is and provide a basis for future negotiations. This year, we're including new questions about "return to the office" mandates, job changes, and your thoughts on job security – issues at the top of a lot of people's minds. We'll be announcing when the survey goes live on Slack and Twitter, and you can always find all details at https://salary-survey.writethedocs.org/.

I'd like to extend a special goodbye to Beth Aitman. This month marks the first newsletter in years that she hasn't participated in. Thanks for your leadership, help, and many other contributions.

The summer was a busy time, with too many conversations to cover here. For example, the `#career-advice channel <https://writethedocs.slack.com/archives/C6ADX1YVA>`__ had multiple discussions of resume formatting and resume peer checks. So if you're looking for help with your resume, join the discussion in the channel.

We do have articles today on motivating people to contribute to internal docs, whether to number your section headings, dealing with unpleasant people in open-source projects, and staying up-to-date with changes you need to make. Something for everyone!

-----------------------------------------
Motivating Contributions to Internal Docs
-----------------------------------------

This month, documentarians shared their best practices and tips for motivating others to contribute to internal docs, especially in work cultures that share information verbally.

If you need to generate support for adding to internal docs, focus on the costs of incomplete or poorly written documentation. Explain how often engineers are interrupted to answer questions, how often they answer the same questions, and how long it takes to regain concentration after an interruption. You might even try to estimate the actual cost of the lost time using engineer salaries. Failing to maintain internal docs is also a business continuity risk: experienced employees have a harder time getting up to speed on new projects, former employees take their knowledge with them when they leave, and new employees can't onboard efficiently.

When it comes to the actual writing, it helps to make the documentation process as efficient and repeatable as possible. Develop patterns for different types of documentation to make the task less burdensome for people who don't write the docs every day. Publish instructions to help people understand how to make small changes themselves and ask for help for big issues. Consider keeping a shorter, more streamlined style guide for internal docs. You might also be able to integrate docs work into other teams' workflows. For example, you could automatically create a docs ticket for every feature initiative opened by a product manager or require information about any relevant docs needs in bug report forms.

Look for opportunities to encourage a sense of ownership among those who contribute to internal docs. When you act on someone's feedback or publish someone's contribution, make sure to follow up with a link to the result so that people know their efforts matter. Interested contributors might benefit from polishing their skills with `Google’s tech writing courses for software engineers <https://developers.google.com/tech-writing>`_.

Other recommendations for further information:

- `Any friend of the docs is a friend of mine: Cultivating a community of documentation advocates </videos/portland/2019/any-friend-of-the-docs-is-a-friend-of-mine-cultivating-a-community-of-documentation-advocates-heather-stenson/>`__ from Write the Docs Portland, 2019
- `2022 State of DevOps Report data deep dive: Documentation is like sunshine <https://cloud.google.com/blog/products/devops-sre/deep-dive-into-2022-state-of-devops-report-on-documentation>`__
- `Why it’s worth it to invest in internal docs <https://increment.com/documentation/why-investing-in-internal-docs-is-worth-it/>`__

--------------------------
Numbering Section Headings
--------------------------

To number or not was a question posed in recent months. In general, these queries related to printed (or PDF) manuals.

Often, the reasons for numbering section headings relate to using the number as a reference or clarifying the sequencing of sections and relationships between sections. As one documentarian noted, "Titles alone do not tell users ... where they will find the information unless they are already ... familiar with the content structure of the document. When you have to check section 3, you know that it is before section 4 and ... after section 2."

Certain domains may also prefer or require section numbers. For example, if your readers are in a scientific community, a legal or academic environment, or a strictly regulated domain, they may expect to see section numbers.

One caution: if your documentation tool doesn't support automatic numbering, then including numbers can be a maintenance nightmare. If your tool doesn't support automatic numbering, perhaps a plug-in may be needed. 

Several people mentioned issues about updating the content and adding in new sections. Even with automatic numbering, readers of previous versions may suggest looking at a specific section by its number – only to find that the number has changed in a recent update.

When numbering is a content convention, it may not represent a sequence to follow. In this case, numbers can interrupt the reader's focus by forcing them determine whether they really need to go through content sequentially. One person wrote, "Numbering is often one of those unnecessary things that people do without really thinking why." Documentarians may have section 3 before section 4 just because that's the sequence that they thought of – not because it needs to come first.

For online documentation, people were less in favor of using numbers. The discussion emphasized that it could depend on the structure of the online content and navigational features.

------------------------------------------------------
Dealing with Unpleasant People in Open-Source Projects
------------------------------------------------------

Although open-source groups are famed for their collaborative attitude, dealing with problematic personalities can sometimes be challenging. A recent WTD discussion provided useful ideas for efficiently dealing with such circumstances.

In this conversation, advice was needed on how to deal with an individual whose behavior in an open-source project was troublesome. This person acted in ways that verged on being unacceptable without being overtly prohibited. Their perceived importance in the community added to the complication.

A critical initial step was suggested: reviewing the project’s code of conduct, ideally with clearly stated repercussions for violations. Reminding individuals of appropriate community conduct addresses the current issue while reassuring other community members.

A real-life example from the Arch Linux mailing lists was also presented in which a similar situation was defused by reminding the member of the code of conduct. This demonstrates how established open-source groups deal with such difficulties.

Moreover, a more empathic strategy was suggested, such as advocating for compassion rather than aggressiveness in response. Recognizing the content of their comments while politely expressing disagreement can pave the way for meaningful discourse.

Finally, it was emphasized that rules of conduct promote a culture of respect and kindness and that leading with the assumption that the person didn’t intend to be impolite can help ease tensions.

Fostering a communal feeling of respect and collaboration is critical in open-source groups. By following standards of behavior and encouraging polite debate, these communities may continue to grow, guaranteeing an inclusive and productive environment for all contributors. Though difficult, dealing with challenging people is critical to sustaining the integrity and vibrancy of open-source initiatives.

-----------------------------------------
Keeping Up-To-Date with Necessary Changes
-----------------------------------------

Even in periods when many people are taking vacations, an organization can have a lot going on. A recent discussion touched on how to stay on top of it all when you have many articles to keep track of. Some complained about working long hours to add documentation only to be told right after it was published that it no longer applied. The discussion turned to tools and processes to avoid such issues.

Many people used a ticketing system. Jira was popular because it was where others were working and so made it easier to follow changes. For similar reasons, others used GitHub or GitLab and followed changes directly in projects. Others had their own separate system in someplace like Asana with just what they needed.

Other than tools, people also suggested setting up regular meetings with people like product managers, especially if these meetings line up with a release schedule. It helped to put in place some sort of check to determine whether doc changes are necessary before release. Others suggested seeing if you can get rid of some content, such as pages with few visits. Then there's less to deal with.

Even with the best process, everyone misses some things. So it helps to think about how to find the things you've missed. For example, make it easy to report issues so you learn about anything that falls through. And multiple people noted the benefits of regular documentation audits, starting with the most important or most visited pages. Go through things slowly but steadily to check that everything still works as it should.

----------------
From Our Sponsor
----------------

This month’s newsletter is sponsored by ClickHelp:

In the world of technical documentation, the essential goals are to empower writers, enhance efficiency, and promote collaboration. ClickHelp emerges as a valuable ally in achieving these objectives.

ClickHelp is a comprehensive cloud-based documentation platform for efficient teamwork. Its robust capabilities empower users to efficiently generate, review, and release documentation. The platform optimizes workflows through features like single sourcing and dynamic output, enhancing the overall process. Furthermore, it is flexible and customizable, with a fast and accurate import process. The tool promotes seamless collaboration and effortless version tracking. It is accessible across various devices and platforms, accommodating multiple formats.

Noteworthy functionalities include OpenAPI (Swagger) integration, seamless migration from Confluence, powerful navigation elements, effective translation management, and many more. Embark on your journey of exploration by initiating a free trial or scheduling a demo to experience its cutting-edge features. Join us on this transformative expedition with ClickHelp.

*Interested in sponsoring the newsletter? Take a look at our* `sponsorship prospectus </sponsorship/newsletter/>`__.

------------------
Featured Job Posts
------------------

- `Staff Technical Writer <https://jobs.writethedocs.org/job/1877/staff-technical-writer/>`__, Cockroach Labs (Hybrid; New York, San Francisco, Toronto)

*To apply for this job and more, visit the* `Write the Docs job board <https://jobs.writethedocs.org/>`_.

----------------
Events Coming Up
----------------

- 8 Sep, 08:30 EDT (New England and Florida, USA): `Focused conversation: Videos in documentation <https://www.meetup.com/write-the-docs-florida/events/295094684/>`__
- 8 Sep, 19:30  IST (Bangalore, India): `Let's bring science into API documentation <https://www.meetup.com/write-the-docs-india/events/295604665/>`__
- 13 Sep, 18:00  MDT (Boulder/Denver, USA): `Building our own applications: Nextworld’s journey to Content 4.0 <https://www.meetup.com/write-the-docs-boulder-denver/events/295749600/>`__
- 21 Sep, 10:00  AEST (Australia): `(Remote): Fight for your promotion in 3 steps <https://www.meetup.com/write-the-docs-australia/events/295577798/>`__
- 21 Sep, 17:30  CDT (Austin, USA): `Write the Docs ATX Happy Hour Meetup: September 21 <https://www.meetup.com/writethedocs-atx-meetup/events/295309065/>`__
- 22 Sep, 12:00  MDT (Boulder/Denver, USA): `Fourth Friday Write the Docs Co-working Social <https://www.meetup.com/write-the-docs-boulder-denver/events/295850155/>`__
- 22 Sep, 08:30 EDT (New England and Florida, USA): `Focused Conversation for Documentarians <https://www.meetup.com/boston-write-the-docs/events/295844994/>`__
- 6 Oct, 08:30 EDT (New England and Florida, USA): `Focused Conversation for Documentarians <https://www.meetup.com/boston-write-the-docs/events/xzpxdtyfcnbjb/>`__
