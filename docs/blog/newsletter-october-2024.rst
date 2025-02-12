:og:image: https://www.writethedocs.org/_static/logo-opengraph.png

.. post:: October 3, 2024
  :tags: newsletter

########################################
Write the Docs Newsletter – October 2024
########################################

Hello hello, wonderful documentarians! I hope you all are able to find sources of inspiration around you. The ideas coming from the Write the Docs community and conferences recently have provided me with hope for the future.

Our most recent conference was the Atlantic 2024 conference. If you missed it, or just want to revisit, check out the `videos from the conference <https://www.youtube.com/playlist?list=PLZAeFn6dfHpn8IckCiREggN0f9oWEMomW>`__ and the `sketchnotes of every talk <https://www.flickr.com/photos/writethedocs/albums/72177720320644083>`__. And once you've seen those, check out the next conference, Australia 2024, which just announced its `speakers and full schedule </conf/australia/2024/news/announcing-speakers-schedule/>`__. Be sure to grab a ticket for November 28–29 in Melbourne if you can.

In other community news, the 2024 WTD Documentation Salary Survey -- our 6th annual survey -- will be open for submissions very soon! We're implementing a couple of frequently requested usability improvements and are still ironing out a few issues, but keep an eye on the `survey website <https://salary-survey.writethedocs.org/>`__ and follow Write the Docs on Twitter and LinkedIn, where it will be announced as soon as it's ready.

Relatedly, the Write the Docs job board has been replaced. In its place, we have a `new sponsorship opportunity </sponsorship/jobs/>`__ for for companies looking to hire documentarians. We're still hoping to provide useful information about job openings, just closer to where our community is.

In the newsletter this month, we have articles on dealing with feedback in large volumes, how to handle freelance work, standards for using callouts, and whether to keep docs in code. Hope you'll find something for you!

------------------------------
Managing mountains of feedback
------------------------------

Resolving feedback on documentation can mean anything from making straightforward updates to undertaking a substantial investigation and revision, but it always takes time away from documenting new product functionality. If you can't hire more documentarians to keep up with both addressing feedback and writing new docs, you can try these ideas.

* Tag feedback tickets with information about their required effort so that writers can take on the quick fixes as a mental break from more involved work. Schedule bigger tickets and critical issues alongside product work.

* If it works with your release cadence, schedule time each month or quarter for a "bug bash" devoted entirely to addressing docs feedback.

* Filter feedback through customer-facing colleagues to identify high-quality requests for docs changes. When appropriate, consider diverting tickets that describe product problems, such as a confusing user interface or functionality, to other teams as requested improvements.

* If you have a customer knowledge base that answers basic questions about the product, try to route some feedback to the team that maintains it. Creating standard responses for the most common issues can also reduce the time everyone spends on repetitive feedback.

It's also possible that much of the feedback you receive isn't worth addressing at all. If you can't automate the process for reviewing feedback, it takes a lot of time. And then, revising something trivial may come at the cost of writing a new topic that could really help someone. Feedback from an engaged user base that feels a sense of ownership is typically very useful, but otherwise, the feedback quality may not be worth the effort you spend evaluating it.

-------------------------------------
Working as a contractor or freelancer
-------------------------------------

Some documentarians consider contracting or freelancing while job hunting. In the `#freelance channel <https://writethedocs.slack.com/archives/CA1J9GV17>`__, a former employee asked about taking on a client.

**What rate to use?**

Rates for technical writers vary widely and depend on many factors. 

* The domain and the audience: In software, developer documentation prompts the highest rates; end-user documentation rates are usually lower. Hardware-associated documentation rates may be lower. Specialist documentation (such as scientific or medical) may command higher rates. 
* The geographical location: In the US, tech hubs, major cities, and the coasts have higher rates. In non-tech industries and non-coastal areas, rates tend to be lower. Rates vary by country and relate to cost of living in a particular area. 
* The type of work requested: Charge less for minor editing. Rewriting or creating new content costs more. Re-organizing content (information architecture) or, in a docs-as-code environment, setting up and working with a tool chain would command higher rates.
* Your skills and experience: Highly skilled and experienced professionals can ask for higher rates.

To calculate an hourly rate (in the US) determine the salary for an equivalent position, divide that by 52x40, and then double or triple that to compensate for benefits. Check job postings and the  `2023 WTD Salary Survey <https://www.writethedocs.org/surveys/salary-survey/2023/>`_ for salaries.

**Can I assume that the client pays taxes?**

If you’re working as a W2 contractor in the US, the agency takes out federal taxes. As a freelancer in the US (1099), you pay all taxes. In other countries, check your local tax requirements, which vary widely.

**How often will I get paid?**

As a contractor, the pay period depends on the agency. As a freelancer, your contract defines the pay period. Some freelancers bill based on the project (milestones); some calculate invoices based on an hourly rate. 

**What can I consider billable hours?**

As a contractor working on site, you normally bill for hours on site based on your contract. As a freelancer working off site, you bill whenever you work on the project. In general, you don't get overtime unless it’s in your contract.

---------------------------------------
Using callouts/admonitions in tech docs
---------------------------------------

When it comes to creating clear and effective technical documentation, knowing when to use callouts and admonitions (sections, often boxes, that stand out from the surrounding text) and avoiding overuse is key to creating user-friendly content. They can highlight important information and ensure your documentation remains accessible and easy to navigate.

