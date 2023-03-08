.. post:: March 06, 2023
   :tags: newsletter

#########################################
Write the Docs Newsletter – March 2023
#########################################

Hello, everyone! March is here, which should mean the changing of the season. I hope you are able to find some balance with the upcoming equinox.

This month's big community news is the `announcement of the Portland conference speakers <https://www.writethedocs.org/conf/portland/2023/news/announcing-speakers/>`__. This marks the return of in-person talks, and the variety of topics and speakers means it's sure to be a treat for those able to attend. If you can't make it to Portland, some other areas are also retuning to in-person meetups. So if that's your thing, check out the list at the end of the newsletter.

Before the meetup list, enjoy some discussions about how to deal with being a sole documentarian, how to break up your docs-as-code, what the most interesting projects some of us have worked on, and how to face the challenge of documenting AI (since we know from last month that it won't yet replace us). 

-----------------------------------------
Loneliness of the "Lone-ly" Documentarian
-----------------------------------------

“Sometimes being surrounded by everyone is the loneliest because you'll realize you have no one to turn to.” — Soraya

A recent discussion in `#lone-writer <https://writethedocs.slack.com/archives/CAL5Y0NB1>`__ elicited some responses with value for all documentarians. The essence of the posted question also appears in #career-advice: How to develop skills to feel successful throughout a career?

Some of the responses related to training opportunities: certification programs or online training (within the domain or for new skills). Some suggested joining the `#learn-tech-writing <https://writethedocs.slack.com/archives/C7YJR1N02>`__ channel and participating in its book club. For some people, reading books may be helpful.

The importance of developing relationships with other documentarians was brought up. Interacting with the Write the Docs community (asking questions in the Slack workspace, mingling in meetups, or attending WTD conferences) was important for many people. Maintaining relationships with previous co-workers or finding a mentor to bounce ideas off of was suggested by others.

Documentarians might have to step out of their comfort zone to ask for feedback. Some suggested developing relationships with "solid doc allies" or trusted subject matter experts within the company to get quality feedback. Learn from it but don't take it personally. Realize that morale boosters are elusive for documentarians, so accept positive feedback gracefully.

Appreciate the benefits of being a lone (or lonely) writer. As the company's advocate for your audience, you can ask for necessary information in a way to focus other teams. As long as the company considers documentation important, you have the power to make a difference and be recognized as an important contributor to your company.

------------------
Semantic Linefeeds
------------------

If you write the docs in a markup language such as Markdown, AsciiDoc, or reStructured Text, you might have encountered semantic linefeeds (also known as `semantic line breaks <https://sembr.org/>`__). Semantic linefeeds mean that you add a line break after each sentence or even clause in your source file, not just after paragraphs. These shorter lines make the source files easier to read and edit (and the pages are still rendered in paragraphs when published).

Some documentarians dislike the choppy, random look that semantic linefeeds can produce. Others like the technique because it helps with docs-as-code issues such as keeping file comparisons ("diffs") neat and legible and because it helps break down text for translation by line.

Among those who do use semantic linefeeds, the most common form is a variation called ventilated prose: one sentence per line. Adding a line break after every sentence feels somewhat natural and makes it easier to compare sentence lengths. Ventilated prose also makes it more obvious when you have long sentences that could be rewritten. 

-------------------------
Most interesting projects
-------------------------

As the role of documentarians has become increasingly crucial in today's fast-paced technological world, they have been tasked with numerous challenging projects. From documenting complex software systems to creating user manuals for cutting-edge devices, documentarians have a lot on their proverbial plates. However, among all these projects, some always stand out as particularly intriguing or memorable. For example, some recall documenting museum software to help guide staff in recording details about everything they collect, such as art, clothing, and dinosaur skeletons.

Others mentioned having a localization voiceover gig to demonstrate using a chainsaw, working on contracts for a company that built and sold childcare facilities, writing instructions for a reading tracking software company, authoring an operations manual for a robotic systems defense contractor, and creating content for a bespoke application for the oil and gas industry. From the variety of examples, it can be said that documentarians are tasked with complex and exciting projects, even if it's just helping a parent write and edit books on sleight-of-hand magic.

The most interesting projects that documentarians have worked on showcase the diverse range of topics and industries they can adapt to and the complexity of the information they need to communicate. As technology continues to evolve and shape our world, documentarians will remain a crucial part of the process, ensuring that information is shared effectively and efficiently with a broad audience. It's clear that it's already a fascinating and challenging field, and it’s expected that more innovative and interesting projects will emerge in the future.

----------------
Documenting AI
----------------

Artificial intelligence (AI) is still top of mind for many. Based on a discussion this month, here's what the community thinks we should we be looking out for.

First up, if you're working on a machine learning (ML) tool, keep an eye on data lineage. It's important to distinguish between the known input for the ML tool and These analysis or predictions that the tool outputs. For example, this might mean labelling a prediction on a person's age as "Age analysis result" rather than "Age of subject". If you're interested, the following article present more on the subject: `Always Leave An Analysis Paper Trail <https://counting.substack.com/p/data-science-practice-101-always-leave-an-analysis-paper-trail-cc17079fae5a>`__, and `An Introduction to the Data Biography <https://weallcount.com/2019/01/21/an-introduction-to-the-data-biography/>`__.

A related challenge can be explaining to end users what AI is actually doing. One discussion participant had been interested in the `End-User-Centered Explainable AI Framework <https://weina.me/euca/>`__, a prototyping tool for explaining AI to users; another linked to an example of a documentation standard trying to be transparent about AI, IBM's `AI FactSheets 360 <https://aifs360.mybluemix.net/introduction>`__.

The community was also interested in the ethics of AI. They recommended a few pieces:

- A paper called `"On the Dangers of Stochastic Parrots" <https://dl.acm.org/doi/10.1145/3442188.3445922>`__.
- A recent publication, `A Critical Field Guide for Working With Machine Learning Datasets <https://knowingmachines.org/critical-field-guide>`__.
- A few books that discuss the technical side of ethics in machine learning, but accessibly: `The Ethical Algorithm <https://wsp.wharton.upenn.edu/book/the-ethical-algorithm/>`__, `The Alignment Problem <https://brianchristian.org/the-alignment-problem/>`__, and `Living in Data <https://us.macmillan.com/books/9780374720513/livingindata>`__.

----------------
From our sponsor
----------------

This month's newsletter is sponsored by Zoomin:

.. raw:: html

    <hr>
    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="width:100%; max-width: 600px;">
      <tbody>
        <tr>
          <td width="75%">
              <p>
                GPT is here, and your users expect the same content experience from you. <a href="https://www.zoominsoftware.com/zoomin-gpt/revolutionizing-the-technical-content-industry">Discover how</a> Zoomin is revolutionizing the technical content industry
              </p>

              <p>
                Our documentation portal is now public and open to all! <a href="https://docs.zoominsoftware.io/">Find out</a> what it looks like to have a SINGLE SOURCE OF TRUTH.
              </p>
          </td>
          <td width="25%">
            <a href="https://www.zoominsoftware.com/?vert=Write_The_Docs_Newsletter&utm_medium=referral&utm_source=WriteTheDocs&utm_campaign=March_Newsletter">
              <img style="margin-left: 15px;" alt="Zoomin" src="/_static/img/sponsors/zoomin.png">
            </a>
          </td>
        </tr>
      </tbody>
    </table>
    <hr>



*Interested in sponsoring the newsletter? Take a look at our* `sponsorship prospectus </sponsorship/newsletter/>`__.

----------------
Events coming up
----------------

- 09 March, 17:30 MST (Boise, USA) - `Write the Docs Boise Revival Kickoff <https://www.meetup.com/write-the-docs-boise/events/291393490/>`__
- 14 March, 08:30 EST (New England and Florida, USA) - `Focused conversation: Tech writers are user advocates <https://www.meetup.com/ne-write-the-docs/events/cfpnxsyfcfbsb/>`__
- 15 March, 17:30 AEDT (Melbourne, Australia) `Creating more accessible content and documents <https://www.meetup.com/write-the-docs-australia/events/291898839/>`__
- 24 March, 12:00 MST (Boulder/Denver, USA) - `Fourth Friday Write the Docs Co-working Social <https://www.meetup.com/write-the-docs-boulder-denver/events/xkrnctyfcfbgc/>`__
- 27 March, 19:00 EST (Pittsburgh, USA) - `Did AI write this presentation? <https://www.meetup.com/write-the-docs-pittsburgh/events/291842688/>`__
- 28 March, 08:30 EST (New England and Florida, USA) - `Morning Social: Focused conversation for documentarians <https://www.meetup.com/ne-write-the-docs/events/cfpnxsyfcdblc/>`__
