.. _conf-web-resources:

.. highlight:: yaml

Conference websites
===================

Each conference has a section of the website, which is part of the same
repository as the main community website. Many parts of the conference
websites are data-driven, like the generation of the schedule.

.. note::
    This documentation applies only for conferences from 2020 onwards.

File locations
--------------

The important locations of files are:

* ``_data/<shortcode>-<year>-config.yaml`` contains the general config file
  for rendering a specific conference. This includes settings like the
  conference dates, sponsors, and ticket prices.
* ``_data/<shortcode>-<year>-sessions.yaml`` contains the conference sessions,
  the main talks on the agenda. For each session, it includes things like the
  title and abstract, and name and other info for the speaker(s).
* ``_data/<shortcode>-<year>-schedule.yaml`` contains the conference schedule.
  This includes the talks, but also peripheral activities like lightning talks, meals, the outing, and social event.
* ``conf/<shortcode>/<year>/`` contains the RST files used for rendering the
  conference website.
* ``include/conf/`` contains text snippets that are generally the same
  between conferences, or at least between conferences in the same location.
  Examples include the description of lightning talks, or the Portland hike.
* ``_templates/<year>/`` and ``_templates/include/`` contain HTML or RST
  templates used to render the conference pages. This includes the
  website design, navigation and snippets used in schedule rendering.
  From 2026 on, the design and the header menu live in
  ``_templates/conference/``. To start a new year, copy the previous year's
  ``_templates/<year>/`` folder.
* ``_data/community.yaml`` lists the upcoming conferences shown on the front
  page and the conferences page. Add a conference there once its site is up.

The YAML files are validated by the `validate-yaml.sh` script, using
the schemas in ``_data/schema-*``.


Typical conference workflow
---------------------------

The conference site changes as the conference goes through its stages. Most
of those changes are a flag in the general config file: the flags switch
pages on in the header menu, pick the buttons on the front page, and decide
which key dates the front page still shows. The lists below say what to do at
each stage, and what the site does in response.

* Create the initial conference website by copying the files from
  ``conf/<shortcode>/<year>/`` from the previous conference
  (chronologically, not the previous conference in the same location).
  You may need to update some reference to specific locations/years,
  and keep an eye on any FIXMEs or TODOs.
* In the initial conference website, set ``flaglanding``,
  to publish a simple landing page with the conference dates.
* Once decided, enter further details of the conference in the general config
  file, like sponsorship and ticket prices, and the dates under ``cfp`` and
  ``date``. Switch off ``flaglanding``.
  Review all conferences pages and activities first, to make sure they are
  correct, or TBA if not yet known. The front page now shows the key dates
  that are still to come: tickets on sale, call for proposals closing, talks
  and schedule announced, and the conference itself. Each one drops off the
  timeline once it has passed, so the dates need no further changes.
* When the sponsorship prospectus is ready, switch on ``flaghassponsors``.
  The front page offers "Sponsor the Conference".
* When the CFP opens, add the CFP details in the general conference config
  file, under ``cfp``, and switch on ``flagcfp``. This adds the Call for
  Proposals page to the menu, "Submit a Talk" to the front page buttons, and
  the closing date to the key dates. Once the CFP has closed, switch it off.
* As soon as tickets go on sale, switch on ``flagticketsonsale``. "Buy a
  Ticket" becomes the first button, and the tickets line leaves the key dates.
* When speakers have been selected, add their sessions to the
  ``_data/<shortcode>-<year>-sessions.yaml`` file.
  Then, switch on ``flagspeakersannounced`` for the Speakers page and button.
* When the schedule is ready, add it to the ``_data/<shortcode>-<year>-schedule.yaml``
  file and switch on ``flaghasschedule`` for the Schedule page and button.
* When the attendee guide is written, switch on ``flaghasattendeeguide``.
* At some point the conference sells out. Switch off ``flagticketsonsale``, and
  switch on ``flagsoldout``. The ticket button goes away.
* The day after ``date.ends``, the site switches to post-conference mode on
  its own: the key dates disappear and the buttons change to the recap, the
  videos and the photos. Set ``flagpostconf`` in the config only to override
  this, for example to keep the site in conference mode for a few days.
* When the photos are up, add the album URL to ``photos.album``. When the
  videos have been published on the Write the Docs YouTube channel, add the
  playlist URL to ``videos.playlist`` and switch on ``flagvideos``.

