:og:image: https://www.writethedocs.org/_static/logo-opengraph.png

.. post:: June 04, 2025
  :tags: newsletter

#####################################
Write the Docs Newsletter – June 2025
#####################################

Greetings, fellow documentarians! The weather here is warming up and people are already leaving town for summer vacations or planning to. I hope you have a break planned at some point soon that can sustain your energy and enthusiasm for good docs.

If you're interesting in keeping up with the Write the Docs community, check out the `most recent quarterly update </blog/2025-Q2-community-board/>`__. You'll learn about what's happened and what the plans are for getting even better.

Those plans include three (3!) more conferences this year. The first is a one-day in-person event this Saturday in Kenya organized by `Write the Docs Kenya <https://www.meetup.com/wtd-kenya/events/305750149/>`__. Then October will see our first conference in Europe with an in-person element since 2019. See more in the `announcement for Write the Docs Berlin 2025 </conf/berlin/2025/news/welcome/>`__. And we'll close the year with the virtual `Write the Docs Australia 2025 </conf/australia/2025/>`__ in November.

This month brings articles on how to help users get useful release notes, automating processes around screenshots (including translations), and how to help non-documentarians think of their readers. Enjoy! 

--------------------------------------------------
Making release notes work: Tips for documentarians
--------------------------------------------------

Release notes usually come at the end of a hectic software cycle, often filled with scattered and highly technical notes. Documentarians whose role involves publishing these notes go beyond summarizing lines of code -- they shape those fragments into a clear, user-focused story that communicates the value of the changes.

While automation can help you extract technical updates such as bug fixes, new features, and API changes, it may miss the bigger picture -- the context, clarity, and real benefits that users need to understand. This is where your expertise can really shine as you translate complex technical details into meaningful insights that users can easily grasp and appreciate.

Here are practical ways to help you improve the release notes process:

1. Partner with developers early. Ask developers to write clear commit messages and use accurate tags in Jira or Git. Provide simple templates they can follow, such as "Fix: Login timeout bug", and give quick shoutouts during standups or in pull requests when they write helpful notes.
2. Automate what makes sense. Let tools do the heavy lifting by pulling in content from pull requests, changelogs, or issues tagged for review. But don’t skip the editorial review—your judgment is essential for making sure the final version is clear, accurate, and user-friendly.
3. Make release notes part of the workflow. Work with your team to build note drafting into your regular tools such as Git, Jira, or GitLab. Whether that’s a shared release notes branch or a custom field in tickets, having a process in place saves time and avoids last-minute stress.
4. Write with the user in mind. Instead of listing technical changes, explain what’s new and why it matters. Use plain language and organize the notes in a way that highlights impact, not just internal ticket types.

When done well, release notes showcase progress, reduce support issues, and reinforce a user-first mindset.

See more Write the Docs resources about `release notes </topics/#release-notes>`__.

--------------------------------------------
Automating screenshot capture or translation
--------------------------------------------

The quantity of screenshots in documentation has been an ongoing issue for many years. The general consensus has been to minimize the number of screenshots — be selective about what to use. For an example, see the 2022 newsletter article `When to create screenshots </blog/newsletter-december-2022/#when-to-create-screenshots>`__. In the past, the concerns usually focused on accessibility, ROI, and maintenance issues. 

A recent discussion in `#doctools <https://writethedocs.slack.com/archives/C4EPE8332>`__ brought up some twists to the screenshot issue. The original poster had been asked to include 900 screenshots of a translated UI! So one issue was whether to satisfy the request for 900 screenshots, which relates to the *When to create screenshots* article. (Some mentioned that requiring this many screenshots in documentation these days means that there’s a UX issue.) In this recent thread, many responses focused on tools to automate the process. Also, in this case, there was another issue: documenting a translated UI. 

**First of all, is there any tool that could automatically take all those screenshots?**

The answer was a conditional yes. 

* One person had used a proprietary tool to capture and update screenshots for company documentation. 
* For a browser-based program, a web QA-related tool may be useful. One suggested command-line utility for taking automated screenshots of websites was `Shot-Scraper <https://github.com/simonw/shot-scraper>`__. 
* To take the burden away from the documentarian, several suggested working with an AI app (such as `Claude <https://claude.ai/>`__) or a UI testing tool (such as `Cypress <https://www.cypress.io/>`__ or `Selenium <https://www.selenium.dev/>`__). 
* Another option could be to simplify the UI for documentation with a technique such as `simplified user interfaces <https://www.techsmith.com/blog/simplified-user-interface/>`__. 

**Secondly, is there a way to adjust existing screenshots for a translated UI?**

