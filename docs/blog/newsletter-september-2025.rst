:og:image: https://www.writethedocs.org/_static/logo-opengraph.png

.. post:: September 02, 2025
  :tags: newsletter

##########################################
Write the Docs Newsletter – September 2025
##########################################

Greetings, fellow documentarians! I hope you are all having adventures at least as successful as those of the kids around here returning to or first experiencing school. Take joy when you can in choosing your own interests to learn about. And in being able to decide what to eat and when, which is not a joy these kids share.

In sad news, the Australia conference has been `cancelled for this year </conf/australia/2025/news/cancel-announcement/>`__. There is a meetup planned for later this month, so come together to feel the joy of in-person connection while you can this year. And stay tuned for reenergized activity next year.

Write the Docs Berlin 2025 is still happening in October. Speakers were just announced so have a look at the `list of talks </conf/berlin/2025/speakers/>`__, get excited, and then `grab your ticket </conf/berlin/2025/tickets/>`__ to join us there. I for one am having a hard time deciding which talk I'm most excited about, though it's probably the chance to see so many friendly faces in one place again.

This month's newsletter brings articles on staying polite when it's difficult, learning API docs and coding, implementing docs for beta features, and how LLMs have affected people's use of docs. Enjoy!

----------------------------
Keeping cool when challenged
----------------------------

Perhaps you, as a documentarian, assume good intentions when people engage with you at work. You may still encounter some people who want things done their way instead of trusting you and your team to write documentation appropriately. You may find it hard to be polite to these people.

