.. post:: October 05, 2020
   :tags: newsletter

########################################
Write the Docs Newsletter – October 2020
########################################

Hi everyone - it’s Beth A and the newsletter team here, back from our summer break. I hope you’ve all had a chance to take a break too recently; I’m feeling the need for time off more than ever.

But there’s plenty to look forward to in the world of documentation! It’s just a few short weeks until our second virtual conference of the year - `"Prague" </conf/prague/2020/>`__, or more accurately, "the one in `CEST <https://time.is/CEST>`__". The `speaker list </conf/prague/2020/speakers/>`__ is out and looking great, so do `grab a ticket </conf/prague/2020/tickets/>`__ while they’re still available! (Ticket sales will close about a week before the conference.) I’ll be helping out on the `Welcome Wagon </conf/prague/2020/welcome-wagon/>`__, so if you’re attending the conference, please do say hi - I’d love to meet you.

And if the Europe and America conferences weren’t in good time zones for you, fear not: our last conference of the year is for you! The `Australia and India conference </conf/australia/2020/>`__ (that’s in `AEDT <http://time.is/AEDT>`__) will be on 3-4 December, and we’ve just announced `the speaker line-up </conf/australia/2020/news/announcing-speakers/>`__.

Finally, a request. Like we did `last year </surveys/salary-survey/2019/>`__, we’re running an anonymous salary survey, to help the community understand the pay scales and benefits in the software industry around documentation. We’d absolutely love it if you could fill it in; it’s open until Monday 16 November. `Find out more here </surveys/salary-survey-sep-2020/>`__.

-------------------------------------
Learning regular expressions (regex)
-------------------------------------

When a documentarian asked if there is an automated way to update links from one format to another, the WTD Slack community replied, "Yes: regex!" A `regular expression <https://en.wikipedia.org/wiki/Regular_expression>`__, shortened to regex, is a sequence of characters that represent a search pattern. The specific sequence depends on the search you want to perform. Regexes are handy for finding and replacing text, finding typographical errors or misspellings, creating link redirects for multiple versions of docs, and similar tasks. A very basic regex is `[abc]`, which will find any character between the brackets -- a, b, or c -- no matter where the characters fall within the text you're searching.

Regular expressions are useful and time-saving, but they do have a bit of a learning curve. Fortunately, the group had great suggestions to help get you started:

* `regular expressions 101 <https://regex101.com/>`_: A regex testing and validation tool with a searchable library, quiz, and sample code generator
* `Rex Egg <http://www.rexegg.com/>`_: This lighthearted tutorial assumes a beginner's starting point
* `Regular expression syntax cheatsheet <https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Regular_Expressions/Cheatsheet>`_: A list of JavaScript-specific regex syntax by MDN Web Docs
* `Ryans Tutorials Grep and Regular Expressions <https://ryanstutorials.net/linuxtutorial/grep.php>`_: When you're ready to pair regex with grep to search text for your regex, try this guide and the accompanying `cheatsheet <https://ryanstutorials.net/linuxtutorial/cheatsheetgrep.php>`_
* `Advanced Bash Scripting Guide Chapter 18 Regular Expressions <https://tldp.org/LDP/abs/html/regexp.html>`_: If you're comfortable working from the command line, this lesson takes you through a regex overview and provides example commands for grepping a text file

-------------------------------------
Organizing docs by role, or by topic?
-------------------------------------

This fall, we fell into a discussion of role-based docs versus topic-based docs, and the reasons to use one over the other. Is it better to organize your documentation by user role or by topic?

With role-based docs, users may spend too much time identifying which type of user you consider them to be. And once they do identify their type, the docs can end up resembling a training course more than a documentation set. A single user can wear many hats, and they then end up needing to jump around more in the docs to do their work; there’s more in `this article from the Nielsen Norman Group <https://www.nngroup.com/articles/audience-based-navigation/>`__. Topic-based docs can allow users to easily go to the topic with the information they need - as long as they can actually find the right topic in the group of topics.

A sensible way forward can be to combine both ideas: for example, providing a list of links to topics associated with a role; or allowing a user to filter a list of topics by role. It also depends a lot on your specific product, and the audience for it: role-based docs may work well for some products, while topic-based docs may be just the thing for others.

-----------------------
Command prompts in docs
-----------------------

Command prompts in docs can be useful visual cues for developers - they provide the context in which to run each command. They also show at a glance that the snippet displays a terminal command and not something else, like a config file. But to avoid mistakes during copying and pasting, our community has these suggestions on integrating the prompt character in documentation:

* Include prompts if the user modes change or are otherwise relevant to the instructions.
* Include prompts for multiple commands in the same snippet, but consider avoiding prompts for single-line snippets.
* Don’t include the command prompt in the same box as the output.
* Make a clear distinction between the command and output. For example, separate them into different listings with labels and distinguish the prompt by color.
* If you don’t want the prompt character to be copyable, try the user-select css property. Or, if you have control over its behaviour, have the copy button in the snippet ignore the prompt character.

