.. post:: May 3, 2019
   :tags: newsletter

####################################
Write the Docs Newsletter – May 2019
####################################

Hello everyone! It's Beth and the newsletter team here, with May's edition full of news and collected wisdom from the community Slack.

This month's biggest announcement is `the dates for Write the Docs Australia </conf/australia/2019/>`__. It'll be 14-15 November 2019, in Sydney. Save the date!

In the nearer future, `the Portland conference </conf/portland/2019/news/schedule-tickets/>`__ is coming up on 19 May. For those who can't make it, you'll be pleased to hear that we'll be live-streaming the conference again this year! `www.writethedocs.org/conf/portland/2019/livestream </conf/portland/2019/livestream/>`__ is the place to watch.

And if you're planning to attend one of our European conferences, now's a great time to buy tickets, which are on sale for `Vilnius </conf/vilnius/2019/tickets/>`__ and `Prague </conf/prague/2019/tickets/>`__. We're also delighted to tell you that `diversity tickets are available for Prague </conf/prague/2019/news/cfp-diversity-tickets/#diversity-tickets-initiative>`__!

Finally, just a reminder: If you spot something on Slack and you think, "That was interesting/useful/cool, we should save that", please go ahead and pop the ``:suggest-for-newsletter:`` emoji on it. That'll bring it to our attention, so we can consider it as a topic for a newsletter article!

Speaking of which, what interesting things have come up this month?

--------------------------------------
Collecting and acting on user feedback
--------------------------------------

This month, a Slack discussion produced a bonanza of insights into how documentarians collect and apply user feedback. Here's a roundup:

* Use Google Analytics to collect traffic information, so you can identify the best way to collect feedback. For example, if you have low traffic but high engagement, you might get great feedback from contacting users by email. See the `Docs by Design <https://docsbydesign.com/>`_ blog for more about tailoring your approach.
* Collect feedback with forms at the end of each page, or provide a feedback email address, chat widget, or survey link. Then sort and group into actionable doc improvements. Some suggested asking targeted questions or having users rank the page instead of requesting open-ended comments. 
* Use services like `MongoDB Stitch <https://www.mongodb.com/cloud/stitch>`_ to push docs feedback directly to a Slack channel.
* Allow users to directly log Salesforce cases/GitHub issues/Jira tickets.
* Contact users one-on-one to ask for feedback or arrange to receive regular ongoing feedback. Don't forget to close the loop: let these users know when you improve something based on their feedback.

The two biggest challenges were prioritizing feedback-based improvements without compromising ongoing documentation efforts, and finding the time to make use of the collected feedback. The main strategy people used for addressing these challenges was holding document improvement sessions to discuss and prioritize the backlog.

And of course, some WTD talks have covered user feedback too:

* `CSAT - what’s that? </videos/na/2016/csat-what-s-that-betsy-roseberg/>`_
* `Feedback handling, community wrangling, panhandling </videos/eu/2016/feedback-handling-community-wrangling-panhandling-chris-mills/>`_
* `You have already succeeded 2.0 </videos/eu/2017/you-have-already-succeeded-design-critique-guidelines-make-feedback-easier-2-0-christy-lutz/>`_

------------------------------------
Tips and tricks for producing videos
------------------------------------

Videos can be a great way of educating users, but it's not always easy to do them well, especially if you haven't worked on video before. Here are some tips from a recent community discussion:

* Keep in mind that videos are not a "quick project": they can be very time-consuming.
* Create a pipeline for video creation and production that suits your organization's specific needs.
* Consider developing a library of assets for videos and commit to maintaining it.
* Be sure to take up-front expenses into account, such as editing software or a higher-quality microphone.
* If you don't have the resources to produce full-fledged tutorial videos, consider shorter videos (five minutes or less) that serve as an introduction to draw the audience into the documentation.
* Collaborate with other teams! UX, Customer Support, Training, and other teams can all be valuable resources for videos.
* Many community members suggested that docs teams should only commit to video content if they have a dedicated person, or even team, to work on videos.

If you've got any more questions, head on over to `#video <https://writethedocs.slack.com/messages/CBZ41NZJS/>`_!

------------------------------------------------------
The variable fortunes of variable placeholders in docs
------------------------------------------------------

In code examples, you often need to put in placeholders for values that users must provide. But no matter what a hapless writer tries, it seems inevitable that users won't realise they need to substitute their own data. Here's a summary of the options that our documentarians have provided for their readers:

* Explain the values that must be replaced, followed by the example.
* Provide an example with placeholder values, then an example with (fake) real values.
* Format the placeholder text in italic, or write it in all caps.
* Surround the placeholder text with angle brackets.
* Beware of indicators that could be taken as part of the code syntax, like angle brackets or curly braces.
* Don't explain the values to be replaced, because you can assume your audience understands what to do.
* Implicit in the previous item, but explicit in the discussion: Know Your Audience!

And one person told the story of an API that, if a user copied and pasted the example code without substituting appropriate values, produced this error: "The user your_username is not a valid user. Did you forget to change the sample code to use your own username and password?”

--------------------------------
Developer to documentarian ratio
--------------------------------

