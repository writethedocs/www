:og:image: https://www.writethedocs.org/_static/logo-opengraph.png

.. post:: December 02, 2025
  :tags: newsletter

#########################################
Write the Docs Newsletter – December 2025
#########################################

Season's greetings, documentarians! I hope you are finding joy wherever you are. At least something that gives you something to look forward to. Personally, I'm thankful for the Write the Docs community and how I can always learn from other people, even when I have less time or energy to contribute much myself.

If you're interested in the work that keeps the community going, check out the `Q4 Community Board update </blog/2025-Q4-community-board/>`__. Lots goes on behind the scenes to make everything we do possible.

As this is the last newsletter for the year, this is our last chance to remind you to fill in the `Write the Docs Documentation Salary Survey <https://salary-survey.writethedocs.org/>`__! The survey closes at the end of December, so if you haven't already contributed, please do so now. The more submissions we get, the more useful the results become, so if you're one of the fabulous people who have already participated, now would be a great time to mention it to your documentation-loving friends and colleagues. 

As noted in the board update, Hillary Fraley and Royce Cook are leaving the newsletter team this month. They have each brought unique perspectives to our monthly recaps, and I am sorry to see them go. If you're interested in being a part of the `newsletter team </team/#newsletter>`__, reach out to me (`@Aaron Collier`) on Slack.

Before leaving, they did leave us with some interesting insights this month. We have articles on the future of AI and documentation, the importance of code examples in developer docs, and documenting features still being developed. Enjoy!

----------------------------------
AI and the future of documentation
----------------------------------

As companies increasingly embrace AI, the documentarian role seems critical and precarious at the same time. Some think that technical writing is evolving into product information management. In this view, technical writers might focus more on information architecture and developer experience as they provide information to customers and AI systems alike. Ellis Pratt dug into the "docs product manager" concept in the post `Documentation product management: Does the AI era demand a new discipline? <https://www.cherryleaf.com/2025/10/documentation-product-management-why-the-ai-era-demands-a-new-discipline/>`__.

Others think that recent layoffs are a more realistic sign of what's in store, as more companies rely on AI for documentation. Companies may favor automated systems that generate documentation from existing resources, resulting in documentation that is good enough to avoid customer dissatisfaction and fewer roles for human writers, who are often already undervalued. Without advocacy, contributions from documentarians may be overlooked in favor of AI-generated content. Traditional documentation roles may become limited to high-value products and reduce job security for technical writers as AI becomes more prevalent.

Another perspective is that companies will always need documentarians to write documentation. LLMs depend on good documentation for training. In fact, AI tools are a new audience for documentation. People also turn to the docs when the answers they get from AI are insufficient. AI tools can draw incorrect conclusions, for example from outdated code comments, and produce inaccurate docs unless they are validated by knowledgeable documentarians. In addition, smaller and newer companies can compete with larger incumbents by focusing on quality and service, including perhaps by providing better documentation.

See more Write the Docs resources about `AI and LLMs </topics/#ai-and-llms>`__.

----------------------------------------------
Why code examples make or break developer docs
----------------------------------------------

In developer documentation, code examples are often presented as optional – a small snippet to illustrate syntax. But conversations across the Write the Docs community consistently show that examples are not decorative. They’re one of the most efficient ways developers learn, recall, and validate information.

Within our field, it’s become clear that examples exist on a spectrum of contexts, and each type serves a different reader need.

**Levels of code examples**

- Syntax Examples: Minimal inline snippets. Useful for quick reference, but often redundant in a world where IDEs surface syntax instantly.
- Contextual Examples: Snippets with realistic values or arguments. They answer the question, “What does this actually look like?”
- Usage Examples: Snippets doing something meaningful: imports, error handling, follow-up calls. These connect isolated knowledge to real workflows.
- Full Sample Applications: Runnable, end-to-end demos that reveal how everything fits together. Essential for onboarding, prototyping, and deeper comprehension.
- Error-Handling Examples: Examples that reflect real-world failure states, not just happy paths. An emerging expectation from developers.

**Why examples matter**

- Developers skim. A concrete example communicates more than paragraphs of explanation.
- Examples clarify intent. This is especially true for API docs where a concrete value such as `+14155551234` instantly shows developers the required phone number format (leading plus sign, country code, and no punctuation).
- Different audiences need different depths. Experts skim for confirmation, while newcomers rely on examples to learn.
- Good examples reduce support load, build trust, and dramatically shorten time-to-integration.

