:template: {{year}}/generic.html

Call for Proposals
==================

G'day fellow documentarians! It's that time of the year again.
We’re very excited to announce that we are now accepting talk proposals for our next {{ city }} conference, coming up on {{date.main}}. The conference is virtual this year, so you can speak or attend from anywhere. We will use regular {{ city }} conference times for the scheduling.

Every year, Write the Docs invites people from all across our community to come up on stage to share their insights and experience. Whether you've worked on documentation for decades or you've just started this year, we want to hear from you!
Read on to learn more about the goals of the conference and what we look for in talk proposals.

{% if flagcfp %}
In the meantime, mark your calendars:

**The deadline for submitting proposals is Midnight {{tz}} on {{cfp.ends}}.**

We'll let you know if your proposal has been accepted by the end of {{cfp.notification}}.
{% else %}
We will announce the CFP soon.
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
        <a style="border-bottom: none; font-size: .875rem;" class="uk-button uk-button-announcement uk-text-center" href="{{ cfp.url }}">Submit your proposal</a>
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

**Mix of roles and perspectives**

Talks from the scientific community, fiction writers, system administrators, and support staff – in addition to technical writers and software developers – are all valuable to our attendees.

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

The focus of Write the Docs is software documentation, but we actively seek talks that address a wide range of related subjects, at various levels of expertise.
Documentation perspectives from other fields are welcome, as are topics from adjacent fields!

**Practicality and positivity**

We prefer talks backed by experience and experimentation to talks about theory, and we definitely don't like talks that bad-mouth technologies or approaches.
Don't tell us why you hate something – tell us how you overcame the problems it was causing.

**Process over tooling**

We tend to avoid talks about specific tools, which often turn into marketing pitches or tutorials.
We would much rather hear about process, culture, data, people, or the metaphysical side effects of spending your life thinking about docs.

**Audience awareness**

When crafting talk proposals, remember that you're going to be talking to a mix of levels of expertise, skill sets, and professions.
Your talk doesn't have to be relevant to everyone, but it should be relevant to most people and shouldn't make too many assumptions about what people already know.
If you are making those assumptions about what your audience knows, it helps everyone if you state them up front explicitly.

It can be  helpful to check out topics that might be related to your talk from previous years as well:

* `Australia {{year-1}} <https://www.writethedocs.org/conf/australia/{{year-1}}/speakers/>`_
* `Portland {{year-1}} <https://www.writethedocs.org/conf/portland/{{year-1}}/speakers/>`_
* `Prague {{year-1}} <https://www.writethedocs.org/conf/prague/{{year-1}}/speakers/>`_
* `Portland {{year-2}} <https://www.writethedocs.org/conf/portland/{{year-2}}/speakers/>`_
* `Prague {{year-2}} <https://www.writethedocs.org/conf/prague/{{year-2}}/speakers/>`_

Not sure about speaking?
------------------------

Don't worry too much about whether we will accept your talk proposal, just submit it anyway, and leave the selection up to us. Just because you're not sure whether your topic is a good fit, feel you don't have enough speaking experience for a conference, or you think someone else may be able to give a better talk on your topic does not mean you don't have awesome things to say.

If you need a hand preparing or honing your talk proposal, there are lots of good places to start:

* **Community mentorship** – We have an ever-growing pool of previous Write the Docs speakers, many of whom are happy to be a second pair of eyes on talk proposals. If you're interested in working with a past speaker, let us know at {{ shortcode }}@writethedocs.org!
* **Meetup brainstorming** – For some in-person workshopping, check in on your `local meetup group <https://www.writethedocs.org/meetups/>`_ and see if they have a talk brainstorming session on their calendar. If they don't... ask if they're planning one!
* **Slack hivemind** – You can also hit up the hivemind directly on the Write the Docs Slack, any time of day! (If you're not registered yet, you can at `http://slack.writethedocs.org/ <http://slack.writethedocs.org/>`_.)
* **Twitter hivemind** – If Twitter is more your speed, `#writethedocs <https://twitter.com/hashtag/writethedocs>`__ will get you there.

Because the conference is virtual this year, there is no need for travel, and we're hoping this will make our CFP accessible to more documentarians. We will also provide resources and support for recording your talk.

Selection process
------------------

We have a small panel of proposal reviewers, and make sure to have a similar diversity in the panel as we're aiming for in our speakers.
We rate talks out of five, and then discuss the top rated proposals.

We actively balance for diversity in as many ways as we can, which means that we do not review talks anonymously. Maybe one day the industry will be in a place where can do that, but we're certainly not there yet.

Presentation format
-------------------

Presentations will be scheduled in 30-minute blocks. As the conference is virtual, all talks will be pre-recorded. We will offer resources and support for making your talk recording. After your talk, there will be a live Q&A session. You can opt out of the Q&A if you do not feel comfortable, but please let us know well in advance.

Speaker benefits & logistics
----------------------------

If you are selected to speak at Write the Docs, we will waive your attendance fee. As the conference is virtual, there are no travel costs.
If speaking incurs any costs that are difficult for you to cover, please `let us know <mailto:{{email}}>`_ and we'll do our best to help out.

If you already have a ticket, we will of course refund it - just drop us an email at `{{email}} <mailto:{{email}}>`_.

{% if flagcfp %}
**You’ll hear from us with our proposal decisions by the end of {{cfp.notification}}.**

All talks will be shown prerecorded, and we'll be asking for a **completed video from you by {{cfp.video_by}}**. We have a host of options to support you in making this happen, including the possibility of a live recording call with our videographer. During the conference we'll ask you to participate in a moderated Q&A video session after your talk recording is shown.

{% endif %}

Note that all Speakers must read, understand, and agree to our :doc:`/code-of-conduct`. All talks and slides will need to follow our Code of Conduct. If you are unsure about any aspect of this, please ask us for clarification.

Example proposal
----------------

If you'd like some guidance on how to create a talk proposal, take a look at our :doc:`Example proposal <example-proposal>`.

Questions?
----------

If you have any questions, please email us at `{{email}} <mailto:{{email}}>`_ and let us know.

{% if flagcfp %}

Submit your proposal
--------------------------

Submit your proposal at {{cfp.url}}. You'll need to sign up for a Pretalx account, unless you already have one from a previous conference.

.. raw:: html

    <div class="announcement" style="background-color:white;">
        <div class="uk-container">
        <a style="border-bottom: none; font-size: .875rem;" class="uk-button uk-button-announcement uk-text-center" href="{{ cfp.url }}">Submit your proposal</a>
        </div>
    </div>

{% endif %}
