.. post:: August 2, 2019
   :tags: newsletter

#######################################
Write the Docs Newsletter – August 2019
#######################################

Hello everyone! It's Beth and the team here, with another packed newsletter issue for you.

A quick correction first: last month we said that the Australia conference is in Melbourne, when it is in fact in **Sydney**. Really sorry about that. If you'd like to speak in **Sydney**, the `CFP </conf/australia/2019/cfp/>`__ is still open: you have until 9th August to submit.

In the other hemisphere, the `Prague speaker speaker schedule is up </conf/prague/2019/schedule/>`__, and `tickets are almost sold out </conf/prague/2019/news/events-activities/>`__. Once they're gone, they're gone, so if you'd like to come, buy your tickets ASAP!

One last thing - we're delighted to have some new recruits to the newsletter team, which means we now have an extra story about what the community has been talking about on Slack! Enjoy :) The newsletter team takes September off, so we'll be back in your inboxes come October.

------------------------------------------------
Adventures in generating docs from code comments
------------------------------------------------

A question about how to improve on tools like `Javadoc <https://www.oracle.com/technetwork/java/javase/documentation/index-jsp-135444.html>`__ and `doxygen <http://www.doxygen.nl/>`__ yielded many insights into getting great results with docs generated from code comments:

* Javadoc is pretty standard for Java development, so you can expect that devs are already looking for the Javadoc - and you can help them just by making sure it's easy to find.
* No matter which tool you use, the content is only as good as the comments in the code. Great documentation depends on collaboration between developers and writers, which can be challenging.

  To improve developer buy-in, try emphasizing that more complete and accurate code comments can help increase adoption: no one will use the product if they can't understand it. Any tactic to open a conversation can help: one writer started by contributing basic grammar edits.
* When it comes to what the docs look like, you can customize the standard doclet yourself or search for existing custom doclets. Take care with custom doclets that aren't maintained or supported: they can take a lot of work. And remember, Javadoc and Doxygen actually only "autogenerate" insofar as they are integrated into the app build process.
* Javadoc interprets the code itself, so it can - even without code comments - generate basic docs on package, class, method, field, and argument names and types. One person mentioned they sometimes run Javadoc just to see what it turns up about the code that isn't documented elsewhere.

For more about a successful Javadoc/doxygen project that included writers and developers, check out Jennifer Rondeau's `Symantec case study <https://www.docslikecode.com/articles/symantec-case-study/>`__. For a discussion of the benefits of writers and developers working together, see our editor's talk `Who Writes the Docs? </videos/portland/2018/who-writes-the-docs-beth-aitman/>`__

-------------------------------
Using writing tests when hiring
-------------------------------

Assessing writers when you're hiring can be a tricky task. Work samples may not be enough to assess skill level; confidentiality agreements bind some candidates, making samples hard to come by; and samples may have been improved by colleagues.

Recently on Slack, documentarians were discussing how writing tests can help get past these limitations, but tests are controversial. Asking a candidate to spend many hours on a test is not very respectful of their time, and not everyone can afford to do it. So here are a few tips from the conversation:

- It can be reasonable to ask a candidate to complete a writing test before interviews, so that you get an indication of their skills. Just be careful about how much time it will take them.
- An alternative is an on-site writing test during an interview day. But keep the test to an hour or less, and be aware that time pressure changes how polished you can expect the work to be.
- Be wary of writing tests on real company topics: while these are more realistic tests, they can also look like you're asking for free work. Instead, perhaps ask them to document a tool or open-source project with no direct benefit to the company.
- Getting candidates to think about the audience of the documentation is crucial!
- You can learn a lot about how a person works through writing tests, so give candidates a chance to talk about their writing process after the test. 

For more ideas, read Cockroach Labs' `Documentation exercises <https://github.com/cockroachlabs/open-sourced-interview-process/blob/master/DocumentationExercises.md>`__.

-------------------------------------------
Advice for creating technical illustrations
-------------------------------------------

Diagrams and technical illustrations were a hot topic this month. Here are some of the things that came up - but if you want to hear more, join `#visual-content <https://writethedocs.slack.com/messages/visual-content>`__!

* Less is more! Like in technical writing, be concise in your technical illustrating.
* Before you start illustrating, identify what resources you have available. For example, if other published materials include images, these may well be vector graphics that you can easily import to use as a starting point for your own illustration.
* Consider reaching out to a designer or similarly skilled person in your organization for help or inspiration.
* *Advanced tip!* If you're publishing a PDF, you can embed 3-D objects into the PDF. When users view your PDF document, they can interact with the 3-D object. You can learn more about this `here <https://helpx.adobe.com/acrobat/using/interacting-3d-models.html#interacting_with_3d_models>`__.

Resources the community mentioned:

* `Mike Parkinson's (of BillionDollarGraphics) Graphic Cheat Sheet <http://billiondollargraphics.com/graphic-cheat-sheet/>`__
* `Alicia Raszkowska's talk "Draw the Docs" </videos/portland/2019/draw-the-docs-alicja-raszkowska/>`__
* `The Back of the Napkin by Dan Roam <https://hbr.org/2008/09/solving-problems-with-your-pen.html>`__
* `Trees, maps, and theorems by Jean-luc Dumont <http://www.principiae.be/X0300.php>`__

And the tools documentarians said they use included:

* GIMP
* Adobe Illustrator
* Visio
* LucidChart
* SolidWorks
* AutoCAD
* Omnigraffle
* Google Docs

-----------------
Writing remotely
-----------------

We see discussions about working remotely a lot on Slack. For some, working remotely allows for a work-life balance that they can't get working in an office. Others worry that working remotely threatens their upward mobility within the company. Is there truth to the belief that companies value in-house employees more, promoting them more regularly than remote employees? Just what is the status quo for remote writing? This month the community pitched in with their own experiences.

