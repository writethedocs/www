.. post:: October 04, 2019
   :tags: newsletter

########################################
Write the Docs Newsletter – October 2019
########################################

Hi, everyone, and welcome back to the newsletter after our summer break!

Top news this month is our salary survey. It can be tough to work out what "normal" pay is, so Write the Docs is carrying out a `salary survey </surveys/salary-survey-sep-2019/>`__ to try to get some answers. The survey is open until 31st October, and we'll be publishing the anonymized data for free. Help the community and `fill it out here <https://www.surveymonkey.com/r/wtd-salary-2019>`__!

On the events side, I thoroughly enjoyed meeting so many of you at the Prague conference! If you missed it, don't despair, because `all the talks are now up on YouTube <https://www.youtube.com/playlist?list=PLZAeFn6dfHpkpYchP1iFnQnc7i-2xJd0I>`__ for your enjoyment. Plus there's one last conference to look forward to this year: we've announced the `speakers and schedule </conf/australia/2019/news/announcing-speakers/>`__ for Write the Docs Australia, coming up on 14-15 November. 

So that's all the news! On to the latest and greatest stories gathered from Slack.

-------------------------------------------------
Behind the scenes with fonts, emojis, and Unicode
-------------------------------------------------

This month, a question about icons and fonts provided a goldmine of information about emojis and unicode. Here are a few interesting facts:

* The "key" underneath all fonts is `Unicode <https://en.wikipedia.org/wiki/Unicode>`__. Fonts just provide glyphs for the underlying Unicode values - and different fonts can have different glyphs for the same Unicode.
* Fonts and typefaces are not the same! A typeface includes more than one font, as fonts are variations on the base (the typeface).
* In theory, two typefaces could have very different glyphs for the same Unicode code point, but it's more standardized these days.
* On a Mac, to get the correct glyph for a font, search in the `Character Viewer <https://support.apple.com/en-us/HT201586>`_ for the Unicode code. You can also mark your favorite emojis in Character Viewer to help you find them quickly.
* Many apps have an emoji menu (look under "Edit") that opens Character Viewer.
* Standard emojis have their own Unicode code points - check out the `full Emoji list <https://unicode.org/emoji/charts/full-emoji-list.html>`_.

Quite a few helpful links were also dropped into the discussion, including:

* `Mac 101: Inserting or typing uncommon characters <https://www.engadget.com/2010/10/11/mac-101-inserting-or-typing-uncommon-characters/>`_ by Steven Sande
* `Inserting Symbols is harder in Office for Mac <https://office-watch.com/2017/inserting-symbols-is-harder-in-office-for-mac/>`_
* `CodePen for Material Icons codes <https://codepen.io/btn-ninja/pen/YrXmax>`_

--------------------------------------------
Feeling like a fraud and how to deal with it
--------------------------------------------

It's totally normal to sometimes feel overwhelmed and to doubt your abilities - especially if you're writing about unfamiliar products. But there are lots of ways to get back on track. Here are some the community suggested:

* Insert a hypothetical user into the conversation. That way you function as a user advocate, re-engineering the docs to meet users' needs and wants. For example, asking "If a user tried to follow these instructions as they are, what info would they be missing?"
* Talk to product managers, subject matter experts, and customer support. These roles may have more information about the users' requirements.
* Establish some clear, short-term deliverables for your work, to get some early wins and regain confidence.
* Remember that you took time to learn the things you already know, so don't feel discouraged when you feel like you can't grasp new material instantly. This work is difficult! Step-by-step, you'll eventually understand the product and get the knowledge you need.
* Make a list of skills and knowledge that you feel you're missing, and then work out what you'd need to do to fill the gaps. Or, make a list of specific, concrete things you want to achieve, have achieved, expect to achieve. Involve your manager so you can turn them into actionable goals. Success is a work in progress.

  If you're interested in setting clear actionable objectives to improve your performance, check out the `SMART criteria <https://en.wikipedia.org/wiki/SMART_criteria>`_.

-------------------------------------------------------
Leading and following: finding a mentor, being a mentor
-------------------------------------------------------

Another great way to build both your confidence and your abilities is to find a mentor, as we discussed recently in  `#career-advice`. General agreement that having a mentor is A Very Good Idea led to some handy info:

* In the UK, the ISTC has a lightweight `mentoring program <https://www.istc.org.uk/professional-development-and-recognition/mentoring-scheme/>`__. One program participant explained that there aren't many guidelines, so they set up a development plan with their mentee and gave feedback on the mentee's CV.
* It can help to draft a development plan to show to a potential mentor, so they know what you're looking for. For ideas, see the ISTC's `Example CPD Records <https://www.istc.org.uk/professional-development-and-recognition/continuing-professional-development/example-cpd-records/>`_.
* Some companies provide formal mentoring programs: people who want to mentor sign up and describe their expertise, and you contact them if you want to be mentored. These programs typically provide internal resources for mentors and mentees as well.
* A useful article: `How to Email a Potential Mentor the Right Way <https://www.themuse.com/advice/be-my-mentor-craft-the-perfect-email-to-someone-you-admire>`__.

