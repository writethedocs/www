:og:image: https://www.writethedocs.org/_static/logo-opengraph.png

.. post:: September 05, 2024
  :tags: newsletter

##########################################
Write the Docs Newsletter – September 2024
##########################################

Howdy, documentarians. I hope everything is going well in your part of the world. We're back from out regular August break and already setting records. So far, it's just heat records here, but maybe we'll set the record for most documentarians inspired this month.

In conference news, the Atlantic conference is coming up this month on 22–24 September. It's virtual so there's still time to get a ticket and you don't have to worry about travel. See the `planned talks </conf/atlantic/2024/speakers/>`__ and then `grab a ticket </conf/atlantic/2024/tickets/>`__. And if seeing the list of talks gets you more inspired, the deadline for `talk proposals for the Australia conference </conf/australia/2024/cfp/>`__ is this Friday (6 September). So get your ideas in while you still can! The speaker lineup will be announced by the end of September so you can start planning travel to the conference.

In other community news, check out the `Q3 update from the WTD Community Board </blog/2024-Q3-community-board/>`__ to see everything going on to make this wonderful community possible.

This month's newsletter has articles on editing difficult content from others, designing APIs to work well with docs, and dealing with employment gaps when job searching. Hope there's something to inspire you!

-------------------------------------------
Dealing with difficult-to-understand drafts
-------------------------------------------

If your work involves getting drafts from others, how do you edit content that doesn’t seem to make any sense? You’re expected to make the content readable, findable, and unambiguous in addition to applying company standards. You can’t do that if you don’t understand what you’re reading. Two issues can produce confusing content from subject matter experts (SMEs).

**The person who wrote the text isn’t fluent in English.**
The writer may be translating from their native language into English and not understand English grammatical rules. In trying to understand the content, it may be hard to know what the subject, verb, or other parts of speech are… or even if there are complete sentences. A related issue is when people write in their native language and then use translation software to convert it to English. The English words might be correct but mistranslations for the intended document.

If this is the case, you might need to ask clarifying questions. Some SMEs may "push back" and say that other SMEs will understand what they’ve written. They assume that their only audience is people with their backgrounds. You might have to remind them that others read and need to understand the content.

**The person who wrote the text isn’t a "good" writer.**
Even if they’re fluent in English, they may not understand how to write for others to understand — especially if their only formal writing experience is academic. They might use obscure words or a lot of unnecessary words. In this case, simplifying the words, moving the subjects and verbs closer together, and removing unnecessary words could be enough. 

You may have to deal with developer-oriented concepts and vocabulary that are unfamiliar. In this case, consider simplifying complex sentences and leaving the topic-specific, technical text as is. 

If the original writer just did a "brain dump", you may have to reorganize the content before editing it. One commenter used AI to group similar content to organize the text before editing it.

----------------------------
API design with docs in mind
----------------------------

This month, documentarians discussed what to prioritize when you get an opportunity to work with developers to shape new APIs. If you have a chance to make API design more documentation-friendly, consider advocating for these best practices:

* Use the `OpenAPI Specification (OAS) <https://www.openapis.org/>`_ to define APIs. The OAS provides a clear source of truth, allows customers and in-house developers to generate code from OAS files, and supports good documentation.

* Require descriptive, meaningful field names that do not use abbreviations or acronyms. For example, use "maximumQuantityToShip" instead of "maxQtySh". Pay special attention to Boolean fields to avoid unintuitive settings, such as `"cancel": false` actually meaning "yes, cancel this." Also, require consistent endpoint paths, ID names across endpoints, and patterns for things like pagination.

* Implement `contract testing <https://smartbear.com/blog/api-contract-testing-for-a-design-first-world/>`_ to ensure that all examples work as documented. Establish a process for adding examples to the tests as needed.

* Adopt an `API-first <https://www.youtube.com/watch?v=ODjX_3tGeeM&t=446>`_ approach: Designing APIs up front saves time and effort and ensures that the documentation is always up to date.

