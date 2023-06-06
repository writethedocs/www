.. post:: June 06, 2023
   :tags: newsletter

#####################################
Write the Docs Newsletter – June 2023
#####################################

Shalom, documentarians! This month marks a year since I first started putting together this newsletter and it's been a great chance for me to learn morea bout all kinds of topics. If you've enjoyed the newsletter, help me learn even more by reacting the most insightful posts in Slack with the ``:suggest-for-newsletter:`` emoji. Although space is limited each month, I always enjoy seeing what everyone is learning from.

Last month, the Portland conference marked our successful return to in-person conferences. If you missed any part of it, catch up with the `conference recap </conf/portland/2023/news/thanks-recap/>`__, which includes a link to videos of all of the talks. After you get through all the talks, get your tickets for the `Atlantic conference </conf/atlantic/2023/tickets/>`__ and make plans for the `Australia conference </conf/australia/2023/news/welcome/>`__.

To keep your mind fresh in the meantime, we have articles this month on whether to make docs public, where to put comments with code samples, how much work to do *before* you get a job, and what kind of tool to choose to build your docs site. Enjoy and we'll be back next month with more.

-----------------------
Public vs. private docs
-----------------------

In the world of software documentation, it’s pretty common to have your docs free and open to use. But is that right for all products? This month, the community discussed some of the pros and cons.

The main reason given across the board for keeping docs private: the advantages of secrecy. Some companies worry that open documentation allows competitors to copy your ideas and designs. And if you work on security or payments tools, exposing the details of how your software works can make it easier for bad actors to try to attack the tools. However, some folks expressed skepticism about whether keeping docs private is a very effective barrier.

The downsides of private docs were around two areas: friction and marketing. Open docs are easier for your users to access. If they have to remember login information, they may just give up and file a support ticket instead. And docs-as-marketing is a well-worn path: there’s the potential to impress evaluators if the doc set looks useful and explains the product clearly, with Stripe often used as the canonical example.

One last point is that it can be hard to have the conversation just based on the pros and cons. The decision to make documentation public or private often comes from high up in the company and keeping docs private is usually an attempt to protect the company. So if you’re trying to change any minds, be aware that it’s a delicate conversation!

-------------------------------------------
Code samples: Comments and placeholder text
-------------------------------------------

Explanatory text can be vital to understanding a code sample, but does the explanation belong in comments within the sample itself or in the surrounding text? As with so many other aspects of technical writing, both approaches have advantages.

Minimizing comments helps keep code samples clear, well formatted, and easy to read. Separating the explanation from the code also gives readers a chance to absorb information about the logic and purpose of the code sample before they try to interpret it.

The practice of adding comments also has benefits. Given that developers are more likely to read the code samples, comments can be a good way to make sure developers see information they really need to use the samples. Also, because code samples are often designed to be copied and pasted, code comments help ensure that important information stays with the code no matter where it is used.

A related question is where to describe placeholders, those brief bits of text in code samples that users must replace with their own values before deploying the code. Placeholder descriptions are typically included in the explanatory text for a code sample rather than within the sample itself.

To read more about comments and code samples, consider these two books: |book_one|_ and |book_two|_.

.. _book_one: https://www.pearson.com/en-us/subject-catalog/p/developing-quality-technical-information-a-handbook-for-writers-and-editors/P200000000159/9780133118971
.. |book_one| replace:: *Developing Quality Technical Information: A Handbook for Writers and Editors*

.. _book_two: https://docsfordevelopers.com/
.. |book_two| replace:: *Docs for Developers: An Engineer’s Field Guide to Technical Writing*

-----------------------
Extreme take-home tests
-----------------------

With the current spate of layoffs and recent graduations, interviewing practices are hot topics. In a recent discussion, a job hunter asked about the appropriateness of spending a lot of time on a take-home writing test about a company’s product. Working on a take-home test presents certain issues to be aware of.

^^^^
Time
^^^^

The general consensus was to limit any time spent to about 1 hour. Some indicated willingness to spend more time. One person indicated spening an hour doing the assignment, but then providing "an explanation of why I wasn't going to respond to all of their requests."

^^^^^
Money
^^^^^

Many in the thread cautioned about doing work about a company’s product for free. One indicated that expecting significant unpaid work was "a big red flag." This can be a way for a company to get free work from a lot of people. Several remarked that they’ve received payment for completing take-home tests. As an interviewee, you may need to ask about payment, especially if the test requires significant work.

^^^^^^^^^
Ownership
^^^^^^^^^

If you do a writing test, does it belong to you or to the company? In general, if you’re writing about a company’s product, it would belong to the company. You may want to get this clarified because it may affect how long you work on the test and whether you have rights to the work itself. If you spend a lot of time on a writing sample, it may work as a good portfolio piece. So it's worth reesolving the question.