If someone has contributed some "good" and "bad" ideas, consider acknowledging the "good" ones and, if necessary, indicating why some were "bad". (To soften your initial reaction, don't respond immediately and consider reevaluating what you consider "bad". See `Who’s running this content? </blog/newsletter-july-2017/#who-s-running-this-content>`__.) Consider communicating the focus of the documentation and documentarians' role in the company. You may get some ideas from `Help contributors think like users </blog/newsletter-june-2025/#help-contributors-think-like-users>`__.

If a person pushes back or frequently requests "bad" content, you and your team may need to set boundaries. (See `Setting boundaries </blog/newsletter-april-2023/#setting-boundaries>`__, which focuses on reviewers but may be relevant to unwelcome contributors.) To avoid personal confrontations, you may have to develop a workflow that addresses problems like this. For example, you could designate a single point of contact, specific dates to respond, specific types of legitimate requests, or procedures for documentation suggestions. (`Help your contributors help your project </blog/newsletter-december-2017/#help-your-contributors-help-your-project>`__ might be useful for procedures for problematic contributors.)

Some people disregard documentarians’ expertise and consider writing to be something that "anyone can do". These people regard their suggestions as better than what you or your team can produce, undermining your team's authority and credibility. Frequent pushback can cause stress and frustration, disrupting your team’s well-being and productivity. You may need to bring in management to support your team’s decisions rather than confronting these people directly.

See more Write the Docs resources about `working across roles </topics/#working-across-roles>`__.

---------------------------------------
Improving your API documentation skills
---------------------------------------

API documentation experience remains a common requirement in job postings, but the proximity to coding can make it seem daunting to learn. Fortunately, several free and lower-cost online courses are available to demystify the subject for people of all backgrounds and experience levels:

- `Documenting APIs: A guide for technical writers and engineers <https://idratherbewriting.com/learnapidoc/>`__ by Tom Johnson is a free online course that is especially good for putting beginners at ease.
- Peter Gruenbaum offers a handful of `API documentation courses on Udemy <https://www.udemy.com/courses/search/?src=ukw&q=peter+gruenbaum>`__ that are often discounted and provide 1- to 2-hour explorations of API documentation and related topics like programming for writers.
- The `Postman Learning Hub <https://www.postman.com/learn/>`__ is a free resource for learning APIs that includes a targeted `path for beginners <https://academy.postman.com/path/api-beginner>`__.

If you are a beginner and want to learn coding skills, consider these free online courses:

- `Computer programming - JavaScript and the web <https://www.khanacademy.org/computing/computer-programming>`__ and `Intro to computer science - Python <https://www.khanacademy.org/computing/intro-to-python-fundamentals>`__ from Khan Academy.
- `CS50x Introduction to Computer Science <https://cs50.harvard.edu/x/>`__ and `CS50P Introduction to Programming with Python <https://cs50.harvard.edu/python/>`__ from Harvard University (available via OpenCourseWare).

Writing API documentation also requires you to work in unstructured environments and to be curious and independent. The information you need is often scattered in many places and source content from developers typically presupposes a certain level of knowledge from users. Good API documentation depends on a writer who asks all the questions that users are likely to have and uses the answers to fill in the gaps.

Don't forget to check out the `WTD resources for API documentation </topics/#api-docs>`_!

--------------------------------------
Scaling beta docs without the headache
--------------------------------------

Rolling out beta features in docs is tricky: you need to guide customer experiments without cluttering production docs or creating a maintenance headache.

Some docs-as-code teams use a separate branch and staging site, granting beta customers gated access to specific docs. When features graduate from beta, the branch is merged into main.

You can achieve similar goals with tools such as MadCap Flare. Use these tools to publish conditionally, sending beta docs to a restricted site while maintaining public access for general content.

Other teams rely on in-doc disclaimers -- warnings that features are in beta (such as an example currently in `Flexera’s public docs <https://docs-snow.flexera.com/snow-atlas/user-documentation/saas/browser-extension/token-broker-proxy/#install-as-a-windows-service>`__). These disclaimers are easy to remove when no longer needed, but users often miss them. Pairing banners with notices in the UI or release notes enhances visibility.

Some organizations formalize beta stages with phased documentation:

* Pilot: No “real” docs; maybe just a PM-created PDF.
* Beta: Concise docs with disclaimers.
* General availability: Comprehensive documentation.

The common thread? Plan for the transition. Whether you branch, gate, or banner, treat beta docs as part of the release process, not an afterthought. A clear path from start to finish ensures your docs scale as smoothly as the product.

See more Write the Docs resources about `specific doc types </topics/#other-specific-doc-types>`__.

------------------------------
The effect of LLMs on docs use
------------------------------

Some documentarians have reported recent declines in traffic to their docs and have generally attributed it to users using large-language models (LLMs) and LLM-powered search engines to generate answers without coming to the docs directly. Others reported that their docs sites have not seen any difference, though they noted strong declines in visits to general tech journalism.

For some docs sites, rather than sites where the product is information, a decrease in traffic may not matter so much if people can still get the right information in a different way. If people learn how to use the product, it may not matter so much where they learned it from. Or if they can learn it all from the UI itself, perhaps from a built-in chatbot powered by information from the docs.

Other companies have long tracked conversions from their docs – they've seen how good docs can turn people into happy customers. So potentially having fewer people visiting the docs means fewer people using the product.

Some research has indicated LLM use was especially prominent among a more technical audience, who preferred to stay within their coding environment as much as possible. Some `other research <https://www.wired.com/story/the-less-people-know-about-ai-the-more-they-like-it/>`__ has indicated that those who know more about AI may be less inclined to use it.

However people consume the information, remember that high-quality docs are important for clear answers, whether the reader is a person or an LLM. Focus on presenting well-structured information to make it more likely that users can find accurate information however they look.

See more Write the Docs resources about `LLMs and AI </topics/#ai-and-llms>`__.

----------------
From our sponsor
----------------

This month’s newsletter is sponsored by `GitBook <https://app.gitbook.com/join?utm_source=writethedocs_ad&utm_medium=email&utm_campaign=adaptive_content_launch>`__.

.. image:: /_static/img/sponsors/gitbook_square.png
  :align: center
  :width: 50%
  :target: https://app.gitbook.com/join?utm_source=writethedocs_ad&utm_medium=email&utm_campaign=adaptive_content_launch
  :alt: GitBook logo

AI has changed the way people discover and use your documentation.

Your users want accurate information instantly, without scanning page titles in your sidebar. GitBook's docs sites include an `advanced AI Assistant <https://gitbook.com/docs/publishing-documentation/search-and-gitbook-assistant?utm_source=writethedocs_ad&utm_medium=email&utm_campaign=adaptive_content_launch?ask=What+can+GitBook+Assistant+do?>`__ trained on your content. Users get up-to-date answers from a trustworthy source — no extra tools or maintenance required.

You can even embed the AI Assistant in your product or website, so users can access your information without switching tools.

Best of all? When you sync user data with GitBook, the AI Assistant knows information like your users' pricing plans and feature access, delivering personalized answers for everyone.

This is a new era for documentation. `Sign up today <https://app.gitbook.com/join?utm_source=writethedocs_ad&utm_medium=email&utm_campaign=adaptive_content_launch>`__ and get started for free!

*Interested in sponsoring the newsletter? Take a look at our* `sponsorship prospectus </sponsorship/newsletter/>`__.

------------------------
Write the Docs resources
------------------------

Write the Docs offers lots of valuable resources related to documentation. See all of the Write the Docs `learning resources </about/learning-resources/>`__. To discuss any of these ideas or others related to documentation, join the conversation in the `Write the Docs Slack community </slack/>`__ in one of the many `channels </slack/#channel-guide>`__.

----------------
Events coming up
----------------

- 5 Sep, 08:30 EDT (US East Coast Virtual): `Social Hour for Documentarians <https://www.meetup.com/write-the-docs-east-coast/events/307540181/>`__
- 10 Sep, 17:00 CDT (Austin, USA): `Practical AI use cases for content folks <https://www.meetup.com/writethedocs-atx-meetup/events/310581466/>`__
- 11 Sep, 18:00 CEST (Amsterdam, Netherlands): `Do AIs dream of good docs? <https://www.meetup.com/write-the-docs-amsterdam/events/310748322/>`__
- 16 Sep, 19:00 MDT (Calgary, Canada): `What is documentation worth? Measuring the impact beyond words <https://www.meetup.com/wtd-calgary/events/304868570/>`__
- 17 Sep, 18:30 EDT (Pittsburgh, USA): `Panel Discussion: Real Talk with SMEs <https://www.meetup.com/write-the-docs-pittsburgh/events/310239988/>`__
- 18 Sep, 18:30 BST (London, United Kingdom): `Hardware Docs: Writing Device Manuals People Actually Want to Read <https://www.meetup.com/write-the-docs-london/events/310124578/>`__
- 19 Sep, 08:30 EDT (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/307540182/>`__
- 24 Sep, 17:15 AEST (Australia): `(Melbourne): Desktop processing, CHM files, and CDs: Tech writing like it's 2005 <https://www.meetup.com/write-the-docs-australia/events/309330640/>`__
- 3 Oct, 08:30 EDT (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/307540183/>`__