The site is rebuilt when a change is pushed, so a date-based change like the
switch to post-conference mode shows up at the next build.

Front page buttons
~~~~~~~~~~~~~~~~~~

The two buttons in the front page hero, and the two in the band above the
footer, are picked from the flags, so they follow the workflow above without
further edits. The template (``_templates/conference/buttons.html``) keeps two
ranked lists of candidate buttons, each shown only while its flag is on, and
shows the top two that apply.

Before and during the conference, in order:

1. Buy a Ticket (``flagticketsonsale`` on and ``flagsoldout`` off)
2. Submit a Talk (``flagcfp``)
3. See the Schedule (``flaghasschedule``)
4. See the Speakers (``flagspeakersannounced``)
5. Attendee Guide (``flaghasattendeeguide``)
6. Sponsor the Conference (``flaghassponsors``)
7. Date and ticket information (the welcome post; always available)

After the conference (``flagpostconf``), in order:

1. Watch the videos (``videos.playlist`` set)
2. Conference recap (the thanks post; always available)
3. Browse the photos (``photos.album`` set)

So a site with the CFP open and tickets not yet on sale shows "Submit a
Talk" and "Sponsor the Conference"; once tickets go on sale it shows "Buy a
Ticket" and "Submit a Talk"; and once the speakers are announced and the CFP
is closed, "Buy a Ticket" and "See the Speakers".

To choose the buttons by hand instead, add a ``buttons`` block to the config
(see below). Conferences up to 2026 do this.


General conference config file
------------------------------

The general conference config file contains most of the per-conference
settings, and is stored in ``_data/<shortcode>-<year>-config.yaml``
If you're setting up a new conference, the easiest may be to take a YAML
config file from the previous conference, and adjust it.

The items in the general conference config file are:

* ``name``: the dynamic part of the name of the conference, e.g. ``Portland``
  for Write the Docs Portland.
* ``shortcode``: the shortcode as used in file paths, config names, and other
  references to the conference, together with the year. Currently used are
  ``portland``, ``prague``, and ``australia``.
* ``year``: the conference year, e.g. ``2020``.
* ``city``: the city for the conference, e.g. ``Portland`` or ``Prague``.
* ``local_area``: the state or country for the conference, e.g. ``Oregon``
  or ``Czech Republic``.
* ``area``: the wider area for the conference. Currently used are
  ``North America``, ``Europe``, and ``Australia``.
* ``area_adj``: the adjective form of the area, e.g. ``Australian``.
* ``tz``: the timezone the conference is located in, e.g. ``PST`` or ``CEST``
  This is displayed in the website, so the format is free.
* ``email``: general contact email for the conference.
* ``color``: the accent color for conference branding, e.g. ``blue`` for 2020.
* ``photos.default``: the default header image.
* ``photos.album``: the URL of the Flickr album with the conference photos,
  once they are up. Used for the "Browse the photos" button.
* ``buttons.top`` and ``buttons.bottom``: optional from 2027 on. Without
  them, the buttons on the top and bottom of the conference pages are picked
  from the flags, as described under `Front page buttons`_. With them, the
  lists are used as they are. Each button has two keys: ``text`` for
  the button text and ``link`` or ``link_absolute`` for a site-relative or
  an absolute link for the button. Top and bottom are often identical.
  Example::

    buttons:
      top:
         - text: Sponsor the conference
           link: /sponsors/prospectus
         - text: Submit a Talk
           link: /cfp
      bottom:
         - text: Sponsor the conference
           link: /sponsors/prospectus
         - text: Submit a Talk
           link: /cfp

* ``videos.playlist``: the URL of the YouTube playlist with the conference
  videos, once they are up. Used for the "Watch the videos" button.
* ``tickets``: the conference ticket prices. The keys, i.e. the names of the
  various sponsorship packages, are fixed and cannot be changed per conference.
  Example::

    tickets:
      corporate:
        price: $500
      independent:
        price: $275
      student:
        price: $100

* ``sponsorship``: the conference sponsorship prices. The keys are fixed and
  referred to in other places. Example::

    sponsorship:
      first_draft:
        price: $900
      second_draft:
        price: $2,500
      publisher:
        price: $5,000
      patron:
        price: $9,500
      keystone:
        price: $17,000

