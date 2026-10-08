:og:image: https://www.writethedocs.org/_static/logo-opengraph.png

.. post:: October 07, 2026
  :tags: newsletter

########################################
Write the Docs Newsletter – October 2026
########################################

Hi, everybody! Aaron and the rest of the newsletter team are back to bring you a roundup of interesting conversations from the Write the Docs community.

If you'd like to take part in fascinating conversations, the Australia conference just `announced its schedule </conf/australia/2026/news/announcing-speakers/>`__. So get your tickets (in-person or virtual) for your chance to discuss these and many other topics with fellow documentarians. For a taste of similar talks (but not the lovely hallway/Unconference conversations), see the `recap from the Berlin conference </conf/berlin/2026/news/thanks-recap/>`__, including the talk videos.

The Berlin conference was a great chance to meet people and spread ideas, including about the value of the `annual salary survey <https://salary-survey.writethedocs.org/>`__. We had a surge in responses from Europe during the conference and we'd love to keep the momentum going because more data helps everyone. If you haven't yet, fill it out today.

This month's newsletter brings articles on getting others involved in your docs, what to do about breaking changes when old versions will still exist, how to deal with a fear of being left behind by rapid change, and how AI dependency may be harmful (a topic which truly coincidentally fits with our sponsor this month). Enjoy!

-------------------------------
Getting others involved in docs
-------------------------------

If, as a documentarian, interactions with others are critical to your work, how do you get those people to work "for you"? Even if they need to contribute to or review your work, they have different priorities. You may need practical methods for engaging others and a perceptual change in your role—from "the person who does the docs" to someone "who authorizes documentation".

Visibility makes documentation-related requests harder to ignore. If you participate in product, engineering, and marketing meetings (or channels), your documentation focus gets noticed. You might create a documentation feedback channel where people can report issues and see them being addressed.

You may have to stop protecting other people from the consequences of not doing their part. If you step in and complete unfinished work, others will continue treating documentation as a low priority. If you establish clear public boundaries, it allows the consequences of inaction to become visible.

Telling people that they need to help isn't enough. If you give them a system that makes the work relatively easy, you’re more likely to get the help you need. This may involve developing templates or training, simplifying the style guide for contributors, or defining or automating a review process.

You may be in a situation where others agree that documentation is important, but their focus on other priorities leaves the documentation work undone. To establish documentation as a shared responsibility, you may need to educate others. Explain what good documentation should look like and establish a plan for getting there. Get the support of higher levels of management. Managers of other departments could make documentation contributions part of performance reviews.

As the documentarian, you may need to create expectations, processes, tools, visibility, and accountability for documentation to be a shared responsibility. Others need to understand what is expected, have the means to accomplish it, and experience consequences when responsibilities aren't met.

See more Write the Docs resources about `working with other roles </topics/#working-with-other-roles>`__.

-----------------
When “new” is old
-----------------

A lone writer recently asked the community how to keep docs evergreen through a breaking product change when some customers will keep using the old version and some will use the new one, without the difference being visible to customers. Their manager had suggested adding wording like "with the new version of X".

Most respondents agreed that time words such as “new” and “now” are best avoided in general documentation because they go stale, with release notes and “what’s new” pages as the lone exceptions. Phrases such as “the new version” assume readers know which version is new and can cause confusion if they don't follow your release announcements.

Instead, documentarians favored naming the change. If the release has a name, use it. If it doesn't, use a stand-in that points to the release the way a name would:

- **Version numbers**: Phrasing such as “as of version X” stays true and needs no cleanup later.  
- **Labels**: When a platform transition has no name or version numbers to point to, create labels for platforms, such as “legacy” and “new”, and state in each article which one applies. One team reported that this helps their AI agent tell the two apart.
- **Dates and compatibility**: Pair either option with “last updated” or “last verified” dates and a clear statement of which versions the page covers.

If you do opt for labels that will expire, such as “legacy”, ask how hard the cleanup will be once the old platform is retired and plan when and how to do it.

Docs outlive their writers and often pass through many hands. One member found a note in a current doc set saying a feature can “no longer” process files from “previous” releases. The oldest PDF of that doc set, from 1998, carried the same disclaimer. That's 28 years of “no longer”. Is there a “new” in your docs that's older than it looks?

See more Write the Docs resources about `specific writing questions </topics/#specific-writing-questions>`__.

-----------------------------------
Dealing with FOMO from rapid change
-----------------------------------

The community recently discussed the fear of missing out (FOMO) or being left behind by the rate of change with today’s technologies. Participants noted that it’s difficult to determine which current tools are worth following because they deliver consistent value to customers and which ones exist with unproven potential. One documentarian observed that agent-like concepts and technology date back to the 1960s, thereby illustrating the fleeting nature of in-demand tooling.

People shared a challenge with accessing the latest AI tools in the face of abrupt layoffs and experiencing stagnant conditions at companies that reject change. Just knowing AI or LLMs may not be enough for career advancement. Participants highlighted the value of being able to organize and consolidate information and write strong documentation.

However, people also noted the limits of relying on traditional writing practices. Some have found Claude and Gemini to be component producers of documentation, meeting notes, and other complex tasks. Embracing the strengths of newer tools can increase how much you can get done and expand your scope of knowledge/expertise. But it can be a lot to keep up with all the latest tools.

The discussion suggested some strategies for overcoming FOMO from rapid change:

