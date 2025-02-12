:og:image: https://www.writethedocs.org/_static/logo-opengraph.png

.. post:: February 06, 2025
  :tags: newsletter

#########################################
Write the Docs Newsletter – February 2025
#########################################

Ahoy, documentarians, and greetings in 2025! I hope the year is off to a splendid start for all of you, full of documentation projects so promising they almost complete themselves, just needing a little nudge from you.

We were saddened to start the year learning that the Society for Technical Communication is shutting down. We appreciate all the work they've put into sharing knowledge and building community over the years. We will keep up the work they started, making documentation and communication a highly valued part of industry, and continue to welcome any and all STC members into the community.

Our community is excited to welcome a new conference in Kenya this year. `Write the Docs Kenya 2025 </conf/kenya/2025/>`__ will take place on June 7 in Nairobi, Kenya. If you're interested, submit an `idea for a talk <https://sessionize.com/wtdkenya-conf/>`__. An announcement for speakers in `Portland </conf/portland/2025/>`__ will be coming soon, so keep an eye out for that.

The 2024 Salary Survey is now closed – a big thanks to everyone who participated! We're now hard at work crunching the numbers and will release the results before the `Portland conference </conf/portland/2025/>`__. 

For articles this month, we have thoughts on selling your work as a documentarian to others in your company, how to get better code documentation, the benefits and drawbacks to being a lone writer, and how to write for both AI and humans. Enjoy!

--------------------------------------------------------------------------
How to make your work as a documentarian shine: Beyond "just writing docs"
--------------------------------------------------------------------------

It's a common challenge for documentarians: underselling the complexity and value of our work. Once tasks start feeling like second nature, we start underestimating how much we contribute to organizational success. If you've ever thought, "I just write docs," it's time to shift that mindset. Here's how to frame your work in language that can help others see the impact you make.

- **Be loud and visible**: Visibility matters. Share your wins! Send monthly updates, create a quarterly newsletter, or give shoutouts in company-wide channels. Showcase not just what you did but how it made an impact – think before-and-after stories that illustrate real change.

- **Track and report everything**: Time-tracking, KPIs, and regular reports help you prove your worth. Document coaching sessions, workshops, and cross-departmental consulting. Use ticketing systems to create a paper trail of your efforts.

- **Embrace strategic terminology**: Think beyond writing and describe your work with terms that resonate with leadership. Use phrases like "stakeholder management," "internal consulting," "change management," and "scalability." You're not just documenting processes – you're enabling knowledge retention, improving self-service, and enhancing productivity across teams.

- **Tie your work to business value**: Executives care about outcomes such as cost reduction, scalability, and operational efficiency. Demonstrate how documentation reduces support tickets, speeds up onboarding, and eliminates knowledge silos. If you can quantify time saved or efficiency gained, you're sure to be heard.

In short, your work isn't just documentation; it's strategy, communication, and business transformation. Advocate for yourself and watch your value grow.

See more Write the Docs resources about `working with other roles </topics/#working-with-other-roles>`__.

-------------------------------------
Tips for improving code documentation
-------------------------------------

Recently, documentarians discussed best practices for improving source code documentation. Developers are usually responsible for documenting their own code. But some developers may not realize that others have to understand their code, they may not know how to write for others to understand their code, or they may not write well in English. Another developer (or a technical writer) may be asked to help (or teach) a developer to document code — especially if the code is complex — so others can understand the code. 

When developers document their own code, they’re immersed in writing the code and write notes to remind themselves about their process. They may assume incorrectly that what they’re doing is obvious to everyone. Code documentation for others (or the writer in 6 months after they have forgotten) may contain:

*   The general objective of the code segment.
*   If the code is complex, a comprehensive explanation.
*   Interactions or relationships with other code segments.
*   If the code is "unconventional", why certain choices were made (NOTE: This information may not be appropriate for all non-internal audiences).

Simplistic documentation of properties (for example, for a string property: `Specifies the name of the object`) might not be so helpful to someone else. Consider including more details about what the value could be and anything else needed for others to understand how to use the property.

To encourage developers to document code for others:

*   Have the developer return to the code after a period of time and see what they still comprehend. 
*   Have the developer write the documentation based on the specifications and then write the code. Correct the documentation as the code gets written and tested.
*   Include in developer productivity metrics a way to equate good code with good documentation.

See more Write the Docs resources about `specific doc types </topics/#other-specific-doc-types>`__.

-----------------------------------
The highs and lows of writing alone
-----------------------------------

Like anything else, being a lone writer comes with benefits and challenges. You often have end-to-end control over the documentation, making the decisions and setting the standards. It's satisfying to have such autonomy, and you may even get to lay the foundation for a future docs team. Yet, as rewarding as it is to have ownership, it can be a double-edged sword. When you're the only person working on the docs, you're responsible if something goes wrong.

Lone writers lack access to the range of skills and perspectives that comes with being part of a docs team. You don't have other documentarians to help with technical challenges or offer feedback on your decisions. It can also be difficult to get everything done, especially in a timely manner. Lone writers sometimes serve in hybrid roles (like engineer/writer or writer/developer educator) and write the documentation for multiple product teams, so they're often pulled in different directions. On the plus side, exposure to different roles and products can help you discover your strengths and passions.

For many, the advantages of being a lone writer outweigh the disadvantages, but much depends on the culture of the organization. For example, you probably won't be able to make much progress without your manager's support for your vision and approach. Still, within the right environment, being a lone writer can be a great opportunity.

See more Write the Docs resources about `career growth </topics/#career-growth>`__.

------------------------------------------------------
Writing AI-friendly *and* human-readable documentation
------------------------------------------------------

