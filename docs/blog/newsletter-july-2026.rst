:og:image: https://www.writethedocs.org/_static/logo-opengraph.png

.. post:: July 01, 2026
  :tags: newsletter

#####################################
Write the Docs Newsletter – July 2026
#####################################

Hello again, documentarians. Aaron here with the rest of the newsletter team to deliver insights from the community before taking a month off to refresh ourselves. In my case, it means finding somewhere to cool off for at least a little while.

In community news, see what the community board has been up to recently in the `Q2 quarterly update <blog/2026-Q2-community-board/>`__. Looking forward, the `Australia conference had its official launch </conf/australia/2026/news/welcome/>`__. Tickets and the Call for Proposals both open in July, so start your planning now. And the `Berlin conference announced its speakers </conf/berlin/2026/news/announcing-speakers/>`__ so you have a better idea of what insight to expect. And the `Kenya conference <https://www.meetup.com/wtd-kenya/events/314376384/>`__ is coming up in August if you can make that.

This month we have articles on how to go about reusing content, what to consider when consolidating from many sources to docs-as-code, how to make your workload visible as a lone documentarian, and how far to go to meet customer requests for their AI needs. We'll be back with more articles in September, so stay safe until then!

-----------------------------------
Developing a content reuse strategy
-----------------------------------

Content reuse, the practice of using the same content in multiple places, has been an ongoing topic for documentarians. For some, the reused content may be just product names. But many documentarians use boilerplate content (such as admonitions, paragraphs, or standard procedures) that must be consistent throughout documentation locations. Many teams use documentation platforms (such as `Paligo <https://paligo.net/content-reuse/>`__, `Docusaurus <https://docusaurus.io/docs/markdown-features/react#importing-markdown>`__, and `Flare <https://www.madcapsoftware.com/articles/the-elusive-promise-of-content-reuse/>`__) to support content reuse.

Successful content reuse requires a clear strategy — not just maximizing reuse. Minimally, writers must evaluate whether a piece of content is likely to require updates in the future. 

Sentence-level or phrase-level reuse can lead to unexpected results. It may introduce unnecessary complexity that makes documentation difficult to understand and complicates maintenance. Highly granular reuse can remove context needed by translators, which makes localization more difficult. (Some systems can combine reusable components with localization frameworks using variables, JSON files, and conditional content.)

It’s possible to use AI tools, such as `Claude Code <https://www.anthropic.com/product/claude-code>`__, to analyze documentation, identify reuse opportunities, generate snippet libraries, and assist with documentation restructuring. There are automated documentation systems where product metadata feeds directly into the documentation through variables and generated references.

If you’re considering content reuse:

- Determine whether your existing documentation tool or platform has reuse features. (If not, then you have to decide how to implement reuse.)
- Review existing documentation for possible content reuse. (This could be done by an AI agent or through a script.)
- Favor significant quantities of information over sentence fragments. 
- Design reuse with future updates in mind, rather than just current convenience.
- Consider the effect on localization, readability, and maintenance.
- Develop a documented content reuse strategy before any implementation.

Remember that a reuse strategy must be applied by ALL content contributors. Therefore, you may need to designate a "content reuse" expert or train contributors.

Well-implemented content reuse is a balance between efficiency and complexity. Content reuse can improve consistency, efficiency, and maintainability when applied properly, but it can create maintenance challenges if overused or poorly designed.

See more Write the Docs resources about `writing doc sets </topics/#writing-doc-sets>`__.

-------------------------------------------
Migrating from many sources to docs-as-code
-------------------------------------------

Raised recently in the `#lone-writer channel <https://writethedocs.slack.com/archives/CAL5Y0NB1>`__, but relevant to teams as well, is the question of how to migrate from multiple sources to docs-as-code. Your content might be spread across platforms such as Confluence, SharePoint, Zendesk, and help authoring tools such as MadCap Flare. Moving to docs-as-code can feel daunting because it's both a change in methodology *and* a new set of tools (see `some tools you might move to </guide/tools/>`__, which may influence the migration process). Add in juggling the migration of content from multiple sources and it’s hard to know where to begin. The community discussion centered on having a plan, working in chunks, and supporting people through the cultural shift. One community member stressed not to overlook the socialization and skills side: people resist change, so explain the big picture and benefits and offer education.

