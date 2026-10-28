Write the Docs Picks process
############################

Once a quarter, we put out :doc:`Write the Docs Picks </picks/>` — a spotlight on written content from across the community. Unlike the :doc:`monthly newsletter </newsletter>`, which rounds up Slack conversations, picks are hand-picked articles that community members have nominated themselves or on behalf of others, via our :doc:`submission process </picks/>`.

This doc explains how to run a Picks edition from open call to publication.

.. TODO: add back in Q2 2027 when the picks tag exists
   `Handy link to the archives </blog/archive/tag/newsletter/>`__.

Collect submissions (throughout the quarter)
********************************************

Submissions come in via the Picks form, landing in a shared spreadsheet. Keep an eye on it throughout the quarter rather than leaving it all to the final week. Use the same spreadsheet and just filter the view to the last three months.


Review and rate submissions (1-2 weeks before shipping)
*******************************************************

Each submission is read and rated independently by the editor and a second reviewer, against the :doc:`editorial guidelines <editorial-guidelines>`.

Score each submission on a 1 to 5 grading scale:

1. I will argue strongly against including this.
2. I'm not a fan, but it wouldn't be the end of the world if we included this.
3. (DO NOT USE. Three means you don't have an opinion. We don't believe you. No threes.)
4. This is decent. I'd be cool with including it.
5. I will fight to make sure this is included.

Once both ratings are in, the editor and reviewer discuss the top-rated submissions and agree on a final selection.

Picking the stories
-------------------

Together, the selections for an edition should be a nice balance. That means:

* A mix of topics and formats, where possible. We don't want every selection reading the same way.
* Not all from the same handful of prolific community voices (see the frequency cap in the editorial guidelines).
* A genuine bar cleared on quality and relevance. It's fine for an edition to run with a few strong picks rather than padding it out with weaker ones.
* No author or topic overlap with recent editions.

Write up the selections (1 week before shipping)
************************************************

For each selected submission, write a brief editorial note on why it made the cut: what's good about it, what it's useful for, why it's worth a reader's time. This is different from the monthly newsletter's neutral, just-the-facts tone. The editorial voice here is part of the value, since it's evidence someone actually read and judged the submission rather than just listing it.

Assemble & review (2-3 days before shipping)
********************************************

Draft the edition. Include the selected submissions along with their editorinal note, a brief intro and a call for submissions to the next edition.

Use the outline template::

   :og:image: https://www.writethedocs.org/_static/logo-opengraph.png

   .. post:: [DATE]
      :tags: picks

   ##################################
   Write the Docs Picks – SEASON YEAR
   ##################################

   [INTRO] Welcome to the latest edition of the Write the Docs Picks — a quarterly, editor-picked selection of writing from across the community. Everything here was submitted by community members and read by our editorial team before making the cut.

   ------------------
   [TITLE OF PIECE 1]
   ------------------

   **[Creator name]** [plain factual description of what they made]. [Editorial note — what it is, why it made the cut.]

   `Read it here <[URL]>`__

   ------------------
   [TITLE OF PIECE 2]
   ------------------

   **[Creator name]** [plain factual description of what they made]. [Editorial note — what it is, why it made the cut.]

   `Read it here <[URL]>`__

   ------------------
   [TITLE OF PIECE 3]
   ------------------

   **[Creator name]** [plain factual description of what they made]. [Editorial note — what it is, why it made the cut.]

   `Read it here <[URL]>`__

   ------------------
   Submit to the next edition
   ------------------

   [OUTRO] If you've written something about the practice of documentation in the last three months — or want to nominate someone else's work — submissions for the next edition are :doc:`open now </picks>`.
   We publish picks quarterly. Subscribe at :doc:`/picks` to get the next one in your inbox.
   — The Write the Docs Community Picks team


When the content is all in place, upload the file to a new branch on GitHub in ``www/docs/blog``. Create a pull request and share in the #team-picks channel for review.

Allow 1-2 days for folks to review and leave comments. (Not *everyone* has to review it, but 2-3 sets of extra eyeballs is ideal.)

Resolve all comments, and then when you're ready to send it...

Ship the picks (0 days before shipping)
******************************************

It's the same mechanism as the newsletter: merging the PR takes the post live, and Mailchimp sends it out to subscribers once the post is tagged correctly.

We don't notify submitters individually, successful or not. People find out by checking when the edition goes live.

Promote it (0 days before shipping)
***********************************

Post about the new edition on the WTD LinkedIn page, and drop a link in the #announcements Slack channel.