A recent discussion in the `#ai channel <https://writethedocs.slack.com/archives/C1NEAD7D4>`__ touched on how to write documentation that could easily be parsed by large language models (LLMs) but still be nice for humans to read. One participant pointed to a `recent somewhat infamous decision <https://github.com/MicrosoftDocs/WSL/pull/2021#issuecomment-2546627586>`__ to close a proposed change to the Microsoft docs because tables might not work well for an AI chat bot. But no one wanted documentation that was only for machines.

Multiple people commented that focusing on writing well for humans is the most effective way to make it usable for everyone, and everything. People focused on standard documentation practices, such as using structured writing and simple, clear language. Others noted that focusing on making your documentation accessible can also help, as good alternative text for images and clear labels can help tools that don't interact with the content in the same way as some humans.

Another strategy was to focus on semantics. This could involve exposing semantic types, rather than keeping them hidden in XML tags. It can also mean making sure you chunk your documentation based on meaning when using techniques such as `retrieval-augmented generation <https://en.wikipedia.org/wiki/Retrieval-augmented_generation>`__. Some thought focusing on traditionally structured documents would be enough to solve this.

If you work with a specific tool for chat, talk with the vendor about what works for that tool or check out their docs (such as the `recommendations from kapa.ai <https://docs.kapa.ai/blog/optimizing-technical-documentation-for-llms>`__). If you want to make your content generally available, consider an `llms.txt file <https://llmstxt.org/>`__. In most cases, if you do the minimum and focus on making your documentation useful to humans, the content will be able to shine in any interface.

See more Write the Docs resources about `AI and LLMs </topics/#ai-and-llms>`__.

----------------
From our sponsor
----------------

This month’s newsletter is sponsored by `Document360 <https://document360.com/signup/?utm_source=nl&utm_medium=write_the_docs>`_.

.. image:: /_static/img/sponsors/document360.png
  :align: center
  :width: 50%
  :target: https://document360.com/signup/?utm_source=nl&utm_medium=write_the_docs
  :alt: Document360 logo


Note from Saravana Kumar, Document360 CEO:

As organizations grow, so does the complexity of managing knowledge. At Document360, we believe a Knowledge Base should empower your customers & teams, not overwhelm them. That’s why we built a platform powered by generative AI to simplify how businesses create, manage, and share knowledge.  

Whether it’s a self-service knowledge base, API documentation, or SOPs, Document360 adapts to your needs – supporting private, public, and mixed silos seamlessly.  

Imagine a workday in which AI assists you in every stage of documentation creation, from generating content and suggesting titles to summarizing articles and even automatically creating FAQs, glossaries, and charts. That’s like hours freed up from your busy schedule!  

Whether you're in SaaS, IT, Fintech, Healthcare, or Manufacturing, Document360 helps you build a 24/7 consumable knowledge base that drives engagement and accelerates product understanding. 

If you want to simplify documentation and deliver real outcomes for your team and customers, I invite you to experience Document360. Start your `free trial <https://document360.com/signup/?utm_source=nl&utm_medium=write_the_docs>`__ today or schedule a `personalized demo <https://document360.com/request-demo/?utm_source=nl&utm_medium=write_the_docs>`__ with our solution experts. I’m confident you’ll see why it’s the preferred choice for technical writers worldwide.

*Interested in sponsoring the newsletter? Take a look at our* `sponsorship prospectus </sponsorship/newsletter/>`__.


------------------
Featured job posts
------------------

`Senior Technical Writer <https://jobs.smartrecruiters.com/Wise/744000034905081-senior-technical-writer-wise-platform>`__, Wise – *London, hybrid, 3 days in the office*

*Interested in promoting your open position? See our* `job posting sponsorship </sponsorship/jobs/>`__ *for more details.*

------------------------
Write the Docs resources
------------------------

Write the Docs offers lots of valuable resources related to documentation. See all of the Write the Docs `learning resources </about/learning-resources/>`__. To discuss any of these ideas or others related to documentation, join the conversation in the `Write the Docs Slack community </slack/>`__ in one of the many `channels </slack/#channel-guide>`__. That's where all the ideas in the newsletter come from.

----------------
Events coming up
----------------

- 6 Feb, 17:30 CST (Austin, USA): `Write the Docs ATX Social Event @ Cherrywood Coffeehouse <https://www.meetup.com/writethedocs-atx-meetup/events/305704589/>`__
- 7 Feb, 08:30 EST (US East Coast Virtual): `Social Hour for Documentarians <https://www.meetup.com/write-the-docs-east-coast/events/305065941/>`__
- 11 Feb, 19:00 MST (Calgary, Canada): `When the going gets tough: How to create great content with limited resources <https://www.meetup.com/wtd-calgary/events/304868525/>`__
- 17 Feb, 11:45 AEDT (Australia): `Virtual: Rethinking traditional approaches to release notes <https://www.meetup.com/write-the-docs-australia/events/305581219/>`__
- 20 Feb, 18:30 GMT (London, United Kingdom): `Support 🤝 Documentation: A Two-Way Street <https://www.meetup.com/write-the-docs-london/events/305977179/>`__
- 21 Feb, 08:30 EST (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/305065943/>`__
- 24 Feb, 12:30 IST (Tel Aviv+, Israel): `How to Make Great Instructional Videos <https://www.meetup.com/write-the-docs-taplus/events/305839803/>`__
- 25 Feb, 18:00 EST (Ottawa, Canada): `Write the Docs Ottawa Meetup <https://www.meetup.com/write-the-docs-ottawa/events/305729414/>`__
- 7 Mar, 08:30 EST (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/305065946/>`__
