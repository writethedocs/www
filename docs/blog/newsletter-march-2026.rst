:og:image: https://www.writethedocs.org/_static/logo-opengraph.png

.. post:: March 03, 2026
  :tags: newsletter

#########################################
Write the Docs Newsletter – March 2026
#########################################

Hello, fellow documentarians! The days are getting longer here, with more sunlight than we've had in months. Sometimes it helps to focus on what doesn't change. The sun is going to rise again tomorrow and I hope it will shine brightly on you.

The Portland 2026 conference announced its `lineup of speakers and talks </conf/portland/2026/speakers/>`__, so check them out and `get your tickets </conf/portland/2026/tickets/>`__.

The WTD Community Board had its quarterly meetings recently. Surprisingly, to increase efficiency, we actually doubled the number of meetings we had. And it worked! You can read about what we've been up to and what we have planned in the `Q1 Quarterly Update </blog/2026-Q1-community-board/>`__. Since those meetings, we've actually expanded the `newsletter team </team/#newsletter>`__ as well -- so welcome to our new contributors Felicity and Andrew!

This month's newsletter has articles on structuring docs for AI agents, creating de-personalized examples, how knowledge graphs might be useful for docs, and AI assistants in docs. Enjoy!

---------------------------------------
Should we structure docs for AI agents?
---------------------------------------

According to a recent discussion in the `#ai channel <https://writethedocs.slack.com/archives/C1NEAD7D4>`__, maybe! The discussion was prompted by an article: `Agent-Friendly Docs <https://dacharycarey.com/2026/02/18/agent-friendly-docs/>`__.

The article presents the findings that AI agents interact with docs very differently from humans. Agents are AI systems that can autonomously browse, retrieve, and act on information to complete tasks on a user's behalf.

The way agents appear to consume your docs may surprise you:

* They don't always search for your docs — They retrieve URLs from deep memory (sometimes from their training data!) or make poor guesses about the URL pattern.  
* They can't parse tabbed or drop-down content — Those beautifully organized procedures optimized for human readers collapse into walls of undifferentiated text for agents.  
* They can't finish long pages — Agents are configured to cut off after a default number of characters. Your longest page, no matter how well-structured, might not even make it to the table.

Agents make up a growing share of web traffic, and if you want your docs to appear in AI interactions (not everyone does!), there are few low-effort things you can do. A good starting point is implementing an `llms.txt file <https://llmstxt.org/>`__ -- a plain text file that tells agents where your content is and how it's organized. Note that agents won't find `llms.txt` files unless explicitly told they exist.

Not everyone was convinced that there's urgency to adapt docs for agent consumption, or that it's even worth the effort. Some argued that agent behavior is still too inconsistent and fast-changing to optimize for and that agents will eventually need to adapt to legacy docs, not the other way around. Others noted that many of the obstacles are infrastructure problems (how a CMS renders tabs or handles redirects) rather than writing problems.

The reassuring consensus: the actual content of good docs largely serves both audiences. Clarity, structure, and good semantics benefit human and agent readers alike.

See more Write the Docs resources about `AI and LLMs </topics/#ai-and-llms>`__.

-------------------------
De-personalizing examples
-------------------------

Effective documentation may require examples within the content. Documentarians must consider ways to protect the security and privacy of your company’s or other people’s information while maintaining clear and usable examples. A recent poster sought guidance on creating in-house guidelines about what would be considered private data (such as email addresses, API tokens, server names, and user IDs), how to mask or replace that data appropriately, and where these standards should be applied (for example, in textual content and screenshots).

For guidance on creating fictitious names, domains, and other sample data, contributors recommended consulting existing style guides (such as the `Red Hat Technical Writing Style Guide <https://stylepedia.net/>`_, `Microsoft Writing Style Guide <https://learn.microsoft.com/en-us/style-guide/welcome/>`_, `Google Developer Documentation Style Guide <https://developers.google.com/style>`_ and the `Splunk Style Guide <https://help.splunk.com/en/splunk-style-guide/welcome-to-the-splunk-style-guide>`_). See also the **General** resources at the end of this article.

Specific recommendations include using neutral or common placeholder names (such as Pat Smith) and internationally representative names where appropriate, clearly fictitious domains such as example.com, and obvious placeholder digits (for example, 0123456789 or repeated numbers). The discussion also advised avoiding copyrighted fictional characters and suggested, where appropriate, that example usernames reflect user roles (such as user or admin).

For visual content (such as screenshots), one person brought up a security consideration: blurred text in images can sometimes be reversed. Improperly applied redactions (such as overlaying black boxes without removing underlying text) can leave sensitive information accessible. For possible solutions, visit the links provided in **Images**.

Appropriate resources may depend on the type of documentation you produce for your company. Depending on your workflow and your access, you may need to consider content in source files, published files, web content, or comments in code. By developing a standards-based guide for your company, you can prevent accidental disclosure of private or proprietary information while maintaining realistic and meaningful examples in any documentation.

