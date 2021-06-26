:template: {{year}}/generic.html

Schedule
========

Write the Docs is more than a conference.
Each year we organize a wide range of events so that people can come together, collaborate, and learn from each other in different ways.

.. contents::
    :local:
    :depth: 1
    :backlinks: none

{{date.day_one.dotw}}, {{date.day_one.date}}
--------------------------------------------------

{% if flaghashike %}

Hike
~~~~

The only event scheduled on Saturday is the :doc:`annual hike to Pittock Mansion </conf/{{shortcode}}/{{year}}/outing>`.
If you get into town early, join us on the hike and take the chance to explore Portland in all of its glory.

* **Where**: Lower Macleay Park or Macleay Park Entrance.
* **When**: 13:45
* **Details**: :doc:`Annual hike to Pittock Mansion </conf/{{shortcode}}/{{year}}/outing>`

{% endif %}

{% if flaghasboat %}

Boat Ride
~~~~~~~~~

The only event scheduled on Saturday is the :doc:`Prague Boat Ride </conf/{{shortcode}}/{{year}}/outing>`.
If you get into town early, join us and experience Prague from the water.

* **Where**: `Dvořákovo nábřeží 6, Old Town, pier no. 1 <https://goo.gl/maps/N8pd3AKtayFEpiD7A>`_
* **When**: 13:45 boarding, boat leaves **promptly** at 14:00, two-hour cruise will end at 16:00
* **Details**: :doc:`Prague Boat Ride </conf/{{shortcode}}/{{year}}/outing>`

{% endif %}


{{date.day_two.dotw}}, {{date.day_two.date}}
----------------------------------------

The Writing Day and Welcome Reception will be held at the **{{about.venue}}**.

*Breakfast and lunch will be provided, as well as snacks and drinks all day.*

.. contents::
    :local:
    :backlinks: none

Writing Day
~~~~~~~~~~~

* **Where**: {{about.venue}}, {{about.mainroom}}
* **When**: **9:00-17:00**
* **Details**: :doc:`Writing Day documentation sprints </conf/{{shortcode}}/{{year}}/writing-day>`

.. separator to fix list formatting

{% if flaghasschedule %}

.. datatemplate::
   :source: /_data/{{shortcode}}-{{year}}-writing-day.yaml
   :template: include/schedule2019.rst

{% else %}
  A detailed schedule will be announced soon.
{% endif %}

Reception
~~~~~~~~~

We encourage everyone to drop by on Sunday evening for the conference reception.
You'll have a chance to get acquainted with each other over some drinks and snacks.
We'll also help groups organize dinner plans, so you can continue your conversations over more substantial food as well.

* **Where**: {{about.venue}}, {{about.mainroom}}
* **When**: **17:00-20:00**

Welcome Wagon: Write the Docs Introduction
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Join us for an informal introduction to Write the Docs, to the `Welcome Wagon </conf/{{shortcode}}/{{year}}/welcome-wagon>`__, and to other first-time conference attendees. We'll pass on some information about the conference specifically for first-timers and give everyone a chance to meet someone new before we join the opening reception.

* **Where**: {{about.venue}}, in the downstairs foyer (near the cloakroom)
* **When**: **17:00**

Welcome Wagon: Venue Tour
~~~~~~~~~~~~~~~~~~~~~~~~~

Come on a short tour of the venue with a veteran Write the Docs attendee so you’ll know where everything is and everything you can take part in.

* **Where**: {{about.venue}}, starting near the registration desk
* **When**: **17:30**


Monday, September 16
--------------------

.. contents::
   :local:
   :backlinks: none

This is the main event! Hear from lots of interesting folks about all things documentation.
We will have talks all day on the main stage, and a unconference session running in parallel in the afternoon.

*Breakfast and lunch will be provided, as well as snacks and drinks all day.*

Welcome Wagon: Venue Tour
~~~~~~~~~~~~~~~~~~~~~~~~~

If you missed the tour on Sunday evening, we'll be re-running it on Monday.

* **Where**: {{about.venue}}, starting near the registration desk
* **When**: **9:15**

Conference Talks
~~~~~~~~~~~~~~~~

* **Where**: {{about.venue}}, {{about.mainroom}}
* **When**: **10:00-18:00**
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/speakers`

.. separator to fix list formatting


{% if flaghasschedule %}

.. datatemplate::
   :source: /_data/{{shortcode}}-{{year}}-day-1.yaml
   :template: include/schedule2019.rst

{% else %}
  A detailed schedule will be announced soon.
{% endif %}

Unconference
~~~~~~~~~~~~

The unconference sessions run in parallel to the main conference talks.

* **Where**: {{about.venue}}, {{about.unconfroom}}
* **When**: **10:40-18:00**
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/unconference`

Monday Night Social
~~~~~~~~~~~~~~~~~~~

The official Write the Docs social!

This event is for **conference attendees only**. Please bring your wristband or badge to be let into the venue.
Light snacks and drinks are included while our tab lasts. Full-service dinner will not be provided.

* **Where**: `eRKo Gastro Pub (Restaurant by Retro), Francouzská 4, Prague 2 <https://goo.gl/maps/qJUvEuShp8kUC7ac8>`_ (Namesti Miru tram/metro stop)
* **When**: **20:00-23:00**

.. TODO add this variable?

Tuesday, September 17
---------------------

.. contents::
   :local:
   :backlinks: none

And the conference goes on!

*Breakfast and lunch will be provided, as well as snacks and drinks all day.*

Conference Talks
~~~~~~~~~~~~~~~~

* **Where**: {{about.venue}}, {{about.mainroom}}
* **When**: **10:00-16:30**
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/speakers`

.. separator to fix list formatting

{% if flaghasschedule %}

.. datatemplate::
   :source: /_data/{{shortcode}}-{{year}}-day-2.yaml
   :template: include/schedule2019.rst

{% else %}
  A detailed schedule will be announced soon.
{% endif %}

.. _{{shortcode}}-{{year}}-job-fair:

Job Fair
~~~~~~~~

We'll be holding a job fair on Tuesday morning!

* **Where**: {{about.venue}}, {{about.unconfroom}}
* **When**: **10:00-12:10**
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/job-fair`

Unconference
~~~~~~~~~~~~

The unconference sessions run in parallel to the main conference talks.

* **Where**: {{about.venue}}, {{about.unconfroom}}
* **When**: **12:10-15:30**
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/unconference`
