{% if not flaghasschedule %}
**WARNING**: This schedule has not been finalized and is subject to change. The schedule will be finalized around 1 month prior to the event.
{% endif %}

Write the Docs is more than a conference.
Each year we organize a wide range of events so that people can come together, collaborate, and learn from each other in different ways.

All times are in `{{ tz }} <https://time.is/{{ tz }}>`_.

.. contents::
    :local:
    :depth: 1
    :backlinks: none


.. raw:: html

   <hr>


{{date.day_one.dotw}}, {{date.day_one.date}}
-----------------------------------------

{{ date.day_one.summary }}

{% if flaghasfood %}

*Breakfast and lunch will be provided, as well as snacks and drinks all day.*

{% endif %}

Conference Talks
~~~~~~~~~~~~~~~~

* **Where**: {{about.venue}}
{% if not flaghasschedule %}
* **When**: **{{ date.day_one.talk_time }} {{ tz }}**
{% endif %}
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/speakers`

Talks are around 30 minutes. Most speakers will have a live, moderated Q&A session after each set of 2 talks.

.. separator to fix list formatting

{% if flaghasschedule %}

{% with day_schedule=schedule.talks_day1 %}
{% include "include/schedule2021.rst" %}
{% endwith %}

{% else %}
    A detailed schedule will be announced soon.
{% endif %}


Social Event
~~~~~~~~~~~~

The official Write the Docs social!
Further details will be announced later,
but expect some music and games,
and bring your favorite beverage to your computer :)

* **Where**: {{ about.social_venue }}
{% if not flaghasschedule %}
* **When**: **{{ date.day_one.social_time }} {{ tz }}**
{% endif %}


.. raw:: html

   <hr>


{{date.day_two.dotw}}, {{date.day_two.date}}
-----------------------------------------

{{ date.day_two.summary }}

{% if flaghasfood %}

*Breakfast and lunch will be provided, as well as snacks and drinks all day.*

{% endif %}

Conference Talks
~~~~~~~~~~~~~~~~

* **Where**: {{about.venue}}
{% if not flaghasschedule %}
* **When**: **{{ date.day_two.talk_time }} {{ tz }}**
{% endif %}
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/speakers`

Talks are around 30 minutes. Most speakers will have a live, moderated Q&A session after each set of 2 talks.

.. separator to fix list formatting

{% if flaghasschedule %}

{% with day_schedule=schedule.talks_day2 %}
{% include "include/schedule2021.rst" %}
{% endwith %}

{% else %}
  A detailed schedule will be announced soon.
{% endif %}

{% if flaghasjobfair %}

Job Fair
~~~~~~~~

We'll be holding a job fair on Tuesday morning!

* **Where**: {{about.venue}}, {{about.job_fair_room }}
{% if not flaghasschedule %}
* **When**: **{{ date.day_two.job_fair_time }} {{ tz }}**
{% endif %}
* **Details**: :doc:`/conf/{{shortcode}}/{{year}}/job-fair`

{% endif %}