One common question is, are there many remote jobs out there? Although most agreed that remote jobs are harder to come by, there are many tech businesses out there who are keen on a remote workforce. Startups, for example, can be more welcoming of remote culture, so worth checking out.

Secondly, the issue of productivity. It’s no surprise that trust and cohesion are incredibly important in a remote environment: managers must trust you to be productive, as they don't get the same oversight as with on-site employees. It can be easier in a smaller company, where staff may be able to form closer bonds than a in larger corporate environment. One way the community suggested to demonstrate productivity is to focus on concrete results and measure deliverables. Some said their companies employ project managers to assist writers with their time management and project delivery.

To read more about working remotely, check out `this online book <https://basecamp.com/books/remote>`__, or `these survey results <https://www.and.co/anywhere-workers>`__ for data on remote workers. 

-------------------------------------------------------
Starting out with analytics - and then upping your game
-------------------------------------------------------

Analytics, metrics, measuring docs quality -- different names for similar questions that come up regularly on Slack, and that just as regularly produce excellent discussions. Forthwith the highlights of a recent conversation:

- Start with Google Analytics: embed a GA tag in the root ``index.html`` of your site, then use the GA dashboard.
- Common data to collect:
  - Number of users (new users and returning)
  - Average time on page
  - Which pages (most visited, least visited)
  - Where and when do users leave your site
- Other potentially useful data includes device type (mobile/desktop/tablet), browser, and language.
- Try Google Tag Manager for managing GA tracking -- it lets you start tracking more items without adding extra code to your site.

People were quick to point out that, while GA shows you what data you can collect automatically, you really need to think about what you want to learn about your docs and users, then pick metrics to achieve those goals. Start with the questions, then gather the data! (More in `Sarah Moir's great talk from Portland </videos/portland/2019/just-add-data-make-it-easier-to-prioritize-your-documentation-sarah-moir/>`__.)

A particular question about measuring ROI generated its own round of ideas and suggestions:

- If you care about driving sales and renewals, work with sales and marketing teams.
- If you care about reducing support tickets (deflection), work with support: they can give users links to relevant docs, and measure how many visit docs pages instead of filing tickets. 

  One example was a support site that took a high bounce rate and low numbers of page views as evidence that users found what they wanted and left. A similar approach could be measuring how many visitors left your site after viewing a support article.
- For more ideas, see this `blog post about support KB effectiveness <https://www.chrisdottodd.com/2019/03/measure-success-of-your-help-knowledge.html>`__.

There were also some clever suggestions for deciding which docs need improvement. High pageviews combined with low page ratings suggest pages in need of attention. Or if a page that helps solve a problem people are filing support tickets for is getting low pageviews, maybe your SEO could use some love.

Recommended reading:

- *Measures of Success: React Less, Lead Better, Improve More*
- *How to Measure Anything*
- `More newsletter entries about metrics! <https://www.writethedocs.org/newsletter/#metrics>`__
- Bob Watson's often cited `blog posts about measuring value <https://docsbydesign.com/category/technical-writing/measuring-value/>`__
- Sarah Moir's blog posts `here <https://thisisimportant.net/2019/05/21/detailed-data-types-you-can-use-for-documentation-prioritization/>`__ and `here <https://thisisimportant.net/2019/05/21/just-add-data-using-data-to-prioritize-your-documentation/>`__

---------
Job posts
---------

* `Technical Content Writer <https://jobs.writethedocs.org/job/131/technical-content-writer/>`__
   Datadog, full-time
* `Documentation Manager <https://jobs.writethedocs.org/job/132/documentation-manager/>`__
   Smartling, full-time

*To apply for these jobs and more, visit the* `Write the Docs job board <https://jobs.writethedocs.org/>`_.

--------------------------
Community events coming up
--------------------------

- 7 August - London, UK - `Summer social <https://www.meetup.com/Write-The-Docs-London/events/262472580/>`__
- 10 August - Bengaluru, India - `Can you Whatfix? <https://www.meetup.com/Write-the-Docs-India/events/263473440/>`__
- 15 August - Sydney, Australia - `It's all about communication <https://www.meetup.com/Write-the-Docs-Australia/events/263411386/>`__
- 16 August - Oakland, CA, USA - `Developer Relations: The Q&A Panel <https://www.meetup.com/Write-the-Docs-Bay-Area/events/262802711/>`__
- 19 August - Berlin, Germany - `Docs hack <https://www.meetup.com/Write-The-Docs-Berlin/events/263220327/>`__
- 20 August - Austin, TX, USA - `Happy hour meetup: August <https://www.meetup.com/WriteTheDocs-ATX-Meetup/events/263370057/>`__
- 28 August - Chicago, IL, USA - `August meetup <https://www.meetup.com/Write-the-Docs-Chicago/events/263576145/>`__
- 4 September - Leeds, UK - `Write a great README <https://www.meetup.com/Write-the-Docs-North/events/263328784/>`__
- 10 September - Ottawa, Canada - `Shopify meetup <https://www.meetup.com/Write-The-Docs-YOW-Ottawa/events/260863754/>`__
- 16 September - Berlin, Germany - `Docs hack <https://www.meetup.com/Write-The-Docs-Berlin/events/hzmpsqyzmbvb/>`__
- 18 September - Toronto, Canada - `Write the Docs Toronto <https://www.meetup.com/Write-the-Docs-Toronto/events/pcqbmqyzmbxb/>`__
- 25 September - Chicago, IL, USA - `September meetup <https://www.meetup.com/Write-the-Docs-Chicago/events/263576179/>`__

