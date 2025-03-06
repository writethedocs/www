:og:image: https://www.writethedocs.org/_static/logo-opengraph.png

.. post:: March 06, 2025
  :tags: newsletter

######################################
Write the Docs Newsletter – March 2025
######################################

Howdy, documentarians! I hope the upcoming equinox is bringing you hope, whether that's hope for warm weather after winter, cool weather after summer, a chance to catch a day of equal day and night, or anything else. We all need some hope for the future to keep us going, so I hope you find yours.

The Portland conference is coming up in just two months. So `get your tickets now </conf/portland/2025/tickets/>`__ and start planning for it. If you can't make it in person, you can now even buy a virtual ticket to watch the talks, interact with other attendees, and more. See `details about virtual tickets </conf/portland/2025/virtual/>`__.

To see how Write the Docs is managing this change along with the many others in the industry and community, check out the `Q1 update from the WTD Community Board </blog/2025-Q1-community-board/>`__.

This month's articles bring you insights on professional behavior in text communication, dealing with people who don't respond, getting the most out of weekly meetings, and where to put content you want to reuse in docs-as-code. Enjoy!

----------------------------------------------
Behavior in text vs in person in the workplace
----------------------------------------------

With the prevalence of online communications (such as Slack and email messages) at work, a recent discussion focused on differences between text-based and in-person (including video, such as Teams) communications. 

Some documentarians insisted that they communicate the same in person and in text. But many others indicated that they differentiate their styles. Often people make a concerted effort to be grammatically correct and polite when communicating about work online and feel that they’re more casual in face-to-face conversations.

Several mentioned that when communicating by text, they’re more focused and edit their text, while in person they may not be as focused and tend to "ramble". One issue is personal processing style. Some people prefer to communicate by text (async), which gives them time to process information. Others prefer the spontaneity of synchronous conversations. 

Others noted that they rely on vocal tone and body language when communicating in person. Sometimes emojis can relay that in text, but there are concerns about whether emojis get interpreted as intended. Alternatively, some people find it hard to evaluate the tone of text if emojis aren’t used: “Is this content passive aggressive or dead serious or what?”

Is it safe or proper to express one’s personality, sense of humor, and personal, non-work opinions at work? Some have a “what you see [or read] is what you get” attitude. Some indicate that they are more conscious of word choice and limit personal sharing when interacting at work -- unless they’re with work friends.

For those people who primarily work online, some expressed concerns about too many text messages and notifications or excessive use of emojis. They caution others to be sensitive to over texting: writing too much or too often. 

See more Write the Docs resources about `working across roles </topics/#working-across-roles>`__.

-----------------------------------------
Contending with unresponsive stakeholders
-----------------------------------------

When stakeholders like subject matter experts (SMEs) don't provide feedback, it can be difficult or impossible to stick to project timelines and meet your goals. To encourage accountability on docs projects, consider a policy that directly addresses what will happen when you can't get feedback form stakeholders.

Establishing a policy that specifies timelines for feedback can work well. The policy might be that after a certain number of unsuccessful attempts to obtain feedback, a project is moved to the backlog until the next planning cycle. For time-sensitive docs that can't languish in the backlog, the policy might be that the docs will be published as-is after a certain number of requests for feedback go unanswered.

Another option is escalating to a manager or leadership, but this tends to be less durable than formal agreements. Instead, consider developing a service level agreement (SLA) or project charter with the project owner that describes your expectations for stakeholder engagement and explains how the project will be reprioritized if feedback is not forthcoming. Project charters also encourage people to be more careful about the kinds of work they request and to see the work as a partnership.

Ticketing systems such as Jira can also help keep requests moving. When stakeholders don't answer a request for feedback, adding a note to the ticket and putting it in the "blocked" column creates a paper trail and sometimes gets a stakeholder's attention. And don't forget to publicly thank "friends of the docs" -- stakeholders and teams who provide feedback quickly, connect you with a useful resource, or are especially helpful or supportive in some way!

See more Write the Docs resources about `working with other roles </topics/#working-with-other-roles>`__.

---------------------------------------
Maximizing the value of weekly meetings
---------------------------------------

Effective meetings are essential for keeping documentation teams aligned, engaged, and productive. However, balancing efficiency with meaningful interaction can be challenging, especially for remote and distributed teams. To make the most of your meeting time, consider these practical strategies for fostering engagement, boosting productivity, and strengthening team cohesion.

- Maintain a consistent meeting cadence.

  - Keep a regular meeting schedule to foster team connection, particularly in remote environments.
  - Use meetings to check in, share updates, and reinforce team rapport.
  - Even if there are no pressing topics, use the time for casual catch-ups or knowledge-sharing.

- Introduce special topics and deep dives.

  - Alternate between standard updates and in-depth discussions.
  - Explore broader topics such as SEO strategies, competitor documentation analysis, or industry trends for professional development.
  - Encourage team members to lead discussions on topics relevant to their expertise.

- Incorporate structure and social elements.

  - Follow a structured agenda with backlog reviews, prioritization, and resolution of blocking issues.
  - Add social elements such as emoji-based temperature checks, show-and-share sessions, or kudos time to keep engagement high.

