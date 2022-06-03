.. post:: June 01, 2022
   :tags: newsletter

#########################################
Write the Docs Newsletter – June 2022
#########################################

Hi from your new newsletter editor, Aaron Collier. I'm taking over as editor this month from Beth Aitman and hoping to continue the doses of news and general awesomeness she and the other newsletter volunteers having been regularly bringing to your inboxes.

I certainly have learned a lot from her already on how to make a newsletter useful and interesting. But it's also important to recognize that the heart of the newsletter comes from you, the Write the Docs community. I had a conversation in Slack recently with a long-standing member who didn't realize they could suggest stories to be included.

So as I start this journey, I'd like to (re-)invite you to come with me. If you see a conversation in Slack you think would be great for the newsletter, tag it with the ``:suggest-for-newsletter:`` emoji. We'll round up the most interesting and thought-provoking ideas and bring them to you.

The past month was full of goodness outside the newsletter as we wrapped up the Portland conference. Those who were there talked a lot about how great all the talks and unconference sessions were. For those of us who couldn't make it, check out the `videos of all the talks on YouTube <https://www.youtube.com/playlist?list=PLZAeFn6dfHpnDhFvXG8GprqlLlzSQRBui>`__ to at least see the talks.

Looking to the future, the `Call for Proposals for the Prague conference <https://www.writethedocs.org/conf/prague/2022/cfp/>`__ is open until the end of the month. So don't hesitate to submit your idea.

But enough from me. Let's get to what's been on your minds this month.


-----------------------
Whether to say "please"
-----------------------

In a recent discussion, the WTD community was trying to figure out: does the magic word, *please*, have a place in how-to documentation and instructions?

Style guides (like `Google's <https://developers.google.com/style/tone?hl=en#politeness>`__) usually advise against it for a simple reason: conciseness. "Please" doesn't add any information; an instruction remains the same instruction, with or without please. So going by the principle of removing unnecessary words, pleasantries should be removed.

But it's not quite as simple as that because "please" does change the meaning, making a phrase into a request that could be optional. For something that's required, leaving out "please" may be the safest bet.

It's common to see "please" used when the writer is trying to be friendly or polite. Direct instructions can come across as rude to some people or in some cultures. And when the user is disgruntled, "please" can be softening -- appropriate when you're asking the user to do something annoying or when it's your software's fault ("If the application crashes, please send us the following troubleshooting information…"). This is particularly relevant when you're writing `error messages <https://medium.com/the-devil-wears-product/error-messages-please-vs-no-please-90cebdfb2ea5>`__. However, the counter-argument is that the politest thing to do is not to waste the user's time. You can be polite by being clear and concise, rather than by starting every instruction with please.

If what is considered polite varies across cultures, translation may have an impact too. The community was pretty uncertain about this one though. On the one hand, it might be best to leave your translator to decide how polite the phrasing should be. On the other, many translations are done word-for-word, so you most likely will need to make a judgement call after all.

-------------------------------------------------
Edge cases and when (and where!) to document them
-------------------------------------------------

A question about the extent to which we should cover edge cases in UI text produced yet another thoughtful and informative discussion. In response to questions such as whether to provide or avoid UI text for edge cases, what constitutes a "major" edge case, and what full coverage of all edge cases might look like, our invincible community produced the following wisdom:

* Maybe features specifically for edge cases would be a better place than a generic part of the UI.
* One rule of thumb is if a case applies to fewer than 20--25% of users, don't worry about it in the UI. This is especially true because there's rarely room for it. But one person suggested that, depending on the larger context, you might want to lower that threshold to 5%.
* Other strategies could include different product design, including progressive disclosure, depending on how users interact with your application.
* Might risk mitigation be another meaningful variable in determining how and how much to explain an edge case? For example, even if only one major customer occasionally experiences a major disruption only some of the time, if the impact to the business is great, maybe it should be explained in either the UI or the documentation.
* The documentation might be the best place for exhaustive explanations of edge cases -- especially for complex security scenarios.

---------------
Estimating work
---------------

Estimating the time it will take to complete a task or assigning story points for work can be challenging, especially if you haven’t done it in a long time. If you find yourself in this situation, there are a few ways to help you correctly approximate the hours or effort needed.

To start, you might consider eight hours to be equal to about one page of work. This calculation can be useful whether you use Flare or other authoring software, but it is often tricky to determine how many pages you have to begin with. Check out a `helpful guide on estimating writing projects <https://writingassist.com/pdfs/EstimatingWritingProjects.pdf>`__ for more tips.

Another option for evaluating work is to `assign story points <https://www.atlassian.com/agile/project-management/estimation>`__ where one point equals half a day of work, two points equals one day, and ten points equal a business week. Though subjective assumptions about the degree of effort for a unit of work may appear odd, it is essential to keep in mind that story points are not time-based and therefore differ from hours.

Instead of focusing on hours, you might think of story points as a more reliable indicator of effort that helps in the division of work. Finally, remember that story points can be assigned based on factors other than just effort, such as complexity and uncertainty.

When used correctly during team planning, story points can give quick approximations, improve project forecasts, and even provide managers with actual statistics during hiring conversations.

------------------
What we’re reading
------------------

The #bipoc group’s been discussing the following materials on diversity, inclusion, and equity. Want to join the conversation? Please join us in the `#bipoc Slack channel <https://writethedocs.slack.com/archives/C016STMEWJD>`_!

A short read: Talent Management describes why `many DEI efforts fall flat and how belonging may be the key <https://www.talentmgt.com/articles/2022/05/10/effectively-creating-belonging-why-diversity-efforts-fall-short/>`__.

