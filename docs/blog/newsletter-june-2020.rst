.. post:: June 03, 2020
   :tags: newsletter

#######################################
Write the Docs Newsletter – June 2020
#######################################

Hey all - it’s Beth and the newsletter team here.

It feels like more and more often that I write to you while the backdrop is bleak, and it would be impossible to not talk about the ongoing protests around the world. `Inclusion is at the core of Write the Docs </about-us/#inclusivity>`__; we are distraught by the suffering, oppression and systemic racism the Black community faces every day. This is much better said in our `statement of support </blog/we-stand-with-the-black-community/>`__, but in particular I wanted to mention that we are matching donations, up to a total of $1,500, to non-profits working to support the Black community. See the `blog post </blog/we-stand-with-the-black-community/>`__ for how to tell us about your donation so that we can match it.

As May has drawn to a close, we’d usually be talking all about the Portland conference, but of course no such news this year. But to have something to look forward to: `tickets to the virtual Portland conference are now on sale </conf/portland/2020/news/online-ticket-sales/>`__. We’re still finalising exactly how everything will work, but the plan is to stay as close to the usual spirit of our events as possible - so including Writing Day, unconference sessions, and a virtual hallway track. Check out the `list of talks </conf/portland/2020/speakers/>`__, and `buy your tickets here </conf/portland/2020/tickets/>`__.

And if you’re in a time zone closer to UTC like me, keep your eyes peeled - we’ll be announcing dates for virtual Prague sometime soon.

With that, let’s see what the community has been talking about this month.


---------------------------------
Broken links and how to find them
---------------------------------

If your product includes links to docs topics, you're likely quite aware of those links. Perhaps you’re careful to fix the product links when docs URLs change, or maybe you just avoid changing link anchors in the docs altogether when you revise or update.

But it gets a bit more complicated when more contributors are making docs updates, and a recent Slack discussion included a helpful idea for this scenario (as long as your docs pages are output in HTML).

First, create a docs page that lists only the product links to docs topics. Then, create a separate testing environment for your docs site that includes the product links page in the HTML output. Finally, before you publish docs updates, build your pages in the testing environment and use a tool like `html-proofer <https://github.com/gjtorikian/html-proofer>`__ to find any broken product links.


---------------------------------
Types of docs and how to use them
---------------------------------

Back in 2017, Daniele Procida gave an often cited talk, `The four kinds of documentation, and why you need to understand what they are </videos/eu/2017/the-four-kinds-of-documentation-and-why-you-need-to-understand-what-they-are-daniele-procida/>`__, written up into `this article <https://documentation.divio.com/>`__. Our community spent some time discussing the details of how to apply Danielel's type distinctions, with some help from Daniele himself. As a refresher, the four types are:

* Tutorials, or learning-oriented docs 
* How-to guides, or problem-solving docs
* Explanations, or understanding-oriented docs
* Reference, or information-oriented docs

Here's how the conversation built on these types:

* Regardless of the type of doc, make sure to provide context to orient the user. Do they need to learn more before they read? What level of expertise is the doc aimed at?
* Other terms used to refer to the same types are "concept" (for explanations), and "procedure" -- which could cover both how-tos and tutorials, because all share a step-by-step approach. But a more nuanced distinction emerged. Tutorials can be thought of as step by step how-tos, but involving larger tasks or a broader grasp of how things work. How-to docs are smaller, and show how to accomplish only a single task.
* Some folks thought of tutorials as the place for users to get started learning *how* to make your product work, whereas others saw them as entry points for anyone at any level of expertise.
* But all agreed with Daniele's recommendation not to mix types - and agreed that no matter how carefully you structure your doc content, users will eventually do their own thing with it.


-------------------------------------
Common words and how to identify them
-------------------------------------

When we decide which words to use in our documentation, it's important to determine how common a word is. Common words are easier to understand and make your documentation more accessible to a wider audience. Picking the more common word can also be a handy way to settle a word choice disagreement - as enjoyable as the debate may be!

In addition to researching the words you use, you can user test them. If your (representative) test users don't know what the words in a document mean, or have difficulty understanding the procedure because of the words used, this can help you confirm that the words are uncommon, or at least not right for your audience.

Here are some tools to help you tell if a word is common or uncommon:

*   `Google Ngram <https://books.google.com/ngrams>`__
*   `Google Trends <https://trends.google.com/trends/?geo=US>`__
*   `iWeb Corpus <https://www.english-corpora.org/iweb/>`__
*   `1000 Most Common English Words <https://1000mostcommonwords.com/1000-most-common-english-words/>`__
*   `Plain English Campaign (guidelines) <http://www.plainenglish.co.uk/>`__
*   `Simplified Technical English (guidelines) <https://en.wikipedia.org/wiki/Simplified_Technical_English>`__


-------------------------------------------
Obvious things and whether to document them
-------------------------------------------

Recently, a discussion on Slack was sparked on the topic of whether or not you should document the “obvious”.

Those against documenting the obvious gave the example of uncomplicated UI procedures like deleting an object: if it’s something you’d expect users of almost any software to be familiar with, you could expect your audience to know it already. Plus, the downsides of being explicit include describing how to fill in every field in detail, or multi-step procedures for something the UI guides you through. More detail like this can make docs feel very long and cluttered, and make it hard for readers to find the bit that’s important to them. And explaining things in too much depth can come across as condescending.

In favour of documenting the obvious: what’s obvious to you isn’t necessarily obvious to others. Besides, those who already know something can skip over it. This discussion provides a reminder of how important it is to know your user base - what is "obvious and familiar" depends on your background, exposure, and contexts. At minimum, make sure you know what your assumptions are: if your assumptions are explicit, you can make deliberate choices on what to leave in and out, based on the intended audience.

Ultimately, be guided by what your specific audience needs to know to achieve their goals. That’s what belongs in documentation.

-------------------------------------------------------------------------------------
From our sponsor: Open Source Curious? Learn (and earn) with Google's Season of Docs!
-------------------------------------------------------------------------------------

This month's newsletter is sponsored by `Season of Docs <https://developers.google.com/season-of-docs>`__:

.. raw:: html

    <hr>
    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="width:100%; max-width: 600px;">
      <tbody>
        <tr>
          <td width="75%">
              <p>
              "<a href="https://developers.google.com/season-of-docs">Season of Docs</a> is a program from the Google Open Source Program Office that connects experienced technical writers with open source projects needing better docs. Writers receive a stipend and mentorship! Applications due <a href="https://developers.google.com/season-of-docs/docs/timeline">July 9</a>!"
              </p>
          </td>
          <td width="25%">
            <a href="https://developers.google.com/season-of-docs">
              <img alt="Season of Docs" src="/_static/img/sponsors/seasonofdocs.png">
            </a>
          </td>
        </tr>
      </tbody>
    </table>
    <hr>

*Interested in sponsoring the newsletter? Take a look at our* `sponsorship prospectus </sponsorship/newsletter/>`__.

---------
Job posts
---------

* `Lead Technical Writer <https://jobs.writethedocs.org/job/202/lead-technical-writer>`__
   Segment, San Francisco but remote-friendly
* `Technical Chainlink Documentation Writer <https://jobs.writethedocs.org/job/203/technical-chainlink-documentation-writer-remote>`__
   SmartContract, remote
* `Technical Writer <https://jobs.writethedocs.org/job/199/technical-writer>`__
   Nylas - SF, NY, Denver, Toronto, Austin, but remote-friendly
* `Content Developer 2 <https://jobs.writethedocs.org/job/205/content-developer-2>`__
   Microsoft, Redmond WA

*To apply for these jobs and more, visit the* `Write the Docs job board <https://jobs.writethedocs.org/>`_.

------------------------
Virtual events coming up
------------------------

- 04 June - hosted in Los Angeles, USA - `Food, drinks, catch-up! (at home) <https://www.meetup.com/Write-the-Docs-LA/events/270815078/>`__
- 05 June - hosted in Barcelona, Spain - `What is the Fourth Industrial Revolution and Why Should You Care? <https://www.meetup.com/Write-the-Docs-Barcelona/events/270549589/>`__
- 15 June to 10 July - `#learn-tech-writing on Slack <https://app.slack.com/client/T0299N2DL/C7YJR1N02>`__ - `Book Club: How to Make Sense of Any Mess <https://www.writethedocs.org/book-club/>`__
- 17 June - hosted in Stockholm, Sweden - `Stockholm meetup #4 <https://www.meetup.com/Write-the-Docs-Stockholm/events/270930060/>`__
- 24 June - hosted in California, USA - `What Not To Document – And Why <https://www.meetup.com/Write-the-Docs-Bay-Area/events/270948142/>`__
- 30 June - hosted in Ottawa, Canada - `WTD Ottawa Shopify Meetup <https://www.meetup.com/Write-The-Docs-YOW-Ottawa/events/xtcbgqybcjbmb/>`__
