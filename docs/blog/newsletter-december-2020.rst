
.. post:: December 03, 2020
   :tags: newsletter

#########################################
Write the Docs Newsletter – December 2020
#########################################

Hey everyone - it's Beth bringing you the final WTD newsletter of the year.

I hope you're all holding up okay. I haven't got any grand thoughts on how to sum up this year, or how we'll handle what's next. But I do want to thank all of you for being part of this community - for your conversations, your contributions, your insights and support and wit and sarcasm. They're what Write the Docs is built on. So thanks, for making our Slack and the three conferences into a source of support and connection - in a year when we've needed it more than ever.

We're already looking towards 2021, and have `just announced </conf/portland/2021/news/welcome/>`__ that Write the Docs Portland will be our fourth virtual conference, on April 25-27. Mark your calendars, and keep an eye out for the Call for Proposals - it's coming sometime in December.

That's it from me. I hope you enjoy our write-ups of what's been happening in Slack; and I wish you a restful holiday season, and the best of luck for 2021.

-----------------------------------------------------
Trying to change when "we've always done it that way"
-----------------------------------------------------

When you're newly charged with stewarding documentation that's been around for a while, it's common to find big things you want to change and polish. But what about that nagging feeling that your manager, your customers, and other stakeholders like the docs just the way they are?

Documentarians who have grappled with this dilemma had some suggestions. First, evaluate whether you have managerial buy-in for the kinds of changes you want to make. If the focus is on documenting new features and fixing errors, you may not find much enthusiasm for reorganization projects. Figuring this out in advance keeps you from wasting work you can't implement or even shipping the start of changes you can't complete (which can leave the docs in a worse state than you found them).

If your manager is generally happy with the status quo but is open to considering your ideas, start with a small example of the changes you'd like to make. This gives you a chance to demonstrate your improvements without spending too much time and effort on work your manager may or may not support.

Finally, customers and other users who are familiar with the existing docs often handle changes quite well if the changes truly improve findability and readability in the docs. The key here is making sure that the changes are clear improvements that justify any inconvenience users experience as they learn the new docs.

-------------------------------------------
Cleaning up your docs style - automatically
-------------------------------------------
​
Docs linting has been getting a lot of attention on the WTD Slack lately. Here's the most recent collective wisdom from the hivemind!

- `Vale <https://github.com/errata-ai/vale/>`_ seems to be the linting tool of choice, most often supplemented with custom rules or third-party rulesets.
- A community member has posted videos to help folks get started. See `Documentation as code (Part 3): A Linting How To - The Vale Linter in Action <https://www.youtube.com/watch?v=p1pfwpMv2wU>`__, from Lynette Miles (@esmerel on Slack).
- Most workflows seem to rely on local linting only, but a few brave souls integrate into an integration pipeline. This seems to be a safer or easier approach if you're building the docs only - that is, if they aren't part of a larger product/code build.
- One solution to the problem of breaking the build because of spelling errors is to run linting at the commit level. It's a variant of the local approach, but integrated into the larger doc workflow instead of relying on individual local integrations of Vale.
- Linting can help maintain consistent enforcement of a style guide - for writers as well as non-writers! 
- It's also useful for an MVP implementation of readability standards. You can lint for simpler words, or simpler grammar.
- To help you when tidying up resolving merge conflicts, it's a good idea to lint for conflict markers!

------------------------------
The best time to use a tooltip
------------------------------

Tooltips and online help are very different tools for providing information to users. How do you choose between them?

The main response from Slack was that it's not a binary choice, and both are useful when implemented well. In fact, they support each other: the brief details in a tooltip can link to online help for fuller details.

Tooltips are simpler for users to access than online help, but they're limited in the amount of text they can contain. They're at their best when they enhance the interface - for example, showing that a component has a keyboard shortcut. Just be careful, as it's not always easy for users to tell that a tooltip is available.

Not every element needs a tooltip! If the information you'd put in a tooltip is obvious, it doesn't add much value. In contrast, good tooltip candidates are elements that new users are likely to have a question about, or that aren't very clear by themselves, but make much more sense with a little bit of extra information.

Be aware of how easy the tooltip content is to consume: it needs to be short and readable. If something takes several paragraphs to explain, or many lines of text, it's hard for users to take in via tooltip. Linking directly to online help is probably better.

One final warning: if tooltip text is scattered among many source code files, it can be a big challenge on the maintenance side. Keeping them all in one resource file can help, especially if you're going to localize the help.

----------------
From our sponsor
----------------

This month’s newsletter is sponsored by `Paligo <https://bit.ly/3fuibKK>`__:

.. raw:: html

    <hr>
    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="width:100%; max-width: 600px;">
      <tbody>
        <tr>
          <td width="75%">
              <p>
              <a href="https://bit.ly/3fuibKK">Paligo is an all-in-one cloud-based CCMS platform.</a> Authoring, versioning, branching, release workflows, publishing, translation management, and more - all updated continuously in the cloud. No more worrying about locally installed software and deployment!
              </p>

              <p>
              Read the case study: <a href="https://bit.ly/2UV2uCQ">https://bit.ly/2UV2uCQ</a>
              </p>
          </td>
          <td width="25%">
            <a href="https://bit.ly/3fuibKK">
              <img style="margin-left: 15px;" alt="Paligo" src="/_static/img/sponsors/paligo.png">
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

- `Technical Documentation Manager <https://jobs.writethedocs.org/job/248/technical-documentation-manager/>`__, Layer (remote - Europe)
- `Technical Proposal Writer <https://jobs.writethedocs.org/job/256/technical-proposal-writer/>`__, Elsevier (Amsterdam, Netherlands)
- `Technical Writer <https://jobs.writethedocs.org/job/258/technical-writer/>`__, Red Hat (Bangalore, India)
- `Technical Writer <https://jobs.writethedocs.org/job/259/technical-writer/>`__, Red Hat (Pune, India)
- `Senior Technical Writer <https://jobs.writethedocs.org/job/260/senior-technical-writer/>`__, Graylog Inc (remote - USA)
- `Technical Editor <https://jobs.writethedocs.org/job/255/technical-editor/>`__, Semaphore (remote)

*To apply for these jobs and more, visit the* `Write the Docs job board <https://jobs.writethedocs.org/>`_.

------------------------
Virtual events coming up
------------------------

- 03 December, 08:30 CST (Austin, TX, USA) - `Virtual Coffee <https://www.meetup.com/en-AU/WriteTheDocs-ATX-Meetup/events/274630337/>`__
- 16 December, 18:00 EST (Toronto, Canada) - `Write the Docs Toronto <https://www.meetup.com/en-AU/Write-the-Docs-Toronto/events/rwphwrybcqbvb/>`__
- 12 January, 19:00 MST (Calgary, Canada) - `Inaugural Write the Docs Calgary Meetup <https://www.meetup.com/en-AU/wtd-calgary/events/274926516/>`__