If 900 screenshots already exist, it might be possible to adjust the existing ones.

* For translated UIs, the `OpenAI image generation API <https://platform.openai.com/docs/guides/image-generation>`__ has been used to pull in translated content from UI translations and apply those translations to existing screenshots. 

Automating the screenshot process may lessen ROI concerns, but there are still accessibility, maintenance, and other issues to consider. 

See more Write the Docs resources about `media such as screenshots </topics/#other-media>`__.

----------------------------------
Help contributors think like users
----------------------------------

Docs that are prepared by contributors such as engineers and product managers often reflect the contributors' perspectives rather than those of actual users. At companies where non-documentarians write the docs, you can try a few strategies to help them provide the information that users really need.

Participating in doc reviews gives you a chance to ask targeted questions of contributors that encourage a user-centric mindset. You can also use targeted questions as writing prompts in templates. These kinds of questions include:

- Who will use this document? What is their role and competency level? How often will they use it?
- What are users trying to do when they read this doc? Are they likely to be frustrated or confused?
- What would a first-time user need to know to get started?
- What assumptions did you make?
- Which steps must users follow and in which order?
- What happens if a user follows these instructions? What if they make a mistake?

Developing user personas based on actual customers can guide contributors to think about what different users need to know. Once you have personas, you can tailor targeted questions for individual user types, for example, "What does an admin user need to know?" For more information, read `Transforming your learning experiences with targeted Learner Personas <https://lxdlearningexperiencedesign.com/toolkit/transforming-your-learning-experiences-with-targeted-learner-personas/>`__ at Learning Experience Design (LXD).

Ask someone outside the contributor's field to try to use the doc, ask questions about anything they don't understand, and provide feedback. It helps to have these test users talk through their thinking process as they try to follow the doc. This user testing surfaces questions and problems that contributors probably haven't thought about and forces contributors to rethink what they're saying and how they're saying it.

Finally, consider giving short talks about good messaging in software, what it means to write messages for users, and the importance of correct spelling and grammar. Suggest looking at competitors' docs as examples of what's right and what's wrong. Explain the detrimental effects of poor messaging, such as lost sales. And share positive user feedback about the product when you can to help motivate contributors.

See more Write the Docs resources about `working with other roles </topics/#working-with-other-roles>`__.

------------------------
Write the Docs resources
------------------------

Write the Docs offers lots of valuable resources related to documentation. See all of the Write the Docs `learning resources </about/learning-resources/>`__. To discuss any of these ideas or others related to documentation, join the conversation in the `Write the Docs Slack community </slack/>`__ in one of the many `channels </slack/#channel-guide>`__.

----------------
Events coming up
----------------

- 5 Jun, 17:30 CDT (Austin, USA): `Write the Docs ATX: Event Planning Survey Results and Social Event <https://www.meetup.com/writethedocs-atx-meetup/events/308028531/>`__
- 10 Jun, 19:00 MDT (Calgary, Canada): `Minimalism: When less is more, how you can know when less is actually less <https://www.meetup.com/wtd-calgary/events/304868556/>`__
- 12 Jun, 18:00 CDT (Huntsville, USA): `Write the Docs Social <https://www.meetup.com/write-the-docs-huntsville/events/307947376/>`__
- 13 Jun, 08:30 EDT (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/305477649/>`__
- 17 Jun, 17:00 EDT (Pittsburgh, USA): `June Happy Hour: Write the Docs Pittsburgh <https://www.meetup.com/write-the-docs-pittsburgh/events/307787034/>`__
- 19 Jun, 18:30 BST (London, United Kingdom): `WTD x GDS: Starting with User Needs <https://www.meetup.com/write-the-docs-london/events/307934947/>`__
- 19 Jun, 18:00 CDT (Huntsville, USA): `Docs as Tests Meetup <https://www.meetup.com/write-the-docs-huntsville/events/307947407/>`__
- 23 Jun, 18:30 EDT (Washington, USA): `Graphic Relief: Beyond Flowcharts and Screenshots (Watch Party) <https://www.meetup.com/write-the-docs-dc/events/308241708/>`__
- 24 Jun, 18:00 EDT (Ottawa, Canada): `Write the Docs Ottawa Meetup <https://www.meetup.com/write-the-docs-ottawa/events/307684420/>`__
- 25 Jun, 18:00 PDT (San Francisco, USA): `QuickDocs – Live Technical Writing Talks in Just 15 Minutes! <https://www.meetup.com/write-the-docs-bay-area/events/307748415/>`__
- 27 Jun, 08:30 EDT (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/305477650/>`__
- 11 Jul, 08:30 EDT (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/306334002/>`__