As with any large documentation migration project, start with a plan (or diagram) mapping the sources and how each will be migrated. Use a spreadsheet to manage everything: give each piece of content its own row, with columns to track its migration status. This makes it easy to report progress to management and to know what done looks like. 

Most people end up converting content to some flavor of Markdown because so many people and tools use it, though `AsciiDoc <https://asciidoc.org/>`__ and `reStructuredText <https://docutils.sourceforge.io/rst.html>`__ are also common, depending on how much structure you need, who is contributing, and what tools you use.

For the conversion process, automate what you can. Community members recommended using `Pandoc <https://pandoc.org/>`__ for the conversion, which can process docs in batches, though some preferred converting one at a time for greater control. Write scripts to remap internal links and relocate images. You may want to use AI tools to help with the mechanics, particularly writing conversion scripts and extracting content from PDFs. Keep a human in the loop because automated conversions across multiple sources are never straightforward.

The consensus in the thread was to work in chunks: migrate one source, tool, or product at a time. Treat the first as a pilot, running the entire process end to end: script the automation, migrate content, train staff, turn on the new source, and archive the old. Learn what didn't go smoothly, then refine before the next chunk.

Once a source is migrated, get the affected people onboard immediately. Move to the new repo straight away, and archive or lock the old location so nobody keeps working there out of habit. Then stay available for questions as people settle in. 

See more Write the Docs resources about `docs-as-code </topics/#docs-as-code>`__.

--------------------------------------
Making your workload visible to others
--------------------------------------

If you work alone on documentation within your organization, you may find it challenging to demonstrate all of the many things you are working on and so you may get requests you aren't able to handle. To get help with this, a question was posed in the `#lone-writer channel <https://writethedocs.slack.com/archives/CAL5Y0NB1>`__ regarding how to make your workload more visible to others.

When co-workers tag documentarians in various Slack threads without context, it can be difficult to communicate where a request sits within overall prioritization. Several respondents shared their experience applying project management strategies to raise awareness of what they are working on and the stage it is in. One uses weekly company-wide syncs to brief everyone on their work’s status and follows up with posts in relevant Slack channels. For them, this replaced the need for a project tracking system that is public within the company.

Other people preferred such a visible system in tools such as Trello or Linear. They also found that having a defined process for docs requests through their board made it more likely that others would see what else they were working on and also easier to gather the context they needed. This provided more helpful structure than a bunch of random asks in a Slack thread.

Others were less able to get time at company meetings and found their tracking boards weren't really visited. Someone noted that sharing daily goals, accomplishments, and work that’s in progress can help at times. Another person focused on finding the right Slack channel to celebrate a release, in this way thanking the people who helped and also announcing the change. This can help involve the right stakeholders.

Another lone documentarian described their success in giving a presentation on documentation at a company all-hands event. By explaining how quality docs support the business and rely on the experience and knowledge of everyone in company, they were able to move a little closer to others seeing that one person alone can't do all the docs and that they all can contribute.

See more Write the Docs resources on `working with other roles </topics/#working-with-other-roles>`__.

-----------------------------------------
Exporting Markdown documentation for LLMs
-----------------------------------------

Is it a good idea to provide customers with an offline Markdown export of product documentation? One documentarian was asked to do so to support a customer using it with an offline LLM, and so they turned to the WTD community for guidance. The response was that beyond just how to generate the files, it's important to also consider the practical challenges of maintaining the copies.

Keeping exported documentation up to date is not a trivial task. Large documentation sets can change frequently, making offline copies outdated almost immediately. Depending on the documentation platform, generating clean Markdown may also require additional tooling rather than being a built-in export option.