------------------------------------------
Choosing a CCMS or a static site generator
------------------------------------------

When deciding whether to suggest a component content management system (CCMS) like Paligo or a static site builder like MkDocs, there are several things to consider. The first is the team and the people helping. Paligo and other CCMSs demand a specific understanding of XML or the tool itself. This makes them better for teams of writers who can help each other. On the other hand, a static site generator that supports Markdown or other forms that are easy to change might be a better choice if you are a single writer or have users who are not tech-savvy.

Cost is another thing to think about. Markdown and MkDocs are free, but CCMSs like Paligo can be costly. But it’s also important to consider hidden costs. Static site generators, for example, often need theme development, build process upkeep, and document conversions, which can take a lot of time and resources.

You should also consider the documentation method. For example, a CCMS could be a good choice if you want one tool to manage and share user documentation for different user jobs and software modules. These tools can make PDFs and web-based documents and work with single sources from the start. Of course, you can also do this with static site generators, but you have to spend time and effort creating the build steps and themes.

Your choice should be based on how willing you are to learn and understand a certain tool, how many resources you have, and your long-term goals for managing and delivering documentation. To find the best choice for your needs, research and compare different options, like those on the `Jamstack website <https://jamstack.org/>`__.

----------------
From our sponsor
----------------

This month's newsletter is sponsored by ClickHelp:

.. raw:: html

  <hr>
    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="width:100%; max-width: 600px;">
      <tbody>
        <tr>
          <td width="75%">
            <p>ClickHelp is an all-in-one cloud documentation platform for technical writers and software teams. It offers powerful features to create, manage, and publish documentation efficiently. Streamline your process with single sourcing and dynamic output. Improve documentation with advanced analytics and user feedback. Collaborate seamlessly, and track versions effortlessly. Accessible across devices and platforms, supporting multiple formats. </p>
            <p>Experience <a href="https://clickhelp.com/clickhelp-technical-writing-blog/clickhelp-april-2023-blossom-update-overview/?utm_source=wtd&utm_medium=text-link&utm_campaign=writethedocs-newsletter-2023-06"  >the latest Blossom 🌸 release</a> with Markdown import, Confluence migration, interactive screenshots, and more. Start a <a href="https://clickhelp.com/online-documentation-tool-free-trial/?utm_source=wtd&utm_medium=text-link&utm_campaign=writethedocs-newsletter-2023-06"  >free trial</a>  or book a demo to explore cutting-edge features. Join us on this transformative journey with ClickHelp.</p>

          </td>
          <td width="25%">
            <a href="https://clickhelp.com/clickhelp-technical-writing-blog/clickhelp-april-2023-blossom-update-overview/?utm_source=wtd&utm_medium=text-link&utm_campaign=writethedocs-newsletter-2023-06">
              <img style="margin-left: 15px;" alt="Zoomin" src="https://2.helpmonks.com/file/remote?a=6475f555a06b27f947bb3512&e=6346d75d21a5bb6d28f246c5&c=false&n=ClickHelp_logo_300x300.png">
            </a>
          </td>
        </tr>
      </tbody>
    </table>
    <hr>

*Interested in sponsoring the newsletter? Take a look at our* `sponsorship prospectus </sponsorship/newsletter/>`__.

------------------
Featured job posts
------------------

- `Technical Writer for Tor/Arti Documentation (3-4 month contract)  <https://jobs.writethedocs.org/job/1473/technical-writer-for-tor-arti-documentation-3-4-month-contract/>`__, The Tor Project

*To apply for this job and more, visit the* `Write the Docs job board <https://jobs.writethedocs.org/>`_.

----------------
Events coming up
----------------

- 7 Jun, 12:00  PDT (Portland, USA): `Call for organizers <https://www.meetup.com/write-the-docs-pdx/events/293742711/>`__
- 16 Jun, 08:30 EDT (New England and Florida, USA): `Focused Conversation for Documentarians <https://www.meetup.com/ne-write-the-docs/events/xzpxdtyfcjbvb/>`__
- 22 Jun, 19:00  EDT (Toronto, Canada): `Write the Docs Toronto  <https://www.meetup.com/write-the-docs-toronto/events/mnpqgsyfcjbcc/>`__
- 23 Jun, 12:00  MDT (Boulder/Denver, USA): `Fourth Friday Write the Docs Co-working Social <https://www.meetup.com/write-the-docs-boulder-denver/events/xkrnctyfcjbfc/>`__
- 28 Jun, 19:00  MDT (Calgary, Canada): `Write the Docs Calgary Meetup <https://www.meetup.com/wtd-calgary/events/292346923/>`__
- 30 Jun, 08:30 EDT (New England and Florida, USA): `Focused Conversation for Documentarians <https://www.meetup.com/ne-write-the-docs/events/xzpxdtyfcjbnc/>`__