**General**

- `Resources for diverse example names <https://www.writethedocs.org/blog/newsletter-july-2020/#resources-for-diverse-example-names>`_ (Write the Docs Newsletter July, 2020)
- `A list of fictitious numbers, domains, and more <https://ddbeck.com/fictitious-numbers/>`_ (Daniel D. Beck blog)
- `Examples and placeholders <https://ocular-d.github.io/styleguide-editorial/examples-placeholders.html>`_ (Ocular-D Editorial Style Guide)
- `Example domains and names <https://developers.google.com/style/examples>`_ (Google developer documentation style guide)
- RFCs (Request for Comments, Internet Engineering Task Force)

  - `RFC 5737 - IPv4 Address Blocks Reserved for Documentation <https://datatracker.ietf.org/doc/html/rfc5737>`_
  - `RFC 3849 - IPv6 Address Prefix Reserved for Documentation <https://datatracker.ietf.org/doc/html/rfc3849>`_

- `Ensuring Privacy Compliance in Documentation: A Practical Guide <https://document360.com/blog/privacy-compliance-in-documentation/>`_ (Document360)

**Images**

- `Screenshot Security: Handling Sensitive Content And Privacy <https://cleariflow.com/blog/screenshot-security-privacy>`_ (Cleariflow)
- `How to Manage PII in Images for GDPR and Privacy Laws Compliance <https://www.redactor.com/blog/how-to-manage-pii-in-images-gdpr-privacy-laws-compliance>`_ (Sighthound Redactor)

**Developer Documentation** 

- `Code examples <https://learn.microsoft.com/en-us/style-guide/developer-content/code-examples>`_ (Microsoft Writing Style Guide)
- `Using Host and Usernames Correctly <https://stylepedia.net/style/#use-hostnames-correctly>`_ (Red Hat Technical Writing Style Guide)
- `Review Web Page Content for Information Leakage <https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/01-Information_Gathering/05-Review_Web_Page_Content_for_Information_Leakage>`_ (OWASP Foundation, Inc.)

See more Write the Docs resources about `style guides </topics/#style-guides>`__.

---------------------------------
Knowledge graphs in documentation
---------------------------------

A recent community discussion explored what it might mean to use knowledge graphs in documentation in practice. Some thought the term was rather abstract, but had some hope that the underlying ideas would be simpler and more practical than expected.

At a high level, a `knowledge graph <https://www.ibm.com/think/topics/knowledge-graph>`__ represents the relationships among related concepts. Each concept is represented as a node and the relationships between them are known as edges. This approach allows information to be explored in context and through relationships rather than as isolated pieces.

One commonly referenced example is `Wikidata <https://www.wikidata.org/wiki/Wikidata:Introduction>`__, which collects structured data representing links among items such as people, concepts, and events. These relationships can be used in a variety of applications, such as improving responses to knowledge queries and building privacy-respecting travel assistants.

In the context of documentation, most teams are not building full knowledge graphs. Instead, they apply the same thinking through intentional linking and structure. This often involves connecting related topics, concepts, and workflows across a documentation set.

Multiple people noted that they use a similar approach in their own personal writing, considering how each page they write relates to others. They did not think of this as building full knowledge graphs, but they still saw benefits in understanding similarities among concepts. They also saw some benefit from feeding the relationships to AI agents for more sophisticated results when searching for information.

This last benefit was something that people were working on for larger documentation sets as well. One participant described developing a knowledge graph so a support chatbot could use it to provide answers (a previous chatbot had used semantic chunking). They had created an `ontology <https://www.ibm.com/think/topics/knowledge-graph#:~:text=Ontologies>`__ and were working on implementing it and getting it ready to maintain. For more thoughts on how knowledge graphs can benefit documentation, see `an article from ClickHelp <https://clickhelp.com/clickhelp-technical-writing-blog/how-knowledge-graphs-can-improve-documentation-creation/>`__.

See more Write the Docs resources about `information architecture </topics/#information-architecture>`__.

---------------------
AI assistants in docs
---------------------

A recent question in the `#ai channel <https://writethedocs.slack.com/archives/C1NEAD7D4>`__ asked whether there was any data or research on user preferences for AI assistants vs. traditional docs?

Some observed that a `Model Context Protocol (MCP) <https://modelcontextprotocol.io/docs/getting-started/intro>`__ server can enable users to connect docs to their preferred tools, but most readers don’t know it exists or lack the infrastructure for it. One person noted an overall positive experience with having a chatbot linked to not only docs, but also forums and a community Slack, to give users more search options.

