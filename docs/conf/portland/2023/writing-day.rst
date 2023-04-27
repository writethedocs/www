:template: {{year}}/generic.html
:banner: _static/conf/images/headers/writing-day.png

Writing Day
===========

{% include "conf/events/writing-day.rst" %}

Schedule
--------

- Date & Time: **{{date.day_two.dotw}}, {{date.day_two.date}}, {{date.day_two.writing_day_time}} {{tz}}**.
- Location: **{{about.unconfroom}}**.

Exact timing information is available on our :doc:`/conf/{{shortcode}}/{{year}}/schedule` page. 

During the conference
---------------------

Check out the :doc:`/conf/{{shortcode}}/{{year}}/writing-day-cheatsheet` for a quick reference 
that you can use during the conference to make the most out of Writing Day. 

Submit Your Project 
-------------------

We encourage attendees to `submit projects <https://forms.gle/NNBzBCwjdB2vF7ZeA>`_ 
for Writing Day in advance. You are more than welcome to bring a project,
and announce it during the actual Writing Day.

Project Listing
---------------

Here are some of the projects that you can work on during Writing Day!

Raspberry Pi
~~~~~~~~~~~~

At Raspberry Pi we build computers and microcontrollers, and develop the software, documentation, 
and other elements that support them.

The `documentation for Raspberry Pi <https://www.raspberrypi.com/news/bring-on-the-documentation/>`_ grew as we did: 
organically. Over the years, hundreds of community contributors have made thousands of individual 
pull requests, ranging from fixing small typos to contributing whole new sections.

Our online documentation is marked up in AsciiDoc, lives in Git, and is built automatically into 
a static site using GitHub Actions.

Raspberry Pi is looking for Writing Day attendees to contribute to our open source documentation. 
We're looking for contributions that focus on: 

- Copy-editing
- Narrative structure
-  `Style Guide <https://github.com/raspberrypi/style-guide>`_ improvements

We’re looking forward to talking to you about the sort of issues (no pun intended) that come up 
when you’re dealing with a big corpus of unedited documentation that comes from a number of 
different sources — at the same time as incorporating new material into the documentation repo.

Step-ca
~~~~~~~

Step-ca is analogous to the popular public web certificate authority, Let’s Encrypt. 
It is an open-source certificate authority toolkit and ACME server for securely 
automating certificate issuance and management.

Step-ca is the perfect project to get involved with if you’d like to dive into how 
TLS and HTTPS work. You can find  `the codebase <https://github.com/smallstep/certificates>`_ and `the docs <https://github.com/smallstep/docs>`_ on GitHub.

We’re looking for volunteers to help polish and make the style more consistent across 
our most popular doc pages. Our docs are technically correct, but are not very concise. 
We have opened issues for each of such pages and appriopately labeled them Writing Day.

Review each identified page and consider making the following types of improvements:

- Update and use Semantic Linefeeds consistently
- Apply guidelines from `Google's Developer Documentation Style Guide <https://developers.google.com/style>`_.
- Edit for grammar and style issues: convert passive voice to active voice, edit run-on sentences with multiple clauses,
  reorder concepts lists as needed, etc.

If you come across something you can't fix, you're welcome to create an issue on our repository.

Our developer advocate Linda is at Writing Day! She is available to help you understand exactly what’s
needed for these tasks and to help work through any problems. We’re so excited to meet you and merge 
your pull requests!

GitLab Documentation (afternoon-only session)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

GitLab is the open-core project behind the platform that empowers people to collaborate 
on their own projects, primarily to deliver software faster, and more efficiently.

The documentation for GitLab and the GitLab documentation website are open-source 
and maintained by GitLab team members and our community.

As with previous years, we want to invite participants to contribute! Participants can 
get a sense of how to contribute to an open-source documentation project, and how to 
use GitLab. The GitLab platform hosts many open-source projects, so participants will 
hopefully garner the skills to contribute to other projects!

Beginners are welcome as we'll have instructions as well as people on hand to help.

Mutual Aid for Tech Writer/Documentarian Job Hunters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Coordinated by Kenzie Woodbridge, they/them. Kenzie has hosted this session 
for previous virtual Write the Docs conferences during Writing Day.

Are you thinking of applying for a new or different tech writer/documentarian 
jobs and would appreciate feedback on your resume? Or, are you responsible for 
hiring and know what you're looking for in a resume and application? Let's get 
together and offer each other some feedback on the important documentation 
we're using to move our careers forward.

Let's help each other get ready for the job fair!

Doc Detective
~~~~~~~~~~~~~

*Meet the Team, Test Your Docs, and Contribute to Ours.*

`Doc Detective <https://github.com/doc-detective/doc-detective>`__ is
an open-source documentation testing framework that aims to make
it easy to keep your docs accurate and up-to-date. You write
low-code (soon no-code) tests, and Doc Detective runs them
directly against your product to make sure your docs match your
user experience. Whether it's a UI-based process or a series of
API calls, Doc Detective can help you find doc bugs before your
users do.

Doc Detective supports tests in Chrome and Firefox today and plans
to support tests for native iOS, Android, macOS, Windows, and
Linux applications in the future.

Our documentation (and source code) is available on GitHub, and
anyone can contribute it:

#. Take a look at the issues labeled "`writing day <https://github.com/doc-detective/doc-detective/labels/writing%20day>`__".

#. If you don’t find something you’d like to work on, view all issues labeled "`documentation <https://github.com/doc-detective/doc-detective/labels/documentation>`__" or browse `the docs <https://github.com/doc-detective/doc-detective>`__ and find something else you’d like to improve (and log it in a new issue).

#. Once you find the issue you want to work on, add a comment mentioning @hawkeyexl to inform us that you’re working on this for Writing Day (and tell us in person!).

#. Create a pull request with your proposed changes.

#. Once your pull request is reviewed and merged, it will appear on the docs site shortly!

Stop by to chat and build some tests for your docs. If you have
any questions, you can reach out to us in person or on
`Discord <https://discord.gg/tTmczpE4Yd>`__.

Read the Docs
~~~~~~~~~~~~~

Read the Docs is an open source hosting tool, mostly focused on Docs as Code.
This sprint will give you a few options:

* Contribute to their `public documentation <https://docs.readthedocs.io/en/stable/>`_ which is on GitHub
* Try building your Docs as Code documentation `on their platform <https://docs.readthedocs.io/en/stable/build-customization.html#build-commands-examples>`_

The documentation is written in Sphinx & reStructuredText, but you can try out 
your own project using any framework, as long as it's open source.