* ``sponsors``: confirmed conference sponsors, using the same keys as the
  pricing. Each sponsor has a name and a link to their website. Their logo
  must be stored in ``_static/img/sponsors/``. Example::

    sponsors:
      keystone:
      patron:
        # logo must be in _static/img/sponsors/patron-sponsor.jpg/png
        - name: patron-sponsor
          link: http://www.example.com
      publisher:
      second:
      first:
      media:
        - name: media-sponsor-one
          link: http://www.example.com

* ``date``: the conference dates and days. Contains:
    * ``main``: the human readable conference dates and location,
      e.g. ``"**May 3-5, 2020, in Portland, Oregon**"``.
    * ``short``: the short human readable dates, e.g. ``May 3-5, 2020``.
    * ``ends``: the last day of the conference as a date, e.g. ``2027-05-04``.
      The site switches to post-conference mode the day after.
    * ``tickets_live``: a human readable date to indicate the month when tickets go on sale,
      e.g. ``January 2020``.
    * ``month``: the month in which the conference is held, e.g. ``May``.
    * ``total_talk_days``: the number of days that have talks, e.g. ``2``.
      Used to automatically read the schedule.
    * ``day_one``, ``day_two``, etc. These are actually events, not days. Each "day" has:
        * ``event``: the name of the event, like ``Hike``, ``Writing Day`` or
          ``Main Conference``.
        * ``date``: the short human readable date, e.g. ``May 2`` or
          ``May 4-5``.
        * ``summary``: a human readable summary of the event that day.
        * ``icon``: the icon used for this event, e.g. ``hike`` or
          ``conference``.
        * ``dotw``: the day(s) of the week for this event, e.g. ``Saturday``
          or ``Monday/Tuesday``.
* ``about``: general conference background. Contains:
    * ``attendees``: the number of attendees.
    * ``summary``: a summary text for the conference.
    * ``venue``: a human readable textual description of the venue location.
    * ``photos``: a link to the conference photos (typically on Flickr).
    * ``mainroom``: the name of the main room.
    * ``unconfroom``: the name of the unconference room.
    * ``job_fair_room``: the location of the job fair.
    * ``projector_ratio``: the ratio for the projector, e.g. ``16:9``.
* ``cfp``: call for papers details. Contains:
    * ``url``: the URL to a google form with the CFP.
    * ``ends``: a human readable date of when the CFP ends,
      e.g. ``31 January, 2020``.
    * ``opens``: a human readable month in which the CFP opens, e.g.
      ``November 2026``. Shown in the key dates until the CFP is open.
    * ``notification``: a human readable date of when accepted speakers
      will be notified.
    * ``schedule_announced``: a human readable date or month for the schedule
      announcement, e.g. ``March 2027``.

The file also includes a few true/false flags. Some of these don't change
as the conference is being planned. These are:

* ``flaghashike``: does the conference have a hike?
* ``flaghasboat``: does the conference have a boat ride?
* ``flagwelcomewagon``: does the conference have a welcome wagon?

Others will change over time:

* ``flaglanding``: is the conference website only a landing page?
  Typically used for an early announcement of conference dates.
* ``flagticketsonsale``: are tickets on sale at this time?
* ``flagsoldout``: is the conference sold out?
* ``flagcfp``: is the CFP currently open?
* ``flagspeakersannounced``: have speakers been announced?
  This flag requires the ``_data/<shortcode>-<year>-sessions.yaml``
  file to exist, which lists the speakers/sessions.
* ``flaghasschedule``: is the schedule ready?
  This flag requires the``_data/<shortcode>-<year>-schedule.yaml``
  file to exist, which contains the schedule.
* ``flaghassponsors``: is the sponsorship prospectus ready?
* ``flaghasattendeeguide``: is the attendee guide written?
* ``flagpostconf``: has the conference ended? From 2027 on this is set from
  ``date.ends`` at build time; set it in the config only to override that.
* ``flagvideos``: are the conference videos published?


Sessions file
-------------

The sessions file contains the conference sessions, i.e. the talks, and
is stored in ``_data/<shortcode>-<year>-sessions.yaml``.

Each talk has the following attributes:

* ``title``: title of the talk
* ``abstract``: talk abstract
* ``slug``: talk slug - referenced in the schedule. Typically, the slug is
  a slugified version of the title, followed by the slugified speaker name.