* Provide a Postman collection or other easy way to test each API. Postman collections and other such tools make it easier for writers to run every request to ensure accuracy before publishing documentation and help customers get started using the APIs more quickly.

------------------------
Handling employment gaps
------------------------

Documentarians discussed strategies for addressing employment gaps during job searches this month, offering valuable insights and support.

One key concern was the potential bias from recruiters and hiring managers against candidates with extended unemployment periods. The group shared several strategies for mitigating this:

**Highlight skill development**: If you've been learning new skills during your gap, make sure to include them on your resume. This not only shows that you've been proactive but also helps your resume perform better with applicant tracking systems, which scan for relevant keywords.

**Include volunteer work or contract projects**: If you've been involved in any volunteer work, freelance projects, or contract roles, list these experiences. They demonstrate that you've remained engaged in your field, even if you weren't in a full-time position.

**Be honest but strategic**: When addressing your gap, consider framing it as a period of self-improvement or career reassessment. For example, you might say you took time to decompress and rethink your career path before updating your skill set. This is particularly relevant in our post-pandemic world, where personal well-being is increasingly recognized as important.

**Resilience and realism**: The group also discussed the frustration of being labeled "overexperienced" by recruiters. Despite these challenges, the documentarians emphasized the importance of staying resilient, continuing to apply for roles, and adjusting expectations as needed.

When handling job gaps in technical writing, honesty paired with a focus on personal growth is key. By highlighting how you've used this time to develop new skills or engage in meaningful projects, you can turn a potential concern into a strength. Staying resilient, updating your resume strategically, and being prepared to discuss your gap with confidence will help you navigate the job market more effectively, positioning yourself as a dedicated and evolving professional.

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

- 5 Sep, 17:30 CDT (Austin, USA): `Write the Docs ATX Social Event @ Cherrywood Coffeehouse <https://meetup.com/writethedocs-atx-meetup/events/302810028/>`__
- 6 Sep, 08:30 EDT (East Coast Quorum, USA): `Social Hour for Documentarians <https://meetup.com/boston-write-the-docs/events/302738135/>`__
- 6 Sep, 17:00 WAT (Port Harcourt & Lagos, Nigeria): `Enhancing User Experience Through Collaboration Between UX Writers and Technical <https://meetup.com/write-the-docs-nigeria/events/303101526/>`__
- 10 Sep, 17:30 CEST (Stockholm, Sweden): `Write the Docs Sweden – The Reboot  <https://meetup.com/write-the-docs-stockholm/events/303072312/>`__
- 10 Sep, 18:00 CEST (Amsterdam, Netherlands): `AI: Do I trust it? <https://meetup.com/write-the-docs-amsterdam/events/302738047/>`__
- 10 Sep, 19:00 MDT (Calgary, Canada): `DITA Doesn’t Have to be Daunting <https://meetup.com/wtd-calgary/events/297725814/>`__
- 18 Sep, 19:00 EDT (Toronto, Canada): `Write the Docs Toronto  <https://meetup.com/write-the-docs-toronto/events/303126865/>`__
- 19 Sep, 18:30 BST (London, United Kingdom): `API products and their docs: when your product becomes a utility <https://meetup.com/write-the-docs-london/events/302428337/>`__
- 20 Sep, 08:30 EDT (East Coast Quorum, USA): `Documentarian Meetup <https://meetup.com/boston-write-the-docs/events/303156792/>`__
- 21 Sep, 10:00 MDT (Boulder/Denver, USA): `Documentarian Social <https://meetup.com/write-the-docs-boulder-denver/events/302850089/>`__
- 4 Oct, 08:30 EDT (East Coast Quorum, USA): `Documentarian Meetup <https://meetup.com/boston-write-the-docs/events/303217675/>`__
- 10 Oct, 12:00 AEDT (Australia): `(Virtual) From Markdown to Mic Drop: A Tech Writer's Guide to Presentations <https://meetup.com/write-the-docs-australia/events/302728564/>`_
