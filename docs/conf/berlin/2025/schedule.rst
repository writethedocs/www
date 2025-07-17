:template: {{year}}/generic.html
:og:image: _static/conf/images/headers/{{shortcode}}-{{year}}-opengraph.jpg

Schedule
========

Write the Docs is more than a conference.
Each year we organize a wide range of events so that people can come together, collaborate, and learn from each other in different ways.

{% if not flaghasschedule %}

**Full schedule will be released closer to the conference.** See the `schedule overview </conf/{{shortcode}}/{{year}}/#schedule-overview>`_ for high level details.

{% else %}

All times are in `{{ tz }} <https://time.is/{{ tz }}>`_.


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

{% endif %}

.. raw:: html

   <hr>

{{date.day_two.dotw}}, {{date.day_two.date}}
-----------------------------------------

.. raw:: html

   {{ date.day_two.summary }}

{% if flaghasfood %}

The unconference is held in {{about.venue}}, {{about.unconfroom}}.

*Snacks and drinks will be provided throughout the day.*
{% endif %}

{% if flaghasschedule %}

{% with day_schedule=schedule.writing_day %}
{% include "include/schedule2021.rst" %}
{% endwith %}

{% else %}
  A detailed schedule will be announced soon.
{% endif %}

Welcome Wagon Introduction
~~~~~~~~~~~~~~~~~~~~~~~~~~

Is this your first time at Write the Docs?
Join us for an informal Introduction to Write the Docs, to the Welcome Wagon, and to other first-time conference attendees.
We'll pass on some information about the conference specifically for first-timers and give everyone a chance to meet someone new.

* **Where**: {{about.unconfroom}}
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/attendee-guide`

.. raw:: html

   <hr>

{{date.day_three.dotw}}, {{date.day_three.date}}
-----------------------------------------

.. raw:: html

   <p>
   {{ date.day_three.summary }}
   </p>

- Conference talks are held in {{about.venue}}
- Unconference is held in {{about.venue}}, {{about.unconfroom}}

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

.. raw:: html

   <hr>

{{date.day_four.dotw}}, {{date.day_four.date}}
-----------------------------------------

.. raw:: html

   <p>
   {{ date.day_four.summary }}
   </p>

- Conference talks are held in {{about.venue}}
- Unconference is held in {{about.venue}}, {{about.unconfroom}}

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

{% endif %}
