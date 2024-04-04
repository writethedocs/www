:og:image: https://www.writethedocs.org/_static/logo-opengraph.png

.. post:: April 04, 2024
  :tags: newsletter

#########################################
Write the Docs Newsletter – April 2024
#########################################

Hail to you, documentarians! I am writing with birds singing outside my window to celebrate the coming of spring (or so I tell myself). I hope you are able to find some sounds that bring you hope for the future.

In the near future, the `Portland 2024 conference </conf/portland/2024/>`__ is starting on April 14th. I hope all of you who are able to attend come away with amazing ideas and connections. For the rest of us, Write the Docs Atlantic 2024 has now opened `ticket sales and grant applications </conf/atlantic/2024/news/tickets-grants/>`__. Plus the `Call for Proposals </conf/atlantic/2024/cfp/>`__ is still open until May 15th, so submit your proposals while you can.

Speaking of conferences, we're furiously putting the finishing touches on the results of the 2023 Documentation Salary Survey so we can publish before the Portland conference starts. The most-ever responses for this survey has meant that there's been a mountain of really fascinating data to process, and we can't wait to share the insights with you! If you're going to be in Portland this year, we're also going to be running a Writing Day session to improve the clarity, inclusivity, and relevance of the questions. 

Our articles this month cover the value of measuring docs by readability scores, whether AI is speeding up docs creation, what questions to ask when hiring a documentarian, and whether and how to combine docs and code changes. I hope you enjoy and let us know what you're thinking about.

---------------------------------
Do Readability Scores Have Value?
---------------------------------

Readability scores (such as the Flesch–Kincaid Grade Level and Dale–Chall formulas) have been used for years in various sectors. But documentarians hesitate to use them to determine the readability of content. In a recent discussion, the general consensus focused on two potential issues:

- **Lacking value**: The scores assume readability can be reduced to simple measures such as length of words, length of sentences, or word choices from a prescribed list. Many readability scores were developed in the United States many years ago for specific audiences. They may not work with other domains or current audiences. 
- **Not addressing comprehension**: Just substituting a shorter word for a longer word may not help comprehension. Also, consistency may be more important than only shorter words.

How relevant are the scores for your audiences? If you score your content and it gets a low score, what do you do? You may edit the content to get a higher score, but did that actually improve the content for your audience? Possibly not… because documentarians must determine the best word choices for their audiences. One poster mentioned, "There seems to be some evidence that [adjusting for a readability score] can reduce comprehension." 

Would metrics (other than readability) work with documentation? One person suggested relying on objective metrics such as lack of typos, adherence to style, and correctness. Others suggested focusing on plain, simple language or measuring how long it takes someone to solve the problem that brought them to the documentation.

For information about readability, see `The Measurement of Readability <https://dl.acm.org/doi/pdf/10.1145/344599.344630>`__. If you've been asked to include readability scores and question their use, these resources may strengthen your position: `Readability formulas: 7 reasons to avoid them and what to do instead <https://www.uxmatters.com/mt/archives/2019/07/readability-formulas-7-reasons-to-avoid-them-and-what-to-do-instead.php>`__, `What makes writing more readable? <https://pudding.cool/2022/02/plain/>`__, and
`Redish on readability formulas <https://redish.net/wp-content/uploads/Redish_on_Readability_Formulas.pdf>`__.

-------------------------------------------
Accelerating Documentation Creation with AI
-------------------------------------------

Documentarians weighing whether to use AI tools in their workflows have many concerns to address, such as content quality, data security, and ethical implications. In many fields, accuracy and reliability are paramount and can't be sacrified for speed.

These topics were relevant to a recent thread in the `#ai channel <https://writethedocs.slack.com/archives/C1NEAD7D4>`__. The question was whether, as some `public commenters have claimed <https://twitter.com/samjulien/status/1765866411404976282>`__, AI can already speed up the creation of product documentation.

Some respondents were adamant that it doesn't help them. Some because their company's security policies forbid its use. Others found it useful for generic content, where it can act like a focused web search but without any ads, but not for specialized questions about a product. Others said it wouldn't help them because writing the first draft is how they learn about the product.

Some of the people who didn't find it personally helpful thought it might help non-writers or non-native speakers. People who struggle getting words on the page might benefit from the ability of large-language models (LLMs) to put together sentences in a commonly understood order.

Others were adamant that LLMs have really helped them speed up their documentation process. For security, it's important to choose a service that doesn't share prompts and responses with the LLM providers for training. 

Even in the best of circumstances, LLMs were compared to "extremely knowledgeable but inexperienced interns." They require dedicated focus and crafting of prompts and other tools to get them to do what you want. It can help to use `retrieval-augmented generation <https://stackoverflow.blog/2023/10/18/retrieval-augmented-generation-keeping-llms-relevant-and-current/>`__ to keep the LLM focused.

The discourse on AI's impact on documentation creation encompasses ethical, societal, and professional dimensions. By fostering ongoing dialogue and collaboration within the technical community, organizations can navigate the complexities of AI integration while promoting responsible and inclusive documentation practices.

----------------------------------
Questions To Ask as an Interviewer
----------------------------------

The WTD community offers valuable resources for job seekers, many captured in the `Guide to Hiring and Getting Hired </hiring-guide/>`__ and the `Getting Hired </topics/#getting-hired>`__ topics. This month in Slack, the focus shifted to the other side of the interview, as documentarians and managers listed their favorite questions to ask candidates. Here's a roundup of the questions they shared, along with any reasons they mentioned.

- How did you get into technical writing?

 - This is an easy starter question that gets candidates comfortable, gauges their enthusiasm for the job, and tells you about their career path.