A couple of contributors suggested that WTD start its own mentoring program, which sounds like an idea we'd love someone to take on! If you're interested, `#meta` is a good place for that conversation. And if this topic captures your interest, see Arran Southall's talk from Prague this year, `Fostering Talent: Mentorship, Peer Reviews and Going Beyond Your Job Description <https://www.youtube.com/watch?v=rom6UW-TjNc&list=PLZAeFn6dfHpkpYchP1iFnQnc7i-2xJd0I&index=18>`__.

(Side note: One *could* argue that we shouldn't use the term "mentee". Classically speaking, the right word for someone being guided by a Mentor is, of course, a "`Telemachus <https://en.wikipedia.org/wiki/Mentor_(Odyssey)#Mentor_as_term>`__".)

-------------------------
Deciding on a new tool...
-------------------------

If you're struggling with the limitations of your docs tools, how do you decide what system to migrate to? In a recent coversation about trying to replace an old CMS, documentarians on Slack compared MadCap Flare, Paligo, static site generators and Adobe Suite, among others.

There was some consensus around establishing your specific business requirements before selecting a tool. What outputs do you need to publish? How much do you need to reuse content? Does OS compatibility matter? How long will migration take? The requirements matter because no single tool is right for all situations. If you understand your needs well, it'll really help - you might even realise that you don't need to switch.

Separating features into must-haves and nice-to-haves makes evaluating tools easier. Take care not to get side-tracked by features that don't address an actual need you have! Someone posted a useful `list of features <http://lauriston.com/requirements_sanitized.pdf>`__ to use as a starting point for your own evaluation.

There are many tools out there, and no one size fits all; make sure you know what you need before picking one.

--------------------------------
... and migrating to a new tool
--------------------------------

Migrating docs from one tool to another is hard, and the bigger the doc set, the harder it is. On top of the technical challenges, there can be content problems too: what do you do if the docs are in dire need of revision?

* The community agreed that it's not wise to try to improve docs as the same time as moving. Migrations are hard enough as it is! Better to resist the urge to edit as you go, and improve things in a second phase after the move.
* Alternatively, weed your docs beforehand. Carry out a content audit to make sure what you're moving is worth the time and trouble. Some bad content you can abandon and start over.

  Some useful rubrics:  ROT (Redundant, Outdated, Trivial); OUCH (Outdated, Unneeded, Current, Have to write); MUSTY (Misleading, Ugly, Superseded, Trivial, Your collection has no need of this - discard it!).
* Everyone agreed they'd underestimated how long a migration would take. Consider migrating in stages, starting with pilot docs that you're confident will work well in the new tool. This lets you learn about problems nice and early. Ideally the pilot docs should have updates on the horizon but not imminent - it'll take longer to move than you think.
* Be wary if you're expected to keep up your normal work at the same time. Lots of people recommended having headcount dedicated to the task. It's often a good subject for contractors or interns, because the projects don't require that much context.

If you're looking for somewhere to chat about these decisions, head over to `#doc-tools`!

-------------
Featured jobs
-------------

* `Documentation Engineer <https://jobs.writethedocs.org/job/146/documentation-engineer/>`__
   Balena, remote
* `Technical Writer <https://jobs.writethedocs.org/job/152/technical-writer/>`__
   Memsource
* `Senior Technical Writer <https://jobs.writethedocs.org/job/148/senior-technical-writer/>`__
   Kiwi.com, Brno or Prague, Czechia

*To apply for these jobs and more, visit the* `Write the Docs job board <https://jobs.writethedocs.org/>`_.

--------------------------
Community events coming up
--------------------------

- 10 October - Wylie, TX, USA - `Doc discussions <https://www.meetup.com/wtd-dallas/events/nmnzfryznbnb/>`__
- 15 October - Austin, TX, USA - `Five things to learn from LEGO <https://www.meetup.com/WriteTheDocs-ATX-Meetup/events/265378713/>`__
- 17 October - Denver, CO, USA - `Hacktoberfest 2019: An evening of open source collaboration <https://www.meetup.com/Write-the-Docs-Boulder-Denver/events/265316110/>`__
- 24 October - Austin, TX, USA - `Happy hour meetup <https://www.meetup.com/WriteTheDocs-ATX-Meetup/events/265298604/>`__
- 24 October - San Francisco, CA, USA - `How and why one company built a documentation app, with Ember.JS <https://www.meetup.com/Write-the-Docs-Bay-Area/events/265079568/>`__
- 29 October - Ottawa, Canada - `Shopify meetup <https://www.meetup.com/Write-The-Docs-YOW-Ottawa/events/xtcbgqyznblb/>`__
- 29 October - Toronto, Canada - `Write the Docs Toronto <https://www.meetup.com/Write-the-Docs-Toronto/events/pcqbmqyznbvb/>`__
- 29 October - Karlsruhe, Germany - `AsyncAPI Swagger for MQTT? Automated documentation of event-based APIs <https://www.meetup.com/Write-the-Docs-Karlsruhe/events/264985964/>`__
- 30 October - Chicago, IL, USA - `October meetup <https://www.meetup.com/Write-the-Docs-Chicago/events/263576196/>`__
- 05 November - Tel Aviv, Israel - `GitHub and Jira and Docs - oh my! <https://www.meetup.com/Write-The-Docs-TAplus/events/265349233/>`__
- 06 November - Leeds, UK - `Take a deep dive into Antora <https://www.meetup.com/Write-the-Docs-North/events/265096599/>`__
