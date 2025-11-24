:og:image: https://www.writethedocs.org/_static/logo-opengraph.png

.. post:: November 05, 2025
  :tags: newsletter

#########################################
Write the Docs Newsletter – November 2025
#########################################

Greetings, documentarians! My head is still buzzing after the Berlin conference last week. Full of ideas and connections that bring hope for the future. It is truly great to get the chance to be together with other people who care about documentation and about their fellow humans as much as everyone I met there did. I hope you all get the chance to find that connection somewhere, whether at a `WTD meetup </meetups/>`__ or conference next year or anywhere else.

If you missed the talks at WTD Berlin or want to relive the best bits, catch up with all of the `videos from the conference <https://www.youtube.com/playlist?list=PLZAeFn6dfHpkP1wAM5OIqAMH4guScopET>`__. The conferences will be back next year.

If you haven't yet filled out the 2025 Salary Survey, we need your input! If you have already contributed, please consider sharing with documentarian friends and colleagues -- the more submissions we gather, the more useful the data becomes for everyone. Head on over to the `survey <https://salary-survey.writethedocs.org/>`__.

If you enjoy the newsletter, consider becoming part of the `newsletter team </team/#newsletter>`__! We are the actual humans who put together these articles every month so your good ideas don't get left behind in Slack. If you like learning about what your fellow documentatiarians are thinking about and want to get your words in front of thousands of eyes, it could be for you. Ping `@Aaron Collier` on Slack if you're interested.

This month the wonderful team has put together articles on optimizing docs for AI consumption, putting together a style guide for your screenshots, and being the first technical writer at a startup. Enjoy!

------------------------
Optimizing docs for LLMs
------------------------

Documentarians are increasingly feeling pressure to produce docs for consumption by large language models (LLMs) rather than humans. The pressure may come from marketing teams that prefer quick solutions based on trends and content that's as easy as possible for AI to consume, like `FAQs </blog/newsletter-may-2020/#to-answer-or-not-to-answer-faqs>`__. However, according to a recent *Intercom* article by Beth-Ann Sher (`Optimizing content for Fin <https://www.intercom.com/help/en/articles/7860255-optimizing-content-for-fin>`_) writing "as if you're doing a radio interview and you don't want to be quoted out of context" can be more effective than FAQs.

Improved rankings hinge on getting chatbots to see your documentation as an authority, but the field is changing rapidly and different sources have different opinions about the best strategies. Writing structured, concise content with clear introductory paragraphs and informative headings can improve AI rankings without inserting FAQs. Much of what we consider good writing for humans turns out to be good for LLMs too. Some also mentioned that certain retrieval setups (RAG/embeddings, chunking, metadata) benefit from a single canonical troubleshooting/summary page that explains the content in other docs.

When you're facing requests for docs overhauls that seem to lean on incorrect assumptions about LLM preferences, try to work with SEO and marketing teams to understand trending queries so that you can adjust content based on analytics. Test the docs with your target LLM and measure retrieval accuracy so that you can develop preferred strategies instead of responding with a flat "no." Consider including FAQs on hidden pages so that they are available to LLMs without cluttering the rest of the docs.

For more opinions about the best way to optimize your docs for LLMs (including some that support the FAQs strategy), consider these additional resources:

- `SEO is Dead (Again) <https://www.bigplayers.co/p/seo-is-dead-again?>`_ and `The Day the Internet's Front Door Moved <https://www.bigplayers.co/p/the-day-the-internets-front-door-moved?>`_ by Matthew Berman
- `AI chat as user research when your reader is a bot <https://docsgoblin.com/blog/25-03-08-making-ai-an-editor.html>`_ by CT Smith
- `Beyond SEO: The triple-threat optimization strategy for visibility in the AI era <https://writer.com/blog/geo-aeo-optimization/>`_ by Alaura Weaver
- `How to Make Your Developer Documentation Work with LLMs: Lessons from the Trenches <https://fusionauth.io/blog/llms-for-docs>`_ by Dan Moore
- `How to Optimize Your Content for ChatGPT & LLM Answer Engines <https://inaiwetrust.com/p/how-to-optimize-your-content-for-chatgpt-and-llm-answer-engines>`_ by Alex Velinov

See more Write the Docs resources about `AI and LLMs </topics/#ai-and-llms>`__.

-------------------------------
Create a screenshot style guide
-------------------------------

Style guides help documentarians write content that’s consistent across products. Some companies include screenshot guidelines within their general style guide; some don’t. As with textual content, screenshot guidelines focus on consistency and best practices. Here are some suggestions.

**Screenshot capture standards**

* Unless your product is for a mobile device, capture images from a laptop or the main desktop monitor.
* Specify maximum dimensions (such as 1000 px wide). Don’t upscale smaller images.
* If your product can be in light or dark mode, decide whether to standardize on one. (NOTE: Generally, light mode is more legible. Some companies prefer to use both dark and light mode screenshots to present the user’s version in the documentation.)
* Always use the same OS (and browser, if relevant) for UI captures.
* If necessary, use tools to standardize UI dimensions so elements appear consistently.

**Image composition**