- Leverage retrospectives and knowledge sharing.

  - Conduct biweekly retrospectives to celebrate wins, discuss challenges, and brainstorm improvements.
  - Host Brown Bag sessions where team members present their work, promoting continuous learning.

- Optimize for productivity and flexibility.

  - Consider an “all-in-the-meeting” format, meaning setting meeting time for anything that needs to be read, to ensure required reading and action items are addressed efficiently.
  - Allow for casual discussions or early dismissals when topics are light to maximize time management.

By implementing alternating formats, structured agendas, and social engagement strategies, you can transform routine meetings into valuable, collaborative touchpoints that enhance productivity and team cohesion.

See more Write the Docs resources about `planning and how we work </topics/#planning-and-how-we-work>`__.

-----------------------------------------------
Where to keep content for reuse in docs-as-code
-----------------------------------------------

A recent question about `#docs-as-code <https://writethedocs.slack.com/archives/C72NZ18FR>`__ focused on whether to store content that would be available for reuse (through `transclusion <https://en.wikipedia.org/wiki/Transclusion>`__) together with the rest of your content (colocation) or in a separate directory (such as `_partials`). The asker felt strongly that a separate location was best, but was getting some pushback that developers not focused on writing would prefer colocation.

The arguments for a separate location included a greater sense of order, relief from fear that the snippets to include would be built as complete pages, and the use of import aliases to not have to worry about relative paths. One person offered the analogy of utility functions in code, which almost no one would advocate for colocating with code if they're reused in various files.

Not everyone immediately jumped in to support this as the right way to do things. Some pointed to colocation being more convenient in the short term. Others noted the need to consider that there is no single right way to approach any project like this.

One person advocated for always looking at the workflows that the solution should address. Who is going to be using these files? What exactly will they be trying to do with them? Addressing the bigger-picture questions first, without worrying about details like specific directories, helps you determine what will work best for your situation, including all of the people that will be working with the docs.

See more Write the Docs resources about `Where to keep content for reuse in docs-as-code </topics/#docs-as-code>`__.

----------------
From our sponsor
----------------

This month’s newsletter is sponsored by `Mintlify <https://mintlify.com/>`_.

.. image:: /_static/img/sponsors/mintlify.png
  :align: center
  :width: 50%
  :target: https://mintlify.com/
  :alt: Mintlify logo

Mintlify helps you create beautiful documentation that converts users.

Documentation is as important as the product, so we help your docs look polished and stay up to date without having to bug your engineers. From AI-powered writing assistance to Git syncing for better collaboration, Mintlify takes care of the technical details so you can focus on writing quality content.

We’re passionate about up-leveling docs across the board, so we created a technical writing guide for non-writers—give it a read and let us know if you have any suggestions!

*Interested in sponsoring the newsletter? Take a look at our* `sponsorship prospectus </sponsorship/newsletter/>`__.


------------------
Featured job posts
------------------

`Technical Copywriter <https://www.linkedin.com/jobs/view/4164570544>`__, RLE Technologies - *Remote*

*Interested in promoting your open position? See our* `job posting sponsorship </sponsorship/jobs/>`__ *for more details.*

------------------------
Write the Docs resources
------------------------

Write the Docs offers lots of valuable resources related to documentation. See all of the Write the Docs `learning resources </about/learning-resources/>`__. To discuss any of these ideas or others related to documentation, join the conversation in the `Write the Docs Slack community </slack/>` in one of the many `channels </slack/#channel-guide>`__.

----------------
Events coming up
----------------

- 6 Mar, 17:30 EST (Pittsburgh, USA): `March Happy Hour: Write the Docs Pittsburgh <https://www.meetup.com/write-the-docs-pittsburgh/events/306054807/>`__
- 7 Mar, 08:30 EST (US East Coast Virtual): `Social Hour for Documentarians <https://www.meetup.com/write-the-docs-east-coast/events/305065946/>`__
- 12 Mar, 18:30 CET (Berlin, Germany): `March Social: BRLO Charlottenburg <https://www.meetup.com/write-the-docs-berlin/events/306437391/>`__
- 19 Mar, 19:00 PDT (San Francisco, USA): `Live Technical Writing Lightning Talks + Food, Drinks & Networking Fun! <https://www.meetup.com/write-the-docs-bay-area/events/305994268/>`__
- 20 Mar, 18:00 CET (Stockholm, Sweden): `Let’s Talk Accessibility – A Must for 2025 and Beyond! <https://www.meetup.com/write-the-docs-sweden/events/306236318/>`__
- 20 Mar, 18:30 GMT (London, United Kingdom): `A Journalist's Guide to Telling Tech Stories <https://www.meetup.com/write-the-docs-london/events/306264460/>`__
- 21 Mar, 08:30 EDT (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/305065947/>`__
- 4 Apr, 08:30 EDT (US East Coast Virtual): `Write the Docs East Coast Virtual Meetup <https://www.meetup.com/write-the-docs-east-coast/events/305065949/>`__
- 8 Apr, 19:00 MDT (Calgary, Canada): `Write the Docs Calgary April 2025 Meetup <https://www.meetup.com/wtd-calgary/events/304868538/>`__