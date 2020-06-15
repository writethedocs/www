.. post:: April 03, 2020
   :tags: newsletter

######################################
Write the Docs Newsletter – April 2020
######################################

Hello, friends. Beth A here, and it feels pretty strange to be sitting down to write the usual newsletter intro to you all, when things in the world and at home are far from usual.

But pandemics aside, there's still a lot happening online in the Write the Docs community, and I hope that this newsletter can bring you something interesting - or at least distracting - in trying times. And if you're in need of some support - whether you're struggling with the current crisis, or with regular documentarian problems - if you need someone to talk to, the community is here for you on `Slack </slack/>`__.

In this month's edition, we've got our usual wide range of topics. As many folks are working remotely for the first time (your editor included - I'm four weeks in), we have some advice from the community on how to manage that. We talk about when keeping docs and code in the same repository might not be the right choice; we look at how the `salary survey results </surveys/salary-survey/2019/>`__ went down; and from the #learn-tech-writing book club, we have an introduction to the principles of 'Every Page is Page One'.

That's it from me. Thinking of you all.

------------------------------
Adapting to working from home
------------------------------

It's no surprise that there's been a lot of discussion about how to work effectively from home. So here's a selection of thoughts that folks on Slack said they'd found helpful:

- While there's plenty of good advice on how to work productively from home, remember that the situation you're in is **not** normal remote work. At best, you're cooped up involuntarily at a time when the news cycle is extremely present; and you may be ill, or caring for your family, or worried to be apart from them. So take any advice with that pinch of salt. Above all, be kind to yourself.
- We could be in this situation for a while, so it's worth gearing up for that. There was strong agreement that it's worth maintaining a routine - it's easy to drift into spending a day in pyjamas, but that can leave you exhausted. Many find it helpful to have a defined start to the work day by getting up and dressed as usual; some even take 'commute' time to walk around the block or listen to podcasts. 
- It's just as important to finish the day, rather than drifting into working late: setting boundaries is the name of the game. If it's possible for you, it helps to have a defined work space away from other activities. And similar to the morning, an end-of-day 'commute' can help you switch off. 
- Taking regular breaks can make a big difference to your energy levels. And while it's a good idea to be more available online than usual, being away from the office also means you can take breaks with no fear of judgement. *Nobody knows that you're taking a nap*.  
- Running virtual meetings can take a bit more thought than in-person ones. `Here's a post on doing it well <https://hbr.org/2020/03/what-it-takes-to-run-a-great-virtual-meeting>`__.
- If you're sad that conferences are being cancelled, check out `this list of conferences that are going online <https://docs.google.com/spreadsheets/d/1IKXAcDoYnWNpuFaDYkn_aplDZ5fRI0bJNWah0rGFO5E/edit#gid=0>`__.
- For managers, this new situation may be a major challenge. Many people will be struggling and need your support - your kindness is more important than ever. `This blog post from Lara Hogan <https://larahogan.me/blog/predictability-stability-terrible-times/>`_ might help.

------------------------------------------
Pros and cons of the docs-as-code approach
------------------------------------------

The `docs as code </guide/docs-as-code/>`_ approach to documentation means using the same tools and workflows for the documentation, as developers use for the code. Writers using this approach are often integrated into the product team, too - but does that mean your docs should be in the code repository too? Here are the community's thoughts:

In favour of *keeping* docs and code in the same repo:

- Less friction to docs contributions: developers don't have to leave their projects to work on the docs.
- Comprehensive pull requests: a single pull request can include code changes and the associated docs updates.
- Eliminates the manual step of coordinating releases and pull request merges between repos.
- Facilitates contributions from the entire product team, which can mean more perspectives are reflected in the documentation.

Pros of *separating* docs and code:

- Less noise in the code repo. For example, docs commits won't appear in automated change logs and team notifications.
- Mistakes in the docs repo cannot affect the code.
- A separate docs repository can be easier for new team members to understand.
- Build time will increase as code + docs size increases (although parallelization can mitigate this problem). If docs are in a separate repo, writers don't have to wait for code builds (and devs don't have to wait for docs builds).
- It takes technical knowledge to set up, customize, and maintain a combined repo and toolchain - so you need either that knowledge yourself, or development resources.
- Some docs publication tools don't play well with a code development workflow (for example, FrameMaker, InDesign, or Word).

