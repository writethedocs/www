Write the Docs Newsletter
#########################

At the beginning of every month, we put out an email newsletter to the community. It's built around a handful of stories that we capture and write-up from the Slack team, and also includes an overview of what the org team is working on and a calendar listing of upcoming community events.

This doc explains how to put the newsletter out each month.

Tag stories in Slack (throughout the month)
********************************************

The newsletter team keeps an eye on the WTD Slack and flags conversations they think might be a good fit by tagging them with the ``:suggest-for-newsletter:`` emoji. The 'Reacji Channeler' plug-in automatically sends the tagged post to the #newsletter-slushpile channel.

The editor has the slushpile channel set to send notifications. Every week or two, they copy and paste those conversations into txt files locally, so nothing gets swallowed up by the Slack limit.

We look for a variety of conversations topics, and usually end up capturing ~10 or so, from which we end up picking 4.

Some of the things we look for are:

* conversations that yield a lot of practical advice about a topic
* conversations that clearly strike a chord with the audience
* conversations that highlight two sides of a docs problem/topic

Assign stories (7-10 days before shipping)
*******************************************

A week before the planned ship date, the editor:

1. Goes through the conversations they've captured
2. Flags five conversations they think would make a good edition (looking for a good balance and some fresh or timely topics).
3. Adds a copy of all of the conversation to the shared 'Slushpile' dropbox folder.
4. In the #newsletter channel on Slack, @mention their writers and ask them to pick a story for the month.

   Link to the slushpile folder, and set a deadline to have drafts back, 2-3 days before shipping.

Picking the stories
-------------------

Together, the five stories should be a nice balance. That means:

* a mix of "technical" and non-technical stories (I try to aim for at least one API docs/docs-as-code piece, but not too many)
* one "list of resources" story is fine, but we don't want too many
* a mix of specific stories (like a point of grammar, or text wrapping) and big idea/theoretical stories can balance each other out nicely
* not too many stories on processes/how to work
* no overlap, and ideally no overlap with the previous issue or two as well

Assemble & review the newsletter (2-3 days before shipping)
************************************************************

Once all the story drafts have come in, it's time to assemble, based on the outline template in Dropbox:

* The top section is an Editor's letter. It's a quick greeting and introduction, then touches on any big things happening in the community during the month, then segues into the stories. Usually 100-200 words, depending on how much news there is.
* Next come the stories. They should be edited for length and clarity and tone, as well as to make sure they've followed the :doc:`editorial-guidelines`.
* If there are sponsors this month, the sponsorship article comes after the main stories.
* Featured jobs section.
* Finally, the upcoming events section lists meetups scheduled for the next month. Get a list of current meetup events from https://www.writethedocs.org/meetups/.

  Include any meetups that happen in the first week or so of the following month, since the newsletter doesn't usually go out right on the first.

When the content for the newsletter is all in place, upload the file to a new branch on GitHub in ``www/docs/blog``. Create a pull request and share in the #newsletter channel for review.

Allow 1-2 days for folks to review and leave comments. (Not *everyone* has to review it, but 2-3 sets of extra eyeballs is ideal.)

Resolve all comments, and then when you're ready to send it... 

Ship the newsletter (no days before shipping)
*********************************************

The newsletter is sent automatically by Mailchimp when there's a new post tagged ``newsletter`` in the blogs category. Check Mailchimp for exactly when it will send, but at the moment it's 9pm CEST on a weekday (after a new article has been published).

So, once you've finalized the newsletter in GitHub, merge your Pull Request (which will take it live on the WTD site). You can then go to MailChimp to **Preview and Test**: check the links, and send a test email to make sure everything renders correctly.

Once you've merged and tested it - you're done! The newsletter will go out automatically at the scheduled time.

Tweet about it (no days before shipping)
****************************************

Once that's all done - write a tweet for the WTD account to send out to announce the newsletter.