- **A curiosity-based approach**: Exploring the latest tools and approaches helps cultivate a level of understanding to be prepared to adapt if or when change (such as a new AI model) is pushed down to the documentarian as the way forward. Documentation teams can experiment with different features to determine what is worth adding to their tool set.
- **A learning model**: Incorporating forward momentum in using the learning resources available can help you stay open to change. Feeling overwhelmed is often accompanied by a learning moment.

Participants agreed that it’s useful to step outside your perspective and ask what others around you are doing, which can lend inspiration and support as we all navigate the seas of change.

See more Write the Docs resources about `learning <https://www.writethedocs.org/topics/#learning>`__.

------------------------------------
What you may lose by depending on AI
------------------------------------

There’s a concern in the documentation community about using AI in a way that individuals lose more than they gain. The boundary between "AI-assisted writing" and "AI writing" may be difficult to recognize in practice. Writers may gradually move from prompting and editing content toward accepting AI-generated material with little oversight. In taking advantage of AI efficiencies, one might be sacrificing skills and knowledge. 

With "AI-assisted writing", documentarians automate repetitive tasks and use AI to help with grammar and basic writing issues (such as consistent tone, voice, and style). "AI writing" can remove the effort involved in drafting, revising, and polishing text; therefore, documentarians may get less practice writing, which weakens their ability to produce usable content from scratch. 

Writing forces documentarians to learn through practice. They clarify ideas, test assumptions, and develop a deeper understanding of their subject. If AI constructs the content, writers may lose that intellectual work ("cognitive surrender"). Without this effort, documentarians may not develop the expertise needed to question AI content effectively. 

AI-generated content still requires knowledgeable humans to evaluate it. A writer needs enough subject-matter knowledge to recognize incorrect assumptions, questionable claims, missing information, and inappropriate recommendations. One person described an AI-assisted technical project where a lack of vocabulary and background knowledge made it difficult to challenge the AI when it went down false paths. 

Documentarians attempt to produce comprehensive documentation for their audience. You might have to question: Does AI content focus only on the simplest use case? Are the reference docs comprehensive? Are nonstandard situations covered?

The use of AI is not good or bad, but there is a distinction is between using AI as an assistant and allowing AI to take over the writing process. Use AI to reduce the "grunt" work (grammar, tone, repetitive work, and similar tasks), but retain the activities that develop writing ability, subject-matter understanding, critical thinking, and judgment.

See more Write the Docs resources about `AI and LLMs <https://www.writethedocs.org/topics/#ai-and-llms>`__.

----------------
From our sponsor
----------------

This month’s newsletter is sponsored by `DoGBench from Promptless <https://dogbench.ai/?utm_source=writethedocs&utm_medium=newsletter&utm_campaign=2026-10>`_.

.. image:: /_static/img/sponsors/dogbench.png
  :align: center
  :width: 50%
  :target: https://dogbench.ai/?utm_source=writethedocs&utm_medium=newsletter&utm_campaign=2026-10
  :alt: DoGBench from Promptless logo

Can AI agents write documentation that an experienced technical writer would accept in review? We built DoGBench to find out, with Write the Docs community members and maintainers from Helm, PostHog, and Mautic. Each agent works through 292 real documentation tasks from open source projects, including some where the right answer is to leave the docs alone. The best of seven agents scored 47.3 out of 100.

If leadership is asking whether AI can take over your docs, these results give you measured evidence to bring to that conversation. The paper, the code, and 175 of the tasks are public, so you can check the work yourself. `See the results at dogbench.ai <https://dogbench.ai/?utm_source=writethedocs&utm_medium=newsletter&utm_campaign=2026-10>`__, from `Promptless <https://promptless.ai/?utm_source=writethedocs&utm_medium=newsletter&utm_campaign=2026-10>`__.

*Interested in sponsoring the newsletter? Take a look at our* `sponsorship prospectus </sponsorship/newsletter/>`__.

------------------------
Write the Docs resources
------------------------

Write the Docs offers lots of valuable resources related to documentation. See all of the Write the Docs `learning resources </about/learning-resources/>`__. To discuss any of these ideas or others related to documentation, join the conversation in the `Write the Docs Slack community </slack/>`__ in one of the many `channels </slack/#channel-guide>`__.

----------------
Events coming up
----------------

- 13 Oct, 18:30 CEST (Barcelona, Spain): `Barcelona WTD In-person Meetup <https://www.meetup.com/write-the-docs-barcelona/events/316777612/>`__
- 15 Oct, 18:00 BST (London, United Kingdom): `Community @ Unity: WTD London lightning talks showcase <https://www.meetup.com/write-the-docs-london/events/313761564/>`__
- 16 Oct, 08:30 EDT (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/311760897/>`__
- 22 Oct, 18:00 EDT (Pittsburgh, USA): `Making documentation AI-ready: How to expose your docs to modern AI agents <https://www.meetup.com/write-the-docs-pittsburgh/events/316313107/>`__
- 28 Oct, 18:30 CET (Munich, Germany): `🎃 WTD Munich: Behind the Scenes of Airports and APIs <https://www.meetup.com/write-the-docs-munich/events/316499656/>`__
- 30 Oct, 08:30 EDT (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/311760898/>`__
- 10 Nov, 19:00 CST (Calgary, Canada): `November 2026 Write the Docs Calgary Meetup <https://www.meetup.com/wtd-calgary/events/312192372/>`__
- 13 Nov, 08:30 EST (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/311760899/>`__
