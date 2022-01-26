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

CFP  - Acceptance template
~~~~~~~~~~~~~~~~~~~~~~~~~~

TBD

CFP - Rejection template
~~~~~~~~~~~~~~~~~~~~~~~~

TBD

CFP - Waitlist template
~~~~~~~~~~~~~~~~~~~~~~~

TBD

01 - Speaker logistics template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Subject:
   WTD {{city}} {{year}} -- speaker logistics

::

   Hi folks!

   Just wanted to drop you all a quick note covering some logistics.

   * I've added some questions to our [CFP tool (Pretalx)]({{cfp.url}}) for you about your pronouns, interesting facts and name pronunciation. Please log in at {{cfp.url}} and answer those (although we'll only need them closer to the event).

   * If you haven't done so already, please upload a speaker pic to your Pretalx account, it'll look so much better than the anonymous outline.

   * Private speaker slack channel! If you're not on the slack already, [join the WTD slack](https://join.slack.com/t/writethedocs/shared_invite/zt-tfokbfyb-4Yxwk8oTZGAQDHmITJGQyQ). Once you're signed up, or if you're already on there, ping me @plaindocs so I can add you to the private speaker channel. It contains all of our past speakers, who will be happy to offer advice or answer questions.

   * [Speaker mentoring guidelines](https://www.writethedocs.org/organizer-guide/confs/cfp/#speaker-mentoring) -- let us know if you'd like to talk over your proposal or slide deck with a speaker from a previous year.

   * While you're working on your talks, we'd love for you to check out our updated [Speaking Tips](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/speaking-tips/) page! It's got all sorts of details on talk format, tech specs, content guidelines, etc.

   Also, if you're ever in doubt about whether something you're writing would be appropriate or not, we'd like to refer you to our conference Code of Conduct, which asks that you refrain from any sexually suggestive or harassing language of any kind. Check it out in full, drop me a line if you have questions: http://www.writethedocs.org/code-of-conduct/

   Looking forward to emailing with you all over the coming months.

   Sam

02 - Video recording template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Subject:
   WTD {{city}} {{year}} -- talk recording

::

   Hi Folks,

   Here are the important details you've been waiting for! I'll get into specifics below, but first the important ones:

   - [ ] we'd love you to upload your recorded talk by the **{{ cfp.video_by }}**, or soon after. If you're likely to need more time, please let me know in advance.
   - [ ] we have folks who can help you record online, both in US and EU time zones, if this is of interest just let me know and I'll get a slot booked. [Recording guidelines](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/talk-recording-guidelines/).
   - [ ] as well as the tips in the recording guidelines we've updated the [speaking tips](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/speaking-tips/) for virtual conferences.

   Now those essentials are covered, a little more info about the event itself:

   * We'll be using [Hopin](https://hopin.to/) for the event, over the coming weeks we'll get you account details so you can update head-shots and taglines on there.
   * We'll be live captioning as usual, and if you can get copies of your slides to make the captioners work easier that would be delightful. We need those a week or so before the event, so no rush.
   * In a change from our in person event, we'll be hosting moderated Q&A in a separate Hopin room, directly after each talk.

   Next week I'll send over a provisional schedule, and if having a particular slot would make it easier to attend the Q&A, let me know and I'll see what I can do.

   And while we're here, ;-) if you don't have a profile picture set in [Pretalx](https://pretalx.com/write-the-docs-{{shortcode}}-{{year}}/login/), now would be a great time to add one.

   And I think that is it! I'm excited to see this taking shape and excited to see all of your hard work on the virtual stage!

   Please get in touch if I can help with anything, if you have worries, thoughts or ideas.

   Sam

03 - Provisional schedule template
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Upload:
   {{cfp_variables['upload']}}

----

Subject:
   WTD {{city}} {{year}} -- schedule and upload drive

::

   Hi Folks,

   Hope you're all well!

   We're about five weeks out from the conference now, lots of stuff is happening behind the scenes, and I hope you're feeling good about recording.

   We've got a [provisional schedule]({{cfp.preview}})) up, and I'd *love it* if you could check your time-slot and make sure you can do a live Q&A immediately after your talk is streamed. Note that the talk slots include the Q&A time. We'll make that public on **1st September**.

   A few folks asked where to upload talk recordings when you have them (by **cfp.video_by** right?):

   - [Talk recording upload]({{cfp_variables['upload']}})

   If you'd like help recording that, let me know and I'll book you a slot with our videographer Bart.

   You might find it useful to check out the [Recording guidelines](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/talk-recording-guidelines/) and [speaking tips](https://www.writethedocs.org/conf/{{shortcode}}/{{year}}/speaking-tips/) for virtual conferences.

   As we've done for the past few years we'll be live captioning all talks, and it makes the [captioners](https://www.youtube.com/watch?v=xFnM6vmvWaI) lives *much* easier if you can send in a copy of your slides, or even a word list of unusual words that you might use. Please upload those to the [Talk recording drive]({{cfp_variables['upload']}}) by **{{cfp.slides_by}}**.

   In a few weeks I'll be in touch with some calendar invites for a sound check during the conference, to make sure you're all sorted with Hopin logins, audio and video, and to answer any questions you might have.

   And I think that is it! I'm excited to see this taking shape and excited to see all of your hard work on the virtual stage!

   Please get in touch if I can help with anything, if you have worries, thoughts or ideas.

   Sam

04 - Hopin URL and calendly invites
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Tickets:
   {{cfp_variables['ticket']}}
Calendly:
   {{cfp_variables['calendly']}}

----

Subject:
   WTD {{city}} {{year}} -- hopin and calendly invites

::

   Hi Folks,

   The conference is almost upon us! First off, thank you all so much for all of the hard work you've put into getting the recordings done and uploaded.

   Especially now the recordings are in, all of the hard work is behind you, and you can settle in and enjoy the conference. :-)

   To that effect, please register your free Hopin speaker ticket so we we can connect the account to your talk:

   ➡️ [register your free Hopin speaker ticket]({{cfp_variables['ticket']}})

   The entire conference is held in Hopin, from writing day on Sunday, all talks, unconference sessions, chat, etc. Only the Monday evening social will be held in Spatial.chat.

   I'd also like you to schedule an audio-visual check with me at least **an hour before** your talk. This helps me know you're around 😉 and lets us clear up any audio or visual issues before your Q&A. We recommend you do this even if you're confident about your setup. The audio-visual checks happen in a private Hopin room.

   ➡️ [book an audio-visual check]({{cfp_variables['calendly']}})

   Remember, all Q&A sessions **start at the end of your recording**, in the Speaker Q&A session (the Monday and Tuesday Q&A sessions have different URLs).

   Some speakers like to hang out in the event chat and answer questions during their talk, but that is entirely up to you. We'll be moderating questions regardless, and then the Q&A will be a live video call with the MC.

   If you have any questions at all about the event, you definitely know how to reach me by now.

   Sam

05 - Post conf
~~~~~~~~~~~~~~

Feedback:
   {{cfp_variables['feedback_form']}}
Gift:
   {{cfp_variables['speaker_gift_form']}}

----

Subject:
   WTD {{city}} {{year}} -- feedback, hoodies and THANKS

::

   Hey Folks,

   It is a wrap! Thank you one last time for your hard work, insight and creativity.

   We'll be publishing the videos at some point this week or next, keep an eye on Twitter, Slack or the mailing list for those. 

   We'd love to know how you found the whole process, from A to Z so we can improve next time. To that end we've got an anonymous (keep in mind that there aren't so many speaks) feedback form for you here:

   ➡️ [Speaker feedback form]({{cfp_variables['feedback_form']}})

   Finally, as is tradition at our in person events, we'd love to send you a free WTD speaker hoodie and sketchnote print of your talk, please fill in the form before {{cfp.gifts_by}}.

   🎁 [Speaker gift form]({{cfp_variables['speaker_gift_form']}})

   Sam

{% elif flagpostconf %}

The conference is over.

{% else %}

Populate the CFP environment variables to see the email templates.::

   export WTD_CFP_UPLOAD='TODO'
   export WTD_CFP_SPEAKER_TICKET='TODO'
   export WTD_CFP_CALENDLY='TODO'
   export WTD_CFP_FEEDBACK_FORM='TODO'
   export WTD_CFP_SPEAKER_GIFT_FORM='TODO'

{% endif%}