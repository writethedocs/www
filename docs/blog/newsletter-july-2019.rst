.. post:: July 2, 2019
   :tags: newsletter

#####################################
Write the Docs Newsletter – July 2019
#####################################

Hi, WTD friends, and welcome to the July newsletter! It's Beth A here writing from sweltering Europe, where I've been learning great new words like *canicule* and *Hitzewelle* - aka heatwave in French and German.

(Fun fact: *canicule* comes from the Latin *dies caniculares*, or "dog days" - the most uncomfortable part of summer, so named because they come after the `heliacal rising <https://en.wikipedia.org/wiki/Heliacal_rising>`_ of Sirius, the Dog Star. Well, I thought it was interesting.)

Aside from fascinating facts about the weather, we also have some exciting announcements for you. Firstly, `tickets are on sale for the Australia conference </conf/australia/2019/news/au-2019-welcome/>`__, and `the call for proposals is also open </conf/australia/2019/cfp/>`__! The CFP closes on 9 August, and the conference itself is 14-15 November in Sydney.

As for Europe, you'll be pleased to know that `Prague speakers have been announced </conf/prague/2019/news/talks-volunteers-tickets-shirts/>`__! `Here's the full list </conf/prague/2019/speakers/>`__, and you can grab your tickets `here </conf/prague/2019/tickets/>`__. Plus, if you're interested in helping out behind the scenes, we'd love you to `volunteer at the conference </conf/prague/2019/news/talks-volunteers-tickets-shirts/#call-for-volunteers>`__.

Lastly is a cool addition to the Hiring Guide. The `Career Community Spotlight </hiring-guide/#community-spotlight>`__ is a series of interviews about how people became documentarians, including tips for how to follow the same path. Please share with anyone interested in getting into the industry, and if you'd like to share your own story, `get in touch <mailto:jobs@writethedocs.org>`__!

So that's the news. What have we been talking about on Slack this month?

-----------------------------------
Making the leap to managing writers
-----------------------------------

One of our big discussions this month was about folks weighing up opportunities to move into managing writers. Here's the guidance the community gave.

There are definitely some things to be wary of. If writing's your passion, moving to management means less time for it. This can mean losing touch with the craft, and leaving your portfolio lighter if you decide to back out. Another issue is that you're accountable for both the successes and failures of your team, which can be stressful. 

But the upsides of management are the bigger projects that can challenge you in different ways, including helping your team reach their full potential. In the long run, teaching others lets you achieve more than you would have been able to on your own.

If you'll be hiring, recruitment can create a more direct sense of accomplishment. On the flip side, you may also at some point be responsible for letting people go, a daunting task.

The general conclusion was: it's not easy to make the move, but if you're happy to spend less time writing and to contribute in a bigger way instead, it might be for you.

For those considering management, take a look at `Rands Leadership Slack <https://randsinrepose.com/welcome-to-rands-leadership-slack/>`__, which offers coaching and educational resources. It's also worth checking out the episodes of Tom Johnson's podcasts on how to manage an all-star team of technical writers: `Managing Writers <https://idratherbewriting.com/2009/03/23/managing-writers-interview-with-richard-hamilton-podcast/>`_ and `Managing Virtual Teams <https://idratherbewriting.com/2007/04/29/managingvirtualteams/>`_.

-------------------------------------------------------
READMEs on READMEs (and other README-related resources)
-------------------------------------------------------

As they're often the first thing people see about a code project, READMEs are pretty important to get right. Fortunately, there are tons of great resources to help you write quality READMes. Check these out:

* `Art of README <https://github.com/noffle/art-of-readme>`_
* `Standard README <https://github.com/RichardLitt/standard-readme/>`_
* `Write the Readable README </videos/na/2016/write-the-readable-readme-daniel-beck/>`_ (Daniel Beck @ Write the Docs NA 2016), and Daniel's `README checklist <https://github.com/ddbeck/readme-checklist>`_
* `Hi, my name is README! </videos/eu/2017/hi-my-name-is-readme-raphael-pierzina/>`_ (Raphael Pierzina @ Write the Docs EU 2017)
* `Ten Steps to a Better README <https://www.youtube.com/watch?v=PC05prd2usY>`_ (Mike Jang @ Ignite OSCON 2015)
* `Developer Experience: GitHub READMEs <https://betta.io/blog/2017/02/07/developer-experience-github-readmes/>`_ (Cristlano Betta's blog post)
* `READMEs and doc-driven development </blog/newsletter-august-2017/#readmes-and-doc-driven-development>`_ (August 2017 WTD newsletter)

-----------------------------------------
For those who might consider freelancing…
-----------------------------------------

… a generous Slack contributor provided a wealth of information and advice about what to look for and what to expect in the land of freelance work.

We were planning to write this up for the newsletter, but very kindly the contributor did it for us! So you can read all about it here: `Real Talk: Freelance/Contract Writing <https://dacharycarey.com/2019/06/12/real-talk-freelance-contract-writing/>`__

A few other people also weighed in with some comments. Some don't work with a 1099 but set up their own corporations (S-Corp or LLC), and then work as their own employees. This approach can provide tax benefits for US workers, and can sometimes make you more appealing to a larger employer. People also suggested that professional support, in the form of a lawyer or accountant, is important if you're planning to work freelance long-term.

And if you're going the independent route, don't forget to consider staffing agencies. They get a cut of whatever the client pays, but they sometimes provide benefits and ease the paperwork burden.

------------------------------
What to do about text wrapping
------------------------------

A very specific topic, but one that usually comes when working with docs-as-code: should you mandate text wrapping in your docs source, and if so, how? For some background before digging into this summary, check out `To Wrap or Not to Wrap: One of Life's Greatest Questions <https://about.gitlab.com/2016/10/11/wrapping-text/>`_.

Forcing a hard wrap at a particular character count or column helps avoid `reflow problems <https://www.w3.org/TR/WCAG21/#reflow>`_, but causes other problems. For example, hard wraps:

* create awkward line breaks on devices with different screen sizes
* wreak havoc on diffs
* make text more difficult to parse for people who are translating to different languages and people with cognitive disabilities

Hard wraps also interfere with using filters like `grep <http://man7.org/linux/man-pages/man1/grep.1.html>`_ to search for words and phrases within a file. Soft wrap is an option for preserving searchability, but it requires everyone to use a text editor with soft wrap support.

Several people mentioned `one sentence per line <https://rhodesmill.org/brandon/2012/one-sentence-per-line/>`_ as a solution, noting that it's the `recommended approach for AsciiDoc <https://github.com/asciidoctor/asciidoctor.org/blob/master/docs/asciidoc-recommended-practices.adoc#one-sentence-per-line>`_.

-----------------------------------------------------------------
From our sponsor: Spotlight on The Not-Boring Tech Writer podcast 
-----------------------------------------------------------------

We're excited to be trying out sponsorship of the newsletter this month. Sponsorship helps us cover the cost of the newsletter, and gives us funding opportunities to expand our ambitions in the future. If you're interested in sponsoring, take a look at our `sponsorship prospectus </newsletter/sponsorship/>`__.

This month's newsletter is sponsored by `KnowledgeOwl <https://www.knowledgeowl.com/home?utm_source=newsletter&utm_campaign=wtd-jul-2019>`__:

.. raw:: html

    <hr>
    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="width:100%; max-width: 600px;">
      <tbody>
        <tr>
          <td width="75%">
              <p>
              Do you love documentation and podcasts? Check out our <a class="reference external" href="https://www.knowledgeowl.com/home/not-boring-tech-writer-podcast-relaunch?utm_source=newsletter&utm_campaign=wtd-jul-2019">spotlight on The Not-Boring Tech Writer podcast</a>. Each episode focuses on a single skill or tool to provide you with actionable content.
              </p>
              <p>
              KnowledgeOwl is proud to sponsor TNBT podcast along with the WTD newsletter. KnowledgeOwl makes knowledge base software and loves to help documentarians. Check out the <a class="reference external" href="https://www.knowledgeowl.com/home?utm_source=newsletter&utm_campaign=wtd-jul-2019">KnowledgeOwl website</a> to learn more.
              </p>
          </td>
          <td width="25%">
            <a href="https://www.knowledgeowl.com/home?utm_source=newsletter&utm_campaign=wtd-jul-2019">
              <img alt="knowledgeowl" src="/_static/img/blog/knowledge-owl-logo.png">
            </a>
          </td>
        </tr>
      </tbody>
    </table>
    <hr>


---------
Job posts
---------

* `Knowledge Management Strategist <https://jobs.writethedocs.org/job/127/knowledge-management-strategist/>`__
   Braintree, Seattle, full-time

*To apply for this job and more, visit the* `Write the Docs job board <https://jobs.writethedocs.org/>`_.

--------------------------
Community events coming up
--------------------------

- 3 July - Munich, Germany - `Terminology & semantics - defining and managing meaning in documentation <https://www.meetup.com/write-the-docs-muc/events/262687214/>`__
- 4 July - Melbourne, Australia - `Documenting API dev portals <https://www.meetup.com/Write-the-Docs-Australia/events/261792791/>`__
- 10 July - London, UK - `Write the Docs Prague talk previews <https://www.meetup.com/Write-The-Docs-London/events/261893453/>`__
- 10 July - Denver, CO, USA - `Docs and Drinks Denver happy hour <https://www.meetup.com/Write-the-Docs-Boulder-Denver/events/262265861/>`__
- 10 July - Portland, OR, USA - `Publication workflow case study <https://www.meetup.com/Write-The-Docs-PDX/events/262694535/>`__
- 12 July - Austin, TX, USA - `Write the Docs ATX lunch meetup <https://www.meetup.com/WriteTheDocs-ATX-Meetup/events/262512533/>`__
- 15 July - Berlin, Germany - `Docs hack <https://www.meetup.com/Write-The-Docs-Berlin/events/262443229/>`__
- 17 July - Manchester, UK - `Summer social <https://www.meetup.com/Write-the-Docs-North/events/260863447/>`__
- 17 July - Toronto, Canada - `Write the Docs Toronto <https://www.meetup.com/Write-the-Docs-Toronto/events/262467288/>`__
- 18 July - Sydney, Australia - `Presentations and lightning talks <https://www.meetup.com/Write-the-Docs-Australia/events/262059088/>`__
- 23 July - Seattle, IL, USA - `Seattle morning social <https://www.meetup.com/Write-The-Docs-Seattle/events/262426584/>`__
- 25 July - Boise, ID, USA - `Document review <https://www.meetup.com/Write-the-Docs-Boise/events/262491452/>`__
- 7 August - London, UK - `Summer social <https://www.meetup.com/Write-The-Docs-London/events/262472580/>`__