A medium read: Want to be more supportive of underrepresented groups but aren't sure how? The Muse offers `seven examples of how to become an ally in the workplace <https://www.themuse.com/advice/what-is-an-ally-7-examples>`__.

A longer read: Now a national holiday in the United States, June 19th is Juneteenth. Want to learn more about it? Oprah `explains the history of Juneteenth <https://www.oprahdaily.com/life/a32893726/what-is-juneteenth/>`__.

----------------
From our sponsor
----------------

This month’s newsletter is sponsored by KnowledgeOwl:

.. raw:: html

    <hr>
    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="width:100%; max-width: 600px;">
      <tbody>
        <tr>
          <td width="75%">
          <p>In the past, the <a href="https://www.knowledgeowl.com/home/blog">KnowledgeOwl blog</a> has covered a wide range of topics from guest bloggers and staff. Now we're tightening our focus to something we care passionately about: Documentarian Quality of Life.&nbsp; </p>
          <p>So we owls have come with a request: we need your help. What are your biggest pain points? What deep-dive posts would you like to see?</p>
          <p>We're also seeking 🦉 owl-themed names 🦉 for our new blog categories (and can offer swag in return). </p>
          <p>See <a href="https://www.knowledgeowl.com/home/our-new-content-strategy">our latest blog post</a> for more details on this shift and how to send us your suggestions. </p>
          </td>
          <td width="25%">
            <a href="https://www.knowledgeowl.com/home/blog">
              <img style="margin-left: 15px;" alt="SPONSOR" src="/_static/img/sponsors/knowledgeowl-owl.png">
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

- `Technical Writer <https://jobs.writethedocs.org/job/718/technical-writer/>`__, Wix (Vilnius, Lithuania )
- `Technical Writer (Developer Documentation) <https://jobs.writethedocs.org/job/717/technical-writer-developer-documentation-fully-remote/>`__,  Humanitec GmbH (Remote)
- `Technical Writer, Serverless, Google Cloud <https://jobs.writethedocs.org/job/731/technical-writer-serverless-google-cloud/>`__, Google (Kitchener, ON, Canada)
- `Technical Writer (IntelliJ) <https://jobs.writethedocs.org/job/735/technical-writer-intellij/>`__, JetBrains (various locations)
- `Senior Manager, Technical Writing, Developer Acceleration Platforms <https://jobs.writethedocs.org/job/729/senior-manager-technical-writing-developer-acceleration-platforms/>`__, Google (Seattle, WA, USA)
- `Technical Content Strategist, Developer Relations Content, Google Cloud <https://jobs.writethedocs.org/job/727/technical-content-strategist-developer-relations-content-google-cloud/>`__, Google (Seattle, WA, USA)
- `Product Documentation Manager <https://jobs.writethedocs.org/job/714/product-documentation-manager/>`__, ReadMe (Remote)
- `Technical Writer, Software Engineering <https://jobs.writethedocs.org/job/733/technical-writer-software-engineering/>`__, Google (Remote)
- `Developer Educator - Remote APJ <https://jobs.writethedocs.org/job/725/developer-educator-remote-apj/>`__, Twilio (Remote)
- `Developer Evangelist <https://jobs.writethedocs.org/job/726/developer-evangelist/>`__, Twilio (Remote)
- `Technical Writer, Cloud Technologies and Tools <https://jobs.writethedocs.org/job/732/technical-writer-cloud-technologies-and-tools/>`__, Google (Waterloo, ON, Canada)
- `Technical Writer, Cloud Data Analytics, Streams and Lakes <https://jobs.writethedocs.org/job/730/technical-writer-cloud-data-analytics-streams-and-lakes/>`__, Google (Remote)
- `Technical Writer, Data Analytics, BigQuery, Google Cloud <https://jobs.writethedocs.org/job/728/technical-writer-data-analytics-bigquery-google-cloud/>`__, Google (Durham, NC, USA)
- `Technical Writer (Kotlin) <https://jobs.writethedocs.org/job/736/technical-writer-kotlin/>`__, JetBrains (various locations)
- `Developer Advocate <https://jobs.writethedocs.org/job/743/developer-advocate/>`__, Trunk (Remote [USA])
- `Technical Writer <https://jobs.writethedocs.org/job/649/technical-writer/>`__, Semaphore  (Remote)

*To apply for these jobs and more, visit the* `Write the Docs job board <https://jobs.writethedocs.org/>`_.

------------------------
Virtual events coming up
------------------------

- 07 June, 08:30 EDT (East Coast Quorum, USA) - `Morning social <https://www.meetup.com/ne-write-the-docs/events/hqvdfsydcjbkb/>`__
- 07 June, 08:30 EDT (Florida, USA) - `Morning social <https://www.meetup.com/write-the-docs-florida/events/qpvdfsydcjbkb/>`__
- 08 June, 18:00 CDT (Austin, USA) - `Why you should be "docs-as-code"-ing, with DevDocs CEO <https://www.meetup.com/WriteTheDocs-ATX-Meetup/events/285797949/K>`__
- 20 June, 12 AEST (Australia) - `Better customer experiences using Machine Learning <https://www.meetup.com/Write-the-Docs-Australia/events/285712379/>`__
- 21 June, 08:30 EDT (East Coast Quorum, USA) - `Morning social <https://www.meetup.com/ne-write-the-docs/events/hqvdfsydcjbcc/>`__
- 30 June, 19:00 PDT (West Coast/Australia Quorum) - `User Research for Technical Writers <https://www.meetup.com/virtual-write-the-docs-west-coast-quorum/events/286322885/>`__