--------------------------
Salary survey speculations
--------------------------

A chorus of thank-yous greeted the publication of the `WTD salary survey for 2019 </surveys/salary-survey/2019/>`_ -- and were quickly followed by numerous anecdotes, speculation about The State of the Profession (technical writing, that is), and more. Highlights of the conversation:

* It was hard to compare absolute salary information across countries and regions without information about cost of living. Some folks offered their sense of differences, though -- for example, lower salaries in Pennsylvania than in New York were thought to be more than offset by the lower cost of living.
* Some people thought that salaries in expensive cities seemed low; others seemed to realize just how low their own salaries were compared with the average for their locale.
* Some felt that the data gave them what they needed to negotiate raises or, more generally, better compensation packages!

The education question in particular produced a plethora of responses. Some were surprised at how many respondents had college degrees; many documentarians shared stories about their degrees in unrelated fields. Not many of the community have degrees or formal training in technical writing/communication (but some do!), and a fair few are interested in pursuing more training. Education -- whether you have a degree, or what your degree is in -- seems to matter less the more experience you have.

General agreement that compulsive curiosity and desire to learn are key attributes of a successful documentarian.

------------------------------------------------
Book club: an intro to  'Every Page is Page One'
------------------------------------------------

This month members of our virtual book club discussed the first few chapters of Mark Baker's ‘Every Page is Page One’ (EPPO). For those who haven't read it, we thought we'd give a summary of the ideas.

The core premise of EPPO is that users rely heavily on web search for help with when they have problems with software. This means you can't rely on them navigating nicely through your doc site structure, starting at your helpful introductory page - any page of your docs can be your user's page one.

There's no disagreement from our book club members on the importance of search engines like Google as an entry point to docs. Not surprisingly, docs locked behind paywalls and/or logins can negatively affect user satisfaction. The community suggests, however, that these barriers can help combat competing content available on the web whether through Reddit, YouTube or other frequently trafficked learning platforms.

Another observation from Baker is that, when it comes to finding what they’re looking for on the web, users opt for the path of least resistance. He calls this "information foraging". So if you want to optimize for this foraging behaviour, that means you need to make sure your content is both ‘nutritious’ (information rich) and ‘easy to catch’.

---------
Job posts
---------

* `Technical Writer <https://jobs.writethedocs.org/job/193/technical-writer/>`__
   Ably, London - full-time
* `Technical Copywriter <https://jobs.writethedocs.org/job/194/technical-copywriter/>`__
   Ably, London - full-time

*To apply for these jobs and more, visit the* `Write the Docs job board <https://jobs.writethedocs.org/>`_, *or check out the* `#job-post-only channel <https://app.slack.com/client/T0299N2DL/C09E989K5>`__ *on Slack.*

--------------------------
Community events coming up
--------------------------

A few WTD meetups are trying out remote sessions, and we've noted those here. For those that are still meant to be in-person, be aware that they might be postponed.

If you're a meetup organiser and you'd like to try running a remote event, check out `this guide to live-streaming a meetup </organizer-guide/meetups/livestreaming-meetups/>`__.

- 08 April - remote (Toronto) - `Staying productive and maintaining your mental health while working from home <https://www.meetup.com/Write-the-Docs-Toronto/events/pcqbmqybcgbtb/>`__
- 08 April - remote (Barcelona) - `Working from home, tooling, and current challenges <https://www.meetup.com/Write-the-Docs-Barcelona/events/269665459/>`__
- 14 April *(may be postponed)* - Ottawa, Canada - `Shopify meetup <https://www.meetup.com/Write-The-Docs-YOW-Ottawa/events/xtcbgqybcgbsb/>`__
- 16 April - remote (Australia and India) - `Remote lightning talks <https://www.meetup.com/Write-the-Docs-Australia/events/269153249/>`__
- 22 April *(may be postponed)* - Arlington, VA, USA - `Word games social hour <https://www.meetup.com/Write-the-Docs-DC/events/269073707/>`__
- 23 April *(may be postponed)* - San Francisco, CA, USA - `Documentation templates for fun and profit <https://www.meetup.com/Write-the-Docs-Bay-Area/events/268792742/>`__
