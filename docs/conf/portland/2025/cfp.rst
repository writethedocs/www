:template: {{year}}/generic.html
:og:image: _static/conf/images/headers/{{shortcode}}-{{year}}-opengraph.jpg

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

**Single vs. co-speakers**

We do strongly prefer talks written and given by a single speaker, and if you're planning to submit with a co-speaker, please let us know why you're doing so.


**Mix of roles and perspectives**

Talks from the scientific community, fiction writers, system administrators, and support staff – as well as technical writers and software developers – all are valuable to our attendees.

**Past speakers**

View our past speaker roles, and always remember, you do not have to fit one of these to be a speaker!

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

**Broad topics**

The focus of Write the Docs is software documentation, but we actively seek talks that address a wide range of related subjects, at various levels of expertise. Documentation perspectives from other fields are welcome, as are topics from adjacent fields!

**Practicality and positivity**

We prefer talks backed by experience and experimentation to talks about theory, and we definitely don't like talks that bad-mouth technologies or approaches. Don't tell us why you hate something – tell us how you overcame the problems it was causing.

**Process over tooling**

We tend to avoid talks about specific tools, which often turn into marketing pitches or tutorials. We would much rather hear about process, culture, data, people, or the metaphysical side effects of spending your life thinking about docs.

**New ideas**

Whatever your background and experience, we prefer hearing about new approaches rather than about tried-and-tested technology.

**Audience awareness**

When crafting talk proposals, remember that you're going to be speaking to a mix of levels of expertise, skill sets, and professions.
Your talk doesn't have to be relevant to everyone, but it should be relevant to most people and shouldn't make too many assumptions about what people already know.
If you are making assumptions about what your audience knows, state them up front explicitly.

Check out topics that might be related to your talk from previous years:

* `Portland {{year-1}} <https://www.writethedocs.org/conf/portland/{{year-1}}/speakers/>`_
* `Atlantic {{year-1}} <https://www.writethedocs.org/conf/atlantic/{{year-1}}/speakers/>`_
* `Portland {{year-2}} <https://www.writethedocs.org/conf/portland/{{year-2}}/speakers/>`_
* `Prague {{year-2}} <https://www.writethedocs.org/conf/prague/{{year-2}}/speakers/>`_

Unsure about speaking?
------------------------

Don't worry too much about whether we will accept your talk proposal. We encourage you to submit it anyway! You may be unsure if your topic is a good fit, whether you have enough speaking experience, or if someone else might give a better talk on your topic, but that does not mean you don't have valuable and awesome insights to share.

If you need a hand preparing or honing your talk proposal, there are lots of good places to start:

* **Community mentorship** – We have an ever-growing pool of previous Write the Docs speakers, many of whom are happy to be a second pair of eyes on talk proposals. If you're interested in working with a past speaker, let us know at {{ shortcode }}@writethedocs.org!
* **Meetup brainstorming** – For some in-person workshopping, check in on your `local meetup group <https://www.writethedocs.org/meetups/>`_ and see if they have a talk brainstorming session on their calendar. If they don't... ask if they're planning one!
* **Slack hivemind** – You can also hit up the hivemind directly on the Write the Docs Slack, any time of day! (If you're not registered yet, you can at `https://writethedocs.org/slack/ <https://writethedocs.org/slack/>`_.)
* **Twitter hivemind** – If Twitter is more your speed, `#writethedocs <https://twitter.com/hashtag/writethedocs>`__ will get you there.

Selection process
------------------

We have a small panel of proposal reviewers. We ensure that the diversity in the panel reflects who we aim to have as speakers. 

Proposals are rated on a scale of five, after which we meet and discuss the top-rated submissions in detail.

To actively promote diversity, we choose not to review talks anonymously, allowing us to intentionally balance various perspectives and backgrounds.

Speaker benefits & logistics
---------------------------

**Benefits** 
- Opportunity to share your views and perspectives with the community!
- Waived attendance fee.
- Supplemental financial support if needed. If speaking incurs any costs that are difficult for you to cover, `contact us <mailto:{{email}}>`_ and we'll do our best to help out.

If you already have a ticket, we will of course refund it - just drop us an email at `{{email}} <mailto:{{email}}>`_.

{% if flagcfp %}

**Logistics**

Presentations will be **May 5-6, 2025**, scheduled in 30-minute blocks, delivered **in-person, on-stage, live in Portland, Oregon.**

All Speakers must read, understand, and agree to our :doc:`/code-of-conduct`. All talks and slides will need to follow our Code of Conduct. If you are unsure about any aspect of this, please ask us for clarification.

CFP proposal
----------------

Below is additional information and ideas to better complete specific prompts in the proposal. 

**Abstract**

This is the content Write the Docs posts on the conference schedule.

Include a brief story, typically two to four paragraphs, describing your personal work experience with the topic. Write to appeal to our audience of documentarians. We’re suspicious of proposals that look like they belong at other conferences.

Include a list of takeaways that our audience can learn from your talk, such as:

- Lessons the audience can apply in their own work
- Ideas the audience should research further
- Spoilers that provide details about the talk

Avoid walls of text. We recommend that you limit your abstract to a maximum of 300 words. If your proposal is accepted, this is what the audience will see in the program when they preview your talk.

**Who and Why**

Answer the questions:
- Who is this talk for?
- Why is this helpful, applicable, important, etc.? 
 
Help your audience think: “Oh yes, this talk could help me when I do X in my work!”

Our audience creates documentation primarily for software. Given the variety of tools used for software documentation, we rarely accept talks that focus on a specific software tool or set of tools. If a talk does include tools, you should also discuss the wider context, applications, and implications of implementing the tools.

Our audience goes beyond the technical writing community. Here’s a typical demographic distribution of people who attend our conferences:

- Technical Writers (60%)
- Developers (10%)
- Support Staff (10%)
- Managers (10%)
- Community Contributors, Enthusiasts & Other Folks (10%)

**Other Information**

Based on your background, use this section to describe your qualifications to the selection committee.

As discussed above, we've welcomed talks from first-time speakers, industry experts, and everyone in between. If you believe that you have something valuable to share, tell us why and submit your proposal.

Submit your proposal
--------------------------

Submit your proposal at {{cfp.url}}. You'll need to sign up for a Pretalx account, unless you already have one from a previous conference.

.. raw:: html

    <div class="announcement" style="background-color:white;">
        <div class="uk-container">
        <a style="border-bottom: none; font-size: .875rem;" class="uk-button uk-button-announcement uk-text-center" href="{{ cfp.url }}" target="_blank">Submit your proposal</a>
        </div>
    </div>

{% endif %}

Questions?
----------

If you have any questions, please email us at `{{email}} <mailto:{{email}}>`_ and let us know.

{% if flagcfp %}

Write the Docs Atlantic 2024
----------------------------

If you want to speak at Write the Docs but can't or don't want to attend an in-person event, keep an eye out for Write the Docs Atlantic, coming later in 2024.
This conference is entirely virtual, between the Central European Summer Time (CEST) and Eastern Daylight Time (EDT) time zones, so you can present or attend from anywhere.