------------------------------------------
What we're learning in #learn-tech-writing
------------------------------------------

Over in the `#learn-tech-writing <https://app.slack.com/client/T0299N2DL/C7YJR1N02>`__ book club, they’re reading through *Don’t Make Me Think* by Steve Krug. One recent conversation was about documentation structure design: both for individual pages of documentation, and for doc sites too.

At the page level, it’s about making pages scannable. You can break them up into clearly defined areas using headings, and it also helps to use short paragraphs and lists. One documentarian talked about using images to make pages look less daunting - while you want to avoid adding gratuitous images, they do really help break up pages visually.

For a doc set, how do you make it easy for readers to find what they need? People search for information in different ways: some stick to Google or the site search, some scan and click around. It helps to talk to your users to find out, but you can’t expect them all to work the same way. And we have to be aware that our personal preferences don’t necessarily match those of our readers.

A big point of discussion was on how to divvy up pages. At one extreme is individual short pages for each topic (About the Feature, Using the Feature, Reference for the Feature...). It can mean more clicking around, but *Don't Make Me Think* suggests: "It doesn’t matter how many times I have to click as long as every click is a mindless, unambiguous choice."

The other extreme is to have everything on one page, and a table of contents to let readers skim and skip through, like the `Asciidoctor manual <https://asciidoctor.org/docs/user-manual/#glossary>`__.

There’s no best answer here. It’s a tradeoff between scrolling/ctrl+F vs clicking/searching to find what you need. And it depends on who you’re optimising for. For new users, a huge page can be overwhelming and intimidating; you don’t know what’s important and what you can skip. But once you’ve gotten used to the content, if you’re going to refer back to it a lot, one page can be pretty convenient.

There are tons more interesting ideas flying about in the book club, so do `take a look <https://app.slack.com/client/T0299N2DL/C7YJR1N02>`__!

----------------
From our sponsor
----------------

This month’s newsletter is sponsored by Microsoft:

.. raw:: html

    <hr>
    <table width="100%" border="0" cellspacing="0" cellpadding="0" style="width:100%; max-width: 600px;">
      <tbody>
        <tr>
          <td width="75%">
              <p>

              Want the simplicity of a source code editor with powerful developer tooling?  Try the lightning-fast, lightweight, massively customizable editor that is taking the world by storm.  Did we mention it’s free and supports MacOS, Linux, and Windows?  To learn more and grab your copy, head here: <a href="https://code.visualstudio.com/docs/editor/whyvscode">https://code.visualstudio.com/docs/editor/whyvscode</a>.
              </p>
          </td>
          <td width="25%">
            <a href="https://blogs.microsoft.com/?p=52559013">
              <img style="margin-left: 15px;" alt="Microsoft" src="/_static/img/sponsors/microsoft.png">
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

* `Director of Product Content <https://jobs.writethedocs.org/job/226/director-of-product-content/>`__, Mews
   Prague, full-time
* `Technical Writer <https://jobs.writethedocs.org/job/228/technical-writer/>`__, AlertMedia
   Austin Texas, full-time
* `Senior Technical Writer <https://jobs.writethedocs.org/job/227/senior-technical-writer/>`__, Awesome Table
   Remote (Europe), full-time

*To apply for these jobs and more, visit the* `Write the Docs job board <https://jobs.writethedocs.org/>`_.

------------------------
Virtual events coming up
------------------------

* 7 October - Philadelphia, PA, USA - `Breaking down complex topics into documentable chunks <https://www.meetup.com/WTD-Philadelphia/events/272488330/>`__
* 8 October - Los Angeles, CA, USA - `Open-source docs for Sawppy <https://www.meetup.com/Write-the-Docs-LA/events/273649263/>`__
* 13 October - Ottawa - `WTD Ottawa Shopify meetup <https://www.meetup.com/Write-The-Docs-YOW-Ottawa/events/xtcbgqybcnbrb/>`__
* 15 October - Austin, TX, USA - `"We miss you!" social hour <https://www.meetup.com/WriteTheDocs-ATX-Meetup/events/273573027/>`__
* 18-20 October - `Write the Docs "Prague" conference </conf/prague/2020/>`__
* 19 October - Detroit, MI, USA - `Emotional personas: writing for the human animal <https://www.meetup.com/Write-the-Docs-Detroit/events/273639865/>`__
* 20 October - Boston, USA - `Morning Social <https://www.meetup.com/meetup-group-RuYaCcRS/events/273665258/>`__
* 21 October - Portland, OR, USA - `Supermeetup: tech industry job panel <https://www.meetup.com/Write-The-Docs-PDX/events/273387204/>`__
* 28 October - Australia - `Introducing Information Architecture <https://www.meetup.com/Write-the-Docs-Australia/events/273289549/>`__
