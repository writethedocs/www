.. post:: February 04, 2024
  :tags: newsletter

#########################################
Write the Docs Newsletter – February 2024
#########################################

Cheerio, documentarians.
I hope your year is off to a good start, full of interesting challenges to document
and supportive people to help get it done.

A very big thank you to everyone who filled out the 2023 salary survey and those who spread the word.
The final tally was a record 1,017 submissions:
938 from employees and 79 from contractors, freelancers, and self-employed people.
Processing is underway, but a little teaser for now:
One of the new questions asked how respondents felt about their job security compared to the same time the previous year.
In a potentially positive sign, 
54% said they felt the same level of job security, 31% said they felt more secure, and only 15% said they felt less secure.
We're on track to publish the full results towards the end of March.

The Australia 2023 conference wrapped up since our last newsletter.
If you missed it or just want to see all the exciting talks,
check out the `recap including links to videos </conf/australia/2023/news/thanks-recap/>`__.
Looking forward, the Portland conference is coming up in April.
See the `list of speakers </conf/portland/2024/news/announcing-speakers/>`__ and grab a ticket.

We've got articles this month on structuring content for LLMs, task-based documentation,
whether to outline before writing, and docs observability.
It's all possible thanks to our contributors, Alia Michaels, Hillary Fraley, and Royce Cook.
If you're interested in contributing yourself, whether regularly or just as a one-time special guest,
send a message in Slack to `Aaron Collier <https://writethedocs.slack.com/archives/DC5HWBL3G>`__.


-----------------------------------------------------
Structured Authoring and Large Language Models (LLMs)
-----------------------------------------------------

This month, the `Copilot for Docs <https://githubnext.com/projects/copilot-for-docs>`_ project inspired a discussion
about how AI will affect structured authoring.
As users increasingly rely on AI tools to interact with documentation,
they could be able to use targeted searches to retrieve the specific information they need.
How might this shift change the way we think about organizing information for users?
Will documentarians begin to use structured authoring specifically for AI?

Metadata that categorizes documents by purpose and structure may be important
because it could help AI tools return relevant information.
For example, a "How do I..." prompt probably means the user wants a how-to guide,
and "Why does..." probably means the user wants an explanation.
In the Copilot for Docs project, users could specify their desired level of detail
and indicate how much they already know to help control the results they received.

Another possibility is that some large language models (LLMs) could use a body of text that includes many types of information
and return responses based on words that the model expects should follow each other.
In this model, LLMs would not operate like search engines that respect metadata such as tags.

Still, responses from AI tools might be improved by the additional context that metadata provides.
For example, the Copilot for Docs project seems to have been tuned to return responses only from a repository's documentation.
A/B testing may be useful to determine whether and how metadata affects AI tool responses.

Some documentarians have already found that headings, chapters in transcripts, and topic size are important to response quality.
Perhaps instead of metadata, documentarians may focus more on standardizing terminology,
intentionally organizing content to help improve AI tool responses,
defining guardrails and rules, and manually reviewing the results and fixing gaps.
For more thoughts about technical documentation and AI tools, read `Why chatbots are not the future <https://wattenberger.com/thoughts/boo-chatbots>`__ by Amelia Wattenberger.

------------------
Task-Based Writing
------------------

A company’s documentation can conform to one of several different documentation strategies.
A recent discussion focused on pros and cons of two strategies: feature-based and task-based documentation.

- A company's feature-based documentation strategy can sell products.
  In this instance, product documentation becomes marketing material.
  This approach works for customers who want certain features and may know how to use them. 
- A task-based strategy can reduce support calls and help customers.
  Customers can learn how to do what they want to do or discover new things they can do. 

Feature-based documentation can be easier to write.
In some companies, developers write about the features that they work on.
Documentarians who work with feature-based documentation may start to address other customer needs
(such as with getting started or onboarding guides).

Depending on the complexity of the software,
some documentarians document some, but not all, use cases for task-based documentation… perhaps common or problematic tasks.
Some writers attempt to document all tasks.
For task-based documentation, UI tooltips may be seen as sufficient to document features.

If a company makes money from offering support services, feature-based documentation may be preferred.
But feature-based documentation may also occur because there is no emphasis on documentation quality…
possibly due to not knowing best practices such as focusing on the audience.

But what happens when documentarians see feature-based documentation
and know that a task-focused strategy would be better for the company’s customers?
Management may determine that there’s a need to "upgrade" from feature-based documentation but not know how to proceed.
One person used an incremental approach by learning the software, developing use cases, and gradually rewriting the feature-based content.
This worked because management could see the improvements in the documentation and their appeal to customers. 

To focus on customer needs, it can help to talk to end users or get information about support calls.
Posters recommended `Diataxis <https://diataxis.fr/>`__ and Dave Gash’s `article on information typing <https://medium.com/@davidagash/a-painless-introduction-to-information-typing-d06041013fd5>`__.
Janet Revell gave a `presentation <https://www.youtube.com/watch?v=N8QSq9mDjFw>`__ about reworking content at WTD Australia 2023.

----------------------------
To Outline Or Not To Outline
----------------------------

In the dynamic world of technical writing,
debate over whether or not to outline returns perennially.
The decision strikes a delicate balance between structure and adaptability,
catering to the specific demands of the document, the audience, and the ever-evolving nature of technology.