Some style guides follow a tiered system to ensure proper use:

- Tip: Helpful advice that can make tasks easier but isn’t critical.
- Note: Relevant but non-essential information that adds context but doesn’t affect the task’s outcome.
- Important: Information that, if missed, could lead to frustration or additional work.
- Warning: Critical details about data loss or security risks, where overlooking the warning could cause significant problems.

The key is moderation. Too many individual notes, tips, or warnings can cause “admonition fatigue” and lead to readers skipping over important information. When deciding between separated content or inline text, weigh the impact. If it’s crucial and might be missed, make it stand out. Otherwise, integrating it into the main body ensures smoother flow and readability.

By setting clear guidelines and using these tools purposefully, you can help users focus on what’s most important—without overwhelming them.

-------------------------------------
Should APIs be documented with code?
-------------------------------------

A recent question about documenting APIs in code in the `#documenting-apis channel <https://writethedocs.slack.com/archives/C0YH9K2JY>`__ met with some strong pushback. Someone felt that putting documentation in code (meaning the code used to generate the product) was the last thing documentarians should want. Others defended the practice.

The reasons given for separating docs and code included the idea that because docs in code relies on automated tools, their syntax is much less human-readable. It was also noted that modifying code might require specialized skills and privileges that some documentarians don't have. Having to compile and test an entire code source for a small docs change was also viewed as a barrier to entry, whereas a separate reference file means documentarians can work independently. 

The responses focused on the benefits of automatic generation and how it meant the reference was much more likely to stay up to date, especially compared to maintaining API definitions by hand. They celebrated the dependence on the code. It was also seen as a way to meet developers where they already are and so lower their barriers to contributing. People advocating for docs in code also said they keep all formatting in code to a minimum, with anything more complex in a guide separate from the API reference.

In the end, almost everyone agreed that the best solution is a single OpenAPI description that acts as a single source of truth for both the product and the docs, focusing on API design first. If this isn't possible, it comes down to your circumstances. If you and your fellow documentarians are code-literate and have access to the code, you may find it best to update API docs in the code itself. If making changes to the product code is difficult, you may need to make modifications to a generated reference or even mirror code changes in your own OpenAPI description.

----------------
From our sponsor
----------------

This month’s newsletter is sponsored by `GitBook <https://www.gitbook.com/?utm_campaign=product-docs&utm_medium=email&utm_source=write_the_docs&utm_content=newsletter>`_:

------

.. image:: /_static/img/sponsors/gitbook.png
  :align: center
  :width: 75%
  :target: https://www.gitbook.com/?utm_campaign=product-docs&utm_medium=email&utm_source=write_the_docs&utm_content=newsletter
  :alt: GitBook logo

+++++++++++++++++++++++++++++++++
Product docs your users will love
+++++++++++++++++++++++++++++++++

GitBook has everything you need to create beautiful docs for your users — so you don’t have to build your own editing tools, CMS, website, and more. You can just focus on writing great content.

GitBook’s branch-based Git workflow encourages your whole team to collaborate by creating a branch, requesting a review, and merging when ready. It’s a flow your developers already know and love — and they can even edit your docs in their code editor using Git Sync.

That’s all backed up by AI that lets your users find what they need fast, publishing settings that put you in control of who can access your docs, and internal documentation for your own team.

Sign up today and `get started for free <https://www.gitbook.com/?utm_campaign=product-docs&utm_medium=email&utm_source=write_the_docs&utm_content=newsletter>`__!

------

*Interested in sponsoring the newsletter? Take a look at our* `sponsorship prospectus </sponsorship/newsletter/>`__.

----------------
Events coming up
----------------

- 3 Oct, 17:30 CDT (Austin, USA): `Write the Docs ATX Social Event @ Cherrywood Coffeehouse <https://www.meetup.com/writethedocs-atx-meetup/events/303289714/?eventOrigin=group_events_list>`__
- 4 Oct, 08:30 EDT (East Coast Quorum, USA): `Social Hour for Documentarians <https://www.meetup.com/boston-write-the-docs/events/303217675/?eventOrigin=group_events_list>`__
- 10 Oct, 12:00 AEDT (Australia): `(Virtual) From Markdown to Mic Drop: A Tech Writer's Guide to Presentations <https://www.meetup.com/write-the-docs-australia/events/302728564/?eventOrigin=group_events_list>`__
- 16 Oct, 19:00 EDT (Toronto, Canada): `Write the Docs Toronto  <https://www.meetup.com/write-the-docs-toronto/events/303672626/?eventOrigin=group_events_list>`__
- 18 Oct, 08:30 EDT (East Coast Quorum, USA): `Social Hour for Documentarians <https://www.meetup.com/boston-write-the-docs/events/303544523/?eventOrigin=group_events_list>`__
- 24 Oct, 18:00 BST (London, United Kingdom): `From one to many - Building a documentation team <https://www.meetup.com/write-the-docs-london/events/303348349/?eventOrigin=group_events_list>`__
- 1 Nov, 08:30 EDT (East Coast Quorum, USA): `Social Hour for Documentarians <https://www.meetup.com/boston-write-the-docs/events/mbdmntygcpbcb/?eventOrigin=group_events_list>`__
