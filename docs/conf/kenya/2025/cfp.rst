:template: {{year}}/generic.html
:og:image: _static/conf/images/headers/{{shortcode}}-{{year}}-opengraph.jpg
:banner: _static/conf/images/headers/2025/lightning-talks.jpg

Call for Proposals
==================

It's that time of year again: We're now accepting talk proposals for our next **in-person** {{ city }} conference, on {{date.main}}.

Every year, Write the Docs invites people from all across our community to come up on stage to share their insights and experience. Whether you've worked on documentation for decades or you've just started this year, we want to hear from you!
Read on to learn more about the goals of the conference and what we look for in talk proposals.

{% if flagcfp %}

In the meantime, mark your calendars:

- **Deadline: {{cfp.ends}} at 11:59 PM {{tz}}**
- **Acceptance emails: by {{cfp.notification}}**

{% else %}
We will announce the CFP dates soon.
{% endif %}

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

.. contents:: Sections
    :local:
    :depth: 1
    :backlinks: none

Conference goals
----------------

Write the Docs conferences are our opportunity to get together to explore and celebrate the craft of documentation in a positive, inclusive environment.

**Our goal is to give documentarians a chance to connect and learn from each other.**

Between the talks on stage, the discussions in the Unconference, the collaboration on Writing Day and other conversations, 100% of the content for our conferences comes from our community! Your perspective on what makes good docs is what this conference is all about.

You'll have the chance to compare notes on what's happening in the industry, dig into questions of convention and good practice, and generally nerd out about all the things we love about documentation.

Who we're looking for
---------------------

The short description here is "if you care about documentation and have something to say about it, we want you to speak"!

That said, there are some more helpful and concrete pointers below.

**Diverse group of speakers**

We welcome first-time speakers, industry experts, and everyone in between. We especially welcome talks from underrepresented groups within the tech community.

We want to hear a variety of viewpoints, so we limit speakers to two talks in any four year period at each location.

**Number of speakers**

We prefer talks *presented* by one *single speaker*. If you're planning to submit with a co-speaker, please let us know why, and take note that it will affect the chances of your talk being selected.

You are of course welcome to write the talk with other people, if only one person is presenting.

**Mix of roles and perspectives**

Talks from the scientific community, fiction writers, system administrators, and support staff – as well as technical writers and software developers – all are valuable to our attendees.

What we’re looking for
----------------------

**Broad topics**

The focus of Write the Docs is software documentation, and we actively seek talks that address a wide range of related subjects, at various levels of expertise.
Documentation perspectives from other fields are welcome, as are topics from adjacent fields!

**Practicality and positivity**

We prefer talks backed by experience and experimentation to talks about theory, and we definitely don't like talks that bad-mouth technologies or approaches. Don't tell us why you hate something – tell us how you overcame the problems it was causing.

**Process over tooling**

We tend to avoid talks about specific tooling, which often turn into marketing pitches or tutorials. We would much rather hear about process, culture, data, people, or the metaphysical side effects of spending your life thinking about docs.

**New ideas**

This isn't a hard and fast rule, but we're more likely to include talks on topics that have not been covered before than talks that have been touched on in multiple recent conferences.

**Benefit to the community**

How does your talk help improve the quality of documentation everywhere? Are you trying a new approach? Are you solving a known problem? Have you done the research into how folks have tried to solve your issue before?

**Audience awareness**

When crafting talk proposals, remember that you're going to be speaking to a mix of levels of expertise, skill sets, and professions.
Your talk doesn't have to be relevant to everyone, but it should be relevant to most people and shouldn't make too many assumptions about what people already know.
If you are making assumptions about what your audience knows, state them up front explicitly.

Check out topics that might be related to your talk from previous years:

* `Portland {{year-1}} <https://www.writethedocs.org/conf/portland/{{year-1}}/speakers/>`_
* `Atlantic {{year-1}} <https://www.writethedocs.org/conf/atlantic/{{year-1}}/speakers/>`_
* `Portland {{year-2}} <https://www.writethedocs.org/conf/portland/{{year-2}}/speakers/>`_
* `Atlantic {{year-2}} <https://www.writethedocs.org/conf/atlantic/{{year-2}}/speakers/>`_

Writing your proposal
---------------------