* Crop tightly around relevant content to reduce visual noise, but maintain enough context.
* Crop with the screen capture tool or a photo editor, not the documentation’s source program.
* Show the UI in context rather than isolating buttons.

**Visual issues**

* Add thin black borders to distinguish light images from the documentation’s background.
* Protect privacy by blurring any ‘real’ data captured, such as usernames and passwords.
* Populate UI examples with believable but fictional data.

**Annotations (if used)**

* Do not write text directly on screenshots.
* Draw rectangles around groups of elements. Use arrows or circles to point out specific elements.
* Keep space between annotations and UI edges.
* If possible, limit the number of annotations in each image.
* For accessibility, describe any annotations in the text.

**Practicalities**

* If your product changes often, minimize the number of screenshots and focus on textual explanations. Use screenshots only when necessary. 
* All screenshots should have descriptive file names.
* All screenshots should have correct, but brief Alt text (and a tooltip if used).
* Inform your users about your basic guidelines for screenshots (such as platform or browser).
* Consider collaborating with someone in marketing or sales for guidelines on color, sizing, and branding.

See more Write the Docs resources about `screenshots </topics/#screenshots>`__ and `style guides </topics/#style-guides>`__.

-----------------------------------
Being the first writer at a startup
-----------------------------------

Startups usually hire their first technical writer when things start slipping through the cracks. Knowledge lives in Slack threads, engineers repeat themselves, and customers can’t find answers. Joining at that moment is both thrilling and challenging -- you’re helping to bring order to chaos.

===================================
What to expect (and how to survive)
===================================

- **Start small**. Focus on what will help the most people right away — troubleshooting guides, onboarding steps, or FAQs. Quick wins build trust and show value fast.
- **Create structure**. Choose your tools, make simple templates, and write a short style guide. Clear systems beat fancy ones at this stage.
- **Build habits early**. Encourage engineers and PMs to review docs as part of their workflow. Regular check-ins keep information accurate without a heavy process.
- **Pick your battles**. You can’t fix everything at once. Decide what matters most and leave the rest for later.
- **Watch the culture**. In small teams, one difficult personality can shape the environment fast. Find allies who value communication and have your back.
- **Track your impact**. Measure what changes -- fewer repeated questions, better onboarding, or faster support. Data helps others see the value of your work.

Being the first writer at a startup is more than a role -- it’s a crash course in clarity, influence, and leadership. It’s messy work, but the lessons stay with you long after the startup dust settles.

See more Write the Docs resources about `jobs and careers </topics/#jobs-and-careers>`__.

------------------
Featured job posts
------------------

`Technical Writer <https://poedit.net/docs-writer>`__, Poedit - *Remote Contract*

*Interested in promoting your open position? See our* `job posting sponsorship </sponsorship/jobs/>`__ *for more details.*

------------------------
Write the Docs resources
------------------------

Write the Docs offers lots of valuable resources related to documentation. See all of the Write the Docs `learning resources </about/learning-resources/>`__. To discuss any of these ideas or others related to documentation, join the conversation in the `Write the Docs Slack community </slack/>`__ in one of the many `channels </slack/#channel-guide>`__.

----------------
Events coming up
----------------

- 5 Nov, 17:30 EST (Pittsburgh, USA): `Doc troubles and social event <https://www.meetup.com/write-the-docs-pittsburgh/events/311359182/>`__
- 6 Nov, 17:45 CET (Amsterdam, Netherlands): `Casual social meetup at the OBA Oosterdok café <https://www.meetup.com/write-the-docs-amsterdam/events/311838366/>`__
- 11 Nov, 18:30 PST (San Francisco, USA): `Strategies for Leveling Up Your Technical Writing Skills <https://www.meetup.com/write-the-docs-bay-area/events/311031264/>`__
- 13 Nov, 18:00 CST (Austin, USA): `Write the Docs ATX Social Event @ Cherrywood Coffeehouse <https://www.meetup.com/writethedocs-atx-meetup/events/311558105/>`__
- 14 Nov, 08:30 EST (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/309520004/>`__
- 14 Nov, 17:30 EST (Carolinas, USA): `Charleston WTD Meetup - Social/Happy Hour <https://www.meetup.com/write-the-docs-carolinas/events/311795694/>`__
- 15 Nov, 08:00 WAT (Port Harcourt & Lagos, Nigeria): `Building an Effective Documentation Culture for Sustainability  <https://www.meetup.com/write-the-docs-nigeria/events/311775896/>`__
- 20 Nov, 18:30 GMT (London, United Kingdom): `Find, Scan, Read: A Structured Approach to Documentation Creation & Improvement <https://www.meetup.com/write-the-docs-london/events/311217477/>`__
- 21 Nov, 12:00 PST (Portland, USA): `Write the Docs PDX - Casual Fridays Meetup - Friday, 11/21 @ noon <https://www.meetup.com/write-the-docs-pdx/events/311827735/>`__
- 28 Nov, 08:30 EST (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/309520008/>`__
- 4 Dec, 18:00 GMT (London, United Kingdom): `Write the Docs Winter Social ❄️ <https://www.meetup.com/write-the-docs-london/events/311423344/>`__