Copies might create the added responsibility of distributing updated exports. If you offer Markdown files, customers may expect ongoing maintenance. On the other hand, refusing the request doesn't necessarily stop customers from creating their own copies. They might do so by scraping your documentation with results that might be a worse version of what you can offer.

Can AI help? AI isn't the best tool for converting documentation. While AI can help generate scripts or automate parts of the workflow, deterministic tools such as `Pandoc <https://pandoc.org/>`__ or HTML-to-Markdown converters are generally more reliable, faster, and less expensive for large-scale conversions.

Some practical suggestions included:

- Treating Markdown exports as a premium offering with paid updates.
- Providing a one-time zipped Markdown package and making customers responsible for future updates.
- Packaging the documentation as a local Model Context Protocol (MCP) server for offline AI use.
- Preparing documentation for AI consumption by publishing Markdown versions of pages, providing an `llms.txt` file, or offering a "Copy as Markdown" option.

In many ways, the real challenge isn't generating Markdown, it's deciding who owns the ongoing maintenance and choosing a sustainable way to deliver it.

See more Write the Docs resources on `AI and LLMs </topics/#ai-and-llms>`__.

----------------
From our sponsor
----------------

This month’s newsletter is sponsored by `Biel <https://biel.ai/?utm_source=writethedocs>`__.

.. image:: /_static/img/sponsors/biel.png
  :align: center
  :width: 50%
  :target: https://biel.ai/?utm_source=writethedocs
  :alt: Biel logo

Your docs already have the answers, but your users just can't find them. 

Biel.ai adds an "Ask AI" button to your documentation, so users get the actual answer with the source cited instead of ten blue links. Every unanswered question lands in your dashboard, so the team sees what to write next. 

Works with Docusaurus, Sphinx, MkDocs, and 20+ others, plus one-click apps for Slack, Teams, and Discord, and an MCP server so your docs show up inside Claude, Cursor, and Copilot.

`Sign up <https://biel.ai/?utm_source=writethedocs>`__ in June to try Biel.ai for free for 30 days!

*Interested in sponsoring the newsletter? Take a look at our* `sponsorship prospectus </sponsorship/newsletter/>`__.

------------------------
Write the Docs resources
------------------------

Write the Docs offers lots of valuable resources related to documentation. See all of the Write the Docs `learning resources </about/learning-resources/>`__. To discuss any of these ideas or others related to documentation, join the conversation in the `Write the Docs Slack community </slack/>`__ in one of the many `channels </slack/#channel-guide>`__.

----------------
Events coming up
----------------

- 10 Jul, 08:30 EDT (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/313625241/>`__
- 16 Jul, 18:00 BST (London, United Kingdom): `Beyond Documentation: Building Immersive Learning with Docs-as-Code <https://www.meetup.com/write-the-docs-london/events/313761448/>`__
- 24 Jul, 08:30 EDT (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/311760892/>`__
- 30 Jul, 18:00 PDT (San Francisco, USA): `Write the Docs Bay Area Meetup — Sponsored by Twilio <https://www.meetup.com/write-the-docs-bay-area/events/315397626/>`__
- 7 Aug, 08:30 EDT (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/313625243/>`__
- 8 Aug, 08:00 EAT (Nairobi, Kenya): `Write the Docs Kenya Conference <https://www.meetup.com/wtd-kenya/events/314376384/>`__
- 8 Aug, 13:00 PDT (San Francisco, USA): `Write the Docs Bay Area Unconference! <https://www.meetup.com/write-the-docs-bay-area/events/315397820/>`__
- 20 Aug, 18:00 BST (London, United Kingdom): `Write the Docs London Summer Social 2026 <https://www.meetup.com/write-the-docs-london/events/313761542/>`__
- 21 Aug, 08:30 EDT (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/311760894/>`__
- 4 Sep, 08:30 EDT (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/313625244/>`__