- What do you do outside your regular role to advocate for your profession?

- Do you take the initiative on docs retros or create presentations for the team?

- Do you like to stretch beyond writing?

- What's one thing we're doing wrong?

- Tell me something about yourself that isn’t on your resume.

 - Answers are usually about hobbies or interests, but sometimes include jobs that aren't on the resume but are still interesting.

- What are the three most important skills that a successful tech writer possesses, and why?

- Tell me about a time you noticed a process that needed to be improved. What did you do about it? How did you implement a process change, if applicable?

 - These questions can lead to follow-ups like "What was your approach to getting the change implemented?", "What response did you get from colleagues?", and "How did you deal with any pushback?"

 - The follow-up questions provide a good idea of how the candidate handles change, how proactive they are, and how they approach collaboration beyond the daily job tasks, even if the change wasn't successful.

- How do you handle ambiguity?

 - This question gives candidates a chance to explain how they work with the best information they have at the time.

- What's exciting about this company?

 - This question tells you about the research the candidates have done and whether they're curious about the company and the job.

- What was your biggest on-the-job mistake and how did you handle it?

 - You might consider easing candidates' nerves about answering this question by sharing a mistake of your own.

-------------------------------
Drafting Docs with Code Changes
-------------------------------

A documentarian recently worried in the `#docs-as-code channel <https://writethedocs.slack.com/archives/C72NZ18FR>`__ about people combining changes to documentation in the same pull request (PR) as changes to code. They were concerned this would lead to lots of changes in one place, with many commits that would potentially overlap or cause confusion. It also could make it seem the docs were less valued since they don't get their own PR.

In the ensuing conversation, people noted that having both changes together was a great way to lower barriers to contributing, making it easier to get docs changes started. Another conversation noted how this goal of docs-as-code doesn't always work in practice, with not many contributions coming in. And sometimes the contributions that do come in take more time than drafting from scratch to get them to the right level of quality.

Our community members had some suggestions for overcoming issues. One was to set up clear contribution guidelines and standards to help keep the quality high. And then requiring a review against those standards from the docs team before publishing the docs changes. To avoid commits overlapping, people suggested setting up a branch off of the PR to focus just on docs changes. Then merging that branch into the PR before the final merge of the PR.

Some companies were noted as examples where this process has worked well. Their secret to success included documentation being a part of the company culture. When this is combined with clear reviews by specialized documentarians, they are able to get many contributions quickly while still maintaining quality standards.

----------------
From Our Sponsor
----------------

This month’s newsletter is sponsored by `Zoomin <https://www.zoominsoftware.com/>`__.

------

.. image:: /_static/img/sponsors/zoomin-2024.jpg
  :align: center
  :width: 75%
  :target: https://www.zoominsoftware.com/watch-a-demo?utm_medium=referral&utm_source=WTD&utm_campaign=march_newsletter&utm_content=watch_demo
  :alt: Zoomin is AI-infused content delivery

**Deliver a unified multichannel content experience with Zoomin**

Is your content scattered across a maze of separate sites? Are different teams creating their own content, using their separate authoring tools and publishing to siloed channels? A fragmented content experience is frustrating for users who are forced to context-switch and may be navigating outdated and inconsistent content.

`Zoomin <https://www.zoominsoftware.com/>`__'s content delivery platform helps you provide a seamlessly unified self-service experience to your users. We ingest your enterprise's entire corpus of content, no matter who created it or which  formats they use. We then surface it at every channel where your customers are looking for answers: your docs portal, developer portal, support site, inside your product and more. Sprinkle in some powerful search, navigation, personalization and AI capabilities and you have a truly effortless self-service experience. See `our product walkthrough <https://www.zoominsoftware.com/watch-a-demo?utm_medium=referral&utm_source=WTD&utm_campaign=march_newsletter&utm_content=watch_demo>`__ or `schedule a meeting <https://www.zoominsoftware.com/book-a-meeting>`__ to learn more.

------

*Interested in sponsoring the newsletter? Take a look at our* `sponsorship prospectus </sponsorship/newsletter/>`__.

----------------
Events Coming Up
----------------

- 5 Apr, 08:30 EDT (New England and Florida, USA): `Social Hour for Documentarians <https://www.meetup.com/boston-write-the-docs/events/299045879/>`__
- 10 Apr, 09:30  MDT (Boulder/Denver, USA): `Open Coffee Chat (Virtual) <https://www.meetup.com/write-the-docs-boulder-denver/events/299782120/>`__
- 14 Apr, 09:00  EDT (East Coast, USA): `Write the Docs Portland 2024 <https://www.meetup.com/virtual-write-the-docs-east-coast-quorum/events/299182314/>`__
- 14 Apr, 09:00  PDT (Portland, USA): `Write the Docs Portland 2024 <https://www.meetup.com/write-the-docs-pdx/events/299182334/>`__
- 17 Apr, 18:00  CEST (Amsterdam, Netherlands): `Drop In: restart meetup, get ready for AI <https://www.meetup.com/write-the-docs-amsterdam/events/300006153/>`__
- 19 Apr, 08:30 EDT (New England and Florida, USA): `Focused Conversation for Documentarians <https://www.meetup.com/boston-write-the-docs/events/299045881/>`__
- 30 Apr, 18:00  EDT (Pittsburgh, USA): `April Happy Hour - Write the Docs <https://www.meetup.com/write-the-docs-pittsburgh/events/300015446/>`__
- 3 May, 08:30 EDT (New England and Florida, USA): `Focused Conversation for Documentarians <https://www.meetup.com/boston-write-the-docs/events/299045882/>`__
