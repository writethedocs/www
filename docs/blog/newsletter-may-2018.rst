.. post:: May 3, 2018
   :tags: newsletter, AB testing, imperatives, API definitions


####################################
Write the Docs Newsletter – May 2018
####################################

Hello everyone!

Kelly O. here, hoping it's been a good week for you all. We're just a few short days out from our first conference of the year. The Portland event marks the beginning of the community's busiest year yet!

The Prague conference may seem a long way off, in September, but the CFP is only open for a few more weeks. If you're interested in speaking, `have a look at the guidelines and submit your proposal <>`_ by **midnight CET on May 15th**. As usual, we're interested in speakers of any experience level on any topic relevant to software documentation. Hit us with your best ideas!

We also have two other Write the Docs events to look forward to in 2018!

* On DATE TK, Write the Docs is teaming up with OpenHelp, an annual SPRINT EVENT DETAILS TK to put on a DAYS TK event in Cincinnati. MORE DETAILS TK
* Then from OTHER DATES TK, Write the Docs Australia will be returning for a second year as a full two-day event MORE DETAILS TK

In addition, our network of meetups is alive and busy! For example, the `London group <>`_ is partnering with the `UK Government Digital Service <>`_ to put on a full-day meetup on June 5th about building a career in documentation. One of the organizers is running a short survey about documentation roles, in order to present his findings at the event. If you have a few minutes and want to participate, you'll find it here: `LINK TK <>`_

*Full disclosure: I am one of the co-organizers of the London meetup group. If you run a meetup and ever need community-wide exposure for a project or a community event, feel free to drop me an email at: `newsletter@writethedocs.org <mailto:newsletter@writethedocs.org>`_ I'm happy to help boost the signal.*

Now, after all that excitement out in the physical world, let's have a look at what folks have been talking about in the virtual one.

-----------------------------
A/B testing for stronger docs
-----------------------------

Measuring doc success is an evergreen topic on Slack. This month's installment started with a question about the possibilities of A/B testing your docs. It produced a nice range of thoughtful responses, from recommendations for tools to more detailed ideas about measuring the effectiveness your documentation updates:

* One contributor described a small-scale, hands-on approach that provides an old doc to a small sample set and asks the sample members to perform a specified task according to the doc. Measure how long it took them to complete the task, then run the same study again with the new doc and a different sample set of readers/testers. Reduced "time to competency" = increased doc efficacy.

* If you'd rathe run full on A/B testing out in the wild (as opposed to a controlled test environment), you might want to look into marketing tools like `Optimizely <>`_. Caution, though – you need upwards of 50 users to get anything like a valid indication, and much higher is better.

* A modicum of statistical savvy is useful when designing your A/B tests. If you're measuring a big difference between docsets, a smaller test population can give you useful insights. If you've trying to assess the effect of smaller changes, you need a larger test population. And it's important to know just what it is you expect to change – time to complete a task, improved expressions of customer satisfaction, something else.

* When trying to ascertain results, beware of relying on traditional web analytics. Bounce rate/time on page, for example, require too much extrapolation. In other words, you can't assume that a short visit means the docs are no good, and you can't assume a longer visit means they work well. You could associate such data with other measures, but by themselves they don't tell us much.

TL;DR: It's hard to provide reliable testing of docs effectiveness – but that won't stop us from trying!

*Teaser line that draws folks into the channel where they might find related conversations:* `#CHANNEL-NAME <https://writethedocs.slack.com/messages/CHANNEL-NAME>`_

----------------------------------
Using imperatives in documentation
----------------------------------

English has no shortage of complexities, idiosyncrasies, and fine distinctions. Navigating them to come up with clear, concise content is at the heart of the documentarian's job. The Write the Docs Slack can be a great resource for when you need a hand with that navigation. For example, this month one documentarian asked about the difference between 'must' and 'have to', sparking a plentiful thread about not only the difference but also important considerations when using them in your docs.

There is a canonical rule for their distinct usages. While both convey an obligation to the reader, "must" is for *specific* requirements, while "have to" refers to more general rules. You can read more about this definition in the `"Must vs Have to" post on Gymglish <https://www.gymglish.com/en/english-grammar/must-vs-have-to>`_.

But how does that play out in the docs? A lot of it has to do with the different tone that each verb carries. 'Must' is more formal, more inescapable. It's usually a good fit for procedural content when talking about necessary actions the reader must take. 'Have to' is better for guiding your readers towards best practices or broader expectations they should be keeping in mind.

*If you find yourself with other grammar or usage questions, `#general <https://writethedocs.slack.com/messages/general>`_ has many word-folks waiting to help you out.*

-----------------------------------------------
Telling the difference between one API and many
-----------------------------------------------

When writing about APIs, it's not always clear where one API stops and another begins. Some teams treat their API as singular entity that covers everything, but others treat it as a collection of APIs instead, separated by product area, function, user segment, etc. So when the question arose – How do you decide whether you're writing about one API with broad functionality or multiple individual, more targeted APIs? – the community attempted to achieve some clarity.

After a thought-provoking discussion, some recurring (though not universal) definitions emerged:

* Everything that lives under one hostname is one API
* Everything that lives under one base URL and uses the same authentication specification is one API
* Even an API with broad-ranging capabilities, loads of endpoints, and a collection of related resources is still just one API, if it's all for the same application

There were some interesting examples of when teams have chosen to run contrary to these rules. For (a particularly topical) example, Facebook's Graph API and Marketing API use the same base URL, but are treated as separate APIs because they are intended for very different purposes and audiences. Similarly, Twilio's Phone and SMS APIs are treated as separate, despite using the same base URL.

To help sort out the question for your team, an API-centric product manager and good API design are crucial. One strongly recommended resource on API design was `Phil Sturgeon's APIs You Won't Hate <https://apisyouwonthate.com/>`_.

*If you work with APIs and want to bounce some ideas around,* `#documenting-apis <https://writethedocs.slack.com/messages/documenting-apis>`_ *is the place for you.*

---------------------
Featured job postings
---------------------
**Hiring? Want to get your job posting in front of real, live, in-person documentarians?**
Any jobs posted on the `Write the Docs job board <https://jobs.writethedocs.org/>`_ by noon PST on Monday, May 7th, will be printed out and displayed at the inaugural Write the Docs job fair at the Portland conference.

If you're currently job hunting and will be joining us in Portland, here's a taste of what to expect at the `job fair <>`_ on Tuesday morning. The jobs below are from Oracle, our headline sponsor for the event.

`JOB POSTING TITLE <JOB BOARD LINK>`_
 [company name], [full-time, part-time, etc.]

-------------------------
Upcoming community events
-------------------------

MMMMMM DD – LOCATION – `EVENT NAME <EVENT URL>`_