For many documentarians,
outlining is akin to constructing a sturdy framework for a complex edifice.
An outline serves as the architectural blueprint,
offering a systematic guide through intricate procedures and multifaceted software functionalities.
This structured approach is particularly useful when dealing with comprehensive manuals or documentation of complicated processes.
It provides a roadmap that ensures clarity, coherence, and completeness in conveying technical information.
When working with large documentation sets,
outlining can help maintain coherence.

In contrast, a decision for spontaneity in technical writing,
sometimes called “pantsing” (writing by the seat of one’s pants),
may be more common in continuous-development environments.
A rigid outline could be seen as stifling creativity and responsiveness
in scenarios where changes are frequent and adaptability is paramount.
Pantsing allows writers to dive into documentation without the constraints of a predefined structure,
fostering an environment where innovation can flourish.
Similarly, quick-reference materials may benefit from a more spontaneous, adaptable approach.

Other documentarians perfer beginning without an outline
because it gives them flexibility later in the process.
They add what information they have at the start,
feeling comfortable that they can always reorganize later
once they have more information.
They are hesitant to put in an outline without knowing how much content there will be.

Some documentarians opt for a middle-ground in navigating this decision-making process. They may start with a loose structure, allowing room for spontaneity, and iteratively refine the outline as the document evolves. This adaptive approach acknowledges the nuanced demands of technical writing, ensuring that both clarity and creativity are seamlessly interwoven in the fabric of effective documentation.

----------------------------------------
Measuring Docs Effect on User Experience
----------------------------------------

Some recent discussions in Slack have focused on how to measure documentation's effect on the user experience.
People were interested in going beyond page views and trying to demonstrate actual user value.
One contributor pointed to Bob Watson's `post on proving the value of documentation <https://docsbydesign.com/2022/02/13/proving-and-defending-the-value-of-technical-writing-again/>`__ as defining the problem well.

The discussion in the `#analytics channel <https://writethedocs.slack.com/archives/C5WF43X6G>`__ concentrated on what metrics to track.
Some ideas included correlating docs with support tickets,
such as how many tickets are created after reading a document
or how quickly tickets with links to documentation are resolved vs. those without.
If you're interested in how your docs contribute to getting new customers,
people also suggested looking at how many customers signed up after reading the docs as compared to the standard conversion rate.
One contributor cautioned to make sure to track support for existing customers as well,
such as how much of the docs traffic comes from signed-in users.
With all the different things to track, someone shared an `article about various metrics categories <https://document360.com/blog/value-of-documentation/>`__
and how to use them to demonstrate business value.

If you have an analytics tool for your product, it can help to use the same tool for your docs.
This works even better if people can log in to your docs
so you can connect reading the documentation to actions in your product.
You want to learn about a user's journey through your entire product, including the documentation as part of that.
Fabrizio Ferri wrote a post describing this combined approach as `docs observability <https://passo.uno/docs-observability-do11y/>`__.

In the end, the conclusion might be to look at what a successful user of your docs might do
and try to see how you could count it.
You can't count everything, but there is definitely value in what you can.

----------------
From Our Sponsor
----------------

This month’s newsletter is sponsored by `GitBook <https://www.gitbook.com/?utm_campaign=launch&utm_medium=email&utm_source=write_the_docs&utm_content=newsletter>`_:

------

.. image:: /_static/img/sponsors/gitbook.png
  :align: center
  :width: 75%
  :target: https://www.gitbook.com/?utm_campaign=launch&utm_medium=email&utm_source=write_the_docs&utm_content=newsletter
  :alt: GitBook logo

GitBook helps engineering teams create a single source of truth for their knowledge — with AI-powered integrations, search and insights that take the effort out of keeping documentation up to date.

With GitBook, you can add to your knowledge base from tools like Slack and VS Code, find information faster using AI-powered search, and use smart insights to find and fix old documentation with the latest data.
Take the effort out of technical documentation. `Get started with GitBook for free today. <https://www.gitbook.com/?utm_campaign=launch&utm_medium=email&utm_source=write_the_docs&utm_content=newsletter>`_

------

*Interested in sponsoring the newsletter? Take a look at our* `sponsorship prospectus </sponsorship/newsletter/>`__.

------------------
Featured Job Posts
------------------

- `Product Marketer (Technical Writer)  <https://jobs.writethedocs.org/job/2499/product-marketer-technical-writer/>`__,  Payara Services Ltd (Remote, Europe) 

*To apply for these jobs and more, visit the* `Write the Docs job board <https://jobs.writethedocs.org/>`_.

----------------
Events Coming Up
----------------

- 6 Feb, 18:30  EST (Washington, D.C., USA): `Write the Docs DC - Meet and Greet, 6 Feb 2024, 06:30 PM <https://www.meetup.com/write-the-docs-dc/events/298744146/>`__
- 9 Feb, 08:30 EST (New England and Florida, USA):  `Social Hour for Documentarians <https://www.meetup.com/boston-write-the-docs/events/298672206/>`__
- 22 Feb, 19:00  EST (Toronto, Canada): `Write the Docs Toronto  <https://www.meetup.com/write-the-docs-toronto/events/298941313/>`__
- 22 Feb, 17:30  AEDT (Australia): `Sydney: The "Tech Writing" book | Structured authoring <https://www.meetup.com/write-the-docs-australia/events/298003367/>`__
- 23 Feb, 108:30 EST (New England and Florida, USA): `Focused Conversation for Documentarians <https://www.meetup.com/boston-write-the-docs/events/298701579/>`__
- 8 Mar, 08:30 EST (New England and Florida, USA): `Focused Conversation for Documentarians <https://www.meetup.com/boston-write-the-docs/events/xzpxdtygcfblb/>`__