* ``series``: the conference series, used for videos, e.g. ``Write the Docs PORTLAND``
* ``series_slug``: the slug of the series, used for videos
* ``year``: the year the talk was given, used for videos
* ``youtubeId``: the Youtube ID of the talk video, if published already
* ``speakers``: the speaker(s) for the talk, in a list of speakers with keys:
    * ``name``: full name of the speaker
    * ``slug``: slug of the speaker
    * ``twitter``: Twitter username
    * ``website``: URL of the speaker's website


Schedule file
-------------

The schedule file contains the conference schedule and is stored in
``_data/<shortcode>-<year>-schedule.yaml``. This is a mix of conference
talks, and other agenda items like "Switch Speakers" or "Lunch Break".

If you're writing a new conference schedule, it may be easier to start from
a copy of the schedule file of the same conference as last year, as they tend
to be quite similar.

For conferences with a writing day, you must add a ``writing_day`` key. Then,
a schedule for each main conference day, in the form of ``talks-day1``,
``talks-day2``,
and more if needed. The number of days must match ``date.total_talk_days``
from the general config file.

Each item must have either a ``title`` or a ``slug``.
A title is used for free text schedule items, like "Snack Break". A slug is
used for conference talks, where the slug must match the slug of a session
in the ``_data/<shortcode>-<year>-sessions.yaml`` file. All sessions must
be in the schedule.

Timing
~~~~~~

The first item of every day must have a specific start time. The time of
other items can be provided in several ways:

* If an item has a specific time set, that is the time when the event is
  listed in the schedule.
* If an item does not have a specific time set, its start time is calculated
  from the duration of all previous items, up to the last item that had
  an explicit start time.

You can mix these methods in the schedule. An item without a duration or time
has a duration of zero. Note that all times in the config file must be written
as strings, i.e. with quotes around them, and in 24 hour time format.
The output format is determined by the ``time_format`` setting for the
conference, which can be ``24h`` or ``12h``. The first entry of the day will
include the conference timezone

In the example below, the talk days use explicit times for every item, the
writing day uses a mix. The writing day schedule would come out to:

* 8:00: Doors open: explicit time set
* 9:00: Helpdesk open: start of previous item (8:00) plus duration
  of previous item (1 hour)
* 9:00: Writing day introduction: start of previous item (9:00) plus duration
  of previous item, which is zero
* 9:15: Sponsor booths open: start of previous item (9:00) plus duration
  of previous item (15 minutes)
* 13:00: Lunch: explicit time set
* 17:00: Wrap up: explicit time set
* 17:15: End of Writing Day: start of previous item (17:00) plus duration
  of previous item (15 minutes)

In legacy conferences, only ``time`` was supported, always as a free form string.
The schedule generator uses legacy mode when ``time_format`` is not set in the
conference config.

Quick view of schedule
~~~~~~~~~~~~~~~~~~~~~~

The ``show-conf-schedule.py`` script in ``_scripts`` takes a shortcode and year,
and will show you the generated schedule. This can come in handy when adjusting
the schedule, to see all generated start times without building the
whole website.

Example
~~~~~~~

A schedule file for a very brief conference could look like::

    writing_day:
      - time: '8:00'
        duration: '1:00'
        title: Doors Open, Breakfast Served
      - title: 'Helpdesk open'
      - duration: '0:15'
        title: 'Writing day introduction'
      - title: 'Sponsor booths open'
      - time: '13:00'
        title: Lunch
      - time: '17:00'
        duration: '0:15'
        title: Wrap up
      - title: End of Writing Day

    talks-day1:
      - time: '8:00'
        title: Doors Open, Breakfast Served
      - time: '9:40'
        title: "<b>Unconference Starts (Lola's Room)</b>"
      - time: '9:40'
        slug: any-friend-of-the-docs-is-a-friend-of-mine-cultivating-a-community-of-documentation-advocates-heather-stenson
      - time: '10:40'
        title: '<b>Group Photo</b>'
      - time: '11:00'
        title: Day 1 wraps up

    talks-day2:
      - time: '8:00'
        title: Doors Open, Breakfast Served
      - time: '9:00'
        slug: draw-the-docs-alicja-raszkowska
      - time: '9:30'
        title: Switch Speakers
      - time: '9:40'
        title: "<b>Job Fair Starts (Lola's Room)</b>"
      - time: '9:40'
        slug: documentation-for-good-riona-macnamara
      - time: '10:00'
        title: "<b>Conference Ends</b> :("
