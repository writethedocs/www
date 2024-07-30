Write the Docs is more than a conference.
Each year we organize a wide range of events so that people can come together, collaborate, and learn from each other in different ways.

All times are in `{{ tz }} <https://time.is/{{ tz }}>`_.

{% if not flaghasschedule %}
**WARNING**: This schedule has not been finalized and is subject to change. The schedule will be finalized around 1 month prior to the event.
{% endif %}


.. contents::
    :local:
    :depth: 1
    :backlinks: none


{% if flaghashike or flaghasboat %}

{{date.day_one.dotw}}, {{date.day_one.date}}
--------------------------------------------------

.. raw:: html

   {{ date.day_one.summary }}

{% if flaghasschedule %}

{% with day_schedule=schedule.outing %}
{% include "include/schedule2021.rst" %}
{% endwith %}

{% endif %}

Hike
~~~~

If you get into town early, join us on the hike and take the chance to explore Portland in all of its glory.

* **Where**: Lower Macleay Park or Macleay Park Entrance.
{% if not flaghasschedule %}
* **When**: **{{ hike.date }} {{ tz }}**
{% endif %}
* **Details**: :doc:`Annual hike to Pittock Mansion </conf/{{shortcode}}/{{year}}/outing>`

{% endif %}

{% if flaghasboat %}

Boat Ride
~~~~~~~~~

The only event scheduled on Saturday is the :doc:`Prague Boat Ride </conf/{{shortcode}}/{{year}}/outing>`.
If you get into town early, join us and experience Prague from the water.

Further details will be announced later.

{% endif %}

.. raw:: html

   <hr>

{{date.day_two.dotw}}, {{date.day_two.date}}
-----------------------------------------

.. raw:: html

   {{ date.day_two.summary }}

{% if flaghasfood %}
*Snacks and drinks will be provided throughout the day.*
{% endif %}

{% if flaghasschedule %}

{% with day_schedule=schedule.writing_day %}
{% include "include/schedule2021.rst" %}
{% endwith %}

{% else %}
  A detailed schedule will be announced soon.
{% endif %}

Writing Day
~~~~~~~~~~~

Get together with other documentarians and work on an open source project and learn some new skills.

* **Where**: {{about.venue}}, {{about.unconfroom}}
{% if not flaghasschedule %}
* **When**: **{{ date.day_two.writing_day_time }} {{ tz }}**
{% endif %}
* **Details**: :doc:`Writing Day documentation sprints </conf/{{shortcode}}/{{year}}/writing-day>`

Welcome Wagon Introduction
~~~~~~~~~~~~~~~~~~~~~~~~~~

Is this your first time at Write the Docs?
Join us for an informal Introduction to Write the Docs, to the Welcome Wagon, and to other first-time conference attendees.
We'll pass on some information about the conference specifically for first-timers and give everyone a chance to meet someone new.

* **Where**: {{about.venue}}, {{about.unconfroom}}
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/welcome-wagon`

{% if flaghasfood %}

Reception
~~~~~~~~~

We encourage everyone to drop by on Sunday evening for the conference reception.
This is a great chance to meet other attendees,
and make sure you know your way around the conference venue.

* **Where**: {{about.venue}}, {{about.unconfroom}}
{% if not flaghasschedule %}
* **When**: **{{ date.day_two.reception_time }} {{ tz }}** 
{% endif %}

{% endif %}

.. raw:: html

   <hr>

{{date.day_three.dotw}}, {{date.day_three.date}}
-----------------------------------------

.. raw:: html

   {{ date.day_three.summary }}

{% if flaghasfood %}
*Snacks and drinks will be provided throughout the day.*
{% endif %}

{% if flaghasschedule %}

{% with day_schedule=schedule.talks_day1 %}
{% include "include/schedule2021.rst" %}
{% endwith %}

{% else %}
    A detailed schedule will be announced soon.
{% endif %}

Conference Talks
~~~~~~~~~~~~~~~~

Talks are around 30 minutes, with moderated 10 minute Q&A.

* **Where**: {{about.venue}}
{% if not flaghasschedule %}
* **When**: **{{ date.day_three.talk_time }} {{ tz }}**
{% endif %}
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/speakers`

Unconference
~~~~~~~~~~~~

The unconference sessions run in parallel to the main conference talks,
with each session happening during a corresponding talk on the main stage.

* **Where**: {{about.venue}}, {{about.unconfroom}}
{% if not flaghasschedule %}
* **When**: **{{ date.day_three.unconference_time }} {{ tz }}**
{% endif %}
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/unconference`

{% if about.social_venue %}

Social Event
~~~~~~~~~~~~

The official Write the Docs social!
Expect a relaxed atmosphere where you can chat and network with your fellow documentarians. 

Snacks and drinks (non-alcoholic & alcoholic) will be provided.

* **Where**: {{ about.social_venue }}
{% if not flaghasschedule %}
* **When**: **{{ date.day_three.social_time }} {{ tz }}** 
{% endif %}

.. raw:: html

   <hr>

{% endif %}

{{date.day_four.dotw}}, {{date.day_four.date}}
-----------------------------------------

.. raw:: html

   {{ date.day_four.summary }}

{% if flaghasfood %}
*Snacks and drinks will be provided throughout the day.*
{% endif %}

{% if flaghasschedule %}

{% with day_schedule=schedule.talks_day2 %}
{% include "include/schedule2021.rst" %}
{% endwith %}

{% else %}
  A detailed schedule will be announced soon.
{% endif %}

Conference Talks
~~~~~~~~~~~~~~~~

Talks are around 30 minutes, with moderated 10 minute Q&A.

* **Where**: {{about.venue}}
{% if not flaghasschedule %}
* **When**: **{{ date.day_four.talk_time }} {{ tz }}**
{% endif %}
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/speakers`

{% if flaghasjobfair %}

Sponsor Expo
~~~~~~~~~~~~

The Sponsor Expo highlights companies that are hiring or offering products for documentarians.

* **Where**: {{about.venue}}, {{about.job_fair_room }}
{% if not flaghasschedule %}
* **When**: **{{ date.day_four.job_fair_time }} {{ tz }}**
{% endif %}
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/job-fair`

{% endif %}

Unconference
~~~~~~~~~~~~

The unconference sessions run in parallel to the main conference talks,
with each session happening during a corresponding talk on the main stage.

* **Where**: {{about.venue}}, {{about.unconfroom}}
{% if not flaghasschedule %}
* **When**: **{{ date.day_four.unconference_time }} {{ tz }}**
{% endif %}
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/unconference`