**Final takeaway**

Thoughtful examples don’t just support documentation – they complete it. Investing in the right mix of contextual, actionable examples turns conceptual understanding into actual capability.

See more Write the Docs resources about `code samples </topics/#code-samples>`__.

-----------------------------------------
Documenting features that don't exist yet
-----------------------------------------

Documenting non-existent features can be a high-risk practice. There are times, though, when it’s necessary — particularly if management is pushing it or the timeline is tight. If you have to do it, it helps to be aware of the benefits and risks involved.

**Benefits**

To document a non-existent feature based on a Product Requirements Document (PRD), documentarians must research its context within the product, understand the intended feature, and possibly suggest improvements. During the research process, discussions with SMEs may reveal questions or issues that help them develop the non-existent feature. If you can’t discuss the feature with a SME, consider adding comments with your questions or concerns that point to issues that developers need to address eventually. Draw on your experience to identify UI/UX issues and possible gaps or edge cases.

Preliminary documentation can help a Quality Assurance (QA) department develop product testing. Depending on the product, draft documentation can help train Customer Support personnel in time for product release.

**Risks**

A manager who wants progress updates may not accept “there’s nothing to document yet” and pressure the team to produce documentation that may not be useful. Draft documentation may be considered authoritative, which may be especially problematic if the PRD is not from the development team (if it is, say, a "wish" list from marketing).

An implemented feature may be quite different than the PRD or any technical specification. So someone needs to keep track of the progress (or lack thereof) because the draft documentation may be "wasted" work — needing significant revision. 

If the feature doesn’t materialize, any related content needs to be deleted. Someone may need to keep track of that deleted content just in case the feature eventually gets included. Realize that the "old" draft documentation must be evaluated against the actual feature before re-instating it.

**Summary**

Successfully documenting non-existent features requires knowledge of the risks, good collaboration with engineering, and careful version control of draft content.

See more Write the Docs resources about `working with other roles </topics/#working-with-other-roles>`__.

----------------
From our sponsor
----------------

This month’s newsletter is sponsored by `Gliffy <https://ter.li/ys85bx>`_.

.. image:: /_static/img/sponsors/gliffy.png
  :align: center
  :width: 50%
  :target: https://ter.li/ys85bx
  :alt: Gliffy logo

Gliffy helps busy teams communicate complexity through diagrams, featuring an intuitive drag-and-drop interface, Mermaid diagramming, and AI diagram generation all in one Confluence add-on.

By creating and managing diagrams directly in Confluence with Gliffy, you can eliminate knowledge silos and make documentation faster and easier to maintain.

Ready to transform your Confluence documentation? `Try Gliffy free <https://ter.li/ys85bx>`__ on the Atlassian Marketplace.

*Interested in sponsoring the newsletter? Take a look at our* `sponsorship prospectus </sponsorship/newsletter/>`__.

------------------------
Write the Docs resources
------------------------

Write the Docs offers lots of valuable resources related to documentation. See all of the Write the Docs `learning resources </about/learning-resources/>`__. To discuss any of these ideas or others related to documentation, join the conversation in the `Write the Docs Slack community </slack/>`__ in one of the many `channels </slack/#channel-guide>`__.

----------------
Events coming up
----------------

- 4 Dec, 18:00 GMT (London, United Kingdom): `Write the Docs Winter Social ❄️ <https://www.meetup.com/write-the-docs-london/events/311423344/>`__
- 11 Dec, 18:00 CET (Sweden): `The Documentarian's Toolbox: From Software to Soft Skills <https://www.meetup.com/write-the-docs-sweden/events/312153095/>`__
- 12 Dec, 08:30 EST (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/309520009/>`__
- 18 Dec, 17:00 AEDT (Australia): `Melbourne: End of year drinks <https://www.meetup.com/write-the-docs-australia/events/312243121/>`__
- 9 Jan, 08:30 EST (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/311760878/>`__
- 20 Jan, 17:30 EST (Pittsburgh, USA): `The Future of Writing and Writing Instruction in the Age of AI <https://www.meetup.com/write-the-docs-pittsburgh/events/312170362/>`__
- 22 Jan, 18:30 PST (San Francisco, USA): `The Content Playbook: Smarter Data, AI, Global Docs <https://www.meetup.com/write-the-docs-bay-area/events/311536701/>`__
- 23 Jan, 08:30 EST (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/311760881/>`__
- 6 Feb, 08:30 EST (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/311760883/>`__