Make sure you read this entire page before putting your proposal together, and pay particular attention to the following points:

- **Spoilers** It's pretty normal not to want to include your main point in your abstract, but please make sure to highlight it for the selection committee!
- **Research** We don't need all talks to be about an entirely new topic, but if you're suggesting a talk that looks really similar to one that was given last year, demonstrate that you realize this and mention why yours is different.
- **Tooling** We're pretty serious about preferring talks about people, process or principles than talks about tooling. If you are submitting a proposal about tooling, tell us what makes this one special.
- **Example proposal** Check out our :doc:`example proposal <example-proposal>` so you know what we expect to see in each field.


Unsure about speaking?
------------------------

Don't worry too much about whether we will accept your talk proposal. We encourage you to submit it anyway! You may be unsure if your topic is a good fit, whether you have enough speaking experience, or if someone else might give a better talk on your topic, but that does not mean you don't have valuable and awesome insights to share.

If you need a hand preparing or honing your talk proposal, there are lots of good places to start:

* **Community mentorship** – We have an ever-growing pool of previous Write the Docs speakers, many of whom are happy to be a second pair of eyes on talk proposals. If you're interested in working with a past speaker, let us know at {{ shortcode }}@writethedocs.org!
* **Meetup brainstorming** – For some in-person workshopping, check in on your `local meetup group <https://www.writethedocs.org/meetups/>`_ and see if they have a talk brainstorming session on their calendar. If they don't... ask if they're planning one!
* **Slack hivemind** – You can also hit up the hivemind directly on the Write the Docs Slack, any time of day! (If you're not registered yet, you can at `https://writethedocs.org/slack/ <https://writethedocs.org/slack/>`_.)
* **Twitter hivemind** – If Twitter is more your speed, `#writethedocs <https://twitter.com/hashtag/writethedocs>`__ will get you there.

Selection process
-----------------

We have a small panel of proposal reviewers. We ensure that the diversity in the panel reflects who we aim to have as speakers.

Proposals are rated on a scale of five, after which we meet and discuss the top-rated submissions in detail.

To actively promote diversity, we choose not to review talks anonymously, allowing us to intentionally balance various perspectives and backgrounds.

{% if flagcfp %}

Speaker benefits
----------------

- Opportunity to share your views and perspectives with the community!
- Waived attendance fee.
- Supplemental financial support if needed. If speaking incurs any costs that are difficult for you to cover, `contact us <mailto:{{email}}>`_ and we'll do our best to help out.

If you already have a ticket, we will of course refund it - just drop us an email at `{{email}} <mailto:{{email}}>`_.

Speaker logistics
-----------------

Presentations will be **{{date.short}}**, scheduled in 30-minute blocks, delivered **in-person, on-stage, live in {{city}}**.
Please plan to attend the whole event.

All Speakers must read, understand, and agree to our :doc:`/code-of-conduct`. All talks and slides will need to follow our Code of Conduct. If you are unsure about any aspect of this, please ask us for clarification.

Timeline overview
-----------------

**{{cfp.ends}}**
    Call for Proposal ends

**{{cfp.notification}}**
    We'll let you know whether your proposal was accepted, and ask for some supplementary information about you.
    Make sure to confirm your talk as soon as you get the email.

**{{cfp.slides_by}}**
    We'll ask for a copy of your slides so our human captioners can prepare for your talk

**{{date.short}}**
    Folks start giving talks on stage!

Example proposal
----------------

Take a look at our :doc:`Example proposal <example-proposal>`, with additional guidance on the proposal format:

Submit your proposal
--------------------------

Submit your proposal at {{cfp.url}}. You'll need to sign up for a Pretalx account, unless you already have one from a previous conference.

.. raw:: html

    <div class="announcement" style="background-color:white;">
        <div class="uk-container">
        <a style="border-bottom: none; font-size: .875rem;" class="uk-button uk-button-announcement uk-text-center" href="{{ cfp.url }}" target="_blank">Submit your proposal</a>
        </div>
    </div>

You'll be able to edit your proposal up until the submission deadline. Please be considerate of our reviewers when making changes to talks you've already submitted.

{% endif %}

Questions?
----------

Email any questions about this process to us at `{{email}} <mailto:{{email}}>`_.
