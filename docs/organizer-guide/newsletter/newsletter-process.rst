Write the Docs newsletter
#########################

At the beginning of every month, we put out an `email newsletter </newsletter/>`__ to the community - around {{newsletter_subs}} readers. It's built around a handful of stories that we capture and write-up from the Slack team; also includes an overview of what the org team is working on, a calendar listing of upcoming community events, and featured jobs from the jobs board.

This doc explains how to put the newsletter out each month. We take two breaks a year when we don't publish - we don't put out a newsletter in January or August.

`Handy link to the archives </blog/archive/tag/newsletter/>`__.

Collect stories from Slack (throughout the month)
*************************************************

The newsletter team keeps an eye on the WTD Slack and flags conversations they think might be a good fit by tagging them with the ``:suggest-for-newsletter:`` emoji. The 'Reacji Channeler' plug-in automatically sends the tagged post to the #newsletter-slushpile channel.

Every week or two, the editor copies and pastes those conversations into a Google doc, so nothing gets swallowed up by the Slack limit. You can set the channel to send you notifications if that helps. Keep an eye out for links and images, which sometimes don't get copied correctly

We usually end up capturing 15-20 topics, from which we end up picking 4.

Some of the things we look for are:

* conversations that yield a lot of practical advice about a topic
* conversations that clearly strike a chord with the audience
* conversations that highlight two sides of a docs problem/topic

Assign stories (7-10 days before shipping)
*******************************************

A week before the planned ship date, the editor should:

1. Go through the conversations they've captured.
2. Select 4 or 5 conversations they think would make a good edition.
3. Copy all of the conversations into a new Google doc, to share with the writers. (`Example <https://docs.google.com/document/d/1XUuoIDWWvgIvgjZLtkaDwOHk_ERVsCDxqEq8eUqNB6U/edit>`__.)
4. In the #newsletter channel on Slack, @mention their writers and ask them to pick a story for the month.

   Link to the new Google doc, and set a deadline to have drafts back, 2-3 days before shipping.

You should also mention the contributor for the BIPOC "What we're reading", so they know about the deadline.

Picking the stories
-------------------

Together, the five stories should be a nice balance, including fresh or timely topics. That means:

* a mix of "technical" and non-technical stories - it's nice to aim to include an API docs or docs-as-code piece each time
* one "list of resources" story is fine, but we don't want too many or we just end up with a bunch of listicles
* a mix of specific stories (like a point of grammar, or text wrapping) and big idea/theoretical stories can balance each other out nicely
* not too many stories on processes/how to work, or hiring/applying for jobs
* no overlap, and ideally no overlap with the previous issue or two as well

Assemble & review the newsletter (2-3 days before shipping)
************************************************************

Once all the story drafts have come in, it's time to assemble, based on the `outline template <https://github.com/writethedocs/www/blob/main/docs/organizer-guide/newsletter/template.rst>`__:

* The top section is an Editor's letter. It's a quick greeting and introduction, then touches on any big things happening in the community during the month, then segues into the stories. Usually 100-200 words, depending on how much news there is. Ping the `staff` channel on Slack to check if there's anything worth mentioning.
* Next come the stories. They should be edited for length and clarity and tone, as well as to make sure they've followed the :doc:`editorial-guidelines`.
* After this is the "What we're reading" section, with three links chosen by folks in the #bipoc channel.
* If there are sponsors this month, the sponsorship article comes after the main stories.
* Featured jobs section.
* Finally, the upcoming events section lists meetups scheduled for the next month. Get a list of current meetup events from https://www.writethedocs.org/meetups/.

  Include any meetups that happen in the first week or so of the following month, since the newsletter doesn't usually go out right on the first.

When the content for the newsletter is all in place, upload the file to a new branch on GitHub in ``www/docs/blog``. Create a pull request and share in the #newsletter channel for review.

Allow 1-2 days for folks to review and leave comments. (Not *everyone* has to review it, but 2-3 sets of extra eyeballs is ideal.)

Resolve all comments, and then when you're ready to send it... 

Ship the newsletter (0 days before shipping)
********************************************

The newsletter is sent automatically by Mailchimp when there's a new post tagged ``newsletter`` in the blogs category. Check Mailchimp for exactly when it will send, but at the moment it's 9pm CEST on a weekday. Make sure you set the date in the "post" to the same day as you merge the PR, otherwise it might not get picked up.

Once you've finalized the newsletter in GitHub, merge your Pull Request (which will take it live on the WTD site). You can then go to MailChimp to **Preview and Test**: check the links, and send a test email to make sure everything renders correctly.

Once you've merged and tested it - you're done! The newsletter will go out automatically at the scheduled time.

Tweet about it (0 days before shipping)
***************************************

Once that's all done - write a tweet for the WTD account to send out to announce the newsletter.