This month, one community member was looking for ideas for when your company asks "Why aren't our docs as great as <other doc site>?" Especially if you don't have the resources you'd need to make something equivalent.

One approach is to find out how many people the other company puts on docs. For example, many folks find their docs being compared to Stripe's; but community members reported that Stripe's site is custom-built, with dedicated engineers as well as writers (plural, of course).

You can also try breaking down the work that's required to get there, and use that to ask for more people (or for the pressure to be taken off). With positive phrasing: "I'd love to do that! Now, here are the resources we'll need to make it happen."

But how many people *do* you need? The ratio of writers to developers varies hugely. `One survey of articles and forum posts <https://www.infomanagementcenter.com/publications/e-newsletter/cidm-enews-03-17/another-look-at-writer-to-developer-staffing-ratios/>`__ had found that between 1:7 and 1:12 was fairly standard, but community members reported ratios as high as 1:51.

It varies because needs vary: a developer team focused on performance improvements won't generate much doc work, whereas two working on big UI changes might create lots. Even with a great writer-to-dev ratio, if the team is building many complex features, writers may still struggle to keep up. Some thought that the ratio of writers to UX designers or product managers might match docs work generated more closely.

There's further discussion on the right ratio in `this blog post <http://www.agiledocumentation.co.uk/2016/04/what-is-optimal-writerdeveloper-ratio.html>`__, and `this post on Medium <https://medium.com/ixda-berlin/staffing-ratios-finding-the-right-balance-between-pm-ux-and-engineering-in-your-team-12ada861a1d0>`__.

---------
Job posts
---------

If you're in Seattle, this is your month!

`Technical Writer <https://jobs.writethedocs.org/job/106/technical-writer/>`__
 MCG Health, Seattle, full-time

`Programming Writer <https://jobs.writethedocs.org/job/103/programming-writer-amazon-alexa/>`__
 Amazon Alexa, Seattle, full-time

`Senior Programming Writer <https://jobs.writethedocs.org/job/104/sr-programming-writer-amazon-alexa/>`__
 Amazon Alexa, Seattle, full-time

`Technical Writer <https://jobs.writethedocs.org/job/107/technical-writer/>`__
 AWS, Seattle, full-time

`Senior Technical Writer - Cryptography Services <https://jobs.writethedocs.org/job/108/sr-technical-writer-cryptography-services/>`__
 AWS, Seattle, full-time

`Senior Programmer Writer <https://jobs.writethedocs.org/job/109/senior-programmer-writer/>`__
 AWS, Seattle, full-time

`Senior Technical Trailhead Content Writer <https://jobs.writethedocs.org/job/105/senior-technical-trailhead-content-writer/>`__
 Salesforce, San Francisco, full-time

*To apply for these jobs and more, visit the* `Write the Docs job board <https://jobs.writethedocs.org/>`_.

--------------------------
Community events coming up
--------------------------

- 6 May - Denver, CO, USA - `WTD and STC Dine-Around <https://www.meetup.com/Write-the-Docs-Boulder-Denver/events/261045278/>`__
- 7 May - Sunnyvale, CA, USA - `Sound talk: producing quality voice-over recordings <https://www.meetup.com/Write-the-Docs-Bay-Area/events/260295281/>`__
- 15 May - `India <https://www.meetup.com/Write-the-Docs-India/events/260664753/>`__ AND `Australia <https://www.meetup.com/Write-the-Docs-Australia/events/260302007/>`__ - Webinar: Season of Docs | Open Source journey
- 14 May - Louisville, CO, USA - `Defying the Status Quo: How a grassroots effort can transform an organization <https://www.meetup.com/Write-the-Docs-Boulder-Denver/events/261073983/>`__
- 15 May - Toronto, Canada - `What it takes to get a short story published <https://www.meetup.com/Write-the-Docs-Toronto/events/pcqbmqyzhbtb/>`__
- 16 May - Oakland, CA, USA - `Doc writing workshop for developers and engineers <https://www.meetup.com/Write-the-Docs-Bay-Area/events/260432676/>`__
- 18 May - Moscow, Russia - `Профессиональная трансформация технического писателя <https://www.meetup.com/Write-the-Docs-Moscow/events/260877795/>`__
- 20 May - Berlin, Germany - `Docs hack <https://www.meetup.com/Write-The-Docs-Berlin/events/hzmpsqyzhbbc/>`__
- 23 May - Munich, Germany - `Ensuring the quality of your documentation <https://www.meetup.com/write-the-docs-muc/events/261040426/>`__
- 28 May - Ottawa, Canada - `WTD Ottawa Shopify meetup <https://www.meetup.com/Write-The-Docs-YOW-Ottawa/events/xtcbgqyzhbsb/>`__
- 29 May - Arvada, CO, USA - `Docs and Drinks daytime edition <https://www.meetup.com/Write-the-Docs-Boulder-Denver/events/258571464/>`__
- 12 June - Manchester, UK - `Becoming a self-employed tech writer <https://www.meetup.com/Write-the-Docs-North/events/259954919/>`__
- 13 June - Paris, France - `Première rencontre WriteTheDocs Paris <https://www.meetup.com/Write-the-Docs-Paris/events/260964602/>`__

