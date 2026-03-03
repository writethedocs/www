:template: {{year}}/generic.html
:orphan:

Speaker email templates
=======================

.. Make this whole file conditional

{% if cfp_variables['print_templates'] and not flagpostconf %}

.. contents::
   :local:
   :depth: 1
   :backlinks: none

.. note:: These templates use the following types of variables:

      * Standard WTD conference variables {% raw %}``{{tz}}``{% endraw %} (which are expanded)
      * Hidden environment variables {% raw %}``{{cfp_variables['upload']}}``{% endraw %} (which are expanded)
      * Pretalx variables which are only expanded in Pretalx {% raw %}``{name}``{% endraw %}


CFP - Acceptance template
~~~~~~~~~~~~~~~~~~~~~~~~~

Subject:
   WTD {{city}} {{year}} -- talk accepted!

::

   Hi {name},

   The Write the Docs {{city}} talk selection committee has finished the review process and we'd love it if you could join us as a speaker!

   Write the Docs {{city}} {{year}} is **in person** in {{city}} on **{{date.short}}**.

   We think your talk: '{proposal_title}' would be a great fit for the conference. We'd love to have you prepare it for a **30-minute** time slot, with additional questions and answers after that.

   First up, make sure to confirm your speaking slot by doing these **three things** by **Friday 7th February**:

   1. Confirm your **attendance in-person** in {{city}} by clicking the {confirmation_link}

   2. Let us know any of the following:

       ○ If you have a strong preference for presenting on Monday or Tuesday, or in the morning or afternoon.
       ○ If you already purchased a ticket so we can issue you a refund.
       ○ If you would like to have an experienced member of the Write the Docs community mentor you through the talk preparation process.

   3. Update your [Pretalx profile](https://pretalx.com/wtd-{{shortcode}}-{{year}}/me/) with a bio and other information that we'll use to create your speaker profile and get our audience excited about your talk.

   Okay, with all that out of the way, it's time for the fun part: preparing your talk! To make sure everybody's on the same page, here are a few important things to keep in mind:

   * Remember that one of the biggest strengths of the Write the Docs community is that we come from a huge variety of professional and personal backgrounds.
     When you're writing your talk (just like when you're writing documentation), think about the diverse needs and interests of your audience, avoid (or define) any jargon-y language, and make sure you clearly express what people are going to learn from your talk.
   * Remember this is a community conference. If you're representing your employer it's okay to mention that, but please don't treat your talk as a marketing opportunity.
   * Make sure you plan your talk to fit in the allotted time. 30 mins for the the talk itself.There will be Q&A after the 30 mins.
   * Please review our Code of Conduct (https://www.writethedocs.org/code-of-conduct/) and make sure your talk content adheres to it. As a rule of thumb, if you're on the fence about whether something in your talk could be considered inappropriate or offensive, leave it out. If you have a question about the code, feel free to email us and ask!

   If you're concerned about travel expenses, let us know. We do have a budget for speaker expenses, but it can't cover all our speakers.

   As we confirm your details, we'll publish your abstract, profile pic, and information on the conference site. We'll also be emailing attendees so they can share in our excitement about the talks we'll be presenting this year!

   Thanks again for submitting your talk, we look forward to seeing you up on the Write the Docs stage! As you share the good news, remember to tag your posts with #writethedocs. And in the meantime, feel free to email us with any questions, concerns, or ideas.

   Thanks for helping make this year's conference another great one!

   The Write the Docs Team

CFP - Rejection template
~~~~~~~~~~~~~~~~~~~~~~~~

Subject:
   WTD {{city}} {{year}} -- talk decision

::

   Hi {name},

   Thanks so much for submitting a proposal to speak at this year's Write the Docs {{city}}. Every year we receive a growing number of proposals, and we're always blown away by the amazing breadth of knowledge that our community brings to the table.  Unfortunately, presentation spots are limited and the talk selection committee wasn't able to include your talk in our program this year.

   During the review process, each member of the review committee considered each proposal carefully and then compared notes to make their final selections. We thought it might be useful to share a couple of the common themes for why talks may not have been included for this year's event:

   * We had too many good talks. The quality of our submissions gets higher every year, and we always end up having to pass up on some talks that we're really excited by.
   * The subject of the talk was too specific for a larger audience. One of the biggest strengths of the Write the Docs community is that we come from a huge variety of professional and personal backgrounds. The committee looks specifically for talks that appeal to a good mix of our attendees.
   * The subject of the talk was too broad and didn't have a strong enough connection to the core interests of the community.
   * The talk focused heavily on documentation tooling. We think these talks are important, but we tend to showcase higher-level concepts that progress the way we think in the documentation world.
   * There were multiple talks on the same topic. We try to choose talks that cover a wide range of topics, which means making some hard choices between multiple great talks on similar topics.

   Keep in mind that we do run several batches of lightning talks that you can sign up for at the event. We also have an unconference space which is a great chance for more informal discussions. We'd love to have you, your ideas, and your passion at the conference--on stage or not, they're what make this event great!

   If you're not planning on attending Write the Docs {{city}}, or just want to hone your talk online, various [Write the Docs meetups](https://www.writethedocs.org/meetups/) hold virtual meetups, and are always looking for speakers.

   Thanks again for your proposal. We strongly encourage you to submit again, for future events, and in the meantime we hope to see you in {{city}} or online!

   The Write the Docs Team


CFP - Waitlist template
~~~~~~~~~~~~~~~~~~~~~~~

Subject:
   WTD {{city}} {{year}} -- talk decision

::

   Hi {name},

   Thanks so much for submitting a proposal to speak at this year's Write the Docs {{city}} conference. Our selection committee has just wrapped up our review, and we had such a hard time choosing from so many awesome proposals. We'd like to ask if you'd be willing to be on the short list of alternate talks that we'd really like to see, but ran out of room for on the schedule.

   Basically, what this entails is bearing with us for another week or two, while we get confirmations from our other speakers. If we have a speaker turn us down, their slot is yours! We'll let you know, one way or the other, in the next couple of weeks, so you won't have be in suspense for too long. Please reply as soon as you can and let us know if you'd be willing to stick it out.

   Thanks again for your proposal, and either way, we hope to see you at the conference!

   The Write the Docs Team


01 - Speaker logistics template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Subject:
   WTD {{city}} {{year}} -- speaker logistics

::

   Hi {name},

   Just wanted to drop you all a quick note covering some logistics.

   ○ First up, if you wanted a mentor, all of those intros have been sent out. Check your inboxes and spam folders and start talking to the good folks who've agreed to support you in your talk preparation.

   ○ Please make sure to log in to [Pretalx](https://pretalx.com/wtd-{{shortcode}}-{{year}}/me/) and fill out the questions on pronouns, name pronunciation and interests for our emcee intro. We also need your **hoodie size** for a free speaker hoodie!

   ○ Private speaker Slack channel! If you're not on the Slack already, [join the WTD Slack](https://join.slack.com/t/writethedocs/shared_invite/zt-2vbvjxiiv-ZUWUdIuimXQ5Q9q_WDPaQw). Once you're signed up, or if you're already on there, ping me @plaindocs so I can add you to the private speaker channel. It contains many of our past speakers, and myself and other organisers, who will be happy to offer advice or answer questions.

   ○ We're working on a provisional schedule, taking into account all requested time slot preferences, I hope to be able to share that with you in a week or so.

   ○ While you're working on your talks, we'd love for you to check out our [speaker info](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/speaker-info/) page! It's got all sorts of details on talk format, tech specs, content guidelines, etc.

   Also, if you're ever in doubt about whether something you're writing would be appropriate or not, we'd like to refer you to our conference Code of Conduct, which asks that you refrain from any sexually suggestive or harassing language of any kind. Check it out in full, drop me a line if you have questions: http://www.writethedocs.org/code-of-conduct/

   Looking forward to emailing with you all over the coming months.

   The Write the Docs Team



02 - Video recording template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Can skip this one for in-person events.

Subject:
   WTD {{city}} {{year}} -- talk recording

::

   Hi {name},

   Here are the important details you've been waiting for! I'll get into specifics below, but first the important ones:

   ○ We'd love you to upload your recorded talk by the **{{ cfp.video_by }}**, or soon after. If you're likely to need more time, please let me know in advance.
   ○ We have folks who can help you record online, both in US and EU time zones, if this is of interest just let me know and I'll get a slot booked. [Recording guidelines](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/talk-recording-guidelines/).
   ○ As well as the tips in the recording guidelines we've updated the [speaker info](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/speaker-info/) for virtual conferences.

   Now those essentials are covered, a little more info about the event itself:

   * We'll be using [Hopin](https://hopin.to/) for the event, over the coming weeks we'll get you account details so you can update head-shots and taglines on there.
   * We'll be live captioning as usual, and if you can get copies of your slides to make the captioners work easier that would be delightful. We need those a week or so before the event, so no rush.
   * In a change from our in person event, we'll be hosting moderated Q&A in a separate Hopin room, directly after each talk.

   Next week I'll send over a provisional schedule, and if having a particular slot would make it easier to attend the Q&A, let me know and I'll see what I can do.

   And while we're here, ;-) if you don't have a profile picture set in [Pretalx](https://pretalx.com/write-the-docs-{{shortcode}}-{{year}}/login/), now would be a great time to add one.

   And I think that is it! I'm excited to see this taking shape and excited to see all of your hard work on the virtual stage!

   Please get in touch if I can help with anything, if you have worries, thoughts or ideas.

   The Write the Docs Team

03 - Provisional schedule template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Upload:
   {{cfp_variables['upload']}}
Slides by:
   {{cfp.slides_by}}
Provisional schedule:
   {{cfp.preview}}

----

Subject:
   WTD {{city}} {{year}} -- provisional schedule

::

   Hi {name},

   Hope you're all well!

   We're about seven weeks out from the conference now, lots of stuff is happening behind the scenes, and I hope you're feeling good about writing and speaking.

   We've got a [provisional schedule]({{cfp.preview}}) up, I've taken note of all of your requests, but I'd *love it* if you could check your time-slot and make sure it works for you. We'll be publishing it **next Monday**, so please request any changes well before that.

   Q&A sessions are audience driven, moderated by the emcee, and asked in a conversation style directionly after your talk, expect about 5 minutes.

   You might find it useful to check out the [speaker info](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/speaker-info/) and the [what to expect guide](https://www.writethedocs.org/blog/what-to-expect-as-a-speaker/).

   As we've done for the past few years we'll be live captioning all talks, and it makes the [captioners](https://www.youtube.com/watch?v=xFnM6vmvWaI) lives *much* easier if you can send in a copy of your slides, or even a word list of unusual words that you might use. We'll let you know where to send these a few weeks before the conference.

   Lastly, if you'd like to share your talk with your social networks, we've got a page to [help with that](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/speaker-media-kit/).

   And I think that is it! I'm excited to see this taking shape and excited to see all of your hard work on stage!

   Please get in touch if I can help with anything, if you have worries, thoughts or ideas.

   The Write the Docs Team

04 - Speaker tickets
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tickets:
   {{cfp_variables['ticket']}}

----

Subject:
   WTD {{city}} {{year}} -- speaker tickets

::

   Hi {name},

   We're just under a month away from meeting up in {{city}}! I hope you're feeling relaxed and confident.

   The [conference schedule](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/schedule/) is live! :-)

   I've got a couple more small logistical checkboxes for you:

   ○ please register your free [speaker ticket]({{cfp_variables['ticket']}}).

   ○ please make sure to log in to [Pretalx](https://pretalx.com/wtd-{{shortcode}}-{{year}}/me/) and fill out the questions on pronouns, name pronunciation and interests for our emcee intro. We also need your **hoodie size** for a free speaker hoodie!

   Take a look at our *freshly updated* [speaker info page](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/speaker-info/) which has everything you need to know about speaking at Write the Docs! Missing something? Let us know!

   We'll be in touch in a couple of weeks for a copy of your slides for our captioners!

   In the meantime, if you have any questions at all about the event, you definitely know how to reach me by now.

   The Write the Docs Team

05 - Pre conf
~~~~~~~~~~~~~~

Slide uload dir:
   {{cfp_variables['upload']}}


----

Subject:
   WTD {{city}} {{year}} -- final touches

::

   Hi {name},

   The conference is almost upon us! I hope you're all comfortably making the final touches to your presentations, and have your ideas lined up.

   I'm over in Portland already, enjoying the spring weather, and I'm really looking forward to seeing what you'll all be sharing with us at the conference.

   Here are a last few boxes to check when it comes to organization and logistics:

   ○ Please [upload your slides]({{cfp_variables['upload']}}) for the captioners by {{cfp.slides_by}}. If you run into any trouble uploading them, please forward them as attachments to sam@writethedocs.org

   ○ We'll be doing [AV/laptop/slide checks](https://www.writethedocs.org/conf/portland/2026/speaker-info/#conference-schedule) at the stage, either first thing in the morning or right before the lunch break. Please make sure you come say hi and do that, even if you think you don't need to 😉. I'll get some calendar invites out for those slots between now and then. Please bring the laptop you'll be presenting from.

   ○ If you've not already let us know what your pronouns and interests are, and how to pronounce your name, please do [log in to Pretalx](https://pretalx.com/wtd-{{shortcode}}-{{year}}/me/) and answer them, it makes life much easier for the folks doing the intros and Q&A.

   There will be a green room for speakers where you can decompress before or after your talk, please ask me or the reg desk where to find it at the event.

   If you have any questions at all about the event, you definitely know how to reach me by now.

   The Write the Docs Team


06 - Post conf
~~~~~~~~~~~~~~

Feedback:
   {{cfp_variables['feedback_form']}}

----

Subject:
   WTD {{city}} {{year}} -- feedback and THANKS

::

   Hi {name},

   It is a wrap! Thank you one last time for your hard work, insight and creativity. You were amazing!

   ○ Videos of all talks are published on [YouTube](https://www.youtube.com/playlist?list=PLZAeFn6dfHplMbtJtidqFFtL7rt3ASNSR).

   ○ Photos are being uploaded to [Flickr](https://www.flickr.com/photos/writethedocs/albums/72177720325861452/), more photos of the rest of the event will follow soon.

   ○ Sketchnotes are up, also on [Flickr](https://www.flickr.com/photos/writethedocs/albums/72177720325990264).

   We'd love to know how you found the whole process, from A to Z so we can improve next time. To that end we've got an anonymous (keep in mind that there aren't many speakers) feedback form for you here:

   ○ [Speaker feedback form]({{cfp_variables['feedback_form']}})

   Thanks, and see you next time!

   The Write the Docs Team

{% elif flagpostconf %}

The conference is over.

{% else %}

Populate the CFP environment variables to see the email templates.::

   export WTD_CFP_UPLOAD='TODO'
   export WTD_CFP_SPEAKER_TICKET='TODO'
   export WTD_CFP_FEEDBACK_FORM='TODO'
   export WTD_CFP_SPEAKER_GIFT_FORM='TODO'

.. note:: Do this *inside* your `venv` if you're using one. For example in `venv/bin/activate`

{% endif%}