Others noticed value in people using a product’s in-docs chatbot to assess the product’s value before building with it. Product Managers and the legal team explore a product’s capability without wanting to build at all. However, everyone will have a context to drop docs into. Another person agreed that it’s a better investment long-term to bring docs to where people are. Providing an AI-powered chatbot on a docs site can source data through interactions with users on how to optimize docs.

Some recognized the increasingly common expectation for users to chat with docs like people converse with ChatGPT. With that mental model in place as a framework, an ideal AI chat solution can identify esoteric knowledge, integrate customer support tooling, and handle escalation flows.

People discussed user preferences for AI-first/AI assistant docs vs. traditional docs. Some highlighted a trend toward "answer engine optimization", meaning structuring content to maximize visibility in AI-powered search results. Tests are being run internally to identify which types of content people prefer. Meanwhile, others shared how knowledge bases have changed from having search bars to implementing conversational search.

The consensus was that AI chatbots are contributing to user satisfaction when navigating docs sites. These tools are helpful guides and streamline the search process for many people, but adoption of AI chatbots depends on identifying exact user needs and matching them with the appropriate product. There is a trend of companies supporting AI-first docs, but there are concerns about long-term reliability.

See more Write the Docs resources about `AI and LLMs </topics/#ai-and-llms>`__.

----------------
From our sponsor
----------------

This month's newsletter is sponsored by `Gliffy <https://marketplace.atlassian.com/apps/254/gliffy-diagrams-for-confluence?hosting=cloud&tab=overview&utm_source=write-the-docs&utm_medium=sponsored-content&utm_campaign=2025-gliffy-gliffydiagramsforconfluence&utm_content=atlassian-marketplace>`_.

.. image:: /_static/img/sponsors/gliffy.png
  :align: center
  :width: 50%
  :target: https://marketplace.atlassian.com/apps/254/gliffy-diagrams-for-confluence?hosting=cloud&tab=overview&utm_source=write-the-docs&utm_medium=sponsored-content&utm_campaign=2025-gliffy-gliffydiagramsforconfluence&utm_content=atlassian-marketplace
  :alt: Gliffy logo

Gliffy gives fast‑moving teams a clearer way to communicate complex ideas. Its drag‑and‑drop canvas, Mermaid support, and AI‑powered diagram creation all come together in a single, seamless Confluence app.

When your diagrams live directly inside Confluence, your documentation stays consistent, accessible, and far easier to keep up to date—no more scattered files or siloed knowledge.

If you’re looking to elevate the way your team documents and collaborates, explore `Gliffy for free on the Atlassian Marketplace <https://marketplace.atlassian.com/apps/254/gliffy-diagrams-for-confluence?hosting=cloud&tab=overview&utm_source=write-the-docs&utm_medium=sponsored-content&utm_campaign=2025-gliffy-gliffydiagramsforconfluence&utm_content=atlassian-marketplace>`__.

*Interested in sponsoring the newsletter? Take a look at our* `sponsorship prospectus </sponsorship/newsletter/>`__.

------------------------
Write the Docs resources
------------------------

Write the Docs offers lots of valuable resources related to documentation. See all of the Write the Docs `learning resources </about/learning-resources/>`__. To discuss any of these ideas or others related to documentation, join the conversation in the `Write the Docs Slack community </slack/>`__ in one of the many `channels </slack/#channel-guide>`__.

----------------
Events coming up
----------------

- 5 Mar, 18:00 CET (Amsterdam, Netherlands): `Two superpowers: developer docs and digital sovereignty  <https://www.meetup.com/write-the-docs-amsterdam/events/313410641/>`__
- 6 Mar, 08:30 EST (US East Coast Virtual): `Social Hour for Documentarians <https://www.meetup.com/write-the-docs-east-coast/events/311760885/>`__
- 10 Mar, 19:00 EDT (Ottawa, Canada): `Write the Docs Meetup – Annual General Meeting <https://www.meetup.com/write-the-docs-ottawa/events/313440478/>`__
- 12 Mar, 18:00 PDT (Seattle, Portland, & San Francisco, USA): `West Coast Super Meetup: Tom Johnson & Dave Nunez (Virtual) <https://www.meetup.com/write-the-docs-bay-area/events/313598292/>`__
- 18 Mar, 18:00 CDT (Austin, USA): `Show & Tell: How Are You Using AI for Docs? <https://www.meetup.com/writethedocs-atx-meetup/events/313592816/>`__
- 19 Mar, 18:30 GMT (London, United Kingdom): `Write the Docs: March event (Save the date!) <https://www.meetup.com/write-the-docs-london/events/313604884/>`__
- 19 Mar, 18:30 PDT (San Francisco, USA): `Technical Writing Career Growth in the Age of LLMs — Panel Discussion <https://www.meetup.com/write-the-docs-bay-area/events/312635049/>`__
- 20 Mar, 08:30 EDT (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/312057445/>`__
- 3 Apr, 08:30 EDT (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/312057453/>`__
