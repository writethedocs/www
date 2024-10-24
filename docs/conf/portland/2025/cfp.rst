:template: {{year}}/generic.html
:og:image: _static/conf/images/headers/{{shortcode}}-{{year}}-opengraph.jpg

Call for Proposals
==================

It's that time of year again: We're now accepting talk proposals for our next **in-person** {{ city }} conference, coming up on {{date.main}}.

Every year, Write the Docs invites people from all across our community to come up on stage to share their insights and experience. Whether you've worked on documentation for decades or you've just started this year, we want to hear from you!
Read on to learn more about the goals of the conference and what we look for in talk proposals.

{% if flagcfp %}

In the meantime, mark your calendars:

**The deadline for submitting proposals is 11:59 PM {{tz}} on {{cfp.ends}}.**

We'll let you know if your proposal has been accepted by the end of {{cfp.notification}}.
{% else %}
We will announce the CFP dates soon.
{% endif %}

.. contents::
    :local:
    :depth: 1
    :backlinks: none

{% if flagcfp %}

Ready to submit your talk?
You can do that here:

.. raw:: html

    <div class="announcement" style="background-color:white;">
        <div class="uk-container">
        <a style="border-bottom: none; font-size: .875rem;" class="uk-button uk-button-announcement uk-text-center" href="{{ cfp.url }}" target="_blank">Submit your proposal</a>
        </div>
    </div>

{% endif %}

Conference goals
----------------

Write the Docs conferences are our chance to get together to explore and celebrate the craft of documentation in a positive, inclusive environment.

Between the talks on stage, the discussions in the unconference, the collaboration on the writing day and other conversations, 100% of the content for our conferences comes from our community! Whether your job title is writer, developer, product manager, support advocate, librarian, or one of a hundred others, your perspective on what makes good docs is what this conference is all about.

Our goal is to give documentarians a chance to connect and learn from each other. You'll have the chance to compare notes on what's happening in the industry, dig into questions of convention and good practice, and generally nerd out about all the things we love about documentation.

This year, as usual, we're trying to iterate on our tried and tested processes, both to improve our program and to give you, the speakers, a better idea of what to expect.

Who we're looking for
---------------------

The short description here is "if you care about documentation and have something to say about it, we want you to speak"!

That said, there are some more helpful and concrete pointers below.

**Diverse group of speakers**

We welcome talks from first-time speakers, from industry experts, and from everyone in between.
Whatever your background and experience, we prefer hearing about new approaches rather than about tried-and-tested technology.
We especially welcome talks from underrepresented groups within the tech community.
We want to hear a variety of viewpoints, so we limit speakers to two talks in any four year period at each location.

If you're a WTD conference organizer, please only submit talks to conferences you're not actively organizing.

**People on stage**

We *strongly* prefer talks written and given by one *single speaker*. If you're planning to submit with a co-speaker, please let us know why you're doing so.

**Mix of roles and perspectives**

Talks from the scientific community, fiction writers, system administrators, and support staff – in addition to technical writers and software developers – are all valuable to our attendees.

**Diverse audience**

Likewise, we love the diversity of our community, and we encourage support-folks to attend talks about programming, developers to attend talks about writing, writers to attend talks about data, and so on and so forth.

**Past speakers**

Past speaker roles include but are not limited to

* Writers
* Developers
* Designers
* Testers
* Support folks
* Developer advocates
* Community managers
* Scientists
* Librarians
* Teachers

What we’re looking for
----------------------

**Diverse topics**

The focus of Write the Docs is software documentation, and we actively seek talks that address a wide range of related subjects, at various levels of expertise.
Documentation perspectives from other fields are welcome, as are topics from adjacent fields!

**Practicality and positivity**

We prefer talks backed by experience and experimentation to talks about theory, and we definitely don't like talks that bad-mouth technologies or approaches.
Don't tell us why you hate something – tell us how you overcame the problems it was causing.

**Process over tooling**

We avoid talks about specific tooling, which often turn into marketing pitches or tutorials.
We would much rather hear about process, culture, data, people, or the metaphysical side effects of spending your life thinking about docs.

**Audience awareness**

When crafting talk proposals, remember that you're going to be talking to a mix of levels of expertise, skill sets, and professions.
Your talk doesn't have to be relevant to everyone, but it should be relevant to most people and shouldn't make too many assumptions about what people already know.
If you are making those assumptions about what your audience knows, it helps everyone if you state them up front explicitly.

It can be  helpful to check out topics that might be related to your talk from previous years as well:

* `Portland {{year-1}} <https://www.writethedocs.org/conf/portland/{{year-1}}/speakers/>`_
* `Atlantic {{year-1}} <https://www.writethedocs.org/conf/atlantic/{{year-1}}/speakers/>`_
* `Portland {{year-2}} <https://www.writethedocs.org/conf/portland/{{year-2}}/speakers/>`_
* `Prague {{year-2}} <https://www.writethedocs.org/conf/prague/{{year-2}}/speakers/>`_

Not sure about speaking?
------------------------

Don't worry too much about whether we will accept your talk proposal, just submit it anyway, and leave the selection up to us. Just because you're not sure whether your topic is a good fit, feel you don't have enough speaking experience for a conference, or you think someone else may be able to give a better talk on your topic does not mean you don't have awesome things to say.

If you need a hand preparing or honing your talk proposal, there are lots of good places to start:

* **Community mentorship** – We have an ever-growing pool of previous Write the Docs speakers, many of whom are happy to be a second pair of eyes on talk proposals. If you're interested in working with a past speaker, let us know at {{ shortcode }}@writethedocs.org!
* **Meetup brainstorming** – For some in-person workshopping, check in on your `local meetup group <https://www.writethedocs.org/meetups/>`_ and see if they have a talk brainstorming session on their calendar. If they don't... ask if they're planning one!
* **Slack hivemind** – You can also hit up the hivemind directly on the Write the Docs Slack, any time of day! (If you're not registered yet, you can at `https://writethedocs.org/slack/ <https://writethedocs.org/slack/>`_.)
* **Twitter hivemind** – If Twitter is more your speed, `#writethedocs <https://twitter.com/hashtag/writethedocs>`__ will get you there.

Selection process
------------------

We have a small panel of proposal reviewers, and make sure to have a similar diversity in the panel as we're aiming for in our speakers.

We rate talks out of five, and then discuss the top rated proposals, as well as intresting exceptions from that list.

We actively balance for diversity in as many ways as we can, which means that we do not review talks anonymously. Maybe one day the industry will be in a place where can do that, but we're not there yet.

Presentation format
-------------------

Presentations will be scheduled in 30-minute blocks, delivered **in-person, on-stage, live**.

Speaker benefits & logistics
----------------------------

If you are selected to speak at Write the Docs, we will waive your attendance fee.
If speaking incurs any costs that are difficult for you to cover, please `let us know <mailto:{{email}}>`_ and we'll do our best to help out.

If you already have a ticket, we will of course refund it - just drop us an email at `{{email}} <mailto:{{email}}>`_.

{% if flagcfp %}

**You'll hear from us with our proposal decisions by the end of {{cfp.notification}}**.

**You'll be delivering your talk live, in-person in Portland, Oregon**.

{% endif %}

Note that all Speakers must read, understand, and agree to our :doc:`/code-of-conduct`. All talks and slides will need to follow our Code of Conduct. If you are unsure about any aspect of this, please ask us for clarification.

Timeline overview
-----------------

**{{cfp.ends}}**
    Call for Proposal ends

**{{cfp.notification}}**
    We'll let you know whether your proposal was accepted

**{{cfp.slides_by}}**
    We'll ask you for a copy of your slides so that our human captioners can prepare for your talk

**{{cfp.info_by}}**
    We'll ask you for your pronouns, how your pronounce your name and some intersting facts about you so our emcee can prepare to introduce you.

**{{date.short}}**
    Folks start giving talks on stage!

Example proposal
----------------

If you'd like some guidance on how to create a talk proposal, take a look at our :doc:`Example proposal <example-proposal>`.

Questions?
----------

If you have any questions about any part of this process, please email us at `{{email}} <mailto:{{email}}>`_, we'll be happy to chat.

{% if flagcfp %}

Submit your proposal
--------------------------

Submit your proposal at {{cfp.url}}. You'll need to sign up for a Pretalx account, unless you already have one from a previous conference.

.. raw:: html

    <div class="announcement" style="background-color:white;">
        <div class="uk-container">
        <a style="border-bottom: none; font-size: .875rem;" class="uk-button uk-button-announcement uk-text-center" href="{{ cfp.url }}" target="_blank">Submit your proposal</a>
        </div>
    </div>

You'll be able to edit your proposal up until we start reviewing talks.

{% endif %}

Write the Docs Atlantic
-----------------------

If you want to speak at Write the Docs but can't or don't want to attend an in-person event, keep an eye out for Write the Docs Atlantic, coming later in the year.

This conference is entirely virtual, between the Central European Summer Time (CEST) and Eastern Daylight Time (EDT) time zones, so you can present or attend from almost anywhere.

Talks for Write the Docs Atlantic are pre-recorded, with live Question and Answer sessions.
